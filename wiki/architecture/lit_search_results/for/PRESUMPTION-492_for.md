SEARCH-FOR-PRESUMPTION-492:
  Date searched: 2026-07-18
  Original item: PRESUMPTION-492
  Original statement: [inferred] The lit pipeline presumes 15d RE-TRIGGER generation stays within daily drain capacity; a 129-item undrained backlog (07-05, 07-12) with no fan-out cap or STALE-aging shows re-triggers can outpace draining unboundedly.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-492
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from the observed 129-item undrained RE-TRIGGER backlog
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. CMU, Harchol-Balter, "A Little Bit of Queueing Theory" (Ch. 27). — Foundational result: when arrival rate λ exceeds service rate μ (ρ ≥ 1), the queue is unstable and expected length grows without bound. Directly grounds "re-triggers can outpace draining unboundedly."
    2. DZone, "Queuing Theory for Software Engineers." — Applies the stability condition to software work queues; ρ ≥ 1 means unbounded growth, confirming the pipeline needs enqueue-rate < drain-rate to stay stable.
    3. pmbanugo.me, "Why Queues Don't Fix Overload (And What To Do Instead)." — Argues unbounded queues silently accumulate stale/dead work; advocates bounded queues + load shedding / TTL — precisely the "fan-out cap or STALE-aging" the presumption says is missing.

  Strength of support: Strong

  Summary: Queueing theory strongly supports the presumption. A pipeline that drains only each day's fresh batch while 15d injects re-trigger cohorts has no guarantee that λ (enqueue) < μ (drain); when it is violated the backlog grows without bound, exactly as observed (110 items from 07-05 + 19 from 07-12, unserviced for 6-13 days). The standard remedies — bound the queue, cap fan-out, and age out stale items (TTL/STALE) — are well established and are the specific mitigations the item calls for. This is a live, in-vivo instance of the instability condition.

  Caveats: The observed backlog is direct system evidence (near-GROUNDED), so the literature mainly supplies the theoretical frame and the remedy catalog rather than novel confirmation.

  Recommendation: SUPPORTED
