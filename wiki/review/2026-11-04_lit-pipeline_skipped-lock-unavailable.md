# Lit pipeline run skipped: run lock unavailable (2026-11-04)

**Run:** scheduled task `c2a2-lit-search-pipeline`, Cowork session 1582da46 (automated, no user present)
**Outcome:** STOPPED at Step 0 (exit 1 case). Nothing else was written.

## What happened

- Step 0 requires `scripts/lit_pipeline_lock.sh acquire` in a shell on the Mac.
- Desktop Commander `start_process` was the only Mac shell. The call was **declined automatically** (no one there to approve it).
- The sandbox shell can't reach `scripts/`; only `wiki/` and `wiki/review/` are mounted.
- The task says not to run unlocked, so this run did not. No release was needed because no lock was acquired.

## Not touched

- No 15a/15b result files, returns appends, queue tags, 15c dispositions, or backups.
- `review/lit_pipeline.lock` and `review/lit_pipeline.lock.d` were not read, moved or edited.
- The queue was not read, so it's unknown whether items are waiting.

## Pattern

This is the **fifth skipped run in a row** (10-31, 11-01 second run, 11-02, 11-03, 11-04), all for the same reason. The pipeline is effectively stalled until one of these is done:

1. Pre-approve Desktop Commander `start_process` for this scheduled task, or
2. Mount the project root (or `scripts/`) so the sandbox can run the lock script. This is untested: the script may assume macOS paths.
