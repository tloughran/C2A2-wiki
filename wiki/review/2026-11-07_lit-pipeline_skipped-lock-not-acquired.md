# Lit pipeline (15a/15b/15c) — run skipped: lock not acquired

- **Date:** 2026-11-07 (~05:34 UTC)
- **Run ID:** cowork-353fddf0-20261107T0534Z
- **Trigger:** scheduled task `c2a2-lit-search-pipeline` (Cowork / local registry copy)
- **Outcome:** STOPPED at Step 0. Nothing else read or written.

## What happened
Step 0 requires running `scripts/lit_pipeline_lock.sh acquire` in a shell on the Mac.

- The Cowork sandbox shell cannot see `scripts/` (only `wiki/` and `wiki/review/` are mounted).
- The Mac shell (Desktop Commander `start_process`) was **auto-declined**: no one was present to approve the tool call during the scheduled run.

So the lock script never ran and no exit code was obtained. Per the task's exit-1 rule ("do not run unlocked"), this run stopped here.

## Not done
- No queue read, no 15a/15b/15c searches, no result files, no register appends, no queue tags.
- No lock release. This run never held the lock, so there was nothing to release.
- The lock directory and the audit trail were not inspected (the task forbids using them to decide whether to run).

## To fix for future runs
Pick one:
1. Pre-approve Desktop Commander `start_process` for this scheduled task, so it can run the lock script on the Mac.
2. Mount the project's `scripts/` folder (or the whole project root) in this task's Cowork session.

If the cloud routine copy ran today, its output is unaffected by this run.
