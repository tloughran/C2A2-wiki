SEARCH-AGAINST-ASSUMPTION-441:
  Date searched: 2026-07-12
  Original item: ASSUMPTION-441
  Original statement: "The qc_sweep report's 0-needs-review is a reliable false negative (synthesis-only blindness); the full-vault transcript scan is the authoritative staleness measure."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-441
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from 2026-07-11 EOD daily run
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial
  Sources:
    1. [Wang, Z. et al., 2020. "Error rates of human reviewers during abstract screening in systematic reviews." PLOS One 15(1):e0227742. — The comprehensive review process routinely treated as the gold standard has a measured total error rate of 10.76% (95% CI 7.43–14.09%). Broad-coverage passes are not error-free; "authoritative" conflates broader scope with correctness.]
    2. [Umemneku Chikere, C. et al., 2021. "Comparative diagnostic accuracy studies with an imperfect reference standard — a comparison of correction methods." BMC Med Res Methodol 21:67. — When an imperfect reference is treated as truth, accuracy estimates of everything measured against it are biased in unknown directions. Crowning the full-vault scan "the authoritative staleness measure" imports exactly this imperfect-gold-standard error.]
    3. [AHRQ Methods Guide, "Options for Summarizing Medical Test Performance in the Absence of a Gold Standard" (NCBI NBK98232). — Standard methodology when two imperfect measures disagree: model both as imperfect and use agreement analysis, rather than designating one authoritative by fiat.]
  Strength of challenge: Moderate
  Summary: The challenge does not rescue qc_sweep — scope blindness is real — but it targets the second clause. The full-vault transcript scan is itself a measurement instrument with its own error modes (pattern misses, stale heuristics, transcript formats it parses poorly), and the literature on imperfect reference standards warns specifically against promoting the broader instrument to "authoritative" without independent validation. The disagreement between the two scans establishes that at least one is wrong, not which one, and not that the wider one is right about every discrepancy.
  Specific risks: If the full scan over-flags (false positives in its staleness heuristic), the system commits to unnecessary review work and, worse, recalibrates qc_sweep against a biased reference; future tooling inherits the bias.
  Mitigations available: The already-queued diff test, extended one step: adjudicate a sample of the disagreement set by hand rather than assuming the full scan's verdicts; treat the full scan as the better screen, not the truth.

  STEELMAN:
    Item: ASSUMPTION-441
    Strongest counterargument: Declaring the broader instrument "authoritative" is the imperfect-gold-standard fallacy in miniature. Both scans are heuristic detectors of staleness; the full-vault scan dominates on coverage but has unmeasured precision. A system that calibrates its QC against an unvalidated reference converts one instrument's quirks into system-wide policy — the same self-referential verification pattern flagged on 07-09/07-10/07-11.
    What would need to be true for C2A2 to be safe: The full scan's positive calls are spot-checked by hand at least once (precision estimate), and "authoritative" is downgraded to "primary screen" until then.
    How to test: Sample n≈20 of the full scan's needs-review verdicts that qc_sweep missed; hand-adjudicate. High precision → the clause survives practically; low precision → both instruments need work.
  Recommendation: PARTIALLY-CHALLENGED
