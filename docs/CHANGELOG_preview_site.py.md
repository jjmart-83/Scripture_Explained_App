# preview_site.py Changelog

## 2026-10-11 — Local HTTP audio preview — [UNCONFIRMED]

**What changed:** Added a loopback-only, standard-library static server with
single byte-range responses for audio seeking. Directory/port are configurable.

**Why:** Test hosted-style playback and JSON loading without Node/npm; regular
file opening can block transcript fetches.

**Dead ends / limitations:** Browser track changes cancelled in-flight MP3
requests and produced harmless connection-aborted tracebacks in the preview log.
The GET handler now quietly handles those normal client disconnects. This is a
local development helper, not a deployed backend; Pages serves production assets.

**Side effects:** Defaults to `site/` on port 8765. Preview processes are stopped
after QA. Full, middle, suffix, and single-byte audio retrieval were checked.
