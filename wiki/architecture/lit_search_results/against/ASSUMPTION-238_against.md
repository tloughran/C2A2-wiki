SEARCH-AGAINST-ASSUMPTION-238:
  Date searched: 2026-05-28
  Original item: ASSUMPTION-238
  Original statement: Broker stays generic — the `tab` request field is analytics-only and does NOT gate behavior server-side; per-tab caps/templates/routing live on the client.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-238
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted.
      15b: Searched for challenging literature on deferred-logic compound debt and analytics-fields drifting into behavior.
    Current status: PARTIALLY-CHALLENGED (Moderate)

  Challenging evidence found: Yes

  Sources:
    1. Hunt & Thomas "Pragmatic Programmer" — broken-window theory: analytics-only fields that look usable drift into ad-hoc behavioral branches over time; "we'll fix it later" is documented anti-pattern.
    2. Brown et al. (2015) "Hidden Technical Debt in Machine Learning Systems" — generic-broker + per-client-logic patterns produce documented compound debt as clients evolve; the cost of later server-side migration grows nonlinearly.
    3. Fowler (2014) "Microservices" — explicit caveat against "anemic gateway" pattern: server-side intelligence is needed for cross-client policies; pure-generic brokers eventually grow ad-hoc server-side logic anyway.
    4. Kreps (2014) "Log: What Every Software Engineer Should Know" — counter-contamination across feature pools is the typical failure mode when server stays generic and client adds caps; coordination problems emerge at scale.
    5. C2A2-internal: if web_enrich cost characteristics diverge significantly per tab, server-side awareness becomes necessary for cost-cap enforcement; the analytics-only stance forecloses this.

  Strength of challenge: Moderate

  Summary: The generic-broker pattern has known failure modes. Analytics-only fields drift into behavior under "we'll add it later" pressure. Per-client cap enforcement creates coordination problems that server-side logic resolves more cleanly. The compound-debt cost of late server-side migration is empirically substantial. The pattern works at small scale but degrades as client complexity grows.

  Specific risks: (a) Per-client caps create cap-bypass surface (any client can claim any tab); (b) cost-cap enforcement is decentralized — harder to audit; (c) future server-side requirement is more expensive than now; (d) "tab" field becomes an unenforceable contract — clients may send wrong values.

  Mitigations available: (a) Document the migration trigger (when to move from analytics-only to behavior-gating); (b) server-side validation of `tab` value (well-formed only, not behavior-gating); (c) periodic check whether `tab` is being used for behavioral branching client-side; (d) maintain a single migration-path doc.

  Recommendation: PARTIALLY-CHALLENGED (Moderate)

  STEELMAN:
    Item: ASSUMPTION-238
    Strongest counterargument: Generic brokers are simple to ship but produce compound debt when client behavior grows. The "tab" field starts as analytics, drifts into client-side branching, then into server-side migration under pressure — at substantially higher cost than if server-side awareness had been built from the start. The pattern is a documented anti-pattern in mature distributed-systems literature when the per-client logic is non-trivial.
    What would need to be true for C2A2 to be safe: Either (a) per-tab logic remains genuinely trivial indefinitely, or (b) explicit migration trigger and re-evaluation date is documented now, before the asymmetry compounds.
    How to test: 90-day audit: has any per-tab logic appeared on the server side? has client-side per-tab logic grown? Track migration debt explicitly.
