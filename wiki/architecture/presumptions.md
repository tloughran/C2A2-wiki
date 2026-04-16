# C2A2 Unstated Presumptions Registry
*Maintained by Agent 14b — Presumption Detector | Initialized: 2026-04-10*

Registry of unstated presumptions — premises that designers relied upon without explicit articulation. These were surfaced through inference from conversation patterns, unquestioned framings, and absent alternatives. Marked as [inferred] throughout.

---

PRESUMPTION-001:
  Date surfaced: 2026-04-10
  Statement: [inferred] "Splitting the unified Agent 14 into 14a and 14b will improve the quality of both assumption extraction and presumption detection compared to a single agent doing both tasks."
  Evidence it was operative: The decision to split was presented as beneficial without discussing costs (added complexity, inter-agent coordination overhead, potential duplication). Tom suggested the split; it was approved immediately without exploring whether the single agent approach had been exhausted.
  Why it was unstated: Obvious to participants — splitting for task specialization seems intuitively good. No one questioned whether two agents coordinating would actually outperform one agent with careful attention.
  Type: methodological
  Related decisions: DECISION-005
  Testability: testable empirically (run 14a/14b against baseline, measure quality and overhead)
  Risk if wrong: Medium — if 14a and 14b duplicate work or if coordination overhead exceeds benefit, the split adds cost without value. The system would benefit from a more careful single-agent approach with robust prompting.
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14b
    Chain: [14b → 15a, 15b → 14b]
    Original item: PRESUMPTION-001
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from CHANGE-2026-04-10-001 where splitting was approved without discussing operational tradeoffs or measurement criteria.
      15a: Searched for supporting literature; found partial support for task specialization; strength=Moderate
      15b: Searched for challenging literature; found challenge on coordination overhead in multi-agent systems; strength=Moderate
      14b: Reconciled: PARTIALLY-SUPPORTED (15a) + CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: Moderate
    Risk: Medium (coordination overhead between 14a and 14b may exceed benefits of specialization)

PRESUMPTION-002:
  Date surfaced: 2026-04-10
  Statement: [inferred] "The Thousand Brains architecture, developed for biological neural systems, will transfer conceptually intact to C2A2's multi-agent AI system without significant loss of fidelity."
  Evidence it was operative: DECISION-003 adopts Thousand Brains Theory as "architectural reference model" based on "structural homology." The entire redesign proposal (including tripling, dispatch enhancements, developmental maturity model) is justified by this homology. But the conditions under which biological principles transfer to AI systems were never examined.
  Why it was unstated: The homology was striking enough to seem self-evident. Transferring principles across domains often feels natural when the surface structures align, but it's a risky move without checking transfer conditions.
  Type: epistemological
  Related decisions: DECISION-003, DECISION-010, DECISION-008
  Testability: testable via literature (theory transfer literature, biological-to-AI metaphor validity)
  Risk if wrong: Critical — if Thousand Brains principles don't transfer, the entire redesign roadmap rests on a flawed foundation. Consensus thresholds, dispatch enhancements, developmental stages, and health metrics may all be misaligned with how multi-agent AI actually works.
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14b
    Chain: [14b → 15a, 15b → 14b]
    Original item: PRESUMPTION-002
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from DECISION-003 context where structural homology was cited as sufficient justification for adopting the entire theoretical framework without examining transfer conditions.
      15a: Searched for supporting literature; found partial support for bio-to-AI transfer; strength=Moderate
      15b: Searched for challenging literature; found challenge on transfer conditions validity; strength=Moderate
      14b: Reconciled: PARTIALLY-SUPPORTED (15a) + CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: Moderate
    Risk: Critical (entire C2A2 architecture depends on this transfer; misalignment would cascade through all design choices)

