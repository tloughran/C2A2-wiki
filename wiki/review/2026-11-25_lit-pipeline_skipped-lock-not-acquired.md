# Lit pipeline (15a/15b/15c) — 2026-11-25 run SKIPPED: lock not acquired

**Run ID:** cowork-1582da46-2026-11-25
**Outcome:** Stopped at Step 0. Nothing was committed.

## What happened
- Step 0 says to acquire the lock with `scripts/lit_pipeline_lock.sh acquire` in a shell on the Mac.
- The sandbox shell can't reach `RC Karpathy Wiki Project/scripts/`. Only `wiki/` and `wiki/review/` are mounted.
- Desktop Commander's `start_process` was the only way to run the script on the Mac. That call was **declined automatically** because no one was available to approve it during the scheduled run.
- Under Step 0's exit-1 rule ("lock could not be created at all"), the run did not go ahead without the lock. I did not hand-create `review/lit_pipeline.lock.d` because only the script may do that.

## What was NOT done
- No agent definitions or queue were read past this point, so I don't know what's in the queue.
- No 15a/15b result files, no `lit_search_returns.md` appends, no queue tags, no 15c dispositions.
- No lock release was needed because no lock was taken.

## To fix for future runs
Pick one:
1. Pre-approve Desktop Commander `start_process` for this scheduled task, or
2. Mount the project root (or `scripts/`) in the Cowork session so the lock script can run in the sandbox. Check first that `mkdir`-based locking on that mount is atomic enough for your needs.

Any items now [QUEUED] will carry over to the next run that gets the lock.
