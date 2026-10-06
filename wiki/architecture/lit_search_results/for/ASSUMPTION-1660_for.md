SEARCH-FOR-ASSUMPTION-1660:
  Date searched: 2026-09-24
  Original item: ASSUMPTION-1660
  Original statement: PRS triplets drawn from a host's summary and chapter list, not the primary
    recording, preserve the claim structure well enough to enter the tradition record.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-1660
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted the stated assumption that secondary summaries suffice for PRS extraction.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Westergaard, D. et al., 2018. "A comprehensive and quantitative comparison of text-mining in
       15 million full-text articles versus their corresponding abstracts." PLOS Computational
       Biology (PMC5831415). — Full text yields more relevant entities overall, but information
       density (relevant/irrelevant ratio) is highest in the abstract. Supports the idea that an
       author-written condensation concentrates the main claims. (Seen in search; first author per
       PLOS listing, co-authors not confirmed by fetch.)
    2. Sybrandt, J., Carrabba, A., Herzog, A. & Safro, I., 2018. "Are Abstracts Enough for Hypothesis
       Generation?" IEEE Big Data 2018 / arXiv 1804.05942 (fetched). — Full-text corpora give only
       marginally higher quantitative quality at much higher cost, and full papers introduce
       "intruder terms" that reduce interpretability. Analogous support: a condensed source can carry
       the usable relational structure.
    3. Pitkin, R.M. et al., 1999. "Accuracy of Data in Abstracts of Published Research Articles."
       JAMA (PubMed 10188662). — Cited here only as the boundary condition: abstracts are usable
       proxies for headline claims, but 18–68% contained data inconsistent with or absent from the
       article. Numeric detail is where condensed sources are least reliable.

  Strength of support: Weak

  Summary: Text-mining literature supports the narrower proposition that an author-produced
    condensation (abstract) concentrates the principal claims at high density and that, for
    relation-level extraction, moving to full text brings marginal gains with added noise. That is
    the closest analogue to extracting premise–relation–support triplets from a summary. No source
    tests a podcast host's summary or chapter list against the recording itself, and the analogy is
    to the author's own abstract, not to a third party's summary.

  Caveats: Domain transfer is the main weakness: a host summary is a secondary, possibly promotional
    rendering, closer to a press release than an author abstract. The abstract-accuracy and "spin"
    literature (Pitkin 1999; Boutron et al. on spin in RCT abstracts) shows that condensations
    selectively amplify favorable claims and drop hedges, which would change claim structure
    (qualifiers, conditions) even when topical coverage is preserved. Support is for coverage of
    main claims, not for preservation of argumentative structure or caveats.

  Search scope: Preliminary — three searches (abstract vs full-text extraction fidelity; abstract
    sufficiency for hypothesis generation; abstract accuracy/spin). No literature on podcast
    show-notes fidelity found.

  Excluded results: arXiv 2606.29251 ("When Summaries Distort Decisions") not used — bears against
    rather than for; left to 15b. Scribd/ResearchGate mirrors not used.

  Recommendation: PARTIALLY-SUPPORTED
