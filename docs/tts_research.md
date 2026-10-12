# Existing TTS Reader and Personal MP3 Plan

> Reviewed: 2026-10-11. Source review of the owner's existing reader, followed by
> isolated sample preparation. This is research/planning; audio quality remains
> subject to the owner's listening test.

## Existing project

Location: `C:/Users/marti/OneDrive/Documents/Code_Projects/tts_reader`.
The folder contains `tts_reader.py`, its batch launcher, and `tts_config.json`.
The reader reports version 2.0.0. Its source SHA256 at inspection was
`7D1E48E563539F63895A9FF82B14869941B57517D085C121F644D3AA7DC82FBF`.
The existing project is not being edited.

| Capability found in source | Relevance |
|----------------------------|-----------|
| Kokoro ONNX local inference | Suitable local speech candidate based on the owner's prior use. |
| Eleven exposed US/UK voice choices | Supports selecting a distinct scripture and explanation voice. |
| Voice passed to each synthesis call | A shared loaded engine can alternate voices between session segments. |
| Sentence-aware chunks around 400 characters | Reuse existing handling instead of feeding entire chapters into one call. |
| Speed, pitch, volume | Useful controls to evaluate after the initial voice-pair sample. |
| MP3 export through soundfile | Fits the owner's personal-file first step. |
| MP4/AAC export with ffmpeg | Optional later format; unnecessary for the first MP3. |
| GUI audio cache and streaming player | Reference behavior for later playback; not a browser component. |

The current config chooses Heart (`af_heart`), speed 1.0, pitch -0.3, and volume
1.0. It contains a single active voice setting, not a two-role session format.

## Reuse constraints

- The Python/Qt GUI cannot be placed directly inside an HTML/Capacitor player.
- `synthesize_text` creates a fresh engine each call. A multi-segment export
  should load the model once and reuse it while changing voice parameters.
- PySide6 imports are unconditional at module scope despite comments calling
  GUI dependencies optional. Importing the complete script or invoking its CLI
  still requires Qt. For this sample, load only its engine/chunking/pitch
  definitions, avoiding GUI startup and dependencies.
- The engine can download missing model files. The sample renderer instead
  requires existing local model paths before synthesis.
- Its source describes the model as about 90 MB, but the exact unquantized
  release asset it names is 325,532,387 bytes and the voice asset is 28,214,398
  bytes. Initial acquisition is about 337 MiB total, excluding dependencies.
- The GUI cache retains up to eight entries in memory. It does not itself
  establish persistent offline storage for a future mobile app.
- Original Markdown stripping removes numbered-list prefixes. Build narration
  from explicit verse records so formatting cleanup cannot erase verse identity.

## Options

| Route | Fit | Remaining work |
|-------|-----|----------------|
| Local Python preparation, MP3 playback | Selected for the first sample; reuse the existing synthesis logic and voices. | Review script, validate verse coverage, render and listen. |
| Local Python service for an HTML UI | Possible desktop workflow. | Local server integration and deployment; a phone would need access to that service. |
| Kokoro inside the browser/app | Potential later local generation on the listening device. | Validate assets, storage, memory, latency, and target WebView behavior. |

The upstream [Kokoro JavaScript documentation](https://github.com/hexgrad/kokoro/blob/main/kokoro.js/README.md)
describes browser inference using WASM or WebGPU, per-request voices, and
streaming. [Kokoro Web](https://github.com/xenova/kokoro-web) is a working-project
reference. These establish a browser route to investigate, not verified
performance on the owner's devices or identical audio to this Python model.

## Authorized first sample

- Complete Isaiah 58, with brief interruptions after selected passage groups.
- Beginner explanations for youth ages 12-18 and new members, defining unfamiliar
  vocabulary and images without assuming prior Church/scripture knowledge.
  Advanced levels are deferred.
- Lesson identity: October 12-18, 2026; full assignment Isaiah 58-66. Only chapter
  58 is selected for this first output.
- Sources: official lesson and chapter; review the lesson-linked Eyring fasting
  talk and Nelson Sabbath talk for selective supporting context.
- Owner-selected initial roles: male scripture narration and female commentary.
  Provisional voices: Michael (`am_michael`) reads scripture; Heart (`af_heart`)
  explains. The specific voices await listening feedback. The owner may want
  selectable/swappable roles later; no role-selection UI is in scope now.
- Deliver an MP3 plus a readable transcript, source references, and timing data.
- Commentary is original, generated study commentary, not official Church text.
- Preserve every verse once, in order. Exclude page navigation, chapter summaries,
  and footnote markers from scripture narration.

The preparation process may use the internet to obtain source pages and initial
dependencies/models. Speech synthesis uses local assets; the MP3 can be copied
to the owner's device for offline listening. Offline speech does not imply
offline retrieval or offline AI explanation generation.

## Setup evidence

A Python 3.12.9 executable was found at
`C:/Users/marti/.local/bin/python3.12.exe`; the normal `python` command resolves
to a Windows Store alias and did not run Python. An isolated environment under
`.tools/tts_env/` has `kokoro-onnx==0.6.1`, numpy, scipy, soundfile, ONNX Runtime,
and Beautiful Soup. Dependencies/model files are local, ignored output.
PySide6 and ffmpeg are unnecessary for this sample's isolated export path.

Record exact dependency versions and model hashes with the rendered output.
Runtime results belong in the source-file changelog until the owner confirms
the listening experience; do not claim mobile or listening quality validation
from file generation alone.
