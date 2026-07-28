SEARCH-AGAINST-ASSUMPTION-496:
  Date searched: 2026-07-22
  Original item: ASSUMPTION-496
  Original statement: FLAG-017 — Levin's "virtual governor" may be Friston's group-level Markov blanket approached from the other side; the equivalence test is stated and tractable.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-496
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-21 daily run FLAG-017
      15b: Searched for scope limits and commensurability objections to FEP/Markov-blanket identifications
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "The Markov Blanket Trick: On the Scope of the Free Energy Principle," philsci-archive 18843. — The blanket construction is routinely applied beyond its licensed scope; a shared formal vocabulary does not license a specific physical/biological identification.
    2. "How particular is the physics of the free energy principle?," arXiv:2105.11203. — The FEP applies only to systems meeting specific conditions (existence of a stationary density, non-degenerate blanket partition); level-of-description and boundary choices are decisive.
    3. "Markov Blanket Density and Free Energy Minimization," arXiv:2506.05794. — Sharpens the objection that a Markov blanket is a statistical partition, not automatically a control structure; the gap between a statistical boundary and a governor with a set-point is exactly what must be bridged.

  Strength of challenge: Moderate-Strong

  Summary: The literature challenges the "tractable" clause specifically. Levin's virtual governor is a control-theoretic object (set-point, error signal, actuation); Friston's group Markov blanket is, at base, a statistical conditional-independence partition. Identifying them requires establishing a shared level of description, a common boundary definition, and a matching notion of "control" — none of which the FLAG-017 statement supplies. The scope critiques of the FEP show these are not formalities: they are where such identifications usually fail. The equivalence may be *statable* but is not shown to be *tractable* in the sense of yielding a legitimate comparison.

  Specific risks: Running the equivalence test without the commensurability check risks a category error — declaring two constructs "equivalent" because they share a diagram, when they are defined at different levels and mean different things by "boundary" and "control."

  Mitigations available: Perform the PRESUMPTION-523 commensurability check first (fix level of description, boundary definition, notion of control); only then run the equivalence test.

  STEELMAN:
    Item: ASSUMPTION-496
    Strongest counterargument: A Markov blanket is a statistical partition and a Watt governor is a mechanism with a set-point; the FEP's own governor analogy is heuristic, not a derivation. To call the equivalence "tractable" is to presume the hard part (commensurability) is already done. Absent a shared formalism for "control," the test either trivially succeeds (both can be drawn as feedback loops) or is undecidable — neither is informative.
    What would need to be true for C2A2 to be safe: A single formal frame in which both a set-point-tracking governor and a group Markov blanket are expressible, with an explicit map between "boundary" in each.
    How to test: Before the equivalence test, write both constructs in one formalism (e.g., a stochastic control model with an explicit blanket partition) and check that "control" refers to the same object in each.

  Recommendation: CHALLENGED
