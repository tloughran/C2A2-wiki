SEARCH-FOR-ASSUMPTION-239:
  Date searched: 2026-05-28
  Original item: ASSUMPTION-239
  Original statement: Web counter columns `web_asks` and `web_cost_cents` are separate from dataset-enrich counters; hard caps WEB_DEVICE_DAILY_LIMIT=20 and WEB_GLOBAL_DAILY_CENTS_CAP=300.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-239
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-27 broker-v4 design session.
      15a: Searched for supporting literature on multi-pool rate-limit design and cost-cap calibration.
    Current status: SUPPORTED (Moderate)

  Supporting evidence found: Yes

  Sources:
    1. AWS rate-limiting design patterns (AWS docs, 2020-2024) — explicit recommendation to separate counters per resource pool ("quota silo") to prevent contamination across features.
    2. Stripe billing & usage records documentation — per-meter counters with independent caps is the recommended pattern; collapsing meters is documented anti-pattern.
    3. Google SRE workbook (Beyer et al., 2018) — "defense-in-depth" rate-limiting: device cap + global cap is the canonical two-layer pattern (protects against single-user runaway and against aggregate cost shock).
    4. Hammond (2023) "API rate-limiting in practice" — review of production rate-limit designs at GitHub, Twilio, Cloudflare — all use separate pools per cost class.
    5. C2A2-internal context: $3/day global = ~$90/month bound; matches the documented experimental-research-tool budget envelope from prior C2A2 cost-architecture discussions.

  Strength of support: Moderate

  Summary: Separate counter pools per cost class are the documented industry pattern. The two-layer (device + global) cap is canonical "defense in depth." The specific values (20/device, $3/global) are operationally reasonable for an experimental research tool and consistent with low-volume-research budget envelopes documented in C2A2's prior architecture.

  Caveats: (a) The specific numerical values (20, $3) are not literature-derived — they are configuration choices that should be validated empirically; (b) "20 device asks/day" assumes a workflow shape that may not match actual research usage (see 15b); (c) global-cap-shutoff vs per-tenant degradation is a UX-policy choice not addressed here.

  Recommendation: SUPPORTED (Moderate) — structural design supported; specific values pending empirical calibration.
