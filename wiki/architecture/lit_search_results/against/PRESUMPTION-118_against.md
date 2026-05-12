SEARCH-AGAINST-PRESUMPTION-118:
  Date searched: 2026-05-10
  Original item: PRESUMPTION-118
  Original statement: "DECISION-027 unify-vs-split presumed reversible at low epistemic cost (no asymmetric-reversibility risk acknowledged)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-118
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-09 EOD ADR scope-extension question
      15b: Searched for counter-evidence on retroactive ADR splitting / merging cost
    Current status: CHALLENGED

  Sources:
    1. Bezos shareholder letter (2015) "two-way doors vs. one-way doors" — asymmetric-reversibility analysis is canonical for architecture decisions; treating decisions as default-reversible is documented failure mode.
    2. Nygard (2011) "Documenting Architecture Decisions" — ADR revision is documented practice but cost is non-trivial; "low epistemic cost" framing not supported.
    3. Brown et al. (1998) "AntiPatterns" — retroactive ADR splitting is documented as more expensive than starting split, due to downstream coupling that accumulates while unified ADR is in force.
    4. Software-architecture literature (Bass, Clements, Kazman 2012) — coupling-removal cost rises non-linearly with time-since-coupling-introduced; reversibility is monotonically decreasing.
    5. C2A2-internal: Once DECISION-027 is canonized at unified scope, downstream agents (tradition agents, lit-search agents, monitor agents) couple to whichever scope is chosen; coupling accumulation begins immediately at canonization.

  Strength of challenge: Strong

  Summary: The presumption that unify-vs-split is reversible at low epistemic cost is strongly challenged by Bezos / Nygard / AntiPattern / software-architecture literatures. The challenge is uniform: asymmetric-reversibility analysis is canonical; treating reversibility as default is a documented anti-pattern. Splitting is the cheap initial state; starting unified and splitting later is more expensive due to downstream coupling accumulation.

  Specific risks: (a) Downstream coupling accumulates immediately at canonization; (b) retroactive splitting requires coupling-removal across all coupled agents; (c) "low epistemic cost" framing forecloses asymmetric-reversibility analysis.

  Mitigations available: (a) Explicit asymmetric-reversibility analysis before canonization; (b) start split (DECISION-027 + DECISION-028) and merge later if substrate-coupling proves dominant; (c) document the reversibility cost explicitly in the ADR.

  Recommendation: CHALLENGED (literature consensus strong against treating reversibility as default; asymmetric-reversibility analysis is canonical guard)

  STEELMAN:
    Item: PRESUMPTION-118
    Strongest counterargument: The Bezos two-way-door framework is canonical: architecture decisions are categorized by reversibility cost before commitment. Treating reversibility as default forecloses this analysis. ADR splitting is documented as more expensive than ADR merging — split is the cheap initial state. The C2A2 self-awareness pipeline has multiple downstream agents (tradition agents, lit-search agents, monitor agents) that will couple to whichever scope is chosen at canonization; coupling accumulation begins immediately. The "low epistemic cost" framing is the mistake the AntiPatterns literature was written to caution against.
    What would need to be true for C2A2 to be safe: (a) Asymmetric-reversibility analysis explicit before canonization; (b) start split if reversibility cost is asymmetric in the split direction; (c) document reversibility cost in the ADR.
    How to test: Estimate the cost of splitting unified DECISION-027 in 6 months; estimate the cost of merging split DECISION-027/028 in 6 months; the cheaper direction is the canonical starting state.
