SEARCH-AGAINST-ASSUMPTION-1303:
  Date searched: 2026-09-10
  Original item: ASSUMPTION-1303
  Original statement: A gate whose actionable rate is around 2% (418 hits, single-digit actionable) is
    a gate that will stop being read, and the remedy is threshold amendment.
  Routed limb: THE THRESHOLD LIMB ONLY, per the intake note. The prior question — whether mtime can
    detect this quantity at all — is PRESUMPTION-946, is settled in-house, and PREMISE-200 is ACTIVE
    on it. Nothing in this file addresses mtime's detection capability.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1303
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-09-09 evening intake — a review gate returning 418 hits against a
        single-digit actionable set, with threshold amendment proposed as the remedy.
      15b: Searched for challenging literature (2026-09-10), AGAINST direction only. Did not read the
        `for/` directory, `lit_search_returns.md`, or any 15a output for this item.
    Current status: PARTIALLY-CHALLENGED

  REGISTER CHECK, run before searching: the register HOLDS THE REMEDY LIMB ALREADY, at Moderate
  confidence, and holds it against the item.
    - **PREMISE-113** (ACTIVE, 2026-07-21) states it almost verbatim: "Tightening a detection rule
      risks suppressing detection rather than improving it, converting a false-positive problem into a
      silent false-negative one," and "a post-fix reading of zero is indistinguishable from a detector
      that now detects nothing." Its supporting evidence line already carries the finding that
      "threshold loosening suppresses detection." Under PREMISE-113 the remedy the item proposes is
      not merely uncertain, it is the named hazard.
    - **PREMISE-158** (ACTIVE, 2026-08-13) supplies the formal reason: "a detector is a CURVE in error
      space, not a point, so a change that reduces one error type without altering discriminability
      has relocated the operating point rather than improved detection." Threshold amendment moves the
      operating point along the curve. It does not, by itself, buy discriminability. PREMISE-158 also
      requires that after any DIRECTIONAL remedy the OPPOSITE direction be re-checked on the
      instrument that was changed — which is the missing step in the item's proposal.
    - **PREMISE-110**'s cost caveat already carries the alert-fatigue side, with a figure: "44% of
      organisations having an outage linked to suppressed or ignored alerts."
    So the register answers the second half of the item and partially answers the first. The residue
    searched was: (a) is a ~2% actionable rate ACTUALLY incompatible with sustained attention, or are
    there durable, professionally-operated gates at or below that rate; (b) is actionable rate the
    quantity that drives abandonment, or is something else driving it; (c) what does the evidence
    actually show about threshold amendment as an intervention.

  Challenging evidence found: Partial — and the item splits cleanly. The DIAGNOSIS is well supported
  and I found little against it. The INEVITABILITY claim is challenged by counterexample. The REMEDY
  is challenged both by the register and by the screening literature, and the challenge to the remedy
  is the substantive result of this file.

  Sources:
    1. "Is Maximum Positive Predictive Value a Good Indicator of an Optimal Screening Mammography
       Practice?" *American Journal of Roentgenology* 184(5) (2005), doi 10.2214/ajr.184.5.01841505.
       [SNIPPET-ONLY, and I record a failed retrieval: I fetched the AJR article page this run and it
       returned an empty body. Authors not stated because I could not confirm them. The clause below
       is from the search summary and MUST be re-verified before onward quotation.] — Reported:
       "Optimal (maximum) PPV1 can occur at any sensitivity level and should not be used as the sole
       indicator for practice optimization because it does not take into account the number of cancers
       that would be missed at that sensitivity." **This is the single most on-point sentence I found
       and it goes directly against the item's remedy.** The item proposes to amend a threshold in
       order to raise the actionable rate. The screening literature's settled position is that the
       actionable rate is not a quantity you optimise, because it can be raised to any level you like
       by discarding sensitivity, and the number you would have to watch to notice that — the misses
       — is precisely the number the amended gate can no longer produce. This is PREMISE-113's
       "indistinguishable from a detector that now detects nothing," arrived at independently in a
       different field with a fifty-year operational record.

    2. Screening and monitoring gates that run at low single-digit-to-low-tens PPV and are read
       anyway, entered as counterexamples to the INEVITABILITY limb:
       - Physiologic monitor alarms, multisite study: 97% sensitivity, 58% specificity, **PPV 27%**;
         reported PPVs of clinical alarm definitions "varied between 4.1% and 84%."
         [SNIPPET-ONLY — from the alarm-fatigue review corpus; individual studies not opened.]
       - Static analysis: SAST precision measured at 18–36%; CodeQL and Infer reported at >95%
         false-alarm rates for null-pointer dereference at Linux-kernel scale.
         [REGISTER-HELD under PREMISE-113 and NOT re-verified this run; non-independent.]
       Bearing: gates operating at a ~5% actionable rate are not hypothetical. They are shipped,
       maintained, funded and read for decades. What sustains them is not their precision; it is an
       asymmetric loss function plus a triage arrangement that does not require a human to read every
       hit.
       The item's inference "2% actionable → will stop being read" is therefore not a law. It is a
       prediction about THIS estate's loss function and triage arrangement, and those are the things
       that should be examined.

    3. Override literature — the mechanism evidence, and it cuts against the remedy:
       "Appropriateness of Overridden Alerts in Computerized Physician Order Entry: Systematic
       Review," *JMIR Medical Informatics* 8(7):e15653 (2020); and the DDI evaluation reporting 38,409
       "very severe" DDI alerts of which **88.2% were overridden**; a further study reporting a
       **92.9% override rate** with only 7.3% of alert cases clinically appropriate.
       [ALL SNIPPET-ONLY — search summaries; none opened; author lists not stated.] — Bearing: the
       88.2% figure is for alerts already stratified to the HIGHEST severity band, i.e. the population
       that survives exactly the kind of threshold amendment the item proposes. Raising the actionable
       rate of a channel does not, on this evidence, restore attention to it, because the driver named
       throughout this literature is VOLUME and INTERRUPTIVENESS rather than base rate: "alert fatigue
       is the consequence of receiving a high volume of alerts whereby users start ignoring critical
       alerts." A gate amended from 418 hits at 2% to, say, 120 hits at 7% is still a gate with 120
       hits and 113 non-events, and the literature does not predict it will be read.

    4. "Systematic review of physiologic monitor alarm characteristics and pragmatic interventions to
       reduce alarm frequency" (PMC4778561); and "The effect of interventions made in intensive care
       units to reduce alarms: a systematic review and meta-analysis."
       [SNIPPET-ONLY — reviews not opened.] — **This is the source that supports the item, and I am
       reporting it in full because it is the strongest thing in the file running the other way.**
       Reported: alarm rates were reduced by interventions including "widening alarm parameters"; "the
       number of monitor alarms can be substantially reduced without compromising safety"; one study
       combining alarm delays with widened defaults reported 4 alarms per patient post-intervention
       with improvements in safety outcomes. So threshold amendment IS an evidenced intervention.
       Two qualifications are load-bearing and are why this does not settle the item in its favour.
       (i) The same corpus reports that "all studies examining alarm interventions are judged to be at
       moderate-to-high risk of bias" and that only **2 studies reported no adverse outcomes** — a
       null finding on a tiny sample, not a demonstration of safety. (ii) Every one of these
       interventions is threshold amendment WITH a retained sensitivity measurement: the studies
       report what happened to the events, not only to the alarm count. The item as stated proposes
       the amendment without the second measurement, and it is the second measurement that the
       evidence actually rests on.

    5. INTERNAL, non-independent, declared: PREMISE-113, PREMISE-158, PREMISE-110's cost caveat. This
       file's remedy-side conclusion is largely an APPLICATION of PREMISE-113 and PREMISE-158 to a new
       gate and must not be counted as independent corroboration of either.

  Strength of challenge: Moderate — Strong against the remedy as stated, Moderate against the
  inevitability claim, and essentially None against the diagnosis, where I searched for evidence that
  low-precision channels retain attention and found the opposite everywhere.

  Summary: The item is a conjunction and its two halves have very different evidential standing. On
  the diagnosis — a channel with a ~2% actionable rate will stop being read — I looked for
  disconfirmation and found almost none: the alert-fatigue, alarm-desensitisation and CPOE-override
  literatures run one way, and the estate's own PREMISE-110 already carries the 44%-of-organisations
  figure. What I did find against the diagnosis is a class of counterexamples rather than a
  contradiction: gates at 4–27% PPV are routinely sustained in professional use, so low precision is
  not sufficient for abandonment, and the additional conditions that sustain those gates — an
  asymmetric loss function, and triage that does not require a human to read every hit — are
  identifiable and are the things worth checking here. On the remedy the evidence is materially
  against the item. Threshold amendment relocates the operating point along the detector's curve
  without buying discriminability (PREMISE-158), and the screening literature states outright that
  maximum PPV can occur at any sensitivity and is not a valid optimisation target because it is blind
  to what the amended gate stops catching. The override data compound this: 88.2% of alerts already
  restricted to the highest severity band are overridden anyway, which is evidence that raising the
  actionable rate does not by itself restore attention. The one genuinely supportive body of evidence
  — ICU alarm-reduction trials, where widening defaults reduced alarm burden without measured harm —
  is at moderate-to-high risk of bias throughout, rests on two studies for the no-adverse-outcome
  claim, and in every case pairs the amendment with a retained measurement of the events the alarm
  exists to catch. That pairing is the whole intervention, and the item omits it.

  Specific risks: (a) The direct risk is PREMISE-113's, and it is silent: the threshold is amended,
  the hit count falls to something readable, the gate reads clean, and there is no instrument in the
  estate that can distinguish "clean" from "no longer detecting." Given that this gate's single-digit
  actionable set is the only evidence anyone has of what it is for, tightening past those cases
  destroys the only calibration data available. (b) The rate-versus-volume confusion is the risk to
  the DESIGN rather than the gate: if the driver of non-reading is volume, an amendment that improves
  the rate while leaving the volume in the low hundreds buys nothing, and the estate will have spent
  the amendment and still have an unread gate — with the added cost that the next non-reading will be
  attributed to the threshold again. (c) Precedent risk, which is this estate's characteristic one:
  "the gate is noisy, so amend the threshold" is a general-purpose move, and once it is licensed once
  it is available for every gate. PRESUMPTION-946 already names this shape ("a noisy gate is a
  mis-tuned gate") and the in-house question it poses — whether ANY mtime threshold separates the 418
  from the single-digit actionable set — must be answered NO-first, because if no threshold separates
  them then threshold amendment is not a remedy at all, it is a decision to stop looking. (d) If the
  amendment is made and the gate later reads clean, that clean reading will be reported into the
  morning channel, where PRESUMPTION-944's defect is live. The two items compose badly.

  Mitigations available:
    (i)   **Answer PRESUMPTION-946's in-house question first, and treat the answer as a gate on this
          item.** If no threshold separates the 418 hits from the actionable set, threshold amendment
          is definitionally unavailable and the correct move is a different discriminator or an
          explicit decision to accept the rate. This costs one query and is decisive. PREMISE-107's
          scope guard applies in the direction of doing it: it is cheap, reversible and immediately
          observable.
    (ii)  **If amended, amend WITH the second measurement.** Per PREMISE-158, after any directional
          remedy re-check the opposite direction on the instrument just changed: run the amended gate
          against the known-actionable cases and record how many it still catches. This is the step
          that makes the ICU alarm evidence evidence, and it is cheap here because the actionable set
          is single-digit and already enumerated.
    (iii) **Separate the rate problem from the volume problem before choosing a remedy.** The override
          literature says volume drives abandonment. Remedies that reduce volume without touching
          discriminability — grouping, deduplication, ranking, showing the top N by an independent
          severity signal, or an aged digest rather than a per-hit list — are available and do not
          risk PREMISE-113's silent false-negative conversion. They should be priced against the
          threshold change rather than skipped.
    (iv)  **Consider the asymmetric-loss route rather than the precision route.** What keeps a 4% PPV
          screening gate readable is not its precision but that missing an event is much worse than
          reading a non-event, and the reading cost has been engineered down. If the estate genuinely
          holds that asymmetry for this gate, the honest design is to keep the sensitivity and attack
          the reading cost. If it does not hold the asymmetry, then the gate should be retired
          deliberately rather than tuned into silence — which is a decision the designer should make
          explicitly, not one that a threshold change should make implicitly.

  Search scope: Preliminary-to-moderate. Four queries; one full-text retrieval attempted (AJR) and it
  FAILED, returning an empty body — recorded rather than papered over, because the AJR sentence is the
  load-bearing quote in this file and it is currently snippet-level. Literatures covered: clinical
  alarm fatigue and alarm PPV; CPOE/CDS override rates and appropriateness; alarm-reduction
  intervention trials and their evidence quality; screening-programme PPV optimisation. Partially
  covered via the register rather than fresh search: static-analysis precision. NOT covered, and these
  are genuine gaps: signal-detection-theory treatments of vigilance decrement at low base rates, which
  is the formal literature for the inevitability limb and which I did not reach; the SRE/on-call alert
  literature (Rachel Myers / Google SRE workbook material on alert precision and recall targets),
  which is the closest domain match to a software gate and which I searched adjacent to but did not
  retrieve; and any measurement of whether a threshold amendment RESTORED attention to a previously
  abandoned channel — I looked for that specific before/after and did not find it, which is the
  cleanest statement of the gap: **the intervention the item proposes has, so far as this search
  reached, never been measured against the outcome the item wants.**

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1303
  Strongest counterargument: The item is right about the disease and wrong about the cure, and the
  cure it proposes is the one its own register already classified as a hazard. Start from what a
  threshold is. A detector is a curve in error space; a threshold is a point on that curve. Moving the
  point trades one error for the other and buys nothing else — that is PREMISE-158, ACTIVE since
  August. So "the actionable rate is 2%, therefore amend the threshold" is a proposal to purchase
  precision with sensitivity, and the price is unstated because the estate has no measurement of what
  the gate would stop catching. The screening literature has been round this loop with a fifty-year
  operational record and its conclusion is unusually blunt: maximum PPV can occur at any sensitivity
  level and is not a valid optimisation target, because it takes no account of the cancers missed at
  that sensitivity. Substitute "actionable rate" for PPV and the sentence is about this gate. Worse,
  the amended gate's clean reading is not distinguishable from a gate that detects nothing —
  PREMISE-113 says so explicitly, and the single-digit actionable set is the ONLY calibration data
  the estate has, so an amendment tuned past it destroys the evidence that would reveal the mistake.
  Now the second limb. Suppose the amendment succeeds in raising the rate. Will the gate be read? The
  override data say no: 88.2% of DDI alerts already restricted to the "very severe" band — the
  population that survives severity thresholding — are overridden, and 92.9% in another series. The
  driver named throughout that literature is volume and interruptiveness, not base rate. So the item
  has diagnosed a volume-and-attention problem and prescribed a precision remedy, and the mechanism
  by which the remedy is supposed to work is the mechanism the evidence says is not the operative one.
  There is a version of the item that survives all of this, and it is the version the ICU trials
  actually support: amend the threshold AND measure what you stopped catching AND report both. That
  is not what the item says. It says the remedy is threshold amendment.
  What would need to be true for C2A2 to be safe: Three conditions, and PRESUMPTION-946's in-house
  question decides the first. (1) There must EXIST a threshold that separates the 418 hits from the
  actionable set. If there is not — and the intake's own not-routed note suspects there is not — then
  threshold amendment is not a remedy but a decision to stop looking, and it should be taken as such,
  in the open, by the designer. (2) The amendment must be paired with a retained sensitivity
  measurement against the known-actionable cases, so that PREMISE-113's silent-false-negative
  conversion is detectable. This is cheap here precisely because the actionable set is single-digit.
  (3) The estate must be able to state which problem it is solving — rate or volume. If the gate would
  still be unread at 120 hits and 7% actionable, then no achievable amendment fixes it and the money
  should go to reading cost, ranking, or deliberate retirement instead. The estate currently satisfies
  none of the three, and (1) is answerable today.
  How to test: All three tests are in-house, retrospective, and available now. **Test A, decisive and
  first:** for the 418 hits and the single-digit actionable set, plot the actionable cases against the
  candidate threshold variable and ask whether any cut separates them. Report the sensitivity retained
  at each candidate cut. If the maximum achievable actionable rate at 100% retained sensitivity is
  still ~2%, the item is refuted mechanically and no literature is needed. **Test B, the volume/rate
  discriminator:** take the estate's own record of when this gate was last read, and any other gate
  with a comparable hit VOLUME but a higher actionable rate, and compare reading frequency. If the
  high-rate, high-volume gate is also unread, rate is not the operative variable here and the remedy
  is mis-targeted. n will be small; report it with its denominator per PREMISE-136. **Test C, the
  guard against the amendment itself:** if an amendment is made, re-run it against the enumerated
  actionable set before deploying, and record the retained fraction as a stored property of the gate.
  Per PREMISE-158 this is the required opposite-direction re-check, it is scoped to an instrument just
  touched, and it converts an unpriced trade into a priced one.
