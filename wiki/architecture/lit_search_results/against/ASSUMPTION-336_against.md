SEARCH-AGAINST-ASSUMPTION-336:
  Date searched: 2026-06-23
  Original item: ASSUMPTION-336
  Original statement: "Correcting the token-read artifact licenses trust in all downstream yield comparisons ("do not inherit a masked drop")"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-336
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 06-22 session as a generalization from one corrected read path to whole-pipeline trust
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Functionize / migration-testing literature on independent failure modes. — Fixing one read path says nothing about other fields, joins, or aggregations; silent corruption can be localized, so one repair does not certify the pipeline.
    2. C2A2-internal family: PREMISE-049 (verify-before-trust), REVISE-129 (no liveness check), MONITOR-296 (silent degradation). — The system has already dispositioned the over-trust / not-fail-loud pattern; "one fix licenses global trust" is the same anti-pattern.
    3. Gentner-style overgeneralization caution. — Generalizing from a single corrected instance to "all" is an inductive leap the evidence does not license.

  Strength of challenge: Moderate-Strong

  Summary: The challenge targets the quantifier "all": correcting one read path is local evidence and does not transfer to every downstream yield comparison. This is a textbook over-trust / fail-loud failure mode the system has already flagged (PREMISE-049, REVISE-129, MONITOR-296). Independent failure modes (other fields, joins, aggregations) remain untested after a single-path fix, so blanket trust is unwarranted.

  Specific risks: Inheriting unverified trust across the whole yield pipeline could let a different masked artifact ride along undetected — precisely the "masked drop" the assumption claims to have eliminated, relocated to another path.

  Mitigations available: Scope trust to reconciled paths; add canary assertions / both-paths reconciliation per derived metric; treat "do not inherit a masked drop" as a per-path verification rule, not a global license.

  STEELMAN:
    Strongest counterargument: If the migration touched exactly one field (token_usage) and that field is now read both-ways, then for the token-yield comparisons specifically there is no remaining masked drop, so trust in THOSE comparisons is in fact licensed.
    What would need to be true for C2A2 to be safe: The premise must be restated with scope: trust extends only to comparisons whose read paths were reconciled, and only if the migration provably touched no other yield-relevant field.
    How to test: Enumerate yield-relevant fields crossing the migration; reconcile each both-ways; trust is licensed exactly for those that pass.

  Search scope: independent failure modes; over-trust family; overgeneralization. Comprehensive.

  Recommendation: CHALLENGED
