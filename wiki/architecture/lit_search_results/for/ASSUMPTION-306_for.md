SEARCH-FOR-ASSUMPTION-306:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-306
  Original statement: On history restore, embedded-frame content is the authoritative state and the shell should resync to it (source-of-truth inversion on load/pageshow).

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-306
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted stated assumption from architecture work log (cycle 0, 2026-06-10)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. web.dev, "Back/forward cache" (Google web platform documentation). — Documents that on bfcache restore, embedded iframes are restored exactly as they were when the page entered the cache, and that pages must use the pageshow event (event.persisted) to detect restore and reconcile stale state — direct grounding for a resync-on-pageshow design.
    2. MDN / browser-platform documentation on pageshow/pagehide and session-history form-state restoration. — Browsers also restore form/scroll state per frame on history traversal; the restored frame content is what the user actually sees, so reconciliation must start from it.
    3. DEV Community, "Navigating the bfcache: Ensuring State and Script Integrity on Back/Forward Navigation" (2024). — Practitioner pattern: on persisted pageshow, re-derive application state rather than assuming in-memory shell state survived; matches the shell-resyncs posture.
  Strength of support: Moderate
  Summary: Platform documentation directly supports two pillars of the assumption: (a) on history restore the browser independently restores embedded-frame content (bfcache snapshots include iframes; non-bfcache traversal restores per-frame session history), so the frame's displayed state can genuinely diverge from shell expectations; and (b) the sanctioned hook is pageshow/load reconciliation. Given the user sees the frame's restored content, resyncing the shell to it is a coherent and precedented reconciliation direction. What the literature does not establish is that the frame is authoritative in general — standard guidance treats restored state as potentially stale and recommends re-fetching from the true source (data/app state), which can mean overwriting the frame instead.
  Caveats: Restore behavior differs across browsers and across bfcache vs non-bfcache paths (iframes themselves are not separately bfcached; Safari/Firefox/Chrome differ in form-state and srcdoc handling) — the inversion is correct for "reflect what the user sees" but wrong if the frame can itself be stale relative to underlying data. A two-way reconciliation rule (frame wins for view state, shell/data wins for content) is the safer reading of the guidance.
  Search scope: 1 WebSearch ("bfcache pageshow iframe state restoration browser back forward cache form state shell resync source of truth").
  Recommendation: PARTIALLY-SUPPORTED
