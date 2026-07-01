SEARCH-AGAINST-PRESUMPTION-421:
  Date searched: 2026-06-30
  Original item: PRESUMPTION-421
  Original statement: "That a human will notice metric staleness and trigger regen by hand — "someone will look" as the liveness mechanism, no watchdog; freeze ran 06-17→06-29 undetected until a chance question."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-421
    Item type: PRESUMPTION (unstated)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference
      15b: Searched for challenging literature (first-time, genuine web search 2026-06-30)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Elementary Data / Sifflet / Metaplane — the entire data-freshness discipline exists because "stale data looks perfectly normal" and humans do NOT reliably notice; the prescribed control is automated freshness SLAs with alerting.
    2. Streamkap, "Data Freshness Monitoring" — freshness must be machine-monitored with thresholds and alerts; manual noticing is not a control.
    3. C2A2-internal: this is the reflexive form of PREMISE-086 (monitor-of-monitor / dead-man's-switch / "absence is the signal") and of REVISE-147 (scheduler dead-man's-switch). A freeze that ran 06-17 -> 06-29 undetected is exactly the liveness single-point-of-failure PREMISE-086 was validated to prevent.

  Strength of challenge: Strong

  Summary: Strong challenge with both literature and a live failure: 'someone will look' is not a liveness mechanism, and the 12-day undetected freeze proves it. The presumption is internally inconsistent with the system's own validated PREMISE-086.

  Specific risks: Any axis can freeze indefinitely between chance human glances; the system silently reports stale state as current. This is a liveness single-point-of-failure.

  STEELMAN: For a low-stakes display with a highly-attentive single operator, a watchdog might seem like over-engineering — but the operative evidence refutes even that: the MOST expert viewer missed a 12-day freeze, so the attentiveness assumption fails for the actual user.

  Recommendation: CHALLENGED (Strong — no support, live counter-evidence, and contradicts validated PREMISE-086)
