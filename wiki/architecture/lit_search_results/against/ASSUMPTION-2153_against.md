SEARCH-AGAINST-ASSUMPTION-2153:
  Date searched: 2026-11-21
  Original item: ASSUMPTION-2153
  Original statement: [stated, second-hand] The shared space is "what intelligence encounters (mathematics)", not the corpus.
  Search scope: PRELIMINARY. 8 web searches shared across the three 11-20 items (result titles seen, none opened). "title seen" = not opened; "recall" = searcher background knowledge, not re-read this run. One orchestrator ran 15a and 15b; all FOR files were composed before any AGAINST file, so independence is procedural only (cf. REVISE-545). Run: cloud-lit-2026-11-21.
  PROVENANCE:
    Origin: 14a
    Chain: 14a -> 15b
    Original item: ASSUMPTION-2153
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from local pass 2026-11-20 (second-hand report of the claim)
      15b: Searched for challenging literature (preliminary)
    Current status: PARTIALLY-CHALLENGED
  Challenging evidence found: Partial
  Sources:
    1. "Convergence without understanding: when language models agree on representations but disagree on reasoning" arXiv:2605.23315 (title seen). Representational agreement does not imply agreement in what the models do with it.
    2. "Reality and practice: a relational reading of the Platonic Representation Hypothesis" ICML 2026 (title seen). Reads convergence as tied to shared practices of data-making rather than to reality alone.
    3. "Exploring the Platonic Representation Hypothesis beyond in-distribution data" (LessWrong; title seen) and "An ontology of representations: limits of universality" (LessWrong; title seen). Informal work reporting that alignment weakens off the shared training distribution.
    4. "What converges in the Platonic Representation Hypothesis? Structure over geometry" arXiv:2609.27252 (title seen). If only coarse structure converges, "the same mathematics" is a stronger claim than the evidence.
    5. Huh et al. 2024 (recall): the authors list shared training data and shared architectural bias as alternative explanations they cannot rule out.
  Strength of challenge: Moderate
  Summary: The main challenge is a confound. Every model in the convergence studies was trained on human-made data from overlapping sources, so convergence cannot by itself show that the shared target is "what intelligence encounters" rather than the corpus. Follow-up work finds convergence is partial (structure, not geometry), weaker off-distribution, and does not extend to reasoning. None of this refutes the claim; it shows the current evidence cannot decide it.
  Specific risks: If C2A2 treats model convergence as evidence for a tradition-independent shared space, it may be reading back the shared corpus (largely English-language, Western-academic) as reality. That is the same correlated-evidence trap PREMISE-004's independence proviso warns about.
  Mitigations available: Treat the claim as a hypothesis; look for convergence across learners with different data (different languages, modalities, or non-human data) before relying on it.
  STEELMAN:
    Item: ASSUMPTION-2153
    Strongest counterargument: Every system shown to converge learned from the same human record. Convergence is exactly what you would expect if the corpus, not the world, were the attractor. A claim that the shared space lies beyond the corpus needs a test the corpus could not pass on its own, and none has been run.
    What would need to be true for C2A2 to be safe: Convergence holds across learners trained on disjoint data (e.g., separate language corpora, or physical-sensor data with no human text), or C2A2 does not lean on the claim for any design decision.
    How to test: Literature: watch for PRH tests on disjoint-data models. In-house: compare representations from models trained on different-language corpora where available.
  Recommendation: PARTIALLY-CHALLENGED
