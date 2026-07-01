SEARCH-FOR-ASSUMPTION-238:
  Date searched: 2026-05-28
  Original item: ASSUMPTION-238
  Original statement: Broker stays generic — the `tab` request field is analytics-only and does NOT gate behavior server-side; per-tab caps/templates/routing live on the client.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-238
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-27 broker-v4 design session.
      15a: Searched for supporting literature on generic-API design and server/client separation of concerns.
    Current status: SUPPORTED (Moderate)

  Supporting evidence found: Yes

  Sources:
    1. Twelve-Factor App methodology (Wiggins, 2011) — explicit guidance that backing services should be generic and configurable, not application-aware; aligns with broker-generic stance.
    2. Fowler (2014) "Microservices" — principle of "smart endpoints, dumb pipes": the broker is a transport/policy layer, not a business-logic layer.
    3. Stripe API design (2010-2024) — canonical example of generic broker pattern: idempotency keys and `metadata` fields enable per-tenant analytics without server-side branching.
    4. AWS API Gateway design patterns (AWS docs, 2022-2024) — generic-route + downstream-classification is the documented preferred pattern over per-route branching at the gateway.
    5. Hunt & Thomas "Pragmatic Programmer" — DRY and orthogonality principles support keeping classification (tab) decoupled from execution (broker behavior).

  Strength of support: Moderate

  Summary: Generic-broker / per-tenant-on-client is a well-established industry pattern. The Twelve-Factor and microservices literatures explicitly favor it. The Stripe and AWS examples demonstrate the pattern at production scale. The "metadata-as-analytics-only" stance is canonical for keeping broker contracts stable while client behavior evolves.

  Caveats: (a) Pattern works best when client variants are similar in cost/security shape; if one tab has dramatically different cost (web_enrich-heavy vs not), server-side awareness becomes more defensible; (b) "analytics-only fields drift into behavior" is a known anti-pattern (see 15b); (c) the migration-cost argument ("one column add later") assumes future migrations remain cheap, which they may not.

  Recommendation: SUPPORTED (Moderate)


---

SEARCH-FOR-ASSUMPTION-238 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-238
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-238
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..2: prior search/disposition cycles (see blocks above)
      15d (2026-06-28): re-triggered on weekly cadence (catchup run; next_check elapsed)
      15a (cycle 3, 2026-06-30): re-searched for supporting literature
    Current status: refresh; no new supporting literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-06-28 (weekly catchup — first 15d fire since 2026-06-07; the 06-14 and 06-21 weekly runs did not fire, so the 06-28 run drained the accumulated due cohort). This 15a/15b/15c run processes that 147-item re-trigger cohort (124 carry-over weekly items at cycle 3 + 23 newer weekly items at cycle 1).
  Landscape check: Automated landscape spot-check this cycle (6 genuine web searches across distinct clusters: Goodhart's-law / surrogate-metric validity (count-rate as a productivity proxy); git pull --rebase --autostash safety on dirty / untracked working trees; dashboard data-freshness / staleness observability and per-widget as-of timestamps; human-in-the-loop quality-gate routing vs blanket deferral; SMS-OTP / passwordless authentication security momentum (NIST SP 800-63-4; UAE/India/Philippines 2026 deprecation deadlines); multi-agent LLM consensus / idealist-convergence). Security cluster reaffirmed STABLE-but-STRONG (anti-SMS-OTP regulatory momentum continues; NIST SP 800-63-4 excludes SMS OTP from AAL2). All other clusters reaffirmed prior for/against profiles; no disposition-flipping literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new supporting literature surfaced in the week(s) since the last cycle. The prior cycles' supportive findings stand.

  Sources (new / refreshed): No new sources this cycle.

  Strength of support: Unchanged from prior cycle.

  Summary: Cycle-3 refresh confirms the prior cycle's finding. The supporting literature base has not materially shifted; no new supportive sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Caveats: An automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; operational evidence from the C2A2 runs themselves remains the more sensitive signal for status change.

  Recommendation: refreshed; carry forward prior recommendation (SUPPORTED (Moderate))
