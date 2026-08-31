SEARCH-AGAINST-PRESUMPTION-893:
  Date searched: 2026-08-31
  Original item: PRESUMPTION-893
  Original statement: [inferred] A remedy at one-snapshot-per-run granularity is sufficient, no
    recovery-point objective being held.
  Generalizable limb searched: Whether a protection interval chosen by convenience (one per run)
    without a declared RPO can be known to be sufficient; what the RPO/RTO literature says about
    undeclared recovery objectives and about the gap between backup frequency and actual recovery
    requirement.

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 3 queries run (2 Pass 1 + 1 Pass 2); no
    full-text reads. UNDER-SEARCHED ON ONE LIMB: I could not locate a peer-reviewed or analyst
    survey quantifying how many organisations operate with no documented RPO. The sources found on
    that limb are vendor and consultancy explainers, which state the qualitative point but not a
    measured rate. The definitional/structural limb is well supported; the prevalence limb is not.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-893
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of any stated recovery objective alongside a remedy whose
        protection interval is set by run boundaries rather than by a tolerance for loss.
      15b: Searched for challenging literature (2026-08-31)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Druva. "Recovery Point Objective (RPO): Definition, Calculation, and Best Practices"
       (glossary/explainer). — States the governing rule that backup frequency must be *less than*
       the RPO for data loss never to exceed the acceptable threshold; the RPO dictates the required
       frequency, not the other way round. This inverts the structure of the presumption: C2A2 has
       chosen a frequency and inferred sufficiency, where the discipline requires choosing a
       tolerance and deriving the frequency.
    2. Commvault, US Patent 10,754,729 (and related 10,761,942; 11,237,915). "Recovery point
       objective (RPO) driven backup scheduling in a data storage management system." — The patents'
       own background section states that operators required to work out backup schedules manually
       to satisfy an RPO frequently fail by this ad hoc approach, "resulting in unacceptable amounts
       of lost data." This is a challenge to convenience-derived intervals specifically, from a
       source with no incentive to overstate the difficulty of the manual approach it replaces.
       Patent background sections are argumentative by nature; treat as directional.
    3. Commvault patent family, as above, on Actual Recovery Point (RPA). — Introduces the concept
       of comparing the declared RPO against the *actual* achieved recovery point, on the reasoning
       that the two diverge in operation. If no RPO is declared at all, this divergence is not
       merely unmeasured but unmeasurable — there is no reference value against which drift could be
       detected.
    4. Expert Insights. "RTO And RPO Explained: Defining Recovery Requirements for Your
       Organization." — Snippet-level; states that most organisations have a disaster recovery plan
       but "far fewer" have clearly defined recovery targets per system, and that without RTO/RPO
       values tied to impact, teams risk "discovering at the worst possible time that their backup
       strategy falls short." Qualitative only — no percentage given, and I could not corroborate a
       figure. This is the weakest source here and is offered only as an indication that the gap is
       a recognised pattern.
    5. Cohesity / Scality / HPE, continuous data protection explainers. — Consistent framing that a
       system backed up at interval N accepts potential loss of up to N, and that periodic snapshot
       approaches carry "risk of data loss between backup intervals" that CDP exists to close. The
       relevant point is not that C2A2 should adopt CDP — it should not — but that the loss window
       is a *chosen quantity* with a determinate size, and choosing it silently is still choosing
       it.
    6. OneUptime, 2026-01-30. "How to Implement Recovery Point Objectives" (blog). — Snippet-level;
       illustrates the failure directly: a policy allowing an RPO of one hour against a last
       successful snapshot three hours old means two hours of work "simply cannot be recovered."
       Practitioner source, not research.

  Strength of challenge: Moderate

  Summary: The challenge here is structural rather than empirical, and it is clean. Every source
    found agrees that the recovery objective is the independent variable and the protection interval
    is the dependent one: you determine how much loss is tolerable, then set frequency to satisfy
    it. C2A2 has done the reverse — adopted an interval given by the run boundary, then presumed
    sufficiency. This is not necessarily wrong in outcome; one snapshot per run may well be adequate.
    But it is unjustified as a claim, and more importantly it is unfalsifiable in its current form.
    Without a declared RPO there is no reference value, so the Actual Recovery Point cannot be
    compared to anything, drift cannot be detected, and the eventual discovery mode is the one the
    literature names repeatedly: finding out at recovery time that the strategy falls short. A
    second, subtler point: "one per run" is a *variable* interval, not a fixed one, because runs
    vary in length and in how much work they contain. A long run with heavy editing carries a much
    larger exposure than a short one, and nothing in the current arrangement notices this. I was
    unable to substantiate how common undeclared RPOs are in practice, so I am not claiming C2A2 is
    typical or atypical — only that the sufficiency claim has no support behind it.

  Specific risks: If one-snapshot-per-run is in fact insufficient, the loss is silent and bounded by
    run length rather than by any considered tolerance — a long run that damages the register early
    and continues writing loses everything after the single snapshot. Because no objective is
    declared, there is no alarm condition: no run can be identified as having exceeded the
    acceptable window, because there is no acceptable window. The risk compounds with
    ASSUMPTION-1233: an untested restore path combined with an unmeasured loss window means neither
    the *reachability* nor the *recency* of the recovery point is known.

  Mitigations available: (a) Declare an RPO explicitly, even a crude one ("no more than one
    substantive edit's worth of work"), so that sufficiency becomes a testable claim rather than a
    presumption; (b) derive the snapshot trigger from the declared tolerance rather than the run
    boundary — e.g. snapshot before each destructive write rather than once per run, which for the
    likely workload is nearly free; (c) record the Actual Recovery Point per run (time or edit-count
    between last snapshot and run end) and compare it to the declared RPO, which converts drift into
    an observable; (d) declare an RTO alongside it — the restore drill proposed under
    ASSUMPTION-1233 would supply the measurement.

  STEELMAN:
    Strongest counterargument: RPO is a construct from environments with continuous, externally
      originated transaction flow — where data arrives whether or not anyone is watching, and loss
      between intervals is unrecoverable because the source is gone. C2A2's register is not like
      that. The work is generated in-session by an agent whose inputs are themselves durable, and a
      lost interval is generally *re-derivable*: the run can be re-executed, the extraction re-run,
      the note re-written. Where the loss window can be closed by redoing work rather than by
      restoring data, the cost of a coarse interval is bounded rework time, not permanent
      destruction — and one snapshot per run may be exactly the right granularity, because the run
      is the natural unit of redo. Formalising an RPO here would import ceremony from a domain whose
      key premise (irreproducible input) does not hold.
    What would need to be true for C2A2 to be safe: The work produced within a run must be genuinely
      re-derivable — inputs retained, runs re-executable, and nothing depending on non-reproducible
      agent output that cannot be regenerated. The run must also be short enough that redoing it is
      cheap. And the snapshot must be taken at the *start* of the run rather than at an arbitrary
      point within it, so that the recovery point aligns exactly with the redo boundary. If those
      hold, the run really is the correct granularity and no separate RPO is needed.
    How to test: Measure rather than argue. Instrument runs to record elapsed time and volume of
      register change between snapshot and run end; the distribution's upper tail is the actual
      exposure. Separately, take one completed run, discard its output, and attempt to re-derive it
      from retained inputs — if re-derivation succeeds cheaply, the steelman holds and the
      recommendation weakens; if it does not, the loss window is real and needs a declared bound.

  Recommendation: CHALLENGED
