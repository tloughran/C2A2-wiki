SEARCH-FOR-ASSUMPTION-421:
  Date searched: 2026-07-07
  Original item: ASSUMPTION-421
  Original statement: "Re-running a completed baseline protocol duplicates artifacts; a structurally identical 3,000-line file two runs later is clutter, not measurement."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-421
    Item type: ASSUMPTION (stated); Priority LOW
    Transform at each step:
      14a: Extracted from the 2026-07-06 autonomous-Monday EOD sources (sewing bootstrap verification report comparing the weekly connectivity census against the older bootstrap census protocol)
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Smithsonian Libraries, 2018. "Research Data Management Best Practices." — States explicitly that "drafts of papers, duplicate copies, superseded versions of datasets, beta versions of software, and other working files are transitory in nature and should probably not be preserved indefinitely," directly supporting the view that a re-run superseded artifact is clutter rather than something to retain.
    2. Office of Research Integrity (HHS), "Why Duplication and Other Forms of Redundancy Must Be Avoided." — Argues that covert data reuse and redundant duplication distort downstream aggregation (e.g., meta-analysis treating dependent data as independent), grounding the claim that a needless duplicate can actively harm the integrity of the record, not merely waste space.
    3. Alation, "Data Duplication: When It Helps, When It Hurts, and How to Manage It." — Frames duplication as context-dependent: redundant copies inflate storage/processing cost and create governance risk when they carry no new informational content, supporting "clutter" for a byte-identical re-run.
    4. Puljak et al., 2023. "Definition, harms, and prevention of redundant systematic reviews." PMC10071231. — Establishes a formal concept of "redundant" repeated work: repetition that adds no new evidence is a recognized harm (wasted resources, reader confusion), analogous to a redundant census re-run.

  Strength of support: Moderate

  Summary: The research-data-management and research-integrity literature clearly supports the general principle that a repeated artifact carrying no new informational content is redundant clutter and, in some framings, an active liability (it can distort aggregation and waste governance/storage resources). Superseded working files and duplicate copies are explicitly named as transitory and not worth indefinite preservation. However, the literature is equally clear that the redundant/valuable distinction turns entirely on whether the re-run carries NEW information — which the claim asserts (structurally identical) but does not prove. The support is therefore for the conditional ("IF byte-identical and no new information, THEN clutter"), not for the factual premise that a two-runs-later census is in fact identical.

  Caveats: Support weakens sharply if the re-run is a replication measurement rather than a duplicate — the replication literature (see ASSUMPTION-421 counter-considerations) values repeated measurement for calibration, drift detection, and variance estimation. "Structurally identical" is doing heavy lifting: two census runs separated in time over a changing vault would normally NOT be identical, and even an identical result can be an informative negative (confirms no drift). The cited sources concern human-curated research datasets, not automated recurring census logs, so transfer is analogical.

  Recommendation: PARTIALLY-SUPPORTED
