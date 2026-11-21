# Lit pipeline (15a/15b/15c): run skipped, lock not acquired

- **Date:** 2026-11-21 (≈05:33 UTC)
- **Run ID:** cowork-1582da46-2026-11-21 (scheduled task `c2a2-lit-search-pipeline`, local Cowork registration)
- **Outcome:** STOPPED at Step 0. Treated as **exit 1**: the lock could not be created.

## What happened
- Step 0 says the lock script has to run in a shell on the Mac:
  `bash ".../RC Karpathy Wiki Project/scripts/lit_pipeline_lock.sh" acquire --run-id ...`
- The sandbox shell can't reach that script. Only `wiki/` and `wiki/review/` are mounted; the project-root `scripts/` folder is not.
- The Mac shell tool (Desktop Commander `start_process`) was **declined automatically**. It needs approval, and nobody was there to approve it during the scheduled run.
- So the script never ran. There's no exit code, and I don't know whether another copy held the lock.

## What was NOT done
- No agent definitions or queue read. No searches.
- No result files, register appends, queue tags or backups written.
- `review/lit_pipeline.lock` (audit trail) and `review/lit_pipeline.lock.d` were not read, created or touched.
- Nothing to release at Step 7, because no lock was acquired.

## To fix for future runs
Pick one:
1. Pre-approve Desktop Commander `start_process` for this scheduled task (a narrow approval: just this script), or
2. Mount the project-root `scripts/` folder in the task's session so the sandbox shell can run the lock script. The lock dir lives under `wiki/review/`, which is already mounted.

Separately, it's still open which of the two registrations (local vs cloud) to remove.
