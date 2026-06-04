SEARCH-FOR-PRESUMPTION-270:
  Date searched: 2026-05-29
  Original item: PRESUMPTION-270
  Original statement: [inferred] The swarm-contract mirror pattern (root architecture/ + wiki/architecture/) is a stable ground-truth pattern; drift risk is not separately defended.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-270
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated stability claim about the mirror pattern.
      15a: Searched for supporting literature on mirrored-doc patterns with low-drift evidence.
    Current status: PARTIALLY-SUPPORTED (Weak)

  Supporting evidence found: Partial

  Sources:
    1. Nygard (2018) — Mirror conventions are documented as workable when paired with a consistency model and drift-detection tooling.
    2. Kleppmann (2017) — Replication literature supports mirror-as-stable IF drift detection runs; without detection, drift is documented as inevitable.
    3. Bass et al. (2021) — Canonical-doc conventions include single-source-of-truth (SSOT) as preferred over mirror; mirror is the second-best when SSOT is operationally infeasible.
    4. Conway (1968) "How Do Committees Invent?" — Documentation conventions tend to drift in directions of organizational structure; same-team mirror is more stable than cross-team mirror.
    5. C2A2-internal: prior mirror conventions (decisions.md cross-references) have not been formally drift-audited.

  Strength of support: Weak

  Summary: Mirror patterns are documented as workable but always paired in the literature with explicit drift-detection. The presumption that the swarm-contract mirror is stable WITHOUT separate drift defense is precisely the gap the literature warns about. The FOR support is limited to "mirror patterns can be stable" — not to "this mirror pattern will be stable without defense."

  Caveats: (a) "Drift risk not separately defended" is exactly the literature's named precondition for failure; (b) the root → wiki/architecture mirror is same-actor (the agent system), reducing some drift drivers; (c) static-text mirror (no logic) drift is bounded by file-write discipline.

  Recommendation: PARTIALLY-SUPPORTED (Weak)
