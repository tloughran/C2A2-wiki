SEARCH-AGAINST-PRESUMPTION-014:
  Date searched: 2026-08-11
  Original item: PRESUMPTION-014
  Original statement: "Cross-tradition signals from AI agents are structurally meaningful, not just surface associations."
  Cycle: 5 (RE-TRIGGER by 15d, queued 2026-07-05; processed 2026-08-11)

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 5)
    Original item: PRESUMPTION-014
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inferred as unstated presumption underwriting the value of cross-tradition signals produced by specialist agents
      15b (cycle 1, 2026-04): initial challenging search (2026-04-13) — structure-mapping/surface-similarity literature, LLM analogy critiques
      15d: re-triggered for cycle 5 monitoring
      15b (cycle 5, 2026-08-11): re-searched for challenging literature; checked for new sources since April 2026
    Current status: CHALLENGED

  Search scope: Comprehensive for the LLM-analogy angle. Covered (a) LLM analogical reasoning benchmarks and mechanistic studies 2025–2026, (b) apophenia / spurious-pattern literature, (c) cross-domain hallucination detection, (d) classical structure-mapping evidence on surface-vs-structure confusion, (e) LLM-as-judge novelty assessment. Not covered: human-expert baselines for cross-tradition synthesis specifically in philosophy/theology (no such benchmark appears to exist — this is itself a finding).

  Challenging evidence found: Yes

  Sources:
    1. Kim et al., 2026. "Enhancing Structural Mapping with LLM-derived Abstractions for Analogical Reasoning in Narratives." arXiv:2603.29997. — Finds LLM analogical performance is sensitive to prompt format AND to the degree of *surface* similarity between narratives; remaining failure modes are abstraction at the wrong level and missed implicit causality. Exactly the failure mode PRESUMPTION-014 denies.
    2. "The Curious Case of Analogies: Investigating Analogical Reasoning in Large Language Models." AAAI 2026 Proceedings (ojs.aaai.org/index.php/AAAI/article/view/40414). — Success on proportional analogies is largely driven by *associative* (semantic-similarity) relations between items rather than by mapping relational structure. Direct contradiction of "structural, not surface."
    3. SCAR (Scientific Analogical Reasoning) benchmark results, reported in analogical-reasoning surveys 2025–2026. — GPT-4-class models frequently select structurally incorrect completions, indicating failure to enforce mapping exclusivity (the one-to-one constraint that defines genuine structure-mapping in Gentner's SMT).
    4. "Structural Ranking of the Cognitive Plausibility of Computational Models of Analogy and Metaphors with the Minimal Cognitive Grid." arXiv:2605.01359 (2026). — Ranks LLM-based analogy models low on cognitive plausibility relative to explicit structure-mapping engines; formal analogy output does not imply structure-mapping process.
    5. "On the Limits of LLM-as-Judge for Scientific Novelty Assessment." arXiv:2606.12071 (June 2026). — LLM novelty/quality judgements diverge substantially and inconsistently from human expert judgements. Undermines using the agents themselves (or an orchestrator LLM) to certify that a cross-tradition signal is structural.
    6. "Do Hallucination Neurons Generalize? Evidence from Cross-Domain Transfer in LLMs." arXiv:2604.19765 (2026). — Evidence for a domain-general hallucination signal; cross-domain generation is precisely where fabrication generalizes, not where it is suppressed.
    7. "Transitive Expert Error and Routing Problems in Complex AI Systems." arXiv:2601.04416 (2026). — Describes systematic overweighting of surface-level similarity and underweighting of differences in causal architecture between adjacent domains — the mechanism by which plausible-but-false cross-tradition bridges are produced.
    8. Gentner & Schumacher (1986); Gentner, Rattermann & Forbus (1993). — Baseline human evidence: surface features dominate *retrieval* of analogues even when structure dominates *evaluation*. Anything that generates candidate analogies (human or LLM) is surface-driven at the generation step; C2A2 has no separate evaluation step.

  Strength of challenge: Strong

  NEW SINCE LAST CYCLE: Yes. Five of eight sources are new since April 2026: arXiv:2603.29997 (Mar 2026), arXiv:2605.01359 (May 2026), AAAI 2026 proceedings entry, arXiv:2606.12071 (Jun 2026), arXiv:2604.19765 (Apr 2026), arXiv:2601.04416 (Jan 2026). What they add: April's challenge rested largely on classical structure-mapping theory plus general hallucination literature. The 2026 additions supply *direct measurement* — LLM analogy success is now empirically attributed to associative similarity rather than relational structure, and the mapping-exclusivity failure is quantified on a scientific-analogy benchmark. The challenge moved from "theoretically plausible" to "empirically demonstrated in the exact modality C2A2 uses."

  Evidence trajectory (challenging): growing

  Summary: The challenging literature has strengthened materially since April 2026. Where cycle 1 could only invoke Gentner-era theory about surface/structure confusion, the 2026 literature now measures it in LLMs directly: analogical success is predominantly associative, mapping exclusivity fails on scientific analogies, and performance degrades with prompt format and surface-similarity manipulations that a genuine structural mapping would be invariant to. Additionally, LLM self-assessment of analogy quality and novelty is now shown to be unreliable, closing the obvious escape hatch of "ask the agent whether the signal is structural." Nothing found supports the presumption that agent-generated cross-tradition signals are structural by default. The honest reading is that C2A2's cross-tradition signals are *candidate* analogies of unknown structural status until externally adjudicated.

  Specific risks: If false, the SUPER-BRIDGE-class findings and the entire cross-tradition layer of C2A2 are a catalogue of surface associations dressed as discoveries. Downstream, every finding that cites a cross-tradition signal inherits the defect, and the wiki accumulates confidently-stated pseudo-connections that are expensive to retract because they have been linked into and narrated over. Because generation is surface-driven and there is no independent structural check, the error rate is unbounded and unmeasured.

  Mitigations available: (a) Require every cross-tradition signal to state the explicit relational mapping (which entities, which relations, which higher-order constraint) rather than a prose assertion of similarity; (b) run a surface-perturbation test — paraphrase away shared vocabulary and re-elicit; a structural signal should survive, a lexical one will not; (c) adversarial disanalogy prompt — require the agent to state what would break the mapping; (d) require an independent human or non-LLM adjudicator, given arXiv:2606.12071; (e) tier signals as CANDIDATE / MAPPED / ADJUDICATED and never cite CANDIDATE signals as findings.

  STEELMAN:
    Strongest counterargument: Structure-mapping benchmarks test forced-choice proportional analogies under time/format constraints that bear little resemblance to C2A2's task, which is open-ended generation reviewed by a human with domain knowledge. The relevant question is not whether an LLM reliably picks the structurally correct completion in a four-way multiple choice, but whether it can surface a candidate that a competent human then recognises as structural — a much lower bar, and one where high recall with moderate precision is genuinely useful. Gentner's own data show that surface similarity dominates human retrieval too, yet human analogical discovery in science works; the fix is not better generation but a downstream evaluation stage, which C2A2 nominally has in the form of human review.
    What would need to be true for C2A2 to be safe: (1) A real, non-perfunctory human evaluation stage exists and is exercised (see ASSUMPTION-017, which the automation-bias literature challenges — these two items interlock); (2) cross-tradition signals are treated as hypotheses, not findings, until adjudicated; (3) the false-positive rate is measured rather than assumed; (4) no downstream artefact cites an unadjudicated signal.
    How to test: Take a random sample of 30 existing cross-tradition signals. For each, (i) generate a matched decoy by pairing two traditions at random and asking the same agent to find a connection; (ii) apply the surface-perturbation test; (iii) have a blinded domain-competent reviewer rate real vs decoy on structural depth. If reviewers cannot distinguish real signals from random-pair decoys above chance, the presumption is falsified. Cost: roughly one day. This test has been available since cycle 1 and has not been run — which is itself the strongest evidence for CHALLENGED status.

  Recommendation: CHALLENGED
