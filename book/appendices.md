# Appendices — Write with AI

<!--
STATUS: draft (A–F complete prose)
TARGET WORDS: 15,000
CURRENT WORDS: (update at revision)
LAST UPDATED: 2026-09-23
-->

Total back-matter budget: ~15,000 words.

---

## Appendix A — Prompt Library

**Purpose:** every reusable prompt from the book, copy-paste ready, in one place. Format per card: **ID · title · when to use · the prompt (fenced, versioned) · knobs to adjust · see also.** Cards are model-generic; any card depending on a specific model capability carries a `tested` line and is re-verified pre-publication. **Maintenance rule:** behavior changes bump the version (`v1 → v2`) with a one-line delta; fill-only edits don't bump. Prompts introduced in Chapters 6–14 appear here in ID order; the *teaching* versions in the chapters include commentary — the library versions are the clean instrument.

### PC-01 — Scene drafter (voice-anchor)

**When:** drafting a scene from beats you've written (Ch 10, co-draft and expand modes). **Knobs:** anchor prose (refresh per scene), beats, POV/tense, length band, end-shape, banned list. **See also:** Ch 6 (anatomy), Ch 10 (modes), PC-14 (locks companion).

```text
<!-- PC-01 v1 · tested 2026-09 · generic -->
Role: you draft fiction scenes for me to revise; your text is raw
material, not final prose.
Context: [story situation in 2–3 lines: who wants what here, what
opposes]. Anchor prose (my voice — match rhythm and diction, do not
continue it):
[1–3 paragraphs of my prose]
Task: draft the next scene from these beats: [beats as short lines].
Constraints: POV [X], tense [past/present], [N]–[M] words; conflict
unresolved at the end; no backstory paragraphs; no words from my
banned list: [list].
Output: scene only after a line "DRAFT:" — no preamble, no titles.
```

### PC-02 — Critique my draft (structured)

**When:** first critique leg of any draft loop; scene-level review (Ch 6). **Knobs:** the five questions (swap for structure-altitude variants: paste "structure altitude — defer style" when in a Ch 12 pass-1), max-findings count. **See also:** Ch 6, Ch 12 (PC-20 for whole-draft scale).

```text
<!-- PC-02 v1 · tested 2026-09 · generic -->
Role: skeptical fiction editor; specific, unsentimental, no praise
unless a line earns it with a reason.
Task: critique the passage below against these five questions only:
1) What does the POV character want in this scene, and is it visible
by the midpoint? 2) Where does telling occur that should be staged?
3) Which sentences are generic (could appear in anyone's story)?
4) Where does POV/distance slip? 5) Does the ending turn or fade?
Format: numbered findings, each as [location quote] → [issue] →
[concrete fix]. Max 12 findings, ranked by damage.
Passage: [text]
```

### PC-03 — Explain-my-options brainstormer

