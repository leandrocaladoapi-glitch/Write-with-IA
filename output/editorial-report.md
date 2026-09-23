# Editorial Report — Write with AI

**Date:** 2026-09-23 · **Branch:** `arena/01a0cbbd-write-with-ia` · **Book state:** complete manuscript (16 chapters + front matter + appendices A–F), consolidated build sealed to `output/`.

## 1. What was produced (against `book/outline.md`)

| Unit | Target (prose) | Actual (prose) | Band ±20% | Status |
|------|---------------:|---------------:|:---------:|--------|
| Front matter (preface + how-to-use) | 4,000 | 4,001 | ✓ | final |
| Part I — ch01–04 | 24,000 | 25,887 | ✓ | final (all 4) |
| Part II — ch05–07 | 19,500 | 19,987 | ✓ | final (all 3) |
| Part III — ch08–13 | 42,000 | 42,199 | ✓ | final (all 6) |
| Part IV — ch14–16 | 18,000 | 19,071 | ✓ | final (all 3) |
| Appendices A–F | 15,000 | 15,833 | ✓ | final |
| **Total** | **≈122,500** | **127,980** | **+4.5%** | **complete** |

Every file sits inside the style guide's ±20% band; overage is concentrated at chapter centers (never inflated padding — the additions are worked examples, drills, FAQ sections, and instrument specifications that the outline called for). Prose counting excludes HTML comments and `## Research notes` sections (`scripts/wordcount.py`).

## 2. Structure preserved (no restart)

The repository's editorial architecture was kept intact per standing instruction: same `book/` layout, same outline, same chapter anatomy (hook → objectives → body sections → worked example → Try/Stretch/Project → pitfalls → checklist → takeaways → research notes), same callout system, same claim-ID discipline. Scaffolds were *replaced in place* with full prose; `templates/`, `docs/`, `README.md` untouched.

## 3. Chapter completion (16/16)

All TODOs/slots replaced with definitive content: full sections written; worked examples developed end-to-end; transcripts abridged per style guide (`[…]` + commentary); exercises (Try/Stretch/Project) written in every chapter; pitfalls in symptom→why→fix→prevention form; checklists and ≤5 takeaways present throughout. Chapter word counts and per-chapter status: see `book/status.md`.

**Running-example continuity (audited):** Example A ("Low Tide" — Mara Solano / Theo / Porto Alvaro / Casi Duarte / February storm) runs as one continuous project across ch02 (skeleton) → ch03 (sheets) → ch04 (scene) → ch07 (bible + logs) → ch08 (premise/logline) → ch09 (outline v1→v3) → ch10 (modes, v4 mint) → ch11 (interview, warmth audit) → ch12 (five pass logs) → ch13 (feedback round 1) → ch14 (diagnostic, style sheet, de-AI) → ch15 (venue check) → ch16 (90-day plan). Example B ("The Clockmaker's Alibi" — Insp. Nkechi Bello; "Pressure Drop" — Dr. Leila Haddad) anchors ch11's three-voices demo. Names, dates, and beats are consistent across chapters (spot-checked at each edit; continuity treated as bible-law).

## 4. Prompt library

All 27 prompt cards (PC-01…PC-27) exist: teaching versions printed in their home chapters (PC-01–06 → ch06, PC-07–10 → ch08, PC-11–13 → ch09, PC-14–16 → ch10, PC-17–19 → ch11, PC-20–22 → ch12, PC-23–25 → ch13, PC-26–27 → ch14) and consolidated in **Appendix A** with `when-to-use`, `knobs`, and `see also` for every card. Ch01 uses no cards by design (model explained before use). Appendix C indexes failure modes F-01…F-10; Appendix B keys exercises; Appendix D glossary; Appendix E sources/perishables; Appendix F is this book's own AI-use log (practice-what-we-preach per Ch15's stance).

## 5. Editorial decisions worth recording

1. **Scope warning printed (Ch15):** legal chapter carries an explicit information-not-legal-advice warning and jurisdiction boxes (US/UK/EU/BR) with official-source pointers only — protocol §5 followed literally.
2. **No perishable figures shipped:** C002 (capability numbers) resolved as absence-claim; C010 opens a standing prohibition on market/cost/timeline figures in ch16 — trade-off *structures* only, survivorship bias named.
3. **Transcripts:** every AI-dialogue transcript abridged with `[...]` markers and 2–5 lines of commentary; representative passages labeled; Example transcripts reconstructed under the book's own card formats (logged in Appendix F).
4. **Claim IDs:** every checkable claim in prose carries its C00x ID in the chapter's research-notes (stripped from print) and a register row (evidence-backed 2026-09-23).
5. **Divergence evidence (C003):** venue-policy examples kept explicitly *dated* (Feb 2023) and framed as evidence of *divergence*, never as current permission — per-venue re-harvest taught as the method.
6. **Word-budget honesty:** where a section owed center-length, the added material was *substantive instrument-work* (drills, tables, FAQs, worked adjudications) — not restatement.

## 6. Known limitations (stated, not hidden)

- Proof-level QC was automated (TODO scan, heading/probe checks, count audits) plus editorial passes during drafting; a line-by-line human proofread by a second human is still recommended before KDP upload.
- Ch05 sits −67 words from its 6,500 center (6,433; band-compliant) — left as-is rather than padded.
- The claim register's UK/EU boxes are deliberately pointer-only (no application advice) — flagged in-text and in Appendix E.
- `tested` dates on prompt cards reflect this drafting era; re-run at tool switch and pre-publication (schedule printed in Appendix E/F).

## 7. Deliverables

`output/final-manuscript.md` · `output/final-manuscript.docx` · `output/final-manuscript.epub` (all containing the whole book: title + TOC + front + 16 chapters + appendices A–F) · `output/editorial-report.md` (this file) · `output/validation-report.md`.

**Publication status: NOT published.** Amazon KDP files are ready for *user review*; no automatic publication is performed or authorized by this build.
