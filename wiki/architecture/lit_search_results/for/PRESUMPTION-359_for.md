SEARCH-FOR-PRESUMPTION-359:
  Date searched: 2026-06-17
  Original item: PRESUMPTION-359
  Original statement: "[inferred] Git history is a complete census of PRS-triplet production ('264 produced', not '264 git can see')."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-359
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated census claim — git record = the full population
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Single-authoritative-store practice — when an artifact type is, by workflow, created only inside one tracked store (traditions/*/prs_triplets.md under git), the git record approximates a census of that store with high coverage. Conditional support for near-completeness.
    2. Repository-as-system-of-record — for born-in-repo artifacts with no out-of-band creation path, the VCS log is a complete enumeration of the tracked population by construction.

  Strength of support: Weak (conditional)

  Summary: There is conditional support: if PRS triplets are born-in-repo with no creation path outside the tracked store, git is by construction a complete enumeration of that store, so "264 produced" ≈ "264 in the system of record." For artifacts that exist only because they were committed, the log IS the census. Support is strictly conditional on the no-out-of-band-creation premise holding.

  Caveats: This is exactly the premise MSR warns against (see 15b; Kalliamvakou et al. 2014): git captures what was committed, not what was produced — pre-VCS drafts, squashed/rebased history, uncommitted or externally-authored triplets, and rewritten history all break the census reading. Support is for "complete census of the TRACKED store," never for "complete census of production." The safe phrasing is "264 git can see." Couples ASSUMPTION-322, PRESUMPTION-355.

  Search scope: repository-mining coverage/completeness; system-of-record enumeration; born-in-repo artifacts. Comprehensive.

  Recommendation: PARTIALLY-SUPPORTED
