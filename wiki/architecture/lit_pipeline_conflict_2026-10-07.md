# Lit-pipeline conflict note — 2026-10-07

Scheduled run of `c2a2-lit-search-pipeline` (second instance) started ~04:36Z and found `architecture/lit_pipeline.lock` in state LOCKED (written 2026-10-07 04:34Z by another c2a2-lit-search-pipeline run; batch PRESUMPTION-896, PRESUMPTION-897, ASSUMPTION-1244, ASSUMPTION-1303, ASSUMPTION-508). Not RELEASED, ~2 min old (< 6 h).

Per the lock file's convention this instance wrote NO registers (for_lit_search.md, lit_search_returns.md, monitor_queue.md, revision_flags.md, validated_premises.md untouched) and no lit_search_results files, and exited.

Queue state at read time (queue_scan.py): 0 searched-by-both-undispositioned, 0 half-searched, 142 bare [QUEUED] literature-lane backlog items; no new 14a/14b intake since 2026-10-03 (assumptions.md / presumptions.md last modified 2026-10-04 03:45Z).

Another instance of the duplicate-schedule problem (cf. lit_pipeline_conflict_2026-10-04.md). If the first instance fails to finish, the lock stays LOCKED and its batch stays queued; inspect/clear the lock and re-run.
