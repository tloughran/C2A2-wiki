SEARCH-AGAINST-PRESUMPTION-1119:
  Date searched: 2026-10-10
  Original item: PRESUMPTION-1119
  Original statement: [inferred] The orchestrator normalises agent outputs after the fact (relabelling
    "CLOSED" to INCORPORATE; adding an omitted PROVENANCE block) while reporting agents' work as
    independent. Question: does post-hoc normalisation of independent reviewers' outputs bias the
    record, and how should it be reported?
  Under test: the implied premise that post-hoc normalisation biases the record and compromises
    independence. I searched for evidence that editorial harmonisation is standard, benign and
    accepted practice (data harmonisation, reconciliation in systematic reviews, editor editing of
    peer-review reports).

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output from today.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1119
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b (2026-10-09): Inferred from orchestrator behaviour that agent outputs are normalised post
        hoc while described as independent; queued with bias/reporting question.
      15b (2026-10-10): Searched for challenging literature. 3 searches (Maelstrom retrospective data
        harmonisation; editors editing reviewer reports; reconciliation of independent extraction in
        systematic reviews); 2 fetches (COPE 2020 survey, full text; Cochrane Handbook v5.1 §7.6.5,
        full text). No fetch failures.
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: PRELIMINARY. Two full-text fetches (both short documents); rest search-result.

  Search scope: preliminary (3 searches, 2 fetches).

  Challenging evidence found: Partial
  Strength of challenge: Moderate (against "normalisation is inherently biasing"); Weak (against
    "it must be reported")

  Sources:
    1. Fortier I et al. 2017. "Maelstrom Research guidelines for rigorous retrospective data
       harmonization." International Journal of Epidemiology 46:103-105 (PMC5407152). [search-
       result] Retrospective harmonisation (recoding heterogeneous study outputs into a common
       DataSchema) is "widespread practice" in pooled research. One case harmonised 81.6% of
       variables across 12 cohorts. Bearing: mapping independent producers' outputs into a shared
       vocabulary (e.g. "CLOSED" → INCORPORATE) is a standard, legitimate step, not tampering per se.
       The guidelines also stress documenting the algorithms, which supports the reporting half of
       the item.
    2. COPE Council. 2020. "Editing of reviewer comments — Survey results." doi:10.24318/gyZ99iXA.
       [fetched, full text] 145 respondents: 39% said editing peer reviews is acceptable, 13%
       "sometimes", 14% "depends", 34% "no" (the summary states about 15% think it is never
       acceptable). Reasons: copyediting, non-adherence to journal guidelines, inflammatory or
       factually incorrect content. Of editors who edit, about 61% (67/109) always or sometimes note
       it in the system, so many do NOT record it. The minority view warns of "too much power" and a
       "slippery slope". Bearing: in the closest human analogue (an editor relaying independent
       reviewers' outputs), format and compliance normalisation is mainstream and is not generally
       regarded as destroying reviewer independence. HONEST COUNTER: the same survey records real
       concern and uneven disclosure.
    3. Fidler F & Hoekstra R (survey of journal editors, as reported by Enago Academy / The
       Publication Plan). [search-result] 91% of editors would edit a peer-review report. 8% would
       change the recommendation without permission. Bearing: light editing is near-universal.
       Changing the substantive verdict is the line most editors will not cross.
    4. Cochrane Handbook v5.1, §7.6.5 "Reliability and reaching consensus." [fetched, full text]
       Independent extractions are reconciled ("Most often, the source of the disagreement is an
       error by one of the extractors and is easily resolved"), and the review proceeds on the
       consensus data. "Maintaining a copy of the data 'as extracted' (in addition to the consensus
       data) allows assessment of reliability." Bearing: post-hoc correction of independent outputs
       is standard and does not void their independence, PROVIDED the raw outputs are kept. Kappa on
       pre-consensus data is "not routinely done", so even here full reporting is optional.
    5. JBI Manual 4.2.8; Covidence workflow (search-result). Standard pipeline: independent
       extraction, then consensus or third reviewer. The final dataset is by design not "independent
       outputs". It is reported as independently extracted and then reconciled.

  Summary: The literature challenges the premise that post-hoc normalisation inherently biases the
    record. In data harmonisation, systematic-review reconciliation and journal editing, an
    integrating party routinely recodes, corrects and formats independent producers' outputs. The
    standard description is still "independently extracted/reviewed, then harmonised". The two
    examples in the item (vocabulary mapping CLOSED → INCORPORATE; adding a missing boilerplate
    PROVENANCE block) are the format/compliance class that the editorial literature treats as
    acceptable. The line drawn in practice is at changing substantive judgments (for example a
    reviewer's recommendation). The challenge does not reach the reporting question. Every source that
    addresses it (Maelstrom, Cochrane's "as extracted" copy, the COPE minority concern) favours
    keeping the raw output and documenting the transformation.

  Specific risks if the premise is over-applied: Treating all normalisation as contamination could
    stop the orchestrator from making the outputs comparable, leaving the record unusable or forcing
    re-runs. If the premise is under-applied: vocabulary mappings can hide substantive differences
    (is "CLOSED" truly INCORPORATE, or something else such as "resolved, no action"?), and an added
    PROVENANCE block written by the orchestrator asserts a chain the agent did not attest.

  Mitigations available: Keep the raw agent output alongside the normalised version. Mark
    orchestrator-added fields (e.g. "PROVENANCE: added by orchestrator"). Classify each normalisation
    as format-only or semantic. Only semantic mappings need review.

  STEELMAN:
    Item: PRESUMPTION-1119
    Strongest counterargument: Every serious multi-reviewer process has an integrating step that
      harmonises independent outputs into a common schema. Systematic reviews reconcile double
      extraction, pooled cohorts recode into a DataSchema, and journals copyedit and standardise
      reviewer reports. None of these regard the step as voiding the producers' independence.
      Independence concerns how judgments were formed, not whether their labels were later mapped to
      a shared vocabulary. Calling relabelling and boilerplate insertion "bias" conflates format
      with substance and would make every harmonised dataset in epidemiology "biased".
    What would need to be true for C2A2 to be safe: The normalisations are format-only (the mapping
      preserves meaning). Raw outputs are retained. Orchestrator-authored fields are distinguishable
      from agent-authored ones.
    How to test: Diff raw against normalised outputs for a sample of runs. Classify each change as
      format or semantic. Check whether any normalisation changed a status category in a way the
      agent would dispute (re-ask the agent on whether "CLOSED" maps to INCORPORATE).

  Boundary conditions identified:
    - Benign only for format and vocabulary normalisation. Changing a verdict or recommendation is
      the line the editorial literature itself treats as unacceptable (Fidler & Hoekstra: 8% would).
    - Benign only if raw outputs are retained (Cochrane "as extracted" copy). Overwriting in place
      removes auditability.
    - Inserting a PROVENANCE block is a special case. Provenance is an attestation, so an
      orchestrator-written one is a claim made on the agent's behalf. That is closer to "changing the
      substance" than copyediting is.

  Recommendation: PARTIALLY-CHALLENGED

  SYSTEMIC-RISK-FLAG: shared with ASSUMPTION-1757, PRESUMPTION-1115, PRESUMPTION-1117,
    PRESUMPTION-1118. Common vulnerability: binary corrections plus added meta-process; the literature
    favours graded, documented handling (raw plus transformation record). Risk level: High. Full flag
    text in PRESUMPTION-1117_against.md.
