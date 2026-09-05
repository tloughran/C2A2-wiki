SEARCH-FOR-PRESUMPTION-910:
  Date searched: 2026-09-05
  Original item: PRESUMPTION-910
  Original statement: [inferred] "Does the outline hold" has a recognisable answer when Tom reads the
    reordered document — a human read of 16,102 lines will detect misplacement without a stated criterion
    for what misplacement looks like.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-910
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a success-criteria gap in the digest's hand-off. Paired with ASSUMPTION-1256.
      15a: Searched for supporting literature (2026-09-05), jointly with ASSUMPTION-1256. NOTE ON
        AUTHORSHIP: run by the 15c orchestrating context after the delegated 15a subagent was interrupted;
        written BEFORE any 15b search for this item was begun in the same context.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. "Don't overthink it: The paradoxical nature of expertise for the detection of errors in conceptual
       business process models," Frontiers in Neuroscience 2022, doi 10.3389/fnins.2022.982764, PMC9731113
       [VERIFIED: title/journal/DOI/PMC; author list NOT verified] — Eye-tracking study, 75 BPMN models,
       experts vs novices, semantic and syntactic errors, no checklist. Experts correctly identified more
       error-free models than novices. Supports that domain expertise alone yields a detection advantage
       without a stated criterion. (Its second finding — experts also produce more false positives — is
       counter-evidence and is recorded in Caveats.)
    2. "An Expert Schema for Evaluating Large Language Model Errors in Scholarly Question-Answering
       Systems," arXiv:2602.21059 [VERIFIED: title/ID; authors NOT verified] — Domain experts recognise
       error classes that require deep knowledge (chronology, causal misattribution, reversed sequences)
       and expert evaluation captures implicit quality criteria that were never written down. Directly
       supports the presumption's mechanism: the criterion exists tacitly in the expert.
    3. SmartBear / Cisco code-review study [VERIFIED: smartbear.com summary; primary report NOT retrieved]
       — 70–90% defect discovery by unaided human reviewers within the 200–400 LOC / 60–90 minute window.
       Supports detection-without-checklist AT BOUNDED SIZE.
    4. "An Empirical Comparative Study of Checklist based and Ad Hoc Code Reading Techniques in a
       Distributed Groupware Environment," arXiv:0909.4260 [VERIFIED: title/ID; authors NOT verified] —
       Located but abstract not read in this search; the checklist-vs-ad-hoc reading literature it belongs
       to has historically found ad hoc reading competitive with checklists for experienced readers.
       Cited as a pointer, NOT as a verified result.

  Strength of support: Weak-to-Moderate

  Summary: There is real support for the mechanism the presumption relies on — experts detect
  domain-specific errors using tacit criteria they cannot state, and the author of a corpus is the
  strongest available expert on it. There is no support for the scale. Every supportive result is
  measured on units of tens to a few hundred lines within a single sitting; none extends to a 16,102-line
  read, and the same sources report detection falling off steeply beyond that window. The most on-point
  study also finds that expertise raises false positives alongside true detections, which for a
  "does the outline hold" question means the read may report misplacements that are not there.

  Caveats: (a) The Frontiers 2022 result is double-edged: expert advantage on error-free models, but more
  false-positive defects. (b) The expert-schema paper is about LLM-answer errors, not document-structure
  errors; transfer by analogy. (c) No source addresses self-review of one's own reorganised material.
  (d) Search scope: preliminary — 4 queries shared with ASSUMPTION-1256; the checklist-vs-ad-hoc
  inspection literature (Basili/Porter-era) and the systematic-review single-screener recall literature
  were not covered and would sharpen this.

  Recommendation: PARTIALLY-SUPPORTED
