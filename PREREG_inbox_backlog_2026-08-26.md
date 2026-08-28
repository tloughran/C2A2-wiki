# PREREG — Is the inbox backlog a debt?

**Written:** 2026-08-26, **before** any card in the sampling frame was read.
**Change under test:** item 2 of `SECOND_BRAIN_COMPILER_REVIEW_2026-08-26.md`.
**Rule:** nothing below may be edited after the sample is drawn. Amendments append, dated.

---

## 0. Correction to the review, entered before results

The review claimed "728 files in `inbox/`; 315 (43%) arrived on or after 2026-06-17 … nearly half of raw/ has never been compiled." **That was an mtime proxy and it is not the right measure.** File mtime answers *when the file was last written*, not *whether it was compiled*. The correct measure is the slug diff against `PROCESSED_LOG.md`, which is what the 2026-07-20 false-backlog incident already established.

Recomputed by slug diff (strip `^\d{4}-\d{2}-\d{2}_` and `.md`; match against the 199 distinct slug keys in the 277 log lines):

| population | total | no PROCESSED_LOG entry | % |
|---|---|---|---|
| root source cards | 304 | 102 | 34% |
| `proposals/approved/` | 301 | **99** | **33%** |
| `proposals/pending/` | 80 | 78 | 98% |
| `proposals/_pending_dupes_resolved/` | 38 | 1 | 3% |

Memory carried "158 approved cards unprocessed." **That figure is stale — the current number is 99.**

`proposals/pending/` is *not* backlog: pending means awaiting Tom's approval decision, which is a review queue, not a compile queue. Root source cards without a proposal are a *proposal-generation* gap, a different question, deliberately out of frame here.

---

## 1. Frame

**N = 99** — files in `wiki/inbox/proposals/approved/` whose slug has no entry in `PROCESSED_LOG.md` as of 2026-08-26.

These are cards Tom has already approved and the pipeline has not ingested. That is the compile debt, exactly.

## 2. Sampling

`n = 30`, drawn with `random.Random(20260826).sample(sorted(frame), 30)`. Seed fixed and published here so the draw is reproducible and cannot be re-rolled.

## 3. Rule 5 split — what code decides, what the model decides

**Code, over all 99 (not the sample):** count `PRS-CANDIDATE-NN` blocks, count `## Cross-Tradition Signals` bullets, tabulate `Confidence:` labels. Presence of an assertion is a deterministic property of the file. There is no reason to sample it and no reason to ask a model.

**Model, over the 30:** novelty only. For each card, classify every candidate assertion as:

- **NEW** — asserts something not already present as a PRS triplet in that tradition's file, or materially sharpens one that is.
- **DUPLICATE** — restates an assertion the tradition file already carries.
- **UNVERIFIABLE** — the card's own evidence line does not support the assertion, or the source could not be confirmed (the `mcgilchrist_commencement-2026` case).

A card counts as **yielding a new assertion** if it has ≥1 NEW. A card counts as **node-only** if all its candidates are DUPLICATE, UNVERIFIABLE, or it carries no candidates at all.

## 4. Pre-registered predictions

**P1 (deterministic).** ≥60% of the 99 carry at least one `PRS-CANDIDATE` block. Rationale: they passed an approval gate, so mechanical emptiness should be rare. *If P1 fails badly, the approval gate is not doing what it is documented to do, and that is the finding.*

**P2 (the actual test).** ≥20% of the 30 sampled cards yield ≥1 NEW assertion.

## 5. Decision rules — fixed now

- **NEW-rate ≥ 50%** → the backlog is a real debt and the burn-down is the priority. Item 1 (single slug-keyed compile-state ledger) becomes a prerequisite and moves ahead of item 5.
- **NEW-rate 20–49%** → partial debt. Do **not** burn down wholesale. Build a cheap triage that ranks cards by candidate count and confidence, ingest the top decile, re-measure. Item 5 keeps its slot.
- **NEW-rate < 20%** → **the backlog is not a debt and must stop being called one.** The correct action is to close it out with a documented decision, not to ingest it. Item 1 drops in priority. The review's framing was wrong and the review gets amended, not defended.
- **UNVERIFIABLE ≥ 15%** → a separate and more serious finding than the debt question: the approval gate is admitting sources that cannot be confirmed, and *that* becomes the next increment regardless of the NEW-rate.

## 6. Known limitations, stated in advance

- Novelty is judged against the tradition file's current PRS triplets. If the resolver bug (fixed in `216e596`, unpushed) affects what is visible in those files, novelty may be **over**-counted. Direction of bias is stated so it cannot be quietly reinterpreted later.
- One model judges all 30. There is no second rater, so inter-rater reliability is unmeasured. This is a scouting measurement, not a publishable one, and will not be cited as though it were.
- n=30 on N=99 gives roughly ±9pp at the 20% level. A result between 15% and 25% is **not** decisive and the decision rules above should be read as "re-measure with a larger n," not as a verdict.
