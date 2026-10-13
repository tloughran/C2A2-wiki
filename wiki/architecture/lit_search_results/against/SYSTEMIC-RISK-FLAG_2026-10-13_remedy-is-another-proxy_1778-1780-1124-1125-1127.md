SYSTEMIC-RISK-FLAG:
  Date: 2026-10-13
  Affected items: ASSUMPTION-1778, ASSUMPTION-1780, PRESUMPTION-1124, PRESUMPTION-1125, PRESUMPTION-1127
    (PRESUMPTION-1128 is adjacent: hedges carried as prose are themselves a dropped-signal proxy)
  Related prior flag: SYSTEMIC-RISK-FLAG_2026-10-12_silence-read-as-evidence.md. That flag covered
    absence of signal read as evidence. This flag extends it to presence of a substitute signal read as
    evidence.

  PROVENANCE:
    Origin: 15b (cross-item synthesis). The underlying items originate in 14a (1778, 1780) and 14b
      (1124, 1125, 1127).
    Chain: [14a/14b → 15b → SYSTEMIC-RISK]
    Transform: 15b (2026-10-13) searched each item independently and identified a common
      vulnerability across the *_against.md files of the same date.
    Current status: FLAGGED

  Common vulnerability: each proposed remedy replaces a failed proxy with another proxy one level up,
    and leaves open whether the new proxy tracks the target state end to end.
      - 1778: "record exists" → "record fresh / heartbeat". Heartbeats are the canonical victim of gray
        failure.
      - 1780: full paper → abstract or talk outline. The abstract is a proxy for the claims, and spin and
        discordance are common.
      - 1124: proxy → "validated proxy". Validation is mechanism-specific and mostly weak (CAST; Prasad
        2015).
      - 1125: independent check → peer verdict, or a re-check on the same substrate. Correlated
        failures mean "independent" is itself a proxy for independence.
      - 1127: fatigue → alert count. Interventions are scored on alarm volume, not on faults caught.
  Literature basis:
    - Huang et al. 2017 HotOS (full text): differential observability, where the observer's proxy is
      green while the consumer sees failure; also detector-driven recovery causing a cascade.
    - Fleming & DeMets 1996; Prasad et al. 2015: surrogate validation is mechanism-specific and
      usually weak.
    - Knight & Leveson 1986: nominally independent versions fail together.
    - Winters et al. 2018; Paine et al. 2016: alarm interventions are evaluated on intermediate counts.
    - Manheim & Garrabrant 2018: proxy validity degrades under optimisation pressure.
  Risk level: High
  Recommendation (for 14a/14b reconciliation; not a design mandate): For each remedy, name its
    reference standard. What end-to-end, consumer-side observation would show that the remedy's signal
    agrees with the true state? Schedule periodic sampling of proxy-target agreement. A remedy
    without a named reference standard should be treated as having moved the proxy up one level, not
    as having closed the gap.
