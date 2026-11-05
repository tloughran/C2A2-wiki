# Lit pipeline run skipped — lock could not be acquired

- **Date:** 2026-10-31 (~00:33 EDT)
- **Run ID:** cowork-1582da46-2026-10-31 (scheduled task `c2a2-lit-search-pipeline`, Cowork/local registration)
- **Outcome:** STOPPED at Step 0. Nothing written: no 15a/15b/15c result files, no register appends, no queue tags, no backups.

## Why

Step 0 requires running `scripts/lit_pipeline_lock.sh acquire` in a shell on the Mac.
- The Cowork sandbox shell cannot reach `scripts/` (only `wiki/` and `wiki/review/` are mounted), so it can't run the script.
- The only Mac shell available (Desktop Commander `start_process`) needs per-call approval, and the request was **declined automatically** because no one was present for the scheduled run.

This is the exit-1 case ("lock could not be created"), so the run did not proceed unlocked.
The lock state was not checked: `review/lit_pipeline.lock` and `lit_pipeline.lock.d` were not read or touched.
No lock was acquired, so no release is owed (Step 7 not applicable).

## To fix for future runs (Tom's call)

1. Pre-approve Desktop Commander `start_process` for this scheduled task, **or**
2. Mount the `scripts/` folder into the session and confirm the script works from the Linux sandbox. It may not: the lock is a directory on the Mac filesystem, and the cloud routine must see the same lock.

Also note: the queue in `architecture/for_lit_search.md` was not read, so it's unknown whether items were waiting.
