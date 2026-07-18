SEARCH-FOR-PRESUMPTION-487:
  Date searched: 2026-07-17
  Original item: PRESUMPTION-487
  Original statement: [inferred] No-Blind-Push and "staged for the Mac" presume a human appears regularly to review and push; on an 11-day autonomous stretch a safety rule has become a durability failure — "staged" == "never persisted."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-487
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption (safety gate presumes bounded human latency)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Axis / Keysight, "Fail-safe vs Fail-secure." — A fail-close control can cause an outage and "must be paired with redundancy and monitoring"; the availability tradeoff is explicit. No-Blind-Push is a fail-secure gate whose availability cost is unpersisted output.
    2. arc42, "Safety Interlocks." — Interlock defaults to safe state when a precondition is unmet; safe here means "do not persist," which under an absent human equals "never persist."
    3. Temporal / MachineLearningMastery, 2026. — Durable pending-approval / queue-then-execute patterns preserve blocked output; the bottleneck "usually comes from poor routing... not from the mere existence of a human step" — i.e., the failure is architectural, matching the presumption.

  Strength of support: Strong

  Summary: The presumption is strongly supported by the fail-safe/fail-secure literature: a safety gate that defaults closed trades availability for safety and, without redundancy, converts an absent consumer into an outage. The human-in-the-loop durability literature confirms that "staged but never committed" is a known failure and that durable commit queues are the standard countermeasure.

  Caveats: Support is for the mechanism and the risk; whether "11 days" is the right threshold is empirical. The remedy must preserve the No-Blind-Push safety property (fail-soft, not fail-open).

  Recommendation: SUPPORTED
