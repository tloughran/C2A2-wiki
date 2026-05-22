SEARCH-FOR-ASSUMPTION-129:
  Date searched: 2026-05-14
  Original item: ASSUMPTION-129
  Original statement: "Nightly alignment-agent protocol diffs `architecture/` ground-truth vs. `wiki/Architecture/` mirror, copies ground-truth → mirror on drift, flags in next session archive; pattern parallels Summa `sync_vault.sh` + launchd"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-129
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from alignment-agent design pass
      15a: Searched for vault-mirror sync protocols and unidirectional-vs-bidirectional sync patterns
    Current status: SUPPORTED

  Sources:
    1. Git / rsync / unison documentation — unidirectional sync with diff + overwrite is the canonical pattern when one side is authoritative.
    2. Allspaw & Robbins (2010) "Web Operations" — declared ground-truth + scheduled-sync is the resilient pattern for derivative-data invariants.
    3. Obsidian-syncthing community patterns (2023-2025) — vault-mirror sync with conflict-flag-on-drift is broadly endorsed for note-system architectures.
    4. C2A2-internal: Summa `sync_vault.sh` + launchd precedent — the pattern is already validated in adjacent infrastructure.
    5. Single-writer / multi-reader invariant (Lamport tradition) — when authority is clearly assigned, unidirectional sync is correct.

  Strength of support: Strong

  Summary: Unidirectional sync from a declared ground-truth to a derivative mirror is the canonical pattern when authority is clear. The Summa `sync_vault.sh` precedent confirms the operational viability. Drift-detection + flag is appropriate for the case where unilateral overwrite would be harmful. Support is strong for the architecture choice. PRESUMPTION-162 (paired) raises the secondary concern that mirror-side edits could occur and bidirectional merge with conflict-resolution is not considered — this is the conditional under which the pattern is correct.

  Caveats: (a) PRESUMPTION-162 — unidirectional sync presumes mirror-side edits will not occur; if any user/agent edits the mirror, overwrite is silent data loss; (b) "Flag in next session archive" assumes someone reads the archive; (c) Diff scope (which subset of files) is not specified in the assumption.

  Recommendation: SUPPORTED — architecture choice is well-supported under the single-writer invariant; PRESUMPTION-162 is the conditional that determines correctness
