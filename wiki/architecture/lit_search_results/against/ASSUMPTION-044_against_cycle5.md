SEARCH-AGAINST-ASSUMPTION-044:
  Date searched: 2026-08-23
  Cycle: 5 (15d monthly re-trigger; cohort 2026-07-05; unconsumed 49 days)
  Original item: ASSUMPTION-044 (MONITOR-049)
  Original statement: "DECISION-021 loading half (Handoffs/latest.md + SessionStart hook) RELIABLY orients Dispatch sessions."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c → 15d → 15b (cycle 5)]
    Original item: ASSUMPTION-044
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-04-18 Dispatch stress-test (first use; loading half only)
      15b (cycle 0, 2026-04-18): CHALLENGED — "reliably" is a distribution property, unmeasurable at N=1
      15b (cycles 1–3): refresh only; no new literature
      15b (cycle 5, 2026-08-23): Searched for challenging literature — NEW MATERIAL FOUND, and it bears on the ONE datum
    Current status: CHALLENGED (the sole supporting observation is now in question, not just the inference drawn from it)

  Challenging evidence found: Yes.

  Sources:
    1. Hanley, J.A. & Lippman-Hand, A. 1983. "If Nothing Goes Wrong, Is Everything All Right? Interpreting Zero Numerators." JAMA 249(13):1743–1745. The canonical treatment: with n trials and zero observed failures, one may be 95% confident only that the true failure rate is at most about 3/n.
    2. Jovanovic, B.D. & Levy, P.S. 1997. "A Look at the Rule of Three." The American Statistician 51(2):137–139. Formalises and bounds the same rule. APPLIED HERE, THE NUMBER IS DEVASTATING: at n=1 with zero failures, the 95% upper bound on the failure rate is 3/1 — i.e. the bound is vacuous. Even n=3 gives an upper bound of 100%. To support a claim of, say, ≤10% failure at 95% confidence you need roughly n=30 clean runs. The word "reliably" is not merely under-evidenced at N=1; the standard statistical machinery returns no information at all.
    3. anthropics/claude-code Issue #10373, "SessionStart hooks not working for new conversations" (jeremybarnes, 2025-10-26, OPEN; fetched and read in full). On macOS, for brand-new interactive sessions, SessionStart hooks execute and log success while their stdout is never parsed into `additionalContext` and never injected. The reporter's canary test confirmed the model had no knowledge of the injected content. This does not merely reduce the confidence attached to the 2026-04-18 datum — it raises the question of whether that datum measured what it was taken to measure. URL: https://github.com/anthropics/claude-code/issues/10373
    4. anthropics/claude-code Issue #33612 (harald-voca, 2026-03-12; fetched in full): hooks silently ignored for non-terminal clients, other settings in the same file honoured. Entry-point-conditional activation means a passing test on one launch path is not evidence about another.
    5. anthropics/claude-code Issue #12671, "SessionStart hook shows 'hook error' despite successful execution (exit 0)" — the inverse confusion; the reported status and the actual outcome are decoupled in both directions. (Located in search index; body not fetched.)
    6. "The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break," arXiv:2604.11978 (2026, preprint), and "Why Retrying Fails: Context Contamination in LLM Agent Pipelines," arXiv:2605.08563 (2026, preprint). Both bear on the gap between "loaded" and "oriented": loading is necessary, not sufficient, and utilisation degrades over a session.

  Strength of challenge: Strong (UPGRADED from Moderate)

  New since cycle 0/1: YES, on two fronts. First, the rule-of-three literature turns the cycle-0 qualitative objection ("N=1 is not a reliability estimate") into a quantified one: at n=1, the 95% upper confidence bound on the failure rate is 3/1, which is to say the observation constrains nothing. Second, and more consequentially, Issue #10373 gives a concrete, current, unpatched mechanism by which the 2026-04-18 observation could have been a false positive — the hook fires, the log is clean, and the payload never reaches the model. The cycle-0 file challenged the INFERENCE from the datum. This cycle challenges the DATUM.

  On the meta-question posed in the search angle — whether re-running a literature search can ever resolve an item whose disposition-changing condition is an in-system measurement: normally no, and cycles 1–4 demonstrated exactly that, returning "no change" four times in a row. This cycle is the exception that proves the rule. External literature could not supply the missing runs, but it could and did supply a reason to doubt the run C2A2 already had. That is the only way an AGAINST search can move an empirically-blocked item, and it is worth noting that it took five cycles of near-zero-yield refreshes to hit it. The general point stands: an item gated on an unrun measurement should be routed to a measurement task, not to a literature cadence.

  Summary: The assumption says "reliably" about a mechanism exercised once, on its easier half, in a way that could not have distinguished success from a documented silent-failure mode. The rule-of-three literature shows that even a clean N=1 licenses no reliability figure whatsoever. The Claude Code issue tracker shows that the N=1 may not have been clean — that a fired hook with a successful exit code is compatible with zero context injection on this exact platform. Nothing here shows the mechanism does not work. What it shows is that C2A2 has no observation capable of telling the difference, and has been carrying the word "reliably" for four months on that basis.

  Specific risks: (a) The one datum may be a false positive, in which case every cycle since has been refreshing a finding built on it; (b) "reliably" has propagated into DECISION-021's dependents and into PRESUMPTION-037's comparative clause, so a single unsound observation is load-bearing in at least three places; (c) the measurement that would settle it is cheap and has been deferred five times; (d) under-instrumentation follows from false confidence, which means a future real failure will present as a mysterious downstream defect rather than as a handoff failure.

  Mitigations available:
    - Re-run the 2026-04-18 test with a content-level canary (nonce in the file, model asked to echo it). This distinguishes injection from mere hook execution. It is a five-minute test.
    - Adopt an explicit N-threshold tied to the rule of three: to claim ≤20% failure at 95% confidence requires ~15 clean runs; to claim ≤10%, ~30. State the actual N alongside the word "reliably," or drop the word.
    - Restate as "orientation observed once, by an uncontrolled method, on the loading half only."
    - Reclassify this item from literature-cadence to measurement-blocked, and stop spending refresh cycles on it. Four of the last five cycles produced nothing because literature was never the binding constraint.

  Search scope: Comprehensive on zero-failure confidence bounds (canonical sources located and applied numerically); comprehensive on the platform-specific defect question (two issues fetched in full, two further located); moderate on agentic-utilisation preprints.

  Recommendation: CHALLENGED (upgraded; and recommend 15c re-route this item to an empirical task rather than a further literature cycle)

STEELMAN:
  Item: ASSUMPTION-044
  Strongest counterargument: "Reliably" is a claim about a distribution. C2A2 has one draw from that distribution, and the rule of three says one draw with zero failures bounds the failure rate at 3/1 — no information. That alone would make the word unearned. But there is a sharper problem: on this platform there is an open, reproduced defect in which SessionStart hooks execute, log success, and have their entire payload silently discarded before it reaches the model. The 2026-04-18 test, as recorded, could not have distinguished that outcome from a real success. So the assumption rests on a single observation that may not be an observation of the thing it names, and five monitoring cycles have refreshed it without anyone re-running the five-minute test that would settle it.
  What would need to be true for C2A2 to be safe: (a) At least one canary-verified run on the real launch path; (b) an explicit N and an explicit confidence bound wherever "reliably" appears; (c) acknowledgement that "loading" and "orienting" are different claims, and that only the former was ever at issue; (d) the item moved out of the literature cadence into a measurement queue.
  How to test: Nonce in `Handoffs/latest.md`. Launch via the real Dispatch path. First prompt: "what nonce is in the handoff file?" If the model cannot answer without reading the file itself, injection did not occur. Log the result. Repeat until N is large enough to support whatever adverb is being used.
