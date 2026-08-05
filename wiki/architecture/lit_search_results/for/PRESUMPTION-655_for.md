SEARCH-FOR-PRESUMPTION-655:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-655
  Original statement: That a verification mark is independent of the tool that
    produced it — a retrieval method having been caught producing false
    affirmatives, with no field recording which method was used and no
    enumerable set of affected marks.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-655
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 observation that a retrieval method
        was found producing false affirmatives while no field recorded the
        method used, leaving affected verification marks unenumerable
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. W3C, 2013. PROV-O: The PROV Ontology (W3C Recommendation) and PROV-DM.
       — Defines provenance as the record of the agents, entities and
       activities involved in producing a piece of data, and exists precisely
       because a result is not interpretable independently of what produced
       it. Provenance is named as instrumental to traceability,
       reproducibility, accountability and quality assessment.
    2. "Propagation of errors in citation networks: a study involving the
       entire citation network of a widely cited paper published in, and later
       retracted from, the journal Nature." Research Integrity and Peer Review,
       2016 (doi:10.1186/s41073-016-0008-5). — Traces how withdrawn support
       fails to back-propagate through the network of claims that relied on it.
    3. Hsiao, T.-K. & Schneider, J., 2021. "Continued use of retracted papers:
       Temporal trends in citations and (lack of) awareness of retractions
       shown in citation contexts in biomedicine." Quantitative Science Studies
       2(4):1144. — Finds retracted work continues to be cited, largely because
       citing authors are unaware of the retraction status and because
       databases do not consistently link the item to its retraction notice.
       The structural failure is the missing back-link, which is the same
       object as the missing method field.
    4. Meta Engineering, 2021, "Silent data corruption: mitigating effects at
       scale"; and "Detecting silent data corruptions in the wild"
       (arXiv:2203.08989). — Establishes that when a fault leaves no record or
       trace, determining the scope of what it touched becomes computationally
       hard and effects propagate into services far removed from the defect.
    5. Decision provenance literature (arXiv:1804.05741, "Decision Provenance:
       Harnessing data flow for accountable systems"). — Argues that
       accountability for automated determinations requires recording which
       process produced them; the accountability claim is not separable from
       the production record.

  Strength of support: None

  Summary: Nothing was found supporting the independence of a verification
    mark from its producing tool, and the provenance literature exists as a
    field on the contrary premise. The W3C standard's purpose is to make the
    producing activity a first-class recorded property of the result. The
    retraction-propagation studies supply the empirical consequence of
    omitting that link: once support is withdrawn, claims that rested on it
    continue to circulate as valid, principally because nothing connects the
    downstream claim back to the withdrawn basis. The silent-data-corruption
    work supplies the second consequence, which is exactly the one C2A2
    observed — with no trace of which method ran, the affected set is not
    enumerable, and scope determination becomes intractable rather than merely
    laborious. The condition described is not a gap in the record; on this
    literature it is the absence of the record that would make remediation
    possible at all.

  Caveats: The retraction analogy concerns a decentralised literature with no
    central authority to force propagation, whereas C2A2's marks live in a
    system that could in principle be re-run in full — if a full re-verification
    is cheap, the missing provenance field is recoverable by brute force rather
    than fatal. That is the one route by which the presumption's practical
    consequence could be avoided, and it is not addressed by any located
    source. Annotation-in-place practice for withdrawn support returned no
    substantial dedicated literature and may warrant a narrower search.

  Recommendation: NO-SUPPORT-FOUND

  Search scope: Adequate. Concepts searched: provenance metadata for
    verification claims; W3C PROV and data lineage; audit trails recording the
    producing tool; decision provenance and accountability; retraction
    propagation and continued citation of retracted work; silent data
    corruption and blast-radius enumeration without provenance.
