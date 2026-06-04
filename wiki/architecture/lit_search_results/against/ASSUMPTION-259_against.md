SEARCH-AGAINST-ASSUMPTION-259:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-259
  Original statement: (Pathway 28) The tradition/structure vocabulary fans out from one COLORS dict; filter checkboxes and focus typeahead are siblings of that source and cannot drift.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-259
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched multi-surface coupling and silent-default failure modes that defeat SSOT.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. LinkedIn/Hidef SSOT-pitfalls articles — SSOT guarantees fail when more than one surface encodes the same fact; coupling leaks through any non-derived surface.
    2. C2A2-internal (couples PRESUMPTION-280) — directory name and frontmatter are additional vocabulary surfaces; the get_group -> 'root' silent fallback is an existing leak that derives nothing from COLORS.
    3. Fail-loud literature (Nygard 'Release It!') — a silent default ('root') hides drift instead of surfacing it, the opposite of a drift guarantee.

  Strength of challenge: Strong

  Summary: The 'cannot drift' claim presumes COLORS is the only coupling surface, but dir name and frontmatter also encode the vocabulary, and get_group's silent 'root' fallback already leaks. SSOT only prevents drift for the state it actually masters; the claim over-extends the guarantee and a concrete silent-default leak already violates it.

  Specific risks: Vocabulary divergence via dir/frontmatter goes undetected; the 'root' fallback silently mis-groups nodes (a fail-loud violation).

  Mitigations available: Make COLORS the sole surface or derive dir/frontmatter from it; replace the 'root' silent fallback with a loud error.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-259
    Strongest counterargument: A single-source *claim* is only as strong as the enumeration of surfaces; with dir name + frontmatter + a silent 'root' default unaccounted for, 'cannot drift' is false as stated.
    What would need to be true for C2A2 to be safe: All vocabulary surfaces provably derive from COLORS and the 'root' fallback is replaced by a hard error.
    How to test: Introduce a deliberate dir/COLORS mismatch and confirm it fails loudly rather than silently defaulting.
