# Lit pipeline run skipped: run lock unavailable (2026-11-03)

**Run:** scheduled task `c2a2-lit-search-pipeline`, Cowork session 54ab6ac4 (automated, no user present)
**Outcome:** STOPPED at Step 0. Nothing else was written.

## What happened

- Step 0 says to run `scripts/lit_pipeline_lock.sh acquire` in a shell on the Mac.
- The only Mac shell available was Desktop Commander `start_process`. That call was **declined automatically** because no one was there to approve it during the scheduled run.
- The sandbox shell cannot reach the script either. Only `wiki/` and `wiki/review/` are mounted, and `scripts/` sits outside them.
- That makes this the **exit 1 case** ("lock could not be created at all"). The task says not to run unlocked, so this run did not.

## Not touched

- No 15a/15b result files, no `lit_search_returns.md` appends, no queue tags, no 15c dispositions, no backups.
- I did not read, move or edit `review/lit_pipeline.lock` or `review/lit_pipeline.lock.d`.
- I did not read the queue, so I don't know whether any items were waiting.

## To fix for future runs

Do one of these:

1. Pre-approve Desktop Commander `start_process` for this scheduled task, or
2. Connect the project root (or `scripts/`) as a folder so the sandbox shell can run the lock script.

Item 2 assumes the lock script works from the sandbox and against the mounted path. That hasn't been tested.
