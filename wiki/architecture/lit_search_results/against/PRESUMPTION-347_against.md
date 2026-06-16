SEARCH-AGAINST-PRESUMPTION-347:
  Date searched: 2026-06-16
  Original item: PRESUMPTION-347
  Original statement: "[inferred] A model identifier pinned in a scheduled-task config stays valid indefinitely (06-14 morning scrape died on unavailable 'claude-fable-5')."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-347
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference from the 2026-06-14 scrape failure
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. API-deprecation practice (oneuptime 2026, "How to Handle API Deprecation"). — Vendor APIs and model endpoints are deprecated on the vendor's schedule, not the consumer's; an identifier valid today can be retired without the pinning client's involvement. Directly contradicts "pin stays valid indefinitely." The 06-14 failure is a textbook instance.
    2. Dependency/config drift and "pinning rot" (general SE reliability). — Pinned references to externally-controlled, mutable namespaces rot over time: the pin freezes the consumer's intent but cannot freeze the provider's availability. Reproducibility-by-pinning assumes immutable, durably-hosted artifacts; a hosted model alias satisfies neither, so the pin provides a false sense of stability.
    3. Graceful-degradation / fallback patterns (AWS Well-Architected REL05-BP01; "Agentic Design Pattern: Fallback Degradation," 2025; "Graceful Degradation Patterns in AI Agent Systems," Zylos 2026). — The consensus reliability pattern is to treat any external model/API as a SOFT dependency with a fallback chain (alternative model, cached response, human escalation). A pinned single model with no fallback is the named anti-pattern these sources exist to correct.

  Strength of challenge: Strong

  Summary: The presumption is strongly challenged and, in fact, already falsified by its own triggering event. External hosted model identifiers are deprecated/retired on vendor timelines; pinning freezes intent but cannot freeze availability, so pins to vendor-controlled namespaces rot. The reliability literature is unanimous that such dependencies must be soft, with version-availability checks and fallback chains. A pinned single model with no degradation path is a recognized anti-pattern, and its failure mode (the whole scheduled task dies when the alias disappears) is exactly what occurred.

  Specific risks: Any scheduled task pinned to a single hosted model silently becomes a time-bomb that fires whenever the vendor retires or renames that alias; the failure is total (task dies) and, combined with PRESUMPTION-348 (no liveness monitor), invisible for days. Multiple scheduled tasks likely share this pattern, so one deprecation can take down several pipelines at once.

  Mitigations available: (a) Preflight version-availability check — before running, verify the pinned model resolves; if not, fall back. (b) Fallback-model chain — ordered list (preferred → alternates → minimal) so a missing model degrades rather than kills the run. (c) Pin to a stable alias tier where the vendor guarantees longevity, or centralize the model ID in one config consumed by all tasks so a single edit fixes all. (d) Surface the substitution in the run log (fail-loud) so a silent downgrade is visible.

  STEELMAN:
    Strongest counterargument: Pinning is the correct default for reproducibility — an UNpinned model that silently changes underneath the task would corrupt outputs invisibly, which is arguably worse than a loud hard failure. So the pin was not the error; the error was the missing fallback layer. The presumption's instinct (pin for determinism) is sound; only the omission (no availability check / fallback) is the defect.
    What would need to be true for C2A2 to be safe: The pinned identifier would need either a vendor longevity guarantee OR a preflight check plus fallback chain, so that a retired alias degrades the run instead of killing it, and the substitution is logged.
    How to test: Enumerate every scheduled task's model pin; for each, attempt resolution and confirm a fallback exists. Any pin with no fallback is a live instance of this risk.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-06-16
    Affected items: PRESUMPTION-347, PRESUMPTION-348 (and the invisibility facet of ASSUMPTION-317)
    Common vulnerability: Scheduled/automated tasks assume positive state from the absence of a signal — a pin is assumed valid because nothing said otherwise (347), a task is assumed to have run because no failure was announced (348), work is assumed not-done because nothing was marked (317). All are instances of the project's standing "Absence ≠ success/event" common-mode cluster (prior 265/287/293/294/296).
    Literature basis: API-deprecation handling; dead-man's-switch/heartbeat monitoring; observability "guilty until proven innocent."
    Risk level: High
    Recommendation: A single coupled remedy covers the cluster: every scheduled task gets (1) a preflight check of its external dependencies, (2) a heartbeat/dead-man's-switch that alerts on ABSENCE of a success ping, and (3) fail-loud logging of any degradation/substitution. Extends, does not replace, the prior out-of-band-vantage recommendation.

  Search scope: API deprecation, dependency/config drift, graceful-degradation and fallback-model patterns in agentic/scheduled systems. Comprehensive.

  Recommendation: CHALLENGED
