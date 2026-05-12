SEARCH-FOR-ASSUMPTION-040:
  Date searched: 2026-04-18
  Original item: ASSUMPTION-040
  Original statement: "ChatGPT projects are strictly account-scoped (no cross-account project visibility in same Chrome instance)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-040
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-18 scrape-session route-elimination logic (ND vs. personal account separation)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. OpenAI ChatGPT Projects help documentation: projects are "tied to your account" and only visible to the signed-in user on that account.
    2. OpenAI Enterprise/Teams data-isolation statements: workspace/project content is scoped to the workspace; cross-workspace visibility is not provided.
    3. SaaS multi-tenancy design patterns (Krebs, Momm & Kounev 2012 "Architectural Concerns in Multi-Tenant SaaS"): per-tenant data isolation at the project/workspace level is the default and expected pattern.
    4. OWASP / session-management authorities: distinct web sessions in the same browser are sandboxed by cookie partitioning; ChatGPT's session model follows standard cookie-auth scoping.
    5. Browser cookie-partitioning behavior for same-origin sessions: switching accounts in a single tab replaces session cookies; there is no mechanism by which one account's content renders in another's DOM without an explicit switch.

  Strength of support: Strong

  Summary: Account-scoping of projects is the standard and documented SaaS tenancy pattern; ChatGPT's help documentation makes it explicit, and cookie/session-management fundamentals rule out accidental cross-account visibility in the same Chrome instance. Both the vendor's product statements and generic web security principles align on this point. The assumption is well-grounded as a design-level claim about ChatGPT's access model.

  Caveats: Account-scoping is about *visibility*, not about *data-ingestion paths*: a file uploaded under account A can of course be manually re-uploaded or copy-pasted under account B. "Strictly account-scoped" here refers to project-level visibility, not an absolute barrier against data flow between accounts operated by the same user. Also: browser profile sharing plus a "stay signed in" state across accounts in adjacent tabs can create user-experience confusion about *which* account is active, even though the data itself is still scoped.

  Recommendation: SUPPORTED
