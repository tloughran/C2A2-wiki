SEARCH-AGAINST-ASSUMPTION-476:
  Date searched: 2026-07-20
  Original item: ASSUMPTION-476
  Original statement: A staleness detector keyed to cycle count loses sensitivity exactly as consumption stalls — "the longer consumption stalls, the less able the staleness detector is to report it." A wall-clock companion rule is the stated remedy, deliberately not implemented.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-476
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 periodic monitor weekly transcript
      15b: Searched for challenging literature (self-referential monitor sensitivity, wall-clock vs event-count aging, liveness vs progress)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial (diagnosis uncontradicted; remedy challenged)

  Sources:
    1. Redis, "Distributed Locks with Redis" (official docs, retrieved 2026-07-20). Redis does not use a monotonic clock for TTL expiration, so a wall-clock shift can cause a lock to be held by more than one process; replicas may expire a key at T by their own clock while the master still considers it live. Direct evidence that wall-clock aging has its own well-documented inversion mode.
    2. "The 'Clock Skew' Conflict: When Time Lies in Distributed Systems" (systemdr.substack.com, retrieved 2026-07-20). Documents that there is no global "now," that a 2026 cloud VPC should assume 1–50 ms generic drift and 100–500 ms cross-region, and that "time usually leaks quietly into leases, TTLs, aggregation windows, and event ordering until the team realizes that the clocks, not the business logic, were the real source of breakage." Challenges the framing of wall-clock as a neutral, more-honest reference.
    3. Zylos Research, "AI Agent Self-Healing: Automated Recovery and Resilience Patterns" (2026-03-02, retrieved 2026-07-20). "Liveness alone is insufficient — agents can be alive and completely stuck, making progress metrics mandatory," and conventional monitoring can concentrate load in a supervisor that becomes a single point of failure. Challenges the remedy's form: adding a second aging clock does not separate liveness from progress, which is the actual defect.
    4. BusinessWire/Morningstar alert-fatigue evidence as recorded in this vault's 2026-07-19 ASSUMPTION-472 search (44% of organizations had an outage linked to suppressed or ignored alerts). Bears directly on the item's own test, which would flip an unknown fraction of 67 carried items to STALE simultaneously.

  Strength of challenge: Moderate

  Summary: The diagnosis is the strong part of this item and nothing retrieved contradicts it — a detector whose sensitivity is conditioned on the process it monitors is a recognised anti-pattern, and the self-referential form here is clean. The remedy is where the challenge lands. Wall-clock aging is not a neutral upgrade: it is the reference that distributed-systems practice specifically warns about, with documented non-monotonicity, drift, and replica disagreement, and Redis's TTL behaviour is a concrete case of a wall-clock-keyed expiry producing exactly the wrong answer. More importantly, the structural defect is that a single signal is carrying both liveness and progress; the agent literature's remedy is to separate those signals, not to add a second aging axis to the conflated one. Finally, the item's proposed test has a load consequence it does not price: enabling wall-clock aging against 67 already-carried items will convert a batch of them to STALE at once, into a channel this vault has already documented as having near-zero throughput.

  Specific risks: If wall-clock aging is added as a companion rule, the first run produces a bulk staleness event that is indistinguishable from a genuine degradation and arrives in a channel with no consumer — the alert-fatigue failure this vault has already recorded against ASSUMPTION-472 and PRESUMPTION-495. If the wall clock in the scheduled execution context differs from the interactive one (a plausible instance of the 2026-07-18 context class), items will age at the wrong rate and the new detector will be wrong in a direction nobody is watching for. And the underlying conflation — one signal meaning both "the pipeline ran" and "the item was considered" — survives the remedy intact.

  Mitigations available: Split the signal before adding a clock: report FIRED (the monitor ran), OBSERVED (the item was read), and DISPOSED (the item was acted on) separately; the failure mode described is invisible only because these are one number. If wall-clock aging is added, key it to a monotonic source where available and record the clock source in the record. Backfill the 67 carried items with a staggered or explicitly-batched first pass so the initial bulk transition is legible as an artefact rather than an event. Measure the throughput of the receiving channel before increasing what is sent into it.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-476
  Strongest counterargument: The observation is correct and important, and the remedy attached to it is a second instance of the same class of error. A cycle-count detector fails because its reference is generated by the monitored process; the proposed fix substitutes a reference that distributed-systems practice treats as one of the least trustworthy quantities available, with documented non-monotonicity and drift, in a system that has just spent a day diagnosing a scheduled execution context whose properties differ from the interactive one — the clock being an obvious candidate for that list and not yet checked. Underneath both is the real defect: one signal is being asked to mean both "this pipeline is alive" and "this item has been considered," and no choice of aging axis separates them. Adding wall clock therefore buys a second way to be wrong about the same conflation, and buys it at the cost of a bulk staleness event landing in a channel with demonstrated near-zero throughput, where the vault's own prior findings predict bulk dismissal. The deliberate non-implementation may have been the better call for the wrong reason.
  What would need to be true for C2A2 to be safe: The wall clock in the scheduled context must be verified monotonic and consistent with the interactive one; the receiving channel must have demonstrated capacity to absorb the resulting transitions; and liveness must already be separated from progress so that the new rule adds information rather than a second ambiguous number.
  How to test: Before implementing, log the wall-clock timestamp from both the scheduled and interactive contexts on the same nominal run and compare — this is a one-line check and it is the discriminating test. Then simulate the wall-clock rule against the existing 67-item record offline and count how many items it would have flipped to STALE on day one; if that count is large relative to the channel's 30-day disposition throughput, the rule is predicted to be suppressed on arrival and the correct order of work is to fix the consumer first.

  Search scope: Preliminary — three targeted searches. The specific literature on metrics whose sensitivity is conditioned on the monitored process was not retrieved directly; the closest match was the agent liveness-vs-progress material.
