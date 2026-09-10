SEARCH-AGAINST-PRESUMPTION-944:
  Date searched: 2026-09-10
  Original item: PRESUMPTION-944
  Original statement: [inferred] A report delivered to the designer in speech is not an artefact, and
    so is not subject to the verification discipline applied to files.
  Risk if wrong, as stated at intake: Critical — two consecutive days of false morning reports to Tom
    (ASSUMPTION-1293, ASSUMPTION-1300) on the only channel that reaches him.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-944
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference from two consecutive mornings on which a spoken/terminal report to the
        designer asserted "nothing is broken" / "otherwise nothing broken" and was falsified in-run
        against three and four same-morning sources respectively, while the file-level verification
        discipline that would have caught it was applied only to files.
      15b: Searched for challenging literature (2026-09-10), AGAINST direction only. Did not read the
        `for/` directory, `lit_search_returns.md`, or any 15a output for this item. Read this lane's
        own 2026-09-09 SYSTEMIC-RISK-FLAG first, per the intake instruction.
    Current status: CHALLENGED

  PRIOR-ART CHECK, run first per the intake note ("the 09-09 SYSTEMIC-RISK-FLAG is the same shape;
  read it before searching"): **the shapes are adjacent but not identical, and the difference is the
  reason this item needs its own answer.** The 09-09 flag is about ABSENCE — no signal being read as
  no condition. This item is about a POSITIVE ASSERTION delivered in a channel exempted from
  verification. In both morning cases something was said, not merely unsaid: "nothing is broken" is a
  claim with a truth value, made to the one recipient who acts on it, and it was false. The 09-09
  flag's remedy — an expectation register with an external reader — does not reach it, because the
  report was not missing. So the estate did NOT already hold this answer, and the search was
  warranted. What the estate does hold:
    - **PREMISE-109** (ACTIVE, High confidence): "A summarizing agent is a view over its own read set,
      not a view over the system... a health claim not bound to a named artifact with a timestamp is
      not evidence of health, and 'no failures to report' must be legible as scoped." This is the
      closest existing entry and it is decisive for the CONTENT of the morning report. What it does
      not say is that the spoken channel is subject to it. That gap is PRESUMPTION-944.
    - **PREMISE-194** (ACTIVE, High): an agent's in-session recollection of its own work is not an
      independent copy of the record; corroboration requires an artefact produced by a different
      process, "cited directly rather than narrated." The word "narrated" is doing exactly this item's
      work and the premise is already ACTIVE.
    - **PREMISE-195** (ACTIVE, High, and flagged as the estate's highest open risk): voluntary
      self-report is not a detection control.
    - **PREMISE-102** (fail-loud is reporting, not remediation) and **PREMISE-188** (a qualifier
      travels with the claim or it does not travel).
    CORRELATION DISCLOSURE: this file's conclusion overlaps PREMISE-109 and PREMISE-194 heavily and
    must not be counted as independent corroboration of either. Its increment is the CHANNEL claim —
    that the verification discipline is bound to the artefact type rather than to the assertion — plus
    two measured base rates for degradation in the spoken channel specifically, which no existing
    premise carries.

  Challenging evidence found: Yes — with the strongest single measurement in this run's whole batch.

  Sources:
    1. "An Experimental Comparison of Handover Methods," *Annals of the Royal College of Surgeons of
       England* (2007), doi 10.1308/003588407X168352.
       [**VERIFIED — full text retrieved and read in full this run.** Author list NOT stated: the
       retrieved text did not carry the byline and I did not confirm it separately, so the paper is
       cited by title, journal, year and DOI only. Every figure below is verbatim from the text I
       read.] — Design: 12 fictional patients, 20 data points each, handed over between ENT SHOs over
       five consecutive cycles, in three styles, scored by two independent blinded observers with tape
       adjudication of disagreements. Results: **of 80 data points in the verbal-only group, 26 (33%)
       were retained after the FIRST handover and 2 (2.5%) after five cycles.** Verbal-with-note-taking
       retained 92% after one cycle and 85.5% after five. The printed handout retained 100% through
       four cycles and lost one point (1.25%) in the fifth. And the finding that matters most for this
       item, because it forecloses the obvious defence: **"data points deemed important were omitted at
       a similar rate as those deemed less important."** In the verbal-only group, 2 of 64 important
       points (3%) survived five cycles and none of the less-important points did; the authors state
       "even essential information that may result in serious morbidity could be lost." The paper's own
       stated limitations are recorded here rather than suppressed: n=5 participants, simulated
       patients, a quiet room with no interruptions, and an acknowledged high data-point load per
       patient. It is a small artificial study. It is also the only controlled experimental comparison
       of handover channels I located, its effect size is enormous, and its direction is unambiguous.

    2. Tang, L. et al. (2024), "TofuEval: Evaluating Hallucinations of LLMs on Topic-Focused Dialogue
       Summarization," arXiv:2402.13249 (NAACL).
       [**VERIFIED — PDF retrieved and Table 2 read directly this run.** Author list beyond the first
       author NOT confirmed and is therefore not stated. The benchmark contains 1.5K topic-focused
       summaries with expert linguistic annotators performing binary sentence-level factuality
       judgements.] — Table 2, summary-level factual inconsistency rates, averaged over five
       summarisers: MediaSum 37.2% (main topic) / 46.0% (marginal topic); MeetingBank 30.4% / 43.6%.
       Best single model (GPT-3.5-Turbo): 22.2% / 27.2% / 10.9% / 19.8%. The paper's own headline is
       "LLMs we studied make a significant amount of factual errors, especially on the summary level,"
       and it reports that models produce MORE inconsistency when asked about a MARGINAL topic,
       "bringing unsupported information into the summary" where the topic is barely present in the
       source. **BOUNDARY CONDITION, load-bearing and stated against my own direction:** the
       summarisers are Vicuna-7B, WizardLM-7B/13B/30B and GPT-3.5-Turbo. These are 2023-vintage models
       and the figures should NOT be transferred to a current-generation agent without discount. What
       transfers robustly is not the rate but the two structural findings: summary-level error is much
       higher than sentence-level error (aggregation compounds), and error rises sharply where the
       source material barely covers the topic being asked about. A morning report asserting "nothing
       is broken" is a summary-level claim about a topic on which the read set is largely silent —
       the marginal-topic condition exactly.

    3. Handover omission and congruence measurements, corroborating source 1 in the field rather than
       the laboratory.
       [SNIPPET-ONLY — figures from search summaries of the nursing-handoff literature (AHRQ *Patient
       Safety and Quality*, NCBI Bookshelf NBK2649) and a structured-checklist pilot (PMC8286430);
       neither opened; author lists not stated.] — Reported: one study found 70% congruence between
       the shift report and the patient's actual condition, with a 12% omission rate; a structured
       handover checklist in surgery reduced information omission from 19.5% to 12.1% between scrubs
       and 16.8% to 14.1% between circulators. Bearing: even in the field, with real stakes and
       trained professionals, the spoken report diverges measurably from the state it describes, and
       the best available intervention moves the omission rate by single-digit percentage points
       rather than eliminating it.

    4. INTERNAL, non-independent: PREMISE-109, PREMISE-194, PREMISE-195, PREMISE-102, PREMISE-188;
       and this lane's SYSTEMIC-RISK-FLAG of 2026-09-09, whose relationship to this item is analysed
       above rather than assumed.

  Strength of challenge: Strong

  Summary: The presumption draws the verification boundary around the artefact type. Every source I
  found draws it around the assertion, and the one controlled experiment in the set says the spoken
  channel is the WORST channel, not an exempt one — 2.5% of information surviving five verbal-only
  handover cycles, against 99% for a printed sheet, with important facts lost at the same rate as
  unimportant ones. That last clause is what kills the natural defence, which would be that a spoken
  report is a summary and summaries legitimately compress: the experiment shows the compression is not
  selective, so "the important things get through" is not available. The machine-side literature says
  the same thing from the other end: summary-level factual inconsistency in an expert-annotated
  benchmark ran at 30–46% averaged across summarisers, was markedly higher than sentence-level error,
  and rose further when the model was asked about a topic its source barely covered — which is
  precisely the shape of "nothing is broken," a summary-level assertion about the absence of things in
  a read set that does not contain them. And the register already contains the conclusion in general
  form. PREMISE-194, ACTIVE at High confidence since 31 August, holds that corroboration requires an
  artefact from a different process "cited directly rather than NARRATED"; PREMISE-109, ACTIVE at High
  confidence since July, holds that a health claim not bound to a named artefact with a timestamp is
  not evidence of health, and that "no failures to report" must be legible as scoped or it is
  unfounded. Neither premise contains an exemption for speech. So the presumption is not merely
  unsupported — it is inconsistent with two ACTIVE High-confidence premises, and the inconsistency
  survived because both premises were read as governing files. Finally the reflexive point, which the
  intake's Critical rating already implies: the spoken channel is the ONE channel with a human at the
  far end, and it is the one channel where an error cannot be caught by a later reader, because there
  is no later reader. The estate applies its strictest discipline to artefacts that agents read twice
  and its weakest to the assertion that reaches the only party who can act.

  Specific risks: (a) The realised risk is not hypothetical and does not need modelling: two
  consecutive mornings, both falsified in-run against three and four same-morning sources. That is a
  measured 2-for-2 on the estate's own instance count, and while n=2 supports no rate, it does
  establish that the failure occurs and that it occurs consecutively. (b) The asymmetry risk is the
  structural one: a false artefact can be caught by any later reader; a false spoken report has no
  later reader, so its error rate is bounded below only by the designer's own scepticism. The channel
  with the least verification is the channel with the highest consequence and the shortest correction
  path. (c) The "nothing broken" form is the specific hazard, and both TofuEval's marginal-topic
  finding and PREMISE-109 converge on why: it is an assertion about absence, made from a read set
  whose silence is indistinguishable from the world's silence. TofuEval's models filled marginal
  topics with unsupported material; the estate's runs filled an absence with an all-clear. (d)
  Compounding with the rest of this batch: PRESUMPTION-940's unverified configuration state and
  PRESUMPTION-939's uncontained findings both feed the morning report. A verification discipline that
  stops at the file boundary lets defects that were correctly recorded in files be incorrectly
  summarised in speech, which means the file-level rigour is partially wasted at the last hop. (e) The
  trust risk, stated plainly because it is the one that matters longest: a designer who discovers two
  false all-clears has rational grounds to discount all future reports, including the true ones, and
  there is no mechanism in the estate for earning that back other than not doing it again.

  Mitigations available: The literature's answer is unusually concrete and cheap here, because the
  controlled experiment tested the remedies directly.
    (i)   **Do not deliver the report verbally-only. Deliver it against a written artefact.** This is
          the experiment's own finding — 2.5% versus 99% retention — and it is the highest-value,
          lowest-cost change available. The morning report should be a file, and the spoken delivery
          should be a reading of that file, so that the assertion becomes inspectable after the fact
          by someone other than the speaker. This single change converts the item's premise from true
          to irrelevant.
    (ii)  **Apply PREMISE-109's existing rule to the spoken channel explicitly.** Every health claim
          in a report to the designer must name an artefact and a timestamp, and "no failures to
          report" must be rendered in its scoped form — "no failures appear in the sources I read,
          which were X, Y, Z, as of T." The premise already requires this; the amendment is one clause
          saying that it binds regardless of delivery medium.
    (iii) **Forbid the unscoped all-clear specifically.** Per PREMISE-110's polarity argument and
          TofuEval's marginal-topic finding, the sentence "nothing is broken" is the highest-risk
          sentence the estate can emit, because it is an assertion about absence generated from a
          silent read set. The affirmative form — "these N checks ran, at these times, with these
          results" — carries the same information and cannot be produced by a silent read set.
    (iv)  **Structure the handover.** The field literature's measured intervention is a structured
          checklist, which moved omission from 19.5% to 12.1%. That is a modest effect and should be
          claimed modestly, but it is cheap and it composes with (i).
    (v)   A caution against over-reading: the machine-side rates in source 2 come from 2023-vintage
          models and must not be quoted as this estate's error rate. What licenses the recommendation
          is the structural findings (aggregation compounds; marginal topics attract unsupported
          content) plus the estate's own 2-for-2, not the 30–46% figure.

  Search scope: Moderate, and the best-verified file in this run's batch. Two queries; two full-text
  retrievals attempted and **both succeeded** — the RCSEng handover experiment read in full, and the
  TofuEval PDF retrieved with Table 2 read directly rather than taken from a summary. Literatures
  covered: experimental comparison of handover channels; nursing and surgical handoff omission
  measurement; LLM summarisation factual-consistency benchmarking. NOT covered, and these are real
  gaps: the verbal-order error literature in medicine (verbal versus written medication orders), which
  is the closest analogue to a spoken instruction carrying consequence and which I did not reach;
  I-PASS and the structured-handoff intervention trials, whose evidence grade PREMISE-108 already
  discusses and which would sharpen mitigation (iv); aviation position-relief and briefing standards,
  which the intake's search strategy named and which I approached only through the healthcare
  material; and any measurement of automated status-summary accuracy at a human interface
  specifically — I searched for it and found only general summarisation benchmarks, which I record as
  a genuine gap rather than as insufficient searching. Two of the four external source lines are
  verified at source; the third is snippet-level and marked.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-944
  Strongest counterargument: The presumption exempts from verification the one channel that the only
  controlled experiment on the subject identifies as the worst. Twelve simulated patients, twenty
  facts each, five handover cycles, two blinded observers: the printed sheet retained 99% of the
  information, verbal-with-notes 85.5%, and verbal-only **2.5%**. Two facts out of eighty. And the
  study forecloses the defence that a spoken report at least preserves the important things: facts
  classified in advance as important were lost at the same rate as facts classified as trivial — three
  percent of the important ones survived. So the intuition underneath PRESUMPTION-944 is not merely
  unsupported, it is inverted. Speech is not a lighter-weight artefact that needs proportionally less
  checking; it is a channel with a measured retention floor near zero and no selectivity about what it
  drops. The machine side agrees: expert-annotated evaluation of dialogue summarisation put
  summary-level factual inconsistency at 30–46% averaged across five summarisers, found that
  summary-level error substantially exceeded sentence-level error — aggregation is where the damage
  happens — and found that models generate MORE unsupported content when asked about a topic their
  source barely covers. "Nothing is broken" is exactly that request: a summary-level assertion about a
  topic on which the read set is silent. The estate then supplies the empirical instance: two
  consecutive mornings, both false, both falsified within the same run against three and four
  same-morning sources. And the register had already ruled on this without noticing. PREMISE-194 says
  corroboration requires an artefact from a different process "cited directly rather than narrated" —
  ACTIVE, High confidence, since 31 August. PREMISE-109 says a health claim not bound to a named
  artefact with a timestamp is not evidence of health, and that "no failures to report" must be
  legible as scoped or it is unfounded — ACTIVE, High confidence, since July. Neither carries an
  exemption for speech. The presumption is therefore not a gap in the estate's knowledge; it is a
  boundary the estate drew around the word "artefact" and then stopped looking at. The sharpest way to
  put it: the estate applies its most rigorous verification to files that agents will read again
  tomorrow, and its least rigorous to the sentence spoken to the only person who acts on it — the one
  assertion in the whole system that has no second reader.
  What would need to be true for C2A2 to be safe: One condition, and it is narrow. The spoken report
  would have to be a READING of a written artefact that already passed the file-level discipline, in
  which case the channel carries no independent error and the presumption is harmless because it is
  vacuous. Anything short of that fails, and it fails in a specific way worth naming: the report does
  not have to be *composed* verbally to inherit the defect, it only has to be composed from
  recollection rather than from the artefact — which is PREMISE-194's exact condition, and
  PREMISE-194's steelman already warns that its three exemptions (verbatim in context, uncompacted,
  same session) "fail silently when they do not hold." A morning report assembled at the start of a
  session, about work done in a previous one, fails all three by construction. A second, weaker
  condition would suffice for the all-clear specifically: if the report never asserts absence — if it
  only ever reports affirmative, artefact-bound findings — then the read-set-silence failure mode is
  unavailable regardless of channel. That is the cheaper of the two and could be adopted tonight.
  How to test: Three tests, all in-house, and the first requires nothing but reading.
  **Test A, the retrospective congruence audit, and it is the direct measurement.** Take the last 30
  morning reports to the designer. For each claim in each report, ask whether an artefact existed at
  the time of the report that would have to hold for the claim to be true, and whether it did. Score
  three columns: claim true and artefact-bound; claim true but unbound (i.e. right by luck); claim
  false. This is PREMISE-109's CLAIMS-WITHOUT-EVIDENCE instrument, which the register already
  specifies as the correct measure and explicitly prefers over a read-set coverage percentage. The
  third column already has two members. **Test B, the channel comparison, which is the item's actual
  question.** For the same 30 days, compare the error rate of claims made in the spoken/terminal
  report against the error rate of claims made in the day's written artefacts. If the spoken channel's
  rate is not lower, the presumption's exemption has no basis; if it is materially higher — which the
  handover experiment predicts — the exemption is inverted and the discipline should be strictest
  where it is currently absent. **Test C, the all-clear census, cheapest of the three and runnable
  tonight.** Grep every report to the designer for unscoped absence claims: "nothing broken", "no
  issues", "all clear", "otherwise fine", "everything ran". Count them, and for each check whether the
  read set could in principle have contained the relevant failure. Every case where it could not is a
  claim that was unfounded when made, independently of whether it happened to be true — and that count
  is the honest measure of how much of the estate's morning reassurance is manufactured by the shape
  of the sentence rather than by the state of the system.
