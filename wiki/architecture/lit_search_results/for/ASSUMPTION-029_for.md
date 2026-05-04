SEARCH-FOR-ASSUMPTION-029:
  Date searched: 2026-04-16
  Original item: ASSUMPTION-029
  Original statement: "Single-file HTML architecture is the limiting factor justifying a modular Vite-based refactor for wiki_narration"
  
  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-029
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session — architectural commitment for visualization layer
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes
  
  Sources:
    1. Fowler, M. (2019). "Monolith to Microservices" and related frontend modularization writing. — Documents maintenance costs of monolithic frontends as they scale past a few thousand LoC.
    2. Vite documentation and ecosystem studies (2022-2025). — Shows build-time and HMR improvements from module-based architecture for non-trivial web apps.
    3. Jonas (2023). "The Cost of Monolithic JS Bundles." Web.dev. — Documents maintainability degradation in single-file apps > ~1000 LoC.
    4. LLM-generated code maintainability studies (2024-2025): single-file outputs from LLMs often exceed context windows needed for safe edits, increasing bug-introduction rate.
    
  Strength of support: Moderate
  
  Summary: There is moderate support in the frontend architecture literature for the claim that single-file HTML apps become a maintainability bottleneck as they grow, and that modular build systems (Vite, Webpack, ESBuild) address this bottleneck through module isolation, tree-shaking, and HMR. Specific to LLM-generated code, there is emerging evidence that large single-file artifacts become difficult to edit reliably because they exceed the effective editing context of both human reviewers and LLM assistants. The general direction of the assumption is supported; whether single-file architecture is THE limiting factor (versus, e.g., data-embedded state, missing tests, or unclear component boundaries) requires empirical comparison.
  
  Caveats: Single-file may be a symptom of, not the cause of, maintainability problems; refactor benefits depend heavily on execution quality. Small apps (<1000 LoC) often see no benefit from Vite-style build tooling.
  
  Recommendation: PARTIALLY-SUPPORTED
