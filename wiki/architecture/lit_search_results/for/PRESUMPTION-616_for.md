SEARCH-FOR-PRESUMPTION-616:
  Date searched: 2026-08-02
  Original item: PRESUMPTION-616
  Original statement: [inferred] That a diagnostic layer which has just established it has no effector will be given one by whoever reads the flag saying so. The SYSTEMIC-RISK-FLAG's entire remedy is to ask Tom a question, delivered by the same instrument — a flag in a register — whose ineffectiveness is the flag's own thesis.

  Claim as tested here: that a monitoring/diagnostic layer reporting it has no effector can be remediated by further reports; that self-reported closed-loop failures in alerting systems are resolved by escalation within the same channel.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-616
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred the presumption from the mismatch between what the flag diagnoses (no effector) and the mechanism by which the flag is delivered (another register write). Recorded as high-confidence because the mismatch is explicit in the source text and unremarked by it.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Ray-Wilson, N. et al., 2026. "Alert fatigue measurement in clinical decision support: a systematic review." Journal of the American Medical Informatics Association (PMID 42148822). — Systematic review finding that alert-fatigue measurement is neither consistently defined nor consistently operationalised; establishes that the field treats repeated notification as a degradable resource rather than a reliably effective one.
    2. Felisberto, M., Lima, G. dos S., Celuppi, I.C. et al., 2024. "Override rate of drug-drug interaction alerts in clinical decision support systems: a brief systematic review and meta-analysis." Health Informatics Journal, 30. — Pooled override prevalence 90% (95% CI 85–95). Quantifies the fate of a warning delivered through the same channel earlier warnings were delivered through.
    3. Poly, T.N. et al., 2020. "Appropriateness of Overridden Alerts in Computerized Physician Order Entry: Systematic Review." JMIR Medical Informatics (PMC7400042). — Average override rates 46.2%–96.2%; notes that after systems were tuned to reduce alert volume, override rates "did not decrease satisfactorily." Bears on whether tuning a report-only channel restores its efficacy.
    4. Singh, H. et al., 2010 and related work. "Notification of Abnormal Lab Test Results in an Electronic Medical Record: Do Any Safety Concerns Remain?" The American Journal of Medicine. — 10.2% of critical-result alerts unacknowledged; timely follow-up lacking in 6.8% and statistically indistinguishable between acknowledged and unacknowledged alerts (6.4% vs 10.1%); dual-alert (broader) communication carried HIGHER odds of non-acknowledgement than single-alert (OR 2.02). The only well-quantified direct test of "more reports / more recipients" as remedy, and it runs the wrong way.
    5. Callen, J.L. et al., 2012. "Failure to Follow-Up Test Results for Ambulatory Patients: A Systematic Review." Journal of General Internal Medicine. — Non-follow-up of 6.8%–62% for laboratory tests and 1.0%–35.7% for radiology despite results being recorded and visible. Establishes that a recorded, readable, correct finding routinely fails to produce action.
    6. "Clinical Decision Support: Moving Beyond Interruptive 'Pop-up' Alerts," 2023 (PMC10491420). — Reviews evidence that a near-"hard stop" prescribing alert produced the desired response in 57.2% of cases versus 13.5% for the non-blocking control, and that a 2020 meta-analysis of 122 RCTs found CDS overall associated with <6% absolute improvement. The gap between the two is the effector, not the report.
    7. "Predictive value of a tiered escalation response system: a case control study," Australian Critical Care, 2023 (ScienceDirect S1036731423000279); and AHRQ, "Failure To Rescue — Rapid Response Systems," Making Healthcare Safer IV (NCBI Bookshelf NBK603026). — Escalation that routes to an actor with intervention authority shows real effect (moderate evidence for reduced cardiorespiratory arrest), with diminishing returns beyond two tiers and documented afferent/efferent limb failures. Positive predictive value rose across tiers (nurse trigger 59%, medical review 75%, RRT 88%) — value came from changing WHO receives, not from repeating.

  Strength of support: Weak

  Summary: The literature supports a narrow version of the claim and contradicts the broad one. Escalation works when it moves a signal OUT of the originating channel to a party holding an effector — rapid response systems, tiered escalation to a clinician with intervention authority, and automatic routing of unacknowledged critical results all show measurable effect. It does not work when the escalation is a further instance of the same instrument to the same audience: override rates of 90% and non-follow-up rates up to 62% are the base rates for correct, visible, recorded warnings, and the one direct test of broadening delivery (dual-alert vs single-alert) found worse acknowledgement. Effect size across the CDS literature tracks how hard the alert makes it to proceed without acting; the interruptive/hard-stop comparison (57.2% vs 13.5%) is the cleanest instance. Applied to PRESUMPTION-616: writing flag 117 into the register that already holds 116 unactioned flags has essentially no supporting evidence; routing the finding to a party who can edit the pipeline does.

  Caveats: (a) Nearly all evidence is from clinical decision support and hospital escalation, where the receiver is a human with role-defined authority and legal exposure; transfer to a single-principal agent network is by analogy. (b) The override literature measures alert DISMISSAL, not the fate of a passive register entry with no interruptive component — the C2A2 channel is weaker than any studied here, so the studied rates are optimistic bounds. (c) Override appropriateness reaches 100% in some categories, so a high non-action rate is not by itself channel failure; the C2A2 case stipulates the non-action is undesired, which the literature does not establish. (d) Hard stops are documented to generate unsafe workarounds, so the supported remedy is not unconditionally safe. (e) The 2020 CDS meta-analysis (<6% absolute improvement) reaches me second-hand through PMC10491420; not retrieved directly.

  Search scope: Comprehensive within the alert-effectiveness, alert-fatigue, CDS-override, critical-result-notification and rapid-response-system literatures. Not searched: aviation/nuclear warning-system human factors, whistleblowing and internal-escalation research in organisational behaviour, and the software on-call/incident-escalation empirical literature (this search returned mostly vendor blogs there). Broader search into organisational-behaviour escalation recommended.

  Recommendation: PARTIALLY-SUPPORTED
