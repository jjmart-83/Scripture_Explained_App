# Project Setup Changelog

## 2026-10-11 — Passage-level spoken verse announcements — [UNCONFIRMED]

**What changed:** Announce the book/chapter at the first scripture block, then
Verse X for a single verse or Verses X to Y for a group. Later scripture blocks
start with the verse/range announcement only. Removed individual spoken verse
labels within each passage; preserve numbered verse records on the page.

**Why:** Orient the listener before each commentary break without interrupting
the scripture repeatedly with verse numbers, as the owner requested.

**Dead ends / limitations:** Earlier setup/player/audio revisions remain pending
owner review; the current instruction authorizes this revision and publication.
No failed approach. Rendered pronunciations and pacing await listening feedback.

**Side effects:** Re-render scripture blocks in all nine chapters using existing
male narration; verify and reuse commentary audio. Preserve prior session/audio
files locally. New audio versions update public URLs and prevent restoring old
positions into revised timelines. Introduction/review and written wording remain
unchanged. Confirmed references/README retain their reviewed baseline.

**Initial checks:** Five speech-format contract checks passed for first/later,
single/multiple verse blocks and invalid ranges. Changed Python files compile.
Export now independently checks the spoken scripture against the canonical text
and announcement rules before publication.

**Validation:** All nine revised MP3s decode as valid non-silent 24 kHz audio.
Each of the forty scripture blocks has exactly one range announcement and the
full canonical text in order; all 160 verse records are unchanged. All 58 chapter
commentary WAVs match the prior files byte for byte. Both weekly framing tracks
and all written text are unchanged. Checked new timestamps against encoded audio,
and refreshed the local manifest/index/transcripts and website ZIP. Total listening
time is now 59.58 minutes. The exporter rejected old per-verse audio metadata,
confirming its new guard prevents stale narration from being published. Single
verse announcements are covered by contract checks; this week's groups all have
multiple verses.

