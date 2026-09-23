# Status Tracker — Write with AI

## Lifecycle definitions (of done)

| Status | Meaning | Done when… |
|--------|---------|------------|
| `scaffold` | File exists with section skeleton | Headings + objectives + exercise slots present |
| `outline` | Fully planned | All sections, examples, exercises, prompt cards, pitfalls specified; research needs listed with claim IDs |
| `draft` | Full prose | Target word count ±20%; all transcripts commented; claims flagged |
| `revision` | Craft + accuracy pass | Style-guide compliant; **all claims verified** in register; counter-evidence recorded; perishables dated |
| `final` | Frozen | Edited, proofed, no open claim rows; changes need explicit re-open |

**Book state (2026-09-23):** all 16 chapters + front matter + appendices A–F in `final` — prose-complete within band (±20% of target, several at center), zero TODOs/placeholders, claim register closed (C001–C010 rows evidence-backed, counter-evidence recorded, perishables dated in each chapter's research-notes + Appendix E), consolidated manuscript built to `output/` (final-manuscript.md/.docx/.epub) with editorial + validation reports. Word-count method: prose only — HTML comments and `## Research notes` sections excluded (`scripts/wordcount.py`).

## Chapters

| File | Chapter | Target | Current (prose) | Status | Updated |
|------|---------|-------:|--------:|--------|---------|
| `chapters/ch01.md` | 1 — Why Write Fiction with AI? | 6,000 | 6,629 | final | 2026-09-23 |
| `chapters/ch02.md` | 2 — Story Fundamentals | 6,000 | 6,663 | final | 2026-09-23 |
| `chapters/ch03.md` | 3 — Character Fundamentals | 6,000 | 6,481 | final | 2026-09-23 |
| `chapters/ch04.md` | 4 — Setting, Scene & POV | 6,000 | 6,114 | final | 2026-09-23 |
| `chapters/ch05.md` | 5 — How Language Models Work | 6,500 | 6,433 | final | 2026-09-23 |
| `chapters/ch06.md` | 6 — Prompt Craft for Fiction | 6,500 | 6,664 | final | 2026-09-23 |
| `chapters/ch07.md` | 7 — Writing Environment & Setup | 6,500 | 6,890 | final | 2026-09-23 |
| `chapters/ch08.md` | 8 — Premise & Concept with AI | 7,000 | 7,102 | final | 2026-09-23 |
| `chapters/ch09.md` | 9 — Outlining & Structure with AI | 7,000 | 7,220 | final | 2026-09-23 |
| `chapters/ch10.md` | 10 — Drafting Scenes with AI | 7,000 | 7,158 | final | 2026-09-23 |
| `chapters/ch11.md` | 11 — Characters with AI | 7,000 | 7,292 | final | 2026-09-23 |
| `chapters/ch12.md` | 12 — Revision & Self-Editing with AI | 7,000 | 7,353 | final | 2026-09-23 |
| `chapters/ch13.md` | 13 — Feedback, Beta Readers & Iteration | 7,000 | 7,076 | final | 2026-09-23 |
| `chapters/ch14.md` | 14 — Voice, Style & Originality | 6,000 | 6,055 | final | 2026-09-23 |
| `chapters/ch15.md` | 15 — Ethics, Disclosure & the Law | 6,000 | 6,611 | final | 2026-09-23 |
| `chapters/ch16.md` | 16 — Publishing & Your Practice | 6,000 | 6,405 | final | 2026-09-23 |

## Front / back matter

| File | Section | Target | Current (prose) | Status | Updated |
|------|---------|-------:|--------:|--------|---------|
| `front-matter.md` | Preface + How to Use This Book | 4,000 | 4,001 | final | 2026-09-23 |
| `appendices.md` | Appendices A–F (A: prompt library PC-01…PC-27; B: workbook keys; C: F-01…F-10; D: glossary; E: research notes & sources; F: AI-use log) | 15,000 | 15,833 | final | 2026-09-23 |

**Total prose: 127,980 words** (budget ≈122,500; +4.5% — all files within ±20% band; overage concentrated at centers, no file inflated).

## Deliverables

| Artifact | State |
|----------|-------|
| `output/final-manuscript.md` | built (strip: HTML comments + research-notes sections) |
| `output/final-manuscript.docx` | built (pandoc 3.9 via pypandoc, TOC) |
| `output/final-manuscript.epub` | built (pandoc 3.9 via pypandoc, TOC) |
| `output/editorial-report.md` | built |
| `output/validation-report.md` | built |
| Publication | **NOT published** — user reviews KDP files first (no auto-publish) |
