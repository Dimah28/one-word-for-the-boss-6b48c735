#!/usr/bin/env python3
"""One Word for the Boss — entry program.

Writes exactly one word (15 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network access; writes only to MAKEFUN_OUTPUT_DIR.
"""

import os
import sys

ENTRY = "Meetingfluencer"


def validate_length(text: str) -> None:
    """Gate: the word is 1-30 characters."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 30:
        raise ValueError(f"entry is {len(text)} characters, must be 1-30")


def validate_single_word(text: str) -> None:
    """Gate: exactly one word, no whitespace of any kind."""
    if len(text.split()) != 1:
        raise ValueError("entry must be a single word")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must not contain whitespace")


def validate_entry(text: str) -> None:
    """Fail loudly if the word breaks the bounty gate (one word,
    1-30 characters, no whitespace) instead of submitting a bad entry."""
    validate_length(text)
    validate_single_word(text)


def main() -> int:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
