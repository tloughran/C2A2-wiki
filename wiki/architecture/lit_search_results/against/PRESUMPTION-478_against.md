SEARCH-AGAINST-PRESUMPTION-478:
  Date searched: 2026-07-16
  Original item: PRESUMPTION-478
  Original statement: [inferred] Model quota is presumed an unmetered substrate - ~37 daily tasks with no budget, no back-pressure, no exhaustion alarm, no precedence; today the evening delivery died on 'out of usage credits' while the day's producers ran to completion and the watchdog reported all clear.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-478
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Extracted/inferred to intake queue (for_lit_search.md)
      15b: Searched for challenging literature; result CHALLENGED (strength Strong)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Floyd & Jacobson, 'Random Early Detection' (1993); Nichols & Jacobson, 'Controlling Queue Delay / CoDel' (2012): finite resources demand admission control and early load-shedding; unmanaged demand collapses the resource for everyone.
    2. SRE load-shedding/throttling practice (Google SRE; Plexobject 2024): prioritize and shed low-value work under exhaustion so critical paths survive; exhaustion must raise an alarm and apply back-pressure.
    3. Observed in-run counterexample: evening delivery died on 'out of usage credits' while lower-value producers completed - precedence-inversion under exhaustion, exactly the failure the literature predicts.

  Strength of challenge: Strong

  Summary: The presumption is strongly challenged. Decades of admission-control and load-shedding literature establish that an unmetered-finite-resource assumption fails predictably: without back-pressure, precedence, or an exhaustion alarm, demand exceeds supply and the failure lands arbitrarily - here on the delivery path while producers ran to completion. The watchdog reported all clear because exhaustion is invisible to a liveness-only monitor (ties to the firing-health family).

  Specific risks: Silent quota exhaustion lands preferentially on delivery/reconciliation paths, is invisible to the watchdog, and defeats every queued remedy (REVISE-198/199 both assume the channel can still transmit).

  Mitigations available: Introduce a token/quota budget with back-pressure, a precedence order that protects delivery over producers, and an exhaustion alarm the watchdog can read.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-478
    Strongest counterargument: A fleet with no admission control and no priority under a shared finite quota does not degrade gracefully - it fails at whichever task happens to run when the ceiling is hit. Because producers are scheduled before delivery, the quota is systematically consumed by lower-value work, guaranteeing that the highest-value path (delivery to the human) is the first casualty. This is a designed-in precedence inversion.
    What would need to be true for C2A2 to be safe: Either the quota is effectively non-binding at 37 tasks/day (it is not - it was hit), or an admission/precedence mechanism protects the critical path.
    How to test: Plot the cost tracker's daily series against the account ceiling; confirm whether delivery tasks are scheduled after producers.
