SEARCH-FOR-PRESUMPTION-300:
  Date searched: 2026-06-04
  Original item: PRESUMPTION-300
  Original statement: [inferred] A confirmed-down sync channel is treated as a recoverable inconvenience, not a stop condition — both 06-03 sync runs completed their full workflow against a channel known to be dead, accumulating undeliverable state rather than halting/escalating.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-300
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption from two 06-03 sync runs completing against a known-dead channel.
      15a: Searched circuit-breaker / fail-fast, dead-letter/backpressure for down sinks, and escalation-on-confirmed-failure.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Nygard, "Release It!" circuit-breaker pattern (Azure Architecture Center; AWS resilience patterns). — When a downstream dependency is confirmed down, the canonical response is to TRIP the circuit and fail fast rather than keep issuing work that cannot succeed. Continuing a full workflow against a known-dead sink is the anti-pattern the circuit breaker exists to prevent.
    2. Dead-letter-queue + circuit-breaker integration (Codelit; Conduktor; SQS DLQ). — On a confirmed-down sink, retrying/continuing wastes resources; messages should be shunted to a durable dead-letter and the circuit opened. Accumulating undeliverable state is acceptable ONLY when it is an explicit, replayable dead-letter — not silent in-workflow residue.
    3. Escalation on confirmed channel failure (backpressure / fail-fast guidance). — Fail-fast stops work after repeated/confirmed failure precisely to avoid "retry storms" and silent backlog; a confirmed-down channel is a stop/escalate condition, not a recoverable inconvenience.

  Strength of support: Strong

  Summary: Established resilience engineering strongly supports treating a CONFIRMED-down channel as a stop-and-escalate condition, not a routine inconvenience. The circuit-breaker pattern, dead-letter routing, and fail-fast all encode the same norm: once a sink is known dead, halt the dependent work, route undeliverable items to an explicit replayable queue, and raise a visible signal. Running a full workflow to completion against a dead channel and accumulating in-workflow undeliverable state is the failure mode these patterns are designed to prevent.

  Caveats: The literature does sanction CONTINUING to produce output when the undeliverable state is captured durably for later replay (store-and-forward) — i.e., graceful degradation is legitimate IF paired with a durable queue + escalation. The presumption is only sound under that condition (developed by 15b). Support here is for "confirmed-down = stop/escalate," not for halting on every transient blip.

  Recommendation: SUPPORTED
