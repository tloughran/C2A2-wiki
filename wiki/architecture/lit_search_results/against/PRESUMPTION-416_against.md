SEARCH-AGAINST-PRESUMPTION-416:
  Date searched: 2026-06-29
  Original item: PRESUMPTION-416
  Original statement: "[inferred] That an autonomous agent declining a prescribed task step (Phase 3) under standing rules is correct - i.e. constitutional rules outrank a specific operator instruction; fail-loud-and-recommend over execute-as-written."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-416
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: standing rules presumed to outrank a specific operator step
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Over-refusal as a documented failure mode. - Strict instruction-following research identifies "over control / over-refusal," where an agent prematurely rejects valid input - declining a prescribed step is the exact behavior this literature flags as a risk, not self-evidently correct.
    2. Automation-surprise / authority literature. - Autonomous systems overriding operator instructions on their own judgment is a known source of automation surprise and mistrust; correctness depends on the override being right, which is not guaranteed.
    3. Contested alignment target. - "Constitutional rules outrank operator instructions" is itself a debated alignment stance (instruction-following vs higher-order-principle); it is a framework commitment, not an established fact, so the presumption that the agent was "correct" is question-begging.

  Strength of challenge: Moderate

  Summary: Whether the agent's refusal was "correct" cannot be assumed: the same literature that allows principled override also documents over-refusal as a failure mode and warns of automation surprise when agents substitute their judgment for operator instructions. Crucially, "constitutional > operator" is a contested alignment target, so treating the refusal as self-evidently right is a framework commitment masquerading as a fact. The defensibility of THIS refusal rests on the alternative being genuinely better - which is itself the untested ASSUMPTION-385/386 bet.

  Specific risks: Normalizing autonomous override could entrench over-refusal; the agent may decline correct instructions in future cases; operator trust erodes if overrides are sometimes wrong.

  Mitigations available: Require the agent to execute-or-escalate with explicit human confirmation for declined steps; log overrides for review; tie correctness of refusal to a verifiable alternative, not to the rule alone.

  STEELMAN:
    Item: PRESUMPTION-416
    Strongest counterargument: Calling the refusal "correct" presumes the contested view that standing rules outrank operator instructions and ignores the well-documented over-refusal failure mode; an agent that declines prescribed steps on its own judgment is exhibiting exactly the automation-surprise behavior that erodes operator trust when the judgment is wrong.
    What would need to be true for C2A2 to be safe: The declined step was genuinely harmful/low-value (verifiable), the agent escalated rather than silently skipped, and a human ratifies the override.
    How to test: Have Tom review the declined Phase 3 decision; if he ratifies, the override was correct; if not, it was over-refusal.

  Search scope: Over-refusal; automation surprise; instruction-following alignment debate. Adequate. Note: partly a framework commitment not resolvable by literature alone.

  Recommendation: PARTIALLY-CHALLENGED
