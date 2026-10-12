# app.css Changelog

## 2026-10-11 — Keep expanded section count on one line — [UNCONFIRMED]

**What changed:** Prevented the section count pill from wrapping or shrinking.

**Why:** Eleven sections made the count wrap on the phone layout beside the
longer Lesson Introduction heading.

**Dead ends / side effects:** The first responsive check exposed the wrapped
count; the heading can still wrap naturally. Owner UI review remains pending.

## 2026-10-11 — Responsive study layout — [UNCONFIRMED]

**What changed:** Added cream/green styling, readable transcript typography,
desktop sidebar, horizontal mobile chapter navigation, large playback controls,
current-passage emphasis, keyboard focus, and reduced-motion support.

**Why:** Make listening controls and scripture comfortable on a phone and desktop.

**Dead ends / limitations:** Replaced text-based replay arrows whose numerals
overlapped with SVG arrows. The viewport override needed a reload before its
screenshot reflected mobile dimensions; DOM width then confirmed no overflow.

**Side effects:** Uses system fonts and Georgia; no external font/image requests.
Checked at an iPhone-sized 390×844 viewport with a 375px content width.
