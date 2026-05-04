SEARCH-FOR-ASSUMPTION-032:
  Date searched: 2026-04-16
  Original item: ASSUMPTION-032
  Original statement: "Computer-use pixel-level inspection is a sufficient substitute for Chrome MCP during native-app debugging"
  
  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-032
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session — tool-degradation compensation pattern
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  
  Sources:
    1. Yang et al. (2024). "SeeAct: Agents That See and Act on the Web." — Visual (screenshot) agents can complete many tasks DOM-based agents can; though with lower reliability.
    2. Chen et al. (2024). "SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents." — Pixel-level grounding achieves non-trivial task completion in general GUI automation.
    3. Anthropic Computer Use technical report (2024-2025). — Visual-based control can substitute for structured APIs at reduced reliability.
    4. Accessibility/software testing literature: screenshot-based black-box testing is a recognized fallback when DOM access is unavailable.
    
  Strength of support: Moderate (qualified)
  
  Summary: The visual-agent literature supports pixel-level inspection as a degraded but functional substitute when DOM/structured access is unavailable. It is sufficient for many debugging tasks, particularly visual layout problems and user-visible bugs. It is not a full substitute for Chrome MCP's DOM-aware tooling when the bug is in hidden state, event handling, or network behavior. The assumption should be read as "sufficient for some native-app debugging scenarios" rather than "fully equivalent."
  
  Caveats: Visual-only debugging has documented accuracy penalties (often cited at 20-40% in head-to-head GUI agent benchmarks). It is a fallback, not a peer.
  
  Recommendation: PARTIALLY-SUPPORTED
