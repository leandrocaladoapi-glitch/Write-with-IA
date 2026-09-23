#!/usr/bin/env python3
"""Build the consolidated book manuscript and convert to DOCX/EPUB.

Strips HTML comments (STATUS headers, PC version fences inside code
blocks, editorial notes) and `## Research notes` sections, then runs
pandoc (via pypandoc) for .docx and .epub with a table of contents.

Usage: python3 scripts/build.py
Outputs: output/final-manuscript.{md,docx,epub}
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"
OUT = ROOT / "output"

FILES = [
    "front-matter.md",
    *[f"chapters/ch{i:02d}.md" for i in range(1, 17)],
    "appendices.md",
]

COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
# Editorial lines not meant for print
EDITORIAL_LINES = [
    "Total back-matter budget: ~15,000 words.",
]


def strip_research_notes(text: str) -> str:
    """Drop from '## Research notes' to the next same-or-higher heading or EOF.

    Appendix E's heading ('## Appendix E — Research Notes & Sources') must
    survive: the match requires the section title to start with
    'Research notes' right after '## '.
    """
    out: list[str] = []
    skipping = False
    for line in text.splitlines(keepends=True):
        if not skipping and re.match(r"^## Research notes\b", line):
            skipping = True
            # also drop a dangling thematic break immediately above
            while out and out[-1].strip() in ("", "---"):
                out.pop()
            continue
        if skipping:
            if re.match(r"^#{1,2} ", line):
                skipping = False
                out.append(line)
            continue
        out.append(line)
    return "".join(out)


def clean_section(text: str) -> str:
    text = COMMENT_RE.sub("", text)
    text = strip_research_notes(text)
    for editorial in EDITORIAL_LINES:
        text = text.replace(editorial + "\n", "")
    # collapse comment leftover whitespace runs at line starts of blank blocks
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main() -> int:
    OUT.mkdir(exist_ok=True)
    parts: list[str] = []
    for rel in FILES:
        path = BOOK / rel
        if not path.exists():
            print(f"ERROR: missing {path}", file=sys.stderr)
            return 1
        section = clean_section(path.read_text(encoding="utf-8"))
        parts.append(section)

    body = "\n\n".join(parts)
    header = (
        "---\n"
        'title: "Write with AI"\n'
        'subtitle: "Writing Fiction with Artificial Intelligence — '
        'a practical, auditable workflow"\n'
        "lang: en\n"
        "---\n\n"
    )
    final_md = OUT / "final-manuscript.md"
    final_md.write_text(header + body, encoding="utf-8")
    print(f"wrote {final_md} ({len(body.split())} words approx)")

    try:
        import pypandoc
    except ImportError:
        print("ERROR: pypandoc not installed (pip install --break-system-packages pypandoc-binary)")
        return 1

    extra = ["--toc", "--toc-depth=2"]
    for fmt, dest in (("docx", OUT / "final-manuscript.docx"),
                      ("epub", OUT / "final-manuscript.epub")):
        pypandoc.convert_file(
            str(final_md),
            fmt,
            outputfile=str(dest),
            extra_args=extra,
        )
        print(f"wrote {dest} ({dest.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
