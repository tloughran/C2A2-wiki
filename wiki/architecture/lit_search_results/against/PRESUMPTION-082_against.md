SEARCH-AGAINST-PRESUMPTION-082:
  Date searched: 2026-04-28
  Original item: PRESUMPTION-082
  Original statement: "Refresh-cycle 'no new evidence found' is reliable, not search-depth-asymmetric"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-082
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Sources:
    1. Cochrane Living Systematic Reviews (Elliott et al. 2017) — explicit: depth-matched search is the precondition for valid null reporting; un-matched depth invalidates the report.
    2. Maier (2007) "Knowledge Management Systems" — silent staleness from un-paired refresh is a documented failure mode.
    3. Trist (1981) — refresh-cycle decay in operational pipelines without re-calibration.
    4. SRE alert-fatigue literature (Beyer et al. 2016) — cumulative null reports lower attention to next change.
    5. C2A2-internal: 39 carry-forwards in 2026-04-27 cycle without depth documentation — the silent-staleness condition is operationally present.

  Strength of challenge: Moderate-Strong

  Summary: The literature is consistent: depth-asymmetric null reports are unreliable. The C2A2 refresh cycles do not document depth, so the reliability claim cannot currently be validated. The presumption is challenged on both literature grounds and operational grounds.

  Specific risks: (a) Silent staleness of MONITOR items; (b) alert fatigue as 39+ carry-forwards accumulate; (c) eventual change goes unnoticed because the carry-forward pattern masks attention.

  Mitigations available: (a) Document depth; (b) periodic depth-matched audits; (c) flag carry-forward beyond N cycles for explicit re-evaluation.

  Recommendation: CHALLENGED (Moderate-Strong) — PRESUMPTION + strong challenge → REVISE per 15c heuristic

  STEELMAN:
    Item: PRESUMPTION-082
    Strongest counterargument: The C2A2 refresh-cycle null reports are produced without depth documentation, against the explicit Cochrane LSR precondition. The pattern is operationally consistent with silent-staleness — and the operational record (39 same-day carry-forwards) makes the alert-fatigue concern empirically present.
    What would need to be true for C2A2 to be safe: Refresh-cycle depth is documented and (sample-)audited against original-cycle depth.
    How to test: Sample 5 carry-forwarded items; run depth-matched search; flag any new evidence missed by carry-forward.
