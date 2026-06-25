SEARCH-AGAINST-PRESUMPTION-395:
  Date searched: 2026-06-25
  Original item: PRESUMPTION-395
  Original statement: "That sessionStorage is meaningfully 'never on disk' and tab-close clearing captures the public-artifact threat model"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-395
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: threat model reduced to disk-persistence and tab lifetime; twin of ASSUMPTION-359
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Browser session-restore behavior. - sessionStorage IS persisted to disk for crash recovery / 'reopen closed tab' / session restore, so 'never on disk' is false.
    2. OWASP HTML5 / Web Storage guidance. - Any script in the origin (XSS, malicious dependency) reads sessionStorage; tab lifetime is irrelevant to this dominant threat.
    3. OWASP Top 10 Client-Side Security Risks. - The threat model for client secrets centers on script-access and shared-machine exposure, not disk persistence.

  Strength of challenge: Strong

  Summary: Strongly challenged on the same grounds as its twin (ASSUMPTION-359). First, 'never on disk' is factually wrong: session restore writes sessionStorage to disk. Second, the threat model is mis-scoped: for a public artifact the dominant risks are XSS/malicious-dependency script access (which reads sessionStorage regardless of lifetime) and shared-machine/session-restore exposure - none addressed by 'cleared on tab close'. Tab lifetime is close to irrelevant to the real attack surface.

  Specific risks: Mis-scoped threat model gives false assurance; a single XSS or a restored session on a shared machine exposes user API keys.

  Mitigations available: Hold secrets in-memory/Web Worker only or proxy via a backend; model XSS and session-restore explicitly; do not rely on tab-close clearing as protection.

  STEELMAN:
    Item: PRESUMPTION-395
    Strongest counterargument: The relevant threat to a public artifact's client-held secret is script read-access and shared-machine/session-restore exposure; framing safety around disk-persistence and tab lifetime answers the wrong question and the 'never on disk' premise is additionally false.
    What would need to be true for C2A2 to be safe: No untrusted script can run in the origin AND session restore is disabled - unattainable guarantees for a public artifact.
    How to test: Trigger session restore and confirm key persistence; inject a benign script to confirm read access from sessionStorage.

  Search scope: Session-restore persistence; client-secret threat modeling. Comprehensive.

  Recommendation: CHALLENGED
