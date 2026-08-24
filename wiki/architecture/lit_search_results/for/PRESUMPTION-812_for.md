SEARCH-FOR-PRESUMPTION-812:
  Date searched: 2026-08-16
  Original item: PRESUMPTION-812
  Original statement: [inferred] That the detection layer is the part worth building; closure is
    downstream and easy.
  Risk if wrong: High.

  POLARITY NOTE — what was searched FOR. The presumption is worded as the DEFECTIVE belief ("detection
  is the valuable half; closure follows cheaply"). The proposition searched FOR is the CORRECTIVE
  CONVERSE, in four clauses: (i) that DETECTION WITHOUT AN ACTING ELEMENT IS NOT A PROTECTION LAYER
  AND EARNS NO CREDIT, a position encoded structurally in functional-safety standards rather than
  offered as advice; (ii) that THE CLOSURE GAP IS MEASURED AND LARGE in every domain that has counted
  — clinical alarms, security operations, vulnerability management, internal audit — and that in the
  best-measured case remediation capacity is roughly CONSTANT regardless of how much is detected;
  (iii) that ADDING DETECTION WITHOUT CLOSURE CAPACITY ACTIVELY DEGRADES THE DETECTION ALREADY IN
  PLACE, through desensitisation and through deliberate disablement, so the marginal detector can have
  NEGATIVE value; and (iv) that quality and safety management SEPARATE CORRECTION FROM CORRECTIVE
  ACTION and require effectiveness verification, i.e. the disciplines that formalised this put closure
  inside the loop rather than downstream of it. "SUPPORTED" below means 14b's worry is well grounded,
  and is equivalently evidence AGAINST the presumption as worded.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-812
    Item type: PRESUMPTION (unstated — surfaced by inference; extra weight per the provenance
      protocol, and unusually well earned here: the designers proposed detectors all day without any
      of them noticing that every proposal was a detector)
    Transform at each step:
      14b: Classified every remedy proposed today and found all of them to be detectors.
      15a: Searched for supporting literature on the corrective proposition; sought a QUANTIFIED
        closure gap, which the register does not hold; and sought an ACCEPTANCE TEST that could be
        applied to a proposed remedy, which is the practically useful output.
    Current status: SUPPORTED (Strong) — with a heavy duplication warning.

  **DUPLICATION WARNING — READ BEFORE DISPOSITION.** PRESUMPTION-812's core claim is **PREMISE-102**,
  minted 2026-07-19 at **HIGH** confidence, thirteen months of runs ago in register time: "**FAIL-LOUD
  IS AN ACT OF REPORTING, NOT AN ACT OF REMEDIATION.** Where the notified channel has demonstrated
  zero throughput, repeated identical non-processing converts a one-time signal into an undecided
  standing policy of non-coverage; the loudness of the report is not evidence that anything is
  receiving it." That is 812, verbatim in substance. It is reinforced by **PREMISE-143 clause (1)**,
  which supplies the mechanism by which detection actively suppresses repair (Tucker & Edmondson's
  "illusory equilibrium"), and by **PREMISE-151** (High): "repeated disclosure of an unremediated
  condition NORMALISES it rather than resolving it... the disclosure record is evidence of INCUBATION,
  not of management." A disposition that mints a new premise here would be re-minting PREMISE-102,
  which PREMISE-138(1) and PREMISE-135 bar. **And note the reflexive point, which is the actual
  finding: PRESUMPTION-812 is PREMISE-102 producing its own predicted output. A fleet holding "fail-
  loud is not remediation" at High confidence for a month, and then spending a day proposing nothing
  but detectors, is the premise being reported rather than enforced. Per PREMISE-151 the second
  recording is the thing to worry about.**

  REGISTER CHECK (performed BEFORE writing this file):
    Grepped `validated_premises.md` for: "alert fatigue", desensiti*, "acceptance decay", remediat*,
    closure, "close the loop", detector, escalation, disclosure, flag, effector.
    Found and read in full:
      - **PREMISE-102** (2026-07-19, ACTIVE, **High**) — see DUPLICATION WARNING. Its Applicable-to
        already names "any agent convention of FLAGGING IN LIEU OF ACTING," which is 812's exact
        observation about the day's remedies.
      - **PREMISE-143 clause (1)** (2026-08-05, ACTIVE, Moderate) — **the mechanism, and it is
        stronger than 812's own claim.** "METRIC INVERSION... reliable catching of small failures
        ACTIVELY SUPPRESSES SYSTEMIC REPAIR, because each successful catch removes the pressure that
        would have justified changing the instrument — Tucker & Edmondson's 'illusory equilibrium,' in
        which first-order problem solving dominates, the organisation LOOKS HEALTHY and its
        effectiveness erodes." Its clause (3) also supplies the object: an INSTRUMENT-DEFECT RECORD
        that outlives and is NOT CLOSABLE BY the run that filed it. And 15a's own note in 143 is
        directly 812: "every source that decomposes the process places DETECTION AT THE FRONT OF A
        LONGER CHAIN — Phimister's seven stages, ISO 9001:2015 cl. 10.2's split between a CORRECTION
        (fix the output) and a CORRECTIVE ACTION (fix the cause, and verify effectiveness)."
      - **PREMISE-151** (2026-08-10, ACTIVE, High) — quoted above; Vaughan's normalisation of
        deviance, cited independently by BOTH directions.
      - **PREMISE-138 clause (2)** (ACTIVE) — a flag raised by a layer that cannot act MUST NAME THE
        ACTOR WHO CAN and leave the channel; clause (1) — in-channel repetition with no effector is
        not a remedy. This is the register's existing acceptance test and 812 is its violation.
      - **PREMISE-121** (ACTIVE) — **the quantified harm mechanism for clause (iii), already held.** A
        reviewer's per-item cost is not constant and capacity does not scale with production: override
        rates 49-96%, acceptance falls as volume and complexity rise, and "DESENSITISATION GENERALISES
        — true positives are discounted alongside false ones. Therefore EACH ADDITIONAL
        CORRECTLY-ARGUED ITEM CAN LOWER THE PROBABILITY THAT ANY ITEM IS ACTED ON." Grounded on the
        clinical-decision-support override literature (Ancker et al. 2017; Nanji et al.). Note its
        explicit exclusion: decision fatigue and the parole-board result are STRUCK and must not be
        argued from.
      - **PREMISE-119** (ACTIVE) — production and judgment are not independently schedulable;
        backpressure is a correctness requirement; and the SEQUENCING REQUIREMENT that where service
        rate is ZERO "the steady-state relations do not hold at all and no reduction in arrivals bounds
        the queue." Directly on point: a detector feeding an absent consumer.
      - **PREMISE-155 FORM CONDITION** (2026-08-13, ACTIVE) — "report artefact AGE as a DISPLAYED
        NUMBER rather than adding a pass/fail freshness alert per artefact per path. Freshness is a
        high-volume alert class and MOVING FROM ALERTING TO DISPLAY gets the signal without the
        acceptance decay." The register already has a design rule derived from clause (iii).
      - **PREMISE-118** (ACTIVE) — naming a defect in an instrument does not license continued use; it
        triggers an obligation to CONTAIN / ASSESS IMPACT / FIX CAUSE / VERIFY, including a
        RETROSPECTIVE impact assessment. "Noting the condition and continuing is a recognised serious
        finding."
      - **PREMISE-164** (2026-08-14, ACTIVE) — durability is a property of ADDRESSING; explicitly
        warns against "building a register with no scheduled reader," and carries GAO-19-686 (35% of
        aviation recommendations open >10 years not fully implemented absent a statutory deadline).
      - **PREMISE-166 / PREMISE-167** (2026-08-15, ACTIVE) — monitor placement and progress-binding;
        and 15b's decisive operational warning in 167, that ESCALATION-AS-LOCK with a human gate dark
        twelve days "converts every handed-up defect into an unfixable one."
    CONCLUSION OF THE CHECK: **NEAR-TOTAL OVERLAP, AND THE CORE CLAIM IS A SUBSTANTIVE DUPLICATE OF A
    HIGH-CONFIDENCE PREMISE. NO NOVELTY-FLAG.** Ten ACTIVE premises bear.
    DECLARED LIMITATION: this was a STRING GREP, measured at ~56% recall (ASSUMPTION-1052). The list
    above is a **LOWER BOUND**, and ten hits argues strongly for a narrow disposition.

  RESIDUAL — what 812 contains that the register does not:
    (R1) **A QUANTIFIED CLOSURE GAP.** PREMISE-102 says fail-loud is not remediation. It attaches no
         number. The literature located here attaches several, and the most useful is that remediation
         capacity is roughly CONSTANT in the size of the detected population — which converts 812 from
         a caution into an arithmetic constraint on how much detection is worth building.
    (R2) **AN ACCEPTANCE TEST FOR A PROPOSED REMEDY, TAKEN FROM A STANDARD.** PREMISE-138(2) requires
         naming an actor. Functional-safety practice supplies a sharper and more mechanical form: a
         safety instrumented function comprises SENSOR, LOGIC SOLVER and FINAL ELEMENT, and something
         with no final element IS NOT A PROTECTION LAYER AND EARNS NO CREDIT. "Name the final element"
         is a one-line test applicable to every remedy the fleet proposes, and it is not in the
         register.
    (R3) **THE DISABLEMENT FINDING, WHICH IS STRONGER THAN THE DESENSITISATION FINDING.** PREMISE-121
         holds that acceptance decays under load. Source 1 holds something worse and it is measured in
         deaths: the single largest contributing factor across 98 alarm-related sentinel events was
         ALARM SIGNALS INAPPROPRIATELY TURNED OFF — a detector that was built, that worked, and that
         the operators disabled. The failure mode of an over-detected system is not fatigue, it is
         removal.

  Supporting evidence found: Yes

  Sources:
    1. The Joint Commission, *Sentinel Event Alert*, Issue 50 (8 April 2013), "Medical device alarm
       safety in hospitals." — **The strongest single source for clauses (ii) and (iii), and it
       supplies R3.** Read in full. Five findings, all read directly. (a) THE DETECTION LAYER IS
       SATURATED AND THE FIGURE IS EXTREME: alarm signals per patient per day "can reach several
       hundred," and "IT IS ESTIMATED THAT BETWEEN 85 AND 99 PERCENT OF ALARM SIGNALS DO NOT REQUIRE
       CLINICAL INTERVENTION." (b) THE CONSEQUENCE IS NAMED AND IT IS NOT MERELY INEFFICIENCY: "As a
       result, clinicians become desensitized or immune to the sounds... In response to this constant
       barrage of noise, clinicians may TURN DOWN THE VOLUME OF THE ALARM, TURN IT OFF, OR ADJUST THE
       ALARM SETTINGS OUTSIDE THE LIMITS THAT ARE SAFE AND APPROPRIATE FOR THE PATIENT — all of which
       can have serious, often fatal, consequences." (c) **THE DECISIVE STATISTIC FOR 812.** Across 98
       alarm-related events reported January 2009 to June 2012 (80 deaths, 13 permanent losses of
       function), the enumerated major contributing factors were: "Absent or inadequate alarm system
       (30); Improper alarm settings (21); Alarm signals not audible in all areas (25); **ALARM
       SIGNALS INAPPROPRIATELY TURNED OFF (36)**." The RESPONSE-SIDE factor is the LARGEST single
       category and exceeds detector-absence by 20%. In the domain with the most instrumented
       detection layer in existence, the leading contributor to fatal outcomes is that the detection
       was switched off. (d) THE NARRATIVE CASE IS A PURE CLOSURE FAILURE: a 60-year-old ICU patient
       whose rising heart rate and falling oxygen set off alarms, to which "staff responded only after
       ONE HOUR, when a critical alarm condition signaled that the patient had stopped breathing"; the
       Alert calls this "a failure to respond to appropriate alarm signals in a timely manner" and
       "a significant problem that occurs every day, in many hospitals." (e) THE REMEDY SET IS
       RESPONSE-SIDE AND GOVERNANCE-SIDE, NOT DETECTOR-SIDE. Of eleven numbered recommendations, the
       first is "leadership ensures that there is A PROCESS FOR SAFE ALARM MANAGEMENT AND RESPONSE";
       others cover inventory, guidelines for settings, tailoring per patient, maintenance, training,
       acoustics, and a cross-disciplinary team. **Recommendation 9 is 812 stated as policy: "RE-
       ESTABLISH PRIORITIES FOR THE ADOPTION OF ALARM TECHNOLOGY; the priority-setting process should
       drive technology adoption RATHER THAN ALLOWING TECHNOLOGY TO DRIVE THE PROCESS."** Not one
       recommendation is "build a better detector." [**VERIFIED this run — the Alert PDF was fetched
       and read in full.** All quotations, the 98/80/13/5 event breakdown and the four
       contributing-factor counts are read directly. The Alert's OWN caveat is carried: sentinel-event
       reporting is voluntary and "these data are not an epidemiologic data set and no conclusions
       should be drawn about the actual relative frequency of events or trends over time" — so the
       36-versus-30 ordering is indicative of what gets reported, NOT a measured population
       proportion, and must not be quoted as one. The 85-99% figure is itself attributed by the Alert
       to AAMI *Horizons* (Spring 2011), which was NOT retrieved.]
    2. IEC 61511 / IEC 61508 functional-safety architecture: a SAFETY INSTRUMENTED FUNCTION comprises
       a SENSOR subsystem, a LOGIC SOLVER subsystem, and a FINAL ELEMENT (actuator) subsystem; the
       safety instrumented system "includes all devices necessary to carry out each SIF FROM SENSOR(S)
       TO FINAL ELEMENT(S)." — **The standards-level support for clause (i), and the acceptance test
       of R2.** The relevant fact is architectural, not advisory: the standard does not define a
       protection layer as something that detects. It defines it as a complete loop that detects,
       decides AND ACTS, and a function missing its final element is not a SIF at all — it is
       instrumentation. In LOPA terms, an arrangement that cannot bring the process to a safe state
       independently earns NO credit as an independent protection layer, which means an
       inventory of detectors and an inventory of protection layers are different inventories and
       adding to the first does not add to the second. Applied to 812: every remedy proposed on
       2026-08-15 was a sensor; none named a final element; and by this standard none of them is a
       protection layer. **This yields a one-line acceptance test that can be applied at proposal
       time: NAME THE FINAL ELEMENT.** [SNIPPET LEVEL — the IEC 61511 standard itself was NOT
       retrieved and no clause number is cited. The sensor / logic-solver / final-element architecture
       was read from four independent secondary and practitioner sources (an IChemE conference paper,
       two functional-safety consultancies, the Wikipedia entry). The architecture is CANONICAL and
       uncontested; the LOPA no-credit-for-common-cause point is carried forward from PREMISE-166,
       where 15b cited LOPA/CCPS, and was NOT independently verified here.]
    3. Cyentia Institute / Kenna Security, *Prioritization to Prediction*, Volume 3: "Winning the
       Remediation Race" (and the series' later volumes). — **The quantified capacity constraint of
       R1, and the sharpest available statement of 812.** The headline finding: **a typical
       organisation, REGARDLESS OF THE NUMBER OF ASSETS OR VULNERABILITIES IN ITS ENVIRONMENT, has the
       capacity to remediate about ONE OUT OF EVERY TEN open vulnerabilities in a given month**; an
       alternative measurement across hundreds of companies puts it at ~15.5% per month. The study
       used survival analysis across roughly 300 organisations of varying type and size. The clause
       that matters for 812 is "regardless of the number": **remediation capacity is approximately
       CONSTANT while detection capacity scales freely with tooling.** It follows arithmetically that
       beyond a modest point, additional detection does not reduce risk — it only lengthens the queue
       and changes which 10% gets done, which is precisely 14b's worry expressed as a rate.
       [SNIPPET LEVEL — the report's library listing at library.cyentia.com and the "Pithy P2P"
       summary page were LOCATED this run; the report was NOT fetched or read. The one-in-ten figure
       was read from two independent summaries of the same underlying report, so treat it as ONE
       source, not two. **THIS IS VENDOR-ORIGINATED RESEARCH** — Kenna Security sells vulnerability
       prioritisation, and the finding is favourable to that product. It is unusually well documented
       for vendor research (named method, stated sample) but it is not peer-reviewed and must not be
       quoted as an independent result.]
    4. Security-operations closure data, 2025 vintage: ~40% of alerts are never investigated (Software
       Analyst Cyber Research Group, *2025 AI SOC Market Landscape*); 61% of security teams admit
       having ignored alerts that later proved critical; the 2025 SANS Detection & Response Survey
       reports 73% of teams naming false positives as their top detection challenge; ~76% of
       organisations cite alert fatigue as a primary SOC concern. — Corroborates clause (ii) in a
       second instrumented domain and shows the same shape: detection volume is not the constraint,
       triage capacity is. [SNIPPET LEVEL, **AND THIS IS THE WEAKEST-PROVENANCE MATERIAL IN THE FILE
       AND MUST NOT BE QUOTED AS RESULTS.** Every figure above comes from VENDOR MARKETING PAGES or
       from vendor summaries of surveys I did not retrieve. Two of the figures (40% and 62% "never
       properly investigated") are mutually inconsistent and appear on competing vendors' sites. The
       SANS survey is a real recurring instrument but was NOT retrieved. Use this cluster as
       DIRECTIONAL EVIDENCE THAT A LARGE CLOSURE GAP IS WIDELY REPORTED, and for nothing else.]
    5. The Institute of Internal Auditors, *Global Internal Audit Standards* (effective January 2025);
       with practitioner guidance on remediation tracking. — **The governance-side confirmation, and
       an interesting structural fact: the profession instruments CLOSURE, not detection.** The
       Standards require chief audit executives to track the MANAGEMENT ACTION PLAN CLOSURE RATE as
       part of performance reporting — i.e. the metric the discipline mandates is not findings raised
       but findings CLOSED. Practitioner sources add the metrics that go with it (closure cycle time,
       overdue action-point ratio, percentage of findings RE-OPENED AFTER CLAIMED CLOSURE) and report
       that over 60% of organisations receiving audit findings face at least one REPEAT finding within
       two years. [SNIPPET LEVEL — **the IIA Standards text was NOT retrieved** and the closure-rate
       requirement is asserted from a practitioner summary; the 60%-repeat figure comes from a SINGLE
       practitioner source and must not be quoted as a result. Note PREMISE-144 already cites the
       IIA's external quality assessment requirement, so the IIA is not an independent source in this
       register.]
    6. ISO 9001:2015 clause 10.2 — the split between a CORRECTION (fix the output) and a CORRECTIVE
       ACTION (fix the cause), with a required review of the EFFECTIVENESS of the action taken; and
       Phimister's seven-stage near-miss management decomposition, in which identification is the
       first of seven. — Clause (iv). **ALREADY REGISTER-HELD via PREMISE-143's 15a return and
       therefore NOT INDEPENDENT CORROBORATION** (PREMISE-111). [CANONICAL — carried forward, NOT
       re-verified this run.]
    7. GAO-19-686 — 35% of aviation safety recommendations open more than ten years were not fully
       implemented absent a statutory deadline. **ALREADY REGISTER-HELD via PREMISE-164 (15b);
       NON-INDEPENDENT.** Recorded because it is the register's own closure-gap datum and 812 should
       cite it rather than the vendor material above. [CANONICAL WITHIN THIS REGISTER — NOT
       re-verified.]

  Strength of support: **Strong.** Clause (i) is encoded in the architecture of a functional-safety
  standard rather than urged. Clause (ii) is measured in four independent domains, and in the
  best-documented case (source 3) the measurement takes the strongest available form — capacity
  constant in detected volume. Clause (iii) has a verified primary source in which the largest
  contributing factor to 98 fatal and near-fatal events is the deliberate disabling of a working
  detector. Clause (iv) is standardised. The grade is held at Strong rather than higher because the
  two quantitative anchors (sources 3 and 4) are vendor-originated, the standard itself was not read,
  and the one fully-verified source carries an explicit warning against reading its counts as
  population proportions.

  Summary: The corrective proposition is strongly supported, and the most useful thing located is that
  the domain with the most heavily instrumented detection layer in existence has published its own
  post-mortem on precisely 812. The Joint Commission reports that 85 to 99 percent of clinical alarm
  signals do not require intervention, that the predictable consequence is clinicians turning the
  volume down, turning alarms off, or setting limits outside safe ranges, and that across 98 alarm-
  related sentinel events — 80 of them deaths — the single largest contributing factor was ALARM
  SIGNALS INAPPROPRIATELY TURNED OFF, at 36, ahead of absent-or-inadequate alarm systems at 30. The
  narrative case is an hour of non-response to an alarm that fired correctly. And the Alert's eleven
  recommendations are almost entirely about response, governance, settings, training and inventory;
  recommendation 9 states 812 as policy — the priority-setting process should drive technology
  adoption rather than allowing technology to drive the process. Functional-safety engineering encodes
  the same conclusion structurally: a safety instrumented function is sensor plus logic solver plus
  FINAL ELEMENT, and something lacking the final element is not a protection layer at all, which
  yields a one-line acceptance test — name the final element — applicable to every remedy the fleet
  proposes. Vulnerability management supplies the arithmetic: an organisation can remediate roughly
  one in ten open vulnerabilities per month REGARDLESS OF HOW MANY IT HAS, so remediation capacity is
  approximately constant while detection capacity scales with tooling, and beyond a modest point
  additional detection changes only which tenth gets done. Security operations and internal audit
  corroborate the shape, the latter interestingly by instrumenting the thing the fleet does not: the
  IIA's 2025 Standards mandate tracking the MANAGEMENT ACTION PLAN CLOSURE RATE, not the finding rate.
  Where this file must stop short is on novelty: the register has held "fail-loud is an act of
  reporting, not an act of remediation" at High confidence since 19 July, and PRESUMPTION-812 is that
  premise producing its own predicted output.

  Caveats:
    (a) THIS IS SUBSTANTIALLY PREMISE-102 AGAIN AND THAT SHOULD DRIVE THE DISPOSITION. See the
        DUPLICATION WARNING. The correct reading of 812 is not "a new finding" but "a High-confidence
        premise, ACTIVE for a month, was not enforced for one day's worth of remedy proposals." Under
        PREMISE-151 that second recording is evidence of incubation rather than management; under
        PREMISE-135 terminality is not purchased by accumulating instances; under PREMISE-138(1)
        in-channel repetition with no effector is not a remedy. Re-minting is barred. Note the
        recursion: filing 812 as a finding, with no effector attached, would itself be a detector.
    (b) THE ITEM'S OWN CLAIM IS NOT LICENSED IN ITS STRONG FORM AND DETECTION IS NOT THE ERROR. Nothing
        located suggests detection is not worth building; every source treats it as necessary. The
        supported claim is about RATIO and SEQUENCING — that detection capacity is cheap and scales,
        closure capacity is expensive and does not, and the second is the binding constraint. Any
        disposition reading 812 as "stop building detectors" exceeds the evidence and would also
        contradict PREMISE-143's sustained steelman, which is explicit that the fleet's practice of
        patching AND announcing is a genuine asset and must not be discouraged, and PREMISE-155's
        ADD-DO-NOT-RELOCATE clause, which says the stage check is a correct instrument and the defect
        is the ABSENCE of the second one.
    (c) THE TWO QUANTITATIVE ANCHORS ARE VENDOR-ORIGINATED AND ONE CLUSTER IS INTERNALLY INCONSISTENT.
        Cyentia/Kenna sells vulnerability prioritisation and its finding is favourable to that product;
        the SOC figures come from marketing pages, include two mutually inconsistent numbers (40% and
        62% uninvestigated) on competing vendors' sites, and summarise surveys I did not retrieve. Per
        PREMISE-140 these should be named by their channel. **The register's own GAO-19-686 datum
        (35%) is better provenanced than anything in source 3 or 4 and 812 should lead with it.**
    (d) THE VERIFIED SOURCE CARRIES A WARNING AGAINST THE USE I AM MOST TEMPTED TO MAKE OF IT. The
        Joint Commission states plainly that sentinel-event reporting is voluntary, represents a small
        proportion of actual events, and that "no conclusions should be drawn about the actual
        relative frequency of events." The 36-versus-30 ordering is therefore about what gets REPORTED
        AND CODED, not about population frequency. It remains striking that response-side disablement
        is the modal coded factor, but it is not a measured proportion and must never be quoted as
        one.
    (e) DOMAIN TRANSFER IS UNEVEN ACROSS THE FOUR DOMAINS. Clinical alarms and functional safety
        concern HUMAN responders under time pressure with physical actuators; C2A2 has agent runs and
        a single human gate. What transfers robustly is the STRUCTURAL result — detection without an
        acting element is not a control — and the CAPACITY result, which is domain-general arithmetic.
        What does NOT transfer is any rate, any alarm-per-day figure, or any claim about how agents
        respond to volume. PREMISE-121's evidence base is already explicitly bounded to the clinical
        override literature and the same bound applies here.
    (f) THE CLOSURE GAP HAS A CAUSE THE ITEM DOES NOT NAME, AND PREMISE-167'S 15b WARNING IS THE MORE
        DANGEROUS FINDING. If C2A2's single human gate has been dark, then closure capacity is not
        merely small — per PREMISE-119's sequencing requirement it may be ZERO, in which case "no
        reduction in arrivals bounds the queue" and detector-versus-closure ratios are the wrong
        analysis entirely. 15b's warning on PREMISE-167 is sharper still: ESCALATION-AS-LOCK with a
        dark human gate "converts every handed-up defect into an unfixable one," so a remedy that
        routes MORE to the gate can be strictly worse than the detector it replaces. **Establish
        whether the service rate is greater than zero BEFORE designing any closure mechanism.** This
        is the register's own instruction and it should precede everything below.
    (g) I SEARCHED FOR AND DID NOT FIND a documented DETECTION-TO-RESPONSE INVESTMENT RATIO — a figure
        for what fraction of reliability or safety spend goes to each half. The queue's search question
        asked for "audit-to-remediation ratios" and no such benchmark was located in any domain. This
        matters: the closure GAP is well evidenced, the appropriate RATIO is not, so 812 supports "the
        gap is real" and does not support any target allocation.

  Search scope: VERIFIED and read in full on the clinical-alarm case, including the event counts and
  the recommendation set, with the source's own epidemiological caveat carried. GOOD at secondary
  level on the functional-safety architecture across four independent sources, with the standard
  itself unread and no clause cited. MODERATE and VENDOR-WEIGHTED on the two quantitative closure
  gaps, both flagged. FULLY REGISTER-HELD and non-independent on ISO 10.2, Phimister, Tucker &
  Edmondson and GAO-19-686. **CLEAN NEGATIVE on any detection-to-response investment ratio.** NOT
  SEARCHED, and each would materially change this: (i) the LOPA / independent-protection-layer
  literature at primary level, which is where the "no credit without a final element" rule is actually
  codified and which would convert R2's acceptance test from a paraphrase into a citation; (ii) the
  incident-response and MTTD-versus-MTTR literature, which is the direct home of the ratio question
  and where the negative result above would most likely be closed; (iii) the human-gate throughput of
  C2A2 itself, which is in-house, is required by PREMISE-119 before any remedy is designed, and is
  not a literature question.

  Recommendation: **SUPPORTED (Strong)** for the corrective proposition; equivalently NO-SUPPORT-FOUND
  for the presumption as worded. **But the disposition should be an ENFORCEMENT ACTION on PREMISE-102,
  not a new premise.** Four carries:
    1. NO NEW PREMISE. PREMISE-102 holds this at High confidence and PREMISE-143(1), 151, 138 and 121
       supply the mechanism, the incubation reading, the acceptance test and the quantified harm. What
       812 records is an ENFORCEMENT GAP — the same disposition PREMISE-141 made for its own systemic
       flag, and for the same reason.
    2. **THE ACCEPTANCE TEST IS THE QUOTABLE OUTPUT AND IT IS ONE LINE.** From functional-safety
       architecture: a sensor with no final element is not a protection layer. Every proposed remedy
       should have to answer "WHAT IS THE FINAL ELEMENT, AND WHO OR WHAT ACTUATES IT?" before it is
       accepted. This is PREMISE-138(2)'s name-the-actor requirement in a mechanical form that can be
       applied at proposal time by anyone, and applying it retroactively to 2026-08-15's remedies is a
       ten-minute pass that would confirm or refute 14b's classification in-system.
    3. THE ARITHMETIC IS THE OTHER QUOTABLE RESULT. Remediation capacity is approximately CONSTANT in
       the size of the detected population (~10% of open items per month in the best-measured
       analogue) while detection capacity scales with tooling. That turns "closure is downstream and
       easy" into a bounded-throughput claim, and it means the marginal detector's value is not merely
       small but — per PREMISE-121's desensitisation-generalises finding and source 1's disablement
       data — potentially NEGATIVE. Cite it with its vendor provenance attached, and prefer the
       register's own GAO-19-686 figure where a better-provenanced number is needed.
    4. ESTABLISH THE SERVICE RATE FIRST — THIS IS SEQUENCING, NOT AN AFTERTHOUGHT. PREMISE-119's
       load-bearing requirement is to establish whether the consumer is SATURATED or ABSENT before
       designing any admission or closure policy, because where service is zero the steady-state
       relations do not hold and no arrival-side change bounds the queue. Combined with PREMISE-167's
       escalation-as-lock warning, this means the first action on 812 is to measure the human gate's
       throughput, not to build a closure mechanism that routes more work to it.
