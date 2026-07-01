SEARCH-AGAINST-PRESUMPTION-423:
  Date searched: 2026-06-30
  Original item: PRESUMPTION-423
  Original statement: "That the fix for frozen approval axes is to ADD another scheduled agent rather than consolidate the three independent feeds (OpenStory/PRS/signals); fragmentation taken as fixed substrate."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-423
    Item type: PRESUMPTION (unstated)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference
      15b: Searched for challenging literature (first-time, genuine web search 2026-06-30)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Agent-count vs decision-complexity literature (cf. C2A2 ASSUMPTION-004, itself MONITORed) — adding agents adds coordination and liveness surface; "add another scheduled agent" multiplies the very freeze-prone surface that caused the problem.
    2. System-design practice — treating fragmentation as fixed substrate is an unexamined framing; consolidation (one freshness-managed scheduler over three jobs) can remove the freeze class outright.
    3. This run's P-421/P-422 findings — the root cause is missing freshness control, not missing capacity; adding an agent without a watchdog re-creates the same single-point-of-failure.

  Strength of challenge: Moderate

  Summary: Moderate challenge: the presumption treats feed fragmentation as fixed and reaches for MORE agents when the diagnosed root cause is a missing freshness watchdog (P-421) and missing per-axis marking (P-422). Adding an agent may not fix the freeze class and adds coordination/liveness surface.

  Specific risks: Agent proliferation without addressing the freshness-control gap; more scheduled surfaces that can themselves freeze undetected.

  STEELMAN: If the three feeds genuinely have different cadences and owners, a thin dedicated agent per feed plus a shared watchdog may be the cleanest design — consolidation could couple independent failure domains. The presumption is only wrong if it skips the watchdog, not if it keeps feeds separate.

  Recommendation: CHALLENGED (Moderate — 'add an agent' addresses capacity, not the diagnosed freshness-control root cause; fragmentation-as-fixed is unexamined)
