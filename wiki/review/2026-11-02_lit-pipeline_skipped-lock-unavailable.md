# Lit pipeline run skipped — lock could not be acquired (2026-11-02)

**Run ID:** cowork-1771f220-2026-11-02 (Cowork scheduled run, `c2a2-lit-search-pipeline`)
**Outcome:** STOPPED at Step 0. Treated as exit 1 (lock could not be created). Nothing was written except this note.

## What happened
- The Mac shell call `bash ".../RC Karpathy Wiki Project/scripts/lit_pipeline_lock.sh" acquire --run-id cowork-1771f220-2026-11-02` (via Desktop Commander) was **automatically declined**: approval was needed and nobody was there to give it.
- The sandbox shell can't reach the script. `scripts/` sits next to `wiki/` and isn't a mounted folder (checked: `wiki/../scripts` does not exist in the sandbox), so there was no fallback.
- The lock state was not checked. Per Step 0, nothing here reads or edits `review/lit_pipeline.lock` or `lit_pipeline.lock.d`.

## Not done
- No queue read, no 15a/15b/15c searches, no result files, no register appends, no queue tags.
- No lock was acquired, so no release was run (and none is owed).

## Pattern
This is the third lock-unavailable skip in four days (10-31, 11-01, 11-02). Every Cowork firing will skip the same way until one of the fixes below is made.

## To fix for future runs (pick one)
1. Allow Desktop Commander `start_process` for this scheduled task (permanent approval), or
2. Connect the `RC Karpathy Wiki Project/scripts` folder (or the whole project root) to the Cowork session so the sandbox can run the script.

Any items queued in `architecture/for_lit_search.md` are still waiting for the next run.
