SEARCH-FOR-PRESUMPTION-404:
  Date searched: 2026-06-26
  Original item: PRESUMPTION-404
  Original statement: "That single-Mac launchd durability transfers to the deferred distributed/VPS-hub future"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-404
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: single-node supervision guarantees presumed to carry over to a distributed deployment
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. (None supportive of transfer.) Distributed-systems literature treats single-node and multi-node durability/availability as DIFFERENT problems requiring different mechanisms (replication, consensus).

  Strength of support: None

  Summary: No literature supports the presumption that single-node launchd durability transfers intact to a distributed/VPS-hub deployment. The well-established position is the opposite: distributed durability and availability require replication and consensus (Lamport/Paxos, Raft) and confront CAP trade-offs that simply do not exist for a single supervised process. The supportive direction is empty; 15b carries the substantive challenge. Note the presumption is about a DEFERRED future, so current risk is latent.

  Caveats: launchd supervision remains correct for the CURRENT single-node deployment (see ASSUMPTION-371); only the transfer claim is unsupported.

  Search scope: Distributed durability/availability. Adequate.

  Recommendation: NO-SUPPORT-FOUND
