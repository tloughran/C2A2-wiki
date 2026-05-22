SEARCH-FOR-ASSUMPTION-159:
  Date searched: 2026-05-18
  Original item: ASSUMPTION-159
  Original statement: "agents.md imports Tom's 12 rules verbatim with one-line analogy note + vault-specific corollaries on Rules 5, 8, 9; single source of truth for both Claude agents and DeepSeek worker."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-159
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted/Surfaced from 2026-05-17 c2a2-self-awareness-daily run (resumed cycle)
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Wang (2011) 'Transfer Learning by Structural Analogy' (AAAI) — structural-alignment-based rule transfer is well-studied; works best when source and target share relational structure.
    2. Gentner & Markman (1997) — structural-alignment theory of analogy; supports the move from coding rules to vault rules via explicit mapping.
    3. Single-source-of-truth (SSOT) literature in software configuration (e.g. 12-factor app methodology) — strong support for canonical rule-files that multiple consumers read.

  Strength of support: Moderate

  Summary: The SSOT pattern for operating contracts is well-established in software engineering and DevOps; importing rules into a canonical agents.md is the canonical form. Analogical transfer of rules from one domain (coding) to another (vault/notes) is supported by structural-alignment theory when the mapping is made explicit — which the 'one-line analogy note + corollaries on 5/8/9' approach does. The combination is reasonable.

  Caveats: Corollary coverage of only Rules 5, 8, 9 leaves 9 rules transferred verbatim; PRESUMPTION-184 explicitly flags this as un-audited transfer. The SSOT pattern works only if all consumers actually read the file; the DeepSeek worker's adherence depends on prompt construction, not file-reading by the model.

  Recommendation: PARTIALLY-SUPPORTED
