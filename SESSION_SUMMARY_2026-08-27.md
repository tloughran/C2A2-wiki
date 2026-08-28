# Session summary — 2026-08-27 evening (Cowork)

**Thread:** PRS / Narrative Connectome. **Resume cue:** "resume the PRS connectome work".
**Handoff:** `handoffs/prs-connectome.md`. **Review bundle:** `REVIEW_track_a_pilot_2026-08-27.md`
(root, excluded via `.git/info/exclude`).

**Result: `origin/main` @ `7ae19a1`, verified against the live remote (`git ls-remote`),
0 ahead / 0 behind.** Two commits: `946eb4d` (tooling) and `7ae19a1` (hawkins), on top of
this morning's six.

---

## What I set out to do, and what actually happened

The morning handoff's next action was **"Track A ingest for the 77."** Rebuilding the
manifest to start that ingest surfaced a defect in the gate, and then three more in the
staging and apply steps. The ingest ran, but only after the instrument was corrected —
which is the whole story of this session.

---

## 1. The gate defect (third in the same function)

`prototypes/backlog/build_prs_manifest.py` imported `ingested_proposal_ids` from
`scripts/ingest_ledger.py` but **not `decided_zero_ids`**. It therefore re-queued **11 cards
already decided** `+0` / `no-net-new` / `citation-upgrade` / `HELD` — including the
McGilchrist commencement card held at a verification gate on 08-11 because no transcript
exists. Every one would have cost attended vetting on a call a human already made.

**How it was caught, and why that matters more than the fix.** The builder reported **97**
un-ingested staging files while `python3 scripts/ingest_ledger.py wiki` independently
reported **OPEN=86**. The 11-card gap was *exactly* the `decided-zero=11` figure the ledger
already printed on its own first line. After the subtraction the two instruments agree
exactly (86 = 86).

> **Two instruments measuring one population must be reconciled before either is believed.
> The disagreement is the finding.**

This is the third defect in this one gate. The first two (found 2026-08-26) were a
Unicode-only arrow regex and an id pattern blind to `-SUPP-`/`-00x`. All three are the same
shape: **a population was named a debt because the instrument could not see a decision
that had already been recorded.**

## 2. Three format defects in `stage_prs.py`, all found by reading the corpus

None of these were visible in the code. One `grep` of `wiki/traditions/hawkins/prs_triplets.md`
showed all three.

- **No `Label:` line.** All 22 live hawkins triplets carry one
  (`Label: P22 (PROP-2026-08-04-001) — <claim descriptor>`), and Label is the **primary
  compile record** — it is how a triplet names the proposal that produced it. Code cannot
  author a claim descriptor, so the stager now emits a loud `<<DESCRIBE>>` placeholder and
  **`apply_prs.py` refuses to insert any block still carrying one.** Guard verified firing.
- **`Date Added` was the source's PUBLICATION date.** The convention is the **ingest** date
  (PRS-21: Date Added 2026-08-09, source 2026-02-25). This is the *same class of error* as
  the capture-date pollution in `prs_pub_years.json` fixed this morning, running in the
  opposite direction. Source date now goes where it belongs, inside `Source:`.
- **`Evidence:` was dropped** even when the card supplied it. Now carried through verbatim,
  never invented.

## 3. A restaging leak in `apply_prs.py`

For a unit collapsed from two same-source cards, it logged **only the primary proposal_id**.
The secondary got no ingestion line and no zero-yield decision — so `ingest_ledger` would
report it OPEN forever and the builder would re-stage it on every future run. The DISPATCH
explicitly requires both ids be logged and the duplicate marked. Fixed; 1 affected unit in
the current 85-unit manifest.

---

## The pilot — hawkins, 13 triplets, PRS-23..PRS-35

Five units emitted 13 triplets. **Footer 22 → 35, ids contiguous 01..35, all 35 Labelled,
zero `<<DESCRIBE>>` survivors, Evidence present where the cards supplied it, the
`## Agentic Calls` block still sits after the footer.**

