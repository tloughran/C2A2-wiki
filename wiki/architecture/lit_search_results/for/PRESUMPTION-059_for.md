SEARCH-FOR-PRESUMPTION-059:
  Date searched: 2026-04-20
  Original item: PRESUMPTION-059
  Original statement: "Chrome profile auth for claude.ai is user-maintained out-of-band (no alternative ingestion channel defined)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-059
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from morning-chat-scrape session 2026-04-20 shifting to a new failure mode without triggering escalation or alternative ingestion
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. User-owned-credential model (OAuth 2.0 best practices RFC 6749; SAML identity federation docs): user-maintained credentials ARE a legitimate model — user owns the auth state, system does not try to impersonate or recover. Supports the "out-of-band" commitment in principle.
    2. Defensive programming literature (Code Complete — McConnell 2004; Clean Code — Martin 2008): single-channel designs are tolerable when the channel is understood to be a single point of failure and the consequences of failure are visible to the user. If Chrome-auth is the ONLY ingestion path, its failure must be surfaced.

  Strength of support: Weak

  Summary: The "user maintains auth out-of-band" commitment is defensible in principle — it respects user ownership of credentials and avoids auth-recovery anti-patterns. HOWEVER, the PRESUMPTION is the SECOND half of the claim: "and no alternative ingestion channel is defined." Literature does not support single-channel designs without fallback or escalation when the single channel has demonstrated recurring failure (5+ days of Chrome issues as of 2026-04-20). The OPERATIONAL-DRIFT cluster that PRESUMPTION-059 joins has been accumulating evidence that single-channel design is failing in practice.

  Caveats: (a) Adding a fallback channel does not mean auto-recovering the auth — it could be as simple as an escalation trigger (notify Tom when Chrome auth fails); (b) the literature supports the out-of-band commitment while also requiring failure-visibility + escalation, which is the gap the presumption surfaces; (c) there may be API-level paths to claude.ai content (conversation export) that have not been audited as fallback candidates.

  Recommendation: NO-SUPPORT-FOUND (the "out-of-band auth" commitment is defensible; the "no alternative channel defined" half is not literature-supported; graceful degradation and escalation-on-precondition-failure are standard reliability-engineering practices)
