SEARCH-AGAINST-PRESUMPTION-414:
  Date searched: 2026-06-29
  Original item: PRESUMPTION-414
  Original statement: "[inferred] That some connectivity measure is the right proxy for vault 'health for synthesis' at all (vs content depth/coverage), even while questioning which edge type to count."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-414
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: connectivity presumed to proxy synthesis health
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Multi-dimensional KG quality frameworks. - Quality decomposes into completeness, content/property quality, coverage, and linkability - connectivity is one axis among several, and optimizing it alone is not validated as "health."
    2. Goodhart / proxy-metric risk. - When a structural metric becomes the target, it ceases to be a good measure; treating connectivity as THE proxy invites gaming (e.g., adding low-value edges that raise connectivity without raising synthesis value).
    3. Content-quality primacy in retrieval. - For synthesis and retrieval, content depth and coverage often predict usefulness more directly than topology; a densely linked but shallow corpus does not synthesize well.

  Strength of challenge: Moderate

  Summary: The presumption that connectivity (any edge type) is the right proxy for synthesis health is challenged by the consensus that knowledge-base quality is multi-dimensional and that content depth/coverage may matter more for synthesis than topology. There is a real Goodhart risk: improving a connectivity metric can be decoupled from improving actual synthesis capacity. The presumption privileges a measurable structural signal over the harder-to-measure content dimension.

  Specific risks: Optimizing connectivity could produce a well-linked but shallow vault; effort spent on edges rather than content; false sense of "health."

  Mitigations available: Pair connectivity with content-coverage/depth measures; validate that connectivity changes track actual synthesis-task performance, not just topology.

  STEELMAN:
    Item: PRESUMPTION-414
    Strongest counterargument: Connectivity is attractive because it is measurable, but knowledge-base health for synthesis is multi-dimensional; making any single topology metric the proxy risks Goodharting it - raising the number while leaving synthesis capacity (which depends on content depth and coverage) untouched.
    What would need to be true for C2A2 to be safe: Connectivity is validated as correlating with actual synthesis-task outcomes, and is used alongside content/coverage measures rather than as the sole proxy.
    How to test: Correlate connectivity changes with performance on a real synthesis/retrieval task before trusting it as a health proxy.

  Search scope: KG quality dimensions; Goodhart's law; content vs topology for retrieval. Adequate.

  Recommendation: CHALLENGED
