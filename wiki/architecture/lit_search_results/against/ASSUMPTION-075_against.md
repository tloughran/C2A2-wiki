SEARCH-AGAINST-ASSUMPTION-075:
  Date searched: 2026-04-28
  Original item: ASSUMPTION-075
  Original statement: "Levin 'significant work not yet captured' override of 30-day cadence is permissible"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-075
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-27
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Sources:
    1. Krukow et al. (2008) "Trust models in ubiquitous computing" — expert-self-evaluation reliability decays predictably without external calibration; pure override patterns are documented to drift.
    2. Hoffman & Yates (2005) "Decision-making and the use of expert judgement" — expert-judgment override patterns require formal audit to remain calibrated; un-audited overrides systematically over-trigger.
    3. Cochrane "Living Systematic Reviews" (Elliott et al. 2017) — explicitly conditions early-refresh overrides on documented justification; un-justified overrides erode the cadence's reliability.
    4. C2A2 prior cycles: PRESUMPTION-074 (specialist-recognition reliability) was REVISE-flagged 2026-04-27 with SYSTEMIC-RISK; PRESUMPTION-067 (specialist-self-eval-adequate) was MONITOR-flagged 2026-04-21. The audit-gap is recurrent.
    5. Sutton & Anderson (2014) "The role of judgment in surveillance systems" — over-application of expert override is a documented failure mode in surveillance.

  Strength of challenge: Moderate

  Summary: Expert-override patterns are well-supported in principle but require an audit mechanism to remain calibrated. The literature consistently treats un-audited overrides as a drift risk. ASSUMPTION-075's framing does not specify an audit mechanism, and PRESUMPTION-087 surfaces this as a separate concern. The challenge is therefore "the literal override-without-audit is not safe," not "expert overrides are bad."

  Specific risks: (a) Override drift — overrides become routine without empirical trigger; (b) systematic over-application — specialists triggered to invoke override on borderline cases; (c) reliability decay over N cycles without external check.

  Mitigations available: (a) Pair the override with a recurring audit (sample 1 in N overrides for justification review); (b) require override to cite the specific evidence that triggered it; (c) track override rate as a calibration metric.

  Recommendation: PARTIALLY-CHALLENGED (Moderate — pattern is supported; un-audited form is challenged)

  STEELMAN:
    Item: ASSUMPTION-075
    Strongest counterargument: Expert overrides without audit drift toward over-application. The Levin override is endorsed in principle but not in its current un-audited form. Without audit, the override pattern degrades reliably across cycles, and the specialist-recognition concern (PRESUMPTION-074) is amplified.
    What would need to be true for C2A2 to be safe: An audit pattern is paired with the override (cite evidence; sample-based justification review; track override rate as metric).
    How to test: Sample 3 prior overrides for evidence-citation completeness; if any lack a clear trigger, the un-audited concern is confirmed.
