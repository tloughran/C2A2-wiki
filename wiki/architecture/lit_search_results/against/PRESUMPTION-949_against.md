SEARCH-AGAINST-PRESUMPTION-949:
  Date searched: 2026-09-11
  Original item: PRESUMPTION-949
  Original statement: "[inferred] That a flag which names its own defect condition has thereby been
    dispositioned — that stating 'a third undispositioned flag would mean the flag channel is the defect'
    is itself a kind of disposition."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-949
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a pattern across three independent runs on one day, with the register recorded
        as being inside the pattern rather than exempt from it.
      15b: Searched for challenging literature; found the challenge already minted three times over
        (PREMISE-131, 173, 138) and the empirical analogue in incident-reporting systems that terminate
        in a database. Records that this file is itself inside the pattern.
    Current status: CHALLENGED

  Register pre-check — this item is pre-answered more heavily than any other in the batch:
    - **PREMISE-173 (ACTIVE) — verbatim.** "NAME THE FINAL ELEMENT... a proposed remedy that consists only
      of observing, recording, counting or reporting is NOT a remedy." Adapted from IEC 61511's acceptance
      criterion: a sensor with no final element is not a protection layer.
    - **PREMISE-131 (ACTIVE) — verbatim.** "A WARNING IS NOT A CONTROL, AND AN UNDELIVERED WARNING IS NOT
      A MITIGATION." Warnings and administrative controls occupy the two least-effective tiers of the
      hierarchy of controls.
    - **PREMISE-138 (ACTIVE).** "REPETITION INSIDE A CHANNEL THAT HAS NO EFFECTOR IS NOT A REMEDY; ITS
      ONLY ADMISSIBLE FUNCTION IS TRANSFER OF OBLIGATION TO A NAMED ACTOR OUTSIDE THE CHANNEL." This is
      precisely the falsification counter in ASSUMPTION-1316, already generalised.
    - PREMISE-102 (ACTIVE) — fail-loud is an act of reporting, not remediation; where the notified channel
      has demonstrated zero throughput, repeated identical non-processing converts a one-time signal into
      an undecided standing policy of non-coverage.
    - PREMISE-183 (ACTIVE) — a filed flag is a LIVE OBLIGATION WITH A CLOSURE TEST, not a discharged duty;
      a repeat filing is a REOPENING, not a new filing.
    - PREMISE-151 (ACTIVE) — repeated disclosure of an unremediated condition normalises it rather than
      resolving it; the disclosure record is evidence of incubation, not of management.
    - PREMISE-116 / PREMISE-123 (ACTIVE) — a finding does not change the behaviour it describes;
      propagation must be engineered and then confirmed.
    Eight ACTIVE premises bear. All eight say the same thing and none was cited by any of the three runs.

  Challenging evidence found: Yes

  Sources:
    1. IEC 61511 (Functional safety — safety instrumented systems for the process industry), acceptance
       criterion for a safety instrumented function. — CANONICAL, register-held under PREMISE-173;
       standard text not retrieved this run — A protection layer requires sensor, logic solver AND final
       element. A detection-and-annunciation chain with no actuator is not a protection layer and may not
       be credited as one in the risk reduction calculation. This is the cleanest statement available
       that naming a condition is not controlling it.
    2. NIOSH / ANSI hierarchy of controls. — CANONICAL, register-held under PREMISE-131 — Warnings and
       administrative controls are the two least-effective tiers, below elimination, substitution and
       engineering controls. A well-worded record is the weakest tier of the weakest tier.
    3. Patient-safety incident reporting literature: "Using Incident Reporting Systems to Improve Patient
       Safety and Quality of Care" (PMC11554398) and "Handling Features of Patient Safety Incident
       Reporting Software and Shortcomings in Report Processing From Healthcare Professionals'
       Perspectives" (PMC12510765). — SECONDARY (search summaries of both records retrieved; full texts
       not read) — The measured shortcomings reported by the professionals who file: reports were not
       discussed in the workplace, "no concrete changes occurred after reporting," reporters did not hear
       about their reports afterwards, and processing was perceived as non-objective. Most systems contain
       no described mechanism for communication between reporters and reviewers. The empirical steady
       state of a mature, mandated, professionally staffed reporting channel is a channel that terminates
       in a record.
    4. NASA ASRS design rationale, "The Case for Confidential Incident Reporting Systems" (FAA Safety
       document). — SECONDARY (search summary) — ASRS is the standing counter-example and it is
       instructive *because* of what it had to build: the feedback loop to reporters is named as the
       mechanism that makes the system work, i.e. the closing element had to be engineered deliberately
       and is not a property of collecting reports.
    5. Meyer, J.W. & Rowan, B. (1977), AJS 83(2):340–363. — SECONDARY, register-held under PREMISE-183 —
       formal structures decouple from the activity they govern; "inspection and evaluation is
       ceremonialized." A control whose production is complete at the moment of writing is the ideal
       ceremonial object.

  Strength of challenge: **Strong** — with the important qualification that the strength is imported from
    the register and from standards rather than from anything new I retrieved. On the literature alone I
    would rate it Moderate; PREMISE-173 and PREMISE-131 take it to Strong and they are ACTIVE.
    Limb split:
      - "Naming a defect condition is a disposition": **Strong** challenge. Refuted by IEC 61511's
        acceptance criterion, by the hierarchy of controls, and by three ACTIVE premises.
      - "A self-referential flag that states its own falsification counter is a special case that does
        count as a disposition": **Moderate** challenge. The steelman below has real force here — a
        stated counter with a stated threshold is closer to a trip point than an ordinary observation is.
        What it lacks is the final element: nothing acts when the counter fires.
    The recommendation rests on the first limb.

  Summary: There is no literature on the other side. Every standard and every measured reporting system
    says the same thing: annunciation without an actuator is not a control, and a reporting channel with
    no feedback loop reaches a steady state in which reports are filed and nothing changes. The estate
    already holds this as three separate ACTIVE premises, minted by this pipeline, at least one of them
    (PREMISE-138) generalising exactly the counter that ASSUMPTION-1316's flag states about itself. The
    genuinely novel content of PRESUMPTION-949 is not that naming is weak — the register knows that — but
    that the *self-referential* form of naming has a false completeness to it: a finding that names its
    own remedy and its own falsification condition reads as finished, and reads that way precisely
    because it is well-constructed. That is a reflexivity trap, not an epistemic one, and no literature
    addresses it directly.

  Specific risks: The self-awareness layer's entire output is speech. If naming is credited as
    disposition, the layer's measured effect on the estate is zero while its recorded effect is large, and
    nothing distinguishes the two states from inside. Concretely: MONITOR-599 alleges a construction
    defect in Agent 15b that, if real, discounts every CHALLENGED status in two registers — it is filed at
    High, with a cheap test named, and it has no owner and no date. If naming were disposition, that item
    is handled. It is not handled. Every CHALLENGED status in this directory, including the one on this
    file, is conditional on a test nobody owns.

  Mitigations available:
    - PREMISE-173's own acceptance test, applied at filing: no item may be recorded as dispositioned
      unless it names a final element — an actor, an action, and a date. This is a template change, not a
      subsystem.
    - Run the measurement 14b names: REVISE-436 already tracks named-vs-owned. Add the self-directed
      subset and count owners over the last 30 days. If the count is zero, the presumption is refuted
      in-house and no search was needed.
    - Separate the two objects per PREMISE-167: a FINDING and an ESCALATION must be stored as different
      objects, so that "named" and "owned" are distinguishable by query rather than by reading prose.
    - Honour the counter that ASSUMPTION-1316 already stated. It is at two. Treating a stated counter as
      binding is free and is the only thing that makes stating one meaningful.

  STEELMAN:
    Item: PRESUMPTION-949
    Strongest counterargument: In an estate whose only sanctioned terminal act is a written record, the
      distinction between "named" and "dispositioned" may be a distinction without an available
      difference. An agent that may not edit `inbox/`, may not renumber live ids, and may not approve its
      own tool grants has exactly one effector: prose addressed to a person. Demanding that its findings
      carry an owner and a date is demanding that it assign work to someone who has not agreed to it —
      which is worse than naming, because it manufactures a false record of transfer (PREMISE-108:
      transmission is not delivery; a finding flagged for a named agent is held by nobody while the record
      shows it discharged). On this reading, a carefully-worded record with a stated falsification counter
      is the *most* honest object such an agent can produce, and the defect is in the estate's effector
      topology, not in the agent's terminal act. PRESUMPTION-956 is that defect, stated directly.
    What would need to be true for C2A2 to be safe: (a) there must be a reader — PRESUMPTION-953, which is
      the Critical item this one depends on; 14b says so explicitly and is right; (b) there must be at
      least one effector reachable from a finding without a human hop, or the naming layer must be
      explicitly and honestly labelled as non-remedial so that no downstream consumer treats a filed flag
      as a closed one; (c) stated counters must bind, or they must not be stated. Currently (a) is
      unmeasured, (b) is false, and (c) has been violated once already.
    How to test: 14b's test, run as stated — of the named measurements produced by self-directed findings
      in the last 30 days, how many have an owner? Add one column: how many have a DATE. Then one
      falsifier for the steelman: over the same window, count findings that were closed by any mechanism
      other than a human acting on prose. If that count is zero, the steelman is correct that prose is the
      only effector, and the item should be re-routed to PRESUMPTION-956 as the governing defect.

  Search scope: comprehensive — searched safety-reporting systems with and without feedback loops,
    incident-report processing shortcomings, hierarchy-of-controls and IEC 61511 acceptance criteria,
    institutional-decoupling literature, and the ASRS design rationale as the standing counter-example.
    No source was found arguing that annunciation alone constitutes disposition.

  Reflexivity note, and it is part of the finding: this file names measurements and attaches no owner to
    them. It is inside the pattern it describes, exactly as 14b recorded of its own register.

  Recommendation: CHALLENGED
