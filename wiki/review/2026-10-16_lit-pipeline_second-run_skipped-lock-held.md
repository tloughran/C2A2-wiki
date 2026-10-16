
# 2026-10-16 lit-pipeline: second firing skipped, lock held

Fired ~04:36 UTC by scheduled task `c2a2-lit-search-pipeline`. review/lit_pipeline.lock was already LOCKED at 04:34:07Z by local-cowork-2026-10-16-16a1601a (host physmini02, pid 3895). The pipeline's other lock file, architecture/lit_pipeline.lock, still reads RELEASED from 2026-10-15; this firing treated the newer LOCKED file as authoritative.

Queue state seen: the bare literature items from the 2026-10-15 intake are PRESUMPTION-1149 and PRESUMPTION-1153; the 131 older bare backlog items are untouched, as declared on 10-12. The 14 [IN-HOUSE] items are not literature-lane.

Action: this firing read the queue, lock files and run notes only. It wrote nothing to the registers, queue, results or returns, and did not touch either lock. Precedent: 2026-10-03, 2026-10-08, 2026-10-13 notes, and the 2026-10-15 concurrent-run CONFLICT where honouring the lock was skipped and data was lost.

If the lock is still LOCKED with no 15c dispositions for PRESUMPTION-1149 and -1153 by mid-morning, the other run likely died and the lock is stale. Tom or the next firing should check.
