SEARCH-AGAINST-PRESUMPTION-106:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-106
  Original statement: "Protocol-routine vs. architectural DECISION-NNN canonization criterion presumed self-evident, never written"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-106
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 implicit-decision pattern
      15b: Searched for inter-rater reliability literature on decision-categorization
    Current status: CHALLENGED

  Challenging evidence found: Yes (strong)

  Sources:
    1. Cohen (1968); Krippendorff (2018) inter-rater-reliability literature — without written criteria, inter-rater agreement on category boundaries is documented to be substantially below 0.7 kappa; presumption of self-evidence is empirically refuted.
    2. ADR literature (Nygard 2011; Tyree & Akerman 2005) — written criteria are canonical; ADR practice was created precisely because architectural-decision boundaries are not self-evident.
    3. Software-architecture literature (Bass, Clements, Kazman 2012) — implicit categorization correlates with category drift, scope creep, and decision-pile-up; the literature flags this as canonical failure mode in maturing architectures.
    4. Empirical knowledge-management research (Davenport & Prusak 2000) — implicit-classification systems show category drift over time; the longer they run unwritten, the more drift accumulates.
    5. C2A2-internal: PRESUMPTION-098 / PRESUMPTION-041 prior cluster — same structural gap surfaced previously; this third recurrence within the implicit-decision-drift cluster confirms the literature's prediction.

  Strength of challenge: Strong

  Summary: "Self-evident" criteria are empirically refuted by inter-rater-reliability literature; documented kappa values without written criteria fall well below operational thresholds. ADR literature was created specifically because architectural-decision boundaries are not self-evident. Software-architecture and knowledge-management literatures uniformly flag implicit-classification as canonical drift-prone pattern. The presumption is the third recurrence of the same gap, which is itself the empirical confirmation of the literature's prediction.

  Specific risks: (a) Decision drift: routines that should be DECISION-NNN remain protocol-only; architectural surface degrades; (b) self-aware system unable to articulate its own classification criterion (PRESUMPTION-069 SELF-AWARENESS-META cluster); (c) compounds with PRESUMPTION-098 walk-thread canonization gap.

  Mitigations available: (a) Write canonization criterion (small artifact, low cost); (b) run inter-rater test on existing routines vs. DECISION-NNN; (c) explicit promotion review on a fixed cadence.

  Recommendation: CHALLENGED — written criteria are canonical; recurrence is the empirical confirmation.

  STEELMAN:
    Item: PRESUMPTION-106
    Strongest counterargument: Every relevant literature treats "self-evident classification" as drift-prone anti-pattern. ADR practice exists because the boundary is not self-evident. Inter-rater reliability literature empirically refutes the self-evidence assumption — without written criteria, agreement is below operational thresholds. Three recurrences of the same gap in C2A2's own self-aware data signal that the system has structural blindness to its own classification step.
    What would need to be true for C2A2 to be safe: (a) written canonization criterion; (b) explicit promotion review; (c) inter-rater test on existing categorization.
    How to test: Run a small inter-rater test — give two reviewers a sample of routines and ask them to classify protocol-vs-DECISION; measure kappa; if below 0.7, self-evidence is empirically refuted.
