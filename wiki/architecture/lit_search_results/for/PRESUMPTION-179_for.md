SEARCH-FOR-PRESUMPTION-179:
  Date searched: 2026-05-15
  Original item: PRESUMPTION-179
  Original statement: "Reference-instance retention (Carpathi Wiki stays live) presumes dual-maintenance burden is sustainable; reference-instance bit-rot risk in FLOSS frameworks unaudited"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-179
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from Pathway 18 toolkit-extraction commitment
      15a: Searched for exemplar-instance maintenance patterns in FLOSS frameworks; showcase-vs-framework attention economics
    Current status: SUPPORTED (Strong)

  Sources:
    1. FLOSS exemplar-instance bit-rot history — Rails Showcase, Django Examples, Hugo Themes: reference instances reliably bit-rot when not maintained as the primary deliverable.
    2. Lerner & Tirole (2002) "Some Simple Economics of Open Source" — showcase-vs-framework attention economics: maintainer attention follows downloads; reference instances lose attention.
    3. Brooks (1995) — second-system effect: reference instance starts as canonical, becomes legacy as framework evolves.
    4. Greenfield-vs-brownfield software engineering literature — reference instances become brownfield; framework moves on.
    5. C2A2-internal: Carpathi Wiki is Tom's day-to-day operational instance; dual-maintenance (Carpathi as reference + framework as toolkit) is direct attention contention.

  Strength of support: Strong

  Summary: Reference-instance bit-rot is well-documented across FLOSS framework history. Showcase-vs-framework attention economics (Lerner-Tirole) predicts that maintainer attention moves to the higher-traffic deliverable. Reference instances bit-rot reliably. The "dual-maintenance burden is sustainable" presumption is empirically false for most FLOSS frameworks; sustainability requires specific mitigations (automated tests against reference, periodic re-instantiation). Strong support: the inference is well-grounded.

  Caveats: (a) Dual-maintenance can be sustainable with specific tooling (automated tests, CI/CD for reference); (b) Carpathi is Tom's operational instance so attention is already there; (c) Cluster: joins PRESUMPTION-173 cognitive-bandwidth concern.

  Recommendation: SUPPORTED (Strong) — reference-instance bit-rot is well-documented; mitigation tooling is load-bearing
