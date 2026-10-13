SEARCH-FOR-ASSUMPTION-1780:
  Date searched: 2026-10-13
  Original item: ASSUMPTION-1780
  Original statement: How reliably do abstracts (and talk outlines) represent a paper's/talk's claims, and what does
    that imply for carding proposals from abstracts alone?

  Premise tested: Abstracts and talk outlines often misrepresent the underlying work, overstating it or leaving out or
    changing data. So C2A2 should not card claims from abstracts alone without marking them as abstract-derived and
    lower confidence.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1780
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-10-12 transcripts on carding proposals from abstracts / talk outlines; queued
        2026-10-12
      15a (2026-10-13): 4 web searches (Pitkin abstract accuracy; Boutron spin; conference abstract vs full
        publication / Toma 2006 / Cochrane MR000005; abstract-only screening in systematic reviews). 1 fetch: Thelwall
        arXiv:2605.27392 (full text read). Other sources are from search-result summaries only.
    Current status: SUPPORTED (Strong for biomedical abstracts; Moderate as a general claim)

  Search scope: PRELIMINARY, but a well-developed meta-research literature. Mostly biomedical. Talk outlines are
    covered only by analogy through conference abstracts.

  Supporting evidence found: Yes

  Sources:
    1. Pitkin, R.M., Branagan, M.A., Burmeister, L.F., 1999. "Accuracy of Data in Abstracts of Published Research
       Articles." JAMA 281(12):1110-1111. [search-result summary] Across 6 major medical journals, 18%-68% of abstracts
       had data that were inconsistent with the body or missing from it. Relevance: direct. Even in top journals,
       abstracts are an unreliable proxy for the paper's content.
    2. Boutron, I., Dutton, S., Ravaud, P., Altman, D.G., 2010. "Reporting and interpretation of randomized controlled
       trials with statistically nonsignificant results for primary outcomes." JAMA 303(20):2058-2064.
       [search-result summary] Spin was found in more than 68% of abstracts of RCTs with nonsignificant primary
       outcomes (vs about 61% of main texts). A follow-up RCT (SPIIN) found that spin in abstracts made clinicians
       rate treatments as more beneficial (small effect). Relevance: direct. Abstracts are where overstatement
       concentrates, and it changes readers' judgments.
    3. Toma, M. et al., 2006. JAMA 295(11):1281 (ACC meeting abstracts vs later full articles); Scherer, R.W. et al.
       Cochrane Methodology Review MR000005, "Full publication of results initially presented in abstracts."
       [search-result summary] 41% of 148 later-published cardiology RCTs had discrepant primary-outcome estimates
       between meeting abstract and article, and in 14% significance flipped. Only about 56% of RCT abstracts reach
       full publication, with a bias toward positive results. Relevance: direct analogue for talk outlines and
       conference abstracts. Figures not checked against full text.
    4. Thelwall, M., 2026 (arXiv:2605.27392, preprint). "Will AI be overconfident about academic research findings
       when reliant on abstracts?" [FULL TEXT READ] GPT-OSS-120B rated main-claim strength in abstract, discussion,
       and conclusion for about 14k MDPI articles across 8 journals. Outside the humanities and social sciences,
       claims were rated stronger in the abstract (and conclusion) than in the discussion, with mostly non-overlapping
       95% CIs. The author concludes that LLMs relying on abstracts may be overconfident. Relevance: very close to
       C2A2's use case, since LLM agents carding from abstracts would inherit inflated certainty.
    5. Supporting context: later replications of spin rates in cardiology (27%), pain/anesthesia (55%), and a 2017
       review of diagnostic-accuracy abstracts (23% overly optimistic). A Cochrane colloquium protocol warns that
       title/abstract screening misses harms data. [search-result summaries, authors not verified]

  Strength of support: Strong for "abstracts frequently misstate or overstate"; Moderate for the C2A2 implication
    (no study directly tests a carding-from-abstract workflow)

  Summary: A consistent meta-research literature shows that abstracts are often inaccurate (data inconsistent with or
    missing from the body), more spun than the main text, and in the case of conference abstracts later changed
    substantially or never published. A 2026 preprint directly models C2A2's risk: LLMs that read only abstracts
    would assign higher certainty to the main claim than the discussion supports. This supports treating
    abstract-only cards as provisional, tagged with source granularity, and capped in confidence.

  Caveats: (i) The evidence is mostly biomedical. Abstract reliability may differ in physics, philosophy, or
    consciousness studies, the domains C2A2 cards most often. Thelwall found little abstract inflation in the
    humanities and social sciences. (ii) Thelwall uses a single LLM as judge, MDPI journals only, and is not peer
    reviewed. (iii) No source directly addresses talk outlines; conference abstracts are the nearest proxy. (iv) Many
    abstracts are accurate. The claim is about error rate, not that abstracts are useless.

  NOVELTY flag: Partial. The abstract-reliability problem is established. A formal rule for carding provenance from
    abstracts in a multi-agent wiki was not found (Thelwall 2026 is the nearest).

  Recommendation: SUPPORTED (Strong for the empirical premise; Moderate for the design implication).
