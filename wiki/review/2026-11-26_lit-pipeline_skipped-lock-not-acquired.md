# Lit pipeline (15a/15b/15c) — 2026-11-26 run SKIPPED: lock not acquired

**Run ID:** local-2026-11-26-cowork-04d7efe7
**Outcome:** Stopped at Step 0. Nothing was committed.

## What happened
- Desktop Commander `start_process` (the only route to run `scripts/lit_pipeline_lock.sh` on the Mac) was **declined automatically**: no one was available to approve it during the scheduled run.
- The sandbox shell can't reach `scripts/`; only `wiki/` and `wiki/review/` are mounted.
- Treated as exit 1 ("lock could not be created"). Did not run unlocked. Did not hand-create `review/lit_pipeline.lock.d`.

## Not done
- Agent definitions and queue not read; queue state unknown.
- No 15a/15b results, no returns appends, no queue tags, no 15c dispositions.
- No release needed (no lock taken).

## Recurring
This is the same failure as most daily runs since 2026-10-31. Until fixed, the pipeline will not process anything. Fix options:
1. Pre-approve Desktop Commander `start_process` for this scheduled task, or
2. Mount the project root (or `scripts/`) in the Cowork session so the lock script runs in the sandbox.
