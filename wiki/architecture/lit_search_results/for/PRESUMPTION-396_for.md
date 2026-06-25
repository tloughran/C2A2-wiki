SEARCH-FOR-PRESUMPTION-396:
  Date searched: 2026-06-25
  Original item: PRESUMPTION-396
  Original statement: "That a single ~40MB inline-script no-build HTML file stays maintainable/verifiable as features accumulate"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-396
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: monolithic single-file delivery is assumed to scale in maintainability; ties to payload-diet pin
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: Partial

  Sources:
    1. (Partial) No-build single-file delivery has real deployment/portability virtues (zero toolchain, trivial hosting) - supports the CONVENIENCE, not maintainability.
    2. (Adjacent) Small self-contained artifacts can be easier to reason about - but this support evaporates at ~40MB scale.

  Strength of support: Weak

  Summary: Supportive evidence covers only the deployment convenience of single-file artifacts (no build step, easy to host/share), not the maintainability-at-scale claim. There is no literature supporting that a ~40MB monolithic inline-script file remains maintainable/verifiable as features accumulate; the relevant software-engineering literature (modularity/information-hiding) points the other way (15b).

  Caveats: Convenience != maintainability. The claim fails precisely where it matters (growth in features/size), and is already hedged by C2A2's own 'payload-diet bright pin'.

  Search scope: No-build single-file tradeoffs; modularity. Adequate.

  Recommendation: NO-SUPPORT-FOUND
