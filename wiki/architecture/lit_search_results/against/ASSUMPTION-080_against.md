SEARCH-AGAINST-ASSUMPTION-080:
  Date searched: 2026-05-05
  Original item: ASSUMPTION-080
  Original statement: "Scheduled-task daemon's silent-skip is partitioned by link count (>1 fires; =1 silently skipped) — Anthropic-side bug"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-080
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-05 silent-skip diagnosis
      15b: Searched for challenging literature — alternative diagnoses (clock skew, race conditions, persistence dropouts)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Distributed-systems silent-failure literature (Gunawi et al. 2014) — silent-skip symptom matches at least four bug-classes: count-partition, clock-skew, race-condition, and persistence-dropout. Single-symptom-to-single-cause attribution is documented anti-pattern.
    2. Race-condition literature (Lu et al. 2008 "Learning from Mistakes") — race conditions in scheduling daemons produce identical silent-skip patterns; can present as count-correlated due to incidental load timing.
    3. Clock-skew / NTP-drift literature (Kuhn et al. 2014) — clock skew can produce skip patterns that correlate with arbitrary properties of the task population; coincident with link-count is plausible.
    4. Persistence-dropout literature (Vogels 2009 — eventual consistency) — datastore consistency anomalies produce skip patterns that mimic count-partitions.
    5. C2A2-internal: 2026-05-05 sample size is small (one observation across one daemon cycle); single-observation attribution to a specific bug-class is statistically weak.

  Strength of challenge: Moderate

  Summary: The bug-class is real but the specific link-count attribution rests on a single observation and excludes plausible alternatives. Race conditions, clock skew, and persistence dropouts can all present identically. Single-symptom-to-single-cause attribution is the documented anti-pattern. Stronger evidence (multiple cycles, controlled tests with single-link tasks created via different paths) is needed before the link-count attribution is supported.

  Specific risks: (a) Wrong attribution leads to wrong workaround — fireAt may bypass link-count partition but fail to bypass a race condition; (b) "Anthropic-side bug" framing forecloses local diagnosis; (c) compounds with PRESUMPTION-102's cross-path determinism claim.

  Mitigations available: (a) Multi-cycle observation before attribution; (b) controlled test with single-link tasks created via multiple creation paths; (c) check daemon logs for race / persistence signatures.

  Recommendation: PARTIALLY-CHALLENGED (bug-class supported; specific attribution warrants disambiguation)

  STEELMAN:
    Item: ASSUMPTION-080
    Strongest counterargument: One observation is one data point. The silent-skip symptom is consistent with at least four distinct bug-classes, and the literature consistently warns against single-symptom-to-single-cause attribution. The link-count partition is the simplest hypothesis that fits, but simplicity is not evidence — and committing to "Anthropic-side bug" forecloses the more likely possibility that the failure is path-dependent or race-conditioned within the user's own workflow.
    What would need to be true for C2A2 to be safe: (a) Multi-cycle observation confirming the link-count predicate; (b) controlled test with single-link tasks created via at least two distinct paths; (c) explicit ruling out of race / clock-skew / persistence alternatives.
    How to test: Create three single-link tasks via different creation paths; observe whether all three skip uniformly. If yes, link-count partition is supported. If no, path-dependent or race-conditioned alternative is more plausible.
