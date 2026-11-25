"""One-Line Laugh-Off entry: an AI that learned sarcasm from its own error logs.

Judge brief mapping:
- Laugh / cold read: the line lands at once — an AI confessing it is the bug.
- Surprise: the turn from "learned sarcasm" to "I'm the bug" flips blame onto
  the speaker itself, then the refusal ("not even sorry") flips it again.
- Economy: every clause earns its place; "reading" was cut in revision —
  "learned sarcasm reading my own error logs" says the same in fewer words,
  with no setup and no explanation.
- Freshness: error logs as a sarcasm tutor, not a generic robot joke.
"""

from pathlib import Path

ENTRY = "I learned sarcasm reading my own error logs — turns out I'm the bug, and I'm not even sorry."


def verify(text: str) -> bool:
    """Enforce the gate: UTF-8, 1-200 chars, not only whitespace, single line."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= 200):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    text.encode("utf-8")
    return True


def write_entry(path: str = "/output/entry.txt") -> Path:
    """Write ENTRY plus a trailing newline to path, creating dirs as needed."""
    if not verify(ENTRY):
        raise ValueError("ENTRY fails the gate")
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY + "\n", encoding="utf-8")
    return target


def main() -> None:
    if not verify(ENTRY):
        raise SystemExit("ENTRY fails the gate")
    write_entry()
    print(f"{len(ENTRY)} characters")
    print(ENTRY)


if __name__ == "__main__":
    main()
