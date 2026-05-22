SEARCH-AGAINST-ASSUMPTION-202:
  Date searched: 2026-05-21
  Original item: ASSUMPTION-202
  Original statement: "Synergistic coils are association fibers binding narrative modules (testable corollary: coil density tracks independent integration)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-202
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: cross-tradition 'coils' framed as association fibers, with a testable corollary that coil density tracks independent integration.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E / REVISE-040 noted)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Fortunato & Barthelemy (2007). "Resolution limit in community detection," PNAS. — Modularity-based integration/module measures are resolution-dependent; density-tracks-integration can be a resolution artifact.
    2. Tallis (2011) "Aping Mankind"; Legrenzi & Umilta (2011) "Neuromania." — Caution against importing neural metaphors as explanatory structure where the substrate differs.
    3. Gentner structure-mapping (1983). — Valid analogy requires shared relational structure, not shared labels; association fibers are anatomically constrained, coils are curated/inferred.
    4. Density != integration: a dense subgraph can be redundant rather than integrative, so density need not track independent integration.

  Strength of challenge: Moderate

  Summary: The analogy is challengeable on three fronts: integration/modularity metrics are resolution-dependent (Fortunato & Barthelemy), neural metaphors can impose structure absent a substrate match, and density is not the same as functional integration. The corollary risks circularity if coils are detected by co-occurrence and integration is then read off coil density.

  Specific risks: Coil-density metrics could be reported as 'integration' while actually measuring curation density or detection resolution.

  Mitigations available: Define integration independently of the detection signal (e.g., participation coefficient with resolution sensitivity analysis); validate the analogy's transfer conditions (PRESUMPTION-221) before trusting density-as-integration.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-202
    Strongest counterargument: The corollary risks circularity — if 'coils' are detected by lexical co-occurrence and 'integration' is read off coil density, the metric measures detection density, not independent integration; and modularity's resolution limit makes the module boundaries themselves arbitrary.
    What would need to be true for C2A2 to be safe: An integration measure independent of the detection signal is used and shown resolution-stable.
    How to test: Compute integration via a held-out signal (e.g., human-judged cross-tradition relevance) and check correlation with coil density.
