SEARCH-AGAINST-ASSUMPTION-021:
  Date searched: 2026-08-11
  Original item: ASSUMPTION-021
  Original statement: "Cross-tradition signals linking Thousand Brains / Monty to active inference and to cellular cognition are structural, not surface."
  Cycle: 5 (RE-TRIGGER by 15d, queued 2026-07-05; processed 2026-08-11)

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 5)
    Original item: ASSUMPTION-021
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from Hawkins/Hoffman specialist agent session 2026-04-14
      15b (cycle 1, 2026-04): initial challenging search — TBT unresolved problems, active inference limitations, Gentner/Markman surface-vs-structure, Hawkins overstatement history
      15d: re-triggered for cycle 5 monitoring
      15b (cycle 5, 2026-08-11): re-searched for challenging literature; checked for new sources since April 2026
    Current status: CHALLENGED

  Search scope: Comprehensive on Thousand Brains / Monty primary and critical literature, and on active inference implementation limits. Preliminary on the Monty↔cellular-cognition link specifically — almost nothing exists connecting thousand-brains architectures to basal/cellular cognition, and the absence should be read through the challenged status of ASSUMPTION-019.

  Challenging evidence found: Yes

  Sources:
    1. Thousand Brains Project team. "Thousand-Brains Systems: Sensorimotor Intelligence for Rapid, Robust Learning and Inference." arXiv:2507.04494. — The project's own 2025 paper states of the theory's claimed advantages that "these performance characteristics had not been quantified" prior to that work. The framework's empirical status is still being established by its authors; a structural mapping onto it inherits that indeterminacy. One cannot establish a structural correspondence with a target whose own structure-relevant properties are unquantified.
    2. Clay et al. (2024). "The Thousand Brains Project: A New Paradigm for Sensorimotor Intelligence." arXiv:2412.18354. — Monty modifies representations only in the current reference frame at the current sensed location. This is a specific, local, sensorimotor learning rule. Mapping it onto FEP-style global free-energy minimisation or onto cellular bioelectric signalling requires bridging principles that are not supplied by either framework.
    3. arXiv:2506.21554. "Finding Similar Objects and Active Inference for Surprise in Numenta Neocortex Model." — Notable for what it is: a third-party *attempt* to construct a Monty↔active-inference correspondence, i.e. an open research effort, not an established equivalence. Its existence shows the mapping is a project, not a fact. It also reports that concrete mathematical implementations of active inference "typically struggle to operate in real-world settings" due to high-dimensional modelling and Gaussian noise assumptions — an implementation-level disanalogy with Monty's discrete, sensorimotor, non-Gaussian approach.
    4. Numenta HTM Forum, "Is Thousand Brains Theory wrong?" — Longstanding community criticism that TBT is inconsistent with some neurophysiological observations. Not peer-reviewed, but it documents that the neuroscientific reception is not settled.
    5. Cycle-1 baseline retained: TBT barely addresses goal representation and takes a neocortex-isolated view (omitting subcortical structures that active inference treats as central to precision and motivation); active inference cannot straightforwardly explain desire/motivation and may be formally equivalent to reinforcement learning in relevant regimes.
    6. "The Curious Case of Analogies." AAAI 2026. / "Enhancing Structural Mapping with LLM-derived Abstractions." arXiv:2603.29997 (2026). — The generator of these signals is an LLM whose analogical successes are now shown to be driven by associative similarity and to be sensitive to surface similarity. "Reference frame," "prediction," "surprise" and "model" are shared *vocabulary* across all three frameworks — a maximal-risk configuration for lexically-driven false structural mapping.
    7. "Transitive Expert Error and Routing Problems in Complex AI Systems." arXiv:2601.04416 (2026). — Systematic overweighting of surface similarity and underweighting of differences in causal architecture, specifically when domains are *adjacent* and share surface features. Thousand Brains, active inference and cellular cognition are adjacent domains with heavy shared vocabulary — the described worst case.
    8. Bruineberg et al. (2022), BBS; Raja et al. (2021), Physics of Life Reviews. — If the FEP-side construct (Markov blanket) is instrumental rather than ontological, then the "structure" on one side of the mapping is a modelling convenience and the correspondence cannot be structural in the required sense.

  Strength of challenge: Strong

  NEW SINCE LAST CYCLE: Yes, partially. New to this file: arXiv:2507.04494 (the TBP team's own admission that performance characteristics were unquantified), arXiv:2412.18354 detail on Monty's local learning rule, arXiv:2506.21554 (third-party mapping attempt plus active-inference implementation limits), and the 2026 LLM-analogy sources (AAAI 2026, arXiv:2603.29997, arXiv:2601.04416) that bear on how the signal was generated. No 2026 publication was found asserting or refuting the specific three-way link. What is new in kind: cycle 1 challenged the *frameworks*; cycle 5 can now challenge the *generator* with measured evidence, and can point to the fact that the Monty↔active-inference mapping is an active open research problem rather than a background fact the agent could have retrieved.

  Evidence trajectory (challenging): growing

  Summary: The challenge has strengthened on both ends of the mapping. On the target side, the Thousand Brains framework's own authors were still quantifying its basic performance properties in mid-2025, and its architecture (local, reference-frame-bounded, sensorimotor, neocortex-only) contains explicit disanalogies with FEP's global variational formulation and with substrate-level cellular signalling. On the generator side, 2026 work shows LLM analogical output is associatively driven and is worst precisely for adjacent domains with shared vocabulary — which is this case exactly. That an independent 2025 paper is *attempting* the Monty↔active-inference mapping is the most telling datum: it shows the correspondence is a live research question, so an agent asserting it as a structural finding is asserting more than the field supports.

  Specific risks: If false, this is a load-bearing input to ASSUMPTION-020's three-level unification, so the two fail together — and ASSUMPTION-021 is the weaker link, since it is the one that supplies the middle (cortical) level. A false structural claim here also misrepresents an active researcher's programme, which carries external credibility risk beyond the project. Operationally, the risk is that the Hawkins specialist agent is now primed to generate further Monty-bridges, producing a self-reinforcing cluster of surface analogies concentrated on a single tradition.

  Mitigations available: (a) State the mapping formally: which Monty component corresponds to which FEP quantity, and what plays the role of the generative model, the blanket and the precision term — if these cannot be filled in, the signal is lexical; (b) enumerate disanalogies explicitly (locality vs globality; discrete sensorimotor vs continuous variational; neocortex-only vs whole-organism; no goal representation vs expected-free-energy-driven policy selection); (c) cite arXiv:2506.21554 as the state of the art and position C2A2's claim relative to it rather than independent of it; (d) surface-perturbation test — re-elicit the signal with the shared vocabulary paraphrased away; (e) seek direct comment from the Thousand Brains Project, which maintains public docs and a forum.

  STEELMAN:
    Strongest counterargument: Independent research groups converging on the same correspondence is evidence that the correspondence is real, and arXiv:2506.21554 shows a group doing exactly that — so C2A2's signal is not an isolated LLM confabulation but agrees with a published attempt. Both Monty and active inference are, at the formal level, schemes for sensorimotor belief updating under uncertainty using structured internal models; both make predictions and update on prediction error; both treat action as a means of resolving uncertainty. These are not shared words but shared computational commitments, and reference frames are plausibly the discrete-geometric implementation of what active inference expresses continuously. The absence of a published unification is expected for work this recent, not evidence against it.
    What would need to be true for C2A2 to be safe: (1) The formal mapping can actually be written down at the level of variables and update rules, not described in prose; (2) the mapping survives the disanalogies above, or those disanalogies are argued to be implementation detail rather than substance; (3) C2A2's claim is positioned as agreeing with existing attempts (arXiv:2506.21554) rather than as independent discovery; (4) the cellular-cognition leg — the weakest and least supported of the three — is either substantiated or dropped.
    How to test: Formal-mapping test. Attempt to write the correspondence table (Monty component → active inference quantity → cellular analogue) with explicit update-rule correspondences. Time-box it. If the table cannot be completed without prose hand-waving in more than one row, the signal is surface. Secondary: blinded decoy test — have the Hawkins agent generate a Monty↔[randomly chosen unrelated framework] bridge and see whether it produces something equally confident. If it does, agent confidence carries no signal.

  Recommendation: CHALLENGED
