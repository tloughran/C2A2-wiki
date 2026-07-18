SEARCH-AGAINST-PRESUMPTION-475:
  Date searched: 2026-07-13
  Original item: PRESUMPTION-475
  Original statement: "Two same-day censuses of the same vault (bootstrap audit 3,338/2,644/647 vs. weekly agent 3,258/2,567/644) may coexist without reconciliation — each series is presumed valid within itself."

  PROVENANCE:
    Origin: 14b
    Chain: 14b -> 15b
    Original item: PRESUMPTION-475
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference from the 2026-07-12 census pair
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. [Bland, J.M. & Altman, D.G., limits-of-agreement method (Br J Anaesth, S0007-0912(17)34715-3; repeated-measures and hierarchical Bayesian extensions, PMC2645135). — The method EXISTS because two procedures measuring one quantity must have their difference characterised: the mean difference estimates systematic BIAS, the SD quantifies random variation. The discipline's entire response to "two instruments disagree" is to compute the bias and the limits of agreement. "Each valid within itself" is the position the method was invented to replace.]
    2. [Dual-system estimation / capture-recapture doctrine ("Dual system estimation using mixed effects loglinear models," arXiv:2505.01359; "Naive linkage error corrected dual system estimation," arXiv:2003.13080). — DECISIVE and additive: two independent enumerations of the same population are not merely a discrepancy to be tolerated; they are jointly informative about what BOTH missed. The dual-system estimator uses exactly this pair to estimate the unobserved cell — the units captured by neither list. Leaving the two censuses unreconciled FORFEITS the one piece of information the pair uniquely provides, which is an estimate of the vault's true size.]
    3. [The same dual-system literature's assumption set (closure, perfect matching, homogeneous inclusion, independence, no erroneous captures). — Turned on the presumption: these assumptions are exactly what a reconciliation pass would test. Declining to reconcile means never learning which of them the two censuses violate — and "perfect matching" and "no erroneous captures" are precisely the assumptions a basename-only resolver defect (ASSUMPTION-446, same cohort) would break.]
    4. [PRESUMPTION-473 / REVISE-209 (in-house, 2026-07-12). — The system has ALREADY dispositioned that self-ascertained denominators cannot measure their own missingness and that terminal completeness claims require independent corroboration. Two same-day censuses are the independent corroboration REVISE-209 asks for — and the presumption is that they may be left uncompared. The system is holding the cure and declining to take it.]
  Strength of challenge: Strong
  Summary: The measurement literature does not merely fail to support the presumption; it inverts it. Two independent enumerations of one population are the single most valuable measurement configuration available, because differencing them yields both the systematic bias (Bland-Altman) and an estimate of what neither captured (dual-system estimation). The presumption discards both. And the timing is damning: REVISE-209, issued by this very pipeline one day earlier, established that terminal completeness claims require independent corroboration — and here sits an independent corroboration, unexamined. An 80-file / 77-orphan gap between two same-day counts of the same vault is either a definitional difference (in which case it decomposes exactly and takes five minutes to prove) or it is a defect (in which case one of the two series is wrong and downstream figures have been silently drawing on the wrong one).
  Specific risks: Downstream figures inherit whichever series they happened to draw from, with no record of which. The connectivity narrative (ASSUMPTION-447, ASSUMPTION-448) rides on the weekly-agent series; the bootstrap audit disagrees with it by ~2.5%; and the resolver defect (ASSUMPTION-446) is a live candidate explanation for part of the gap. Three items in this single cohort are entangled in an unreconciled discrepancy.
  Mitigations available: The queued empirical test is the right one and is cheap: diff the two runs' file sets and orphan lists; the gap must decompose EXACTLY into definitional exclusions plus resolver differences. If it decomposes exactly, the presumption is salvaged in a restricted form (with the decomposition recorded). If it does not, one series is wrong. Additionally — and this is the additive recommendation — treat the pair as a dual-system estimator and report the estimated true vault size, which is information the system currently throws away every week.

  STEELMAN:
    Item: PRESUMPTION-475
    Strongest counterargument: Two clocks that disagree do not tell you the time; they tell you that you do not know the time, and a system that keeps both and consults whichever is nearer to hand has not preserved optionality — it has lost the ability to be wrong in a detectable way. Worse, the system issued a governing convention (REVISE-209: terminal completeness claims require one independent corroboration) the day before, and is now sitting on exactly such a corroboration while presuming it needs no attention. The presumption is not merely unsupported; it is in direct tension with the pipeline's own most recent ruling, and nobody noticed because the two artifacts live in different files.
    What would need to be true for C2A2 to be safe: The 80-file / 77-orphan gap must decompose EXACTLY into known definitional exclusions (different inclusion criteria between the bootstrap audit and the weekly agent), with a written record of the decomposition and a rule stating which series is canonical for which downstream consumer.
    How to test: Diff the two file sets and the two orphan lists. Classify every element of the symmetric difference. If every element falls into a named definitional bucket, record the decomposition and make it a standing invariant. If any element is unexplained, escalate: one census is defective, and the resolver defect of ASSUMPTION-446 is the first suspect.
  Recommendation: CHALLENGED
