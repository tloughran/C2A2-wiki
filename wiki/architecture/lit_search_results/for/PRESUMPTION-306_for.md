SEARCH-FOR-PRESUMPTION-306:
  Date searched: 2026-06-06
  Original item: PRESUMPTION-306
  Original statement: [inferred] "Two verbs over one dataset" presumes the curated graph (156, CC-001...) and the cards directory (855, C0001...) are unifiable, despite measured near-total disjointness (0 id / 3 name / 5 host matches). P3 rests on a join that may be very sparse.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-306
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated presumption that two near-disjoint record sets are unifiable into one dataset.
      15a: Searched record-linkage / entity-resolution methods that recover joins from disjoint keys (name, host, fuzzy match).
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. "Record linkage" (Wikipedia survey) / Christen, entity-resolution literature. — Record linkage exists precisely to join records that share NO unique identifier, using probabilistic matching over name/address/other fields plus blocking; establishes that absence of a shared id key does not by itself mean the sets cannot be joined.
    2. Splink (MoJ Analytical Services) and Data Ladder, "Record Linkage for Incomplete Data." — Production-grade fuzzy/probabilistic linkage routinely recovers joins from noisy, partially-overlapping name/host fields; supports the feasibility of recovering CC<->C0001 correspondences beyond exact-id matching.
    3. Towards Data Science, "Entity Resolution: Identifying Real-World Entities in Noisy Data." — Blocking + similarity scoring can surface true matches hidden by formatting differences; supports that the measured 3 name / 5 host exact matches may understate true correspondence recoverable by fuzzy methods.

  Strength of support: Weak-Moderate

  Summary: Entity-resolution theory genuinely supports the bare possibility that the two sets are unifiable without a shared id: probabilistic linkage over name/host with blocking can recover correspondences that exact-key matching misses, so the measured 0 id / 3 name / 5 host is a floor, not a ceiling. This is real but thin support — it establishes that a join COULD be recovered, not that a meaningful one exists. The decisive condition the same literature attaches (discriminative overlapping attributes must actually be present, and aggressive thresholds inflate false matches) is exactly where the near-zero base overlap makes the FOR case fragile.

  Caveats: ER's power is conditional on there being a recoverable signal. At 0/3/5 matches across 156x855, fuzzy linkage may manufacture false positives rather than recover true links, and the literature explicitly warns that low-overlap forcing increases false-match rates. So support is for "a join is not impossible," not for "the join is dense enough to carry P3." The construct question — whether the two sets even describe the same population — is outside what ER can answer (see PRESUMPTION-311).

  Recommendation: PARTIALLY-SUPPORTED
