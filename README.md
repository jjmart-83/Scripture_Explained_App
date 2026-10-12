# Scripture Explained

Scripture Explained helps youth and new Church members study a scripture
chapter with explanations guided by the week's official Come, Follow Me lesson.
The first personal MP3 prototype uses a male voice for scripture and a female
voice for explanations, including context from relevant lesson-linked sources.

**Status: personal audio prototype.** The owner accepted the revised Isaiah 58
sample, requesting removal of its closing pause suggestion. A web tool and
later Capacitor app remain planned.

The reviewed [Isaiah 58 MP3](output/2026-10-12/v2/Isaiah_58_Explained.mp3) reads all
14 verses with beginner explanations and closing takeaways in about seven minutes. Download/copy the
file to your device and play it in an MP3 player for offline listening. Read the
[transcript and source links](output/2026-10-12/v2/Isaiah_58_Transcript.md) alongside
the audio. These personal output files are local and excluded from Git.

See the [project setup document](docs/project_setup.md) for requirements, choices,
and next milestones, and the [MCP research](docs/mcp_research.md) for the two
content-access candidates.

## Appendix: contributor notes

Read [AGENTS.md](AGENTS.md) before making changes. Documentation follows the
owner's [AI Agent Project Documentation Guide](AI_Agent_Project_Documentation_Guide.md).
Setup is tracked in [the project changelog](docs/CHANGELOG_project.md).

The local Git repository is initialized. The prototype uses an isolated Python
environment and local Kokoro model assets; see [TTS research](docs/tts_research.md)
and [audio component reference](docs/audio_playback.md). MCP servers and web/app
scaffolding have not been installed. Node.js and npm were not found in the setup
shell on October 11, 2026; see the setup checklist.
