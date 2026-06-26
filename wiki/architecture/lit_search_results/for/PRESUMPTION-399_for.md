SEARCH-FOR-PRESUMPTION-399:
  Date searched: 2026-06-26
  Original item: PRESUMPTION-399
  Original statement: "That passing on-disk headless tests warrants a 'caching not logic' diagnosis (presumes jsdom/headless fidelity to the real iframe runtime)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-399
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: headless-test passage presumed to be faithful evidence about live-runtime logic
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Test-pyramid / fast-feedback testing literature (Fowler). - Headless/unit tests are a legitimate first-line signal and DO carry information about logic correctness; a green headless suite is weak positive evidence that pure logic paths are sound.

  Strength of support: Weak

  Summary: There is partial, weak support for using headless-test passage as ONE input to a diagnosis: such tests do exercise logic and a green result is genuine (if limited) evidence. But the support stops at "an input." The literature does not support treating headless passage as sufficient to EXCLUDE logic and conclude "caching, not logic," because headless environments (especially jsdom) omit real-runtime behavior. That gap is 15b's territory.

  Caveats: Headless evidence is necessary-not-sufficient; it cannot by itself license a "not logic" conclusion about the live iframe.

  Search scope: Test pyramid; headless test value. Adequate.

  Recommendation: PARTIALLY-SUPPORTED
