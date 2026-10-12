# Project Setup

> Status: pre-implementation planning. Requirements below come from the owner;
> proposals are for review, not approved technical decisions.
> Last reviewed: 2026-10-11 (America/Los_Angeles).

## Requirements stated by the owner

| Requirement | Meaning |
|-------------|---------|
| Personal/family use first | First-version scope; public distribution has not been decided. |
| Beginner explanations first | Main intended learners are youth ages 12-18 and new members with no assumed scripture background. |
| Advanced levels later | An eventual option for experienced readers; defer level controls and advanced scripts. |
| One male and one female voice | Start with male scripture narration and female explanations; role selection is a future option. |
| HTML tool first | Build a web experience, with later Capacitor packaging. |
| Two speaking voices | One reads scripture; another interjects explanations. |
| Scripture chapters | Chapter reading is central, rather than isolated verse lookup alone. |
| Weekly Come, Follow Me alignment | Explanations follow the official lesson's focus for the selected week. |
| Both sources required | Obtain the scripture text and the lesson before preparing the session. |
| Documentation before coding | Use the owner's documentation guide during setup and development. |
| Mostly offline use | Prioritize local speech and files that can be played without an account or connection. |
| Personal MP3s first | The initial Isaiah 58 sample is accepted; now prepare every assigned chapter, Isaiah 58-66. |
| Linked-source context | Review relevant links from the lesson, including conference talks; include context only when useful. |
| Natural chapter endings | End with summaries/takeaways; omit the suggestion to pause the recording. |
| Chapter navigation later | Future app has a next arrow, with optional chapter autoplay under consideration. |

Working name: Scripture Explained. Final app name, language, target devices,
voice preferences, hosting, and budget are still open. Mostly offline listening
and MP3 output are now stated priorities; offline explanation-model inference
and eventual on-device generation have not been selected.

## Intended listening experience

The listener selects a week and chapter. The scripture voice reads in order.
At useful passage boundaries, the explanation voice gives context connected to
the lesson, then the scripture voice resumes. This sequence describes the
owner's intent; the UI and interruption frequency have not been designed.

Proposed first proof: one official weekly lesson, one complete assigned chapter,
and a small number of lesson-focused explanations with identifiable sources.
Using one chapter for validation does not narrow the intended weekly coverage.

## Compare explanation preparation

| Consideration | Prepared weekly sessions | On-demand generation |
|---------------|--------------------------|----------------------|
| Workflow | Retrieve sources, create the script, review it, then listen. | Retrieve sources and create the script when a session is requested. |
| Review | Gives the owner time to check lesson alignment and accuracy before playback. | Needs automatic validation and a decision about whether review precedes playback. |
| Start time | Previously prepared sessions can start promptly. | New sessions require retrieval and generation; actual delay needs measurement. |
| Consistency | A saved version can replay the same explanations. | Content can vary unless a completed script is saved and reused. |
| Flexibility | Preferences require editing or regenerating the saved script. | Can tailor explanations to selected chapters and preferences at request time. |
| Service use | Generation happens during preparation; reuse can avoid repeat generation. | New requests may cause repeat generation; caching policy affects cost. |
| Offline potential | Depends on locally available text and the chosen audio/voice system. | New generation depends on the selected model's connectivity; saved sessions may differ. |
| Maintenance | Someone prepares and checks new weeks. | Requires a dependable generation and recovery workflow. |

**First step selected by the owner:** prepare a personal MP3 sample for the full
Isaiah 58 chapter. Preparation can access online source material; the resulting
MP3 is for offline listening. The eventual app's preparation mode remains open.
A possible later hybrid generates, validates, and saves a stable session before
playback. Both modes could share the same session format.

## Proposed system boundaries

1. **Content access:** find the correct official lesson and obtain its assigned
   scripture chapters with source URLs, language, and retrieval metadata.
2. **Lesson interpretation:** identify lesson themes, questions, and associated
   passages. Follow relevant lesson links to review supporting context, retaining
   each source URL and its relationship to the lesson. Include useful context
   selectively, with clear attribution; inaccessible links must be recorded as
   unread rather than silently treated as reviewed. Do not recursively crawl all
   links or replace the lesson focus with an unrelated topic.
3. **Session preparation:** place commentary between scripture segments and
   retain references to the scripture and lesson sections supporting it.
4. **Playback:** use separate voice roles and advance through the prepared
   sequence without overlaps, skipped verses, or duplicate speech.
5. **Web interface:** select the week/chapter and operate playback. Confirmed
   controls and accessibility requirements will be documented later.
6. **Capacitor integration:** reuse the web interface and validate native audio,
   interruptions, screen-lock behavior, and storage on the selected devices.

These boundaries are planning proposals, not existing modules or API contracts.
A future session record might include the lesson identity, assigned passages,
exact verse text, ordered scripture/commentary segments, citations, preparation
status, and version. Decide the actual schema before implementation.

## MCP and application runtime

MCP exposes content-access tools to an AI client. Jason Bell's current server
uses a Node process and stdio transport; that process does not run inside a
plain HTML page or a Capacitor WebView. A hosted service or a separate content
preparation workflow is a possible integration boundary. See the
[source-backed MCP review](mcp_research.md).

The HTML player could consume sessions prepared outside the app. If the app
must retrieve sources and generate explanations itself, we need to decide
where those operations run. Keep any paid service credentials on the service
side of that boundary.

