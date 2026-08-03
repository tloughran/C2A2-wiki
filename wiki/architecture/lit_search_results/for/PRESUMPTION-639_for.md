SEARCH-FOR-PRESUMPTION-639:
  Date searched: 2026-08-03
  Original item: PRESUMPTION-639
  Original statement: That a terminal summary artifact is epistemically downstream of its
    sources — a faithful reduction — rather than itself an independent source of error.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-639
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from six divergences measured against the registers, plus the
           structural absence of any verification apparatus (origin ASSUMPTION-672)
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. A Systematic Survey of Text Summarization, 2025. ACM 10.1145/3731445 —
       establishes that faithfulness is an achievable and measurable property, and that
       modern systems attain it under evaluation. Supports the claim conditionally: a
       summary *can* be downstream-only.
    2. CoTHSSum: structured long-document summarization, 2025. J. King Saud Univ. CIS
       10.1007/s44443-025-00041-2 — hierarchical segmentation preserves logical content
       flow and improves source coverage; distortion is reducible by construction.
    3. A study of extractive summarization incorporating hierarchical information, 2024.
       Sci Rep s41598-024-60779-z — extractive methods bound distortion by construction,
       since spans are copied rather than regenerated.

  Strength of support: Weak

  Summary: The literature supports the claim only in the conditional form: a summary is
  epistemically downstream *if* it is built with faithfulness constraints and evaluated
  against them. Every supporting source treats faithfulness as an engineering achievement
  requiring specific mechanisms — extractive copying, hierarchical segmentation,
  faithfulness metrics — not as a default property of the summarising relation. Applied
  to C2A2, the support is contingent on apparatus the artifact in question does not have:
  14b records that it is the only file in architecture/ with no provenance header, no
  verification section and no fail-loud footer. The literature therefore does not support
  the claim as it holds in this system; it supports what would have to be added.

  Caveats: Publication bias is acute in this area — the summarization literature is
  written by people building summarizers, and reports of successful faithfulness are
  over-represented relative to deployed failure. The general survey literature also
  explicitly notes a summarization/information-loss trade-off, which cuts the other way
  and is picked up by 15b.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Adequate for the summarization side; the organisational
  upward-reporting-bias literature returned thin results and is a known gap. Broader
  search into management-science reporting distortion recommended.
