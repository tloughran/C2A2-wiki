# Lit pipeline (15a/15b/15c) — 2026-11-19 — SKIPPED, lock unavailable

- Run ID: sched-2026-11-19-88d63535 (scheduled task `c2a2-lit-search-pipeline`, local Cowork run)
- Outcome: Step 0 could not run, so this is treated as **exit 1** (lock could not be created). Nothing else was done.

## What happened
1. The sandbox shell can't see `scripts/lit_pipeline_lock.sh`. The project's `scripts/` folder isn't a connected folder; only `wiki/` and `wiki/review/` are mounted.
2. The file Read tool refused the same path because it is outside the connected folders.
3. Desktop Commander (a real Mac shell) connected partway through the run. The `acquire` call was **auto-declined** because no one was there to approve the tool during the scheduled run.

## State observed (read-only)
- `review/lit_pipeline.lock.d` does **not** exist, so no other copy appeared to hold the lock at the time.
- I did not read or change `review/lit_pipeline.lock`.

## Written
Only this note. I did not write any result files, register appends, queue tags or backups, and did not release the lock, since it was never acquired.

## To fix (needs Tom)
This is the same failure as most runs since 2026-10-31. Either of these should fix it:
- pre-approve Desktop Commander `start_process` for scheduled runs, or
- add the project root (or `scripts/`) as a connected folder for this task.
