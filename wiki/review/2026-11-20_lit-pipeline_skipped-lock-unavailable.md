# Lit pipeline (15a/15b/15c) — run skipped: lock could not be acquired

- **Date:** 2026-11-20
- **Run ID:** cowork-sched-2026-11-20-9c1cdd18 (scheduled Cowork run, no user present)
- **Outcome:** STOPPED at Step 0. Nothing was written: no result files, register appends, queue tags or backups. This note is the only write.

## What happened

1. The Linux sandbox can't run `scripts/lit_pipeline_lock.sh`. Only `wiki/` and `wiki/review/` are mounted there, and `scripts/` sits outside them.
2. Desktop Commander, the Mac shell, was available. The call to `lit_pipeline_lock.sh acquire` was **declined automatically**, because nobody was there to approve the tool permission during the scheduled run.
3. Without the lock script there's no exit code to branch on. Step 0 says not to run unlocked and not to hand-edit `review/lit_pipeline.lock` or the `lit_pipeline.lock.d` directory. So I treated this as the exit-1 case and stopped.

I did not read the queue (`for_lit_search.md`), so I don't know whether any items were waiting.

## Observed (read-only)

- `review/lit_pipeline.lock` (audit trail) was last modified 2026-11-19 00:43. I did not inspect whether `lit_pipeline.lock.d` exists.

## To fix for future runs (Tom's choice)

- Approve Desktop Commander `start_process` for this scheduled task, so the lock script can run on the Mac; **or**
- Mount the project's `scripts/` folder (or the project root) into the Cowork session so the sandbox can reach the script. Check first that the script's `mkdir`-based lock works across the mount. **Or**
- Remove the duplicate registration (local vs cloud routine) so the lock is less critical.

No lock was taken, so none needs releasing (Step 7 not applicable).
