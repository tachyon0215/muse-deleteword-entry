#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "The Word You'd Delete From the Dictionary": lisp.
Candidates compared: 'moist' (the first pick everyone thinks of, fails
freshness), 'synergy' (a familiar corporate-jargon deletion), and 'lisp'
(selected: the word for a speech impediment its sufferers cannot pronounce
cleanly, so deleting it is funny at first sight from the word itself).
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "lisp"
TEXT = LINE + "\n"
MAX_CHARS = 77


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if len(body.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
