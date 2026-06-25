SEARCH-AGAINST-PRESUMPTION-396:
  Date searched: 2026-06-25
  Original item: PRESUMPTION-396
  Original statement: "That a single ~40MB inline-script no-build HTML file stays maintainable/verifiable as features accumulate"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-396
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: monolithic single-file delivery assumed to scale in maintainability; ties to payload-diet pin
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Parnas 1972. 'On the Criteria To Be Used in Decomposing Systems into Modules.' CACM. - Modularity/information-hiding is the established basis of maintainability; a monolith forgoes the decomposition that makes change safe.
    2. Software-complexity literature (McCabe; Lehman's laws of software evolution). - Complexity grows as systems evolve; without modular structure, change cost and defect risk rise super-linearly.
    3. Tooling limits: diff/review/static-analysis tools degrade or fail on very large single files, undermining verifiability (relevant to the project's own 'node --check' verification step).

  Strength of challenge: Strong

  Summary: Strongly challenged by core software-engineering principles: maintainability and verifiability come from modular decomposition and information hiding, which a single ~40MB inline-script file forgoes by construction. As features accumulate, Lehman's laws predict rising complexity, and a monolith concentrates that complexity with no module boundaries to contain change impact. Practically, large single files strain diff/review/static-analysis tooling - directly threatening the project's own validation workflow. The presumption runs against decades of modularity evidence, and C2A2's own 'payload-diet bright pin' already registers the concern.

  Specific risks: Rising change-cost and defect risk; verification tooling (including the project's node --check / validation step) failing or becoming unreliable at scale; onboarding/review friction.

  Mitigations available: Introduce a build step / module bundling as features grow; split logic into testable modules; keep the single-file artifact as a BUILD OUTPUT, not the source of truth.

  STEELMAN:
    Item: PRESUMPTION-396
    Strongest counterargument: Maintainability is a function of modular structure; a growing 40MB monolith has none, so change-impact is unbounded and verification tooling degrades - the convenience of no-build is paid back as compounding maintenance and verification risk.
    What would need to be true for C2A2 to be safe: Feature growth is bounded, OR the file is generated from modular sources with its own tests (single file is output, not source).
    How to test: Track change-cost/defect metrics and tooling performance as the file grows; if verification time or diff reliability degrades, the presumption fails.

  Search scope: Modularity/information-hiding; software evolution; tooling limits. Comprehensive.

  Recommendation: CHALLENGED
