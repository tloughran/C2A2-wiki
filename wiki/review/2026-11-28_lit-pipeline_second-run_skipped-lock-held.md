# Lit pipeline run skipped — lock could not be acquired (exit-1 path)

- Date: 2026-11-28
- Run ID: cowork-local-1582da46-2026-11-28 (local Cowork scheduled task `c2a2-lit-search-pipeline`)
- Outcome: STOPPED at Step 0. Nothing written: no 15a/15b/15c results, no register appends, no queue tags, no backups.

## Why
Step 0 needs `scripts/lit_pipeline_lock.sh acquire` to run in a shell on the Mac.
- The Cowork Linux sandbox has only `wiki/` and `wiki/review/` mounted. `scripts/` is outside those, so the script can't be reached from there.
- The Mac shell (Desktop Commander `start_process`) was **declined automatically**: nobody was there to approve it during the scheduled run.

So the lock could be neither acquired nor checked. That is the "exit 1 — lock could not be created" branch, so per the task this run did not proceed unlocked. I did not read or edit `review/lit_pipeline.lock` or `lit_pipeline.lock.d`. Step 7 release does not apply because no lock was taken.

Note: the filename uses the `second-run_skipped-lock-held` pattern from the task spec, but the lock was **not known to be held**. This is the could-not-acquire case.

## To fix for future runs (one of)
1. Pre-approve Desktop Commander `start_process` for this scheduled task, or
2. Mount the project root (or `scripts/`) in the task's Cowork folders so the sandbox can run the script, or
3. Rely on the cloud routine copy and remove this local registration (which also resolves the duplicate-firing issue the lock exists for).

The queue in `architecture/for_lit_search.md` was not inspected. Any [QUEUED] items are still pending.
