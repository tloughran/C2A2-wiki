SEARCH-FOR-PRESUMPTION-395:
  Date searched: 2026-06-25
  Original item: PRESUMPTION-395
  Original statement: "That sessionStorage is meaningfully 'never on disk' and tab-close clearing captures the public-artifact threat model"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-395
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: the threat model is reduced to disk-persistence and tab lifetime; twin of ASSUMPTION-359
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: Partial

  Sources:
    1. (Partial) sessionStorage is cleared on normal tab close and is shorter-lived than localStorage - a relative improvement only.
    2. OWASP Web Storage testing guidance - acknowledges sessionStorage's shorter lifetime but does not endorse it as adequate secret protection.

  Strength of support: Weak

  Summary: As with its twin (ASSUMPTION-359), only weak relative support exists: sessionStorage is more ephemeral than localStorage. But the presumption's framing - that 'never on disk' and 'tab-close clearing' adequately capture the public-artifact threat model - finds no support; the threat model for a public artifact is dominated by XSS read-access and shared-machine/session-restore exposure, which tab-lifetime does not address.

  Caveats: Tab-lifetime/disk framing omits the dominant threats (XSS, session restore, shared machines). Supportive evidence does not reach the presumption's claim.

  Search scope: Web-storage threat modeling; OWASP guidance. Adequate.

  Recommendation: NO-SUPPORT-FOUND
