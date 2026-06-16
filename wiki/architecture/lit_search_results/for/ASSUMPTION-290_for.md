SEARCH-FOR-ASSUMPTION-290:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-290
  Original statement: The capture gap should be solved with an external symlink session-bridge, not an OpenStory fork, to stay on upstream.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-290
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated architectural assumption from 2026-06-08 OpenStory→Agent-Explorer build sessions (cycle 0, priority LOW)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: SUPPORTED

  Supporting evidence found: Yes
  Sources:
    1. Meta Engineering, 2026. "Escaping the Fork: How Meta Modernized WebRTC Across 50+ Use Cases." engineering.fb.com. — Large-scale case study replacing a years-diverged fork with a shim/adapter layer; staying current with upstream eliminated compounding merge debt.
    2. Preset (Beaumont, M. et al.), "Stop Forking Around — The Hidden Dangers of 'Fork Drift' in Open Source Adoption." preset.io. — Documents fork drift: cherry-pick/rebase burden compounds (possibly exponentially) with each local change; recommends external extension points instead.
    3. Fedora Project Wiki, "Staying close to upstream projects." — Long-standing distro policy precedent: minimize carried patches; the closer to upstream, the lower the long-term maintenance cost.
    4. Rocha, J., 2024. "How to fork: Best practices and guide." — Practitioner synthesis: fork only when integration seams are unavailable; isolate customizations outside the upstream tree where possible.
  Strength of support: Strong
  Summary: The adapter/shim-over-fork preference is well supported by both case-study and policy literature. Fork drift is a documented failure mode with compounding maintenance cost, and Meta's WebRTC shim migration is a direct empirical precedent for solving an integration gap with an external bridging layer while tracking upstream. Distro packaging policy (Fedora, Debian) institutionalizes the same principle. An external symlink session-bridge is a minimal instance of this pattern — fully reversible, zero patches carried against upstream OpenStory.
  Caveats: The pattern's economics assume upstream keeps evolving and the bridge's contact surface (file layout/symlink semantics OpenStory reads) is stable; a bridge coupled to an undocumented internal layout can silently break on upstream changes, whereas a fork at least fails loudly at merge time. Symlink-specific bridges have portability/permission edge cases not covered by this literature.
  Search scope: 1 query — "fork versus adapter shim staying close to upstream open source maintenance burden vendoring patches".
  Recommendation: SUPPORTED
