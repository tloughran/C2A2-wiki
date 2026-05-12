SEARCH-FOR-PRESUMPTION-133:
  Date searched: 2026-05-11
  Original item: PRESUMPTION-133
  Original statement: "'Documentation-only approach is not converging' framing presumes a programmatic fix would converge — implicit unsupported counterfactual"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-133
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-10 EOD remediation-strategy switching observation
      15a: Searched for remediation-strategy comparison literature and counterfactual-evidence requirements
    Current status: PARTIALLY-SUPPORTED

  Sources:
    1. ITIL Problem Management (v4, 2019) — remediation-strategy switching is supported when the current approach has documented failure; counterfactual evidence is preferred but not always required for switch decisions.
    2. Nygard (2018) "Release It!" — escalation from documentation to programmatic enforcement is canonical when recurrence persists; "documentation has not converged" is a legitimate trigger for escalation.
    3. Lean (Rother 2010) — Plan-Do-Check-Act (PDCA) explicitly endorses switching strategies when "Check" reveals current strategy has not converged; counterfactual is not required to switch.
    4. C2A2-internal: PRESUMPTION-122 (REVISE 2026-05-10) is the upstream documentation-as-fix cluster; PRESUMPTION-133 captures the alternative-strategy counterfactual gap.
    5. Pearl (2000) "Causality" — counterfactual claims (would converge under alternative) require explicit causal model; absent such model, the claim is asserted rather than supported.

  Strength of support: Moderate

  Summary: Remediation-strategy switching when current strategy is failing is canonical ITIL/Lean practice; explicit counterfactual evidence is not required to motivate switching. However, the strong claim that the alternative ("programmatic fix") "would" converge is a counterfactual claim that requires causal modeling per Pearl. The legitimate framing is "documentation has not converged; programmatic enforcement is the conventional next step" — which is supported. The presumption that the programmatic fix "would" converge — without evidence of feasibility — is the unsupported part.

  Caveats: (a) Programmatic fixes have their own failure modes (brittleness, gaming, edge-case-coverage); switching is canonical but convergence is not guaranteed; (b) "Documentation-only" framing may itself be incomplete — documentation paired with audit-trigger is a hybrid that has not been tested; (c) Counterfactual-evidence-required is the strict reading; convention-default is the operational reading.

  Recommendation: PARTIALLY-SUPPORTED (Moderate) — strategy-switching is canonical; the implicit "would-converge" counterfactual is the unsupported component
