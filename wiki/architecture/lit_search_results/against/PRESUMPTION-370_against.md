SEARCH-AGAINST-PRESUMPTION-370:
  Date searched: 2026-06-21
  Original item: PRESUMPTION-370
  Original statement: "[inferred] An agent-only day with no attended session is presumed to carry no extraction-worthy epistemic content ('null day' = nothing to record)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-370
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated salience criterion tying extraction-worthiness to attended activity
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Survivorship / selection bias (Abraham Wald, WWII aircraft) — reasoning only from the cases that "made it back" (here: attended, salient days) systematically misreads the system, because the informative cases are precisely the ones filtered out. Equating "no attended session" with "no content" is the same filter that hid the bullet holes on the planes that didn't return. (Wald; Survivorship bias, Wikipedia/Brilliant.)
    2. Selection bias more broadly — survivorship bias is the special case where the selection variable is "survival"; conditioning the record on human attendance is a selection mechanism that biases the system's self-model toward attended states and away from the unattended states where unsupervised drift actually accumulates.
    3. Streetlight effect / availability — recording only where the light is (attended sessions) measures convenience, not where the relevant information is. Routine/low-salience intervals are where silent change accrues.
    4. Self-demonstrating evidence (C2A2-internal) — the 06-19→06-20 "null days" were exactly when the EOD pipeline silently stalled (OPEN-086 / PRESUMPTION-369). The presumed-empty period contained the single most decision-relevant fact of the window. The "null day" was not null.
    5. Unit-of-analysis objection — choosing "attended session" rather than "system-day" as the recording unit is a methodological choice, not a fact about information content; a system that runs autonomously 24/7 has a system-state worth a liveness record every day regardless of human presence.

  Strength of challenge: Moderate-Strong

  Summary: The presumption is challenged on well-established methodological grounds: tying extraction-worthiness to attended human activity is a selection/survivorship filter that biases the system's self-knowledge toward the cases least likely to harbor unsupervised drift. The challenge is sharpened by self-demonstration — the very null days that prompted this item were when the pipeline silently failed, so "null day = nothing to record" was false in the most consequential possible way. The challenge is rated Moderate-Strong rather than Strong only because a legitimate resource-rational counter-practice (don't log noise) genuinely exists; the correct target is not "record everything" but "record a minimal system-day liveness/status entry."

  Specific risks: The system's self-model is biased toward attended periods; unattended drift and silent failures are under-represented exactly where they matter; absence-of-record is misread as absence-of-event, compounding PRESUMPTION-369.

  Mitigations available: Record a minimal heartbeat/system-day status entry every day (attended or not), distinguishing "no-op / nothing changed" from "did-not-run"; treat null-day records as the baseline against which drift is measured; couple directly to the PRESUMPTION-369 liveness fix — one daily liveness record discharges both.

  STEELMAN:
    Strongest counterargument: Recording everything is a real anti-pattern — indiscriminate capture inflates cost, buries signal, and fuels alert fatigue. Most agent-only days really are uneventful, and forcing extraction from them manufactures noise and false precision; selective, salience-driven recording is sound observability practice.
    What would need to be true for C2A2 to be safe: The filter must drop only genuinely zero-information content while still capturing a cheap liveness/no-change signal — i.e., "nothing notable happened" must itself be recorded as a positive fact, not inferred from silence. If silence and no-op are indistinguishable, the presumption is unsafe.
    How to test: Compare a no-op day's record against a did-not-run day's record; if they are indistinguishable in the vault, the presumption has erased exactly the signal needed to detect a stall.

  Search scope: survivorship/selection bias (Wald); streetlight/availability effects; selective-logging vs liveness-recording tradeoff; unit-of-analysis choice; C2A2-internal failure record. Comprehensive.

  Recommendation: CHALLENGED

  ---
  SYSTEMIC-RISK-FLAG:
    Date: 2026-06-21
    Affected items: PRESUMPTION-369, PRESUMPTION-370 (and prior family: ASSUMPTION-270 → MONITOR-296 autonomous-sync silent-degradation; PREMISE-049 verify-before-trust)
    Common vulnerability: Over-trust of unattended automation / failure to fail loud — the system treats silence as success and absence-of-record as absence-of-event. 369 is the mechanism (no liveness check on the auditor); 370 is the epistemics (unattended periods presumed contentless). Together they form a closed blind spot: the auditor can silently die AND the period in which it dies is presumed to contain nothing to record.
    Literature basis: dead man's switch / heartbeat monitoring; silent-failure detection; survivorship/selection bias (Wald); quis custodiet (monitor-the-monitor).
    Risk level: High
    Recommendation: Treat 369+370 as a single coupled fix — a mandatory daily system-day liveness record plus an external dead-man's-switch alert on missed runs. This discharges both the mechanism gap (369) and the epistemic gap (370) at once and closes the silent-degradation family.
