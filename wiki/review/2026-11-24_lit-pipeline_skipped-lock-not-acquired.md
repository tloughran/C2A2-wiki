# Lit pipeline (15a/15b/15c) — run skipped, lock not acquired

- **Date:** 2026-11-24
- **Run ID:** cowork-2cdf9f69-2026-11-24 (scheduled task `c2a2-lit-search-pipeline`, Cowork local run)
- **Outcome:** STOPPED at Step 0. Nothing was written to the wiki apart from this note.

## What happened

Step 0 says to run `scripts/lit_pipeline_lock.sh acquire` in a shell on the Mac. In this run:

1. **Mac shell (Desktop Commander `start_process`):** the tool call was auto-declined because no one was there to approve it during the scheduled run. The lock script never ran, so there is no exit code.
2. **Sandbox shell:** `RC Karpathy Wiki Project/scripts/` isn't mounted in the sandbox (only `wiki/` and `wiki/review/` are), so the script couldn't run there either.

I treated this as **exit 1 (lock could not be created)** and did not run unlocked. I also didn't create or touch `review/lit_pipeline.lock.d` or `review/lit_pipeline.lock` by hand, because the task says only the script may do that.

## Not done

- The queue (`architecture/for_lit_search.md`) wasn't read. I don't know whether any items are [QUEUED].
- No 15a, 15b or 15c results, no returns, no register appends, no queue tags.
- No lock release (none was acquired, so there will be no STALE-BREAK from this run).

## To fix for future runs

Either:

- **pre-approve** Desktop Commander `start_process` for this scheduled task, so the lock script can run on the Mac; or
- **mount** the `RC Karpathy Wiki Project/scripts/` folder (or the project root) into Cowork, so the lock script can run in the sandbox against the mounted `wiki/review/`.

If the cloud copy of this routine ran today, its results are the only output for 2026-11-24.
