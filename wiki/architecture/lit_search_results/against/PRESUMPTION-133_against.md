SEARCH-AGAINST-PRESUMPTION-133:
  Date searched: 2026-05-11
  Original item: PRESUMPTION-133
  Original statement: "'Documentation-only approach is not converging' framing presumes a programmatic fix would converge — implicit unsupported counterfactual"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-133
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-10 EOD remediation-switching counterfactual gap
      15b: Searched for counter-evidence on programmatic-fix convergence assumption
    Current status: PARTIALLY-CHALLENGED

  Sources:
    1. Pearl (2000) "Causality" — counterfactual claims require explicit causal model; "would-converge" without model is unsupported.
    2. Brooks (1975) "The Mythical Man-Month" — programmatic fixes introduce their own non-trivial failure modes (brittleness, edge-cases, maintenance burden); convergence is not guaranteed by mode-of-fix.
    3. Cunningham (1992) WikiWikiWeb origins — documentation as enforcement mechanism has documented success in collaborative settings; not all documentation failures imply programmatic alternative will succeed.
    4. Hollnagel (2012) "Safety-I and Safety-II" — substitution of one failure-prone mechanism for another is documented anti-pattern; both modes can fail in different ways.
    5. PRESUMPTION-122 (REVISE 2026-05-10) — documentation-as-fix cluster; PRESUMPTION-133 captures the paired counterfactual gap.

  Strength of challenge: Moderate

  Summary: The challenge is moderate. The counterfactual claim ("programmatic fix would converge") is unsupported without explicit causal model (Pearl). Brooks and Hollnagel both warn that mode-substitution is not a generic remedy — programmatic fixes have their own failure modes. The legitimate framing is "documentation has not converged; programmatic enforcement is the conventional next step" (supported); the strong "would converge" counterfactual is the unsupported part.

  Specific risks: (a) Mode-substitution without addressing root cause; (b) implicit confidence that programmatic fix will succeed where documentation failed; (c) "documentation-only" framing may strawman documentation-with-audit hybrid; (d) cluster joint with PRESUMPTION-122 (REVISE).

  Mitigations available: (a) Explicit causal model for why programmatic fix would converge; (b) pilot test of programmatic fix before commitment; (c) acknowledge both modes have failure surfaces; (d) consider documentation-with-audit hybrid as third option.

  Recommendation: PARTIALLY-CHALLENGED (Moderate)

  STEELMAN:
    Item: PRESUMPTION-133
    Strongest counterargument: The "would converge" claim is a counterfactual that requires causal model under Pearl's discipline; without the model, the claim is asserted rather than supported. Brooks (Mythical Man-Month) and Hollnagel (Safety-I/II) both document that mode-substitution introduces new failure modes rather than eliminating failure altogether. The cluster joint with PRESUMPTION-122 (documentation-as-fix) is the structural concern: the system is substituting one mode for another without engaging the underlying cause.
    What would need to be true for C2A2 to be safe: (a) Explicit causal model; (b) pilot test before commitment; (c) acknowledge programmatic-fix failure modes; (d) documentation-with-audit hybrid considered.
    How to test: Audit whether programmatic-fix decision specifies a causal model; check whether pilot test is performed; track programmatic-fix's own convergence rate.
