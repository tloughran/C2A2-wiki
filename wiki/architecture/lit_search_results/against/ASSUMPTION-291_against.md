SEARCH-AGAINST-ASSUMPTION-291:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-291
  Original statement: Shared wiki-node references are a meaningful relational signal between agents — a valid sociogram edge model.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-291
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated design assumption from 2026-06-08 OpenStory→Agent-Explorer build sessions
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Colavizza & Franceschet et al. line, summarized in J. Scientometric Research, 2024. "Bibliographic Coupling and Conceptual Similarity: Are the Bibliographically Coupled Papers also Conceptually Similar?" — Shared references are no guarantee that two works use the same information; coupling strength is driven more by total reference counts than by genuine shared content (sparsity artifact).
    2. Boyack & Klavans, 2010. "Co-citation analysis, bibliographic coupling, and direct citation: Which citation approach represents the research front most accurately?" JASIST 61(12). — Even in the home domain (papers), shared-reference methods only weakly recover latent structure and disagree with each other; accuracy is method- and field-dependent, not a given.
    3. Borgatti & Halgin, 2011. "On Network Theory." Organization Science 22(5). — Tie-type validity: co-occurrence/affiliation ties (two-mode projections) are not interaction ties; treating similarity edges as social/relational edges conflates distinct network theories and invalidates flow-based interpretations (influence, coordination).
    4. Zhou, Ren, Medo, Zhang, 2007. "Bipartite network projection and personal recommendation." Phys. Rev. E 76. — Projecting a bipartite (agent–wiki-node) graph onto one mode destroys information and inflates clustering; hub nodes (popular wiki pages) generate dense spurious cliques among otherwise unrelated agents.
  Strength of challenge: Strong
  Summary: The proposed edge model is a one-mode projection of an agent–document bipartite graph, and the literature on exactly this construction is cautionary on three fronts. First, shared-reference similarity is a weak and confounded proxy even in bibliometrics, dominated by reference-list length and hub popularity rather than genuine relatedness. Second, projection mathematically inflates connectivity: a handful of popular wiki nodes (e.g., Master/Architecture pages many agents touch) will produce near-complete subgraphs carrying no relational information. Third, and most fundamentally, network theory distinguishes affiliation/similarity ties from interaction ties; a "sociogram" implies social relations between agents, but two agents citing the same page have not interacted, coordinated, or influenced one another. The edges are real similarity signal but invalid as sociogram semantics without weighting and reframing.
  Specific risks: Agent Explorer displays dense hairballs around popular wiki nodes that users read as "these agents work together"; downstream analyses (centrality, communities) measure wiki-page popularity, not agent relations; design decisions get made from artifact structure.
  Mitigations available: Hub-discounting weights (hyperbolic/resource-allocation weighting per Zhou et al.; TF-IDF on node rarity); minimum-shared-reference thresholds; backbone extraction (Serrano et al. 2009 disparity filter); rename/label edges "shared context," not relations; reserve sociogram language for actual interaction edges (one agent consuming another's output).
  STEELMAN:
    Strongest counterargument: For C2A2's purpose the edges need only mean "these agents operate on shared knowledge territory," which shared references measure directly and validly; bibliographic coupling remains the best-performing pure-citation method (Boyack & Klavans) and works at small scale where edges can be visually inspected. With rarity weighting, the hub artifact is controllable.
    What would need to be true for C2A2 to be safe: Edges are weighted by node rarity, thresholded, and labeled as similarity (not interaction); users are not invited to read them as collaboration.
    How to test: Compute the edge set with and without the top-5 most-referenced wiki nodes; if the sociogram's structure collapses or reorders substantially, edges were popularity artifacts. Spot-check 10 random edges against human judgment of "actually related agents."
  Search scope: 1 search — "criticism limitations co-citation analysis bibliographic coupling validity similarity measure". Plus established network-science literature.
  Recommendation: CHALLENGED
