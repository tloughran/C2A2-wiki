SEARCH-FOR-ASSUMPTION-284:
  Date searched: 2026-06-08
  Original item: ASSUMPTION-284
  Original statement: The right safety split is "approved data auto-publishes, generator/template code changes are gated for human visual review."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-284
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the stated safety policy for the auto-regeneration pipeline.
      15a: Searched for support that code changes warrant heavier human gating than (already-approved) data changes — i.e., a blast-radius-based review asymmetry.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Progressive-delivery / deployment-gating practice (canary, feature flags, gated promotion; Humble & Farley, "Continuous Delivery," 2010). — Changes are gated in proportion to blast radius; code/template changes that alter rendering logic for the whole artifact have larger, harder-to-bound blast radius than appending a row of already-approved data, which supports heavier review on the code path.
    2. Human-in-the-loop release gating literature. — Keeping a human visual-review checkpoint on the high-blast-radius change class (generator/template) while automating the low-variance class is the standard HITL cost/risk allocation.
    3. Risk-asymmetry / change-classification practice (code vs config/data change types in CD pipelines). — Distinguishing change classes and applying different gates per class is recognized good practice, not an ad-hoc split.

  Strength of support: Moderate (for the asymmetry direction only)

  Summary: The DIRECTION of the split is supported: gating intensity should track blast radius, and a generator/template change (which can corrupt every node of the published connectome at once) is genuinely higher-blast-radius than appending already-approved data, so a human visual-review gate on code changes is well-justified. Differential gating by change class is established CD practice.

  Caveats: The support attaches to "code changes deserve MORE review," not to "data changes deserve NONE." The "approved data auto-publishes (unreviewed)" half rests on the separable claim that data regeneration is deterministic/safe enough to skip review — which is PRESUMPTION-319 and is challenged. So this is the floor (asymmetry is real) under a contested ceiling (data is review-exempt). Support is for the asymmetry, not for a zero-review data path.

  Recommendation: PARTIALLY-SUPPORTED
