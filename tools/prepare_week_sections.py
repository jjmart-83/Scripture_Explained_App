"""Prepare the lesson introduction, weekly reflection, and consistent chapter openings.

This edits local prepared scripts only. Render them before exporting the website.
Keep the original scripts/metadata/WAVs as a verified reuse source for the renderer.
"""
import argparse
import copy
import json
import shutil
from pathlib import Path

INTRODUCTION = """Welcome to this week's Come Follow Me study, The Redeemer Shall Come to Zion. We will read Isaiah chapters fifty-eight through sixty-six. Isaiah was a prophet in ancient Israel whose vivid language points us toward Jesus Christ.

The lesson begins with Jesus reading Isaiah in Nazareth and announcing His mission to bring healing and freedom. Watch for four connected themes: worship that blesses others, Christ's power to rescue, His light gathering His people, and hope for His return.

One voice reads each chapter in full. A second offers thoughtfully prepared explanations, generated to illuminate the language and meaning of the scriptures and deepen understanding. This is personal study commentary informed by the Church's lesson and selected linked resources.

As you listen, consider: what do I learn about the Savior, and how can I respond to His love?"""

REVIEW = """This week's Come Follow Me lesson brings Isaiah's many images into one hopeful picture: Jesus Christ can redeem His people and lead them into a renewed future.

In Isaiah fifty-eight, sincere worship reaches outward. Fasting and Sabbath observance invite us to draw closer to God and care for people who need help. In chapters fifty-nine and sixty-one, the Savior is the One who steps in to rescue and bring comfort. Chapters sixty and sixty-two describe His light and the gathering of His people. The later chapters remember His lovingkindness and combine honest repentance with hope for a world renewed under His reign.

Together, these passages invite us to remember what Christ has done, recognize His help now, and look forward to His return. Our response can begin in ordinary choices: tell the truth, relieve someone's burden, make room for God on the Sabbath, and help another person see the Savior's light.

As you reflect on the whole week, choose one promise about Jesus Christ to remember and one way to live differently because of it. You do not need to understand every image in Isaiah to begin trusting the Redeemer and following Him more closely."""

NUMBERS = {58: "fifty-eight", 59: "fifty-nine", 60: "sixty", 61: "sixty-one",
           62: "sixty-two", 63: "sixty-three", 64: "sixty-four", 65: "sixty-five", 66: "sixty-six"}
OPENING_PHRASE = "with explanations generated to bring clarity to its language and deepen our understanding of its message."


def write_json(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def prepare(chapters_dir: Path) -> list[Path]:
    originals = {}
    backup_root = chapters_dir.parent / "revisions" / "before_week_sections"
    sessions = []
    for number in NUMBERS:
        folder = chapters_dir / f"Isaiah_{number}"
        backup = backup_root / folder.name
        if not backup.exists():
            backup.mkdir(parents=True)
            for name in ("session.json", "render_metadata.json"):
                shutil.copyfile(folder / name, backup / name)
            shutil.copytree(folder / "segments", backup / "segments")
        original = json.loads((backup / "session.json").read_text(encoding="utf-8"))
        originals[number] = original
        session = json.loads((folder / "session.json").read_text(encoding="utf-8"))
        opening = session["segments"][0]
        if opening["role"] != "commentary":
            raise ValueError(f"Expected opening commentary: {folder}")
        if number == 58:
            opening["text"] = (f"This study reading covers Isaiah chapter {NUMBERS[number]}, {OPENING_PHRASE} "
                               "The chapter connects sincere fasting and joyful Sabbath worship with caring for people in need.")
            session["lesson_focus"] = "Fasting, helping people in need, and finding joy in the Sabbath."
        else:
            old_phrase = "with generated explanations for beginners."
            original_opening = original["segments"][0]["text"]
            if old_phrase not in original_opening:
                raise ValueError(f"Unrecognized original chapter opening: {folder}")
            opening["text"] = original_opening.replace(old_phrase, OPENING_PHRASE)
        session["title"] = f"Isaiah {number} Explained"
        session["kind"] = "chapter"
        session["revision"] = max(session.get("revision", 1), original.get("revision", 1) + 1)
        session["revision_notes"] = ["Consistent chapter opening; week-level context moved to Lesson Introduction."]
        write_json(folder / "session.json", session)
        sessions.append(folder / "session.json")

    lesson = copy.deepcopy(next(s for s in originals[58]["sources"] if s["id"] == "lesson"))
    scripture_sources = []
    for number, original in originals.items():
        source = copy.deepcopy(next(s for s in original["sources"] if s["id"] == "scripture"))
        source["id"] = f"isaiah_{number}"
        scripture_sources.append(source)
    luke = copy.deepcopy(next(s for s in originals[61]["sources"] if "luke/4" in s["url"]))
    luke["id"] = "luke4"
    intro_sources = [lesson, scripture_sources[0], scripture_sources[1], scripture_sources[2],
                     scripture_sources[3], scripture_sources[4], scripture_sources[7], luke]
    for kind, title, folder_name, filename, text, sources, focus in (
        ("introduction", "Lesson Introduction", "Week_Introduction", "Week_Introduction.mp3",
         INTRODUCTION, intro_sources, "A first look at the lesson and the themes connecting Isaiah 58–66."),
        ("summary", "Week in Review", "Week_in_Review", "Week_in_Review.mp3",
         REVIEW, [lesson, *scripture_sources], "Bring the week's themes together and choose one way to put them into practice."),
    ):
        session = {
            "id": "lesson-introduction" if kind == "introduction" else "week-in-review",
            "kind": kind, "title": title, "audio_filename": filename,
            "expected_verse_count": 0, "verses": [], "revision": 1,
            "lesson_dates": originals[58]["lesson_dates"],
            "audience": originals[58]["audience"],
            "commentary_status": "Generated personal study commentary; awaiting owner review",
            "voices": {"commentary": originals[58]["voices"]["commentary"]},
            "sources": sources, "lesson_focus": focus,
            "segments": [{"role": "commentary", "text": paragraph,
                          "source_ids": [s["id"] for s in sources]}
                         for paragraph in text.split("\n\n")],
        }
        path = chapters_dir / folder_name / "session.json"
        write_json(path, session)
        if kind == "introduction":
            sessions.insert(0, path)
        else:
            sessions.append(path)
    return sessions


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chapters", type=Path, default=Path("output/2026-10-12/chapters"))
    args = parser.parse_args()
    for path in prepare(args.chapters):
        print(path)
