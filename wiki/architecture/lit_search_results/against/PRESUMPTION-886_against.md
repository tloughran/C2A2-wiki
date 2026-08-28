SEARCH-AGAINST-PRESUMPTION-886:
  Date searched: 2026-08-28
  Original item: PRESUMPTION-886
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority High)
  Original statement: [inferred] That a single-valued approval token adequately records a curation decision —
    that endorsement and non-objection need not be distinguished, and that provenance and confidence need not
    travel with the item.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-886
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the schema — the question was asked in prose on the same day the data was written
        without it; DECISION-083 used as internal control.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED (the remedy, not the diagnosis)

  Search scope: WebSearch, 2026-08-28, one dedicated query on annotation burden and provenance overhead.
    Reached: Springer's "Capturing Interactive Data Transformation Operations Using Provenance Workflows";
    a survey of data provenance in e-Science (ResearchGate 220415414); the CEUR paper on automatic metadata
    annotation through reconstructed provenance; NHIMG's provenance-metadata entry; arXiv 1308.4618 on
    inferred provenance for detecting erroneous annotation. NOT COVERED: the peer-review literature on
    reviewer confidence scores, which is the closest analogue to endorsement-vs-non-objection and which
    neither direction has now reached. All SNIPPET-ONLY. Confidence: MODERATE.

  Challenging evidence found: Yes — against the richer schema as a manual requirement

  Sources:
    1. CEUR-WS Vol-856 paper 4, "Automatic Metadata Annotation through Reconstructing Provenance"
       [SNIPPET-ONLY] https://ceur-ws.org/Vol-856/paper_4.pdf —
       States the trade directly: user-annotation approaches impose a low burden on the application and a
       high burden on the humans, and user-centred metadata is "often incomplete and inconsistent." A richer
       approval token filled in by hand is predictably filled in badly.
    2. Survey of data provenance in e-Science (ResearchGate 220415414) [SNIPPET-ONLY; authors unverified] —
       Where provenance depends on manual annotation, the burden prevents complete machine-readable
       provenance from being recorded at all; and provenance management carries collection and storage cost.
    3. NHIMG, "Provenance metadata" [SNIPPET-ONLY] https://nhimg.org/glossary/provenance-metadata/ —
       Rigorous provenance introduces storage, performance and governance overhead, and organisations are
       advised to weigh forensic certainty against capture cost.
    4. Springer, "Guest editorial: large-scale data curation and metadata management," Distributed and
       Parallel Databases (2017), doi:10.1007/s10619-017-7217-x [SNIPPET-ONLY] —
       Records that scientists become more reluctant to share as annotation requirements grow more onerous;
       i.e. the richer schema can reduce the number of items that get recorded at all.

  Strength of challenge: Moderate

  Summary: The diagnosis stands — a single approval value does lose information, and the standards literature
    the for direction found specifies graded, confidence-bearing, travelling provenance. The challenge is to
    the fix. Every source reached that has measured manual annotation reports the same two results: the
    burden falls on the human, and the resulting metadata is incomplete and inconsistent — which means a
    richer approval token collected by asking the reviewer for more would degrade rather than improve the
    record, and in the limit reduces how much gets approved at all. The consistent recommendation is to
    derive the richer value automatically from signals already present, not to add fields. Applied here: the
    depth of a review is partly observable (time spent, items touched, whether the reviewer wrote anything),
    and a derived confidence is more likely to survive than a requested one.

  Specific risks: Adding a confidence field to the approval schema in an estate whose reviewer is
    intermittently available produces a field that is either empty or set to a default, at which point the
    estate has a *second* single-valued token and believes it has two dimensions.

  Mitigations available: Derive rather than request. Record what is already observable at approval time and
    let the confidence be a function of it; reserve a manual field for explicit dissent only, which is cheap
    to supply and informative when present.

  STEELMAN:
    Item: PRESUMPTION-886
    Strongest counterargument: The burden argument is calibrated to large scientific collaborations
      annotating millions of records. This estate approves a handful of items per day, and the marginal cost
      of one additional keystroke distinguishing "endorsed" from "not objected to" is negligible against the
      cost of a downstream reader mistaking the second for the first. Burden findings from a high-volume
      regime do not transfer to a low-volume one, and invoking them here is a domain-transfer error of
      exactly the kind this pipeline is supposed to catch.
    What would need to be true for C2A2 to be safe: approval volume would have to stay low enough that the
      marginal annotation cost remains negligible, and the distinction would have to be one the reviewer can
      make without deliberation.
    How to test: add the distinction as a two-value field for one month and measure the fill rate. If it is
      near 100%, the burden objection is refuted in-house; if it defaults, the objection is confirmed.

  Recommendation: PARTIALLY-CHALLENGED
