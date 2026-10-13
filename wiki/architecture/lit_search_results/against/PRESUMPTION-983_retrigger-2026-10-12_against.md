SEARCH-AGAINST-PRESUMPTION-983 (RE-TRIGGER cycle 3):
  Date searched: 2026-10-12
  Original item: PRESUMPTION-983
  Original statement: [inferred] That where an in-house test is *written* determines whether it is ever
    run.
  Under test this cycle (MONITOR-609, Medium): the comparative limb only — machine-readable, co-located
    remediation is executed at a higher rate than the same remediation written in prose. (Determinative
    limb went to REVISE-469.) The MONITOR rests on human-literature support (Mehta 2022, +31.8 pp) with a
    NOVELTY-FLAG that no study covers autonomous-agent readers. Owed: the four-way in-house
    stratification (PLACEMENT / ADDRESSING / TOPIC-OWNERSHIP / COST vs executed-within-48h). That limb is
    in-house; I searched for challenges to (a) the robustness of the human evidence base and (b) the
    transfer to LLM-agent readers.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read lit_search_results/for/ or 15a sections of
    lit_search_returns.md. I read 15b's own cycle-0 AGAINST return. No fetch refused as "already fetched".

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 3)]
    Original item: PRESUMPTION-983
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b (2026-09-13): Inferred from the ASSUMPTION-1384 counter-example (SQL test inside failing row).
      15a (cycle 0): [not read — independence]
      15b (cycle 0, 2026-09-14): CHALLENGED (Strong) — PREMISE-164 (addressing, not medium);
        Sadowski et al. 2018; van der Sijs et al. 2006.
      15c: DISPOSITION-958 → MONITOR-609 (comparative limb), REVISE-469 (determinative limb).
      15d: re-triggers 09-27 (cycle 1), cycle 2, 2026-10-11 (cycle 3).
      15b (cycle 1, 2026-09-28): no new challenging evidence.
      15b (cycle 3, 2026-10-12): 4 searches (nudge meta-analysis bias; nudge units at scale; LLM
        position effects; instruction hierarchy); 2 fetches (Maier et al. 2022 full text; Wallace et
        al. 2024 abstract).
    Current status: CHALLENGED
    Sources this cycle: Maier et al. 2022 [full text]; Wallace et al. 2024 [abstract]; DellaVigna &
      Linos 2022 [search-result]; Liu et al. 2023 "Lost in the Middle" via secondary papers
      [search-result].
    Date: 2026-10-12

  EVIDENCE GRADE: MIXED — one full-text letter with a table, one abstract, two search-result summaries.

  Challenging evidence found: Yes

  Sources:
    1. Maier, M., Bartoš, F., Stanley, T. D., Shanks, D. R., Harris, A. J. L. & Wagenmakers, E.-J. (2022).
       "No evidence for nudging after adjusting for publication bias." PNAS 119(31):e2200300119.
       [fetched, full text incl. Table 1] Re-analysis of Mertens et al. 2022 with RoBMA: combined effect
       d=0.43 unadjusted → 0.04 adjusted (BF01=0.95); "structure" interventions (defaults, effort
       reduction — the class co-location belongs to) 0.58 → 0.12, evidence UNDECIDED (BF01=1.12);
       "assistance" (reminders, commitment) 0.22 → 0.01, evidence AGAINST (BF01=9.05); strong
       publication bias across subdomains; but heterogeneity everywhere except finance, "which implies
       that some nudges might be effective". Bearing: the human evidence class MONITOR-609 leans on
       (choice architecture / effort reduction) is undecided once bias is corrected; a +31.8 pp single
       estimate should not be imported as the expected effect size.
    2. DellaVigna, S. & Linos, E. (2022). "RCTs to Scale: Comprehensive Evidence from Two Nudge Units."
       Econometrica 90(1):81–116. [search-result/abstract summaries only] 126 RCTs, 23M people: nudge-
       unit trials average 1.4 pp vs 8.7 pp in academic-journal nudges; ~70% of gap explained by
       selective publication + low power. Bearing: scale failure — effects shrink by ~6x when every
       trial an organisation runs is counted, which is C2A2's situation (all in-house tests, no
       selection).
    3. Wallace, E., Xiao, K., Leike, R., Weng, L., Heidecke, J. & Beutel, A. (2024). "The Instruction
       Hierarchy: Training LLMs to Prioritize Privileged Instructions." arXiv:2404.13208. [fetched,
       abstract only] Models are trained to "selectively ignore lower-privileged instructions"; indirect
       injection via tool outputs is among targeted attack types (per search summaries, not verified in
       body). Bearing — a failed transfer specific to C2A2's readership: an instruction embedded in a
       data artefact (a failing status row, a tool result) is structurally the prompt-injection pattern
       that current models are deliberately trained to deprioritise. Co-location may LOWER execution
       likelihood for agent readers unless the agent's own (privileged) prompt tells it to execute tests
       found there. The 1384 counter-example fits this: the executing agent's procedure already
       addressed that artefact (the addressing/ownership reading of PREMISE-164).
    4. Liu, N. F. et al. (2023/2024). "Lost in the Middle: How Language Models Use Long Contexts."
       [search-result via later papers only; replication mixed] U-shaped position effect in long
       contexts; some replications find it task/length-specific. Bearing: for LLM readers, what matters
       may be position in context (start/end) and recency, not machine-readability — a different
       variable than the one MONITOR-609 proposes to stratify.

  Strength of challenge: Moderate-Strong (vs the comparative limb's evidential basis and its transfer
    to agents)

  Summary: The comparative limb's support comes from a human choice-architecture literature which, once
    corrected for publication bias, leaves effort-reduction effects undecided and reminder effects near
    zero, and whose at-scale effects are ~1/6 of published ones. For C2A2's actual readers (LLM agents),
    instruction-hierarchy training deliberately makes instructions embedded in data less, not more,
    likely to be followed. The four-way stratification remains the right test, but the literature now
    predicts that PLACEMENT will not separate outcomes once ADDRESSING is held fixed.

  Specific risks: the estate reformats tests into status rows (cheap), sees no change, and loses a cycle;
    or, worse, teaches agents to execute instructions found in data artefacts — a safety regression.

  Mitigations available: add a fifth stratum — whether the executing agent's own prompt names the
    artefact as a place to find runnable checks (privilege). Run the stratification on all tests in the
    window (no selection) and report denominators per PREMISE-168.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-983 / MONITOR-609 comparative limb
  Strongest counterargument: The human evidence that "putting the action where people trip over it"
    works is mostly publication bias — corrected, effort-reduction nudges are undecided and reminders
    do nothing, and at organisational scale effects shrink six-fold. C2A2's readers are not humans:
    they are LLMs explicitly trained to ignore instructions they find inside data rather than in their
    own prompts. A test written into a failing row is, to such a reader, an injected instruction. If
    co-location ever works, it works because the reader's own procedure already told it to look there —
    which is addressing, not placement.
  What would need to be true for C2A2 to be safe: the stratification shows a placement effect with
    addressing AND privilege held fixed, with denominators.
  How to test: as REVISE-469's four-way table plus a privilege column; minimum: compare co-located tests
    whose reader's prompt names that file vs co-located tests whose reader's prompt does not.

  Search scope: preliminary — 4 searches, 2 fetches. Novelty flag (no agent-reader study) stands; the
    instruction-hierarchy work is the nearest agent-side evidence and points against.
