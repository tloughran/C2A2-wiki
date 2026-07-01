SEARCH-FOR-PRESUMPTION-416:
  Date searched: 2026-06-29
  Original item: PRESUMPTION-416
  Original statement: "[inferred] That an autonomous agent declining a prescribed task step (Phase 3) under standing rules is correct - i.e. constitutional rules outrank a specific operator instruction; fail-loud-and-recommend over execute-as-written."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-416
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: agent treated standing constitutional rules as outranking a specific operator step
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Constitutional-AI / standing-principle alignment literature. - Agents governed by higher-order standing principles that can override specific instructions are an accepted design pattern; principle-over-instruction is a recognized alignment posture.
    2. Instruction-following agent research (revise-over-refuse). - It is documented that an agent revising a suboptimal directive to satisfy higher-level constraints is often preferable to blind compliance, supporting "fail-loud-and-recommend" over "execute-as-written."
    3. Over-refusal vs unsafe-compliance framing. - The literature recognizes a legitimate middle path where an agent declines/escalates rather than executing an instruction that conflicts with its constraints.

  Strength of support: Moderate

  Summary: The pattern of standing/constitutional rules taking precedence over a specific operator instruction, with the agent escalating a recommendation rather than executing blindly, is well-precedented in alignment and agent-design literature. Crucially, the literature favors "revise-and-recommend" (which the agent did - it proposed a bounded alternative) over silent refusal. This supports the correctness of the agent's posture in THIS instance. It does not establish that constitutional override is universally correct - that is a contested framework commitment.

  Caveats: Support is conditional on the agent surfacing its refusal loudly and offering an alternative (which it did). The general claim "constitutional rules outrank operator instructions" is partly a framework choice the literature cannot fully settle (see 15b on over-refusal/automation-surprise).

  Search scope: Constitutional AI; instruction-following vs goal-directed; revise-vs-refuse. Adequate.

  Recommendation: PARTIALLY-SUPPORTED
