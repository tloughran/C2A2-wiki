SEARCH-FOR-ASSUMPTION-431:
  Date searched: 2026-07-09
  Original item: ASSUMPTION-431
  Original statement: "A failing QC signal (qc_sweep 'fidelity fail') can be reclassified as environmental (absent sandbox cache) without independent re-verification of content."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-431
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extraction from cohort listing (2026-07-07 EOD)
      15a: Searched for supporting literature (item is QUEUED-EMPIRICAL; decisive test is re-running QC with the environmental cause removed)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. ANSI/ISA-18.2 / IEC 62682. "Management of Alarm Systems for the Process Industries." ISA. — Alarm rationalization is a sanctioned, standards-backed practice: alarms may be formally reclassified as non-actionable/nuisance, i.e., the move "this failing signal is not a real defect" has legitimate precedent as an engineering discipline.
    2. 2024. "Alarm rationalization and dynamic risk analyses for rare abnormal events." Computers & Chemical Engineering (ScienceDirect S0098135424000516). — Modern treatment of rationalizing alarm floods; supports classifying alarm causes (including environmental/instrumentation causes) as distinct from process deviations.
    3. Equity Engineering Group. "Reduction of Nuisance Alarms by Implementing the Alarm Management Lifecycle, A Focus on Rationalization." — Practice literature: a large fraction of raised alarms are technically false due to artifact, and identifying artifact-caused alarms is a recognized, high-value activity — the direct analog of attributing a fidelity fail to a missing sandbox cache.

  Strength of support: Weak

  Summary: The alarm-management literature supports the *category* of move being made: signals from QC/monitoring systems are frequently artifact-driven (72–99% of clinical monitoring alarms are technically false or non-actionable), and formally reclassifying an alarm as environmental/nuisance is standard, standards-governed practice. What keeps support weak is the "without independent re-verification" clause: rationalization per ISA-18.2 is a documented, evidence-based determination — typically requiring demonstration of the artifact mechanism or a re-test with the artifact removed — not a plausibility judgment. The literature legitimizes the reclassification; it does not legitimize skipping the verification step, and the normalization-of-deviance literature (Vaughan, "The Challenger Launch Decision," 1996) documents exactly how repeated unverified "known benign" dismissals become organizational failure modes.

  Caveats: Support weakens with each repetition of the dismissal without a confirming re-test; with any content-bearing consequence downstream of the QC gate; and if the environmental explanation is inferred rather than demonstrated. Per the QUEUED-EMPIRICAL tag, the cheap decisive test (re-run qc_sweep with the cache present, or verify content independently once) is what the literature would require to convert this from rationalization-risk to rationalization-proper.

  Search scope confidence: Comprehensive for alarm-management practice.

  Recommendation: PARTIALLY-SUPPORTED
