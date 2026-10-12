# Weekly Sections — Pending Owner Review

> Date: 2026-10-11. Owner-authorized requirements and implementation candidate;
> listening quality and revised UI still await owner feedback.

Add Lesson Introduction before Isaiah 58, and Week in Review after Isaiah 66.
The introduction relocates the week's orientation and two-voice explanation
from Isaiah 58. It frames the lesson around Christ as Redeemer, worship expressed
through service, His guiding light, and hope for His return. The review brings
those themes together with one invitation to remember a promise and act on it.
Both use the existing female commentary voice; scripture remains the male voice.

The audience remains youth/new members. Each chapter should use a consistent
opening describing explanations generated to bring clarity to scripture language
and deepen understanding of its message. Avoid labeling the listener a beginner.
Keep names such as Henry B. Eyring and Russell M. Nelson punctuated normally in
written transcripts. Speech-only normalization continues to omit initial periods.

The proposed listening sequence has eleven sections: introduction, nine chapters,
and review. Keep the existing public `chapters` array as the ordered sequence;
add `kind` (introduction/chapter/summary), retain stable IDs, and allow null chapter
numbers and zero verse counts for the two framing tracks. Previous/next and
autoplay traverse the whole sequence. Nine remains the displayed chapter count.
Use an MP3 hash as `audioVersion` for fresh audio URLs and saved-position checks,
so revised audio cannot use an older browser-cached file or mismatched timestamp.

Candidate maintenance workflow from the project root:

```powershell
.\.tools\tts_env\Scripts\python.exe tools/prepare_week_sections.py
$weekSessionPaths = @('output/2026-10-12/chapters/Week_Introduction/session.json')
$weekSessionPaths += 58..66 | ForEach-Object { 'output/2026-10-12/chapters/Isaiah_' + $_ + '/session.json' }
$weekSessionPaths += 'output/2026-10-12/chapters/Week_in_Review/session.json'
.\.tools\tts_env\Scripts\python.exe tools/render_personal_session.py @weekSessionPaths --reuse-from-dir output/2026-10-12/revisions/before_week_sections
.\.tools\tts_env\Scripts\python.exe tools/prepare_site.py
```

Preparation is specific to this week's locally prepared content. It retains prior
session/metadata/WAVs in the ignored revisions directory. The renderer verifies
the original session hash and reader/model hashes before reuse, then compares
each segment's spoken text and full voice settings and checks decoded WAV shape,
duration, and sample rate. Only matching segments may be reused. Revised openings
are synthesized again; old scripture/explanation WAVs remain unchanged. New
Markdown transcripts use canonical text and Scripture/Commentary labels.

The exporter preserves canonical commentary text for display and independently
checks that speech normalization matches the actual rendering metadata. Scripts
and exported website assets are versioned; local model assets and audio working
files remain ignored. This does not change the offline/background playback limits.