**Publication:** Revision `a774747` deployed successfully in
[Pages run 38206786112](https://github.com/jjmart-83/Scripture_Explained_App/actions/runs/38206786112).
The live library matches the revised export exactly, and all eleven full published
MP3 hashes match the validated local files, including the nine new chapter tracks.

## 2026-10-11 — Consistent Isaiah 58 application wording — [UNCONFIRMED]

**What changed:** Replaced Isaiah 58's closing "For this week, choose one small
action" invitation with "A small application is to help someone with a burden
or plan something that helps you find joy in the Sabbath." Updated the prepared
session, canonical transcript, closing commentary audio, and website export.

**Why:** Match the application wording used at the end of the other chapters,
as explicitly requested by the owner after comparing their recaps.

**Dead ends / limitations:** Earlier setup/player/audio entries remain pending
owner review; this instruction authorizes the targeted revision and publication.
No new failed approach. Listening quality of the revised sentence awaits review.

**Side effects:** Retain the previous Isaiah 58 rendering locally and reuse its
eleven unchanged WAVs. Only the final commentary segment is synthesized again.
The existing audio-version mechanism refreshes the public MP3 and saved position.

**Validation:** All fourteen verse records and the eleven unchanged WAV segments
match the preceding Isaiah 58 revision. Only its closing commentary was rendered;
the MP3 decodes as valid non-silent 24 kHz audio (426.07 seconds). The other ten
public track entries are unchanged. Updated the local transcript, weekly manifest,
index, and website ZIP. The ignored validation helper initially needed the project
root added to its Python import path; subsequent checks passed.

**Publication:** Revision `550bafe` deployed successfully in
[Pages run 38205703097](https://github.com/jjmart-83/Scripture_Explained_App/actions/runs/38205703097).
The live library matches the local export, includes the revised closing sentence,
and the full published Isaiah 58 MP3 hash matches the validated local audio.

## 2026-10-11 — Weekly opening, review, and written initials — [UNCONFIRMED]

**What changed:** Added Lesson Introduction before Isaiah 58 and Week in Review
after Isaiah 66. Moved week orientation/two-voice instructions out of Isaiah 58,
made chapter openings consistent, and replaced "generated explanations for
beginners" with explanations generated to bring clarity to scripture language
and deepen understanding. Written commentary now retains canonical middle-initial
periods; only spoken text removes them. Added source-linked preparation helpers,
verified WAV reuse, canonical Markdown transcripts, and per-track audio versions.

**Why:** Frame the whole Come Follow Me lesson and make the explanations welcoming
without labeling the listener, while keeping natural speech and normal writing.

**Dead ends / limitations:** No new content/render failure. Kept shared name
normalization independent of numerical TTS dependencies so static exporting remains
lightweight. Earlier setup/audio/player entries remain pending review; this request
authorizes revisions and continued publication without confirming those entries.

**Side effects:** Eleven playable sections, including the nine original scripture
chapters. Revised MP3s receive hash-versioned URLs and old saved times are reset
when their audio revision differs. The prior session/metadata/WAVs are preserved
locally. Canonical scripture and the 89 unchanged WAV segments match the prior
version. New helper scripts and exported MP3s are committed; models/working files
remain ignored. Confirmed references/README retain their reviewed baseline.

**Validation:** Introduction 56.0 seconds, review 74.4 seconds, total 61.09 minutes.
All eleven MP3s decode as valid 24 kHz audio; all 160 verse records are unchanged.
Exported written text matches canonical scripts; normalized text matches rendered
speech. Cache mismatch/unsafe-filename guards passed. Browser checks verified
introduction playback, autoplay into Isaiah 58, and written Eyring/Nelson initials.
Further UI/publishing results will be recorded after completion; owner review is pending.

**Additional checks:** Browser autoplay traversed introduction → Isaiah 58 and
Isaiah 66 → Week in Review. Review finished without looping and Next was disabled.
The phone-sized layout had no page overflow; fixed the count pill wrapping beside
the longer introduction title. Standalone Python exported all eleven sections
without numerical/TTS dependencies. Revised HTML versions its script/style URLs,
and the player revalidates the library to avoid stale content after publication.

**Publication:** Pushed revision `4244999` and verified successful
[Pages deployment 38204855384](https://github.com/jjmart-83/Scripture_Explained_App/actions/runs/38204855384).
The published library matches the revised local export exactly; all eleven full
MP3 SHA-256 hashes match their local files. Reloading the live browser displayed
eleven sections, and the introduction played without errors using its versioned
audio URL. Browser tab handles expired during QA; a fresh tab and batched live
check completed successfully. Paused playback, saved the published preview, and
kept the live player open. Refreshed the eleven-track website ZIP as well.

## 2026-10-11 — Create repository and publish Pages — [UNCONFIRMED]

**What changed:** The owner explicitly authorized uploading the entire project
to a new GitHub repository and publishing the player. Prepare an initial main
branch commit, a public `jjmart-83/Scripture_Explained_App` repository, and the
existing Pages deployment workflow. Record the final deployment result below.

**Why:** Make the player available on the owner's iPhone through its hosted URL.

**Dead ends / limitations:** Prior implementation/audio/setup entries remain
pending owner review; the publication instruction authorizes deployment without
asserting listening or iPhone validation. No remote existed at session start.
The initial whitespace check stopped on intentional Markdown line breaks in the
owner's original guide. Preserved that file and checked the remaining staged files.

**Side effects:** Upload project source/docs and intentionally versioned MP3s;
honor existing ignore rules for secrets, models, dependencies, caches, and local
generated working files. Initial repository scan found no credential patterns
in uploadable files. The website and repository will be public.

**Outcome (2026-10-11):** Created the public repository
[`jjmart-83/Scripture_Explained_App`](https://github.com/jjmart-83/Scripture_Explained_App)
and pushed the complete 38-file initial project commit `b2c9e88` to `main`.
Enabled workflow-based Pages with HTTPS and set the repository homepage to
[`https://jjmart-83.github.io/Scripture_Explained_App/`](https://jjmart-83.github.io/Scripture_Explained_App/).
[Deployment run 38202876793](https://github.com/jjmart-83/Scripture_Explained_App/actions/runs/38202876793)
succeeded. Live HTML returned 200, the library matched local data exactly, and
all nine MP3 endpoints returned valid 206 byte ranges matching the local files.
Chrome playback on the published page reached ready state 4 and advanced time
without an audio error; paused playback and left the published player open.
Owner listening and actual iPhone lock-screen/Bluetooth review remain pending.

**Verification tooling:** Windows PowerShell's web-request helper rejected a
Range header before sending the request; standard Python urllib verified every
published audio range successfully. Actions emitted nonblocking runner/runtime
deprecation notices but completed the Pages deployment successfully.

## 2026-10-11 — Build GitHub Pages listening tool — [UNCONFIRMED]

**What changed:** Moved into owner-authorized web implementation with a static
HTML/CSS/JS listening tool and all nine prepared MP3s/transcripts in `site/`.
Added the Pages workflow, exporter, preview helper, SVG mark, `.nojekyll`, pending
web-player planning/deployment documents, and agent instructions for the new phase.
Source-file changelogs record behavior separately. Created a website-only ZIP
with index/assets/data at its root for optional branch-based hosting.

**Why:** Give the owner an iPhone-friendly player on GitHub Pages without manual
MP3 transfers, with role-only transcripts and chapter navigation.

**Dead ends / limitations:** Existing setup/audio entries remain unconfirmed;
the current request authorizes the player work without establishing prior audio
quality review. A Node REPL `process` lookup was unavailable; JS syntax checking
worked using its documented fs/vm modules. README and confirmed component
references remain at their reviewed baselines, as required by the owner's guide.
No native app, remote deployment, or reliable offline cache was implemented.

**Side effects:** The publishable audio is intentionally versioned under `site/`;
local source pages, models, and `output/` remain ignored. Original documentation
guide, previous audio, renderer, and sibling TTS reader are preserved.
Added standard Python bytecode ignore patterns after compiling the new helpers.

**Validation:** Root and subpath local browser playback passed, as did all nine
chapter sources/transcripts, exact 160-verse coverage, no voice fields in public
data, byte-range retrieval, and website ZIP integrity (25.83 MiB). Chrome checks
covered transcript seeking/highlight, saved progress/speed, autoplay transition,
final chapter stopping, and responsive layout. Actual iPhone lock-screen/Bluetooth
and GitHub deployment still require verification. No content was published.

## 2026-10-11 - Expand to Isaiah 58-66 and record chapter navigation - [UNCONFIRMED]

**Status:** [UNCONFIRMED] - weekly files await owner review. The owner accepted
the version-two sample apart from the spoken pause instruction.

**What changed:** Recorded natural chapter endings, a future next-chapter arrow,
and optional autoplay. Expanded personal audio preparation to all nine chapters
in the linked lesson, with source-linked transcripts and per-chapter recaps.
Confirmed the previously reviewed name/summary revision and updated its
component reference and README. The full-week output remains pending review.

**Why:** Make the accepted beginner format useful for the entire assigned
reading while preserving one chapter as the unit of playback.

**Dead ends / limitations:** No new failed approach. The app navigation design
remains a requirement; no web/native application has been built.

**Side effects:** Personal generated files remain ignored by Git. Earlier
samples are preserved; the sibling TTS reader is not edited.

**Outcome (2026-10-11):** Delivered `Isaiah_58-66_Explained.zip` (25.83 MiB), with
nine separate MP3s and nine source-linked transcripts. Generated a local chapter
index and weekly manifest. Audio totals 58.53 minutes and covers all 160 verses;
the updated Isaiah 58 file is 7:12 with its pause suggestion removed. All chapter
files preserve male Michael scripture/female Heart commentary, beginner
explanations, and concluding takeaways. Source coverage, decoded audio, hashes,
speaker roles, and archive integrity passed. Future next-arrow navigation and
optional autoplay are recorded as app requirements, not existing features.

## 2026-10-11 - Chapter recap and spoken-name correction - [CONFIRMED 2026-10-11]

**Status:** [CONFIRMED 2026-10-11] - revised audio awaits listening feedback. The owner's
"good start" feedback confirms the initial personal MP3 prototype; the original
documentation-baseline entry has not been explicitly reviewed.

**What changed:** Recorded the requirement for smoother spoken initials and a
beginner-friendly overall chapter summary with key takeaways. Prepared a
versioned revision so the prior sample remains available. Updated README to
describe the previously reviewed MP3 prototype and added an audio component
reference for its confirmed baseline; the new recap is still pending review.

**Why:** Turn the owner's listening observations into a reusable speech rule
and close the chapter with a clear lesson-focused synthesis.

**Dead ends / limitations:** No new failed approach. An app and explanation-level
selector remain future scope. The updated MP3 is not marked confirmed by
automated file checks.

**Side effects:** Local revised audio/transcript/session data under
`output/2026-10-12/v2/`; earlier outputs preserved.

**Outcome (2026-10-11):** Delivered the revised 7:16 MP3 and transcript. The
female explanation voice gives a concluding 180-word chapter summary with four
takeaways and a simple application prompt, starting around 6:11. Technical
checks confirm unchanged verse text/coverage, correct roles, valid decoded
audio, and middle-initial correction in the actual spoken text. The new audio
remains unconfirmed pending listening feedback.

## 2026-10-11 - Offline MP3 direction and existing reader review - [UNCONFIRMED]

**Status:** [UNCONFIRMED] - the owner chose mostly offline use and a full Isaiah
58 MP3 sample; technical setup and listening quality await review.

**What changed:** Reviewed the existing `tts_reader` source and config. Added
`docs/tts_research.md`; updated planning and agent instructions with offline MP3
scope and selective review of lesson-linked sources. Added `output/` to ignore
rules. Created `.tools/tts_env/` and downloaded the exact model/voice release
assets named by the existing reader into `.tools/tts_models/`.
The owner then specified youth/new-member explanations as the sole current
level; advanced levels are a future option. Recorded that target in planning
and prepared the sample's vocabulary/context accordingly.
The owner subsequently selected a male scripture voice and female explanation
voice for the sample, with future role swapping optional. Updated the session,
transcript, and planning to Michael narration and Heart commentary.

**Why:** Reuse the owner's familiar local speech engine and produce a concrete
personal audio test before building the web/native application.

**Dead ends / limitations:** The shell's `python` is a nonworking Store alias;
a separate Python 3.12.9 executable was located. Qt imports in the existing
reader are unconditional, so loading the whole script would require GUI
dependencies even for CLI export. No existing-reader code was changed. A
guessed browser-demo worker URL returned 404; the upstream README still provides
the browser API evidence used in research.

**Side effects:** Local dependencies and approximately 337 MiB of model/voice
assets acquired online. README operating behavior remains at the initial
application setup baseline pending owner confirmation of audio results.

**Sample outcome (2026-10-11):** Produced the beginner Isaiah 58 MP3 (6:10) and
source-linked transcript under `output/2026-10-12/`. Includes all 14 verses,
five explanation breaks plus an introduction, and selective context from the
lesson-linked Eyring and Nelson talks. Rendering used local model assets; the
MP3 requires no online speech account. File decoding, verse coverage, segment
roles, and unchanged original-reader source were verified. Listening approval
and perceived speech quality remain unconfirmed.

## 2026-10-11 - Initial documentation and local repository - [UNCONFIRMED]

**Status:** [UNCONFIRMED] - awaiting the owner's review of the setup documents;
no application behavior exists to test.

**What changed:** Initialized local Git and added `AGENTS.md`, `.gitignore`,
`README.md`, `docs/project_setup.md`, and `docs/mcp_research.md`. Captured the
owner's HTML/Capacitor direction, lesson-guided dual-voice reading, personal/family
first audience, and undecided explanation preparation method. The original
documentation guide was preserved.

**Why:** Establish durable project context before coding, compare content-access
candidates from evidence, and keep proposed architecture separate from settled
requirements and actual functionality.

**Dead ends / limitations:** Neither MCP was installed or tested. Source review
found that Jason's index excludes the current Home and Church URL pattern;
direct lesson retrieval remains a candidate. Node.js and npm were not found in
the setup shell or common Node locations checked. No failed runtime experiment
has occurred.

**Side effects:** Added a local `.git/` directory. No commit, remote, application
scaffolding, service registration, or dependency installation was created.
