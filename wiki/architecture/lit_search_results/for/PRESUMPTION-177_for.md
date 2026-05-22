SEARCH-FOR-PRESUMPTION-177:
  Date searched: 2026-05-15
  Original item: PRESUMPTION-177
  Original statement: "Chrome-MCP-offline failure today recurs after only one successful day; degraded-mode protocol treats as credential issue rather than recurring architectural failure mode"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-177
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from ASSUMPTION-141 Chrome-MCP-offline observation
      15a: Searched for recurring-failure-mode pattern recognition in operational tooling
    Current status: SUPPORTED (Strong)

  Sources:
    1. Reason (1990) "Human Error" — recurring failure framed as user-level/credential cause masks system-level cause; "swiss cheese" model; framing-error pattern is canonical.
    2. Allspaw (2009) "10+ Deploys Per Day" — second consecutive incident of same type indicates architectural failure mode, not user-level cause.
    3. SRE practice (Beyer et al. 2016) — failure recurrence within one cycle requires root-cause analysis, not just credential-level fix.
    4. Hollnagel (2014) "Safety-II" — surface-level fixes that restore service without addressing systemic cause reliably recur.
    5. C2A2-internal: PRESUMPTION-159 carry-forward (REVISE 2026-05-14) — credential-layer-as-architectural-fix anti-pattern; PRESUMPTION-177 is the same pattern's second data point.
    6. 2026-05-14 data point: Chrome-MCP failed today after one good day yesterday — recurrence is direct observation.

  Strength of support: Strong

  Summary: Recurring-failure framed as credential issue is documented anti-pattern across safety engineering (Reason, Hollnagel), SRE practice (Beyer, Allspaw), and the C2A2-internal PRESUMPTION-159 cluster. The 2026-05-14 recurrence after a one-day recovery is direct evidence of the pattern. PRESUMPTION-159 (REVISE) is the architectural counterpart; PRESUMPTION-177 extends the cluster. Strong support: the inference is well-grounded; architectural-failure-mode framing should replace credential-issue framing.

  Caveats: (a) The presumption is about framing, not about the immediate operational response (degraded-mode-with-visible-flag is correct); (b) Cluster: PRESUMPTION-159 (REVISE carry-forward), substrate-decomposition cluster.

  Recommendation: SUPPORTED (Strong) — recurring-failure-as-credential framing is documented anti-pattern; architectural reframing recommended
