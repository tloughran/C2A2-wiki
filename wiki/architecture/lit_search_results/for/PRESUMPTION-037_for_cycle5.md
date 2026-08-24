SEARCH-FOR-PRESUMPTION-037:
  Date searched: 2026-08-23
  Cycle: 5 (15d monthly re-trigger; cohort 2026-07-05)
  Original item: PRESUMPTION-037
  Original statement: [inferred] "File-based handoff (Handoffs/latest.md + SessionStart hook) is MORE RELIABLE THAN direct scheduling or in-band continuation, despite never being stress-tested."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15a (cycle 5)]
    Original item: PRESUMPTION-037
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — an untested reliability *ordering* over three handoff mechanisms was being relied on without ever being stated
      15a: Searched for supporting literature (2026-08-23, cycle 5)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial (descriptive sub-claim: yes; ordinal sub-claim: no direct comparison found)

  Sources:
    1. Zylos Research. 2026-04-24. "Durable Execution for AI Agent Runtimes: Checkpointing, Replay, and Recovery." — Surveys the 2026 landscape (Temporal, Azure Durable Task, AWS Step Functions, Cloudflare Workflows, LangGraph/LangSmith). States the design rationale explicitly: durability comes from persisting state *outside application memory*, so that workflows survive process crashes, network partitions and redeployments. This is a direct, on-domain articulation of the qualitative ordering the presumption assumes — persisted artifact beats live-process state under crash.
    2. Applied Technology Index. 2026. "2026 Comparative Analysis: Durable Execution Infrastructure for Long-Running AI Agents." — A comparative survey across durable-execution platforms. Comparative in the descriptive sense (feature/architecture comparison); notably it is *not* a controlled reliability experiment, and I found no paired failure-rate data for persisted-artifact vs. direct-invocation handoff in it.
    3. "Atomix: Timely, Transactional Tool Use for Reliable Agentic Workflows." 2026. arXiv:2602.14849. — Argues for transactional/durable semantics around agent tool use as a reliability mechanism, i.e. the same directional claim: externalised, durable state is the reliability-bearing element. Preprint.
    4. "Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline." 2026. arXiv:2606.04315. — The closest thing to a head-to-head found: eight memory systems benchmarked against a plain agent-harness baseline. It compares *memory architectures*, not *handoff mechanisms*, so it does not test the comparands named in this presumption (direct scheduling, in-band continuation).
    5. Carried forward from cycle 0/1: Hohpe & Woolf 2003 "Enterprise Integration Patterns" (store-and-forward vs. direct invocation); Fisher 1935 on paired experimental design; Majors et al. 2022 "Observability Engineering" on per-link instrumentation as a precondition for comparative reliability claims.

  Strength of support: Weak-Moderate (unchanged; qualitative directional support strengthened, quantitative comparative support still absent)

  New since cycle 0/1: Yes, partially. New on-domain 2026 sources (durable-execution-for-agents surveys and the Atomix preprint) restate the qualitative ordering — persisted external state is more crash-tolerant than in-memory continuation — in the agent domain specifically rather than by analogy to enterprise integration. That is a modest strengthening of the *direction* of the ordinal claim. What has NOT changed, across five cycles: there is still no paired empirical comparison of file-based handoff against direct scheduling or in-band continuation with matched workloads and reported failure rates. Cycle 1's core finding stands.

  Summary: The presumption bundles two sub-claims and they continue to behave differently under search. The descriptive sub-claim ("file-based handoff is a durable, crash-tolerant mechanism") now has on-domain 2026 support from the durable-execution literature, which states the persist-outside-memory rationale explicitly for agent runtimes. The ordinal sub-claim ("more reliable *than* direct scheduling or in-band continuation") still rests on architectural reasoning rather than measurement: every source located argues the ordering from first principles about crash semantics, and none reports a paired trial against the named comparands. Note also that the ordering the literature supports is scoped to *crash/restart* failure modes; it says nothing about the failure mode C2A2 actually cares about here, which is whether a loaded payload is correctly acted on. On that dimension the ordering is untested in either direction.

  Caveats: (a) The durable-execution sources are vendor-adjacent grey literature with commercial incentive to favour durable-state products — publication bias is material here and I am flagging it rather than discounting the sources entirely. (b) Enterprise durable-execution engines differ from a single markdown file plus a startup hook in every property that matters for reliability (transactional writes, replay determinism, retry semantics); the analogy supports the direction but not the magnitude. (c) The ordinal claim's support weakens to nothing if the failure mode of interest is hook-non-firing or payload-misinterpretation rather than process crash, since the cited literature addresses only the latter.

  Search scope: Searched durable execution vs. in-memory continuation (2026), store-and-forward vs. direct invocation reliability, agentic workflow transactional tool use, agent memory system head-to-head benchmarks. Comprehensive for the "is there a head-to-head?" question; the answer is no. Preliminary on queueing-theory and message-broker reliability measurement literature, which was not searched this cycle.

  Recommendation: PARTIALLY-SUPPORTED

  NOVELTY-FLAG:
    Item: PRESUMPTION-037, ordinal sub-claim only ("more reliable than direct scheduling or in-band continuation")
    Searched: durable/persistent message passing vs. in-band continuation; store-and-forward vs. direct invocation reliability; paired empirical comparisons of handoff mechanisms; agent-domain durable execution comparisons (2026)
    Finding: Across five cycles and this cycle's on-domain 2026 sweep, no published head-to-head empirical comparison of persisted-artifact handoff against direct scheduling or in-band continuation, with matched workloads and reported failure rates, was located. The literature argues the ordering architecturally and never measures it.
    Implication: The ordinal sub-claim is not merely under-evidenced within C2A2 — it appears to be under-evidenced in the published literature generally. It cannot be resolved by further literature search; only a paired local test would move it.
    Recommended status: NOVEL (scoped strictly to the ordinal sub-claim; the descriptive sub-claim is well-attested and is NOT novel)
