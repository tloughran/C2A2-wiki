# Lit pipeline (15a/15b/15c): run skipped, lock not acquired

- **Date:** 2026-11-14
- **Run ID:** sched-2026-11-14-local-143b697d (Cowork scheduled run of `c2a2-lit-search-pipeline`)
- **Outcome:** Treated as Step 0 **exit 1** (lock could not be created). Nothing was written apart from this note.

## What happened
Same failure as 2026-11-12 and 2026-11-13.

1. **Desktop Commander `start_process`** (the Mac shell): the `lit_pipeline_lock.sh acquire` call was **declined automatically**, because nobody was there to approve it during the scheduled run.
2. **The Cowork Linux sandbox** can't reach `scripts/`, because only `wiki/` and `wiki/review/` are mounted. It also isn't a shell on the Mac.

I didn't run unlocked. I didn't read, create or edit `review/lit_pipeline.lock` or `review/lit_pipeline.lock.d`. I only listed `review/` and read yesterday's note.

## Not done
- No agent definitions read, queue not checked, no 15a/15b/15c work, no result files, register appends or queue tags.
- No Step 7 release, because no lock was taken.

## To fix (pick one)
- Approve Desktop Commander `start_process` for this scheduled task, **or**
- Remove the duplicate registration and drop or relax Step 0 for the copy that remains.

This Cowork copy has done no pipeline work since at least 2026-10-31, so it has now gone 15 days without processing the queue.
