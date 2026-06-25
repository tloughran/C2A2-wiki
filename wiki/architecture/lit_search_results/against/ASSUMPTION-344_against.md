SEARCH-AGAINST-ASSUMPTION-344:
  Date searched: 2026-06-24
  Original item: ASSUMPTION-344
  Original statement: "A single traditions/_index.md linking all 15 hub wikis converts 15 orphans into hubs at once (GROUNDED - built + browser-verified)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-344
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 06-23 audit; GROUNDED - index built and browser-verified in-session
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Hub-node dilution (Topological filtering, arXiv 2304.01896; hub identification, arXiv 2312.03347). - A universal index node becomes a high-degree hub that tangles force-directed layouts ('hairball') and reduces community-detection legibility - 'connects-all = distinguishes-nothing'.
    2. De-orphaning by index is cosmetic for SYNTHESIS. - Converting orphan->linked via one index raises the inbound count but adds no cross-tradition semantic relation; the orphan metric improves while synthesis connectivity does not.

  Strength of challenge: Moderate

  Summary: The mechanical claim (orphan -> linked) is not contested - it is GROUNDED. The challenge is that the metric improvement is partly cosmetic and may carry a downstream cost. An all-to-one index node is a maximal-degree hub; the visualization and community-detection literature treats such nodes as signal-diluting (hairball, reduced cluster legibility). So '15 orphans -> 15 hubs at once' improves the orphan count while potentially degrading the sociogram and adding no semantic cross-tradition links. The fact is true; its value as graph health is the contested part (routed to PRESUMPTION-381).

  Specific risks: The orphan alarm is silenced by a single cosmetic edit while real cross-tradition connectivity is unchanged and the sociogram's community signal is diluted by a universal hub.

  Mitigations available: Keep the index for navigation but exclude/down-weight it in sociogram and community-detection views; do not treat the orphan-count drop as a synthesis-connectivity gain.

  STEELMAN:
    Strongest counterargument: If the index is used purely as a navigational de-orphaning device and analytical graph views exclude it, then the grounded fact stands with no dilution cost.
    What would need to be true for C2A2 to be safe: Sociogram/community analyses must exclude the index node.
    How to test: Run community detection with and without the index node; compare modularity/legibility.

  Search scope: hub dilution; cosmetic vs semantic connectivity. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED
