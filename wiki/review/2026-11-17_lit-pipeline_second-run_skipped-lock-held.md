# Lit pipeline run skipped: lock could not be acquired (treated as exit 1)

- **Date:** 2026-11-17
- **Run ID:** cowork-2026-11-17-a9805cf9 (scheduled Cowork run, c2a2-lit-search-pipeline)
- **Outcome:** STOPPED at Step 0. Nothing was written: no result files, no register appends, no queue tags, no backups.

## Why

Step 0 says to run `scripts/lit_pipeline_lock.sh acquire` in a shell on the Mac.

1. **Mac shell (Desktop Commander `start_process`):** the call was declined automatically because nobody was around to approve it during the scheduled run.
2. **Sandbox shell:** only `wiki/` and `wiki/review/` are mounted. `scripts/lit_pipeline_lock.sh` is outside both, so the sandbox can't reach it.

No exit code came back from the script. Per Step 0, a lock that can't be created counts as **exit 1**: do not run unlocked, write a note, stop. I did not read, create or remove `review/lit_pipeline.lock` or `lit_pipeline.lock.d` to decide whether to run.

Note: this filename uses the `second-run_skipped-lock-held` pattern that Step 0 gives. The lock was **not** known to be held. It could not be acquired.

## What would fix it (any one of these)

- Approve Desktop Commander `start_process` (or the specific lock command) for unattended scheduled runs, or
- Add the project's `scripts/` folder to this task's connected folders, so the sandbox can run the lock script, or
- Run this pipeline from the copy that can reach a Mac shell (the cloud routine or local registry entry, whichever has it), and remove the copy that can't.

## Queue status

Not checked. Step 2 comes after the lock, so the queue in `architecture/for_lit_search.md` is untouched. Any items queued by the 14a/14b run are still waiting.
