SEARCH-FOR-ASSUMPTION-340:
  Date searched: 2026-06-24
  Original item: ASSUMPTION-340
  Original statement: "Reconnecting the ~15 tradition hub pages yields more graph-health value than seeding a thousand leaves (hub leverage)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-340
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 06-23 audit as a stated prioritization claim
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Centrality / network-repair literature (Gomez, Centrality in Networks; MDPI Mathematics 9(18):2294 important-node selection). - Reconnecting high-centrality nodes restores global reachability more efficiently than equivalent edits to peripheral nodes; targeted hub repair has outsized effect on integration.
    2. Module-based network analysis (arXiv 1502.00353). - The nodes that link different communities dominate global connectivity; restoring a small set of such nodes recovers the giant component faster than seeding many leaves.
    3. GraphRAG construction (arXiv 2507.03226). - A few well-placed high-connectivity links yield more retrieval value than many loosely-related links.

  Strength of support: Moderate

  Summary: Network-repair and centrality literature broadly supports hub-leverage: a small number of high-centrality reconnections restore global reachability and integration far more efficiently than a large number of peripheral (leaf) additions. For graph-health-as-reachability, reconnecting ~15 tradition hubs is the high-leverage move. The support is moderate rather than strong because 'leverage' depends on which centrality matters (closeness/degree vs betweenness) and on whether the 15 hubs are in fact bridge nodes.

  Caveats: Hubs maximize degree/closeness leverage but not necessarily betweenness - bridge (between-community) nodes can have higher betweenness than hubs (see AGAINST). 'Graph-health value' must be defined as reachability for the claim to hold cleanly.

  Search scope: betweenness/closeness centrality; network repair; module-based connectivity. Adequate.

  Recommendation: PARTIALLY-SUPPORTED
