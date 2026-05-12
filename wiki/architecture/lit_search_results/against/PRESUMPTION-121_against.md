SEARCH-AGAINST-PRESUMPTION-121:
  Date searched: 2026-05-10
  Original item: PRESUMPTION-121
  Original statement: "Codex-style external-LLM diagnostic for Chrome MCP error presumed reliable enough to skip independent project-context adjudication — DIRECT EXTENSION OF PRESUMPTION-115 SYSTEMIC-RISK to chat-scrape failure-mode layer"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-121
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-09 EOD Codex Chrome-MCP-error-diagnostic adoption pattern
      15b: Searched for counter-evidence on external-LLM root-cause-attribution failure modes
    Current status: CHALLENGED

  Sources:
    1. LLM-evaluation literature (Ribeiro et al. 2020; Bowman & Dahl 2021) — cross-LLM diagnostic-reliability studies show systematic failure modes (training-data overlap, prompt-sensitivity, plausible-but-wrong attribution).
    2. Review-aggregation frameworks (GRADE; Cochrane Handbook; AMSTAR-2) — uniformly require independent local adjudication of external-source recommendations; near-verbatim adoption is contraindicated.
    3. Software-engineering external-tool integration patterns — local-context adjudication is canonical for any external-tool recommendation before adoption.
    4. PRESUMPTION-074 / PRESUMPTION-115 cluster — same failure mode at specialist self-attribution and external-LLM prioritization layers; this presumption is the third instance.
    5. C2A2-internal: "One source treated as primary signal without adjudication" pattern at three layers in <30 days is structural rather than incidental.

  Strength of challenge: Strong

  Summary: The presumption is strongly challenged by LLM-evaluation, review-aggregation, and software-engineering literatures. The challenge is uniform: external-LLM diagnostic uptake without independent project-context adjudication is documented failure mode. The recurrence-without-remediation pattern (PRESUMPTION-074 → PRESUMPTION-115 → PRESUMPTION-121) is the structural signal: this is the third instance of the same failure mode at successive layers.

  Specific risks: (a) Plausible-but-wrong external diagnostic adopted without local check; (b) recurrence of PRESUMPTION-074 / 115 SYSTEMIC-RISK at chat-scrape failure-mode layer; (c) DECISION-027 candidate scope must extend to external-tool-review per ASSUMPTION-099.

  Mitigations available: (a) Independent project-context adjudication of external diagnostics; (b) DECISION-027 scope extension; (c) cross-LLM divergence test for high-stakes diagnostics.

  Recommendation: CHALLENGED (literature consensus strong; recurrence-without-remediation pattern at SYSTEMIC-RISK level)

  STEELMAN:
    Item: PRESUMPTION-121
    Strongest counterargument: This is the third instance of the "external source treated as primary signal without adjudication" failure mode in <30 days (PRESUMPTION-074 specialist self-attribution; PRESUMPTION-115 external-LLM prioritization; PRESUMPTION-121 external-LLM diagnostic). Each instance has been REVISE'd individually but the pattern recurs at successive layers — this is the structural signal that the architectural-discipline track lags behind the surfacing track. The LLM-evaluation literature documents specific failure modes (training-data overlap, prompt-sensitivity) that local adjudication is designed to catch; near-verbatim adoption skips that check by construction.
    What would need to be true for C2A2 to be safe: (a) Independent project-context adjudication step inserted before external-LLM diagnostic uptake; (b) DECISION-027 scope extension per ASSUMPTION-099; (c) cross-LLM divergence test for high-stakes diagnostics.
    How to test: Generate the same Chrome MCP diagnostic from a different LLM family; check whether the diagnoses agree; if they diverge, the near-verbatim adoption was selection-biased.
