SEARCH-FOR-ASSUMPTION-1228:
  Date searched: 2026-08-28
  Original item: ASSUMPTION-1228
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority Medium)
  Original statement: An index at 82% of a hard read limit requires a compaction strategy, and compaction
    carries a real cost — the loss of an accumulated known-traps record.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1228
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim; the underlying measurement was attempted and found out of mount, declared.
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Search scope: WebSearch, 2026-08-28, one dedicated query on context management and memory compaction for
    long-running LLM agents. Literature reached: LangChain's engineering write-up on context management for
    deep agents; a cluster of 2025-2026 arXiv papers on agent context compaction and eviction
    (2605.30785, 2509.25250, 2605.23296, 2606.11213, 2606.10209, 2602.22402); the JetBrains research blog.
    NOT COVERED and material: (i) the cache-replacement and working-set literature in systems, which is the
    mature analogue and would give the eviction-policy vocabulary; (ii) any study measuring downstream task
    degradation attributable specifically to losing a failure/known-traps record. All sources SNIPPET-ONLY.
    Search confidence: HIGH on the phenomenon, LOW on the specific cost claimed.

  Supporting evidence found: Yes

  Sources:
    1. LangChain, "Context Management for Deep Agents" [SNIPPET-ONLY]
       https://www.langchain.com/blog/context-management-for-deepagents —
       States the structural form of the problem: the context window is finite but the trajectory of work is
       not. Reports an observed autocompaction reducing 132k tokens of accumulated message state to 2.3k —
       a 98% reduction — "discarding the nuanced understanding that took an entire session to build."
    2. Anon., "Beyond Compaction: Structured Context Eviction for Long-Horizon Agents" (arXiv:2606.11213)
       [SNIPPET-ONLY; authors unverified] —
       Gives the two named limitations of summarisation-based compaction: lossiness is unpredictable
       because the summariser judges salience under its own constraints and need not match what the
       downstream agent will need; and structure is destroyed — explicit causal structure in the trajectory
       collapses into narrative, "erasing the provenance that would let the agent revisit its own reasoning."
       This is the assumption's cost claim, stated in the literature's own words.
    3. Anon., "Contextual Memory Virtualisation: DAG-Based State Management and Structurally Lossless
       Trimming for LLM Agents" (arXiv:2602.22402); "Parallel Context Compaction for Long-Horizon LLM Agent
       Serving" (arXiv:2605.23296) [SNIPPET-ONLY; authors unverified] —
       Establish that structurally-lossless trimming is an active research target precisely because naive
       compaction is not lossless; i.e. the cost the assumption names is the field's motivating problem.

  Strength of support: Strong on the mechanism; None on the 82% figure

  Summary: The assumption's substantive claim — that compaction of an accumulated record is lossy in an
    unpredictable, structure-destroying way, and that a known-traps record is exactly the kind of
    accumulated causal structure most at risk — is directly and repeatedly supported by current work on
    long-horizon agent memory. The loss is not a rounding error: one documented case reports 98% token
    reduction with the session's accumulated understanding among what was dropped. The field's response has
    been to seek *structurally lossless* trimming, which concedes the premise. Separately, and this is
    stated rather than smoothed over: nothing found bears on the 82% figure, which the queue entry itself
    records as unmeasured because the path was out of mount.

  Caveats: Nearly all sources are 2026 arXiv preprints with unverified authorship, read at snippet level;
    one is vendor engineering material with an obvious interest in the problem being real. The literature is
    about conversational trajectories, not a markdown index file, and the transfer is assumed.

  Recommendation: SUPPORTED
