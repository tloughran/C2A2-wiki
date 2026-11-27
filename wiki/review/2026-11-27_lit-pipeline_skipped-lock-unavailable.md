# Lit pipeline run skipped: lock could not be acquired (2026-11-27)

**Run:** scheduled task `c2a2-lit-search-pipeline`, Cowork local session (run-id `cowork-local-2026-11-27-74a26143`)
**Outcome:** STOPPED at Step 0. Handled as the exit-1 case ("lock could not be created"). Did not run unlocked.

## What happened

- The lock script `scripts/lit_pipeline_lock.sh` has to run in a shell on the Mac.
- The only Mac shell available was Desktop Commander. Its `start_process` call was **auto-declined** because no one was there to approve it during the scheduled run.
- The Linux sandbox can't fall back to running the script. The `scripts/` folder is outside the mounted folders, which are `wiki/` and `wiki/review/` only.
- I did not hand-create `review/lit_pipeline.lock.d`, per the Step 0 rules.

## What was NOT done

- Nothing was read beyond the directory listing, and nothing was written beyond this note.
- No 15a/15b result files, no edits to the queue or the register, no 15c dispositions.
- The queue in `architecture/for_lit_search.md` was not checked. It is unknown whether any items are waiting.
- No lock was acquired, so there is nothing to release (Step 7 doesn't apply).

## To fix for future runs (one of these)

1. Pre-approve Desktop Commander `start_process` for this scheduled task, or
2. Mount the project's `scripts/` folder (or the whole project root) in this task's session so the sandbox can reach the lock script. Note: a lock taken from the Linux sandbox only coordinates with the cloud routine if both see the same `review/` directory on disk.
3. Or remove the duplicate registration, local or cloud, which is the root fix named in Step 0.
