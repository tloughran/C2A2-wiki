SEARCH-AGAINST-PRESUMPTION-890:
  Date searched: 2026-08-28
  Original item: PRESUMPTION-890
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority High) [FIX FIRST candidate]
  Original statement: [inferred] That job liveness is an adequate proxy for artifact production, and that a
    monitor which has declared its own read failure may still report green.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-890
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a green report read against the directory listings it describes; the missing
        2026-08-26 run is the demonstrated instance.
      15b: Searched for challenging literature
    Current status: NO-CHALLENGE-FOUND (limb 2) / PARTIALLY-CHALLENGED (limb 1, on the remedy only)

  Search scope: WebSearch, 2026-08-28, one dedicated query on the limits of synthetic and output-based
    monitoring — shared corpus with ASSUMPTION-1230_against.md, recorded here rather than presented as
    independent corroboration. Reached: Splunk on synthetic assertions; USENIX ;login: on synthetic
    monitoring and E2E testing; dotcom-monitor, UptimeRobot, Microsoft's engineering playbook. NOT COVERED:
    any source defending liveness-only monitoring, which I searched for and did not find. All SNIPPET-ONLY.
    Confidence: MODERATE.

  Challenging evidence found: No, for the presumption itself; Partial, for its remedy

  Sources:
    1. Splunk, "Assert Like You Mean It" [SNIPPET-ONLY]
       https://www.splunk.com/en_us/blog/observability/synthetic-test-assertions.html —
       "A test can pass even when functionality is broken." Without assertions you have surface-level checks
       only. An existence check on an output file is a surface-level check.
    2. USENIX ;login:, "Synthetic Monitoring & End-to-End Testing: Two Sides of the Same Coin"
       [SNIPPET-ONLY] — Places output-based monitoring in the same discipline, with the same limits, as E2E
       testing rather than above it.
    3. UptimeRobot / dotcom-monitor practitioner material [SNIPPET-ONLY] — Multi-step flows fail in ways
       basic checks miss; the page loads and the submit breaks.

  Strength of challenge: None on the presumption; Moderate on the fix

  Summary: This is the run's clearest asymmetry and it should be stated as such: after a search directed at
    finding the strongest available defence, no source was found that supports treating liveness as a proxy
    for output, and none at all was found bearing on the second limb — a monitor reporting green while
    declaring its own read failure. That limb is undefended in the literature, and I looked. What the
    against direction can contribute is a warning about the obvious fix: replacing "scheduler ran" with
    "file exists" produces another check that passes while the thing is broken. The property that matters is
    assertion on content, and the estate's demonstrated failure — outputs absent for 2026-08-26, unflagged
    for a day — would be caught by a dated-content assertion and by a dead-man window, but not reliably by
    an existence test.

  Specific risks: (a) A cosmetic fix (existence check) closes the item while leaving the failure class open.
    (b) The self-declared-blind-instrument limb is the more dangerous of the two and the less likely to be
    fixed, because it is a reporting-semantics defect rather than a coverage one, and nobody's dashboard
    turns a colour for it.

  Mitigations available: Three, in order of value: (1) a monitor that cannot read its source reports UNKNOWN,
    never green — this is a one-line semantics change and it is the highest-value item in this cohort;
    (2) assert on a content property that cannot occur by accident (run-date inside the artifact);
    (3) a dead-man window so that silence alarms without being queried.

  SYSTEMIC-RISK cross-reference: see SYSTEMIC-RISK-FLAG_2026-08-28_G1.md — this item, ASSUMPTION-1230 and
    PRESUMPTION-891 share one vulnerability (instruments that read proxies and are triggered by events
    rather than by state).

  STEELMAN:
    Item: PRESUMPTION-890
    Strongest counterargument: Liveness monitoring is not a claim about output; it is a claim about the
      scheduler, and it is the correct instrument for the failure it is designed to catch — a job that stops
      being scheduled at all. Faulting it for not detecting empty outputs is faulting a smoke detector for
      not finding a gas leak. The defect is the absence of a second instrument, and the presumption
      mischaracterises a coverage gap as a design error.
    What would need to be true for C2A2 to be safe: the monitor's *report* would have to be scoped to what it
      measured. A report saying "scheduler reachable" is honest; one saying "healthy" is not.
    How to test: read the monitor's output string. This is a one-command test and it settles the item.

  Recommendation: NO-CHALLENGE-FOUND (limb 2) / PARTIALLY-CHALLENGED (limb 1, remedy only)
