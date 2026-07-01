SEARCH-AGAINST-PRESUMPTION-427:
  Date searched: 2026-07-01
  Original item: PRESUMPTION-427
  Original statement: "[inferred] That fixing one identity-keying bug makes the toolchain trustworthy — a second audit-identity divergence (qc_trace) appeared same session."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-427
    Item type: PRESUMPTION (unstated)
    Transform at each step:
      14b: Surfaced as unstated presumption from the A-396 keying fix
      15b: Searched for challenging literature (genuine web search 2026-07-01)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Defect-clustering / Pareto principle (BrowserStack, professionalqa, QA Trail) — defects cluster: ~80% of faults concentrate in ~20% of modules, and "when you find one bug, look for its friends nearby." One identity-keying bug predicts MORE keying bugs, not a clean toolchain.
    2. Pesticide paradox (PIT Solutions, softwaretestinghelp) — fixing the specific found defect does not eliminate the class; the same check stops finding new defects while related ones persist.
    3. C2A2-internal EMPIRICAL: a second identity divergence (qc_trace) appeared in the SAME session — direct confirmation that the class was not eliminated by the single fix.

  Strength of challenge: Strong

  Summary: Defect-clustering theory predicts exactly what was observed: identity-keying is a cluster, and one fix does not make the toolchain trustworthy — it flags a fault-dense region deserving a systematic audit. The same-session qc_trace divergence is empirical refutation of the presumption.

  Specific risks: A false sense of a trustworthy toolchain after one fix leaves other keying/identity mismatches live, silently corrupting audit trails and ingestion identity.

  Mitigations available: Run a systematic keying-mismatch audit across every identity join in the toolchain (proposal_id, qc_trace, filename surfaces), not just the one that surfaced.

  STEELMAN:
    Item: PRESUMPTION-427
    Strongest counterargument: If the two divergences share a single root cause (one keying convention applied inconsistently), then fixing that convention everywhere IS a class fix — the presumption is wrong only about scope, and a single well-targeted convention change could legitimately restore trust.
    What would need to be true for C2A2 to be safe: The audit confirms all identity joins now use one stable key (proposal_id) and no surface-key joins remain.
    How to test: Grep the toolchain for filename/surface-key joins; assert zero remain.

  SYSTEMIC-RISK: member of the "one-shot-fix-as-durable-solution" cluster (with A-393, P-425).

  Recommendation: CHALLENGED (Strong — defect clustering + same-session second divergence refute "one fix = trustworthy")
