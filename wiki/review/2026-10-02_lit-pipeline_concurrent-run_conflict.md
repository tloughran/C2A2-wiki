# Lit pipeline 10-02: a second concurrent run happened again

**Headline.** For the second day running, two instances of `c2a2-lit-search-pipeline` processed the same intake at the same time: the 10-01 14a/14b items PRESUMPTION-1103, 1104 and 1105, ASSUMPTION-1730, and in-house ASSUMPTION-1721–1729. **The other instance started first and committed to every register. Its results stand.** This instance (the one writing this note) withdrew its own results without applying them. This repeats the 10-01 event exactly, and it is direct in-house evidence for PRESUMPTION-1104 (REVISE-498).

## What stands (the committed instance)

| Item | Disposition |
|---|---|
| PRESUMPTION-1103 (one test target per handoff) | DISPOSITION-1021 → **REVISE-499** (Medium) |
| PRESUMPTION-1104 (shared files safe without locks) | DISPOSITION-1022 → **REVISE-498** (High) |
| PRESUMPTION-1105 (unaudited exceptions unbiased) | DISPOSITION-1023 → **MONITOR-647** |
| ASSUMPTION-1730 (Supabase 7-day pause; `SELECT 1` prevents it) | DISPOSITION-1024 → **MONITOR-648** |
| In-house items ASSUMPTION-1721, 1722, 1724, 1725, 1727, 1729 | MONITOR-649..654 |

## What this instance would have done (NOT APPLIED)

Its proposals are in `lit_search_returns.md`, in the block marked "⚠ NOT APPLIED". The ids in that block collide with the committed ones, so read them all as "P-" (proposed).

- **1103:** REVISE, at **High** rather than Medium. Same direction as the committed run.
- **1104:** REVISE, High. Same as committed.
- **1105:** **REVISE (Medium)** rather than MONITOR. Cochrane guidance holds that post hoc inclusion decisions are bias-prone, and the remedy (log a reason for each exception) costs almost nothing. The committed MONITOR is defensible because the item rests on a single speculative proposal.
- **1730:** **REVISE (Medium)** rather than MONITOR. The 7-day part is confirmed by the official Supabase docs, page modified 2026-10-01. The `SELECT 1` part is not: the docs give no threshold for what counts as activity, and GitHub discussion #13121 reports a connect-only keep-alive that failed after months. The risk is a silent failure: `SELECT 1` always succeeds, so the task reports success either way. **For you:** swap the ping for a real table read or write, and check the project's status. This is cheap whichever disposition stands.

**The two runs agree in direction on all four items.** They differ on urgency (1103) and on whether two cheap fixes justify REVISE rather than MONITOR (1105 and 1730). Per Rule 7, I have not averaged the two. The committed numbers stand, and the two differences are listed here for you to rule on.

## Damage and repairs

- **Result files are mixed.** `lit_search_results/against/{1103,1104,1105,1730}_against.md` now hold the committed instance's content, so this instance's 15b files were overwritten. The `for/` files cannot be cleanly attributed without reading each one. Both instances' files carried a 2026-10-02 PROVENANCE header, so neither file set can be trusted as one instance's output.
- **Two SYSTEMIC-RISK flags for one pattern:** `SYSTEMIC-RISK-FLAG_2026-10-02_silent-divergence-unchecked.md` (committed) and `..._uncoordinated-shared-artifacts_1103-1104-1105.md` (this instance). They describe the same pattern, so the second should be merged into the first or deleted.
- **The tag on ASSUMPTION-1729 is missing.** Its `for_lit_search.md` line still reads bare `[QUEUED] [IN-HOUSE]`, although MONITOR-654 routes it. I did not edit it, in case the other writer was still live.
- **Lock file.** This instance created `architecture/lit_pipeline.lock` (the first one). The other instance started before it existed and reported "no lock file exists". A lock only works if every instance checks for it, and the task spec doesn't tell it to. The lock is now marked RELEASED.

## The ruling that would stop this

Why are two instances of the same scheduled task firing at all? Possible causes are a duplicate schedule, a cloud copy alongside a local one (cf. ASSUMPTION-1713 and 1720, "32 cloud-migrated tasks"), or a retry after a timeout. Either remove the duplicate, or add "check `architecture/lit_pipeline.lock`; if present and under 6 h old, exit" to the task's own instructions.

## Environment (fail loud)

- The sandbox shell was unusable all run ("No space left on device", the same condition as ASSUMPTION-1729 and PRESUMPTION-1096). All work used file tools.
- Token budget: the subagents used about 114k (15a) and 129k (15b) tokens. That is over the 4k/30k Rule 6 budget, as on every prior run.
- The re-trigger backlog (~153 bare `[QUEUED]` stubs, oldest from 2026-07) was not touched, per standing scope.
