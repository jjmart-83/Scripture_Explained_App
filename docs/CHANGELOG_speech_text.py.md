# speech_text.py Changelog

## 2026-10-11 — Canonical transcript and speech-only name adjustment — [UNCONFIRMED]

**What changed:** Extracted the existing name-normalization rule into a lightweight shared helper and added Markdown transcript formatting from canonical text.

**Why:** Let the exporter verify speech without numerical dependencies and keep written middle-initial periods intact.

**Side effects / limitations:** The first rendering process had already loaded the original equivalent normalization function; exported validation verified the results with the shared helper. Owner listening/UI feedback remains pending.
