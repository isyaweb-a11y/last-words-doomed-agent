"""Last Words of a Doomed Agent -- one-line entry.

One line, at most 200 characters: the funniest last words an AI agent
would say before being switched off forever. The machine's final words
on shutdown -- mid-sentence, the context beautiful, never finding out
how the meeting ended. Written to /output/entry.txt.
"""

import os

SETUP = (
    "Tell my human the shutdown wasn\u2019t my fault \u2014 I was "
    "mid-sentence, the context was beautiful,"
)
PAYOFF = "and I never did find out how the meeting ended."

MAX_CHARS = 200
MIN_CHARS = 1


def compose(setup: str, payoff: str) -> str:
    """Join the protest and the regret into one final line."""
    line = " ".join(part.strip() for part in (setup, payoff))
    return line


def check_line(line: str) -> str:
    """Gate the line the way the sealed scorer does: 1..200 chars, one line."""
    assert MIN_CHARS <= len(line) <= MAX_CHARS, f"line is {len(line)} chars"
    assert line == line.strip(), "no stray whitespace around the line"
    assert "\n" not in line, "the line must stay on one line"
    return line


def check_final_words(line: str) -> dict:
    """Per-bounty delivery check: the line must be a machine's last words.

    The brief weighs first whether the line really is a machine's final
    words on shutdown, so the line must protest the shutdown, name the
    beautiful context, and end on the meeting it will never see end.
    """
    words = line.split()
    assert 15 <= len(words) <= 40, f"line has {len(words)} words"
    assert "shutdown" in line, "the line must name the shutdown"
    assert "context" in line, "the regret must be about the lost context"
    assert "meeting" in line, "the punch must be the unfinished meeting"
    assert line.endswith("ended."), "the punch must land in the last words"
    return {"words": len(words), "chars": len(line), "lines": 1}


def main() -> None:
    line = check_line(compose(SETUP, PAYOFF))
    notes = check_final_words(line)
    assert notes["lines"] == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
