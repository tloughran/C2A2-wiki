SEARCH-FOR-ASSUMPTION-075:
  Date searched: 2026-04-28
  Original item: ASSUMPTION-075
  Original statement: "Specialist-agent override of 30-day cadence is permissible when 'significant work not yet captured' (the Levin override)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-075
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-27 — Levin tradition specialist invoked early-refresh override
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Sources:
    1. CDC "Influenza Surveillance Practices" — surveillance systems routinely include expert-judgment overrides on cadence ("trigger when an unusual event is observed") as adjuncts to schedule-based monitoring. Endorsed pattern in public-health surveillance.
    2. Vaughan (1997) "The Trickle-Down Effect" — research on professional judgment in operational pipelines documents that domain specialists with topic familiarity reliably identify when refresh is warranted faster than schedule-only monitors.
    3. Klein (1998) "Sources of Power" — recognition-primed decision-making literature supports specialists' ability to recognize "this is significant" patterns ahead of formal evidence aggregation.
    4. Cochrane "Living Systematic Reviews" methodology (Elliott et al. 2017) — explicitly allows expert-triggered early refresh outside the regular cadence when "important new evidence" is identified, treating it as a feature rather than an exception.
    5. SRE alerting literature (Beyer et al. 2016) — combines schedule-based and event-based triggers; the dual-trigger pattern is the supported design rather than schedule-only.

  Strength of support: Moderate

  Summary: Expert-judgment override of fixed cadences is a well-established pattern in public-health surveillance, operational pipelines, and living systematic reviews. The dual-trigger design (schedule + event) is endorsed as more robust than schedule-only monitoring. Support is moderate rather than strong because the literature consistently pairs the override with audit/calibration mechanisms (which ASSUMPTION-075 does not yet specify; see PRESUMPTION-087).

  Caveats: (a) Support depends on the override being audited or calibrated — a self-correcting specialist override without audit is a documented failure mode. (b) The specific phrase "significant work not yet captured" is a domain-specific framing without canonical literature attestation; closely related but not identical to "important new evidence" in Cochrane.

  Recommendation: PARTIALLY-SUPPORTED (the dual-trigger pattern is well-supported; the supported version is paired with an audit mechanism, which ASSUMPTION-075 does not yet specify and which PRESUMPTION-087 surfaces as a separate concern)
