# CHANGELOG - tools/render_personal_session.py

## 2026-10-11 — Commentary-only lesson tracks and verified segment reuse — [UNCONFIRMED]

**What changed:** Added safe introduction/review filenames, commentary-only validation, and an optional prior-render directory. Reuse requires matching original session, reader/model hashes, spoken text, full voice settings, WAV duration/rate, and valid mono samples. Added canonical Markdown transcript output using role-only headings.

**Why:** Render two new framing tracks and nine revised openings while preserving unchanged scripture/commentary WAVs.

**Side effects / limitations:** The first full-week rerender reused 89 unchanged WAVs. Only nine openings plus the two framing tracks were synthesized. Original voice settings, scripture text, and speech normalization were retained. Owner listening/UI feedback remains pending.

## 2026-10-11 - Full weekly chapter batch and natural endings - [UNCONFIRMED]

**Status:** [UNCONFIRMED] - the full weekly audio set awaits listening review.

**What changed:** Generalized chapter labels and MP3 filenames and added ordered
multi-session CLI rendering with one shared loaded Kokoro model. Prepared
Isaiah 58-66 as individual chapter files with beginner explanations and closing
summaries/takeaways. Removed the spoken suggestion to pause the recording.

**Why:** The owner approved the revised sample apart from the pause instruction
and requested each chapter. Separate chapter files support the planned next
arrow and optional chapter autoplay without spoken control instructions.

**Dead ends / limitations:** No new failed approach. Navigation/autoplay are
documented future app requirements, not implemented controls. Scripted source
coverage and audio-file validation do not replace owner listening review.

**Side effects:** New local weekly outputs under `output/2026-10-12/chapters/`
and a ZIP containing the MP3s and transcripts. Earlier samples remain available.

**Verification (2026-10-11):** The shared-engine batch rendered all nine chapters
successfully. Every MP3 decodes to valid non-silent 24 kHz audio; filenames,
voice assignments, source-session hashes, and ordered verse coverage match each
chapter's session. All 160 verse texts were compared with cached official pages.
Each chapter has a closing recap, and no spoken text contains the recording-pause
suggestion. The combined duration is 58.53 minutes. ZIP integrity and its nine
MP3/nine transcript entries passed. Original reader source is unchanged. The
novel chapters remain unconfirmed pending owner listening/content feedback.

## 2026-10-11 - Spoken initials and chapter recap revision - [CONFIRMED 2026-10-11]

**Status:** [CONFIRMED 2026-10-11] - revised audio awaits the owner's listening review.

**What changed:** Added personal-name normalization before commentary sentence
chunking: middle-initial periods are omitted from speech, while scripture and
source text retain their wording/punctuation. Rendering metadata now records
the actual spoken text. Prepared a second Isaiah 58 session with a concluding
chapter summary, four key lessons, and a simple application prompt.

**Why:** The owner heard unnecessary pauses in names such as Henry B. Eyring and
requested a chapter overview and takeaways. Applying the correction before
chunking avoids treating the initial as a sentence ending.

**Dead ends / limitations:** No new failed approach. The change targets personal
names in commentary, retaining ordinary sentence endings and abbreviations.
Listening confirmation of the revised pronunciation remains pending.

**Side effects:** Revised local outputs are stored in `output/2026-10-12/v2/`;
the reviewed first sample is retained for comparison.

**Verification (2026-10-11):** Name normalization checks passed for Henry B.
Eyring, Russell M. Nelson, and multiple initials, preserving normal sentence
punctuation, other abbreviations, and numbers. Revision two rendered successfully
to a 435.836-second MP3 (7:16); its closing summary starts at 370.960 seconds
(6:11). All 14 verse records match the first sample unchanged and occur once in
order. All 12 segments use the selected voice roles. Recorded spoken text omits
the initials' periods; decoded MP3 and recap WAV have valid non-silent audio.
The original reader source hash is unchanged. Perceived pronunciation and recap
quality await owner confirmation.

## 2026-10-11 - First offline dual-voice MP3 utility - [CONFIRMED 2026-10-11]

**Status:** [CONFIRMED 2026-10-11] - awaiting successful rendering and the owner's
confirmation after listening.

**What changed:** Added a local renderer for a prepared session containing exact
verse records, commentary, source metadata, and two voice roles. Reuses engine,
chunking, and pitch definitions from the owner's `tts_reader.py` without loading
Qt. Loads existing model files once, produces MP3 plus individual WAV segments
and timing metadata, and checks verse order/coverage and encoded audio.

**Why:** The owner requested one complete Isaiah 58 sample for personal offline
listening before building the app. Keeping scripture and commentary separate
permits exact coverage checks and audible voice changes.

**Dead ends / limitations:** Original-reader CLI/import would still require Qt
because GUI imports are unconditional. This utility avoids that dependency.
The first render attempt stopped before synthesizing audio because the isolated
helper namespace omitted `re`, required by the reader's sentence chunker. Added
that import to the helper namespace before retrying.
The subsequent render was stopped when the owner chose male scripture narration
and female explanations. The prepared session was updated to Michael/Heart in
those roles before restarting; the canceled run is not a delivered sample.
It depends on selected definitions in the sibling reader and is intended for
the personal prototype, not a finalized mobile architecture. Human listening
and commentary approval remain required.

**Side effects:** Outputs under `output/2026-10-12/` are local and ignored by Git.
No model download or content fetch occurs in the renderer. Source acquisition
and initial asset download are separate preparation steps.

**Runtime verification (2026-10-11):** Rendering succeeded after the namespace
fix and voice-role update. Delivered MP3 duration is 370.455 seconds (6:10),
24 kHz mono, 2,889,840 bytes. Decoding verified valid non-silent audio with a
peak below full scale. All 14 source verses appear once in order; all 11 segment
voice assignments match male Michael scripture and female Heart commentary.
The original reader hash is unchanged. Owner listening/content confirmation
remains pending; these checks do not assess pronunciation or perceived quality.
