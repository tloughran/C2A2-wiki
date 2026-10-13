SEARCH-AGAINST-PRESUMPTION-1128:
  Date searched: 2026-10-13
  Original item: PRESUMPTION-1128
  Original statement: [unstated] Do hedges and uncertainty labels survive citation and aggregation, or
    are they lost (citation distortion, e.g. Greenberg 2009; hedging in science communication)?
  Under test: the premise that hedges are systematically lost when claims are cited or aggregated.
    I searched for evidence that hedges survive, or are even added, in citation and in downstream
    communication, and for limits on how far Greenberg 2009 generalises.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output for this item.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1128
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b (2026-10-12): Inferred from 2026-10-12 transcripts, where hedged source statements were
        restated in summaries.
      15b (2026-10-13): Searched for challenging literature. 3 searches: caveat propagation from press
        releases to news (Sumner group); quotation-accuracy meta-analyses (Jergas & Baethge) and
        Greenberg generalisability; hedging in citing sentences (Small et al.; Di Marco & Mercer). 1
        fetch attempted (PMC5158314, Sumner et al. 2016), which was blocked by a reCAPTCHA, so nothing
        was read.
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: PRELIMINARY. Snippets and abstracts only. The fetch failed.
  Search scope: preliminary (3 searches, 1 failed fetch).

  Challenging evidence found: Partial
  Strength of challenge: Moderate

  Sources:
    1. Sumner P, Vivian-Griffiths S, Boivin J, et al. 2016. "Exaggerations and Caveats in Press Releases
       and Health-Related Science News." PLoS ONE 11(12):e0168217 (PMC5158314). [snippet/abstract]
       When caveats appeared in press releases, news uptake did not fall and caveats in the news
       increased clearly. Exaggeration likewise propagated (Sumner et al. 2014 BMJ: 58% of news
       exaggerated when the press release did, against 17% when it did not). Bearing: hedges are not
       inherently lost. They propagate about as faithfully as exaggerations do. Loss happens where an
       intermediate stage drops them, which locates the problem at the summarising step, not in
       citation as such.
    2. Bott L, Bratton L, et al. 2019. [Cardiff ORCA 121559; authors not confirmed by search] J Exp
       Psychol Appl (APA). [abstract] Across four experiments, caveated news was judged more cautious,
       with no loss of reader interest or newsworthiness. Adams RC et al. 2019 (BMC Medicine) [snippet]
       found that press releases corrected to be more accurate produced more accurate news with no drop
       in coverage. Bearing: preserving hedges carries no measured downstream cost, so nothing pressures
       a careful intermediary to drop them.
    3. Small H, Boyack KW, Klavans R. 2019. "Citations and certainty: a new interface between
       citation and hedging." Scientometrics 118(3). [snippet] Citing sentences hedge more for
       less-cited and newer findings, and hedging declines as findings become established. Di Marco &
       Mercer 2004 (AAAI Symposium) [snippet] found hedging is more frequent in citation contexts than
       in text overall. Bearing: across a corpus, citers tend to calibrate certainty to the claim's
       standing rather than stripping hedges indiscriminately. Loss of hedges over time may partly
       reflect legitimate consolidation.
    4. Jergas H & Baethge C. 2015. "Quotation accuracy in medical journal articles." PeerJ 3:e1364
       [snippet]: major quotation errors 11.9%, total 25.4%. Baethge & Jergas 2025 update [snippet]
       (46 studies, about 32,000 quotations): 16.9% incorrect, 8.0% major. Bearing: this supports the
       premise that distortion is real, while limiting its scale. Most citations, about 75-83%, are
       accurate, and the error type is not specific to hedges.
    5. Greenberg SA. 2009. "How citation distortions create unfounded authority." BMJ 339:b2680.
       [snippet] Citation bias, amplification, and "conversion of hypothesis into fact" in one network
       (242 papers, 675 citations, one IBM claim). I found no published critique of its
       generalisability. A replication (Dong, Huang & Zhou 2018) reused the same network and did not
       test other claims. Bearing: the canonical evidence comes from a single case and has not been
       shown to be typical.

  Summary: The premise has strong qualitative support (Greenberg) and moderate quantitative support
    (8-12% major quotation errors). The literature does not show that hedges are systematically lost.
    In press-release-to-news chains, caveats propagate when present and cost nothing in uptake. In
    citing sentences, certainty tracks the claim's maturity and citers often add hedges. The
    "conversion of hypothesis to fact" in Greenberg's case is well documented but rests on one network.
    The defensible version is narrower: hedges are lost at intermediate summarising steps that omit
    them, and loss is not an inherent property of citation.

  Specific risks: (a) C2A2 treats hedge loss as inevitable and adds blanket uncertainty labels
    everywhere. The labels then lose their signal, which ties to alarm fatigue (PRESUMPTION-1127). (b)
    C2A2 under-attends to its own summariser step, the actual locus of loss, while blaming citation in
    general. (c) Over-hedging well-established claims misrepresents consolidation (Small 2019).

  Mitigations available: Carry hedges as structured fields (a confidence tier in provenance) and not
    as prose that a summariser can drop. Audit the summarising agents' outputs against sources
    specifically for dropped modal verbs. Let a hedge be downgraded only with a cited reason.

  STEELMAN:
    Item: PRESUMPTION-1128
    Strongest counterargument: Hedge loss is real but conditional, not systematic. Where it has been
      measured at scale, caveats in a source travel downstream at least as reliably as exaggerations,
      with no penalty in uptake. Citers hedge more, not less, for new and weakly established claims.
      Greenberg's network is a vivid single case that has not been replicated on another claim. Treating
      loss as the default risks misdirected remedies, such as blanket labels, when the measurable
      failure is located in specific summarising steps.
    What would need to be true for C2A2 to be safe: Hedge preservation is checked at C2A2's own
      summarisation and aggregation steps, which is where the evidence locates loss. Hedges travel as
      structured metadata.
    How to test: Sample about 30 hedged source statements and trace each through C2A2's cards and
      master-wiki aggregation. Count the hedges preserved, dropped, and strengthened at each hop.

  Boundary conditions identified:
    - The evidence concerns human writers and journalists. LLM summarisers may drop hedges at different
      rates. That literature was not searched and should be searched next.
    - Aggregation (many-to-one synthesis) was not separately tested. The evidence covers one-to-one
      transmission.

  Recommendation: PARTIALLY-CHALLENGED
