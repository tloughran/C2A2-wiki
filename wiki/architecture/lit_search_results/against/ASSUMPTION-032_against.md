SEARCH-AGAINST-ASSUMPTION-032:
  Date searched: 2026-04-16
  Original item: ASSUMPTION-032
  Original statement: "Computer-use pixel-level inspection is a sufficient substitute for Chrome MCP during native-app debugging"
  
  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-032
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session — tool-degradation compensation
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes
  
  Sources:
    1. WebArena / VisualWebArena benchmarks (Zhou et al., 2023-2024): visual agents consistently underperform DOM-based agents by 20-40% on identical tasks.
    2. AgentBench / WebShop literature: structured-API access yields substantially higher task completion than visual-only.
    3. Accessibility testing literature: screenshot-based testing misses hidden state, event bindings, and semantic structure.
    4. SeeAct / SeeClick technical reports: pixel-level grounding is effective for simple visible actions but degrades on complex interactions.
    
  Strength of challenge: Moderate-Strong
  
  Summary: The challenging evidence shows pixel-level inspection is reliably lower-performance than DOM-aware tooling for web apps. For native-app debugging specifically, the tooling comparison is less direct — but the underlying limitation (no access to hidden state, event bindings, or DOM-like structure) is universal. "Sufficient substitute" is too strong a framing; "degraded fallback for some scenarios" is better supported. The assumption is defensible as an emergency-mode claim, not as a peer-substitute claim.
  
  Specific risks: Debugging time inflation; missed root causes for bugs in non-visible state; false confidence in "no bug found" when visual inspection missed structural issues.
  
  Mitigations available: Fall back to Chrome MCP when possible; combine visual + log/console access; document tool-limitation explicitly in debug sessions.
  
  Recommendation: PARTIALLY-CHALLENGED
  
  STEELMAN:
    Item: ASSUMPTION-032
    Strongest counterargument: GUI-agent benchmarks consistently show 20-40% performance degradation for visual-only agents versus DOM-aware agents. "Sufficient substitute" overstates what the literature supports; "degraded fallback" is the accurate framing. Using pixel inspection as a peer substitute risks missing bugs that require structural visibility.
    What would need to be true for C2A2 to be safe: Explicit acknowledgment that pixel-inspection is a fallback with measurable accuracy penalty; preference for Chrome MCP or dedicated MCPs when available.
    How to test: Log diagnoses where pixel-only was used; compare to ground-truth root causes; measure miss rate.
