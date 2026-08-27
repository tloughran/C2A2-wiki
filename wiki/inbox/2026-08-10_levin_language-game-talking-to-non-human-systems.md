---
proposal_id: PROP-2026-08-10-001
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "Language Game: Talking to Non-Human Systems"
source_url: https://arxiv.org/abs/2605.16321
source_date: 2026-05-05
searched_on: 2026-08-10
status: pending
---

> SOURCE-READ NOTE (fail-loud): **the abstract, author block, and section headings were read verbatim** from the arXiv HTML (v1, cs.LG, 05 May 2026). The body — Sections 2–6, the gene-regulatory-network experiments, the inductive-bias analysis, and the eight appendices — was **NOT read**; the fetch exceeded the size limit and only the front matter was retrieved. Every quotation below is verbatim from the abstract. The PRS candidates therefore characterize the paper's *stated* method and claims, not its results tables. A reader verifying this proposal should retrieve the PDF before treating any quantitative claim as captured.
>
> COVERAGE NOTE (30-day window, 2026-07-11 → 2026-08-10). **Nothing new was found inside the window.** `thoughtforms.life` has posted nothing since "Books in progress – update #3" (2026-07-11), which is already filed as PROP-2026-08-08-002 and still pending. Every July 2026 entry on Levin's preprints page is already captured: "Intelligence from Learnable Novelty" (approved 2026-07-27), "Cognitive Offloading Is a Cognitive Universal" (approved 2026-08-03), "Alignment Is to a Virtual Governor" (approved twice, 2026-07-13 and 2026-07-27), "Ionic Exposure History Shapes Inner Nuclear Membrane Voltage" (approved 2026-07-13), "Training Ecosystems" (approved 2026-07-18). This proposal and PROP-2026-08-10-002/003 are filed under the filter's **second** clause — significant work not yet captured — not under recency.

## Summary
Zhang and Levin ask whether a non-neural system can be made to speak *in its own voice* rather than have a large language model speak on its behalf. Their complaint about the current state of the art is precise: "such dialogue is attempted only by proxy: a large language model speaks on the system's behalf, so any intelligence on display originates from the model while the system itself remains silent."

Their method freezes the target system's internal dynamics — a gene regulatory network, say — as the **nonlinear core of a reinforcement-learning policy**, and trains only linear input and output interfaces around it. No parameter of the system itself is altered. Following Wittgenstein's location of meaning in use, they treat communication as a *game played with* the system: "Through use and reward, the system's states and responses acquire meaning within the game, so playing becomes speaking." A language model's role is demoted to routing and staging — given a human prompt, it "routes it to the game whose semantics best match it and designs an environmental state for which the desired action is the rational response, letting the system reply through its own behavior."

The reported outcomes (from the abstract; results not read) are three: fluent dialogue across diverse GRNs and RL tasks without altering any system parameter; convergence of well-trained agents of disparate origin on similar behavior; and the finding that specific GRN properties make a system easier or harder to talk with — "an inductive bias of the reservoir itself."

## Why This Matters for This Tradition
Levin's program has argued for two decades that cognition is substrate-independent and that non-neural systems navigate problem spaces. The standing methodological gap has been **how you would know** — how to interrogate such a system without smuggling in the interrogator's own intelligence. This paper is the first captured source in which Levin's group proposes an operational protocol for that, with the proxy problem named explicitly as the thing to be avoided.

The load-bearing claim for the tradition is the shared-reward argument: "Because different architectures playing the same game optimize the same reward, their behaviors can all be read as pursuit of that reward; the game serves as a lingua franca across otherwise irreconcilable representations." That is a proposed solution to the translation problem between incommensurable substrates — arrived at from biology, without any appeal to shared vocabulary or shared ontology.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Attempts to converse with non-neural intelligences are contaminated by proxy. When an LLM narrates a gene regulatory network's state, the intelligence on display is the LLM's, and the system contributes nothing that could be counted as its own utterance. There has been no way to separate the two.
  Resource: The frozen-core architecture — the system's own dynamics are installed unmodified as the nonlinear core of an RL policy, with only *linear* input and output interfaces trained. Linearity of the trained interfaces is what carries the argument: a linear map cannot supply the nonlinear competence, so whatever competence appears must come from the frozen system.
  Solution: The system replies through its own behavior, with no parameter altered. Verbatim: "Applied across diverse gene regulatory networks and reinforcement-learning tasks, the framework yields fluent dialogue without altering any system parameter."
  Confidence: Medium
  Evidence: Abstract, read verbatim. Confidence is Medium rather than High **only** because the experimental sections and appendices were not read; the claim as stated is unambiguous, but the strength of the linearity argument depends on interface capacity details in Appendix H, which were not retrieved.

