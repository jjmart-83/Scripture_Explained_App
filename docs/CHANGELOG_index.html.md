# index.html Changelog

## 2026-10-11 — Weekly study labels and description — [UNCONFIRMED]

**What changed:** Changed chapter-specific controls to Previous/Next section, added direct introduction/review links, and used clarity/understanding wording in descriptive text.

**Why:** Include weekly framing in the existing player and replace beginner labels with a more welcoming description.

**Side effects / limitations:** Default new-listener heading and native fallback reference Lesson Introduction. Transcript roles remain Scripture and Commentary. Owner listening/UI feedback remains pending.

## 2026-10-11 — Mobile audio/transcript page — [UNCONFIRMED]

**What changed:** Created the lesson header, chapter navigation, persistent audio
element, playback controls, transcript/source areas, accessible labels, and
no-JavaScript MP3 links. Transcript roles are Scripture and Commentary only.
Explicitly names the speed control through its visible label for accessibility.

**Why:** Let the owner listen through GitHub Pages on an iPhone without moving MP3s.

**Dead ends / limitations:** Direct file opening can block the JSON fetch; the
fallback retains native Isaiah 58 audio controls. Use HTTP preview or Pages.

**Side effects:** References only relative local assets and the official lesson.
Chrome desktop/mobile-size QA passed; actual iPhone behavior is pending review.
