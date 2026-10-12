# app.js Changelog

## 2026-10-11 — Weekly section navigation and revised-audio resume — [UNCONFIRMED]

**What changed:** Navigation/autoplay now span introduction, chapters, and review. Displays nine scripture chapters, shows appropriate commentary-only status, requests versioned MP3 URLs, and restores time only for the same audio revision.

**Why:** Make the new framing playable in order without using stale audio or positions after revisions.

**Side effects / limitations:** Stable chapter IDs preserve chapter selection and listening preferences; modified tracks restart at their beginning when old timestamps no longer correspond. Owner listening/UI feedback remains pending.

## 2026-10-11 — Playback and synchronized transcripts — [UNCONFIRMED]

**What changed:** Added JSON loading, nine-chapter selection, exact numbered
scripture text and spoken commentary, timestamp seeking, passage highlight,
optional follow scrolling/autoplay, fifteen-second skips, playback speed, saved
chapter/position/options, and progressive Media Session system controls.

**Why:** Support chapter-based listening and resume through a static Pages site.

**Dead ends / limitations:** Exact-label Speed lookup in browser QA matched no
elements because the nested select contributes option text; used its observed
stable ID. No application workaround was needed. Mobile system controls vary by
browser and still require an actual iPhone check. Storage can be unavailable.

**Side effects:** One persistent audio element retains immediate play calls in
tap handlers. Relative URLs work at root and under project subpaths. Uses local
browser storage; no account, runtime AI, or external speech service. Guards
metadata handling when the library fetch fails, retaining native audio fallback.
Seeking while paused refreshes the status message instead of leaving a completed
chapter message on screen. Reduced-motion scrolling uses standard auto behavior.

**Validation:** JavaScript syntax passed. Chrome verified Play, Pause, seeking,
transcript jump/highlight, saved position/speed after refresh, all chapter
transcripts/audio sources, autoplay transition, and final-track stopping. No
browser console warnings/errors were observed during the chapter checks.
