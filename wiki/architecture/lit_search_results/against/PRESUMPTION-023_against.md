SEARCH-AGAINST-PRESUMPTION-023:
  Date searched: 2026-04-14
  Original item: PRESUMPTION-023
  Original statement: "Three concurrent infrastructure failures (git lock, Gmail stale, wiki auth) are independent incidents"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-023
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from three concurrent failures observed 2026-04-14
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. AWS/distributed systems literature — Correlated and cascading failures are the norm, not exceptions.
    2. Common-cause failure analysis — Shared infrastructure (power, network, time-sync, credentials) causes concurrent failures.
    3. Cascading failure research — One failure causes latency spike that fails others.
    4. Incident analysis frameworks — Concurrence = correlation until proven otherwise.

  Strength of challenge: Strong

  Summary: The assumption of independence is precisely wrong in distributed systems context. Correlated and cascading failures are the norm. Common causes: shared infrastructure, operator actions touching all systems, common dependency failures, cascading overload. Three failures occurring simultaneously suggests correlated cause, cascading, or common operator action. Treating as independent misses root cause and invites recurrence.

  Specific risks: Fixing individually leaves shared vulnerability. Correlated failures will repeatedly block research. Individual patches without root cause analysis leave system vulnerable.

  Mitigations available: Full incident analysis assuming correlation. Map shared dependencies. Implement isolation (circuit breakers). Monitor for cascading. Set SLOs.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: Three failures CAN be independent if systems use completely segregated infrastructure. But this is rare. In typical architectures, correlated failures are the default. The solution is to verify independence: measure temporal synchronization, shared dependencies, and ripple effects. Only after testing should independence be claimed.
    What would need to be true for C2A2 to be safe: Full incident analysis for each failure. Test cascading by deliberately triggering each. Map shared dependencies.
    How to test: Deliberately trigger one failure; measure whether others are affected. If yes, correlated.
