# Lit pipeline (15a/15b/15c) — local run skipped, lock could not be acquired

- **Date:** 2026-11-09
- **Run ID:** cowork-ae281aeb-2026-11-09 (local Cowork scheduled run)
- **Outcome:** STOPPED at Step 0. Nothing else was written: no result files, no register appends, no queue tags, no backups.

## Why

Step 0 says to run `scripts/lit_pipeline_lock.sh acquire` in a shell on the Mac. This run could not do that:

- The Mac shell tool (Desktop Commander `start_process`) was **declined automatically**, because nobody was there to approve it during the scheduled run.
- The sandbox shell cannot reach `RC Karpathy Wiki Project/scripts/`. Only `wiki/` and `wiki/review/` are mounted.

Under the Step 0 rules ("exit 1: do not run unlocked"), the run stopped.

## Context (read-only, informational — not used to decide whether to run)

- `review/lit_pipeline.lock.d` does not exist, so nobody holds the lock right now.
- The audit trail shows the cloud copy already ran today: `cloud-lit-2026-11-09`, LOCKED 05:40:45Z and RELEASED 05:42:19Z. It processed ASSUMPTION-2067 and PRESUMPTION-1227/-1228, which became MONITOR-710..712. Today's queue was probably handled, but this run did not open the queue to check.

## Defect worth your attention

The cloud runs on 11-08 and 11-09 logged "**manual append; script unavailable**". They wrote lines to the audit log but never created `lit_pipeline.lock.d`. So the cloud copy does not actually take the lock. If the local copy ever gets shell approval, the two copies are **not** mutually excluded, which is the 10-01 / 10-15 collision risk again.

## Options

1. Remove one of the two registrations. This is the real fix, and Step 0 calls itself a stopgap until it happens.
2. If the local copy should run, pre-approve Desktop Commander `start_process` for scheduled runs, or mount `scripts/`.
3. Give the cloud routine access to the lock script, so its lock is real and not just a log line.
