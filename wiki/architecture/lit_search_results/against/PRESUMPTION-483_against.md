SEARCH-AGAINST-PRESUMPTION-483:
  Date searched: 2026-07-16
  Original item: PRESUMPTION-483
  Original statement: [inferred] Two monitors agreeing is presumed stronger evidence than one, but the scheduler health check and morning project status both derive 'all clear' from the same lastRunAt signal - their agreement is one blind spot counted twice, not two independent confirmations.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-483
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Extracted/inferred to intake queue (for_lit_search.md)
      15b: Searched for challenging literature; result CHALLENGED (strength Strong)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Knight & Leveson (1986) and follow-ups: independence of redundant components cannot be assumed; shared specification/input produces correlated (common-mode) failure - ~50% of faults were correlated in the seminal experiment.
    2. Common-cause failure literature: two monitors sharing an input signal fail together on that input; their agreement is one observation counted twice, not two.

  Strength of challenge: Strong

  Summary: Strongly challenged. Because both the scheduler health check and the morning project status derive 'all clear' from the same lastRunAt signal, they are not independent: any defect in that signal (e.g., firing-as-success) fools both simultaneously. Knight & Leveson's result - that even small correlation destroys the reliability gains redundancy is assumed to give - applies directly. The one artifact-reading monitor that could dissent is outvoted by two correlated liveness monitors.

  Specific risks: Correlated green checks give false confidence; the redundancy is illusory (the 07-14 all-clear was a single blind spot counted twice).

  Mitigations available: Map each monitor to the signal it consumes; require that at least one monitor read a genuinely independent source (artifact content), and weight correlated monitors as one.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-483
    Strongest counterargument: Redundant monitoring that shares an input is not defense-in-depth; it is a single point of failure wearing two badges. The system's confidence scales with the number of agreeing monitors, but its actual coverage scales with the number of independent signals - here, one. Adding more lastRunAt-derived monitors would increase apparent assurance while adding zero real coverage.
    What would need to be true for C2A2 to be safe: The two monitors would need to consume independent signals for their agreement to add evidence - falsified by both reading lastRunAt.
    How to test: Trace each monitor's data source; count distinct signals behind the N agreeing green checks.
