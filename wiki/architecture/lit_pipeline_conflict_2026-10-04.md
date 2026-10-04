# Lit-pipeline conflict note — 2026-10-04

Scheduled run of `c2a2-lit-search-pipeline` (second instance) started ~04:36Z and found `architecture/lit_pipeline.lock` in state LOCKED (written 2026-10-04 04:33:56Z by another c2a2-lit-search-pipeline run; scope 10-03 intake — PRESUMPTION-1110..1113 + 7 [IN-HOUSE] items). It is not RELEASED and is ~2.5 min old (< 6 h).

Per the lock file's own convention, this instance wrote NO registers (for_lit_search.md, lit_search_returns.md, monitor_queue.md, revision_flags.md, validated_premises.md untouched) and no lit_search_results files, and exited.

Observed queue at read time (04:36Z): PRESUMPTION-1110, 1111, 1112, 1113 bare [QUEUED] (no SEARCHED tags yet); 7 [IN-HOUSE] items (ASSUMPTION-1743/1744/1745/1746/1750/1752, PRESUMPTION-1114) unrouted.

This is another instance of the duplicate-schedule problem (cf. PRESUMPTION-1106 / REVISE-502, PRESUMPTION-1110): two registrations of the same task fire concurrently. If the first instance fails to finish, the lock will remain LOCKED and the items stay queued; re-run after clearing/inspecting the lock.