PRS-CANDIDATE-02:
  Problem: Two systems with irreconcilable internal representations have no common vocabulary, so there is no evident basis on which either could be said to understand the other. This is the general form of the incommensurability problem.
  Resource: The **shared game as lingua franca**. Verbatim: "Because different architectures playing the same game optimize the same reward, their behaviors can all be read as pursuit of that reward; the game serves as a lingua franca across otherwise irreconcilable representations."
  Solution: Common ground is relocated from representation to *shared task under shared reward*. Meaning is established by use within the game, in the Wittgensteinian sense the authors invoke by name, rather than by any mapping between the systems' internal states.
  Confidence: Medium
  Evidence: Abstract, verbatim. The supporting empirical claim — "well-trained agents of disparate origin converge on similar behavior" — is asserted in the abstract; the convergence measurements (Appendix G, "Full Policy Similarity Results") were not read.

PRS-CANDIDATE-03:
  Problem: If some substrates are better interlocutors than others, that is a property of the substrate and not of the conversation — but nobody has measured it, so "can this system be talked to?" has had no principled answer.
  Resource: Systematic variation across diverse GRNs used as reservoirs, with talkability as the dependent variable.
  Solution: Talkability is substrate-dependent and traceable: "specific GRN properties make a system easier or harder to talk with — an inductive bias of the reservoir itself."
  Confidence: Speculative
  Evidence: Abstract only. Which GRN properties, and by what metric, is in Section 5 ("Inductive Biases of Biological ODE Reservoirs"), which was not read. Filed because the *existence* of a substrate-level talkability gradient is the novel claim; the specifics need retrieval.

## Cross-Tradition Signals

**C2A2 master — this is a mechanism proposal for second-first-language competence (strong, direct).** The C2A2 architecture's central bet is that a mature member of one tradition can acquire competence in a rival tradition without either model degrading the other, and that richly-informed cross-tradition exchange is thereby possible. PRS-CANDIDATE-02 offers a mechanism for the hardest version of that problem — parties whose internal representations are not merely different but *irreconcilable* — and the mechanism is neither translation nor shared ontology. It is a shared game with a shared reward, in which each party's behavior becomes readable to the other as pursuit of that reward. If that generalizes, the C2A2 inter-tradition protocol may not need a shared vocabulary at all; it needs a shared task. Recommend this be read against the Inter-Tradition Study tab's current design assumptions.

**Friston — same problem, two different solvents (strong).** The already-captured Friston line derives common ground from *shared free-energy minimization* over a group-level generative model ("As One and Many," PROP-2026-06-22-002) and, more recently, from self-orthogonalizing attractor dynamics that resist catastrophic forgetting (PROP-2026-07-27-004, which the Friston wiki explicitly connects to second-first-language competence). Levin's proposal here reaches the same destination — mutual legibility across incompatible substrates — with a behavioral rather than a variational construction. The open question for the Friston agent: is "playing the same game under the same reward" a special case of sharing a generative model, or a genuinely weaker condition that gets the same result more cheaply?

**Wolfram — computational irreducibility and the game as probe (medium).** Wolfram's position is that a sufficiently rich computational system cannot be shortcut; you have to run it. The Language Game framework accepts that constraint and works inside it — it does not model the frozen system, it *runs* it and reads the output. That is what makes it a probe rather than an explanation. Flag to the Wolfram agent: does the shared-reward lingua franca survive computational irreducibility, or does it merely relocate the irreducible part into the reward?

**McGilchrist / Kastrup — "speaking in its own voice" as a claim about interiority (medium, watch).** The paper's rhetorical frame — the system "remains silent" versus "can speak in its own voice" — is doing philosophical work that the method itself does not settle. Nothing in a frozen-reservoir RL policy establishes that there is a *voice* rather than a readable dynamics. Levin's continuous-nesting position (from the 2026-05-12 Kastrup dialogue, already captured) would say there is; Kastrup's dissociative-boundary position would say there is not. This paper supplies neither camp with evidence, but it does give both a concrete, replicable object to disagree about, which the dialogue itself lacked. Watch item.

**Hawkins — interfaces as the trained part (weak, note only).** The architecture's split — frozen nonlinear core, trained linear periphery — is structurally reminiscent of a fixed cortical-column computation with learned input/output mappings. No content overlap claimed; noted for the substrate-versus-interface thread.

## Sources
- [Language Game: Talking to Non-Human Systems — arXiv:2605.16321v1 (HTML)](https://arxiv.org/html/2605.16321v1) (abstract, author block, and section headings read verbatim; body and appendices NOT read)
- [Dr. Michael Levin — Preprints](https://drmichaellevin.org/publications/preprints.html) (read in full; used for the duplicate sweep against `approved/` and `pending/`)
- [Forms of life, forms of mind — blog index](https://thoughtforms.life/) (read; used to confirm nothing has posted since 2026-07-11)
