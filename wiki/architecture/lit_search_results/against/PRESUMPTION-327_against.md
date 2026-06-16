SEARCH-AGAINST-PRESUMPTION-327:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-327
  Original statement: Making the agent swarm legible/comparable/rankable is itself benign or good (observability treated as normatively neutral).

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-327
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference (legibility project undertaken with no consideration that measurement is an intervention)
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Scott, J.C., 1998. "Seeing Like a State." Yale UP. — The canonical anti-thesis: legibility projects are never neutral; standardization/simplification for the viewer's convenience destroys local knowledge (mētis) and reshapes the system toward what the legibility scheme can see. High-modernist dashboards make things governable by making them simpler than they are.
    2. Espeland & Sauder, 2007. "Rankings and Reactivity: How Public Measures Recreate Social Worlds." AJS 113(1). — Empirical demonstration that rankings are interventions: once entities are ranked, resources, attention, and behavior reorganize around the ranking, regardless of the rankers' intent ("reactivity").
    3. Muller, J., 2018. "The Tyranny of Metrics." Princeton UP. — Metric fixation displaces judgment: what is rendered comparable gets managed, what resists comparison gets neglected; the harm operates through the measurer, not only the measured.
    4. Espeland & Stevens, 1998. "Commensuration as a Social Process." Annual Review of Sociology 24. — Making things comparable (commensuration) is itself a transformative act that discards the incommensurable qualities of the entities compared; comparability is a design decision with normative content, not a neutral lens.
  Strength of challenge: Moderate
  Summary: A deep and consistent literature holds that legibility, ranking, and commensuration are interventions with predictable side effects, not neutral observation. The strongest mechanism here is reactivity-through-the-operator: the agents themselves don't observe the dashboard, but their author does, and Espeland & Sauder's result is that the ranker's own attention and resource allocation reorganize around what the ranking shows — under-rendered agents (PRESUMPTION-326) get pruned, high-eval/apply agents (PRESUMPTION-323) get imitated, and the swarm evolves toward dashboard-favorable shapes. The challenge is moderate rather than strong because the classic harms (worker surveillance, destroyed mētis, gamed targets) assume measured parties with interests and an external power relation; a one-person reflective instrument over their own software agents is at the benign end of the spectrum — but C2A2 is explicitly a self-modifying architecture, which is precisely the loop where measurement effects compound.
  Specific risks: Agent population silently optimized toward legibility (simple, frequent, countable agents thrive; subtle or episodic ones get pruned); explorer-visible metrics become de facto fitness functions in later C2A2 self-modification cycles; incommensurable agent qualities exit the architecture's self-understanding entirely.
  Mitigations available: Record the normative choice explicitly (what the explorer makes visible/invisible) as an architecture note; resist ranked presentations (use unordered small multiples); periodic "what would this dashboard kill?" review; keep authored narration (per ASSUMPTION-287 mitigation) as the channel for the non-commensurable.
  STEELMAN:
    Strongest counterargument: Scott's harms require a state-scale power asymmetry over unconsenting subjects; here observer and owner are the same person, the "measured" are artifacts without interests, and the alternative — an illegible swarm — has its own documented failure mode (unaccountable automation, silent rot). Self-observability of one's own machines is closer to engineering hygiene than surveillance, and reflexive awareness of measurement effects (this very pipeline) is itself the mitigation.
    What would need to be true for C2A2 to be safe: Explorer metrics never become automated selection pressure without a deliberate decision step; the legibility scheme is revisable; non-rendered agent qualities have some other channel into design decisions.
    How to test: Longitudinal check — after N weeks of explorer use, audit agent create/modify/prune decisions for whether dashboard salience predicted them better than stated purpose did; that correlation measures the reactivity the presumption denies.
  Search scope: 1 search — ""seeing like a state" legibility critique dashboards quantification surveillance harms". Plus established literature (Espeland & Sauder, Muller, Espeland & Stevens).
  Recommendation: PARTIALLY-CHALLENGED
