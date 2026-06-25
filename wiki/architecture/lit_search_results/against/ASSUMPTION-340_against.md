SEARCH-AGAINST-ASSUMPTION-340:
  Date searched: 2026-06-24
  Original item: ASSUMPTION-340
  Original statement: "Reconnecting the ~15 tradition hub pages yields more graph-health value than seeding a thousand leaves (hub leverage)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-340
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 06-23 audit as a stated prioritization claim
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Betweenness centrality nuance (Gomez centrality chapter; PuppyGraph). - Hub nodes often have LOW betweenness; the nodes that carry global information flow are the BRIDGES BETWEEN hubs, not the hubs themselves - so reconnecting hubs may not maximize the relevant leverage.
    2. Leaf-as-bridge cases. - Some 'leaves' connect otherwise-separate communities; seeding the RIGHT leaves can beat reconnecting hubs for cross-tradition integration.
    3. Module-based analysis (arXiv 1502.00353). - Connectivity value concentrates in community-bridging nodes; degree alone (what hubs maximize) is not the right leverage metric.

  Strength of challenge: Weak-Moderate

  Summary: The challenge is conditional: 'hub leverage' conflates degree with betweenness. The centrality literature shows hubs maximize degree but often have LOW betweenness, while the high-leverage nodes for global integration are the bridges between communities. If cross-tradition synthesis is the goal, reconnecting 15 same-type hubs may add intra-cluster degree while leaving the inter-tradition bridges (possibly 'leaves') unbuilt. So 'reconnect hubs > seed leaves' holds for reachability but may fail for the integration the project cares about.

  Specific risks: Effort could go to high-degree hub reconnection that improves a vanity reachability number while the cross-tradition bridges that actually enable synthesis stay missing.

  Mitigations available: Choose targets by betweenness/bridging value, not degree; identify the specific leaves that bridge traditions and weigh them against hub reconnection.

  STEELMAN:
    Strongest counterargument: If the 15 tradition hubs ARE the inter-community bridges (each hub connects its tradition to the others), then reconnecting them is also the high-betweenness move and the claim holds.
    What would need to be true for C2A2 to be safe: The hubs must be bridges, not just high-degree centers within their own tradition.
    How to test: Compute betweenness for the 15 hubs vs candidate bridge-leaves; compare leverage empirically.

  Search scope: betweenness vs degree; bridge nodes. Adequate.

  Recommendation: PARTIALLY-CHALLENGED
