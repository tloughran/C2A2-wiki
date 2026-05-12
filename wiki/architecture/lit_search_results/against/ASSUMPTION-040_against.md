SEARCH-AGAINST-ASSUMPTION-040:
  Date searched: 2026-04-18
  Original item: ASSUMPTION-040
  Original statement: "ChatGPT projects are strictly account-scoped (no cross-account project visibility in same Chrome instance)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-040
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-18 route-elimination logic (ND vs. personal)
      15b: Searched for challenging literature
    Current status: NO-CHALLENGE-FOUND (with scope caveats)

  Challenging evidence found: No (for the central claim); partial for scope-related edge cases.

  Sources:
    1. Cookie-jar cross-contamination literature (Englehardt & Narayanan 2016; browser cookie/tracking-protection work): provides no mechanism by which account-A's project renders in account-B's session in the same browser; cross-account visibility is not accidentally produced by browser behavior.
    2. OpenAI post-incident disclosures (2023 ChatGPT incident disclosing titles across users — Redis caching bug): the historical exception is a *vendor-side* caching bug, not a cross-account visibility *by design*. It is a data-leak incident, not counter-evidence to account scoping as the intended model.
    3. Shared / family-mode browser cases (e.g., macOS shared profiles, Chrome profile auto-sign-in): a user who is simultaneously signed in to multiple ChatGPT accounts in adjacent tabs can confuse which account is active. This is user-confusion, not a cross-account visibility defect.
    4. ChatGPT "shared projects / invite a collaborator" features (rolled out in 2025): deliberately extend visibility across accounts within a workspace. This is not a counterexample to account-scoping — it is an explicit, invite-gated sharing mechanism — but it weakens the absolute form of the claim.

  Strength of challenge: Weak

  Summary: No credible literature suggests that ChatGPT projects leak across accounts in the same browser by accident. The 2023 title-leak incident is a reminder that vendor-side caching bugs can cause one-off cross-user data visibility, but it was a defect, not a feature of the access model. The only substantive qualifier to the universal claim is the explicit collaborator-invite feature: projects can be *shared* across accounts, but only deliberately. For the route-elimination logic's intended meaning — "I cannot automatically see another account's projects just by being signed in elsewhere" — the assumption holds.

  Specific risks: Low. The main risk is user-confusion across simultaneously-authenticated tabs, which would produce a wrong-account ingest rather than a data-leak.

  Mitigations available: Use distinct Chrome profiles per account to eliminate same-instance adjacency. Verify active account in the UI before each scrape. Prefer profile separation over "rely on correct tab" discipline.

  Recommendation: NO-CHALLENGE-FOUND (for the design-level claim); a small scope qualifier applies to deliberate sharing and to user-confusion failure modes.
