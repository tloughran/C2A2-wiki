SEARCH-AGAINST-ASSUMPTION-306:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-306
  Original statement: On history restore, embedded-frame content is the authoritative state and the shell should resync to it (source-of-truth inversion on load/pageshow).

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-306
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated assumption (state-reconciliation design choice on restore)
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. web.dev, "Back/forward cache" (Articles). — Iframes are NOT separately eligible for bfcache; iframe navigation history and restoration behavior diverge from the main frame, so "what the frame shows after restore" is browser- and history-path-dependent, not a stable authority.
    2. Hyvä Docs, "Back-Forward Cache (bfcache)." — Documented pattern of restored pages carrying broken/stale JS state (disabled buttons, outdated counters) after pageshow; restored state is preserved-as-frozen, not validated, and must be actively reset rather than trusted.
    3. DEV Community, "Web Page Not updating on back navigation? The bfcache Problem and Fix." — The canonical bfcache failure is precisely stale content presenting as current; treating restored content as authoritative is the named anti-pattern (fix: detect event.persisted and re-derive state).
    4. WICG, "bfcache NotRestoredReason" explainer. — Restoration is non-uniform across browsers and frame trees; pages with iframes get partial/blocked restores for many reasons, so the frame's post-restore state has multiple distinct provenances the shell cannot distinguish.
  Strength of challenge: Moderate
  Summary: The bfcache literature challenges the premise that the embedded frame's post-restore content is a well-defined single thing to defer to. Depending on browser, navigation path, and NotRestoredReasons, the frame after pageshow may be (a) a frozen snapshot from minutes ago, (b) a fresh reload at its original src, or (c) a back-navigation within the iframe's own history — and the shell cannot reliably tell which. The documented anti-pattern is exactly "trust the restored content"; the recommended pattern is to detect restore (event.persisted) and re-derive state from a durable source (URL params, sessionStorage) rather than from whichever frame state the browser happened to revive. Source-of-truth inversion toward the least-deterministic component inverts the reliability ordering.
  Specific risks: Shell controls (filters, tab state, narration position) resync to a stale or freshly-reset frame and silently discard the user's last real state; behavior differs between Safari/Firefox (aggressive bfcache) and Chrome, producing unreproducible "sometimes it forgets" bugs; future shell features inherit an authority rule that is wrong in a browser-dependent fraction of restores.
  Mitigations available: Persist canonical state in the URL hash or sessionStorage at every change and have BOTH shell and frame rehydrate from it on pageshow; treat frame content as a cache, never an authority; add a version/timestamp handshake so the shell can detect a reset frame.
  STEELMAN:
    Strongest counterargument: In this architecture the frame holds the substantive interactive state (graph position, selections) and the shell is thin chrome; when the browser restores, the frame snapshot is the closest thing to what the user last saw, and resyncing the shell to it minimizes visible discontinuity. A third durable store adds machinery a single-author local tool may not need, and in the common Chrome same-tab case the frame snapshot is in fact the last real state.
    What would need to be true for C2A2 to be safe: Target browsers restore shell and frame atomically from the same snapshot; the frame is never independently navigated or reloaded; users only ever restore via paths where bfcache succeeds whole-tree.
    How to test: Navigate away and back in Safari, Firefox, and Chrome (plus a hard reload) and log which of frame/shell state survives each path; any divergence falsifies frame-as-authority.
  Search scope: 1 WebSearch ("iframe bfcache restore state inconsistent browser back forward cache stale iframe content pitfalls").
  Recommendation: PARTIALLY-CHALLENGED
