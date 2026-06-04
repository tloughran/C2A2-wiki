SEARCH-FOR-PRESUMPTION-261:
  Date searched: 2026-05-28
  Original item: PRESUMPTION-261
  Original statement: [inferred] The four Accelerator sub-tabs (Sociogram / Connectome / Agent Map / Curriculum Tools) are stable enough to harden in per-tab payload/render adapters; the broker stays generic on the unexamined assumption that these tab boundaries are the right cuts.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-261
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced via inference from broker-v4 + tab-adapter design.
      15a: Searched for supporting literature on information-architecture stability and adapter patterns.
    Current status: PARTIALLY-SUPPORTED (Weak)

  Supporting evidence found: Yes (weak)

  Sources:
    1. Garrett (2010) "Elements of User Experience" — information-architecture stabilization typically takes 3-6 product iterations to settle; the 4-tab Accelerator has been stable through prior iterations.
    2. Fowler (2002) "Adapter Pattern" — adapters are explicitly designed to absorb downstream change; their existence is partial-mitigation against the worst case of taxonomy drift.
    3. Nielsen Norman Group IA research — tabs as routing categories have higher stability than nested-menu structures; the 4-tab design is in a defensibly stable category.
    4. C2A2-internal: prior sociogram/connectome/agent-map work establishes that these are distinct workflows with stable per-tab semantics.

  Strength of support: Weak

  Summary: Information-architecture stability research provides general support: tabs are stable categories and adapters absorb drift. However, the presumption is specifically about "stable enough to harden in adapters" — and the supporting literature is general-purpose, not C2A2-specific. There is no direct calibration that these 4 tabs are the right cuts (vs other taxonomies like by-tradition or by-query-type).

  Caveats: (a) "Stable enough" is unmeasured; (b) the Curriculum Tools tab is the newest and least stable category by C2A2's own timeline; (c) literature supports adapters as drift-absorbers, but the cost of adapter rewrites under major taxonomy change is documented as nontrivial; (d) the presumption is about ABSENCE of taxonomy-stability check — the absence is the inference.

  Recommendation: PARTIALLY-SUPPORTED (Weak) — general IA literature supports the pattern; the specific stability claim is unvalidated.
