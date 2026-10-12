# Web Player — Pending Owner Review

> Status: authorized implementation, unconfirmed behavior. This is a planning
> and review record, not a confirmed component reference.
> Date: 2026-10-11.

The owner requested an HTML tool to show the transcript and play the prepared
audio, hosted on their GitHub Pages site for listening on an iPhone. Transcript
speaker labels must be Scripture or Commentary, with no TTS voice names.

The implementation candidate uses plain HTML/CSS/JavaScript in `site/`. It loads
one local JSON library containing all nine Isaiah 58–66 transcripts and timestamps.
MP3s are copied into `site/data/audio/`. There are no runtime external dependencies,
font/CDN requests, accounts, TTS generation, or application server. An official
lesson link and per-chapter source links remain available.

Proposed interface: chapter picker; play/pause; previous/next chapters; fifteen
second skips; seeking; speed; optional next-chapter autoplay; current transcript
highlight; timestamp jumps; optional follow scrolling; local saved position.
Autoplay and follow scrolling start off. Selecting another chapter while playing
continues playback; selecting while paused keeps it paused. Reload restores the
last position without automatically playing. The final chapter has no next track.

Use one persistent HTML audio element and invoke play directly within tap handlers
to preserve mobile user activation. Media Session handlers support system controls
where available. Catch autoplay rejection with a tap-to-play message. The JSON
export excludes voice configuration and raw source pages, preserves every verse,
and uses the actual spoken commentary text from the rendering metadata.

`tools/prepare_site.py` exports local session/metadata files without regenerating
speech. It checks session hashes, segment roles, verse coverage, audio size, and
verse/timing correspondence. `tools/preview_site.py` serves the site on loopback
with byte ranges for testing audio seeking. The Pages workflow uploads only `site/`.

Review limits: browser QA does not establish iPhone background playback, Bluetooth
controls, or quality of the generated commentary. Hosted audio streams over the
network; reliable offline caching is future work. Saved positions belong to this
browser/site origin, and can be lost when browser storage is cleared. This is
not a native CarPlay application. Confirmed references and README behavior will
be updated after owner feedback, per the owner's documentation guide.
