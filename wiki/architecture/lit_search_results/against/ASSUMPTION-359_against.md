SEARCH-AGAINST-ASSUMPTION-359:
  Date searched: 2026-06-25
  Original item: ASSUMPTION-359
  Original statement: "Storing API keys in sessionStorage (not localStorage) is the right privacy posture - cleared on tab close, never written to disk"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-359
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted (twin of PRESUMPTION-395)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. OWASP HTML5 Security Cheat Sheet / Web Storage testing guide. - Do NOT store secrets (tokens, API keys) in localStorage OR sessionStorage; any JavaScript in the origin (including XSS) can read them. No HttpOnly-style protection exists.
    2. OWASP ASVS V3.2.3 / 'client side storage does not contain secrets'. - Sensitive data must not be placed in web storage.
    3. Browser session-restore behavior. - sessionStorage is persisted to disk and restored after crash/'reopen closed tab'/session restore, contradicting 'never written to disk'.
    4. OWASP Top 10 Client-Side Security Risks. - Storing API tokens in web storage is listed as a critical client-side risk.

  Strength of challenge: Strong

  Summary: This assumption is directly challenged on two fronts. First, the factual claim 'never written to disk' is false: browsers persist sessionStorage to disk for crash recovery and session restore, so the data can survive on disk. Second, the security premise is contrary to explicit OWASP guidance: secrets should not live in ANY web storage (session or local) because a single XSS reads the entire origin's storage; sessionStorage's shorter lifetime is a marginal improvement, not 'the right posture'. The recommended postures are HttpOnly/SameSite cookies, a backend-for-frontend, or holding the secret only in a Web Worker / ephemeral memory.

  Specific risks: An XSS or malicious dependency exfiltrates the user's API key; on shared machines, a restored session re-exposes the key; users may over-trust a posture OWASP classifies as a critical risk.

  Mitigations available: Hold keys in-memory only (JS closure / Web Worker, never web storage); prefer BFF/proxy so the raw key never reaches the client; if web storage is unavoidable, document the XSS residual risk explicitly and minimize lifetime.

  STEELMAN:
    Item: ASSUMPTION-359
    Strongest counterargument: For a PUBLIC artifact where any injected script reads origin storage, sessionStorage offers essentially no confidentiality for a secret; the 'never on disk' belief is additionally false due to session restore, so the stated posture is both factually wrong in part and against established guidance.
    What would need to be true for C2A2 to be safe: There is no untrusted script in the origin (no third-party deps, no XSS) AND session restore is disabled - conditions a public artifact cannot guarantee.
    How to test: Inject a benign test script and confirm it can read the key from sessionStorage; trigger session restore and check whether the key reappears from disk.

  Search scope: OWASP web-storage guidance; session-restore persistence. Comprehensive.

  Recommendation: CHALLENGED
