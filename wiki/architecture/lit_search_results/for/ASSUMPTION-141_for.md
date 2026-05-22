SEARCH-FOR-ASSUMPTION-141:
  Date searched: 2026-05-15
  Original item: ASSUMPTION-141
  Original statement: "Evening cowork-to-chat browser delivery FAILED (Chrome MCP offline); degraded-mode protocol invoked (visible failure flag in summary header)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-141
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-14 operational summary
      15a: Searched for degraded-mode-with-visible-failure protocols in operational tooling
    Current status: SUPPORTED (Strong)

  Sources:
    1. SRE practice (Beyer et al. 2016, Limoncelli et al. 2014) — degraded-mode-with-visible-failure-flag is canonical fail-safe pattern; graceful degradation > silent fail.
    2. Norman (2013) "Design of Everyday Things" — visible failure flags preserve user trust; silent failures erode user model.
    3. Reason (1990) — safety culture requires that failures be visible, not concealed.
    4. Joint Commission alarm-management — visible-failure principle: failure flags must reach the operator.
    5. Aviation HF literature (FAA, NTSB) — degraded-mode operations require visible failure flags; canonical safety practice.
    6. C2A2-internal: aligns with Pathway 14 honesty-layer commitment (ASSUMPTION-130 INCORPORATE / PREMISE-019); the degraded-mode visible-failure flag is the operational instantiation of the same epistemic commitment.

  Strength of support: Strong

  Summary: Degraded-mode operation with visible-failure flag is canonical across SRE, safety engineering, aviation HF, and design literature. The "visible failure flag in summary header" framing matches Norman/Reason recommendations and aligns with C2A2's already-validated Pathway 14 honesty commitment (PREMISE-019). Strong support: the protocol is the right pattern for the operational regime. The descriptive claim (Chrome MCP offline, degraded-mode invoked, flag visible) is straightforward observation.

  Caveats: (a) PRESUMPTION-177 paired — Chrome-MCP-offline today recurs after one good day; framing as "credential issue" rather than recurring architectural failure mode is the load-bearing concern; (b) Degraded-mode-with-visible-flag handles the symptom; doesn't address the recurring failure pattern; (c) "Degraded-mode protocol" must be documented and tested — not just invoked ad-hoc.

  Recommendation: SUPPORTED (Strong) — degraded-mode-with-visible-failure is canonical; recurring failure pattern (PRESUMPTION-177) is the architectural concern
