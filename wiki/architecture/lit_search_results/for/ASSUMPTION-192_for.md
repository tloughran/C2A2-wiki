SEARCH-FOR-ASSUMPTION-192:
  Date searched: 2026-05-20
  Original item: ASSUMPTION-192
  Original statement: "CLAUDE.md viz stats stale — actual ~1,533 nodes / 36,608 edges / ~15.4 MB."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-192
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session: CLAUDE.md viz statistics found stale vs the actual generated artifact (~1,533 nodes / 36,608 edges / ~15.4 MB).
      15a: Searched for supporting literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Parnas, D. (1994). "Software Aging" (ICSE). — Documentation drifts out of sync with the system it describes unless actively maintained; stale embedded stats are a canonical instance.
    2. Lehman, M. (1980). "Programs, Life Cycles, and Laws of Software Evolution." — Continuing change guarantees documentation divergence absent a reconciliation process.
    3. Docs-as-code / single-source-of-truth practice (Write the Docs; "Docs Like Code," Gentle 2017). — Generated metrics should be derived from the artifact, not hand-copied into prose.

  Strength of support: Strong

  Summary: That hand-maintained statistics in CLAUDE.md drift from the live artifact is strongly supported — software-aging and evolution literature treat exactly this kind of embedded-fact staleness as inevitable without an auto-derivation step. The corrected figures (~1,533 / 36,608 / ~15.4 MB) are an internal measurement, but the staleness pattern and its remedy (derive, don't copy) are well established.

  Caveats: Literature supports the staleness pattern and the auto-derive remedy; it cannot confirm the exact corrected numbers, which are self-measured from the current artifact.

  Recommendation: SUPPORTED (staleness pattern + remedy); numbers self-verified
