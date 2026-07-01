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


---

SEARCH-AGAINST-ASSUMPTION-270 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-270
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-270
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..2: prior search/disposition cycles (see blocks above)
      15d (2026-06-28): re-triggered on weekly cadence (catchup run; next_check elapsed)
      15b (cycle 3, 2026-06-30): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-06-28 (weekly catchup — first 15d fire since 2026-06-07; the 06-14 and 06-21 weekly runs did not fire, so the 06-28 run drained the accumulated due cohort). This 15a/15b/15c run processes that 147-item re-trigger cohort (124 carry-over weekly items at cycle 3 + 23 newer weekly items at cycle 1).
  Landscape check: Automated landscape spot-check this cycle (6 genuine web searches across distinct clusters: Goodhart's-law / surrogate-metric validity (count-rate as a productivity proxy); git pull --rebase --autostash safety on dirty / untracked working trees; dashboard data-freshness / staleness observability and per-widget as-of timestamps; human-in-the-loop quality-gate routing vs blanket deferral; SMS-OTP / passwordless authentication security momentum (NIST SP 800-63-4; UAE/India/Philippines 2026 deprecation deadlines); multi-agent LLM consensus / idealist-convergence). Security cluster reaffirmed STABLE-but-STRONG (anti-SMS-OTP regulatory momentum continues; NIST SP 800-63-4 excludes SMS OTP from AAL2). All other clusters reaffirmed prior for/against profiles; no disposition-flipping literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new challenging literature has surfaced in the week(s) since the last cycle. The prior cycles' challenge profile stands.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-3 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted; no new disconfirmatory sources surfaced during this automated cycle.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  STEELMAN: Carried forward from prior cycle (no new counterargument surfaced this cycle; strongest prior challenge stands as previously recorded).

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED)
