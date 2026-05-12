SEARCH-AGAINST-PRESUMPTION-076:
  Date searched: 2026-04-27
  Original item: PRESUMPTION-076
  Original statement: "Canonical-works fallback is methodologically equivalent to native wiki tradition entries"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-076
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated structural premise of ASSUMPTION-064
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Knowledge-curation-vs-extraction literature (Suchanek et al. 2007 on YAGO; Bollacker et al. 2008 on Freebase): native curation substantially outperforms on-the-fly extraction on structured queries because curation does the disambiguation, normalization, and structuring work upfront.
    2. RAG-failure-mode literature (Shi et al. 2023 "Large Language Models Can Be Easily Distracted by Irrelevant Context"; Liu et al. 2023): retrieval over canonical works adds noise, and downstream syntheses can be derailed by irrelevant retrieved content.
    3. Synthesis-quality differential: native curated entries encode the curator's editorial judgment about what's relevant; canonical-works fallback retrieves text without that judgment.
    4. Operational-asymmetry: in C2A2, the original 11 traditions have detailed curated entries with PRS-triplet decomposition; Wright and Rohr would lack equivalent decomposition until manually curated, creating quality asymmetry.
    5. Long-tail-knowledge literature (Mallen et al. 2023): canonical works in training data are not uniformly well-represented; specific scholarly debates and minority readings may be underrepresented compared to curated entries.

  Strength of challenge: Moderate

  Summary: The literature consensus is that native curation outperforms canonical-works fallback for structured downstream tasks, especially when the curation step encodes editorial judgment. The presumption's "methodologically equivalent" framing is too strong; the more accurate framing is "operationally substitutable with quality cost." For C2A2's PRS-triplet-driven syntheses, the quality cost is non-trivial.

  Specific risks: (a) Quality asymmetry between original 11 and added Wright/Rohr propagates downstream; (b) cross-program signal recognition is biased toward traditions with native curation; (c) syntheses citing "the C2A2 reading of Wright" are actually using on-the-fly extraction, not curated reading.

  Mitigations available: (a) Native curation for Wright and Rohr before treating them as load-bearing; (b) explicit tagging of fallback vs. native entries in dispatch records; (c) downstream syntheses note when they rely on fallback rather than native.

  Recommendation: CHALLENGED ("methodologically equivalent" is too strong; the literature treats native curation as substantially superior for structured downstream use)

  STEELMAN:
    Item: PRESUMPTION-076
    Strongest counterargument: Native curation does work that canonical-works fallback cannot replicate: editorial judgment about what's relevant, disambiguation, PRS-triplet structuring, cross-program seed identification. Treating the two as equivalent imports a quality asymmetry into the system that downstream consumers cannot see. The asymmetry is the kind of designer-unaware drift that PRESUMPTION-tagged items deserve extra scrutiny on.
    What would need to be true for C2A2 to be safe: (a) Wright and Rohr receive native curation matching the original 11's depth before downstream syntheses depend on them; (b) fallback entries are explicitly tagged as such; (c) syntheses cite the source type (native vs. fallback) for each input.
    How to test: Run a representative cross-program synthesis once with fallback Wright and once with native curated Wright; compare quality metrics (specificity, technical depth, accurate citation). If the gap is large, equivalence is locally falsified.
