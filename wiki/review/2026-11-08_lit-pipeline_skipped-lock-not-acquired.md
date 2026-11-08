# Lit pipeline (15a/15b/15c): run skipped, lock not acquired

- **Date:** 2026-11-08
- **Run ID:** cowork-755019c1-2026-11-08
- **Trigger:** scheduled task `c2a2-lit-search-pipeline` (Cowork / local registry copy)
- **Outcome:** STOPPED at Step 0. Nothing else was read or written.

## What happened
Step 0 says to run `scripts/lit_pipeline_lock.sh acquire` in a shell on the Mac.

- The Cowork sandbox shell can't see `scripts/`. Only `wiki/` and `wiki/review/` are mounted.
- The Mac shell (Desktop Commander `start_process`) was **auto-declined**, because no one was there to approve the tool call during the scheduled run.

The lock script never ran, so there is no exit code. Under the exit-1 rule ("do not run unlocked"), this run stopped here.

## Not done
- Nothing past Step 0: no queue read, no 15a/15b/15c searches, no result files, no register appends, no queue tags.
- No lock release. This run never held the lock.
- The lock directory and the audit trail were not inspected.

## Pattern
This is the same failure as 2026-10-31 and 2026-11-02 through 11-07. The local copy has not been able to run the pipeline for over a week. Any progress depends on the cloud routine copy.

## To fix for future runs
Do one of these:
1. Pre-approve Desktop Commander `start_process` for this scheduled task, so it can run the lock script on the Mac.
2. Mount the project's `scripts/` folder (or the whole project root) in this task's Cowork session.
3. If the cloud routine is meant to be the one that runs, delete this local registration.
