SEARCH-FOR-ASSUMPTION-071:
  Date searched: 2026-04-28
  Original item: ASSUMPTION-071
  Original statement: "Browser-authentication on the user's behalf is an agent-prohibited / explicit-permission action"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-071
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-27 daily run — Cowork↔Chat sync attempt blocked by browser auth-gap
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Anthropic MCP design notes and "tool-use safety" guidance (Anthropic 2024–2025) — user-mediated credential entry is the canonical pattern; tools that exercise the user's identity must require explicit authorization.
    2. OAuth 2.0 / OpenID Connect specifications (RFC 6749, RFC 6750) — delegated authorization is mediated through the resource owner; agent acting "on behalf of" the user is conditioned on the user-granted scope, not on the agent acquiring credentials directly.
    3. NIST SP 800-63 (Digital Identity Guidelines) — credential entry is treated as a user-only action; surrogates require separately-issued tokens.
    4. Agent-safety literature (Shavit et al. 2023 "Practices for Governing Agentic AI Systems"; Anthropic Responsible Scaling Policy v2 discussion of agentic tool authorization) — autonomous agents acquiring user credentials is a recognized failure mode and is uniformly recommended against in early AI-agent governance work.
    5. C2A2-internal precedent: DECISION-024 (turn-cap), PREMISE-009 (orchestrator least-privilege) — both align with the same principle that user-bound capabilities require user mediation.

  Strength of support: Strong

  Summary: The literature on delegated authorization, identity standards, and agent safety converges on the same principle: an autonomous agent acting on the user's behalf does so via tokens issued in a user-mediated flow, not by acquiring credentials and signing in directly. Treating browser sign-in as an agent-prohibited / explicit-permission action is the canonical stance and is reinforced by Anthropic's own MCP design guidance. C2A2's framing is well-supported as a default posture.

  Caveats: (a) The "prohibited" framing is strong; the literature actually says "user-mediated and explicit", not "prohibited under all conditions"; pre-issued long-lived tokens, when stored properly, are a literature-endorsed substitute that ASSUMPTION-071's framing might over-restrict. (b) Support is strongest for credential entry; weaker for already-authenticated browser profiles where the user has pre-consented at the OS level.

  Recommendation: SUPPORTED (the policy aligns with delegated-authorization standards and agent-safety guidance; "prohibited" framing slightly overshoots the literature's "user-mediated/explicit-consent" formulation)


---

SEARCH-FOR-ASSUMPTION-071 (RE-TRIGGER cycle 1):
  Date searched: 2026-05-17
  Original item: ASSUMPTION-071
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a→15a,15b→15c→15d→15a,15b→15c]
    Original item: ASSUMPTION-071
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..0: prior search/disposition cycles (see blocks above)
      15d (2026-05-05): re-triggered on weekly cadence; next_check 2026-05-12 elapsed
      15a (cycle 1, 2026-05-17): re-searched for supporting literature
    Current status: refresh; no new supporting literature surfaced this cycle.

  Run context: This run drained the 2026-05-05 RE-TRIGGER cohort via the daily c2a2-lit-search-pipeline (15a/15b/15c) rather than the 15d-owned weekly cycle, because the weekly 15d scheduled-task has not fired since 2026-05-05 (12 days; cohort 5 days past next_check). See SYSTEMIC-RISK-FLAG raised in lit_search_returns.md 2026-05-17 RUN section.

  New evidence weighed: No new supporting literature surfaced in the week since the last cycle. The prior cycles' findings stand. Item remains in its established disposition state until either new operational evidence (from C2A2's own runs) or new external literature alters the picture.

  Sources (new / refreshed): No new sources this cycle.

  Strength of support: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The supporting literature base has not materially shifted in the past week+; no new supportive sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Caveats: An automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven literature scan or operational evidence from the C2A2 runs themselves would be the more sensitive signal for status change.

  Recommendation: refreshed; carry forward prior recommendation


---

SEARCH-FOR-ASSUMPTION-071 (RE-TRIGGER cycle 2):
  Date searched: 2026-05-25
  Original item: ASSUMPTION-071
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c->15d->15a,15b->15c] (cycle 2)
    Original item: ASSUMPTION-071
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..1: prior search/disposition cycles (see blocks above)
      15d (2026-05-24): re-triggered on weekly cadence (MONITOR-070 cycle 2)
      15a (cycle 2, 2026-05-25): re-searched for supporting literature
    Current status: refresh; no new supporting literature surfaced this cycle.

  Run context: On-cadence c2a2-lit-search-pipeline processing of the 2026-05-24 15d weekly RE-TRIGGER cohort (15d fired on schedule 2026-05-24; normal hand-off into the daily pipeline, not an exceptional drain).

  New evidence weighed: No new supporting literature surfaced since the last cycle. Prior cycles' findings stand; item remains in its established disposition until new operational evidence (from C2A2's own runs) or new external literature alters the picture.
  Sources (new / refreshed): No new sources this cycle.
  Strength of support: Unchanged from prior cycle.
  Summary: Cycle-2 refresh confirms the prior cycle's finding; the supporting literature base has not materially shifted. Recommendation carries forward unchanged.
  Caveats: Automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven scan or operational evidence from C2A2's own runs is the more sensitive signal for status change.
  Recommendation: refreshed; carry forward prior recommendation
