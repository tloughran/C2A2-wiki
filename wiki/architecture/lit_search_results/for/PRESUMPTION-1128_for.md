SEARCH-FOR-PRESUMPTION-1128:
  Date searched: 2026-10-13
  Original item: PRESUMPTION-1128
  Original statement: Do hedges and uncertainty labels survive citation and aggregation, or are they lost (citation
    distortion, e.g. Greenberg 2009; hedging in science communication)?

  Premise tested (unstated, inferred by 14b): Hedges and uncertainty labels tend to drop away as claims are cited,
    summarised, and aggregated, so tentative claims harden into "facts". C2A2's multi-hop agent pipeline needs explicit
    mechanisms to carry uncertainty labels forward.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1128
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-10-12 transcripts where hedged claims were aggregated without carrying their hedges;
        queued 2026-10-12
      15a (2026-10-13): 3 web searches (Greenberg 2009; Latour & Woolgar modalities + Horn 2001 + Hyland hedging;
        Sumner 2014 press releases + Jergas & Baethge 2015 quotation errors). 1 fetch shared with ASSUMPTION-1780:
        Thelwall arXiv:2605.27392 (full text read). Other sources are from search-result summaries.
    Current status: SUPPORTED (Moderate-to-Strong)

  Search scope: PRELIMINARY. Citation-network analysis, sociology of science, applied linguistics (hedging),
    science-communication exaggeration, quotation-accuracy meta-analysis.

  Supporting evidence found: Yes

  Sources:
    1. Greenberg, S.A., 2009. "How citation distortions create unfounded authority: analysis of a citation network."
       BMJ 339:b2680. [search-result summary] Network of 242 papers / 675 citations on one inclusion-body-myositis
       claim. Names three distortions: citation bias (refuting papers ignored), amplification (citations from papers
       with no data), and invention, where hypotheses are converted into fact through citation alone. The same
       patterns appeared in NIH grant text. Relevance: direct. Invention is hedge loss through citation.
    2. Latour, B. & Woolgar, S., 1979/1986. Laboratory Life. [search-result summary] Statements move from heavily
       modalised ("X may suggest Y") to unmodalised fact as qualifiers are dropped. A claim becomes more fact-like when
       embedded as an unqualified premise in later work. Relevance: theoretical grounding. Hedge-stripping is the
       mechanism of fact construction.
    3. Horn, K., 2001. "The consequences of citing hedged statements in scientific research articles." BioScience
       51(12):1086. [search-result summary] Applies the Latour-Woolgar statement-type scale (1 speculative to 5 fact).
       Scientists citing or paraphrasing earlier work often change the hedges, and removing the reference can turn a
       claim into a type-4 fact. Relevance: the most direct empirical/analytical match to the premise.
    4. Jergas, H. & Baethge, C., 2015. "Quotation accuracy in medical journal articles: a systematic review and
       meta-analysis." PeerJ 3:e1364. [search-result summary] 28 studies. Pooled total quotation-error rate 25.4%
       (major errors about 11.9%). A 2025 update reports no improvement. Relevance: the citation step itself is lossy
       about a quarter of the time, which is the base rate for distortion, including overstatement.
    5. Sumner, P. et al., 2014. "The association between exaggeration in health related science news and academic
       press releases." BMJ 349:g7015. [search-result summary] Of 462 press releases, 33% exaggerated causal claims,
       36% exaggerated animal-to-human relevance, 40% exaggerated advice. Exaggeration in news rose to 58% when the
       release exaggerated, vs 17% when it did not. Relevance: aggregation steps (paper → release → news) amplify
       certainty. NOTE (counter-signal, reported for completeness): caveats in press releases did not reduce news
       uptake (69% vs 51%), so hedges can survive one hop when stated explicitly.
    6. Thelwall, M., 2026 (arXiv:2605.27392, preprint). [FULL TEXT READ] Main claims are rated stronger in abstracts
       than in discussions in 6 of 8 fields. LLMs summarising from abstracts are expected to transmit inflated
       certainty ("weak hallucination"). Cites Yao et al. 2023 (Scientometrics): hedging in Science articles declined
       from 1997 to 2021. Relevance: direct analogue for LLM-agent aggregation in C2A2.

  Strength of support: Moderate-to-Strong. Converging evidence from several independent fields. Quantitative
    hedge-retention rates across citation hops were not found.

  Summary: Sociology of science (Latour & Woolgar) describes fact-making as the progressive removal of modal
    qualifiers. Horn (2001) documents citing authors changing hedges. Greenberg (2009) shows hypotheses converted into
    accepted fact through citation alone in a real network. Meta-research finds about 25% of quotations are
    inaccurate, and science-communication chains amplify causal and generalisation claims. A 2026 preprint shows
    abstracts, the most-used summary layer, already carry stronger claims than the body, so LLM aggregation starting
    from abstracts begins with inflated certainty. This supports the premise that hedges tend to be lost in citation
    and aggregation, and the C2A2 need for explicit, structured uncertainty labels that travel with each claim.

  Caveats: (i) Sumner 2014 shows that explicit caveats can survive one hop. Loss is a tendency, not a law, and
    explicit structured labels may resist it better than inline linguistic hedges, which supports C2A2's
    label-based approach. (ii) Greenberg is a single-claim case study. (iii) Horn and Latour are partly qualitative.
    (iv) Hedge words are an imperfect proxy for certainty (one study: r = 0.55). (v) Most evidence covers human
    authors. LLM-specific evidence is one preprint.

  NOVELTY flag: Partial. Hedge loss through citation is established. Measured hedge retention across automated
    multi-agent aggregation hops was not found, so C2A2 could measure this itself.

  Recommendation: SUPPORTED (Moderate-to-Strong).
