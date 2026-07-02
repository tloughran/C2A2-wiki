SEARCH-AGAINST-PRESUMPTION-433:
  Date searched: 2026-07-02
  Original item: PRESUMPTION-433
  Original statement: "[inferred] That the disk-full failure is isolated to the OpenStory feed, when one full compute disk produced two symptoms attributed to two separate problems."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-433
    Item type: PRESUMPTION (unstated)
    Transform at each step:
      14b: Surfaced as unstated presumption from the 2026-07-01 dual-symptom incident
      15b: Searched for challenging literature (genuine web search 2026-07-02)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. AWS Builders' Library, "Minimizing correlated failures in distributed systems" — a single root cause (a shared resource) characteristically produces many simultaneous, seemingly-independent failures; the ToR-switch example is the canonical shape. Directly challenges treating co-occurring symptoms as isolated.
    2. Baeldung / bluepes failure-model writeups — "a resource limitation on one system may cause performance degradation on another system, not apparent unless one knows the architecture"; symptoms rarely map one-to-one to causes. Local symptom attribution is a known misdiagnosis.
    3. arXiv 2605.14866 (root-cause localization for microservices) — failures "rarely manifest directly; instead they are revealed through observable anomalies," so multiple anomalies commonly share one upstream cause; per-symptom triage misses it.

  Strength of challenge: Moderate-Strong

  Summary: The distributed-systems literature directly contradicts the isolation reading: one exhausted resource (the full disk) is exactly the kind of shared root cause that surfaces as multiple, apparently-separate symptoms. Attributing the two symptoms to two separate problems is the classic per-symptom misdiagnosis the correlated-failure literature warns against. The presumption is challenged.

  Specific risks: Fixing only the OpenStory symptom leaves the shared cause (full disk) live, so the second symptom recurs and is re-triaged as yet another "separate" problem — wasted effort and a persistent latent fault. Root cause is never retired.

  Mitigations available: On any multi-symptom day, check shared resources (disk/memory/session) FIRST before attributing symptoms independently; add a root-cause-aggregation step that correlates co-occurring anomalies to common substrates.

  STEELMAN:
    Item: PRESUMPTION-433
    Strongest counterargument: Sometimes co-occurring failures really are independent (coincidence happens), so demanding a shared root cause every time risks over-fitting. But the correct default under resource-exhaustion evidence is to SUSPECT a shared cause and rule it out, not to ASSUME isolation; the cost of a missed common cause (recurrence) exceeds the cost of a quick shared-resource check.
    What would need to be true for C2A2 to be safe: A cheap shared-resource check is run before symptoms are filed as independent, and the disk-full cause is confirmed retired.
    How to test: After remediating the OpenStory symptom, confirm the second symptom also cleared once disk was freed; if it did, they shared the cause.

  Recommendation: CHALLENGED (Moderate-Strong — one exhausted resource produces multiple symptoms; isolation is a misdiagnosis pattern)
