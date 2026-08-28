SEARCH-FOR-PRESUMPTION-886:
  Date searched: 2026-08-28
  Original item: PRESUMPTION-886
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority High)
  Original statement: [inferred] That a single-valued approval token adequately records a curation
    decision — that endorsement and non-objection need not be distinguished, and that provenance and
    confidence need not travel with the item.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-886
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the schema — the question was asked in prose on the same day the data was written
        without it; DECISION-083 used as internal control.
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND (for the presumption); the richer schema is documented practice

  Search scope: WebSearch, 2026-08-28, one dedicated query on provenance metadata, confidence annotation
    and curation approval records. Literature reached: the IPAW proceedings volume "Provenance and
    Annotation of Data and Processes"; a CEUR workshop paper on reconstructing provenance for automatic
    annotation; a 2026 arXiv paper defining a verified imaging dataset standard (2604.17525); a US patent on
    curation systems with workflow-state version control; the arXiv paper on broken data authenticity,
    consent and provenance for AI (2404.12691). NOT COVERED and material: the W3C PROV recommendation in
    primary form, which is the standard this whole area is built on and which I should have gone to first;
    and the editorial-peer-review literature on reviewer-confidence scores, which is the closest analogue to
    endorsement-vs-non-objection. All sources SNIPPET-ONLY. Search confidence: LOW-MODERATE.

  Supporting evidence found: No

  Sources:
    1. Anon., "VIDS: A Verified Imaging Dataset Standard for Medical AI" (arXiv:2604.17525) [SNIPPET-ONLY;
       authors unverified] — Specifies a Provenance object containing Annotator, AnnotationProcess and a
       QualityControl block carrying reviewer identity, review date, outcome (approved / revisions /
       rejected) *and a confidence score*. This is the multi-valued token the presumption assumes is
       unnecessary, specified as a standard.
    2. Anon., "Data Authenticity, Consent, & Provenance for AI are all broken: what will it take to fix
       them?" (arXiv:2404.12691) [SNIPPET-ONLY; authors unverified] — Argues that without standardised
       documentation attached to data as it travels, downstream tracking becomes unfeasible; i.e. the
       travelling requirement the presumption drops is the field's stated precondition.
    3. NHIMG glossary, "Provenance metadata" [SNIPPET-ONLY] https://nhimg.org/glossary/provenance-metadata/ ;
       Springer, "Metadata and Provenance Management" (ResearchGate record 45917763) [SNIPPET-ONLY] —
       Treat provenance as multi-dimensional metadata from which the *confidence* of data is derived, rather
       than as a boolean.

  Strength of support: None

  Summary: No source was found that endorses recording a curation decision as a single approval value. The
    documented standards go the other way, and they do so specifically on the two points the presumption
    elides: outcome is recorded as a graded value alongside reviewer identity and a confidence score, and
    the record is required to travel with the item rather than sit in a header. The distinction the
    presumption collapses — endorsement versus non-objection — was not found named in those terms anywhere,
    which is the one place this item may be doing original work; but the more general requirement it
    depends on is standard practice, so a novelty flag would overstate the case.

  Caveats: The corpus reached is thin and skewed to recent preprints; the W3C PROV standard, which is where
    this claim would be settled, was not read. The medical-imaging standard's transfer to a philosophical
    wiki's approval gate is assumed.

  NOVELTY-FLAG (partial):
    Item: PRESUMPTION-886
    Searched: provenance/annotation standards, curation approval schemas, confidence annotation.
    Finding: the general requirement (graded, travelling, confidence-bearing provenance) is well established;
      the specific distinction between *endorsement* and *non-objection* as separate approval states was not
      found in the literature reached.
    Implication: possible small original contribution in the vocabulary, not in the underlying requirement.
    Recommended status: partial NOVEL — flagged weakly, on a LOW-MODERATE-confidence search.

  Recommendation: NO-SUPPORT-FOUND
