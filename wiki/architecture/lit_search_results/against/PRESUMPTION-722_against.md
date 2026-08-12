SEARCH-AGAINST-PRESUMPTION-722:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-722
  Original statement: That a provenance field naming a file that was not read is harmless because the two are believed identical; disclosed in prose while the artefact carries the live mtime.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-722
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inferred by comparing where the caveat was recorded against where the field will be read
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "A Framework for Managing Evolving Information Resources on the Data Web" (arXiv:1504.06451) — notes that many file formats carry no intrinsic self-description of provenance; once a name is decoupled from content, the link back to provenance is "difficult to recover" once drift occurs.
    2. Solix Technologies, "Data Lineage: Architecture, Failure Modes, and How to Keep It Working" (2025) — identifies "lineage gaps on cross-tool joins" as a critical, scale-dependent failure mode, i.e. reference-based (name-based) linkage silently breaks under real-world editing.
    3. Cyberhaven, "Data Lineage vs. Data Provenance" — provenance is explicitly characterized as "a snapshot of origin, not a running account of everything that happened afterward," meaning a provenance field is definitionally stale the moment the referenced artefact changes.

  Strength of challenge: Moderate

  Summary: The data-provenance/lineage literature repeatedly documents the same failure shape described here: a name-based reference is trusted as equivalent to a live artefact without content verification, and that trust silently expires as the artefact mutates. None of these sources are C2A2-specific — they are general data-management findings — but they converge on the same mechanism (unverified identity claims decay) that this presumption flags. Prose disclosure of the caveat does not close the gap because prose is not machine-checked at read time.

  Specific risks: If the field is later trusted programmatically (e.g., a downstream agent skips re-reading the artefact because the provenance field claims identity), it will silently operate on a stale mtime/state — the exact prose-vs-artefact split already named once in PRESUMPTION-680 and now recurring two days later, suggesting the underlying process has no structural fix, only a documented workaround.

  Mitigations available: Content hashing/checksums instead of (or alongside) filenames; verifying identity at read time rather than trusting a written claim; treating the caveat as a machine-readable flag rather than prose.

  STEELMAN:
    Item: PRESUMPTION-722
    Strongest counterargument: Unverified equivalence between a named reference and a live, mutable artefact is a textbook provenance anti-pattern — the literature shows this drifts silently and is discovered only during audits or incidents, never proactively. Prose notes are read by humans occasionally, not machines continuously, so they cannot prevent the divergence they merely disclose. The recurrence of this exact split (per PRESUMPTION-680) two days after supposedly being "answered correctly" is itself evidence the fix was procedural, not structural.
    What would need to be true for C2A2 to be safe: The two files would need to be either (a) cryptographically verified identical at each read (hash match), or (b) never diverge in practice because the artefact is append-only/immutable after the provenance field is written, or (c) the provenance field itself would need to reference a content hash rather than a filename.
    How to test: Hash both files at the time the provenance field is written and again at each subsequent read; alert if the hashes diverge while the field still asserts identity.
