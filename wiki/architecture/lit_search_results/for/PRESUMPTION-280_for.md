SEARCH-FOR-PRESUMPTION-280:
  Date searched: 2026-05-30
  Original item: PRESUMPTION-280
  Original statement: [inferred] Pathway 28's 'cannot drift' presumes COLORS is the only coupling surface; dir name + frontmatter are also surfaces, and the get_group -> 'root' silent fallback is an existing leak.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-280
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15a: Searched single-source-of-truth guarantees and their preconditions.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Pragmatic Programmer (DRY) / SSOT articles — a true single source does prevent drift for the state it masters; the guarantee is real *within its precondition*.
    2. Red Hat SSOT-in-architecture — normalization to one canonical element removes drift for derived views.
    3. Webel IT SSOT vs DRY — formalizes the precondition: exactly one authoritative surface.

  Strength of support: Weak

  Summary: SSOT genuinely prevents drift, but only under the precondition that there is exactly one authoritative surface. The support is weak here because the presumption's whole point is that the precondition is violated.

  Caveats: Support is conditional on single-surface, which is the contested fact.

  Recommendation: PARTIALLY-SUPPORTED
