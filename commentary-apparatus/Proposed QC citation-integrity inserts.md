---
title: Proposed QC Citation-Integrity Inserts
updated: 2026-07-17
status: proposed — Tom applies Part A to the Summa vault's Summa.md; installs Part B over the scheduled task
source_of_truth: "[[Referencing and linking foundation]]" §6 (this folder)
note: Parts A/B are applied in the SUMMA 2026 vault (they govern its constitution + scheduled task); this canonical copy lives with the apparatus.
---

# Proposed QC Citation-Integrity Inserts

Two surgical additions giving the Summa QC agent a **verify-only** citation-integrity frame (foundation §6). Nothing here generates citations — the frame flags and escalates. Ship **report-only** for one sweep cycle (findings in the `mark --note`), then flip to gating once `qc_sweep.py` gains the new flags (Part C).

The QC agent does not self-edit `Summa.md`; **Tom applies Part A** in the Summa vault. Part B is a revised block for the scheduled-task SKILL.md (the uploaded copy is read-only), installed over the task.

---

## Part A — insert into the Summa vault's `Summa.md`, section "The QC agent"

Under **"### What it does each run" → item 2 "Two-frame review on each pair"**, rename to **"Three-frame review"** and add this third frame after the "Synthesis sense frame" block:

> - **Citation-integrity frame** (verify only; flag/escalate, never invent a citation). Per the referencing foundation §6 (canonical copy: RC Karpathy Wiki Project `commentary-apparatus/Referencing and linking foundation.md`):
>   - **Surname resolution.** Every roster surname (the 15) in the synthesis *body* resolves to ≥1 cite-key in `works_cited.json`, or is flagged `no canonical work registered for <thinker>`.
>   - **Id resolution.** Every `PRS-NN` / `CROSS-NN` / `FLAG-NN` / `FINDING-NNN` resolves to a real wiki node when the Karpathy mount is present; when absent, record `ids-deferred (wiki mount absent)` and re-queue — do not count fully clean.
>   - **Banned possessive form.** No `X's PRS-NN` in body or footer (`wiki's PRS-NN` allowed).
>   - **No internal role-classification in the body.** "primary on", "the lead", "as counterpoint", "NOT the metaphysical lead" must not appear in prose (footer sourcing notes are exempt but stripped at export).
>   - **Quote verification (character-for-character).** Every verbatim block quote carries a resolvable cite-key and matches its canonical source exactly. Scripture (cited translation), *Catechism* (paragraph), council/magisterial texts, Aquinas (article) verified each sweep; a mismatch is fixed from source and logged in the transcript's typo-cleanup blockquote. A thinker's published line is checked when the source is retrievable, else marked `quote-unverified (source not retrievable)` — never asserted verified without the source.

Under **"### When the QC agent must escalate, not rewrite"**, add:

> - A body citation cannot be resolved to any registered work, or a verbatim quote fails character-for-character against a *retrievable* canonical source. Append "ESCALATION: citation unresolved / quote mismatch — Day NNN" and do not fabricate a source.

Under **"### What it does each run" → item 5**, extend the state written on each file:

> Also set `last_citation_qc_at` and `last_citation_qc_outcome` (`pass` / `flag` / `deferred`) independently of the sense/fidelity outcome.

---

## Part B — revised block for the scheduled-task SKILL.md

Add **Step 3c** immediately after the "Synthesis sense frame" in Step 3:

> **Citation-integrity frame (verify only — flag, don't generate).** Read the referencing foundation §6 (Karpathy `commentary-apparatus/`) at run start alongside the other contract files. For each pair, check: (1) every roster surname (15) in the body resolves to a cite-key in `works_cited.json`, else flag `no canonical work registered`; (2) every PRS/CROSS/FLAG/FINDING id resolves to a wiki node when the Karpathy mount is present, else record `ids-deferred (wiki mount absent)` and re-queue; (3) no `X's PRS-NN` possessive; (4) no role-classification ("primary on", "the lead", "as counterpoint") in the *body* (footer exempt); (5) every verbatim block quote has a cite-key and matches its canonical source character-for-character (Scripture/CCC/council/Aquinas verified each run; thinker lines when retrievable, else `quote-unverified`). **Until `works_cited.json` exists, run this frame in report-only mode:** record findings in the `mark --note`, gate nothing.

Add to **Step 4 (escalate)**:

> - A body citation resolves to no registered work, or a verbatim quote fails character-for-character against a retrievable source → append "ESCALATION: citation unresolved / quote mismatch"; do not fabricate.

---

## Part C — `qc_sweep.py` support (builder task, not QC)

Before the frame can *gate* (until then report-only via `--note`):

1. `mark` accepts `--citation-pass | --citation-flag | --citation-deferred` and writes `last_citation_qc_at` / `last_citation_qc_outcome` to both files.
2. `report` re-queues any pair whose `last_citation_qc_outcome` is `deferred` or `flag` (independent of the 7-day staleness), once the Karpathy mount is present.
3. A read-only helper `resolve_citations.py` that, given a synthesis path + `works_cited.json` + the wiki mount, returns the §6 findings as JSON for the sweep to fold in.

---

## Apply order

1. Seed `commentary-apparatus/works_cited.json` (all 15 seedable here now — foundation §7 step 1: import `ACPA_2026_references.md`, join `prs_pub_years.json`, extract from `wiki/traditions/`).
2. Apply Part A to `Summa.md`; install Part B over the scheduled task — safe immediately (report-only; gates nothing without `works_cited.json`).
3. Land Part C, then flip report-only → gating.
