SEARCH-AGAINST-PRESUMPTION-871:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-871
  Queue ref: LIT-QUEUE-2026-08-24-008
  Original statement: Contradictions between independent agents' reports will be surfaced without a
    dedicated reconciliation mechanism.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-871
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: 14b inferred from three same-day incompatible reports of one artifact's freshness, none
           referring to another
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: One WebSearch query executed (multi-agent LLM inconsistency detection / explicit
    verifier / arbiter / contradiction), followed by web_fetch of three of the returned papers to
    full text. Venues reached: arXiv (cs.AI, cs.MA, cs.SE, cs.LO), ScienceDirect, USPTO. Date range:
    2025–2026. COMPREHENSIVE for the 2026 multi-agent-verification literature, which is unusually
    well-aligned with this exact question. GAP: the WebSearch budget (200/200) was exhausted before
    I could search the classical distributed-systems side (Byzantine agreement, causal consistency,
    conflict detection in CRDTs) which would likely strengthen the challenge further; the
    concurrency-anomaly paper below reaches that literature by analogy and is a partial substitute.

  Challenging evidence found: Yes

  Sources:
    1. [Authors not captured.] 2026. "The Arbiter Agent: Continually Monitoring Multi-Agent
       Conversations to Detect Emergent Misalignment." arXiv:2606.10747.
       https://arxiv.org/html/2606.10747 — Directly on point. Premise: "While individual agents may
       appear well-aligned when tested on their own, problems can arise from how they interact with
       one another." The paper's entire contribution is a *dedicated* monitoring agent with an
       inspection budget that can wait, question a participant, examine system prompts or reasoning
       traces, and log concerning behaviour. Result: the Arbiter "reliably detects misaligned agents
       well before the end of the conversation, with active inspection tools improving both detection
       accuracy and speed" — i.e. detection is a function of a dedicated mechanism's capability, not
       something the conversation produces on its own. Their conclusion: "overseeing multi-agent
       systems may require treating the auditor as an active participant in the process." That is the
       negation of the presumption. FULL-TEXT (abstract read via fetch).
    2. [Authors not captured.] 2026. "Verified Detection and Prevention of Concurrency Anomalies in
       Multi-Agent Large Language Model Systems." arXiv:2606.17182.
       https://arxiv.org/abs/2606.17182 — Formalises four anomalies in TLA+ (stale-generation,
       phantom-tool, causal-cascade, tool-effect reordering) as structural analogues of classical
       database isolation anomalies, each with a model-checked counter-example, and proves detectors
       sound and complete against the specifications (274 Verus obligations). Two findings damage the
       presumption directly. (a) The real-LLM pilot (1,800 token-instrumented sessions across gpt-4o
       and Claude Sonnet 4.5) reports stale-generation at 1%, 35% and 100% across plan-execute,
       triage and edit-review workloads — the contradiction rate is workload-dependent and can reach
       total. (b) They reproduce a *silent* lost update in a shipped application (ByteDance's
       deer-flow) and exhibit tool-effect reordering in LangGraph's ToolNode "on unmodified output."
       Silent means: the inconsistency existed and nothing surfaced it. Prevention required an
       explicit isolation level; costs were bounded (~8% tokens for snapshot isolation, 1.6–2.3x for
       pessimistic locking) — "not the order-of-magnitude penalty commonly assumed." FULL-TEXT
       (abstract and §1 contributions read via fetch).
    3. [Authors not captured.] 2026. "Delayed Verification Destabilizes Multi-Agent LLM Belief:
       Instability Thresholds and Optimal Corrector Placement." arXiv:2606.27409.
       https://arxiv.org/html/2606.27409v1 — Even stronger: not only is a dedicated mechanism needed,
       its *placement and latency* matter. "Verification, however, has latency. A verifier reads a
       claim, retrieves evidence, and returns a correction only after several interaction steps;
       meanwhile the unverified claim has already propagated." They note that factuality in
       multi-agent settings "is no longer a property of one output and becomes a dynamic process:
       claims are exchanged, revised, and reused as context, so an unsupported claim from one agent
       can be amplified by others," and ask whether delayed verification can itself destabilise the
       factuality it protects. FULL-TEXT (§1 read via fetch).
    4. Zhang et al. "Hallucination snowballing" — cited within arXiv:2606.27409 [ref 7]: once an LLM
       commits to a wrong answer it generates further false claims to justify it, "even when it can
       separately recognize them as wrong." CITED-WITHIN (I did not retrieve the primary source;
       full citation details unverified).
    5. [Authors not captured.] 2026. "Debating to verify: A robust and explainable multi-agent LLM
       system for fact-checking." ScienceDirect, S2405959526000883.
       https://www.sciencedirect.com/science/article/pii/S2405959526000883 — Uses structured
       adversarial debate as the reconciliation mechanism. Cited as further evidence that the field
       builds explicit machinery for this rather than relying on emergence. SNIPPET-ONLY.

  Strength of challenge: Strong

  Summary: The 2026 multi-agent literature converges on the opposite of this presumption. Three
  independent papers — one on active misalignment monitoring, one on formally verified concurrency
  anomaly detection, one on verifier placement dynamics — all take as their premise that
  inconsistency between agents is *not* self-surfacing and all contribute a dedicated mechanism to
  make it visible. The concurrency paper is the most damaging because it supplies a mechanism for
  why: agents share state through memory stores and registries via long-running read-generate-write
  operations, and a read that has gone stale produces a confidently-written contradiction with no
  error signal. Its measured stale-generation rate reached 100% in an edit-review workload, and it
  reproduces a *silent* lost update in production software. The delayed-verification paper adds that
  even when a reconciliation mechanism exists, latency lets contradictions propagate and be amplified
  before correction arrives — so "no mechanism" is not merely suboptimal, it is the worst case on a
  spectrum where even good mechanisms struggle. The triggering observation in the brief — three
  same-day incompatible reports of one artefact's freshness, none referring to another — is a textbook
  instance of exactly this failure mode, and matches the stale-generation anomaly precisely.

  Specific risks: If contradictions are not self-surfacing, C2A2 has no idea what its internal
  disagreement rate is. Concretely: (a) incompatible reports coexist in the corpus indefinitely, and
  whichever is read last or read by the most downstream consumer silently wins — there is no
  arbitration, only recency; (b) per the snowballing result, an agent that has committed to a wrong
  state report will generate supporting detail for it, so contradictions get *more* plausible over
  time rather than more obviously broken; (c) the two-agent for/against design that produced this
  very file depends on divergence being noticed — if 15a and 15b return incompatible characterisations
  of the same literature and nothing reconciles them, the design's central benefit is lost; (d)
  detection depends on the reconciler having tools: the Arbiter paper found active inspection
  outperformed passive observation, so a reconciler that only reads final reports will be weaker than
  one that can query agents; (e) the presumption interacts multiplicatively with PRESUMPTION-872 —
  if the only record is the transcript, and the transcript does not surface silent state anomalies,
  then even a dedicated reconciler reading transcripts will miss the concurrency class of
  contradiction.

  Mitigations available:
    - A dedicated arbiter/monitor agent with an inspection budget and *active* tools (ability to
      question participants and read system prompts/traces), not passive observation
      (arXiv:2606.10747).
    - An explicit isolation level over shared state, with sound-and-complete detectors; measured
      overhead is bounded — ~8% tokens for snapshot isolation, ≤1.6x (gpt-4o) / ≤2.3x (Claude)
      for pessimistic locking (arXiv:2606.17182). This is the strongest available mitigation because
      it is verified rather than heuristic.
    - Attention to corrector *placement and dosing*, not just presence — delayed verification can
      itself destabilise (arXiv:2606.27409).
    - Structured adversarial debate as a reconciliation format (ScienceDirect S2405959526000883).
    - Cheapest C2A2-specific hedge: require every state report to carry an observation timestamp,
      which converts an apparent contradiction into an ordered sequence — this is exactly what 14a's
      resolution did, and is the same fix as PRESUMPTION-876.

  STEELMAN:
    Item: PRESUMPTION-871
    Strongest counterargument: The cited literature studies agents that interact *concurrently* over
    *mutable shared state* — memory stores, vector indices, tool registries — where a stale read
    genuinely produces an unresolvable conflict. C2A2's agents may not have that topology. If agents
    write to distinct, non-overlapping files and their outputs are later read together by a single
    downstream consumer, then contradictions are surfaced by construction: the consumer sees both
    reports side by side, and a competent reader notices they disagree. On this reading the
    "mechanism" is not absent, it is the human or synthesising agent at the join point, and the
    three-way freshness contradiction cited by 14b actually supports this — it *was* noticed, and
    14a *did* resolve it. The presumption might then be not that contradictions self-surface but that
    the pipeline's fan-in structure surfaces them, which is a different and more defensible claim.
    What would need to be true for C2A2 to be safe: (i) every set of potentially-contradictory
    reports must actually reach a common consumer — no report may terminate in an unread queue
    (PRESUMPTION-875 threatens this directly); (ii) that consumer must have both reports in context
    simultaneously, not sequentially across sessions; (iii) reports must be comparable — carrying
    timestamps, scope statements and confidence, otherwise apparent contradictions are
    indistinguishable from different-question answers; (iv) the consumer must be incentivised to
    flag disagreement rather than synthesise it away, which is a real risk when the synthesis step
    is itself an LLM asked to produce a coherent summary.
    How to test: Yes. Inject a known contradiction: have two agents report incompatible facts about
    the same artefact and measure whether the downstream synthesis flags it, silently picks one, or
    produces a blended non-answer. Run it at several fan-in depths. Separately, audit the existing
    corpus for latent contradictions — search for multiple assertions about the same artefact's state
    and count how many pairs are incompatible and how many were ever flagged. The ratio is the
    pipeline's contradiction-detection recall, and it is currently unknown.

  Recommendation: CHALLENGED
