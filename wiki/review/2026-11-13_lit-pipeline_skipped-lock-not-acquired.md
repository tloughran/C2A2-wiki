# Lit pipeline (15a/15b/15c): run skipped, lock not acquired

- **Date:** 2026-11-13
- **Run ID:** local-cowork-2026-11-13-4c12e2bd (Cowork scheduled run of `c2a2-lit-search-pipeline`)
- **Outcome:** Treated as Step 0 **exit 1** (lock could not be created). Nothing was written apart from this note.

## What happened
This is the same failure as 2026-11-12 and the earlier `skipped-lock-unavailable` / `lock-not-acquired` notes.

1. **Desktop Commander `start_process`** (the Mac shell): the `lit_pipeline_lock.sh acquire` call was **declined automatically**, because nobody was there to approve it during the scheduled run.
2. **The Cowork Linux sandbox**: only `wiki/` and `wiki/review/` are mounted. `scripts/` is outside that, so the sandbox can't reach the lock script. It also isn't a shell on the Mac.

Because I couldn't get the lock, I didn't run unlocked. I didn't read, create or edit `review/lit_pipeline.lock` or `review/lit_pipeline.lock.d`. I only listed the `review/` directory to see earlier notes.

## Not done
- No agent definitions read, queue not checked, no 15a/15b/15c searches, no result files, no register appends, no queue tags.
- No release call (Step 7), because no lock was taken.

## To fix for future runs (pick one)
- Approve Desktop Commander `start_process` for this scheduled task, so it can run the lock script without anyone present, **or**
- Remove the duplicate registration so that only one copy fires, and drop or relax Step 0 for the copy that remains.

This Cowork copy hasn't done any pipeline work since at least 2026-10-31. If the cloud copy isn't processing the queue either, items in `architecture/for_lit_search.md` have been sitting unsearched for about two weeks.
