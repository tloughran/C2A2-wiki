SEARCH-AGAINST-ASSUMPTION-467:
  Date searched: 2026-07-18
  Original item: ASSUMPTION-467
  Original statement: The maintained 300-PRS narrative figure is treated as canonical over the master current-status per-file sum (447 today); two same-day agents each advanced a different count.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-467
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-17 EOD run
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Gromov, "The Single Source of Truth Illusion" (Analyst's Corner). — Warns that an SSOT that doesn't reflect a domain's reality drives users to shadow systems; a decreed canonical number can be the WRONG one. Challenges any presumption that the computed 447 should simply override the maintained 300.
    2. "The Myth of the Single Source of Truth" (Data Dynamics). — Argues discrepancies should be "treated as signals to be examined rather than errors to be eliminated." The 300-vs-447 gap is diagnostic, not a defect to auto-resolve toward one side.
    3. PowerMetrics, "What does 'single source of truth' actually mean for metrics?" — A metric is only canonical relative to an agreed DEFINITION; without a shared PRS definition, neither 300 nor 447 is authoritative, and picking the computed sum risks over-counting.

  Strength of challenge: Moderate

  Summary: The literature challenges the implicit resolution (treat the computed per-file sum as canonical). Single-source-of-truth is not automatically the machine-computed number: if the per-file sum counts drafts, duplicates, or non-canonical items that the narrative 300 deliberately excludes, then 447 over-counts and adopting it would corrupt the metric. The disciplined move is to treat the divergence as a signal and first define what a "PRS" is, THEN designate the source — not to privilege either figure by default.

  Specific risks: Silently adopting 447 (or defending 300) without a definition entrenches a wrong metric and hides the definitional disagreement that produced two same-day counts.

  Mitigations available: Write an explicit PRS counting rule; compute both figures under it; reconcile once; automate the canonical count from the rule so agents can't diverge.

  STEELMAN:
    Strongest counterargument: "Canonical" should attach to a DEFINITION, not to whichever process is more automated. The per-file sum feels authoritative because it is computed, but computation of the wrong predicate is precisely how you get a precise, trusted, wrong number (Goodhart by mechanization). The real defect is the missing definition, not which number wins.
    What would need to be true for the assumption's resolution to be safe: A single, written PRS definition must exist and both counters must implement it; only then is the computed sum trustworthy as canonical.
    How to test: Define PRS; recompute; if 300 and 447 converge under the definition, the gap was a bug; if they legitimately differ, they measure different things and neither is "the" count.

  Recommendation: PARTIALLY-CHALLENGED
