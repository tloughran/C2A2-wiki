SEARCH-FOR-ASSUMPTION-275:
  Date searched: 2026-06-06
  Original item: ASSUMPTION-275
  Original statement: Graph and Cards are two non-redundant "verbs over one dataset"; neither can absorb the other's function, so keeping both is justified (P4 "keep only one" rejected).

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-275
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as a stated justification for maintaining two coordinated surfaces (graph + cards directory) over one corpus.
      15a: Searched coordinated-multiple-views (CMV) literature on the value of complementary views over one dataset.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Baldonado, Woodruff & Kuchinsky, 2000. "Guidelines for Using Multiple Views in Information Visualization." AVI. — The Rule of Diversity: use multiple views when there are correlations or disjoint sets of attributes that a single view cannot present; directly supports keeping two surfaces when each affords a function the other cannot. (Note: the same paper's Rule of Parsimony is the matching cost caveat — see 15b.)
    2. Roberts, 2007. "State of the Art: Coordinated & Multiple Views in Exploratory Visualization." CMV. — CMV improves task performance and reveals relationships not visible in any single view; an overview/structure view plus a detail/list view is a canonical, validated pairing.
    3. Wang Baldonado / Scherr, "Multiple and Coordinated Views in Information Visualization." — Multiple views give different perspectives of the same data (alternative viewpoints, contextual information), supporting the "two verbs, one dataset" framing where a node-link graph (structure/relations) and a card list (attributes/lookup) are complementary, not duplicative.

  Strength of support: Strong

  Summary: CMV is one of the best-established patterns in information visualization, and it directly supports the assumption: a relational/structure surface (the graph) and an attribute/lookup surface (the cards directory) present complementary affordances over one corpus, and the literature documents performance and insight benefits from such pairings. The "neither can absorb the other" claim aligns with the Rule of Diversity. The literature's one binding condition is the Rule of Parsimony — keep a view only while its benefit exceeds its cost — which is the caveat, not a refutation.

  Caveats: Support is conditional on the two views genuinely serving disjoint functions over the SAME corpus. If Cards can be reduced to a saved/filtered state of the Graph (i.e., one surface can absorb the other), the Rule of Diversity no longer applies and the Rule of Parsimony argues for one. This also presumes the two surfaces share a dataset — a presumption directly doubted by PRESUMPTION-306 (measured near-total disjointness), which weakens the "over ONE dataset" half of the claim.

  Recommendation: SUPPORTED