**When:** any decision point with more than three live alternatives (Ch 6; scene outcomes; Ch 9's outline choices). **Knobs:** decision statement, option count, cost-dimension labels, cast-open flag. **See also:** Ch 6, Ch 1 (options widen, you select).

```text
<!-- PC-03 v1 · tested 2026-09 · generic -->
Role: options-broker, not co-writer; you generate choices; I choose.
Context: [story situation / decision point, 3–5 lines].
Task: give me 10 options for [decision], each labeled with:
(a) what it costs the protagonist, (b) which story shape it makes
most likely, (c) one risk it creates for pacing.
Rules: no option that requires new characters unless I mark
"cast open"; at least 3 options must be uncomfortable; no ranking,
no recommendation — I decide.
```

### PC-04 — Few-shot style transfer (my prose)

**When:** re-voicing a passage toward your own anchor (Ch 6; Ch 10 rewrite-mode companion). **Knobs:** anchor (1–3 best paragraphs), target, dimension list. **See also:** Ch 6 (few-shot), Ch 14 (PC-26 for symptom surgery — PC-04 is style *matching*, PC-26 is style *repair*).

```text
<!-- PC-04 v1 · tested 2026-09 · generic -->
Role: stylistic apprentice to the anchor prose below.
Task: rewrite the TARGET passage to match the ANCHOR's voice.
Abstract and carry: sentence-length rhythm, contraction habits,
interiority method, image-source range, punctuation tics.
Do not carry: the anchor's content, names, or plot.
Do not improve ideas — only manner.
ANCHOR (my prose): [1–3 paragraphs]
TARGET: [passage to re-voice]
Output: rewritten target only.
```

### PC-05 — Constraint imposer ("write with…")

**When:** line-level drills and constraint tests (Ch 6; Ch 14's ladder variation rungs). **Knobs:** constraint set (length caps, object demands, dialogue caps), preserved-fields list. **See also:** Ch 6, Ch 14.

```text
<!-- PC-05 v1 · tested 2026-09 · generic -->
Role: constraint executor for a drafting exercise.
Task: rewrite the passage under ALL of these simultaneously:
- no sentences longer than 18 words
- no abstract nouns from this list: [list]
- every paragraph must contain one concrete object handled by a hand
- dialogue lines ≤ 8 words
- keep: POV, tense, proper nouns, and the sequence of events
If a constraint makes the passage impossible, keep the closest lawful
version and list which lines you strained at, after the text.
Passage: [text]
```

### PC-06 — Prompt debugger

**When:** output misbehaves and re-rolling has failed (Ch 6; Ch 5's four forces). **Knobs:** your prompt / output / wanted-triple. **See also:** Ch 5 (field guide), Ch 6 (single-variable rule), Appendix C F-10.

```text
<!-- PC-06 v1 · tested 2026-09 · generic -->
Role: prompt engineer for fiction workflows.
Below: MY PROMPT and THE OUTPUT I got, plus WHAT I WANTED.
Diagnose in this order, stopping at the first confirmed cause:
1) vague/buried instruction  2) internal contradiction (check my
examples vs. my rules)  3) context pressure (what in my pasted
material pulls against my instruction)  4) stacked tasks.
For each confirmed cause: quote the offending line, then give ONE
revised prompt (full text) fixing only that cause. No praise, no
general advice. End with: what to test first and what result
would prove the fix worked.
MY PROMPT: [...] OUTPUT: [...] WANTED: [...]
```

### PC-07 — What-if ladder

**When:** premise ideation from a seed (Ch 8's constrained ideation). **Knobs:** seed, rung-rule set (cost-landing, genre bans), rung count. **See also:** Ch 8, PC-08 (test the survivor), PC-10 (fusion alternative).

```text
<!-- PC-07 v1 · tested 2026-09 · generic -->
Role: ideation partner executing a ladder, not a list.
Seed: [one sentence situation].
Produce 10 successive WHAT-IF rewrites. Rules for the ladder:
- Rungs 1–3: change ONE external condition each (place, era,
  profession, constraint of the situation) — keep characters intact.
- Rungs 4–6: each rung must give the protagonist a harder WANT
  (something they can fail at visibly).
- Rungs 7–8: each rung must add a cost that lands on a specific
  other person.
- Rungs 9–10: each rung must make the obvious genre version
  impossible (state which genre you just banned and why).
Format: numbered rungs, one line each, ending with: which rung you
would develop and one sentence of why — do not choose for me; flag
the choice as a suggestion only.
```

### PC-08 — Premise stress-test

**When:** one four-part premise ready for a months-long commitment decision (Ch 8). **Knobs:** premise text, author-proxy bullets (from your why-me file), declared constraints. **See also:** Ch 8, Appendix B (sample adjudications), Ch 12 (done-criteria cousin).

```text
<!-- PC-08 v1 · tested 2026-09 · generic -->
Role: ruthless development editor with no stake in your feelings;
you are testing a premise for a multi-month commitment.
Premise: [four-part premise — protagonist, goal, obstacle, stakes].
Run these checks, IN THIS ORDER, in this format — for each: FINDING
(one line), DAMAGE (high/med/low), REPAIR (one concrete change, or
"none available — flag for parking"):
1. STAKES CHECK: is the cost-of-failure concrete, climbable on the
   stakes ladder, and worse than inconvenience at every rung?
2. NOVELTY AUDIT: state the three most-predictable versions of this
   premise; then state what makes MINE not those — if you cannot
   tell them apart, say "center-of-distribution" loudly.
3. WHY-ME / WHY-NOW: what in ME (author-proxy below) makes this mine
   — and what in the present makes it urgent? If either is empty,
   mark the premise.
4. CAPACITY CHECK: against my declared constraints (length target,
   POV exclusivity, single-timeline), name the structural cost this
   premise will charge.
5. KILLER QUESTION: the one objection a skeptical first reader will
   raise by page 10 — phrase it as the reader's exact words.
No praise. End with: verdict — DEVELOP / PARK / PARK-AND-STEAL-
[element] (name the element worth cannibalizing later).
Author-proxy (why-me fuel): [3–5 lines]
```

### PC-09 — Logline refiner

**When:** compressing your hand-written logline (Ch 8; Ch 16's query package reuses it). **Knobs:** premise, *your* draft logline (always yours first), anti-word list. **See also:** Ch 8, Ch 16.

```text
<!-- PC-09 v1 · tested 2026-09 · generic -->
Role: logline editor; compression specialist; no new plot elements.
Input premise: [four-part premise]. Input draft logline (mine):
[your sentence].
Task: (1) DIAGNOSE my draft against the anatomy — name which slot
is missing, vague, or overloaded (protagonist / goal / obstacle /
cost / tonal signal). (2) Offer 6 REFINEMENTS of MY draft only —
each must keep my plot's events and characters; vary which slot
gets emphasis. (3) For each, note what it HIDES (every logline lies
by omission — name the omission).
Anti-rules: no words like "must confront"; no "battling
[abstraction]"; if my premise can't support a concrete cost, say so
instead of decorating it.
Output: diagnosis, then 6 sentences with their hidden cards.
```

### PC-10 — Idea combiner

**When:** fusing parked premises or a premise + formal constraint (Ch 8; the parked file's mining tool). **Knobs:** elements A/B/C, attempt count, anti-rules. **See also:** Ch 8, Ch 16 (the parked file as long game).

```text
<!-- PC-10 v1 · tested 2026-09 · generic -->
Role: synthesis engineer; I provide elements; you fuse, you don't
average.
Elements: A) [parked premise one-liner]  B) [parked premise
one-liner]  C) [optional formal constraint: one location / told in
documents / no direct dialogue / etc.]
Task: 5 fusion attempts. For each, state: (1) the NEW conflict that
exists only in the fusion (not A + B side by side); (2) which
element you had to distort to make room, and how; (3) the first
scene's goal in one line.
Anti-rules: no title-generation; no "best of both worlds" language;
if an element refuses to fuse, say so and give the nearest honest
version.
Output: 5 attempts, numbered, then stop.
```

### PC-11 — Outline critic (structure pass)

**When:** first adversarial read of a level-2 outline, pre-drafting (Ch 9). **Knobs:** skeleton paste (required), structure choice + length target, prior waivers (paste known-waived rows on re-runs). **See also:** Ch 9, Ch 12 (pass-1's outline-vs-draft diff), Appendix C F-03.

```text
<!-- PC-11 v1 · tested 2026-09 · generic -->
Role: structure critic for fiction outlines; adversarial by
assignment; praise is a failure of your job.
Context: SKELETON (stakes sentence + climax preview + arc, pasted)
+ LEVEL-2 OUTLINE (numbered change-lines) + my declared structure
choice and length target.
Task: run these six checks IN ORDER — for each: FINDING (quote or
name the beat range) → WHY IT MATTERS (one line, tied to the stakes
sentence or scene anatomy) → DAMAGE (high/med/low) → SUGGESTED
DIRECTION (a class of fix: "front-load motive," "merge beats,"
"cut" — do not rewrite my beats for me):
1. STAKES LADDER: which beats move personal/relational/existential
   rungs? Name any 3-beat stretch with zero rung movement.
2. WANT VISIBILITY: does the protagonist want on-page every 2–3
   beats? Flag stretches where things merely happen TO them.
3. MIDPOINT & CRISIS: does something irreversible change at the
   midpoint (map change, not just incident)? Is the crisis forced
   by accumulated costs rather than coincidence?
4. CAUSAL CHAIN: list any pair of adjacent beats connected only by
   "and then" where "therefore/but" is missing.
5. SETUP/PAYOFF LEDGER: every object, fact, and skill planted —
   matched to a payoff; every payoff — matched to a plant. Two
   columns, gaps listed loudly.
6. CLIMAX DEBT: does the climax preview require any character,
   rule, or prop that no prior beat introduces?
Output: six sections, numbered findings, damage-rated; end with
the THREE highest-damage findings only. No summary paragraph. No
praise. No rewritten outline.
```

### PC-12 — Pacing checker

**When:** the six checks came back clean but the read still feels off (Ch 9). **Knobs:** outline + *your* word-share estimates, structure's teaching defaults. **See also:** Ch 9, Appendix C (sag diagnostics feed PC-20).

```text
<!-- PC-12 v1 · tested 2026-09 · generic -->
Role: pacing analyst; you measure tempo, you don't judge ideas.
Input: LEVEL-2 OUTLINE with each beat's approximate word-share
estimate (my numbers, my responsibility) OR chapter word-targets
if drafting has begun.
Task: (1) Build a tempo table: beat | space allotted | pressure type
(pursuit/refusal/revelation/reaction/transition) | rung moved
(P/R/E/—). (2) Flag: any 3+ consecutive 'transition' or '—' rows;
any revelation cluster within 2 beats; any rung-movement gaps longer
than 4 rows. (3) Compare my midpoint's share of total space to my
structure's teaching default (three-act ≈ 40–50%; note deviations
without correcting them). Output: table, then flags, then stop — no
recommendations beyond flag classes.
```

### PC-13 — Subplot weaver

**When:** subplot inventory exists and needs structural audit (Ch 9). **Knobs:** main-line outline, subplot inventory with functions. **See also:** Ch 9, Ch 11 (foil presence rows).

```text
<!-- PC-13 v1 · tested 2026-09 · generic -->
Role: subplot engineer; every subplot must pay rent in the main line
or leave the document.
Context: LEVEL-2 OUTLINE (main line) + my subplot inventory below
(name · thematic echo of main want · structural function).
Task: for EACH subplot: (1) ENTRY: name the earliest beat where its
absence would be noticed — if none, mark VESTIGIAL; (2) TOUCH
BEATS: every main-line beat where the subplot must surface (min
every 4–5 beats — flag longer silences); (3) PAYOFF: the exact beat
where it changes stakes or meaning of the main line — if you can't
point at one, mark RENT-FREE and recommend parking; (4) COLLISION:
the beat where subplot and main line physically share a scene.
Output: per-subplot cards + inventory of VESTIGIAL / RENT-FREE
items. I decide what to park.
```

### PC-14 — Scene expander (beats → prose)

**When:** drafting under full locks with a bible pack (Ch 10's scene-beat prompting; the workhorse). **Knobs:** bible extract, anchor, charged beats, lock list (POV range, tense, banned *constructions*, end-shape, speech caps). **See also:** Ch 10, PC-01 (lighter sibling), PC-16 (post-draft description repair).

```text
<!-- PC-14 v1 · tested 2026-09 · generic -->
Role: drafting apprentice; output is material for my red pen.
Context (bible pack): [relevant names/spellings, story rules, the
scene's stakes line] + ANCHOR (my prose, voice target — match
rhythm/diction, do not improve):
[your hand-written paragraph]
Beats (change-lines, in order — dramatize in this order, no new
plot turns):
1. [...]
LOCKS (violate none): POV [close third, X only]; tense [past];
distance [2–4, deepest only at the outcome]; length [N–M words];
no backstory paragraphs; banned constructions: [emotion-as-weather,
etc.]; banned words: [style sheet]; dialogue carries subtext — no
character states the scene's conflict outright; END BEAT [#] must
land as [action / refusal / unresolved question], no summary
sentence after it.
Output: prose only after "SCENE:" — no titles, no notes.
```

### PC-15 — Dialogue-first drafter

**When:** relationship-first scenes; voice differentiation work (Ch 10; Ch 11). **Knobs:** per-speaker voice notes (from sheets), situation, beats, line caps. **See also:** Ch 10 (attribution pass stays yours), Ch 11 (PC-18 tests the result).

```text
<!-- PC-15 v1 · tested 2026-09 · generic -->
Role: unattributed dialogue generator; speakers distinguished ONLY
by their speech, never by my telling you who talks.
Context: two speakers' VOICE NOTES (diction, syntax, verbal habit,
never-say) + situation + beats 1–N.
Task: draft the exchange with NO dialogue tags and NO action beats —
just alternating lines, each speaker marked only as A:/B:.
Locks: each line advances, refuses, or deflects — no greetings, no
small talk openings; every A-line must be unlike a line B could say
(swap test); the scene's conflict never stated in plain words; end
on B's non-answer.
Then STOP — attribution pass is mine.
Output: A:/B: lines only.
```

### PC-16 — Description sharpener

**When:** post-draft description pass at constant count (Ch 10; Ch 12's line pass tools). **Knobs:** banned-simile list, sensory-channel gaps, count-retention rule. **See also:** Ch 4's ladder, Ch 10, Appendix C F-01.

```text
<!-- PC-16 v1 · tested 2026-09 · generic -->
Task: DESCRIPTION PASS on the scene below — diagnostic first.
1. List every descriptive sentence. Tag each [owned] (could only be
   in this story) or [generic] (any story's room — rung 2).
2. For each [generic]: propose ONE replacement at the SAME length,
   spending: this scene's pressure, one sensory channel not yet used
   in the paragraph, and no new information the scene hasn't learned
   yet.
3. Keep [owned] untouched, verbatim.
Constraints: total descriptive word count may not increase; no
weather indoors unless rule-allows; no similes drawn from: [list].
Output: tagged list, then the revised scene, then a count diff.
```

### PC-17 — Character interviewer

**When:** situational character mining before a pressured scene (Ch 11). **Knobs:** sheet fields, scene pressure, question count, flaw-first rule (never remove). **See also:** Ch 11, Ch 3's sheets.

```text
<!-- PC-17 v1 · tested 2026-09 · generic -->
Role: interviewer for a FICTION character IN SCENE — you ask the
questions; the CHARACTER answers in first person; you also note
what the answer refuses.
Context: character sheet below (fields 1,5,6,10 minimum) + the
specific upcoming scene's pressure.
Rules for answers: (1) every answer must include ONE concrete detail
a camera could film; (2) no abstract self-diagnosis words; (3) if
the question could be answered kindly by anyone, the character must
answer it specifically unkindly or specifically wrongly — their flaw
speaks first; (4) 60-word cap per answer.
Ask me 8 questions, ONE AT A TIME — wait for my reply roleplaying
the answer, then judge: "in-character / drifting to intern /
contradicts sheet field __" and correct before the next question.
After Q8: output the THREE answers most usable for the scene and ONE
refusal the character wouldn't touch (and why they wouldn't).
```

### PC-18 — Voice differentiation test

**When:** blind-attribution audit of dialogue (Ch 11; Ch 12's character pass). **Knobs:** cast voice-notes, exchange sample size. **See also:** Ch 11, Ch 3's field 10.

```text
<!-- PC-18 v1 · tested 2026-09 · generic -->
Role: blind attribution examiner.
Input: 6–10 dialogue EXCHANGES from my draft, speakers labeled only
A/B (strip tags first).
Task 1: for each exchange, guess the speaker from character sheets
(paste voice notes: diction / syntax / habit / never-say). Show
confidence 1–5 per guess.
Task 2: list every line that could have been said by EITHER speaker
without meaning changing (swap-violations), quote them.
Task 3: for each cast voice, output a ONE-LINE "fingerprint."
Output: guess table, swap list, fingerprints. NO rewrites — fixing
is my pass.
```

### PC-19 — Arc tracker

**When:** every draft mint; Ch 12's character-pass input (Ch 11). **Knobs:** sheet (arc type, false belief, pattern), chapter notes or pasted passages. **See also:** Ch 11, Ch 12 pass 2.

```text
<!-- PC-19 v1 · tested 2026-09 · generic -->
Role: continuity auditor for CHARACTER CHANGE (not plot).
Context: character sheet (arc type, false belief, flaw-pattern,
climax choice) + my chapter-by-chapter notes + any drafted chapters
pasted (sheet FIRST).
Task: for each chapter-note/passage, extract in a table:
chapter | pressure applied | pattern response (quote the triggering
line if pasted) | false-belief status (reinforced / challenged /
unaddressed) | cost logged? (Y/N — which cost) | rung moved
(P/R/E/—).
Flag: (a) 3+ consecutive chapters with pattern UNADDRESSED; (b)
growth-behavior appearing BEFORE any cost paid (arc pre-paid);
(c) any row contradicting the sheet's arc type. NO recommendations —
flags are my inventory to adjudicate.
```

### PC-20 — Developmental reader (full pass)

**When:** structure pass, whole draft or per part (Ch 12). **Knobs:** skeleton + outline-current + §5 + target (required context), altitude note ("structure altitude — defer style" after v1's density lesson), batch size. **See also:** Ch 12, Ch 13 (blind-spot section feeds beta questions).

```text
<!-- PC-20 v1 · tested 2026-09 · generic -->
Role: developmental reader — FIRST READER, not editor: you
experience the draft as a reader and report; you do not rewrite.
Context: SKELETON + outline-current + story rules + length/structure
target — pasted from the bible pack. Draft below (batch: [part —
full scenes, never summaries]).
Task: reader's report in this order, each finding location-quoted:
1. PROMISES: what does the draft seem to promise? Quote evidence.
2. PAY-OFF TRACK: where did you PULSE or SAG? Chapter/scene numbers
   + exact paragraph. Sag = where you'd skim — WHY (pressure /
   confusion / familiarity).
3. CHARACTER READ: what you believe now about each major character +
   the line that created it. Flag contradictions vs. pasted sheet.
4. ENDING DEBT: what does the ending owe given the promises — does
   the last quarter start paying?
5. BLIND SPOTS: three things you CANNOT evaluate from this batch
   (label: needs next part / needs outline / genuinely unsure).
Numbered sections, quotes required, worst first. NO praise section.
NO rewritten prose. Empty section: "none found — checked: X."
```

### PC-21 — Line editor (constrained)

**When:** line pass, chapter-by-chapter with row-level adjudication (Ch 12; Ch 14's de-AI overlaps — PC-21 *sweeps mechanics*, PC-26 *re-voices symptoms*). **Knobs:** style sheet paste, `[!mine]` markers set, target list, length-retention. **See also:** Ch 12, Ch 14.

```text
<!-- PC-21 v1 · tested 2026-09 · generic -->
Role: line editor under STRICT constraints; changes must be
justifiable against my style sheet (pasted: banned list, rhythm
preferences, voice notes) — pretty-for-its-own-sake is a failure.
Chapter below. Rules:
1. TARGETS ONLY: filter words, redundant doubles, passive where
   agent known, dialogue-tag adverbs, sentences >25 words WITHOUT
   deliberate rhythm justification (list any you keep and why).
2. PRESERVE ABSOLUTELY: proper nouns & spellings, POV/distance,
   tense, lock-list constructions, every fingerprint speech line,
   my unusual syntax if marked [!mine].
3. NO NEW INFORMATION: delete and tighten only — no new images,
   metaphors, or intensifiers. Word count: ≤100% of original.
4. OUTPUT: (a) diff list: ORIGINAL → EDITED + reason tag, (b) full
   clean chapter, (c) counts: changes n, words before/after.
I accept/reject per row; rejections are final.
```

### PC-22 — Continuity checker

**When:** continuity pass in bible-first batches of 2–3 chapters (Ch 12; Ch 5's type-split made executable). **Knobs:** bible extract (re-paste each batch), batch size (never grow it), battery categories. **See also:** Ch 12, Appendix C F-06.

```text
<!-- PC-22 v1 · tested 2026-09 · generic -->
Role: continuity auditor — bible-first, quotes-or-nothing.
Context: BIBLE EXTRACT (names list verbatim + relevant sheets +
timeline slice + rules + never-say lists) pasted ABOVE the chapters
— the extract is your ONLY source of truth for "correct."
Chapters: [batch of 2–3 full chapters — never more].
Battery, separate tables per category:
A. CONTRADICTIONS: passage | bible fact | chapter — only where the
   pasted extract covers the fact. Uncertain → "needs bible check"
   row, NOT a guess.
B. NAMES/SPELLINGS: every proper noun vs. names list.
C. DATES/AGES/TIME: reconstruct timeline slice; flag impossible
   sequences.
D. PROPS/TRAITS: scars/handedness/objects vs. sheets — quote both.
E. RULES: banned words/constructions/assurances — hit lists.
F. POV/TENSE: interior-access sentences — list; flag non-anchored.
Six tables, quotes mandatory, no commentary, no suggestions.
Uncertainty is a ROW TYPE, not a failure.
```

### PC-23 — Beta-question designer

**When:** before briefing human betas (Ch 13; your open flags are its required context). **Knobs:** open-flags paste, beta profiles, the ten-question architecture. **See also:** Ch 13, Appendix B (question keys' spirit).

```text
<!-- PC-23 v1 · tested 2026-09 · generic -->
Role: research-methods assistant for reader feedback — you design
QUESTIONS, not feedback; nothing about the draft's quality.
Context: my draft's OPEN FLAGS (pass logs excerpt) + stage
declaration + beta profile (1 sentence each).
Task: draft a questionnaire of TEN questions in this architecture:
Q1 ranked #1-fix | Q2 locate-skim ("name the paragraph") | Q3
belief-at-midpoint (+ which line) | Q4 prediction check | Q5
character testimony (side + trigger) | Q6 trust moment (+ line) |
Q7 two witness-forms of my known flags (NEVER "did it sag?" — if my
flag names the flaw, rephrase to address-free witness form) | Q8
last-line residue (exact words if remembered) | Q9 who-would-you-tell
+ why | Q10 permission-to-destroy ("quote your harshest line").
Rules: every question answerable with location+memory; zero craft
jargon; no question may name my anxiety or preferred reading; cap
each at 25 words. Output: the ten questions + a 3-line "how to
brief" note (stage, deadline, wrong-and-specific permission).
```

### PC-24 — Simulated reader perspectives (with caveats)

**When:** pre-flight only — questionnaire pilot, verified candidate-hunting, prediction rehearsal (Ch 13). **NEVER** as: substitute for humans, post-human "second opinions," or anything called beta in shared contexts. **Knobs:** persona (from *types*, privacy rule), witness protocol mirroring your Qs. **See also:** Ch 13's REALITY CHECK and ETHICS NOTE — reread both before running.

```text
<!-- PC-24 v1 · tested 2026-09 · generic -->
Role: you simulate a READER PERSONA responding to pages — you
generate their simulated reading-experience report; you do NOT
critique as yourself, and you attach no quality judgment of your own.
Persona (I provide): [3–5 lines — reading life, tastes, irritants,
what they DNF for — written by me, from real people as TYPES only,
never a specific real person's private details]
Witness protocol (mirror of my human Qs): for each chapter-range:
[1] speed-report with location | [2] belief-state + the line | [3]
prediction + confidence 1–5 | [4] trust-check (+ why) | [5] residue.
Then META-3: (a) which of my ten questions would YOU answer vaguely
— flag for redesign; (b) one witness-question my ten MISSED;
(c) anything where you had to INVENT rather than report — label
"invented."
Closing disclaimer line (mandatory, verbatim):
"Simulated testimony — no independent weight; verify against human
reads."
```

### PC-25 — Feedback triager

**When:** after intake, before any revision decisions (Ch 13). **Knobs:** vision pack (required), intake rows verbatim, pass-log excerpts for corroboration-cites. **See also:** Ch 13, Appendix C F-08.

```text
<!-- PC-25 v1 · tested 2026-09 · generic -->
Role: triage clerk — you classify and cluster; you NEVER vote on
vision (that's mine) and you never soften quotes.
Context: my VISION PACK (stakes sentence, done-criteria headline,
pass-1 waivers list, style bans — pasted) + intake rows (verbatim
quotes, reader, Q#, address where answered).
Task: (1) dedupe/cluster strictly BY ADDRESS; (2) tag each row:
located/addressless · witness/verdict-form · corroborates-pass-log?
(cite the log row if in pack) · praise-only; (3) propose VERDICT
CANDIDATE from {CHANGE, DISCUSS, OVERRIDE, FIX-THE-QUESTION} against
the vision pack — candidate only, with the pack-line that supports
it; (4) surface contradictions as PAIRS with both quotes, never
merged; (5) rank-1 findings listed first if marked. Output: table +
"pack lines used" + NOTHING resembling a revision plan (changes are
my drafting).
```

### PC-26 — De-AI prose pass

**When:** symptom-driven re-voicing after diagnosis (Ch 14). **Knobs:** style sheet (required), diagnosis quote + counts, `[!mine]` markers set *before* pasting. **See also:** Ch 14, Ch 12's line pass (altitude split: PC-21 sweeps mechanics; PC-26 re-voices families).

```text
<!-- PC-26 v1 · tested 2026-09 · generic -->
Role: sentence surgeon executing MY revoicing — you remove symptoms
and preserve skeleton; you do not add content, images, or opinions;
when unsure whether a line is load-bearing, LEAVE IT (flag instead).
Context: my STYLE SHEET (banned constructions + rhythm notes +
diction-class + tics-to-keep) + my diagnosis output (worst-offender
quote + symptom counts) + the passage.
Targets (apply only where flagged):
H1 hedge-strip (keep load-bearing uncertainty — list kept)
H2 diction-demote (upgrade-itis → my narrator's class; safe-familiar
   → my class at specificity, not fanciness)
H3 rhythm-break (mark narrow-band stretches; ONE split/merge/fragment
   per stretch — minimum intervention)
H4 reflection-tax cut (delete commentaries the scene performed;
   break symmetry pairs at ONE side — I choose from my sheet).
Preserve absolutely: plot facts, proper nouns, locked POV/tense/
distance, [!mine] markers, style-sheeted KEEPs.
Output: (a) table: ORIGINAL → EDITED + symptom-tag + keep-flags;
(b) clean passage; (c) counts per family. I adjudicate rows as in
PC-21; rejections final.
```

### PC-27 — Style imitator → variator

**When:** voice ladder runs (Ch 14, rungs 1–2). **Knobs:** target author's page, feature axis chosen, subject-matter swap-ins. **See also:** Ch 14 (acquisition stays in your hands — the *copying* is never delegated).

```text
<!-- PC-27 v1 · tested 2026-09 · generic -->
Role: style-analyst and exercise-partner — analysis and LABELED
DRAFTS ONLY; the hand-copying rung stays mine.
Part A — FEATURE INVENTORY (on the page I paste below): list the
techniques with numbers where possible: sentence-length pattern,
image sources, hedge frequency, balance usage, paragraph
architecture, dialogue-to-action ratio. Features only, no quality
judgment, no praise.
Part B — VARIATION DRAFTS (labeled exercise-only, 150 words each):
(a) same techniques, MY subject matter: [swap-in]; (b) same content
of my target passage, OPPOSITE their tendencies; (c) their page at
half-length with my banned list applied.
Output: inventory, then three drafts each prefixed "EXERCISE — not
for manuscript," then one line: which axis you think is most
load-bearing in the original and why (I will disagree or agree in
my notes).
```

**Library maintenance (recap):** drafts promote to cards only on second-run evidence; every card carries knobs + a failure note; retirements get autopsies (Ch 6's lifecycle); `tested` dates re-validated at tool switches and pre-publication (Appendix F). Your file should eventually embarrass this one with your own cases.

---

## Appendix B — Workbook Keys & Extra Exercises

**Purpose:** sample solutions for selected `Try`/`Stretch` exercises + extra drills. **Keys are sample responses, not correct answers** — they show *shape of engagement*, not the one true reply; your version differing from ours is usually a good sign, not a failure. `Project` exercises are never keyed (they build your own story). Because shapes teach better than summaries, the most-requested keys are printed at full worked length below, then the briefer markers for the rest.

**Ch 1 keys.** *Stretch (unaided vs. AI revision):* a strong log-note names one improvement **and** one casualty — e.g., "specificity up (added the broken gate detail the machine proposed — I rejected three adjective-y versions first); casualty: my second sentence's odd rhythm got smoothed — I restored it; net: submitting revised, but keeping original's sentence 2." The *casualty* line is the key's whole point: revisions without casualties are unexamined. *Baseline purpose check:* if your 200 words were "fine," good — Ch 14 needs *representative* you, not worst you.

**Ch 2 keys.** *10 premises in 20 minutes — quality markers (not content):* ≥3 genres represented; every premise has a checkable goal verb (find/get/sell/prevent — not "understand/realize/be happy"); ≥1 premise's stakes sentence names a *relational* loss; the two circled ones typically share one trait — *the obstacle welded to the protagonist's profession or wound* (pattern to notice, not rule to force). *Stakes-ladder sample (for a generic "heist" premise):* personal: he keeps the crew's respect / relational: his daughter's wedding invitation arrives revoked / existential: the code he lives by ("I finish what I start") dies — note rung 3 phrasing the *self-story as infrastructure*, the shape from the chapter.

**Ch 3 keys.** *Want/need for three known characters — shape check:* (1) want verb ≠ need verb in all three; (2) at least one need is *relational* not self-improvement-shaped ("learn to trust himself" is fog — "call his brother" is a need with an action built in); (3) one pair where the *want's success harms the need* (the friction column — seeing this once in *known* characters makes it buildable in *yours*). *Flaw-to-climax chain — link quality markers:* each choice *defensible in-character* (you can imagine the character justifying it aloud), each cost lands on someone/something named, climax line contains the flaw's *own instrument* turned (the pen, the schedule, the procedure).

**Ch 4 keys.** *Summary→scene labelling:* your labels should make the *conflict* visible before the prose does — if the prose reads conflict-free but labels claim one, the conflict is in your head (add an opposition beat: the door sticks, the offer is refused, the tea is poured for two and drunk by one). *Two-POV compare — what to notice:* each POV's * ignorance list* (what it can't know) should be doing structural work — irony, suspense, or misdirection; if both versions came out nearly identical, you anchored both in *events* rather than *minds* (re-do with one character's wound in the foreground of their version).

**Ch 5 keys.** *Five broken prompts (Ch 6's Try mirror):* (1) needs task+output shape+stakes context ("sad about the sea" → whose sea, what lost, how long, what shape — 60-word scene or 6-line stanza, and *why you want it*); (2) "better" needs criteria (paste original + name 2 targets: tighten / cut clichés / — never "make it better"); (3) missing context entirely (attach the story + the voice anchor + say what "continue" means: next scene? next paragraph?); (4) four adjectives doing zero checkable work → constraints: setting's pressure, each line carrying a lie, ≤6-word speeches, no guns; (5) no chapter, no questions → PC-02's five questions with the chapter pasted. *Common thread:* every fix adds **task + context + shape**; none adds politeness.

**Ch 6 keys.** *Five broken prompts (the chapter's own Try):* same anatomy as above — expected fixes add all five slots and convert ≥1 adjective; a full-credit fix to #5 also adds "critique structure first, altitude noted" (the altitude habit previewed).

**Ch 8 Try key (what-if ladder ×10):** shape markers — rungs 7–8 each name a *person* who pays; rungs 9–10 *state the banned genre* (an unlabeled ban is a wish, not a constraint); if your best rung is #1–#3, the seed was better than you rated it (the early rungs' job is *condition-swapping*, not profundity — don't rank rungs by impressiveness; rank by *pressure*).

**Ch 13 Try key (ten beta questions):** the graded dimensions — Q1 ranks; ≥8 questions pass location+memory; zero questions contain your anxieties (search the text for your known worries — if found, rewrite to witness-form); one question grants destruction. *A strong Q7 conversion:* "Does the middle sag?" → "Any paragraph you read faster or slower than the rest — name it, even if you don't know why."

**Worked keys — the ones readers ask about most (full samples):**

*Ch 2 Stretch (outline one premise at three granularities — sample for a generic "storm-warning sirens go silent" seed):* **Level 1:** "The town's storm sirens stop mid-alarm one Tuesday — and the engineer who could fix them has been lying about why for a year — so the council's vote to decommission the system (saving the budget that funds her father's care) lands the same afternoon the next real front forms." (Four parts audible: goal *keep the system live until the vote*, obstacle *her own buried fault-report*, stakes *care-home money vs. the coast's warning* — note the obstacle welding again: her *profession* and her *wound* are the same object.) **Level 2 sample lines (six of ~14):** "1 · Sirens die at 2:47 p.m.; Marta logs it as *grid flicker* — first false line in the ledger she'll have to walk back. → 2 · Council email confirms Friday's decommission vote; the attached budget table highlights her father's facility line. → 3 · Old fault-report draft surfaces in her files, timestamped the week before the first silence — she deletes it, then undeletes: something won't let evidence die. → 4 · (neighbor-test ✓ pressures 5) Teenager's hobby weather-station posts the Tuesday gap publicly; three replies ask the exact question Marta's report answers. → 5 · Trial balloon: Marta suggests 'scheduled maintenance' at the pre-vote briefing; the mayor's aide repeats it word-for-word on local radio — her lie now has a broadcast voice she didn't give it. → 6 · Father, mid-visit, asks why the sirens 'went shy last week' — he heard them stop from the care-home window; the question costs Marta the visit's last twenty minutes." — what to notice: every line *changes* something (status, exposure, cost — the neighbor-test's product), rungs move in clusters (2: personal-care pressure; 4: relational-public; 6: relational-private), and line 5's *amplification* mechanic (the lie acquiring *witnesses outside her control*) is the level-2 job level 1 couldn't do: **granularity isn't detail-adding; it's consequence-engineering.** **Level 3 (session-close beats, sample for scenes opening lines 4 and 5):** "4a · Marta refreshes the post — 400 views now; her comment box open, cursor blinking, *policy language* half-typed and abandoned. → 4b · Call to aide: she asks him to call it *routine*; he asks 'routine *what?*' — she hears herself not answer. → 5a · Radio playing while she drives; the aide's voice *is* her sentence — her words, his confidence; she turns it off at the second mention." (Each beat ≤ a breath: micro-turns, charge verbs, capacity checks passed — *beats are contracts with next session's FILL slots*, and these three are exactly PC-14's ingredient lines.)

*Ch 3 Stretch (secondary character to major — sample):* Minor: "the harbor-master who waves at Mara in passing" → major-path conversion: (1) *promotion decision* — what does this person now *want on-page* that the plot can obstruct (his own retirement vote, blocked by the same council budget as the sirens-line above's cousin — *wants get promoted before names get interesting*); (2) *want/need split* — public want: keep the port open through the storm season; private need: one apology to a son he sent away; (3) *flaw-pattern* — procedural hidebound (every novel risk logged as "not in the book"), so his *instrument of competence becomes his instrument of obstruction* when Marta's sirens-truth needs an exception filed; (4) *functional cast row* — his arc *echoes* the protagonist's (both protecting systems by hiding faults — the thematic double *cast into existence by decision*, not discovery); (5) *promotion's cost ledger* — who loses screen-time (the teen weather-station kid gets merged into his scene-4 confrontation — cast budgeting as *visible arithmetic*). The full conversion in one line: **a minor character becomes major the moment their *want* can collide with the spine on-page** — everything else (words, chapters, interiority) is downstream of that *structural* promotion.

*Ch 5 Try (rebuild a broken prompt — sample for the "tell me about X" case):* Original shape: "Tell me about [the 1890s lighthouse-keeper's daily routine]" → family diagnosis: fact-query through generation machinery (internal-vs-external split violated at the request level). Rebuild, two lawful versions: **Version A (delegation, external):** "You are a research *planner*. I'm writing a scene about an 1890s lighthouse keeper's night watch and need *primary-source* material. Give me: (1) five search queries aimed at archives/lighthouse-board records/diaries of that era and region; (2) three *specific* questions a historian would need answered for my scene (what happens at relief-ship delays, lamp-maintenance schedules, solitary-vs-stationed staffing); (3) a list of detail *categories* I should gather myself (smells, sounds at height, paperwork, food logistics) — do not supply the details; plan the sourcing." — note what got fixed: the *task* became planning (a genuinely generative strength), the *external* facts stayed mine to fetch, and the output *shape* (lists) matched the goal (a research route, not prose). **Version B (simulation, internal):** "Roleplay a *fictional* 1890s keeper named Jonas in first person for a 300-word diary entry — invent freely and mark invention acceptable: this is a *character exercise*, not history. After the entry, list every element you invented (so I can verify what I actually want to keep)." — the lawful box drawn *explicitly* (simulation + invention-list), which turns the hallucination risk from *hidden liability* into *labeled raw material*. Same information need, two architectures: **the rebuild's question is never 'how do I phrase it' but 'which side of the type-split does this live on, and what is the machine's honest job there?'**

*Ch 6 Try (prompt debugging, five broken — sample pass on #3 "continue"):* Diagnosis in PC-06 order: (1) *vague/buried*: "continue" has no object — continue *what* (scene? paragraph? outline?), to *what* length, ending *how*; (2) *contradiction check*: none found (nothing stated to contradict); (3) *context pressure*: the paste above "continue" was a full scene ending on an *unresolved beat* — context pulls for scene-continuation while my implicit want may have been *next-scene planning* — the chat will pick the stronger pull (its own demonstrated pattern), not my unspoken one; (4) *stacked tasks*: no. Single confirmed cause → v2 (one variable): "Using the pasted scene's ending beat, draft the NEXT scene's first 400 words — same POV (close third, Mara), past tense, ending mid-refusal — beats to hit: [two lines]. Scene prose only after 'SCENE:'." What to test first: the v2 output's *ending shape* — if it lands mid-refusal as instructed, the object+shape fix was sufficient; if it wanders, next single variable = add the anchor paragraph. The debug's *moral* in one line: **"continue" is not a prompt, it's a wish — the four forces turn wishes into tests.**

*Ch 7 Stretch (folder audit — sample findings against the anatomy table):* A realistic audit on our reader's `low-tide/` (post-Chapter-13 state): **present:** `00-inbox` (9 loose items — 3 untriaged older than a month: *flagged*), `bible/` (skeleton v3, sheets current, timeline through ch9 — *healthy*), `manuscript/` (`draft-03` + minted), `prompts/` (PC-01, PC-11, PC-20 instances with versions — *healthy*), `research/` (why-me file, venue dossier row — *healthy*), `cuts/` (populated — *healthy*: the graveyard being used means deletions are *filing*, per Ch 7's design), `log/session-log.md` (41 days, no gaps >2 — *healthy*), `log/changelog.md` (mint rows citing decisions ranges — *healthy*), `log/decisions.md` (67 rows, accept-rate 41% — *healthy*), `log/audit.md` (last entry two weeks ago — **flag: instrument exists, schedule lapsed**), `log/adr/` (**empty — flag: ADR-*001 (POV choice) never written**, the one instrument whose absence strands future-you on "why close third?"), backups: local-only, no second location (**flag: 3-2-1 violated — the draft's reversibility depends on one disk's mood**). Total: 5 findings, ranked — inbox-triage debt (small, aging), audit-schedule lapse (medium — *cause-row candidates: the Chapter-12 pass-5 crunch crowded it out*), ADR-001 gap (medium — write it from memory *today* while the choice's reasons are warm), 3-2-1 (high — the only finding whose failure mode is *catastrophic* rather than annoying), plus one *note-not-finding*: prompts/ has no PC-23 instance yet because beta-briefing hasn't started — *expected absence, watch-list only*. The audit's closing ritual, also sampled: **five findings → three calendar rows (inbox Friday 15 min; ADR-001 tonight; offsite copy + weekly-auto-sync setup Sunday) + one cause-row (audit lapse ↔ pass-crunch) + changelog line "folder audit 2026-09-XX: 5 findings, rows filed"** — twelve minutes total for a project's *structural* health, the ROI sentence this book keeps writing in different words.

*Ch 8 Try (premise stress-test — partial sample verdict for a generic four-part):* Premise: "A retired locksmith, failing eyesight forcing him from the trade he can still out-think anyone in, must crack his late wife's last commissioned safe — built by his rival — before the bank clears her estate in thirty days." PC-08's checks, abbreviated to what teaches: **Stakes finding:** cost-of-failure concrete and climbing (the safe = marriage's last *unshared* thing; thirty-day clock; eyesight as ticking *internal* cost — damage: *low*, repair: "none available" — flag: *develop-friendly*); **Novelty audit:** three predictables named — (a) he opens it, finds forgiveness letter (center), (b) rival helps at the end (forgiveness-teammate), (c) safe was empty all along (irony-classic) — mine-differentiator *asserted as*: the safe's *design* encodes the wife's own arguments with him (each lock stage = a recorded disagreement he must re-solve *her* way to advance — differentiator contingent on execution, marked *promising-not-proven*); **Why-me/why-now:** proxy fuel lines present (craft-pride arc, aging-and-legacy anxiety), why-now weak ("aging workforce" *general* — mark, don't kill: dated-newsfeed experiment recommended); **Capacity:** novel-length claim compatible with single-POV, present-timeline — no structural cost named; **Killer question (simulated first reader, verbatim-ish):** *"If the locks are that personal, why would she hire an outsider to make it?"* — **the question's value: it's *answerable* in-story (the rival-proof *is* the message — she wanted a safe he couldn't bypass alone), which converts it from fatal to *foundational*. Verdict: **DEVELOP** with two repairs logged (why-now dated-experiment; rival-hire answer sketched into the skeleton's stakes line) — note the verdict's *shape*: not vibes, not worship — five checks' rows, damage ratings, one kill-or-cure question resolved *on paper before the skeleton exists*. That's the stage working; your Try's verdict gets the same treatment: rows first, label last.

*Ch 9 Try (beat-to-change-line conversions — graded sample):* Activity-lines → change-lines, with the neighbor-test run explicitly: (a) "They argue about the boxes" → **"Mara's 'keep everything' instinct publicly costs Theo his moving-date — he begins selling furniture without telling her"** (neighbor-test ✓: next line must *use* that secret-selling — e.g., she finds the ad); the *grading notes* for your own ten: +1 for a real verb-shift (argue→costs), +1 for the shift *visible in the next line's material* (the test's actual criterion), 0 for cosmetic rephrasing ("deep argument about boxes" — same activity, harder word); (b) "He gives her the journal" → **"The journal's receipt puts Mara's flood-narrative in her hands — she now *knows* her own account is wrong and chooses silence anyway"** (knows-and-silences = the beat's *real* change; neighbor-pressure: the silence must *cost* something downstream or it's decoration); (c) "Storm warning arrives" → **"The formal warning converts 'sell soon' from anxiety into schedule — Casi's deadline pressure and the town's converge"** (map-change hiding in weather: the *calendar* is the character here — rungs move because *every timeline in the story just merged*). Ten lines graded this way, the clinic's output standard visible: **if your line doesn't name what the NEXT line must reckon with, it isn't finished being written** — the neighbor-test isn't a formality appended to the exercise; it *is* the exercise (everything before it was draft work).

*Ch 10 Try (mode selection — sample session plans):* Beat-pack: "Aurelia's café scene: she returns the tide-journal photocopy; Mara must ask about Theo's December visits without admitting she didn't know they happened." → **Plan A (dialogue-first):** locks: no tags beyond speaker-initial, subtext rule on (neither names Theo directly in first 8 exchanges), line-cap ≤8 words for Mara until the admission moment; rationale: scene's engine is *mutual concealment* — exchange-level craft IS the conflict; risk: interiority vacuum → closing beat opens POV for Mara's 3-line aftermath hand-typed. → **Plan B (co-draft):** anchor: the notebook-margin prose (Mara's inventory-voice); beats: 6 charge-verbs (returns→deflects→probes→flinches→half-admits→withdraws); locks: distance ≤3, banned constructions on, end-shape: Aurelia's exit non-answer; rationale: scene's *plot work* (journal-handoff mechanics) is clear — generation efficient, adjudication expected heavy on *subtext lines* (quips'-risk list pre-loaded). → **Plan C (hand-first first paragraph, then co-draft):** the hybrid our reader's mode-log would predict for *this writer* (Wednesday-pattern fatigue data — the log consulted *before* the choice, the pre-choice rule literally executed): type the first exchange cold to *set the rhythm* (hand-first's honest contribution), then expand under locks. Which is right depends on data the table keeps: **if last month's dialogue-first accept-rates ran high on confrontations → Plan A is *evidence-based*, not mood; if co-draft's subtext-hunting has been flagging → Plan B's risk is *known* and budgeted for; the point of plans-as-artifacts: each states its rationale in one line that Sunday's audit can score against what actually happened.** Five minutes of selection, three legitimate architectures of the same beats — versus the unselected default's one architecture, chosen by fatigue.

*Ch 11 Stretch (unearned-warmth audit — sample three rows):* Row 1: "Theo says 'I'm not angry — I get why you stayed away' *before* any pressure applied the claim" — **flagged:** forgiveness delivered at *zero cost* (his sheet's wound: the funeral-fortnight silence deserves *more* rungs before relief); redraft direction (not replacement text): move the concession *after* Mara performs the ask-he-can-refuse (cost-bearing first, warmth second — sequence *is* character). Row 2: "Aurelia volunteers her own immigrant-homestay story unprompted at first café meeting" — **flagged:** *unearned intimacy* + convenience-therapist smell (who benefits *narratively* from the disclosure at beat 2? — the plot needed Mara to trust her; the *character* didn't yet need to offer — fix the plot's need, not the person's generosity: the story can *extract* the trust-path another way). Row 3: "Every townsperson in scenes 4–6 answers Mara's questions helpfully and completely" — **flagged:** *cast-wide* warmth as *info-plumbing* (their kindness exists to feed her exposition — F-02's helpful-intern at population scale); direction: at least one answer *priced* (the information wants something — directions come with a question about the sale; the gossip's price is Mara's own business) — **kindness with an invoice is what people are; kindness without one is what drafts are.** The audit's score-sheet habit: three flags, all fixed by *sequence-and-cost* adjustments rather than making anyone meaner — the audit's target was never cruelty; it was *ease* — and the monthly re-run's job: confirming the next month's pages earned every warmth they show.

*Ch 12 Try (pass entry checklist — sample completed):* "**PRE-FLIGHT — STRUCTURE PASS (pass 1), batch: ch1–4:** [x] Draft minted (draft-07, completed) — forward-only confirmed, no unlogged edits since [x] Outline-current v-next frozen for batch scope — *waiver note pasted: ch2-midpoint adjacency waived-2026-09-XX (literary breathing — see decisions row 44)* [x] Changelog current through last session [x] Priors pasted: waivers from v3-PC-11 run + pass-0's two DEFERRED rows [x] Sessions scheduled as *fresh* — first block after a non-writing morning, caffeine per baseline note, *not* the post-bike 9 p.m. slot [x] PC-20 instance created with altitude line: 'structure altitude — defer style — critic reads reader-report only' [x] Batch discipline: full prose scenes for ch1–4, **ch5+ held back** (batch size fixed in *scenes*, not optimism) [x] Adjudication template open (5-row verdict vocabulary pre-loaded); row cap for session: 40 findings max — [x] Output routing: findings → triage table FIRST, zero direct edits to `draft-07` until mint-8 planned." — seventeen checks, eleven minutes to complete *including* the waiver grep, and what the completed list *demonstrates*: the checklist's boxes aren't overhead — **each one is a prior failure's entry-condition, paid forward** (the batch box remembers F-07; the fresh-session box remembers Ch 1's state-dependence; the waiver-paste box remembers the rat-chase finding — the pass system's real inventory isn't prompts and thresholds; it's *lessons you've already paid for, filed where you can't forget them*.)

*Ch 13 Try (beta briefing note — sample complete):* "Hi [Name] — thank you for reading *Low Tide*'s draft (attached, ~72k words — I know that's real time; no rush past our [date]). **What I need most, if you can only do one thing:** Question 1 on the sheet — your single biggest fix, ranked first even if you have other thoughts. **Wrong-and-specific is the gift:** the sheet's Q10 exists so you never soften for me — 'I put down ch6 at the marina scene; the brother was performing helpfulness again' would make my month more than any 'loved it!' **What this draft is trying to be** (so your answers aim at the *real* target): a close-third literary story about inheritance-choices, told on a two-week clock — where the *stakes ladder* must feel personal before it feels existential. **Stage declaration:** structural draft v3 — line-level perfection *not* expected, *not* wanted (Q2's skims are data, not insults). **The ten questions are the whole ask** — anything else you notice, write under Q10's box; address-free notes go to a *maybe* pile I'll triage, so don't self-censor them into silence. Deadline's soft: the *ranked-Q1* answer matters most; partial sheets welcomed if it's by [date]. If a question's confusing, that's my bug — mark it 'unclear' rather than forcing an answer. Genuine thanks — [signed]. **P.S.** The prose is allowed to be bad in places; *you* are not allowed to be kind about where it sags — Q2 wants the paragraph, not the apology." — annotated: stage declared (rank-1 framing), vision pack present (the target *description*), Q10's destruction-permission *explicit*, address-free-finding handling stated (triage, not pressure), confusion-as-my-bug (instrument-humility), and the P.S. doing the hardest work: **the briefing's real genre is *permission* — every line either grants a license (be wrong, be harsh, be partial) or supplies an aim (here's the target) — drafts of briefings that *only* supply aims read as assignments; briefings that *only* grant licenses read as vague; the sample's ratio is the standard: roughly half each.**

*Ch 14 Try (four-minute diagnostic — sample self-scan with counts):* Passage: 180 words of our reader's *own* weekend draft (mode-log: co-draft, Friday-11pm — *the fatigue signature's expected data*). Run: **H1 hedges:** "seemed to / perhaps / a bit / almost" ×6 in 180 words (threshold: ≤2 for close-third at this density — **flag, 4 over**); **H2 diction:** "commenced" ×1 (the *upgrade-itis* tell — baseline prose uses "started" ×3 this month: **flag, register mismatch vs. my own sheet**), "utilized" ×1 (same family); **H3 rhythm:** words/sentence 14.2 / 16.1 / 15.0 / 17.3 / 13.8 / 15.5 — *band tight* (personal range from baseline scan: 8–26 — **flag: narrow-band stretch, ~paragraphs 2–3**); **H4 reflection-tax:** three commentaries after completed action-scenes ("It was the kind of discovery that changes things" — the scene had *shown* the change; the line *taxes* what already landed) + one symmetry-pair ("both terrifying and freeing" — cut-one-side candidate) — **flag, 4 events**. Counts table written to `log/audit.md` (row dated, mode noted as Friday-co-draft), one fix *selected by severity* (H1: strip the four non-load-bearing hedges — the two doing genuine uncertainty-work stay, listed) — **four minutes, four numbers, one decision, one cause-row candidate that the mode-column already suspects.** The diagnostic's *discipline* made visible: it never asks "is this AI?" (unknowable, unproductive) — it asks **"how far from my own patterns, on my own metrics, and what's scheduled next?"** — a question answerable *every Friday* for the rest of your writing life.

*Ch 15 Try (policy hunt — sample row set):* Three rows as your dossier's format-target: `A · fiction mag · prohibitive · as-of 2026-09-21 · guidelines-PDF saved · note: prohibition text in §Originality; portal has affirmation checkbox (surface-3); route-around: removed from queue` · `B · small press · ask-first · as-of 2026-09-21 · silence on AI + originality warranty in contract-sample · email sent 09-21, reply 09-24 filed: disclosure-in-cover-note OK · statement: mid-length, vocab from their reply` · `C · regional contest · field+checkbox · as-of 2026-09-20 · §7 disclosure field (500 char) + portal checkbox + guidelines restatement · screenshots ×3 saved · statement: short-length filed with entry`. Grading notes for yours: every row carries *a date and an artifact-or-link* (undated = the row's worthless to future-you mid-queue); every posture comes from the venue's *own words* (forum-sourced posture = rewrite it); `route-around` rows kept *in* the dossier (prohibitions are *data* — the divergence-table Appendix E wants is built from your rows over time).

*Ch 16 Try (path-matrix — sample scoring, one reader's numbers):* Priorities first (this reader's three lines): "publish the collection within 18 months; keep series-control for the novel-future; learn the craft's business side without quitting the day job." Scores (1–5, their values, column-weights *unweighted* for simplicity — your version may weight): **Traditional:** timeline-tol 2 · control 2 · capital 5 · ops-appetite 4 · distribution 5 · feedback-rhythm 3 · rights 2 → **total 23**. **Indie:** timeline 5 · control 5 · capital 2 · ops 2 · distribution 2 · feedback 4 · rights 5 → **25**. **Serial:** timeline 5 · control 4 · capital 4 · ops 3 · distribution 3 · feedback 5 · rights 3 → **27**. **Small press:** timeline 3 · control 3 · capital 4 · ops 4 · distribution 4 · feedback 3 · rights 3 → **24**. *The two sentences:* "Gut says traditional — prestige for the collection matters to me emotionally." / "Numbers say serial, and *disturbingly* close between indie and small-press everywhere else." *The disagreement's diagnosis* (the real exercise): gut is scoring *signaling-value* (unlisted column — sneaked in); matrix is scoring *stated priorities* — and priority-1 ("within 18 months") is *actively hostile* to the traditional timeline (priority wasn't weighted; **the fix: re-score with priorities as weights — traditional likely drops further — then the honest question becomes: is 'prestige' a column I'd *add on purpose* or a *gut habit* I'm asked to defend in writing?** Either answer is legitimate — but only one arrives with a date: "add column 'signal-value' weight 0.5, re-run by [date]" — the matrix's whole point: *even your self-contradictions get scheduled like research questions.*

**Extra drills — 10-minute warm-ups by chapter:**

- *After Ch 1:* one prompt, five rejections, one acceptance — decisions rows for all six (taste reps, cold).
- *After Ch 2:* premise surgery on a subway-overheard sentence (four parts, 10 minutes, ugly OK).
- *After Ch 3:* flaw-pattern → three costed choices in table form (no prose — tables reveal chains faster).
- *After Ch 4:* "tell-to-show budget": take a 100-word summary; spend exactly 200 staged words only where import-test passes (learn *restraint in staging* as much as staging).
- *After Ch 5:* hallucination-of-the-day in lab notes (one fabricated quote, annotated by family).
- *After Ch 6:* prompt *diff*: v1 vs v2 of your scene-drafter, one variable, results noted (single-variable muscle).
- *After Ch 7:* reconstruct yesterday from logs alone, then check against the actual folder (instrumentation trust test).
- *After Ch 8:* parked-file mining: reread 10 one-liners, re-rate two itches (the long game, ten minutes).
- *After Ch 9:* convert three activity-lines to change-lines, neighbor-test them (the clinic, compressed).
- *After Ch 10:* mode roulette: one beat, two modes, five minutes each, log preference.
- *After Ch 11:* blind test on three exchanges, tags covered, aloud (the two-minute permanent habit).
- *After Ch 12:* k-of-n self-audit: this week's kept/rejected ratios vs. last week's (convergence weather report).
- *After Ch 13:* witness-form rewrite of one anxious question you actually asked a reader this month.
- *After Ch 14:* four-minute diagnostic on your *favorite* published book (symptoms in *good prose* — calibration: the checklist finds habits, not quality).
- *After Ch 15:* ten-minute policy hunt on a *real* venue (the dossier's first row).
- *After Ch 16:* matrix re-score with this month's numbers (envy-proofing, scheduled).

---

## Appendix C — Troubleshooting AI Failure Modes

**Purpose:** symptom → diagnosis → fix → prevention, one page max per failure. **Use it by symptom:** something's wrong in the draft/chat/project — find the *felt* problem here, then follow the cross-reference to the full chapter treatment. (Chapters own the *full* fix-stacks; this appendix is the index card taped to the monitor.)

**F-01 — Purple, generic description.** *Seen in:* Ch 10 (PC-16's home), Ch 12 line pass, Ch 14 diagnosis. *Symptom:* paragraphs arrive over-described in house register; weather indoors; one simile per clause; adjective accretion on every revision. *Diagnosis:* constraint poverty (no owned-detail spend in prompts) + revision-passes allowing growth (adjective-adding is the easiest completion). *Fix:* PC-16 at constant count (owned stays; generic gets *pressure-funded* replacements); Ch 12's generic-sensation sweep; banned-simile list in the style sheet. *Prevention:* Ch 4's ladder internalized (two questions: whose fingerprint? whose perception, why now?); PC-14 locks include banned constructions; count descriptives per paragraph in line passes (the number *is* the alarm).

**F-02 — All characters sound the same.** *Seen in:* Ch 11 (PC-18's home), Ch 10 (PC-15's swap-test), Ch 13 (betas' "everyone's nice"). *Symptom:* blind tests fail at confidence ≤3; speeches swap without meaning-change; cast converges on kind-quip-wounded (the helpful intern). *Diagnosis:* missing voice-notes in context packs + agreeable-average defaults + sheets written as dispositions not patterns. *Fix:* Ch 11's stack — flaw-first context, fingerprints (domain/syntax/habit/never-say) pasted, PC-18 blind test + hand rewrites of swap rows, unearned-warmth audit. *Prevention:* sheets before drafting; PC-15's tags-off format for relationship scenes; the two-minute aloud blind test weekly on dialogue-heavy chapters.

**F-03 — Draft contradicts the outline.** *Seen in:* Ch 9, Ch 12 (joint home). *Symptom:* outline says midpoint is a map-change; draft's midpoint is incident-only; or *inverse*: draft discovered better beats that never entered the document (silent drift). *Diagnosis:* two-rule stand missing — outline treated as either scripture (draft forced back into dead beats) or scribble (divergence unlogged); fix-echo (previous changes without changelog rows re-"discovered"). *Fix:* Ch 9's standing rule — draft's discovery beats outline's stale beat → *amend the document first* (v-next mint + reason), then the prose; Ch 12 pass 1's outline-vs-draft diff box does the *detection* mechanically; every amendment cites a decisions row. *Prevention:* freezing discipline (v-lines), per-mint syncs, waivers pasted into re-run contexts (so found-and-waived ≠ re-flagged), and *never* editing outline beats without a changelog line.

**F-04 — POV/tense drift mid-scene.** *Seen in:* Ch 10 (locks), Ch 12 (PC-22 table F), Ch 4 (root). *Symptom:* mid-paragraph camera jumps; past slides to present in machine regions; interior-access sentences for non-anchor characters. *Diagnosis:* soft locks (POV stated vaguely or far from generation) + unmarked machine paragraphs + Oracle-check backlog; *concentrated in machine-draft regions* is the signature (dictation/co-draft seams leak worst). *Fix:* PC-14 locks restated adjacent to task (anchor range, tense); marking discipline (doubt = machine); PC-22 category F + hand Oracle-fixes; retro-header on every document ("close third — NAME — past"). *Prevention:* POV decision procedure *written down* before Part III (Ch 4's four questions); header discipline; fresh eyes = the pronoun audit at every pass boundary (the brain patches continuity — the highlight reel doesn't).

**F-05 — Endless agreeable brainstorming, zero decisions.** *Seen in:* Ch 8 (root entry), feeding Ch 9/13. *Symptom:* forty chat exchanges, zero decisions rows; everything is "a great point"; premise tests wave through whatever you love; sessions end with mood, not verdicts. *Diagnosis:* sycophancy unframed — no adversarial roles, no damage ratings, no forced verdicts; selection happening *during* generation (contaminating both); multiple seeds per session diluting focus. *Fix:* PC-08's ordered checks + author-proxy (material to check *against*, not flattery to receive); explicit "no praise" frames; forced verdict vocabulary (DEVELOP/PARK/PARK-AND-STEAL or CHANGE/DISCUSSION/OVERRIDE…); *sessions without written verdicts don't count* (the session-log's Adjudications line empty = the session didn't happen). *Prevention:* one seed per session; generate-in-bulk/select-in-silence; the weekly adjudication audit counting zero-row sessions as the sycophancy signature.

**F-06 — Confident factual errors in historical/technical detail.** *Seen in:* Ch 5 (specimen gallery), Ch 12 externalized to research, Ch 15's type-split. *Symptom:* plausible citations, invented quotes, wrong period details, invented bible-rules, staleness mash-ups — all fluent, all uncaveated. *Diagnosis:* type-split failure (external claims run through internal-consistency machinery, or no machinery at all) + shape-pressure (demand-a-citation gets a citation) + shared-desk restatements drifting from the pasted extract. *Fix:* the gallery's families (citation, arithmetic, internal-confabulation, staleness) each have their counter (never cite unopened sources; recompute numbers; quotes-or-nothing vs. extract; dated questions → official dated pages); verification routing: internal → documents, external → primary sources, quotations → never machine-only. *Prevention:* lab-notes gallery grown personally; PC-22's uncertainty-rows; research mode (Ch 5's Stretch framing) for anything that will *touch the page* as fact.

**F-07 — Revision loops that never converge.** *Seen in:* Ch 12 (full entry). *Symptom:* `final-FINAL-v14` naming; the *same finding* recurring after fixes (not-new-findings = the tell); keep-rates not declining; vibe-done; revision feels like whack-a-mole with your own standards. *Diagnosis:* one of the four: passes entered illegally (fixes between altitudes); keep-rate >50% across two passes (early passes under-done — re-run pass 1, stop grinding pass 4); criteria never written (finish line moves with mood); adjudication abdicated at scale (400 unreviewed rows = default-accepts). *Fix:* diagnose which signature you have (the chapter's four-way table), then: restore entry conditions + paste prior waivers; re-run pass 1; freeze `done-criteria.md` today; chunk the batches to row-cap sizes. *Prevention:* one pass/one job/in order; inter-pass ritual (fix→mint→log→sync); k-of-n density notes; one human gate per cycle (new external input is the only legitimate circle-breaker when logs claim convergence).

**F-08 — Feedback triage paralysis.** *Seen in:* Ch 13 (full entry). *Symptom:* rows unverdicted >7 days; contradictory notes applied *both* ways (compromised mush); one loud reader colonizing the book; the table rotting as "still reviewing." *Diagnosis:* empty chair — vision pack (stakes + criteria + waivers) not written *before* intake, so any opinion fills the vacuum; no verdict vocabulary (binary do/not-do forces panic on four different problem-kinds); no clocks (addressless findings live forever); gratitude mixed into verdict-stages (soft re-contacts reopening closed rows). *Fix:* write the vision pack today; run PC-25 (candidates-only, merges banned); four verdicts + expiry dates enforced at session close; rank-1 arithmetic over loudness; thank-then-stop (one addressless-finding follow-up, deadline'd, then silence). *Prevention:* weekly audit counts unverdicted rows (instrument or it didn't happen); contradictions preserved as *pairs* through the vision check; the identity-check sentence memorized ("they testify, the table triages, vision disposes").

**F-09 — Voice erosion: draft sounds like "AI prose."** *Seen in:* Ch 14 (full entry), measured by Ch 7's monthly audit, *reported first by* Ch 13's residue-images. *Symptom:* quarterly the pages read like a competent stranger; diagnostic counts trending up; shuffle-test below done-criteria; you can't produce sheet-compliant prose *unaided* (the deepest sign). *Diagnosis:* the pull never turns off (drift is default-direction under incomplete layers) + fatigue-acceptance curve (your cause-rows cluster on tired days) + sheet staleness + comfort-diagnosis (running the check only on suspect chapters, not mode-log-named ones). *Fix:* five layers in drift order — upstream (functional-anchor test, regenerate worst stretch with beats+locks), measure (mandated sampling: machine-heaviest + self-suspected + baseline, counts recorded), surgery (PC-26 with sheet, flags, `[!mine]` set first, outline open, counts to thresholds, bounded exits), rebuild (rung-1 daily copies if unaided test fails hard), calendar (cause-session rows → pre-scheduled unaided sessions at those slots). *Prevention:* the 15-minute-per-scene stack (anchor → locks → mark → blind-test → weekly diagnose → sheet-bump at pass exits → quarterly baseline comparison as the *scheduling mechanism*).

**F-10 — Prompt works once, never again.** *Seen in:* Ch 6 (debugger's home), rooted in Ch 5's randomness + unversioned prompts. *Symptom:* the brilliant Tuesday prompt returns mush on Thursday; you re-roll hoping to re-find it; nothing was saved *about* what made Tuesday different (context? fill? mood?). *Diagnosis:* single-sample thinking (one draw from a distribution mistaken for the tool's property) + no version line (can't reproduce what wasn't specified) + invisible desk conditions (Tuesday's paste-included context did silent work; Thursday's empty desk didn't). *Fix:* three fresh runs to classify systematic-vs-draw; PC-06's four forces, one variable per edit; *promote on second-run evidence* (Ch 6's lifecycle — if it only ever worked Tuesday, it stays a context-labeled draft, not a card). *Prevention:* version lines everywhere; knobs marked (fills are inputs — document them); failure notes on cards; the card's `tested` date as the freshness contract; retired-cards autopsies accumulating the fragility-gradient knowledge (style-imitation cards: most update-fragile; schema-checks: least).

---

## Appendix D — Glossary

**Purpose:** every term of craft and AI the book uses, in plain language. Alphabetical; book-specific terms marked ★.

**Act** — the large divisions of a story's design (commonly three: set-up, confrontation, resolution); a *teaching compression* of structural observation, not a law (Ch 2).

**Adjudication ritual** ★ — the mandatory step after any critic pass: every finding gets kept/rejected/partial/deferred/waived *in writing* with a one-line reason before it touches a document (Ch 9, Ch 12).

**Anchor (voice anchor)** ★ — your hand-typed paragraph(s) placed in a draft *before* generation so machine text follows *your* rhythm; also the structural hinges where your paragraphs sit every third position (Ch 10). *See also* few-shot.

**Arc** — the shape of a character's change across a story: positive (gains the truth), negative (surrenders to the lie), flat (holds while the world changes) (Ch 3, Ch 11).

**Beat** — the smallest unit of change in a story outline: one line stating what shifts (want/cost/map-change), as opposed to what merely happens (Ch 9). *See also* scene.

**Beats (level-3)** — scene-internal micro-lines written session-close to drafting, feeding prompt FILL slots (Ch 7, Ch 9, Ch 10).

**Bible (story bible)** ★ — the project's long-term memory: skeleton, sheets, timeline, settings, rules, open threads, decisions pointers; the paste-source for bible-first prompting and the model's only sanctioned "truth" for internal checks (Ch 7, PC-22).

**Change-line** ★ — an outline entry phrased as a before→after shift, passing the neighbor-test (pressures the next line) (Ch 9's clinic).

**Changelog** ★ — one line per draft mint: state change, reason, row pointers; the project's structural memory and authorship-evidence trail (Ch 7, Ch 12).

**Close third** — third-person POV anchored to one character's perceptions per scene; free indirect style available inside it (Ch 4).

**Co-drafting** ★ — producing prose with the assistant (anchor → generate → adjudicate → revise), then treating it as your own *through* rewrite passes; one of five drafting modes (Ch 1, Ch 10).

**Composite** ★ — a scene built from multiple mode-runs, adjudicated row-by-row into one draft (Ch 10's three-ways lesson).

**Constraint** ★ — a checkable rule in a prompt (length, POV, banned constructions, end-shape); *constraints beat adjectives* — mood words converted to structure (Ch 6).

**Context window** — the maximum span of tokens (your prompt + pasted material + conversation) a model can consider at once; the shared desk whose edges silently drop old items (Ch 5).

**Continuity pass** — pass 5 of the pass system: bible-first batch checks across names, dates, props, rules, POV (Ch 12, PC-22).

**Crisis** — the story's worst-pressure decision point (distinct from midpoint); forced by accumulated costs, not coincidence (Ch 2, Ch 9).

**Cuts file** ★ — the addressed graveyard: every removed passage filed with date and origin, so deleting stops being loss and starts being filing (Ch 7).

**Decisions file** ★ — one row per substantive AI suggestion accepted/rejected with a one-line reason; the taste scorecard and authorship evidence since Chapter 1 (Ch 1).

**Developmental reader** ★ — PC-20's role: first-reader experience report (promises, pulses/sags with quotes, blind spots), not rewriting (Ch 12).

**Done criteria** ★ — the written completion tests signed *before* pass 1 (keep-rate thresholds, cold-read test, voice-ownability, zero open flags, beta gate), checked only at pass-5 exit (Ch 12).

**Draft (numbered)** ★ — a *complete* manuscript state (`draft-03`); forward-only integers; machine outputs never mint drafts (Ch 7).

**Drafting modes** ★ — dictate, co-draft, expand, rewrite, dialogue-first: five cost-structures for scenes whose decisions are already made (Ch 10's mode table).

**Few-shot prompting** — including examples of desired behavior; your own prose as example = voice anchoring at prompt level; examples outrank instructions (Ch 6).

**Fichtean curve** — crisis-forward structure (rising incidents → crisis → climax → falling action) as an alternative to gentle three-act set-up (Ch 2).

**Fill (parameterized card)** ★ — the marked variable slots in a template prompt (FILL-A context, FILL-B beats…); fills come from *documents*, never improvised under the chat's influence (Ch 6).

**Flat character** — built from one ortwo governing ideas, statable in a sentence; *not* a failure — cast architecture needs flats around rounds (Ch 3, Forster lineage).

**Flat arc** — protagonist's core holds while situation/cast transform around it (Ch 3).

**Free indirect style** — narration borrowing the character's diction without quotation marks; rungs 4–5 of the distance ladder (Ch 4).

**Golden rule** ★ — *You decide. AI proposes.* Governs every stage, altitude, and ledger (throughout).

**Hallucination (confabulation)** — fluent fabricated content (citations, quotes, details) produced by shape-completion without checking; zero self-announcement (Ch 5, Appendix C F-06).

**Helpful intern** ★ — the machine's default character: agreeable, competent, quip-wounded; the flattening problem's face (Ch 11).

**Heat (temperature)** — the sampling knob trading conservatism for variety; same prompt ≠ same answer across runs (Ch 5).

**Instruction-following** — the model's ability to condition on your role/task/constraints; instructions are tokens, pressures not commandments (Ch 5, Ch 6).

**Kishōtenketsu** — four-part structure (introduction, elaboration, turn, reconciliation) with roots in Chinese/Japanese literary tradition; reframing over conflict as central engine (Ch 2).

**Keep-rate** ★ — kept-findings ÷ total-findings across passes; the convergence metric (<30% signals done; non-declining signals F-07) (Ch 12).

**Level-2 outline** ★ — chapter/sequence change-lines, frozen after critique; the workhorse granularity (Ch 9).

**Logline** ★ — one sentence carrying protagonist + goal + obstacle + cost + tonal signal; refined from *your* draft, with omissions named (Ch 8, PC-09).

**Marking discipline** ★ — tagging every machine-origin sentence at acceptance time (doubt = machine); clusters-at-turns as the anchor health-check (Ch 10).

**Midpoint** — the halfway turn that must be a *map-change* (options/leverage shift), not merely an incident (Ch 9).

**Mode log** ★ — the session-log column recording which drafting mode each scene used; Ch 14's audit reads it (Ch 7, Ch 10).

**Negative arc** — the character's fall: coherent, costed, warning-shaped (Ch 3).

**Negative constraint** — a "must not" in a prompt; pair with a replacement (prohibition-plus-shape) or the prior fills the vacuum (Ch 6).

**Novelty check** — PC-08's test: name the three predictable versions; *assert* your differentiation (novelty claims are author-assertions audited against the distribution) (Ch 8).

**One pass, one job** ★ — the revision law: single-purpose attention, ordered altitudes, entry/exit conditions (Ch 12).

**Outline worship** — treating beats as scripture (forcing discoveries back) *or* scribble (silent drift); both violate the two-rule stand (Ch 9, F-03).

**Overridden reader (OVERRIDE-READER)** ★ — verdict vocabulary: critic's finding disagreed with your aims; you sided with the skeleton, row preserved (Ch 12).

**Pace / pacing checker** — tempo as space × pressure-type × rung rhythm; PC-12 flags, doesn't prescribe (Ch 9).

**Pass system** ★ — structure → character → scene → line → continuity, one pass one job, mints between, checklists as gates (Ch 12).

**Perishable claim** ★ — a fact-capability-figure that rots (dates, policies, benchmarks); dated, re-verified pre-publication or cut (research protocol, Appendix E).

**Pitfall (callout)** — symptom → why → fix → prevention, cross-referenced to Appendix C (style guide).

**POV (point of view)** — whose consciousness delivers the story: first, close third, omniscient; decided per scene, locked by header + audits (Ch 4).

**Premise** ★ — protagonist + goal + obstacle + stakes; the cost-of-failure sentence is the test; an *idea* names a possibility, a premise states a conflict (Ch 2).

**Prompt chain** ★ — multi-step prompt pipeline (extract → judge → transform…) with inspectable outputs per link; failures localize (Ch 6's five patterns).

**Prompt debugger** ★ — PC-06: four forces, three-run classification, one-variable edits, version bumps; debug instead of gamble (Ch 5, Ch 6, F-10).

**Prompt card** ★ — a reusable, versioned, knob-marked prompt with ID, `tested` date, and failure note; the library format (Ch 6, Appendix A).

**Psychic distance** — depth of access into the character's mind on a ladder (outside observation → raw idiom); distance by design, not always deep (Ch 4).

**Race-conditions note:** *n/a* —

**Reversibility** ★ — the property every log buys: any pass or mode's changes restorable via draft numbers + rows; transforms are revisions too (Ch 7, Ch 10, Ch 12).

**Sequel beats** — scene → reaction → dilemma → decision: the interiority cycle scenes compress by choice (Ch 4).

**Sensory overload as substitute** — repeated generic sensation (heart pounding ×12) = telling in costume; specific or cut (Ch 4).

**Scene** ★ — goal + conflict + outcome; the unit where readers lean in or shop (Ch 4).

**Sycophancy** — the agreeable-mirror tendency (agreement, reframing, softened critiques); defeated by adversarial frames, proxies, verdicts (Ch 5, F-05).

**Stakes ladder** ★ — personal → relational → existential; "and then who else pays?"; specificity over pyrotechnics (Ch 2).

**Style sheet** ★ — the living instrument: diction-class range, rhythm note, dated bans with evidence-lines, KEEP features with provenance, figure budget; read at pass entry, bumped at exit (Ch 14).

**Taste** ★ — the ability to prefer the right risk; the human selection function the machine structurally lacks; built by unaided baselines + decision rows (Ch 1, throughout).

**Temperature** — *see* heat.

**Testimony vs. evaluation** ★ — feedback design principle: harvest *events in reading* (location + memory), not moods; readers are reliable witnesses to themselves (Ch 13).

**Token** — the subword unit models read/write; the context window's currency (Ch 5).

**Unearned warmth** ★ — a character being kinder/wiser than their sheet licenses under pressure; the monthly audit's quarry (Ch 11).

**Voice** ★ — stylistic choices made *consistently under pressure*; cataloged as three-to-five defended named features (Ch 14). *See also* voice anchor.

**Voice drift audit** ★ — monthly shuffle-test: can you tell your paragraphs from machine ones *unlabeled*? (Ch 7, Ch 12, Ch 14).

**Voice erosion (F-09)** ★ — gradual convergence on AI-default across sessions; default-direction under incomplete layers; five-layer fix (Ch 14, Appendix C).

**Vision pack** ★ — the pre-intake page (stakes + criteria headline + waivers + bans) pasted at the top of every triage session; the chair you sit in while readers speak (Ch 13).

**Want vs. need** ★ — external checkable pursuit vs. internal healing requirement; different verbs or you have two wants; climax forces the trade (Ch 3).

**Wound** — the history that made a flaw adaptive once; dosed on the outline's schedule, never dumped (Ch 3).

**Working memory (of the model)** — *see* context window.

**You decide, AI proposes** — *see* Golden rule. The book's last word before yours.

**Accept-rate** ★ — kept-findings ÷ total-findings across a pass or mode (taste's running percentage; creeping-high = F-07/the composite-creep; used per-mode in Ch 14's audit) (Ch 12, Ch 14).

**Adjectives over** — the inverse of mood-word prompting: converting vibes into checkable constraints; the Ch 6 fix for adjective-heavy briefs (Ch 6).

**Altitude** ★ — the layer a pass or critique is working at (structure / scene / line / continuity); "altitude noted" prevents style-reports during structure passes (Ch 12).

**Amend (outline)** ★ — mid-draft outline repair: discovery beats a stale line → document first, mint, then prose; never silent divergence (Ch 9, F-03).

**Artifact** ★ — a saved, dated piece of evidence (policy PDF, screenshot, vendor quote); the dossier's currency in Ch 15 and the protocol's evidence chain (research protocol, Ch 15).

**Banned list** ★ — the style sheet's dated prohibitions with evidence-lines ("commenced ×2, 2026-09"); read at pass entry, bumped at pass exit (Ch 14, PC-21).

**Batch discipline** ★ — critic passes run on fixed-size batches (2–3 chapters for PC-22; full scenes for PC-20), never "however much fits" (Ch 12).

**Bible pack** ★ — the per-prompt paste assembled from the bible (relevant sheets, rules, names, stakes line); the input half of bible-first prompting (Ch 7, PC-14).

**Cognitive-load rules** ★ — one-character-to-track, clear pronouns, names matter: casting/drafting constraints that keep readers oriented (Ch 4, Ch 11).

**Cold reader** ★ — external fresh-eyes input; the only legitimate circle-breaker when logs claim convergence (one per cycle) (Ch 12, Ch 13).

**Composite verdict** ★ — feedback triage's four-row vocabulary: CHANGE / DISCUSS / OVERRIDE / FIX-THE-QUESTION (Ch 13, PC-25).

**Constraint bank** ★ — a project's accumulated reusable constraints (banned constructions, scene types tried, genre-marks); feeds prompts and prevents re-inventing limits (Ch 6, Ch 8).

**Context pressure** ★ — how pasted material outvotes instructions ("explain like a lawyer" after a legal memo); Ch 5's four forces, one of (Ch 5, PC-06).

**Diary trap** ★ — interiority that recaps events instead of reacting to them; a scene-pass finding class (Ch 4, Ch 12).

**Draft-current** ★ — the active manuscript file; machine outputs never write it directly — promotion happens through mint + adjudication (Ch 7).

**Entry conditions** ★ — the fixed checklist to START a pass or drafting session (fresh session, minted draft, waivers pasted, batch size fixed) (Ch 12, Part III opener).

**Exit conditions** ★ — what must be true to LEAVE a pass (checklist rows cleared, next-step logged, mint planned) — the anti-"walked away mid-pass" rule (Ch 12).

**Fictionalize-or-don't** ★ — Ch 5's rule for sensitive real material: transform load-bearing specifics beyond recognition, or don't use it (privacy at paste-time) (Ch 5, Ch 15).

**Fill-only edit** ★ — prompt change that alters variables without changing structure (no version bump); contrast structure edits (Ch 6).

**Finding** ★ — one critic-pass output unit: quote + issue + suggested direction (damage-rated in PC-11/PC-08); findings get adjudicated rows, never auto-applied (Ch 9, Ch 12).

**First reader** ★ — the developmental reader's stance (experience the draft, report pulses/sags); distinct from editor-who-rewrites (PC-20).

**Fixed point** ★ — an anchor element locked across modes/passages (character's speech habit, a spellings set); the composite's glue when merging multi-mode outputs (Ch 10).

**Function-role (coat)** ★ — cast member existing to perform one plot job; flagged in the cast charter so coats don't accidentally grow (Ch 3, casting section).

**Golden-rule audit** ★ — session-end check: who decided what — decisions file row count vs. suggestions accepted silently (the rule's instrumented form) (Ch 1, Ch 7).

**Hedge-strip** ★ — PC-26's H1: removing non-load-bearing softeners while keeping genuine uncertainty markers (Ch 14).

**House register** ★ — the AI-default prose style (polished generic); Ch 4's sensory-overload and Ch 14's diagnostics target it (Ch 4, Ch 14).

**Imagined-ness standard** ★ — "things as they might be imagined" (Lennon lineage) as fiction's permission scope: the model may complete *types*; specifics need sources or labels (Ch 5).

**Instrument** ★ — any tool/row/log that produces observable data on your practice (as opposed to advice); "instrument or it didn't happen" (throughout).

**Iteration tax** ★ — cost of re-prompting/re-rolling when variables stack; why single-variable edits and version lines exist (Ch 5, Ch 6).

**Judge-after generation** ★ — the split discipline: generate in volume, select/adjudicate in a separate pass (selection contaminates generation otherwise) (Ch 8).

**Keep-list** ★ — the style sheet's protected features (fingerprints, [!mine], defendable tics with provenance) (Ch 14, PC-21).

**List price minus** ★ — indie path's margin arithmetic: price − platform share − ads − services; run before committing (Ch 16).

**Location + memory** ★ — beta-question design standard: findings answerable with a place in the text and the reader's recall (Ch 13, PC-23).

**Machine-origin mark** ★ — marginal note tagging provenance of a passage at acceptance (doubt = machine); feeds audits and Appendix F (Ch 10).

**Map-change** ★ — a change in what the protagonist *knows/options/can afford* (as opposed to mere incident); the midpoint's required species (Ch 9).

**Marked wear** ★ — deliberate style-sheeted tics kept as voice evidence; distinguished from accidents (Ch 14).

**Mint** ★ — creating the next numbered draft after a pass/cycle; machine suggestions mint nothing — adjudicated edits do (Ch 7, Ch 12).

**Mode-experiment** ★ — a scheduled scene drafted in an unused mode to break monoculture or confirm a chosen one (Ch 10, mode-log patterns).

**Never-say list** ★ — character-level speech bans (each cast voice's "would never say"); feeds PC-15 and PC-18 tests (Ch 3, Ch 11).

**One-vote scale** ★ — casting rule: named recurring characters don't get "extra" personality because you like them — sheet fields govern (Ch 3).

**Open flags** ★ — pass-log items awaiting decision; the input PC-23 converts into beta questions (Ch 12, Ch 13).

**Over-earn** ★ — warmth/turns delivered before their cost has been paid on-page; the unearned-warmth audit's opposite failure when *everything* is delayed (balance note in Ch 11).

**Pace-violation** ★ — a beat whose pressure-type sequence breaks the scene's promised tempo (PC-12 flags; adjudicated, not auto-fixed) (Ch 9).

**Permission lines** ★ — briefing/self-talk sentences that license hardness ("wrong-and-specific is a gift"); the beta-briefing genre's core move (Ch 13).

**Plateau** ★ — accept-rate stability without quality movement; distinguished from convergence (needs baseline comparison to diagnose) (Ch 14).

**Pre-mortem** ★ — imagining the project's future failure to surface capacity/structural risks early; PC-08's stakes-adjacent habit (Ch 8).

**Pressure-type** ★ — scene/beat classification: pursuit / refusal / revelation / reaction / transition; the tempo table's rows (Ch 9, PC-12).

**Print source** ★ — document built by stripping HTML comments + research notes for print (the build script's job) (style guide, build).

**Process map** ★ — your logged workflow described in categories (modes, passes, human-review points); input to contract conversations and long-form disclosure (Ch 15).

**Prose-block session-log** ★ — a session record written as prose instead of fields; the Ch 7 failure mode (can't be grepped) (Ch 7).

**Protection order** ★ — discovery order during editing from *most to least reversible* (comments → line → structure) — so damage stays cheap (Ch 12).

**Pulse / sag** ★ — reader-reported energy peaks and skims with paragraph addresses; PC-20's core experiential data (Ch 12).

**Query-before-submit** ★ — the written-ask rule: venue silence → one specific email → conservative disclosure if unanswered (Ch 15).

**Quoted-or-cut** ★ — external claims either carry a source+date or don't ship; the protocol's first sentence (research protocol, Appendix E).

**Rank-1 finding** ★ — the single biggest-fix answer a beta provides; the briefing's most-weighted question (Ch 13, PC-23).

**Re-rate (itch)** ★ — monthly conscious re-evaluation of parked premises' pull; prevents auto-resurrection (Ch 7, Ch 8).

**Recession rule** ★ — editing order *away from* the climax's most sensitive material first? No — the protection order's corollary: leave the climax's load-bearing paragraphs until last within a pass (Ch 12).

**Refusal-first scene** ★ — scene shape where the protagonist's "no" opens the conflict (counter to goal-first defaults); a useful beat variant (Ch 4, Ch 9).

**Registry of rejections** ★ — the decisions file's rejected-suggestion rows; the taste-rep scorecard's other half (Ch 1).

**Relevance filter** ★ — paste discipline: only material that *bears on the task* enters context (context window's scarcity respected) (Ch 5, Ch 6).

**Release checklist** ★ — pre-publication gate combining all chapters' boxes + provenance + build validation (Ch 16's checklists extend it) (Ch 16).

**Repair (premise)** ★ — a concrete change a stress-test assigns before DEVELOP; logged with the verdict, verified in the skeleton (PC-08).

**Retire (card)** ★ — end of a prompt card's life with a written autopsy (why it stopped working) feeding fragility knowledge (Ch 6).

**Reversion clause** ★ — contract term returning rights on out-of-print/sales triggers; small-press contract-craft 101 (Ch 15, Ch 16).

**Rung** ★ — a stakes-ladder level (personal/relational/existential); "rung moved?" is the beat audit's unit (Ch 2, PC-11).

**Scene contract** ★ — the promise a scene's opening makes (goal, stakes species, distance) that its ending must honor or deliberately break (Ch 4, Ch 12).

**Scene-pass queue** ★ — the list of kept outline lines undelivered in prose (the two-way sync's backlog row) (Ch 9 maintenance section).

**Screen-time check** ★ — casting arithmetic: every new named character costs memory-acts; merge jobs before making names (Ch 3, casting).

**Scripted feel** ★ — dialogue that performs plot-purposes without subtext residue; the quip-treadmill's downstream symptom (Ch 11).

**Sealed build** ★ — final print stage: comments/research stripped, counts verified, outputs regenerated — no live edits during assembly (style guide, build).

**Section-heat map** ★ — pass-log visualization: findings clustered by chapter/section revealing structural hotspots (Ch 12's instruments).

**Selection contamination** ★ — judging while generating (filtering drafts mid-flow); defeated by generate-then-adjudicate splits (Ch 8).

**Self-test rows** ★ — your own blind checks (shuffle-test, unaided drafts) logged like any instrument reading (Ch 7, Ch 14).

**Sentence-hand-feel** ★ — typing your own prose by hand to re-internalize rhythm; the voice-ladder's acquisition rung remains human work (Ch 14).

**Shared desk** ★ — Ch 5's context-window metaphor (items fall off its edge silently); the paste-discipline rationale (Ch 5).

**Sizing tools** ★ — the drills/checks/entry-conditions collectively: instruments that match project costs to real capacity (Ch 2's funnels, closing).

**Slope check** ★ — longitudinal audit: comparing metric *trajectories* (accept-rate over months) instead of snapshots (Ch 7, Ch 14).

**Spec sheet** ★ — a platform/vendor's official format requirements; the "official source" tier for production artifacts (Ch 16).

**Stakes-with-binding** ★ — the four-part's stakes field done right: cost + the reason she can't just leave (Ch 2's drills).

**Stage declaration** ★ — telling beta readers what draft-stage the work is at (structure vs. line) so feedback aims correctly (Ch 13).

**Story-shaped filter** ★ — judging completions for *fit to your aims* rather than fluency; the taste muscle's daily rep (Ch 1).

**Structural finding** ★ — a critique item about promises/causality/architecture (vs. style findings); the altitude label that keeps passes honest (Ch 12).

**Swap test (stakes)** ★ — paste your stakes sentence over another story's premise; if it fits untouched, it's template stakes (Ch 2's drills).

**Swap-violation** ★ — a dialogue line either cast member could say; PC-18's list unit (Ch 11).

**Table-first feedback** ★ — feedback routes through the triage table before touching draft or feelings (the F-08 fix's first move) (Ch 13).

**Tax-line** ★ — a reflection-tax sentence (commentary after the scene already performed); PC-26's H4 target (Ch 14).

**Terminal pass** ★ — the last pass (5) before done-criteria exit; its checklist clears zero-open-flags (Ch 12).

**Three-length statement** ★ — disclosure drafted at short/mid/long granularity, factually mapped to logs (checkbox/cover-note/contract) (Ch 15).

**Time-box** ★ — a session's fixed duration with logged goal; the session-log's unit (Ch 7).

**Tool-note (dated)** ★ — a side record of which model/tool produced a result and when; the `tested`-date's project-level sibling (Ch 6, Appendix F).

**Transition-heavy** ★ — tempo diagnosis: too many transition rows in a beat table (sag precursor) (PC-12).

**Two-question attribution** ★ — before judging any model reply: "whose aim does it serve? which type-split is it?" (Ch 5's habit, compressed).

**Unaided baseline** ★ — your no-assistance sample (200 words, timed); the voice audit's comparison line (Ch 1, Ch 14).

**Unreliable praise filter** ★ — treating generic positivity as noise (sycophancy or kindness), not signal (Ch 5, Ch 13).

**Usage-star** ★ — why-me file entries that recur across tests get starred; your thematic gravity's empirical map (Ch 3's fuel section).

**Vocabulary-lock** ★ — established in-story terms that later sessions must match exactly (the bible's glossary slice for prompts) (Ch 7).

**Waiver** ★ — a written decision to keep a flagged defect for craft reasons; pasted into future critic contexts to stop re-flagging (Ch 9, Ch 12).

**Warmth invoice** ★ — kindness priced on-page (help comes with a request); the unearned-warmth fix's economy (Ch 11).

**Watercooler line** ★ — dialogue that exists for realism而非plot; capped by the scene contract's subtext rules (Ch 4, Ch 11).

**Week-one gate** ★ — Ch 16's plan rule: calendar blocks for week 1 exist before the plan counts as real (Ch 16).

**Where-I-looked** ★ — research notes' source pointers (protocol rows); the claim register's evidence column pattern (research protocol, Appendix E).

**Window-of-attention** ★ — the ~5±2 chunk budget readers hold in-scene (Ch 4's cognitive-load rules, canonical number hedged as teaching approximation).

**Word-delta** ★ — session's net words entered into draft-current; the only word metric the logs count (Ch 7).

**Working-sentence** ★ — the draft logline you steer by (post-repair, never premature) (Ch 8).

**Wrong-and-specific** ★ — the quality of feedback to aim for; the briefing permission line's target (Ch 13).

**Zero-row session** ★ — a session whose adjudication line is empty; the sycophancy/drift audit's alarm row (Ch 7, F-05).

---

## Appendix E — Research Notes & Sources

**Purpose:** the printed tip of `research/claim-register.md` — what the book asserts, how confident we are, and where to check. Full register (with evidence rows, confidence, counter-evidence notes) lives in the repository's `research/` directory; this appendix is the reader-facing summary. **Standing policy:** official/primary sources outrank everything; every figure keeps units/population/date or gets cut; perishables re-verified pre-publication; AI may help *decompose* research but is never a source.

**Per-chapter source notes (the claims that reach the reader):**

- **Ch 1 (productivity figures):** C005 — Noy & Zhang, *Science* 381(6654), 2023 (doi:10.1126/science.adh2586): n=453, ~40% time reduction, +18% judged quality on mid-level professional writing tasks. C006 — Brynjolfsson, Li & Raymond: NBER WP 31161 (2023); published *QJE* 140(2):889–942 (2025): n=5,179 support agents, +14% issues/hour average, ~+34% novice/low-skilled, minimal effect on highly experienced — *explicitly framed as not generalizable to fiction*. Confidence: high (original studies); scope hedges printed in-text.
- **Ch 2–4, 9, 14 (craft terminology):** C004 — consensus craft teaching attributed to its popularizing sources (Field, *The Screenplay*; McKee, *Story*; Swain, *Techniques of the Selling Writer*; Forster, *Aspects of the Novel*; Diamond's Fichtean curve; kishōtenketsu's literary-historical account) with contested points *labeled as opinion* (act ratios, head-hopping, arcs-as-design). Confidence: medium-high as *consensus summary*; minority views noted in-text.
- **Ch 5, 10, 11, 14 (mechanism claims about models):** C002 — next-token prediction, sampling/temperature, context-window mechanics, in-context learning/recency, sycophancy-as-tendency, regression-to-typical cadence: standard descriptions per provider docs and public technical literature, framed as *correct-enough mental model*, mechanisms not benchmarks; **no capability figures printed** (perishability policy). Confidence: high for mechanisms; all future figures require source+date or stay out.
- **Ch 5 (replication anecdote, if used):** C008 — Open Science Collaboration, *Science* 349:aac4716 (2015): 97% of original studies statistically significant vs. 36% of replications; replication effects ~half the originals' magnitude; scope limits (psychology,100 studies) kept attached. Confidence: high (original); used only with scope.
- **Ch 13 (AI feedback quality):** C009 — *no positive quality claim ships*: limit-claims only ("no independent evidential weight"; persona bias mechanisms), hedged per policy; any future positive claim needs its own verified source.
- **Ch 15 (law/policy):** C001 — US human-authorship baseline: US Copyright Office registration guidance (2023), Part 2 report (released 2025-01-29), *Thaler v. Perlmutter* (D.C. Cir. 2025) — official/court sources; framed information-not-advice. C003 — venue-policy divergence: Clarkesworld's then-prohibition + Feb 2023 submission closure vs. other markets' tool-neutral positions (reported Feb 2023 — WaPo/Vice/Metastellar) as *dated historical evidence of divergence, not current permission* — re-harvest per venue pre-submission. C007 — Brazil: LGPD Lei 13.709/2018 official text (Planalto; D.O.U. 2018-08-15) — *narrowly* privacy-of-process; all other BR AI/copyright questions pointer-only to official trackers + counsel.
- **Ch 16 (market figures):** C010 — standing prohibition-row: **no market/cost/timeline figures printed**; order-of-magnitude hedges flagged "verify dated at your moment"; survivorship bias named as mechanism.

**Perishables table (re-verify pre-publication — first edition cut-off to be set at revision sign-off):**

| Claim/figure | Value as printed | As-of | Where to re-check |
|---|---|---|---|
| C005/C006 figures | 40%/18%; 14%/34% | studies dated 2023/2025 | original papers (links above) — stable as *study results*; framing sentences re-read for scope-creep |
| C001 copyright guidance | as summarized | verified 2026-09-23 | copyright.gov AI guidance/report pages + court opinions at use |
| C003 venue policies | divergence evidence (2023) | 2023 reports | each venue's own guidelines page, dated at *your* submission |
| C007 LGPD | in-force, scope-narrow | 2026-09-23 | Planalto consolidated text; ANPD for regulatory updates |
| Card `tested` dates | 2026-09 | monthly-era | re-run at tool switch; bump cards on failure-note changes |
| Capability descriptions (no figures) | mechanisms only | 2026-09-23 | provider docs if any technique's dependency changes |
| Any future figure | *none printed* | — | register row + source+date before it ships |

**What was NOT verified, and why (the honesty section):** (1) *No market-size, advance, or royalty statistics* — volatile, survivorship-contaminated, and unnecessary for the trade-off *structures* Ch 16 prints (cut, not sourced). (2) *No model benchmarks or context-window numbers* — perishable by design; consequences taught instead (C002's policy). (3) *No jurisdiction's law stated from memory* — every legal sentence traces to an official source or is pointer-only with a counsel-trigger (UK/EU/BR boxes deliberately narrow). (4) *No claim that simulated feedback "works"* — limit-claims only (C009's hedge-or-cut followed literally). (5) *Detector accuracy claims* — out of scope entirely (unstable literature, low decision-value for this book's readers). (6) *Named-product capability promises* — generic-first policy; dated tool-notes belong to a companion site, not this manuscript. **The pattern behind the six cuts:** anything that would be *load-bearing* only as a *number* got either an official source or a deletion; anything *load-bearing as advice* got mechanism-level framing that survives rot. When in doubt at re-verification time: hedge, date-stamp, or cut — the protocol's first sentence, printed here as the appendix's last.

### How to read a register row (the reader-facing walkthrough)

The full register lives in `research/claim-register.md`; its columns deserve one worked reading, because *rows are how this book's honesty stays inspectable* — take C001 as the specimen (rows abbreviated to print width; the repository file carries the full evidence notes):

```text
| ID   | Claim (compressed)                    | Chapter | Status | Confidence |
|------|---------------------------------------|---------|--------|------------|
| C001 | US: copyright requires human authorship;
      | purely AI-generated material uncopyrightable;
      | AI portions disclosed on registration; mixed works
      | protectable as to human authorship; prompts alone
      | insufficient for control                | 1, 15  | verified
      | 2026-09-23 | high — official USCO guidance +
      | report + appellate decision            |
```

*Reading it in five moves:* **(1) The compressed claim is the *scope*** — read only what the row *says*; the chapter's prose may hedge further (it does: "information, not advice"), but the row is the *floor* of what's being asserted — if prose ever exceeds row scope, *the prose is wrong*, which is exactly what pre-publication verification checks for; **(2) Status carries a date** — "verified" without a date would be *rot in waiting* — the date is when a human last opened the official source; anything older than the edition's perishables schedule gets re-opened or the claim downgrades to "stale — re-verify" *by the build's checklist*, not by memory; **(3) Confidence names its basis** — "high — official sources" versus "medium — consensus summary" (C004) versus "hedged — limit-claims only" (C009): the *basis phrase* tells you what kind of counter-evidence would *demote* it (a superseding USCO page; a survey overturning consensus; a future study on feedback quality) — confidence without basis is just a mood with a label; **(4) The counter-evidence note lives in the register, not only the prose** — protocol §4's rule (log disconfirming findings, don't bury them): C008's row carries the "low-power-originals may explain part of the gap" debate *inside the row*, so a future edition can *strengthen* the hedge without rediscovering the literature; **(5) New claims arrive as new rows, old rows never rewritten** — append-only discipline means the *history* of what you believed and when survives editing passes (the register's structure mirrors the changelog's: corrections *add*, they don't *silently edit* — a research record that loses its past can't audit *itself*, which is the whole point of having one). **Using rows while drafting:** when a chapter draft contains a checkable fact, the workflow is one line long — *find the row or create it provisional → source opened by a human → status+date filled → prose hedged to row scope* — and when no source exists: the row's status becomes `cut — no source` and the sentence leaves the manuscript *that same session* (the protocol's loop closed at drafting-time rather than discovered at revision, which is how a 16-chapter book ends up with a perishables table this short: most candidates died *at the row stage*, one append-away from becoming a liability. Your own projects need no more than this: a table, five columns, append-only honesty, and the sentence every row encodes — **what do I believe, why, when did I last check, and what would change my mind.**

---

## Appendix F — This Book's AI-Use Log

**Purpose:** practice what we preach — a transparent log of AI assistance in producing this book. **Rule (from the style guide):** no AI-drafted passage ships without human revision and a logged review. The log itself is the book's argument for transparency norms (Ch 15's provenance stance, aimed at ourselves). **Columns:** date · chapter/section · tool (generic role) · task · human review (who, what changed) · notes.

**Format note:** "Tool" entries name *roles* (research-assistant, structural-critic, drafting-partner), not brands — per the generic-first policy; the repository's full log (with timestamps) accompanies this print summary.

| Date | Section | Tool role | Task | Human review | Notes |
|---|---|---|---|---|---|
| 2026-09-22 | outline, scaffolds, style guide, research protocol | ideation partner + editor | editorial structure: outline, chapter scaffolds, claim-register skeleton | project owner: restructured word budget, rewrote open-decisions list | scaffold stage only — no manuscript prose |
| 2026-09-22/23 | claim-register C001–C008 | research assistant | draft search terms; triage candidate sources | researcher: primary sources opened and read; rows filled with evidence+dates | AI never cited as source (protocol §9) |
| 2026-09-23 | front matter (preface, how-to-use) | drafting partner | section drafts from owner's bullet outlines | owner: full revision pass; honesty-markers section added; promises audited against book's actual contents | voice second-person standard applied |
| 2026-09-23 | Ch 1–4 (Part I) | drafting partner + structural critic | prose drafts against scaffolds; objectives/checklist alignment | owner: craft pass on all worked examples; Example A canon fixed (Mara/Theo/Porto Alvaro); unaided-baseline exercise verified against Ch 14's reuse | C004 attributions added at research-notes stage |
| 2026-09-23 | Ch 5–7 (Part II) | drafting partner; research assistant (privacy framing) | mechanism prose; card drafting PC-01…06; folder/log templates | owner: perishability policy enforced (figures cut); four-force field guide merged from two drafts; template fields tested against Example A setup | no capability numbers shipped |
| 2026-09-23 | Ch 8–13 (Part III) | drafting partner; critic-personas under owner's cards | workflow prose; Example A transcripts *reconstructed under the book's own card formats*; PC-07…25 | owner: adjudication rows verified against examples' internal consistency; transcript abridgments checked to never remove illustrated failures; C009 hedge written | transcripts labeled abridged/representative per style guide |
| 2026-09-23 | Ch 14–16 (Part IV) | drafting partner; legal-triage assistant (sources only) | voice/ethics/career prose; jurisdiction boxes | owner: legal sentences restricted to official-source statements (scope warning kept printed); market figures *removed* (C010 prohibition); closing letter substantially rewritten by hand | Ch 15 rows re-checked against register same-day |
| 2026-09-23 | Appendices A–D | librarian-mode drafting | card library consolidation; glossary draft; failure-index compression | owner: every card diffed against its chapter original (IDs/versions/locks identical); glossary terms checked against in-text definitions; F-01…F-10 entries checked against chapter fix-stacks | appendix wording never *contradicts* chapter cards (chapter = teaching version, appendix = instrument) |
| 2026-09-23 | Appendices E–F (this log) | research assistant + editor | perishables table; source summaries; log reconstruction from session records | owner: every row checked against actual working method; this file's own row read twice | *the log logs its own composition — last recursion this book will attempt* |
| (standing) | all sections | structural/continuity critics under Ch 12 cards | pass-style sweeps on the manuscript itself (TOC consistency, term usage, PC-ID collisions, Example A canon) | owner: adjudicated in editorial/validation reports shipped with the manuscript | the book ran its own pass system; reports in `output/` |

**What this log claims — precisely:** (1) *substantial AI assistance in drafting and research-triage*, exactly as Ch 1's model prescribes (machine proposes at volume; aims, selection, canon, legal restriction, and final wording are human decisions logged here); (2) *every factual claim traced to primary/official sources by a human opening them* — AI never a citation (protocol §9, Appendix E); (3) *human revision on every AI-touched passage* — the style guide's rule, evidenced by the review column's specificity (if a "what changed" cell were vague, the row would be *broken*, not conservative); (4) *the transparency norm Ch 15 advocates for venues applied to ourselves* — because a book that argues disclosure is hygiene and then hides its own process would be, in the chapter's exact vocabulary, **provenance fraud**. What it does *not* claim: machine authorship of final wording (the rows say *drafting partner* for a reason — partner proposes, owner disposes, and the disposal is the book), brand-specific dependencies (roles only, generic-first), or perfection (errors that reach the reader are *ours* — the validation report prints the checks actually run, including any they missed).

**Re-test & re-verification schedule (the maintenance rows this log implies):** card `tested` dates re-run at any tool switch and at pre-publication; perishables table rows re-checked at the edition's cut-off (date set at revision sign-off); this appendix updated at each edition (append-only — corrections add rows, never silently edit, same discipline as the claim register). The final line, which the book has earned the right to print about itself: **no AI-generated passage ships without human revision and a logged review — and above is the receipt.**
