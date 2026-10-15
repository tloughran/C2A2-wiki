SEARCH-AGAINST-PRESUMPTION-1141:
  Date searched: 2026-10-15
  Original item: PRESUMPTION-1141
  Original statement: "Outputs can be validated without recorded process (workflow) lineage. Literature question: what do data-provenance and workflow-lineage literatures (W3C PROV; scientific-workflow provenance) say about validating outputs without lineage?"
  Independence: run by a separate subagent that did not read 15a output. (Shared web-fetch cache not used by either: no fetches.)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1141
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-10-14 transcripts.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes
  Search scope: PRELIMINARY — broader search recommended. Titles/URLs only; no full text read; UNVERIFIED items from background knowledge.

  Sources:
    1. Moreau, Missier et al., 2013. W3C PROV-DM. — UNVERIFIED (background). Provenance exists so consumers can assess quality, reliability, trustworthiness: the premise the presumption rejects.
    2. Khan et al., CWLProv (w3id.org/cwl/prov/0.2.0). — Title/URL only. Retrospective provenance needed for reproducibility; capture is hard, so partial lineage is common.
    3. "Provenance in support of workflows for science" (TU Berlin DepositOnce). — Title only; authors/year unknown. UNVERIFIED.
    4. Freire, Koop, Santos, Silva, 2008. "Provenance for Computational Tasks: A Survey." Computing in Science & Engineering. — UNVERIFIED (background). Provenance for verifying and reproducing results.

  Strength of challenge: Moderate

  Summary: The literature holds lineage is what lets one judge whether an output is trustworthy. Without it only output-level checks remain (plausibility, internal consistency, independent comparison); these miss silent upstream errors (wrong input version, parameters, contaminated source) and cannot attribute faults. It does not say validation is impossible, only weaker.

  Specific risks: Plausible-looking errors pass undetected; faults cannot be traced; results cannot be reproduced or audited; the same output may come from different processes.

  Mitigations available: Validate against independent ground truth or held-out sample; re-derive with a second independent process; output-only invariant checks; capture minimal lineage (inputs, queries, timestamps, tool versions).

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1141
  Strongest counterargument / conditions for safety / test: Output-level validation suffices where outputs are self-verifying (checkable facts, citations resolvable against primary sources), where verification is cheaper than lineage capture, and where the claim is about output correctness not process fidelity. Safe if errors are detectable from the output alone, no claim depends on how the output was produced, and the independent check is truly independent. Test: seed known defects (wrong source, stale data, fabricated item) and measure output-only detection rate.
