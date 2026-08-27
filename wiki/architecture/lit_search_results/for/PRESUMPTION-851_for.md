SEARCH-FOR-PRESUMPTION-851:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-851
  Original statement: "[inferred] That corroboration is external if its content is external — independence of evidence conferred by externality of authorship, when selection was internal."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-851
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by tracing the selection path of a source credited as external
        validation.
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Search scope: PRELIMINARY — BROADER SEARCH STRONGLY RECOMMENDED. This item was searched
    last and the session's web-search budget (200/200 calls) was exhausted before its two
    dedicated queries could execute. The intended and unrun queries were: (a) congeniality
    bias and confirmation bias in literature selection / selective citation as a threat to
    evidential independence; (b) prospective registration of search strategy (PROSPERO,
    pre-specified protocols) as a control on selective inclusion. Neither was run.
    What I did reach, incidentally via searches conducted for ASSUMPTION-1164,
    ASSUMPTION-1175 and PRESUMPTION-849 and via a full-text fetch: the blinding and
    double-blind-peer-review literature, the bias-against-novelty literature in bibliometric
    indicator use, and the correlated-error / algorithmic-monoculture literature bearing on
    the reflexive case (REVISE-350). Full text read: arXiv:2101.02701.
    Recorded gaps: no coverage of philosophy-of-evidence work on independence of evidence
    and triangulation; no coverage of citation-bias meta-research (e.g. citation distortion,
    selective citation in trials); no coverage of PROSPERO/protocol-deviation empirical work.
    These are the three places a positive case would most plausibly be found.

  Supporting evidence found: No

  Sources:
    (No source was located that supports the presumption as stated. The following were
    reached and bear on the question; both cut against it or are neutral. They are recorded
    for transparency of scope, not as supporting evidence.)

    1. Sun, M., Danfa, J. B. & Teplitskiy, M. "Does double-blind peer review reduce bias?
       Evidence from a top computer science conference." arXiv:2101.02701. — Bears directly
       on whether externality of content suffices for independent assessment, and finds it
       does not. Across 5,027 ICLR submissions, masking author identity — leaving the
       content entirely unchanged — significantly lowered mean ratings for the top prestige
       tercile (p=0.0035), raised inter-reviewer disagreement, and improved rejection
       accuracy (2-year citations of rejected papers significantly lower under double-blind,
       p=0.0016; p=4.4×10⁻¹¹ for the most effectively anonymised subset). Who is attached
       to a piece of evidence changes how it is weighed independently of what the evidence
       says. (read in full)
    2. Wang, J., Veugelers, R. & Stephan, P., 2017. "Bias against novelty in science: A
       cautionary tale for users of bibliometric indicators." Research Policy,
       46(8):1416–1436. — Neutral-to-against. Demonstrates that the selection instrument
       (standard bibliometric indicators) systematically mis-ranks externally authored,
       externally published work: novel papers are less likely to be top-cited in short
       windows and appear in lower-IF journals, yet are more likely to become long-run hits.
       Externality of authorship does not make the selection channel unbiased.
       (search-snippet-only)
    3. Kim, E., Garg, et al., 2025. "Correlated Errors in Large Language Models." ICML 2025;
       arXiv:2506.07962. — Bears on the reflexive case named in the brief (REVISE-350).
       Across 350+ models, error correlation is driven by shared architecture and provider,
       and the paper demonstrates the downstream consequence specifically for LLM-as-judge
       evaluation. Where the selector of evidence and the assessor of that evidence share a
       generator, their errors are correlated by construction; the externality of the
       selected content does not decorrelate them. (search-snippet-only)

  Strength of support: None

  Summary: I found no literature supporting the presumption that externality of authorship
    confers evidential independence when the selection of that evidence was internal. This
    is a preliminary result and should be read as such — the two queries designed to test
    this item directly were never run because the session's search budget was exhausted, and
    the three most likely homes for a positive case (philosophy of evidence on independence
    and triangulation; citation-bias meta-research; empirical work on pre-registered search
    protocols) were not reached at all. What I did reach points the other way. The ICLR
    natural experiment shows that changing only who is visibly attached to a fixed body of
    content changes both how it is scored and how accurately it is sorted, which is the
    cleanest available demonstration that externality of content does not by itself
    neutralise the selecting party's disposition. The bias-against-novelty work shows the
    selection instrument itself carries systematic bias regardless of the externality of what
    it selects. And on the reflexive sub-case, the correlated-error literature shows that
    when selector and assessor share a generator their errors are correlated by construction.
    None of this is a substitute for the dedicated search that was not run.

  Caveats:
    - The primary caveat is the search itself. This is a preliminary, budget-truncated
      search and a NO-SUPPORT-FOUND result here carries much less weight than it would from
      a comprehensive one. It should not be read as evidence of absence.
    - The three sources listed were retrieved for other items and reached here by
      adjacency. None was selected by a query designed to test this presumption, which is
      itself a selection-path problem of exactly the kind the presumption concerns — noted
      openly rather than elided.
    - Sun et al. is human peer review, not literature selection by an agent, and its authors
      note they cannot rule out that ICLR's policy change altered the submission pool. The
      transfer to an agentic evidence pipeline is by analogy.
    - There is a plausible positive case I could not test: that convergent corroboration
      from multiple independently authored sources retains evidential value even under a
      biased selector, provided the selection criterion is orthogonal to the proposition at
      issue. Triangulation arguments of this shape exist in the methodological literature.
      I did not reach them and cannot report on their strength either way.
    - Asymmetry of assignment: I searched only for supporting evidence and did not pursue
      the disconfirming case. The against-direction search (15b) should be treated as
      carrying the weight on this item until the FOR search is redone properly.

  Recommendation: NO-SUPPORT-FOUND

  PARTIAL NOVELTY-FLAG:
    Item: PRESUMPTION-851, reflexive sub-case only.
    Searched: no dedicated query was executed (budget exhausted). The finding below rests on
      sources reached incidentally while searching other items.
    Finding: the general question — whether independence of evidence survives a
      non-independent selection path — is almost certainly NOT novel; it is standard ground
      in confirmation-bias, citation-bias and search-protocol methodology, and I simply did
      not reach that literature. No novelty is claimed for the general limb. The reflexive
      sub-case is different: I found nothing addressing the configuration in which the
      selector of corroborating evidence and the assessor of that corroboration are the same
      generative model, so that "external content" is retrieved and judged by a single
      correlated epistemic apparatus. The correlated-error literature establishes the
      mechanism for LLM-as-judge but does not extend it to LLM-as-selector-and-then-judge.
    Unaddressed sub-claim, precisely: "content authored outside a system provides
      corroboration that is evidentially independent of that system, when the system both
      selected the content and assessed its corroborative force."
    Implication: this is the sub-claim that bears on REVISE-350 and it should not be
      discharged on the strength of the present search. Recommend re-running the FOR search
      for this item with a fresh budget before any register status is changed.
    Recommended status: NOVEL (reflexive sub-case only; general limb NOT flagged — unsearched,
      not unaddressed).
