SEARCH-AGAINST-PRESUMPTION-087:
  Date searched: 2026-04-28
  Original item: PRESUMPTION-087
  Original statement: "Specialist 'significant work not yet captured' override is self-correcting; no audit mechanism required"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-087
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Sources:
    1. Krukow et al. (2008) "Trust models in ubiquitous computing" — expert-self-evaluation reliability decays without external calibration.
    2. Hoffman & Yates (2005) — un-audited expert overrides systematically over-trigger.
    3. Kruger & Dunning (1999) — self-evaluation bias in expert domains.
    4. C2A2-internal: PRESUMPTION-074 (specialist-recognition reliability) was REVISE-flagged 2026-04-27 with SYSTEMIC-RISK; PRESUMPTION-067 was MONITOR-flagged 2026-04-21. The audit-gap is recurrent across cycles.

  Strength of challenge: Strong

  Summary: The literature is consistent: pure self-correction without external check is not a calibration mechanism. The presumption is contradicted by both general literature and C2A2's recurring flags. The 2026-04-27 SYSTEMIC-RISK already named this as a system-wide concern.

  Specific risks: (a) Override drift — overrides become routine without empirical trigger; (b) systematic over-application; (c) reliability decay over N cycles.

  Mitigations available: (a) Add an audit pattern: require override to cite specific evidence; (b) sample-based justification review; (c) track override rate as a calibration metric.

  Recommendation: CHALLENGED (Strong) — PRESUMPTION + strong challenge → REVISE

  STEELMAN:
    Item: PRESUMPTION-087
    Strongest counterargument: Self-correction without external check is not a calibration mechanism — it is the absence of one. The literature is unambiguous; C2A2's prior cycles already flagged the concern. PRESUMPTION-087 is a clean instance of the pattern PRESUMPTION-074 named at the system level.
    What would need to be true for C2A2 to be safe: An audit mechanism is added (citation requirement, sample review, rate metric).
    How to test: Sample 3 prior overrides for evidence-citation completeness; if any lack a clear trigger, the un-audited concern is empirically confirmed.
