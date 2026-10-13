SEARCH-FOR-PRESUMPTION-1120:
  Date searched: 2026-10-11
  Original item: PRESUMPTION-1120
  Original statement: Each proposal-writing job presumes its own evidential threshold is the house threshold (wiki daily
    run declined to propose from unverifiable content; Wolfram agent proposed from segment titles and deferred the check
    to the reviewer). Question: Should all proposal-writing agents share one explicit evidential threshold, and where
    should unverifiable-but-relevant items go?

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1120
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from divergent behaviour of two proposal-writing jobs (one declined unverifiable content, one
        proposed from segment titles and deferred verification to the reviewer); queued 2026-10-10
      15a (2026-10-11): 3 web searches, 1 fetch (PubMed 31272125; succeeded, abstract). A first fetch attempt on the
        pubmed.ncbi.nlm.nih.gov URL was blocked by the tool (URL not in provenance set) and returned nothing. Found
        systematic-review practice that fixes shared eligibility criteria, pilots them for consistent interpretation,
        and routes "maybe / can't tell" records to a defined next stage; documented between-rater variation in triage
        scales; GRADE treats "evidence gap" as a category distinct from "very low certainty".
    Current status: PARTIALLY-SUPPORTED (Moderate)

  Search scope: PRELIMINARY. 3 web searches: (a) systematic-review screening disagreement, explicit criteria, "unclear"
    records; (b) standardised triage thresholds and inter-rater variation; (c) GRADE certainty and an
    "insufficient evidence" category. 1 fetch: PubMed abstract 31272125 (succeeded).

  Supporting evidence found: Partial

  Sources:
    1. Systematic-review screening guidance: Virginia Tech and NYU library guides; Covidence "How to resolve conflicts
       during screening"; CASRAI title/abstract screening guide. [search-result] Best practice is one written set of
       eligibility criteria, piloted so that all screeners interpret it the same way, plus a "maybe / can't tell"
       option. "Maybe" records are treated as included at title/abstract and go to full-text review; a "maybe" against
       a "no" goes to conflict resolution by a defined arbiter. Relevance: direct analogue. One shared threshold, and
       an explicit lane for unverifiable-but-relevant items (forward with a "maybe" tag rather than drop or silently
       pass).
    2. Dual-review study, PubMed 31272125 (Wiley 2019; authors not captured). [fetched, abstract] Within one large
       review, a second reviewer at title/abstract recovered 6.6-9.1% more eligible studies and at full text 6.6-11.9%
       more. Relevance: individual screeners applying the same criteria still diverge, so consistency needs process,
       not just a stated rule. Indirect support.
    3. Triage scale reliability: Australasian Triage Scale and CTAS studies (dovepress; Cambridge Core; Int J Emerg
       Med 2020). [search-result] "Considerable variation" in how nurses apply the scale; authors call for improved
       uniformity and standardised approaches. Relevance: analogue for agents applying a threshold idiosyncratically.
    4. GRADE certainty framework (NHMRC "Assessing certainty of evidence"; PMC tables). [search-result] An "evidence
       gap" row ("available evidence is insufficient to determine true effect") sits outside the four certainty
       levels. Relevance: precedent for a named category for insufficient/unverifiable evidence, separate from low
       confidence.

  Strength of support: Moderate for a shared explicit threshold and a defined "maybe" lane; Weak for evidence that this
    improves outcomes in agent pipelines.

  Summary: Systematic-review methodology prescribes a single written set of eligibility criteria applied by all
    screeners, piloted for shared interpretation, and an explicit "can't tell" category routed forward to a defined
    stage and arbiter. This matches both halves of the question. Triage and dual-screening studies show that even with
    shared criteria raters diverge, which supports making the threshold explicit and auditable. GRADE offers a model
    for labelling unverifiable items as an evidence gap rather than either rejecting them or presenting them as
    proposals.

  Caveats: (i) Review guidance favours sensitivity at early stages ("maybe" goes forward), which matches the Wolfram
    agent's behaviour, provided the item is labelled; it is not support for the stricter wiki-run behaviour as the
    universal default. (ii) Forwarding "maybe" items shifts burden to the reviewer; reviewer capacity is the C2A2
    constraint (see PRESUMPTION-1121). (iii) Human-screener evidence; transfer to LLM agents is by analogy.

  NOVELTY flag: none for the principle; application to heterogeneous AI proposal-writing agents not found.

  Recommendation: PARTIALLY-SUPPORTED (Moderate). Preliminary search; broader search recommended (Cochrane Handbook
    ch. 4 on selection; PRISMA-S; inter-screener kappa studies).
