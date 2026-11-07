# Lit pipeline run skipped: run lock unavailable (2026-11-07)

**Run:** scheduled task (15a/15b/15c pipeline), Cowork session, automated, no user present
**Outcome:** NOT RUN. Only this note was written.

- The lock script (`scripts/lit_pipeline_lock.sh`) is outside the mounted folders (`wiki/`, `wiki/review/`), and no approvable shell was available, so the run lock could not be taken.
- The cloud copy of this pipeline fires about 05:40Z (the same time as this run). Running unlocked risks the concurrent-run conflict seen on 2026-10-15, so I did not.
- Queue as seen: 1 literature-lane item waiting (PRESUMPTION-1222), plus [IN-HOUSE] items that this pipeline does not search. Last lock line: RELEASED 2026-11-06T05:41:03Z by cloud-lit-2026-11-06.
- Not touched: queue, results, returns, monitor/validated/revision registers, lock files.

Fix: mount `scripts/` (or the project root) for this task, or pre-approve Desktop Commander `start_process`, or retire this local registration if the cloud copy is the one to keep.
