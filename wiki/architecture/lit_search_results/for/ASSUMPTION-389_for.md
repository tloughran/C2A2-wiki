SEARCH-FOR-ASSUMPTION-389:
  Date searched: 2026-06-30
  Original item: ASSUMPTION-389
  Original statement: "PRS-triplet / cross-program extraction is quality-sensitive and gated to attended sessions by standing policy — the unattended daily orchestrator deliberately defers backlog extraction."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-389
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-06-29 self-awareness cohort (metabolism-axis / liveness / push-pattern review)
      15a: Searched for supporting literature (first-time, genuine web search 2026-06-30)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Hyperscience, "Human-in-the-Loop ML vs. Attended Automation" — gating quality-sensitive extraction to human-attended sessions is a recognized pattern when error cost is high and judgment is required.
    2. Comet (2024), "Human-in-the-Loop Review Workflows for LLM Applications & Agents" — deferring low-confidence / high-stakes extraction to human review is standard; "the cost of AI errors often exceeds the cost of oversight."
    3. Docsumo, "Human-in-the-Loop Systems: Design for Real-World Accuracy" — quality-sensitive extraction pipelines routinely hold back outputs for attended validation.

  Strength of support: Moderate

  Summary: Gating quality-sensitive extraction to attended sessions is a well-supported HITL design when the cost of a bad extraction is high and the task needs human judgment. The standing policy is defensible: it trades throughput for quality on exactly the axis (PRS/cross-program extraction) where errors are expensive to unwind.

  Caveats: Support is for SELECTIVE gating (route only the ambiguous/high-stakes items), not necessarily for blanket deferral of the entire backlog; see 15b.

  Recommendation: SUPPORTED (Moderate — HITL gating of quality-sensitive extraction is sound practice)
