# Personal Audio Preparation and Playback

> Status: personal MP3 prototype; version-two Isaiah 58 sample accepted on
> 2026-10-11 with a request to remove the spoken pause suggestion. Web/native
> playback is not implemented.
> Source: `tools/render_personal_session.py` and the sibling `tts_reader.py`.
> Last reviewed: 2026-10-11.

## Purpose

Prepare a complete scripture chapter with beginner explanations for youth and
new members, then deliver an MP3 suitable for personal offline listening. The
first reviewed sample is Isaiah 58, aligned with the October 12-18, 2026 lesson.
One male voice (Michael) reads scripture; one female voice (Heart) explains.
Selectable voice roles and advanced explanation levels are future options.

## Confirmed baseline interface and data

The renderer accepts a prepared session JSON path, an optional sibling-reader
path, and a local-model directory. It performs no source retrieval or model
download. The session holds exact numbered verse records, official source URLs,
ordered scripture/commentary segments, and voice parameters for each role.

The reviewed sample reads verses 1-14 once in order, with an introduction,
five explanation breaks, and a closing chapter summary with four takeaways.
Commentary defines unfamiliar language and uses
selective context from the lesson-linked Eyring and Nelson talks. The source
transcript distinguishes scripture from generated study commentary and links
the reviewed material.

Outputs live beside the session JSON: an MP3, per-segment WAVs, and a rendering
metadata JSON with duration, roles, timings, coverage, dependencies, and asset
hashes and actual spoken text. Middle-initial periods in commentary names are
removed before sentence chunking, preserving scripture/source wording. Outputs
and installed assets are ignored by Git. The reviewed version-two sample remains
in `output/2026-10-12/v2/`.

## Internal design and dependencies

Load only the existing reader's engine, chunking, and pitch definitions to avoid
its unconditional Qt imports. Initialize Kokoro once from existing local assets
and reuse the model across voice changes. Use numpy/soundfile for combining and
encoding audio and scipy for the existing pitch fallback. Preserve chapter
coverage before synthesis; verify that the encoded MP3 decodes, has the expected
sample rate/duration, and contains valid non-silent samples.

## Constraints and prior failures

- The original helper-loading attempt omitted `re`, which the reader's sentence
  chunker requires. That dependency is now included.
- Importing the whole existing reader requires PySide6 even for CLI use. Keep
  this prototype's isolated engine path rather than introducing Qt unnecessarily.
- The reader is a sibling-project dependency, not a packaged mobile component.
- Initial source research and model/dependency acquisition used the internet;
  local rendering and the delivered MP3 do not need an online speech account.
- File validation does not establish pronunciation, pacing, or perceived quality.
- User-visible audio revisions remain unconfirmed until the owner listens.

## Current requirements and pending expansion

Remove the closing suggestion to pause the recording. The owner wants a next
arrow in the eventual app and may want optional chapter autoplay; these are
future navigation requirements, not functioning UI.

The owner requested each chapter in the lesson. The current batch covers
Isaiah 58-66 as separate MP3s with transcripts under
`output/2026-10-12/chapters/`. Generalized chapter output and batch rendering are
tracked as unconfirmed until reviewed. Endings provide takeaways/application
without spoken recording-control instructions.
