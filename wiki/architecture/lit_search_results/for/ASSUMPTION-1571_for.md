SEARCH-FOR-ASSUMPTION-1571:
  Date searched: 2026-09-21
  Original item: ASSUMPTION-1571
  Original statement: Staleness-based downgrading selects for defective items -- 8 of 9 searched items
    from the downgraded cohorts went to REVISE, 1 stayed open, 0 confirmed -- and therefore slows the
    clock on exactly the items most in need of it.

  **Execution note (recorded for honesty, not buried):** this run of 15a and 15b was executed by a
  single scheduled process (`c2a2-lit-search-pipeline`, 2026-09-21). The two directions were run as
  separately-framed query sets and the FOR files were written before any AGAINST query was issued, but
  the strict independence the spec assumes (two processes, neither seeing the other) was NOT achieved.
  Read the strength ratings with that caveat.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-1571
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-09-20 15d weekly cycle.
      15a: Searched for supporting literature on queue-discipline inversion and defect aging.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Defect-aging practice literature (QA/defect-triage bodies of practice; e.g. Bugasura, "Defect
       Aging Explained: What Stale Bugs Mean for QA"; Bug0 defect-triage knowledge base). — States the
       supporting half directly: older unresolved issues, particularly in critical modules, *indicate
       hidden instability* rather than low importance, and time-in-queue-by-severity is tracked as "the
       early sign that triage is slipping." This is the claim's core correlation, treated as received
       practice.
    2. Maintenance-backlog triage practice (oxmaint manufacturing-plant triage checklist). — Encodes the
       same correlation as an operating rule: work over 30 days on high-criticality assets requires
       *immediate* review because "aging work on high-criticality equipment compounds failure risk with
       every passing week." Age is treated as a reason to escalate, not to defer — the exact inversion
       14a is alleging.
    3. Under-triage literature in emergency medicine (systematic review of prehospital under-triage in
       older trauma patients, PMC8463357; PMC4143318). — The best-studied real-world case of a triage
       system systematically *under*-prioritising a population that turns out to have worse outcomes.
       It supplies the mechanism-level analogue: triage criteria tuned on a general population
       mis-sort a subpopulation whose risk the criteria do not measure.

  Strength of support: Moderate

  Summary: Two independent practice literatures — software defect triage and asset maintenance — treat
    item age as a *positive* indicator of latent defect and build escalation rules on that basis, which
    is the correlation 14a asserts. Emergency-medicine under-triage research supplies a validated case
    where a triage rule systematically deprioritised the higher-risk group. So the claim's general shape
    is supported by practice consensus and by one well-studied analogue.

  Caveats: The supporting sources are practitioner literature and one out-of-domain clinical analogue,
    not primary research on aging-based deprioritisation in review queues. More seriously, the in-house
    evidence offered (8 of 9 to REVISE) is a sample of the *searched* items only, and items get searched
    non-randomly — this is a selection-on-the-dependent-variable risk that the supporting literature
    does not touch. The claim about the estate's own queue is in-house testable and that test, not this
    search, should carry the weight. Preliminary search.

  Recommendation: PARTIALLY-SUPPORTED
