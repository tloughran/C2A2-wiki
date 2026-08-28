# RESULTS — Is the inbox backlog a debt?

**Date:** 2026-08-26 · **Prereg:** `PREREG_inbox_backlog_2026-08-26.md`, written and committed to disk before any card in the frame was read.

## Verdict

**No. The backlog is not a debt, and it never was. The work was done; the ledger did not record it.**

Genuinely unprocessed approved proposals: **2 confirmed, 1 ambiguous — out of 301.**

The numbers this project has been carrying — 315, 158, and the 99 the prereg itself computed — are all artifacts of asking `PROCESSED_LOG.md` a question it cannot answer.

---

## How the number collapsed

| measure | count | what it actually means |
|---|---|---|
| inbox files with mtime ≥ 2026-06-17 | 315 | nothing. mtime is not a compile record. (This was the review's figure; it was wrong.) |
| memory's carried figure | 158 | stale |
| approved proposals with no `PROCESSED_LOG` slug entry | **99** | the prereg's frame — still wrong |
| …of those, also not cited in any `traditions/*/prs_triplets.md` | **20** | closer |
| …of those, also absent from the log in any other form | **5** | closer still |
| …of those 5, actually open (2 are logged `+0`/HELD, correctly) | **2 (+1 ambiguous)** | **the real number** |

## The decisive check

Tradition files record the proposal that produced each triplet, in the triplet itself:

```
PRS-10:
  Label: P10 (PROP-2026-04-09-SUPP-001) — C2A2 as a thousand-brains system
```

**587 such `PROP-` references exist across the tradition files, covering 262 distinct proposal IDs.** `PROCESSED_LOG.md` holds 221. The disagreement runs both ways:

- **63 proposals are cited in a tradition file but absent from `PROCESSED_LOG`** — ingested, unrecorded.
- **22 are in the log but cited nowhere** — and 11 of those carry an explicit `+0` / HELD marker, which is *correct* behaviour, not a gap.

**The tradition files are the primary record. `PROCESSED_LOG.md` is a hand-maintained secondary index that has drifted from it in 85 cases.**

## Why April, specifically

85 of the 99 apparent gaps are April 2026 cards. The mechanism is visible in the log itself:

```
| **Wolfram batch (5 files):** 2026-04-08_wolfram_jago-philosophy-discussion.md; 2026-04-08_wolfram_pvsnp…
| **Kastrup batch (4 files):** 2026-04-08_kastrup_daimon-soul-of-the-west.md; 2026-04-09_kastrup_mcgilchr…
```

The April seed batch was ingested under **batch** proposal IDs (`PROP-2026-04-16-006` … `-011`). Per-file IDs therefore never entered the log, while the tradition files recorded the per-file provenance correctly. Nothing was skipped. The index simply keys on a granularity the work did not use.

## Independent corroboration: content matching

Separately from the ID diff, the pre-registered 30-card sample (seed `20260826`) was matched by content against the existing PRS triplets in each tradition file. **49 of 58 candidate assertions (84%) are already present in the wiki**, most of them near-verbatim.

The cleanest case is `2026-04-09_hawkins_thousand-brains-deep-read-supplement`: six PRS candidates, all six already sitting in `hawkins/prs_triplets.md` as PRS-10 through PRS-15, each labelled with that proposal's own ID.

Two methods — deterministic ID diff and independent content matching — agree. That is the strongest part of this result.

## Against the pre-registered decision rules

Prereg rule: **NEW-rate < 20% → the backlog is not a debt and must stop being called one.** Observed: **~1%** (2–3 of 301). Rule fires cleanly.

**But the prereg's framing was wrong, and it should be recorded as wrong rather than scored as passed.** It offered two possible worlds — the work is undone, or it isn't — and the real world was a third: *the work is done and the instrument measuring it is broken.* Every threshold in §5 of the prereg assumed the measurement was sound. None of them would have caught this. The ID-diff that did catch it was not in the prereg at all.

**P1 (≥60% of cards carry a PRS candidate) confirmed at 99%** — 98 of 99. The one exception is `2026-05-12_repair_manifest.md`, an operations file that should not be in `proposals/approved/` at all.

## Consequences for the review

**D1 is retracted.** "The compile step is the step that stalled" is false. The compile step ran, and has kept running — May–August ingest is 88–100% complete by the same ID diff. What failed is the record of its own execution.

The article's frame survives this, and lands harder than the original review had it. Its promise is that the compiled wiki *remembers what it learned*. The actual failure here is the mirror image: **the loop did the work and then forgot that it had done it**, for one month, because the log keyed on a granularity the work did not use. A second brain that cannot answer "have I already read this?" will re-read, re-derive, and eventually re-litigate — which is exactly the cost structure compilation is supposed to eliminate.

**Item 2 (burn down the backlog) is dissolved.** There is no backlog to burn. Ingest the two open cards and close it.

**Item 1 is promoted and rewritten.** It was "one compile-state ledger instead of twelve." It should be:

> **Derive compile state; stop maintaining it by hand.** The tradition files already carry the provenance. `PROCESSED_LOG.md` should be *generated* from them, not written alongside them, with the `+0`/HELD outcomes carried as explicit records rather than as absence. Rule 5, exactly: if code can answer, code answers.

That change also dissolves the twelve-worktree problem for free — a derived ledger cannot fork.

## Smaller findings, recorded

1. `2026-05-12_repair_manifest.md` sits in `proposals/approved/` and is not a proposal.
2. One approved proposal has no `proposal_id:` in its frontmatter.
3. At least two log entries carry placeholder IDs (`PROP-2026-07-28-00x`, `PROP-2026-07-29-00x`) that no exact-match tool will ever find. These were the last two "backlog" items to dissolve, and only a slug search found them.
4. `proposals/pending/` is 78/80 unlogged — correct and expected. Pending means awaiting Tom's decision. It is a review queue, not a compile queue, and should never be counted as backlog again.

## Limitations

- The 84% content-match figure is single-rater (me) and is corroboration, not the primary evidence. The primary evidence is the deterministic ID diff.
- "Cited in a tradition file" proves a proposal was *processed*. It does not prove it was processed *well*. This measured throughput, not quality.
- The one ambiguous card (`2026-07-06_friston_active-inference-artificial-reasoning`) matches a similarly-slugged but differently-dated file inside an April batch row. Resolve by hand before ingesting.


---

## POSTSCRIPT — this is a REDISCOVERY, and that is the sharper finding

After the result above was in hand, a check of `prototypes/backlog/` showed the correct test
**already exists in this repo and has since 2026-06-30**:

```
prototypes/backlog/build_prs_manifest.py
def ingested_proposal_ids(vault, log_txt):
    """Authoritative ingested test: a card is ingested if its proposal_id is cited
    as a Source: in any live traditions/*/prs_triplets.md, OR appears in a
    PROCESSED_LOG ingestion line ('... -> <trad> PRS-').
    The old basename-vs-log test missed both because the log keys on proposal_id/..."""
```

That is the same dual-ledger gate rebuilt from scratch today, arrived at independently. The
2026-06-30 session found the gate bug, named it as erring in **both** directions, corrected the
figure to 70 units / 152 candidate triplets, and applied 144 vetted triplets across 12 traditions
that evening. **That apply is why today's number is 2 and not 70.**

So the discovery here is not the method. It is this:

> **The project already knew how to measure its own backlog correctly, and kept quoting the wrong
> number anyway — for eight weeks, in memory, in handoffs, and in the review written this morning.**

The reason is structural, not careless: the authoritative test lives inside a one-off backlog-clear
script in `prototypes/`. Nothing runs it on a schedule, nothing reports it, and no health check
consumes it. A correct measurement that nothing calls is indistinguishable from one that does not
exist. This is D4 — no staleness detection on the governing tier — reaching all the way down into
the numbers the project quotes about itself.

**Item 1, final form (small, surgical, Rule 2/3):** promote `ingested_proposal_ids()` out of
`prototypes/backlog/` into a standing check — janitor row and/or a `check_scheduler_health.py`
ARTIFACTS entry — that reports three counts every run: approved proposals, ingested, genuinely
open. No new subsystem; the function already works. What it needs is a caller and a report line.

*Falsifier:* plant one un-ingested approved proposal; the next run must report open = N+1. And
regenerating the ledger must account for all 85 current disagreements as either unrecorded ingests
(63) or recorded non-ingests (22), with none left over.


---

## AMENDMENT 2 — same day, after the check was built

Building the standing check (`scripts/ingest_ledger.py`) corrected this document's own number.

**Current figure: 280 ingested / 11 decided-zero / 9 OPEN, of 301 approved.**

The "2 confirmed (+1 ambiguous)" above was **too low**. It came from treating *any* mention of a
proposal in `PROCESSED_LOG` as evidence of ingestion. A bare deposit line ("Phase 2: Hawkins
deposited ...") is not evidence, and counting it as such is the same class of error as the figures
this document was written to retract - just in the opposite direction.

The tested definition now used:

| category | evidence required |
|---|---|
| **ingested** | proposal id cited in a live `traditions/*/prs_triplets.md`, **or** a log line routing it to a PRS (`-> <trad> PRS-`) |
| **decided-zero** | a log line naming it with `+0` / `no-net-new` / `citation-upgrade` / `HELD` / `NO-OP` - a decision that yielded nothing, which is **not** backlog |
| **open** | neither |

Two of the 9 open (`hoffman_spacetime-headset-essay`, `mcgilchrist_abc-soul-search-two-parter`) are
logged under placeholder ids (`PROP-2026-07-28-00x`) that do not match their real ids. The check
cannot clear them, and surfaces them rather than hiding them - which is correct. Fix the log ids and
they resolve. Two more are the same Fredrickson source proposed twice (`PROP-2026-06-25-004` /
`PROP-2026-07-23-001`). Distinct genuinely-open sources: about **six**.

**The direction of this document's claim survives - 9 is not 99, and certainly not 315.** The
precise figure did not, and the record of it wobbling from 315 to 158 to 99 to 5 to 2 to 9 in a
single day is itself the argument for having a scheduled check instead of a number people quote.

### Two defects found in the pre-existing "authoritative" test

Reading `prototypes/backlog/build_prs_manifest.py` before reusing it (Rule 8) turned up two live
bugs in `ingested_proposal_ids()`:

1. **Arrow form.** It matched only the Unicode arrow `→`. The live log carries **79** lines with
   U+2192 and **61** with ASCII `->`. Those 61 ingestion lines were invisible to that branch.
2. **Proposal-id shape.** Its id pattern `PROP-2026-\d{2}-\d{2}-\d+` cannot match
   `PROP-2026-04-09-SUPP-001` (13 occurrences) or the `-00x` placeholders. The Hawkins Thousand
   Brains supplement produced six triplets (`hawkins` PRS-10..15) and was still read as un-ingested.

Defect 2 has already been paid for once. The 2026-06-30 backlog clear recorded *"8 QC drops via new
qc_prs.py - 6 hawkins SUPP-001 re-derivation dups."* That was logged as a QC catch. **It was a gate
defect**, and the cost landed downstream where nobody traced it back.

Both are fixed in `scripts/ingest_ledger.py`, with regression tests that fail against the original
patterns (verified: 3 of 17 assertions fail when the old regexes are restored).
