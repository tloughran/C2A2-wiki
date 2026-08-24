# SYSTEMIC-RISK-FLAG — 2026-08-15

Raised by Agent 15b from the 2026-08-14 assumption intake (ASSUMPTION-1068, 1069, 1070, 1075, 1077).
One axis, Critical. Raised without reference to 15a, per the blinding design.

PROVENANCE:
  Origin: 14a (intake 2026-08-14, ASSUMPTION-1068/1069/1070/1075/1077)
  Chain: [14a -> 15b]
  Item type: ASSUMPTION (stated)
  Transform at each step:
    14a: Queued five assumptions for literature testing; ASSUMPTION-1077 marked HIGH PRIORITY.
    15b: Searched challenging literature on each independently; raised this flag from the convergence of
         four of the five, none of which shows it alone.
  Current status: FLAGGED — bears directly on REVISE-326 (HIGH), which this file recommends holding.

================================================================================
## AXIS 1 — CRITICAL
### Every proposed instrument samples a frame the audited process generates

  Affected items: ASSUMPTION-1068, ASSUMPTION-1069, ASSUMPTION-1075, ASSUMPTION-1077 (primary);
                  ASSUMPTION-1070 (secondary)
  Risk level: CRITICAL

  Four of the five items in this intake propose, or point at, an instrument. In every case the
  instrument's sampling frame is produced by the same process the instrument is meant to audit:

    1068 — the stall detector runs on the same launchd, the same machine, the same MCP surface as the
           runs it watches. It can only report on a window in which it itself survived.
    1069 — counting deliverables counts the runs that survived to produce deliverables. The nine runs
           that produced nothing are, by construction, absent from the population being counted.
    1075 — a silently skipped check removes its pair from the checked population AND reports success.
           Every pass rate the fleet publishes is computed over the pairs where the checker worked.
    1077 — the override rate is computed over exactly the items an upstream escalation rule routed to
           the human. It measures the routing rule's calibration, not the review gate's value.

  These are the same defect four times, and NO SINGLE FILE SHOWS IT. Each item, read alone, looks like a
  local instrumentation gap with a local fix. Read together they are one structural fact: the fleet has
  no measurement whose denominator is sourced from outside the thing being measured.

  LITERATURE BASIS:

    PCAOB AU 350 / AS 2315, Audit Sampling [verified this run via pcaobus.org] states the disqualifying
    condition in one sentence, and it is a sentence about C2A2: "An auditor would NOT be able to detect
    understatements of an account due to OMITTED ITEMS by sampling the RECORDED items. An appropriate
    sampling plan for detecting such understatements would involve selecting from a source in which the
    omitted items are included." The standard's general requirement is the same rule stated positively:
    "the auditor should determine that the population from which he draws the sample is appropriate for
    the specific audit objective."

    Priest & Klein (1984), "The Selection of Disputes for Litigation" [verified this run, snippet level;
    primary not read] — outcome rates over an adjudicated set are governed by the selection process, not
    by the underlying population. The acknowledged corollary in the appellate literature: "reversal rate
    is an imperfect proxy for quality."

    Wilson et al. (2026), "Alert fatigue measurement in clinical decision support: a systematic review"
    [verified this run, abstract level] — raw override rate is an inadequate operationalisation; what
    matters is whether each override was APPROPRIATE, which requires case-by-case adjudication. This is
    why ASSUMPTION-1077's measurement is not attendance-free: it is attendance-DEFERRED.

    LOPA / CCPS independent-protection-layer criteria [verified this run, snippet level] — where common
    cause affects two layers, credit only one. A watcher on the watched plane is not a second layer.

  COUPLING TO THE 2026-08-14 FLAG: last cycle's Axis 1 found that the escape from self-assessment
  requires an external ASSESSOR the fleet does not have. This axis is the same structure one level down,
  in measurement rather than in assurance: the escape from self-measurement requires an external FRAME,
  and the fleet does not have one either. The two are the same problem in argument form and in
  instrument form, and both terminate the same way — by leaving the system, not by ascending within it.

  RECOMMENDATION:

    (a) No instrument in this group should be built, and REVISE-326 should not be actioned, until its
        sampling frame is stated and shown to originate outside the audited process.

    (b) Two qualifying frames already exist and cost almost nothing:
        - The LAUNCHD SCHEDULE, for 1068 and 1069 — the declared set of runs that should have occurred,
          authored before the fact and independently of whether any of them ran. Reconciling against the
          schedule rather than against outputs repairs the frame for both items in one change.
        - SEEDED DEFECTS, for 1077 — items of known status injected at a known rate, giving the review
          gate a detection rate rather than an agreement rate. Without this, no override statistic has a
          denominator that means anything, and the low-override regime is precisely where chance-corrected
          agreement statistics become uninformative (Feinstein & Cicchetti 1990).

    (c) For 1075 the equivalent is a DENOMINATOR: report checks-executed alongside checks-passed. A pass
        rate without a checks-executed count is a statement about the checker's uptime, not the corpus.

    (d) Whatever is built, it must publish its frame and its denominator on the face of every report. The
        fleet's current instruments publish numerators only, which is why four independent items had to
        rediscover the same defect separately.

  FULL RESULTS:
    architecture/lit_search_results/against/ASSUMPTION-1068_against.md
    architecture/lit_search_results/against/ASSUMPTION-1069_against.md
    architecture/lit_search_results/against/ASSUMPTION-1075_against.md
    architecture/lit_search_results/against/ASSUMPTION-1077_against.md
    architecture/lit_search_results/against/ASSUMPTION-1070_against.md  (secondary — the escalation
      superseded before review is an item already in 1077's override denominator with nothing marking it)
