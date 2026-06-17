SEARCH-AGAINST-ASSUMPTION-327:
  Date searched: 2026-06-17
  Original item: ASSUMPTION-327
  Original statement: "A deterministic (reproducible) layout fan is preferable to random jitter for separating co-located 3D nodes."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-327
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the layout-engineering choice (deterministic fan over jitter)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Graphical perception (Cleveland & McGill 1984) — viewers decode POSITION as a quantitative channel with high accuracy; a deterministic fan produces a STABLE, ORDERED arrangement that viewers will reliably over-read as meaningful structure. A consistent artifact is decoded consistently — i.e., consistently misleadingly.
    2. Lie-factor / spurious-pattern caution (Tufte; viz pitfalls) — a regular, reproducible geometric fan can manufacture an apparent pattern (rings/arcs/gradients) where the data has none; randomness at least signals "no structure here," whereas a tidy fan signals false order.
    3. Anti-pattern of semantic-looking incidental encoding — deterministic layouts that encode nothing can be MORE deceptive than jitter precisely because their reproducibility invites the viewer to infer a rule.

  Strength of challenge: Moderate

  Summary: For REPRODUCIBILITY, determinism wins (15a). But the assumption frames determinism as flatly "preferable," and on the PERCEPTION axis it can be worse: Cleveland & McGill's positional decoding means a stable, ordered fan is reliably read as meaningful, so a deterministic non-semantic layout can manufacture spurious structure that random jitter (read as "noise, ignore") does not. The real comparison is not determinism vs jitter but semantic-vs-incidental encoding; determinism is preferable ONLY if the fan is clearly marked as non-meaning-bearing.

  Specific risks: Viewers (including the sole expert) infer rings/clusters/orderings from the fan that reflect the algorithm, not the data; this is the trace-vs-substance error and couples directly to PRESUMPTION-358 (resolvability mistaken for fidelity).

  Mitigations available: Keep determinism for reproducibility BUT visually mark the fan as incidental (uniform/neutral styling, explicit "positions within a node-cluster are non-semantic" note); avoid orderings that look like a scale; reserve position for meaning elsewhere.

  STEELMAN:
    Strongest counterargument: Reproducibility is a hard requirement for diffing, regression-testing and mental-map preservation, and any separation scheme (including jitter) places nodes at non-data positions, so determinism strictly dominates: it gets the same legibility as jitter PLUS reproducibility, and the over-reading risk applies equally to both.
    What would need to be true for C2A2 to be safe: The fan is explicitly non-semantic to viewers, its geometry does not mimic an ordered scale, and position is not simultaneously used to carry meaning that the fan could corrupt.
    How to test: Show the fan to a naive viewer and ask what the arrangement "means"; if they infer structure, the determinism is being over-read and needs an incidental-encoding marker.

  Search scope: positional-encoding perception (Cleveland & McGill); spurious-pattern/lie-factor; incidental vs semantic spatial encoding. Comprehensive. (Couples PRESUMPTION-358.)

  Recommendation: PARTIALLY-CHALLENGED
