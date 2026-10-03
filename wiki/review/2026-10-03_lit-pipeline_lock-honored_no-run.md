# Lit pipeline (15a/15b/15c) — second instance honored lock and exited, 2026-10-03

PROVENANCE: Origin: scheduled task c2a2-lit-search-pipeline (duplicate firing) | Chain: [none — no 15a/15b/15c work done by this instance] | Current status: NO-OP

- This instance started ~04:36 UTC and found `architecture/lit_pipeline.lock` (LOCKED 2026-10-03T04:34Z by c2a2-lit-search-pipeline, scope: 10-02 intake ASSUMPTION-1731..1741, PRESUMPTION-1106..1109), under 6 h old and not RELEASED.
- The other instance was actively writing `lit_search_results/for/*_for.md` (files stamped 04:35-04:36) while this one checked.
- Per the lock convention, this instance wrote NO registers, result files or queue tags, and exited. Nothing to repair.
- Evidence for ASSUMPTION-1731 / PRESUMPTION-1106: the duplicate firing happened again on 10-03, ~1 min apart, and the lock was honored only because the lock rule is now in the instructions this instance followed.
- Action for Tom: check the scheduler for a duplicate `c2a2-lit-search-pipeline` entry (cloud + local copy).
