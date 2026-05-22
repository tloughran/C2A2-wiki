SEARCH-AGAINST-PRESUMPTION-229:
  Date searched: 2026-05-21
  Original item: PRESUMPTION-229
  Original statement: "The connectome viz + network-neuroscience metrics stay legible/meaningful at much larger N (scale blindness vs the 2000-node crash cap)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-229
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred: presumed the connectome visualization and its network-neuroscience metrics remain legible and meaningful at much larger N, despite the existing 2000-node crash cap.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E / REVISE-040 noted)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. The "hairball" problem (Ghoniem et al. 2004). — Node-link diagrams become illegible as N/density grow; the current viz will degrade.
    2. Fortunato & Barthelemy (2007) resolution limit; Telesford et al. (2011) / van den Heuvel small-worldness normalization. — Connectome metrics are size/density-dependent, so "meaningful at larger N" is not given.
    3. In-system evidence: the 2000-node crash cap. — A documented hard scale limit; the presumption assumes past a barrier the system already hit.

  Strength of challenge: Strong

  Summary: Strong challenge: node-link legibility collapses at scale (hairball), several connectome metrics are explicitly size/density-dependent (resolution limit; small-worldness normalization), and the system already enforces a 2000-node crash cap — direct evidence that scale is a live constraint. The failure is gradual/future but real.

  Specific risks: Both the visualization and the metric values silently degrade as the corpus grows; conclusions drawn at large N may be artifacts of size.

  Mitigations available: Adopt size-normalized metrics with null models; plan multiscale/matrix representations before crossing scale thresholds; set a metric-stability monitor tied to N.

  Recommendation: CHALLENGED (strong)

  STEELMAN:
    Item: PRESUMPTION-229
    Strongest counterargument: The presumption projects small-N legibility and metric behavior past a barrier the system has already hit (the 2000-node crash cap); node-link diagrams hairball at scale and connectome metrics like modularity and small-worldness are size/density-dependent, so both the picture and the numbers can degrade without warning as the corpus grows.
    What would need to be true for C2A2 to be safe: Size-normalized metrics and multiscale representations are adopted before scaling, with a stability monitor.
    How to test: Compute metrics on nested subgraphs of increasing N and check for drift; render at increasing N and assess legibility.
