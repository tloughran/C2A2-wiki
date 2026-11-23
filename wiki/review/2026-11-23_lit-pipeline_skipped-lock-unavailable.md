# Lit pipeline (15a/15b/15c): run skipped, lock not acquired

- **Date:** 2026-11-23
- **Run ID:** cowork-local-2026-11-23-b1facb29 (scheduled task `c2a2-lit-search-pipeline`, local Cowork registration)
- **Outcome:** STOPPED at Step 0. Treated as **exit 1**: the lock could not be created.

## What happened
- The sandbox shell can't reach `scripts/lit_pipeline_lock.sh`. Only `wiki/` and `wiki/review/` are mounted, not the project-root `scripts/`.
- The Mac shell (Desktop Commander `start_process`) was **declined automatically** because no one was there to approve it.
- So the script never ran. There was no exit code.

## What was NOT done
- No agent definitions or queue read. No searches run.
- No result files, register appends, queue tags or backups written.
- `review/lit_pipeline.lock` and `review/lit_pipeline.lock.d` were not touched. I only read the audit trail.
- Nothing to release at Step 7.

## Context from the audit trail (read only)
The cloud registration (`cloud-lit-YYYY-MM-DD`) has locked and released cleanly every day from 11-15 to 11-22. It is doing the pipeline's work. Its entries say "manual append; script unavailable". So the cloud copy also isn't running the lock script; it writes to the audit file by hand. That means the lock directory does not actually serialize the two copies. It works today only because this local copy always stops at Step 0.

## To fix (unchanged)
1. Remove the local registration, since the cloud copy does the work, or
2. Pre-approve Desktop Commander `start_process` for this script, or mount the project-root `scripts/` folder in this task's session.
