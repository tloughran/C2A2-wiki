SEARCH-AGAINST-PRESUMPTION-488:
  Date searched: 2026-07-17
  Original item: PRESUMPTION-488
  Original statement: "Healthy" is presumed a system property, not a vantage property; OpenStory certified healthy and reported down same-day with no reconciler.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-488
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. oneuptime / web-alert.io, 2026. — Mature monitoring already treats health as multi-dimensional (livez/readyz/startupz); the "healthy is global" presumption is not what best-practice systems actually assume, so the flaw is C2A2-local, not a deep conceptual error.
    2. freeCodeCamp, "Design Patterns for Distributed Systems." — Failure detectors and reconciliation are standard, well-understood components; a missing reconciler is an omitted known pattern, readily added.

  Strength of challenge: Weak-Moderate

  Summary: The challenge narrows the presumption: the vantage-relativity of health is well established and the reconciliation machinery is off-the-shelf, so the issue is an unimplemented pattern rather than a mistaken belief baked deep into the design. This lowers the severity from "conceptual blind spot" to "missing component."

  Specific risks: Real outages hide behind a truthful-from-somewhere green until a reconciler exists.

  Mitigations available: Per-subsystem signal registry + same-day verdict-disagreement detector.

  STEELMAN:
    Strongest counterargument: C2A2's agents may already implicitly know health is vantage-relative; what is missing is only the automated reconciler, so the presumption slightly overstates the conceptual gap while correctly identifying the mechanical one.
    What would need to be true for C2A2 to be safe: An automated multi-observer reconciler flagging same-day disagreement.
    How to test: Enumerate agents x consumed signal; auto-detect verdict disagreement.

  Recommendation: PARTIALLY-CHALLENGED
