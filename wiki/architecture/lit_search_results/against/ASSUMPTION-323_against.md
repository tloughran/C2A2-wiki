SEARCH-AGAINST-ASSUMPTION-323:
  Date searched: 2026-06-17
  Original item: ASSUMPTION-323
  Original statement: "A commit-message self-report ('+38 PRS triplets') is an adequate cross-check that verifies the derived yield series."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-323
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the verification step grounding confidence in the yield series
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Commit-message reliability (MSR; "Quick remedy commits..."; Bird et al. on bias) — commit messages are unreliable ground truth: they are aspirational, rounded, batched, sometimes describe prior/next commits, and frequently disagree with the actual diff. A self-reported "+38" is not an independent gold standard.
    2. Non-independence of witnesses — if the commit author and the pipeline both read the same working tree, the "cross-check" is not independent; agreement can reflect shared method, not corroboration (circularity).
    3. Single-point verification critique (sampling/coverage) — one matching figure verifies one window, not a series; "adequate cross-check" overstates the evidential reach of a single self-report.

  Strength of challenge: Moderate-Strong

  Summary: The self-report cross-check is materially challenged: commit messages are documented as unreliable narrators (rounded, aspirational, batched, often inconsistent with the diff), so a "+38" is not a gold standard; and if the author derived "+38" the same way the pipeline does, the agreement is circular rather than corroborating. Even granting an honest, independent count, it touches only one window and cannot "verify the series." "Adequate cross-check" overstates a weak, point-local, possibly non-independent signal.

  Specific risks: False confidence — a single matching self-report is taken as series validation, so systematic pipeline errors on uncorroborated days go undetected and propagate to the headline yield.

  Mitigations available: Verify against the actual diffs (count triplet ids added), not the prose; sample multiple windows; ensure the cross-check is independent of the pipeline's own derivation; report it as "one window corroborated," not "series verified."

  STEELMAN:
    Strongest counterargument: A contemporaneous, specific number written by the author at the time of the work is real independent evidence for that window, and a match is more reassuring than no check at all; demanding full-series verification before trusting anything is an unreasonably high bar for a lightweight sanity check.
    What would need to be true for C2A2 to be safe: The self-report is derived independently of the pipeline (e.g., the author counted by hand), it matches the diff not just the prose, and it is treated as point-local corroboration, not series verification.
    How to test: Recount triplet-id additions from diffs across several windows; compare to both the pipeline and the commit prose; check whether author and pipeline share a derivation.

  Search scope: commit-message reliability; witness independence/circularity; single-point vs systematic validation. Comprehensive.

  Recommendation: CHALLENGED
