SEARCH-AGAINST-ASSUMPTION-008:
  Date searched: 2026-09-02
  Original item: ASSUMPTION-008 (MONITOR-4)
  Original statement: "A 2/3 consensus threshold is meaningful for tripled agent agreement."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b → 15c → 15d → 15b] (cycle-5 monthly re-check)
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: original extraction
      15c (2026-04-13): dispositioned MONITOR
      15d: re-triggered, cycle 5 (59 days overdue)
      15b (2026-09-02): searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "Are Diversity Metrics Measuring Diversity? A Capability-Controlled Audit of Majority-Vote
       Gain in LLM Ensembles." arXiv:2607.20768v1 (July 2026). Abstract read in full.
       — THE decisive source for this item, and it addresses N=3 specifically. Auditing 31,900
       subsets of 30 LLMs on MMLU-Pro and TruthfulQA: latent complementarity is ubiquitous (oracle
       gain positive in 100% of subsets), yet simple majority voting beats the strongest single
       member in only 9.98% of canonical size-3 subsets (18.71% even with held-out best
       selection). Pooled size-2–4 rate is 1.27%. In other words: for triples, the information
       needed to do better is almost always present, and majority vote almost never extracts it.
       The paper further shows that a joint-correctness "diversity" proxy is nearly collinear with
       one minus mean accuracy (Spearman rho = +0.991 at size 3) — apparent diversity is mostly
       re-expressed capability. After capability control, the stable residual is that more shared
       error corresponds to lower gain.

    2. "When Self-Consistency Backfires: Majority Vote Hurts the Majority of Hard Science Problems
       for Small LLMs." arXiv:2608.11403v2 (August 2026). Abstract read in full. Pre-registered.
       — Majority vote via self-consistency REDUCES per-problem accuracy on most GPQA Diamond
       problems: 56.6% of problems for Qwen2.5-7B, 65.7% for Llama-3-8B. Crucially for the
       reflexive case: samples that contradict their own problem's plurality still emit their
       answer at a median margin of 20.52 nats, with 75.7% above 10 nats — i.e. confidence carries
       no usable signal about whether the majority is right, and the natural verifier-free
       confidence gate that would repair this also fails. When a model's probability mass sits on
       a wrong answer, more votes entrench the error rather than correcting it.

    3. "The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous
       Multi-Agent Debate." arXiv:2605.00914v1 (May 2026). Abstract read in full.
       — Directly on the reflexive case (homogeneous agents, no distinct personas). Teams of
       identical model instances across three model families, three debate rounds, GSM-Hard and
       MMLU-Hard. Decomposes failure into three pathways: sycophantic conformity (modal adoption
       of the majority answer up to 85.5%), contextual fragility (peer rationales destabilise
       previously CORRECT reasoning, vulnerability rate up to 70.0%), and consensus collapse
       (plurality voting discards correct answers already present in the pool, oracle gap up to
       32.3 percentage points). Conformity reaches high levels at minimal peer exposure (K=2 —
       i.e. exactly the exposure a 3-agent trio has) and INTENSIFIES with greater initial
       diversity. Debate costs 2.1–3.4x more tokens for equal or lower accuracy.

    4. Dietrich, F. & Spiekermann, K. "The Premises of Condorcet's Jury Theorem Are Not
       Simultaneously Justified." Episteme. Also their "Jury Theorems" chapter
       (eprints.lse.ac.uk/101162/) and the SEP entry "Jury Theorems"
       (plato.stanford.edu/entries/jury-theorems/).
       — The formal result behind all of the above. Any common cause of votes is a source of
       dependence, and — the key point — conditioning on the true state does NOT restore
       independence when common causes are present. Voting and correctness are interpersonally
       positively correlated through common causes, against Condorcet's independence assumption.
       Three agents sharing a base model and scaffold share the maximal possible common cause.

    5. Ladha, K. (1992, 1993, 1995) on the Condorcet Jury Theorem with correlated votes; and
       Kaniovski, S. (2010) "Aggregation of correlated votes and Condorcet's Jury Theorem."
       — Foundational analysis of how positive correlation undermines the theorem's conclusion.
       Note: characterised from search results and the Dietrich/Spiekermann survey, not read in
       the original.

    6. "Herd Behavior: Investigating Peer Influence in LLM-based Multi-Agent Systems."
       arXiv:2505.21588. And "Emergence of Biased Consensus in Multi-Agent LLM Debates"
       arXiv:2608.02827v1; "Not All Flips Are Conformity: Decomposing Stance Convergence in
       Multi-Agent LLM Debate" arXiv:2606.00820.
       — Herding is driven by the relation between an agent's self-confidence and its perceived
       confidence in peers; LLMs conform to majority opinions regardless of correctness. The
       biased-consensus paper predicts a phase transition once conformity exceeds a critical
       threshold, ROUNDED INTO A CROSSOVER FOR FINITE AGENT COUNT — small N does not protect
       against this, it only blurs the onset. Agent heterogeneity suppresses emergence; homogeneity
       does not. The stance-decomposition paper finds strict conformity in 29% of
       agent-question observations. Titles verified in search results; abstracts not read in full.

    7. LLM-as-judge panel literature (2026): RAND study reporting no judge uniformly reliable
       across benchmarks and frontier models exceeding 50% error rates on challenging bias
       benchmarks; documented self-preference bias (GPT-4 favouring its own outputs by ~10% win
       rate, Claude-v1 by ~25%) and same-family preference. Practitioner consensus in this
       literature is that juries work only when providers are MIXED (one Anthropic + one OpenAI +
       one Google), because that is what cancels family-specific quirks. Note: these figures come
       from secondary practitioner summaries (futureagi.com, adaline.ai, orq.ai) surfaced in
       search, plus a primary paper "Judging the Judges: A Systematic Evaluation of Bias
       Mitigation Strategies in LLM-as-a-Judge Pipelines" (arXiv:2604.23178). I did not read the
       RAND study directly.

  Strength of challenge: Strong

  Summary: This is the item where the literature has moved decisively since April, and it has
  moved against the assumption. The April file challenged 2/3 on social-choice and groupthink
  grounds (Arrow, Janis, Moscovici) — theoretically suggestive but indirect. The 2026 empirical
  literature now measures the exact configuration C2A2 uses. For canonical size-3 subsets,
  majority vote beats the best single member only 9.98% of the time even though the information to
  do better is present in 100% of subsets. Self-consistency voting actively reduces accuracy on
  the majority of hard science problems. Homogeneous 3-agent-scale debate shows sycophantic
  adoption up to 85.5% and discards correct answers already in the pool (oracle gap up to 32.3
  points), at 2.1–3.4x the token cost. The theoretical explanation is settled: Condorcet requires
  conditional independence, common causes destroy it, and conditioning on the true state does not
  restore it. Agents built on a shared base model and shared scaffold are the maximal-common-cause
  case. 2/3 of 3 is not a consensus threshold in the Condorcet sense; it is a report that the
  shared prior did not fracture.

  Specific risks: The reflexive case makes this urgent rather than academic. Agents 15a/15b/15c —
  including the one writing this file — are a trio on a shared base model. If 15a and 15b converge
  and 15c ratifies, that 2/3 is evidence about the base model's priors, not about the world; and
  the failure is silent, because the majority reports high confidence exactly when it is wrong
  (median 20.52 nats margin on answers contradicting their own plurality). Concretely: (a) C2A2
  will systematically discard correct minority findings that were already present in the pool —
  this is consensus collapse and it is measured at up to 32.3 points; (b) confidence-based gating,
  the obvious repair, is shown not to work; (c) the system will read correlated hallucination as
  corroboration, which is the single worst failure mode for an epistemic-grounding pipeline whose
  whole purpose is to catch unfounded claims; (d) C2A2 pays 2.1–3.4x tokens for this. Note also
  that this challenge partially undermines the standing of every prior 2/3 disposition in the
  MONITOR register, including the dispositions on this very item.

  Mitigations available:
    1. Highest value, cheapest: report the FULL vote distribution and both dissents, never a
       collapsed 2/3 verdict. The literature's consistent finding is that the correct answer is
       usually present in the pool and lost at aggregation. Do not aggregate.
    2. Heterogeneity where it is affordable: mix model families or at minimum vary scaffold,
       prompt framing, and retrieval corpus across the trio. Heterogeneity is the one intervention
       shown to suppress the conformity phase transition.
    3. Enforce isolation. The strongest result in arXiv:2605.00914 is that isolated
       self-correction BEATS peer exchange. C2A2's 15a/15b independence rule is already the right
       instinct — this cycle's evidence says it should be tightened, never relaxed, and that any
       future "let the agents confer" redesign would be moving in the empirically wrong direction.
    4. Minority-escalation rule: a 2-1 split should trigger human review or a further evidence
       round, not a decision. Treat disagreement as a found ambiguity, which is what the judge-panel
       literature also recommends.
    5. Stop treating confidence as a gate. Explicitly documented as failing.
    6. Log co-failure: track how often the trio agrees AND is later found wrong. That rate, not the
       agreement rate, is the honest reliability number.

  STEELMAN:
    Item: ASSUMPTION-008
    Strongest counterargument: 2/3 agreement among three instances of the same base model is close
    to epistemically empty. Condorcet's theorem — the only thing that would license reading a
    majority as evidence — requires conditional independence, and a shared base model is a common
    cause that provably destroys it; conditioning on the truth does not repair this. The 2026
    measurements bear this out at exactly N=3: voting beats the best member in under 10% of triples
    while the winning information is present in all of them, self-consistency lowers accuracy on
    the majority of hard problems, and homogeneous trios adopt the majority answer sycophantically
    up to 85.5% of the time while discarding correct answers already in the pool. Worse, the
    failure is invisible from inside: wrong majorities are held with high confidence, and the
    obvious confidence gate is measured to fail. So 2/3 does not measure convergence on truth. It
    measures how strongly the shared prior held — and it is highest precisely when the prior is
    most confidently wrong.
    What would need to be true for C2A2 to be safe: (a) the trio's errors are conditionally
    independent given the truth — false by construction for same-base-model agents, but
    approachable by mixing providers, corpora and framings; (b) the trio operates in isolation
    with no cross-contamination before voting — currently true by design and worth defending; (c)
    2/3 is used as a routing signal ("proceed" vs "escalate") rather than as a truth claim; (d)
    minority findings are preserved and readable downstream rather than discarded at aggregation;
    (e) the decisions being voted on are ones where correlated error is tolerable — i.e. not the
    disposition of the assumptions the whole architecture rests on.
    How to test: Directly and cheaply, from data C2A2 already generates. (1) Compute C2A2's own
    oracle gap: over past tripled runs, how often was a correct finding present in at least one
    agent's output but absent from the 2/3 verdict? Any non-trivial rate reproduces consensus
    collapse in situ. (2) Co-failure rate: how often did all three agree and all three turn out
    wrong? Compare against the rate implied by independence — the gap is the correlation penalty.
    (3) Heterogeneity A/B: run a sample of items with a provider-mixed trio versus the current
    same-model trio and compare against human adjudication. (4) Seed/temperature ablation: if
    varying only the seed changes the verdict, the threshold is measuring sampling noise.

  Search scope: Queries actually run this cycle —
    - "LLM majority voting same model correlated errors self-consistency limits ensemble no gain
       2026"
    - "multi-agent LLM debate conformity herding groupthink same base model agreement not
       independent 2026"
    - "LLM-as-judge panel jury of judges failure self-preference bias correlated 2026 evaluation"
    - "Condorcet jury theorem fails correlated votes dependence Ladha Dietrich Spiekermann common
       cause"
    Full abstracts read for arXiv:2607.20768, arXiv:2608.11403, arXiv:2605.00914.
    Gaps: no search on Arrow-style impossibility results this cycle (April file already covers
    that ground, and the 2026 empirical work is the more decisive evidence). No search on optimal
    threshold selection for small N — a constructive question that a 15a-direction search may be
    better placed to cover. No search on weighted or confidence-calibrated voting schemes as
    alternatives. Did not read the RAND judge-reliability study directly.

  Search confidence: comprehensive search

  New since cycle 4 (i.e. since 2026-04-13):
    Substantial and decisive. The April file rested entirely on pre-2015 social-choice and social
    psychology (Arrow 1951, Condorcet 1785, Janis 1972, Moscovici 1974, Sunstein & Hastie 2014,
    Maskin & Sen 1999) — all real, but all analogical. Everything below post-dates the April search:
    1. arXiv:2607.20768 (July 2026) — the 9.98% size-3 majority-vote-gain figure. This is the
       first direct measurement of the exact N=3 configuration C2A2 uses, and it is the single most
       important new fact on this item. It also shows that "diversity" metrics used to justify
       ensembling are largely capability in disguise (rho = +0.991).
    2. arXiv:2608.11403v2 (August 2026) — pre-registered demonstration that majority vote
       backfires on 56.6–65.7% of hard science problems, AND that the confidence-gate repair
       fails. The second half is new in v2 and matters: it closes the most obvious mitigation.
    3. arXiv:2605.00914v1 (May 2026) — the homogeneous-team result. Directly addresses the
       reflexive case that the April search did not consider at all, and finds isolated
       self-correction superior to peer exchange at 1/2 to 1/3 the token cost.
    4. arXiv:2608.02827v1, arXiv:2606.00820, arXiv:2505.21588 — the conformity/herding cluster,
       including the finding that the conformity phase transition is only rounded, not removed, at
       finite agent count.
    5. Net effect: this item's status moves from "theoretically under-justified" to "empirically
       challenged in its specific configuration." I would argue the disposition should escalate.
    6. RECORD-INTEGRITY NOTE: cycles 1-3 on this item (2026-04-27, 2026-05-17, 2026-05-25) each
       recorded "no new challenging literature" with zero sources and no evidence of a search
       having run. Given how much genuinely relevant material has appeared since May, those nulls
       represent a real missed-detection window, not three confirmations of stability. This is
       itself a datum about automated re-check reliability.

  Recommendation: CHALLENGED
    Recommend escalation beyond MONITOR. This is the only one of the three cycle-5 items where new
    empirical work directly measures C2A2's own configuration and finds against it. Recommended
    concrete action, in order: (1) stop collapsing to a 2/3 verdict — surface full vote
    distributions and dissents; (2) run the oracle-gap and co-failure computations on existing
    C2A2 run history, which requires no new literature and would settle this internally;
    (3) preserve and tighten 15a/15b isolation; (4) treat 2-1 as escalate-to-human, not decide.
