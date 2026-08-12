SEARCH-AGAINST-ASSUMPTION-017:
  Date searched: 2026-08-11
  Original item: ASSUMPTION-017
  Original statement: "AI synthesis is complementary to human validation; AI does first-pass synthesis, humans validate."
  Cycle: 5 (RE-TRIGGER by 15d, queued 2026-07-05; processed 2026-08-11)

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 5)
    Original item: ASSUMPTION-017
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from morning walk chat summary 2026-04-14
      15b (cycle 1, 2026-04): initial challenging search — automation bias, overreliance, hallucination detectability
      15d: re-triggered for cycle 5 monitoring
      15b (cycle 5, 2026-08-11): re-searched for challenging literature; checked for new sources since April 2026
    Current status: CHALLENGED

  Search scope: Comprehensive. Covered (a) automation bias and human-AI reliance experiments 2024–2026, (b) human oversight frameworks and oversight-fatigue at agent scale, (c) AI in systematic review/evidence synthesis with quantified residual error, (d) rubber-stamping/human-factors critique, (e) 2026 AI safety reporting on oversight. This is the best-evidenced item in the batch.

  Challenging evidence found: Yes

  Sources:
    1. "Artificial intelligence in systematic reviews and meta-analyses: task-specific performance, residual error quantification, and human oversight." ScienceDirect, 2026 (S1877056826002148). — The single most damaging new source. Quantifies generative-AI performance on exactly C2A2's task: GenAI missed 68%–96% of relevant studies in searching; incorrect inclusion decisions in 0%–29% of cases; incorrect *exclusion* decisions in 1%–83%. Conclusion: current evidence does not support autonomous use. A "first pass" that misses up to 96% of relevant literature is not a first pass a human can validate — the human never sees what was missed.
    2. Adnan Masood, July 2026. "The Unbearable Lightness of Clicking Approve." Medium. — Synthesises three decades of human-factors research: reviewers of accurate systems drift into rubber-stamping — they stop verifying and approve by default while the record still shows a human decision. Quantifies the scaling failure: 50 agents × 20 tool calls/hour = 1,000 approval-eligible events/hour; routing even 10% to human review consumes 3+ FTE doing nothing but rubber-stamping. Directly relevant to the 33-agent plan (ASSUMPTION-023) — the two items interlock.
    3. "The Oversight Fatigue Problem: Why HITL Breaks Down at Scale." HackerNoon, 2026. — Human-in-the-loop degrades as a function of event volume; the oversight guarantee is strongest exactly when it is least needed and weakest when volume rises.
    4. "Keeping an Eye on AI: A Framework for Effective Human Oversight of AI Systems." arXiv:2605.16278 (May 2026). — Argues effective oversight requires specific structural conditions (capability, authority, incentive, information access); nominal human-in-the-loop without them does not constitute oversight. C2A2's arrangement — a single human validating output from a system that produced it — meets few of these.
    5. "Effects of Generative AI Errors on User Reliance Across Task Difficulty." arXiv:2604.04319 (2026). — Reliance on erroneous AI output increases with task difficulty. C2A2's synthesis tasks (cross-tradition philosophy of mind) are high-difficulty, i.e. the worst case for validation.
    6. Randomised experiment, n=2,784 (reported in 2026 oversight reviews). — Participants were less likely to correct erroneous suggestions labelled as AI-sourced when correcting required extra effort or when they held favourable attitudes toward AI. Both conditions hold for C2A2: correction requires reading primary sources, and the operator is by construction favourably disposed toward the method.
    7. International AI Safety Report 2026. arXiv:2602.21012. — Institutional-level treatment of oversight limitations at scale.
    8. Cycle-1 baseline retained: AI & Society 2025 automation-bias review (explainability can *increase* inappropriate reliance); Microsoft Research 2022 overreliance review; Farquhar et al., Nature 2024 semantic-entropy hallucination detection (hallucinations systematic, poorly calibrated for human detection); hallucination survey (arXiv 2023).

  Strength of challenge: Strong

  NEW SINCE LAST CYCLE: Yes — and the new material is qualitatively stronger than April's. Five new sources: ScienceDirect 2026 systematic-review error quantification, Masood 2026, HackerNoon 2026 oversight fatigue, arXiv:2605.16278 (May 2026), arXiv:2604.04319 (Apr 2026), plus the International AI Safety Report 2026. What they add: April's file argued automation bias *generically*. The 2026 literature (a) quantifies AI error rates on the specific task of literature search and screening, with a recall failure so severe that human validation is structurally impossible for the missed set, and (b) quantifies oversight collapse as a function of agent count, which converts ASSUMPTION-017 from a general concern into a specific incompatibility with the 33-agent plan.

  Evidence trajectory (challenging): growing

  Summary: This assumption is now challenged on two independent fronts that did not both exist in April. First, the error-profile front: AI literature search misses the majority of relevant studies, and a human validator cannot validate an omission they cannot see — so the complementarity claim fails asymmetrically, catching commission errors while being blind to omission errors, which are the dominant error type. Second, the oversight-capacity front: rubber-stamping is the documented default for accurate-seeming systems, and review capacity collapses at agent scale, with 2026 work putting concrete numbers on it. Combined with arXiv:2604.04319's finding that reliance on error *increases* with task difficulty, the conditions under which C2A2 operates are close to worst-case for the assumption. Nothing found in this cycle supports the complementarity claim as stated.

  Specific risks: If false, "human validation" is a documentation artefact rather than a control, and the wiki's credibility rests on a check that is not happening. The specific failure mode is silent: omitted literature never surfaces, so the project cannot distinguish "no contradicting evidence exists" from "the search missed it" — which is exactly the confusion ASSUMPTION-019 (paradigm-shift interpretation of literature absence) then converts into a positive claim of novelty. These two items compound: a search that misses 68–96% of relevant work, interpreted through a Kuhnian lens, manufactures false novelty. At 33 agents, review volume makes genuine validation arithmetically impossible.

  Mitigations available: (a) Measure recall directly — construct a gold-standard set of 20 papers known to be relevant to a C2A2 topic and check what fraction the pipeline retrieves; (b) sample-audit rather than full-review, with a declared sampling rate and error-rate estimate, which is honest where full review is not feasible; (c) separate the validator from the generator — the person who commissioned the synthesis is the worst validator; (d) require primary-source citation checks on a random sample (cheapest high-yield control); (e) hard-cap the number of items requiring human sign-off per day and refuse to generate beyond it; (f) log validation *effort* (time spent per item), since near-zero time is direct evidence of rubber-stamping.

  STEELMAN:
    Strongest counterargument: The automation-bias literature studies operators validating decisions in domains where they lack independent expertise and face time pressure and volume — radiologists, pathologists, annotation crowdworkers. C2A2's operator is domain-invested, unhurried, personally motivated to catch errors, and reviewing a small number of high-salience claims rather than a stream of routine approvals. The systematic-review recall figures concern fully autonomous AI search replacing a trained information specialist; C2A2 does not claim exhaustive recall, it claims useful first-pass synthesis, and low recall is only fatal if the project treats absence as evidence — which is a separate assumption (ASSUMPTION-019), not this one. Complementarity is a division of labour claim, and division of labour does not require either party to be error-free.
    What would need to be true for C2A2 to be safe: (1) The human validator actually reads primary sources for a defined sample, and this is logged rather than assumed; (2) low recall is acknowledged in every artefact, so absence is never read as evidence; (3) review volume stays within human capacity — which constrains agent count independently of ASSUMPTION-023; (4) validation is adversarial in structure, not confirmatory.
    How to test: Two cheap tests. (i) Seeded-error test: insert 5 fabricated citations and 3 subtly wrong claims into a synthesis batch and measure detection rate. A detection rate below ~80% falsifies the assumption directly. (ii) Recall test: take a topic where the true relevant set is known and measure what fraction the pipeline surfaced. Both are half-day exercises and neither has been run in five cycles.

  Recommendation: CHALLENGED
