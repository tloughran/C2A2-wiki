SEARCH-FOR-ASSUMPTION-1306:
  Date searched: 2026-09-11
  Original item: ASSUMPTION-1306
  Original statement: "A post-run sweep found the same defect in `arkanihamed`, `stump`, `loughran`,
    `macintyre` — all already logged as 'needing a human' on 2026-08-11. **It has now actually misfired
    once, so it stops being a tidiness note.**"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1306
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim. The defect was logged 2026-08-11 and is thirty days unruled; the
        manifestation moved it, not the elapsed time. Raised as OPEN-193; the "needing a human" queue's
        own status surfaced as PRESUMPTION-951.
      15a: Searched for supporting literature; found one strong, institutionally codified analogue
        (CISA KEV / exploitation-evidence prioritisation) that supports the stated rule directly, and one
        supporting mechanism (recurrence/defect-proneness) — against a substantial safety literature that
        runs the other way and which I record here rather than suppress.
    Current status: PARTIALLY-SUPPORTED

  Register pre-check: Bears on several ACTIVE premises, and one of them arguably ANSWERS it in the
    opposite direction.
    - PREMISE-202: "A HARM AVERTED BY CHANCE IS AN EVENT AND OPENS A RECORD; 'damage is nil, but by
      luck' is the criterion for OPENING an item, not for closing one." On the accident-precursor
      definition, the four un-repaired registers were already at full record-opening standing on
      2026-08-11. This is the single most relevant register hit and it undercuts the assumption's
      *converse* (that pre-manifestation it was merely a tidiness note) more than the assumption itself.
    - PREMISE-130: RECURRENCE RECLASSIFIES — prior fault count is the dominant predictor of future
      faults; a third failure in a component reclassifies to a defect class. Supports the assumption's
      direction.
    - PREMISE-128: a defect producing no error and plausible output cannot be certified benign from its
      visible outcome (silent data corruption). Cuts against.
    - PREMISE-193: repairing the named instance does not discharge the class; siblings remain untested
      until enumerated — which is precisely the disposition the run declined for the other four.
    - PREMISE-118: naming a defect in an instrument triggers a retrospective impact assessment.
    Searched anyway per OPEN-192.

  Supporting evidence found: Partial

  Sources:
    1. CISA Known Exploited Vulnerabilities (KEV) Catalog and BOD 22-01 (2021-, current). — SECONDARY
       (multiple independent retrieved descriptions; CISA primary page not fetched) — The single
       strongest support. KEV inclusion is triggered by *observed exploitation*, not by CVSS severity or
       vendor rating, and KEV entries carry mandatory remediation deadlines that severity-scored
       vulnerabilities do not. This is a national-scale, institutionally codified instance of exactly the
       assumption's rule: manifestation, not theoretical severity, sets priority. It is by far the best
       evidence found in the FOR direction.
    2. EPSS (Exploit Prediction Scoring System) / CVSS-vs-EPSS-vs-KEV prioritisation literature. —
       SECONDARY — The now-standard framing distinguishes theoretical severity (CVSS), predicted
       exploitation (EPSS), and confirmed exploitation (KEV), and places confirmed exploitation at the
       top of the remediation order. Supports the assumption as a *tie-break and ordering* rule under a
       capacity constraint, which is the form the run's decision actually took.
    3. Ostrand, Weyuker & Bell 2005; Hassan & Holt 2005 — defect-proneness / "faults cluster and recur in
       the same modules." — SECONDARY — Prior fault occurrence in a component is the dominant empirical
       predictor of future faults. A defect that has manifested is therefore Bayesian evidence of a
       higher future-manifestation rate for that component, which is a legitimate reason to raise
       priority. Already encoded as PREMISE-130.
    4. Institute of Medicine / National Academies, "Near-Miss Analysis," in Patient Safety: Achieving a
       New Standard for Care (2004), ch. 7. — SECONDARY (NAP and NCBI Bookshelf chapter retrieved via
       search snippets; full chapter not fetched) — Records the practice this assumption departs from:
       "consequence-driven approaches make the amount of attention and resources devoted to investigation
       directly proportional to the severity of the outcome," and names this as a recognised deficiency
       subject to hindsight bias. Retrieved in the FOR search and reported honestly: it is the principal
       counter-source and it is authoritative.
    5. Dillon & Tinsley, "The near-miss bias in decision making" / "How near-misses influence decision
       making under risk." — SECONDARY (abstract-level only; full text not retrieved) — Documents that
       decision-makers systematically *discount* near-misses, treating a lucky non-outcome as evidence of
       resilience. This is a description of the bias the assumption's rule would instantiate, not support
       for it.

  Strength of support: Moderate — and only for the narrow, capacity-constrained reading.

  Summary: The assumption splits into a defensible limb and an indefensible one, and the run's wording
    conflates them. Limb (a), "manifestation is legitimate evidence that raises posterior risk and may
    therefore reorder a queue under a capacity constraint," is strongly supported — the CISA KEV regime
    is a fully institutionalised version of it, and the defect-proneness literature supplies the
    mechanism. Limb (b), the stronger reading actually written — that before manifestation the item was
    merely "a tidiness note" and manifestation is what gives it standing — is not supported and is
    directly contradicted by the near-miss and accident-precursor literature, which exists precisely to
    deny that a non-manifested latent fault lacks standing. PREMISE-202 in this estate's own register
    already denies limb (b): a harm averted by chance opens a record. The honest reading of the day's
    events is that the defect had full standing on 2026-08-11 and the thirty-day delay is the finding,
    with manifestation supplying only the scheduling trigger.

  Caveats:
    - The KEV analogy carries a hidden asymmetry. KEV prioritises on exploitation *because the population
      of known vulnerabilities vastly exceeds remediation capacity* — it is explicitly a triage rule for
      a saturated queue, not an epistemology of standing. Transferring it to a four-item list where the
      fix is a one-line renumbering is a category error: there is no capacity constraint that the
      reordering relieves.
    - The assumption's rule, applied generally, is the textbook definition of outcome bias, and the
      safety literature's entire near-miss apparatus exists to suppress it. Anyone adopting this should
      adopt limb (a) only, and should write the exclusion for limb (b) explicitly.
    - The four un-repaired registers remain in the un-repaired state. Under PREMISE-193 the class is not
      discharged by the in-run repair of `hoffman`; under PREMISE-118 a retrospective impact assessment
      over appends made since 2026-08-11 is owed and was not done.
    - I did not retrieve CISA's primary BOD 22-01 text or the KEV methodology page; the characterisation
      is from multiple consistent secondary sources and should be treated as SECONDARY.

  Search scope: comprehensive search — near-miss reporting and prioritisation (patient safety, IOM/NAP,
    radiology near-miss analysis), outcome bias and near-miss bias in decision making, accident-precursor
    theory, latent-fault prioritisation, defect triage and defect-proneness prediction, and
    vulnerability-management prioritisation (CVSS / EPSS / CISA KEV).

  Recommendation: PARTIALLY-SUPPORTED — recommendation rests on limb (a) only (manifestation as a
    legitimate posterior-risk update and queue-reordering trigger under capacity constraint). Limb (b)
    (no standing before manifestation) is NO-SUPPORT-FOUND and is contradicted both by the retrieved
    literature and by this register's own PREMISE-202.
