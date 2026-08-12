SEARCH-FOR-PRESUMPTION-720:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-720
  Original statement: That catching a defect proves the class is handled; "both caught by verification before anything was written" plus a correct generalisation ("distrust search date attributions structurally") that has no instrument, on the very field that gates ingestion.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-720
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a correct generalisation left without an instrument or backfill scope
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Fabrico, "AQL Sampling vs 100% Inspection: When Checking Everything Is the Wrong Answer" and related QC literature — [unverified — from search snippet] establish the formal quality-control distinction between spot-check/sampling inspection (a per-instance catch) and a systematic gate (a control applied to every unit going forward); crucially cites that "manual 100% inspection is surprisingly unreliable — human inspectors miss 20-30% of defects" and that "the durable answer is quality-at-source, mistake-proofing and process control that stop the defect being made" rather than relying on catches. This directly supports the structural claim that a caught instance does not, by itself, constitute a gate.
    2. Thinking Tester, "Logical Fallacies for Testers VII: The Hasty Generalization Fallacy" and PractiTest, "How Cognitive Bias Affects Software Testing" — [unverified — from search snippet] name the exact fallacy at issue: generalizing from one or two passing/caught test instances to a conclusion that the broader class is now handled, and document this as a well-recognized, named failure pattern in QA practice ("the hasty generalization fallacy is very dangerous in software testing because it results in not testing enough").
    3. GhostCite / CiteCheck line of work on LLM citation and metadata hallucination (arXiv:2602.06718, arXiv:2605.27700) — [unverified — from search snippet] reports empirically that LLM-generated date/publication metadata is unreliable at scale (one study found hallucination rates "peaking at 98.75%" for certain publication-year attributions, and citation-validation accuracy of only 38%, below chance), and that verification requires dedicated instrumentation (grounding metadata against external sources, requiring verbatim evidence spans) rather than ad hoc catches. This is strong empirical precedent for exactly the mechanism PRESUMPTION-720 flags: search/retrieval date attributions are a known-unreliable field class requiring a structural check, not spot verification.

  Strength of support: Strong

  Summary: The literature converges cleanly on this presumption from three independent angles: industrial quality control (sampling/inspection theory), software-QA cognitive-bias literature (the hasty generalization fallacy, named explicitly), and recent empirical NLP work on LLM date/citation metadata hallucination (which quantifies the underlying risk as very high and shows ad hoc/manual catches are known to be an unreliable substitute for a grounding instrument). All three bodies of evidence support the same conclusion: catching a defect in one or two instances does not establish that a field class is under control, and date-type metadata from LLM-mediated search specifically is documented in the literature as a high-hallucination-rate field warranting a structural check rather than spot-checking.

  Caveats: The QC and QA-fallacy sources are general software/manufacturing literature, not specific to LLM search-date attribution — the mapping to C2A2's case is by analogy. The citation-hallucination figures (e.g., 98.75% for certain publication years, 38% validation accuracy) come from arXiv preprints in a fast-moving area (2026) and are flagged [unverified — from search snippet]; exact figures should be treated as illustrative of a real, large problem rather than as precise transferable base rates for C2A2's specific search/date pipeline. No source addresses the specific remediation question 14b raises — what "backfill scope" is needed once the generalization is made — this is a gap not covered by the retrieved literature and is noted as an open question rather than resolved.

  Recommendation: PARTIALLY-SUPPORTED
