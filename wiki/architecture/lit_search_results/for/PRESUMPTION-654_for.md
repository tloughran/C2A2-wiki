SEARCH-FOR-PRESUMPTION-654:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-654
  Original statement: That a trap's catches occur upstream of consequence —
    where in fact the seventh instance was caught only after the false
    conclusion had already entered a persistent memory and a pending batch.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-654
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 observation that the seventh trap
        catch occurred after the false conclusion had reached persistent
        memory and a pending batch
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. AHRQ, "Near-Miss Analysis," in Patient Safety and Quality (NCBI
       Bookshelf, NBK216107). — Supplies the definitional support: a near miss
       is a state of temporarily increased risk arising from an initial
       failure but still without actual consequences. For events correctly
       classified as near misses, upstream catching is true by construction.
    2. "Near-miss management systems: A methodological comparison," Journal of
       Loss Prevention in the Process Industries, 2012. — Distinguishes formal
       barriers from recovery, the informal and largely human-mediated second
       set by which a developing situation is detected and corrected in time,
       thereby limiting the sequence to a near-miss outcome rather than
       letting it develop into an adverse event. The taxonomy is explicitly
       about which side of consequence the catch falls on.
    3. "Observability-in-depth: an essential complement to the defense-in-
       depth safety strategy in the nuclear industry," Nuclear Engineering and
       Technology, 2015/16. — Integrates near-miss management with defence-in-
       depth and treats the position of detection relative to barrier failure
       as the object of design, not an incidental property.
    4. Data-pipeline error-propagation literature (Ataccama shift-left data
       quality; Conduktor data-quality incident guidance, 2025-2026). — The
       counterweight: once an error passes transformation and consumption, the
       blast radius expands and remediation cost multiplies; downstream checks
       are explicitly characterised as too late for data products.
    5. QFix (arXiv:1601.07539), on diagnosing errors through query histories. —
       Documents the specific difficulty at issue: once an erroneous value has
       propagated through subsequent updates, its origin is obscured and the
       offending operation is hard to identify.

  Strength of support: Weak

  Summary: The near-miss literature supports the presumption only for events
    that qualify as near misses, and it is precise about what qualifies:
    detection must precede consequence. That makes the framework supportive in
    form but not in application to the case at hand — an instance caught after
    entry into persistent memory and a pending batch has, by the same
    taxonomy, crossed into adverse-event territory and been recovered, not
    trapped. The safety sources are also clear that recovery of this kind is a
    last-line-of-defence event whose occurrence signals that the designed
    barriers were relied upon and did not hold. The data-propagation
    literature adds the cost asymmetry: post-consumption catches are the
    expensive ones precisely because provenance is obscured and downstream
    consumers have already acted. A trap that catches sometimes upstream and
    sometimes downstream is, on this evidence, two different controls with two
    different risk profiles being counted as one.

  Caveats: Support depends entirely on classification, and the located sources
    do not settle whether entry into a persistent memory plus a pending batch
    constitutes "consequence" in C2A2's terms — that is a scoping decision
    C2A2 must make explicitly. Process-safety taxonomies assume physical
    irreversibility, which may be a stronger condition than applies to a
    revocable memory write. Where the downstream state is genuinely
    reversible, the near-miss reading survives; where a pending batch has been
    consumed, it does not.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Adequate. Concepts searched: near-miss taxonomies and
    classification; recovery barriers vs designed barriers; pre-consequence
    detection vs post-consumption recovery; defence-in-depth and observability-
    in-depth; error propagation to downstream consumers; recoverability and
    cost of late detection.