[Capacitor's documentation](https://capacitorjs.com/docs) supports the intended
web-to-native direction. It does not settle the audio implementation.
[Browser speech synthesis](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis/getVoices)
exposes voices available on the current device. Two acceptable distinct voices,
quality, offline availability, and long-session reliability need device checks.
The owner supplied an existing Python Kokoro ONNX reader and then prioritized
mostly offline MP3s. Reusing that local engine is the first sample's approach;
see [TTS research](tts_research.md). Browser-side Kokoro remains a candidate for
the later app. Cloud speech is not required for this sample.

## First personal audio sample

The owner selected the full Isaiah 58 chapter, using this exact
[lesson URL](https://www.churchofjesuschrist.org/study/manual/come-follow-me-for-home-and-church-old-testament-2026/42?lang=eng).
The official page labels it October 12-18, 2026 and assigns Isaiah 58-66. Follow
the provided lesson identity rather than silently substituting a lesson based
on today's date. The initial sample was Isaiah 58; the owner now authorizes each
of the nine assigned chapters as a separate MP3 with beginner explanations,
summary, and takeaways. Use natural endings without a pause instruction.

Review the lesson's fasting and Sabbath sections plus the linked Eyring and
Nelson talks. Keep exact scripture text separate from original commentary,
provide a source-linked transcript, and use different voices for scripture and
commentary. MP3, session data, transcript, and rendering metadata are local
outputs under `output/2026-10-12/`, excluded from Git. The first voice pair is
provisional: Michael (`am_michael`, male) reads scripture; Heart (`af_heart`,
female) gives explanations. The owner selected the initial roles; specific voice
quality/preferences still need a listening test. Swapping roles in a future app
is an option to preserve in the design, not a feature to implement now.

Use the beginner level only: explain terms such as transgression, yoke,
rearward, and Sabbath, make the passage's situation clear, and use simple
reflection questions. Assume neither prior scripture reading nor familiarity
with Church practices. Do not frame the lesson as instructions to begin or
extend a fast; this first sample explains the text and its connections.

Initial dependency/model acquisition requires a connection. Rendering from
available model files and listening to the resulting MP3 are separate from
online content research. This does not establish a fully offline explanation
model or a completed mobile app.

## Quality criteria to propose for the first implementation

- Scripture spoken from retrieved, checked text; commentary stored separately.
- Every inserted explanation identifies its passage and supporting lesson
  section/source. Label generated commentary and avoid implying Church endorsement.
- Missing, partial, or mismatched source content prevents session preparation
  and produces a clear recovery path.
- Commentary insertion preserves the full chapter's verse order and coverage.
- Voice changes occur at segment boundaries; starting a new session cancels old
  playback. Verify pause/resume and interruption behavior on target devices.
- Source links remain available for the listener to inspect the original material.

The owner has not yet approved these as acceptance criteria. Do not record them
as implemented or tested behavior.

## Setup inventory and next milestones

Observed on 2026-10-11: the folder originally contained only the documentation
guide. No ancestor AGENTS.md was found along the workspace path. A local Git
repository is now initialized; no commit or remote has been created. Git
2.55.0.windows.5 is available. Node.js and npm were not found in the current
shell, and Node was absent from the common installation locations checked.
This does not establish that no installation exists anywhere on the machine.

| Milestone | Work | Completion evidence |
|-----------|------|---------------------|
| 0. Documentation baseline | Agent instructions, setup/requirements, MCP research, status README, ignore rules. | Files are reviewable; setup changelog remains unconfirmed pending owner review. |
| 1. Settle first-version choices | Preparation mode, target device/browser, voice requirements, chapter coverage, online/offline behavior, budget. | Explicit decisions recorded; unknowns remain labeled. |
| 2. Content-access validation | Official lesson, scripture pages, and relevant linked sources were retrieved directly for personal preparation. MCP runtime testing remains a separate future investigation. | All 160 verse texts in Isaiah 58-66 compared with the official source pages; MCP candidates are still untested. |
| 3. Record implementation plan | Personal preparation uses a Python/Kokoro utility and explicit session records. Web tooling and its runtime boundary remain open. | Audio component reference records the reviewed prototype and actual source constraints. |
| 4. First listening prototype | Isaiah 58 with lesson-focused explanations, corrected spoken initials, and chapter recap. | Owner accepted revision two apart from the pause suggestion. |
| 5. Weekly audio set | Prepare separate Isaiah 58-66 MP3s with transcripts and natural endings. | Rendering/file checks followed by owner review of the new chapters. |
| 6. Web and native application | Build the HTML interface, including next-chapter navigation; investigate optional autoplay and later Capacitor packaging. | Tests on chosen platforms and owner confirmation when app coding begins. |

Before public distribution or bundled/offline content, resolve applicable
content-use terms and any third-party code licensing. Access through an MCP
server alone does not answer those questions; no legal conclusion is recorded.

## Documentation lifecycle

This setup plan may record new questions, research, and proposed decisions while
the project is being defined. `docs/audio_playback.md` now records the
owner-reviewed personal audio baseline. Other confirmed component references,
such as `docs/content_pipeline.md`, will be added as their designs are settled.
The content-pipeline filename remains a suggestion, not a file that exists.

Source-file changelogs begin with actual source changes and use the owner's
confirmation markers. README operating instructions and implemented component
behavior are updated after user confirmation, as required by the guide.
