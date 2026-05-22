SEARCH-AGAINST-PRESUMPTION-168:
  Date searched: 2026-05-15
  Original item: PRESUMPTION-168
  Original statement: "25-pathway extended inventory presents 3 structure groups (Portability/Learning-governance/System-self-reference) as conceptual; cuts may reflect walk-pacing rather than underlying structure"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-168
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption
      15b: Searched for counter-evidence on walk-emergent vs designed structure groups
    Current status: NO-CHALLENGE-FOUND (Weak)

  Sources:
    1. The presumption is an inference about a documented risk pattern (walk-pacing artifact); there isn't substantial literature refuting the inference itself.
    2. Counter-pattern: some structure-group taxonomies generated in single sessions do prove stable (e.g., Kruchten 4+1 views were proposed in one paper and have survived 30 years); the presumption-as-inference is correct in general but not deterministic.
    3. Bryar-Carr (Working Backwards) — Amazon's PR/FAQ structure was generated in a single session and has been stable; counter-example to the "walk-pacing artifact" generalization.

  Strength of challenge: Weak

  Summary: The presumption is a probabilistic inference about a documented risk pattern. Counter-examples exist (Kruchten 4+1, Amazon PR/FAQ) where single-session taxonomies have been stable over time, but these are exceptions. The literature supports the inference more than it refutes it. Weak challenge: the inference may not deterministically apply to every single-session taxonomy.

  Specific risks: (a) Treating the inference as deterministic produces false alarm (some single-session taxonomies are stable); (b) Over-auditing structure-groups before they have been used.

  Mitigations available: (a) Schedule second-pass audit but don't presume failure; (b) Track which structure-groups prove stable vs. need re-cutting; (c) Don't escalate to disposition-change until second-pass evidence.

  Recommendation: NO-CHALLENGE-FOUND (Weak) — inference is well-grounded; second-pass audit will resolve

  STEELMAN:
    Item: PRESUMPTION-168
    Strongest counterargument: The inference is correct in direction but probabilistic. Not every single-session taxonomy is walk-pacing artifact — some are durable. The presumption is right to flag the risk; it would be wrong to treat the risk as certainty.
    What would need to be true for C2A2 to be safe: (a) Second-pass audit scheduled; (b) Stability tracking by structure-group.
    How to test: Re-derive structure-groups from pathway docs at +2 weeks; check whether the same cuts emerge.