**One unit dropped by judgment.** `PROP-2026-08-11-001` (+ its re-staging
`PROP-2026-06-30-001`) is the *Neural Computation* 38(6) publication of the TBS paper whose
arXiv preprint is already held as PRS-16/17 — and the same source was already decided
no-net-new on 2026-06-23 as `PROP-2026-06-23-002`. Per the DISPATCH guardrail: logged `+0`,
and the **citation upgraded in place** on PRS-16 and PRS-17 (NECO 38(6):845–896,
DOI 10.1162/NECO.a.1508) rather than minted as a new triplet.

**Order matters here.** Logging that `+0` *first* made the gate drop the unit on the next
build, so the restage renumbered hawkins contiguously **23–35 with no numbering hole**
(`apply_prs.py --drop` does not renumber). The pipeline ate its own dogfood. **This is the
supported order for any future drop.**

**Backlog: `ingest_ledger` OPEN 86 → 79** — exactly 5 ingested + 2 decided-zero.

---

## Where the backlog stands

Manifest rebuilt clean: **84 units / 192 candidate triplets** across 12 remaining traditions.

| tradition | units | | tradition | units |
|---|---|---|---|---|
| rohr | 16 | | fredrickson | 3 |
| levin | 15 | | hoffman | 3 |
| wright | 11 | | carroll | 3 |
| friston | 10 | | arkanihamed | 2 |
| mcgilchrist | 7 | | stump | 1 |
| wolfram | 4 | | | |
| kastrup | 4 | | | |

---

## Owed

1. **Step 4 of the attended loop was NOT done for hawkins.** Four of the five cards carry
   cross-tradition agentic calls (Levin, Friston, Hoffman, McGilchrist, Wolfram,
   Pattern-detector) that should become CROSS-/FINDING- entries in
   `wiki/master/cross_program_index.md`. They are unrouted and still sit in the source
   cards. **This is now a debt carried by pushed work, not an open decision.** Settle
   whether routing rides with each unit or is a separate pass *before* the other 12
   traditions.
2. **The remaining 79.**
3. **Downstream regens.** `wiki/architecture/metrics/prs_yield.py` reconstructs the yield
   series from GIT HISTORY and fails loud on triplets present on disk but absent from git —
   so the triplet commit must precede it. hawkins is committed, so it can now see the new
   data. Then `bash scripts/regen_prs_connectome.sh`. **This morning's axis fix has still
   not been shown one new datum.**
4. Carried untouched: untrack `wiki/prs_3d_debug.html`; the tau slider (blocked on
   reposition machinery that does not exist); 38 approved cards emitting no parseable
   signal; 185 cards flagged for non-roster targets; 7 dependabot vulnerabilities.

---

## Process notes

- **Token budget breached.** Well past the 30k session ceiling, spent almost entirely in
  the diagnostic phase — each of the four defects needed corpus evidence rather than a code
  reading. Surfaced at the time, not after.
- **Git through `device_bash` strands a lock it cannot unlink.** Every call leaves a 0-byte
  `.git/index.lock` (sometimes `HEAD.lock` too), so the *next* call dies with "Another git
  process seems to be running." `add` succeeded; `commit` failed four times. **Run git
  through Desktop Commander** — `rm -f .git/index.lock .git/HEAD.lock` and the whole chain
  in one call. Filed as `feedback_git_on_mount_strands_locks`.
- **The remote-devices bridge dropped twice mid-session.** Nothing was lost because every
  intermediate result was already on disk or in a commit. Do not hold pipeline state only
  in the conversation.

## Irreversible

The push — two commits are public on a public repo. `wiki/traditions/hawkins/prs_triplets.md`
gained 13 triplets and two upgraded `Source:` lines; `wiki/inbox/PROCESSED_LOG.md` gained
9 lines under a `## 2026-08-27 — Track A PRS backlog clear (attended apply_prs)` header.
