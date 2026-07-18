SEARCH-FOR-ASSUMPTION-444:
  Date searched: 2026-07-12
  Original item: ASSUMPTION-444
  Original statement: "The Chrome login is the single root cause of the 9-day sync outage; signing back in restores both directions."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-444
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from 2026-07-11 EOD daily run
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. [Microsoft Learn Q&A, "Azure AD refresh token is getting invalid frequently." — Documents the standard mechanism: refresh tokens have absolute lifetimes and revocation triggers; once invalid, silent renewal stops and the integration is fully dead until an interactive re-login. Matches the observed pattern (sync silently stops; nothing recovers on its own; login is the specific remedy).]
    2. [OneUptime, "How to Fix 'An error occurred (ExpiredTokenException)'" (2026). — Expired credentials are a common, well-documented single proximate cause of total service-integration failure, and re-authentication is the documented complete fix in the credential-expiry case.]
    3. [flowgenius.in, "n8n Token Expired Error: Complete Fix Guide (Google, Microsoft, Slack)." — Practitioner literature on sync/automation platforms: OAuth session expiry is the leading cause of bidirectional sync outages, and full re-login (not retry) restores both directions when expiry is the operative fault.]
  Strength of support: Moderate
  Summary: Authentication-expiry literature strongly precedents the hypothesized mechanism: an expired or logged-out browser session kills a sync integration completely and silently, and interactive re-login restores it. As a *leading hypothesis*, "Chrome login" is well-supported — it is the single most common cause of exactly this failure signature. What the literature supports is the priority of the hypothesis, not its exclusivity: sources establish that login expiry is sufficient to explain such outages, not that it is the only fault present after 9 days of downtime.
  Caveats: Support covers "login expiry can fully explain the outage and re-login is the right first move." The clauses "single root cause" and "restores both directions" are predictions verifiable only by the first post-login scrape and delivery runs — which is the queued empirical test, essentially free.
  Recommendation: PARTIALLY-SUPPORTED
