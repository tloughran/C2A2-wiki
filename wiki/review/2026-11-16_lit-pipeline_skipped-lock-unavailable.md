# Lit pipeline (15a/15b/15c) — skipped, lock unavailable — 2026-11-16

- Run ID: cowork-1582da46-2026-11-16 (scheduled Cowork run, no user present)
- Outcome: **STOP per Step 0, exit-1 branch.** Nothing was searched, written, tagged or backed up.
- Why: The sandbox shell can't reach `scripts/lit_pipeline_lock.sh`, because the project-root `scripts/` folder isn't mounted (only `wiki/` and `wiki/review/` are). Desktop Commander connected and offered a Mac shell. Its `start_process` call was **auto-declined** because nobody was there to approve it during the scheduled run.
- I did not read or touch the lock state (`lit_pipeline.lock` / `lit_pipeline.lock.d`). I did not release anything, because this run never acquired the lock.
- Queue (`architecture/for_lit_search.md`) was not read.

## To unblock future runs (pick one)
1. Pre-approve Desktop Commander `start_process` for this scheduled task, so the lock script can run on the Mac.
2. Or mount the project root (or `scripts/`) in the task's folders, so the sandbox shell can run the script.
3. Remove one of the two registrations (local vs cloud), as Step 0 already anticipates.

This is the latest in a run of daily skips going back to about 2026-10-31.
