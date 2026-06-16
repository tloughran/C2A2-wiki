SEARCH-FOR-PRESUMPTION-343:
  Date searched: 2026-06-12
  Original item: PRESUMPTION-343
  Original statement: "Disposition quality is batch-size invariant (a 188-item drain ≈ daily cadence quality)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-343
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference from 2026-06-11 EOD session
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Polanin et al., 2019. "Best Practice Guidelines for Abstract Screening Large-Evidence Systematic Reviews and Meta-Analyses." Research Synthesis Methods, 10(6). — Establishes that structured protocols with pre-specified eligibility criteria are the primary mechanism for maintaining screening consistency across large corpora. Protocol adherence, not batch size per se, is the primary determinant of quality. Training on ~20-30 representative items plus pilot testing further stabilises quality at volume.

    2. Guo & Siddharth (PMC6959565), 2020. "Error rates of human reviewers during abstract screening in systematic reviews." PLOS ONE. — Measured human reviewer error rates during abstract screening; found a total error rate of ~10.76%. Importantly, this baseline was relatively stable across session length when structured criteria were applied, though the study did not directly compare 188-item batch versus 10-item batch performance.

    3. Covidence / Systematic Review methodology guides (covidence.org). — Industry-standard guidance for systematic review screening recommends layered quality-control checks at multiple stages rather than limiting batch size, suggesting that structured protocols can maintain quality at high volume without necessarily requiring small batches. Multi-layered QC (first-level + second-level review + targeted QC) is the prescribed approach for high-volume projects.

  Strength of support: Weak

  Summary: The literature provides moderate support for the claim that structured protocols maintain quality at volume, and this is the best analogue to the C2A2 presumption. However, no directly applicable study compares a 188-item single-session batch against a distributed daily-cadence review on the same items with the same protocol. The systematic review literature consistently finds that reviewer fatigue is a real risk factor in large batches, and best practices recommend scheduling breaks and dividing work across sessions rather than assuming batch-size invariance. The claim as stated is therefore not supported in its strong form; a conditional form ("quality is approximately maintained if the structured protocol is followed carefully") is the most the literature supports.

  Caveats: A 2025 preprint (medrxiv 2025.09.02) specifically studied how batch size affects LLM screening performance, finding that performance does degrade as batch size increases — this is direct disconfirming evidence for the strong form of the claim (note: not reported here as this is a FOR search, flagged only as a caveat for scope completeness). Human reviewer studies consistently flag fatigue as a quality moderator. The claim's plausibility depends heavily on whether the AI agent performing the review is subject to analogous fatigue-like degradation.

  Search scope: Searched for: (1) structured review protocol quality at high volume, (2) systematic review screening batch size effects, (3) checklist effects on screening consistency, (4) reviewer fatigue in abstract screening. Preliminary — a targeted search on AI agent performance degradation with increasing task volume would be highly relevant.

  Recommendation: PARTIALLY-SUPPORTED
