SEARCH-AGAINST-PRESUMPTION-230:
  Date searched: 2026-05-21
  Original item: PRESUMPTION-230
  Original statement: "Confirming gating logic + data == confirming rendered behavior — UX symptom dispositioned by data-reasoning over reproduced observation."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-230
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred: a UX symptom was dispositioned by reasoning over gating logic + data, presuming that confirming logic/data equals confirming the rendered behavior.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E / REVISE-040 noted)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "Works as designed != works": the spec/implementation gap. — UX bugs are emergent at the render layer (browser/CSS/layout/event handling), not visible in gating logic.
    2. Dijkstra. — Reasoning about a program is not observing it; emergent UI behavior must be observed in the rendered result.
    3. Reproduced-defect discipline (software-testing best practice). — A defect should be reproduced and the fix observed; dispositioning a UX symptom by logic alone skips reproduction.
    4. In-system: symmetric to PRESUMPTION-218 (honest null vs under-search) and engages Rule 12 (fail loud) — a UX symptom closed without reproduction is a silently-skipped verification.

  Strength of challenge: Strong

  Summary: Strong challenge: rendered UX behavior is emergent at a layer the gating logic does not capture, so confirming logic+data does not confirm what the user sees. Best practice requires reproducing the rendered defect and observing the fix. Dispositioning a UX symptom by data-reasoning alone is a verification gap (symmetric to PRESUMPTION-218; engages Rule 12).

  Specific risks: UX bugs are marked resolved while still visible to users; the self-measurement layer over-trusts logic-level reasoning.

  Mitigations available: Require reproduced-observation (screenshot/render check) before dispositioning UX symptoms; treat logic+data as necessary-not-sufficient for UX.

  Recommendation: CHALLENGED (strong)

  STEELMAN:
    Item: PRESUMPTION-230
    Strongest counterargument: Rendered UX lives at a layer (browser, CSS, layout, event timing) that gating logic does not model, so confirming the logic and data cannot confirm what the user actually sees; closing a UX symptom by data-reasoning alone is a skipped verification (Rule 12) symmetric to mistaking an unsearched null for a true null (PRESUMPTION-218).
    What would need to be true for C2A2 to be safe: UX dispositions require reproduced observation of the rendered behavior.
    How to test: Re-open the UX symptom and attempt to reproduce it in the rendered artifact; if reproducible, the logic-only disposition was wrong.
