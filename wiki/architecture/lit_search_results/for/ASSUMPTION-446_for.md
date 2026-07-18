SEARCH-FOR-ASSUMPTION-446:
  Date searched: 2026-07-13
  Original item: ASSUMPTION-446
  Original statement: "Census trend continuity (2483 -> 2567 orphans, no jump) suffices to establish that the basename-only resolver defect was introduced and caught within the 2026-07-12 run, and that no back-correction of earlier CSV rows is warranted."

  PROVENANCE:
    Origin: 14a
    Chain: 14a -> 15a
    Original item: ASSUMPTION-446
    Item type: ASSUMPTION (stated; QUEUED-EMPIRICAL)
    Transform at each step:
      14a: Extracted from the 2026-07-12 EOD run (resolver defect self-caught in-run)
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. [Statistical Process Control / Shewhart chart doctrine (standard SPC texts; control-chart special-cause rules). — A process showing no special-cause signal (no step, no run, no trend violation) is conventionally treated as "in control," so absence of a jump IS a recognised, legitimate first-line evidence form for "no regime change occurred before this point."]
    2. [Bland, J.M. & Altman, D.G., limits-of-agreement lineage; and the repeated-measures extension (Br J Anaesth, S0007-0912(17)34715-3). — Establishes that two measurement procedures can differ by a bounded, characterised amount without either being invalid; supports the weaker reading that a small proportional shift need not indicate corruption of the earlier series.]
    3. [Kudrjavets, G., Nagappan, N. & Ball, T. (2006). "Assessing the Relationship Between Software Assertions and Faults." ISSRE / MSR-TR-2006-54. — In-run self-checks empirically catch real defects cheaply and early; higher assertion density correlates with lower fault density. Supports the "caught within the run" half of the claim as a plausible detection story.]
  Strength of support: Weak
  Summary: The literature gives the claim a real but thin foundation. SPC legitimises "no special-cause signal" as first-line evidence of process stability, and the assertion/self-check literature makes "introduced and caught within one run" a credible detection narrative. But no source supports the inferential leap from "the aggregate series shows no discontinuity" to "the defect did not affect earlier rows." SPC's own doctrine is that Shewhart charts are insensitive to small sustained shifts (which is precisely why CUSUM and EWMA exist), and a resolver defect that mis-attributes a roughly constant PROPORTION of links produces exactly a smooth, jump-free series. The support is therefore for the weakest reading only, and it is conditional on the defect being step-shaped rather than proportional.
  Caveats: Support evaporates entirely for proportional/multiplicative defects. No source addresses retroactive exoneration of prior output from a trend statistic. The decisive evidence is in-house, not in the literature: the queued dual-mode re-run of the prior resolver against the 2026-07-05 snapshot.
  Recommendation: PARTIALLY-SUPPORTED
