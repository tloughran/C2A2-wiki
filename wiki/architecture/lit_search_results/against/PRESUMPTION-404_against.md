SEARCH-AGAINST-PRESUMPTION-404:
  Date searched: 2026-06-26
  Original item: PRESUMPTION-404
  Original statement: "That single-Mac launchd durability transfers to the deferred distributed/VPS-hub future"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-404
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: single-node supervision guarantees presumed to carry over to distributed deployment
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. CAP theorem (Brewer; Gilbert & Lynch 2002). - Distributed deployments face partition/consistency/availability trade-offs that a single node does not; single-node reasoning does not transfer.
    2. Consensus/replication literature (Lamport Paxos; Ongaro & Ousterhout 2014 Raft). - Multi-node durability/availability requires replication and agreement protocols; a per-node supervisor (launchd) provides neither.
    3. Distributed-systems fallacies ("the network is reliable", etc.). - Assuming single-node guarantees survive distribution is a classic, well-documented error.

  Strength of challenge: Moderate

  Summary: The presumption is a scaling-transfer error. launchd guarantees per-node process restart; it says nothing about node failure, network partition, split-brain, or cross-node consistency - the defining problems of the distributed/VPS-hub future. CAP and the consensus literature show distributed durability/availability need replication and agreement that supervision cannot supply, and the "fallacies of distributed computing" name this exact over-confidence. Risk is latent (the future is deferred), but the guarantee lapses precisely at the named next step.

  Specific risks: At the distributed step: data loss on node failure, split-brain/inconsistency, no failover - all invisible while reasoning from the single-node supervisor's success.

  Mitigations available: At the distributed step, introduce replication + consensus (Raft) and explicit consistency/availability targets; do not carry the single-node durability claim forward; re-evaluate durability design when leaving single-node.

  STEELMAN:
    Item: PRESUMPTION-404
    Strongest counterargument: Single-node supervision solves "keep one process up"; distribution introduces an orthogonal problem set (partition, replication, consensus) that supervision does not touch - so the durability guarantee does not scale, it lapses, exactly where the roadmap goes next.
    What would need to be true for C2A2 to be safe: At distribution, durability/availability are re-derived with replication+consensus; the single-node claim is retired, not extrapolated.
    How to test: At the distributed step, kill a node and partition the network; observe data loss/inconsistency that launchd cannot prevent.

  Search scope: CAP; consensus/replication; distributed fallacies. Comprehensive.

  Recommendation: CHALLENGED
