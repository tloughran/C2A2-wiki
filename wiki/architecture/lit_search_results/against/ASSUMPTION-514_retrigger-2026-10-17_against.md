SEARCH-AGAINST-ASSUMPTION-514 (RE-TRIGGER cycle 1):
  Date searched: 2026-10-17
  Original item: ASSUMPTION-514
  Original statement: Any self-measurement of the pipeline's completeness/accuracy must cite an
    external referent/seeded denominator or be reported UNCALIBRATED.
  Under test this cycle (MONITOR-473, High; subordinate to PREMISE-124): limits of seeded-fault and
    capture-recapture estimation (seeded faults unrepresentative; independence violations) and
    cases where internal consistency checks are adequate. Cycle 0 challenged from the other side
    (rule too strict); this cycle tests whether the rule's remedy — a seeded denominator — is
    itself sufficient for "calibrated".

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read lit_search_results/for/, any *_for file, or 15a
    sections of lit_search_returns.md. I read only my own cycle-0 file for this item.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: ASSUMPTION-514
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from PREMISE-124 report.
      15a (cycle 0): independent; not read by this agent
      15b (cycle 0, 2026-07-24): PARTIALLY-CHALLENGED (Weak-Moderate) — rule slightly too strict;
        "external" should mean "independent of the measured quantity". Note: cycle-0 sources were
        cited without read-depth marks and appear to be background knowledge — UNVERIFIED.
      15c: disposition → MONITOR-473 (High).
      15d: re-trigger, cycle 0 → 1.
      15b (cycle 1, 2026-10-17): 2 searches (error-seeding limitations; capture-recapture
        independence in inspections); 1 fetch (NASA NTRS record, abstract read in full).
        Shared with the systemic search on shared-fate referents (see SYSTEMIC-RISK flag).
    Current status: PARTIALLY-CHALLENGED
    Sources this cycle: Knight & Ammann 1985 [abstract]; Chun 2006 [snippet]; Thelin et al. 2002
      [snippet]; Lloyd, Yip & Chan 1999 [title only].
    Date: 2026-10-17

  EVIDENCE GRADE: PRELIMINARY. One empirical study at abstract depth; others search-result only.

  Challenging evidence found: Partial — against the sufficiency of the remedy, not the norm.

  Sources:
    1. Knight, J. C. & Ammann, P. E. (1985). "An experimental evaluation of error seeding as a
       program validation technique." Proc. Tenth Annual Software Engineering Workshop, NASA GSFC.
       NTRS 19860020890. https://ntrs.nasa.gov/citations/19860020890 [abstract — read in full]
       408 programs (17 independent versions x seeded errors). Seeded and indigenous errors were
       "approximately equally difficult to locate" overall, BUT "the assumption that, for each type
       of error, all errors are equally difficult to locate was not borne out", and "since a
       seeded error occasionally corrected an indigenous error, the assumption that errors do not
       interfere with each other was proven wrong." Authors: seeding "can be made useful by taking
       these results into account in modifying the underlying model." Bearing: a seeded
       denominator is calibrated only under assumptions (equal detectability within type;
       non-interference) that the one controlled test found partly false. Citing a seeded
       denominator does not by itself make an estimate calibrated.
    2. Chun, Y. H. (2006). "Estimating the number of undetected software errors via the correlated
       capture-recapture model." European Journal of Operational Research. [snippet] Standard
       capture-recapture assumes independent inspectors; a correlated model outperformed
       independence-based models in numerical analysis. Bearing: in C2A2 the "inspectors" (agents
       checking completeness) share prompts, models and the same wiki — positive dependence that
       would shrink the estimated undiscovered population (biased toward overstating completeness;
       direction inferred, not stated in the snippet).
    3. Thelin, T., Petersson, H., Runeson, P. & Wohlin, C. (2002) — re-analysis of inspection
       experiment for behavioural heterogeneity. [snippet; exact title not verified] Proposes
       behavioural models as a diagnostic for violated inspector independence. Bearing: the
       independence assumption is routinely suspect and should be tested, not assumed.
    4. Lloyd, C. J., Yip, P. S. F. & Chan, K. S. (1999). "Estimating the number of faults:
       efficiency of removal, recapture, and seeding." [title only] Comparative efficiency of
       seeding vs recapture designs; conclusions not retrieved.

  Not found: any source showing internal consistency checks alone are adequate for completeness
    estimation. Cycle 0's metacognition/cross-validation points remain unverified background.

  Strength of challenge: Moderate (up from Weak-Moderate) — directed at the remedy, not the norm.

  Summary: Nothing found weakens the core norm that an uncalibrated self-measurement must be
    labelled as such. The challenge is that the prescribed escape — "cite a seeded denominator" —
    is itself a model with assumptions that controlled work found partly false: seeded faults are
    not uniformly representative within type, and they interact with real faults. Capture-
    recapture versions rest on inspector independence, which is implausible for agents sharing a
    model and a corpus, and dependence biases the estimate. So the binary CALIBRATED/UNCALIBRATED
    split is too coarse: a seeded-denominator estimate is "calibrated under stated assumptions".

  Specific risks: PREMISE-124's audit trail shows a seeded denominator and the completeness figure
    is accepted as calibrated, while seeds are easier (or harder) to find than real gaps, or the
    finders and the seeder share blind spots. Completeness is overstated with an apparent external
    warrant — worse than an honest UNCALIBRATED.

  Mitigations available: require each seeded-denominator claim to state (a) who/what seeded, and
    that the seeder is not the measured pipeline; (b) seed-type mix vs expected real-gap mix; (c)
    an independence note for the finders; and report as "CALIBRATED-CONDITIONAL" when any is
    missing. Periodically compare seeded-recovery rate with a sample of real gaps found later.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-514
  Strongest counterargument: The rule treats a seeded denominator as the cure for self-measurement,
    but seeding is self-measurement with one more assumption. The only controlled test located
    found seeded errors differ in detectability within type and sometimes mask real errors; the
    capture-recapture literature treats inspector independence as the assumption most likely to
    fail. In a system where the seeder, the finders and the measured pipeline are all the same
    family of agents over the same wiki, the "external" referent shares fate with what it
    measures. The rule then licenses false confidence it was written to prevent.
  What would need to be true for C2A2 to be safe: seeds are planted by a process independent of
    the pipeline (ideally Tom or a different tool), span the real gap types, and seeded recovery is
    periodically checked against real gaps discovered later.
  How to test: plant two seed sets — one agent-generated, one human-generated — and compare
    recovery rates. A material gap means agent-seeded denominators are not independent referents.

  Search scope: preliminary — 2 searches, 1 fetch (abstract). Full text of Knight & Ammann not read.
