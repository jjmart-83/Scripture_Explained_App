"""Export reviewed-format local sessions to a portable, static listening library."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

try:
    from .speech_text import normalize_spoken_names
except ImportError:
    from speech_text import normalize_spoken_names


def prepare(chapters_dir: Path, site_dir: Path) -> dict:
    chapters = []
    folders = sorted(chapters_dir.glob("Isaiah_*"), key=lambda p: int(p.name.split("_")[-1]))
    if (chapters_dir / "Week_Introduction" / "session.json").exists():
        folders.insert(0, chapters_dir / "Week_Introduction")
    if (chapters_dir / "Week_in_Review" / "session.json").exists():
        folders.append(chapters_dir / "Week_in_Review")
    for folder in folders:
        session = json.loads((folder / "session.json").read_text(encoding="utf-8"))
        metadata = json.loads((folder / "render_metadata.json").read_text(encoding="utf-8"))
        digest = hashlib.sha256((folder / "session.json").read_bytes()).hexdigest()
        if digest != metadata["session_sha256"]:
            raise ValueError(f"Stale rendering metadata: {folder}")
        if len(session["segments"]) != len(metadata["timings"]):
            raise ValueError(f"Segment count mismatch: {folder}")
        verses = {v["number"]: v["text"] for v in session["verses"]}
        segments = []
        coverage = []
        for segment, timing in zip(session["segments"], metadata["timings"]):
            role = segment["role"]
            if role not in ("scripture", "commentary") or role != timing["role"]:
                raise ValueError(f"Invalid segment role: {folder}")
            entry = {
                "role": role,
                "start": timing["start_seconds"],
                "duration": timing["duration_seconds"],
            }
            if role == "scripture":
                numbers = segment["verse_numbers"]
                if numbers != timing["verse_numbers"]:
                    raise ValueError(f"Verse timing mismatch: {folder}")
                coverage.extend(numbers)
                entry["verses"] = [{"number": n, "text": verses[n]} for n in numbers]
            else:
                if normalize_spoken_names(segment["text"]) != timing["spoken_text"]:
                    raise ValueError(f"Commentary text differs from rendered speech: {folder}")
                entry["text"] = segment["text"]
            segments.append(entry)
        if coverage != list(range(1, session["expected_verse_count"] + 1)):
            raise ValueError(f"Missing or repeated verses: {folder}")
        audio = folder / metadata["output"]
        if audio.stat().st_size != metadata["bytes"]:
            raise ValueError(f"Audio size mismatch: {audio}")
        destination = site_dir / "data" / "audio" / audio.name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(audio, destination)
        focus = session["lesson_focus"].replace("This chapter sample follows the lesson emphasis on ", "")
        chapters.append({
            "id": session.get("id") or f"isaiah-{session['chapter']}",
            "kind": session.get("kind", "chapter"),
            "number": session.get("chapter"),
            "title": session["title"] if session.get("kind") in ("introduction", "summary") else f"Isaiah {session['chapter']}",
            "focus": focus[:1].upper() + focus[1:],
            "verseCount": len(verses),
            "duration": metadata["duration_seconds"],
            "audio": f"audio/{audio.name}",
            "audioVersion": hashlib.sha256(audio.read_bytes()).hexdigest()[:12],
            "sources": [{"title": s["title"], "url": s["url"]} for s in session["sources"]],
            "segments": segments,
        })
    if not chapters:
        raise ValueError(f"No chapters found in {chapters_dir}")
    library = {
        "id": "2026-10-12-isaiah",
        "title": "The Redeemer Shall Come to Zion",
        "dates": "October 12–18, 2026",
        "reading": "Isaiah 58–66",
        "lessonUrl": "https://www.churchofjesuschrist.org/study/manual/come-follow-me-for-home-and-church-old-testament-2026/42?lang=eng",
        "chapters": chapters,
    }
    data = site_dir / "data" / "library.json"
    data.write_text(json.dumps(library, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return library


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chapters", type=Path, default=Path("output/2026-10-12/chapters"))
    parser.add_argument("--site", type=Path, default=Path("site"))
    args = parser.parse_args()
    library = prepare(args.chapters, args.site)
    print(f"Prepared {len(library['chapters'])} listening sections in {args.site.resolve()}")
