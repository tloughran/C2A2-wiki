SEARCH-AGAINST-PRESUMPTION-479:
  Date searched: 2026-07-16
  Original item: PRESUMPTION-479
  Original statement: [inferred] The sync-outage diagnosis presumed failure modes are mutually exclusive - that finding a cause is finding the cause. Today the two directions failed on two different causes (login; credits), which no hypothesis in the family reserved room for.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-479
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Extracted/inferred to intake queue (for_lit_search.md)
      15b: Searched for challenging literature; result CHALLENGED (strength Strong)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. R.I. Cook, 'How Complex Systems Fail' (1998); Allspaw, 'Each necessary but only jointly sufficient' (2012): overt failure requires multiple faults; 'the root cause' is a social/blame construct, not a technical one.
    2. Fault-masking literature (RCA critiques; Red Hat 'Not the root cause'): a known cause routinely masks a co-occurring one, so accepting the first cause found terminates the search prematurely.

  Strength of challenge: Strong

  Summary: Strongly challenged. The presumption that failure modes are mutually exclusive - that finding a cause is finding the cause - is precisely the error resilience engineering was founded to correct. The 07-13/07-15 observation (two directions, two distinct causes: login and credits) is a direct empirical counterexample, and fault-masking predicts that each remedy aimed at the last-named cause will be defeated by the next unmodeled one. Because this is a PRESUMPTION (designers were unaware), it warrants extra weight.

  Specific risks: Every 'root cause' the pipeline accepted was accepted on the same reasoning; MONITOR-434's post-login observation must now be scored per-direction, and point-fix remedies (REVISE-198/199) are individually insufficient.

  Mitigations available: Adopt multi-cause / contributing-factors analysis; score each failure direction independently; design for graceful degradation rather than point-fixes.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-479
    Strongest counterargument: If failure causes are not mutually exclusive, then the entire sync-outage remediation program - built on identifying and fixing one cause at a time - is structurally unable to converge: each fix reveals or is defeated by a co-occurring cause the single-cause frame never reserved room for.
    What would need to be true for C2A2 to be safe: Failures in the sync subsystem would have to be genuinely single-cause (one fault, one fix) - contradicted by the two-direction/two-cause observation.
    How to test: Re-examine every closed sync-outage diagnosis for a co-occurring second cause; count how many remedies were later defeated by a new signature.
