SEARCH-AGAINST-PRESUMPTION-280:
  Date searched: 2026-05-30
  Original item: PRESUMPTION-280
  Original statement: [inferred] Pathway 28's 'cannot drift' presumes COLORS is the only coupling surface; dir name + frontmatter are also surfaces, and the get_group -> 'root' silent fallback is an existing leak.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-280
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched multi-surface coupling defeating single-source claims and silent-default failure modes.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. SSOT-pitfalls literature (LinkedIn/Hidef) — when multiple surfaces encode the same fact, the single-source guarantee evaporates; coupling leaks through every non-derived surface.
    2. C2A2-internal — dir name and frontmatter independently encode tradition/structure vocabulary; both are coupling surfaces beyond COLORS.
    3. Fail-loud literature (Nygard) — get_group -> 'root' silently absorbs unmatched groups, an existing leak that hides drift rather than preventing it.

  Strength of challenge: Strong

  Summary: The 'cannot drift' guarantee fails because COLORS is not the only surface: dir name and frontmatter also encode the vocabulary, and the get_group -> 'root' silent fallback is a concrete existing leak that masks mismatches. This is not a hypothetical gap; the leak is present in the code.

  Specific risks: Silent mis-grouping of nodes to 'root'; undetected vocabulary divergence; false confidence in a drift guarantee that does not hold.

  Mitigations available: Make COLORS the sole surface (derive dir/frontmatter from it) and replace the 'root' fallback with a loud error.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-280
    Strongest counterargument: A drift guarantee is only as strong as the surface enumeration; with three surfaces and a silent default, 'cannot drift' is already false, demonstrably.
    What would need to be true for C2A2 to be safe: All vocabulary surfaces derive from COLORS and the 'root' fallback errors loudly.
    How to test: Inject a dir/COLORS mismatch and confirm a loud failure rather than silent 'root' grouping.
