# Decisions — 2026-06-23

Email approved all 7 *positions* (PROP-2026-06-23-001…007). Those are positional
IDs from the review page's JS `pids` array (known generator bug: the decision
template emits position IDs, not the cards' stable proposal_ids). Recovered the
true targets by card order from the quarantined review HTML
(`review/_deleted_quarantine/2026-06-23_review.html`). Position N → card N:

- pos 001 -> card 1 -> PROP-2026-06-19-002 (Arkani-Hamed, Surfaceology): APPROVE -> approved/ + queued for ingest
- pos 002 -> card 2 -> PROP-2026-06-19-001 (Carroll, Quantum Cyclic Universe): APPROVE -> approved/ + queued for ingest
- pos 003 -> card 3 -> PROP-2026-06-21-001 (Rohr, A New Way of Living): APPROVE -> approved/ + queued for ingest
- pos 004 -> card 4 -> PROP-2026-06-22-002 (Friston, As One and Many): APPROVE -> approved/ + queued for ingest
- pos 005 -> card 5 -> PROP-2026-06-22-001 (Levin, Cognitive Glue): APPROVE-by-position but **routed to denied/** — exact duplicate of approved+ingested PROP-2026-06-01-001 (same DOI 10.1177/25763113261454327, same source-date 2026-05-27). Do NOT re-ingest / do NOT re-count. Duplicate guard overrides bulk-approve.
- pos 006 -> card 6 -> PROP-2026-06-23-002 (Hawkins, Thousand Brains NeCo): APPROVE — already moved to approved/+inbox on the 06-23 partial run.
- pos 007 -> card 7 -> PROP-2026-06-23-001 (Hoffman, DMT / Traces of the Other): APPROVE — already moved to approved/+inbox on the 06-23 partial run.

**Correction note (2026-06-27 run):** the original 06-23 archive entry mis-mapped the
literal email strings to stable proposal_ids (matched only Hoffman -001 and Hawkins
-002; logged 003–007 as "no proposal file found"). That left the 5 carried proposals
stranded in pending/. This run recovered them by card order and routed them correctly:
4 approved + ingest-queued, 1 (Levin dup) denied.
