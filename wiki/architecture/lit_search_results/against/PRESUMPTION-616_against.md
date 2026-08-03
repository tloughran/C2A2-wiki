SEARCH-AGAINST-PRESUMPTION-616:
  Date searched: 2026-08-02
  Original item: PRESUMPTION-616
  Original statement: That a monitoring or diagnostic layer which reports it has no effector can be remediated by producing further reports; that self-reported closed-loop failures in an alerting system are resolved by escalation within the same channel.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-616
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced an unstated assumption that a diagnostic layer's own reporting is an adequate remedy for its own lack of an effector; recorded as a presumption about escalation-within-channel.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Ivers, N. et al., 2012 (updated 2025/2026). "Audit and feedback: effects on professional practice and healthcare outcomes." Cochrane Database of Systematic Reviews CD000259. — The canonical test of "report the problem back and behaviour changes": weighted median adjusted risk difference of 4.3% absolute increase in compliance (2012); the updated review reports a median absolute improvement of 2.7% (IQR 0.0-8.6) across 558 outcomes from 177 studies, mean 6.2% (95% CI 4.1-8.2). Feeding information back through the same channel produces small effects; it does not close a loop.
    2. Felisberto, M. et al., 2024. "Override rate of drug-drug interaction alerts in clinical decision support systems: A brief systematic review and meta-analysis." Health Informatics Journal 30(3), SAGE. — Average override rates of 46.2%-96.2%. Where a channel is already saturated, adding reports raises the override rate rather than the action rate.
    3. Poly, T.N. et al., 2020. "Appropriateness of Overridden Alerts in Computerized Physician Order Entry: Systematic Review." JMIR Medical Informatics (PMC7400042). — 29.4%-100% of overrides were judged appropriate depending on alert class; the most common documented override reason was "will monitor." That is the exact failure mode in question: the response to a report is another report of intent, not an effector action.
    4. Ray/Wilson et al., 2026. "Alert fatigue measurement in clinical decision support: a systematic review." JAMIA (PubMed 42148822). — Finds that alert fatigue is not even consistently defined or measured across the literature; a system cannot assume its own escalation volume is being received as signal, because the receiving-end degradation is unmeasured in most deployments.
    5. Canadian Centre for Occupational Health and Safety. "Hazard and Risk — Hierarchy of Controls" (ISO 45001-aligned). — Warnings and administrative controls sit at the bottom of the effectiveness hierarchy precisely because they depend on a human effector downstream; a control that only emits information is classified as the weakest control type available.
    6. PagerDuty Incident Response / Operational Reviews documentation (practitioner literature). — Defines "unactionable incidents" as informational alarms where "there is nothing for a responder to do other than acknowledging they received a notification," and identifies alerts with no clear owner as a distinct pathology. Escalation policies in this literature explicitly require a channel change and a named owner per tier; escalation within the same channel is treated as a known anti-pattern.

  Strength of challenge: Strong

  Summary: The literature on audit-and-feedback, alert override, and the hierarchy of controls converges against the presumption. Information returned through the channel that produced it yields small, decaying behaviour change (median 2.7-4.3% absolute), and where the channel is already dense the dominant response is override with a deferral reason ("will monitor") — a report about a future action, not an action. The occupational-safety hierarchy classifies information-only controls as the weakest available, and incident-response practice treats "alert with no owner and no possible responder action" as a defect to be removed rather than a state to be escalated. No source located supports the proposition that a monitoring layer lacking an effector can obtain one by reporting that it lacks one.

  Specific risks: The system accumulates a growing archive of accurate self-diagnoses that never change behaviour, while the archive itself is read as evidence of health ("we detected it"). Detection is then miscounted as mitigation. Because the failure is silent — nothing errors, the report is filed correctly — the divergence between reported and actual closure can persist indefinitely and grows with report volume. Second-order risk: report saturation raises the override/ignore rate on the genuinely actionable reports.

  Mitigations available: (a) Require every diagnostic that reports a closed-loop failure to name an effector outside its own channel — a human, a scheduled job, a blocking gate; (b) treat "reported N times, unremediated" as an escalating severity that changes channel at a threshold, not as a repeat of the same event; (c) track a closure rate, not a detection rate, as the health metric; (d) convert the highest-frequency repeat reports into forcing functions (see PRESUMPTION-623); (e) audit for unactionable reports and delete them, per alerting-principles practice.

  Search scope: Comprehensive for the clinical alerting, audit-and-feedback and hierarchy-of-controls literatures. Preliminary for organisational escalation design — the academic literature on escalation-channel design specifically (as opposed to psychological safety and organisational silence) is thin in accessible sources and the practitioner material found is grey literature; broader search of the human-factors and high-reliability-organisation literature recommended.

  STEELMAN:
    Strongest counterargument: Repeated reporting is not meant to be the effector; it is meant to raise the posterior probability that a human effector attends. The Cochrane audit-and-feedback effect is small but real and positive, and the review explicitly finds larger effects where baseline performance is low and where co-interventions are present — which is the regime a repeat report is in. A monitoring layer that reports it has no effector is doing the only correct thing available to it: it is not claiming to remediate, it is transferring the obligation to a layer that can. Refusing to report because reporting is weak would be strictly worse than reporting.
    What would need to be true for the system to be safe: (i) a named human or automated effector actually reads the channel; (ii) repeat reports change something observable — severity, channel, or destination — rather than repeating identically; (iii) the report volume in that channel is low enough that override/ignore rates stay low; (iv) closure is measured downstream, not inferred from the report having been written.
    How to test: Take the last N self-reported closed-loop failures in the system's own logs. For each, measure elapsed time to an observable state change outside the reporting channel (a code change, a config change, a human acknowledgement). Compute the closure rate and the median time-to-closure, and compare first reports against second-and-later reports of the same defect. If later reports do not shorten time-to-closure, escalation-within-channel is confirmed inert.

  Recommendation: CHALLENGED
