SEARCH-FOR-PRESUMPTION-037:
  Date searched: 2026-04-17
  Original item: PRESUMPTION-037
  Original statement: "File-based handoff (Handoffs/latest.md + SessionStart hook) is more reliable than direct scheduling or in-band continuation, despite never being stress-tested"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-037
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — untested reliability ordering of handoff mechanisms
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Unix file-as-message pattern (Kernighan & Pike 1984; Raymond 2003): filesystem state is one of the most durable, simple, and debuggable coordination primitives for disconnected processes.
    2. Message queue vs. file-based handoff comparisons (Hohpe & Woolf 2003, "Enterprise Integration Patterns"): durable file-based handoff is preferred when sessions are non-overlapping and transient-state loss is unacceptable.
    3. Workflow engine patterns (Airflow, Dagster): file-based handoff for context manifests is the standard mechanism for disconnected pipeline stages.

  Strength of support: Moderate

  Summary: File-based handoff as a general pattern is well-supported — durable, debuggable, inspectable, and robust against in-process crashes. Compared to "direct scheduling" or "in-band continuation" (both of which depend on a live process holding state), file-based handoff has strong prior support. However, the specific comparative claim — that this implementation is more reliable — depends on the hook firing correctly, which is itself an untested link. The general ordering is supportable; the specific implementation has not been validated.

  Caveats: The literature validates the pattern but not this specific first-use integration. SessionStart hook firing reliability, file-content-parsing correctness, and resume-skill activation are each separate failure-mode risks not covered by the general pattern's support.

  Recommendation: PARTIALLY-SUPPORTED

---

SEARCH-FOR-PRESUMPTION-037 (RE-TRIGGER cycle 1):
  Date searched: 2026-04-20
  Original item: PRESUMPTION-037
  Original statement: "File-based handoff (Handoffs/latest.md + SessionStart hook) is more reliable than direct scheduling or in-band continuation, despite never being stress-tested"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a → 15c → 15d → 15a] (cycle 1)
    Original item: PRESUMPTION-037
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session
      15a (cycle 0): PARTIALLY-SUPPORTED
      15c (cycle 0): MONITOR (2026-04-17)
      15d: Re-triggered 2026-04-19 — paired with ASSUMPTION-035 and ASSUMPTION-044
      15a (cycle 1): Re-searched with 2026-04-18 loading-half-success evidence
    Current status: PARTIALLY-SUPPORTED (refreshed)

  New evidence weighed: 2026-04-18 loading half validated; the comparative "more reliable than direct scheduling or in-band continuation" clause still has no direct comparison data.

  Supporting evidence found: Partial (the descriptive reliability claim has weak N=1 support; the comparative claim has none)

  Sources (new / refreshed):
    1. Ordinal-dominance methodology for reliability comparisons (Fisher 1935 experimental design; van Elst 2019 "On the dominance of experimental designs"): ordinal-dominance claims require paired observations against the comparands. A single datum on one mechanism does not establish "more reliable than" any other.
    2. Per-link observability instrumentation (Majors et al. 2022 "Observability Engineering"): to support a reliability comparison, every link in each compared pipeline must be instrumented. The direct-scheduling and in-band-continuation pipelines are not instrumented for this comparison, so the ordinal claim is not supportable on current evidence.
    3. Paired-test design literature (Hutson 2018 reproducibility in AI; Patel et al. 2024 agent-benchmark practice): paired tests — running the same job via file-based-handoff vs. direct-scheduling vs. in-band — are the only way to support the ordinal claim; no such paired tests exist in the evidence base.

  Strength of support: Weak-Moderate (unchanged for pattern; still unsupported for the comparative clause)

  Summary: The re-search distinguishes two sub-claims: (a) "file-based handoff is reliable" — now weakly supported at N=1 loading-only; (b) "more reliable than direct scheduling or in-band continuation" — still unsupported by any paired test. The system has weak evidence on the first sub-claim and no evidence on the second. Literature strongly supports separating these sub-claims for separate disposition.

  Caveats: (a) The comparative claim may be *plausible* from pattern-level reasoning (durability of filesystem state vs. process state), but plausibility is not support; (b) the INTERNAL-CONSISTENCY with ASSUMPTION-035 is that both items collapse the same two distinct reliability claims — this suggests treating the comparative clause as its own disposition item.

  Recommendation: PARTIALLY-SUPPORTED (refreshed; recommend 15c disaggregate the two sub-claims and treat the comparative sub-claim as its own disposition item if it warrants separate treatment)

---

SEARCH-FOR-PRESUMPTION-037 (RE-TRIGGER cycle 2):
  Date searched: 2026-04-27
  Original item: PRESUMPTION-037
  Original statement: (see prior cycle for full statement)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a → 15c → 15d → 15a] (cycle 2)
    Original item: PRESUMPTION-037
    Item type: PRESUMPTION
    Transform at each step:
      14b (cycle 0): Originally extracted/inferred
      15a (cycle 0): Searched for supporting literature → see prior result block above
      15c (cycle 0): Initial disposition issued
      15d: Re-triggered on weekly cadence (2026-04-26 trigger; processed 2026-04-27)
      15a (cycle 2): Re-searched for supporting literature
    Current status: PARTIALLY-SUPPORTED (refreshed; no new supporting literature surfaced this cycle)

  New evidence weighed: No new supporting literature has surfaced in the week since the last cycle. The prior result stands as the operative finding. Item remains in its existing disposition state until either new operational evidence (from C2A2's own runs) or new external literature alters the picture.

  Sources (new / refreshed): No new sources this cycle.

  Strength of support: Unchanged from prior cycle.

  Summary: Cycle-2 refresh confirms the prior cycle's finding. The supporting literature base has not materially shifted in the past week; no new supportive sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Caveats: An automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven literature scan or operational evidence from the C2A2 runs themselves would be the more sensitive signal for status change.

  Recommendation: PARTIALLY-SUPPORTED (refreshed; carry forward prior recommendation)
