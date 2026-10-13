SEARCH-FOR-PRESUMPTION-1119:
  Date searched: 2026-10-10
  Original item: PRESUMPTION-1119
  Original statement: The orchestrator normalises agent outputs after the fact (relabelling 15c's "CLOSED" to
    INCORPORATE; adding a PROVENANCE block 15b omitted) while reporting agents' work as independent. Question: Does
    post-hoc normalisation of independent reviewers' outputs bias the record, and how should it be reported?

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1119
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from orchestrator edits to 15b/15c outputs (label remapping; inserted PROVENANCE block) that were
        not disclosed when the outputs were reported as independent; queued 2026-10-09
      15a (2026-10-10): 3 web searches, 1 fetch (succeeded, abstract). Found support that undisclosed changes mislead
        readers and should be reported explicitly (Willroth & Atherton 2024 on preregistration deviations). Found
        precedent in reliability methodology for reporting independent (pre-reconciliation) and post-reconciliation
        agreement separately. W3C PROV offers a standard vocabulary for recording revisions and the agent responsible.
        No source specifically on an orchestrator editing AI reviewers' outputs.
    Current status: SUPPORTED (Moderate)

  Search scope: PRELIMINARY. 3 web searches: (a) inter-rater reliability reported before vs after consensus discussion;
    (b) reporting deviations from preregistration; (c) data provenance raw vs cleaned / W3C PROV revisions. 1 fetch:
    APS page for Willroth & Atherton 2024 (succeeded; abstract only, full text behind login).

  Supporting evidence found: Yes (Moderate)

  Sources:
    1. Willroth, E.C. & Atherton, O.E., 2024. "Best Laid Plans: A Guide to Reporting Preregistration Deviations."
       Advances in Methods and Practices in Psychological Science 7(1). DOI 10.1177/25152459231213802. [fetched,
       abstract] Preregistration keeps its value despite deviations "as long as those deviations are well documented and
       transparently reported". Most deviations "go unreported or are reported in unsystematic ways". The paper proposes
       a standardized reporting framework. Relevance: closest analogue. The task spec / agent output is the registered
       plan, and orchestrator normalisation is a deviation that must be itemised.
    2. Analyses of preregistered studies, e.g. Claesen et al. (Psychological Science Preregistered-badge articles
       2015–2017). [search-result; authorship and details not verified] Many studies deviated and several disclosed none.
       Undisclosed deviations give readers the incorrect impression that the study ran as planned. Relevance: empirical
       precedent that undisclosed post-hoc change biases the record.
    3. Inter-rater reliability practice: Cochrane Handbook v5.1 §7.6.5 "Reliability and reaching consensus"
       [search-result]; O'Connor/Joffe-style team coding reports and arXiv examples (2107.11449 grounded theory IRR in
       SE; 2604.21870) [search-result]. Reliability is computed on independent ratings BEFORE discussion, then consensus
       is reported separately. Several sources say the reconciliation procedure itself must be described. Relevance:
       direct methodological analogue for a pre/post normalisation report. Agreement measured after an editor
       harmonises labels overstates independent agreement.
    4. W3C PROV-DM / PROV-O (W3C Recommendation 2013; PROV Primer). [search-result] Provides wasRevisionOf,
       wasDerivedFrom and wasAttributedTo to link a revised entity to its original and to the responsible agent.
       Relevance: an existing standard for recording "15b output → orchestrator revision" without overwriting the
       original. Related arXiv work (2310.18079) notes that cleaned data can become "less traceable" when changed values
       are not recorded.

  Strength of support: Moderate. The transparency principle is well supported in open-science and reliability
    methodology. One anchor was fetched at abstract level; the rest are search results. Transfer to orchestrator edits
    of AI-agent outputs is by analogy.

  Summary: Open-science methodology holds that pre-specified processes keep their evidential value under deviation only
    if each deviation is documented, and audits show that undisclosed deviations are common and mislead readers. In
    multi-rater work the established practice is to report independent (pre-reconciliation) agreement separately from
    post-consensus results and to describe the reconciliation step. Otherwise harmonisation inflates apparent
    independence. Provenance standards (W3C PROV) provide a ready vocabulary for keeping the raw output and the
    normalised revision linked and attributed. Together these support the proposed practice: preserve raw agent output,
    record each normalisation as an attributed revision, and report pre- and post-normalisation states.

  Transfer caveats: (i) Some normalisations (formatting, adding a missing boilerplate PROVENANCE block) may be
    content-neutral. The literature targets substantive deviations, so a materiality threshold is a design choice not
    settled by these sources. (ii) Relabelling "CLOSED" to INCORPORATE is a semantic mapping and falls on the
    substantive side. (iii) Preregistration sources are psychology-focused. (iv) No source on automated orchestrators
    editing AI reviewer outputs was found.

  NOVELTY flag: partial. Transparency about post-hoc edits is established. Applying it to an orchestrator normalising
    nominally independent AI agents' outputs was not found in this preliminary search.

  Recommendation: SUPPORTED (Moderate). Preliminary search; broader search recommended (editorial intervention in peer
    review / systematic-review data extraction; outcome-switching literature, e.g. COMPare).
