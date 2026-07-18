SEARCH-FOR-ASSUMPTION-458:
  Date searched: 2026-07-16
  Original item: ASSUMPTION-458
  Original statement: 'The .md file is the primary deliverable - it persists even if browser delivery fails'; the fallback presumes the failure lands at the delivery step, but a crash before Step 2 writes no file at all.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-458
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted/inferred to intake queue (for_lit_search.md)
      15a: Searched for supporting literature; result PARTIALLY-SUPPORTED (strength Weak)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Write-ahead logging / checkpoint literature (Mohan et al. ARIES 1992; WAL surveys): durability guarantees require the durable write to precede the risky operation; 'persists even if X fails' holds only if the persist step has already executed.
    2. Crash-only software (Candea & Fox, HotOS 2003): critical state must be committed to non-volatile media before failure for the persistence guarantee to hold.

  Strength of support: Weak

  Summary: The literature supports the CONDITION under which the assumption is true (write-before-risk), which means it also exposes when the assumption is false. As stated - 'the .md persists even if delivery fails' - the claim is only conditionally supported: it holds iff the write precedes the failure point. So 15a finds weak support for a corrected version, not the stated version.

  Caveats: EMPIRICAL and effectively demonstrated false in-run on 07-14: a crash before Step 2 wrote no file.

  Recommendation: PARTIALLY-SUPPORTED
