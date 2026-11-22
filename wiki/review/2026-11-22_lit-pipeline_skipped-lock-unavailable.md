# Lit pipeline (15a/15b/15c): run skipped, lock not acquired

- **Date:** 2026-11-22
- **Run ID:** cowork-local-2026-11-22-7ef9be40 (scheduled task `c2a2-lit-search-pipeline`, local Cowork registration)
- **Outcome:** STOPPED at Step 0. Treated as **exit 1**: the lock could not be created.

## What happened
- The sandbox shell can't reach `scripts/lit_pipeline_lock.sh`. Only `wiki/` and `wiki/review/` are mounted, not the project-root `scripts/`.
- The Mac shell (Desktop Commander `start_process`) was **declined automatically** because no one was there to approve it.
- So the script never ran. No exit code, and it's unknown whether another copy held the lock.

## What was NOT done
- No agent definitions or queue read, and no searches run.
- No result files, register appends, queue tags or backups written.
- `review/lit_pipeline.lock` and `review/lit_pipeline.lock.d` were not touched.
- Nothing to release at Step 7.

## Recurring
This is the same failure as on most days since 2026-10-31 (notes for lock-unavailable or not-acquired exist for nearly every day). On 11-06, 11-11 and 11-17 the notes say lock-held instead, so the other registration may have run on those days. I did not check whether it did.

## To fix (unchanged)
1. Pre-approve Desktop Commander `start_process` for this task, limited to this script, or
2. Mount the project-root `scripts/` folder in the task's session.

Still open: which of the two registrations (local or cloud) to remove.
