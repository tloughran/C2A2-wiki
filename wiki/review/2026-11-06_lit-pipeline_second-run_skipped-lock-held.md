# Lit pipeline run skipped — lock could not be acquired

- **Date:** 2026-11-06
- **Run ID:** cowork-62da89b5-2026-11-06 (local Cowork scheduled task `c2a2-lit-search-pipeline`)
- **Outcome:** STOPPED at Step 0. Handled as **exit 1** (the lock could not be created). Nothing was written apart from this note.

## What happened
- The Cowork Linux sandbox can't reach `RC Karpathy Wiki Project/scripts/`, because only `wiki/` and `wiki/review/` are mounted. So `lit_pipeline_lock.sh` can't run there.
- I tried to run it on the Mac through Desktop Commander `start_process`. That tool call was **declined automatically**, because nobody was there to approve it during the scheduled run.
- When this run checked, the lock was **not held**: `review/lit_pipeline.lock.d` did not exist, only the `lit_pipeline.lock` audit file. So this is not a real "another copy is running" case. The lock could simply not be taken.
- I did not create `lit_pipeline.lock.d` by hand, because the task says only the script may create or remove it.

## Not done
- Steps 1–7 were not run: no agent reads, no queue check, no 15a/15b/15c results, no register appends, no queue tags.
- No release was needed (nothing was acquired), so there will be no STALE-BREAK.

## To make this run work in future
Pick one:
1. Approve Desktop Commander `start_process` for this scheduled task, so it can run the lock script on the Mac.
2. Mount the `scripts/` folder (or the project root) in this task's Cowork session, so the sandbox can run the script.
3. If the cloud routine is the copy you want to keep, remove this local registration.
