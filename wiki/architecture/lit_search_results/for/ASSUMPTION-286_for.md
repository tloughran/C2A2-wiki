SEARCH-FOR-ASSUMPTION-286:
  Date searched: 2026-06-08
  Original item: ASSUMPTION-286
  Original statement: Policy-layer rules (the 12 CLAUDE.md rules) are waivable; capability/constitutional boundaries (sandbox credentials) are not; a policy rule may coincide with a hard capability wall.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-286
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the stated two-layer model of constraints (waivable policy vs non-bypassable capability), with a noted coincidence case.
      15a: Searched for support for a policy/mechanism (configurable-policy vs non-bypassable-capability) separation and for least-privilege/capability theory.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Saltzer & Schroeder 1975, "The Protection of Information in Computer Systems." — Foundational statement of least privilege, fail-safe defaults, and complete mediation; a capability/credential boundary that simply cannot be exceeded is the mechanism layer, distinct from discretionary policy.
    2. Policy/mechanism separation (Wulf et al., HYDRA; Lampson). — A classic, well-established design principle: the mechanism (what is enforceable/non-bypassable) is separated from the policy (what is configured and therefore changeable). This is exactly the two-layer model ASSUMPTION-286 states.
    3. Capability-based security (unforgeable tokens; "once baked, the rules in a capability cannot be changed without changing the key itself"). — Capabilities encode non-bypassable authority bounds: you cannot waive your way past an authority you were never granted, which grounds "sandbox credentials are not waivable."

  Strength of support: Strong

  Summary: The two-layer distinction is a direct restatement of one of the most established principles in computer security: configurable policy sits above a non-bypassable enforcement mechanism, and you cannot talk your way past a capability you do not hold. Least-privilege and capability theory give "credentials/sandbox boundaries are hard walls" strong grounding, and policy/mechanism separation gives "the 12 rules are waivable policy" equally strong grounding.

  Caveats: The literature also warns that the layers can be CONFUSED in practice — a constraint can look like waivable policy while actually being load-bearing safety (or vice versa). The "a policy rule may coincide with a hard capability wall" clause is the dangerous-but-real case the AGAINST search develops: when a policy rule happens to track a capability boundary, treating it as freely waivable invites probing a wall that will (correctly) refuse. Support is for the distinction; care is required at the coincidence.

  Recommendation: SUPPORTED
