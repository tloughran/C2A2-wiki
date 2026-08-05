SEARCH-FOR-PRESUMPTION-653:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-653
  Original statement: That two different figures for one quantity constitute a
    reconciliation problem rather than evidence that no agent owns the
    quantity — ten figures for five quantities in a single day, answered by
    declaration and by institutionalising the disagreement.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-653
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 observation of ten figures reported
        for five quantities, resolved by declaration rather than by assigning
        ownership
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Arya, A. & Fellingham, J., "Double Entry Bookkeeping and Error
       Correction" (Ohio State University). — The supporting strand:
       deliberately maintained redundant records are a recognised error-
       detection control. Because the two sides must agree, the system detects
       its own mistakes, and reconciliation is the designed mechanism rather
       than a symptom of disorder.
    2. Bank/ledger reconciliation practice literature (2026 accounting-control
       guidance). — Periodic reconciliation against an external authoritative
       statement reliably catches duplicates, omissions and drift. Note the
       load-bearing condition: an authoritative record exists and the
       reconciliation is scheduled.
    3. "Data Stewardship and Ownership: Best Practices," in Springer, 2024
       (doi:10.1007/978-3-031-67268-2_16); enterprise data-governance
       literature (Acceldata, Actian, OvalEdge, 2025-2026). — The counterweight:
       duplicate metric calculations arise when multiple teams compute the
       same quantity from different sources and logic, each correct in
       isolation; without a designated owner the definitions drift apart over
       time rather than converging.
    4. Master data management literature on data decay (Profisee, CluedIn,
       Maextro, 2025-2026). — States plainly that without assigned stewardship
       quality programmes decay, that the structural cause of duplication is
       the absence of a single source of truth, and that one-time cleanup
       without continuing ownership is followed by renewed divergence.
    5. Semantic-drift literature (AtScale, Syntaxia, 2025-2026). — Describes
       the mechanism by which metric meanings erode when definitions are
       introduced ad hoc under immediate need rather than designed up front.

  Strength of support: Weak

  Summary: The presumption gets genuine but narrow support. Accounting
    practice shows that maintaining two independently derived figures for one
    quantity can be a control rather than a defect — double-entry and bank
    reconciliation are exactly that design. What that literature also shows is
    the condition attached: one of the records must be authoritative, and the
    comparison must be a scheduled process with a defined resolution rule.
    Where those conditions are absent, the data-governance and MDM literature
    is consistent and unfavourable — unowned duplicate metrics diverge rather
    than converge, definitions drift, and cleanup without stewardship is
    followed by recurrence. Resolving by declaration supplies a value but not
    an owner, and so does not meet the condition under which the supportive
    literature applies. "Institutionalising the disagreement" finds no support
    at all: no located source treats a permanent unreconciled fork as an
    acceptable terminal state.

  Caveats: The accounting analogy transfers only where the two figures are
    genuinely independent derivations of the same defined quantity; if they
    are computed from different definitions, reconciliation is not even
    well-posed and the ownership reading is the correct one. Most governance
    sources are practitioner rather than peer-reviewed, and the decay figures
    quoted in that literature (e.g. contact-data decay rates) are vendor-
    sourced and should not be relied on quantitatively.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Adequate. Concepts searched: single source of truth and data
    reconciliation; whether unowned duplicate metrics converge or diverge;
    metric definition drift and semantic drift; data ownership and stewardship
    and their measured effect on quality; master data management and data
    decay; double-entry bookkeeping and redundancy as an error-detection
    control.
