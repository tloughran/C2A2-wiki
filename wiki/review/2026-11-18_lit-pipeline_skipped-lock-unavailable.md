# Lit pipeline (15a/15b/15c): skipped because the lock was unavailable, 2026-11-18

- Run ID: local-cowork-2026-11-18-60af000d (scheduled Cowork run, no user present)
- Outcome: **Stopped at Step 0 (the exit-1 branch).** Nothing was searched, written, tagged or backed up.
- Why the lock was unavailable:
  - The sandbox shell can't reach `scripts/lit_pipeline_lock.sh`. The project-root `scripts/` folder isn't mounted; only `wiki/` and `wiki/review/` are.
  - Desktop Commander's `start_process` would have given a Mac shell, but it was **auto-declined** because nobody was there to approve it.
- This run never acquired the lock, so it released nothing. The queue (`architecture/for_lit_search.md`) was not read.
- Note: I listed `review/` and tailed `lit_pipeline.lock` while working out the format for this note. That tail shows `cloud-lit-2026-11-18` locked and released at 05:40:21Z with an empty queue. I did not use it to decide whether to run; that decision came from the failed acquire alone.

## To unblock future runs (pick one)
1. Pre-approve Desktop Commander `start_process` for this scheduled task.
2. Or mount the project root (or `scripts/`) in the task's folders.
3. Or remove the local registration. The cloud routine is completing the runs: it ran on 11-16, 11-17 and 11-18. Each local firing since about 10-31 has only produced a skip note like this one.
