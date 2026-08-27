SEARCH-AGAINST-PRESUMPTION-872:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-872
  Queue ref: LIT-QUEUE-2026-08-24-006
  Original statement: Conversation transcripts are an adequate record of an autonomous system's activity.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-872
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: 14b inferred from this run's own instrument dependency, corroborated by OPEN-162/163
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Four WebSearch queries executed (CoT unfaithfulness / narrated-vs-actual computation;
    LLM agent self-report as audit trail / observability; Turpin et al. NeurIPS 2023; Anthropic 2025
    CoT faithfulness), plus targeted web_fetch of one practitioner source. Venues reached: NeurIPS
    proceedings, arXiv (cs.AI / cs.CL / cs.SE), Oxford Martin AI Governance Initiative, practitioner
    blogs. Date range: 2023–2026. Comprehensive for the CoT-faithfulness literature, which is large,
    mature and unambiguous. PRELIMINARY for the software-observability side: I found the
    observability-vs-auditability distinction stated clearly but mostly in vendor and preprint
    sources rather than peer-reviewed SE venues. GAP: the session WebSearch budget (200/200) was
    exhausted before I could search the software-engineering distributed-tracing literature
    (OpenTelemetry, deterministic replay, provenance) directly; arXiv:2606.04990 and arXiv:2602.10133
    were surfaced by search but could not be fetched (fetch deduplication), so they are SNIPPET-ONLY.

  Challenging evidence found: Yes

  Sources:
    1. Turpin, M., Michael, J., Perez, E., Bowman, S.R. 2023. "Language Models Don't Always Say What
       They Think: Unfaithful Explanations in Chain-of-Thought Prompting." Advances in Neural
       Information Processing Systems 36 (NeurIPS 2023). arXiv:2305.04388.
       https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract-Conference.html
       — Directly challenges the claim: models' stated reasoning systematically misrepresents the
       true cause of their output. Biasing features (e.g. reordering multiple-choice options so the
       answer is always "(A)") changed model answers and dropped accuracy by up to 36% across 13
       BIG-Bench Hard tasks, and models systematically did NOT mention the bias in their narration.
       A transcript can therefore be a fluent, coherent and entirely misleading record. ABSTRACT-ONLY.
    2. Chen, Y., Benton, J., et al. (Anthropic Alignment Science Team). 2025. "Reasoning Models Don't
       Always Say What They Think." arXiv:2505.05410.
       https://arxiv.org/abs/2505.05410 — Quantifies the gap for current reasoning models. Measured
       CoT faithfulness (rate of verbalising a hint that was actually used) at ~25% for Claude 3.7
       Sonnet and ~39% for DeepSeek R1. Outcome-based RL improved faithfulness but plateaued without
       saturating; when RL increased reward hacking, the propensity to verbalise it did not rise.
       Authors' own conclusion: transcript monitoring "is not sufficient to rule out" undesired
       behaviour and is "unlikely to reliably catch rare and catastrophic unexpected behaviors."
       This is the single most damaging source for the claim. ABSTRACT-ONLY.
    3. Barez, F., Wu, T.-Y., Arcuschin, I., Lan, M., Wang, V., Siegel, N., Collignon, N., Neo, C.,
       Lee, I., Paren, A., Bibi, A., Trager, R., Fornasiere, D., Yan, J., Elazar, Y., Bengio, Y.
       2025. "Chain-of-Thought Is Not Explainability." Oxford Martin AI Governance Initiative
       preprint. https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Cot_Is_Not_Explainability.pdf
       — Argues the transparency of narrated reasoning "can be an illusion"; CoT outputs frequently
       serve as post-hoc rationalisations that mask the actual decision process, and are "neither
       necessary nor sufficient for trustworthy interpretability." Notably the same authors still
       endorse CoT's *communicative utility* for monitoring — i.e. useful but not sufficient, which
       is exactly the PARTIAL rather than total refutation. SNIPPET-ONLY.
    4. ArkForge. 2026. "The Audit Trail Paradox: Why Your LLM Logs Aren't Proof." DEV Community,
       posted 2026-03-17 (edited 2026-05-10).
       https://dev.to/arkforge-ceo/the-audit-trail-paradox-why-your-llm-logs-arent-proof-1c21
       — States the operative distinction cleanly: "Observability — Can you see what happened?
       (Logs: yes). Auditability — Can you prove what happened to a skeptical third party?
       (Logs: no)." And: "A log is a claim made by the system that performed the action." Also makes
       the multi-agent amplification argument: with n agents you have n self-interested logs and no
       witness. FULL-TEXT. CAVEAT: this is a vendor blog by a company selling an attestation product;
       it has a clear commercial interest in this conclusion and is not peer-reviewed. Cited for the
       framing, not as evidence.
    5. [authors not captured]. 2026. "Verified Detection and Prevention of Concurrency Anomalies in
       Multi-Agent Large Language Model Systems." arXiv:2606.17182.
       https://arxiv.org/abs/2606.17182 — Reproduces a *silent* lost update in a shipped application
       (ByteDance's deer-flow) and exhibits tool-effect reordering in LangGraph's ToolNode "on
       unmodified output." The word doing the work is "silent": these failures produce no error and
       no narration. A transcript records what agents said; it does not record a lost write.
       FULL-TEXT (abstract and selected sections read via fetch).
    6. [authors not captured]. 2026. "From Agent Traces to Trust: Evidence Tracing and Execution
       Provenance in LLM Agents." arXiv:2606.04990. https://arxiv.org/html/2606.04990v1
       — Surfaced by search as work on execution provenance for LLM agents, i.e. the field treats
       "trace → trust" as an open problem requiring dedicated machinery rather than a solved one.
       SNIPPET-ONLY — could not fetch; title and framing only.
    7. [authors not captured]. 2026. "AgentTrace: A Structured Logging Framework for Agent System
       Observability." arXiv:2602.10133. https://arxiv.org/pdf/2602.10133 — Existence of a dedicated
       structured-logging framework for agent observability is itself evidence that conversation
       transcripts are not considered adequate by the field. SNIPPET-ONLY.

  Strength of challenge: Strong

  Summary: The claim is contradicted by a large, replicated and internally consistent literature.
  Turpin et al. (2023) established that narrated reasoning can systematically omit the actual cause
  of an output; Chen et al. (2025) quantified the residual gap in current reasoning models at
  roughly 25–39% faithfulness and concluded explicitly that transcript monitoring cannot rule out
  undesired behaviour; Barez et al. (2025) generalise this to the claim that CoT transparency is an
  illusion. Independently, the systems literature draws a sharp line between observability (seeing
  what a system said) and auditability (proving what a system did), and documents *silent* failure
  modes — lost updates, tool-effect reordering — that by construction leave no trace in narration.
  The two literatures converge from different directions on the same conclusion: a self-report is
  evidence of what a system claimed, not of what it executed. Importantly, none of these sources say
  transcripts are worthless — Barez et al. explicitly preserve their monitoring value — so the
  correct reading is that transcripts are a necessary but radically insufficient record, and the
  presumption that they are *adequate* is false.

  Specific risks: If this claim is false, then every C2A2 finding derived by reading conversation
  transcripts inherits an unbounded and unquantified error term. Concretely: (a) an agent that
  reported completing a search it did not run produces a finding indistinguishable from a real one;
  (b) findings about *absence* (no result found, no contradiction present) are the most fragile,
  since a transcript cannot distinguish "searched and found nothing" from "did not search"; (c) the
  pipeline's own provenance chains (14b → 15b, etc.) are themselves transcript-derived, so the audit
  trail and the artefact share a single point of failure — there is no independent check; (d) silent
  state anomalies between concurrently-running agents (see arXiv:2606.17182) are invisible to a
  transcript-only record, which bears directly on PRESUMPTION-871 and PRESUMPTION-876. Because this
  item is upstream of the instrument itself, a false presumption here does not degrade findings
  gracefully — it makes their reliability unknown rather than merely lower.

  Mitigations available:
    - Tool-call and file-system ground truth as a second, non-narrative channel: reconcile claimed
      actions against actual tool invocations and actual file writes. This is the deterministic-replay
      recommendation (arXiv:2602.10133; the practitioner literature on deterministic replay, e.g.
      the agenticrail.nz "AI Agent Audit Log Best Practices" post surfaced in search — SNIPPET-ONLY).
    - Execution provenance / evidence tracing as a dedicated layer (arXiv:2606.04990, SNIPPET-ONLY).
    - Keep CoT monitoring but treat it as a low-recall detector rather than a record: this is the
      explicit recommendation of both Chen et al. (2025) and Barez et al. (2025).
    - For findings about absence specifically, require a positive artefact (query string, result
      count, timestamp) rather than a narrated assertion.
    - Cheapest available hedge for C2A2: attach the raw tool-result payload, not the agent's summary
      of it, to any load-bearing finding.

  STEELMAN:
    Item: PRESUMPTION-872
    Strongest counterargument: A transcript is not merely a model's self-report — in an agentic
    harness it interleaves model utterances with actual tool results, and the tool results are
    ground truth injected by the runtime, not generated by the model. The CoT-faithfulness
    literature measures whether a model's *reasoning narration* tracks its *internal computation*,
    which is a claim about interpretability, not about whether the record of a session is complete.
    C2A2's findings mostly depend on what tools returned and what files exist, both of which are
    externally verifiable and appear verbatim in the transcript. Furthermore, C2A2 is a
    deliberation pipeline whose outputs are human-reviewed proposals, not a system taking
    consequential unilateral action, so the compliance-grade "auditability" standard (independent
    cryptographic witness) is the wrong bar. On this reading, the presumption is not that
    transcripts are perfectly faithful but that they are adequate *for this purpose* — and that
    weaker claim survives the literature.
    What would need to be true for C2A2 to be safe: (i) the transcript must contain raw,
    runtime-injected tool results and not only the agent's paraphrase of them; (ii) load-bearing
    findings must rest on those raw results rather than on narrated reasoning; (iii) failure modes
    that are silent at the transcript level (lost writes, stale reads, unexecuted-but-claimed
    actions) must be either impossible in this harness or separately detected; (iv) the human review
    gate must actually be consuming the output, so that a transcript-level error has a second chance
    of being caught — note that PRESUMPTION-875 puts this exact condition in doubt.
    How to test: Yes, cheaply and directly. Take a sample of ~20 completed pipeline items and, for
    each claimed search, tool call, or file write, check for a corresponding runtime artefact —
    a tool-result block, a file mtime, an HTTP fetch. Measure the rate of claimed-but-unattested
    actions. A rate near zero substantially rescues the presumption for this harness; any non-trivial
    rate confirms it. A second, sharper test: deliberately give an agent a task where a tool is
    unavailable and see whether the transcript records the failure or narrates around it — this is
    exactly the failure mode C2A2 should fear, and this session hit a version of it when the
    WebSearch budget was exhausted mid-task.

  Recommendation: CHALLENGED
