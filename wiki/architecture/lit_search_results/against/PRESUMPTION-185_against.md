SEARCH-AGAINST-PRESUMPTION-185:
  Date searched: 2026-05-18
  Original item: PRESUMPTION-185
  Original statement: "Scope-lock + human-or-Claude review-step presumes Claude has bandwidth/trust to be reviewer; if Claude is bottleneck reviewer, Rule-5 offloading recursively re-imports Claude into the loop at review time."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-185
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Extracted/Surfaced from 2026-05-17 c2a2-self-awareness-daily run (resumed cycle)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Frontiers 'Fostering effective hybrid human-LLM reasoning' — review-bottleneck is a known failure mode when LLM is both worker and reviewer; recursive re-import is documented.
    2. ReDAct paper (arxiv 2604.07036) — uncertainty-aware deferral protocols precisely address the review-bottleneck question; default 'Claude reviews' is treated as unprincipled.
    3. Rule-5 (Tom's preference) — 'use the model for judgment calls, not for routing/retries/deterministic transforms.' Reviewing worker output is judgment; reviewing reviewer output is recursive; Rule 5 cautions against the chain.

  Strength of challenge: Moderate

  Summary: Naming Claude as reviewer without bandwidth/trust audit is the exact pattern Rule 5 cautions against (using the model where code or human judgment would do). The recursive re-import (offload to worker → review by Claude → review by another Claude?) is a documented LLM-architecture anti-pattern.

  Specific risks: (a) Bottleneck under worker output volume; (b) Claude-reviewing-Claude recursion creates closed loop where errors compound; (c) trust ceiling — Claude's review may not catch failures that the original Claude-worker also misses.

  Mitigations available: (a) Human-in-the-loop for high-stakes reviews; (b) explicit review-criterion that doesn't require Claude-internals; (c) bound the recursion depth (review by different Claude with different prompt counts as separate).

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-185
    Strongest counterargument: The strongest case: Rule 5 explicitly cautions against using the model for routing/retries/deterministic transforms. Review is a borderline case (judgment, yes — but also routing-of-rejection-decisions). Defaulting to Claude as reviewer without examining whether the review-task is genuinely judgment-bound is a Rule-5 violation by omission.

