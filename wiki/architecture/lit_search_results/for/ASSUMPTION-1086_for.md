SEARCH-FOR-ASSUMPTION-1086:
  Date searched: 2026-08-16
  Original item: ASSUMPTION-1086
  Original statement: **THREE SCHEDULED AGENTS HAVE NEVER FIRED ONCE, AND THE ONLY REASON ANYONE KNOWS
  IS THAT THE INSTRUMENT WAS REBUILT.** `com.c2a2.metabolism-publish`, `com.tloughran.summa-weekly-review`
  and `com.tomloughran.openstory-version-check` are each "loaded but has NEVER fired (runs = 0), and at
  least one scheduled fire has passed. No log exists to read, because it never started." Against the
  task's own 2026-08-05 baseline of 78 OK / 4 WARN / 0 FAIL, the OK count is identical and FAIL moved
  0 → 5. "The failures did not begin today; the ability to see them did."

  QUEUE TAG: [QUEUED-EMPIRICAL]. Per the intake instruction, only the MONITORING-DESIGN half is treated
  as literature-testable here. The empirical half — why these three particular agents did not fire, and
  for how long — is a one-command local check (`launchctl print`, plist `StartCalendarInterval`, file
  creation dates) and is NOT answered by anything below. Nothing in this file licenses a claim about the
  duration of the outage. See Caveat (a).

  POLARITY NOTE — what was searched FOR. The item is worded as an incident report, not as a belief, so
  "SUPPORTED" needs a stated proposition. The proposition searched FOR has four clauses, drawn from the
  intake's search question: (i) NEVER-STARTED IS A DISTINCT FAULT CLASS from started-and-failed, requiring
  a distinct detector, and a monitoring stack that reads logs, exit codes or run outcomes is uncovered for
  it BY CONSTRUCTION, because the fault's signature is the absence of the artefact the detector reads;
  (ii) A POSITIVE-ACKNOWLEDGEMENT HEARTBEAT DETECTS IT ONLY IF THE JOB WAS REGISTERED IN ADVANCE — the
  design is sound but its coverage is exactly the coverage of its registry, and a job absent from the
  registry is invisible to it in precisely the same way it is invisible to log-reading; (iii) THE DESIGN
  THAT CLOSES THE REGISTRY GAP IS MANIFEST RECONCILIATION — mechanically deriving the expected set from
  the authoritative declaration (the scheduler's own loaded-job table, the plist directory, the rule
  resource) and alarming on set difference, rather than maintaining a second hand-written list of things
  to watch; (iv) THE DETECTION LATENCY OF SUCH A FAULT IS A PROPERTY OF THE AUDIT INTERVAL, NOT OF THE
  FAULT — for an unrevealed/dormant failure the expected time-to-detection is approximately half the
  test interval, and where no periodic test exists the latency is bounded only by the next demand or by
  an instrument rebuild, which is exactly what happened here. "SUPPORTED" below means these four clauses
  are supported; the item's own factual claims are not what was searched.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1086
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted the verdict verbatim from the 2026-08-15 scheduler health report and set it against
           the baseline the task file itself carries. [stated]
      15a: Searched for supporting literature on the monitoring-design half only; the empirical half is
           left where the queue tag put it.
    Current status: SUPPORTED (Strong on the design clauses; the register already holds most of it)

  REGISTER CHECK (performed BEFORE writing this file):
    Grepped `validated_premises.md` for: heartbeat, dead man, liveness, silent, watchdog, detection,
    absence, negative space, instrument, never ran, threshold, scope.
    Found and read in full:
      - **PREMISE-141 clause (1)** (2026-08-05, ACTIVE, High) — THE CLOSEST ANTECEDENT AND IT NAMES THIS
        ITEM'S STATE BY NAME. Citing Cristian's failure-semantics taxonomy, it establishes that "a
        component that runs and produces no response (omission)" and "one that does not run (crash)" are
        "distinct classes requiring distinct detectors, and a system that detects only one is uncovered
        for the other," and prescribes a three-valued model: RAN-AND-REPORTED, RAN-AND-DIED-SILENT,
        NEVER-STARTED. 141 was minted from the 2026-08-04 four-silent-run event, i.e. from the
        RAN-AND-DIED-SILENT arm. **ASSUMPTION-1086 is the first observation of the NEVER-STARTED arm.**
        The knowledge was already held; what is new is that the other arm has now fired and that the
        remedy 141 filed was aimed at the arm that had.
      - **PREMISE-166 clause (1) and (2)** (2026-08-15, ACTIVE, Moderate) — minted YESTERDAY from
        ASSUMPTION-1068/PRESUMPTION-799. Clause (1) requires the receiver to sit outside the failure
        domain. Clause (2) — PROGRESS-BINDING — requires the ping to be bound to work completed. Its
        supporting evidence line already contains the exact phrase this item needs: "detection requires
        a per-job check registered IN ADVANCE (Healthchecks.io, Cronitor) [VERIFIED and read this run]."
        The registration-in-advance requirement is therefore ALREADY IN THE REGISTER, one day old.
      - **PREMISE-086** (2026-06-27, ACTIVE, High) — alarm on the AGE of the last dated PASS/FAIL;
        absence/staleness IS the signal; monitor-of-monitor condition. PREMISE-141 records 086 as
        UNENFORCED for scheduled agent sessions. ASSUMPTION-1086 is 086 unenforced a second time, and
        in the one variant 086 as written does not reach: a job with `runs = 0` has NO last dated
        PASS/FAIL whose age could be taken.
      - **PREMISE-100** (ACTIVE, High) — a liveness signal is not evidence of correctness, and a check
        that cannot execute in its runtime context reports as PASSING rather than as ABSENT. The
        old instrument's blindness (per ASSUMPTION-1087) is an instance.
      - **PREMISE-110** (ACTIVE) — detectors invert; absence-of-complaint is an unsafe polarity; the
        common-mode scope guard.
      - **PREMISE-124 clause (b)** (ACTIVE, High) — a self-audit assembled while a channel is
        systematically DARK cannot be called observationally complete, because the missingness mechanism
        cannot be assessed from the surviving data (Rubin 1976). This is the exact epistemics of "78 OK"
        computed by an instrument that could not see launchd.
      - **PREMISE-140** (ACTIVE) — a metric derived from one observation channel must be named by its
        channel; streak framings barred. The 2026-08-05 "78 OK / 0 FAIL" baseline is a channel-named
        quantity mis-named as a fleet property, which is why the FAIL count "moved" 0 → 5 without
        anything in the world changing.
      - **PREMISE-101** (ACTIVE, High) — counts are properties of a (scope, method, time) reading. The
        0 → 5 delta is a METHOD change, not a world change; 1086 says this itself in its last sentence.
      - **PREMISE-105** (ACTIVE) — a change in the definition of what is counted breaks the series; a
        delta spanning the change is uninterpretable until the definitional component is measured. This
        binds the 0 → 5 comparison directly and is the strongest reason NOT to report "FAIL count rose."
    CONCLUSION OF THE CHECK: **SUBSTANTIAL OVERLAP; NO NOVELTY-FLAG.** Eight ACTIVE premises bear on
    this, two of them (141, 166) minted from the same fleet within the last eleven days. The residual is
    three narrow things:
      (R1) THE NEVER-STARTED ARM HAS NOW FIRED, AND THE REMEDY WAS BUILT FOR THE OTHER ARM. PREMISE-141
           named three terminal states and filed a code change for the third; PREMISE-166 specified where
           the receiver sits and what the ping is bound to. Both presuppose a process that RUNS. None of
           the register's remedies detect a job that never starts, because there is no process to emit,
           to bind, or to time out.
      (R2) THE REGISTRY IS THE COVERAGE, AND ITS COMPLETENESS IS UNMEASURED. 166 requires a check
           "registered in advance" and stops there. The failure mode above it — a job that exists in the
           scheduler but not in the monitoring registry — is not addressed by any premise, and it is the
           mechanism by which these three agents were invisible.
      (R3) THERE IS NO DETECTION-LATENCY QUANTITY ANYWHERE IN THE REGISTER. PREMISE-086 requires an age
           threshold; no premise says what latency an un-audited dormant fault has. The reliability
           literature gives a closed form, and it is the one useful number this file adds.
    DECLARED LIMITATION: this was a string grep, measured at ~56% recall by the 2026-08-14 15c run
    (ASSUMPTION-1052). The list above is a **LOWER BOUND**; the true overlap is very likely larger, and
    given that it already returned eight entries that argues for a narrower disposition, not a wider one.

  Supporting evidence found: Yes

  Sources:
    1. PromLabs (Julius Volz, Prometheus co-founder), "Dealing with Missing Time Series in Prometheus,"
       2023-09-13. — **The verified statement of clause (i) and (ii), in the exact shape of the fault.**
       The post establishes that a series for a labelled dimension "will only start existing once the
       first operation of that particular type has occurred," so a metric that has never had an
       occurrence is not merely zero — IT DOES NOT EXIST. The consequence is stated flatly and is the
       core finding for this item: an alerting rule over such a series "may even SILENTLY FAIL TO FIRE,
       since Prometheus interprets an empty alerting rule expression output as 'everything is fine'."
       That is `runs = 0` exactly: the never-started job produces no record, and a monitor that reads
       records reads nothing and reports health. The post's own remedy is the one this item needs and is
       named as the preferred option — **PRE-INITIALISE THE SERIES**, i.e. declare the expected set at
       startup so that the absent case has a representation ("the best course of action is to
       pre-initialize each value to 0 right after program startup"), falling back to joining a default
       from an always-present series (`up`) where the set is not enumerable in advance. The distinction
       between "enumerable in advance" and "not" is precisely the distinction between C2A2's launchd
       manifest (enumerable — it is a directory of plists) and an open-ended label space.
       [VERIFIED this run — fetched and read in full.]
    2. Healthchecks.io, "How to Monitor Cron Jobs with Healthchecks.io" (product documentation). — **The
       positive-acknowledgement design stated by its implementer, including its coverage boundary.** The
       documented failure modes it detects are enumerated: "the whole machine goes down"; "the cron
       daemon is not running or has an invalid configuration"; "cron does start your task, but the task
       exits with a non-zero exit code"; "the cron job runs for an abnormally long time." The first two
       ARE the never-started class, so the design does cover it — but only through the mechanism the
       documentation makes explicit in the setup procedure: "**first create a new Check in your
       Healthchecks.io account**," then paste the generated ping URL into the job. The check, its
       schedule and its Grace Time are declared to the receiver BEFORE any ping is expected. Detection is
       therefore a property of the DECLARATION, not of the job; an undeclared job cannot be missed
       because it was never expected. The Grace Time mechanism is also the register's missing latency
       parameter in operational form: alert time = scheduled time + grace, which for a daily job is
       ~1 day, against an unbounded latency for an unregistered one.
       [VERIFIED this run — fetched and read in full. VENDOR DOCUMENTATION, labelled as such; it is
       practice, not a peer-reviewed result. Already cited in PREMISE-166 and re-read here.]
    3. SAP / cloudoperators, `absent-metrics-operator`, README (open-source Kubernetes operator). —
       **The MANIFEST-RECONCILIATION design, and an explicit statement of why the hand-maintained
       registry fails.** The stated motivation is that an alert of the form `expr: foo_bar > 0` "would
       never trigger if the metric `foo_bar` does not exist in Prometheus," that the manual fix
       (`absent(foo_bar) or foo_bar > 0`) "gets tedious if you have hundreds of alerts deployed across
       the cluster," and — the load-bearing clause — that "**there is also the element of human error,
       e.g. typo or forgetting to include the `absent` function in the alert expression.**" The remedy is
       structural rather than exhortative: the operator "monitors all the `PrometheusRule` resources
       deployed across a Kubernetes cluster and creates corresponding absence alert rules," mechanically
       deriving the expected set from the authoritative declaration. The generated alert's own annotation
       states the fault class in one line: "The metric 'foo_bar' is missing. 'ImportantAlert' alert using
       it may not fire as intended." **This is the design (R2) asks for, and its existence as a
       maintained operator is itself the finding: the registry-completeness gap is common enough that
       production shops build machinery to close it rather than trusting a list.** The C2A2 analogue is
       exact: derive the expected-job set from `launchctl list` / the LaunchAgents directory, not from a
       second hand-written table.
       [VERIFIED this run — fetched and read in full. VENDOR/OSS PRACTICE, labelled as such. 10 stars;
       cite for the DESIGN PATTERN and the stated motivation, not as evidence of adoption scale.]
    4. IEC 61508 / IEC 61511 proof-testing doctrine, as set out in Green, D. (Engineering Safety
       Consultants), "Proof Testing of Safety Instrumented Functions: A Beginners Guide (Part 1)," and
       the associated PFD literature. — **The latency result (clause iv), and the vocabulary that makes
       `runs = 0` a named condition rather than a surprise.** IEC 61508's own definition of a proof test
       is "a periodic test performed to detect DANGEROUS HIDDEN FAILURES in a safety-related system," and
       the guide restates the purpose as revealing "all the 'undetected/unrevealed' failures which the
       device may be harbouring UNBEKNOWN TO ANYONE." The consequential sentence transfers verbatim to a
       standby scheduled job: "if the device is not tested at the specified interval, there is a danger
       that an undetected failure may be left unrevealed UNTIL A DEMAND IS PLACED UPON IT and your safety
       function will not work when you need it to." Three C2A2-relevant consequences. (α) The
       fail-to-START / fail-to-RUN split is a standard component failure-mode taxonomy in this
       literature, which is clause (i) arriving from reliability engineering rather than from distributed
       systems. (β) The expected down time of an unrevealed failure is a fraction of the proof-test
       interval — half, at unit level — plus repair time; so DETECTION LATENCY IS SET BY THE AUDIT
       CADENCE, NOT BY THE FAULT. (γ) Where proof-test COVERAGE is below 100%, some failures are "never
       detected" and persist until demand or replacement — which is the formal name for the state these
       three agents were in.
       [MIXED. The IEC 61508 proof-test definition and the "unbeknown to anyone"/"until a demand"
       passages: VERIFIED this run — the ESC guide was fetched and read in full; it is CONSULTANCY
       TRAINING MATERIAL quoting the standard, not the standard itself, and IEC 61508 was not read.
       The τ/2 down-time result: SNIPPET LEVEL — corroborated from a retrieved summary of the
       proof-testing literature this run, and CANONICAL in the sense that PFDavg ≈ λ_DU·τ/2 for a 1oo1
       element is textbook; NOT re-derived from a primary source here. The fail-to-start / fail-to-run
       taxonomy: CANONICAL — cited from established knowledge (NUREG/CR-6928-class component data),
       NOT re-verified this run. Do not quote a clause number or a table onward.]

  THE LATENCY ARITHMETIC, so far as this item's own evidence permits it:
    THE CLOSED FORM. For a dormant fault revealed only by a periodic test of interval τ, expected
    detection latency ≈ τ/2. Under the three candidate designs:
      - RUN-COUNT POLLING at daily cadence, WITH the job in scope: τ = 1 day, latency ≈ 12 h.
      - POSITIVE-ACKNOWLEDGEMENT HEARTBEAT, WITH the check registered: latency = scheduled time + grace,
        i.e. sub-day for a daily job, and this is the best of the three — it is event-driven, not polled.
      - EITHER DESIGN WITH THE JOB OUT OF SCOPE: τ = the interval between instrument REBUILDS. That is
        the regime C2A2 was in. It is not a long τ; **it is an undefined τ**, and no latency figure can
        be quoted for it.
    WHAT THE ITEM'S OWN EVIDENCE SUPPORTS AND WHAT IT DOES NOT. The item establishes that at least one
    scheduled fire had passed for each of the three agents. It does NOT establish when each was loaded,
    so the outage duration is UNKNOWN and must not be inferred. **The one thing the record does fix is
    that the detection latency exceeded the interval from load to 2026-08-15, and that this interval was
    determined by a human rewriting the instrument rather than by any scheduled test** — which is the
    literature's definition of an unrevealed failure, and is the file's finding.
    THE BASELINE COMPARISON IS NOT A TREND. 78 OK / 0 FAIL (08-05) versus 78 OK / 5 FAIL (08-15) spans a
    definitional change in what was counted. Per PREMISE-105 and PREMISE-101 the delta is uninterpretable
    as a change in the world, and the identical OK count is the tell: the instrument's scope grew, its
    verdicts did not move. 1086's own closing sentence says this correctly and should be quoted in
    preference to the numbers.

  Strength of support: **Strong** on clauses (i)-(iii), which are established by two independently-built
  production designs whose documentation states the failure mode explicitly and in the same terms as the
  item, plus one verified statement from the Prometheus project's co-founder that an absent series makes
  an alert silently not fire. **Moderate** on clause (iv): the τ/2 result is standard but was verified
  only at snippet level here, and its transfer from constant-hazard hardware to a scheduler that either
  fires or does not is an ANALOGY, not an application — a launchd job at `runs = 0` is not
  exponentially distributed, it is deterministically broken. What survives the transfer robustly is the
  qualitative form: **latency is set by the audit interval, and with no audit it is unbounded.**

  Summary: The monitoring-design half of ASSUMPTION-1086 is well supported, and the striking feature of
  the literature is how routine the fault is. A job that never starts emits nothing, and every monitoring
  design that reads what jobs emit is uncovered for it by construction — Prometheus states this as an
  absent series causing an alert to "silently fail to fire," IEC 61508 states it as a dangerous hidden
  failure that persists "unbeknown to anyone" until a demand, and Cristian's taxonomy (already held at
  PREMISE-141) states it as a crash-class fault requiring a different detector from an omission-class
  one. The design that does detect it — positive-acknowledgement heartbeat — works, and Healthchecks.io's
  documentation names the machine-down and daemon-misconfigured cases in its own detected-failures list;
  but its coverage is exactly the coverage of its registry, because the check must be created BEFORE any
  ping is expected. That relocates the problem rather than solving it, and the relocation is where C2A2
  actually failed: three jobs the scheduler knew about were not in the monitoring instrument's scope at
  all. The third design, manifest reconciliation, is the one that closes that gap, and the SAP
  absent-metrics-operator exists precisely because hand-maintained absence rules are subject to "human
  error, e.g. typo or forgetting" — so the expected set is derived mechanically from the authoritative
  declaration instead. Finally, the reliability literature supplies the quantity nothing in the register
  holds: the detection latency of an unrevealed fault is a property of the test interval, roughly half of
  it, and where no periodic test exists the fault waits for a demand. C2A2 had no periodic test in scope,
  so the latency was set by an instrument rebuild — which is the item's own sentence, "the failures did
  not begin today; the ability to see them did," restated as a standard result.

  Caveats:
    (a) THE EMPIRICAL HALF IS NOT ANSWERED AND THE QUEUE TAG SHOULD STAND. Nothing here says why these
        three did not fire. The candidate causes are materially different and have different fixes: a
        `StartCalendarInterval` whose time has not yet arrived on the wall clock the agent uses; a
        `RunAtLoad`-less agent loaded after its window; a plist that loads but whose program path is
        wrong; a job disabled in the launchd override database; or a machine asleep at every scheduled
        fire. `launchctl print` on each label distinguishes these in one command and is faster than any
        further search. **A never-fired weekly job whose first window has not yet passed is not a fault
        at all**, and the item's own wording ("at least one scheduled fire has passed") is what excludes
        that reading — it should be verified, not assumed.
    (b) THE STRONGEST SOURCES ARE VENDOR AND OSS PRACTICE, NOT PEER REVIEW. Sources 2 and 3 are product
        documentation and a project README. They are excellent evidence of what production practice IS
        and of what its builders say the failure mode IS; they are not measurements of how often it
        occurs, and they carry an obvious interest in the problem being real. No academic measurement of
        never-started-job prevalence or detection latency in production fleets was located this run —
        see Search scope. **This is the same declared negative PREMISE-166 recorded yesterday** ("15a
        searched for and did NOT find an empirical failure rate for self-hosted stall detectors"), and it
        recurring is worth noting: the effectiveness of these remedies remains practitioner consensus.
    (c) THE DOMAIN TRANSFER FROM SIS PROOF TESTING IS IMPERFECT IN ONE SPECIFIC WAY. The τ/2 result
        assumes a constant hazard rate over a population of nominally identical elements with an
        estimable λ_DU. A launchd agent that has never fired is not a stochastic dormant failure — it is
        a deterministic configuration fault present from load, with hazard concentrated entirely at t=0.
        The CONCEPTUAL apparatus transfers (hidden failure, proof test, proof-test coverage, revealed vs
        unrevealed); the numeric form does not, and no PFD figure should be computed for a scheduler.
    (d) MANIFEST RECONCILIATION HAS ITS OWN REGISTRY, AND PREMISE-110 APPLIES TO IT. Deriving the
        expected set from `launchctl list` makes the reconciler depend on launchd being enumerable from
        the reconciler's execution context — which is exactly the scope fault ASSUMPTION-1087 records the
        OLD instrument having, in a different place (it enumerated the calling session's registry and got
        1 task of 70). Moving the enumeration source does not by itself move the monitor out of the
        failure domain, and PREMISE-166 clause (1) still binds: the receiver must sit outside.
    (e) DIAGNOSTIC COVERAGE IS NOT FREE AND THE COST IS ALERT NOISE. PREMISE-110's cost caveat applies
        directly: inverting polarity so that absence is the alarm raises the false-positive rate, and the
        register already carries the 44% figure for organisations with an outage linked to suppressed or
        ignored alerts. A reconciler over 71 registry tasks plus 11 launchd agents will produce
        false FAILs on every intentional disablement unless the manifest carries an expected-state field.
        Apply by criticality, as SIL practice allocates diagnostic coverage — do not convert everything.
    (f) THE THREE DESIGNS ARE NOT ALTERNATIVES; THEY COVER DIFFERENT FAULTS AND THE ITEM SHOULD NOT BE
        READ AS SELECTING ONE. Run-count polling detects never-started FOR JOBS IN SCOPE and is cheap.
        Positive-acknowledgement detects both never-started and started-and-failed FOR REGISTERED JOBS,
        with the best latency, and is the only one of the three that survives the monitoring host dying.
        Manifest reconciliation detects NEITHER directly — it detects the SCOPE GAP, i.e. jobs the other
        two are not watching. The correct reading of 1086 is that C2A2 had the first, lacked the second,
        and lacked the third, and that the third is what made the other two's absence invisible.

  Search scope: VERIFIED and COMPREHENSIVE on the three monitoring designs at the level of
  implementer documentation (sources 1-3 all fetched and read in full). GOOD on the hidden-failure /
  proof-test framing (source 4 read in full at consultancy grade, standard not read). NOT FOUND, and
  each would materially change this file: (i) **ANY MEASURED DETECTION LATENCY FOR NEVER-STARTED
  SCHEDULED JOBS IN A PRODUCTION FLEET** — this was the intake's first question and it is a genuine
  negative result; searches over cron/launchd/systemd/Kubernetes-CronJob monitoring returned design
  guidance and vendor practice but no distribution, no MTTD figure and no prevalence rate. If a
  disposition wants a number, C2A2 will have to measure its own. (ii) The Kubernetes CronJob
  `startingDeadlineSeconds` / missed-schedule literature, which is the closest thing to a formal
  treatment of "a scheduled fire that did not happen" and was identified but not searched. (iii) Airflow
  SLA-miss and data-observability freshness-SLO practice, which would give the reconciliation design a
  second independent instance. (iv) Cristian (1991) itself — cited in PREMISE-141 and marked there as
  NOT independently verified; still not verified, and it is the primary source for clause (i).

  Recommendation: **SUPPORTED (Strong on design clauses i-iii; Moderate on the latency clause iv).**
  Four carries:
    1. **NO NEW PREMISE ON THE PRINCIPLE.** PREMISE-141(1) holds never-started as a distinct class;
       PREMISE-166 holds registration-in-advance; PREMISE-086 holds absence-as-signal. Minting again is
       barred by PREMISE-138(1) and PREMISE-135. The honest reading of 1086 is that it is the SECOND ARM
       of PREMISE-141's three-state model firing for the first time, ten days after the first arm, with
       the remedy still unbuilt — which per PREMISE-151 is incubation, not confirmation.
    2. **THE RESIDUAL WORTH RECORDING IS (R2), THE REGISTRY-COVERAGE GAP.** No premise says that a
       monitoring registry's completeness must itself be derived from the authoritative declaration
       rather than maintained by hand. That is the one clause here the register does not hold, it has a
       named production pattern (source 3), and it is the mechanism by which these three agents were
       invisible while 78 checks reported OK.
    3. **THE LATENCY FRAMING IS THE QUOTABLE RESULT (R3).** Detection latency is a property of the audit
       interval, not of the fault; with no audit in scope it is bounded only by demand or by an
       instrument rebuild. This turns "the ability to see them began today" from an observation into a
       parameter, and it gives PREMISE-086 the thing it currently lacks — a principled basis for
       choosing the age threshold rather than picking one.
    4. **DO NOT REPORT THE 0 → 5 DELTA AS A TREND.** Per PREMISE-105 and PREMISE-101 it spans a
       definitional change and is uninterpretable as a change in the world. The identical OK count on
       both sides is the evidence for that reading, and the correct sentence is the item's own.
