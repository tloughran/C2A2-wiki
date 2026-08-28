SEARCH-AGAINST-PRESUMPTION-885:
  Date searched: 2026-08-28
  Original item: PRESUMPTION-885
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority High)
  Original statement: [inferred] That draining a backlog by hand changes time-to-disposition rather than
    resetting it; and that the availability of a manual clearance does not suppress investment in a
    structural remedy.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-885
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from absent alternatives across the day's outputs; checked against PRESUMPTION-883 and
        PRESUMPTION-875 for non-duplication.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED — note: this direction challenges the *for* direction's finding,
      which is unusual and is flagged rather than smoothed

  Search scope: WebSearch, 2026-08-28, one dedicated query on whether backlog clearance and surge capacity
    durably improve throughput. Reached: InfoQ's queue-recovery capacity-planning article; oxmaint
    maintenance-backlog guidance; prebenormen on backlog reduction; arXiv 2605.19139 (hospital queue
    simulation); LeSS on flow and queueing theory. NOT COVERED and material: any critique of Repenning &
    Sterman's capability-trap model, which is what a symmetric challenge would require and which I did not
    find; the absence is stated rather than filled with a substitute. All SNIPPET-ONLY. Confidence: LOW-MODERATE.

  Challenging evidence found: Partial

  Sources:
    1. InfoQ, "The Mathematics of Backlogs: Capacity Planning for Queue Recovery" [SNIPPET-ONLY]
       https://www.infoq.com/articles/capacity-planning-queue-recovery/ — Treats queue recovery as a solvable
       capacity-planning exercise: a temporary excess of service over arrival clears a backlog and, if the
       steady-state service rate exceeds arrival, does not recur. The presumption's "reset, not change" is
       therefore conditional on the steady-state relation, not automatic.
    2. oxmaint, "How to Reduce Maintenance Backlog in Large Commercial Buildings" [SNIPPET-ONLY]
       https://oxmaint.com/industries/facility-management/how-to-reduce-maintenance-backlog-in-large-commercial-buildings —
       Reports 15–25% labour-capacity recovery from criticality-based prioritisation plus PM optimisation,
       with temporary contractor surges supplementing without permanent cost. Documented case where a
       clearance-plus-triage intervention changed the generating process rather than resetting an observable.
    3. Anon. (2026), "Reducing Waiting Time for Medical Tourists Through Hybrid Agent-Based and
       Discrete-Event Simulation" (arXiv:2605.19139) [SNIPPET-ONLY; authors unverified] — Capacity expansion
       identified as the clearest high-impact lever, i.e. the structural remedy is reachable and known, not
       foreclosed by the availability of the manual one.

  Strength of challenge: Weak-Moderate

  Summary: The challenge is narrow and honest about being so. The capability-trap mechanism the for
    direction found is a strong and well-identified result, and I found no critique of it. What the against
    corpus supplies is a boundary condition: a manual clearance *accompanied by a change to triage or
    capacity* is a different intervention from a bare drain, and in facilities and healthcare settings the
    combined intervention is documented as producing durable improvement. The presumption is therefore
    challenged only in the case where the clearance was bundled with an admission or prioritisation change —
    and whether this one was is an in-house fact this direction cannot establish. The suppression conjunct
    is not challenged at all; nothing found suggests that having a manual remedy available leaves structural
    investment unaffected.

  Specific risks: If the estate accepts the capability-trap reading unconditionally it may decline a
    clearance that would in fact help, on the grounds that clearances never help. The larger risk runs the
    other way and this direction should say so: with the suppression conjunct unchallenged, the default
    expectation is that the manual drain will be repeated instead of the gate being fixed.

  Mitigations available: Bundle any future clearance with one admission-side change, so the intervention is
    testable as more than a reset. Record which was done.

  STEELMAN:
    Item: PRESUMPTION-885
    Strongest counterargument: A one-person estate is not a factory. The capability trap is a model of an
      organisation that *could* invest in capability and chooses firefighting; where the constraint is a
      single human's availability, there is no alternative allocation to be crowded out, so the suppression
      mechanism has nothing to bite on. Clearing the queue by hand may simply be what the only available
      server can do, and calling it a trap imports an organisational structure the estate does not have.
    What would need to be true for C2A2 to be safe: there would have to be no cheap structural remedy that
      was passed over — i.e. the admission-control change would have to be genuinely unavailable rather than
      merely unbuilt.
    How to test: ask what admission-side change was considered at the time of the 08-27 clearance. If none
      was, the suppression conjunct is supported in-house and no literature is needed; if one was considered
      and rejected on cost, the steelman holds and the item should be re-framed.

  Recommendation: PARTIALLY-CHALLENGED
