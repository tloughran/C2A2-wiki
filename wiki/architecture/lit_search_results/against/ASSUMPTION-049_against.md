SEARCH-AGAINST-ASSUMPTION-049:
  Date searched: 2026-04-20
  Original item: ASSUMPTION-049
  Original statement: "Session lifetime = one full tradition agent run (all pending proposals for that tradition); NOT one session per proposal"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-049
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Execution Protocol v1.0 architectural commitment
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Long-context degradation literature (Liu et al. 2023 "Lost in the Middle"; Anthropic context-length evaluations 2024-2025): model performance degrades on tasks buried mid-context; long sessions with many proposals may see later-proposal-quality regression if earlier proposals dominate the context.
    2. Cross-proposal pollution risk (prompt-engineering folklore 2023-2026; studies on few-shot ordering effects): earlier in-context outputs bias later ones; reasoning about proposal N+1 may be contaminated by reasoning produced for proposal N, particularly if the N outputs share surface features.
    3. Parallelism-forfeit argument (distributed-systems practice; Fowler 2018 on pipeline design): per-proposal sessions can be run in parallel, trading cache-hit for latency. Per-agent-run sessions serialize proposals within one tradition — a throughput penalty.
    4. Checkpointing and recovery (resilience engineering; Nygard 2007 "Release It!"): longer sessions have larger blast-radius on failure — if a 20-proposal session crashes at proposal 15, you've lost 14 proposals of work. Per-proposal sessions localize failure.
    5. Context-budget ceiling (Anthropic / OpenAI model limits 2024-2026): 200K-1M tokens per session; if prefix + N proposals × per-proposal-context grows past the ceiling, per-agent-run topology forces truncation or session-split mid-run.

  Strength of challenge: Moderate

  Summary: Per-agent-run topology is the dominant pattern but carries real tradeoffs the assumption does not acknowledge. Long-context degradation, cross-proposal pollution, parallelism forfeit, and failure blast-radius are all documented concerns. The assumption is SUPPORTED for short-to-medium queue depths (N ≤ 10 proposals), but at higher N the economics flip. Literature would recommend a HYBRID — cap session length at a configurable number of proposals, spill to a new session when the cap is hit — rather than a pure one-session-per-agent-run policy.

  Specific risks: (a) Quality regression on late proposals in long queues (Lost-in-the-Middle effect); (b) cross-proposal reasoning pollution; (c) blast-radius on mid-session failure; (d) context-window saturation at ambitious queue depths.

  Mitigations available: (a) Configurable session-length cap (e.g., max 10 proposals per session); (b) periodic summarization to compress in-session context; (c) spill-to-next-session protocol; (d) proposal-ordering policy (diverse proposals first to reduce pollution).

  Recommendation: PARTIALLY-CHALLENGED (the commitment is defensible as a default but should include a ceiling/spill policy; the literature would recommend a hybrid rather than an absolute commitment)

  STEELMAN:
    Item: ASSUMPTION-049
    Strongest counterargument: While per-agent-run sessions maximize cache reuse on small queues, they expose the system to context-quality degradation, cross-proposal reasoning pollution, larger failure blast-radius, and context-window ceiling violations as queue depth grows. The literature consistently recommends HYBRID topologies — cache-friendly within a bounded session, spill to a new session when a cap is hit. An absolute one-session-per-agent-run commitment forfeits a well-documented safety margin for a small additional cache benefit.
    What would need to be true for C2A2 to be safe: Queue depths empirically stay low (typically N ≤ 10 per tradition per run); OR a spill-policy exists for long queues; OR periodic in-session summarization is implemented to contain context growth.
    How to test: Measure per-proposal quality as a function of position within session across the first 4 weeks of v1.0 deployment; regression at position > N signals the ceiling.
