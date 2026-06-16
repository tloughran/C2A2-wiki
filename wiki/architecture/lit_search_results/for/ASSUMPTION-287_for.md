SEARCH-FOR-ASSUMPTION-287:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-287
  Original statement: Observed telemetry should replace authored narration as the basis of the Agent Explorer.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-287
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated architectural assumption from 2026-06-08 OpenStory→Agent-Explorer build sessions (cycle 0, priority MEDIUM)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: SUPPORTED

  Supporting evidence found: Yes
  Sources:
    1. van der Aalst, W.M.P., 2016. "Process Mining: Data Science in Action." Springer (2nd ed.). — Foundational case that event logs reveal the real process, which is "usually not the same as" the documented/idealized one; the entire discipline rests on observed-trace as the truth-basis of a system representation.
    2. Carmona, J., van Dongen, B., Solti, A., Weidlich, M., 2018. "Conformance Checking: Relating Processes and Models." Springer. — Formalizes the observed-vs-modeled gap; conformance checking exists precisely because authored models drift from actual behavior.
    3. Jonathan, D., 2025. "Architecture Drift: Why Systems Fail Gradually Before They Fail Suddenly." Medium. — Practitioner articulation of documentation/design-layer drift: authored descriptions decay while behavioral telemetry stays current by construction.
    4. OpenTelemetry project docs, "Observability primer" (opentelemetry.io). — Industry-standard framing that telemetry signals (traces/logs/metrics) are the canonical way to understand what a system actually does.
  Strength of support: Strong
  Summary: The process-mining literature directly supports grounding a system representation in observed event data rather than authored description: documented models are repeatedly shown to be idealized and divergent from real execution, and discovery-from-logs is an established, validated methodology (van der Aalst 2016). Observability practice converges on the same premise — telemetry is the live, non-decaying record of system behavior, while authored documentation drifts. This supports telemetry as the *basis* of the Agent Explorer. The strict "replace" framing gets slightly less support: the same literature treats observed behavior and modeled intent as complementary (conformance checking needs both).
  Caveats: Literature supports observed-data primacy for fidelity, not full deletion of authored intent — traces show what happened, not what was meant or why; drift detection itself requires retaining an intent layer to compare against. Transfer assumes the telemetry capture is reasonably complete (see PRESUMPTION-322's question, searched separately).
  Search scope: 2 queries — "observability telemetry traces as system documentation vs authored documentation drift"; "process mining event logs actual process vs documented process model conformance". Plus established literature (van der Aalst; Carmona et al.).
  Recommendation: SUPPORTED
