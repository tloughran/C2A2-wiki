SEARCH-AGAINST-ASSUMPTION-270:
  Date searched: 2026-06-04
  Original item: ASSUMPTION-270
  Original statement: An autonomous browser/sync agent must not authenticate as Tom; a lapsed claude.ai session is therefore a hard external blocker the pipeline cannot self-clear (re-auth is attended-only).

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-270
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the attended-only re-auth safety boundary.
      15b: Searched scoped delegated-credential / token-refresh patterns for unattended automation and the cost of a fully attended-only boundary.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. OAuth Client-Credentials flow / M2M auth (Scalekit; Airbyte "What is OAuth 2.0"). — There is an established third option between "agent logs in AS the user" and "a human must": the agent authenticates as its OWN service identity with a short-lived, scoped token. Background jobs and sync agents are a textbook use case. This directly challenges the dichotomy underlying the "attended-only" conclusion.
    2. Refresh tokens / token vaults for unattended automation (Auth0 Token Vault; nhimg OAuth refresh token). — Refresh tokens exist precisely so automation "that cannot keep prompting a human for re-authentication" can mint new access tokens unattended — without holding the user's password and without being the user. The "pipeline cannot self-clear" claim ignores this standard mechanism.
    3. Workload Identity Federation (Microsoft Entra; Curity least-privilege template). — Federated workload identity lets a workload exchange a platform identity for scoped IAM credentials with NO long-lived secret and NO user impersonation. A lapsed session need not be a hard external blocker; it can be a self-refreshing, least-privilege, revocable machine credential.

  Strength of challenge: Moderate-Strong

  Summary: The first clause ("must not authenticate as Tom") is sound and unchallenged. The SECOND clause — that a lapsed session is therefore a hard blocker the pipeline cannot self-clear, with re-auth necessarily attended-only — rests on a false dichotomy. The standard machine-to-machine patterns (client-credentials flow, refresh tokens, token vaults, workload-identity federation) are designed exactly for unattended automation to maintain access WITHOUT impersonating the user and WITHOUT a human in the loop, using short-lived, scoped, revocable credentials. So "self-clearing" is achievable while still honoring "never be Tom."

  Specific risks: Accepting attended-only as necessary builds a single point of failure into the autonomous pipeline: any lapsed session hard-blocks all sync indefinitely until Tom is present (the realized 06-03 failure), and — coupled with PRESUMPTION-300 — the pipeline then runs on accumulating undeliverable state instead of self-recovering.

  Mitigations available: Provision a scoped, least-privilege, revocable delegated credential (service identity / token-vault entry) for the sync channel ONLY, so the agent can refresh its own session unattended without ever carrying Tom's identity or broad authority. Keep human gating for anything beyond the narrow sync scope.

  STEELMAN:
    Item: ASSUMPTION-270
    Strongest counterargument: "Agent must not be Tom" is right, but it does NOT entail "re-auth is attended-only." That entailment only holds if the sole alternative to attended re-auth is user impersonation — which is false. The established M2M pattern (scoped service credential + refresh) gives unattended self-recovery under least privilege. Treating attended-only as a law, rather than as one conservative point on a spectrum, manufactures an availability single-point-of-failure that the field already knows how to avoid.
    What would need to be true for C2A2 to be safe: A delegated sync credential must be genuinely least-privilege (sync scope only), revocable, short-lived/refreshable, and auditable — so it adds minimal attack surface relative to the availability it restores. (Counter-tension: 15a's least-privilege/excessive-agency literature cautions that ANY standing refreshable credential on an autonomous agent is added attack surface — so this is a genuine capability-vs-surface tradeoff, not a free win.)
    How to test: Stand up a sync-scoped service token in a vault; on a dry run with Tom absent and the user session lapsed, confirm the agent refreshes ONLY the sync scope and completes delivery, and that the token cannot perform any non-sync action.

  Recommendation: PARTIALLY-CHALLENGED
