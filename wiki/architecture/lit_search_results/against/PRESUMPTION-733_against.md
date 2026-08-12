SEARCH-AGAINST-PRESUMPTION-733:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-733
  Original statement: That the queue backlog is a throughput problem; the run's own headline is that all five drawn items name a measurement on C2A2's own output as their disposition condition and none needs literature — which makes the queue mis-routed rather than slow, and 31 days of drain-rate reporting a measurement of the wrong constraint.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-733
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Took the run's own headline finding as a claim about the queue rather than about five items
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Multiple system-design sources on queue backlog diagnosis (Medium "The queue backlog that slowly eroded our system SLOs"; "Temporal Queues: 9 Backlog Patterns Before Incidents") — converge on "queue backlog is never just a queue problem; it is often a systems problem wearing a queue-shaped mask," i.e. routing/classification defects commonly masquerade as throughput problems. This supports the presumption's diagnostic move (don't default to "just add throughput"). [unverified — from search snippet]
    2. Cobbai Blog, "Advanced Strategies for Queue Design: Skills, Teams, and Workload Management" and Microsoft Dynamics 365 "Configure work classification rulesets" — describe standard practice of skill/type-based routing precisely because naive "assign to next available" routing produces items sitting in the wrong queue, indistinguishable from a slow queue without decomposition. [unverified — from search snippet]
    3. getnave.com "Demand vs. Capacity Analysis" and enji.ai "Capacity Planning Mistakes" — the dominant practitioner framing treats backlog growth as a genuine demand > capacity problem first, with misrouting treated as a secondary, detectable-only-by-decomposition cause. This is the "opposite" reading: most real-world backlog literature still defaults to capacity/throughput as primary diagnosis, and treats routing defects as an edge case requiring positive evidence (item-level classification), not the default explanation. [unverified — from search snippet]

  Strength of challenge: Weak

  Summary: The literature does support the general move of decomposing an aggregate backlog metric before accepting a throughput explanation, and confirms routing/classification defects are a real, well-documented failure mode distinct from capacity shortfall. However, the disciplinary default in queueing and workforce-management literature is still to treat backlog as a capacity signal until routing is specifically diagnosed — meaning PRESUMPTION-733's confident reframing ("mis-routed rather than slow") from a five-item sample is going beyond what the source material would license without further decomposition of a larger sample. The evidence is more "boundary condition" than "direct contradiction": misrouting is a known real phenomenon, but inferring it as the answer from n=5 is a small-sample generalization the general queueing literature would caution against.

  Specific risks: If C2A2 treats every item as needing "measurement of its own output" as a diagnostic and reclassifies the whole backlog as a routing defect, it risks under-provisioning genuine throughput/consumer capacity (the classic failure mode in Little's Law: unbounded producer output with no consumer scaling), while over-investing in reclassification tooling for a problem that may resolve once more items are sampled.

  Mitigations available: Standard mitigation is decomposition + sampling before reclassifying an aggregate metric — audit a larger, randomly drawn sample of queue items (not just the 5 most recently drawn) to establish routing-defect rate; instrument dead-letter/misroute detection separately from drain-rate so the two failure modes are distinguishable, per dead-letter-queue practice.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-733
  Strongest counterargument: Extraordinary claims (backlog is mis-routed, not slow) need proportionate evidence; a 5-item sample out of a much larger queue is a classic small-N generalization, and the dominant literature default (capacity/throughput) exists precisely because misdiagnosing backlog as routing dysfunction is a common analyst error that delays the boring, correct fix (add capacity, unblock the consumer). Without a comparison of misrouting rate across many more items, "all five" could easily be a local cluster rather than a system-wide property.
  What would need to be true for C2A2 to be safe: The reclassification would need to hold on a larger, representative sample of the backlog (not just the most recently or arbitrarily drawn 5), and there would need to be a positive mechanism identified for why items keep arriving pre-mismatched to their consumer (e.g., an upstream classifier bug), not just an absence of a throughput signal in this subset.
  How to test: Draw a random sample of 30-50 backlog items, code each independently for "needs literature vs. names a measurement on own output," and compute the proportion; if it stays near 100%, the routing-defect explanation strengthens; if it regresses toward a mixed distribution, the throughput/capacity explanation regains plausibility.

Search scope: Preliminary search — broader search recommended (general queueing/backlog literature only; no C2A2-specific or multi-agent-system-specific backlog studies found).
