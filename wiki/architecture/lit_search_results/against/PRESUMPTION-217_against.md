SEARCH-AGAINST-PRESUMPTION-217:
  Date searched: 2026-05-20
  Original item: PRESUMPTION-217
  Original statement: "One entity index serves search + linking + Ask without incompatible requirements (Pathway 27)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-217
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — Pathway 27 presumes a single entity index can serve search, linking, and Ask surfaces without incompatible requirements.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Young, G. / Fowler, M. — CQRS. — Divergent read requirements (search relevance vs deterministic joins vs semantic retrieval) are the canonical case for separate read models.
    2. Lewis, P. et al. (2020). "Retrieval-Augmented Generation" (NeurIPS). — Ask/RAG needs dense/semantic retrieval and freshness guarantees an inverted search/links index may not provide.
    3. Sadalage, P. & Fowler, M. (2012). "NoSQL Distilled" (polyglot persistence). — Forcing incompatible access patterns onto one store compromises each.

  Strength of challenge: Moderate-Strong

  Summary: The moderate-strong challenge mirrors ASSUMPTION-197: search (relevance ranking), linking (exact joins/determinism), and Ask (semantic retrieval + freshness) are three different read problems, and CQRS/polyglot-persistence experience says one store tends to compromise at least one. 'Without incompatible requirements' is the load-bearing, contestable clause — Ask is the likely misfit. The staging plan (Ask after the broker) helpfully defers but does not resolve the question.

  Specific risks: Ask quality compromised to fit the shared index, or a costly late split when Ask is added; the incompatibility surfaces after commitment.

  Mitigations available: Validate Ask retrieval requirements before committing; design the boundary so an Ask-specific read model (e.g., vector store) can attach without re-architecting; keep search+links unified.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-217
    Strongest counterargument: Search, linking, and Ask are distinct read problems; CQRS exists because one model rarely serves divergent reads well. 'No incompatible requirements' is precisely the clause most likely to fail, at the Ask surface, and the cost shows up late.
    What would need to be true for C2A2 to be safe: Safe if Ask's requirements are validated against the shared index before commitment, with a vector-store fallback designed in.
    How to test: Prototype Ask retrieval on the proposed index vs a dedicated vector store with representative queries; compare retrieval quality and freshness.


---

SEARCH-AGAINST-PRESUMPTION-217 (RE-TRIGGER cycle 1):
  Date searched: 2026-06-01
  Original item: PRESUMPTION-217
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14b
    Chain: [14b->15a,15b->15c->15d->15a,15b->15c]
    Original item: PRESUMPTION-217
    Item type: PRESUMPTION
    Transform at each step:
      cycle 0..0: prior search/disposition cycles (see blocks above)
      15d (2026-05-31): re-triggered on weekly cadence; next_check 2026-05-31 elapsed
      15b (cycle 1, 2026-06-01): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-05-31 (weekly cadence fired on time; next_check 2026-05-31 elapsed). Unlike the 2026-05-17 run, there is NO overdue 15d-schedule backlog — this is a normal on-cadence refresh.
  Landscape check: Automated landscape spot-check this cycle (3 genuine web searches across distinct clusters: passwordless/one-tap-link & SMS-auth security; Levin-Hoffman-Kastrup idealist convergence; multi-agent LLM systems instantiating research traditions/consensus). All three reaffirmed prior for/against profiles; no material literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new challenging literature has surfaced in the past week. The prior cycles' challenge profile stands.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted; no new disconfirmatory sources surfaced during this automated cycle.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  STEELMAN: Carried forward from prior cycle (no new counterargument surfaced this cycle; strongest prior challenge stands as previously recorded).

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED)
