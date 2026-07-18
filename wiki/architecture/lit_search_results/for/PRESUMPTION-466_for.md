SEARCH-FOR-PRESUMPTION-466:
  Date searched: 2026-07-10
  Original item: PRESUMPTION-466
  Original statement: "Count discrepancy means prior figures were estimates, not that items were lost — the loss hypothesis went unvoiced."
  QUEUED-EMPIRICAL: literature clause only searched; in-house empirical test out of scope for 15a.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-466
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inference from 2026-07-09 EOD cohort
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Beyer et al. (Google), 2016. "Effective Troubleshooting." Site Reliability Engineering (sre.google/sre-book). — Codifies parsimony in triage: "different failure modes occur at different frequencies... the simplest problems tend to be the ones that occur most often," so likely/common causes should be investigated first. Supports privileging the high-base-rate explanation (record drift) over the rarer one (loss).
    2. DeHoratius & Raman, 2008. "Inventory Record Inaccuracy: An Empirical Analysis." Management Science. — Empirical base rates: ~65% of records inaccurate at any time, discrepancies overwhelmingly produced by ordinary transaction/recording errors rather than loss events; establishes that in counted-record systems, benign record-keeping error is the modal cause of count discrepancies.
    3. Radio World / Buc, 2010s. "Occam's Razor: A Handy Guide to Troubleshooting." radioworld.com. — Practitioner articulation of the same principle: when multiple explanations fit, investigate the simplest first; supports the triage ordering the presumption embodies.
    4. NCBI/PMC, 2014. "Data quality audit of the arthroplasty clinical outcomes registry NSW." (PMC4247213) — Registry-audit example where discrepancies between running registry figures and audited counts were resolved as completeness/accuracy artifacts of record-keeping (measured against ~95% benchmarks), not lost cases; illustrates the standard interpretive default in registry auditing.

  Strength of support: Moderate (for the benign-default triage ordering); None (for leaving the loss hypothesis unvoiced)

  Summary: The literature supports the probabilistic core of the presumption: in manually maintained tallies, discrepancies are far more often produced by recording error, drift, and estimate-carrying than by actual loss of items, and triage doctrine (Google SRE, Occam's-razor troubleshooting) says to weight the common, simple explanation first. On base rates alone, "prior figures were estimates" is the correct leading hypothesis for a 116-vs-110 discrepancy, and registry-audit practice routinely resolves such gaps as bookkeeping artifacts. However, the same doctrine that supports the ordering does not support silence about the alternative: SRE guidance explicitly warns that the simple-first heuristic is a prioritization rule, not an elimination rule (and notes cases where correlated symptoms mislead). No source endorses leaving the competing loss hypothesis unstated; parsimony literature assumes rejected hypotheses are enumerated, then deprioritized.

  Caveats: Support is for "benign explanation is the best prior," not "benign explanation is established" — only item-level reconciliation (the queued test) discriminates the two, since recorded-greater-than-actual is also the signature of genuine loss. The base-rate evidence is imported by analogy from retail inventory and clinical registries, not from agent-maintained backlog files. The "went unvoiced" clause is a process observation the FOR literature cannot rescue; support applies to the inference, not the omission.

  Search scope confidence: comprehensive for triage-parsimony and inventory/registry base-rate angles

  Recommendation: PARTIALLY-SUPPORTED