PRESUMPTION-003:
  Date surfaced: 2026-04-10
  Statement: [inferred] "Adding reference_frame_location and conceptual_bearing fields to the dispatch format will be useful information rather than noisy overhead."
  Evidence it was operative: CHANGE-2026-04-10-004 added these fields to all 11 tradition agents as part of the Thousand Brains reference frame principle. The decision states "Master Agent can eventually build a spatial map of inter-tradition conceptual space," but the current utility of the fields before "eventually" is unaddressed.
  Why it was unstated: The intuition that directional data would be useful seemed sufficient. No one asked whether adding fields to every dispatch might increase noise, or whether the spatial mapping capability was necessary for near-term goals.
  Type: methodological
  Related decisions: DECISION-008
  Testability: testable empirically (measure whether these fields increase signal or noise in Master Agent's analysis)
  Risk if wrong: Low to Medium — if the fields add noise without current utility, they clutter the dispatch format and increase cognitive load. Reversible, but worth measuring.
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14b
    Chain: [14b → 15a, 15b → 14b]
    Original item: PRESUMPTION-003
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from CHANGE-2026-04-10-004 where fields were added without discussion of near-term utility or noise metrics.
      15a: Searched for supporting literature; found partial support for dispatch metadata; strength=Moderate
      15b: Searched for challenging literature; found challenge on overhead-to-utility ratio; strength=Moderate
      14b: Reconciled: PARTIALLY-SUPPORTED (15a) + CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: Moderate
    Risk: Low-Medium (reversible if metadata proves noisy)

PRESUMPTION-004:
  Date surfaced: 2026-04-10
  Statement: [inferred] "The 2/3 consensus threshold (≥2/3 agreement) is optimal for tripled tradition agents. It balances sensitivity and specificity."
  Evidence it was operative: DECISION-010 specifies "intra-tradition consensus (≥2/3 agreement)" as the bar for items entering cross-tradition dialogue. This threshold was chosen without discussion of alternatives (2/3, 3/3, simple majority, weighted voting, etc.).
  Why it was unstated: 2/3 majority feels like a "natural" threshold (it's the standard parliamentary majority). No one questioned whether this was right for the epistemic function of consensus in C2A2.
  Type: methodological
  Related decisions: DECISION-010
  Testability: testable empirically (measure cross-tradition robustness against different consensus thresholds and calibrate)
  Risk if wrong: Medium — a threshold that's too low admits weak items; too high rejects good items. The optimal threshold depends on empirical data (agreement-validity curves) that don't exist yet.
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14b
    Chain: [14b → 15a, 15b → 14b]
    Original item: PRESUMPTION-004
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from DECISION-010 specification where the 2/3 threshold appeared without comparative justification.
      15a: Searched for supporting literature; found partial support; strength=Moderate
      15b: Searched for challenging literature; found challenge on threshold optimality; strength=Moderate
      14b: Reconciled: PARTIALLY-SUPPORTED (15a) + CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: Moderate
    Risk: Medium (threshold may be suboptimal)

PRESUMPTION-005:
  Date surfaced: 2026-04-10
  Statement: [inferred] "Separating the supportive literature search (15a) from the challenging search (15b) prevents confirmation bias without introducing other biases."
  Evidence it was operative: CHANGE-2026-04-10-002 states: "A single agent searching both directions would inevitably be biased by whichever direction it searches first." This is stated as a problem, but the solution (two independent agents) assumes that independent searches won't be biased by different factors (search strategy differences, access to different databases, framing effects in how each agent interprets results).
  Why it was unstated: The intuition that splitting prevents bias seemed sufficient. No one examined whether two agents with different priors, search strategies, or result interpretation thresholds might introduce *different* biases that don't cancel.
  Type: epistemological
  Related decisions: DECISION-006
  Testability: testable empirically (compare 15a and 15b results on same items; measure correlation and divergence patterns)
  Risk if wrong: Medium — if 15a and 15b are biased in different ways, their "independent" searches might still systematically miss true results or over-count false positives. The independence assumption is critical but unvalidated.
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14b
    Chain: [14b → 15a, 15b → 14b]
    Original item: PRESUMPTION-005
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from CHANGE-2026-04-10-002 where the bias-prevention mechanism in 15a/15b was presented as proven by design rather than tested.
      15a: Searched for supporting literature; found partial support; strength=Moderate
      15b: Searched for challenging literature; found strong challenge (Druckman & Bolsen, Taber & Lodge); role assignment creates motivated reasoning; strength=Strong
      14b: Reconciled: PARTIALLY-SUPPORTED (15a) + STRONGLY CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: Moderate
    Risk: Medium (role assignment may create motivated reasoning rather than prevent bias)

PRESUMPTION-006:
  Date surfaced: 2026-04-10
  Statement: [inferred] "The six-stage developmental maturity model (Stages 0-5) reflects the actual progression that C2A2 will follow. Stage advancement is monotonic and stages won't need to be revisited."
  Evidence it was operative: CHANGE-2026-04-10-005 created the maturity model with specific benchmarks (Stage 0: definitions written, Stage 1: first 14a/14b cycle, Stage 2: tripling, etc.). The model is presented as a roadmap without discussing whether real system development might be non-linear (backtracking, restarts, abandoned phases).
  Why it was unstated: Staging models feel inherently directional. The assumption of linear progress is embedded in the very concept of "stages" and wasn't questioned.
  Type: structural
  Related decisions: DECISION-009
  Testability: testable empirically (track whether actual progression matches the model or deviates)
  Risk if wrong: Low to Medium — if development becomes non-linear, the stage framework becomes misleading. Phases might need to be revisited (e.g., if tripling reveals that the 11-tradition framework was wrong).
  Status: CHALLENGED
  Provenance:
    Origin: 14b
    Chain: [14b → 15a, 15b → 14b]
    Original item: PRESUMPTION-006
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from CHANGE-2026-04-10-005 where the maturity model is presented as a directed pathway without discussing non-linearity or backtracking.
      15a: Searched for supporting literature; found no support for linear stage models; strength=None
      15b: Searched for challenging literature; found challenge on linear assumption; strength=Moderate
      14b: Reconciled: NO-SUPPORT-FOUND (15a) + CHALLENGED (15b) → CHALLENGED
    Current status: CHALLENGED
    Confidence: Moderate
    Risk: Low-Medium (linear assumption contradicted by systems complexity research)

PRESUMPTION-007:
  Date surfaced: 2026-04-10
  Statement: [inferred] "Literature search via Agents 15a and 15b will be sufficient to validate or challenge architectural assumptions and presumptions. Gaps in the literature can be safely treated as 'NOVEL' rather than as concerning blind spots."
  Evidence it was operative: The self-awareness pipeline (14a/14b → 15a/15b) treats literature absence as a valid outcome ("NOVEL" status in provenance_protocol.md). But literature availability is biased by field, language, publication bias, and what scholars choose to study. An assumption might be unstudied not because it's novel, but because it's obvious, unfashionable, or from a field C2A2 isn't accessing.
  Why it was unstated: The assumption that literature is representative of knowledge seems so obvious that it wasn't examined. The provenance protocol itself embeds it.
  Type: epistemological
  Related decisions: DECISION-006, DECISION-007
  Testability: testable via literature (publication bias, knowledge representation, search strategy limitations)
  Risk if wrong: Medium — if C2A2 treats literature absence as validation success, it may become overconfident about unstudied premises. A NOVEL assumption is not necessarily safe.
  Status: CHALLENGED
  Provenance:
    Origin: 14b
    Chain: [14b → 15a, 15b → 14b]
    Original item: PRESUMPTION-007
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the design of the self-awareness pipeline where "NOVEL" is treated as a terminal status rather than as a gap requiring deeper inquiry.
      15a: Searched for supporting literature; found no support; strength=None
      15b: Searched for challenging literature; found strong challenge (publication bias, Ioannidis); strength=Strong
      14b: Reconciled: NO-SUPPORT-FOUND (15a) + STRONGLY CHALLENGED (15b) → CHALLENGED
    Current status: CHALLENGED
    Confidence: Moderate-High
    Risk: Medium (literature absence cannot be safely treated as validation)

PRESUMPTION-008:
  Date surfaced: 2026-04-10
  Statement: [inferred] "The health metric r (intra-consensus / cross-survival rate) will be computable and meaningful before Stage 3 is complete. The denominator (cross-survival) will be large enough to be statistically meaningful without requiring excessive time."
  Evidence it was operative: DECISION-009 specifies that r is the core health indicator, and OPEN-005 asks "What sample size is needed?" — implying that the answer isn't yet known. Yet the metrics framework (2026-04-10_snapshot.md) treats r as a central measure from Stage 3 onward.
  Why it was unstated: The assumption that r will be computable and meaningful seemed to follow from the definition. But OPEN-005 already signals doubt — the question wouldn't exist if the answer were obvious.
  Type: methodological
  Related decisions: DECISION-009
  Testability: testable empirically (measure how many cross-tradition hypothesis tests are needed for r to reach statistical significance)
  Risk if wrong: Medium — if r requires hundreds of tests to become statistically meaningful, it may not be a practical metric. C2A2 might need alternative health measures.
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14b
    Chain: [14b → 15a, 15b → 14b]
    Original item: PRESUMPTION-008
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the gap between DECISION-009 (asserting r as core metric) and OPEN-005 (questioning whether it's feasible).
      15a: Searched for supporting literature; found partial support for statistical power analysis; strength=Moderate
      15b: Searched for challenging literature; found challenge on sample size requirements; strength=Moderate
      14b: Reconciled: PARTIALLY-SUPPORTED (15a) + CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: Moderate
    Risk: Medium (health metric r may require excessive sample size)

PRESUMPTION-009:
  Date surfaced: 2026-04-10
  Statement: [inferred] "Provenance tracking (the full PROVENANCE header protocol) will improve system credibility more than it increases operational overhead. The benefit will be clear by Stage 1."
  Evidence it was operative: The entire provenance_protocol.md (DECISION-007) is justified as enabling "epistemic honesty" and traceability. But the cost — requiring every inter-agent message to carry a detailed chain header — was never discussed in terms of latency, storage, or cognitive load on agents reading the headers.
  Why it was unstated: The intuitive appeal of traceability made the overhead seem worth it. No one asked "compared to what?" — are there simpler ways to get most of the benefit with less overhead?
  Type: normative
  Related decisions: DECISION-007
  Testability: testable empirically (measure whether provenance headers are actually used by downstream agents and humans, and whether benefit scales with adoption)
  Risk if wrong: Low to Medium — if provenance becomes cargo-cult overhead (headers written but not read or used), the protocol should be simplified. The benefit must be validated.
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14b
    Chain: [14b → 15a, 15b → 14b]
    Original item: PRESUMPTION-009
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from DECISION-007 where the protocol is justified on grounds of principle without discussing operational costs.
      15a: Searched for supporting literature; found partial support for traceability; strength=Moderate
      15b: Searched for challenging literature; found challenge on overhead-to-benefit ratio; strength=Moderate
      14b: Reconciled: PARTIALLY-SUPPORTED (15a) + CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: Moderate
    Risk: Low-Medium (overhead reversible if benefit proves insufficient)

PRESUMPTION-010:
  Date surfaced: 2026-04-10
  Statement: [inferred] "Agent 16's condition-based monitoring (watching for external events like "transcript published") can reliably detect when conditions are met using web search and automated checks, without human intervention."
  Evidence it was operative: DECISION-015 and OPEN-011 suggest Agent 16 will monitor conditions like "has this transcript been published?" But OPEN-011 explicitly asks "What are the constraints on web search access from scheduled agent runs?" — revealing that the feasibility of automated checking wasn't confirmed.
  Why it was unstated: The design of Agent 16 assumes it can check conditions autonomously. But the open question reveals this assumption wasn't validated before the agent definition was written.
  Type: methodological
  Related decisions: DECISION-015, DECISION-016, OPEN-011
  Testability: testable empirically (run Agent 16 and measure false-negative rate — missed conditions — and latency in detecting when conditions are met)
  Risk if wrong: Medium — if Agent 16 cannot reliably detect condition changes, deferred items will languish. The system might need human spot-checks or more explicit condition definitions.
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14b
    Chain: [14b → 15a, 15b → 14b]
    Original item: PRESUMPTION-010
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the gap between DECISION-015 (Agent 16 monitors conditions) and OPEN-011 (questioning whether this is feasible).
      15a: Searched for supporting literature; found partial support for automated monitoring; strength=Moderate
      15b: Searched for challenging literature; found challenge on false-negative rates in automated systems; strength=Moderate
      14b: Reconciled: PARTIALLY-SUPPORTED (15a) + CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: Moderate
    Risk: Medium (automated detection may miss conditions)

PRESUMPTION-011:
  Date surfaced: 2026-04-13
  Statement: [inferred] "Specialist agents' quality filters (applied during proposal generation) are sufficient to ensure only high-quality, non-duplicate material enters the review pipeline. The agents' judgment about what 'passes the filter' is trustworthy without calibration."
  Evidence it was operative: All four specialist agent sessions applied quality filters — "Must be from the thinker themselves," "Must be substantively new," "Must be recent or significant." The Carroll agent rejected content "already captured in prior proposals." The Wolfram agent selected CAG and consciousness Q&A while filtering out other content. These quality judgments were made autonomously by agents with no external validation of their filter accuracy or miss rate.
  Why it was unstated: The quality filter criteria are explicit in the task definition, but the assumption that agents *apply them correctly* was never questioned. No one asked: "How often do agents incorrectly filter out good material, or incorrectly admit low-quality material?"
  Type: methodological
  Related decisions: DECISION-003
  Testability: testable empirically (audit agent filter decisions against human judgment on same source material; measure false-positive and false-negative rates)
  Risk if wrong: Medium — if agents systematically miss important papers or admit marginal ones, the wiki's coverage becomes biased by agent judgment. The 14 proposals produced today were never independently checked for completeness of coverage.
  Status: CHALLENGED
  Provenance:
    Origin: 14b
    Chain: [14b → 15a, 15b → 14b]
    Original item: PRESUMPTION-011
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from specialist agent sessions 2026-04-13 where quality filters were applied without external validation or miss-rate measurement
      15a: Searched for supporting literature; found no support for unadjusted automated filters; strength=None
      15b: Searched for challenging literature; found challenge on filter accuracy; strength=Moderate
      14b: Reconciled: NO-SUPPORT-FOUND (15a) + CHALLENGED (15b) → CHALLENGED
    Current status: CHALLENGED
    Confidence: Moderate
    Risk: Medium (filter accuracy unvalidated; coverage bias likely)

PRESUMPTION-012:
  Date surfaced: 2026-04-13
  Statement: [inferred] "The fixed weekly schedule for specialist agents (Mon: Levin+Friston, Tue: Hawkins+Hoffman, etc.) produces adequate coverage despite the uneven publication rhythms of different thinkers. One search per week per thinker is sufficient."
  Evidence it was operative: Today (Monday) ran Levin+Friston agents as scheduled, but also ran catch-up sessions for Thursday (Stump+Fredrickson), Friday (Carroll+Arkani-Hamed), and Saturday (Wolfram) — suggesting missed runs on those days. The schedule assumes each thinker needs exactly one search per week, but publication patterns differ (e.g., Wolfram blogs frequently; Arkani-Hamed publishes infrequently). No one questioned whether the weekly cadence should be thinker-adaptive.
  Why it was unstated: A fixed weekly schedule is the simplest design. The assumption that it's adequate for all thinkers was embedded in the convenience of uniform scheduling.
  Type: methodological
  Related decisions: DECISION-003
  Testability: testable empirically (compare material-discovery rates across thinkers; measure staleness of coverage per tradition)
  Risk if wrong: Low to Medium — fast publishers (Wolfram, Levin) may have proposals delayed by up to a week; slow publishers (Arkani-Hamed) may have wasted searches. The risk is coverage asymmetry rather than system failure.
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14b
    Chain: [14b → 15a, 15b → 14b]
    Original item: PRESUMPTION-012
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the fixed weekly schedule design and the catch-up pattern observed on 2026-04-13 (four days' agents running on one day)
      15a: Searched for supporting literature; found partial support for fixed scheduling; strength=Moderate
      15b: Searched for challenging literature; found challenge on adaptive vs. fixed scheduling; strength=Moderate
      14b: Reconciled: PARTIALLY-SUPPORTED (15a) + CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: Moderate
    Risk: Low-Medium (coverage asymmetry across thinkers)

PRESUMPTION-013:
  Date surfaced: 2026-04-13
  Statement: [inferred] "Infrastructure failures (auth errors, API key expiry) in automated pipelines will be caught and resolved before they compound into data loss or wiki drift. The system is resilient to individual run failures."
  Evidence it was operative: The wiki daily run (C282 wiki agent daily run) failed completely with a 401 authentication error today. The morning briefing noted that "Last C2A2 daily run was Apr 9 — no runs on Apr 10-12." This is 4 days of missed wiki processing. Yet no alarm or escalation mechanism triggered. The morning system health check did not flag this. The system proceeded as if this were acceptable.
  Why it was unstated: Auth failures seem like transient operational issues, not architectural concerns. No one designed an alerting mechanism for multi-day pipeline failures because the assumption was that these would be caught quickly.
  Type: architectural
  Related decisions: DECISION-004 (Agent 14 relies on daily runs happening)
  Testability: testable empirically (measure time-to-detection for pipeline failures; measure cumulative drift from missed runs)
  Risk if wrong: Medium to High — if wiki daily runs fail silently for extended periods, the wiki diverges from reality: proposals pile up, PRS counts freeze, pattern detection stalls. Today's evidence suggests this is already happening (76 PRS triplets unchanged since Apr 10 despite 14+ new proposals generated).
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14b
    Chain: [14b → 15a, 15b → 14b]
    Original item: PRESUMPTION-013
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from wiki daily run failure (auth error, 2026-04-13) and morning briefing observation of 4-day processing gap with no alerting
      15a: Searched for supporting literature; found partial support for failure resilience; strength=Moderate
      15b: Searched for challenging literature; found strong challenge (cascade failures, silent failures); strength=Strong
      14b: Reconciled: PARTIALLY-SUPPORTED (15a) + STRONGLY CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: High (active violation already observed)
    Risk: Medium-High (4-day wiki failure demonstrates this is not theoretical — already occurring)

PRESUMPTION-014:
  Date surfaced: 2026-04-13
  Statement: [inferred] "Cross-tradition signals claimed by specialist agents during proposal generation are structurally meaningful — not just surface-level keyword associations. When an agent says 'Fredrickson trust paper × C2A2 architecture: trust infrastructure required for stranger-paradigm dialogue,' this reflects a genuine theoretical connection."
  Evidence it was operative: All four specialist agent sessions produced cross-tradition signal sections. The Wolfram agent connected CAG to CROSS-016 and CROSS-001. The Carroll agent claimed the emergence taxonomy "provides the shared framework for evaluating every consciousness/causation claim across all 11 traditions." The Levin agent labeled the neurobots paper a "Paradigm Shift Candidate." These claims are passed downstream without independent verification of their structural (vs. surface) validity.
  Why it was unstated: Cross-tradition signals are the system's most valued output. The assumption that agents can reliably distinguish structural homologies from surface analogies is so central to C2A2's value proposition that questioning it would feel like questioning the system's reason for existing.
  Type: epistemic
  Related decisions: DECISION-003
  Testability: testable empirically (have independent agents or human reviewers evaluate a sample of cross-tradition claims; measure inter-rater agreement on structural vs. surface classification)
  Risk if wrong: High — if agents produce superficial cross-tradition connections that look impressive but don't survive scrutiny, C2A2's core output is noise dressed as signal. The pattern detector should be catching this, but it depends on the same agents' framing.
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14b
    Chain: [14b → 15a, 15b → 14b]
    Original item: PRESUMPTION-014
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cross-tradition signal claims in specialist agent outputs 2026-04-13, which are treated as actionable without independent validation of structural depth
      15a: Searched for supporting literature; found partial support for cross-domain analogy detection; strength=Moderate
      15b: Searched for challenging literature; found challenge (structure-mapping theory, LLM analogy quality); surface vs. structural distinction hard to verify; strength=Moderate
      14b: Reconciled: PARTIALLY-SUPPORTED (15a) + CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: Moderate
    Risk: High (C2A2's core value proposition depends on structural quality of cross-tradition signals; unvalidated)

PRESUMPTION-015:
  Date surfaced: 2026-04-13 (evening run)
  Statement: [inferred] "The self-awareness pipeline can meaningfully evaluate its own structural assumptions without circularity problems. When 15a and 15b search for evidence about ASSUMPTION-003 (FOR/AGAINST prevents bias) and PRESUMPTION-005 (separating 15a/15b prevents bias without introducing others), they are evaluating claims about their own design using their own design."
  Evidence it was operative: The lit search pipeline (2026-04-13) processed ASSUMPTION-003 and PRESUMPTION-005 — both of which are claims about whether the 15a/15b structure itself is valid — using the 15a/15b structure. The results (PARTIALLY-CHALLENGED for both) were accepted as authoritative without noting the circularity. If the pipeline is biased, its evaluation of its own bias is also biased.
  Why it was unstated: Self-referential evaluation is a well-known philosophical problem (Gödel, bootstrapping), but in practice, engineering systems routinely self-test. The circularity was probably invisible because the pipeline is designed to feel like an objective external check.
  Type: epistemic
  Related decisions: DECISION-006, DECISION-012
  Testability: testable empirically (have an independent evaluation mechanism — e.g., a single neutral agent or human reviewer — assess the same items and compare results with the 15a/15b pipeline's self-evaluation)
  Risk if wrong: Medium-High — if the pipeline's self-evaluation is circular, the system may be falsely confident about items that concern its own structure. The PARTIALLY-CHALLENGED status for ASSUMPTION-003 and PRESUMPTION-005 may itself be biased.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-015
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from lit search pipeline session 2026-04-13, where the pipeline evaluated claims about itself without acknowledging circularity
    Current status: UNTESTED

PRESUMPTION-016:
  Date surfaced: 2026-04-13 (evening run)
  Statement: [inferred] "A single-day literature search pass is sufficient for reliable dispositioning of architectural assumptions and presumptions. The quality of search results does not improve significantly with additional time, iterative refinement, or alternative search strategies."
  Evidence it was operative: All 25 items were searched by 15a and 15b and dispositioned by 15c on the same day (2026-04-13). No discussion occurred about whether a second pass, different search terms, or broader database coverage might change results. The dispositions were treated as final (INCORPORATE/MONITOR/REVISE) rather than preliminary.
  Why it was unstated: The scheduled task ran once and produced results; the results felt authoritative because they were structured and comprehensive. No one asked whether the search quality was adequate or whether re-running with different parameters would yield different dispositions.
  Type: methodological
  Related decisions: DECISION-006, DECISION-012
  Testability: testable empirically (re-run searches on a subset of items with different strategies; measure disposition stability across runs)
  Risk if wrong: Medium — if dispositions are sensitive to search strategy, the INCORPORATE/REVISE decisions may flip on subsequent passes. The 7 REVISE items may include false positives (items challenged by narrow search that would be supported by broader search), and the 3 INCORPORATE items may include false negatives.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-016
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the single-pass design of the lit search pipeline on 2026-04-13, where all 25 items were dispositioned in one cycle without discussion of search adequacy
    Current status: UNTESTED

PRESUMPTION-017:
  Date surfaced: 2026-04-13 (evening run)
  Statement: [inferred] "Data consistency discrepancies in the self-awareness pipeline (e.g., monitor_queue.md having 13 entries vs. 15 expected MONITOR items) are cosmetic bookkeeping issues rather than symptoms of deeper pipeline reliability problems."
  Evidence it was operative: The lit search pipeline noted that "monitor_queue.md has 2 fewer entries than expected from the 15 MONITOR dispositions — the authoritative record is dispositions_2026-04-13.md." The discrepancy was flagged but treated as a minor data reconciliation issue. No one examined whether the missing entries indicated a systematic failure in how 15c routes items to downstream files.
  Why it was unstated: Small data discrepancies feel normal in complex pipelines. The presumption that discrepancies are cosmetic (vs. structural) was embedded in the decision to proceed without investigation.
  Type: methodological
  Related decisions: DECISION-012 (15c pipeline)
  Testability: testable empirically (audit the full data flow from 15c dispositions to downstream files; identify root cause of the 2-item discrepancy)
  Risk if wrong: Low-Medium — if routing failures are systematic, the monitor queue and revision flags may silently drop items. Over time, this could mean MONITOR items go unwatched and REVISE items go unreviewed.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-017
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from lit search pipeline session 2026-04-13, where a data consistency discrepancy was noted but treated as non-structural
    Current status: UNTESTED

PRESUMPTION-018:
  Date surfaced: 2026-04-13 (evening run)
  Statement: [inferred] "The Claude Chat conversation ('Morning walk check-in') serves as a reliable inter-session memory channel — context delivered in the evening will be accurately available for the morning walk discussion."
  Evidence it was operative: The evening sync (2026-04-13) delivered a detailed summary of the day's C2A2 work to the "Morning walk check-in" conversation on claude.ai. This is treated as a reliable handoff mechanism. Chat acknowledged the sync and "primed" 4 discussion topics. But Chat's context window limitations, potential for context loss between sessions, and the fidelity of retrieval were never discussed.
  Why it was unstated: Chat feels like a persistent conversation partner. The assumption that context persists across sessions is embedded in the user experience of conversational AI. The evening sync treats Chat as a database; in reality, Chat is an LLM with context window constraints.
  Type: architectural
  Related decisions: None (emerged from operational practice, not a formal decision)
  Testability: testable empirically (verify whether morning walk discussions reference evening sync content accurately; measure information loss across the session boundary)
  Risk if wrong: Low-Medium — if Chat loses or garbles context, the morning walk discussion may miss critical items from the evening sync. The 4 primed topics (wiki auth fix, Phase 2a pause, PRESUMPTION-002 de-risking, PRESUMPTION-007 operationalization) may not all surface.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-018
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from evening cowork-to-chat sync session 2026-04-13, where Chat was used as an inter-session memory channel without discussion of reliability constraints
    Current status: UNTESTED

PRESUMPTION-019:
  Date surfaced: 2026-04-14
  Statement: [inferred] "Disciplinary boundary-crossing can be measured empirically through co-authorships, citation networks, and keyword emergence — and these bibliometric signals are reliable proxies for genuine intellectual convergence."
  Evidence it was operative: Tom's morning walk proposal for a "paradigm shift detector" tool assumed that the observable signals of interdisciplinary convergence (co-authorships, citation patterns, keyword emergence) are valid proxies for genuine intellectual synthesis. He described seeing the "bluing" of fields as they merge. But bibliometric signals can reflect strategic collaboration (e.g., for funding), methodological borrowing without theoretical integration, or citation courtesy rather than genuine convergence.
  Why it was unstated: Bibliometrics is a well-established research field. The assumption that its signals map to genuine intellectual convergence seems obvious in context — but the gap between bibliometric proximity and theoretical integration is well-documented in scientometrics.
  Type: methodological
  Related decisions: DECISION-003 (extending paradigm detection capabilities)
  Testability: testable via literature (scientometrics, co-citation analysis validity, interdisciplinary research measurement)
  Risk if wrong: Medium — if the paradigm shift detector is built on unreliable proxies, it will generate false positives (detecting "convergence" that is actually strategic or superficial) and false negatives (missing genuine synthesis that doesn't show up in bibliometric signals).
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-019
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from morning walk discussion 2026-04-14, where a paradigm shift detector was proposed using bibliometric signals without examining the signal-to-convergence mapping validity
    Current status: UNTESTED

PRESUMPTION-020:
  Date surfaced: 2026-04-14
  Statement: [inferred] "AI synthesis of interdisciplinary research is qualitatively different from — and complementary to — human synthesis, rather than being a faster version of the same process that introduces its own systematic biases."
  Evidence it was operative: Tom's reframing of C2A2 (ASSUMPTION-017) positions AI as doing "first-pass synthesis" while humans "validate and accelerate." This implicitly treats AI synthesis as a neutral, scalable version of human synthesis that humans can then quality-check. But LLM-based synthesis has known systematic biases: preference for majority viewpoints in training data, difficulty distinguishing structural from surface analogy, tendency to find connections where humans would see noise (apophenia). If AI synthesis has its own bias profile (different from human bias), human validation may not catch AI-specific errors because humans aren't primed to look for them.
  Why it was unstated: The vision of AI-as-synthesizer is exciting and aligns with the current moment of AI capability expansion. The presumption that AI synthesis is complementary (rather than introducing new failure modes) feels natural because the alternative — that AI synthesis might be systematically misleading in ways humans can't easily detect — is threatening to the project's rationale.
  Type: epistemic
  Related decisions: DECISION-003
  Testability: testable empirically (compare AI-generated cross-tradition connections with expert-generated ones; measure false-positive rate and bias profile of each)
  Risk if wrong: High — if AI synthesis introduces systematic biases that human validators aren't primed to catch, C2A2 could produce confident but wrong cross-tradition connections. This risk is amplified because the system's value proposition depends on the quality of these connections. See also PRESUMPTION-014 (cross-tradition signal validity).
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-020
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from morning walk discussion 2026-04-14, where AI synthesis was positioned as complementary to human judgment without examining AI-specific bias profiles
    Current status: UNTESTED

PRESUMPTION-021:
  Date surfaced: 2026-04-14
  Statement: [inferred] "The 'depth' of FINDING-011 (SUPER-BRIDGE) can be reliably assessed by the same pipeline and agents that generated it. There is no independent depth metric."
  Evidence it was operative: The wiki daily run identified FINDING-011 as a triple-flag (⚑⚑⚑) finding — the highest priority. The evening sync called it "the deepest cross-tradition signal the system has found." But the depth assessment was made by the pattern detector agent and the master wiki agent — both of which are inside the system. No independent metric of "depth" exists. The system is judging its own output's significance without external calibration.
  Why it was unstated: Significant findings feel significant. The triple-flag notation creates an appearance of objective assessment, but the criteria for flag assignment are internal to the system. No one asked: "by whose standards is this deep?"
  Type: epistemic
  Related decisions: DECISION-003
  Testability: testable empirically (have domain experts in Hoffman, Friston, and Levin traditions independently evaluate whether the trace-logic/Markov-blanket/dissociative-boundary mapping is mathematically valid, not just analogically suggestive)
  Risk if wrong: Medium-High — if FINDING-011 is a surface analogy dressed in mathematical language, prioritizing it over other findings wastes attention and reduces trust in the pipeline. The system's credibility depends on its ability to distinguish genuine from spurious cross-tradition signals. See also PRESUMPTION-014.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-021
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the elevation of FINDING-011 to top priority on 2026-04-14, where depth assessment was made entirely within the system without external calibration
    Current status: UNTESTED

PRESUMPTION-022:
  Date surfaced: 2026-04-14
  Statement: [inferred] "The REVISE backlog (11 items as of April 14) represents a bounded, manageable problem that Tom can address through periodic triage. The REVISE queue will not grow faster than Tom's capacity to review."
  Evidence it was operative: The evening sync noted "11 REVISE items piling up" and recommended they "need at least a triage pass." The self-awareness pipeline generated 4 new REVISE items in a single cycle (April 13 evening). If each subsequent cycle generates 2-4 new REVISE items (as it does when processing presumptions, which have a high REVISE rate), and Tom reviews 0-2 per session, the queue grows monotonically. This mirrors the proposal review bottleneck (ASSUMPTION-012) — the same structural pattern at a meta-level.
  Why it was unstated: The system frames REVISE items as requiring human review, which is correct. But no one asked whether the review rate could match the generation rate. The meta-level irony: ASSUMPTION-012 (human review is the bottleneck for proposals) is repeating itself at the self-awareness layer (human review is the bottleneck for REVISE items).
  Type: architectural
  Related decisions: DECISION-012 (15c disposition framework)
  Testability: testable empirically (track REVISE queue growth rate vs. review rate over 2-3 cycles; if queue grows monotonically, the process needs redesign)
  Risk if wrong: Medium — if REVISE items accumulate without review, the self-awareness pipeline's outputs lose actionability. Items flagged for revision that never get revised become noise. The pipeline would be surfacing problems but not closing the loop — undermining its stated purpose.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-022
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the growing REVISE backlog (7 → 11 in one cycle) and the zero review throughput observed 2026-04-14, mirroring the proposal review bottleneck pattern
    Current status: UNTESTED

PRESUMPTION-023:
  Date surfaced: 2026-04-14
  Statement: [inferred] "The three simultaneous infrastructure failures (git index.lock, Gmail connector stale, wiki 401 auth error) are independent incidents with separate root causes. They are not symptoms of a common underlying problem."
  Evidence it was operative: The wiki daily run reported git push blocked by index.lock. The morning briefing reported Gmail integration stale. The wiki auth error is Day 5. Each is treated as a separate issue requiring a separate fix. But all three involve credential/session/permission management in automated scheduled tasks running on the same machine. The evening sync recommended them as "5 minutes of manual intervention" — implying they are quick, independent fixes.
  Why it was unstated: Infrastructure issues are typically triaged individually. The pattern of three concurrent failures in the same authentication/permission domain was not examined as a systemic signal. This connects to PRESUMPTION-013 (infrastructure resilience) — the same vulnerability now manifesting through multiple channels simultaneously.
  Type: architectural
  Related decisions: DECISION-015 (Agent 16 — deferred action monitor, which could detect correlated failures)
  Testability: testable empirically (investigate root causes of all three failures; determine whether they share a common cause such as OS update, credential rotation, or file system permission change)
  Risk if wrong: Low — two of three failures resolved (git locks cleared, Gmail confirmed working in active sessions). Wiki auth was the substantive issue; the others were routine operational friction, not correlated systemic failure.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-023
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from three concurrent infrastructure failures on 2026-04-14, all involving authentication/permission/session management, treated as independent incidents
    Current status: UNTESTED

PRESUMPTION-024:
  Date surfaced: 2026-04-15
  Statement: [inferred] "The boundary convergence hypothesis (FINDING-011a) reflects genuine structural unity across all 11 traditions, not a selection effect produced by a system designed to find cross-tradition connections."
  Evidence it was operative: Tom's afternoon session generated FINDING-011a by systematically mapping each of the 11 traditions onto the inside/outside boundary framework. The mapping was articulated by the system's designer during an extended creative session. No one asked whether a system designed to detect cross-tradition patterns (C2A2) would inevitably find them, regardless of whether the patterns are real — a form of apophenia at the design level. The boundary hypothesis may be a projection of the system's structure onto its subject matter.
  Why it was unstated: The hypothesis was exciting and intellectually compelling. The question "are we finding this because it's there, or because we're built to find it?" is threatening to the project's most important output.
  Type: epistemic
  Related decisions: DECISION-017
  Testability: testable empirically (present the boundary mapping to domain experts in each tradition without revealing C2A2's architecture; ask whether the mapping is structurally valid from within their discipline; if experts independently confirm, the selection effect concern is mitigated)
  Risk if wrong: Critical — if FINDING-011a is a selection artifact, it is the system's largest false positive. The emails to Kastrup/Hoffman/Friston and Levin are premised on the mapping being genuine. A false positive of this magnitude would undermine C2A2's credibility.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-024
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from FINDING-011a creation session 2026-04-15, where the system's designer generated the boundary mapping during creative exploration without adversarial testing of the mapping's validity
    Current status: UNTESTED

PRESUMPTION-025:
  Date surfaced: 2026-04-15
  Statement: [inferred] "Reversing the Phase 2a pause (from cautious delay to full-rollout commitment bet) is justified by the REVISE triage and OPEN-012 resolution, not by resolution of the underlying epistemic concerns that motivated the pause."
  Evidence it was operative: ASSUMPTION-016 and ASSUMPTION-018 established that pausing Phase 2a was prudent because literature search results challenged key architectural assumptions. The concerns that motivated the pause — OPEN-004 (agent differentiation), contested assumptions about consensus thresholds, challenged presumptions about the Thousand Brains transfer — have not been resolved. What changed is operational: the REVISE backlog was cleared and infrastructure was fixed. But operational cleanup does not resolve the epistemic concerns. Tom unpaused Phase 2a (ASSUMPTION-023) based on confidence from clearing backlogs, not from resolving the contested foundations.
  Why it was unstated: Clearing backlogs feels like progress. The distinction between operational progress (backlog cleared) and epistemic progress (contested assumptions resolved) was not explicitly drawn. The momentum of a productive session may have shifted the threshold for proceeding.
  Type: methodological
  Related decisions: DECISION-010, OPEN-004
  Testability: testable empirically (track whether Phase 2a implementation encounters the same problems flagged by ASSUMPTION-003, 004, 007, 008 — if so, the pause should not have been lifted)
  Risk if wrong: Medium-High — if Phase 2a proceeds on unresolved foundations, the 33-agent deployment may need to be rolled back. The cost of rollback (rewriting 22 new agent definitions) exceeds the cost of further delay.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-025
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the gap between ASSUMPTION-023 (full rollout approved) and the unresolved epistemic concerns (ASSUMPTION-003/004/007/008, OPEN-004) that motivated the original pause
    Current status: UNTESTED

PRESUMPTION-026:
  Date surfaced: 2026-04-15
  Statement: [inferred] "Batch triage of REVISE items (16 in one session) produces adequate review quality comparable to deliberate individual review."
  Evidence it was operative: Tom triaged all 16 REVISE items in one session (CHANGE-2026-04-15-005). Several were resolved by category rather than individual deliberation: 3 SUPERSEDED BY FRAMEWORK, 3 ALREADY ADDRESSED. The Kuhnian evidence framework (created the same day) retroactively resolved items that were flagged for revision. This suggests the triage was influenced by the creative momentum of the session rather than by careful examination of each item's evidence. The 1 DISMISSED item (REVISE-016 on data discrepancy) may have been dismissed prematurely — PRESUMPTION-017 flagged routing failures as potentially structural.
  Why it was unstated: Batch triage is efficient and satisfying. The presumption that "faster review with frameworks = adequate review" was embedded in the productivity-oriented framing of the session.
  Type: methodological
  Related decisions: DECISION-012
  Testability: testable empirically (track whether any batch-triaged items need to be re-opened; if ACCEPTED items later prove problematic or DISMISSED items resurface, the triage was inadequate)
  Risk if wrong: Medium — if triage quality was insufficient, problematic items pass through unexamined. The REVISE mechanism exists precisely because these items had strong evidence against them. Clearing them too quickly defeats the purpose.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-026
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from CHANGE-2026-04-15-005 where batch triage applied categorical resolutions rather than item-by-item deliberation to HIGH urgency items
    Current status: UNTESTED

PRESUMPTION-027:
  Date surfaced: 2026-04-15
  Statement: [inferred] "Sending the boundary-equivalence email to Kastrup, Hoffman, Friston (cc Levin) and a separate direct email to Levin will elicit substantive responses that advance C2A2's research. The recipients will engage with the questions as posed rather than ignoring, misunderstanding, or objecting to the framing."
  Evidence it was operative: Two emails were drafted as the highest-leverage action items from the session. The emails pose technical questions about the boundary equivalence and assume the recipients will recognize the value of the inquiry. But: (a) these are unsolicited emails from a researcher the recipients may not know; (b) the questions assume the recipients accept the premise that their programs share a common boundary structure; (c) Hoffman, Friston, and Kastrup may see the mapping as reductive of their distinct programs; (d) Levin's empirical program may not map onto the formal framework as cleanly as the email suggests.
  Why it was unstated: The intellectual excitement of the boundary hypothesis made the email feel like an obvious next step. The possibility of non-response, hostile response, or response that reveals the mapping is wrong was not considered.
  Type: methodological
  Related decisions: DECISION-017
  Testability: testable empirically (observe response rate and quality from the four recipients; if no response within 4 weeks, or if responses reveal fundamental objections to the framing, the presumption is challenged)
  Risk if wrong: Low to Medium — non-response is the likeliest outcome and is costless. Hostile response or response revealing the mapping is wrong would be informative (negative results are still results). The risk is primarily to the time invested in the email framing.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-027
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the email drafting session 2026-04-15, where outreach to four principals was planned without considering response likelihood or failure modes
    Current status: UNTESTED

PRESUMPTION-028:
  Date surfaced: 2026-04-15
  Statement: [inferred] "The lit search pipeline's completion of all 42 items with 0 in queue represents a stable endpoint rather than a snapshot that will immediately be invalidated by the next 14a/14b cycle."
  Evidence it was operative: The lit search pipeline ran its third full cycle on April 15, processing 10 items from April 14. The completion report states "42/42 items dispositioned. 0 in queue." But this run of 14a/14b (the current session) is generating 6 new assumptions and 5 new presumptions, immediately re-populating the queue with 11 items. The "0 in queue" state lasted less than one day. The pipeline is in a steady-state where it processes items from the prior cycle while the current cycle generates new ones — it is never truly "caught up."
  Why it was unstated: Completion feels like an achievement. The fact that each self-awareness cycle generates new items for the next lit search cycle was not framed as a structural property of the system.
  Type: architectural
  Related decisions: DECISION-006, DECISION-012
  Testability: testable empirically (track how long the "0 in queue" state persists across cycles; if it never lasts more than one day, the system is in permanent queue-generation mode)
  Risk if wrong: Low — this is not a risk so much as a framing correction. The pipeline is working as designed; the expectation of "caught up" is the error.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-028
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the lit search pipeline completion report (42/42, 0 queued) on the same day that 14a/14b generates 11 new items for the next cycle
    Current status: UNTESTED

PRESUMPTION-029:
  Date surfaced: 2026-04-16
  Statement: [inferred] "The +5 pattern detector findings (FINDING-013 through FINDING-017) produced by the April 16 massive-ingestion run represent genuine cross-tradition signals rather than artifacts of processing 45 files through three parallel subagents with correlated prompting."
  Evidence it was operative: The wiki daily run reported "+5 pattern detector findings (12→17)" and elevated FINDING-013 (Friston × Fredrickson × McGilchrist), FINDING-014 (Hawkins/C2A2 isomorphism), and FINDING-015 (Kastrup × Koch × IIT) to highest-priority status in the morning briefing. No discussion occurred of whether finding-detection rate at 5 findings per 45 files was consistent with historical baseline (prior runs average ≤1 finding per ingestion day) or whether the three parallel subagents used correlated prompts that would inflate cross-tradition detection.
  Why it was unstated: The findings themselves are the goal, so a surge in findings feels like success. The prior presumption cluster (PRESUMPTION-014, 020, 024) was focused on single-agent LLM signals; nobody extended that concern to the multi-subagent batch case.
  Type: methodological
  Related decisions: DECISION-003
  Testability: testable empirically (re-run any three FINDING-013–017 using fresh single-agent extraction; if disposition changes, subagent correlation is a real effect)
  Risk if wrong: HIGH — if 5 findings in one day is inflated by subagent correlation, then the pattern detector's cumulative count is overstating cross-tradition structure. Extends the PRESUMPTION-024 "selection effect" concern from FINDING-011a to the broader findings stream.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-029
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from wiki-daily-run 2026-04-16 reporting a 5× surge in findings without baseline comparison or subagent-correlation check
    Current status: UNTESTED

PRESUMPTION-030:
  Date surfaced: 2026-04-16
  Statement: [inferred] "The C2A2 wiki git repository being uncommitted for 8 days (189 dirty files since April 8, including all research content) was acceptable operating practice and no data was lost." The rescue commit was framed as a checkpoint, not as evidence of a systemic version-control gap.
  Evidence it was operative: The debug-wiki-visualization session discovered 189 uncommitted files going back to April 8. The assistant wrote a checkpoint-commit.sh script for Tom to run locally; the problem was framed as "the current HTML works well enough to be a useful checkpoint" and "we've been operating without version control on a 1341-line generated file." No audit was proposed of what changes might have been lost or corrupted during the 8-day window, nor of whether other automated tasks (daily wiki run, 14a/14b, 15a-d) had also been running against an unversioned tree.
  Why it was unstated: The problem felt like a visualization-tool issue (HTML editing), not a whole-project version-control failure. The automated pipelines appear to be working, so the missing commits are framed as cosmetic rather than structural.
  Type: architectural
  Related decisions: [none — pattern not yet formalized as a decision]
  Testability: testable empirically (inspect whether any files in the 189-dirty set contain silent corruption from parallel tool writes; inspect whether any automated-task outputs were overwritten between April 8 and April 16)
  Risk if wrong: MEDIUM-HIGH — if version-control hygiene has been missing for 8 days across all daily-run outputs, then any silent corruption is unrecoverable, and the "operational health" reported on April 15 ("most productive day in C2A2's operational history") was measured against a tree that had no baseline.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-030
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the debug-wiki-visualization session 2026-04-16, where 189 uncommitted files were discovered but the framing treated it as an HTML-only issue
    Current status: UNTESTED

PRESUMPTION-031:
  Date surfaced: 2026-04-16
  Statement: [inferred] "The rotation schedule (Mon: Levin+Friston, Tue: Hawkins+Hoffman, Wed: McGilchrist+Kastrup, Thu: Stump+Fredrickson, Fri: Carroll+Arkani-Hamed, Sat: Wolfram) provides adequate tradition coverage, and the orchestrator's Phase-2 fallback on non-scheduled days is epistemically equivalent to specialist coverage." On April 16 (Thursday), the orchestrator searched for all 9 non-Thursday traditions as fallback, producing only 2 proposals (Levin, Carroll).
  Evidence it was operative: The wiki daily run's Phase 2 executed 14 web searches for 9 non-scheduled traditions and produced only 2 high-quality hits. This suggests that either (a) the orchestrator's generic search is substantially less effective than specialist agents, or (b) the specialist agents are also hitting a ceiling — but the "only 2 proposals" outcome was reported as normal, not as a signal about coverage adequacy.
  Why it was unstated: The rotation schedule has run for 5+ weeks without examination. Its design-time rationale (LLM cost distribution, avoiding duplication) was never compared to empirical per-tradition yield data.
  Type: methodological
  Related decisions: DECISION-003
  Testability: testable empirically (compare proposal-per-search yield of scheduled specialist days vs. orchestrator-fallback searches for the same tradition; yields should be compared over 4+ weeks)
  Risk if wrong: MEDIUM — if orchestrator-fallback produces substantially fewer or lower-quality proposals, then the 6 traditions not covered each week are accumulating hidden gaps. Over months, this would bias the PRS-triplet distribution (some traditions chronically under-represented).
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-031
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from Phase 2 orchestrator-fallback pattern on 2026-04-16, where 14 searches produced 2 proposals — low yield reported as normal
    Current status: UNTESTED

PRESUMPTION-032:
  Date surfaced: 2026-04-16
  Statement: [inferred] "Infrastructure degradation (Chrome MCP unavailable, Gmail connector stale since April 14 for walk-note capture, voice-dispatch window missed) is temporarily inconvenient but not systematically eroding the morning-handoff signal chain." Two scheduled tasks on April 16 (c2a2-morning-chat-scrape, morning-walk-cowork-handoff) produced empty or failure-note outputs due to infrastructure issues.
  Evidence it was operative: The morning walk handoff reported "No walk notes found" (Gmail stale); the chat scrape failed entirely (Chrome extension not connected). The failure paths were documented per-task but no cross-task pattern was noted: over two consecutive days, Tom's intent-signal channels (walk notes, chat recap) have been partially or entirely offline, yet the pipeline continued to operate on the assumption that wiki state alone is sufficient to drive the day's work.
  Why it was unstated: Each task logs its own failure in isolation. No agent aggregates failure patterns across the morning-handoff chain. The daily briefing was generated successfully (from wiki state), so the output looked complete even though the intent-input was missing.
  Type: architectural
  Related decisions: DECISION-015 (Agent 16 — could extend to morning-handoff chain)
  Testability: testable empirically (track over 2 weeks: frequency of "No walk notes found" plus "Chrome extension not connected" events; correlate with downstream drift in execution queue and priorities)
  Risk if wrong: MEDIUM — if the morning-handoff chain is silently drifting from Tom's actual intent, the agents will increasingly optimize for wiki-state goals rather than Tom's walking-priority goals. The "healthiest operational state since C2A2 began" framing from April 15 may mask degradation of the input signal.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-032
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from morning-walk-cowork-handoff and c2a2-morning-chat-scrape sessions 2026-04-16, where both intent-capture channels failed without a cross-channel escalation
    Current status: UNTESTED

PRESUMPTION-033:
  Date surfaced: 2026-04-16
  Statement: [inferred] "The claim that wiki_narration.html is 'good enough to be a useful checkpoint' is an evaluation grounded in the assistant's own pixel-level screenshots, not in Tom's user-experience." The assistant used computer-use zooms to identify issues (brightness slider missing, footer collapsed) and then decided the current state was stable enough to commit.
  Evidence it was operative: The debug-wiki-visualization session's first substantive claim — "The current HTML works well enough to be a useful checkpoint" — was made after the assistant had just finished listing three active bugs ("brightness ceiling too low, OpenAI Test button silent, maybe a cache issue on Play/Pause"). The decision-criterion for "well enough" was the assistant's own UI assessment, not any user-task completion measure. Tom did not directly evaluate the HTML before agreeing to the checkpoint.
  Why it was unstated: The checkpoint-then-refactor framing is standard engineering practice. What went unstated is that in Cowork mode the assistant is both producer and evaluator of the artifact, and no independent user-task-completion criterion was proposed for the "well enough" threshold.
  Type: methodological
  Related decisions: [none formal]
  Testability: testable empirically (has Tom successfully completed a "narrate today's wiki run" task using the checkpointed HTML? If not, the checkpoint was premature)
  Risk if wrong: LOW-MEDIUM — premature checkpoint creates a compounding effect where later bugs are anchored to a tagged baseline; any rollback is less useful than expected.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-033
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the debug-wiki-visualization session 2026-04-16, where the "well enough" claim was made without any independent user-task criterion
    Current status: UNTESTED

PRESUMPTION-034:
  Date surfaced: 2026-04-16
  Statement: [inferred] "The C2A2 daily-run naming convention ('daily run') presumes a daily ingestion cadence, but on April 16 the run actually processed an 8-day backlog (proposals from April 8–15). The 'daily run' label continues to name the schedule, not the per-run scope."
  Evidence it was operative: The session logs labeled a 45-file batch as a "daily run" without noting that its scope (8 days of proposals) was 9× typical. The PRS count jumped from 80→151 (+71), labelled "Massive ingestion." All downstream metrics (assumptions, presumptions, findings) will be attributed to "2026-04-16" in the metrics snapshot, compressing 8 days of generative work into one day's counters. This distorts trajectory assessment.
  Why it was unstated: Nobody renamed the process when the backlog cleared. The label is a vestige of the intended daily cadence that was never enforced as an invariant when the cadence slipped.
  Type: epistemic
  Related decisions: DECISION-003
  Testability: testable empirically (re-allocate the April 16 +71 PRS triplets across April 8–15 dates based on proposal creation dates; compare trajectory metrics before and after re-allocation)
  Risk if wrong: LOW — does not affect system correctness; affects the interpretability of trajectory metrics. But small distortions compound: the metrics snapshot becomes less trustworthy over time.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-034
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from wiki-daily-run 2026-04-16 where a multi-day backlog was silently labelled a single "daily run"
    Current status: UNTESTED

---

## Status Summary

Total presumptions surfaced: 34

By type:
  Methodological: 15 (PRESUMPTION-001, 003, 004, 008, 010, 011, 012, 016, 017, 019, 025, 026, 027, 029, 031)
  Epistemological: 9 (PRESUMPTION-002, 005, 007, 014, 015, 020, 021, 024, 034)
  Structural: 1 (PRESUMPTION-006)
  Normative: 1 (PRESUMPTION-009)
  Architectural: 8 (PRESUMPTION-013, 018, 022, 023, 028, 030, 032, 033)

By risk level:
  Critical: 2 (PRESUMPTION-002 — Thousand Brains transfer; PRESUMPTION-024 — selection effect on FINDING-011a)
  High: 3 (PRESUMPTION-014 — cross-tradition signal validity; PRESUMPTION-020 — AI synthesis bias profile; PRESUMPTION-029 — subagent correlation inflates findings)
  Medium to High: 5 (PRESUMPTION-013, 015, 021, 025, 030)
  Medium: 13 (PRESUMPTION-001, 003, 004, 005, 008, 009, 010, 016, 019, 022, 026, 031, 032)
  Low to Medium: 7 (PRESUMPTION-006, 007, 012, 017, 018, 027, 033)
  Low: 3 (PRESUMPTION-023, 028, 034)

By status (2026-04-16):
  PARTIALLY-CHALLENGED: 11 (PRESUMPTION-001, 002, 003, 004, 005, 008, 009, 010, 012, 013, 014)
  CHALLENGED: 3 (PRESUMPTION-006, 007, 011)
  UNTESTED: 20 (4 from Apr 13 evening + 5 from Apr 14 + 5 from Apr 15 + 6 from Apr 16)

Key event (2026-04-16): Six new presumptions surfaced. PRESUMPTION-029 extends the epistemic-validation-gap cluster (024, 020, 021, 014) to the multi-subagent batch case — a 5-findings-in-one-day surge that was not examined for subagent-correlation inflation. PRESUMPTION-030 surfaces an 8-day version-control gap as potentially systemic rather than cosmetic. PRESUMPTION-031 questions the specialist-rotation schedule's empirical coverage. PRESUMPTION-032 aggregates the morning-handoff chain's intent-capture failures across two channels (Gmail, Chrome extension). PRESUMPTION-033 notes that the "well enough" checkpoint criterion for wiki_narration.html was defined by the assistant, not by Tom. PRESUMPTION-034 surfaces the "daily run" naming drift (an 8-day backlog labelled a single daily run).

## Notes

The highest-risk presumptions:
  - PRESUMPTION-002 (Thousand Brains transfer): CRITICAL RISK — entire architecture depends on this
  - PRESUMPTION-024 (selection effect on FINDING-011a): CRITICAL RISK — the system's most important output may be an artifact of its own design. This is the deepest self-awareness question: can a system designed to find cross-tradition connections reliably distinguish genuine connections from projections of its own structure?
  - PRESUMPTION-014 (cross-tradition signal validity): HIGH RISK — core output quality
  - PRESUMPTION-020 (AI synthesis bias profile): HIGH RISK — threatens the AI-as-synthesizer vision
  - PRESUMPTION-025 (Phase 2a unpause justification): MEDIUM-HIGH RISK — 33-agent deployment on unresolved foundations
  - PRESUMPTION-015 (self-referential circularity): MEDIUM-HIGH RISK — pipeline evaluated claims about itself
  - PRESUMPTION-021 (internal depth assessment): MEDIUM-HIGH RISK — system judges its own findings' significance
  - PRESUMPTION-013 (infrastructure resilience): MEDIUM-HIGH RISK — now resolved but pattern may recur

Thematic cluster (expanded): PRESUMPTION-024 joins the "epistemic validation gap" cluster (020, 021, 014). PRESUMPTION-029 (2026-04-16) now extends that cluster specifically to the multi-subagent batch case: if a 5-findings-in-one-day surge was inflated by correlated subagent prompting, the pattern detector's entire recent trajectory (FINDING-013 through -017) is under the same selection-effect question as FINDING-011a. The emails to the principals (PRESUMPTION-027) represent the first external test of this question; the subagent re-run proposed by PRESUMPTION-029 would be the first internal test.

Secondary cluster (operational infrastructure): PRESUMPTION-030 (8-day version-control gap), PRESUMPTION-032 (morning-handoff chain degradation), and PRESUMPTION-031 (rotation-schedule coverage gaps) together form a new "silent operational drift" cluster. Each individual failure was logged locally; none of them aggregated into an escalation. This pattern is adjacent to PRESUMPTION-013 (infrastructure resilience) and suggests the April 15 "fully operational" framing was about individual components, not system-level signal integrity.

14 of 34 presumptions have been reconciled with literature search results. 20 are UNTESTED and queued for 15a/15b.
