SEARCH-AGAINST-PRESUMPTION-720:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-720
  Original statement: That catching a defect proves the class is handled; "both caught by verification before anything was written" plus a correct generalisation ("distrust search date attributions structurally") that has no instrument, on the very field that gates ingestion.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-720
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a correct generalisation left without an instrument or backfill scope
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "Escaped Defects: Definition, Tracking & How to Reduce Them" (em-tools.io, plandek.com, 2026). Establishes that catching individual defects via spot verification does not change the escape rate for the defect class; only a systematic gate applied to every instance measurably reduces escapes, while ad hoc catches leave the class-level rate unmeasured.
    2. "Software Quality Gates: What They Are & Why They Matter" (testRigor, 2026). Distinguishes spot-check inspection (samples, catches individual instances) from quality gates (blocks every instance meeting a criterion) — a spot-check result only tells you the sampled cases were fine, saying nothing about the unsampled population.
    3. GhostCite: "A Large-Scale Analysis of Citation Validity in the Age of Large Language Models" (arXiv:2602.06718, 2026) [unverified — arXiv preprint, not confirmed peer-reviewed] and related metadata-hallucination studies. Document that hallucination/error rates on bibliographic and date-type metadata fields vary roughly 14–95% across models, and that these errors are frequent and unevenly distributed rather than rare one-offs — directly relevant to the "search date attribution" field named in this presumption.

  Strength of challenge: Strong

  Summary: The software-quality literature draws a sharp, well-established line between "a defect was caught" (an existence statement about one instance) and "the defect class is handled" (a claim about the whole population), and explicitly warns spot-verification catches do not license the population-level claim without a systematic gate or a measured escape rate. Independently, the LLM-metadata-hallucination literature shows date/citation-type fields are a documented hallucination hotspot with wide, non-trivial error rates, reinforcing that two catches provide weak evidence about the true underlying error rate on that specific field.

  Specific risks: If search-date attribution errors are more frequent than the two observed catches suggest, uncaught bad dates will pass verification and gate ingestion decisions, silently corrupting downstream date-dependent logic (freshness judgments, provenance chains) with no measurement of how often this happens.

  Mitigations available: Yes — standard practice is to convert ad hoc catches into either (a) a systematic automated cross-check of every search-date attribution against a second source, or (b) a measured escape/defect rate via retrospective sampling, rather than relying on the two known catches as reassurance.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-720
  Strongest counterargument: Two successful catches during manual verification is an existence proof, not a rate estimate; quality-engineering literature is explicit that spot-checks and gates answer different questions, and the LLM-metadata literature shows the specific field in question (search date attribution) is a documented hallucination hotspot with wide error rates — so the generalisation "distrust search date attributions structurally" is likely correct, but its correctness is exactly why leaving it uninstrumented is dangerous: a correct structural distrust with no structural check is a known anti-pattern.
  What would need to be true for C2A2 to be safe: Either a systematic, automated cross-check on every search-date attribution before ingestion, or a periodic sampling audit that estimates the actual escape rate — either would convert "we distrust this field" from a belief into a measured, bounded risk.
  How to test: Pull a random sample of already-ingested search-date attributions and independently re-verify them against source; a nonzero error rate in the sample, especially above an acceptable threshold, would confirm the presumption is currently false in practice.
