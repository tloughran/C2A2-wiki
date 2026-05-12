SEARCH-AGAINST-PRESUMPTION-035:
  Date searched: 2026-04-17
  Original item: PRESUMPTION-035
  Original statement: "Four Chrome-extension failures in one day meet the OPERATIONAL-DRIFT threshold defined by PRESUMPTION-032 — although PRESUMPTION-032 never specified a threshold"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-035
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — threshold-free invocation of drift alert
      15b: Searched for challenging literature
    Current status: STRONGLY CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Beyer et al. (2016) "Site Reliability Engineering"; Google SRE Workbook (2018): pre-defined, documented SLIs/SLOs/SLAs are the only way to ensure consistent drift alerting; retrospective thresholds are explicitly identified as an anti-pattern that degrades alerting fidelity over time.
    2. Rosen et al. (2020) and alert-fatigue literature: undefined thresholds produce both false positives (over-alerting on normal variance) and false negatives (missing real drift when the threshold "feels" different). Both failure modes erode signal value.
    3. Observability literature (Honeycomb, Majors 2019-2022): drift alerts without quantitative thresholds are functionally equivalent to gut-feel escalation — valid in the moment, invalid as a system property.
    4. Incident-management literature (Allspaw 2012): threshold-free invocation prevents retrospective evaluation of whether alerts fired appropriately.

  Strength of challenge: Strong

  Summary: Retrospectively invoking a threshold that was never defined is a well-documented alerting anti-pattern. The literature is unanimous: drift thresholds must be pre-defined, documented, and consistently applied. Without this, there is no way to tell whether an invocation is appropriate or reflects operator attention bias. Four failures "feels like a lot" may be right today and wrong next week; inconsistency is the cost.

  Specific risks: Alert inconsistency — some 4-failure days trigger, others don't, depending on operator mood/attention; both false-positive and false-negative accumulation; OPERATIONAL-DRIFT designation becomes noise rather than signal; downstream decisions premised on the flag (e.g., what to remediate first) are unstable.

  Mitigations available:
    - Define threshold before next invocation (e.g., "≥N failures across ≥M channels within T hours")
    - Document threshold in monitor_queue or an SRE-style runbook
    - Retroactive-threshold rule: "we'll define a threshold this week; until then, invocations are provisional"

  Recommendation: STRONGLY CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-035
    Strongest counterargument: The SRE literature is essentially unanimous on this point — drift alerts without defined thresholds are not a monitoring system but an emotional response. Retrospectively declaring "this met the threshold" when no threshold existed is indistinguishable from confirmation bias. The invocation may be reasonable as a judgment call but should not be labeled as meeting a threshold that was never defined.
    What would need to be true for C2A2 to be safe: Pre-defined, documented drift threshold before the next invocation; invocations evaluated against that threshold, not retrospectively rationalized.
    How to test: Compare next 4-channel-failure incident against the newly-defined threshold; assess whether the flag fires consistently.
