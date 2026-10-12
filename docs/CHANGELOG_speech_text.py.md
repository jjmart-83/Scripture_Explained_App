# speech_text.py Changelog

## 2026-10-11 — Say “and” for exactly two verses — [UNCONFIRMED]

**What changed:** Exactly two verses are announced as Verses X and Y. Single
verses retain Verse X, and groups of three or more retain Verses X to Y.

**Why:** Apply the owner's refinement to the passage-announcement wording.

**Dead ends / side effects:** No failed approach. Canonical text, first-block
book/chapter identification, and written transcript formatting are unchanged.

## 2026-10-11 — One announcement per scripture passage — [UNCONFIRMED]

**What changed:** Added scripture speech construction with a single Verse X or
Verses X to Y announcement, followed by exact unnumbered verse text. Book/chapter
is included only for the first scripture block. Reject empty, nonconsecutive,
out-of-order, duplicate, noninteger, and nonpositive verse ranges.

**Why:** Remove distracting individual spoken verse labels while orienting the
listener to each passage before the next commentary block.

**Dead ends / side effects:** No failed approach. Written transcript formatting
is unchanged. Five contract checks cover first/later and single/multiple verse
blocks plus invalid ranges. Listening quality awaits owner feedback.

## 2026-10-11 — Canonical transcript and speech-only name adjustment — [UNCONFIRMED]

**What changed:** Extracted the existing name-normalization rule into a lightweight shared helper and added Markdown transcript formatting from canonical text.

**Why:** Let the exporter verify speech without numerical dependencies and keep written middle-initial periods intact.

**Side effects / limitations:** The first rendering process had already loaded the original equivalent normalization function; exported validation verified the results with the shared helper. Owner listening/UI feedback remains pending.
