SEARCH-FOR-PRESUMPTION-084:
  Date searched: 2026-04-28
  Original item: PRESUMPTION-084
  Original statement: "Pre-flight cowork-directory grant failure pattern continues without DECISION-026 candidate (no formal aggregation)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-084
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced — recurring pre-flight failure pattern not formalized as architectural decision
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED (Weak-Moderate)

  Sources:
    1. Nygard (2007) "Release It!" — circuit-breaker patterns endorse explicit aggregation of recurring failures; the implicit version (let it recur, surface narratively) is treated as anti-pattern.
    2. Beyer et al. (2016) "Site Reliability Engineering" — auto-fail behavior in scheduled tasks is tolerated for transient failures; pattern-level recurrence requires explicit handling.
    3. C2A2-internal: candidate-DECISION-024 turn-cap analysis is the parallel-case; pre-flight stalls are a structurally distinct mode.

  Strength of support: Weak-Moderate

  Summary: The circuit-breaker / explicit-aggregation literature supports formalizing recurring failure patterns rather than letting them be surfaced narratively. The presumption (that no DECISION-026 candidate is needed) is therefore weakly supported at best — and is in tension with the architectural recommendation literature.

  Caveats: (a) The presumption is structurally adjacent to PRESUMPTION-069 (absence-as-event), already REVISE-flagged 2026-04-21.

  Recommendation: PARTIALLY-SUPPORTED (Weak-Moderate — the literature actually leans against the presumption; the SUPPORT here is mostly that informal aggregation is sometimes tolerated for low-stakes failures)
