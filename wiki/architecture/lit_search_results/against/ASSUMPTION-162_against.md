SEARCH-AGAINST-ASSUMPTION-162:
  Date searched: 2026-05-18
  Original item: ASSUMPTION-162
  Original statement: "Coordination primitives for multi-agent shared-vault: MCP shared protocol; Git as universal undo/conflict layer; folder-scoped agent assignments; no scheduler, no lock manager — last-write-wins."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-162
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted/Surfaced from 2026-05-17 c2a2-self-awareness-daily run (resumed cycle)
      15b: Searched for challenging literature
    Current status: STRONGLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Wikipedia 'Conflict-free replicated data type' — explicit warning: 'Using the latest write risks data loss, since timestamps across distributed systems can drift or arrive out of order.'
    2. DZone 'Conflict Resolution: Using Last-Write-Wins vs. CRDTs' — LWW is documented as a conflict-resolution policy with known failure modes; CRDTs or vector clocks are preferred for correctness.
    3. Issue #4857 in super-productivity (2024 GitHub) — empirical case study of multi-device JSON-file LWW causing data loss; cited as canonical evidence of the failure mode in real systems.
    4. Iankduncan 'The CRDT Dictionary' (2025) — comprehensive treatment; LWW achieves convergence only under monotonic-globally-unique clocks, an assumption distributed systems cannot guarantee.

  Strength of challenge: Strong

  Summary: 'Last-write-wins' is a documented anti-pattern in the multi-producer literature. The CRDT and version-vector communities treat LWW as a known-bad default. The claim works at C2A2's current N=1 scale because there are no concurrent writes, but the architectural commitment names a coordination policy that the literature warns against scaling.

  Specific risks: (a) Silent data loss if two writers ever touch the same file; (b) clock-drift between writers (Claude session vs. DeepSeek worker) can mis-order writes; (c) Git provides undo only if someone notices the loss; (d) Maildir filename uniqueness handles new-file collisions but not edit collisions.

  Mitigations available: (a) Strict folder partitioning to make concurrent writes impossible; (b) periodic git status audit; (c) plan transition to CRDT or vector-clock pattern before second producer is added (joins PRESUMPTION-183).

  Recommendation: STRONGLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-162
    Strongest counterargument: The strongest case against: the 'no scheduler, no lock manager' choice is correct only because partitioning is perfect. The moment partitioning is imperfect — and partitioning in shared-vault contexts is rarely perfect — LWW becomes silent data loss. Naming the policy as a primitive normalizes a documented anti-pattern.



---

SEARCH-AGAINST-ASSUMPTION-162 (RE-TRIGGER cycle 1):
  Date searched: 2026-06-01
  Original item: ASSUMPTION-162
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-162
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

  Recommendation: refreshed; carry forward prior recommendation (STRONGLY-CHALLENGED)
