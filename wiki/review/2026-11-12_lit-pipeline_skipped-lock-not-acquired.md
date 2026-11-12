# Lit pipeline (15a/15b/15c): run skipped, lock not acquired

- **Date:** 2026-11-12
- **Run ID:** cowork-1582da46-2026-11-12 (Cowork scheduled run of `c2a2-lit-search-pipeline`)
- **Outcome:** Treated as Step 0 **exit 1** (lock could not be created). Nothing was written apart from this note.

## What happened
Step 0 says to run `scripts/lit_pipeline_lock.sh acquire` in a shell on the Mac. This session has two shells:

1. **Desktop Commander `start_process`** (the Mac shell): the call was **declined automatically**, because nobody was there to approve the tool during the scheduled run.
2. **The Cowork Linux sandbox**: only `wiki/` and `wiki/review/` are mounted. `scripts/` is outside `wiki/`, so the sandbox can't reach the lock script. It also isn't a shell on the Mac.

Because I couldn't get the lock, I didn't run unlocked, as Step 0 requires. I didn't read, create or edit `review/lit_pipeline.lock` or `review/lit_pipeline.lock.d`.

## Not done
- No agent definitions read, queue not checked, no 15a/15b/15c searches, no result files, no register appends, no queue tags.
- No release call (Step 7), because no lock was taken.

## To fix for future runs (pick one)
- Approve Desktop Commander `start_process` for this scheduled task, so it can run the lock script on the Mac without anyone present, **or**
- Remove the duplicate registration (local or cloud) so that only one copy fires. Then decide whether this Cowork copy should keep running.

If the cloud copy fired today, today's queue may already have been processed there. Check `architecture/for_lit_search.md` for `[SEARCHED-15a: 2026-11-12]` tags.
