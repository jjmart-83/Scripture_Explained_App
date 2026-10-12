# prepare_site.py Changelog

## 2026-10-11 — Verify rendered scripture announcements — [UNCONFIRMED]

**What changed:** Export now checks actual spoken scripture text against canonical
verses and the new first/later range announcement before copying audio/data.

**Why:** Prevent publishing old per-verse announcements or transcript/audio
disagreement after the speech-format revision.

**Dead ends / side effects:** No failed approach. Written verse numbers and
commentary punctuation remain unchanged. Export remains standard-library only.

## 2026-10-11 — Weekly listening sequence and written punctuation — [UNCONFIRMED]

**What changed:** Exported introduction and review around the nine chapters with kind, stable IDs, nullable chapter numbers, and MP3 version hashes. Written commentary comes from canonical session text, validated against normalized rendered speech.

**Why:** Show initials with periods in the transcript while preventing TTS pauses; publish an eleven-section sequence and refresh revised audio reliably.

**Side effects / limitations:** Exporter remains standard-library only: normalization is shared through speech_text.py instead of importing the numerical TTS renderer. Owner listening/UI feedback remains pending.

## 2026-10-11 — Static listening-library exporter — [UNCONFIRMED]

**What changed:** Added a standard-library exporter from local session/render
metadata to `site/data/library.json` and nine MP3 copies. Checks session hashes,
matching roles/segments/verse timings, complete verse coverage, and audio size.
Exported fields omit voice identities and retain exact verses, normalized spoken
commentary, chapter focus, timestamps, and official source links.

**Why:** Make local audio preparation publishable without browser TTS dependencies.

**Dead ends / limitations:** Fixed an intermediate capitalization helper before
delivery because `capitalize()` would lowercase names in the focus description.
Exporting does not generate speech or prove editorial/audio quality.

**Side effects:** About 26 MiB of publishable audio is intentionally tracked in
`site/`, while raw inputs/model files remain ignored. Existing audio is untouched.

**Validation:** All nine exported MP3 hashes match their originals; all 160 verses
match their source records; timestamps are ordered and within chapter duration;
public data has no voice configuration. Relative asset references resolve.
