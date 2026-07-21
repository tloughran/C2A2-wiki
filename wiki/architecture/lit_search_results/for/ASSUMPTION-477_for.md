SEARCH-FOR-ASSUMPTION-477:
  Date searched: 2026-07-20
  Original item: ASSUMPTION-477
  Original statement: 15a/15b independence became structural on 2026-07-19 for the first time; every prior disposition in the record was produced under an asserted rather than enforced independence.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-477
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 lit-search pipeline transcript
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. "Minority Sentinel: When to Overturn Majority Voting in Multi-Agent LLM Debates" (arXiv:2606.29270). — The strongest and most directly on-point source. States the independence assumption explicitly as inherited from the Condorcet Jury Theorem — "individual voter errors must be mutually independent" — and then reports that contemporary LLMs "share highly similar pretraining corpora, training procedures, and architectural designs, causing their errors to exhibit strong correlations that fundamentally violate this independence assumption." Names the consequence "Minority Truth": the correlated majority systematically suppresses correct minority opinions. This is exactly the epistemic risk ASSUMPTION-477 identifies in the pre-07-19 record, and it establishes that asserted independence between LLM evaluators is not merely unenforced but is known to fail even when procedurally honoured.
    2. "The Confident Liar: Diagnosing Multi-Agent Debate with Log-Probabilities and LLM-as-Judge" (arXiv:2606.10296). — Reports that an LLM judge reading debate logs "yields negative Net Gain when the majority errs due to shared reasoning biases, as the judge is highly likely to make the same mistake," and that a non-LLM classifier "fundamentally circumvents the systematic interference of LLM error correlation on adjudication accuracy." Bears directly on 15c: an LLM reconciler over two correlated LLM searches can make the aggregate worse than either input, which is a stronger claim than ASSUMPTION-477 makes.
    3. Bearman, M. et al. / Cochrane methods literature via "The value of a second reviewer for study selection in systematic reviews" (PMC6989049). — Establishes the systematic-review standard the C2A2 pipeline is modelled on: AHRQ, CRD, IOM and Cochrane all require two or more team members "working independently" to screen, and the measured effect of the second independent reviewer is an average 9% increase in eligible studies identified (range 0-32%). This quantifies what independence buys and therefore what its absence costs.
    4. Blinded-vs-unblinded assessment literature: Berger, V.W. et al., "Blinded versus unblinded assessments of risk of bias in studies included in a systematic review"; Saltaji, H. et al. via Cochrane. — Reports that blind assessments produced "significantly lower and more consistent scores." Directly supports the item's in-house test design: if structural blocking lowers 15a's confidence or raises 15b's challenge strength relative to the pre-07-19 baseline, the delta estimates the prior contamination.
    5. Rooyen, S. van et al. (1998), via "Blinding as a Solution to Bias" (Rothman & Snyder chapter, U. Arizona). — Reported as a null result: blinding "made no editorially significant difference in the quality of review, the recommendations of reviewers, or the time taken to review." Included per no-cherry-picking rule: the peer-review blinding literature is genuinely mixed, and this is the strongest null.
    6. "Multi-Agent Debate for LLM Judges with Adaptive Stability Detection" (arXiv:2510.12697); "When AIs Judge AIs: The Rise of Agent-as-a-Judge Evaluation for LLMs" (arXiv:2508.02994). — Supply the mitigation: "diversity of agent roles is critical to multi-agent evaluation; if all agents are prompted with the same persona or perspective, the benefits diminish." Supports the C2A2 design of assigning 15a/15b opposed directions as a diversity mechanism — but only if the assignment is enforced rather than asserted.

  Strength of support: Strong (for the epistemic importance of enforced independence); Not assessed (for the dated factual claim)

  Summary: The item's normative core — that asserted independence is materially weaker than enforced independence, and that dispositions produced under the former should be discounted — is strongly supported and, in the LLM case specifically, understated. The multi-agent-evaluation literature of 2025-2026 does not merely say independence is desirable; it reports that LLM evaluators violate independence *structurally*, through shared pretraining, even when procedurally separated, and that a correlated majority actively suppresses correct minority findings. That is a stronger conclusion than ASSUMPTION-477 draws, and it implies that 2026-07-19 did not achieve independence but only removed one of several contamination channels. The systematic-review literature supplies the quantitative baseline (second independent reviewer yields ~9% more eligible items) and validates the item's proposed re-run test, since blinded assessment is documented to produce lower and more consistent scores — a measurable signature to look for.

  Caveats: (a) The dated factual claim ("became structural on 2026-07-19 for the first time") is an internal historical assertion about C2A2's own run log and is not the kind of thing literature can support; it is outside search scope and I make no finding on it. (b) The blinding literature is genuinely mixed — van Rooyen et al. is a well-known null — so the *size* of the contamination effect should not be presumed large. The systematic-review effect sizes (9%, range 0-32%) are the best available estimate and their lower bound is zero. (c) The LLM-correlation sources undercut the item's implied relief: structural file-access blocking does not address shared-pretraining correlation, which is the dominant channel in the retrieved literature. The 905-pair record may be contaminated by a mechanism the 07-19 fix does not touch. This is support for the item's concern but not for its proposed resolution. (d) Sources 1, 2 and 6 are recent preprints and have not been assessed for peer-review status.

  Recommendation: SUPPORTED
