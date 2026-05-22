SEARCH-AGAINST-PRESUMPTION-210:
  Date searched: 2026-05-20
  Original item: PRESUMPTION-210
  Original statement: "Raw queue depth is a valid proxy for 'generate more?' — no decomposition before throttling."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-210
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — generation throttling keyed off raw queue depth, without decomposing into generation-rate vs throughput-capacity.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Reinertsen, D. (2009). "Principles of Product Development Flow." — Depth without decomposition into arrival and service components is under-determined; the right lever depends on which is moving.
    2. Goldratt, E. (1984). "The Goal" (Theory of Constraints). — Acting on a queue requires identifying the constraint; raw depth does not identify it.
    3. Anderson, D. (2010). "Kanban." — WIP/arrival-side controls, not raw depth, drive the "generate more?" decision; depth alone over- or under-throttles.
    4. Hopp, W. & Spearman (2000). "Factory Physics." — Throughput, WIP, and cycle time are jointly determined; using one (depth) as a control proxy is a known error.

  Strength of challenge: Strong

  Summary: Strong challenge, identical in shape to PRESUMPTION-202: raw queue depth without decomposition into generation rate and throughput capacity is an under-determined control signal. Whether to generate more depends on the gap between arrival and service rates, not on depth alone; lean/TOC/factory-physics all converge here. Using raw depth as a generate-more proxy will systematically mis-throttle. Couples OPEN-055 and ASSUMPTION-186 (the depth was itself a measurement artifact).

  Specific risks: Over- or under-generation; oscillation; compounding with the dedup artifact (ASSUMPTION-186) so the proxy is both wrong-metric and wrong-value.

  Mitigations available: Decompose depth into generation-rate and throughput-rate per cycle; key the generate-more decision off the rate gap, not raw depth; report all three.

  Recommendation: CHALLENGED (REVISE)

  STEELMAN:
    Item: PRESUMPTION-210
    Strongest counterargument: Raw queue depth under-determines the generation decision: the same depth can mean 'generation too fast' or 'review too slow,' and the right action is opposite in each case. Every flow/TOC framework requires decomposing depth into arrival and service rates first.
    What would need to be true for C2A2 to be safe: Safe once the generate-more decision is keyed off the generation-vs-throughput rate gap, with raw depth used only as a trigger to decompose.
    How to test: Decompose a recent throttle decision into generation-rate and throughput-rate trends; check whether raw depth would have prescribed the same action as the decomposed signal.
