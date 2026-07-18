SEARCH-AGAINST-PRESUMPTION-467:
  Date searched: 2026-07-11
  Original item: PRESUMPTION-467
  Original statement: "Firing-health aggregates to system health — a scheduler watchdog may say 'all clear' while multi-day outcome-level outages stand."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-467
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced by inference from 2026-07-10 EOD daily run
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. [HappySignals / Computer Weekly / ITSM literature on the "Watermelon Effect" (e.g., "The Watermelon Effect in IT," HappySignals; "Watermelon SLAs – making sense of green and red alerts," Computer Weekly). — Names and documents exactly this pattern: component/SLA metrics green on the outside while the user-experienced service is red inside; a decades-old, well-characterized ITSM failure mode driven by measuring activity rather than outcomes.]
    2. [Beyer, B., et al., 2016/2018. "Site Reliability Engineering" and "The Site Reliability Workbook," Google (sre.google: Monitoring Distributed Systems; Alerting on SLOs). — Core SRE doctrine: reliability must be defined by SLOs measured at the user-outcome level; cause-side/component signals ("the scheduler fired") are explicitly rejected as health definitions because one layer's health says nothing about end-to-end outcomes.]
    3. [Huang, P., et al., 2017. "Gray Failure: The Achilles' Heel of Cloud-Scale Systems." HotOS 2017. — Formalizes the divergence as differential observability: the observer (watchdog) and the affected party (wiki consumers) have different views, and systems whose reaction loops key off the observer's view systematically fail to react to real outages.]
    4. [Avasant, 2021. "Avoid the Watermelon Effect — Focus on Customer Experience"; ALVAO/XLA literature. — Industry remediation consensus: replace or supplement SLA-style component metrics with experience/outcome-level agreements (XLAs), because green component dashboards demonstrably coexist with sustained user-facing outages.]
  Strength of challenge: Strong
  Summary: This presumption — that a firing-level watchdog aggregates to system health — is contradicted by three independent literatures that all converge on the same conclusion: liveness/activity metrics do not compose into outcome health. The ITSM literature calls it the watermelon effect; Google SRE doctrine forbids defining health by cause-side signals; the gray-failure literature explains mechanistically why the watchdog's view diverges from reality (differential observability). C2A2 has already lived the counterexample: the watchdog reported green through a multi-day outcome outage, which is not an edge case of the presumption but its predicted failure mode. Note the framing subtlety: 14b surfaced this presumption as a critique, so the literature here confirms 14b's inference — the challenge lands on the underlying design assumption, which remains embedded in the watchdog as built.
  Specific risks: Watchdog green becomes a systemwide sedative — no agent or human investigates because "monitoring is fine"; outage duration is bounded only by human happenstance rather than detection; retrospective health reporting (uptime, run counts) overstates delivered value; trust in all pipeline dashboards erodes once one watermelon is discovered.
  Mitigations available: Define 2-4 outcome-level SLIs (e.g., "EOD report exists, is valid, and is dated today," "queue age of oldest unprocessed item < X days," "DB passes integrity check") and have the watchdog alert on those; keep firing-health as a diagnostic layer, never the headline; a synthetic end-to-end canary task whose output is consumed and verified by an independent checker; watchdog self-test — inject a known outcome failure quarterly and confirm it pages.
  STEELMAN:
    Strongest counterargument: A scheduler watchdog's honest scope is the scheduler: it can only attest to what it observes, and a component-scoped green is true and useful information (the scheduler genuinely wasn't the problem — triage can skip it). The failure is not the watchdog but the absence of any outcome-level monitor beside it, plus a labeling problem ("all clear" instead of "scheduler clear"). Layered monitoring with correctly scoped signals is standard practice; demanding every monitor measure end-to-end outcomes conflates layers and produces unactionable alerts.
    What would need to be true for C2A2 to be safe: The watchdog's report is consumed as "firing-layer clear" rather than "system clear" by every downstream reader (human and agent); at least one other monitor owns outcome-level health; and incident triage documents show the green watchdog never suppressed investigation of outcome symptoms.
    How to test: Fault injection — stop one task's real output while leaving its schedule firing, and measure time-to-detection and which signal detected it. If detection depends on a human noticing stale content, the presumption is operationally live and the challenge stands.
  Recommendation: CHALLENGED
