SEARCH-FOR-ASSUMPTION-357:
  Date searched: 2026-06-25
  Original item: ASSUMPTION-357
  Original statement: "Real synthesis often coins NEW vocabulary, so the shared-id test risks a false negative; an honest fix needs a contemporaneous derived_from lineage field"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-357
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted; gates OPEN-091; instrument-before-trust
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Fauconnier & Turner 2002. 'The Way We Think: Conceptual Blending.' - Genuine conceptual integration characteristically produces NEW emergent structure/terms not present in either input, so a shared-token test would miss it.
    2. Small 1973 / co-citation & bibliographic-coupling literature. - Identifier-overlap measures of relatedness systematically miss links that are conceptual but lexically novel (false negatives).
    3. Interdisciplinarity measurement (Porter & Rafols 2009). - Cross-field synthesis frequently introduces hybrid vocabulary; provenance/lineage tracking is the standard remedy for attributing derived concepts.

  Strength of support: Moderate

  Summary: The assumption's worry is well-founded: theories of conceptual synthesis predict that real integration coins novel vocabulary, and identifier/keyword-overlap proxies are known to generate false negatives precisely on such lexically-novel links. The proposed remedy - a contemporaneous derived_from lineage field - matches the standard provenance approach to attributing derived concepts, and reflects sound 'instrument-before-trust' discipline (don't trust a shared-id PASS/FAIL until you've measured its false-negative behavior).

  Caveats: Supports the false-NEGATIVE direction (synthesis missed by shared-id). It does not by itself validate the PASS direction (does shared-id overlap validly mean integration?) - that converse construct-validity question is PRESUMPTION-391. A lineage field also introduces its own annotation overhead and error.

  Search scope: Conceptual blending; co-citation false negatives; provenance fields. Adequate.

  Recommendation: SUPPORTED
