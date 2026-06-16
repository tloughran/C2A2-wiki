SEARCH-AGAINST-PRESUMPTION-322:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-322
  Original statement: The event stream is a faithful proxy for what an agent is and does (telemetry captures agent substance).

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-322
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference from 2026-06-08 build sessions (telemetry treated as agent substance without argument)
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Kaplan, A., 1964 (popularized as the "streetlight effect"; see thecoder.cafe/psychsafety syntheses, 2024-25). — Observation concentrates where instrumentation already shines; green dashboards measure the lit area, not the system. What an agent's event stream omits (reasoning quality, fitness-for-purpose of outputs, harm avoided) is structurally invisible.
    2. Naur, P., 1985. "Programming as Theory Building." — The substance of an intelligent process (its theory: why, what-maps-to-what) transcends all written artifacts; an event log is the most reduced artifact of all. Identity cannot be reconstructed from execution records.
    3. Sen, A., 1973. "Behaviour and the Concept of Preference." Economica 40. — Canonical critique of revealed preference: choice/behavior data underdetermines the values and intentions behind it; inferring "what the agent is" from "what it did" repeats a known fallacy.
    4. Muller, J., 2018. "The Tyranny of Metrics." Princeton UP. — Quantitative process records systematically misrepresent qualitative work; the most measurable aspects of work are rarely the most important, and the substitution happens silently.
  Strength of challenge: Strong
  Summary: This is the load-bearing presumption beneath ASSUMPTION-287, and the literature against it is old, broad, and convergent. Event streams record tool invocations and turn structure — the mechanical exhaust of agent work — while everything that distinguishes a good agent from a busy one (judgment, restraint, output quality, alignment with purpose) leaves either no events or indistinguishable events. An agent that wisely does nothing and a dead agent emit the same stream. Revealed-preference critiques and the streetlight effect both name the same failure: treating the observable as the substance because it is observable. Telemetry is a faithful proxy for *activity*; the presumption silently extends it to *substance*, and that extension is where every cited tradition objects.
  Specific risks: The Agent Explorer becomes an activity monitor mistaken for an agent ontology; quiet-but-valuable agents read as negligible, noisy-but-thrashing agents read as substantial; later C2A2 layers inherit the conflation as ground truth.
  Mitigations available: Explicitly label the explorer as a behavioral/activity view; join event data with output artifacts (what the agent produced, not just that it acted); include human/eval quality annotations as a separate channel; surface "not captured here" as a visible disclaimer per agent.
  STEELMAN:
    Strongest counterargument: For software agents — unlike humans — there is no inner life beyond the I/O: the prompt, the events, and the outputs *are* the agent's entire causal footprint, so a complete event stream is far closer to substance than human telemetry ever is. The alternative (authored self-description) is strictly less reliable. Faithful-enough is the right bar for a v1 explorer.
    What would need to be true for C2A2 to be safe: Event capture is genuinely complete (no capture gap — currently false); outputs and prompts are included in "the stream," not just tool events; consumers of the explorer treat it as behavior, not identity.
    How to test: Take 3 agents; have a blinded human characterize each from event stream alone, then from event stream + outputs + prompt; measure how often the stream-only characterization is materially wrong about what the agent is for or how well it works.
  Search scope: 1 search — "streetlight effect observability metrics what dashboards miss activity vs outcomes". Plus established literature (Naur, Sen, Muller).
  Recommendation: CHALLENGED
