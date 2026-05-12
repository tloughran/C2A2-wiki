SEARCH-AGAINST-ASSUMPTION-081:
  Date searched: 2026-05-05
  Original item: ASSUMPTION-081
  Original statement: "`update_scheduled_task --fireAt` is a working workaround for the link-count silent-skip bug"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-081
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-05 fireAt-recovered runs
      15b: Searched for challenging literature on workaround fragility under underlying-bug patch
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. SRE workbook (Beyer et al. 2018) — workarounds inherit dependence on the bug; if Anthropic patches the daemon (e.g., changes link-count semantics or fireAt API), the workaround silently breaks.
    2. Software-maintenance literature (Lehman 1980; Parnas 1994 "Software Aging") — workarounds tend to ossify and become invisible dependencies; literature warns that the longer a workaround is in use, the harder it is to remove.
    3. API-deprecation literature (Robbes et al. 2012; Sawant et al. 2018) — explicit-time fire APIs are commonly deprecated or behavior-changed in scheduler systems; workaround stability is bounded by API stability.
    4. C2A2-internal: ASSUMPTION-081 has worked once (2026-05-05 morning); single-observation success does not establish ongoing reliability.
    5. Workaround-as-permanent-fix anti-pattern (Allspaw 2018) — recurrence of the underlying bug should be tracked, but the ASSUMPTION-081 framing does not surface tracking discipline.

  Strength of challenge: Weak-to-Moderate

  Summary: The workaround works tactically but is fragile in two directions: (a) if the underlying bug is patched without notice, behavior may change silently; (b) if the workaround pattern ossifies, the system becomes dependent on the bug's continued existence. The literature consistently pairs workaround use with explicit bug-tracking and migration plans. ASSUMPTION-081 surfaces neither.

  Specific risks: (a) Anthropic-side patch invisibly changes fireAt semantics; (b) workaround use ossifies and becomes load-bearing without acknowledgment; (c) PRESUMPTION-094 (no-broader-interaction) compounds the fragility.

  Mitigations available: (a) Track workaround use frequency; (b) add a "patch-detection" step to the catch-up routine (e.g., observe whether single-link tasks now fire normally); (c) document the workaround as known-tactical, not as architectural fix.

  Recommendation: PARTIALLY-CHALLENGED (workaround works; fragility under underlying-bug patch is real and not currently mitigated)

  STEELMAN:
    Item: ASSUMPTION-081
    Strongest counterargument: A workaround that depends on an unfixed bug is a workaround that depends on the bug not being fixed. If Anthropic patches the daemon, fireAt may continue to work but with different semantics — say, firing immediately rather than at the specified time, or queuing rather than executing. C2A2 has no patch-detection step, so the change would be invisible until something downstream broke. Workarounds without migration plans become permanent technical debt.
    What would need to be true for C2A2 to be safe: (a) Workaround-use frequency tracked; (b) patch-detection probe at the start of each cycle; (c) documented migration plan if the underlying bug is fixed.
    How to test: After each catch-up cycle, attempt to register a single-link task without fireAt and observe whether it fires normally. If yes, the underlying bug is patched; migration plan activated. If no, workaround continues with explicit acknowledgment.
