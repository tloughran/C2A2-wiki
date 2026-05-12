SEARCH-FOR-PRESUMPTION-086:
  Date searched: 2026-04-28
  Original item: PRESUMPTION-086
  Original statement: "PREMISE-013 N-collisions threshold not examined; flag-and-roll-forward scales without breakdown"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-086
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced — PREMISE-013 was ratified at N=2 collisions/day with no upper bound on cumulative unresolved
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED (Weak-Moderate)

  Sources:
    1. Shapiro et al. (2011) on CRDTs — collision-merge handling scales gracefully *up to* a system-specific saturation; the literature explicitly identifies a saturation point.
    2. Kleppmann (2017) "Designing Data-Intensive Applications" — eventual-consistency tradeoffs are well documented; "scales without breakdown" overshoots literature.
    3. Birthday-paradox-style scaling analysis (Stinson 2005 "Cryptography Theory and Practice") — collision rate grows with √N for random IDs; non-trivial at moderate N.
    4. C2A2-internal: PREMISE-013 acknowledged conditions (a) collision rate stays low, (b) durable mapping, (c) follow-renames; the presumption attempts to extend beyond these conditions.

  Strength of support: Weak-Moderate

  Summary: Literature endorses flag-and-roll-forward up to a saturation point — not without one. The presumption that the pattern scales "without breakdown" is therefore weakly supported. PREMISE-013's explicit conditions are the load-bearing safeguards; the presumption attempts to elide them.

  Caveats: (a) "Without breakdown" is a strong reading; the weaker reading is "scales as well as the conditions hold," which is what PREMISE-013 actually says.

  Recommendation: PARTIALLY-SUPPORTED (Weak-Moderate — the conditional version supported via PREMISE-013; the unconditional version surfaced as PRESUMPTION-086 is not)
