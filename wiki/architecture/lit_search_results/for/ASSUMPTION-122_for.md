SEARCH-FOR-ASSUMPTION-122:
  Date searched: 2026-05-14
  Original item: ASSUMPTION-122
  Original statement: "Eager-tier perspective-lattice content lives in vault at `wiki/Perspectives/` with structure-group tag (first-class wiki citizen)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-122
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from perspective-lattice architecture pass
      15a: Searched for eager-vs-lazy content tiering and structure-group-tag schema design
    Current status: PARTIALLY-SUPPORTED

  Sources:
    1. Obsidian / Logseq / Tana community patterns (2022-2025) — tag-based first-class typing is the dominant pattern for cross-referencing heterogeneous content in vault-style knowledge bases.
    2. Fowler (2003) "Patterns of Enterprise Application Architecture" — eager-loading patterns are appropriate when content is on the critical path; lazy-loading when content is large and conditional.
    3. C2A2-internal Sociogram / structure-group precedent — existing structure-group tags work for thinkers and PRS triplets; extending the same pattern to perspectives is consistent.
    4. Norman (2013) "The Design of Everyday Things" — first-class affordances (the same interactions available across content types) reduce cognitive load.

  Strength of support: Moderate

  Summary: First-class tagged content in a vault is a well-established pattern. Eager loading is appropriate when perspectives are on the critical reading path. The C2A2-internal precedent (thinker / PRS / structure-group code paths) means the extension is consistent with existing machinery. Support is moderate-strong on the storage pattern; PRESUMPTION-155 (paired) raises the genuine concern that the existing code paths may have implicit schema assumptions that perspectives violate.

  Caveats: (a) PRESUMPTION-155 — machinery-transfer audit not performed; existing structure-group / Sociogram code may assume thinker or PRS schema; (b) Eager tier may not be the right tier for all perspective content — graduated tiering may be needed; (c) Tag-collision risk if structure-group tag namespace is not extended.

  Recommendation: PARTIALLY-SUPPORTED — storage pattern is well-supported; machinery-transfer audit (PRESUMPTION-155) is the load-bearing gap
