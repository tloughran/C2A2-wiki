SEARCH-FOR-ASSUMPTION-359:
  Date searched: 2026-06-25
  Original item: ASSUMPTION-359
  Original statement: "Storing API keys in sessionStorage (not localStorage) is the right privacy posture - cleared on tab close, never written to disk"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-359
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted (twin of PRESUMPTION-395)
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: Partial

  Sources:
    1. (Partial only) MDN / web-platform docs: sessionStorage is scoped per-tab and cleared when the tab/session ends, so it is more EPHEMERAL than localStorage - a relative, not absolute, improvement.
    2. OWASP HTML5 Security Cheat Sheet & Web Storage testing guide - note sessionStorage's shorter lifetime, but explicitly advise AGAINST storing secrets in any web storage.

  Strength of support: Weak

  Summary: Only weak, relative support exists. It is true that sessionStorage is more ephemeral than localStorage (per-tab, cleared on normal tab close), so as a comparison 'sessionStorage > localStorage for secret lifetime' is defensible. But the assumption's stronger claims - that this is 'the right privacy posture' and that secrets are 'never written to disk' - are not supported and are contradicted by the security literature (see 15b). The supportive case tops out at 'marginally less bad than localStorage'.

  Caveats: The 'never written to disk' claim is factually wrong (session-restore can persist sessionStorage to disk), and OWASP guidance is that NO web storage should hold secrets because any XSS reads it. Supportive evidence does not reach the assumption's actual claims.

  Search scope: Web-storage lifetime semantics; OWASP web-storage guidance. Adequate.

  Recommendation: NO-SUPPORT-FOUND
