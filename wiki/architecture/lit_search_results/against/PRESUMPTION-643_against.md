SEARCH-AGAINST-PRESUMPTION-643:
  Date searched: 2026-08-03
  Original item: PRESUMPTION-643
  Original statement: That a high near-miss rate with a zero incident rate indicates a
    working control.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-643
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from six instances with no repeating catch mechanism
           (origin ASSUMPTION-668, ASSUMPTION-643)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. NIOSH Hierarchy of Controls — Eliminate > Substitute > Engineer > Administrative >
       PPE. A catch depending on a person noticing is administrative or below and is
       classified weak *by its position*, independent of its historical catch record.
    2. Bird, F.E. — 1.7M accident reports, ~300 companies: serious accidents are preceded
       by many lower-consequence incidents and near misses. Near misses are precursors.
    3. EHS Insight, "Near Miss Reporting and Investigation" — near misses are leading
       indicators giving "an early read on where controls, training, or supervision may
       be failing before a serious injury happens." The reading is of failure, not health.
    4. Learning from Workers' Near-miss Reports, 2020. Mining, Metallurgy & Exploration
       10.1007/s42461-020-00206-9 — near misses share underlying causes with accidents.
    5. IJSRP, "The role of Near-Miss Management in Reducing Major Accidents" — the value
       of near-miss data is that it precedes the accident, which presupposes the accident
       is coming.

  Strength of challenge: Strong

  Summary: The safety literature inverts the presumption. A near miss is defined as an
  event in which the harm did not occur *this time*; the entire field collects them
  because they forecast the occasion when it does. A zero incident count alongside a high
  near-miss count is the canonical description of an unprotected system with a good run,
  not of a protected one. The hierarchy-of-controls adds an independent argument that does
  not depend on counting at all: a control is graded by its position, and person-dependent
  catches sit near the bottom. C2A2's specific configuration is worse than the generic
  case, because the six catches used six *different* accidental mechanisms — meaning there
  is no control whose reliability could even be estimated, only six coincidences.

  Specific risks: Six recorded instances, six different accidental catch mechanisms, and
  the named failure mode injects false defects into another subsystem's input. Because the
  zero incident count is currently read as evidence of health, the system has no trigger
  to install a real control — the metric that should be alarming is the one being cited as
  reassurance. Each further near miss caught by accident strengthens the false inference.

  Mitigations available: Yes, and the hierarchy names them in order. (i) Eliminate: remove
  the path by which false defects can reach the downstream subsystem's input. (ii) Engineer:
  add a mechanical gate — a validation step that fails loud — so the catch does not depend
  on anyone noticing. (iii) At minimum, instrument: record catch mechanism per instance and
  publish the count of *distinct* mechanisms, which makes "no control, only luck" visible.
  (iv) Track near-miss rate as a leading indicator with a threshold that triggers action,
  which is the literature's standard use of the data.

  Recommendation: CHALLENGED

  RELATION TO TODAY'S SYSTEMIC-RISK-FLAG (per 14b's instruction): checked. The 2026-08-02
  flag's Cluster A cites the same hierarchy-of-controls sources but addresses a different
  claim — documentation substituting for execution. It neighbours this item; it does not
  answer it. This item concerns the inferential validity of a zero incident count, which
  Cluster A does not treat. No redundancy, and the shared source base is evidence of a
  recurring root rather than of duplication.

  STEELMAN:
    Item: PRESUMPTION-643
    Strongest counterargument: The inference "no incidents, therefore the control works"
    requires that incidents would have occurred had the control failed. But a near miss is
    by definition an occasion when the control *did* fail and something else intervened.
    Six near misses is therefore six control failures, and the zero incident count measures
    the intervening luck, not the control. That the six were caught by six different
    accidental mechanisms is decisive: a control has a mechanism, and a mechanism that is
    different every time is not a mechanism. The reasoning error is survivorship in its
    purest form — the system is inferring the strength of a barrier from the absence of the
    events the barrier was supposed to stop, on a sample where every observation is a case
    of the barrier not stopping them.
    What would need to be true for C2A2 to be safe: that a single, named, repeatable
    mechanism catches these cases, and that it sits above the administrative tier — i.e.
    it does not depend on a person or an agent happening to look.
    How to test: enumerate the six instances and record, for each, the catch mechanism.
    If the count of distinct mechanisms equals the count of instances, there is no control.
    This is an in-house query and can be run today.
