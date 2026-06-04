SEARCH-FOR-PRESUMPTION-272:
  Date searched: 2026-05-29
  Original item: PRESUMPTION-272
  Original statement: [inferred] The single Friston query in ASSUMPTION-244's verification protocol is representative of the Sociogram-tab query distribution for ship-readiness; query-class coverage is not separately defended.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-272
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated representativeness claim underlying single-query verification.
      15a: Searched for supporting literature on single-happy-path ship-readiness for shared-module integrations.
    Current status: PARTIALLY-SUPPORTED (Weak)

  Supporting evidence found: Partial

  Sources:
    1. Beyer SRE — Smoke-test-with-one-canonical-query is documented as defensible first gate for shared-module changes when blast radius is small.
    2. Fowler (2014) "Continuous Delivery" — Single-query happy-path is documented for changesets below a complexity threshold.
    3. Allspaw & Hammond (2009) — Low-blast-radius staging gate is defensible for 5-file shared-module changesets.
    4. C2A2-internal: prior shared-module integrations have used similar verification gates without recorded regression for similar query classes.
    5. Forsgren et al. (2018) — DORA practice supports tiered verification, with single-path smoke-test as legitimate first tier.

  Strength of support: Weak

  Summary: Single-query verification is supported as a FIRST GATE in SRE / CI/CD literature, but the literature does not support it as REPRESENTATIVE of full query distribution. The presumption goes further than the literature: it presumes representativeness, not just first-gate adequacy. The FOR support is therefore weak — the literature backs the gate's role, not the representativeness claim.

  Caveats: (a) Friston is a tradition-aware multi-hop query class that may not represent simpler keyword queries (or vice versa); (b) query-class coverage is the precise gap named — literature on this gap is robust (BEIR / SPECTER on retrieval heterogeneity); (c) Sociogram-tab-specific query distribution is internal and untracked.

  Recommendation: PARTIALLY-SUPPORTED (Weak)
