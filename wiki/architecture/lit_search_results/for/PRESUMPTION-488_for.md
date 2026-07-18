SEARCH-FOR-PRESUMPTION-488:
  Date searched: 2026-07-17
  Original item: PRESUMPTION-488
  Original statement: [inferred] "Healthy" is presumed a property of the system, not of the reporting agent's vantage; OpenStory is simultaneously certified healthy (DB probe) and reported down (delivery) on 07-16, and no reconciler notices the contradiction.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-488
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption (health treated as global, not vantage-relative)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. oneuptime / dev.to, 2026. "Liveness vs Readiness." — Health is not one property: liveness ("process up") and readiness ("service usable") can legitimately disagree; a 200 on liveness coexists with a 503 on readiness.
    2. DZone / etcd, "Split-Brain in Distributed Systems." — "From a node's perspective, another node might be dead, unreachable, or perfectly healthy but separated"; observers hold vantage-relative views that must be reconciled (quorum, vector clocks).
    3. freeCodeCamp, "Design Patterns for Distributed Systems." — Failure detectors and reconciliation are required precisely because no single observer has global truth.

  Strength of support: Strong

  Summary: The presumption's core claim — that "healthy" is vantage-relative and requires explicit reconciliation — is directly supported. Liveness/readiness semantics show two truthful probes disagreeing by design; split-brain literature shows that partial observability makes multi-observer reconciliation a first-class requirement, which C2A2 currently lacks.

  Caveats: The literature's reconciliation mechanisms (quorum) assume comparable observers; C2A2's observers consume different signals (DB probe vs delivery), so reconciliation must be signal-aware, not vote-counting.

  Recommendation: SUPPORTED
