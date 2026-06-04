SEARCH-FOR-ASSUMPTION-263:
  Date searched: 2026-05-31
  Original item: ASSUMPTION-263
  Original statement: Re-authenticating claude.ai in the extension's Chrome profile is the single fix that restores the full daily sync loop -- both the morning intake scrape and the evening cowork-to-chat delivery. One re-login unblocks both directions.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-263
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-05-30 EOD self-awareness batch (3rd-cycle logout).
      15a: Searched single-cause/single-fix recovery in auth-gated pipelines and session-token expiry as a common root cause.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. drdroid.io / Stytch / Supabase auth diagnosis guides, 2025-26. "Session Expired / Invalid Session Token." — Natural JWT/session-token expiry is the single most common root cause of auth-gated breakage; the canonical resolution is to prompt re-login, which regenerates a valid token.
    2. oneuptime.com, 2026. "How to Fix 'Expired Token' Errors in OAuth2." — Re-authentication is the standard recovery path for expired-credential outages; one fresh login restores access for all flows sharing that credential.
    3. C2A2-internal: both loop directions (Chrome scrape + cowork→chat delivery) ride the *same* claude.ai session in the *same* Chrome profile, so a shared-credential model predicts one re-login restores both.

  Strength of support: Moderate

  Summary: When two channels depend on one shared session credential, expiry of that credential is a single common root cause and a single re-login is the expected, sufficient fix for both — exactly the shared-credential topology C2A2 reports. Token-expiry-as-root-cause is the best-documented failure mode in auth-gated pipelines, and re-login is its canonical remedy. Support is Moderate (not Strong) because the literature supports the *mechanism* (shared-credential expiry → single fix) conditional on expiry actually being the sole cause.

  Caveats: Support holds only if the breakage is genuinely a single shared-credential expiry and not a compounded failure (profile/cookie corruption, a second independent break in either channel). The claim "one re-login unblocks both AND stays fixed" is stronger than "one re-login is the right first action," and the literature only firmly supports the latter.

  Recommendation: PARTIALLY-SUPPORTED
