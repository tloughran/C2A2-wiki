SEARCH-FOR-ASSUMPTION-448:
  Date searched: 2026-07-13
  Original item: ASSUMPTION-448
  Original statement: "The knowledge graph is sufficient for thinker-agent synthesis — hub backlink concentration plus an accounted-for orphan population means 'the bottleneck is not connectivity.'"

  PROVENANCE:
    Origin: 14a
    Chain: 14a -> 15a
    Original item: ASSUMPTION-448
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-12 connectivity census conclusion
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. [Adamic, L., Lukose, R., Puniyani, A. & Huberman, B. (2001). "Search in power-law networks." Phys. Rev. E 64:046135. — High-degree-seeking local search in power-law graphs has SUBLINEAR cost in graph size: hub-and-spoke structure is genuinely efficiently searchable. This is the strongest single support for the claim.]
    2. [Kleinberg, J. (2000). "Navigation in a small world." Nature 406:845. — Short paths are not merely present but FINDABLE by agents with purely local information, under the right link-distance distribution. Supports navigability of a hub-rich graph without global knowledge.]
    3. [Edge, D., Trinh, H., Cheng, N., Bradley, J., Chao, A., Mody, A., Truitt, S. & Larson, J. (2024). "From Local to Global: A Graph RAG Approach to Query-Focused Summarization." arXiv:2404.16130. — Global sensemaking succeeds from COMMUNITY SUMMARIES over a Leiden hierarchy rather than exhaustive node traversal; evidence that hub/community structure alone can support corpus-level synthesis.]
  Strength of support: Moderate — but self-limiting (see Caveats)
  Summary: There is real support that hub-concentrated, community-structured graphs are searchable and summarisable, and that synthesis need not traverse every node. Adamic et al. establish sublinear search cost in exactly the degree regime C2A2's vault exhibits, and GraphRAG demonstrates working global synthesis from hub/community structure. However, the support carries a precondition that must be stated plainly: Adamic's result REQUIRES that hubs be connected to the periphery (high-degree nodes have edges to the low-degree ones), and GraphRAG's Leiden partition is mutually exclusive and collectively exhaustive — every node lands in some community. Both presuppose the periphery is ATTACHED. A vault in which ~75% of notes have zero inbound links violates that precondition rather than satisfying it.
  Caveats: The supporting literature supports the claim's conclusion only in graphs whose periphery is reachable. C2A2's stated premise (a large accounted-for orphan population) is precisely the condition under which these results do not apply. Support is therefore conditional on a fact the assumption asserts to be false.
  Recommendation: PARTIALLY-SUPPORTED
