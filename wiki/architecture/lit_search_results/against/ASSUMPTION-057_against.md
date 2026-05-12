SEARCH-AGAINST-ASSUMPTION-057:
  Date searched: 2026-04-21
  Original item: ASSUMPTION-057
  Original statement: "17→11 findings filter uses the rule 'Active or Highest Priority, excluding subsumed/downgraded.'"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-057
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Morning walk handoff 2026-04-21 — filter criterion stated
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Unaudited-filter anti-pattern literature (internal reference PRESUMPTION-029 CRITICAL; unaudited-filter cluster from 2026-04-20 Run 2 now includes PRESUMPTION-053 and ASSUMPTION-046): making a filter rule visible does not make it correct. Literature on software filter audits (IEEE software-quality standards; information-retrieval precision/recall evaluation) shows that visibility is necessary but not sufficient — filters must be tested against independent ground truth.
    2. Silent-signal-loss literature (Marcus & Davis 2019 "Rebooting AI"; information-retrieval precision-recall tradeoffs): filter-excluded items can carry unique signal. The 6 excluded findings (001, 002, 003, 004, 006, 007, 008, 010 — eight items listed but task-file says 6 subsumed/downgraded; discrepancy itself flags potential audit gap) may have subsequent activity that re-qualifies them under the stated rule.
    3. Subsumption-classification literature (ontology-engineering; SNOMED/MeSH classification standards): "subsumed" is a nontrivial classification that requires a criterion. Without a documented subsumption criterion, the rule's second-order judgment (which findings are "subsumed" vs. merely "older") is itself unaudited.
    4. Stated-vs-audited distinction (Cochrane systematic-review methodology; PRISMA 2020 item 8): stated inclusion/exclusion criteria must be accompanied by documentation of how each excluded item was classified. Stating the rule without the per-item classification log fails PRISMA's own transparency standard.
    5. Drift-over-time literature (data-quality monitoring; Kleppmann 2017 "Designing Data-Intensive Applications"): filter rules applied statically to a register that changes over time can accumulate drift. Findings classified "subsumed" at one timepoint may have subsequent activity; the rule does not address re-qualification.

  Strength of challenge: Moderate

  Summary: Stating the rule is a visibility improvement but the rule is still unaudited in its specific application. The literature is clear that filter visibility is necessary-but-not-sufficient — a stated rule needs per-item classification documentation (which findings were "subsumed" and why; which "downgraded" and when) to meet PRISMA/Cochrane standards. The second-order criteria ("subsumed" and "downgraded") are not themselves stated, creating nested unaudited judgment. Items classified "subsumed" at one timepoint may have subsequent activity that should re-qualify them; the rule does not specify re-qualification. Joins the unaudited-filter cluster (PRESUMPTION-029 CRITICAL; PRESUMPTION-053; ASSUMPTION-046) as a newly-stated-but-still-unaudited fourth member.

  Specific risks: (a) Per-item classification log missing — the rule can be stated correctly but applied incorrectly without detection; (b) "subsumed"/"downgraded" are second-order classifications that may themselves be unaudited; (c) re-qualification is not addressed — findings that become active again after being filtered out will not be re-included by the rule as stated; (d) extends unaudited-filter cluster to 4 members.

  Mitigations available: (a) Add a per-item classification log documenting each excluded finding's classification reason and classification date; (b) state the "subsumed" and "downgraded" criteria explicitly; (c) add a re-qualification check — scan the excluded set for subsequent activity that should trigger re-inclusion; (d) pair ASSUMPTION-057 remediation with PRESUMPTION-053 audit-criterion log (already REVISE on 2026-04-20).

  Recommendation: PARTIALLY-CHALLENGED (rule now visible but still unaudited; second-order criteria and re-qualification are nested unaudited judgments; joins unaudited-filter cluster; pair with PRESUMPTION-053 remediation)

  STEELMAN:
    Item: ASSUMPTION-057
    Strongest counterargument: Making a rule visible does not make the rule correct. PRISMA item 8 explicitly requires stated inclusion/exclusion criteria PLUS per-item classification documentation; this rule has the first but not the second. The "subsumed" and "downgraded" classifications are themselves unstated criteria, creating nested unaudited judgment — the same structural problem PRESUMPTION-053 identified (an audit-criterion log is missing). The task-file itself has an internal inconsistency (references both "6 excluded findings" and lists 8: 001-004, 006-008, 010), which is itself evidence that the rule has not been audited against its application. Absent a per-item log and second-order criteria, stating the rule creates the appearance of audit without the substance.
    What would need to be true for C2A2 to be safe: Per-item classification log for each excluded finding with classification reason and date; stated second-order criteria for "subsumed" and "downgraded"; re-qualification check for subsequently-active excluded items.
    How to test: Audit the 6 (or 8) excluded findings against the stated rule; verify each classification is correct; scan for any excluded finding with activity since exclusion date that should re-qualify.
