SEARCH-AGAINST-ASSUMPTION-214:
  Date searched: 2026-05-23
  Original item: ASSUMPTION-214
  Original statement: "A single self-contained handoff document can carry an experiment's full context into a cold-start chat, making the experiment portable across sessions."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-214
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the two-summa cold-start brief packaging.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E noted)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Polanyi (1966) "The Tacit Dimension." — "We know more than we can tell"; load-bearing knowledge resists full explicit articulation, so a written brief cannot carry all of it.
    2. Collins (2001) "Tacit Knowledge, Trust and the Q of Sapphire" / TEA-laser studies. — Experiments famously could NOT be replicated from written reports alone; tacit, person-to-person transfer was required.
    3. Reproducibility crisis (Baker 2016, Nature; Open Science Collaboration 2015). — Even detailed methods sections routinely fail to reproduce results, evidence that documents under-carry context.

  Strength of challenge: Moderate-Strong

  Summary: The strongest empirical case against full-context portability is the replication literature: experiments often cannot be reproduced from their written record alone (Collins), because experimental competence is partly tacit (Polanyi) and specifications are constitutively incomplete. For an LLM cold start the risk is amplified — the model lacks the human reader's shared background that normally fills documentation gaps. The claim "full context" is therefore too strong; "enough context, sometimes, after iteration" is the defensible version.

  Specific risks: The two-summa experiment launches from a brief that silently omits a load-bearing detail, producing a run that looks faithful but diverges from intent — and the divergence is hard to detect precisely because the omission was invisible.

  Mitigations available: Treat the brief as a hypothesis to be tested: cold-start it, diff the resulting setup against the author's intent, and iterate; keep a "what a reader must already know" appendix; version the brief as defects are found.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-214
    Strongest counterargument: Decades of replication research show that written records systematically under-carry the tacit competence needed to reproduce experimental work; "full context in one document" is precisely the assumption the reproducibility crisis falsified. A cold-start chat is the worst case because it has none of the shared human background that normally repairs documentation gaps.
    What would need to be true for C2A2 to be safe: The experiment's load-bearing context is genuinely explicit and verifiable, and the brief has survived at least one real cold-start reproduction test.
    How to test: Hand the brief to a fresh chat with no extra steering; have the author flag every place the run diverged from intent. Non-zero load-bearing divergences falsify "full context."


---

SEARCH-AGAINST-ASSUMPTION-214 (RE-TRIGGER cycle 1):
  Date searched: 2026-06-01
  Original item: ASSUMPTION-214
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-214
    Item type: ASSUMPTION
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
