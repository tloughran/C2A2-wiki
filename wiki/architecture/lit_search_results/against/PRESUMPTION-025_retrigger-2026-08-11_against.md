SEARCH-AGAINST-PRESUMPTION-025:
  Date searched: 2026-08-11
  Original item: PRESUMPTION-025
  Original statement: [inferred] "Resuming a paused deployment was justified by epistemic progress, not just operational cleanup."
  Cycle: 5 (RE-TRIGGER by 15d, queued 2026-07-05; processed 2026-08-11)

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 5)
    Original item: PRESUMPTION-025
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced as unstated presumption — the unpause decision conflates operational and epistemic readiness
      15b (cycle 1, 2026-04): initial challenging search — enterprise scaling data, sunk cost, perpetual-pilot-trap inversion, Gartner governance
      15d: re-triggered for cycle 5 monitoring
      15b (cycle 5, 2026-08-11): re-searched for challenging literature; checked for new sources since April 2026
    Current status: PARTIALLY-CHALLENGED

  Search scope: Comprehensive on escalation-of-commitment and premature-scaling literature, including the new LLM-specific escalation work. Note a structural limitation: this presumption concerns a *specific past decision* in this project, so no literature can confirm or refute it directly — the literature can only establish base rates and mechanisms, and identify whether the decision's conditions match known failure profiles. Rated accordingly.

  Challenging evidence found: Partial

  Sources:
    1. Staw's escalation-of-commitment literature, as summarised in 2026 AI-investment analyses (thepricingconundrum.substack.com, "Buying AI Once, Justifying AI Twice"). — The four amplifying conditions are named precisely: (i) the original decision was made publicly, (ii) the decision-maker was personally responsible, (iii) the project felt close to producing expected outcomes, and (iv) performance feedback was ambiguous enough to permit multiple interpretations. The source explicitly notes all four apply to typical 2026 AI commitments. All four also apply to C2A2's unpause: the pause and unpause are documented in the wiki, the operator made both decisions, the project is described as approaching a rollout, and the feedback (literature-pipeline output) is maximally ambiguous. This is the strongest single element of the challenge and is new to this file.
    2. "Getting out of the Big-Muddy: Escalation of Commitment in LLMs." arXiv:2508.01545. — New and pointed: LLMs *themselves* exhibit escalation of commitment. Since the unpause reasoning was produced with LLM assistance, the advisory channel shares the bias rather than correcting it. There is no independent check in the loop.
    3. "CogBias: Measuring and Mitigating Cognitive Bias in Large Language Models." arXiv:2604.01366 (2026). — Corroborates persistent cognitive biases including sunk-cost-type reasoning across model families.
    4. Gartner and 2026 enterprise data. — ~30% of generative AI projects abandoned after proof of concept; >40% of agentic projects predicted cancelled by end-2027; 89% of agent pilots never reach production; ~54% stall 3–9 months after an apparently successful pilot. The last figure is the relevant one: "apparently successful pilot followed by resumption of scaling" is the exact profile that stalls at the highest rate.
    5. CIO (2026). "Why most agentic AI projects stall before they scale." — Mismatch between expectations and reality typically does not become visible until projects move *beyond* pilots into operational settings; costs rise and projects are then paused or cancelled. Implies that operational cleanup during a pause cannot surface the failures that matter, so a clean pause is weak evidence of readiness.
    6. Pertama Partners (2026), "AI Project Failure Rate 2026" and related 2026 due-diligence guidance. — Base-rate context for resumption decisions; emphasises that governance readiness, not operational tidiness, predicts successful scaling.
    7. Cycle-1 baseline retained: enterprise scaling failure statistics; sunk-cost/forward-looking-expected-value distinction; the inverted perpetual-pilot-trap argument; Gartner governance-before-scaling.

  Strength of challenge: Moderate

  NEW SINCE LAST CYCLE: Yes, but modest in volume and high in relevance. Three new sources: the four-conditions escalation framing applied explicitly to 2026 AI commitments, arXiv:2508.01545 (escalation of commitment in LLMs), and arXiv:2604.01366. Updated base rates (89% never reach production; 54% stall post-pilot) replace April's older figures. What they add: April's file asserted sunk-cost risk generically; cycle 5 can now check the decision against four named amplifying conditions, all of which are satisfied here, and can note that the LLM advisory channel shares the bias rather than counteracting it. That converts a generic warning into a specific diagnostic match.

  Evidence trajectory (challenging): growing

  Summary: The presumption is not refuted — no literature can adjudicate a specific past decision — but the conditions under which escalation of commitment is strongest are all present in this case, which shifts the burden of proof onto the resumption decision. The most damaging structural point is that the ambiguity of the feedback is precisely what makes the presumption unfalsifiable from the inside: "epistemic progress" was never operationalised, so any state of the literature pipeline can be read as progress. The new finding that LLMs themselves escalate commitment removes the assistant as a corrective. Nothing found supports the claim; the honest status is that it is unverified rather than false, and it is unverified in a way that matches a known failure pattern.

  Specific risks: If false, the project resumed on the strength of feeling unblocked rather than being unblocked, and the twelve items in this very batch — all still CHALLENGED or PARTIALLY-CHALLENGED at cycle 5, four months after the unpause — are the direct evidence. That is the concrete risk realised: the epistemic questions that motivated the pause are demonstrably not resolved. Continuing to scale on that basis means the 33-agent rollout (ASSUMPTION-023) rests on assumptions the project's own pipeline still flags as challenged, and each further cycle raises the cost of reversing.

  Mitigations available: (a) Retrospectively state what epistemic progress was claimed at the unpause and check it against the current status of the items that motivated the pause — this is a one-hour audit with a decisive answer; (b) separate the two readiness types explicitly in future decisions (operational-ready ≠ epistemic-ready) and require both to be asserted separately; (c) obtain an outside view — someone not responsible for the original decision, since personal responsibility is one of the four amplifying conditions; (d) pre-register unpause criteria before any future pause, so the decision cannot be made on ambiguous feedback; (e) treat resumption as reversible by default with a scheduled re-review rather than as a commitment.

  STEELMAN:
    Strongest counterargument: Pauses have real costs and indefinite pauses are a documented failure mode in their own right (see ASSUMPTION-016). A project that refuses to resume until every epistemic question is closed will never resume, because these questions — the ontological status of Markov blankets, whether LLM analogies are structural — are open research problems that a personal wiki project cannot close. The rational policy under irreducible uncertainty is to resume with hedges: proceed on the reversible parts, mark the contested claims as contested, and continue monitoring. Operational cleanup is not nothing, either — it removes the failure modes that were actually blocking, and holding out for epistemic resolution before fixing operational problems would be the wrong ordering. Escalation-of-commitment framing is unfalsifiable in the opposite direction: any decision to continue can be labelled escalation.
    What would need to be true for C2A2 to be safe: (1) The resumed activity is genuinely reversible, and contested claims are marked as such in the wiki rather than asserted; (2) the epistemic questions are being actively worked, not merely monitored — five cycles of re-triggering with no empirical test run is monitoring, not working; (3) an explicit stop rule exists for the resumed activity; (4) at least one person other than the decision-maker has reviewed the resumption rationale.
    How to test: Unpause audit. Retrieve the stated rationale for the unpause. List the specific concerns it claimed were resolved. Check each against the current cycle-5 status of the corresponding item. If the majority remain CHALLENGED — which, on this batch's results, they do — then the unpause was operational rather than epistemic and PRESUMPTION-025 is falsified for this instance. This test is available immediately and requires no external input.

  Recommendation: PARTIALLY-CHALLENGED
