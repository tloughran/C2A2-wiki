---
prop_id: PROP-2026-08-31-002
proposal_id: PROP-2026-08-31-002
thinker: Karl Friston
tradition_key: friston
source_type: paper
source_title: "Life-inspired interoceptive artificial intelligence for autonomous and adaptive agents"
source_url: https://www.nature.com/articles/s42256-026-01296-8
source_date: 2026-08-26
searched_on: 2026-08-31
status: pending
---

## Summary
Lee, Oh, An, Yoon, Friston, Hong and Woo argue that the missing ingredient in autonomous AI is interoception — an agent's monitoring and regulation of its own internal state. Their claim is that current agents have no internal environment to speak of: reward arrives from outside, so the agent has no standing needs of its own and therefore no basis for choosing goals rather than being handed them.

The proposed remedy is architectural. Factorize the state variables explicitly into internal and external, then give the internal-state dynamics mathematical properties borrowed from living systems (bounded viability, homeostatic regulation). Once that factorization exists, internal states can serve a second function the authors treat as the more important one: they become a universally available, intrinsically valuable *context* — a stable reference signal that modulates learning and behaviour when the external environment shifts. Neuromodulatory mechanisms are proposed as the biological template for that modulation. The paper is a Perspective, not an empirical result; it synthesizes cybernetics, theories of life, reinforcement learning and neuroscience into a design programme.

Published 26 August 2026 in *Nature Machine Intelligence*; accepted 29 July 2026. The arXiv precursor (arXiv:2309.05999) dates to 2023, so the journal version is the citable form of a long-developing argument.

## Why This Matters for This Tradition
This is the FEP's internal/external partition — the Markov blanket — proposed as an explicit engineering requirement rather than a descriptive formalism. Friston's framework has always held that a system's boundary is what makes it an agent; here that claim is turned into a build specification for artificial agents, with a testable consequence (agents so factorized should adapt where flatly-specified agents fail). It also connects FEP to the goal-selection problem, which the tradition has historically addressed through prior preferences without saying where preferences come from. Interoception supplies a candidate answer: they come from the internal state's viability bounds.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Artificial agents pursue goals given to them from outside and cannot select goals of their own, because they have no internal environment whose condition could ground a need.
  Resource: Explicit factorization of state variables into internal-environment and external-environment representations, with internal-state dynamics given life-inspired mathematical properties (viability bounds, homeostatic regulation).
  Solution: Autonomy is recast as a structural property of the state space rather than a capability to be trained in — an agent with a regulated internal environment has needs, and needs generate goals without external specification.
  Confidence: Medium
  Evidence: The paper states that developing interoceptive AI "requires explicit factorization of state variables representing internal and external environments, together with mathematical formalization of life-inspired properties governing internal-state dynamics." It is presented as a Perspective's design claim, not a demonstrated result.

PRS-CANDIDATE-02:
  Problem: Agents degrade when the environment shifts away from training conditions, because every reference signal they hold is external and shifts with it.
  Resource: Internal states treated as "universally available and intrinsically valuable contexts" — reference signals that persist across external change — together with neuromodulatory mechanisms as the modulation channel.
  Solution: Adaptivity is grounded in a signal the environment cannot move. Learning and behaviour are modulated against the agent's own internal condition, giving a stable context under distribution shift.
  Confidence: Medium
  Evidence: "internal states can also function as universally available and intrinsically valuable contexts, serving as stable reference signals that modulate learning and behaviour under changing external environments."

## Cross-Tradition Signals
- **Levin — flag explicitly.** This is active inference specified at the level of internal-state regulation with no commitment to neurons, which is the substrate-independence claim Levin's programme makes from the biological side. Levin's bioelectric anatomical setpoints are, structurally, a regulated internal state carrying a reference signal. The question worth putting is whether the factorization this paper requires is already instantiated in non-neural tissue, or whether Levin's setpoints fail one of the life-inspired properties the authors specify. A negative answer is as useful as a positive one.
- **Hawkins**: the paper's neuromodulatory modulation channel is a claim about how context gates cortical learning. Hawkins' thousand-brains account has reference frames doing the contextualizing work. These are rival mechanisms for one job, not complementary ones — file as a live disagreement.
- **C2A2 / alignment relevance**: an agent that selects its own goals from its own viability needs is the strongest form of the alignment problem, and the paper proposes building exactly that. Worth routing to the master wiki as an alignment-relevant development: if goals are generated internally, alignment cannot be achieved by goal specification and must instead operate on the agent's viability bounds.
- **Fredrickson**: interoception as the ground of adaptive behaviour under changing conditions is adjacent to her account of affect as an internal signal that broadens or narrows behavioural repertoire. Speculative; do not record without checking whether the mathematical claims survive translation.
