SEARCH-AGAINST-PRESUMPTION-075:
  Date searched: 2026-04-27
  Original item: PRESUMPTION-075
  Original statement: "Chrome MCP egress workaround is a permanent solution rather than a contingent patch"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-075
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated operational premise
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Browser-extension fragility literature (Mozilla, Google security blogs; CWE-1419 on extension privilege issues): browser extensions are an actively-evolving surface; what works today may break with the next browser update.
    2. Browser auth-state literature (OAuth specifications; Chrome cookie-policy changes 2023–2025): auth states drift, expire, and re-prompt; treating today's success as permanent is a known fragility pattern.
    3. Workaround-debt literature (Cunningham 1992 on technical debt; Allman 2012 "Managing Technical Debt"): workarounds accrue debt; treating them as permanent without investing in robustness amplifies risk.
    4. Ad-blocker / anti-fingerprinting interaction (Snyder et al. 2017 on browser security extensions): user-installed extensions can silently break MCP-style integrations.
    5. C2A2 own evidence: PRESUMPTION-068 (the same-day Chrome-MCP success representing resolved auth state) is itself currently MONITOR-pending — meaning the system already recognizes the auth state may not be stable.
    6. OPEN-039 (Chrome MCP escalation question) is open precisely because the workaround's permanence is doubted.

  Strength of challenge: Moderate-to-Strong

  Summary: Browser-based workarounds are a well-documented fragility surface. Treating today's success as permanent is exactly the optimism the literature warns against. The system itself has open questions (OPEN-039) and a sibling presumption (PRESUMPTION-068) about whether the current state is permanent or transient — the answer hasn't been settled yet, and "permanent" is too strong absent that resolution.

  Specific risks: (a) Browser update breaks the workaround silently; (b) auth state expires unexpectedly; (c) user-installed extensions interfere; (d) operational confidence is built on a fragile foundation.

  Mitigations available: (a) Maintain robust failure detection and alerting on Chrome MCP path; (b) keep an alternative egress route warm; (c) treat the workaround as MONITOR rather than as permanent until N successive successes establish reliability; (d) re-derive the presumption when browser or extension updates land.

  Recommendation: CHALLENGED (the "permanent" framing is too strong; treat as conditional with active monitoring)

  STEELMAN:
    Item: PRESUMPTION-075
    Strongest counterargument: Browser-extension workarounds are a fragility surface that fails silently on browser updates, auth-state drift, or extension-interaction effects. Treating today's success as permanent — rather than as the start of a track record that needs accumulation — invites the failure mode where the workaround breaks at a critical moment without prior warning. The system has flagged related uncertainties (OPEN-039, PRESUMPTION-068) but is acting as if "permanent" is settled.
    What would need to be true for C2A2 to be safe: (a) The workaround is treated as conditional, not permanent, until a defined success threshold is met (e.g., 30 successive successes across 3+ browser versions); (b) failure detection and alerting are explicit; (c) an alternative egress route exists in standby.
    How to test: Track success/failure rate over 30 days across browser updates; if any update causes a regression, "permanent" is locally falsified.
