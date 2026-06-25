SEARCH-FOR-ASSUMPTION-338:
  Date searched: 2026-06-24
  Original item: ASSUMPTION-338
  Original statement: "The vault is intentionally hub-and-spoke, not densely cross-linked, and this topology is healthy (low backlink density is design, not defect)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-338
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 06-23 Sewing-Agent bootstrap audit as a stated topology claim
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Barabasi-Albert / scale-free network literature (Wikipedia link-structure study, arXiv cs/0611068; Scale-free network, Wikipedia). - Large collaborative wikis self-organize into hub-and-spoke (preferential attachment to high-degree pages like countries/years); hub-spoke is the EXPECTED emergent topology, not a defect.
    2. Emergent scale-free networks (PNAS Nexus 2024, pgae236). - Scale-free robustness is rooted in inhomogeneous connectivity; the majority of nodes carry few links by design, so low average backlink density is consistent with a healthy, robust structure.
    3. Memgraph/NetworkX community-detection practice. - Hub-organized graphs remain navigable and cluster cleanly; hub pages function as legitimate entry points.

  Strength of support: Moderate

  Summary: Network science supports the descriptive half of the claim strongly: collaborative knowledge graphs naturally become hub-and-spoke via preferential attachment, and such topologies are robust to random failure precisely because most nodes are low-degree. Low backlink density is therefore consistent with normal, healthy scale-free structure rather than evidence of defect. Support for 'intentional' and 'healthy' is weaker - the topology is emergent, and 'healthy' depends on the task the graph must serve.

  Caveats: Support covers 'normal/robust', not 'optimal for synthesis'. Scale-free robustness is to RANDOM node loss; hub-targeted loss is a separate, fragile case (see 383). 'Intentional' is not established - emergence is not design.

  Search scope: scale-free topology; Wikipedia link structure; network robustness. Adequate.

  Recommendation: PARTIALLY-SUPPORTED
