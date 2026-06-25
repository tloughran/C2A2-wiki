SEARCH-AGAINST-ASSUMPTION-343:
  Date searched: 2026-06-24
  Original item: ASSUMPTION-343
  Original statement: "Synthesis stubs should be created only where the link graph demands them (broken bridge links); fabricating un-asked-for bridges is speculative"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-343
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 06-23 audit as a stated restraint criterion for stub creation
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Demand-signal incompleteness (link-prediction literature, arXiv 2403.18855; KG completion, MDPI 13(3):485). - Many warranted links are latent and never explicitly stubbed; relying on broken links under-generates needed bridges.
    2. Circularity (tension-twin PRESUMPTION-384). - 'Demand = broken link' lets the graph only request bridges someone already gestured at, making 'no demand' self-confirming.
    3. Cross-domain bridging. - The most valuable cross-tradition synthesis links are exactly the non-obvious ones no author thought to stub.

  Strength of challenge: Moderate

  Summary: The restraint against fabricating bridges is reasonable, but the CRITERION ('only where the link graph demands') is challenged as incomplete and self-justifying. Link-prediction research shows warranted connections are routinely latent - absent from explicit link structure - so broken links capture only the bridges someone already pointed at. For cross-tradition synthesis, the highest-value bridges are precisely the non-obvious ones with no broken link, which this criterion will never surface. The rule is safe against over-generation but systematically blind to under-generation.

  Specific risks: Genuine cross-tradition synthesis bridges go unbuilt because no broken link names them; the graph stays sparse exactly where it most needs connecting.

  Mitigations available: Augment broken-link demand with independent bridge enumeration (embedding link-prediction over the PRS connectome); treat broken links as a floor, not the whole demand.

  STEELMAN:
    Strongest counterargument: If the only acceptable stubs are those with explicit demand AND a separate process enumerates latent bridges, then 'no fabrication' is a safe conservative rule rather than an under-generation trap.
    What would need to be true for C2A2 to be safe: A second, demand-independent channel must exist to surface warranted-but-unstubbed bridges.
    How to test: Run link-prediction over the connectome; count warranted bridges with no broken link - if many, the criterion under-generates.

  Search scope: latent links; demand-signal completeness. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED
