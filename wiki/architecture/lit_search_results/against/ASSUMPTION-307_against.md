SEARCH-AGAINST-ASSUMPTION-307:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-307
  Original statement: Git-history-derived yield is a valid productivity axis for the agent-metabolism instrument (tokens as cost, commits as yield), pending PRS-completion integration.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-307
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated assumption (metric-validity claim for metabolism instrument)
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Forsgren, Storey, Maddila, Zimmermann, Houck & Butler, 2021. "The SPACE of Developer Productivity." ACM Queue. — Explicitly argues no single activity metric (commits, PRs, LOC) can capture productivity; activity counts are listed as the canonical myth, valid only alongside satisfaction/performance/efficiency dimensions.
    2. Goodhart (1975)/Strathern formulation; surveyed in Hillel Wayne, "Goodhart's Law in Software Engineering" (Buttondown) and CodePulse, "Goodhart's Law: Why Your Metrics Get Gamed." — Once commit count drives a displayed yield score, the correlation between commits and value breaks: padding, splitting, and trivial commits are the documented responses.
    3. GitVelocity, "Lines of Code, Commit Counts, and Other Metrics That Measure Nothing." — Commit counts conflate granularity habits with output; a refactor deleting code or one large meaningful commit scores below ten cosmetic commits.
    4. Forsgren, Humble & Kim, 2018. "Accelerate." IT Revolution. — DORA program deliberately rejects per-unit output counts in favor of outcome measures (lead time, change-fail rate), on validity grounds.
  Strength of challenge: Strong
  Summary: The software-measurement literature is near-unanimous that commit counts are an invalid productivity axis: they measure granularity conventions, not value, and they degrade further once observed (Goodhart). The agent context worsens this — agents control their own commit granularity programmatically, so "yield" is a free variable: the same work product can be 1 or 40 commits at zero cost. A tokens-per-commit metabolism ratio therefore has an ungrounded denominator and an easily-inflated numerator's complement. The assumption's own hedge ("pending PRS-completion integration") concedes the criterion problem; the literature says the interim proxy is not merely noisy but directionally corruptible, and interim metrics have a documented tendency to become permanent.
  Specific risks: Agent activity drifts toward many small low-value commits (or commit-splitting) to look metabolically efficient; cross-agent or cross-period comparisons on the instrument are meaningless because granularity differs; decisions about scheduling/budgets (cf. ASSUMPTION-308 layer) get optimized against a corrupted signal.
  Mitigations available: Normalize yield by something less gameable (PRS-items closed, validated-artifact count, reviewed-and-accepted changes); display tokens-per-commit only with an explicit "uncalibrated proxy" label and a sunset date; freeze commit-granularity conventions (e.g., one commit per attended gate approval) so the unit is at least stable; never feed the interim metric into any allocation decision.
  STEELMAN:
    Strongest counterargument: For a single-operator system with a human attended commit gate, commit granularity is set by the human gatekeeper, not the agents, so the Goodhart channel is closed: agents cannot self-inflate a count the human controls. As a coarse metabolism display (is anything being produced for the tokens burned?), commits are an honest, zero-instrumentation-cost signal, and the claim is explicitly interim pending PRS integration.
    What would need to be true for C2A2 to be safe: Commit granularity stays human-controlled and stable; the metric is never used for optimization or agent feedback, only passive display; PRS integration actually arrives and replaces it.
    How to test: Plot commits-per-token over a period with known constant real output; if granularity drift moves the ratio, the axis is invalid in practice.
  Search scope: 1 WebSearch ("commit count lines of code bad productivity metric developer Goodhart's law gaming software metrics critique SPACE framework").
  Recommendation: CHALLENGED
