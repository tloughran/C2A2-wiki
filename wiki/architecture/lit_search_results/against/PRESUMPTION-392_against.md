SEARCH-AGAINST-PRESUMPTION-392:
  Date searched: 2026-06-25
  Original item: PRESUMPTION-392
  Original statement: "That a degree-preserving rewire is the right null (node degree the only confound; topic/time/author adjacency ignored)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-392
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: the configuration-model null is adopted without considering topic/time/author confounds
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Temporal-network null models (Holme & Saramaki 2012). - In time-stamped networks, static degree-preserving nulls ignore temporal ordering and over-detect structure.
    2. Topic/attribute-aware nulls (Fosdick et al. 2018, 'Configuring Random Graph Models with Fixed Degree Sequences', SIAM Review). - Degree-only nulls leave attribute (topic/author) clustering uncontrolled, inflating apparent significance.
    3. Co-citation confounds: shared topicality and temporal co-occurrence create connectivity that a degree-only null attributes to 'signal'.

  Strength of challenge: Moderate

  Summary: Partially challenged: the degree-preserving rewire is a legitimate FIRST null but not a sufficient one for a knowledge network with strong topic, time, and author structure. The null-model literature shows that controlling degree alone leaves topical/temporal/author clustering uncontrolled, so a 'beyond degree-matched random' effect can be a topical or temporal artifact rather than evidence of the coil mechanism. The presumption treats degree as the only confound, which the literature contradicts.

  Specific risks: A degree-only null could yield false-positive support for H1 (ASSUMPTION-356), because topical/temporal co-clustering is misread as coil-driven flow.

  Mitigations available: Add topic-, time-, and author-matched nulls as robustness checks; report H1 only if it survives the stricter nulls, not just the degree null.

  STEELMAN:
    Item: PRESUMPTION-392
    Strongest counterargument: Degree is one confound among several in a knowledge network; topic, time, and author adjacency independently generate connectivity, so a degree-only null over-rejects and can manufacture significance the coil mechanism does not warrant.
    What would need to be true for C2A2 to be safe: H1 survives topic-, time-, and author-matched nulls, not merely the degree-preserving null.
    How to test: Re-run H1 under stratified/attribute-matched nulls; compare effect sizes to the degree-only null.

  Search scope: Temporal/attribute-aware null models. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED
