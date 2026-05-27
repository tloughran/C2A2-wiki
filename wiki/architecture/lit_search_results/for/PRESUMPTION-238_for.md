SEARCH-FOR-PRESUMPTION-238:
  Date searched: 2026-05-23
  Original item: PRESUMPTION-238
  Original statement: "Parking the history scrub presumes acceptable residual exposure while parked; stop-tracking presumed sufficient interim mitigation; no trigger set (success-criteria gap)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-238
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the decision to stop-tracking now and defer (park) the git-history scrub.
      15a: Searched for supporting literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E noted)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Risk-management practice (NIST SP 800-30): time-boxed risk acceptance is a legitimate posture when residual risk is bounded and the asset is not yet exposed.
    2. Git practice: gitignore + git rm --cached prevents FUTURE commits of a file — a valid first step that stops the bleeding.
    3. Defense-in-depth: keeping the repository private while a remediation is pending is a recognized compensating control.

  Strength of support: Weak-Moderate

  Summary: Deferring a history rewrite can be defensible IF the repo stays private (compensating control) and the risk acceptance is explicit and time-boxed. Stop-tracking is a correct first step that prevents recurrence. Support is weak-moderate and conditional: the cited practices require that residual exposure be BOUNDED and that an explicit trigger/decision exist — precisely the "no trigger set" gap the presumption flags, which means the supportive case is incomplete as the situation currently stands.

  Caveats: Support holds only while the repo is private and only if risk acceptance is made explicit; it does not cover "park indefinitely with no trigger" (the 15b challenge).

  Recommendation: PARTIALLY-SUPPORTED
