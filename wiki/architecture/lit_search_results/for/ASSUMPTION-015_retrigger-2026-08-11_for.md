SEARCH-FOR-ASSUMPTION-015:
  Date searched: 2026-08-11
  Original item: ASSUMPTION-015
  Original statement: "Running a potentially biased pipeline (FOR/AGAINST search) is better than not running one at all."
  Cycle: 5 (RE-TRIGGER by 15d, queued 2026-07-05; processed 2026-08-11)

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a, 15b → 15c → 15d → 15a (re-trigger cycle 5)
    Original item: ASSUMPTION-015
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from lit-search pipeline session 2026-04-13, where the pipeline acknowledged its own structural bias risk but operated anyway
      15a (cycle 1, 2026-04-13): initial supporting search — Li/Thurston NIH expertise-vs-bias, GRADE publication bias, Aston 2023; SUPPORTED, Strong
      15d: re-triggered for cycle 5 monitoring
      15a (cycle 5, 2026-08-11): re-searched for supporting literature; checked for new sources since April 2026
    Current status: SUPPORTED

  Search scope: Expertise-vs-bias in evaluation (NIH peer review literature); second-best reasoning and the epistemology of imperfect information; bias in AI-assisted evaluation tools (2025-2026); expert elicitation under heuristics and biases. Comprehensive for the core trade-off; preliminary on the specific question of *self*-evaluating pipelines with structurally opposed FOR/AGAINST arms.

  Supporting evidence found: Yes

  Sources:
    1. Li, D., 2017. "Expertise versus Bias in Evaluation: Evidence from the NIH." American Economic Journal: Applied Economics (AEA, 10.1257/app.20150421). — Re-confirmed as the load-bearing source. Evaluators in their own area are both better informed and more biased; "on net, the benefits of expertise weakly dominate the costs of bias," and "policies designed to limit bias by seeking impartial evaluators may reduce the quality of funding decisions." Directly supports running the informed-but-biased process over not running one.
    2. "Same Performance, Hidden Bias: Evaluating Hypothesis- and Recommendation-Driven AI." arXiv 2603.15824 (2026). — NEW. Finds that equal aggregate performance can mask differing bias profiles, and that expert users are as susceptible to hidden bias as novices — expertise improves discrimination without immunising against systemic bias. Supportive of the assumption only in the weak sense that it treats biased-but-running evaluation as the operative baseline; it is chiefly a boundary condition.
    3. "Evaluating bias in forensic evidence: from expert analysis to AI-based decision tools." Forensic Science International: Synergy (ScienceDirect S2589871X25000749, 2025). — NEW. Domain where the "don't evaluate at all" alternative is unavailable; the field's settled position is bias mitigation and disclosure within a running process, not suspension of the process.
    4. NIHR/NCBI, "Reviewing the evidence: heuristics and biases" (in: Developing a reference protocol for structured expert elicitation in health-care decision-making, NBK571047). — Supports the assumption's core logic explicitly: "excluding all participants who may have strong feelings or vested interests in the outcome may result in the exclusion of those individuals with the greatest expertise in the subject."
    5. Texas Law Review, "The Epistemology of Second Best." — NEW to this file. Cuts both ways and is reported here for honesty: where the path to knowledge is not "continuously upward sloping," acquiring more (imperfect) knowledge can leave a decider worse off than before, and one often cannot know the shape of that path in advance. This is the sharpest identified bound on ASSUMPTION-015.

  Strength of support: Moderate

  NEW SINCE LAST CYCLE: Yes — sources 2, 3, and 5 are new to this file since April 2026. What they add: they do not strengthen the core claim; they sharpen its boundary. The 2026 AI-evaluation work shows expertise does not immunise against systemic bias, and the second-best epistemology literature supplies a formal condition (non-monotone knowledge paths) under which running a biased process is worse than abstaining. The primary supporting result (Li/NIH) is unchanged and unchallenged.

  Evidence trajectory (supporting): stable

  Summary: The central supporting finding — that informed-but-biased evaluation weakly dominates uninformed evaluation — remains intact and remains the strongest available evidence for ASSUMPTION-015. What has changed since April is the arrival of qualifying material rather than reinforcing material: 2026 work on AI-assisted evaluation shows bias can be invisible at constant aggregate performance, and second-best epistemology identifies conditions where more imperfect evidence degrades rather than improves decisions. I am therefore recording Strength as Moderate rather than the cycle-1 Strong, on the grounds that the qualifying literature is now specific enough to name a failure condition, not because any source refutes the core result.

  Caveats: (a) The NIH result is about *expert* bias — evaluators who know more. C2A2's FOR/AGAINST arms are structurally biased by assignment, not by expertise, so the "better informed" leg of the trade-off is assumed rather than demonstrated. (b) The second-best result means support is conditional on the pipeline's error being roughly monotone-improving; if FOR/AGAINST assignment produces systematically misleading rather than merely noisy output, the trade-off flips. (c) No literature quantifies where the flip occurs. (d) Support is weakest exactly where C2A2 sits: automated self-evaluation with no external adjudicator.

  Recommendation: SUPPORTED
