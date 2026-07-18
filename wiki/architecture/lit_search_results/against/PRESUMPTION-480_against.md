SEARCH-AGAINST-PRESUMPTION-480:
  Date searched: 2026-07-16
  Original item: PRESUMPTION-480
  Original statement: [inferred] Captured work is presumed non-perishable - 24 proposals pending since 07-01 (+4 today), ~29 REVISE flags pooled, and no expiry, decay, or triage rule anywhere; append-only artifacts have no vocabulary for staleness.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-480
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Extracted/inferred to intake queue (for_lit_search.md)
      15b: Searched for challenging literature; result PARTIALLY-CHALLENGED (strength Moderate)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Perishable-inventory / queueing-with-abandonment literature (perishable-inventory queueing surveys; arXiv:2308.06518): items held in a queue lose value or expire over time; the analogy maps on-hand inventory->pending proposals, patience/lifetime->relevance window.
    2. Empirical stale-issue/PR rot in OSS: aging issues and pull requests become moot or superseded; projects adopt stale-bots and triage precisely because captured work decays.

  Strength of challenge: Moderate

  Summary: Moderately challenged. Perishable-inventory theory and the empirical stale-issue literature both establish that captured-but-unprocessed work decays in value: proposals filed weeks ago may be moot or superseded, and a backlog ordered by filing date rather than remaining value systematically works the wrong items first. Append-only storage has no vocabulary for this, so staleness is invisible until re-examined.

  Specific risks: If proposals perish, the 24-item backlog is a loss already taken, and the morning priority list is mis-ordered by age rather than value.

  Mitigations available: Add an expiry/decay or freshness field; triage on remaining value; empirically re-score a sample of the 24 pending proposals against their filing-day rationale.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-480
    Strongest counterargument: An append-only capture system with no decay model does not merely risk staleness - it guarantees that its own backlog metric is meaningless, because it cannot distinguish 24 live proposals from 24 dead ones. The absence of a freshness vocabulary is not an oversight to patch but a structural inability to measure whether captured work is still worth doing.
    What would need to be true for C2A2 to be safe: The pending proposals' value would have to be genuinely time-invariant (a fix proposed 07-01 is exactly as valuable today) - contradicted by superseding events since.
    How to test: Re-score a random sample of the 24 pending proposals against current state; report the moot/superseded fraction.
