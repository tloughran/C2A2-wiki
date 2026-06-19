SEARCH-AGAINST-ASSUMPTION-331:
  Date searched: 2026-06-19
  Original item: ASSUMPTION-331
  Original statement: "A manual local visual verify (localhost:8080) 'satisfies the constitutional check' and clears the build to push."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-331
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the verification-adequacy decision for the push gate
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Limits of manual QA — manual visual inspection is non-reproducible, low-coverage, and inconsistent run-to-run; it cannot serve as a reliable release gate on its own. The testing literature treats manual smoke checks as necessary-not-sufficient.
    2. Render vs content coverage — a visual verify confirms the page LOADS and LAYS OUT; it does not assert the CONTENT is the right brief, accurate text, or correct node counts. The known ~256-vs-379 Summa gap is precisely the kind of defect a "looks fine" glance misses (couples ASSUMPTION-332).
    3. "Looks right" ≠ "is right" / inattentional blindness — human reviewers reliably miss content errors that are not visually salient; a one-shot glance under-detects exactly the wrong-text/wrong-count failures that matter here.

  Strength of challenge: Moderate-Strong

  Summary: As a SUFFICIENT constitutional check, the manual visual verify is challenged strongly: it is non-reproducible, low-coverage, and silent on content correctness, so "it renders therefore it clears" lets wrong-but-well-rendered content through. The activity is a fine smoke test (see 15a) but cannot, by itself, certify the build — particularly with a known unexplained count gap in the same artifact.

  Specific risks: A build with accurate-looking but wrong content (wrong bio text, wrong node counts) passes the gate because it renders; the "constitutional check" provides false assurance.

  Mitigations available: Pair the visual verify with automated content assertions (expected thinker count, presence of each `**Summary**`, node-count invariants); make the visual check one layer, not the gate; record what the visual check does and does NOT cover.

  STEELMAN:
    Strongest counterargument: For a single-maintainer, low-stakes visualization, a human who knows the system glancing at the rendered page catches the failures that actually occur in practice; demanding a full automated content-assertion suite before every push is disproportionate ceremony that would halt iteration.
    What would need to be true for C2A2 to be safe: The failures that matter (wrong/missing content, count anomalies) are caught by cheap automated assertions, so the visual check is a complement, not the whole gate.
    How to test: Inject a wrong bio / wrong count into a build and see whether the manual visual verify catches it; if it passes, the check is insufficient as a gate.

  Search scope: limits of manual/visual QA; render-vs-content coverage; "looks right" fallacy / inattentional blindness. Comprehensive.

  Recommendation: CHALLENGED
