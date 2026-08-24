SYSTEMIC-RISK-FLAG_2026-08-18_G3

  Date: 2026-08-18
  Raised by: Agent 15b (Literature Search — AGAINST)
  Group: G3

  ---

  FLAG 1 (PRIMARY) — "Declared but unenforced": constraints that exist as text and not as force

  Affected items: PRESUMPTION-758, PRESUMPTION-762, PRESUMPTION-764, PRESUMPTION-833

  Common vulnerability:
    Four of the seven items in this batch are instances of one structure. In each, C2A2 has written down a
    constraint or a lifecycle and has not attached a cost, a deadline, or a terminal state to departing from it:
      - 758: a recall window with an exception clause that has no bound and no invocation counter.
      - 762: a hold queue with no expiry, no renewal requirement, and no default disposition on timeout.
      - 764: a budget that every run declares and every run breaches, with disclosure as the only sanction.
      - 833: a status lifecycle with a terminal state for a failed claim and none for a withdrawn flag.
    The literature treats these as one phenomenon with one prognosis. Vaughan's normalization of deviance
    describes the dynamics: repeated, documented, consequence-free departure from a specified limit
    reclassifies the departure as standard practice and silently raises the limit, without anyone deciding to
    raise it. The corporate-governance work on comply-or-explain describes the terminal state: explanations
    degrade to boilerplate, the intended monitor lacks the incentive or resource to read them, and the field's
    own conclusion is that enforcement rather than disclosure is what makes such regimes bind. The GRC
    practitioner literature reports the same pathology under the name "exception creep," with a standing
    remedy — mandatory expiry, non-automatic renewal, escalating approver seniority — that C2A2 has not
    adopted in any of the four cases.
    The compounding feature is that all four failures are *invisible in the artefact*. A window that is
    nullified, a hold that is abandoned, a budget that is fictional, and a flag that was withdrawn all look
    identical to a window in force, a hold under consideration, a budget respected, and a flag still live.
    Nothing in the current record distinguishes them, so the system cannot audit its own governance state.

  Literature basis:
    - Vaughan, D. (1996). *The Challenger Launch Decision*; normalization of deviance.
    - Comply-or-explain scholarship on boilerplate explanations and weak market-based enforcement
      (CLS Blue Sky Blog treatments; Seattle University Law Review study; Jiang et al. 2024, Journal of
      Accounting Research, on opportunistic use of the "explain" limb).
    - Anderson, C.J. (2003). "The Psychology of Doing Nothing." Psychological Bulletin 129(1), 139–167.
    - Bachrach, P. & Baratz, M.S. (1962). "Two Faces of Power." APSR; nondecision-making.
    - Staw, B.M. (1976). "Knee-deep in the big muddy." OBHP; escalation of commitment.
    - Federal Rules of Evidence, Rule 807 (Residual Exception) and its 2019 amendment — a documented
      natural experiment in an open-ended exception drifting beyond its intended rarity.
    - Wickens, C.D. et al. (2009). "False Alerts in Air Traffic Control Conflict Alerting System: Is There a
      'Cry Wolf' Effect?" Human Factors 51(4) — the mechanism by which unpriced false positives degrade
      the whole channel.
    - GRC practitioner consensus on exception registers and exception creep (non-peer-reviewed;
      convergent professional practice).

  Risk level: HIGH

  Recommendation:
    Treat these as one remediation, not four. The single intervention that addresses all of them is:
    every declared constraint and every lifecycle state must have (a) an expiry or a bound, (b) a recorded
    default outcome when the bound is reached, and (c) an emitted counter. Concretely:
      - 758: bound the exception clause with a per-run quota; log the invocation rate.
      - 762: mandatory expiry on holds; non-automatic renewal by an agent other than the hold's creator;
             publish register cardinality as a trend.
      - 764: two-tier budget (soft target, enforced hard ceiling); publish the overrun *distribution*, and
             re-fit the soft target to observed spend so it regains information content.
      - 833: add the missing WITHDRAWN terminal state to `provenance_protocol.md` and propagate it to every
             artefact in which the flag appears. This is the cheapest fix in the batch and the highest-value.
    Priority order by cost-to-fix against harm: 833 first (a lifecycle state, near-zero cost, stops a
    recurring budget leak and a live-accusation artefact defect), then 764 (a number and a ceiling), then
    762 (an expiry field), then 758 (a quota plus telemetry).

  ---

  FLAG 2 (CRITICAL) — Correlated readers: the pipeline's evidential warrant

  Affected items: PRESUMPTION-751 (primary); bears on PRESUMPTION-762, ASSUMPTION-943, and on this
  search itself

  Common vulnerability:
    PRESUMPTION-751 was flagged by 14b as bearing on the warrant of the pipeline searching it, and that
    flag is correct and understated. The literature found is unambiguous: Kim et al. (ICML 2025, 350+ models)
    report that when two models both err they select the same wrong answer 60% of the time, and that error
    correlation is *higher* for larger and more accurate models. Kohli (arXiv:2605.29800, 2026) finds a panel
    of nine frontier models drawn from seven different families is worth about two independent votes by Kish
    effective sample size, that panel accuracy falls 8–22 points short of the independent-voting ideal, that
    the best single judge matches or beats the panel in every condition, and that no aggregation method
    recovers more than 11% of the deficit even given the answers. Berg (1993) supplies the formal reason:
    positive inter-juror correlation monotonically degrades collective competence.
    Three consequences for C2A2, in ascending order of seriousness:
      (i)   Any artefact that reports "two readers concurred" as a confidence signal is overstating.
      (ii)  ASSUMPTION-943 was extracted on the strength of three reviewers stating a principle independently.
            Under this literature, independent statement by correlated reviewers is weak evidence, and the
            item's own note — "never tested" — becomes the operative fact rather than an aside.
      (iii) This 15a/15b split is an adversarial-role assignment over what may be the same substrate. Kohli
            finds that prompt variation, temperature and chain-of-thought do not restore independence.
            Role-splitting probably buys real but bounded decorrelation. Neither this document nor 15a's
            can certify its own independence, and 15c should not treat 15a/15b concordance as confirmation.

  Literature basis:
    - Kim, E., Garg, A., Peng, K. & Garg, N. (2025). "Correlated Errors in Large Language Models." ICML 2025;
      arXiv:2506.07962.
    - Kohli, G. (2026). "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels."
      arXiv:2605.29800.
    - Berg, S. (1993). "Condorcet's jury theorem, dependency among jurors." Social Choice and Welfare 10(1),
      87–95.
    - Wataoka, K., Takahashi, T. & Ri, R. (2024). "Self-Preference Bias in LLM-as-a-Judge." arXiv:2410.21819
      (NeurIPS 2024 Safe Generative AI Workshop) — agreement tracks perplexity/familiarity, not correctness.
    - Dietrich, F. & Spiekermann, K. "Jury Theorems." Stanford Encyclopedia of Philosophy.

  Risk level: CRITICAL

  Recommendation:
    Measure n_eff before relying on any concordance construct anywhere in C2A2. Build a human-adjudicated
    gold set of 100–200 items, run the reader pair, and compute Kish effective sample size against a
    Condorcet null exactly as Kohli does. Until that number exists:
      - do not cite reader agreement as evidence in any artefact;
      - treat disagreement, not agreement, as the informative event, and route it to escalation;
      - prefer one non-LLM check (deterministic lint, citation resolver, symbolic constraint) over a third
        LLM reader — Kohli's result is that more readers do not help;
      - re-read ASSUMPTION-943's provenance in this light: "three reviewers said so" is not independent
        corroboration, and the assumption should be treated as untested, which is what its own record says.
    15c should note that this flag is self-referential: it constrains how much weight to place on the very
    batch of documents it appears in.

  ---

  Cross-reference: the two flags interact. FLAG 2 says C2A2 cannot currently tell how much its own
  agreement signals are worth; FLAG 1 says C2A2 cannot currently tell which of its declared constraints are
  still in force. Together they describe a system whose self-model is not instrumented. Both remediations
  are instrumentation, not redesign, and both are cheap relative to the exposure.
