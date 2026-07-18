SEARCH-FOR-ASSUMPTION-428:
  Date searched: 2026-07-09
  Original item: ASSUMPTION-428
  Original statement: "Deferring the 117-item 15d refresh backlog is acceptable so long as the deferral is surfaced and a remedy recommended ('deferred and surfaced, not silent')."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-428
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extraction from cohort listing (2026-07-07 EOD)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. NIST, 2011. "SP 800-39: Managing Information Security Risk." NIST. — Codifies risk acceptance as a legitimate, sanctioned response when remediation cost outweighs impact, provided the acceptance is documented, owned, and time-bounded — the formal analog of "deferred and surfaced, not silent."
    2. ISC2, 2025. "Risk Acceptance: A Sticking-Plaster Solution?" ISC2 Insights. — Describes the documented risk-acceptance memo + risk-register pattern: deferral is acceptable practice when the item stays visible with compensating controls and an agreed remediation timeline; also documents the failure mode when acceptance becomes routine.
    3. Risk-register practice guides (V-Comply 2026; TrustCloud 2026). "Risk Register" guides. — Centralized registration of deferred items keeps risks visible through their lifecycle and is presented as materially better than undocumented deferral; supports the surfaced-vs-silent distinction directly.

  Strength of support: Moderate

  Summary: The assumption maps directly onto documented risk acceptance, a mainstream, standards-backed practice (NIST SP 800-39, ISO 31000 family): deferring remediation is acceptable when the deferral is recorded, visible to stakeholders, and paired with a recommended remedy and revisit point. The "surfaced, not silent" clause is precisely what the literature identifies as the difference between legitimate risk acceptance and negligence. Support is moderate rather than strong because the literature attaches conditions the bare assumption omits: an owner, a revisit date, and monitoring of cumulative accepted risk.

  Caveats: Support weakens when (a) surfaced items accumulate without action — the alert-fatigue and surfaced-but-unactioned literature (Vectra, Monte Carlo; Equifax 2017 case) shows surfaced findings buried in a triage backlog behave like silent ones; (b) no revisit date or owner is attached (surfacing without a trigger decays into wallpaper); (c) deferred premises go stale faster than the review cadence (117 items at 15d refresh implies a large staleness window). Acceptability is conditional on the deferral register actually being consumed.

  Search scope confidence: Comprehensive for risk-acceptance practice; preliminary for quantitative premise-staleness thresholds (none found).

  Recommendation: SUPPORTED
