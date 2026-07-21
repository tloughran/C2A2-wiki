SEARCH-AGAINST-PRESUMPTION-503:
  Date searched: 2026-07-20
  Original item: PRESUMPTION-503
  Original statement: [inferred] A summarizing agent is presumed to read the same evidence as the agents it summarizes — a status report presumed to be a view over artifacts rather than an independent parallel account. The summary read its own sources faithfully; those sources do not include the failing agents' outputs.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-503
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-07-19 morning project status transcript read against four same-morning failure transcripts
      15b: Searched for challenging literature (derived-claim provenance, dashboard-to-source binding, limits of coverage metrics)
    Current status: NO-CHALLENGE-FOUND (to the claim); PARTIALLY-CHALLENGED (to the remedy)

  Challenging evidence found: Partial — searched specifically for evidence that aggregation layers can be assumed source-coupled, and found none; every retrieved source runs the other way.

  Sources:
    1. Michael Brenndoerfer, "Monitoring LLM Systems: Metrics, Logging, Alerting, and Dashboards" (retrieved 2026-07-20). The four-layer stack — instrumentation, collection, visualization, alerting — with "each layer depends on the ones beneath it, and weaknesses in any layer propagate upward." Corroborates the presumption's diagnosis: a visualization layer is a view over its collection layer, not over reality.
    2. SoftwareSeni, "Why Your Existing Monitoring Stack Cannot See When Your LLM Is Failing" (retrieved 2026-07-20). Silent degradation described as the dominant failure mode in LLM-powered production, structurally invisible to tools that see only timing and status codes. Again corroborating.
    3. futureagi.com, "LLM Eval Monitoring Dashboards" (2026, retrieved 2026-07-20). Warns that most eval dashboards are "theaters of data" piling on rollups, and that the aggregate panel can look healthy while a single route sits at the floor; remedy given is per-route delta, i.e. **binding claims to slices**, not maximising coverage.
    4. Zylos Research, "AI Agent Self-Healing" (2026-03-02, retrieved 2026-07-20). Notes that conventional monitoring "can concentrate load in a single supervisor that itself becomes a single point of failure," and recommends fleet-level aggregate signals alongside, not instead of, per-agent ones. Bears on the remedy: expanding one summarizer's read set to full coverage moves load into the component the literature warns about.

  Strength of challenge: Weak

  Summary: This search was run adversarially and found nothing supporting the presumed coupling. The claim that a summarizing layer is a view over its own read set rather than over the system is the standard description of monitoring architecture, and the four-layer dependency account states the propagation mechanism directly. The item is, on the retrieved evidence, correct — and correct in a way that also explains ASSUMPTION-480, which is better read as this item's evidencing instance than as a separate claim. Where a challenge does apply is the remedy. The item proposes enumerating each summarizer's read set and computing coverage of the artifacts it makes claims about. Coverage as stated is an unbounded target — complete observability of a growing artifact set is not attainable, and a coverage percentage is a metric agents can raise by reading more without reading better, which is the Goodhart pattern. The retrieved dashboard guidance points elsewhere: bind each claim to the specific slice that evidences it, and surface per-route deltas rather than a global rollup. That is bounded, is checkable per claim, and does not create a new number to optimise. There is also a load caution: routing all artifacts through one summarizer to raise its coverage recreates the single-supervisor concentration the agent-resilience literature warns against.

  Specific risks: If the remedy is implemented as a coverage percentage, the system acquires a metric that rises as summarizers read more marginal artifacts while still missing the decisive one, and the metric will read green during exactly the failure it was built to catch — the inversion class PRESUMPTION-505 names, now installed deliberately. If coverage is pursued to completion, the summarizer's read cost grows with the vault, colliding with the read-cost finding in PRESUMPTION-498 and the budget finding in ASSUMPTION-478.

  Mitigations available: Bind claims, not coverage: every health assertion carries the artifact and timestamp it rests on, and an assertion with no bound artifact is reported as unknown rather than green. This is the item's own in-house test in its cheaper form and it is what the dashboard literature actually recommends. Report per-source status alongside the rollup so an absent source is visible as absent. Where coverage is measured, measure it over a fixed named critical set rather than over all artifacts, so the denominator cannot drift.

  Recommendation: PARTIALLY-CHALLENGED (claim stands; remedy needs bounding)

STEELMAN:
  Item: PRESUMPTION-503
  Strongest counterargument: The presumption itself survives this search — I looked for evidence that a summarizing layer can be assumed to see what its subjects see and found only sources saying the opposite, so the honest report is that the diagnosis is sound and that ASSUMPTION-480 is its instance rather than its equal. The challenge that remains is about what to build. "Enumerate the read set and compute coverage" sounds like measurement and behaves like a target: coverage rises when a summarizer reads more artifacts, whether or not it reads the ones that matter, and complete coverage of a growing vault is not reachable, so the number will sit somewhere below 100% forever and its movements will be uninformative. The monitoring literature the item's diagnosis rests on prescribes something different and cheaper — per-slice binding, per-route deltas, an absent source rendered as absent rather than as healthy — because the failure being prevented is a claim made without evidence, and the fix for that is to require evidence per claim, not evidence in aggregate. There is also a structural caution: driving all artifacts through one summarizer to raise its coverage concentrates load in the exact component that agent-resilience work identifies as becoming a single point of failure. The item is right about what happened and one step away from installing a version of it.
  What would need to be true for C2A2 to be safe: The critical artifact set would have to be finite, named, and stable enough that coverage over it is a meaningful denominator — otherwise coverage is a drifting proxy and per-claim binding is the only sound instrument.
  How to test: Take the 2026-07-19 morning summary and, for each health claim it made, record the artifact and timestamp that would have to be true for the claim to hold. Count how many claims have no such artifact. That count — claims-without-evidence — is bounded, decisive, and requires no read-set enumeration. Then compare it against the coverage number the item proposes and check whether the two ever disagree; if coverage can be high while claims-without-evidence is also high, coverage is the wrong instrument and the comparison proves it.

  Search scope: Moderate — one targeted search cluster across four sources, run in the disconfirmatory direction. Reported as no-challenge-found on the primary claim, which is itself informative.
