SEARCH-AGAINST-PRESUMPTION-328:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-328
  Original statement: A localhost-served copy is render-equivalent to the file:// production artifact for verification purposes.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-328
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference from sociogram verification workflow (2026-06-09 EOD run): verification ran against localhost while the production artifact is opened via file://
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. MDN Web Docs. "Reason: CORS request not HTTP." — CORS operates only over http(s); file:// URLs are a different behavior class. Browsers (Firefox, Chrome) treat local files as having opaque origins by default, so same-origin logic differs categorically between the two environments.
    2. juplo.de, "Bypassing the Same-Origin-Policy for Local Files During Development." — Documents cross-browser divergence under file:// (e.g., Firefox blocks a local font load that Chrome permits): file:// behavior is not only different from http, it is inconsistent across browsers.
    3. johnskinnerportfolio.com, "XMLHttpRequest blocked by CORS policy in local HTML document." — Fetch/XHR that succeeds on localhost fails under file:// with opaque-origin errors; any code path involving fetch, modules, workers, or storage can pass on localhost and fail in the file:// artifact.
    4. Portswigger Web Security Academy, "CORS explained." — Origin semantics (scheme/host/port) underpin many runtime behaviors; localhost (http origin) and file:// (opaque/null origin) occupy different security contexts, a canonical environment-parity gap.
  Strength of challenge: Strong
  Summary: Web-platform documentation establishes that file:// and http://localhost are different origin classes with different security behavior: opaque origin vs proper origin, different CORS treatment, different rules for ES modules (which fail outright under file://), service workers, localStorage partitioning, and some font/asset loading — with the additional twist that file:// behavior varies by browser. The direction of the inference matters: verification on localhost (the more permissive environment) cannot demonstrate that the stricter file:// production artifact renders correctly; things that pass under http can fail under file://. For the current single-file artifact with inline JS/CSS and no fetches, the divergent behavior classes are mostly dormant — but the presumption is unsound as a general verification rule, and silently breaks the moment the artifact gains a fetch, module, web worker, or external asset.
  Specific risks: A verification pass on localhost is recorded as proof the production artifact works while file:// users (the actual distribution mode) hit a broken render; failures are browser-specific and so escape single-browser checks; future refactors (e.g., splitting the 4MB file, adding fetch-based data loading) invalidate the equivalence without anyone re-deriving it.
  Mitigations available: Verify at least once per release in the actual file:// mode and target browser; keep the artifact strictly self-contained (no fetch, no modules, no external refs) and assert that property in validate_html.py so the equivalence precondition is machine-checked; document the equivalence as conditional, not general.
  STEELMAN:
    Strongest counterargument: For a fully self-contained single-file HTML with inline scripts, inline styles, embedded data, and zero network or module requests, the known divergence classes (CORS, opaque origin, module loading, storage) are all unexercised, so localhost and file:// rendering are equivalent in practice for THIS artifact. Localhost verification is also more automatable (headless drivers handle http better than file://), so the trade-off is rational.
    What would need to be true for C2A2 to be safe: The artifact provably triggers none of the divergent behavior classes (no fetch/XHR, no ES modules, no workers, no external assets, no storage APIs); this invariant is checked automatically, not remembered.
    How to test: Add a static check to validate_html.py for fetch(, XMLHttpRequest, type="module", new Worker, localStorage, and external src/href; plus one manual or scripted open of the real file:// URL in the target browser per release, screenshot-diffed against the localhost render.
  Search scope: "file:// protocol vs http localhost different browser behavior CORS origin testing not equivalent" (1 search); plus MDN origin/CORS documentation as established reference.
  Recommendation: CHALLENGED
