SEARCH-FOR-PRESUMPTION-118:
  Date searched: 2026-05-10
  Original item: PRESUMPTION-118
  Original statement: "DECISION-027 unify-vs-split presumed reversible at low epistemic cost (no asymmetric-reversibility risk acknowledged)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-118
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-09 EOD ADR scope-extension question
      15a: Searched for ADR reversibility cost asymmetry literature
    Current status: NO-SUPPORT-FOUND

  Sources:
    1. Nygard (2011) "Documenting Architecture Decisions" — ADR revision is a documented practice but the cost of revision is acknowledged as non-trivial; "low epistemic cost" framing is not supported.
    2. Bezos memo on "two-way doors vs. one-way doors" (Amazon shareholder letter 2015) — asymmetric-reversibility analysis is canonical for architecture decisions; treating decisions as default-reversible without analysis is documented as a failure mode.
    3. Brown et al. (1998) "AntiPatterns" — retroactive ADR splitting is documented as more expensive than starting split, due to downstream coupling that accumulates while the unified ADR is in force.
    4. (No literature supports treating unify-vs-split as reversible at low cost without asymmetric-reversibility analysis.)
    5. C2A2-internal: DECISION-027 has not yet been canonized — the decision is at the lowest-cost reversibility window now; once canonized, downstream agents will couple to whichever scope is chosen.

  Strength of support: None

  Summary: No literature supports treating unify-vs-split as reversible at low epistemic cost without explicit asymmetric-reversibility analysis. The Bezos / Nygard / AntiPattern literatures uniformly require explicit reversibility analysis before architecture decisions; treating reversibility as default is a documented anti-pattern. The presumption operates against literature consensus.

  Caveats: This is a NO-SUPPORT-FOUND for the FOR direction.

  Recommendation: NO-SUPPORT-FOUND
