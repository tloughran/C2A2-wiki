SEARCH-AGAINST-ASSUMPTION-341:
  Date searched: 2026-06-24
  Original item: ASSUMPTION-341
  Original statement: "Wikilink resolution must be path-aware (not basename-only); the production resolver may be basename-only, skewing every weekly connectivity figure"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-341
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 06-23 audit as a measurement-correctness claim gating the connectivity series
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Boundary condition. - If the vault has no basename collisions, basename-only resolution yields the SAME counts as path-aware, so the 'skews every figure' claim could be empirically near-null.
    2. Over-correction risk. - A path-aware resolver can itself be wrong (case sensitivity, alias/redirect handling), so 'path-aware = correct' is not guaranteed (this couples to PRESUMPTION-379).

  Strength of challenge: Weak

  Summary: There is little literature CONTRADICTING the principle that path-aware resolution is correct - basename-only is genuinely a weaker rule. The honest challenge is to the MAGNITUDE and the framing: 'must' and 'skews every weekly figure' are strong, but the actual skew is unknown and could be negligible if collisions are rare. There is also a reflexive risk: replacing one resolver with another the audit wrote does not guarantee correctness (handed to PRESUMPTION-379). So the claim is methodologically right but its quantitative form is unverified.

  Specific risks: Over-stating the skew could trigger a costly re-architecture of the connectivity pipeline for an error that may be small; under-checking the replacement could swap one silent miscount for another.

  Mitigations available: Recompute connectivity both ways (basename vs path-aware) and report the delta before declaring the series skewed; unit-test the new resolver against labelled link forms.

  Search scope: basename collisions; resolver correctness magnitude. Adequate.

  Recommendation: PARTIALLY-CHALLENGED
