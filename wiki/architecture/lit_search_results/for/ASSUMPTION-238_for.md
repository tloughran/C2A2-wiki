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
