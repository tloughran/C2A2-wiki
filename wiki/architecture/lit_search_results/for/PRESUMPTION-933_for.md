SEARCH-FOR-PRESUMPTION-933:
  Date searched: 2026-09-09
  Original item: PRESUMPTION-933
  Original statement: [inferred] Agents fail loudly — a run that reports nothing has nothing to report,
    so silence from a scheduled task is evidence of an uneventful run rather than of an unobserved one.
  Routed question: how reliable is self-reporting as a failure-detection channel under partial failure,
    and what is the measured detection gap between self-report and external heartbeat/watchdog
    monitoring?

  DIRECTION NOTE: per the orchestrator's dispatch, FOR here means evidence that self-report / fail-loud
    IS a reliable channel — i.e. FOR the presumption as the pipeline holds it. (The intake entry in
    `for_lit_search.md` files "contexts in which self-report is empirically sufficient" under AGAINST,
    i.e. assigns that direction to 15b. The dispatch governs; the discrepancy is recorded so 14b does
    not read a sign inversion. If 15b also searched for sufficiency, the pair is not independent on
    this item.)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-933
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inferred from two same-day silent runs that no consumer recorded as silent —
        `metabolism-regen-daily` produced no terminal verdict of any kind under a fail-loud spec, and
        `morning-system-health` stalled at a permission prompt and wrote no report. Both were counted
        as fired.
      15a: Searched for supporting literature (2026-09-09), FOR direction only.
    Current status: NO-SUPPORT-FOUND

  PREMISE-REGISTER OVERLAP (checked before searching, per DEFECT-G): DECISIVE — THE REGISTER ALREADY
  SETTLES THIS ITEM, AND SETTLES IT AGAINST THE PRESUMPTION.
    Grepped for: fail-silent, self-report, watchdog, dead man, near-miss, failure detector, silence.
    - PREMISE-195 (ACTIVE, High confidence, validated 2026-08-31, on an ELEVATED MONTHLY re-check
      cadence as "the estate's highest-rated open risk", next due 2026-09-30): "Voluntary self-report is
      not a detection control. A control whose only output is the assertion of the controlled party
      produces silence as the shared output of 'nothing went wrong' and 'detection is not working,' and
      nothing downstream can distinguish them." THIS IS PRESUMPTION-933'S EXACT DENIAL, ALREADY
      VALIDATED, ALREADY CHALLENGED-STRONG IN THE SAME DIRECTION BY 15b, AND ALREADY CARRYING IN-HOUSE
      EVIDENCE (n=2, 2026-08-31: of two destructive writes, one was self-reported and one was invisible
      to every agent involved).
    - PREMISE-171 (ACTIVE): "A DECLARATION REGISTER IS NOT A FAILURE DETECTOR — ITS COMPLETENESS IS
      ZERO … in Chandra & Toueg's terms it satisfies no completeness property whatever, so it is not a
      weak detector but not a detector at all." Includes the VERIFIED Apple statement that non-calendar
      launchd and cron jobs are silently skipped and never run if the machine is off, and the
      LOAD-BEARING NEGATIVE that a naive heartbeat installs the gray failure it was bought to treat.
    - PREMISE-100 / PREMISE-110: liveness is not correctness; a monitor's pass-state is reachable while
      the subject is dead.
    - Register line ~2579 records, from the multi-agent-failure taxonomy already in-house: "75.17% of
      failures emit no hard error signal."
    - Register line ~5668 already records that liveness "is not monitorable from a finite trace (Alpern
      & Schneider)" and that "failure detectors are unreliable by" construction.
    - Register lines ~4954-4956 already carry the systemd `WatchdogSec` caution and Koopman/Ganssle on
      the kick-regardless anti-pattern.
    NARROWING APPLIED: I did NOT re-derive the case against self-report, which is the single
    best-established position in this register. I searched ONLY for the affirmative — whether any
    literature establishes conditions under which self-report IS sufficient, since a genuine finding
    there would be the one thing capable of moving PREMISE-195, and since the dispatch explicitly
    invites NO-SUPPORT-FOUND as an informative answer.

  Supporting evidence found: No

  Sources (searched in the FOR direction; what was actually found):
    1. The fail-fast design principle.
       [PRACTITIONER AND ENCYCLOPAEDIA LEVEL ONLY — Wikipedia "Fail-fast system" plus several
       engineering blogs retrieved this run; NONE READ IN FULL; no primary or peer-reviewed source
       located] — The only thing found in the FOR direction, and it does not do the job. The definition
       retrieved: a fail-fast system "immediately reports at its interface any condition that is likely
       to indicate a failure." That is a DESIGN PRESCRIPTION, not a finding about how systems behave,
       and its own wording contains the limit that defeats PRESUMPTION-933. It reports conditions
       "LIKELY TO INDICATE A FAILURE" — i.e. anticipated conditions, at instrumented checkpoints, that
       the designer thought of. It says nothing about unanticipated stalls, and it presupposes the
       process reaches an interface at all. Both of today's incidents are outside its scope: a task that
       blocks on a permission prompt never reaches a reporting point, and a task that terminates without
       emitting its specified terminal verdict has by definition failed to fail fast. The principle also
       explicitly contrasts itself with fail-silent behaviour, which is to say the literature treats
       fail-loud as something you must ENGINEER AND VERIFY, never as a default you may assume.
       WEIGHT: None as support. It is the design goal the estate's spec already stated and the runs
       already violated — which makes the spec's existence evidence against the presumption, not for it.
    2. Chandra, T.D. & Toueg, S., 1996. "Unreliable Failure Detectors for Reliable Distributed Systems."
       Journal of the ACM 43(2):225-267.
       [CANONICAL; ALREADY REGISTER-HELD AT PREMISE-171 WHERE IT IS MARKED "CANONICAL — not
       re-verified". This run I confirmed the JACM listing and multiple independent PDF copies exist;
       PAPER NOT READ] — Searched deliberately in the FOR direction, looking for any construction in
       which a process's own report satisfies a completeness property. There is none, and the framework
       explains why in a way that is fatal rather than merely unhelpful: completeness requires that the
       detector eventually suspects every process that ACTUALLY CRASHES. A crashed or stalled process
       cannot emit its own suspicion. Self-report is therefore not a weak detector; like PREMISE-171's
       declaration register, it is not a detector of the crash class at all. WEIGHT: None as support;
       recorded because a serious FOR search must go where the affirmative would have to live, and
       report that it is empty.
    3. Voluntary incident reporting — measured detection rates (the human analogue the intake named).
       [SEARCH-SUMMARY LEVEL, plus one identified primary venue: "Error Reporting Systems," chapter in
       Kohn, L.T., Corrigan, J.M. & Donaldson, M.S. (eds.), To Err Is Human: Building a Safer Health
       System, Institute of Medicine / National Academies Press, NCBI Bookshelf NBK225170.
       VERIFIED: the chapter exists at that Bookshelf identifier. CHAPTER NOT READ. The "about 5
       percent" figure below is FROM A SEARCH SNIPPET AND UNVERIFIED AGAINST THE CHAPTER] — Reported:
       self-reporting typically identifies only about 5 percent of actual events; systematic detection
       tools such as the Global Trigger Tool detect significantly more events than voluntary reporting.
       WEIGHT: None as support — it is a ~95% miss rate. NOTE: this is the SAME ORDER as the figure
       already carried in PREMISE-195's challenge line (Bates et al., 2023, NEJM 388:142-153 — mature
       voluntary systems detect on the order of one event in twenty), which the register records as
       "the CEILING under favourable conditions." Two independent bodies of the healthcare literature
       agree at roughly 5%, and PREMISE-195's in-house n=2 pointed the same way at 50%.
    4. Conditions under which self-report is sufficient.
       NONE FOUND. Four queries in this direction returned no source proposing that an actor's own
       report is adequate as a sole detection channel. The nearest thing to a positive finding is
       PREMISE-195's own preserved steelman, which is 15b's from a prior cycle and which I am not
       re-deriving: agents lack the blame-culture and career-risk disincentives that drive human
       under-reporting, so the binding constraint may be NOTICING rather than WILLINGNESS. Today's two
       incidents support that DIAGNOSIS and not its conclusion — neither agent concealed anything; both
       simply did not report, and one could not.

  Strength of support: None.

  Summary: I searched the affirmative and it is empty. The only material found in the FOR direction is
  the fail-fast principle, which is a design prescription rather than an empirical claim, and whose own
  definition — reporting "at its interface any condition that is LIKELY to indicate a failure" — carves
  out exactly the two cases that generated this presumption: a stall that never reaches an interface,
  and a termination that omits the verdict the spec required. That the estate had a fail-loud SPEC which
  both runs violated is itself the strongest available datum, and it points against. The distributed-
  systems framework the intake named makes the impossibility structural rather than contingent: a
  process that has crashed or blocked cannot emit its own suspicion, so self-report satisfies no
  completeness property over the crash class. The human analogue is quantified and brutal — voluntary
  reporting in healthcare detects on the order of 5% of actual events, a figure that appears
  independently in the To Err Is Human material found this run and in the Bates NEJM figure already
  carried in the register. And the register has already settled this: PREMISE-195 states the denial
  almost verbatim, holds High confidence, was CHALLENGED-STRONG by 15b in the same direction, carries
  in-house evidence, and sits on an elevated monthly re-check as the estate's highest-rated open risk.
  PRESUMPTION-933 is a belief the estate's own validated register already rejects.

  Caveats:
  (a) THE FINDING IS AN ABSENCE, AND ABSENCES ARE WEAKER THAN PRESENCES. Four queries in the FOR
      direction found nothing; that bounds my search, not the literature. I would note, however, that
      the absence is of the structural kind rather than the unstudied kind — as with PRESUMPTION-925's
      authorship limb, no one has proposed self-report as a sole detection channel because the object
      does not carry the required property, not because the question is neglected.
  (b) THE 5% FIGURES ARE SNIPPET-LEVEL AND FROM ONE DOMAIN. I did not open To Err Is Human, and the
      Bates figure is quoted from the register rather than re-verified. Both are healthcare, where
      under-reporting is driven substantially by blame culture — a mechanism agents lack. The
      steelman preserved in PREMISE-195 remains live and is NOT refuted by anything I found.
  (c) DO NOT ANSWER THIS WITH A HEARTBEAT. PREMISE-171 carries this as a load-bearing negative and it
      applies with full force here: gray failure is canonically the detector observing health over a
      path that bypasses the sick path, and the register also already holds the systemd `WatchdogSec`
      caution and the Koopman/Ganssle kick-regardless anti-pattern. A heartbeat added to answer
      PRESUMPTION-933 would very likely install the failure it was bought to treat. PREMISE-171's named
      minimal repair — store an EXPECTED-NEXT-FIRE and alarm on the divergence between expected and
      observed — is the one already-validated remedy shape, and it costs one field.
  (d) THE MEASURED DETECTION GAP THE QUESTION ASKS FOR DOES NOT EXIST IN WHAT I SEARCHED. The routed
      question asks for "the measured detection gap between self-report and external heartbeat/watchdog
      monitoring." I found no such measurement for software estates. The healthcare figures are the
      nearest analogue and the transfer is contested (see (b)). If the estate wants this number for
      itself it is obtainable in-house and cheaply: PREMISE-195's n=2 is the beginning of exactly that
      series, and the two incidents of 2026-09-08 take it to n=4.
  (e) SEARCH SCOPE: narrowed deliberately (see overlap section) — four queries. Not covered: near-miss
      reporting-rate research in aviation and rail (searched obliquely, nothing FOR found); crash-
      reporting completeness studies (Windows Error Reporting / Breakpad telemetry coverage), which is
      the one remaining place a genuine FOR finding might live and which I did not reach.

  Recommendation: NO-SUPPORT-FOUND
    (Strength: None. The FOR direction is empty; the only material located in it is a design
     prescription whose own scope excludes both triggering incidents, and every quantified source found
     runs the other way.)

  NOVELTY-FLAG:
    Item: PRESUMPTION-933
    Searched: four queries across fail-fast/fail-silent design, failure-detector theory (completeness
      and accuracy), voluntary incident-reporting detection rates, and conditions for self-report
      sufficiency.
    Finding: No existing literature was found proposing that an actor's own report is a sufficient sole
      failure-detection channel. This is a negative novelty finding of the same shape as
      PRESUMPTION-925's authorship limb: the absence is structural (a stopped process emits nothing)
      rather than evidential.
    Implication: PRESUMPTION-933 should be read as absence of warrant, not as an original contribution.
      It corroborates PREMISE-195 from the outside, independently, on the day two fresh instances
      occurred.
    Recommended status: NOVEL in the unfavourable sense — an unwarranted estate-local default, not a
      recognised method.

  DISPOSITION STEER FOR 15c: do NOT mint. PREMISE-195 and PREMISE-171 already hold this at High
    confidence with both search directions agreeing. What 2026-09-08 supplies is n=3 and n=4 for
    PREMISE-195's in-house series and a dated propagation failure — the estate holds the premise and
    two consumers acted against it. That is REVISE/MONITOR material and, given PREMISE-195's
    2026-09-30 re-check, it is arguably re-check evidence that should be attached there rather than
    processed as a new item.
