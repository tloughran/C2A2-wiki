SEARCH-AGAINST-PRESUMPTION-364:
  Date searched: 2026-06-19
  Original item: PRESUMPTION-364
  Original statement: "[inferred] Local visual verify certifies correctness — rendering-correctness implies content-correctness (right brief, accurate text)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-364
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated render-implies-content inference
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Render-vs-content separation (testing fundamentals) — a page can render perfectly while displaying the wrong brief, stale text, or incorrect counts; presentation correctness and content correctness are orthogonal assertions. The inference render ⇒ content is a category error.
    2. Smoke-test coverage limits — visual smoke tests verify "it loads and lays out," explicitly NOT "the data/text is right"; relying on them for content correctness is using a test outside its coverage.
    3. Inattentional blindness / automation bias — humans glancing at a rendered page systematically miss non-salient content errors; the very fluency of a correct-looking render suppresses scrutiny of whether the content is actually right.

  Strength of challenge: Strong

  Summary: The inference is strongly challenged: rendering correctness does not imply content correctness — a flawless render can show the wrong brief or wrong numbers, smoke tests don't cover content, and human glances miss non-salient errors. This is a recognized verification fallacy, made concrete here by the unexplained ~256-vs-379 Summa count gap that a "looks fine" verify would not surface.

  Specific risks: Wrong/inaccurate bio text or wrong node counts ship because the page rendered; the "verify" gives false certification of correctness.

  Mitigations available: Add explicit content/fidelity assertions (expected text present, expected counts, each `**Summary**` non-empty and matching source); treat render-verify and content-verify as separate required checks; never let "it renders" stand in for "it's correct."

  STEELMAN:
    Strongest counterargument: In practice the maintainer reading the rendered bios IS checking content, not just layout, so the render/content split is academic here — a human reading the pop-ups verifies both at once.
    What would need to be true for C2A2 to be safe: The verify step actually reads and checks the CONTENT against the source (not just confirms it renders), and ideally automates the checkable parts (counts, presence).
    How to test: Render a build with a deliberately wrong bio and correct layout; if the verify passes, render-correctness is standing in for content-correctness illegitimately.

  STEELMAN note: This is the strong twin of ASSUMPTION-331; 331 over-claims sufficiency of the visual check, 364 makes the underlying render⇒content inference explicit.

  Search scope: render-vs-content separation; smoke-test coverage; inattentional blindness/automation bias. Comprehensive.

  Recommendation: CHALLENGED
