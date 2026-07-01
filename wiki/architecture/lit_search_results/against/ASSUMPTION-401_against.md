SEARCH-AGAINST-ASSUMPTION-401:
  Date searched: 2026-07-01
  Original item: ASSUMPTION-401
  Original statement: "Cross-tradition routing into master/cross_program_index.md can be deferred out of the first commit without harming ingestion."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-401
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-30 staged-commit plan
      15b: Searched for challenging literature (genuine web search 2026-07-01)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Staged-rollout consistency literature — deferring a downstream artifact opens a temporary inconsistency window: the cross_program_index lags its sources, so anything reading the index (or a human trusting it) sees an incomplete cross-tradition picture until backfill.
    2. Push-debt / deferred-work pattern (C2A2-internal REVISE-150, PRESUMPTION-424) — "defer out of the first commit" is the same shape as deferred pushes: the deferred step is prone to being forgotten and accumulating, not harmlessly waiting.
    3. Index/view divergence risk — an index that is out of sync with content is worse than no index in one respect: it can be silently trusted as complete when it is not (cf. the freshness-mislead family, REVISE-158).

  Strength of challenge: Weak-Moderate

  Summary: "Without harming ingestion" is probably true (ingestion reads vault+git per A-399), but "without harm" full stop is not: the deferral creates a divergence window in which the cross-tradition index is silently incomplete, and it joins the deferred-work/push-debt cluster where deferred steps get forgotten. The harm is to downstream cross-tradition views and to anyone trusting the index, not to ingestion narrowly.

  Specific risks: The index is trusted as complete while missing the newly-ingested cross-tradition routing; the backfill is forgotten and the divergence persists.

  Mitigations available: Track the deferral explicitly (an OPEN item with an owner) and mark the index as partial/as-of until backfilled — the same per-axis as-of discipline as REVISE-158.

  STEELMAN:
    Item: ASSUMPTION-401
    Strongest counterargument: Narrowly scoped to INGESTION, the assumption is correct and the deferral is standard incremental-commit hygiene; the challenge is really about a different consumer (the index's readers), so within its own scope the assumption holds.
    What would need to be true for C2A2 to be safe: The deferral is tracked and the index is marked incomplete until backfilled.
    How to test: Confirm the backfill commit lands and the index matches ingested content.

  Recommendation: PARTIALLY-CHALLENGED (Weak-Moderate — true for ingestion; creates a tracked-divergence risk downstream)
