"""Speech-only adjustments and canonical written transcript helpers."""
import re


def normalize_spoken_names(text: str) -> str:
    """Remove middle-initial stops in personal names before sentence chunking."""
    return re.sub(
        r"\b([A-Z][a-z]+)((?:\s+[A-Z]\.)+)(?=\s+[A-Z][a-z])",
        lambda match: match[1] + match[2].replace(".", ""),
        text,
    )


def transcript_markdown(session: dict) -> str:
    """Keep original written punctuation and label sections by role only."""
    lines = [f"# {session['title']}", "", f"Come, Follow Me: {session['lesson_dates']}", "",
             "Personal study commentary, generated to illuminate scripture language and meaning and deepen understanding.",
             "", "## Study sources", ""]
    lines.extend(f"- [{source['title']}]({source['url']})" for source in session["sources"])
    verses = {verse["number"]: verse["text"] for verse in session["verses"]}
    for segment in session["segments"]:
        lines.extend(["", "## Scripture" if segment["role"] == "scripture" else "## Commentary", ""])
        if segment["role"] == "scripture":
            for number in segment["verse_numbers"]:
                lines.extend([f"{number}. {verses[number]}", ""])
        else:
            lines.append(segment["text"])
    return "\n".join(lines).rstrip() + "\n"
