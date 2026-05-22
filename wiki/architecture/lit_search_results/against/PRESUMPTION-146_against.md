SEARCH-AGAINST-PRESUMPTION-146:
  Date searched: 2026-05-13
  Original item: PRESUMPTION-146
  Original statement: "Loughran papers on-disk without processing-trigger — content-architecture artifact treated as load-bearing despite not-yet-ingested status"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-146
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-12 Loughran-papers on-disk-pending-ingest framing
      15b: Searched for counter-evidence on natural-cadence processing without explicit-trigger DECISION
    Current status: CHALLENGED

  Sources:
    1. Reinertsen (2009) — make-ready inventory is operationally distinct from delivered value; "natural-cadence processing" without trigger criterion produces systematic latency and WIP accumulation.
    2. Poppendieck (2003) — Lean software development: WIP-without-trigger is anti-pattern; explicit pull triggers are canonical.
    3. PMBOK 7th ed. — completed vs. in-progress work distinction; on-disk-pending is in-progress.
    4. C2A2-internal: PRESUMPTION-128 (MONITOR-115 — workflow-accommodation cluster) and ASSUMPTION-111 (MONITOR-113 — first-ever pendings precondition) — both share the structural shape (on-disk artifacts treated as load-bearing without trigger). PRESUMPTION-146 is the third recurrence at the Loughran-papers layer.
    5. Per-thinker asymmetry: Wright/Rohr pending proposals are explicitly tagged as "blocking" (ASSUMPTION-111) while Loughran papers are framed as "not-yet-ingested without urgency" — the asymmetry is the structural concern; same on-disk status, different treatment.

  Strength of challenge: Moderate

  Summary: The challenge is moderate. Lean / Reinertsen / PMBOK converge: on-disk-pending artifacts treated as load-bearing without explicit ingest trigger inflate apparent throughput and produce schedule risk. PRESUMPTION-146 is the third recurrence of the on-disk-pending-as-load-bearing pattern (after PRESUMPTION-128 and ASSUMPTION-111). The per-thinker asymmetry (Wright/Rohr blocking vs. Loughran natural-cadence) is the specific structural concern unique to this presumption.

  Specific risks: (a) Loughran papers accumulate without ingest trigger; (b) Architectural decisions referencing the papers are based on artifacts-that-exist rather than artifacts-that-have-been-processed; (c) Per-thinker asymmetry produces inconsistent workflow treatment; (d) Joint with PRESUMPTION-128 cluster.

  Mitigations available: (a) Explicit ingest trigger for Loughran papers (date, event, or workflow signal); (b) per-thinker policy parity — apply same trigger framework to Wright/Rohr/Loughran; (c) WIP visualization for on-disk-pending; (d) joint remediation with PRESUMPTION-128 cluster.

  Recommendation: CHALLENGED (Moderate) — third recurrence at the Loughran layer; per-thinker asymmetry is unique structural concern

  STEELMAN:
    Item: PRESUMPTION-146
    Strongest counterargument: On-disk-pending artifacts treated as load-bearing without explicit ingest trigger is documented anti-pattern in Lean (Reinertsen, Poppendieck) and PMBOK. The C2A2 system has the asymmetric pattern: Wright/Rohr pending proposals are explicitly "blocking" while Loughran papers are "not-yet-ingested without urgency" — same on-disk status, different operational treatment. The asymmetry is the structural concern: the system has two different default policies for the same operational state. PRESUMPTION-146 is the third recurrence of on-disk-as-load-bearing-without-trigger after PRESUMPTION-128 and ASSUMPTION-111.
    What would need to be true for C2A2 to be safe: (a) Explicit ingest trigger for Loughran papers; (b) policy parity across thinkers; (c) WIP visualization.
    How to test: Audit per-thinker treatment of on-disk-pending artifacts; document the asymmetry; propose unified trigger framework.
