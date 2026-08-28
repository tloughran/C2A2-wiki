SEARCH-FOR-PRESUMPTION-889:
  Date searched: 2026-08-28
  Original item: PRESUMPTION-889
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority High)
  Original statement: [inferred] That a provenance caveat placed in a document header governs the claims in
    the body, and survives citation of those claims.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-889
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the gap between one file's header and its own body; the originating run recorded
        itself as an instance.
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND (the literature documents the opposite)

  Search scope: WebSearch, 2026-08-28, one dedicated query on the loss of hedges and caveats along
    communication and citation chains. Literature reached: PNAS Nexus (2024), "Expressions of uncertainty in
    online science communication hinder information diffusion" (also at PMC11489878); Jensen, J. D. (2008),
    "Scientific Uncertainty in News Coverage of Cancer Research," Human Communication Research; Gustafson &
    Rice (2020), "A review of the effects of uncertainty in public science communication," Public
    Understanding of Science; an arXiv paper on uncertainty propagation in LLM-based systems (2604.23505);
    an arXiv paper on annotating scientific uncertainty (2503.11376). NOT COVERED and material: the
    citation-distortion literature proper (Greenberg's 2009 BMJ network analysis of belief propagation),
    which is the exact mechanism at the citation step and which the 2026-08-26 run touched from a different
    angle. All sources SNIPPET-ONLY. Search confidence: MODERATE-HIGH.

  Supporting evidence found: No

  Sources:
    1. Anon. (2024), "Expressions of uncertainty in online science communication hinder information
       diffusion," PNAS Nexus 3(10):pgae439 [SNIPPET-ONLY; authors unverified]
       https://academic.oup.com/pnasnexus/article/3/10/pgae439/7811203 —
       NLP analysis of over 2 million social-media messages about scientific findings: more uncertain
       messages are shared less often. Supplies a selection mechanism by which hedges are stripped as claims
       propagate — the hedge does not travel because hedged versions travel less.
    2. Jensen, J. D. (2008), "Scientific Uncertainty in News Coverage of Cancer Research," Human
       Communication Research [SNIPPET-ONLY] https://jakobdjensen.com/wp-content/uploads/2016/02/2008_Jensen_Human-Com-Research.pdf —
       Reports that news reports of scientific research are rarely hedged: caveats, limitations and other
       uncertainty indicators are absent at the retransmission step.
    3. Gustafson, A., & Rice, R. E. (2020), "A review of the effects of uncertainty in public science
       communication," Public Understanding of Science [SNIPPET-ONLY]
       https://journals.sagepub.com/doi/abs/10.1177/0963662520942122 — Review-level treatment; also supplies
       the *reason* the removal is systematic rather than careless: uncertainty qualifiers can undermine
       trust and sharing, so communicators have an incentive to drop them.
    4. Anon., "Uncertainty Propagation in LLM-Based Systems" (arXiv:2604.23505) [SNIPPET-ONLY; authors
       unverified] — Reports that communication topology — who receives an uncertainty signal, how it is
       retransmitted, how contributions are weighted at aggregation — can amplify, damp or distort the
       evidential content of propagated uncertainty. Directly transferable to a multi-agent estate.

  Strength of support: None for the presumption; Strong for its negation

  Summary: A supportive search returns no support and a well-populated contrary literature. Across science
    communication, journalism studies and now multi-agent LLM systems, the consistent finding is that
    evidentiary qualifiers are lost at each retransmission, and that the loss is structural rather than
    accidental: hedged versions diffuse less, and the actors doing the retransmitting have incentives to
    strip them. The specific architectural form the presumption assumes — a caveat in a header governing an
    unhedged body — is the arrangement most exposed to this, since the body is what gets cited. Nothing was
    found supporting header-scoped qualification.

  Caveats: The corpus is about public communication of science, not internal machine-generated records; the
    transfer is strongly plausible but assumed. The LLM-topology paper is an unreviewed 2026 preprint.

  Recommendation: NO-SUPPORT-FOUND
