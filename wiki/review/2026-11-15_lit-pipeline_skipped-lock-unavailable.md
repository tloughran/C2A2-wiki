# Lit pipeline (15a/15b/15c) — run skipped: lock could not be acquired

- **Date:** 2026-11-15
- **Run ID:** cowork-1582da46-20261115 (Cowork scheduled task `c2a2-lit-search-pipeline`)
- **Outcome:** STOPPED at Step 0 — treated as exit 1 (lock could not be created). Nothing committed.

## What happened
1. The lock script `scripts/lit_pipeline_lock.sh` lives outside the folders mounted in this session (only `wiki/` and `wiki/review/` are mounted), so the sandbox shell cannot run it.
2. The only Mac-side shell available (Desktop Commander `start_process`) was **auto-declined**: no one was present to approve the tool during the scheduled run.
3. No exit code was obtained, so ownership of `review/lit_pipeline.lock.d` was never established.

## What was NOT done (per Step 0 rules)
- No result files, register appends, queue tags, or backups written.
- `for_lit_search.md` not read; queue state unknown.
- `review/lit_pipeline.lock` (audit trail) and `lit_pipeline.lock.d` not touched.
- No release call (nothing was acquired).

## To fix for future runs
- Pre-approve Desktop Commander `start_process` for this scheduled task, **or**
- Mount the project root (or `scripts/`) in the task so the sandbox shell can run the lock script — note the script must still operate on the real `wiki/review/` path for the lock to be meaningful across the local and cloud copies.
- Separately (from the task file): remove one of the two duplicate registrations.
