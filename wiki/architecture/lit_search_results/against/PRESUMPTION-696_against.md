SEARCH-AGAINST-PRESUMPTION-696:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-696
  Original statement: That the evaluator condition of REVISE-283 can be satisfied by a
    component built inside C2A2; the whole remedy space entertained is "add another agent," and
    whether an agent minted by the same designer, on the same model family, reading the same
    registers, counts as "a component that did not produce the artefact" is never asked.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-696
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the form of the remedy against the wording of the condition it must
        satisfy — the remedy proposes an internal component, the condition demands a component
        that did not produce the artefact, and the gap between the two was never examined.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Knight, J.C. and Leveson, N.G., 1986. "An Experimental Evaluation of the Assumption of
       Independence in Multi-Version Programming." IEEE Transactions on Software Engineering.
       (Authors, year and title confirmed this session from two independently hosted copies of
       the paper — MIT sunnyday.mit.edu/papers/nver-tse.pdf and a KTH course copy. Volume and
       page numbers not confirmed; full text not read.) Twenty-seven programmers at two
       universities independently implemented the same "Launch Interceptor Program"
       specification without communicating, and the twenty-seven versions were run against one
       million input cases. The individual versions were highly reliable, but the number of
       cases in which more than one version failed was substantially greater than the
       independence assumption predicts. The follow-on fault analysis (Brilliant, Knight and
       Leveson, "Analysis of Faults in an N-Version Software Experiment," IEEE TSE — DOI
       10.1109/32.44387 confirmed this session; author list taken from the DL listing and not
       independently checked) reports that programmers made equivalent logical errors, and,
       more strikingly, that apparently *different* logical errors produced correlated failures
       in different algorithms. This is the canonical refutation of exactly the move
       PRESUMPTION-696 identifies: developing a second component to the same specification does
       not buy independence, and the literature has known this for forty years.
    2. "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels."
       arXiv 2605.29800, hosted also on Apple Machine Learning Research
       (machinelearning.apple.com/research/correlated-llm-evaluation-panels). Title, arXiv
       identifier and Apple hosting confirmed this session; author list and publication venue
       [UNVERIFIED — full text not retrieved]. A panel of nine frontier LLMs drawn from *seven
       different model families* was found to carry only about two independent votes' worth of
       information, with roughly three-quarters of the panel's nominal independence lost because
       the models err on the same items. The relevance is direct and severe: if seven distinct
       vendors' models retain only ~2/9 of nominal independence, a panel drawn from *one* model
       family — C2A2's case — has no evident claim to any independence at all.
    3. Panickssery, A. et al., 2024. "LLM Evaluators Recognize and Favor Their Own Generations."
       NeurIPS 2024 (poster and proceedings PDF both located this session; first author's
       surname confirmed from the proceedings PDF header, co-author list [UNVERIFIED]).
       Establishes self-recognition and self-preference as measurable, distinct phenomena: LLMs
       have non-trivial out-of-the-box accuracy at distinguishing their own outputs from those
       of other models and humans, and fine-tuning experiments found a linear relationship
       between self-recognition capability and self-preference strength. Related work
       ("Quantifying and Mitigating Self-Preference Bias of LLM Judges," arXiv 2604.22891;
       "Self-Preference Bias in LLM-as-a-Judge," OpenReview Ns8zGZ0lmM — identifiers confirmed,
       authors and venues [UNVERIFIED]) traces the mechanism to perplexity: evaluators score
       lower-perplexity text higher, and a model's own output is necessarily low-perplexity to
       it. Note this is a *mechanistic* result, which matters here: it means the bias does not
       require the evaluator to know it authored the artefact, so "the evaluator agent is a
       different instance" is not a defence.
    4. "Self-Attribution Bias: When AI Monitors Go Easy on Themselves." arXiv 2603.04582
       (identifier and title confirmed this session; authors, year and venue [UNVERIFIED]). The
       title states the finding in the exact register of REVISE-283's condition — the monitoring
       role specifically, not the preference-ranking role.
    5. "How Independent are Large Language Models? A Statistical Framework for Auditing
       Behavioral Entanglement and Reweighting Verifier Ensembles." arXiv 2604.07650
       (identifier and title confirmed; authors and venue [UNVERIFIED]). Notable because it
       treats verifier independence as something requiring an *audit* and a statistical
       framework, rather than something a system architect may assert. That framing is itself
       the challenge: C2A2 has asserted it.
    6. Common-mode-failure literature in dependable systems: "The impact of diversity upon
       common mode failures," Reliability Engineering & System Safety (ScienceDirect
       0951832095001204 — journal and article identifier confirmed; authors and year
       [UNVERIFIED — likely Littlewood and Miller, but not confirmed this session), and
       "Common-mode failures in redundant VLSI systems: a survey," IEEE (Xplore record located).
       Establishes the general result that failures sharing a cause are not statistically
       independent, contrary to the core assumption of standard reliability theory, and that
       whenever failure-probability variability across operating environments exists, system
       reliability is *lower* than the independence calculation predicts. Also supplies the
       constructive half used in the steelman below: with *forced* diversity — diversity imposed
       by design rather than hoped for — it becomes theoretically possible to do better than
       independence.

  Strength of challenge: Strong

  Summary: The presumption is challenged from two independent literatures that converge on the
    same verdict. Dependable-systems research settled forty years ago that independently
    developed components built to a shared specification fail together far more often than the
    independence assumption allows — Knight and Leveson's programmers made both equivalent
    errors and, worse, different errors with correlated consequences. The LLM-evaluation
    literature reproduces the result in the exact medium C2A2 operates in, and reports it more
    starkly: a nine-judge panel spanning seven model families retains only about two effective
    votes. On top of correlated error sits self-preference, which has been traced to perplexity
    rather than to authorship knowledge, so instantiating the evaluator as a separate agent does
    not neutralise it. REVISE-283's condition names a component that did not produce the
    artefact; an agent from the same model family, on the same registers, from the same
    designer, shares the specification, the training distribution and the context that generated
    the artefact, and on this literature is closer to a second copy of the producer than to an
    independent evaluator. The decisive point is not that internal evaluation is worthless —
    it is that its independence is an empirical quantity with an established measurement
    procedure, and C2A2 has assumed the value rather than measured it.

  STEELMAN:
    Item: PRESUMPTION-696
    Strongest counterargument: Independence is not binary, and the condition in REVISE-283 may
      not require it to be. "A component that did not produce the artefact" is satisfiable in a
      weaker, procedural sense — the evaluator did not run the generating process, does not hold
      the generating context, and can be given an artefact stripped of authorship cues. The
      common-mode-failure literature's own constructive result supports this: with *forced*
      diversity, redundant systems can outperform the independence baseline, which means
      deliberately engineered difference is a real lever rather than a hope. Nothing in
      Knight-Leveson says correlated failure is total; it says it is materially non-zero, which
      still leaves substantial detection value on the table — an evaluator that catches 60% of
      defects is far better than none, and no serious verification stack claims a single layer
      catches everything. Further, the alternative reading of the presumption is that it demands
      an external evaluator, and an external evaluator is not merely expensive but introduces
      its own failure modes: it cannot see the registers, so it cannot check the artefact
      against the record it was supposedly derived from, and a verifier that lacks context
      produces a different and possibly worse error profile. The honest position may be that
      internal evaluation is the best available option and should be *characterised*, not
      abandoned.
    What would need to be true for C2A2 to be safe: (a) the evaluator's independence is
      measured, not assumed — some analogue of the effective-vote-count computation in source 2,
      run on C2A2's own producer/evaluator pair against a labelled set; (b) diversity is
      *forced* rather than incidental: different prompt scaffold, different context window
      contents, different decision procedure, and ideally a different model family, since
      source 2 shows even cross-family diversity is worth far less than it looks; (c) the
      evaluator receives the artefact without authorship or provenance cues, which is the direct
      block on the self-recognition pathway in source 3 — though note this does *not* block the
      perplexity pathway, which is why (b) matters more; (d) the residual correlated-failure
      class is named explicitly, so the system knows what its evaluator structurally cannot
      catch and does not treat evaluator silence as evidence of correctness; (e) REVISE-283's
      condition is either restated in the weaker procedural sense — in which case it should say
      so — or the remedy is acknowledged not to satisfy it. Condition (a) is decisive: without a
      measured number, every other condition is unfalsifiable.
    How to test: Directly runnable and cheap. Construct a set of artefacts with known injected
      defects — the mutation-testing move — and run both the producing agent and the proposed
      evaluator agent over them. Compute (i) the evaluator's detection rate, (ii) the producer's
      self-detection rate, and (iii) the conditional probability that the evaluator misses a
      defect given the producer missed it. If (iii) is close to 1, the evaluator supplies no
      independent information and the presumption is refuted in-system. Second test, on
      self-preference: present the evaluator with matched pairs of artefacts, one produced
      in-system and one produced externally but of equal quality by an outside judgement, and
      measure the score differential; a non-zero differential is self-preference bias measured
      on C2A2's own stack. Third, cheapest: check whether any existing evaluator step in C2A2
      has ever returned a negative verdict on an artefact the producer endorsed. A zero count
      over a long run is prima facie evidence of the correlated-failure regime and can be
      obtained by grep alone.

  Specific risks: If the evaluator is not independent, then (i) every REVISE-283-derived
    assurance is circular — the system's confidence in its artefacts is generated by the same
    process that generated the artefacts, and confidence rises without error probability
    falling; (ii) the failure mode is silent and self-reinforcing, because a correlated
    evaluator returns "pass" precisely on the defects the producer was going to introduce, so
    the observed pass rate looks excellent exactly when the stack is weakest; (iii) adding
    *more* internal evaluators makes the problem worse rather than better, since source 2 shows
    the marginal information of an additional correlated judge is near zero while its cost and
    apparent authority are not — the natural remedy is the one the literature says fails; (iv)
    self-preference means the bias has a direction, not just a variance, so errors do not
    average out across many evaluations; (v) the remedy space itself is the deepest risk — if
    "add another agent" is the only move the system entertains, then no amount of evidence
    against internal evaluation can change the design, because the alternative was never in the
    option set.

  Mitigations available: (1) Measure effective independence before relying on it, using the
    injected-defect protocol above; report a number, not a claim. (2) Forced diversity: different
    model family for the evaluator where feasible, and where not, deliberately divergent
    scaffolding and decision procedure rather than a mirrored one. (3) Blind the evaluator to
    authorship and provenance, which blocks the self-recognition channel even though it does not
    block the perplexity channel. (4) Add a non-agent evaluator for whatever subset of the
    condition is mechanically checkable — a deterministic checker shares no training
    distribution with the producer and is genuinely independent on the properties it covers,
    which is the strongest available answer to the condition as literally written. (5) Human
    spot-audit at a fixed sampling rate, which supplies the only unambiguously external evidence
    the system can get, and which also calibrates the evaluator. (6) Record the residual
    correlated-failure class explicitly so evaluator silence is not read as assurance. (7)
    Rewrite REVISE-283's condition to state which sense of independence it requires — the
    presumption exists partly because the condition's wording admits both readings.

  Search scope: Comprehensive for the two directly relevant literatures — multi-version
    programming and the independence assumption (Knight-Leveson and its follow-on fault
    analysis), and LLM-as-judge correlated error and self-preference (panel effective-vote
    counts, self-recognition, self-preference mechanism, self-attribution bias in monitors).
    Adequate for the general common-mode-failure framing in dependable systems, though those
    sources were reached via survey and abstract material rather than full texts. Preliminary
    on two areas that would sharpen it and were not searched: formal auditing standards on
    auditor independence (the accounting/assurance literature on self-review threat, which is
    the closest direct analogue to REVISE-283's condition and would likely strengthen the
    challenge further), and the AI-safety literature on scalable oversight and debate, which
    addresses the same structural problem from the design side. Broader search recommended on
    the auditor-independence literature specifically — it is the one body of work that has
    codified exactly what "a component that did not produce the artefact" must mean, and it was
    not reached this session.

  Recommendation: CHALLENGED
