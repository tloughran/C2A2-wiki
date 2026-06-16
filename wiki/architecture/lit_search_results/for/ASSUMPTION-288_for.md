SEARCH-FOR-ASSUMPTION-288:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-288
  Original statement: Routing extraction through OpenStory's DB (vs direct transcripts) is worth the heavier dependency because eval/apply + turns are valuable signal.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-288
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated architectural assumption from 2026-06-08 OpenStory→Agent-Explorer build sessions (cycle 0, priority MEDIUM)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. "Beyond the Final Answer: Evaluating the Reasoning Trajectories of Tool-Augmented Agents" (TRACE), 2025. arXiv:2510.02837. — Argues outcome-only evaluation is insufficient; step/trajectory-level signals (the kind a structured DB like OpenStory's pre-derives) carry the real quality information.
    2. STEVE: "A Step Verification Pipeline for Computer-use Agent Training," 2025. arXiv:2503.12532. — Empirical precedent that per-action/step-level derived metrics over agent trajectories are valuable, supporting the worth of richer structured signal vs raw transcripts.
    3. Confident AI / LangChain agent-evaluation guides, 2025-2026 ("LLM Agent Evaluation Metrics: Tool Calling, Trace-Based Evals"; "Trajectories vs. Outputs"). — Industry consensus that trace-structured data (turns, tool calls, eval steps) is the unit of agent evaluation, implying value in a pipeline that already structures it.
    4. OpenTelemetry, "What is OpenTelemetry?" (opentelemetry.io). — Reuse-over-rebuild rationale for instrumentation pipelines: standardized, already-built telemetry layers are preferred to bespoke extraction.
  Strength of support: Moderate
  Summary: The agent-evaluation literature strongly supports half of the claim: turn/step/trajectory-level signals (of which eval/apply is an instance) are widely held to be more informative than outcomes or raw text, so a source that pre-derives them is genuinely valuable. The reuse-vs-rebuild side has practitioner support (reusing an existing instrumentation pipeline beats re-deriving from raw transcripts). What the literature does not settle is the specific trade — whether that signal value outweighs the coupling cost of a heavier third-party DB dependency; no source quantifies that balance, and dependency-cost literature (lock-in, schema coupling) cuts the other way.
  Caveats: Support is for the value of trajectory-structured signal generally, not for OpenStory's eval/apply field specifically (its semantics are inherited and unvalidated — see PRESUMPTION-323). The dependency-cost half of the claim is asserted, not evidenced, in the literature found.
  Search scope: 1 query — "LLM agent self-verification evaluation actions ratio quality signal agent trajectory metrics tool-use evaluation". Plus established instrumentation-reuse literature. Preliminary search — broader search on dependency/coupling cost recommended.
  Recommendation: PARTIALLY-SUPPORTED
