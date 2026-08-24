SEARCH-FOR-PRESUMPTION-819:
  Date searched: 2026-08-17
  Original item: PRESUMPTION-819
  Original statement: [inferred] That an instrument's silence and its clean result are distinguishable
    after the fact. Four agent-level mutes and one check-level no-op today, and the remedy adopted in
    both cases is a clause instructing the component that failed to report its own failure.
  Risk if wrong: **Critical**. Priority: Critical.
  Search question (as queued): watchdog and dead-man's-switch design; liveness versus safety properties;
    why self-reporting monitors fail and why external heartbeats are standard; silent-failure detection
    in scheduled batch systems.

  POLARITY NOTE — WHAT WAS ACTUALLY SEARCHED FOR. The item is worded as the DEFECTIVE belief. The
  proposition searched FOR is the CORRECTIVE CONVERSE, in five clauses:
    (C1) SILENCE AND A CLEAN RESULT ARE FORMALLY INDISTINGUISHABLE FROM ANY FINITE OBSERVATION. This is
         not a tooling shortfall; it is a theorem about the shape of the property.
    (C2) THEREFORE DETECTION MUST BE INVERTED: the signal must be POSITIVELY REQUIRED on a cadence and
         its ABSENCE made the alarm.
    (C3) THE OBSERVER MUST BE EXTERNAL TO THE OBSERVED. A component in a failed state cannot be relied
         upon to emit its own failure report; this is the modelled assumption, not a pessimistic gloss.
    (C4) SELF-DIAGNOSTICS HAVE A BOUNDED, QUANTIFIED COVERAGE AND THE UNDETECTED RESIDUE IS THE
         DANGEROUS PART — found only by an INDEPENDENT off-line test, never by more self-testing.
    (C5) THE SPECIFIC REMEDY 14b OBSERVED — a clause instructing the failing component to report itself
         — IS THE NAMED ANTI-PATTERN in scheduled-job monitoring.
  "SUPPORTED" below means 14b's diagnosis is well grounded, and is equivalently evidence AGAINST the
  presumption as worded.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-819
    Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: the remedy was ADOPTED
      TWICE the same day without anyone noticing it presupposes the thing that failed)
    Transform at each step:
      14b: Inferred from four agent-level mutes and one check-level no-op, plus the shape of the remedy
        adopted in both cases.
      15a: Searched for supporting literature on the corrective proposition; register check first.
    Current status: SUPPORTED (Strong) — BUT SEE THE DUPLICATION WARNING, WHICH IS THE SEVEREST IN
      THIS BATCH

  **DUPLICATION WARNING — READ BEFORE DISPOSITION. SIX ACTIVE PREMISES ALREADY HOLD THIS.**
    - **PREMISE-086** (ACTIVE): a silent multi-day pipeline stall is made visible by surfacing the AGE
      of the last dated PASS/FAIL and ALARMING ON STALENESS — "**absence/staleness is the signal**
      (dead-man's-switch / heartbeat pattern)," with two conditions: alarm on AGE not last-known-value,
      and **the monitor must have its own independent liveness check (monitor-of-monitor) so it cannot
      freeze unnoticed.** Supporting evidence already recorded as 15a SUPPORTED/Strong.
    - **PREMISE-100** (High): a health check that cannot execute **reports as passing rather than as
      absent**; conflation produces false-green proportional to the number of inoperable checks.
    - **PREMISE-110**: generalises 100 — "a monitor's pass state is systematically reachable while its
      subject is dead, and **monitor/subject independence in this fleet is ASSERTED RATHER THAN
      ENGINEERED**."
    - **PREMISE-141**: a run that starts is not a run that reports.
    - **PREMISE-166** (2026-08-15): a monitor's independence from its subject is a QUANTIFIED,
      PLACEMENT-DEPENDENT property.
    - **PREMISE-169** (2026-08-16, ONE DAY BEFORE THIS FILE): **THE REGISTRY IS THE COVERAGE.** A
      scheduled job that never started emits nothing, so it is "invisible BY CONSTRUCTION to every
      monitor whose input is the job's own output"; heartbeat designs detect a never-started job ONLY
      for jobs already registered with the receiver; **an absent series is read as "everything is fine"
      unless the expected set is PRE-INITIALISED**; detection latency is ~half the audit interval and
      unbounded where no audit exists. Its sources (PromLabs on missing Prometheus series;
      Healthchecks.io; SAP absent-metrics-operator) were **fetched and read in full one day ago.**
  Grep terms used against `validated_premises.md`: silent, watchdog, heartbeat, liveness, dead-man,
  self-report, report its own, no-op, cannot execute, inoperable, false-green, mute, absence, staleness,
  monitor. DECLARED LIMITATION: string grep at ~56% recall (ASSUMPTION-1052) — LOWER BOUND.
  **NO NOVELTY-FLAG.** This is one of the most thoroughly established results in the fleet's register.
  **THE RESIDUAL, and the only reason this file was worth writing:** every one of the six premises is
  about a JOB or a CHECK — a scheduled unit with a runtime, an exit code and a registry entry.
  **PRESUMPTION-819's four instances are AGENT-LEVEL MUTES: a section of a report that was simply not
  emitted.** PREMISE-169 names the scheduled-task roster as the artefact that must be independently
  maintained. **No premise names the REPORT TEMPLATE as a registry.** The extension is exact and cheap:
  a report's expected-sections manifest is the same object as Prometheus's pre-initialised expected
  series, and an absent section must render as ABSENT rather than not render at all.

  Supporting evidence found: Yes

  Sources:
    1. Alpern, B. & Schneider, F.B. (1985), "Defining Liveness," *Information Processing Letters*
       21(4):181-185; and (1987), "Recognizing Safety and Liveness," *Distributed Computing* 2:117-126.
       Following Lamport, L. (1977), "Proving the Correctness of Multiprocess Programs," *IEEE TSE*
       SE-3(2):125-143. — **The formal core of clause (C1), and the reason 819 is a theorem rather than
       an observation.** A SAFETY property is one that, if violated, is **already refuted by some FINITE
       PREFIX** of the trace — "something bad has happened," and the finite log proves it. A LIVENESS
       property is one that **can NEVER be definitively refuted by any finite prefix**, because every
       finite trace is a prefix of some trace that satisfies it. "The instrument will report" is a
       liveness property. Therefore **no finite observation of the log can distinguish "has not failed"
       from "has not run yet" from "will never run."** This is exactly 819's claim, and it is the
       strongest form available: the distinguishability the presumption assumes is not merely absent
       from the current implementation, it is unobtainable from output alone by any implementation. The
       corollary is the one that matters operationally: **to make silence detectable you must convert
       the liveness question into a safety question** by adding a DEADLINE — "no signal by time T" is
       finitely refutable. That conversion is precisely what a watchdog timer is.
       [CANONICAL + SNIPPET. The papers are cited from established knowledge. The finite-prefix
       characterisation, the limit-closed/dense metric formulation, and the co-safety/co-liveness duals
       were confirmed this run against retrieved summaries (Roșu 2012, "On Safety Properties and Their
       Monitoring," *Scientific Annals of Computer Science* 22(2):327-365, located as PDF; Deutschbein's
       UNC lecture notes on Alpern & Schneider; the Springer chapter "Refining the Safety–Liveness
       Classification of Temporal Properties According to Monitorability," Havelund et al.). **No primary
       paper was opened in full.** The register already carries this family: PREMISE-046's supporting
       line cites "Safety vs liveness properties (Hillel Wayne; Lamport) — 'no error' is a weak safety
       signal, not the liveness property that the change was staged."]
    2. IEC 61508-2, *Functional safety of E/E/PE safety-related systems*, on DIAGNOSTIC COVERAGE and
       PROOF TESTING. — **The support for clause (C4), and the quantitative form of "self-reporting is
       not enough."** Diagnostic coverage (DC) is defined as the fraction of DANGEROUS failures detected
       by automatic ON-LINE diagnostic tests. The standard's whole architecture is built on the fact
       that DC < 1: **"the real concern is the presence of dangerous UNDETECTABLE failures, which can be
       identified only through an OFF-LINE proof test"** — that is, by a mechanism of a DIFFERENT KIND,
       run by a different agency, at a declared interval. And where proof-test coverage is itself below
       100%, "undetectable dangerous failures can potentially occur that will NEVER be detected by
       testing," with latent-failure probability **accumulating with time regardless of the proof-test
       interval**. Transferred to 819: adding a clause instructing an agent to report its own failure
       raises DC by some unmeasured amount and does nothing at all to the residue; the residue is
       reached only by an external reader with an independent view.
       [SNIPPET LEVEL — the IEC 61508-2 text at cechina.cn, GT Engineering's proof-test/DC explainer,
       Risknowlogy's fault-detection article, and an ScienceDirect paper on proof-test interval and
       coverage were located this run and read at retrieved-summary level. **The standard was not
       opened.** PREMISE-169 already records IEC 61508 proof-test-interval material at SNIPPET LEVEL, so
       this adds depth of argument but not depth of verification.]
    3. Watchdog-timer and fail-silent design in dependable embedded systems — surveyed in "Dependability
       in Embedded Systems: A Survey of Fault Tolerance Methods and Software-Based Mitigation
       Techniques" (arXiv:2404.10509). — **The support for clause (C3).** The FAIL-SILENT property is
       defined as the guarantee that **no output is provided in the event of failure** — the failure mode
       is designed to BE silence, which is why silence must be given an independent meaning. The
       watchdog is the standard answer: an independent timer that must be periodically reset by the
       software, and **if the software fails to reset it within the window, the watchdog ASSUMES a fault
       and acts.** Note the direction of the inference — the watchdog does not wait to be told; it
       treats non-reset as positive evidence. This is the architectural embodiment of clause (C2).
       [SNIPPET LEVEL — the arXiv survey, an EDN article on watchdogs for fault tolerance, and an
       automotive fail-operational/fail-degraded/fail-safe taxonomy paper (arXiv:2106.11042) were
       located and read at retrieved-summary level; none opened in full.]
    4. Dead-man's-switch / heartbeat monitoring practice for scheduled jobs (Healthchecks.io-class
       services; the cron-monitoring literature). — **The support for clause (C5), and the direct
       refutation of the remedy adopted twice today.** The practitioner statement of the problem is
       flat: "**Cron monitoring usually fails because the signals are INTERNAL** ... If the cron job
       itself never runs, there's no code executing to report the failure." The pattern inverts the
       direction of reporting — the process pings an external receiver on cadence, and the RECEIVER
       alarms when the ping stops. And the placement rule is explicit: "**use an external monitoring
       service, NOT one running on the same server as your cron jobs. If the server goes down, both your
       jobs and your monitoring go down together — defeating the purpose.**" A clause in an agent's own
       prompt instructing it to announce its own muting is the maximally co-located monitor: it shares
       not just a host with its subject but an execution context and a model instance.
       [SNIPPET LEVEL this run — cron-monitoring vendor documentation and explainers (watchflow,
       crontap, UpDog, AppStatus, Drumbeats, Nurbak) located and read at retrieved-summary level; **none
       opened in full, and all are vendor marketing content.** GRADE ACCORDINGLY. The register holds a
       better-verified version of the same point: **PREMISE-169's Healthchecks.io and PromLabs citations
       were fetched and read in full on 2026-08-16**, including the finding that Prometheus reads an
       absent series as "everything is fine" and the remedy of pre-initialising the expected set.]
    5. SAP `absent-metrics-operator` (README), via PREMISE-169. — Cited because it is the one located
       source that names the FAILURE MODE OF THE REMEDY: hand-maintained absence rules fail through
       "**typo or forgetting**," so the expected-set manifest must be DERIVED from the deployment
       manifest rather than written. This bears directly on the extension recommended below — an
       expected-sections list for a report is a hand-maintained absence rule and inherits exactly this
       defect unless it is generated from the agent roster.
       [REGISTER-HELD — recorded in PREMISE-169 as VERIFIED (fetched and read) on 2026-08-16. NOT
       re-fetched this run. Counted as reinforcing, not as independent evidence.]

  Strength of support: **Strong** on (C1), (C3) and (C5); **Moderate-to-Strong** on (C4);
    **Strong** on (C2) but ALREADY REGISTER-HELD at Strong (PREMISE-086), so it adds no new weight.
    (C1) is the strongest clause in this batch: it is a proved characterisation, not an empirical
    regularity, and it settles the item's central question in the negative with no scope conditions.
    (C3) and (C5) rest on convergent design practice across two unrelated domains (safety-critical
    embedded systems; scheduled-batch operations), which is good structural evidence, but the sources
    reached this run are surveys and vendor pages rather than primary standards.

  Summary: The corrective proposition is strongly supported, and on its central clause the support is
  formal rather than empirical. Alpern and Schneider's characterisation makes "the instrument will
  report" a LIVENESS property, and liveness properties can never be refuted by any finite prefix of a
  trace — so no finite record can distinguish an instrument that stayed silent from one that ran clean.
  The presumption is therefore not merely unmet by the current tooling; it is unmeetable from output
  alone. Every discipline that has confronted this has responded the same way: convert the liveness
  question into a safety question by attaching a deadline, and put the deadline in a party that is not
  the subject. Watchdog design formalises this — fail-silent is the MODELLED failure, so non-reset of an
  independent timer is taken as positive evidence of fault. Cron-monitoring practice states the
  refutation of today's remedy directly: if the job never runs there is no code executing to report the
  failure, and a monitor co-located with its subject dies with it. IEC 61508 supplies the quantitative
  version — self-diagnostics have a measured coverage below one, and the undetected residue is reached
  only by an independent off-line test, with latent-failure probability accumulating regardless of
  interval. Where this file must stop short of the item is that six ACTIVE premises already hold this
  result, one minted yesterday. The genuine residual is narrow: all six govern JOBS and CHECKS, and
  today's instances are MISSING REPORT SECTIONS. PREMISE-169's "pre-initialise the expected set" needs
  to be extended from the scheduled-task roster to the report template.

  Caveats:
    (a) THIS IS SIX PREMISES RESTATED AND THAT SHOULD DRIVE THE DISPOSITION. PREMISE-151 applies:
        repeated disclosure of an unremediated condition normalises it rather than resolving it. The
        honest reading of 819 is not "we have learned something" but "we hold this at High confidence
        and did not apply it," which makes this a PROPAGATION failure, not a validation gap — the same
        diagnosis the 2026-08-13 batch reached about the fleet's binding constraint.
    (b) THE REGRESS DOES NOT TERMINATE, AND PRETENDING IT DOES IS THE SECOND-ORDER VERSION OF THE SAME
        ERROR. An external heartbeat receiver is itself a component that can go silent. PREMISE-086
        already requires a monitor-of-monitor; PREMISE-169's own 15b line records the resolution —
        **the regress terminates only by DIFFERING IN KIND**, which is why 169 names the registry rather
        than a better monitor. Any remedy adopted from this file that is "another agent checks the first
        agent" reproduces the fault at one remove.
    (c) THE EXPECTED-SET MANIFEST IS A HAND-MAINTAINED ABSENCE RULE AND FAILS BY OMISSION. Source 5's
        "typo or forgetting" is the exact failure. An expected-sections list that is written rather than
        DERIVED from the agent roster will silently omit a newly-added agent, and that agent's mute will
        then be invisible in precisely the way today's were. If this is built, it must be generated.
    (d) **THE DOMINANT DOMAIN-TRANSFER PROBLEM, AND IT IS SPECIFIC TO LLM AGENTS: THE WATCHDOG
        LITERATURE ASSUMES SILENCE IS THE FAILURE MODE. FOR AN LLM AGENT IT USUALLY IS NOT.** A
        heartbeat, a section-presence manifest and a dead-man's switch all detect ABSENCE. They are
        completely blind to the far more likely LLM failure: a section that IS emitted, IS well-formed,
        and is vacuous, hallucinated, or a restatement of yesterday. Four mutes are the visible tail of
        that distribution. The correct instrument for the invisible bulk is not a watchdog at all — it is
        closer to PREMISE-159 (a repeated identical instrument reading obliges a LIVENESS TEST OF THE
        READER) and PREMISE-162 (a run auditing its own instrument yields a catch count with no
        denominator). **A remedy scoped to presence would close the small half of the exposure while
        creating a green signal over the large half**, which is PREMISE-100's failure mode rebuilt.
    (e) DETECTION LATENCY IS NOT ZERO AND MUST BE STATED. PREMISE-169's analytic result — latency is
        approximately half the audit interval — applies here unchanged. A daily report gives a mean
        half-day exposure and a worst case of a full day. Neither 169 nor this file has a MEASURED
        latency or prevalence figure; PREMISE-169 records that BOTH search directions independently
        failed to locate one, and this run reproduces that negative for a third time.
    (f) SOURCE INDEPENDENCE AND VERIFICATION DEPTH. **No primary source was fetched and read in full
        this run.** Source 1 is canonical-plus-summary; sources 2 and 3 are surveys; source 4 is vendor
        marketing; source 5 is register-held from another agent's verified read. Per PREMISE-132, the
        citation count overstates the evidential depth. The one clause that does NOT depend on this —
        (C1) — is a mathematical characterisation and is safe.

  Search scope: GOOD on the theory and on operational practice; SHALLOW on verification. Searched:
    Alpern/Schneider/Lamport safety-liveness and its monitorability refinements; IEC 61508 diagnostic
    coverage and proof testing; watchdog-timer and fail-silent embedded design; dead-man's-switch and
    heartbeat monitoring for cron and scheduled batch. NOT SEARCHED, and each would materially change
    this file: (i) **RUNTIME VERIFICATION AND MONITORABILITY proper** — the Bauer/Leucker/Schallhart
    result on which properties are monitorable from finite traces is the precise formal answer to "what
    CAN be detected after the fact," and was seen in a result title but not pursued; (ii) **SRE
    literature on symptom-based versus cause-based alerting** and on the "perceived-liveness trap,"
    which bears on caveat (d); (iii) **any empirical prevalence or detection-latency study for silent
    scheduled-job failure** — sought and NOT FOUND for the third time across three agents, which is now
    a well-observed literature gap and should be recorded as such; (iv) **LLM-agent-specific silent-
    degradation detection** (vacuous-output detection, response-collapse monitoring), which is where
    caveat (d) says the real exposure lies and which this run did not touch at all.

  Recommendation: **SUPPORTED (Strong)** for the corrective proposition; equivalently NO-SUPPORT-FOUND
  for the presumption as worded. **Disposition should be a SCOPE-EXTENSION OF PREMISE-169 FROM THE JOB
  ROSTER TO THE REPORT TEMPLATE — no new premise.** Four carries:
    1. NO NEW MINT. Six ACTIVE premises hold this, one from yesterday. Re-minting is barred by
       PREMISE-138(1) and PREMISE-135, and per the 2026-08-13 precedent (PRESUMPTION-781/783) an
       ENFORCEMENT gap against held premises is dispositioned as a REVISE, not a mint.
    2. THE EXTENSION IS ONE SENTENCE. PREMISE-169 says the registry of what OUGHT to exist is the upper
       bound on coverage. Extend "registry" from the scheduled-task roster to **the report's
       expected-sections manifest**, GENERATED from the agent roster (caveat c), so that an absent
       section renders as an explicit ABSENT row rather than not rendering.
    3. WITHDRAW THE SELF-REPORTING CLAUSE RATHER THAN KEEPING IT AS BELT-AND-BRACES. It is not merely
       insufficient; it is the co-located monitor the practice literature names as defeating the
       purpose, and leaving it in place produces the appearance of coverage. If it is kept, it must be
       scored at ZERO in any coverage claim — the same treatment PREMISE-131 requires for a warning on
       a dark channel.
    4. **SCOPE THE CLAIM NARROWLY TO PRESENCE, AND SAY SO OUT LOUD (caveat d).** A section-presence
       manifest detects mutes and nothing else. The larger exposure — a section present and vacuous — is
       untouched and belongs to PREMISE-159/162. Any adoption that lets "all sections present" render
       green would rebuild PREMISE-100's false-green one level up, and that is the specific way this
       remedy would fail.
