# Validation Report — Write with AI

**Date:** 2026-09-23 · **Branch:** `arena/01a0cbbd-write-with-ia` · **Final GitHub commit (manuscript payload):** `55274176005412acd3fcbbc1037aa578b75363c1` (complete book + reports + build; this SHA line was recorded in the immediately following seal commit on the same branch — see Git history)

## 1. Real word count

**Method:** prose only — `scripts/wordcount.py` strips HTML comments (`<!-- … -->`) and everything from `## Research notes` to the next heading, then whitespace-counts. This matches the style guide's counting rule (comments, metadata, research notes, and editorial instructions are not book text).

| Unit | Prose words |
|------|------------:|
| `book/front-matter.md` | 4,001 |
| `book/chapters/ch01.md` | 6,629 |
| `book/chapters/ch02.md` | 6,663 |
| `book/chapters/ch03.md` | 6,481 |
| `book/chapters/ch04.md` | 6,114 |
| `book/chapters/ch05.md` | 6,433 |
| `book/chapters/ch06.md` | 6,664 |
| `book/chapters/ch07.md` | 6,890 |
| `book/chapters/ch08.md` | 7,102 |
| `book/chapters/ch09.md` | 7,220 |
| `book/chapters/ch10.md` | 7,158 |
| `book/chapters/ch11.md` | 7,292 |
| `book/chapters/ch12.md` | 7,353 |
| `book/chapters/ch13.md` | 7,076 |
| `book/chapters/ch14.md` | 6,055 |
| `book/chapters/ch15.md` | 6,611 |
| `book/chapters/ch16.md` | 6,405 |
| `book/appendices.md` | 15,833 |
| **Total (sources)** | **127,980** |
| `output/final-manuscript.md` (built; +title metadata) | 127,990 |

Budget ≈122,500 → actual 127,980 (+4.5%); every file within the ±20% band (per-file bands verified; only ch05 sits below center, at −67 of 6,500).

## 2. Chapters completed

**16 of 16 chapters + front matter + appendices A–F — complete prose.** Status table with per-file counts: `book/status.md` (all rows `final`, dated 2026-09-23).

## 3. Verifications performed

**Claim register (`research/claim-register.md`):**
- **C001** (US human-authorship / copyrightability) — verified 2026-09-23 against USCO registration guidance (2023), USCO Part 2 report (released 2025-01-29), *Thaler v. Perlmutter* (D.C. Cir. 2025). Counter-evidence recorded (boundary litigation; re-check clause printed). Confidence: high.
- **C002** — resolved as absence-claim: **zero** capability/context-window figures printed in ch05 (audit). Confidence: high.
- **C003** (venue-policy divergence) — verified 2026-09-23: Clarkesworld Feb-2023 prohibition + submission closure (500+ bans; WaPo 2023-02-22, Vice 2023) vs. Metastellar's tool-neutral position (2023-02-21). Framed as dated divergence evidence; per-venue re-harvest mandated in-text. Confidence: high (as divergence claim).
- **C004** (craft consensus) — attributed to Field/McKee/Swain/Forster/Diamond + kishōtenketsu sources; contested points labeled opinion; minority views noted. Confidence: medium.
- **C005** (Noy & Zhang: −40% time, +18% quality, n=453) — *Science* 381(6654), 2023, doi:10.1126/science.adh2586 opened 2026-09-23; scope limits kept in-text. Confidence: high.
- **C006** (+14%/+34%, n=5,179) — NBER WP 31161 / *QJE* 140(2):889–942 opened 2026-09-23; explicitly framed not-generalizable-to-fiction. Confidence: high.
- **C007** (LGPD Lei 13.709/2018) — official Planalto text + D.O.U. 2018-08-15 opened 2026-09-23; scope narrowed to privacy-of-process; CNPq branch excluded; other BR matters pointer-only. Confidence: high (narrow scope).
- **C008** (97%→36%, halved effects) — Open Science Collaboration, *Science* 349:aac4716 (2015) opened 2026-09-23; low-power/counter-explanation recorded; psychology/n=100 scope attached. Confidence: high (with scope).
- **C009/C010** — appended as absence-claims (no positive AI-feedback stats anywhere; no market figures in ch16). Audits confirm both.

**No open claim rows remain.** Counter-evidence sought for every factual row (protocol §4); perishables table with as-of dates and re-check locations printed in **Appendix E**.

**Placeholder / TODO scan:** `grep -rn "TODO|FIXME|PLACEHOLDER|TBD|XXX" book/` → **zero actual placeholders** (remaining hits are (a) ch12's checklist text that *names* the scan and (b) status.md's old front-matter row, replaced in this cycle). Built manuscript scan → zero (three matches are prose that *uses the words* legitimately: "placeholder kitchen" craft example, "placeholder content" prompt tip, the ch12 gate line itself).

**Build validation (`scripts/build.py`):**
- HTML comments stripped: `STATUS: draft` count in `output/final-manuscript.md` = **0**.
- `## Research notes` sections stripped: count = **0** (Appendix E retained — heading differs by design).
- **EPUB probe:** `Chapter 1`, `Chapter 16`, `Appendix A`, `Appendix F`, `PC-01`, `PC-27`, `Preface`, `Worked example` — all present in EPUB HTML (whole book, TOC included).
- **DOCX probe:** `Chapter 1`, `Chapter 16`, `Appendix A`, `Appendix F`, `PC-27`, `Low Tide`, `Mara` — all present in `word/document.xml`.
- Card ID spot-check: `PC-27` appears 7× in built manuscript (ch14 teaching version + Appendix A + cross-refs); `Appendix F` 13×; `Chapter 16` 14×.

**Editorial QC:** band compliance per file (all ✓); running-example canon consistency spot-checked across ch02–ch16 at each edit; all 27 prompt cards present in Appendix A; F-01…F-10 indexed in Appendix C; every chapter has exercises + pitfalls + checklist + takeaways (heading scan during drafting).

## 4. Files delivered (`output/`)

| File | Bytes | Contains whole book? |
|------|------:|:--------------------:|
| `final-manuscript.md` | 885,500 | ✓ (title+TOC+front+16 ch+A–F) |
| `final-manuscript.docx` | 449,487 | ✓ (probe-verified) |
| `final-manuscript.epub` | 403,080 | ✓ (probe-verified) |
| `editorial-report.md` | — | n/a (report) |
| `validation-report.md` | — | n/a (this file) |

## 5. Final GitHub commit

**Manuscript payload commit:** `55274176005412acd3fcbbc1037aa578b75363c1` on `arena/01a0cbbd-write-with-ia` — contains all 16 chapters, front matter, appendices, verified claim register, `book/status.md` (final), `scripts/build.py`, all three manuscript files in `output/`, and both reports (with this SHA recorded in the seal commit directly after it). Full history on the branch: `fbf9e92` (appendices + ch02–07 top-ups) → `d5d85a4` (ch08–13/15 top-ups) → `5527417` (ch01/ch05 close, status final, register verified, build + outputs + reports) → seal commit.

**Publication: not performed.** KDP files await user review (explicit standing instruction: no auto-publish).
