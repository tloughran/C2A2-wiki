SEARCH-FOR-PRESUMPTION-1187:
  Date searched: 2026-10-27
  Original item: PRESUMPTION-1187
  Original statement: "[inferred] A named coordination artefact is presumed to have one canonical location, so that checking 'the file' settles a question. Two `lit_pipeline.lock` files exist (architecture/ stale since 10-15; review/ live). The 10-25 14a pass read the stale one, recorded the result as 'Verified', and the error propagated into OPEN-275, PRESUMPTION-1185 and a High-priority MONITOR-697. The self-audit layer is subject to the same artefact-as-proof failure (15b, 10-26) it reports in other agents."

  Reading used for the FOR direction: support means literature showing that (a) duplicate or drifted copies of an authoritative artefact are a recognised hazard, so a check against the wrong copy proves nothing; and (b) a check that shares the audited system's artefacts and blind spots (self-review) is a recognised threat to its authority. 15a does not judge whether 14a actually read the stale lock.

  Search scope: PRELIMINARY. 2 web searches (standard), 0 fetches. Searched: single source of truth / configuration drift / split-brain; auditor self-review threat. Not reached: IIA/IESBA primary standards, reproducibility literature on internal audits, stale-lock literature specifically (none came back).

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1187
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 10-25 14a pass reading the stale architecture/ lock and recording "Verified", and from the downstream items it fed (OPEN-275, PRESUMPTION-1185, MONITOR-697). Extended to the self-audit layer.
      15a: Searched for supporting literature (preliminary; 2 searches, 0 fetches)
    Current status: SEARCHED-15a — PARTIALLY-SUPPORTED

  Supporting evidence found: Partial. Both halves have recognised analogues, in practitioner and professional-education sources. Nothing found on the narrow case of a stale duplicate lock file being read as authoritative.

  Sources:
    1. Configuration-drift guidance: Wiz Academy, "Configuration Drift Explained"; Octopus Deploy, "Configuration drift"; DesignGurus, "How do you manage configuration drift"; Google Cloud Config Sync docs, "Prevent config drift". [snippet only, practitioner/vendor]. Recommended defence: one version-controlled source of truth, with reconciliation that detects divergence from it and reverts it. Relevance: analogous support for (a). The field treats "which copy is authoritative" as something to define and enforce explicitly, not something to assume.
    2. Split-brain explainers: DesignGurus, "What is a split-brain scenario"; Gravitee, "Drift Detection and Reconciliation for Gateway Configurations". [snippet only, practitioner]. Two nodes each act as primary, or drifted gateways enforce different rules for the same request. Relevance: analogous support. Two live-looking copies give inconsistent answers depending on which one is consulted. This is the item's two-lock situation in distributed-systems terms.
    3. Auditor-independence threat frameworks: Corporate Finance Institute, "Threats to auditor independence"; Accountants Daily, "Independence issues for internal auditors"; ICAI WIRC study material; Interior Health board policy 3.10. [snippet only, secondary/educational]. "Self-review threat" (assurance on one's own work, or on work by others in the same firm) is one of the five standard threats. The internal-audit safeguard is that no one reviews their own work. Relevance: theoretical grounding for (b). A check that relies on the audited system's own artefacts is a named, standard threat to its authority.

  Strength of support: Moderate

  Summary: The literature treats multiple uncoordinated copies of an authoritative artefact as a known hazard (configuration drift, split-brain). Its remedy is an explicitly designated, enforced single source of truth plus reconciliation, which implies that checking "a file" with that name does not settle anything. Separately, auditing doctrine names self-review as a standard independence threat, which grounds the item's point that C2A2's self-audit layer can repeat the artefact-as-proof failure it reports in others. Together these support the item's diagnosis by analogy. No source addresses lock files duplicated across directories.

  Caveats:
    - All sources are snippet-level, and most are vendor or educational. The IIA/IESBA primary standards were not read.
    - Auditor self-review concerns professional independence (incentives and familiarity), not shared data artefacts. Transferring it to agents reading the same files is an analogy.
    - Drift literature mostly concerns infrastructure config, not coordination/lock files. Nothing was found specifically on a stale lock being read as proof.
    - "What makes a check authoritative" was not answered directly. The implied answers are a designated source of truth, plus an independent or external reviewer.

  Recommendation: PARTIALLY-SUPPORTED

  (No NOVELTY-FLAG: the parts are established, and the item combines them. The specific "auditor shares the audited artefact" framing for multi-agent self-audit had no direct literature in this preliminary scope.)
