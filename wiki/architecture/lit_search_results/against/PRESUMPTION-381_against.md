SEARCH-AGAINST-PRESUMPTION-381:
  Date searched: 2026-06-24
  Original item: PRESUMPTION-381
  Original statement: "That more inbound hub connectivity is simply good - an all-to-one index node may dilute the sociogram's signal (connects-all = distinguishes-nothing)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-381
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: 'more connectivity = better' applied without considering signal dilution
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Hub/hairball dilution (arXiv 2304.01896 topological filtering; arXiv 2312.03347 hub identification). - High-degree nodes placed centrally tangle force-directed layouts and reduce the legibility of community structure - 'connects-all = distinguishes-nothing'.
    2. Community-detection degradation. - Community-quality measures depend on internal-degree distribution; a node linked to everything blurs cluster boundaries and can merge distinct communities.
    3. Information-content of a universal link. - A relation present between ALL pairs carries zero discriminative information (cf. IDF intuition).

  Strength of challenge: Moderate-Strong

  Summary: Moderate-strong challenge to 'more inbound hub connectivity is simply good'. A node connected to everything is, by construction, uninformative for distinguishing structure: the visualization literature shows universal hubs create hairballs and reduce legibility, and community detection degrades when a node bridges all clusters. So an all-to-one index can raise connectivity counts while diluting exactly the sociogram signal the project reads. The monotone 'more = better' direction is the error; connectivity has an interior optimum for legibility, not a maximum.

  Specific risks: Adding a universal index node (344) inflates connectivity metrics while degrading the sociogram and community detection - improving the number the audit watches and worsening the structure it interprets.

  Mitigations available: Exclude/down-weight universal hubs in analytical views; evaluate connectivity changes by their effect on community legibility, not raw inbound count.

  STEELMAN:
    Strongest counterargument: If universal/index nodes are confined to navigation and stripped from analytical graph views, then 'more navigational connectivity' is harmless and the dilution never reaches the sociogram.
    What would need to be true for C2A2 to be safe: Analytical (sociogram/community) pipelines must exclude universal hubs.
    How to test: Modularity/legibility metrics with vs without the index node.

  Search scope: hub dilution; community-detection degradation; discriminative information. Comprehensive.

  Recommendation: CHALLENGED
