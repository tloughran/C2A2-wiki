SEARCH-FOR-ASSUMPTION-453:
  Date searched: 2026-07-16
  Original item: ASSUMPTION-453
  Original statement: Both connectivity claims hinge entirely on whether retrieval over the vault is traversal-based or embedding-based; determining the retrieval mode settles ASSUMPTION-447 and ASSUMPTION-448 at once.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-453
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted/inferred to intake queue (for_lit_search.md)
      15a: Searched for supporting literature; result PARTIALLY-SUPPORTED (strength Moderate)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. GraphRAG / hybrid-retrieval literature (Microsoft GraphRAG; Neo4j 'Advanced RAG'; arXiv:2507.03226). Graph-traversal retrieval and dense-embedding retrieval have materially different reachability properties: traversal exploits backlink/edge structure for multi-hop connections that vector similarity misses, and vice-versa. So the retrieval mode does substantially determine which connectivity claims hold.
    2. Reciprocal Rank Fusion hybrid-RAG results: because production systems increasingly fuse both modes, connectivity is often a blend rather than one-or-the-other - supporting that the mode is decisive while cautioning it may not be binary.

  Strength of support: Moderate

  Summary: The retrieval literature supports the assumption's core: traversal-based and embedding-based retrieval have genuinely different structural consequences, so identifying which one the thinker agents actually consume would largely settle whether backlink structure matters for connectivity. Support is moderate rather than strong because modern stacks are frequently hybrid, in which case 'the mode' is not a single switch and both A-447 and A-448 could be partially true.

  Caveats: This is an EMPIRICAL item: the literature only frames the question; the actual settlement requires reading C2A2's retrieval path and running the BFS-reachability test proposed in the search angle.

  Recommendation: PARTIALLY-SUPPORTED
