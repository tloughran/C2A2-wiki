SEARCH-FOR-PRESUMPTION-328:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-328
  Original statement: A localhost-served copy is render-equivalent to the file:// production artifact for verification purposes.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-328
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference from sociogram verification workflow (2026-06-09 EOD run)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. MDN Web Docs. "Reason: CORS request not HTTP." — Authoritative documentation that the rendering engine is shared across schemes; divergence is confined to enumerable origin-dependent feature classes (CORS, fetch of local resources, opaque origins).
    2. freeCodeCamp / Auth0 CORS guides ("How to Fix Cross-Origin Errors"; "CORS Tutorial"). — Standard practice endorses local HTTP servers as the verification environment for HTML artifacts, treating localhost as the canonical stand-in.
    3. Browser vendor documentation (Chrome/Firefox file-URL security policy). — file:// is treated as an opaque origin; the differences are one-directional restrictions on file://, not arbitrary divergence.
  Strength of support: Weak
  Summary: Practice and documentation support a conditional version of the presumption: layout, CSS, and JS execution are scheme-independent, so for a fully self-contained HTML file (no fetch/XHR, no external resources, no storage APIs, no ES modules loaded cross-file) localhost and file:// renders are effectively equivalent — which matches the wiki_narration.html artifact's self-contained design. The same documentation, however, establishes that the divergences run in the unfavorable direction: file:// is *more* restrictive (opaque origin, blocked local fetches, storage quirks), so a page that verifies clean on localhost can still fail under file://. Verification on localhost is therefore necessary-but-not-sufficient evidence about the file:// artifact; the equivalence holds only given a feature audit confirming none of the origin-sensitive APIs are used.
  Caveats: Equivalence is conditional on the artifact remaining fully self-contained; any future addition of fetch(), Web Workers, ES module imports, localStorage, or service workers voids it. The safe verification direction is the reverse: test under file:// itself, since localhost success does not entail file:// success.
  Search scope: 1 query ("file:// protocol vs http localhost differences browser behavior CORS testing environment parity"); productive.
  Recommendation: PARTIALLY-SUPPORTED
