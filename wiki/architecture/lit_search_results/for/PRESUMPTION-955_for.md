SEARCH-FOR-PRESUMPTION-955:
  Date searched: 2026-09-11
  Original item: PRESUMPTION-955
  Original statement: "[inferred] That a status vocabulary's first duty is to protect the downstream
    alarm from false positives, and only its second to protect the reader from false assurance."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-955
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the stated ordering of reasons in a run that asked for exactly this ruling.
        Moderate confidence — the run may hold the opposite priority and have reported the reasons in
        the order they occurred rather than in order of weight.
      15a: Searched for supporting literature; found the strongest support of the ten items, in the
        international alarm-management standards, which also supply the design the run improvised.
    Current status: PARTIALLY-SUPPORTED

  Register pre-check:
    - PREMISE-110 (ACTIVE) — "Detectors do not reliably degrade gracefully; they invert. A monitor whose
      failure presents as a nominal reading becomes MORE reassuring as the monitored condition worsens
      (stuck-at-nominal)." This bears directly on the observed cost: `Morning system health` reading a
      7-day-cold `metabolism_data.json` without firing.
    - PREMISE-100 (ACTIVE) — a health check that cannot execute in its runtime context reports as
      passing rather than as absent; monitoring that conflates the two produces false-green.
    - PREMISE-141 (ACTIVE) — absence of a report is a third terminal state, not a value of the other
      two. **This is the formal statement of the design the telemetry run needed and did not have.**
    - PREMISE-063 (ACTIVE) — gap-honest visualisation: must not show data that do not exist, must
      distinguish measured from inferred, must encode absence as distinct from a true zero.
    - PREMISE-086, PREMISE-084 (ACTIVE) — alarm on the AGE of the last dated PASS; signal change only
      when change is real.
    - PREMISE-167 (ACTIVE) — an escalation and a measurement are different objects and must be stored as
      different objects; an escalation expressed only as a withheld PASS-mark has no representation on
      disk distinct from staleness.
    - ASSUMPTION-1314 as named; searched once for both per the intake note.
    Recording the hits per OPEN-192; searched anyway.

  LIMB SPLIT:
    Limb A (ALARM PRECISION IS THE ALARM'S FIRST DUTY): a signal that does not require a response should
      not fire, and protecting the alarm from false positives is the primary design obligation of an
      alarm channel.
    Limb B (A QUALIFIED PASS DISCHARGES THE TRUTHFULNESS DUTY): where the two duties conflict, the
      reader's protection is adequately served by a qualifier attached to a green status.

  Supporting evidence found: Yes (Limb A), No (Limb B)

  Sources:
    1. ANSI/ISA-18.2 (and its international equivalent IEC 62682), *Management of Alarm Systems for the
       Process Industries*. — SECONDARY (standard text not retrieved; definition and requirement via
       exida, Yokogawa/Control Engineering, ProcessVue and Merobix summaries, which agree) — ISA-18.2
       defines an alarm as "an audible and/or visible means of indicating to the operator an equipment
       malfunction, process deviation, or abnormal condition **requiring a response**." The standard
       further requires that **alarms requiring no operator response be converted to indications or
       events**. This is Limb A stated as a definition, in the discipline that has thought hardest about
       it, and it is decisive support: the alarm's first duty *is* precision, because an alarm that does
       not demand action is by definition not an alarm.
    2. EEMUA 191, *Alarm Systems: A Guide to Design, Management and Procurement*. — SECONDARY (via
       comparison summaries) — Converges with ISA-18.2 on the same fundamental principle: an alarm needs
       a defined operator response. The two standards are described as compatible and mutually
       reinforcing rather than alternatives, so the position is not a single body's idiosyncrasy.
    3. Alarm rationalisation practice (Emerson white paper, *Alarm Rationalization*, Oct 2019; Siemens
       PCS 7 alarm-management paper; exida alarm-management resources). — SECONDARY — "Incidents
       involving human error often include a failure of the operator to respond to an alarm, which is
       often directly or indirectly caused by nuisance alarms." This supplies the causal claim behind
       Limb A: false alarms do not merely annoy, they *cause* missed detections, so the two costs are
       not independent and suppressing nuisance alarms is itself a missed-detection control.
    4. Clinical alarm-burden figures. — SECONDARY — **80%–99%** of alarms in hospital units are false or
       clinically insignificant; **90%–99%** of alarms received by security monitoring centres are false
       or non-actionable. And in the clinical decision support systematic review (23 articles,
       PMC7400042), override rates run **46.2%–96.2%**, with individual DDI studies at **92.9%** and
       **92.2%**. These establish the magnitude of the cost Limb A is protecting against; they are
       consistent across two unrelated domains, which is why I weight them despite none being retrieved
       as primary.
    5. The same standards literature, on where the truthfulness duty goes — **and this is the finding
       that splits the item.** — SECONDARY — ISA-18.2's remedy for a condition that does not require
       operator response is *reclassification of the signal* into an indication or event, not
       suppression and not annotation of a nominal status. The condition remains visible in its own
       channel with its own record. The standard therefore grants Limb A and simultaneously denies Limb
       B: alarm precision is purchased by moving the signal, never by letting a green status stand for a
       condition that is not green.

  Strength of support: Strong (Limb A), None (Limb B)

  Summary: This is the best-supported item of the ten and the one that converts most directly into a
    design. Limb A is not merely supported, it is *definitional* in ANSI/ISA-18.2 and IEC 62682: an
    alarm indicates a condition requiring a response, and a signal that requires no response must be
    reclassified out of the alarm class. The alarm-fatigue magnitudes (80–99% false in clinical units,
    90–99% in monitoring centres, 46–96% override rates in CDS) establish that this is not a
    fastidiousness about definitions but a measured failure mode with a causal path to missed detection
    — nuisance alarms *produce* non-response. So the telemetry run's ordering of reasons was correct,
    and 14b's moderate-confidence inference that the run holds alarm precision first should be recorded
    as vindicated rather than as a defect. Limb B is where it fails. The standards do not permit the
    truthfulness duty to be discharged by a qualifier on a green status; they require a third channel —
    the condition becomes an *event* or *indication*, carried with its own visibility and its own
    record. That is PREMISE-141 ("absence of a report is a third terminal state") and PREMISE-167 (an
    escalation and a measurement are different objects) restated by an external standards body, which is
    an unusually clean corroboration. The cost 14b identified — `Morning system health` reading a 7-day
    -cold artefact without firing — is exactly what a missing third channel produces, and PREMISE-110
    names the mechanism as stuck-at-nominal inversion.

  Caveats: ISA-18.2 and EEMUA 191 govern process-industry operator consoles with continuous human
    attendance, a defined response procedure per alarm, and consequences measured in lives; the estate's
    `morning-system-health` has an intermittent reader and no per-alarm response procedure. The transfer
    is good for the *taxonomy* (alarm / event / indication as distinct classes with distinct duties) and
    poor for the *thresholds* (the standards' target alarm rates are calibrated to an attended console).
    I did not retrieve either standard's text — both are paywalled — so the definition and the
    convert-to-indication requirement are SECONDARY, though four independent summaries agree on both.
    The clinical and security alarm-burden percentages are ranges from secondary sources and should not
    be quoted as point estimates.

  Search scope: comprehensive — searched ISA-18.2/IEC 62682/EEMUA 191 alarm philosophy and
    rationalisation, nuisance-alarm elimination, alarm fatigue in clinical and security monitoring,
    clinical decision support override rates, and the asymmetric costs of false alarm versus missed
    detection. Did not search signal detection theory (ROC / Bayesian decision thresholds), which would
    formalise the asymmetry but would not change the verdict, since the standards' answer is
    reclassification rather than threshold-setting.

  Recommendation: PARTIALLY-SUPPORTED. The recommendation rests on the split, and the split is the
    answer to the ruling the telemetry run asked for. Limb A is SUPPORTED at Strong — do not fire
    `morning-system-health` over feeds that are genuinely current, and the run was right to refuse a
    bare FAIL. Limb B is NO-SUPPORT-FOUND — a qualified `PASS` is the wrong instrument, because the
    qualifier has no representation the downstream health check can act on, which is precisely why the
    7-day-cold `metabolism_data.json` passed. The standards prescribe the fix directly and it is a small
    one: add a third status alongside PASS and FAIL — call it what ISA-18.2 calls it, an *event* or
    *indication* — so that "verified current but not produced by me" has a home that is neither an alarm
    nor a green light. That answers ASSUMPTION-1314 in the same stroke, and it is PREMISE-141 already on
    the books.
