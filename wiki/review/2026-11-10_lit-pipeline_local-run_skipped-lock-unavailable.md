# Lit pipeline (15a/15b/15c): local run skipped, lock could not be acquired

- **Date:** 2026-11-10, about 00:33 EST (05:33Z)
- **Run ID:** cowork-local-2026-11-10 (local Cowork scheduled run)
- **Outcome:** STOPPED at Step 0, treated as exit 1. Nothing else was written: no result files, no register appends, no queue tags, no backups. The queue was not opened.

## Why

- The Mac shell call (Desktop Commander `start_process` running `scripts/lit_pipeline_lock.sh acquire`) was **declined automatically**, because nobody was there to approve it during the scheduled run.
- The sandbox shell cannot reach `RC Karpathy Wiki Project/scripts/`. Only `wiki/` and `wiki/review/` are mounted.

Step 0 says "do not run unlocked", so this run stopped. This is the same failure as 11-07, 11-08 and 11-09.

## Context (informational only, not used to decide whether to run)

- No `review/lit_pipeline.lock.d` directory was present.
- The last audit-trail entry is `cloud-lit-2026-11-09` RELEASED. The cloud copy normally locks at about 05:40Z, so it had probably not run yet when this run started.

## Still open (carried from the 11-09 note)

- On 11-08 and 11-09 the cloud copy logged "manual append; script unavailable". It writes audit lines but never creates `lit_pipeline.lock.d`, so the two copies do not actually exclude each other.
- The fix is still to remove one registration. Otherwise, to keep the local copy, pre-approve Desktop Commander `start_process` for scheduled runs (or mount `scripts/`). If the cloud copy is the one being kept, disable this local task so these daily skip notes stop.
