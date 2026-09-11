SEARCH-AGAINST-PRESUMPTION-953:
  Date searched: 2026-09-11
  Original item: PRESUMPTION-953
  Original statement: "[inferred] That the estate's daily reports are read — that a finding correctly
    surfaced to a human is a finding on its way to being handled."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-953
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a convergence of six independent terminal requests in one day against a measured
        response record; stated without accusation, with the 36-card batch APPROVE recorded as direct
        evidence the reader is there and the fourteen-day gap as direct evidence the latency is long.
      15b: Searched for challenging literature; found three independent domains with measured base rates
        for "correctly surfaced and not acted upon," all of them large, and one VERIFIED figure.
    Current status: CHALLENGED

  Register pre-check — this is the most heavily pre-answered item in the batch after 949:
    - **PREMISE-108 (ACTIVE) — verbatim.** "Transmission is not delivery. A finding 'flagged for' a named
      agent does not transfer responsibility for it; the loop is closed only on evidence that the
      recipient received AND acted, and until then the finding is held by nobody while the record shows it
      discharged. **That state is worse than not flagging.**" This is PRESUMPTION-953, already minted.
    - **PREMISE-102 (ACTIVE).** "Fail-loud is an act of reporting, not an act of remediation. Where the
      notified channel has demonstrated zero throughput, repeated identical non-processing converts a
      one-time signal into an undecided standing policy of non-coverage; the loudness of the report is not
      evidence that anything is received."
    - PREMISE-116 (ACTIVE) — a finding does not change the behaviour it describes; the best-measured
      analogue is audit and feedback. PREMISE-123 (ACTIVE) — a validated finding does not reach the agent
      it governs unless an explicit propagation mechanism carries it.
    - PREMISE-131 / 138 / 173 (ACTIVE) — the warning/final-element family.
    - PREMISE-121 (ACTIVE) — review-queue acceptance is a function of workload and cumulative exposure
      rather than item merit; override rates 49–96%; acceptance falls as volume and complexity rise. This
      is the quantitative shape of what happens when six requests arrive on one day.
    Six-plus ACTIVE premises bear. None was cited by any of the six runs that terminated in a request.

  Challenging evidence found: Yes

  Sources:
    1. Cyentia Institute / Kenna Security, "Prioritization to Prediction, Vol. 3: Winning the Remediation
       Race" (2019), as summarised by its own author on cyentia.com. — **VERIFIED at the authoring
       institute's own restatement** (page retrieved and read 2026-09-11; the report PDF itself is gated,
       recorded) — "The typical organization only fixes about 10% of its vulnerabilities in any given
       month. And that's consistent regardless of how many assets are in the environment." Survival
       analysis over hundreds of organisations. Note the second clause: remediation capacity does not
       scale with the number of findings, so the *proportion* handled falls as the finding rate rises.
       This is the single best-measured statement available of "correctly surfaced ≠ on its way to being
       handled," and it is measured in a domain with dedicated staff, tooling, budget and regulatory
       pressure — all of which C2A2's channel lacks.
    2. Callen, J.L., Westbrook, J.I., Georgiou, A. & Li, J. (2012), "Failure to Follow-Up Test Results for
       Ambulatory Patients: A Systematic Review," J Gen Intern Med 27(10). — SECONDARY (search summaries
       of the Springer record and the AHRQ PSNet abstract retrieved; full text not read) — Tests not
       followed up: 6.8%–62% for laboratory results, 1.0%–35.7% for radiology. The review's most relevant
       finding for C2A2 is the EHR one: even with computerised notification of abnormal results firing an
       alert on every log-on, results are still missed — and "physicians electronically acknowledging
       alerts does not necessarily indicate they have read and acted upon the abnormal result."
       Acknowledgement is not action. The estate has no acknowledgement signal at all.
    3. Clinical decision support override literature — the 49–96% override band described across CDSS
       studies; Brigham and Women's Hospital study in which clinicians overrode 73.3% of medication alerts
       reviewed, of which 40% were inappropriately dismissed; one study at 92.9%. — SECONDARY (search
       summaries; individual studies not retrieved). Register-held: the 49–96% band is already inside
       PREMISE-121. Included here because the *direction* matters: the more correctly-surfaced items
       arrive, the lower the fraction acted on, which is the mechanism by which six well-formed requests
       in one day is a worse position than one.
    4. Patient-safety incident-reporting processing literature (PMC12510765; PMC11554398). — SECONDARY
       (search summaries) — Professionals' reported experience of a mandated, staffed reporting channel:
       reports not discussed, "no concrete changes occurred after reporting," reporters never heard back.
       The steady state of a *supported* reporting channel is a channel with no closing act.
    5. Columbia Accident Investigation Board (2003), Vol. I; and the normalization-of-deviance literature
       following Vaughan. — SECONDARY (search summaries; the CAIB PDF was located at two URLs and NOT
       retrieved this run — recorded as a gap) — The canonical case in which information was correctly
       surfaced, repeatedly, by the right people, through the right channel, and was not acted upon; and
       in which the 1985 ASAP warning preceded Challenger by a year without changing anything. Reported at
       structural strength only: I did not read the report and no quantitative claim rests on it.
    6. Internal-audit follow-up literature (EUROSAI best-practices guide; ISACA follow-up material). —
       SECONDARY — The profession requires a *scheduled* follow-up with a tri-state re-rating precisely
       because "reported" and "implemented" were found to diverge. NEGATIVE RECORDED: no cross-organisation
       non-implementation base rate was retrievable; the figures I found (71% completed in one
       45-recommendation follow-up; a 90%-in-three-years target at one SAI) are single-organisation and
       carry no weight here.

  Strength of challenge: **Strong**, and this is the item where I hold the bar highest because 14b rated
    it Critical and because the register's charter says a PRESUMPTION with a strong challenge leans REVISE
    at HIGH urgency.
    Limb split — and the limbs matter, because 14b's own framing is the precise one:
      - "Nobody reads": **No challenge, and not the claim.** The 36-card batch APPROVE on 2026-09-09 is
        direct positive evidence. I found nothing supporting this limb and 14b does not assert it.
      - "Read soon enough to matter": **Strong** challenge. Every measured analogue puts the
        correctly-surfaced-to-acted-upon conversion well below 1, often far below, in environments far
        better resourced than this one. The Cyentia figure is the cleanest: ~10% per month, capacity
        invariant to finding volume.
      - "A correctly surfaced finding is thereby on its way to being handled": **Strong** challenge,
        and it is the limb PREMISE-108 already refutes in the estate's own words — the state where the
        record shows a finding discharged and nobody holds it is *worse than not flagging*.
    The recommendation rests on the second and third limbs.

  Summary: The challenge is strong and it is unusually well-evidenced, because "was the correctly
    surfaced finding acted on?" is one of the few questions in this batch that several industries have
    actually measured. The measured answers are consistently poor: ~10% of open vulnerabilities remediated
    per month with capacity invariant to volume; 6.8–62% of laboratory results not followed up; 49–96%
    alert override; a documented finding that electronic acknowledgement does not indicate reading or
    acting. All of those are from domains with staff, budget and regulatory pressure. C2A2's channel has
    one person, no acknowledgement signal, no follow-up schedule, and a Chat↔Cowork sync dark in both
    directions for three days and inbound for eight. Against that, the estate has one strong positive
    datum — 36 cards answered in a single act — which is exactly what a long-latency batching process
    looks like, and which is compatible with both "reads eventually" and "does not read soon enough to
    matter." The honest form of the measurement is therefore latency distribution, as 14b says, and it is
    the one measurement in this batch that the estate could produce today and has not.

  Specific risks: Every "flagged, not fixed" disposition in the estate banks on this, and that is most of
    them. Under PREMISE-108 the failure is not neutral: a finding recorded as flagged-and-pending is held
    by nobody while the record shows it discharged, which is worse than never having flagged it, because
    it consumes the attention budget that would have gone to an actual control. It is also the presumption
    that makes PRESUMPTION-949 tolerable — naming without owning is only safe if naming reaches an owner —
    so if 953 fails, 949 fails with it and the self-awareness layer's entire output loses its warrant at
    once. And because the estate's only escalation path is upward to one human (PRESUMPTION-956), there is
    no second channel to absorb the failure.

  Mitigations available:
    - **Measure the latency distribution.** 14b's test, and it is half-done already: take every request
      addressed to a person in the last 30 days, and record response / no response and age. Report the
      distribution, not a rate. This is one pass and it converts a Critical presumption into a number.
    - **Add an acknowledgement signal — but do not credit it.** The Callen finding is that acknowledgement
      does not indicate action, so an ACK closes the transmission question and leaves the delivery question
      open. Both are worth having, and they must be stored as different fields (PREMISE-167).
    - **Bound the request rate per report.** PREMISE-121's mechanism is that acceptance falls as volume
      rises; six requests in one day is the condition under which the measured override rates are worst.
      One ranked ask per report, with the rest held, is likely to raise the absolute number handled.
    - **Attach an expiry to every human-addressed request** — see PRESUMPTION-951 and the systemic flag
      filed today. A request with no deadline cannot be distinguished from a request that was declined,
      and the reader cannot triage a queue whose items have no age.
    - **Re-price the deferrals that depend on it.** Any disposition whose safety argument is "a human will
      handle this" should be re-read once the latency number exists. That includes the four registers in
      PRESUMPTION-951 and both scope-blocked fixes in PRESUMPTION-956.

  STEELMAN:
    Item: PRESUMPTION-953
    Strongest counterargument: The analogues are badly matched and all of them overstate the problem in
      the same direction. Cyentia's 10% is measured over environments with millions of open findings and a
      staff whose capacity is genuinely the binding constraint; C2A2's principal faces single-digit
      requests per day and answered 36 cards in one act, which is a throughput no vulnerability-management
      team achieves. The CDSS override literature measures interruptive alerts fired at a clinician mid-
      task, a design C2A2 does not use. The test-result literature measures a system with thousands of
      results routed among many clinicians, where the failure mode is *ambiguity of ownership* — a mode
      that does not exist here, because there is exactly one owner and he knows it. Most importantly, the
      estate has direct evidence, not analogy: the principal did respond, comprehensively, within the
      window. A fourteen-day gap in a single-principal system with no SLA is ordinary human batching, and
      inferring abandonment from it is the base-rate fallacy applied to a sample of one.
    What would need to be true for C2A2 to be safe: (a) the latency distribution must have a bounded right
      tail — items must eventually be answered, and the batch behaviour must be representative; (b) the
      items that matter most must not be the ones that wait longest — i.e. latency must be uncorrelated
      with, or negatively correlated with, urgency, which is testable and which I would expect to fail,
      because a one-line register fix is less salient than a 36-card batch; (c) the deferrals resting on
      the presumption must be able to survive the observed latency — a FLAG-023 with a time-limited
      window and a fourteen-day reader latency is not safe even if the reader always answers eventually;
      (d) there must be at least one non-human effector, or (a)–(c) must hold permanently rather than
      typically. (b) and (c) are the ones I would test first.
    How to test: the latency distribution, with urgency as a covariate. Over 30 days: for every request
      addressed to a person, record (date raised, date answered or NULL, stated urgency, size of the ask).
      Three outputs settle it — median and 90th-percentile latency; the never-answered fraction; and the
      correlation between stated urgency and latency. If the never-answered fraction is near zero and
      latency is uncorrelated with urgency, the steelman holds and the presumption should be recorded as
      PARTIALLY-CHALLENGED with the latency stated as an operating parameter. If either fails, the
      Critical rating is confirmed by the estate's own data.

  Search scope: comprehensive — vulnerability-remediation capacity and survival analysis; clinical
    test-result follow-up failure (systematic review level); clinical decision support override and alert
    fatigue; patient-safety incident-report processing; internal-audit recommendation follow-up;
    organisational-accident literature (CAIB / normalization of deviance). NOT RETRIEVED: the CAIB Volume
    I PDF (located, not fetched); the Cyentia P2P Vol. 3 report itself (gated — the figure is verified only
    at the authoring institute's own summary page); any cross-organisation audit non-implementation base
    rate (searched, not found).

  Recommendation: CHALLENGED
