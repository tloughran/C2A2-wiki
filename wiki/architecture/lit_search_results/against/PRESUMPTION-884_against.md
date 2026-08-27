SEARCH-AGAINST-PRESUMPTION-884:
  Date searched: 2026-08-26
  Original item: PRESUMPTION-884
  Queue ref: for_lit_search.md — ITEM: PRESUMPTION-884 (Priority High)
  Original statement: [inferred] That a benign cause of record, once established, can be applied to an
    entire flag population without per-item test — that explaining one instance explains the class.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-884
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from an internal tension inside a single transcript — a blanket dismissal of a
           307-pair fidelity `fail` population as "the recorded cold-cache condition" (ASSUMPTION-1209)
           and a preserved true positive (Day 76, ratio 0.610, escalated 2026-08-17, still open)
           stated in the same report and not read against each other. High confidence. Checked against
           PRESUMPTION-876 for duplication; the mechanism is scope-of-attribution, not
           staleness-of-verdict.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Three WebSearch queries executed 2026-08-26 (diagnostic premature closure; alarm
    suppression masking true alarms; security-alert false-positive suppression and base rates), plus
    material carried over from the PRESUMPTION-878 static-analysis searches. Literatures reached:
    (a) clinical cognitive-error taxonomy — premature closure, anchoring, search satisficing,
    attribution error; (b) industrial and clinical alarm management, including quantified true-alarm
    suppression rates; (c) SOC alert-triage practice on false-positive suppression and bulk closure;
    (d) static-analysis suppression practice (from the 878 searches). Venues reached: Merck Manual
    Professional Edition, Springer (Croskerry's case-based critical-thinking volume), AAFP, APSF,
    Emerson/Control Engineering for industrial alarm management, several USPTO patent disclosures on
    alarm suppression, and a set of vendor/practitioner SOC sources.
    NOT COVERED, and these matter: (i) the **signal-detection-theory** treatment of suppression
    thresholds (d′, ROC, the explicit cost function relating false-alarm reduction to missed
    detections), which is the formal frame for this exact trade and which I did not reach — it would
    likely raise this to Very Strong; (ii) the ISA-18.2 / EEMUA-191 alarm-management standards in
    primary form, which contain the actual normative rules on when suppression is permitted;
    (iii) the epidemiological literature on **ecological fallacy** and on inferring individual causes
    from group-level explanations, which is the cleanest statement of the scope error; (iv) any
    peer-reviewed source for the SOC true-positive-suppression figures below — those come from vendor
    material. Search confidence: MODERATE-HIGH on the mechanism, LOW on the quantitative limbs.

  Challenging evidence found: Yes

  Sources:
    1. Pat Croskerry [attribution from the chapter title page; editorship/volume details unverified].
       2019. "Premature Closure: Anchoring Bias, Occam's Error, Availability Bias, Search Satisficing,
       Yin-Yang Error, Diagnosis Momentum, Triage Cueing, and Unpacking Failure." In *A Case-Based
       Guide to Critical Thinking in Medicine*. Springer.
       https://link.springer.com/chapter/10.1007/978-3-319-93224-8_23 — The named form of the
       presumption. Premature closure is "the mistake of accepting a diagnosis before it has been
       fully verified. **When the diagnosis is made, the thinking stops.**" That last sentence is 14b's
       "a cause once diagnosed becomes the reading of the flag, and the flag stops being evidence,"
       arrived at independently. The chapter also names *search satisficing* — "the physician does not
       seek additional information after reaching a conclusion" — which is exactly what happened when
       the cold-cache explanation was applied to all 307 pairs without a per-item test.
       ABSTRACT-ONLY (paywalled chapter).
    2. Merck Manual Professional Edition. "Cognitive Errors in Clinical Decision Making."
       https://www.merckmanuals.com/professional/special-subjects/clinical-decision-making/cognitive-errors-in-clinical-decision-making
       — Two directly transferable findings. First, anchoring/premature closure "is the most frequent
       single cause of diagnostic error," and consists in "relying on an initial diagnostic impression
       despite subsequent information to the contrary." Second, and more precisely on point,
       **attribution error**: the canonical illustration is a clinician who assumes an unconscious
       patient smelling of alcohol is intoxicated "and misses hypoglycemia, diabetic ketoacidosis, or
       intracranial injury." That is the structure of the C2A2 case exactly — a plausible benign cause
       is present and true for most of the population, and it masks the minority for whom a serious
       cause is present. Day 76 is the hypoglycaemia. Reference source, high reliability, tertiary.
       FULL-TEXT (freely readable; read via search summary).
    3. [authors unverified]. "Flaws in Clinical Reasoning: A Common Cause of Diagnostic Error."
       American Family Physician, 2011. https://www.aafp.org/pubs/afp/issues/2011/1101/p1042.html —
       "Disregarding the possibility of other diagnoses can lead to premature closure." Corroborates
       (1) and (2) from an independent venue. SNIPPET-ONLY.
    4. Alarm-management sources — Anesthesia Patient Safety Foundation
       (https://www.apsf.org/article/alarm-fatigue-and-patient-safety/) and Emerson / Control
       Engineering on industrial practice
       (https://www.emersonautomationexperts.com/2025/industrial-software/best-practices-with-alarm-management/,
       https://www.controleng.com/reduce-downtime-and-risk-with-effective-alarm-management/) — Two
       findings. First, a quantified suppression cost: **"the suppression rate for true alarm
       detection can be between 2.33% and 17.73%"** — i.e. suppression rules demonstrably swallow real
       alarms at a non-trivial rate, and this is a measured quantity in deployed systems, not a
       theoretical worry. Second, the normative rule: suppression of resultant alarms is legitimate
       only where the causal alarm has *already fired and been acknowledged*, and systems "must ensure
       that no generated alarm notifications are lost if the alarm suppression works incorrectly."
       C2A2's blanket attribution meets neither condition — there is no per-item causal confirmation
       and no residual channel. **The 2.33–17.73% figure is from a practitioner/vendor context surfaced
       by search; I could not trace it to a primary study and it should not be quoted as an
       established range.** SNIPPET-ONLY.
    5. SOC alert-triage practitioner sources —
       https://www.conifers.ai/glossary/false-positive-suppression/,
       https://www.prophetsecurity.ai/blog/alert-triage, https://www.vectra.ai/topics/reduce-false-positives
       — Supply the concept C2A2 lacks: the **True Positive Suppression Rate**, "the percentage of
       genuine threats accidentally filtered by suppression logic, a critical metric that should be
       monitored closely and remain at or near zero." Also the behavioural mechanism: "when a high
       percentage of alerts in a given category turn out to be false positives, analysts tend to
       develop a pattern of quicker dismissal for that category, which is understandable at the
       individual level, but it creates organizational risk." And the consequence of bulk closure:
       "when those severity tiers get bulk-closed without investigation, the SOC is systematically
       blind to the early phases of the kill chain." Vendor sources; framing is standard practice but
       none of the figures should be treated as evidence. SNIPPET-ONLY, low weight.
    6. [authors unverified]. 2025. "An Empirical Study of Suppressed Static Analysis Warnings."
       FSE 2025. https://software-lab.org/publications/fse2025_suppressions.pdf — Carried over from
       the PRESUMPTION-878 search. Establishes that suppression on false-positive grounds is routine
       (34.4% of suppression cases) and that suppressions persist. Relevant here because the blanket
       cold-cache attribution *is* a suppression rule — it has no expiry, no sampling, and no review
       trigger. SNIPPET-ONLY.
    7. [authors unverified]. "Veritas-RPM: Provenance-Guided Multi-Agent False Positive Suppression for
       Remote Patient Monitoring." arXiv:2604.16081. https://arxiv.org/pdf/2604.16081 — Surfaced twice
       across independent queries; the existence of dedicated recent work on *provenance-guided*
       (i.e. per-item, cause-traced) false-positive suppression is itself evidence that blanket
       attribution is the recognised failure mode the field is designing against. Not read.
       SNIPPET-ONLY.

  Strength of challenge: Strong

  Summary: The presumption has an established name in two independent literatures, and in both it is
  classified as an error rather than a heuristic. In clinical reasoning it is premature closure with
  search satisficing — "when the diagnosis is made, the thinking stops" — and anchoring, which the
  Merck Manual identifies as "the most frequent single cause of diagnostic error." The sub-type that
  matches C2A2 most exactly is attribution error, whose textbook illustration is structurally
  identical to the cold-cache case: a plausible benign cause is genuinely present, is genuinely the
  right explanation for most of the population, and precisely because of that it masks the minority
  for whom the serious cause is present. In monitoring and alarm management the same operation is a
  suppression rule, and the practice literature is explicit that suppression is legitimate only where
  the causal condition has been confirmed per-instance and where a residual channel guarantees no
  alarm is silently lost. C2A2's blanket attribution has neither: it covers all 307 entries with no
  sampling, no expiry, and no per-item test. The decisive evidence, however, is not in any literature
  — it is inside the single transcript that 14b read. Day 76 carries a genuine fidelity failure at
  ratio 0.610 against a hard ±25% bound, escalated on 2026-08-17 and still open, and the same run held
  Day 76 on exactly that ground *in the same report* that dismissed the whole population as
  cold-cache. The population is therefore not merely "known to be mixed" as a matter of inference; it
  is demonstrated mixed, by the run's own output, with a true positive already in hand. The blanket
  attribution is refuted by a counterexample the system itself produced and did not read against it.
  Rated Strong rather than Very Strong because the quantitative limbs are weak — the true-alarm
  suppression figures come from practitioner sources I could not trace to primary studies, and I did
  not reach signal-detection theory, which is where the formal argument lives.

  Specific risks: (a) The fidelity check currently contributes nothing — a check whose entire output
  is dismissed by a standing rule has an effective detection rate of zero, and it is being run and
  maintained at full cost. (b) The one real failure it caught is visible only because a human escalated
  it eight days ago, which means the check's demonstrated true-positive yield in this system is
  attributable to a human, not to the check. (c) A suppression rule with no expiry and no sampling —
  the rule will continue to dismiss every future fidelity `fail` including ones arising from causes
  that have nothing to do with cache warmth, and nothing in the system will ever trigger its review.
  (d) Per the SOC literature's behavioural finding, the dismissal habit generalises: once a category is
  known-benign, dismissal accelerates and the category becomes invisible rather than merely
  low-priority. (e) The cheapest fix in the entire batch is unbuilt — one warm-cache run recounts the
  population and the residual fails are the real ones; this is a single execution, not a project.
  (f) Compounds with PRESUMPTION-876 (the cold-cache condition is itself a *dated* verdict being read
  as current state — 884 is the scope error, 876 the time error, and they multiply) and with
  PRESUMPTION-878 (each new check C2A2 builds is a candidate for the same blanket dismissal, which is
  what makes 884 the empirical demonstration of 878's alert-fatigue risk).

  Mitigations available:
    - **Warm the segment cache once and recount.** 14b named it; it is one run; it converts the entire
      question from an inference into a measurement. Nothing else in this batch has a comparable
      cost-to-value ratio.
    - Failing that, sample. Test 20 randomly selected entries from the 307 against the cold-cache
      hypothesis individually. The residual failure rate in the sample estimates the population's, and
      the sample cost is bounded.
    - Give the suppression rule an expiry and a review trigger. Any standing benign attribution should
      carry a date, a scope statement, and a condition under which it is re-tested — otherwise it is
      indistinguishable from having disabled the check.
    - Introduce a residual channel: entries dismissed by a blanket rule should be recorded as
      *suppressed*, not as *passed*, so the suppressed population remains countable and auditable.
      This is the alarm-management rule that "no generated alarm notifications are lost if the
      suppression works incorrectly."
    - Track a True Positive Suppression Rate. Day 76 already provides one confirmed true positive
      inside the suppressed population; that is a rate of at least 1/307 measured with zero effort,
      and it is already above the practitioner threshold of "at or near zero."
    - Institutionally: require that any blanket attribution be stated *against* the known exceptions in
      the same report. The failure here was not that the run lacked the counterexample — it had it, in
      the same document.

  STEELMAN:
    Item: PRESUMPTION-884
    Strongest counterargument: Blanket attribution from a diagnosed cause is not a fallacy when the
    cause is *mechanistically sufficient and uniformly applicable*. A cold segment cache is not a
    probabilistic explanation like "most chest pain is benign"; it is a deterministic property of the
    measurement apparatus that applied to the entire run, and if the cache was cold for all 307 pairs
    then all 307 measurements are invalid for the same reason, per-item testing or not. Testing each
    entry individually against a condition known to have held globally would be pure ceremony. The
    Day 76 case does not refute this: Day 76's fidelity failure was established by a *different* route
    — a human escalation on 2026-08-17 with a specific measured ratio (1692 rendered / 2773 raw ASR =
    0.610) — and the run *did* hold Day 76, in the same report, which is evidence that the reviewer
    was reading the exception rather than blind to it. On this reading the run behaved correctly: it
    invalidated a measurement it knew to be instrumentally corrupted, and separately preserved a
    finding it knew to be independently established. Calling that premature closure imports a
    probabilistic-diagnosis frame onto what is really an instrument-calibration judgment. And the
    alternative is not free: 307 per-item tests against a condition known to hold globally is a real
    cost, in a system whose budget has been breached on fifteen consecutive runs.
    What would need to be true for C2A2 to be safe: (i) the cold-cache condition must genuinely have
    held for *all* 307 pairs, not merely for the run as a whole — if any pair was measured after the
    cache warmed, its `fail` is real and is currently suppressed; (ii) the cold-cache condition must be
    *sufficient* to produce a fidelity `fail`, not merely capable of it, otherwise the attribution
    over-explains; (iii) the condition must be *specific* — if a fidelity `fail` can also be produced
    by genuine truncation, then cold cache explains the *presence* of fails but not their *count*, and
    the correct inference is that the population is a mixture of unknown proportions, which is exactly
    what Day 76 demonstrates; (iv) the suppression must be scoped to the affected run and must not
    persist as a standing rule, since the cache condition is a property of one execution; (v) Day 76's
    preservation must be a *rule* the reviewer applied rather than an accident of a human having
    escalated it — if the only reason the true positive survived is that a human happened to escalate
    it eight days earlier, then the run's own procedure would have dismissed it, and the system has no
    mechanism for finding the Day 76s that no human noticed.
    How to test: Decisively testable in one execution, and this is the strongest reason to treat the
    item as urgent rather than merely open. Warm the segment cache and re-run the fidelity check over
    all 307 pairs. Three outcomes and each is informative: (a) zero residual fails — the blanket
    attribution was correct and the presumption is refuted for this instance (though the *general*
    presumption about standing suppression rules survives, since correctness here would be luck rather
    than method); (b) exactly one residual fail, Day 76 — the attribution was correct in aggregate but
    the check was contributing nothing beyond what a human already knew; (c) more than one residual
    fail — the presumption is confirmed and the count of previously-invisible true positives is
    exactly the number of defects the blanket rule was hiding. Independently, and at near-zero cost:
    check whether the cold-cache condition was recorded per-pair or per-run. If per-run, condition (i)
    of the steelman is unverified and the attribution rests on an assumption about uniformity that
    nobody has checked.

  Recommendation: CHALLENGED

  SYSTEMIC-RISK-FLAG:
    Date: 2026-08-26
    Affected items: PRESUMPTION-878, PRESUMPTION-879, PRESUMPTION-880, PRESUMPTION-881,
      PRESUMPTION-882, PRESUMPTION-883, PRESUMPTION-884
    Common vulnerability: **Every remedy path in this batch terminates at the same single, currently
      unresponsive human review gate, and not one of the seven presumptions conditions its behaviour
      on that gate's responsiveness.** PRESUMPTION-884's contribution to the pattern is that it shows
      what the gate's silence produces downstream: a standing suppression rule over 307 entries that
      no one ruled on, that has no expiry, and that survives because there is no adjudicator to ask it
      the one question (was the cache cold for every pair, or only for the run?) that would settle it.
      It is also the empirical demonstration of PRESUMPTION-878's risk: build a check, and its output
      gets blanket-dismissed at a gate that cannot process it.
    Secondary common vulnerability (this item and -878): **flag populations produced by automated
      checks are being disposed of in bulk rather than per-item, and neither the bulk disposal nor its
      true-positive cost is measured.** 884 is the realised instance (307 entries, one known true
      positive inside the dismissed set); 878 proposes four more checks that would produce four more
      such populations. The literature basis is common to both — alert fatigue and warning suppression
      (https://dl.acm.org/doi/10.1109/TSE.2023.3329667;
      https://software-lab.org/publications/fse2025_suppressions.pdf) and the alarm-management rule
      that suppression requires per-instance causal confirmation plus a residual channel
      (https://www.apsf.org/article/alarm-fatigue-and-patient-safety/).
    Risk level: Critical (batch-level); High for this item specifically
    Recommendation: Run the warm-cache recount before building any further checks — it costs one
      execution and it settles both this item and the empirical premise of PRESUMPTION-878. See the
      identical batch note on PRESUMPTION-878, -879, -880, -881, -882 and -883.
