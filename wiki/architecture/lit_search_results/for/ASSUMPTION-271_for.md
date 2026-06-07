SEARCH-FOR-ASSUMPTION-271:
  Date searched: 2026-06-05
  Original item: ASSUMPTION-271
  Original statement: The PROCESSED_LOG canonical ingest backlog is 36 files; the divergent 152 from a naïve filename diff is a format artifact (per-file rows mixed with batch narratives), not 116 extra un-ingested files.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-271
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated claim that the 36-vs-152 PROCESSED_LOG divergence is a mixed-format counting artifact, not lost/un-ingested files.
      15a: Searched log-as-system-of-record design, event-sourcing/audit-log distinctions, and whether a canonical count is recoverable from a mixed-format operational log.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Fowler, M. "Event Sourcing." martinfowler.com (EAA Dev). — An append-only log can serve as the authoritative system of record, with current state derived (folded) from the event sequence rather than stored redundantly. Supports the principle that the "true" count is a derived projection over the log, so a raw line/filename count can legitimately diverge from the canonical count without implying loss.
    2. Lemaire, A. "Event Sourcing, Audit Logs, and Event Logs." Sunday/Medium, 2026. — Explicitly distinguishes records that capture state changes from records that capture what was attempted/narrated; the two are different projections of the same history. Grounds the claim that per-file ingest rows and batch narratives are heterogeneous record types whose naïve union over-counts.
    3. Microsoft Learn / Azure Architecture Center. "Event Sourcing Pattern." — Canonical guidance that the materialized count of entities is reconstructed deterministically from the log; a divergent number from a different read is expected when the read does not respect record semantics. Supports recoverability-in-principle of the canonical 36.

  Strength of support: Moderate

  Summary: The log-as-system-of-record literature supports the structural half of the assumption: an operational log routinely mixes heterogeneous record kinds (per-item rows vs. batch narratives), so a naïve line/filename diff is a different and generally inflated projection than the canonical entity count. The event-sourcing principle that "current state is a deterministic fold over the log" means the canonical 36 is recoverable-in-principle if the fold rules are applied correctly. What the literature does NOT supply is the empirical fact that 36 (not some number between 36 and 152) is the correct fold for THIS log — that requires an actual reconciliation pass, not a theoretical argument.

  Caveats: Support is for the mechanism (mixed-format logs over-count under naïve diffs and canonical counts are derivable), not for the specific figure. The same literature insists the canonical count be demonstrated by an explicit, rule-respecting reconciliation; asserting 36 without running that fold is exactly the gap 15b targets. Domain transfer is clean (general log/record design), so no transfer discount applies.

  Recommendation: PARTIALLY-SUPPORTED
