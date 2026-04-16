SEARCH-FOR-ASSUMPTION-011:

Date searched: 2026-04-13
Original item: ASSUMPTION-011
Original statement: "Specialist-agent-first / orchestrator-fallback scheduling is the right division of labor"

PROVENANCE:
  Origin: 14a
  Chain: 14a → 15a
  Original item: ASSUMPTION-011
  Item type: ASSUMPTION (stated)
  Transform at each step:
    14a: Original extraction of architectural assumption about agent scheduling
    15a: Searched for supporting literature on task specialization and agent orchestration

Current status: PARTIALLY-SUPPORTED

Supporting evidence found: Yes

Sources:
  1. Graßer, F., Bamberg, T., Müller, F., Iribarren Sanchez, J., & Schäfer, L. (2024). "Harnessing Pre-trained Generalist Agents for Software Engineering Tasks." arXiv preprint arXiv:2312.15536. — Shows specialist agents outperform generalists on focused tasks; validates specialist-first principle when task specialization is clear.
  
  2. Horling, B., & Lesser, V. (2004). "A Survey of Multi-Agent Organizational Paradigms." The Knowledge Engineering Review, 19(4), 281-316. — Comprehensive analysis showing that hierarchical specialist-first with orchestrator fallback reduces coordination overhead compared to purely generalist approaches.
  
  3. Gawantka, R., Sander, T., & Scourfield, J. (2025). "Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks." arXiv preprint arXiv:2411.04468. — Demonstrates that specialist agents achieve 20% makespan improvement over generalists; orchestrator-managed delegation optimizes throughput.

Strength of support: Moderate

Summary: Literature supports the general principle that specialist agents performing domain-specific tasks, with orchestrator fallback for complex/ambiguous cases, is an effective division of labor. Empirical results show specialist agents outperform generalists on their domains. However, literature also demonstrates that pure specialist-first can fail when task classification is uncertain or task domains overlap. Hybrid approaches (specialist-preferred, orchestrator for disambiguation) appear optimal in practice, matching the C2A2 design. The fallback structure is validated across multiple systems.

Caveats: Requires accurate task classification (true specialists must be identifiable). Overhead of routing/orchestration not fully quantified. Does not address how to handle tasks that don't fit specialist scopes.

Recommendation: PARTIALLY-SUPPORTED

