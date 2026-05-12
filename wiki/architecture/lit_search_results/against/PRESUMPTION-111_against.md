SEARCH-AGAINST-PRESUMPTION-111:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-111
  Original statement: "Third-consecutive cowork-to-chat sync failure presumed not to warrant fallback channel design"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-111
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 sync-failure pattern
      15b: Searched for counter-evidence on three-strikes thresholds for workaround design
    Current status: CHALLENGED

  Challenging evidence found: Yes (strong)

  Sources:
    1. Allspaw (2012); Beyer et al. (2016) "SRE" — three consecutive failures of a primary channel is the canonical threshold for fallback-design escalation; presuming non-warrant is documented anti-pattern.
    2. Avizienis et al. (2004) "Basic Concepts and Taxonomy of Dependable and Secure Computing" — three-failure threshold for redundant-path activation is canonical.
    3. OWASP authentication-design literature — third-failure fallback for browser-auth-required workflows is endorsed; manual-only fallback is documented anti-pattern.
    4. Empirical reliability literature (Schroeder & Gibson 2010) — failure clustering at three-strikes is empirical pattern that justifies fallback design rather than continued primary use.
    5. C2A2-internal: ASSUMPTION-071 / PRESUMPTION-038 prior cluster — the third recurrence of the same gap.

  Strength of challenge: Strong

  Summary: SRE / fault-tolerance / browser-auth-design literatures uniformly treat three consecutive failures as the canonical threshold for fallback-design escalation. The presumption "does not warrant" inverts the canonical disposition. The presumption is the third recurrence of the cowork-to-chat sync cluster (ASSUMPTION-071 / PRESUMPTION-038), which the literature predicts will continue to fail without fallback design.

  Specific risks: (a) Continued failure of primary channel without fallback; (b) accumulating reliability deficit; (c) compounds with ASSUMPTION-071 / PRESUMPTION-038 — third recurrence pattern.

  Mitigations available: (a) Design fallback channel (manual export, email, alternate API); (b) document three-strikes threshold and adhere to it; (c) cluster-level remediation across recurrences.

  Recommendation: CHALLENGED — three-strikes-fallback is canonical; "does not warrant" inverts the literature's disposition.

  STEELMAN:
    Item: PRESUMPTION-111
    Strongest counterargument: Three-strikes is the canonical fallback-design threshold. SRE / fault-tolerance / authentication-design literatures uniformly require fallback at this point. The presumption inverts the canonical disposition. Three recurrences of the same gap signal structural absence of the fallback-design step.
    What would need to be true for C2A2 to be safe: (a) explicit fallback-channel design; (b) three-strikes threshold compliance; (c) cluster-level remediation.
    How to test: Audit the historical sync-failure rate; if exceeds three-in-row, fallback design is empirically justified.
