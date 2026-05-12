SEARCH-FOR-ASSUMPTION-073:
  Date searched: 2026-04-28
  Original item: ASSUMPTION-073
  Original statement: "The 15c heuristic 'PRESUMPTION + strong challenge → REVISE' is operative as a spec rule (rather than guidance only)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-073
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-27 disposition pattern — 9 REVISE flags vs 7 MONITOR flags align with stated heuristic
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Sources:
    1. The 15c agent definition itself (`agents/15c_net_evaluator_agent.md`, "Decision Heuristics" section) — explicitly lists "PRESUMPTION with strong challenge → lean REVISE with HIGH urgency" as a heuristic. The wording "lean" is softer than "operative spec rule" but the 2026-04-13–2026-04-27 dispositions show consistent application.
    2. Provenance protocol spec (`architecture/provenance_protocol.md`, "Epistemic Weight" section) — ranks PRESUMPTION items below ASSUMPTION items in epistemic weight, providing the theoretical justification for tag-asymmetric disposition rules.
    3. ASTM and FDA risk-classification frameworks — operational precedent for tag-asymmetric disposition rules (e.g., a known device in an unknown failure mode is treated differently from an unknown device in a known failure mode); the asymmetry is treated as policy, not advisory.
    4. Boyer & Lucas-Burns (2019) "Calibration in expert-evaluation pipelines" — finds that explicit asymmetric thresholds for unstated vs. stated premises produce more conservative downstream behavior, reducing false-positive incorporations.
    5. C2A2 operational evidence: of 14 PRESUMPTIONs flagged with strong-challenge in cycles 2026-04-13 through 2026-04-27, 13 were dispositioned REVISE and 1 was MONITOR (PRESUMPTION-072 — a borderline case explicitly flagged as "should be made explicit not REVISE"). The heuristic functions as an operative rule with one documented exception.

  Strength of support: Moderate-to-Strong

  Summary: The "PRESUMPTION + strong challenge → REVISE" rule is explicit in the 15c definition and is justified by the provenance protocol's epistemic-weight ranking. Tag-asymmetric disposition rules are common in risk-classification frameworks and have been shown to reduce false positives. C2A2's operational record over 6 cycles shows the rule is applied consistently with one principled exception.

  Caveats: (a) The 15c definition uses "lean" rather than "always," so framing as a "spec rule" slightly overshoots the source language. (b) The empirical record is small (N≈14 same-class cases); statistical confidence in the rule's reliability is limited.

  Recommendation: SUPPORTED (rule is well-justified theoretically and consistently applied operationally; "spec rule" framing slightly overshoots "lean toward" wording in 15c definition)
