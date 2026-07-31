SEARCH-AGAINST-ASSUMPTION-514:
  Date searched: 2026-07-24
  Original item: ASSUMPTION-514
  Original statement: Any self-measurement of the pipeline's completeness/accuracy must cite an external referent/seeded denominator or be reported UNCALIBRATED.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-514
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from PREMISE-124 report
      15b: Searched for evidence that valid self-measurement is possible without an external referent
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Metacognition literature (Fleming & Lau, 2014, "How to measure metacognition"). — Under proper scoring rules, agents can produce well-calibrated confidence from internal signals alone; meta-d'/type-2 sensitivity can be genuine. Self-measurement is not uniformly uninformative.
    2. Internal consistency / cross-validation methods (statistics). — A system can bound its own error using held-out internal partitions (train/test splits, seeded canaries) without an external gold standard, weakening the claim that ONLY an external referent will do.
    3. Calibration-training results (extensions of Kruger-Dunning cure). — Calibration improves with internal feedback loops; an external referent is one route, not the only route.

  Strength of challenge: Weak-Moderate

  Summary: The blanket requirement is slightly too strong. A seeded internal canary or held-out partition can calibrate a completeness/accuracy estimate without a fully external gold standard, and proper-scoring-rule metacognition can be well-calibrated from internal signals. The challenge refines rather than refutes: the operative requirement is a referent that is INDEPENDENT of the thing being measured (which a seeded denominator supplies) — it need not be exogenous to the whole system. The item already allows "seeded denominator," so this is a clarification of "external."

  Specific risks: Over-strict reading could tag genuinely calibrated internal estimates as UNCALIBRATED, discouraging useful self-measurement.

  Mitigations available: Define "external referent" as "independent of the measured quantity" (seeded canary counts), not "outside the system entirely."

  STEELMAN:
    Item: ASSUMPTION-514
    Strongest counterargument: Well-designed systems calibrate against seeded ground truth (canaries, injected test items) with no human/external oracle; demanding an exogenous referent for every completeness claim is impractical and unnecessary.
    What would need to be true for C2A2 to be safe: at least one independent seeded denominator must actually exist and be checked; a claim with neither exogenous nor seeded referent is still UNCALIBRATED.
    How to test: for each completeness claim on record, verify a seeded denominator exists (the item's own in-house test).

  Recommendation: PARTIALLY-CHALLENGED
