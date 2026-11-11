# Lit pipeline run skipped: lock could not be acquired

- **Date:** 2026-11-11
- **Run ID:** cowork-353fddf0-2026-11-11 (scheduled task `c2a2-lit-search-pipeline`, local Cowork registration)
- **Outcome:** STOPPED at Step 0. Treated as **exit 1** (lock could not be created). It was **not** exit 3; no other holder was seen.

## What happened

1. The run tried to start `scripts/lit_pipeline_lock.sh acquire --run-id cowork-353fddf0-2026-11-11` in a Mac shell through Desktop Commander `start_process`.
2. That tool call was **declined automatically** because no one was there to approve it during the scheduled run.
3. The run also had a Linux sandbox, but it had no fallback: the sandbox mounts only `wiki/` and `wiki/review/`, so `scripts/lit_pipeline_lock.sh` can't be reached from there.
4. Step 0 says not to run unlocked and not to create or touch `review/lit_pipeline.lock.d` by hand, so the run stopped.

## Writes this run made

Only this note. The run made no result files, register appends, queue tags or backups. It never read the queue, so whether items are queued is **unknown**.

## Fix for future runs (needs Tom)

Either:

- allow Desktop Commander `start_process` for this scheduled task without asking, or
- mount the project-root `scripts/` folder in the Cowork session, so the lock script can run in the sandbox. Check first that the sandbox can handle the lock directory atomically on the mounted filesystem.

Separately: two copies of this task are still registered (local + cloud). Removing one is still the real fix.
