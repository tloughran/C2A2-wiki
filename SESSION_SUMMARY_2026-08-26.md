# Session summary — 2026-08-26, second-brain-compiler thread

## The headline

Six defects were asserted this morning. **One was tested. It failed.**

D1 ("the compile step stalled") was wrong at both the measurement and the causal story. D5 (twelve
forked `PROCESSED_LOG`s) partly dissolves as a consequence — a *derived* count cannot fork.

That leaves **D2, D3, D4 and D6 untested.** The honest inference from a 1-for-1 refutation rate is
not that the remaining five are sound. Each rests on a number that has not had the treatment D1 got.

---

## What is of value

**1. The backlog does not exist.** 280 ingested / 11 decided-zero / **9 open** of 301 approved
(about six distinct sources; two of the nine are placeholder-id artifacts in the log). Earlier in the
day this was reported as 2 - that was too loose, and the correction is recorded in AMENDMENT 2 of
the results doc.
A phantom debt of 99–315 cards has been shaping memory entries, handoffs, the ingestion runbook and
this morning's review for eight weeks. Removing it frees the next increment to be about something
real. This is the session's actual product.

**2. The portable lesson, worth more than the instance.** The correct test already existed —
`ingested_proposal_ids()` in `prototypes/backlog/build_prs_manifest.py`, written 2026-06-30 — and
nothing called it.

> **A correct measurement that nothing schedules or reports is indistinguishable from one that does
> not exist.**

That is D4 surfacing where D4 did not predict: not stale governing *docs*, but stale governing
*numbers*.

**3. The method held.** Prereg on disk before the sample was drawn; two independent methods
(deterministic ID diff, and content-matching a seeded 30-card sample) in agreement; the falsifier
fired against the person who wrote it. Worth keeping as a habit, not a one-off.

**4. The article was worth about one good question.** Its "compiler" metaphor breaks under load — a
compiler is deterministic and rebuildable; this is a lossy path-dependent accumulator, and
*metabolism* was already the better word. But *"is the wiki tier derived, or authored?"* is the
question that produced everything above.

---

## Done

| artifact | state |
|---|---|
| `SECOND_BRAIN_COMPILER_REVIEW_2026-08-26.md` | + AMENDMENT 1 (D1 retracted, item 2 dissolved, item 1 rewritten) |
| `PREREG_inbox_backlog_2026-08-26.md` | on disk **before** the sample was drawn |
| `RESULTS_inbox_backlog_2026-08-26.md` | + POSTSCRIPT (the rediscovery finding) |
| `handoffs/second-brain-compiler.md` | resume cue + next increment + parked items |
| project memory | updated; the stale 158 figure corrected |

Nothing staged, committed, or pushed. No `index.lock` left on the mount.

---

## The evidence, compactly

`traditions/*/prs_triplets.md` is the **primary** compile record — each triplet names its
originating proposal inside itself (`Label: P10 (PROP-2026-04-09-SUPP-001)`). 587 such references
covering 262 distinct proposal IDs, against `PROCESSED_LOG`'s 221. They disagree **85 ways**:
63 ingested-but-unlogged, 22 logged-but-uncited (11 correctly marked `+0`/HELD).

The April seed batch was ingested under **batch** proposal IDs (`PROP-2026-04-16-006`…`-011`), so
per-file IDs never entered the log while the tradition files recorded provenance correctly. That
alone accounts for 85 of the 99 apparent gaps. Nothing was skipped.

Corroboration: 49 of 58 candidate assertions (84%) in the seeded sample are already in the wiki,
mostly near-verbatim. Cleanest case — `2026-04-09_hawkins_thousand-brains-deep-read-supplement`:
six candidates, all six present as `hawkins` PRS-10…15, each labelled with that proposal's own ID.

---

## To do — ranked, none ratified

1. **Give `ingested_proposal_ids()` a caller.** Report approved / ingested / genuinely open on a
   schedule. Smallest item here and the one that stops this recurring. **Do not rebuild the method.**
2. **Ingest the two real cards**; resolve the ambiguous Friston one by hand. Expect low yield —
   both largely duplicate existing triplets.
3. **Audit D2 before acting on it.** The 87.9%-co-occurrence edge census is load-bearing for the
   whole "RAG in wiki clothes" claim and deserves exactly what D1 just got. Item 3 stays held until
   `claude/wikilink-resolver-fix` lands regardless.
4. **Item 5 — the rebuild-fidelity probe.** Still the only item producing research output rather
   than tidiness, and better motivated now that the tradition files are known to be the primary record.
5. **Item 4 — split `CLAUDE.md`** (464 lines; six constitutional rules + ten ops manuals in one
   file). Independent; needs a call on the split boundary.

**Unpaid, and blocking:** `claude/wikilink-resolver-fix` has seven unpushed commits. Items 3 and 4
queue behind it.

**Minute-each loose ends:** `proposals/approved/2026-05-12_repair_manifest.md` is not a proposal;
one approved proposal has no `proposal_id:`; placeholder log IDs (`PROP-2026-07-28-00x`) are
invisible to exact-match tooling — use slug search.
