SEARCH-FOR-PRESUMPTION-918:
  Date searched: 2026-09-07
  Original item: PRESUMPTION-918
  Original statement: [inferred] A context that has lost evaluator independence can accurately assess how
    much that loss mattered; declaring a bias discharges it. Tested as two sub-claims: (i) an agent that
    knows it has been exposed to a biasing input can, under some conditions, correct or accurately
    bound the resulting bias (self-assessment CAN work); (ii) declaring the exposure to a downstream
    reader is a workable remedy (disclosure CAN work).

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-918
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-09-06 run's practice of the orchestrator writing AGAINST files after
        reading FOR files and then declaring the compromised independence.
      15a: Searched for supporting literature (2026-09-07) by a delegated 15a subagent (one subagent, all
        three items, FOR direction only).
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Wilson, T.D. and Brekke, N., 1994. "Mental contamination and mental correction: Unwanted
       influences on judgments and evaluations." Psychological Bulletin 116(1), 117-142. [VERIFIED:
       title, journal, year via PubMed 8078969 and Semantic Scholar listings; the four correction
       conditions (awareness of the bias, motivation to correct, knowledge of direction and magnitude,
       sufficient control over the response) from search snippets; pages from prior knowledge, NOT
       verified in this search; full text NOT retrieved] — Usually cited AGAINST self-correction, but the
       model is explicitly conditional: correction succeeds when the four conditions are met. The C2A2
       case satisfies the first two by construction (the orchestrator knows exactly what it read and is
       motivated to flag it), so the model predicts partial correction is possible and identifies what
       is missing (a magnitude estimate).
    2. Wegener, D.T. and Petty, R.E., 1997. "The Flexible Correction Model: The role of naive theories of
       bias in bias correction." Advances in Experimental Social Psychology 29, 141-208. [VERIFIED:
       title, series, volume, pages via ScienceDirect (S0065260108600179) and richardepetty.com PDF
       listing; core postulates (correction occurs when judges are motivated and able, guided by their
       theory of the bias, adjusting in the opposite direction by an amount commensurate with perceived
       bias) from search snippets; full text NOT retrieved] — Empirical programme showing people DO
       correct judgments for biases they believe are operating, provided they hold a theory of the bias
       and are motivated. Direct support for sub-claim (i): an agent with an explicit theory of its own
       contamination ("I read the FOR file first") can and does adjust.
    3. Lord, C.G., Lepper, M.R. and Preston, E., 1984. "Considering the opposite: A corrective strategy
       for social judgment." Journal of Personality and Social Psychology 47(6), 1231-1243. [VERIFIED:
       title, journal, year via PubMed 6527215 and Semantic Scholar; result (consider-the-opposite
       instruction had greater corrective effect than instructions to be fair and unbiased) from search
       snippets; volume/pages from prior knowledge, NOT verified; full text NOT retrieved] — Structured
       self-correction (explicitly generating the opposing case) demonstrably reduces biased
       assimilation. Supports the specific C2A2 move: an orchestrator that has read FOR and then
       deliberately writes AGAINST is executing a consider-the-opposite procedure, which is the one
       debiasing strategy with a strong replication record.
    4. Pronin, E. and Kugler, M.B., 2007. "Valuing thoughts, ignoring behavior: The introspection
       illusion as a source of the bias blind spot." Journal of Experimental Social Psychology 43(4),
       565-578. [VERIFIED: title, journal via ScienceDirect (S0022103106000916) and Princeton listing;
       key result (participants ceased denying their relative susceptibility to bias only after being
       educated about nonconscious processes and the fallibility of introspection) from search
       snippets; issue/pages NOT verified; full text NOT retrieved] — The bias-blind-spot programme
       itself reports a condition under which self-assessment improves: education about the
       unreliability of introspection. Supports sub-claim (i) in its weak form: self-assessment of bias
       is trainable, not fixed.
    5. Sah, S., Loewenstein, G. and Cain, D.M., 2013. "The burden of disclosure: Increased compliance
       with distrusted advice." Journal of Personality and Social Psychology 104(2), 289-304. [VERIFIED:
       title, journal, volume, pages via SSRN 1615025, PubMed 23088229 and CMU PDF listing; moderating
       conditions (pressure to comply is reduced when the decision is made in private, when disclosure
       comes from an external source, when it is not common knowledge, or after a cooling-off period)
       from search snippets; full text NOT retrieved] — The disclosure literature is largely
       cautionary, but this paper identifies conditions under which disclosure works as intended:
       disclosure by a third party, private downstream decision, cooling-off. In C2A2 the declaration is
       written into a file read later by a different agent (14b) with no social pressure, which is
       structurally the "private decision, cooled off" case. Conditional support for sub-claim (ii).
    6. Kadavath, S., Conerly, T., Askell, A., Henighan, T., Drain, D., Perez, E., et al. (36 authors),
       2022. "Language Models (Mostly) Know What They Know." arXiv:2207.05221. [VERIFIED: abstract page
       retrieved from arxiv.org; verbatim: "larger models are well-calibrated on diverse multiple choice
       and true/false questions when they are provided in the right format"; "We find encouraging
       performance, calibration, and scaling for P(True)"; also "they struggle with calibration of
       P(IK) on new tasks"] — LLM self-evaluation of its own outputs is measurably calibrated for large
       models in suitable formats. Supports the premise that an LLM context can produce a meaningful
       self-assessment of its own reliability, which the presumption requires.
    7. Saunders, W., Yeh, C., Wu, J., Bills, S., Ouyang, L., Ward, J. and Leike, J., 2022.
       "Self-critiquing models for assisting human evaluators." arXiv:2206.05802. [VERIFIED: abstract
       page retrieved from arxiv.org; verbatim: "Larger models write more helpful critiques, and on most
       tasks, are better at self-critiquing, despite having harder-to-critique outputs"; "Larger models
       can also integrate their own self-critiques as feedback"; also "even large models may still have
       relevant knowledge they cannot or do not articulate as critiques"] — LLM self-critique produces
       critiques that help humans find flaws they would otherwise miss. Supports the C2A2 practice of
       an agent self-reporting a defect (loss of independence) as informative to a downstream human or
       agent reader.

  Strength of support: Moderate (for sub-claim i, in its conditional form); Weak (for sub-claim ii)

  Summary: The social-psychology correction literature is conditional rather than flatly negative:
  Wilson and Brekke (1994) and Wegener and Petty (1997) both predict that an agent who is aware of a
  specific biasing exposure, motivated to correct, and holding a theory of the bias will adjust in the
  right direction, and Lord, Lepper and Preston (1984) show that the structured "consider the opposite"
  procedure — which is what writing AGAINST after reading FOR amounts to — is among the most effective
  debiasing moves known. Pronin and Kugler (2007) add that self-assessment of bias improves with
  education about introspection's limits. On the LLM side, Kadavath et al. (2022) and Saunders et al.
  (2022) show that large models' self-evaluations and self-critiques are calibrated enough to be useful
  to downstream readers. For the declaration half, Sah, Loewenstein and Cain (2013) identify conditions
  (third-party or asynchronous disclosure, private decision, cooling-off) under which disclosure does
  what it is meant to, and the C2A2 file-based hand-off resembles those conditions more than the
  face-to-face advisor case that produces the perverse effects.

  Caveats: (a) None of the sources support the strong reading that the contaminated context can
  ACCURATELY quantify how much the loss mattered; Wilson and Brekke's third condition (knowing
  magnitude) is precisely the one C2A2's declaration does not meet, and Kadavath et al. report
  calibration failures on out-of-distribution tasks. (b) None support "declaring a bias discharges it";
  at best disclosure lets a downstream reader discount, and Sah et al.'s main finding is that disclosure
  often backfires. (c) The Wegener/Petty corrections are guided by naive theories that can be wrong,
  producing over- or under-correction; accuracy of the correction is not guaranteed. (d) The LLM
  evidence is for factual self-evaluation and summary critique, not for self-assessment of
  cross-document contamination; domain transfer is by analogy. (e) Search scope: preliminary — 8
  queries; not covered: Church and Kuang (2009) on disclosure combined with sanctions, Loewenstein,
  Sah and Cain (2012) "The unintended consequences of conflict of interest disclosure", the LLM
  self-correction debate (Huang et al. 2023 "Large language models cannot self-correct reasoning yet"
  vs Madaan et al. 2023 Self-Refine), and the judicial-recusal / self-recusal literature, which is the
  closest institutional analogue.

  Recommendation: PARTIALLY-SUPPORTED
