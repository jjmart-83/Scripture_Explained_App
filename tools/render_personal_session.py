"""Render a prepared personal study session with the owner's local Kokoro reader.

This is an audio-prototype utility, not the web application. It performs no
content retrieval or model download. Models and a prepared session must exist.
Only selected definitions are loaded from the reader, so Qt is not required.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.metadata
import json
import logging
import os
import re
import threading
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro
try:
    from .speech_text import normalize_spoken_names, transcript_markdown
except ImportError:
    from speech_text import normalize_spoken_names, transcript_markdown

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def reader_definitions(path: Path) -> dict:
    source = ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
    names = {"KokoroEngine", "segment_text", "_split_long_sentence", "pitch_shift"}
    selected = []
    for node in source.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in names:
            selected.append(node)
        elif isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "MAX_SEGMENT_CHARS"
            for target in node.targets
        ):
            selected.append(node)
    found = {node.name for node in selected if hasattr(node, "name")}
    if found != names:
        raise ValueError(f"Reader definitions changed; missing: {names - found}")
    namespace = {
        "np": np, "os": os, "re": re, "threading": threading,
        "log": logging.getLogger("personal_tts"), "__file__": str(path),
    }
    exec(compile(ast.Module(body=selected, type_ignores=[]), str(path), "exec"), namespace)
    return namespace


def validate_session(session: dict) -> dict[int, str]:
    if not session["segments"]:
        raise ValueError("A study section must contain at least one spoken segment")
    if session.get("kind") in ("introduction", "summary") and (
        session["expected_verse_count"] != 0 or any(s["role"] != "commentary" for s in session["segments"])
    ):
        raise ValueError("Lesson framing sections must contain commentary only")
    verses = session["verses"]
    expected = list(range(1, session["expected_verse_count"] + 1))
    if [verse["number"] for verse in verses] != expected:
        raise ValueError("Source verses are incomplete, duplicated, or out of order")
    verse_map = {verse["number"]: verse["text"] for verse in verses}
    if any(not text.strip() for text in verse_map.values()):
        raise ValueError("An empty scripture verse was supplied")
    used = []
    sources = {source["id"] for source in session["sources"]}
    for segment in session["segments"]:
        if segment["role"] not in session["voices"]:
            raise ValueError("Unknown voice role")
        if segment["role"] == "scripture":
            used.extend(segment["verse_numbers"])
        elif not segment["text"].strip() or not set(segment["source_ids"]) <= sources:
            raise ValueError("Commentary is empty or refers to an unrecorded source")
    if used != expected:
        raise ValueError("Narration must include every verse exactly once and in order")
    return verse_map


def create_engine(reader_path: Path, model_dir: Path):
    for path in (reader_path, model_dir / "kokoro-v1.0.onnx", model_dir / "voices-v1.0.bin"):
        if not path.is_file():
            raise FileNotFoundError(f"Required local asset missing: {path}")
    helpers = reader_definitions(reader_path)
    engine = helpers["KokoroEngine"]()
    engine._kokoro = Kokoro(str(model_dir / "kokoro-v1.0.onnx"),
                            str(model_dir / "voices-v1.0.bin"))
    engine.device = "CPU"
    return engine


def session_filename(session: dict) -> str:
    if session.get("kind") in ("introduction", "summary"):
        name = session["audio_filename"]
        if not re.fullmatch(r"[A-Za-z0-9_-]+\.mp3", name):
            raise ValueError("Lesson audio filename must be a simple MP3 basename")
        return name
    book = re.sub(r"[^A-Za-z0-9]+", "_", session.get("book", "Isaiah")).strip("_")
    if not book or int(session["chapter"]) < 1:
        raise ValueError("A book name and positive chapter number are required")
    return f"{book}_{int(session['chapter'])}_Explained.mp3"


def render(session_path: Path, reader_path: Path, model_dir: Path, *, engine=None,
           reuse_from: Path | None = None) -> Path:
    model = model_dir / "kokoro-v1.0.onnx"
    voices = model_dir / "voices-v1.0.bin"
    for path in (session_path, reader_path, model, voices):
        if not path.is_file():
            raise FileNotFoundError(f"Required local asset missing: {path}")
    session = json.loads(session_path.read_text(encoding="utf-8"))
    verse_map = validate_session(session)
    asset_hashes = {"reader_sha256": sha256(reader_path), "model_sha256": sha256(model),
                    "voices_sha256": sha256(voices)}
    previous_session = previous_metadata = None
    if reuse_from is not None:
        previous_path = reuse_from / "session.json"
        previous_session = json.loads(previous_path.read_text(encoding="utf-8"))
        previous_metadata = json.loads((reuse_from / "render_metadata.json").read_text(encoding="utf-8"))
        if previous_metadata["session_sha256"] != sha256(previous_path):
            raise ValueError("Reuse source session does not match its rendering metadata")
        if any(previous_metadata[key] != value for key, value in asset_hashes.items()):
            raise ValueError("Reuse source was rendered with different reader/model assets")
    helpers = reader_definitions(reader_path)
    # Load existing local assets directly; do not invoke the reader's downloader.
    engine = engine if engine is not None else create_engine(reader_path, model_dir)
    sample_rate = None
    all_audio = []
    timings = []
    cursor = 0
    first_scripture = True
    output_dir = session_path.parent
    segment_dir = output_dir / "segments"
    segment_dir.mkdir(exist_ok=True)

    for index, segment in enumerate(session["segments"], 1):
        role = segment["role"]
        params = session["voices"][role]
        text = segment.get("text", "")
        if role == "scripture":
            text = "\n\n".join(
                f"Verse {number}. {verse_map[number]}"
                for number in segment["verse_numbers"]
            )
            if first_scripture:
                text = f"{session.get('book', 'Isaiah')}, chapter {session['chapter']}.\n\n{text}"
                first_scripture = False
        else:
            text = normalize_spoken_names(text)
        reused = False
        audio = None
        if previous_metadata and index <= len(previous_metadata["timings"]):
            prior = previous_metadata["timings"][index - 1]
            if (prior["role"] == role and prior["spoken_text"] == text
                    and previous_session["voices"][role] == params):
                wav = reuse_from / "segments" / f"{index:02d}_{role}.wav"
                audio, rate = sf.read(wav, dtype="float32")
                if (audio.ndim != 1 or rate != previous_metadata["sample_rate"]
                        or abs(len(audio) - round(prior["duration_seconds"] * rate)) > 1
                        or not len(audio) or not np.isfinite(audio).all()):
                    raise ValueError(f"Invalid reusable audio segment: {wav}")
                reused = True
                print(f"{session['title']} segment {index}: reused unchanged {role}", flush=True)
        if audio is None:
            chunks = []
            pieces = helpers["segment_text"](text)
            for part_index, piece in enumerate(pieces, 1):
                print(f"{session['title']} segment {index}/{len(session['segments'])} {role}: "
                      f"chunk {part_index}/{len(pieces)}", flush=True)
                chunk, rate = engine.synthesize(
                    piece, params["voice"], params["speed"], params["lang"], params["pitch"]
                )
                if sample_rate is None:
                    sample_rate = rate
                if rate != sample_rate or not len(chunk) or not np.isfinite(chunk).all():
                    raise ValueError("Synthesis returned invalid audio or changed sample rate")
                if part_index > 1:
                    chunks.append(np.zeros(round(rate * 0.15), dtype=np.float32))
                chunks.append(chunk)
            audio = np.concatenate(chunks)
        else:
            if sample_rate is None:
                sample_rate = rate
            if rate != sample_rate:
                raise ValueError("Reusable segment sample rate differs from new synthesis")
        sf.write(segment_dir / f"{index:02d}_{role}.wav", audio, sample_rate)
        timings.append({
            "segment": index, "role": role, "voice": params["voice"],
            "start_seconds": cursor / sample_rate,
            "duration_seconds": len(audio) / sample_rate,
            "verse_numbers": segment.get("verse_numbers", []),
            "source_ids": segment.get("source_ids", ["scripture"]),
            "spoken_text": text,
            "reused_audio": reused,
        })
        all_audio.append(audio)
        cursor += len(audio)
        if index < len(session["segments"]):
            gap = np.zeros(round(sample_rate * 0.7), dtype=np.float32)
            all_audio.append(gap)
            cursor += len(gap)

    combined = np.concatenate(all_audio)
    if np.max(np.abs(combined)) >= 1:
        combined = combined * (0.98 / np.max(np.abs(combined)))
    output = output_dir / session_filename(session)
    sf.write(output, combined, sample_rate, format="MP3", bitrate_mode="CONSTANT")
    decoded, decoded_rate = sf.read(output, dtype="float32")
    if decoded_rate != sample_rate or abs(len(decoded) - len(combined)) > sample_rate:
        raise ValueError("Encoded MP3 duration/sample rate does not match rendered audio")
    if not np.isfinite(decoded).all() or np.max(np.abs(decoded)) < 0.001:
        raise ValueError("Encoded MP3 is invalid or silent")
    metadata = {
        "output": output.name, "sample_rate": sample_rate,
        "duration_seconds": len(decoded) / decoded_rate,
        "peak": float(np.max(np.abs(decoded))), "bytes": output.stat().st_size,
        "verse_coverage": list(verse_map), "timings": timings,
        "session_sha256": sha256(session_path), **asset_hashes,
        "dependencies": {name: importlib.metadata.version(name) for name in
                         ("kokoro-onnx", "onnxruntime", "numpy", "scipy", "soundfile")},
        "owner_listening_confirmation": "pending",
        "speech_normalization": "Middle-initial periods removed in commentary names before chunking",
    }
    if previous_metadata:
        metadata["reuse_source_session_sha256"] = previous_metadata["session_sha256"]
    (output_dir / "render_metadata.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )
    transcript_name = output.stem.removesuffix("_Explained") + "_Transcript.md"
    (output_dir / transcript_name).write_text(transcript_markdown(session), encoding="utf-8")
    print(f"Saved {output}\nDuration: {metadata['duration_seconds'] / 60:.2f} minutes", flush=True)
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("session", type=Path, nargs="+",
                        help="Prepared chapter sessions, rendered in order with one loaded model")
    parser.add_argument("--reader", type=Path,
                        default=ROOT.parent / "tts_reader" / "tts_reader.py")
    parser.add_argument("--models", type=Path, default=ROOT / ".tools" / "tts_models")
    parser.add_argument("--reuse-from-dir", type=Path,
                        help="Prior rendered folders by matching session folder name; reuse verified unchanged WAVs")
    args = parser.parse_args()
    shared_engine = create_engine(args.reader, args.models)
    for session_path in args.session:
        prior = args.reuse_from_dir / session_path.parent.name if args.reuse_from_dir else None
        render(session_path, args.reader, args.models, engine=shared_engine,
               reuse_from=prior if prior and prior.is_dir() else None)
