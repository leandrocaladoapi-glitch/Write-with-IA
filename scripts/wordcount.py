#!/usr/bin/env python3
"""Word counter for the Write with AI manuscript.

Counts prose words only: HTML comments and the trailing "Research notes"
section (manuscript-only, not printed) are excluded, per the style guide.
Usage: python3 scripts/wordcount.py [files...]
       python3 scripts/wordcount.py            # all book inputs
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FILES = (
    [ROOT / "book" / "front-matter.md"]
    + sorted((ROOT / "book" / "chapters").glob("ch*.md"))
    + [ROOT / "book" / "appendices.md"]
)

COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
RESEARCH_RE = re.compile(
    r"\n## Research notes\b.*$", re.DOTALL | re.IGNORECASE
)
WORD_RE = re.compile(r"[A-Za-z0-9]+(?:['’\-][A-Za-z0-9]+)*")


def prose_words(text: str) -> int:
    text = COMMENT_RE.sub(" ", text)
    text = RESEARCH_RE.sub("\n", text)
    return len(WORD_RE.findall(text))


def main() -> None:
    files = [Path(f).resolve() for f in sys.argv[1:]] or DEFAULT_FILES
    total = 0
    for f in files:
        if not f.exists():
            print(f"MISSING  {f}")
            continue
        n = prose_words(f.read_text(encoding="utf-8"))
        total += n
        try:
            label = f.relative_to(ROOT)
        except ValueError:
            label = f
        print(f"{n:>7}  {label}")
    print(f"{total:>7}  TOTAL")


if __name__ == "__main__":
    main()
