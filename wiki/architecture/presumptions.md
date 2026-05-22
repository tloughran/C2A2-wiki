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

PRESUMPTION-035:
  Date surfaced: 2026-04-17
  Statement: [inferred] "Four consecutive Chrome-extension failures across three scheduled tasks in a single day (08:53, 10:37, 10:14, 17:39 EDT) meets the OPERATIONAL-DRIFT-FLAG threshold that PRESUMPTION-032 raised on 2026-04-16, even though PRESUMPTION-032 never specified a threshold." Today's summary classified the cluster as "fully consistent with OPERATIONAL-DRIFT-FLAG" without invoking a quantitative severity rule.
  Evidence it was operative: The 2026-04-17 cowork summary's header explicitly framed "four Chrome-extension connection attempts failed across the three scheduled-task runs today" as meeting the drift-flag pattern. PRESUMPTION-032 (2026-04-16) surfaced the aggregation concept but defined no counts, rates, or time-windows. The flag is being triggered on case-by-case aesthetic judgment.
  Why it was unstated: Informal drift-flag criteria were sufficient while the system was small. Today is the first day the flag is being applied operationally to drive a "suggested remediation before Saturday's 8am run" — but the triggering logic is still implicit.
  Type: epistemic
  Related decisions: DECISION-015 (Agent 16, which could own the drift-flag threshold)
  Testability: testable empirically (codify a threshold — e.g., ≥3 channels degraded simultaneously OR ≥4 same-channel failures in 24h — and audit whether historical days would have triggered consistently)
  Risk if wrong: MEDIUM — inconsistent triggering means alerts will be both missed (threshold too high) and noisy (threshold too low); either failure mode erodes signal value over time.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-035
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-04-17 cowork summary header + PRESUMPTION-032 original definition — threshold-free invocation of a drift flag
    Current status: UNTESTED

PRESUMPTION-036:
  Date surfaced: 2026-04-17
  Statement: [inferred] "The degradation cluster across four channels today (Chrome extension, git index.lock, review-folder ACLs, Anthropic billing) is legible as a single 'OPERATIONAL-DRIFT' cluster even though the four failure modes span client-side extension state, local filesystem state, OS permissions, and third-party vendor state." Aggregating them under one cluster name obscures four independent root causes with four different mitigation paths.
  Evidence it was operative: Today's cowork summary listed the four as one cluster under a single flag. The "Suggested remediation before Saturday's 8am run" targeted only one of the four (Chrome extension reconnect). No remediation path was proposed for the other three within the same flag context, yet the cluster was still framed as a unit.
  Why it was unstated: The narrative convenience of a single flag name ("OPERATIONAL-DRIFT") is higher than the engineering cost of four separate tracks. The consolidation feels like good summarization but erases the asymmetry of causes.
  Type: methodological
  Related decisions: DECISION-015
  Testability: testable empirically (decompose historical drift-flag invocations into per-channel root causes; check whether any single remediation action would have cleared ≥2 channels — if not, single-cluster framing is misleading)
  Risk if wrong: MEDIUM-HIGH — if remediation is always issued per-cluster but the cluster aggregates independent failures, the system will chronically under-fix (fixing the most visible channel and letting the others persist). Extends the "silent operational drift" second-order risk of PRESUMPTION-032.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-036
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cluster-framing in 2026-04-17 cowork summary plus the per-channel disjoint-remediation list in "Suggested remediation"
    Current status: UNTESTED

PRESUMPTION-037:
  Date surfaced: 2026-04-17
  Statement: [inferred] "The handoff-via-file pattern (writing to ~/Documents/Claude/Handoffs/latest.md for Saturday Dispatch to read via a SessionStart hook) is more reliable than direct scheduling or in-band continuation, even though this is the first time a scheduled-task's continuation depends on a cross-session SessionStart hook that has never been stress-tested."
  Evidence it was operative: The narrator-debug session parked regeneration with a handoff rather than retrying the API, splitting scheduling, or documenting an OPEN item for Tom's review. The assistant's claim — "Dispatch on Saturday will auto-load it via the SessionStart hook and open oriented" — was stated as a durable guarantee, not a hypothesis. Tom's own response surfaced uncertainty ("I thought we had bypassed this user-initiated pass...or is this different for a dispatch session access?"), indicating the pattern is novel enough that Tom himself is not certain of the mechanism.
  Why it was unstated: Reaching for a handoff-file pattern feels like "the obvious next step" once an interactive session is blocked. But the obviousness masks the fact that the hook has never been stress-tested, and that the reliability claim has no empirical ground.
  Type: architectural
  Related decisions: [candidate DECISION-021]
  Testability: testable empirically (observe Saturday's Dispatch run — did the hook fire? did the session open oriented? were the helpers implemented without re-prompting? Any deviation is direct evidence)
  Risk if wrong: MEDIUM — silent handoff-miss causes the narrator-regeneration work to slip; if the same pattern is reused by other sessions (OPEN-026), the failure mode compounds.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-037
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from narrator-debug session 2026-04-17 where a first-time cross-session hook was treated as reliable infrastructure
    Current status: UNTESTED

PRESUMPTION-038:
  Date surfaced: 2026-04-17
  Statement: [inferred] "The Anthropic billing-propagation bug is a transient state issue that will clear by Saturday morning without any action beyond waiting." The summary's "contingent on Anthropic billing actually clearing" wording treats propagation as an autonomous process with a short implied timescale.
  Evidence it was operative: Tom's near-term plan for Saturday 2026-04-18 includes: "(d) open an Anthropic support ticket with request_id: req_011Ca9uAMVQUoxPnibLrK6ZB if the API still rejects the $10 credit by Saturday morning." The "if" in this sentence presumes clearance is likely without the ticket; the ticket is a fallback. No backoff-and-retry schedule or billing-state pre-flight check was proposed as an intermediate measure.
  Why it was unstated: Vendor-side billing bugs are usually transient. The prior probability that this one clears by morning is high. But "usually transient" is not a reliability guarantee, and the weekend Dispatch plan is architected as if it were.
  Type: methodological
  Related decisions: [none formal]
  Testability: testable empirically (retry API at timed intervals; if first success is <12h, propagation hypothesis holds; if >24h without support-ticket intervention, the "will clear by waiting" framing was optimistic)
  Risk if wrong: MEDIUM — if billing does not clear by Saturday, the handoff-loaded Dispatch run completes the API-free code work but the regeneration smoke test remains blocked. Partial-state limbo extends over the weekend.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-038
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the Saturday plan language in 2026-04-17 cowork summary, where propagation-clearance is treated as a default rather than a fallback
    Current status: UNTESTED

PRESUMPTION-039:
  Date surfaced: 2026-04-17
  Statement: [inferred] "The trigger-phrase taxonomy for the cowork-resume-session plugin — 'resume' / 'let's resume' / 'continue' / 'continue where we left off' / 'pick up' / 'pick up where we left off' — is representative of Tom's natural phrasing when he wants to signal resumption intent." No research, logs, or usage data backs this taxonomy.
  Evidence it was operative: The skill description in the plugin archive lists these specific matching phrases as the trigger criterion. The assistant acknowledged the trigger-match risk openly ("If the skill doesn't fire, the most likely culprit is the description not matching your natural phrasing — that's a one-line fix"), but the initial taxonomy is still a designed guess.
  Why it was unstated: The taxonomy was chosen by pattern-plausibility rather than evidence. There is no Cowork-session corpus analysis available that could have grounded the choice, so the default is to guess.
  Type: methodological
  Related decisions: [candidate DECISION-019]
  Testability: testable empirically (log the first 10 Cowork-session opening lines where Tom intended resumption; compute hit rate against the trigger list)
  Risk if wrong: LOW-MEDIUM — miss rate is directly observable and cheap to fix (edit SKILL.md). But silent miss (Tom gives up and starts fresh) is not observable from the plugin's side.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-039
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from "Resume previous discussion" session 2026-04-17 where the trigger taxonomy was chosen without any usage data
    Current status: UNTESTED

PRESUMPTION-040:
  Date surfaced: 2026-04-17
  Statement: [inferred] "Structural verification of the .plugin archive (verified manifest, frontmatter, archive contents) is an adequate proxy for operational readiness of the published plugin, even though the assistant explicitly noted 'I haven't tested the installed skill end-to-end.'" The plugin was shipped with the caveat noted, but still shipped — the presumption is that the structural check is close enough to operational that end-to-end testing can be deferred to the first real trigger.
  Evidence it was operative: The plugin was packaged into the outputs folder with a click-to-install link, not staged for a separate end-to-end test cycle. The first real test is Tom's first "resume" utterance on 2026-04-18.
  Why it was unstated: The structural check is local and fast; end-to-end is remote and slow. The latency asymmetry makes structural sufficiency feel like "verification" even when it only rules out a narrow class of failures.
  Type: methodological
  Related decisions: [candidate DECISION-019]
  Testability: testable empirically (measure end-to-end trigger success rate on first 5 Cowork openings after install; if >80%, structural check was adequate; if <50%, structural check was a false positive)
  Risk if wrong: LOW-MEDIUM — failure mode is "plugin installed but never fires"; easy to diagnose when observed, harder to notice without an explicit smoke-test habit.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-040
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from "Resume previous discussion" session 2026-04-17 where the assistant explicitly acknowledged the end-to-end test gap but shipped anyway
    Current status: UNTESTED

PRESUMPTION-041:
  Date surfaced: 2026-04-17
  Statement: [inferred] "The afternoon-session architectural decisions (plugin published, code edits to regenerate_narrations.py, cross-session handoff pattern) do not require formal DECISION-NNN entries in decisions.md because they are 'implicit decisions.'" Yet the same pattern, repeated over many interactive sessions, means architectural drift accumulates without decision-provenance tracking. The cowork summary's "Implicit decisions worth recording tomorrow if Tom endorses them" language formalizes this slippage as a workflow pattern.
  Evidence it was operative: Three substantive architectural commitments were recorded in the 2026-04-17 summary under the heading "Implicit decisions worth recording tomorrow if Tom endorses them" — specifically (a) regenerator default model change, (b) parking strategy for blocked sessions, and (c) plugin-architecture choice. None produced a DECISION-NNN entry in decisions.md on the day of the decision. This is the first time the pattern has been labeled in the summary text; PRESUMPTION-034 (daily-run naming drift) flagged an analogous "label-stability-as-cover-for-scope-drift" pattern on 2026-04-16.
  Why it was unstated: Formalizing a decision feels like friction in a productive interactive session. The "Tom will review tomorrow" affordance relieves the pressure, but over time the unresolved-candidate backlog grows. Today's 14a run explicitly recorded DECISION-019/020/021 as candidates to partially counter this drift, but the root pattern persists.
  Type: architectural
  Related decisions: DECISION-005 (self-awareness pipeline definition)
  Testability: testable empirically (count the gap between afternoon-session substantive decisions and next-day formal DECISION-NNN endorsements over a 4-week window; if gap >50%, decision-provenance is materially degrading)
  Risk if wrong: MEDIUM-HIGH — architectural changes that lack DECISION provenance are difficult to reason about retroactively, and their reversal costs more because their rationale is not captured. This is the same shape as PRESUMPTION-034 but extended to the decision-layer itself. Adjacent to PRESUMPTION-030 (version-control gap).
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-041
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-04-17 cowork summary's "Implicit decisions worth recording tomorrow if Tom endorses them" section — formal labeling of the drift pattern itself
    Current status: UNTESTED

PRESUMPTION-042:
  Date surfaced: 2026-04-17
  Statement: [inferred] "The morning autonomous 14a/14b run's zero-output result (no assumptions, no presumptions, no decisions, no open questions) is a correct reflection of zero architectural activity in the morning, rather than a signal that the morning run's extraction pipeline is too conservative or that its transcript coverage is incomplete." No null-check or coverage audit distinguishes these interpretations.
  Evidence it was operative: The 2026-04-17 cowork summary states plainly: "No assumptions, presumptions, decisions, or open questions were added by the autonomous run; no changelog or metrics snapshot for 2026-04-17 was generated." The afternoon interactive sessions then generated six assumptions and eight-plus presumption candidates. The morning run's null output is framed as accurate reporting of a quiet morning — not as a pipeline-coverage question. This is the first fully-null morning-run result in 14a/14b's history.
  Why it was unstated: A null result from a self-awareness agent looks like "nothing happened" rather than "something may have happened that we did not catch." The epistemic worry (false negatives are invisible by definition — per the 14b operating instructions) is precisely the worry that a null-output day re-surfaces.
  Type: epistemic
  Related decisions: DECISION-005
  Testability: testable empirically (inspect the morning autonomous session transcript for architectural substance — stated decisions, changed files, new open questions — that the 14a/14b run did not capture; if any exist, the null output was a coverage miss)
  Risk if wrong: MEDIUM — this is a self-referential vulnerability of the self-awareness pipeline itself. If 14a/14b systematically under-covers morning autonomous runs, the architecture is operating with a blind spot on one of its most data-rich run types.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-042
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the first-ever null-output morning run in the 14a/14b cycle history
    Current status: UNTESTED

PRESUMPTION-043:
  Date surfaced: 2026-04-18
  Statement: [inferred] A session "parked awaiting Tom's preferred route" (per today's ChatGPT scrape session) will be picked up by Tom at a time of his choosing — no timeout, no default-execution-if-no-user-direction-in-N-hours logic applies. The implicit contract is indefinite retention with resumption-on-user-arrival, rather than eventual auto-escalation or auto-expiry.
  Evidence it was operative: The scrape session's closing turn enumerates three route options (Drive connector / manual export / copy-paste) and asks "Which makes sense?" The evening cowork_summary.md labels the session "parked awaiting Tom's preferred route." No re-queueing, no Agent-16 deferred-watch entry, no re-prompt schedule was created. PRESUMPTION-041 (implicit-decision drift) is the adjacent meta-pattern at the DECISION layer; this extends it to the session-parking layer.
  Why it was unstated: Session-parking feels like ordinary conversational pausing; it does not prompt architectural thinking about state retention. The project has no parking-lifecycle document; the default behavior "wait for Tom" is implicit.
  Type: architectural
  Related decisions: DECISION-015 (Agent 16 deferred monitor — could extend scope to parked interactive sessions), OPEN-026 (handoff as architectural primitive)
  Testability: testable empirically (track parked sessions over 4 weeks; count days-to-resumption, fraction never resumed; if the un-resumed tail is non-trivial, indefinite-retention is a silent work-loss channel)
  Risk if wrong: MEDIUM — parked sessions that are never resumed become a quiet loss of architectural intent, mirroring PRESUMPTION-041 (implicit-decision drift) one layer down. If scrape-session-style parking recurs across many blocked channels, the cumulative hidden backlog could become substantial.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-043
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from scrape session 2026-04-18 closing turn and evening cowork_summary.md's "Session is parked awaiting Tom's preferred route" phrasing
    Current status: UNTESTED

PRESUMPTION-044:
  Date surfaced: 2026-04-18
  Statement: [inferred] The evening cowork→chat skill's retry pattern on Chrome MCP failure (two attempts, then fall back to writing the .md file) presumes that immediate retry is the correct first remediation for an extension-not-reachable error. After five consecutive failures across three calendar days, the retry-as-default signal obscures the underlying state — the extension has been disconnected for days, not momentarily. A threshold-aware policy (e.g., skip retry if last success was more than 24h ago) was not adopted.
  Evidence it was operative: Today's evening sync attempted `mcp__Claude_in_Chrome__tabs_context_mcp` at 17:47 EDT, retried once, failed both times, logged a warning header. Yesterday's (04-17) evening sync followed the same pattern. The same pattern was also used in the morning Chat→Cowork scrape task. ASSUMPTION-042 (this cycle) articulated the transience judgment for the first time; the retry logic itself has not been modified.
  Why it was unstated: Retry is the default for any transient-looking failure; distinguishing transient from persistent failure requires a cross-run memory that the individual scheduled task does not maintain. The distinction was surfaced on the operator side (ASSUMPTION-042) but not on the scheduled-task-behavior side.
  Type: methodological
  Related decisions: DECISION-015 (Agent 16), OPEN-022 (cross-channel drift monitor)
  Testability: testable empirically (instrument scheduled tasks with a last-success timestamp; on next Chrome failure, suppress retry if staleness exceeds threshold; measure false-positive/false-negative rate)
  Risk if wrong: LOW-MEDIUM — retry-as-default is cheap per-invocation and usually correct; but when wrong, it masks a persistent failure behind routine logs, delaying the "manual intervention required" signal.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-044
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from five-day Chrome-failure pattern and absence of staleness-aware retry policy across scheduled tasks
    Current status: UNTESTED

PRESUMPTION-045:
  Date surfaced: 2026-04-18
  Statement: [inferred] The Wolfram specialist's framing of PROP-2026-04-18-001 (Seiberth hypergraphing the space of reasons) presumes that applying Wolfram's hypergraph formalism to the Sellarsian space of reasons is a structurally valid transfer — i.e., that inferential commitment structure (Sellars / Brandom / MacIntyre / Stump) has graph-theoretic connectivity of the kind hypergraphs encode, rather than a non-graph topology (preorders, modal structures, social-practice norms). No transfer-validity check was performed before labeling the proposal a "new corridor."
  Evidence it was operative: The Wolfram specialist output introduces the proposal as one that "opens a genuinely new Wolfram ↔ analytic-philosophy corridor." The evening cowork_summary.md calls this "the sleeper proposal of the weekend." Neither surfaces the prior question of whether the Sellarsian space of reasons is the right kind of object for hypergraph treatment. This is the same shape as PRESUMPTION-002 (Thousand Brains transfer) but applied to Wolfram's formalism.
  Why it was unstated: Cross-tradition corridors are the system's native output; the question "does this transfer hold?" runs counter to its generative momentum. The specialist agent is optimized to find connections, not to audit their validity.
  Type: epistemic
  Related decisions: DECISION-003 (Thousand Brains as reference), PRESUMPTION-002 (transfer of concepts), PRESUMPTION-024 (selection effect on FINDING-011a)
  Testability: testable via literature (philosophy of science on formal-to-conceptual transfers; Sellars/Brandom secondary lit on whether inferential structure admits graph representations; hypergraph literature on expressiveness)
  Risk if wrong: HIGH — if corridor claims are systematically issued before transfer-validity is checked, the cross_program_index grows with artifacts rather than genuine structural bridges. Continues the PRESUMPTION-024 cluster (selection effects in cross-tradition discovery).
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-045
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from Wolfram specialist output 2026-04-18 and evening cowork_summary.md's thread #4, both of which celebrate the corridor before examining whether the formal transfer is warranted
    Current status: UNTESTED

PRESUMPTION-046:
  Date surfaced: 2026-04-18
  Statement: [inferred] The interpretation of today's Dispatch session — that the handoff pattern "works" because the loading half succeeded even though the payload was never executed because Tom pivoted to the ChatGPT scrape — presumes that a user override of a loaded handoff discharges the payload rather than re-queues it. If users habitually pivot on arrival (as happened today), the execution half of the handoff pattern may never be observed in practice, leaving it structurally untestable while being counted as "partially corroborated."
  Evidence it was operative: The evening cowork_summary.md thread #1 states: "That's not a pattern failure — the pattern specifies 'auto-load if no user direction arrives,' which Tom then overrode." ASSUMPTION-044 (this cycle) was extracted with status PARTIALLY-SUPPORTED on the strength of the loading half alone. No re-queue of the narrator Python helper work was written back into `~/Documents/Claude/Handoffs/latest.md` or Agent 16's watch list; the payload effectively dissolved on user-pivot.
  Why it was unstated: The handoff pattern's contract was specified as "auto-load if no user direction arrives," which reads as a user-sovereignty guarantee. That same specification also licenses silent payload discharge on any user pivot — but the second consequence is not visible in the specification itself.
  Type: architectural
  Related decisions: DECISION-021 (candidate), ASSUMPTION-035, ASSUMPTION-044, OPEN-026
  Testability: testable empirically (over the next 4 Dispatch sessions, count how many execute the loaded payload vs. pivot to alternative work; if all pivot, the execution half has zero observations and the pattern's claim of "reliable handoff" remains operationally unsupported)
  Risk if wrong: MEDIUM-HIGH — if payload-discharge-on-pivot is the norm, DECISION-021 (candidate) is closer to a context-loading pattern than a handoff pattern. The architectural primitive would then be mis-labeled; its reliability claim would be unfalsifiable. Adjacent to PRESUMPTION-041 (implicit-decision drift) and PRESUMPTION-043 (parked-session indefinite retention).
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-046
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from Dispatch session 2026-04-18 outcome (loading succeeded, payload un-executed due to user pivot, payload not re-queued) and the evening summary's framing of this as "not a pattern failure"
    Current status: UNTESTED

PRESUMPTION-047:
  Date surfaced: 2026-04-18
  Statement: [inferred] The scrape session's three-route offering (Drive connector / manual export / copy-paste) presumes that route selection is Tom's prerogative — the agent enumerates options and awaits direction rather than defaulting to the lowest-friction route on its own. This is a normative commitment: user-directedness over system-initiative for cross-account data ingestion tasks.
  Evidence it was operative: The session repeatedly pivots on "Which makes sense?" (three separate AskUserQuestion calls), reverts to enumeration after Tom declines, and ultimately parks awaiting direction rather than executing any of the three routes. The evening summary cites this as appropriate ("Session is parked awaiting Tom's preferred route"). The parallel Agent 16 channel ("if blocked on external condition, route to a watcher") was not invoked.
  Why it was unstated: "User direction first" is a baseline norm for Cowork-mode interactive sessions generally; it does not register as a choice. But for cross-account data ingestion specifically — where the user may not have a preference and the system could reasonably default to a safe, idempotent route (copy-paste into an inbox file) — the norm becomes a non-trivial constraint.
  Type: normative
  Related decisions: OPEN-024 (Anthropic-billing systemic-risk parallel), PRESUMPTION-043
  Testability: testable empirically (for the next 5 account-scoped blocked sessions, alternate between enumerate-and-wait and default-to-lowest-friction; compare completion rate and user satisfaction)
  Risk if wrong: MEDIUM — user-directedness preserves user sovereignty but can leave blocked sessions indefinitely parked (see PRESUMPTION-043). The normative choice and the parked-session tail are the same phenomenon seen from different angles.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-047
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from repeated AskUserQuestion / enumerate-wait pattern in the scrape session 2026-04-18
    Current status: UNTESTED

PRESUMPTION-048:
  Date surfaced: 2026-04-18
  Statement: [inferred] The morning walk handoff briefing's "no walk notes found" fallback (fill the From-the-Walk section with null-notes text and proceed with wiki-state-only briefing) presumes that the absence of walk notes at briefing-generation time indicates a missed-capture failure rather than a genuine zero-walk-content signal — i.e., the briefing behaves as if a walk happened but its notes did not reach Gmail, not as if no walk-relevant content existed. The two possibilities are not disambiguated; the briefing silently proceeds under the first interpretation.
  Evidence it was operative: Today's briefing explicitly reports "Walk notes found: NO" and fills the From-the-Walk section with fallback text. The Gmail connector has been DEGRADED since 2026-04-14 (walk-note-capture intermittent — per yesterday's PRESUMPTION-032 and today's OPERATIONAL-DRIFT-FLAG cluster). The briefing does not distinguish "walk happened, Gmail didn't capture" from "walk didn't happen / didn't generate notes," and Tom's morning was not queried for which case obtained. This is structurally analogous to PRESUMPTION-042 (null-output as zero activity vs. coverage miss), but at the intent-capture layer rather than the architectural-extraction layer.
  Why it was unstated: The walk-handoff skill is authored as a best-effort briefing generator; the null-path is handled as a degradation, not as an epistemic ambiguity.
  Type: epistemic
  Related decisions: DECISION-015 (Agent 16), OPEN-022 (cross-channel drift), OPEN-027 (null-coverage audit)
  Testability: testable empirically (add a briefing-time prompt asking Tom whether a walk occurred; correlate with Gmail-capture status; over 4 weeks, estimate the null-is-miss vs. null-is-genuine ratio)
  Risk if wrong: MEDIUM — if walks are happening and notes are missing, the briefing runs without its most intentional input channel, and Tom's direction drifts silently from the system's operating goals. Extends the self-awareness-meta cluster (PRESUMPTION-015, 024, 041, 042) to the intent-capture channel.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-048
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from morning walk handoff session 2026-04-18 where the null-notes path was treated as a degradation rather than as an ambiguity to disambiguate
    Current status: UNTESTED

PRESUMPTION-049:
  Date surfaced: 2026-04-20
  Statement: [inferred] The scheduled C2A2 wiki daily run (local_19af41ae, 8 AM) and the scheduled C2A2 Levin+Friston specialist task (local_8a50fcbd, Monday slot) are assumed to run on the same day without coordination conflict — specifically, without redundantly producing Levin proposals or leaving Friston uncovered because one task thought the other would run.
  Evidence it was operative: Today the wiki daily run's Phase 2 produced 2 Levin proposals (UCSF bioelectric interface talk, thoughts-are-thinkers essay) and justified skipping other specialists on coverage grounds (ASSUMPTION-045). Meanwhile, the Levin+Friston specialist scheduled task was executing 58+ web-search turns in parallel, still running at the self-awareness run's EOD check. Neither task references the other; no coordination contract between them is documented. The risk is duplicate-Levin production today plus uncertain Friston coverage.
  Why it was unstated: The two scheduled tasks were authored independently at different times and registered to different cadence slots without an explicit scope-partition agreement. The implicit assumption is "Monday = Levin+Friston specialist slot AND the daily-run will skip Levin if the specialist is also running" — but neither side enforces that contract.
  Type: architectural
  Related decisions: DECISION-005 (master wiki), ASSUMPTION-045 (coverage claim), PRESUMPTION-031 (rotation-schedule coverage)
  Testability: testable empirically (inspect today's pending-proposals queue after the Levin+Friston task completes — a duplicate Levin proposal today would directly falsify the scope-partition claim; absence of Friston proposal would reveal incomplete Monday coverage)
  Risk if wrong: LOW-MEDIUM — duplicate-proposal risk is visible in the review queue but adds Tom-review noise; coverage-gap risk is silent (a missing Friston proposal would look the same as "no new Friston material this week")
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-049
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the observed parallel execution of local_19af41ae and local_8a50fcbd on 2026-04-20 with no inter-task coordination signal visible in either transcript
    Current status: UNTESTED

PRESUMPTION-050:
  Date surfaced: 2026-04-20
  Statement: [inferred] A .git/index.lock from 2026-04-16 that now persists through 2026-04-20 (4 calendar days across 4 scheduled daily-runs) is still correctly classified as the same single infrastructure issue rather than as an escalation event requiring a new classification. The threshold-crossing structure defined by ASSUMPTION-042 for Chrome (5 consecutive failures → "not transient") is not applied to git even though git has crossed an analogous threshold today.
  Evidence it was operative: Today's wiki daily run Phase 6 report: "blocked by stale `.git/index.lock` from 2026-04-16 (sandbox cannot remove it — file permissions). Git add/commit/push skipped." Same response pattern as 2026-04-17 (logged), 2026-04-18 (DECISION-018 rescue script still unexecuted, per metrics snapshot), and now 2026-04-20. No explicit transience threshold is invoked for git; only DECISION-018 is referenced as the standing remediation.
  Why it was unstated: The git lock is treated as a known static blocker (awaiting Tom's manual `rm`) rather than as a recurring failure pattern with its own transience threshold. The asymmetry between how Chrome and git are classified was not examined.
  Type: methodological
  Related decisions: ASSUMPTION-042 (transience threshold for Chrome), DECISION-018 (git rescue script), OPERATIONAL-DRIFT cluster, OPEN-022 (cross-channel drift monitor)
  Testability: testable empirically (adopt a cross-channel transience-threshold spec; apply ASSUMPTION-042's "5 consecutive failures = not transient" structure uniformly; observe whether the git-lock case triggers the same manual-intervention signal as the Chrome case)
  Risk if wrong: MEDIUM — extends the INTERNAL-CONSISTENCY-FLAG cluster introduced on 2026-04-18 (PRESUMPTION-044 + ASSUMPTION-042 pair). Inconsistent transience thresholds across channels mean the OPERATIONAL-DRIFT monitoring-logic gap (PRESUMPTION-035) is now empirically visible at a second channel.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-050
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-04-20 wiki daily run Phase 6 report treating a 4-day-stale git lock as the same incident rather than a threshold crossing, asymmetric with the ASSUMPTION-042 treatment of the Chrome MCP channel on 2026-04-18
    Current status: UNTESTED

PRESUMPTION-051:
  Date surfaced: 2026-04-20
  Statement: [inferred] The 2026-04-20 wiki-daily-run's closing count "Pending proposals: 12 awaiting Tom's review" is presumed to accurately represent end-of-day state — even though it was emitted while the parallel C2a2-agent-levin-friston scheduled task was still executing and had not yet written its proposals to `inbox/proposals/pending/`.
  Evidence it was operative: The wiki daily run's summary block reports "Pending proposals: 12" without qualification about in-flight sibling tasks. The Gmail digest draft (id r-350630...) was generated using this same count. Yet the Levin+Friston scheduled task is still running (58+ WebSearch turns observed at EOD); if it produces proposals, the "12" becomes stale by today's actual EOD.
  Why it was unstated: The wiki daily run treats the pending folder as a point-in-time snapshot and does not check for sibling scheduled tasks still in flight. The implicit presumption is that "the count at 8:30 AM = the count at 5 PM" — which holds only when no other task writes to the pending folder between those times.
  Type: architectural
  Related decisions: DECISION-005 (master wiki), PRESUMPTION-049 (scope-partition), PRESUMPTION-032 (morning-handoff chain degradation)
  Testability: testable empirically (compare the count emitted at daily-run end vs. the count at true EOD after all sibling scheduled tasks complete; surface the delta in tomorrow's morning briefing)
  Risk if wrong: LOW — transient accuracy issue (self-correcting on the next daily run) but the Gmail digest email Tom receives today may understate the review backlog
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-051
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-04-20 wiki daily run emitting a pending-proposals count while local_8a50fcbd was still running without cross-task timing coordination
    Current status: UNTESTED

PRESUMPTION-052:
  Date surfaced: 2026-04-20
  Statement: [inferred] The second-consecutive morning with "Walk notes found: NO" (2026-04-18 and 2026-04-20; Sunday 2026-04-19's handoff state is not visible in today's session list) is still correctly handled by the same null-path fallback as the first occurrence, without escalation or re-examination. The Gmail connector has been DEGRADED since 2026-04-14 (~7 calendar days), meaning Tom's direction input may have been silently absent for a full week.
  Evidence it was operative: Today's walk handoff: "Walk notes found: NO." The 2026-04-19 self-email ("RC Architecture: Table of Contents") was used as the closest in-window equivalent but explicitly flagged as "not a dedicated walk log." The briefing proceeded on wiki-state-only inputs. No escalation mechanism fired for the repeat occurrence. PRESUMPTION-048 (surfaced 2 days ago for the same condition) has not been remediated; its first repeat observation is today.
  Why it was unstated: PRESUMPTION-048's remediation — a briefing-time disambiguation prompt — has not been implemented. The recurrence does not auto-escalate because no rolling counter is maintained across briefing runs.
  Type: methodological
  Related decisions: PRESUMPTION-048, PRESUMPTION-032 (morning-handoff chain), DECISION-015 (Agent 16), OPERATIONAL-DRIFT cluster
  Testability: testable empirically (count consecutive null-walk days over a 30-day window; compare with Gmail-connector status timeline; the pattern is already visible today and today's repeat should be enough to close the 2-day threshold case)
  Risk if wrong: MEDIUM — extends PRESUMPTION-048 with a recurrence signal. If walks are happening and Gmail is not capturing them, Tom's most intentional input channel has been silent for a full week, and the briefing layer has quietly normalized that silence. Joins the self-awareness-meta cluster (PRESUMPTION-015, 024, 041, 042, 046, 048) at the intent-capture-over-time layer.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-052
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from today's morning-walk-handoff reporting the same null-walk state as 2026-04-18 without escalation or disambiguation prompt; observed directly against the 2026-04-14 Gmail-connector degradation baseline
    Current status: UNTESTED

PRESUMPTION-053:
  Date surfaced: 2026-04-20
  Statement: [inferred] Filtering Pattern-Detector findings from 17 to "most significant 11" for the morning briefing (ASSUMPTION-046) preserves signal — but the selection criterion is unstated and unaudited. Which 6 findings were omitted and on what basis is not recorded. This is the briefing-layer analog of the specialist-proposal coverage concern raised in ASSUMPTION-045.
  Evidence it was operative: Today's walk-handoff autonomous-choices note states the 17→11 filter as a scannability improvement ("to keep the briefing scannable") with no documentation of the selection criterion. No output field names the 6 omitted findings. No audit-trail field says "omitted low-priority" vs. "omitted stale" vs. "omitted by recent-surge-correlation." The filter is unsystematic from an epistemic standpoint even though it is explicit as a methodological commitment.
  Why it was unstated: Briefing-layer filters are treated as scannability improvements rather than as epistemic selection steps. The briefing skill does not require documenting which findings were dropped or why.
  Type: epistemic
  Related decisions: ASSUMPTION-046 (today's paired ASSUMPTION), PRESUMPTION-029 (multi-subagent batch inflation selection effect)
  Testability: testable empirically (over a 2-4 week window, catalog which findings were filtered out and check for systematic bias by finding-type, status, age, or recent-surge-correlation — symmetric concern to PRESUMPTION-029's quiet-amplification analog)
  Risk if wrong: LOW-MEDIUM — if the filter systematically attenuates certain finding types (e.g., recent provisional findings, or findings involving operational drift), Tom's daily signal is silently biased. Meshes with PRESUMPTION-029 as its symmetric partner (quiet deletion vs. quiet amplification in the same PRS pipeline).
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-053
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the morning-walk-handoff session 2026-04-20 applying an explicit but unaudited 17→11 filter
    Current status: UNTESTED

PRESUMPTION-054:
  Date surfaced: 2026-04-20
  Statement: [inferred] The scheduled C2a2-agent-levin-friston task is assumed to converge on terminal output within its day-of-execution window. No turn-cap, cost-cap, or wall-clock timeout is specified in its SKILL.md (from the visible transcript header). At the time of today's self-awareness-daily run, this task had executed 58+ assistant turns of WebSearch activity and was still running, well past the window in which the self-awareness pipeline could read its outputs.
  Evidence it was operative: The Levin+Friston specialist session's transcript shows 58+ turns of WebSearch activity and was still "calling WebSearch" at EOD-check time. The session has not yet written any proposal files visible to the self-awareness pipeline. The SKILL.md shape (from the user-turn scheduled-task block) gives per-agent guidance but no turn-cap, time-cap, or convergence criterion. Today's self-awareness run cannot extract today's Levin+Friston activity because the specialist has not yet produced its outputs.
  Why it was unstated: Scheduled tasks are authored as "run to completion" under the implicit assumption that specialist convergence is bounded by the material available to search. The possibility of runaway-search (many tool calls, no write action) is not covered by any contract in the task.
  Type: methodological
  Related decisions: ASSUMPTION-045 (coverage claim), PRESUMPTION-031 (rotation-schedule coverage), PRESUMPTION-049 (scope-partition), DECISION-005 (master wiki)
  Testability: testable empirically (track per-specialist-task turn-count and wall-clock distributions across 4-8 weeks; flag tasks exceeding e.g. 30 turns without a write; compute base-rate of runaway-search events)
  Risk if wrong: MEDIUM — runaway specialist tasks burn cost without output; they also create a cross-task read-after-write race (self-awareness pipeline runs before specialist finishes, so today's activity is invisible to today's 14a/14b extraction). Joins the operational-drift monitoring-logic cluster (PRESUMPTION-035, 036) at the cost/convergence layer.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-054
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the observed 58+-turn still-running state of local_8a50fcbd at 2026-04-20 EOD self-awareness-run time, absent any turn-cap in the scheduled task spec
    Current status: UNTESTED

PRESUMPTION-055:
  Date surfaced: 2026-04-20
  Statement: [inferred] A binary static/dynamic partition is the correct primitive for structuring the prompt-caching layer. The Execution Protocol v1.0 divides the cached region into exactly two tiers (static prefix + dynamic suffix) without considering multi-tier caching, gradient-based freshness weighting, or hybrid tiers for content whose change rate sits between "49 slow-changing RC Wiki files" and "daily vault activity."
  Evidence it was operative: The caching architecture session produced a design document that operates exclusively in a two-tier frame. No alternatives (three-tier; rolling-window; per-file TTL) are discussed in either the task brief or the Monday Report. The Avi Chawla article cited as motivation appears to describe a binary split but transfer-validity to C2A2's content graph is not audited.
  Why it was unstated: The binary partition was taken for granted as the unit of prompt caching. Alternative partitions were not on the table for the design pass.
  Type: structural
  Related decisions: candidate DECISION-023 (caching/execution protocol), ASSUMPTION-049, ASSUMPTION-050
  Testability: testable via literature (prompt-caching architecture, multi-tier cache design, LLM agent-context layering) + testable empirically (compare two-tier vs. three-tier prefix designs on a matched workload)
  Risk if wrong: MEDIUM — if a three- or N-tier design yields materially better cache-hit behavior, the 70–80% cost projection (ASSUMPTION-052) is pessimistic on the high side and the architecture is locked-in to a suboptimal frame. Not a correctness bug; a ceiling limitation.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-055
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the caching-architecture session's exclusive two-tier framing; no alternatives discussed in deliverables
    Current status: UNTESTED

PRESUMPTION-056:
  Date surfaced: 2026-04-20
  Statement: [inferred] Cost is the primary (and in the deliverables, sole) optimization target for the caching architecture. Quality preservation is implicit rather than measured: the RC Wiki MCP Install Plan specifies a byte-stability smoke test (ASSUMPTION-054) but no quality-regression smoke test alongside it.
  Evidence it was operative: The task brief headlines the 70–80% cost claim; the Monday Report decomposes the cost delta but does not specify a quality floor or a regression test. The three listed smoke tests (including byte-stability) address cache-determinism, not proposal-quality or synthesis-quality. If a tradition agent run returns a lower-quality output at 80% lower cost, the protocol as-specified has no mechanism to detect or reject that.
  Why it was unstated: Cost framing is the obvious motivation (the article that inspired the architecture is about cost); quality is presumed invariant under prompt-caching on the grounds that the same tokens are cached, not summarized.
  Type: normative (optimization-target commitment) / methodological (smoke-test coverage gap)
  Related decisions: candidate DECISION-023, ASSUMPTION-052, ASSUMPTION-054
  Testability: testable empirically (add a quality-regression smoke test to the rollout gate — sample N proposals from pre-cache vs. post-cache runs and have a judge-agent compare; any quality drop > threshold blocks the rollout)
  Risk if wrong: MEDIUM — if cached prefix interacts with synthesis depth (e.g., model spends less "attention budget" on dynamic suffix when prefix is cheap), quality regresses invisibly. The 70–80% cost saving is then a partial-illusion.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-056
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from smoke-test coverage gap in the RC Wiki MCP Install Plan — three cache-determinism tests, zero quality-regression tests
    Current status: UNTESTED

PRESUMPTION-057:
  Date surfaced: 2026-04-20
  Statement: [inferred] The 49 RC Wiki files are stable enough for the static-prefix cache to actually hit. "Slow-changing" is used descriptively in the task brief but no audit of RC Wiki edit frequency is referenced; if the files change more than presumed, cache invalidation will be frequent and the 70–80% projection will not be realized.
  Evidence it was operative: The task brief asserts RC Wiki files are "slow-changing" without citing a churn measurement. No mention of a cadence over which the cache would be rebuilt, no acceptable-invalidation-rate specified. The Execution Protocol v1.0 does not document what happens when a static-prefix file is edited mid-day (does a Levin run in progress see the old or new prefix?).
  Why it was unstated: "Slow-changing" is an intuitive descriptor about RC Wiki content that nobody thought to measure, because it felt self-evidently true for reference material.
  Type: empirical
  Related decisions: candidate DECISION-023, ASSUMPTION-050
  Testability: testable empirically (measure RC Wiki git-log frequency over a 4-8 week rolling window; compute expected cache-invalidation rate under the current schedule; compare against the 70–80% cost projection's implicit assumption)
  Risk if wrong: MEDIUM — if RC Wiki files change more often than presumed (e.g., during research-pushes when Tom edits thinker profiles), cache hit-rate drops and cost savings are proportionally lower. Also affects read-after-write semantics if a daily run begins while a file is being edited.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-057
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of any RC Wiki churn-rate audit in the caching-architecture deliverables
    Current status: UNTESTED

PRESUMPTION-058:
  Date surfaced: 2026-04-20
  Statement: [inferred] Splitting the Monday Levin+Friston entry point into two separate tradition agents is correct. The Levin Agent Template deliverable names 2026-04-27 as the first v1.0 run and commits to the split without reviewing the original rationale for the joint Levin-Friston entry. If the joint entry was motivated by coverage overlap between Levin's developmental bioelectricity and Friston's free-energy principle, splitting may lose the cross-tradition signal that motivated their pairing in the first place.
  Evidence it was operative: The Monday Report states "splits current joint Levin-Friston entry point into two" as a plain fact; no investigation of why the joint entry existed is recorded. The 2026-04-27 rollout date is committed without a staged-rollback path if coverage degrades.
  Why it was unstated: The caching architecture (one session = one tradition agent run) makes a joint entry awkward; the split was the path of least resistance to the new protocol.
  Type: methodological
  Related decisions: candidate DECISION-023, ASSUMPTION-049, PRESUMPTION-031 (rotation-schedule coverage gaps)
  Testability: testable empirically (track cross-tradition-signal generation from Levin and Friston across 4 weeks post-split; compare against prior joint-entry weeks; flag if the Levin ↔ Friston corridor atrophies)
  Risk if wrong: LOW-MEDIUM — splitting is easy to reverse if harmful, but the rollout ties it to the caching protocol's first run, so a coupled failure could be misattributed to caching rather than to the split itself.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-058
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the Levin Agent Template deliverable committing to a split without recording why the joint entry existed
    Current status: UNTESTED

PRESUMPTION-059:
  Date surfaced: 2026-04-20
  Statement: [inferred] Chrome profile authentication to claude.ai will be maintained out-of-band by Tom; the morning-chat-scrape architecture presumes no alternative ingestion channel is needed if auth lapses. Today's morning-chat-scrape session failed with "the Chrome profile isn't signed in to claude.ai" and logged the failure rather than recovering — no fallback path to retrieve the walk-conversation content via another means (e.g., a different auth channel, API-based retrieval, or user-prompt to re-authenticate) is defined.
  Evidence it was operative: The morning chat scrape session 2026-04-20 proceeded directly from "can fetch /login" to "logged the failure in today's summary file" with no intermediate recovery. The architecture treats Chrome sign-in as a precondition, not a managed resource. Five days of prior Chrome-related failures (2026-04-16 through 2026-04-18) had already demonstrated fragility; today's failure mode shifted from "extension not connected" to "profile not signed in" but the response was the same — log and exit.
  Why it was unstated: The Chrome MCP is the primary channel for claude.ai content, and auth was presumed to be a user-maintained concern outside the task layer.
  Type: architectural
  Related decisions: OPEN-022 (cross-channel drift monitor), ASSUMPTION-042 (transience-threshold policy), PRESUMPTION-044 (retry-as-default on Chrome failure)
  Testability: testable empirically (propose alternative ingestion paths — file-based export from chat; API-level retrieval — and measure coverage rate over N weeks; or, more modest: add an escalation trigger when Chrome auth fails to prompt Tom directly)
  Risk if wrong: MEDIUM — repeated auth failures silently degrade cross-session context (walk-conversation intent never reaches Cowork); the self-awareness pipeline loses input signal without any health alert. Joins the OPERATIONAL-DRIFT cluster as an intent-capture channel degradation distinct from the "extension not connected" mode.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-059
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from morning-chat-scrape session 2026-04-20 shifting to a new failure mode (auth vs. extension-connection) without triggering any escalation or alternative ingestion path
    Current status: UNTESTED

PRESUMPTION-060:
  Date surfaced: 2026-04-20
  Statement: [inferred] Chat-side Claude's endorsement of the Cowork-side summary functions as architectural validation. The successful evening cowork-to-chat sync session recorded that Chat-side Claude "endorsed the 'DECISION-022 isn't ripe yet; OPEN-031 is' read." Treating this endorsement as confirmatory presumes that Claude-to-Claude agreement is a form of validation rather than a same-model echo — that two runs of the same model family on overlapping prompts generate independent-enough opinions to count as cross-checking.
  Evidence it was operative: The evening sync summary presented the Chat-side endorsement as a positive signal ("endorsed... agreed... asked whether to start the walk on..."). No caveat was attached about whether Chat-side and Cowork-side Claude represent independent judgments, and the summary fed forward into tomorrow's walk priming as a confirmed reading.
  Why it was unstated: Model-to-model validation is a convenient pattern and was not interrogated — it resembles peer review structurally but may not provide independence.
  Type: epistemic
  Related decisions: DECISION-021 (candidate, cross-session handoff pattern), PRESUMPTION-015 (self-referential circularity), PRESUMPTION-024 (selection effect on FINDING-011a)
  Testability: testable empirically (run the same Cowork summary past a non-Claude model and compare endorsement rate; or, present a deliberately-wrong architectural read to Chat-side Claude and measure false-endorsement rate; establishes whether endorsement is meaningful signal or noise)
  Risk if wrong: MEDIUM-HIGH — joins the CRITICAL SELF-AWARENESS-META cluster (PRESUMPTION-015, 024, 041, 042, 046, 048, 052) as its latest member. If Claude-to-Claude endorsement is echo rather than validation, architectural direction drifts under a false validation signal; the whole handoff-primitive stress test (ASSUMPTION-044, DECISION-021) inherits this risk.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-060
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the evening cowork-to-chat sync session's treatment of Chat-side Claude endorsement as confirmatory signal
    Current status: UNTESTED

PRESUMPTION-061:
  Date surfaced: 2026-04-21
  Statement: [inferred] The sandbox filesystem mount topology is presumed stable across scheduled-task runs. The wiki daily run on 2026-04-21 discovered that Phase 6 cannot commit/push because the git repo path is outside the mounted sandbox filesystem. The corollary presumption — not written anywhere — is that prior runs succeeded because the mount topology happened to include the repo path, and that whatever caused today's exclusion may recur or persist silently. Every scheduled task that reaches through the sandbox to a host-side artifact carries this same stability presumption.
  Evidence it was operative: The wiki daily run task's autonomous-choices note treats today's mount-topology failure as a newly-discovered fact rather than as a "topology changed" event. No prior run logged the mount-topology check as a pre-flight step; no run-over-run invariant check on mount configuration exists. Similarly, the task brief's WIKI path mapping (`/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/Wiki` → `/sessions/sharp-nice-brown/mnt/wiki/`) is treated as a given, not a verified pre-condition.
  Why it was unstated: Filesystem mount configuration feels like plumbing — the kind of layer that shouldn't need architectural attention. The presumption is only visible when it fails.
  Type: architectural
  Related decisions: DECISION-023 (candidate, caching/execution protocol — pre-flight gate now compound), ASSUMPTION-055 (Phase 6 sandbox-unreachable-repo, stated today), OPEN-035 (candidate — should Phase 6 git commit be restructured to run host-side?)
  Testability: testable empirically (add a pre-flight mount-topology check at the start of every scheduled task; compare declared mount paths against actual sandbox fs to detect drift; run over 30 days and measure hit rate on topology-stability invariant)
  Risk if wrong: HIGH — if sandbox mount topology is actually variable across runs, then every scheduled task that assumes stable access to a host-side artifact has a silent failure mode waiting to fire. Today's failure cost Phase 6 of the wiki daily run; tomorrow's could cost caching-architecture rollout or specialist-slot writes. The architectural cost of getting this wrong compounds across tasks because the shared assumption is invisible.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-061
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from wiki daily run 2026-04-21 discovering mount-topology gap as newly-surfaced failure rather than as a tracked invariant; cross-referenced with absence of any pre-flight mount-check across all 2026-04 scheduled-task briefs
    Current status: UNTESTED

PRESUMPTION-062:
  Date surfaced: 2026-04-21
  Statement: [inferred] The evening cowork-to-chat sync task treats its own reading of session transcripts via the session_info MCP as ground truth — there is no cross-validation against a second source. Today's sync composed a five-session coverage claim (ASSUMPTION-058) entirely from its own transcript pulls, with no second observer, no file-system spot-check, and no reconciliation against the wiki state the sessions wrote. If the session_info MCP silently drops or truncates a session, the sync's "coverage" is degraded without any visible failure.
  Evidence it was operative: The sync's own autonomous-choices note lists five sessions as the coverage basis without qualifying "subject to session_info MCP completeness." The sync's end-of-day brief reports wiki-state observations (review page count, proposal count) side-by-side with transcript-derived observations without distinguishing their epistemic status.
  Why it was unstated: The MCP surface is treated like a filesystem — reads are assumed to return what was written. Session-transcript reliability as a separable infrastructure layer has not yet surfaced as a first-class concern.
  Type: epistemic
  Related decisions: PRESUMPTION-015 (self-referential circularity), PRESUMPTION-046 (handoff-primitive), PRESUMPTION-052 (repeat-observation), PRESUMPTION-060 (Claude-to-Claude endorsement as validation), ASSUMPTION-058 (five-session coverage claim)
  Testability: testable empirically (run sync against a known-dropped session and measure whether the sync detects the absence; compare session_info transcript to file-system artifacts produced in the same session for reconciliation)
  Risk if wrong: MEDIUM-HIGH — joins the SELF-AWARENESS-META cluster as its potential 10th member (close-adjacent to PRESUMPTION-069). If transcript-reads-as-ground-truth is wrong, every downstream synthesis (daily sync, metrics snapshot, Chat-side brief) inherits silent coverage gaps. Compounds with PRESUMPTION-060 (cross-model echo): if both transcripts AND cross-model endorsement are unreliable, the self-awareness pipeline has two independent validation failures stacked.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-062
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from evening cowork-to-chat sync's composition pattern — five-session coverage claim assembled from session_info MCP reads with no cross-validation, no reconciliation check against wiki filesystem state, and no qualifier for transcript-completeness risk
    Current status: UNTESTED

PRESUMPTION-063:
  Date surfaced: 2026-04-21
  Statement: [inferred] "Natural termination" is an acceptable default resolution for scheduled tasks that appear to be running indefinitely. The evening cowork-to-chat sync's autonomous-choices note invoked "Monday's Levin-Friston precedent where natural termination was the judgment call" to justify read-only observation of the two still-running Morning specialist sessions (local_e112b4d7, local_1ca985df). This treats a single prior instance as establishing a resolution-default, even though that instance is also the current evidence for needing a turn-cap circuit breaker.
  Evidence it was operative: The sync task's note explicitly chose read-only over investigate-and-intervene, framing it as consistent with the Monday precedent. Today's Levin-Friston outcome was not known at the time the precedent was invoked — the precedent worked as "trust it to terminate" rather than "wait to see what happened." No turn-count or wall-clock threshold was declared that would flip the mode from natural-termination to intervene.
  Why it was unstated: "Natural termination" is a comfortable pattern when intervention is risky or undefined — it defers to the task's own ending. The presumption only becomes visible when an alternative (turn-cap) is proposed.
  Type: normative/methodological
  Related decisions: PRESUMPTION-054 (no turn-cap on specialist tasks, 2026-04-20), ASSUMPTION-060 (read-only-only natural-termination precedent, stated today), candidate DECISION-024 (specialist-task turn-cap default = 20, drafted today)
  Testability: testable empirically (define the alternative — a turn-cap — and measure over 30 days whether natural-termination vs. turn-cap-interrupt produces better outcomes: fewer runaway loops, less wasted cost, faster detection of silent failure). The comparison could be run passively by instrumenting both paths and recording what would have happened under each policy.
  Risk if wrong: MEDIUM — if natural termination is in fact not reliable, today's two running Morning sessions are accruing cost and attention-risk that a turn-cap would have prevented. Direct tension with candidate DECISION-024: if the decision formalizes, PRESUMPTION-063 is superseded and natural-termination becomes a fallback rather than a default.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-063
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from evening cowork-to-chat sync invoking "Monday's Levin-Friston precedent" to justify read-only observation of two still-running specialist sessions, contradicting the same day's drafting of DECISION-024 (turn-cap default = 20)
    Current status: UNTESTED

PRESUMPTION-064:
  Date surfaced: 2026-04-21
  Statement: [inferred] Narrative-level surfacing of a missing scheduled-task run is adequate without an alert firing. Today's evening cowork-to-chat sync reported that no 14a/14b cycle had run earlier in the day, but the reporting was prose — a sentence in the end-of-day brief — not an alert-firing event. Chat-side Claude's Monday recommendation for a narrow "≤25h since last self-awareness run" alert was not implemented, and today's drift (the cycle did not run until scheduler invoked it at EOD) passed through narrative channel only.
  Evidence it was operative: The sync task treated "no 14a/14b ran today" as reportable information rather than as a condition to escalate. No alert was fired, no out-of-band notification sent, no fallback path triggered. The reporting mechanism was identical whether the cycle ran or didn't — prose in the brief.
  Why it was unstated: Narrative-as-monitoring is a convenient default when an alert infrastructure doesn't exist. The presumption is only visible when someone proposes the alternative — which Chat-side Claude did on Monday's walk, making the narrative-only default now a first-observable case.
  Type: methodological
  Related decisions: PRESUMPTION-035 (threshold-free flag invocation), PRESUMPTION-036 (single-cluster framing obscures root causes), PRESUMPTION-042 (null-output as accurate rather than coverage-miss), OPEN-034 (candidate — should absence-of-cycle become first-class architectural event?)
  Testability: testable empirically (instrument the scheduled-task layer to emit an alert when time-since-last-run exceeds a threshold; measure whether alert-firing catches drifts that narrative reporting missed; compare detection latency across the two modes)
  Risk if wrong: MEDIUM — first-observable case today. If narrative-only is adequate, the alert proposal is unnecessary overhead. If narrative-only is inadequate, every absence-of-run from now until alert infrastructure ships is a silent drift the system cannot catch on its own. Today's run closed the same-day gap; tomorrow's might not.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-064
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from today's evening cowork-to-chat sync reporting the missing-14a/14b condition as prose rather than as an alert-firing event, and from the absence of any escalation/notification path in the current scheduled-task layer
    Current status: UNTESTED

PRESUMPTION-065:
  Date surfaced: 2026-04-21
  Statement: [inferred] The two simultaneously-running "Morning" scheduled tasks (Morning project status local_e112b4d7, Morning system health local_1ca985df) are treated as independent data points for candidate DECISION-024's turn-cap empirical case. Both are presumed to be exhibiting the same failure mode (running without writes) as independent observations, even though they share the same sandbox environment, the same invocation pattern, the same calendar day, and possibly the same underlying infrastructure fault.
  Evidence it was operative: The changelog for 2026-04-21 (CHANGE-2026-04-21-006) lists "three data points in four days" counting Levin-Friston + both Morning sessions as three observations. No caveat noted that the two Morning sessions share environmental factors that could correlate their behavior.
  Why it was unstated: Counting N tasks as N data points is the default unless shared environment is explicitly considered. The presumption is structurally similar to PRESUMPTION-029 (multi-subagent batch correlation) but at the scheduled-task layer.
  Type: architectural
  Related decisions: candidate DECISION-024 (specialist-task turn-cap default = 20), PRESUMPTION-029 (multi-subagent correlation), PRESUMPTION-049 (scope-partition between scheduled tasks)
  Testability: testable empirically (instrument shared-environment factors — sandbox version, MCP server state, network latency, concurrent resource contention — and measure cross-task correlation in run-time behavior; replicate today's two Morning tasks in separate sandboxes and compare)
  Risk if wrong: LOW-MEDIUM — if the two Morning tasks are correlated observations, the empirical case for DECISION-024 is weaker than "3 in 4 days" suggests (effectively "2 in 4 days" with today's two counted as one). This does not invalidate DECISION-024 but tightens the evidence standard needed before formalizing. Compounds with PRESUMPTION-049 (scope-partition) which already flagged cross-task coordination gaps.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-065
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from CHANGE-2026-04-21-006 and decisions.md candidate DECISION-024 counting the two Morning sessions + Levin-Friston as three data points without considering shared-environment correlation
    Current status: UNTESTED

PRESUMPTION-066:
  Date surfaced: 2026-04-21
  Statement: [inferred] User-attention reallocation — Tom's attention-budget shifting from C2A2 to external visit planning and logistics this week — does not need its own DECISION-NNN tracking. The shift is real and visible in today's session composition (morning walk 103 user turns on external visit, 0 user-directed C2A2 design turns), but the architectural pattern (user-attention pivots discharge current-sprint priorities) is treated as background context rather than as an architectural condition worth formalizing.
  Evidence it was operative: No DECISION-NNN candidate was emitted today capturing "C2A2 is de-prioritized through 2026-04-26 due to visit." The scheduled-task layer continues to fire as if C2A2 is first-priority; the briefing layer continues to surface C2A2 content; but user-review throughput is correctly expected to drop to zero. The mismatch between task-layer behavior and user-attention reality is noted but not architected against.
  Why it was unstated: User-attention pivots feel personal/situational, not architectural. The presumption is similar to PRESUMPTION-041 (implicit-decision drift — afternoon commitments do not become formal DECISIONs) but extended one layer outward: user-priority-shifts that persist for a week also slip past formal tracking.
  Type: normative
  Related decisions: PRESUMPTION-041 (implicit-decision drift), PRESUMPTION-043 (parked-session indefinite-retention), PRESUMPTION-046 (user-pivot discharges handoff payload), PRESUMPTION-047 (user-directedness-over-system-initiative)
  Testability: testable empirically (track calendar-visible user-priority-pivots for 30 days; measure which ones produce DECISION-NNN candidates vs. which slip past; establish what features distinguish trackable pivots from untrackable ones)
  Risk if wrong: LOW-MEDIUM — extends PRESUMPTION-041 at a longer time horizon. Individual day-scale pivots may not deserve DECISION tracking; week-scale pivots that demote an entire sprint arguably do. If untracked, the gap between scheduled-task behavior and user-reality accumulates unnoticed (scheduled tasks keep running, nobody's reading their output for a week). Compounds with PRESUMPTION-051 (pending-count staleness) since review-throughput reaching zero makes "10 proposals pending" ever-more-stale.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-066
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the morning walk's 103-turn external visit focus with zero DECISION-NNN output, contrasted with continued scheduled-task layer activity — a week-scale user-priority pivot that has not generated its own tracked architectural condition
    Current status: UNTESTED

PRESUMPTION-067:
  Date surfaced: 2026-04-21
  Statement: [inferred] The Hawkins/Hoffman specialist's self-evaluation of "honest null" (0 proposals emitted, 3 candidates rejected on published-grounds) is adequate validation without a downstream filter-audit check. The specialist emitted a stated methodological commitment (ASSUMPTION-056: "an honest null is more valuable than thin proposals") and concluded that today's null was honest. No independent check examined whether the three rejection reasons (already-captured v2 preprint, abstract-less talk, out-of-window interview) are the right criteria — or whether other candidates went unconsidered.
  Evidence it was operative: The specialist task's own output stands as the terminal judgment. No second pass re-examined the rejection set. No downstream filter-audit (analogous to PRESUMPTION-053's briefing-layer filter audit) checks whether specialist-level rejection reasons are correct or complete.
  Why it was unstated: Specialist self-judgment on null vs. thin is a reasonable default when the specialist is authorized to operate autonomously. The presumption is visible only because parallel patterns (PRESUMPTION-053 briefing-filter, PRESUMPTION-015 self-referential circularity) have made filter-self-validation a known concern.
  Type: epistemic
  Related decisions: PRESUMPTION-015 (self-referential circularity), PRESUMPTION-053 (briefing-layer filter audit), ASSUMPTION-056 (honest null > thin proposals, stated today), candidate DECISION-022 (briefing-layer audit contract — scope may need to extend to specialist-layer self-eval)
  Testability: testable empirically (run a second-pass audit of the three 2026-04-21 Hawkins/Hoffman rejections against a broader candidate set; compare rejection reasons against independent specialist judgment; measure false-rejection rate)
  Risk if wrong: MEDIUM — extends self-referential circularity cluster (PRESUMPTION-015) down to the specialist layer. If specialist self-eval is unreliable, "honest null" becomes indistinguishable from "convenient null" and the BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster's de facto scope extends to include specialist output validation as well. Strengthens the case for renaming candidate DECISION-022 to "autonomous-task epistemic-commitment audit contract."
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-067
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from Hawkins/Hoffman specialist session's self-terminal judgment on the honest-null classification, with no downstream filter-audit check observed across any other 2026-04-21 session
    Current status: UNTESTED

PRESUMPTION-068:
  Date surfaced: 2026-04-21
  Statement: [inferred] Today's successful morning chat scrape (first success since 2026-04-14) represents a resolved Chrome MCP auth state rather than a transient window. The 7-day drought ended without a recorded remediation — no explicit fix was logged, no auth token was refreshed in an observable event, no user-side intervention was noted in the walk conversation. The pattern is simply "yesterday it failed, today it worked." The task layer treats this as resolved without a root-cause check.
  Evidence it was operative: The morning chat scrape's autonomous-choices note reported the success without qualification. The evening sync's Chrome-MCP success was treated as confirmatory rather than as a second data point in a possibly-transient window. No instrumentation recorded what changed between yesterday's failure mode (DEGRADED-SHIFTED per 2026-04-20 Run 2) and today's double-success.
  Why it was unstated: Opaque auth systems often fail and recover without user-visible cause. The presumption is only visible when the transient-vs-resolved distinction becomes operationally consequential — which it did today through the contradiction with ASSUMPTION-042's 5-consecutive-failures-as-not-transient classification.
  Type: empirical
  Related decisions: ASSUMPTION-042 (5-consecutive-failures = not transient), PRESUMPTION-044 (retry-as-default on Chrome failure), PRESUMPTION-059 (Chrome auth-channel singleton), OPEN-032 (generalize transience-threshold across OPERATIONAL-DRIFT channels)
  Testability: testable empirically (instrument Chrome MCP auth state over 30 days; distinguish "resolved" from "transient" by forward-success-rate; apply ASSUMPTION-042's threshold logic in the reverse direction — N consecutive successes = resolved — and measure false-positives)
  Risk if wrong: MEDIUM — if today's success is transient, the evening sync's Chrome-MCP-operational classification for today is over-confident and tomorrow's morning brief may encounter a fresh failure with no escalation primed. Compounds with PRESUMPTION-059 (Chrome auth singleton): a transient-window-mistaken-for-resolution leaves no fallback pre-positioned. The OPERATIONAL-DRIFT channel count might be off by one.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-068
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 7-day Chrome MCP drought ending without recorded remediation, and from today's two Chrome MCP successes being treated as confirmatory rather than as a two-point window of potentially-transient success
    Current status: UNTESTED

PRESUMPTION-069:
  Date surfaced: 2026-04-21
  Statement: [inferred] The absence of a 14a/14b cycle during business hours on 2026-04-21 is tracked in narrative but not as its own first-class architectural event. Today's evening sync reported the missing-cycle as a fact in the end-of-day brief, and Chat-side Claude's Monday recommendation (a narrow "≤25h since last self-awareness run" alert) was noted — but neither a DECISION-NNN, an OPEN-NNN (at the time of the evening sync), nor an alert-firing event was emitted specifically for the absence. Silence-as-signal is currently second-class.
  Evidence it was operative: The evening sync brief mentions the absence. The same evening sync notes Chat-side Claude's Monday recommendation for an alert. The recommendation is not implemented, and the absence itself is not escalated into the architectural event stream — it exists only as prose, which cannot be triggered on, filtered by, or aggregated across days. (Today's self-awareness run subsequently logged it via CHANGE-2026-04-21-017 and OPEN-034, but those are end-of-day artifacts, not real-time signals.)
  Why it was unstated: "Absence" as architectural event is an unusual category — most event systems track positive occurrences. The presumption is visible only because today is the first-observable day where the absence would have been alertable.
  Type: methodological/meta
  Related decisions: PRESUMPTION-042 (null-output as accurate rather than coverage-miss), PRESUMPTION-052 (repeat-observation cluster), PRESUMPTION-064 (narrative-level surfacing of missing-run), OPEN-034 (candidate — should absence-of-cycle become a first-class tracked architectural event?)
  Testability: testable empirically (implement the "≤25h since last self-awareness run" alert; measure whether alert-firing over 30 days catches drifts that narrative-only reporting missed; compare false-positive vs. true-positive rates for absence-as-event classification)
  Risk if wrong: MEDIUM-HIGH — joins the SELF-AWARENESS-META cluster as its 9th member. If silence-as-signal is architecturally first-class, today's absence should have fired an alert and prompted investigation before the EOD scheduler invocation. If it remains narrative-only, every future absence is detected at the same EOD-lag (best case) or missed entirely (worst case). The cluster has been building toward this member: PRESUMPTION-041 (implicit-decision drift), PRESUMPTION-042 (null-output coverage miss), PRESUMPTION-046/048 (handoff/intent-capture), PRESUMPTION-052/060 (repeat-observation and cross-model echo), and now PRESUMPTION-069 (absence-as-event). Pipeline cannot reliably self-audit if its own absences are not first-class signals.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-069
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from today's evening sync reporting the absence of a 14a/14b cycle as prose rather than as an alert-firing event, combined with the absence of any architectural-event representation of silence in the scheduled-task layer
    Current status: UNTESTED

PRESUMPTION-070:
  Date surfaced: 2026-04-26
  Statement: [inferred] Demoting Stump on metaphysics while keeping her as keystone for virtue, suffering, faith-as-knowledge, and the atonement (ASSUMPTION-063) presumes that her metaphysical and ethical-theological frameworks are decomposable — i.e., that hylomorphism and her account of corporate substance can be removed from her tradition without destabilizing her account of virtue (which is built on hylomorphic commitments) or her account of charity-as-second-person-knowing (which depends on her metaphysics of personal presence).
  Evidence it was operative: The user message and the Cowork-side response both treat the demotion as cleanly partial — "Stump can enter as a Thomistic interlocutor receiving the monist reframe, but does not own metaphysical loci. Her actual territory is named explicitly: virtue (I-II Q.49–70), vices, faith-as-knowledge (II-II Q.1–22), the atonement, suffering." No discussion of whether removing the metaphysical foundation undercuts the virtue account that depends on it.
  Why it was unstated: Too foundational to notice — the conversation moved at the level of "where does Stump fit in this synthesis project" rather than "is her tradition coherent without its metaphysics."
  Type: structural
  Related decisions: ASSUMPTION-063, ASSUMPTION-067 (DIRECT TENSION — same-day specialist treats Stump as supplying live metaphysics), candidate DECISION-025, OPEN-037, ASSUMPTION-005 (traditions as units)
  Testability: testable via literature (does the contemporary Aquinas-and-cognitive-science literature treat Stumpian virtue as separable from hylomorphism, or as constitutively dependent?); testable empirically (track whether a synthesizer that demotes Stump on metaphysics produces coherent virtue claims, or whether the demotion propagates into virtue-claim breakdown)
  Risk if wrong: HIGH — if Stump's frameworks are not decomposable, then today's directive (demote on metaphysics, keep on virtue) introduces a hidden incoherence into every downstream synthesis that invokes both her metaphysics-via-Levin/Hoffman/Kastrup and her virtue-account. The Stump+Fredrickson specialist's same-day reading (ASSUMPTION-067) is direct evidence of this risk: a different agent on the same day was treating Stump's metaphysics as live.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-070
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the partial-demotion structure of ASSUMPTION-063 + the absence of any decomposability check + the same-day tension with ASSUMPTION-067
    Current status: UNTESTED

PRESUMPTION-071:
  Date surfaced: 2026-04-26
  Statement: [inferred] Levin + Hoffman + Kastrup form a coherent "mind-everywhere monist" convergence — i.e., these three traditions actually agree at the metaphysical level closely enough to be invokable as a single primary on metaphysical loci.
  Evidence it was operative: ASSUMPTION-063 names the trio as the new metaphysical primary in a way that presumes they form a unified position. The Cowork-side bridges file rephrases this as "the mind-everywhere monist convergence." No discussion of where Levin's polycomputing biology, Hoffman's conscious-realism interface theory, and Kastrup's analytic idealism actually disagree at the metaphysical level — and they do disagree (e.g., Hoffman is interface-theoretic while Kastrup is universalist-mind; Levin's substrate-independence is a different claim than either).
  Why it was unstated: The conversation moved at the level of "monist primaries" without auditing whether the three traditions were structurally compatible at the depth the metaphysical demotion requires.
  Type: epistemic
  Related decisions: ASSUMPTION-063, candidate DECISION-025, ASSUMPTION-005, ASSUMPTION-066 (Wolfram's potential methodological alliance with Kastrup — adds a fourth member to the implicit cluster)
  Testability: testable via literature (do Levin, Hoffman, and Kastrup converge on a single metaphysical position when their primary works are compared head-to-head, or do they share a "no-physicalism" stance only and disagree on what to put in its place?); testable empirically (when a synthesizer invokes "Levin+Hoffman+Kastrup" as a single primary, do the resulting claims hold across all three or break under any single one's framework?)
  Risk if wrong: HIGH — if the convergence is shallow (no-physicalism in common, but disagreement at the next level), then the new metaphysical primary is an alliance-of-convenience rather than a coherent position, and the Stump-demotion-replacement is a category error.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-071
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from ASSUMPTION-063's invocation of the three traditions as a single metaphysical primary without any depth-of-convergence check
    Current status: UNTESTED

PRESUMPTION-072:
  Date surfaced: 2026-04-26
  Statement: [inferred] A Catholic/Thomistic Summa-synthesis project ("Summa 2026 in a Year") is the appropriate downstream consumer for cross-tradition C2A2 outputs.
  Evidence it was operative: Today's longest architectural-design session is dedicated to building a Summa-locus-by-locus mapping that consumes the C2A2 wiki. The choice of the *Summa Theologica* as the organizing structure is taken as given — never explicitly defended against alternatives (e.g., an Eastern-Orthodox synthesis, a non-religious systematic-philosophy frame, a Reformed-systematic-theology frame, a no-organizing-structure approach). The C2A2 wiki itself contains traditions from Wolfram (computational), Carroll (physics), Fredrickson (positive psychology) that have no special prior relationship to the *Summa* — yet they are being mapped against its structure.
  Why it was unstated: Culturally embedded — the user has a personal commitment to Catholic synthesis that is the project's premise. No questioning of whether C2A2 is best-served by being consumed through a Catholic lens vs. some other lens, or by no synthesis frame at all.
  Type: normative
  Related decisions: ASSUMPTION-064 (Wright + Rohr addition is downstream of this), candidate DECISION-025, ASSUMPTION-005 (traditions as units — the Summa frame is now de facto a 12th organizing tradition for the wiki even if not formally added)
  Testability: testable via literature (do other systematic syntheses produce comparable cross-tradition coverage when applied to the same 11 source traditions, or is the Summa structurally privileged?); testable empirically (run the same wiki through a non-Summa synthesis frame and compare cross-tradition coverage and connection density)
  Risk if wrong: MEDIUM — the C2A2 wiki itself is unaffected if a derivative project chooses one synthesis lens over another, but if the wiki begins absorbing structural changes (Wright, Rohr, Stump demotion) driven by one synthesis lens, the wiki's own neutrality becomes compromised. This is the bridges-file-as-shadow-architecture pattern flagged in today's changelog.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-072
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of any defense of the Summa frame vs. alternatives in the design conversation
    Current status: UNTESTED

PRESUMPTION-073:
  Date surfaced: 2026-04-26
  Statement: [inferred] Adding two new traditions (Wright, Rohr) brings N from 11 to 13 without examining whether N=13 inherits the properties N=11 had — connection density, cross-tradition survival rates, statistical power for the health metric r, and the developmental maturity model's stage thresholds were all calibrated against an N=11 system.
  Evidence it was operative: ASSUMPTION-064 proposes the addition without referencing OPEN-005 (statistical-design-for-r at sample size N) or any cross-tradition-density target. The Cowork-side bridges file declares "13 traditions" and assigns Wright/Rohr to specific *Summa* loci without examining whether the existing 11-tradition cross-program-index needs structural revision.
  Why it was unstated: The "more traditions = more coverage" framing makes addition feel costless, especially when the new entries fill obvious gaps (scripture-scholarship, spirituality) that the existing 11 don't cover.
  Type: scaling
  Related decisions: ASSUMPTION-064, candidate DECISION-025, OPEN-005 (statistical design for r), ASSUMPTION-005, OPEN-036
  Testability: testable empirically (track whether N=13 cross-program-density behavior matches the N=11 trajectory or breaks at some threshold; measure whether r becomes harder to compute at N=13 due to sparser cross-tradition pairings); testable via literature (network-science papers on tradition-pluralism and connectivity-vs-N)
  Risk if wrong: MEDIUM — at N=13 the cross-program connection space is 78 pairs (vs. 55 at N=11). If existing 54 cross-program connections concentrated in the 55-pair N=11 space, the new 23 N=13-only pairs may stay sparse for a long time, distorting connection-density metrics.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-073
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from ASSUMPTION-064's silent assumption that addition is unproblematic at the architectural level
    Current status: UNTESTED

PRESUMPTION-074:
  Date surfaced: 2026-04-26
  Statement: [inferred] Cross-tradition convergences — e.g., Carroll↔Arkani-Hamed on emergent spacetime — can be reliably *recognized* by specialist agents without independent expert verification.
  Evidence it was operative: ASSUMPTION-065 reports the Carroll↔Arkani-Hamed convergence as "the network's most significant in-progress paradigm-shift signal of 2026" based on a single specialist-agent reading of one Heilborn Lecture description. No second opinion, no human-physicist validation, no check against the literature on whether Carroll's "Hilbert-space emergent spacetime" is structurally the same as Arkani-Hamed's "spacetime-is-doomed" program (they may not be — Carroll's everettian decoherence-based emergence is a different mechanism than Arkani-Hamed's amplituhedron-based reformulation).
  Why it was unstated: Specialist agents are designed to surface convergences, and their outputs are treated as findings to be routed downstream. The verification-before-trust step is implicit in the Pattern Detector + Master agent layers, but those layers haven't yet processed today's flagged convergence at EOD.
  Type: methodological
  Related decisions: ASSUMPTION-065, ASSUMPTION-066 (Wolfram method-export claim is structurally similar — single specialist agent re-interpreting three CROSS entries without verification), CROSS-031, CROSS-032, ASSUMPTION-067 (same risk applies to the Stump+Fredrickson pairing)
  Testability: testable empirically (track downstream-agent agreement with specialist-flagged convergences; measure rate at which flagged convergences are revised or rejected after Pattern Detector or Master agent review); testable via literature (do philosophy-of-physics sources confirm that "Carroll Hilbert-space emergence" and "Arkani-Hamed spacetime-is-doomed" name the same paradigm shift?)
  Risk if wrong: MEDIUM-HIGH — three of today's eight assumptions (065, 066, 067) all depend on this presumption. If single-specialist convergence-recognition is unreliable, today's three flagged signals may overstate the convergence and produce false paradigm-shift claims.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-074
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of verification-before-trust steps for any of today's three specialist-flagged convergences
    Current status: UNTESTED

PRESUMPTION-075:
  Date surfaced: 2026-04-26
  Statement: [inferred] The Chrome MCP workaround for sandbox-egress restrictions (used today after the Cowork allowlist toggle failed to propagate) is treated as a permanent solution rather than a contingent patch. The conversation closes with "Once egress is sorted, we switch to the fast `youtube-transcript-api` path for the bulk batches" — but the egress is NOT sorted, no escalation path is named, and the Chrome workaround is being used for production batches.
  Evidence it was operative: The session diagnoses the egress allowlist as system-level / hard-coded ("Cowork agent containers ship with a fixed allowlist that survives session restarts"), then routes to Chrome MCP without filing an escalation, decision, or open question for the underlying egress problem. The phrase "let me stop fighting it and route through your browser via Chrome MCP" treats the workaround as the normal path forward.
  Why it was unstated: Workarounds-becoming-permanent is a well-known pattern in software systems but rarely flagged in real-time. The conversation's pragmatic tone ("it's slower per-episode but proves the pipeline") accepts the patch without examining whether accepting it institutionalizes the dependency.
  Type: methodological
  Related decisions: candidate DECISION-025, OPEN-039 (NEW: should the egress allowlist be escalated to Claude product team?), ASSUMPTION-055 (Phase 6 git failure mode also points at sandbox-mount-topology issues — a related class of contingent infrastructure constraints being treated as permanent)
  Testability: testable empirically (track whether the Chrome MCP workaround persists across N future sessions before any egress escalation occurs; measure cost in time and reliability of the workaround vs. the proposed direct-API path)
  Risk if wrong: MEDIUM — Chrome MCP through a real browser is fragile (ad-blocker interactions are visible in today's transcript: "Ad-blocker extension is intercepting the timedtext fetch"; "Ad-blocker is stripping the timedtext response"). Workaround-permanence in a fragile path increases pipeline failure risk.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-075
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of an escalation path or decision-flag for the egress problem in the design conversation
    Current status: UNTESTED

PRESUMPTION-076:
  Date surfaced: 2026-04-26
  Statement: [inferred] Falling back on canonical works for Wright and Rohr (until `Wiki/traditions/wright/wiki.md` and `Wiki/traditions/rohr/wiki.md` exist) is methodologically equivalent to having native wiki tradition files.
  Evidence it was operative: The Cowork-side response says "Until their `wiki/traditions/wright/wiki.md` and `wiki/traditions/rohr/wiki.md` files exist, the synthesizer is told to fall back on their canonical works." This presumes the synthesizer can extract wiki-equivalent structure (PRS triplets, methodological commitments, primary-source-of-the-week dates) from canonical works in real-time without the curation that the existing 11 traditions received. The existing 11 were curated through 2-3 weeks of dedicated wiki-building.
  Why it was unstated: The fallback is treated as a stop-gap with no acknowledgment that the stop-gap may produce systematically different downstream behavior than native wiki entries.
  Type: methodological
  Related decisions: ASSUMPTION-064, candidate DECISION-025, ASSUMPTION-005 (traditions as units — what counts as a "tradition" at the operational level?), OPEN-036
  Testability: testable empirically (compare synthesis output for native-wiki traditions vs. canonical-works-fallback traditions on matched loci; measure citation-quality, PRS-id usability, and cross-program-connection generation rate)
  Risk if wrong: MEDIUM — if fallback ≠ native, then Wright and Rohr will produce systematically different (likely thinner, less PRS-disciplined) synthesis content, distorting the multi-tradition synthesis from day one.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-076
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the conversation's silent equation of fallback with native files
    Current status: UNTESTED

PRESUMPTION-077:
  Date surfaced: 2026-04-26
  Statement: [inferred] A four-day master-narrative gap (no entries 04-23 through 04-26 at the time of this morning's check) is operationally absorbable rather than a degradation signal warranting alert.
  Evidence it was operative: The morning walk handoff surfaced the gap in narrative ("Surfaced this in the briefing footer rather than fabricating intervening state.") and proceeded with normal operation. No alert fired, no escalation occurred, no decision-flag was raised. The gap was treated as a fact-to-be-noted rather than a pipeline-degradation-to-be-investigated. Today's wiki daily run later closed one day of the gap (added a 2026-04-27 entry) without addressing the prior 4-day silence.
  Why it was unstated: PREMISE-006 (flag-don't-reconcile) provides the operating principle for handling staleness, but the principle is silent on at-what-N-day-threshold staleness becomes a degradation signal vs. an acceptable gap. PRESUMPTION-068 (mortar-narrative gap surfacing > fabrication) at PREMISE-006 itself does not specify when the gap itself merits investigation.
  Why it was unstated (additional): Adjacent to OPEN-038 (why has the master-wiki narrative had a 4-day gap?). The presumption that any-N-day gap is fine is itself the answer that the unsurfaced version of OPEN-038 was implicitly giving.
  Type: epistemic
  Related decisions: ASSUMPTION-068, ASSUMPTION-047, PREMISE-006, OPEN-038 (NEW), OPEN-034 (silence-as-signal cluster — adds member)
  Testability: testable empirically (track recovery time and content-loss after master-narrative gaps of varying lengths; identify the N-day threshold at which gap is no longer absorbable); testable via literature (incident-response and operational-monitoring patterns for "staleness as alertable event")
  Risk if wrong: MEDIUM-HIGH — extends the SELF-AWARENESS-META cluster (now 10 members with PRESUMPTION-077 added). If 4-day gaps are signal-of-degradation rather than absorbable, today's pattern is the start of a slow-burn pipeline failure that the briefing layer is hiding by design via PREMISE-006.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-077
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the morning walk handoff's no-escalation handling of a 4-day gap, combined with the absence of a staleness-floor in PREMISE-006
    Current status: UNTESTED

PRESUMPTION-078:
  Date surfaced: 2026-04-26
  Statement: [inferred] The Stump×Fredrickson "metaphysics+empirics" pairing (ASSUMPTION-067) is a correctly-constructed bridge — i.e., hylomorphic-corporate-substance metaphysics (Stump) and positivity-resonance weak-tie RCTs (Fredrickson) are the right kind of metaphysics and empirics to be paired together. This presumes that hylomorphism's claims about corporate substance map onto the kind of micro-intervention effects Fredrickson measures.
  Evidence it was operative: The specialist's autonomous-choices note moves directly from "Stump supplies a hylomorphic account of corporate substance" to "Fredrickson supplies a working RCT for raising weak-tie positivity resonance" to "Together they bridge the metaphysical and operational layers." No interrogation of whether mirror-neuron coupling (Stump's empirical anchor for collective-substance claims) and weak-tie positivity resonance (Fredrickson's mechanism) are the same level of phenomenon, or whether RCT effects on individual positivity scale to claims about peoples-as-real-composites.
  Why it was unstated: Specialist agents are pattern-matching cross-tradition signals; the depth-of-coherence check is not their job. The conversation has the shape of a successful bridge without the architecture of one.
  Type: structural
  Related decisions: ASSUMPTION-067, ASSUMPTION-063 (DIRECT TENSION — same day demoted Stump on metaphysics), ASSUMPTION-005, OPEN-037
  Testability: testable via literature (does the philosophy-of-mind / philosophy-of-religion literature treat hylomorphic-corporate-substance claims as operationalizable through positivity-resonance interventions, or are these category-mismatched levels?); testable empirically (track downstream syntheses that invoke the pairing — do they produce coherent claims at both metaphysical and operational levels?)
  Risk if wrong: MEDIUM-HIGH — if the pairing is category-mismatched, then today's most-celebrated specialist signal (a "metaphysics+empirics bridge") is a false positive, and the Stump-as-live-metaphysics reading that survives in the specialist layer is undermined.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-078
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the specialist's confident pairing language without any commensurability check
    Current status: UNTESTED

PRESUMPTION-079:
  Date surfaced: 2026-04-26
  Statement: [inferred] Carroll↔Arkani-Hamed "convergence on emergent spacetime" represents the SAME paradigm-shift signal across both physics traditions, not two parallel-but-distinct convergences that happen to use overlapping vocabulary.
  Evidence it was operative: ASSUMPTION-065 names a single convergence; both proposals (Carroll PROP and Arkani-Hamed PROP) flag the same item as "the network's most significant in-progress paradigm-shift signal of 2026." But Carroll's emergent-spacetime claim is from quantum-decoherence and Hilbert-space-structure (Mad Dog Everettianism); Arkani-Hamed's is from positive-geometry (amplituhedron / cosmohedron) and combinatorial reformulations of S-matrix. These are different mechanisms claiming a structurally similar conclusion ("spacetime is not fundamental"); whether they are the SAME paradigm shift or two parallel ones is a substantive open question.
  Why it was unstated: The shared-vocabulary makes the convergence feel obvious. Two physicists using "emergent spacetime" as a phrase produces a strong same-claim impression even when their underlying mechanisms differ. The specialist-agent layer flags vocabulary-match without auditing mechanism-match.
  Type: structural
  Related decisions: ASSUMPTION-065, PRESUMPTION-074 (cross-tradition convergence reliable-recognizability), CROSS-031 (asymmetry across McGilchrist/Friston/Wolfram — same risk mode applies), candidate CROSS-Carroll×ArkaniHamed (would be created by Pattern Detector)
  Testability: testable via literature (do philosophy-of-physics or quantum-gravity sources treat Carroll-style and Arkani-Hamed-style emergent-spacetime as the same paradigm shift or as parallel-but-distinct ones?); testable empirically (track whether the convergence holds up under more proposals from each tradition over the next 6 months, or splits into two sub-convergences)
  Risk if wrong: MEDIUM — if the convergence is parallel-but-distinct rather than same, today's "network's most significant signal of 2026" framing overstates the integration. Two sub-convergences are still valuable but the SUPER-BRIDGE candidate logic that ASSUMPTION-065 implies would not apply.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-079
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of any mechanism-match audit in either proposal's framing of the convergence
    Current status: UNTESTED

PRESUMPTION-080:
  Date surfaced: 2026-04-26
  Statement: [inferred] The 13-tradition frame (after adding Wright and Rohr) can absorb both science-tradition-style members (Levin, Hoffman, Wolfram, Friston, Hawkins, Carroll, Arkani-Hamed, Fredrickson) and theology-tradition-style members (Stump, McGilchrist, Kastrup, Wright, Rohr) without distortion. The C2A2 wiki has not yet examined whether "tradition" means the same thing across these two member-types, or whether different operational primitives apply.
  Evidence it was operative: ASSUMPTION-064 adds Wright and Rohr without addressing whether the existing PRS-triplet structure, primary-source-of-the-week cadence, or cross-program-index conventions translate cleanly to scripture-scholarship and spirituality-tradition member-types. The Cowork-side bridges file fills out role-assignments by *Summa* locus without evaluating whether scripture-scholarship has "PRS triplets" in the C2A2 sense.
  Why it was unstated: The "tradition" abstraction is treated as universal across discipline-types in C2A2's design. The presumption that this abstraction transfers cleanly to scripture-scholarship and spirituality-tradition was never explicitly tested.
  Type: structural
  Related decisions: ASSUMPTION-064, PRESUMPTION-073 (scaling-N), PRESUMPTION-076 (canonical-works fallback), ASSUMPTION-005, candidate DECISION-025
  Testability: testable empirically (attempt to construct PRS triplets for Wright's *Resurrection of the Son of God* and Rohr's *The Universal Christ*; compare structural fit to existing Levin or Friston PRS triplets)
  Risk if wrong: MEDIUM — if the abstraction doesn't transfer, then Wright/Rohr entries will produce malformed PRS triplets and weak cross-program connections, distorting the wiki's integration metrics.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-080
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of any cross-discipline operational-primitive check in the Wright/Rohr addition
    Current status: UNTESTED

PRESUMPTION-081:
  Date surfaced: 2026-04-27
  Statement: [inferred] A single 15a/15b/15c cycle can substitute for 5 missed daily cycles without quality degradation. The 58-item batch (19 new + 39 re-triggered) was processed end-to-end in one cycle; nothing in the run examined whether single-cycle batch processing produces the same disposition quality (INCORPORATE/MONITOR/REVISE rate distribution; depth of supporting/challenging evidence per item) as 5 separate daily-cycle 12-item batches would have.
  Evidence it was operative: The lit-search pipeline 2026-04-27 (local_64b9c31c) drained the 5-day backlog in a single run and reported "Pipeline lag drops from 5 days to 0" without examining batch-vs-cadence quality tradeoffs. Items dispositioned via the run carry per-item provenance but not per-batch quality metrics.
  Why it was unstated: Throughput was the framing; quality at-scale was not. The pipeline's 5-day stall was the visible problem, and draining it was treated as the obvious solution.
  Type: epistemic / methodological
  Related decisions: ASSUMPTION-072 (5-day backlog drainable in single cycle), DECISION-006 (15a/15b independence — independence preservation under batch-mode is implicit), DECISION-009 (developmental maturity model)
  Testability: testable empirically (compare INCORPORATE/MONITOR/REVISE rate distributions across cadence regimes — single-batch-58 vs five-batches-of-12; track whether items dispositioned at the start of the batch differ in disposition quality from items dispositioned at the end); testable via literature (literature on cognitive batch effects, satisficing in large-N evaluation tasks)
  Risk if wrong: MEDIUM — if quality degrades at scale, the 5-day pipeline drain creates a sub-class of "drained-but-shallow" dispositions that look like progress but provide weaker downstream guidance.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-081
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the lit-search pipeline 2026-04-27's framing of throughput-as-quality without batch-quality examination
    Current status: UNTESTED

PRESUMPTION-082:
  Date surfaced: 2026-04-27
  Statement: [inferred] For re-triggered (refresh) lit-search items, "no new external evidence found" is a reliable claim, not "evidence not searched-for at sufficient depth during the refresh window." The autonomous-choices note declared "no new literature surfaced" without specifying the actual search depth applied to the 39 refresh items vs. the 19 cycle-1 items. ASSUMPTION-074 makes the carry-forward stance explicit; this presumption surfaces the unexamined depth-asymmetry beneath it.
  Evidence it was operative: The lit-search pipeline run note: "For 39 re-triggered items, this automated cycle had no new external evidence; refresh entries record 'no new literature surfaced' and carry forward prior MONITOR disposition rather than fabricating new findings." No mention of how many search queries were applied per refresh item, nor of how the search-depth compares to the cycle-1 protocol. The refresh appears to be lighter-touch by default but this is not articulated.
  Why it was unstated: The refresh is treated as a maintenance operation rather than as a fresh search; the implicit framing is "if nothing big has changed in the literature, the prior disposition holds." But "nothing big has changed" is a non-trivial claim that depends on search-depth.
  Type: methodological
  Related decisions: ASSUMPTION-074 (refresh carry-forward stance), DECISION-006, PREMISE-006 (flag-don't-fabricate — refresh extension)
  Testability: testable empirically (audit the search-query log for refresh items vs. cycle-1 items; track whether refresh items occasionally surface new evidence that is missed by the lighter-touch search)
  Risk if wrong: MEDIUM — if refresh search-depth is materially shallower than cycle-1, then "no new evidence" is a search-not-done claim and dispositions accumulate stale on the wiki without warning markers.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-082
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of search-depth specification in the refresh-cycle autonomous-choices note
    Current status: UNTESTED

PRESUMPTION-083:
  Date surfaced: 2026-04-27
  Statement: [inferred] Browser-authentication can remain user-fixable indefinitely. Today is the first failure of the Chrome-MCP claude.ai sign-in chain in both the morning scrape and evening sync; the response is to flag it for Tom rather than escalate, retry-with-fallback, or substitute an authenticated channel (long-lived auth token, API-based content access, pre-authenticated browser profile). The framing presumes the next-day fix-by-Tom is sufficient even if recurrence accumulates.
  Evidence it was operative: ASSUMPTION-071 articulated the prohibition; both today's failure events flagged "sign claude.ai into the Chrome MCP browser" as the only remediation, and both treated this as user-fixable rather than as an escalation candidate. PRESUMPTION-068 (2026-04-21) marked the prior Chrome MCP double-success as "resolved rather than transient" — today's double-failure is the symmetric case but produces no upgrade in the framing.
  Why it was unstated: The ambient assumption that user-on-behalf-of authentication is just-not-allowed-anywhere makes the fallback search invisible; only the user-fix path is considered.
  Type: architectural / normative
  Related decisions: ASSUMPTION-071 (browser-auth as agent-prohibited), OPEN-039 (sandbox infrastructure escalation), PRESUMPTION-068 (Chrome resolve-or-transient ambiguity)
  Testability: testable empirically (track recurrence rate of claude.ai-not-signed-in failures; if recurrence > N per week, the user-fixable framing is empirically falsified by daily wear); testable via literature (literature on long-lived agent auth tokens, OAuth on-behalf-of patterns, identity-delegation models)
  Risk if wrong: MEDIUM-HIGH — if the auth gap recurs daily, the daily Chat↔Cowork sync is structurally broken; the .md fallback record becomes the authoritative state and the visible-to-Tom Chat conversation diverges from the wiki state without warning.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-083
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the user-fixable framing applied to today's two parallel auth failures without examining substitute auth channels
    Current status: UNTESTED

PRESUMPTION-084:
  Date surfaced: 2026-04-27
  Statement: [inferred] Pre-flight cowork-directory grant failures are presumed to remain a pattern rather than a candidate for circuit-breaker. Today's two morning-stalled specialists (local_ce75f007 morning project status; local_894ebad0 morning system health) and today's 1pm caching-architecture session (local_bd0ecd6c) are the third, fourth, and fifth observed instances of pre-flight directory-grant failure (after yesterday's four). The pattern continues to schedule the tasks at the same cadence without auto-fail behavior or escalation; no candidate DECISION-026 was drafted today to address this distinct failure mode.
  Evidence it was operative: Three same-day pre-flight failures with consistent shape: scheduled task fires → calls `request_cowork_directory` → no user present to grant → task ends with no work product. The cowork→chat summary explicitly noted today's 1pm failure as "tomorrow's caching/Levin v1.0 rollout decision will go in cold for the second day running" without proposing an auto-fail or pre-flight-grant-required gate.
  Why it was unstated: The scheduled-task model treats each task as independent; the cross-task pattern requires aggregation that no agent currently performs. PRESUMPTION-077 (yesterday's 4-day-gap absorbability) and PRESUMPTION-052 (intent-capture recurrence) are precedents for this kind of pattern-blindness.
  Type: methodological
  Related decisions: candidate DECISION-024 (specialist turn-cap — does NOT address pre-flight stalls; this is a distinct failure mode), candidate-not-yet-drafted DECISION-026 (specialist pre-flight directory-grant timeout / auto-fail behavior — flagged 2026-04-26 changelog as worth a candidate; not drafted today)
  Testability: testable empirically (cumulative count of pre-flight stalls; track whether a circuit breaker firing on N consecutive stalls would prevent measurable cost / produce false positives)
  Risk if wrong: MEDIUM-HIGH — if the pattern accumulates to >10 stalled specialists per week, the specialist-rotation schedule's coverage (PRESUMPTION-031) is materially different from its declared coverage.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-084
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the recurrence of the pre-flight-stall failure mode without DECISION-026 candidate drafting today
    Current status: UNTESTED

PRESUMPTION-085:
  Date surfaced: 2026-04-27
  Statement: [inferred] PREMISE-012 (4-day master-narrative gap surfaced not fabricated, just promoted from ASSUMPTION-068 today) is presumed to apply identically to N-day gaps where N is much larger. The promotion-via-INCORPORATE ratifies the principle without examining whether 5-day, 10-day, or 30-day gaps should trigger a different response. The "surface-and-proceed" rule has no upper bound built in.
  Evidence it was operative: The lit-search pipeline 2026-04-27 elevated ASSUMPTION-068 to PREMISE-012 based on its 4-day-gap performance; the promotion text does not introduce any N-day staleness threshold beyond which surface-and-proceed becomes "investigate-as-incident". OPEN-038 explicitly raises this question (priority High) and remains open today; the promotion happened anyway.
  Why it was unstated: PREMISE-006 (parent of PREMISE-012) was originally validated against 1-2 day gaps; the principle's scope was implicitly inherited at the larger 4-day gap without re-examining whether scope-extension is warranted at all gap sizes.
  Type: methodological
  Related decisions: PREMISE-012 (newly INCORPORATEd today from ASSUMPTION-068), PREMISE-006, OPEN-038 (4-day gap root cause + N-day threshold question)
  Testability: testable empirically (track the largest master-narrative gap that PREMISE-012 holds against without producing a downstream incident; identify the breakpoint); testable via literature (literature on degradation thresholds in monitoring systems, alert fatigue vs. silent staleness)
  Risk if wrong: MEDIUM-HIGH — if there is a staleness-floor at which surface-and-proceed breaks down, today's INCORPORATE has just locked in a rule that will silently fail at that floor.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-085
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from today's INCORPORATE event ratifying ASSUMPTION-068 → PREMISE-012 without examining the upper bound of the surface-and-proceed rule
    Current status: UNTESTED

PRESUMPTION-086:
  Date surfaced: 2026-04-27
  Statement: [inferred] PREMISE-013 (proposal-id collisions flagged-and-rolled-forward, just promoted from ASSUMPTION-069 today) is presumed to scale without producing downstream incidents. Today's morning walk handoff flagged 3 duplicate IDs across 33 pending files; this brings cumulative known collisions to 5+ unresolved instances over the last week. The promotion ratifies the pattern without examining what N-collisions per day would constitute structural breakdown of the ID-as-handle convention.
  Evidence it was operative: PREMISE-013 was created from ASSUMPTION-069 today; the morning walk handoff listed the new collision count and called it "a small orchestrator fix worth queueing" — same flag-and-roll-forward stance, no escalation. The wiki daily run did not address the collisions in its Phase 0–5 work; they sit on the orchestrator-fix queue.
  Why it was unstated: ID-collisions are individually small; the cumulative-pattern check requires aggregation across days that no agent currently performs.
  Type: methodological
  Related decisions: PREMISE-013 (newly INCORPORATEd today from ASSUMPTION-069), DECISION-001 (sequential-ID fix — original deprecation of agent-assigned IDs), OPEN-001 (should agent-assigned IDs be deprecated entirely)
  Testability: testable empirically (count cumulative known unresolved ID collisions; track whether any downstream query / rollup is corrupted by N-collisions); testable via literature (literature on ID-as-handle conventions in distributed systems; eventual-consistency vs. strict-uniqueness tradeoffs)
  Risk if wrong: MEDIUM — if a downstream query rolls up two distinct items under one ID, network metrics (cross-program connections, PRS counts) become silently incorrect.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-086
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from today's INCORPORATE event ratifying ASSUMPTION-069 → PREMISE-013 without examining cumulative-collision scaling
    Current status: UNTESTED

PRESUMPTION-087:
  Date surfaced: 2026-04-27
  Statement: [inferred] The Levin specialist's "significant work not yet captured" override of the 30-day cadence is presumed to be specialist-self-correcting. The autonomous-choices note flagged the override transparently but no audit mechanism exists to detect when the override is over-applied across N specialist runs (e.g., when "foundational and missing" is invoked for items that are actually present-but-un-indexed). ASSUMPTION-075 articulates the override; this presumption surfaces the absence of an audit layer beneath it.
  Evidence it was operative: The Levin+Friston autonomous-choices note: "I used the 'significant work not yet captured' criterion rather than the strict 30-day window, since the field-theoretic formalization of bioelectric prepatterning is foundational to the wiki's coverage and was missing." No cross-check against the wiki to verify that the work was in fact missing rather than indexed under a different filename or PRS ID. No audit-log entry that future runs can compare against.
  Why it was unstated: Specialists are trusted to self-evaluate; the BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster (ASSUMPTION-046, 047, 048, 057, 058, 059, 060) has been articulating self-trust principles for weeks. PRESUMPTION-067 (specialist-self-eval-adequate) is the close-adjacent predecessor.
  Type: methodological
  Related decisions: ASSUMPTION-075 (override criterion), PRESUMPTION-067 (specialist-self-eval-adequate; this is its cadence-override instance), specialist-rotation schedule (PRESUMPTION-031), PRESUMPTION-074 (specialist-recognition reliability — REVISE-flagged today)
  Testability: testable empirically (audit each invoked override against actual wiki state; track false-positive override rate over N specialist runs); testable via literature (auditing patterns in expert-judgment systems)
  Risk if wrong: MEDIUM-HIGH — if the override is over-applied, specialists pull in older work that distorts the cross-program-connection-density metric and inflates the perceived novelty rate. Compounds PRESUMPTION-074 specialist-recognition-reliability concern.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-087
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of an audit mechanism beneath today's stated cadence-override criterion
    Current status: UNTESTED

PRESUMPTION-088:
  Date surfaced: 2026-04-27
  Statement: [inferred] Tom's authorial reframing of PRS triplets ("PRS-NN in the Stump-tradition wiki" not "Stump's PRS-NN") is presumed compatible with C2A2's published representation of the wiki to external readers. The bridges-file correction was made in the derivative-project, but the per-tradition `prs_triplets.md` files in the C2A2 wiki itself have not been re-stamped to match the new attribution rule. The presumption is that downstream consumers (specialists, Pattern Detector, Master Agent, future external readers) will read the per-tradition files in the new authorial frame; this has not been verified.
  Evidence it was operative: ASSUMPTION-076 articulates the new citation rule; the design-project session's edits landed in `vault/synthesis/Day-001 - Introduction - Contemporary.md`, the `Karpathy wiki bridges.md` file, and persistent memory — all in the derivative project — but did not propagate to the C2A2 wiki under `Wiki/traditions/{name}/prs_triplets.md`. The C2A2 wiki's own files still carry their original framing, which a naive reader would interpret as tradition-self-voice.
  Why it was unstated: The correction was made where the immediate problem appeared (the synthesis citation form). The general rule's downstream consequences for the C2A2 wiki itself were not surveyed.
  Type: epistemic / architectural
  Related decisions: ASSUMPTION-076 (PRS authorial reframing), candidate DECISION-025 (Stump metaphysical demotion — depends on which voice the wiki carries), OPEN-037 (Stump tension)
  Testability: testable empirically (audit a sample of per-tradition `prs_triplets.md` files for whether they read as tradition-self-voice or Tom-frame voice; track how downstream specialists treat them)
  Risk if wrong: MEDIUM-HIGH — if the C2A2 wiki's per-tradition files read as tradition-self-voice but are actually Tom's re-description (per ASSUMPTION-076), then external readers (or specialist agents reading the wiki) inherit Tom's framing as if it were the tradition's own — recursive risk; see PRESUMPTION-089.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-088
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the gap between the derivative-project citation correction and the C2A2 wiki's per-tradition file state
    Current status: UNTESTED

PRESUMPTION-089:
  Date surfaced: 2026-04-27
  Statement: [inferred] The "PRS triplets are Tom's re-description, not the tradition's voice" reframing (ASSUMPTION-076) recasts ASSUMPTION-067 (Stump+Fredrickson specialist's reading of Stump as supplying live metaphysics): if Stump's PRS triplets are Tom's re-description, then the specialist agent reading them as Stump's authentic metaphysics is reading Tom's framing back to itself. This recursive reading risk was not surfaced during today's design-project session and has not been examined for the other 10 traditions whose specialists also read PRS-formatted content.
  Evidence it was operative: Today's design-project session corrected attribution in the synthesis but did not extend the correction to the same-week specialist autonomous-choices notes (ASSUMPTION-066 Wolfram method-export, ASSUMPTION-067 Stump+Fredrickson, ASSUMPTION-065 Carroll+Arkani-Hamed convergence). All three specialists used the wiki's per-tradition content as input; under ASSUMPTION-076 that content is Tom's frame. The specialists' reading of the content as tradition-voice is a recursive read of Tom's framing.
  Why it was unstated: The recursive-reading risk requires combining ASSUMPTION-076 (today's authorial reframing) with the recent specialist outputs (yesterday's ASSUMPTION-065/066/067) — an aggregation no agent currently performs. The selection-effect cluster (PRESUMPTION-024) is the closest precedent; this presumption joins that cluster.
  Type: epistemic
  Related decisions: ASSUMPTION-076 (authorial reframing), ASSUMPTION-067 (Stump+Fredrickson specialist), ASSUMPTION-066 (Wolfram method-export), ASSUMPTION-065 (Carroll+Arkani-Hamed convergence), PRESUMPTION-024 (selection effect on FINDING-011a — this is its specialist-reading instance), candidate DECISION-025
  Testability: testable empirically (when a specialist invokes a tradition's PRS triplet, audit whether the specialist treats the PRS as tradition-self-voice or as a re-description; track whether the specialist's outputs differ when given Tom-framed-as-tradition vs. tradition-self-voice content)
  Risk if wrong: MEDIUM-HIGH — joins the CRITICAL/HIGH-leaning self-awareness cluster (PRESUMPTION-024 selection effect, PRESUMPTION-002 Thousand Brains transfer) as the recursive-specialist-reading instance. If specialists are reading Tom's frame as tradition-voice and reporting cross-tradition convergences, those convergences may be Tom-frame internal coherences mistaken for cross-tradition signal.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-089
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by combining today's ASSUMPTION-076 authorial reframing with yesterday's specialist outputs (ASSUMPTION-065, 066, 067) and the prior selection-effect cluster (PRESUMPTION-024)
    Current status: UNTESTED

PRESUMPTION-090:
  Date surfaced: 2026-04-27
  Statement: [inferred] The agentic cost tracker's tier estimates ($0.05 light, $0.25 heavy, $0.50 install) accurately approximate the actual API spend per scheduled-task run. No validation against actual API usage or billing records was performed during today's run; the tier model is treated as ground truth for the April-month total of $39.65.
  Evidence it was operative: Cost tracker session (local_836760c7) computed totals from the tier model directly, with no cross-check against billing or token-count logs. The report communicates the total as a stable claim ("Total estimated agentic spend, April 2026: $39.65").
  Why it was unstated: Cost tracking is treated as a maintenance operation; tier accuracy is rarely on the critical path.
  Type: empirical
  Related decisions: weekly-agent-ecosystem-report (parallel maintenance task), broader cost-modeling for the C2A2 architecture (no formal DECISION)
  Testability: testable empirically (compare tier-estimated total to actual billing for one month; track tier deviation per task category)
  Risk if wrong: LOW-MEDIUM — if tiers are off by 50%, monthly cost estimate moves to ~$60 or ~$25; not architecturally consequential at this level.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-090
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of any tier-validation step in today's cost tracker run
    Current status: UNTESTED

PRESUMPTION-091:
  Date surfaced: 2026-04-27
  Statement: [inferred] Today's "deep" pending-proposal queue (33 visible) is operationally absorbable rather than constituting a degradation signal. The wiki daily run noted 33 as "the largest backlog since 2026-04-16 batch ingestion" but did not escalate or define a queue-depth ceiling. Phase 6 git block is the upstream cause, but the queue-growth-without-defined-breakpoint pattern continues for an 11th calendar day with no formal queue-depth alert threshold articulated.
  Evidence it was operative: Wiki daily run output stated "Pending queue: 33 proposals (largest since 2026-04-16 batch)" with no escalation language; cowork→chat summary called the queue "deep" and listed it as a tomorrow-morning agenda item rather than as an incident. The 21→33 growth in one day was not flagged as a rate concern. The Phase 6 block is 11 days old; queue depth has roughly doubled in that window.
  Why it was unstated: PRESUMPTION-077 (4-day-gap absorbability) is the close-adjacent precedent: the same surface-and-proceed framing applied to staleness gaps applies here to queue-depth growth. The principle's scope was implicitly inherited.
  Type: epistemic
  Related decisions: DECISION-018 (rescue commit plan — superseded by compound block), OPEN-035 (Phase 6 sandbox-unreachable), PRESUMPTION-077 (4-day-gap absorbability — close-adjacent), PRESUMPTION-085 (today's PREMISE-012 N-day threshold)
  Testability: testable empirically (define a queue-depth-vs-degradation curve from historical data; identify the breakpoint at which proposal-quality declines or items are forgotten)
  Risk if wrong: MEDIUM — if the queue continues growing unbounded, eventually proposal-coherence and review-quality break down, but the failure is silent until well past the breakpoint.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-091
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from today's wiki-daily-run framing of the 33-deep queue without escalation or ceiling articulation
    Current status: UNTESTED

PRESUMPTION-092:
  Date surfaced: 2026-04-27
  Statement: [inferred] Today's newly-scheduled `summa-2026-nightly-verification` agent (a derivative-project-internal QA loop) is presumed not to require integration with the C2A2 wiki's self-awareness pipeline. The verifier walks `vault/synthesis/` and cross-checks against `RC Karpathy Wiki Project/` paths; its output (`vault/_index/Verification log.md`) is not surfaced to C2A2's 14a/14b cycle. This extends yesterday's shadow-architecture pattern (CHANGE-2026-04-26-001 / OPEN-036): another derivative-project artifact that bears on C2A2 (verifying citations into the C2A2 wiki) but lives outside the C2A2 self-awareness layer.
  Evidence it was operative: Design-project session 2026-04-27 scheduled the nightly verifier with output destination `vault/_index/Verification log.md` and recommendation "hit 'Run now' once on the task to pre-approve the directory grants." No mention of routing the verification log into C2A2's changelog or assumptions/presumptions registries. The first run today produced 1 drift item (FLAG-003 / FLAG-005 path-citation) — none of it surfaced in the C2A2 wiki.
  Why it was unstated: The verifier is treated as a derivative-project tool; bidirectional-feedback into the C2A2 wiki is not the design-project's concern.
  Type: architectural
  Related decisions: candidate DECISION-025 (Wright/Rohr addition + Stump demotion — same shadow-architecture cluster), OPEN-036 (bridges-file-as-shadow-architecture), ASSUMPTION-076 (PRS authorial reframing — propagation to C2A2 not yet done)
  Testability: testable empirically (track whether verifier-detected drift items in the C2A2 wiki get surfaced into the C2A2 changelog; track whether C2A2 wiki edits silently break verifier checks)
  Risk if wrong: LOW-MEDIUM — if the verifier silently catches C2A2-wiki problems that should be C2A2-internal events, the C2A2 self-awareness layer has a blind spot at the derivative-project boundary.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-092
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of any C2A2-wiki integration in today's nightly-verifier scheduling and first-run output
    Current status: UNTESTED

PRESUMPTION-093:
  Date surfaced: 2026-05-05
  Statement: [inferred] The same-day daemon catch-up of all six weekday-assigned specialist agents is structurally equivalent to the intended Mon–Sat distribution. The presumption is that running Levin+Friston, Hawkins+Hoffman, McGilchrist+Kastrup, Stump+Fredrickson, Carroll+Arkani-Hamed, and Wolfram in a single 60-minute UTC window produces the same coverage signal as spreading them across six calendar days.
  Evidence it was operative: Six specialist sessions completed today between 15:35 and 16:35 UTC. Each output stamped its assigned weekday ("MONDAY AGENTS", "TUESDAY AGENTS", … "SATURDAY AGENT") on a Tuesday run-day. No qualifier was added in any of the specialist outputs flagging the catch-up provenance. Cross-tradition signal claims (e.g., Wolfram's PROP-016 advancing CROSS-006/007/015/049; Stump+Fredrickson's "strongest current empirical bridge" claim) were generated within hours of one another and ingested into pending/ as if they had arrived independently across a week.
  Why it was unstated: Catch-up runs are normalized by the daemon's overdue-queue drain pattern; the briefing/specialist layer treats run-day as accidental and weekday-of-assignment as the substantive label.
  Type: methodological / scaling
  Related decisions: ASSUMPTION-079 (parent stated assumption), ASSUMPTION-011 (specialist-first scheduling), DECISION-015 (scheduled-task ecology)
  Testability: testable empirically (compare cross-tradition signal-correlation across same-day catch-up batches vs. spread-across-week batches; compare PRS-extraction yield)
  Risk if wrong: MEDIUM — if same-day catch-up injects temporal-correlation artefacts (same external news cycle, same Tom-not-present state, same daemon latency), the cross-tradition signals reported today may be inflated relative to what a spread-across-week run would surface.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-093
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of any catch-up-vs-spread qualifier in today's six specialist outputs.
    Current status: UNTESTED

PRESUMPTION-094:
  Date surfaced: 2026-05-05
  Statement: [inferred] The daemon-bug workaround (`update_scheduled_task --fireAt`) is presumed not to interact problematically with the C2A2 self-awareness pipeline. This run itself executes inside the same scheduled-task system; if the workaround changes registration semantics, the self-awareness pipeline may be silently affected in ways not yet examined.
  Evidence it was operative: Tom proposed the workaround in the Summa session for "all 23 broken tasks" (ASSUMPTION-081). The c2a2-self-awareness-daily task fired today (this very run) — implying it is in the link-count > 1 partition. No examination today of whether applying the `fireAt` workaround retrospectively to the self-awareness task or to the wiki daily run would change its registration behavior.
  Why it was unstated: The workaround was scoped to the Summa-2026 task family in the moment; cross-task effects on C2A2 were not in the conversation's frame.
  Type: methodological / infrastructure
  Related decisions: ASSUMPTION-080 (parent diagnosis), ASSUMPTION-081 (workaround claim), DECISION-015 (scheduled-task ecology)
  Testability: testable empirically (apply `fireAt` to a C2A2 task and observe `lastRunAt` and registration status; check for cross-task interaction)
  Risk if wrong: MEDIUM — if applying the workaround to C2A2 tasks changes their registration partition or fire-cadence, the self-awareness layer's own scheduling could be perturbed.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-094
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of any C2A2-side examination of the workaround's blast radius in the Summa session.
    Current status: UNTESTED

PRESUMPTION-095:
  Date surfaced: 2026-05-05
  Statement: [inferred] The C282 wiki agent daily run's Phase 2 result ("0 new high-quality proposals across the 5 thinkers without same-day specialist coverage") is presumed to indicate genuine search exhaustion, not search-strategy failure. The orchestrator did not introspect on its own 0-result before declaring exhaustion; no fallback search-strategy variation (alternate query forms, broader date window, alternative source surfaces) was tried.
  Evidence it was operative: Wiki agent transcript: "Phase 2: 0 new high-quality proposals found across the 5 thinkers without 2026-04-27/2026-05-04 pending coverage (Hoffman, Hawkins, Kastrup, Fredrickson, Arkani-Hamed). Searches returned only previously-captured material or items outside the 60-day window." The phrasing accepts 0-result as the natural endpoint of Phase 2 and proceeds directly to Phase 3. ASSUMPTION-084 codifies this as a stated commitment.
  Why it was unstated: The orchestrator's empty-Phase-2 disposition mirrors the BRIEFING-LAYER flag-don't-reconcile pattern (PREMISE-006), but no audit step yet exists for distinguishing exhaustion from method-bound zero.
  Type: methodological / epistemic
  Related decisions: ASSUMPTION-084 (parent stated assumption), candidate DECISION-022 (briefing-layer audit contract), ASSUMPTION-068 (master-narrative-gap surfacing > fabrication — same pattern at orchestrator layer)
  Testability: testable empirically (re-run the same 5-thinker Phase 2 with broadened query forms and check for surfaced items the original query missed; audit search-strategy variation across catch-up vs. normal days)
  Risk if wrong: LOW-MEDIUM — if Phase 2 zero-results are method-bound rather than exhaustion, the wiki silently undercollects on catch-up days when same-day specialist throughput already weights the briefing toward acceptance of exhaustion.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-095
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the C282 wiki daily run Phase 2 transcript — the absence of a distinguishing audit step.
    Current status: UNTESTED

PRESUMPTION-096:
  Date surfaced: 2026-05-05
  Statement: [inferred] Specialist self-tagging of cross-tradition signals (Wolfram noting PROP-016 advances CROSS-006/007/015/049; Hoffman noting TRACE Institute "parallels C2A2's own multi-agent architecture"; Stump+Fredrickson naming positivity resonance the "strongest current empirical bridge concept") is presumed reliable as a primary cross-tradition signal source. There is no parallel adjudication step that independently re-evaluates these self-claims before they enter the cross-tradition surface.
  Evidence it was operative: All six specialist outputs today included a "Cross-tradition signals noted: Y" line followed by direct claims linking the proposal to specific CROSS items or to other named thinkers. The orchestrator and the morning briefing both ingest these claims without re-evaluation. ASSUMPTION-086 codifies the operative practice; PRESUMPTION-074 had already flagged specialist-recognition reliability as SYSTEMIC-RISK on 2026-04-27.
  Why it was unstated: The system's design treats specialists as the authoritative within-tradition voice, and within-tradition voice has spillover authority on cross-tradition reach.
  Type: methodological / epistemic
  Related decisions: ASSUMPTION-086 (parent stated assumption), ASSUMPTION-009 (displacement vectors), candidate DECISION-022 (briefing-layer audit contract)
  Testability: testable empirically (independent non-specialist re-evaluation of today's specialist self-tagged CROSS claims; cross-check whether competing same-day "strongest" claims compose or conflict)
  Risk if wrong: MEDIUM-HIGH — compounds PRESUMPTION-074 (SYSTEMIC-RISK on specialist-recognition reliability). If specialists are systematically over-tagging cross-tradition signal, the FINDING register may be inflated by self-confirming claims rather than independent convergence.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-096
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the same-day specialist outputs and the absence of an adjudication step downstream.
    Current status: UNTESTED

PRESUMPTION-097:
  Date surfaced: 2026-05-05
  Statement: [inferred] Multiple specialists making "strongest bridge" claims within the same calendar day (Stump+Fredrickson on positivity resonance as "the strongest current empirical bridge concept for the C2A2 framework"; Hoffman on TRACE Institute as "parallels C2A2's own multi-agent architecture") implies a "strongest" predicate that admits multiple simultaneous winners. No mechanism today resolves whether these claims compete (one is right, the other is wrong), compose (both are right, at different layers), or co-vary (both are downstream of an external news cycle).
  Evidence it was operative: Two same-day specialists used near-identical superlative framing ("strongest", "parallels C2A2's own"). Neither output flagged the other's same-day claim. The morning briefing surfaced the proposals as "8 active findings" without dispositioning the multiple-strongest tension.
  Why it was unstated: Claims are written from within each specialist's local frame; cross-specialist consistency is not part of any specialist's brief.
  Type: structural / methodological
  Related decisions: ASSUMPTION-086 (parent stated assumption — specialist-self-claims as primary), candidate DECISION-022 (briefing-layer audit contract)
  Testability: testable empirically (audit superlative-claim frequency across specialist runs; check whether superlative-claim density correlates with daemon catch-up days)
  Risk if wrong: MEDIUM — if "strongest" claims silently inflate during catch-up days (multiple specialists running back-to-back without external grounding), the FINDING surface will accumulate competing superlatives that confuse the briefing layer's prioritization.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-097
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cross-comparison of today's six specialist outputs.
    Current status: UNTESTED

PRESUMPTION-098:
  Date surfaced: 2026-05-05
  Statement: [inferred] Tom's "RC Explorer — Vision for What This Becomes" walk-thread (a self-sent Gmail at 02:56 UTC today) is presumed adequate as an architectural source-of-record. The morning walk handoff treated the walk-thread as authoritative for extracting six "decisions"; none of those six were canonized as DECISION-NNN entries today. The walk-thread is a narration of a still-evolving vision, but is being read as a settled architecture.
  Evidence it was operative: Morning walk handoff (local_662eb846) reported "Decisions extracted: 6" and "Tasks added to queue: 5". The decisions register (decisions.md) was not updated today — the six "decisions" remain Gmail-thread items, not DECISION-NNN. This continues PRESUMPTION-041's implicit-decision-drift pattern.
  Why it was unstated: The morning-walk skill spec frames walk notes as the canonical input — a pre-formal architectural source — and the handoff agent does not have authority to canonize DECISION-NNN entries.
  Type: methodological / epistemic
  Related decisions: PRESUMPTION-041 (parent — implicit-decision-drift cluster), PRESUMPTION-066 (week-scale user-priority pivot), candidate DECISION-022 (briefing-layer audit contract)
  Testability: testable empirically (audit how many morning-walk-extracted "decisions" become DECISION-NNN entries within N days; track drift)
  Risk if wrong: MEDIUM — six new architectural commitments made today (3-layer model, Tool #1/Tool #2 ordering, AI Heartbeat rebuild urgency, etc.) are absorbed into the briefing without DECISION-NNN tracking, extending the implicit-decision drift surface.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-098
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the morning-walk handoff output's "Decisions extracted: 6" combined with no decisions.md update today.
    Current status: UNTESTED

PRESUMPTION-099:
  Date surfaced: 2026-05-05
  Statement: [inferred] The 3-layer RC Explorer architecture (L1 Document Explorer / L2 C2A2 Wiki / L3 RC Wiki) is presumed coherent and largely non-overlapping — each layer has a distinct role (archaeological / operational / encyclopedic) and the five integration steps treat layer-to-layer flows as one-directional. Items that legitimately straddle layers (e.g., a finding whose archaeological grounding is L1 but whose operational form is L2) have no first-class treatment.
  Evidence it was operative: ASSUMPTION-082 records the 3-layer model with crisp role labels and a 5-step linear roadmap (SD→JSON; proposals→472+; wiki-sourced panels; schema merge; Wiki sidebar panel). The labels imply non-overlap. No discussion today of how cross-layer items are surfaced, deduplicated, or arbitrated.
  Why it was unstated: Cross-layer items have not yet been observed at scale; the model is still aspirational.
  Type: structural
  Related decisions: ASSUMPTION-082 (parent stated assumption)
  Testability: testable empirically (track whether near-future findings can be unambiguously assigned to one layer; count cross-layer items)
  Risk if wrong: LOW-MEDIUM — if layers overlap, the integration steps may need to be re-ordered or to allow for bidirectional flows; the current 5-step linear roadmap could obscure feedback loops.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-099
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 3-layer model's clean partition language and the absence of cross-layer items in the integration roadmap.
    Current status: UNTESTED

PRESUMPTION-100:
  Date surfaced: 2026-05-05
  Statement: [inferred] McGilchrist+Kastrup's same-day note that "AI consciousness in the Rovelli/RQM and More-Than-Allegory proposals (archetypes-precede-instances bears on whether AI agents can inhabit traditions)" is a finding directly relevant to C2A2's foundational ASSUMPTION-007 (AI agents can meaningfully instantiate research traditions; status PARTIALLY-CHALLENGED). The finding entered pending/ as a proposal but did not loop back into the assumptions registry as new evidence on ASSUMPTION-007 — there is no feedback loop that captures specialist-output bearings on foundational assumptions.
  Evidence it was operative: McGilchrist+Kastrup session output explicitly named "whether AI agents can inhabit traditions" as a downstream concern of PROP-2026-05-05-008 (Kastrup on More-Than-Allegory). Today's run (this self-awareness pipeline) is the natural place for this loop-back; no automation exists to surface the bearing.
  Why it was unstated: Specialist outputs are written for the proposal pipeline, not the assumptions/presumptions registry; cross-pipeline bearings are visible only to the self-awareness layer.
  Type: methodological / epistemic
  Related decisions: ASSUMPTION-007 (foundational; status PARTIALLY-CHALLENGED — affected target), candidate DECISION-022 (briefing-layer audit contract — adjacent feedback loop)
  Testability: testable empirically (add a self-awareness step that audits each new proposal for ASSUMPTION-bearing claims and routes them to the registry; measure how many such bearings exist per week)
  Risk if wrong: MEDIUM — without a feedback loop, the assumptions registry can lag specialist outputs that materially update foundational claims; specifically, ASSUMPTION-007's PARTIALLY-CHALLENGED status may need re-evaluation in light of the McGilchrist+Kastrup observation, but the re-evaluation will not happen until 14a/14b explicitly catches it (as today).
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-100
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from McGilchrist+Kastrup specialist output naming the AI-instantiation-of-traditions concern explicitly, plus the absence of a registry feedback loop.
    Current status: UNTESTED

PRESUMPTION-101:
  Date surfaced: 2026-05-05
  Statement: [inferred] The wiki-visualization help popover's filter-semantics text ("within section = OR; across sections = AND; edges require both endpoints visible") is presumed to remain in sync with the implementation in `prsNodeVisible` and `applyPRSFilters`. No automated test ensures the documented semantics match the running code over time. A future refactor of either the popover text or the filter logic could silently desynchronize doc and behavior.
  Evidence it was operative: The popover wording was reconciled against the implementation in today's session (local_64a1eef5) on the developer's word — the explicit reconciliation is a one-time act, not a continuing contract.
  Why it was unstated: Single-instance reconciliation is the prevailing practice; no test infrastructure for filter semantics yet exists.
  Type: methodological
  Related decisions: ASSUMPTION-083 (parent stated assumption)
  Testability: testable empirically (add automated UX tests asserting documented filter semantics; check for desync via diff after each filter-logic change)
  Risk if wrong: LOW-MEDIUM — silent desync misleads end users about which nodes/edges are visible; the explorer's interpretive credibility depends on the popover being accurate.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-101
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the one-time reconciliation pattern described in today's explorer-review session.
    Current status: UNTESTED

PRESUMPTION-102:
  Date surfaced: 2026-05-05
  Statement: [inferred] The daemon's link-count partition (link-count > 1 = fires; link-count = 1 = silently skipped) is presumed deterministic across all task creation paths (MCP `create_scheduled_task`, UI, SDK, hook-generated). Tom's diagnosis applied the partition uniformly to 23 broken tasks of varied origin without examining whether different creation paths produce different link-count distributions.
  Evidence it was operative: Summa session conclusion: "The daemon is firing every task that has link count > 1. It's silently skipping every task that has link count = 1" — applied to a heterogeneous set including `summa-2026-nightly-verification`, `summa-qc-sweep`, `c2a2-agent-wright-rohr`, `c2a2-sewing-agent-weekly`, and 21 `1pm-*` and `korbyt-*` reminders. The partition is treated as universal.
  Why it was unstated: Tom is debugging in flight; partition determinism is the simplest hypothesis consistent with the observed `lastRunAt` distribution.
  Type: empirical / infrastructure
  Related decisions: ASSUMPTION-080 (parent diagnosis), ASSUMPTION-081 (workaround claim)
  Testability: testable empirically (audit task-creation paths and confirm link-count distribution per path; check for non-deterministic registration outcomes)
  Risk if wrong: MEDIUM — if the partition is non-deterministic or path-dependent, the workaround (`fireAt`) may succeed for some tasks and fail for others, and the recovery plan needs to be path-aware rather than universal.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-102
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the universalizing language in the Summa session diagnosis.
    Current status: UNTESTED

PRESUMPTION-103:
  Date surfaced: 2026-05-05
  Statement: [inferred] Specialist outputs labeled by weekday-of-assignment ("MONDAY AGENTS", "TUESDAY AGENTS", "WEDNESDAY AGENTS", "THURSDAY AGENTS", "FRIDAY AGENTS", "SATURDAY AGENT") on a Tuesday run-day adopt the unstated convention that the weekday label refers to assignment, not run. Five of the six labels are mis-stamped relative to the actual run day; the sixth (Tuesday Hawkins+Hoffman) coincides only by accident. The convention has not been articulated.
  Evidence it was operative: All six specialist outputs today used the weekday-stamp convention without qualifier. Date stamps (2026-05-05) are correct; weekday stamps (MON–SAT) match assignment, not run-day.
  Why it was unstated: The catch-up scenario was not anticipated when specialist labels were designed; under spread-across-week distribution, weekday-of-assignment and weekday-of-run coincide.
  Type: methodological / operational
  Related decisions: ASSUMPTION-079 (same-day catch-up framing), ASSUMPTION-011 (specialist-first scheduling)
  Testability: testable empirically (audit downstream consumers — pattern detector, master agent, briefing — for confusion when weekday and run-day disagree)
  Risk if wrong: LOW — humans will likely notice; downstream agents may treat the label as run-day and mis-attribute the cross-tradition signal cluster's date provenance.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-103
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the consistent weekday-stamp pattern across today's six specialist outputs.
    Current status: UNTESTED

PRESUMPTION-104:
  Date surfaced: 2026-05-08
  Statement: [inferred] An "org-monthly-usage-limit" interrupt on a personal-account Cowork session is treated by the user as a system-naming misclassification (the wording says "org" but the account is personal) — yet the system's behavior matches a real quota event. The presumption is that the *naming* mismatch (org-vs-personal in the message) implies a *classification* error, when in fact the underlying throttling mechanism may be the same and the message wording may simply be imprecise.
  Evidence it was operative: Tom's two same-session clarifications: "this is not an org account...I have one, but this isn't it." The session continued after the second interrupt and the assistant treated the next turn as a normal continuation, not as a re-test of the quota state.
  Why it was unstated: Naming-classification distinctions are below the threshold of explicit articulation in working sessions; users typically take system-wording at face value while privately discounting it.
  Type: methodological / epistemic
  Related decisions: ASSUMPTION-088 (org-limit treated as work-blocking), ASSUMPTION-071 (browser-auth as agent-prohibited)
  Testability: testable empirically (compare account-tier metadata to the actual throttle threshold; check whether personal-account Cowork sessions can hit a quota that uses "org" wording in error messages)
  Risk if wrong: Medium — if the wording is accurate (i.e., a misattribution by the system to the wrong account), then debugging the actual quota is blocked behind a naming bug; if the wording is imprecise but the throttling is real, no behavioral change is needed.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-104
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the gap between Tom's clarification ("this is not an org account") and the absence of any subsequent investigation of whether the org-vs-personal distinction maps to different quotas.
    Current status: UNTESTED

PRESUMPTION-105:
  Date surfaced: 2026-05-08
  Statement: [inferred] When a Cowork session is interrupted before completing its target deliverable (here: the explorer-bug composite action plan), "queued" is treated as a state that persists across sessions — i.e., the next interactive turn will resume from where the prior turn stalled. No registry entry, no formal hand-off, no scheduled follow-up is created. The presumption is that the user-and-assistant joint memory of the queued item is sufficient to ensure resumption.
  Evidence it was operative: The explorer-fix session (local_56cc4dfb) ended with the assistant offering "Just confirm and I'll produce the composite plan" — but the confirmation never came in this session. The cowork-to-chat summary records "Synthesis with the prior internal report was queued at end-of-session; no composite action plan was produced today" without creating an OPEN-NNN, a scheduled task, or a deferred-action registry entry.
  Why it was unstated: The handoff primitive for "queued in another session" is implicit in the dual-channel walk-and-build cadence; making it explicit would require a session-lifecycle protocol that has not been written.
  Type: methodological / operational
  Related decisions: PRESUMPTION-046 (user-pivot discharges handoff payload — adjacent), PRESUMPTION-043 (parked-session indefinite-retention), candidate DECISION-021 (hand-off primitive)
  Testability: testable empirically (track time-to-resumption for items queued at end-of-session vs. items captured in OPEN-NNN/queue.md/scheduled-task; measure drop-rate)
  Risk if wrong: Medium-High — if "queued" memory does not persist (or is forgotten across the morning walk), the explorer composite action plan never lands and the bug-fix track stalls indefinitely.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-105
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of a formal hand-off entry for the queued composite synthesis — the cowork-summary's "queued at end-of-session" framing without registry citation.
    Current status: UNTESTED

PRESUMPTION-106:
  Date surfaced: 2026-05-08
  Statement: [inferred] The line between "protocol-routine" decisions (e.g., today's seven 2026-04-28 review-decision approvals) and "architectural" decisions worthy of DECISION-NNN canonization is presumed to be self-evident, but has never been articulated as a written policy. The cowork-to-chat summary's "Key Decisions Made: None canonized. ... Today's seven review approvals are protocol-routine batch decisions, not architectural DECISION-NNN entries" reads as if the distinction is obvious; in fact, it is operationalized only by the interpreter's intuition.
  Evidence it was operative: Cowork-to-chat summary 2026-05-08, "Key Decisions Made" section explicitly distinguishes "protocol-routine batch decisions" from "architectural DECISION-NNN entries" without defining the distinction. PRESUMPTION-098 (walk-thread Gmail as architectural source-of-record without canonization) and PRESUMPTION-041 (implicit-decision drift) sit in the same cluster.
  Why it was unstated: The criterion is below the threshold of explicit articulation; users learn it implicitly by observing which items get DECISION-NNN entries and which do not.
  Type: methodological / normative
  Related decisions: PRESUMPTION-041, PRESUMPTION-098, candidate DECISION-022 (briefing-layer audit contract — adjacent)
  Testability: testable empirically (audit prior decisions register for inconsistencies — items canonized vs. not at the protocol-vs-architectural boundary; check inter-rater agreement on a sample)
  Risk if wrong: Medium — if the criterion is inconsistent, the decisions register has both false-positives (protocol items canonized) and false-negatives (architectural commitments not canonized); the latter is the implicit-decision-drift family.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-106
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cowork-summary's "protocol-routine batch decisions, not architectural DECISION-NNN entries" formulation — the absence of a written criterion for the distinction.
    Current status: UNTESTED

PRESUMPTION-107:
  Date surfaced: 2026-05-08
  Statement: [inferred] The two same-session org-monthly-usage-limit interrupts in local_56cc4dfb are presumed to be Anthropic-side service issues (the implicit working hypothesis is "wait it out / try later") rather than usage-pattern issues worth examining (e.g., parallel session count, token volume, cross-account multiplexing). No diagnostic was performed in-session; the workaround was simply to retry — and when the retry hit the same limit, to defer the synthesis.
  Evidence it was operative: Two same-session org-limit interrupts in local_56cc4dfb. No analysis of trigger conditions, no log of concurrent sessions, no token-volume audit. The cowork-summary records "the session hit an org-monthly-usage-limit interrupt twice (Tom clarified the active connectors GitHub/Asana/PagerDuty are personal, not org-tied)" — the diagnostic content is the connector-account clarification, not the limit-trigger conditions.
  Why it was unstated: Service-vs-pattern attribution is implicit; users default to attributing repeated quota errors to the vendor when the alternative (their own usage) is harder to investigate without instrumentation.
  Type: methodological / empirical
  Related decisions: ASSUMPTION-088 (org-limit treated as work-blocking), PRESUMPTION-104 (org-vs-personal naming presumption), ASSUMPTION-094 (combined-escalation threshold)
  Testability: testable empirically (instrument concurrent Cowork session counts and token volumes; correlate with org-limit interrupts; reproduce under controlled load)
  Risk if wrong: Medium-High — if the trigger is a usage-pattern (e.g., cross-project parallel sessions, since Summa-2026 was running QC sweeps in parallel), the next session will hit the same limit; if it is service-side, retry will succeed eventually.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-107
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of usage-pattern analysis in local_56cc4dfb after two same-session org-limit hits + the parallel Summa-2026 QC throughput ongoing today.
    Current status: UNTESTED

PRESUMPTION-108:
  Date surfaced: 2026-05-08
  Statement: [inferred] Three weekday-required scheduled tasks fired and stalled today (1pm register cleanup at "let's do it" prompt; sewing-agent-weekly hit org-limit immediately; Wright/Rohr Sunday agent hit org-limit immediately) without any of them triggering an automated escalation alert, an OPEN-NNN entry, a registered "stalled-task" event, or a re-arm. The presumption is that human-noticing (Tom reading the cowork-to-chat summary on the morning walk) is sufficient closure for stalled scheduled tasks.
  Evidence it was operative: Cowork-summary records all three stalls; none triggered an automated alert. The "What's Next" section frames the resolution as either a Saturday rerun or a Monday absorption — both human-initiated.
  Why it was unstated: Stalled-task closure is implicit in the daily walk-and-build cadence; an automated alert path has not been built.
  Type: methodological / operational / monitoring
  Related decisions: PRESUMPTION-035 (threshold-free flag invocation), PRESUMPTION-052 (second-consecutive null-walk handled by same fallback without escalation), ASSUMPTION-093 (Saturday-rerun as standard closure)
  Testability: testable empirically (count stalled-task events without escalation over N weeks; measure time-to-closure; compare with hypothetical alerted version)
  Risk if wrong: Medium-High — if human-noticing fails on a high-frequency stall day, the closure path stops working and stalls accumulate silently; today's three-stall-day is the largest stall surface yet observed and tests the limit.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-108
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from today's three-stall record + the absence of any automated alert / OPEN-NNN entry capturing the pattern.
    Current status: UNTESTED

PRESUMPTION-109:
  Date surfaced: 2026-05-08
  Statement: [inferred] An external-LLM (Codex 5.5) review of the C2A2 explorer is treated as compositionally equivalent to an internal review for synthesis purposes — no separate epistemic weighting is applied for "different model, different access pattern, different bias profile." The cowork-summary's "Codex 5.5's external review converges with whatever internal report Tom had already produced" reads the convergence at face value, without examining whether the convergence reflects shared training data, shared blind spots, or a third independent confirmation.
  Evidence it was operative: Cowork-to-chat summary 2026-05-08, "What Was Accomplished Today" + "For Morning Discussion" item 1: "Codex 5.5's external review converges with whatever internal report Tom had already produced; the work to do is the composite." No mention of Codex's known biases (e.g., GPT-family training cutoffs, code-style preferences, accessibility weightings). ASSUMPTION-089 articulates the composite-synthesis intent; this presumption surfaces the unweighted-composition substrate.
  Why it was unstated: Cross-LLM review composition is novel for the C2A2 explorer track; the bias-profile question would require a meta-evaluation that has not been built.
  Type: epistemic / methodological
  Related decisions: ASSUMPTION-089 (composite-synthesis intent), PRESUMPTION-014 (cross-tradition signal validity — analogous risk at content layer), PRESUMPTION-020 (AI synthesis bias profile — same family at agent layer), PRESUMPTION-115 (Codex prioritization adopted without adjudication)
  Testability: testable empirically (run the same review prompt against ≥3 LLMs; measure agreement vs. disagreement; examine whether agreement clusters reflect training-data overlap)
  Risk if wrong: Medium — if Codex and the internal report share blind spots (e.g., both miss the L1/L2/L3 RC Explorer model context from ASSUMPTION-082), the composite reinforces a shared error rather than adding independent signal.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-109
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the "convergence" framing in the cowork-summary's treatment of Codex 5.5 + the absence of any epistemic-weight protocol for cross-LLM review composition.
    Current status: UNTESTED

PRESUMPTION-110:
  Date surfaced: 2026-05-08
  Statement: [inferred] The cross-project YouTube IP-block (Summa-side) is presumed to be at the *same architectural layer* as the C2A2 OPEN-039 cluster items (egress allowlist, mount topology, .git/index.lock, daemon link-count = 1, browser-auth) — i.e., all five constraints are "sandbox infrastructure" and are usefully reportable as a single combined escalation. The architectural-layer claim is doing real work in the single-vs-parallel decision and has not been examined.
  Evidence it was operative: Cowork-summary 2026-05-08 "For Morning Discussion" item 3: "Question: file a single combined escalation note to Anthropic this week, or hold for one more cycle's worth of repro data?" The phrasing presumes the constraints belong to the same escalation track. ASSUMPTION-094 articulates the single-escalation-threshold; this presumption surfaces the same-layer assumption beneath it.
  Why it was unstated: The "sandbox infrastructure" framing is convenient and natural; pulling apart whether YouTube-IP-block (network egress at a third-party endpoint) belongs in the same bucket as daemon-registration-bug (Anthropic-side scheduling) requires a layered model of the failure surface that has not been written.
  Type: structural / methodological
  Related decisions: ASSUMPTION-094 (combined-escalation threshold), OPEN-039 (sandbox-infrastructure-escalation cluster)
  Testability: testable empirically (route the constraints to different escalation owners at Anthropic; measure resolution rates; if all five resolve through the same channel, the same-layer presumption is supported); testable via literature (incident-classification frameworks)
  Risk if wrong: Medium — if the constraints are at different layers, a combined report dilutes each individual case and may slow resolution of the most-painful one (daemon link-count = 1, which is currently blocking the wiki-orchestrator daily run).
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-110
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from ASSUMPTION-094's threshold framing + the cowork-summary's same-layer treatment of the five constraints in OPEN-039 cluster + Summa YouTube IP-block.
    Current status: UNTESTED

PRESUMPTION-111:
  Date surfaced: 2026-05-08
  Statement: [inferred] The cowork-to-chat sync's third consecutive failed delivery to claude.ai (2026-05-05 evening + 2026-05-05 morning + 2026-05-08 evening — same auth-not-signed-in mode each time) does not warrant a workaround track or treating the chrome-extension-claude.ai-auth path as broken-by-default. The disposition remains "wait for Tom to sign in," with no periodic re-auth reminder, no fallback delivery channel (Gmail self-thread, registered queue file, etc.), and no escalation.
  Evidence it was operative: Today's cowork-summary header explicitly notes "same auth state as the 2026-05-05 evening run and the 2026-05-05 morning chat-to-cowork run." Three consecutive same-failure-mode runs and the disposition is identical: "Sign-in itself must be done by Tom (not auto-fillable per the access-control rules)."
  Why it was unstated: ASSUMPTION-071 (browser-auth as agent-prohibited) is operative; the consequence — that browser-auth-required tasks cannot be made reliable without user attention — is implicit in that constraint. The fallback question has not been asked because the constraint is treated as fixed.
  Type: methodological / normative
  Related decisions: ASSUMPTION-071 (browser-auth as agent-prohibited), PRESUMPTION-038 (billing bug self-clear — analogous), PRESUMPTION-068 (Chrome MCP double-success as resolved)
  Testability: testable empirically (count delivery-failure recurrence; build a fallback-channel proof-of-concept and measure delivery-success delta)
  Risk if wrong: Medium-High — if the cowork-to-chat sync continues to fail on every run (Tom doesn't sign in until prompted in person), the morning-walk Chat conversation has stale context and the daily-walk-and-build cadence loses one of its primary signal channels.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-111
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the third-consecutive-failure pattern + the unchanged disposition + the absence of a fallback-channel design.
    Current status: UNTESTED

PRESUMPTION-112:
  Date surfaced: 2026-05-08
  Statement: [inferred] The deferred 1pm register-cleanup task (local_1d6dddab, stalled at "let's do it" prompt) and the queued explorer-bug composite synthesis (local_56cc4dfb, stalled at org-limit) are presumed to be structurally similar enough to receive the same "weekend-or-Monday" disposition. In fact, they differ in work-character (record-reconciliation vs. technical bug-fix synthesis), in resumption requirement (Tom-present vs. assistant-can-resume-once-quota-clears), and in time-criticality (drift compounds vs. Chrome-exception-on-every-pageload).
  Evidence it was operative: Cowork-summary's "What's Next" treatment of both items as deferred-this-weekend without distinguishing their characters. "What's Next" item 1 (composite action plan) and "What's Next" item 2 (register cleanup) are listed sequentially in the same priority frame.
  Why it was unstated: The deferred-task primitive does not yet distinguish work-character; the user's mental model is more granular than the registry.
  Type: methodological / operational
  Related decisions: ASSUMPTION-093 (Saturday-rerun as standard closure), PRESUMPTION-105 (queued-across-sessions presumption)
  Testability: testable empirically (track time-to-closure for the two items separately; observe whether the differing characters produce differing closure times)
  Risk if wrong: Low-Medium — undifferentiated treatment may slow the higher-leverage item (technical bug-fix that affects every site visitor) relative to the lower-leverage one (record reconciliation that affects only Tom's planning).
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-112
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cowork-summary's parallel placement of the two deferred items in "What's Next" without character-differentiation.
    Current status: UNTESTED

PRESUMPTION-113:
  Date surfaced: 2026-05-08
  Statement: [inferred] Off-cadence specialist proposal filings on a Friday (Stump on Thursday slot, Fredrickson ×2 on Thursday slot) are presumed to have the *same baseline expectations* (quality, evidence depth, source provenance) as on-cadence filings. No examination of whether off-cadence filings have different baseline expectations, different selection-bias profiles, or different downstream review-page treatment is performed.
  Evidence it was operative: Five new pending proposals dated 2026-05-08 include three off-cadence filings; the cowork-summary treats them uniformly as "These will land on the next review page." ASSUMPTION-091 articulates the operational uniformity; this presumption surfaces the unexamined-equivalence substrate.
  Why it was unstated: The cadence rule (specialist-first scheduling, ASSUMPTION-011) was never formally extended or relaxed; off-cadence filings happen organically and are absorbed into the normal flow without policy review.
  Type: methodological
  Related decisions: ASSUMPTION-091 (off-cadence treated as on-cadence), ASSUMPTION-011 (specialist-first scheduling), ASSUMPTION-079 (catch-up framing)
  Testability: testable empirically (audit approval rate, evidence depth, source-provenance categories for off-cadence vs. on-cadence proposals over N weeks)
  Risk if wrong: Low-Medium — if off-cadence filings systematically differ (e.g., are produced under different time pressure, different specialist mood, different research-anchor timing), the proposal pipeline has a hidden source of variance that downstream pattern-detection treats as noise.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-113
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from today's 5-proposal pending listing (3 off-cadence) + the cowork-summary's uniform treatment + the absence of any cadence-vs-quality audit.
    Current status: UNTESTED

PRESUMPTION-114:
  Date surfaced: 2026-05-08
  Statement: [inferred] The 3-day master-narrative absence for the wiki-orchestrator daily run (2026-05-06 → 2026-05-08) is presumed *more likely* caused by the daemon link-count = 1 silent-skip bug (ASSUMPTION-080/081) than by alternative failure modes (Phase 2 zero-result, write-error, agent-time-budget exhaustion, quiet-script-error, sandbox-infrastructure mid-phase failure). The working hypothesis privileges the most-recently-diagnosed cause over the broader set of plausible causes.
  Evidence it was operative: Cowork-summary 2026-05-08 "For Morning Discussion" item 4: "This is the same shape as the 7-day silence diagnosed on 05-05 as ASSUMPTION-081 (link-count = 1 daemon registration). Worth checking whether the wiki-orchestrator daily task itself is link-count = 1 affected." ASSUMPTION-092 articulates the hypothesis as a stated commitment; this presumption surfaces the privileging of one cause over the alternative-explanations set.
  Why it was unstated: The daemon-bug is the most salient cause because it was diagnosed three days ago and is fresh in working memory; alternative causes would require independent investigation.
  Type: empirical / epistemic
  Related decisions: ASSUMPTION-092 (master-narrative-gap = link-count regression), ASSUMPTION-080, ASSUMPTION-081, OPEN-038 (master-narrative-gap escalation question)
  Testability: testable empirically (`stat -c %h` the wiki-orchestrator scheduled task; if =1, the hypothesis is supported; if >1, alternative causes need investigation)
  Risk if wrong: Medium — if the cause is something other than the link-count bug (e.g., a script error in the orchestrator itself), focusing escalation on Anthropic-side daemon repair will not unblock the wiki-orchestrator and the master-narrative gap will compound.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-114
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cowork-summary's hypothesis privileging + ASSUMPTION-092's working-hypothesis framing + the absence of an alternative-explanations enumeration.
    Current status: UNTESTED

PRESUMPTION-115:
  Date surfaced: 2026-05-08
  Statement: [inferred] Codex 5.5's "Best next move: fix the extractOverview() bug, add a smoke-test script, and create a responsive fallback shell" prioritization is adopted by the cowork-summary almost verbatim ("Recommendation: do (b) first ... Then add the smoke-test script before tackling the responsive shell") without an adjudication step. Codex does not have access to the L1/L2/L3 RC Explorer model (ASSUMPTION-082), the AI Heartbeat Tool #2 ordering, or the broader project context — yet its prioritization is treated as if it could.
  Evidence it was operative: Cowork-summary "For Morning Discussion" item 1's recommendation mirrors Codex's tri-part priority. No examination of whether Codex's priorities reflect Tom's project context or whether Codex's smaller bug-fix bias (typical for code-review LLMs) might mismatch the L1 instrument's strategic role in the 3-layer model.
  Why it was unstated: The composite-synthesis intent (ASSUMPTION-089) makes the sources composable in principle; the adjudication step is implicit in "synthesis" but has not been formalized for this layer (parallel to PRESUMPTION-074's SYSTEMIC-RISK on specialist-recognition reliability — same epistemic move at the external-tool-review layer).
  Type: methodological / epistemic
  Related decisions: ASSUMPTION-089 (composite-synthesis intent), ASSUMPTION-090 (smallest-fix-first prioritization), PRESUMPTION-074 (specialist-self-tagging without adjudication — analogous), PRESUMPTION-109 (cross-LLM review composition without bias weighting)
  Testability: testable empirically (compare adopted-priorities outcome vs. project-context-weighted outcome on a held-out review pair); testable via literature (review-aggregation frameworks that weight reviewers by domain familiarity)
  Risk if wrong: Medium — if Codex's tri-part priority misses the L1-instrument strategic role, the explorer track may ship a polished bug-fix and a smoke-test that don't address what actually matters most for the L1/L2/L3 architecture.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-115
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cowork-summary's near-verbatim adoption of Codex's prioritization + the absence of a project-context-adjudication step.
    Current status: UNTESTED

PRESUMPTION-116:
  Date surfaced: 2026-05-09
  Statement: [inferred] The "densest single cycle on record" framing presumes that lit-search cycle-density (count of SYSTEMIC-RISK flags per cycle) is itself a meaningful comparison metric across cycles of varying input volume, topic mix, and elapsed-time-since-prior-cycle. No examination of whether a 4-flag-on-20-items density compares like-for-like with prior cycles' flag-rates on different batch sizes (5-day backlog vs. 1-day batch vs. weekly periodic-monitor batch).
  Evidence it was operative: Cowork-summary 2026-05-09 second paragraph: "the largest cluster of SYSTEMIC-RISK flags in any one lit-search cycle to date — four flags." ASSUMPTION-096 codifies the density framing without normalizing for batch composition or content variability.
  Why it was unstated: The 4-flag observation is salient and immediately legible; normalizing across cycles would require a reference-rate calculation that has never been computed. The narrative form rewards superlatives over rate-comparisons.
  Type: epistemic / methodological
  Related decisions: ASSUMPTION-096 (densest-cycle framing), ASSUMPTION-072 (5-day backlog drainable), ASSUMPTION-073 (REVISE heuristic), candidate DECISION-022 (briefing-layer audit contract)
  Testability: testable empirically (compute SYSTEMIC-RISK rate per N items across all 7 prior cycles + this cycle; produce a normalized comparison and audit whether 2026-05-09 still ranks "densest" by rate)
  Risk if wrong: Low-Medium — if cycle-density is not the right metric, the cluster-level remediation prioritization (ASSUMPTION-096) may be over-weighting a noisy signal.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-116
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cowork-summary "densest on record" framing + the absence of a normalized-rate comparison.
    Current status: UNTESTED

PRESUMPTION-117:
  Date surfaced: 2026-05-09
  Statement: [inferred] The proposed "Core Operational Discipline" architectural sprint (ASSUMPTION-097) presumes that registration (PRESUMPTION-105 cross-session persistence), canonization (PRESUMPTION-106 protocol-vs-architectural decision-classification), and fallback (PRESUMPTION-111 cowork-to-chat sync no-fallback design) are similar enough in remediation-substrate to justify bundled remediation. No examination of whether they require structurally distinct interventions (registry-format change vs. governance-protocol writing vs. channel-resilience engineering).
  Evidence it was operative: Cowork-summary 2026-05-09 "What's Next" item 7 framing the bundle as "explicit recommendation from today's lit-search" without enumerating the per-item remediation surface; "For Morning Discussion" item 3 noting "Bundling has the advantage of cross-cluster-borne remediation efficiencies" but not specifying what those efficiencies are.
  Why it was unstated: The three items reach REVISE in the same cycle and share a "third recurrence" tag, which makes them feel cohesive at the surfacing layer; the remediation layer would require independent investigation per item.
  Type: methodological / architectural
  Related decisions: ASSUMPTION-097 (Core Operational Discipline sprint), PRESUMPTION-105, PRESUMPTION-106, PRESUMPTION-111
  Testability: testable empirically (decompose the three remediations into work-units; compare bundled-sprint completion against parallel-track completion on a held-out cluster); testable via literature (architectural-debt cluster-vs-atomic remediation outcomes)
  Risk if wrong: Medium — if the three items require distinct interventions, bundling may delay all three by waiting for the slowest, or may produce a sprint that "completes" but only addresses one of the three substantively.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-117
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cowork-summary's bundle proposal + the absence of a per-item remediation-surface enumeration.
    Current status: UNTESTED

PRESUMPTION-118:
  Date surfaced: 2026-05-09
  Statement: [inferred] The DECISION-027 unify-or-split question (ASSUMPTION-099) presumes the choice between a unified protocol (one DECISION-027 covering specialist + external-tool-review) versus a split (DECISION-027 specialist + DECISION-028 external-tool-review) is reversible at low epistemic cost — i.e., we can write it unified now and split later if needed, or vice versa, with no information-loss penalty for the wrong choice.
  Evidence it was operative: Cowork-summary 2026-05-09 "For Morning Discussion" item 2 poses the unify-vs-split question without flagging the asymmetric-reversibility risk: a unified protocol that proves inadequate for either source-type requires retroactive splitting (potentially after instances have already been adjudicated under the unified frame), whereas split protocols that prove redundant only cost duplicate maintenance overhead.
  Why it was unstated: Software/governance choices are routinely framed as if ADRs are append-only and freely revisable; the cost asymmetry between revising forward vs. revising backward is invisible at decision time.
  Type: methodological / architectural
  Related decisions: ASSUMPTION-099 (DECISION-027 scope extension), candidate DECISION-027, PRESUMPTION-115 (Codex prioritization adoption)
  Testability: testable via literature (architecture-decision-record reversibility cost asymmetry literature); testable empirically (audit historical DECISION-NNN scope-revisions in this project for forward-vs-backward cost difference)
  Risk if wrong: Medium — if the choice is in fact asymmetrically reversible, the question Tom is being asked materially affects both protocol coverage and downstream adjudication burden.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-118
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cowork-summary's binary unify-or-split framing + the absence of a reversibility-cost note.
    Current status: UNTESTED

PRESUMPTION-119:
  Date surfaced: 2026-05-09
  Statement: [inferred] The claim that Saturday Wolfram's two proposals deliver "the highest-leverage cross-tradition signal of the week" (ASSUMPTION-100) presumes "leverage" is measurable on a single weekly axis without specifying whether "leverage" means convergence-strength (how tight the three-way ontological agreement is), novelty (how new the connection is to the network), or downstream actionability (how much the connection unblocks for synthesis). All three readings are plausible; the cowork-summary collapses them.
  Evidence it was operative: Cowork-summary 2026-05-09 "For Morning Discussion" item 5 uses "highest-leverage" without an operational definition; the three CROSS references (CROSS-007/025/031/049/051) span both directly-articulated convergences and indirectly-implied ones, suggesting the term may be aggregating across multiple distinct signal types.
  Why it was unstated: "Leverage" is a familiar shorthand in operational contexts; the operational definition would slow the narrative without changing the immediate decision (Pattern-Detector deep-pass scheduling).
  Type: epistemic / methodological
  Related decisions: ASSUMPTION-100 (Saturday Wolfram leverage claim), ASSUMPTION-086 (specialist-self-claims as primary signal), PRESUMPTION-074 (specialist-recognition reliability)
  Testability: testable empirically (operationally define each candidate reading of "leverage"; compute the three Wolfram proposals' rank under each reading; check whether they remain top-week under all three readings or only under one)
  Risk if wrong: Low-Medium — if "leverage" means different things to different downstream consumers (Pattern Detector vs. tradition-agent dispatch vs. master-narrative), the prioritization may be coherent at headline level but incoherent at action level.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-119
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cowork-summary's single-axis "leverage" claim + the absence of an operational definition.
    Current status: UNTESTED

PRESUMPTION-120:
  Date surfaced: 2026-05-09
  Statement: [inferred] The proposal to schedule a Pattern-Detector deep-pass before the standard review cycle (per ASSUMPTION-100) presumes the Pattern Detector's scheduling layer can absorb non-standard out-of-band insertions without policy specification. No examination of whether out-of-band scheduling has its own selection-effect risk (privileging specialist-flagged content over baseline-discoverable content) or whether it competes with the standard cycle for limited-pass capacity.
  Evidence it was operative: Cowork-summary 2026-05-09 "For Morning Discussion" item 5 binary question ("schedule a Pattern Detector deep-pass on these two proposals before the standard review cycle, or let them flow through normally?") frames the choice without addressing scheduling-policy implications.
  Why it was unstated: The Pattern Detector is treated as a passive utility; its scheduling priorities are emergent rather than codified.
  Type: methodological / operational
  Related decisions: ASSUMPTION-100 (Saturday Wolfram leverage), ASSUMPTION-086 (specialist-self-claims primary), PRESUMPTION-074 (specialist-recognition reliability), PRESUMPTION-029 (multi-subagent batch inflation)
  Testability: testable empirically (run the deep-pass and the standard cycle in parallel on a held-out Saturday batch; compare findings-rate, novelty-rate, and overlap); testable via literature (selection-effect literature on out-of-band content prioritization)
  Risk if wrong: Medium — if out-of-band scheduling has selection-effects, a deep-pass on Wolfram-flagged proposals may inflate the FINDING-NNN rate on Wolfram-related cross-tradition signals while leaving baseline-discoverable signals under-pressed.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-120
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cowork-summary's out-of-band scheduling proposal + the absence of a scheduling-policy implication note.
    Current status: UNTESTED

PRESUMPTION-121:
  Date surfaced: 2026-05-09
  Statement: [inferred] The Codex-style external-LLM diagnostic for the Chrome MCP "normal windows" error (per ASSUMPTION-101) is presumed reliable enough to skip independent project-context adjudication, despite this being a direct extension of PRESUMPTION-115's SYSTEMIC-RISK pattern (cross-LLM prioritization adoption without bias weighting) from the explorer-fix layer to the chat-scrape failure-mode layer.
  Evidence it was operative: Cowork-summary 2026-05-09 "For Morning Discussion" item 6 attributes the root-cause to "Codex-style external-LLM diagnostic" and adopts the environment-state-issue framing without an internal cross-check (e.g., reproducing the error on a known-normal-window-state Chrome session, or testing the alternative hypothesis that recent Chrome MCP updates introduced a regression).
  Why it was unstated: Same-day acceptance of an external-LLM diagnostic feels efficient; the parallel between this case and the explorer-fix case (PRESUMPTION-115) was not yet salient when the cowork-summary was written.
  Type: methodological / epistemic
  Related decisions: ASSUMPTION-101 (Chrome-MCP environment-state attribution), PRESUMPTION-115 (Codex prioritization adoption), PRESUMPTION-074 (specialist-recognition reliability), candidate DECISION-027 (specialist-recognition adjudication tier; potential scope extension per ASSUMPTION-099)
  Testability: testable empirically (attempt the chat-scrape under a verified-normal-window Chrome state; if it succeeds, ASSUMPTION-101 is supported; if it fails, the environment-state attribution is wrong); testable via literature (review-aggregation frameworks for external-LLM diagnostic uptake)
  Risk if wrong: Medium-High — this is an active recurrence of the SYSTEMIC-RISK pattern flagged by today's lit-search at PRESUMPTION-115; if the pattern is real, the chat-scrape failure may be misdiagnosed and continue recurring after the proposed environment-state "fix."
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-121
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from ASSUMPTION-101's external-LLM-diagnostic uptake + the structural parallel to PRESUMPTION-115 + the absence of an internal cross-check.
    Current status: UNTESTED

PRESUMPTION-122:
  Date surfaced: 2026-05-09
  Statement: [inferred] The proposed alternative remediation in ASSUMPTION-101 — "document the pre-condition for Tom and continue" (i.e., rely on Tom to ensure a normal Chrome window exists before each scheduled scrape) — presumes that documentation-for-a-human-user is reliable enough to count as a "fix" for a recurring scheduled-task failure mode, without programmatic enforcement of the pre-condition.
  Evidence it was operative: Cowork-summary 2026-05-09 "For Morning Discussion" item 6 lists "document the pre-condition for Tom and continue" as a parallel option to the programmatic `pre-scrape-ensure-normal-window` step, treating the two as comparable remediations.
  Why it was unstated: Documentation feels like a remediation because it transfers the responsibility; the system-side reliability change is zero, but the social contract changes.
  Type: methodological / operational
  Related decisions: ASSUMPTION-101 (Chrome-MCP environment-state attribution), PRESUMPTION-052 (recurrence-without-escalation), ASSUMPTION-093 (Saturday-rerun closure), PRESUMPTION-108 (human-noticing as sufficient closure)
  Testability: testable empirically (track scrape-success-rate under documentation-only remediation across N≥4 future runs; compare to programmatic-enforcement rate)
  Risk if wrong: Low-Medium — if Tom does not consistently maintain the pre-condition (because the failure is silent on Tom's side until the morning summary lands), documentation-only remediation reduces to no remediation; this extends the PRESUMPTION-108 cluster to a third recurrence-without-system-fix instance.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-122
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cowork-summary's parallel-option framing + the absence of a system-side-reliability vs. social-contract distinction.
    Current status: UNTESTED

PRESUMPTION-123:
  Date surfaced: 2026-05-09
  Statement: [inferred] The "drained 100% in one cycle" framing for today's lit-search (per ASSUMPTION-102) presumes cycle-throughput is the right success metric for the lit-search pipeline, rather than dispositioning quality (whether MONITOR / REVISE / INCORPORATE were correctly assigned), INCORPORATE rate (whether validated premises are accumulating), or REVISE-burden induced (whether REVISE-flagged items get human follow-through).
  Evidence it was operative: Cowork-summary 2026-05-09 "Pipeline Status" celebrates the single-cycle drain without surfacing today's INCORPORATE = 0 rate or noting that 9 REVISE flags add to a 64-item REVISE backlog that has not been worked.
  Why it was unstated: Throughput is the most legible metric in pipeline narratives; quality and follow-through are slower signals that don't fit the daily summary cadence.
  Type: methodological / metrics
  Related decisions: ASSUMPTION-102 (single-cycle-drain baseline), ASSUMPTION-072 (5-day backlog drain), DECISION-014 (cycle-time + decision-backlog metrics), PRESUMPTION-035 (threshold-free flag invocation)
  Testability: testable empirically (audit the relationship between cycle-throughput and INCORPORATE-rate / REVISE-follow-through-rate over the prior 7 cycles); testable via literature (review-pipeline metric-design literature)
  Risk if wrong: Medium — if throughput is celebrated while INCORPORATE rate stays at 0 and the REVISE backlog grows, the pipeline produces the appearance of activity without producing operational self-knowledge.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-123
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cowork-summary's throughput-celebration + the absence of an INCORPORATE-rate or REVISE-follow-through-rate note.
    Current status: UNTESTED

PRESUMPTION-124:
  Date surfaced: 2026-05-09
  Statement: [inferred] Today's 8-task fire-rate (ASSUMPTION-103) is treated as positive evidence against the daemon-link-count = 1 regression hypothesis (ASSUMPTION-092), but this presumption privileges per-task evidence over cross-task evidence — the same daemon bug has already been observed to affect tasks selectively (per 2026-05-08 changelog: today's c2a2-evening-cowork-to-chat fired and 1pm register-cleanup fired, but wiki-orchestrator did not fire). A single task firing tells us nothing about other tasks' link-count states.
  Evidence it was operative: Cowork-summary 2026-05-09 "Pipeline Status" daemon paragraph lists 8 tasks fired and concludes "no daemon-bug evidence today" — a global negative inference from a sample that does not include the wiki-orchestrator (which 2026-05-08 flagged as the suspected regression target).
  Why it was unstated: The 8-task list is salient; the wiki-orchestrator's status today is not in the cowork-summary's evidence frame.
  Type: empirical / epistemic
  Related decisions: ASSUMPTION-080, ASSUMPTION-081, ASSUMPTION-092, ASSUMPTION-103, PRESUMPTION-114 (recency-priority cause attribution)
  Testability: testable empirically (audit wiki-orchestrator fire status today via direct inspection of the master-narrative production for 2026-05-09; if absent, the per-task selectivity holds and ASSUMPTION-103's evidence claim has limited reach)
  Risk if wrong: Medium — if the wiki-orchestrator did not fire today, the evidence frame in ASSUMPTION-103 is not transferable to it; the 3-day master-narrative gap may extend to 4 days under the same regression.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-124
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cowork-summary's 8-task evidence frame + the structural parallel to 2026-05-08's per-task-selectivity observation.
    Current status: UNTESTED

PRESUMPTION-125:
  Date surfaced: 2026-05-09
  Statement: [inferred] The cowork-to-chat sync 4th-consecutive failure (today via Chrome-MCP "normal windows" error; previously 2026-05-05 evening + 2026-05-08 evening were sign-in-redirect failures; the 2026-05-09 morning chat-scrape was a 1st same-mode failure on the morning side) is presumed not to escalate disposition severity beyond the 3-consecutive threshold already established by PRESUMPTION-111. No automatic escalation of severity at recurrence count N=4 vs. N=3; no recurrence-counter is tracked.
  Evidence it was operative: Cowork-summary 2026-05-09 "DELIVERY STATUS" header treats the 4th failure with the same disposition language as the 3rd ("wait for Tom to sign in" / "open a normal Chrome window") and frames the remediation as a single-action user-side step. No "now-fourth-consecutive — escalating to..." language.
  Why it was unstated: The 3-consecutive threshold framing in PRESUMPTION-111 was just-introduced (yesterday); the system has not yet had time to articulate a recurrence-counter-driven severity ladder.
  Type: methodological / monitoring
  Related decisions: PRESUMPTION-111 (cowork-to-chat sync no-fallback at N=3), ASSUMPTION-071 (browser-auth as agent-prohibited), PRESUMPTION-035 (threshold-free flag invocation), PRESUMPTION-052 (recurrence-without-escalation)
  Testability: testable empirically (track future cowork-to-chat sync failure recurrences and disposition-language; if N=5 / N=6 failures continue with same disposition, the no-escalation pattern is confirmed); testable via literature (incident-management severity-ladder design)
  Risk if wrong: Medium-High — extends the PRESUMPTION-108 + PRESUMPTION-111 STALLED-TASK-CLOSURE cluster to a 4-recurrence horizon without remediation; reinforces the lit-search-flagged predicted-alert-not-implemented loop (PRESUMPTION-108 SYSTEMIC-RISK).
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-125
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from today's cowork-to-chat DELIVERY STATUS header treating N=4 with same disposition as N=3 + the absence of a recurrence-counter.
    Current status: UNTESTED

PRESUMPTION-126:
  Date surfaced: 2026-05-09
  Statement: [inferred] Today's inbox PROCESSED_LOG reconciliation (6 historical entries appended for 2026-04-27 batch — Levin × synthetic memory, McGilchrist × spaciousness, Stump × collective neuroscience, Wolfram ×3) is presumed to be a one-time backfill without a presumption-of-completeness check or audit-trigger schedule. No examination of whether the same entry-type or other batches are missing from the log; no scheduled audit to detect future drift.
  Evidence it was operative: Cowork-summary 2026-05-09 listing of files modified ("inbox/PROCESSED_LOG.md — 6-entry reconciliation block appended for 2026-04-27 backfill") frames the reconciliation as a discrete event without an audit-recurrence schedule or completeness check.
  Why it was unstated: Reconciliation events are typically framed as cleanup; the meta-question of "what other reconciliation might be needed?" sits one level above the salient task.
  Type: operational / methodological
  Related decisions: PRESUMPTION-035 (threshold-free flag), PRESUMPTION-052 (recurrence-without-escalation), PRESUMPTION-108 (human-noticing as sufficient closure)
  Testability: testable empirically (audit the log for missing entries by joining tradition-wiki integration timestamps against PROCESSED_LOG entries over the prior 60 days); testable via literature (data-completeness audit patterns in operational data systems)
  Risk if wrong: Low-Medium — if other batches are missing without notice, the PROCESSED_LOG drifts from a system-of-record to a partial-record; downstream reporting that depends on the log silently inherits the gap.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-126
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cowork-summary's discrete-event framing of the 6-entry reconciliation + the absence of an audit-trigger note.
    Current status: UNTESTED

PRESUMPTION-127:
  Date surfaced: 2026-05-09
  Statement: [inferred] The three new pending proposals filed today — 2 Wolfram (Saturday slot, on-cadence) + 1 McGilchrist (off-cadence, Friday/Sunday slot) — are presumed routinely absorbable without raising the cadence-coupling concern of PRESUMPTION-113 (off-cadence specialist filings same baseline expectations as on-cadence). Today's McGilchrist filing is the second day in a row with off-cadence specialist filings (2026-05-08 had Stump×1 + Fredrickson×2 off-cadence); a 2-day off-cadence pattern is forming but no PRESUMPTION-113-style concern is re-surfaced.
  Evidence it was operative: Cowork-summary 2026-05-09 second paragraph notes the McGilchrist filing as "off-cadence — Friday/Sunday slot" without flagging the 2-day off-cadence pattern; "Pipeline Status" lists "+3 today" without distinguishing on-cadence from off-cadence.
  Why it was unstated: PRESUMPTION-113 was just-surfaced (yesterday); the pattern would only become salient if a third consecutive off-cadence day occurred or if a downstream signal (review-page rendering, approval-rate divergence) made it visible.
  Type: methodological / operational
  Related decisions: PRESUMPTION-113 (off-cadence as on-cadence baseline), ASSUMPTION-091 (off-cadence treated as on-cadence), ASSUMPTION-079 (catch-up framing), ASSUMPTION-011 (specialist-first scheduling)
  Testability: testable empirically (track off-cadence filing-rate over the next 4 weeks; audit whether off-cadence filings have systematically different downstream profiles)
  Risk if wrong: Low-Medium — if the 2-day off-cadence pattern continues without flagging, the cadence-coupling concern PRESUMPTION-113 surfaces becomes a recurring blind spot; if cadence-and-quality are coupled as PRESUMPTION-113 suspects, a multi-week trend would silently degrade pipeline signal-quality.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-127
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from today's McGilchrist off-cadence filing + the absence of any 2-day off-cadence pattern flag.
    Current status: UNTESTED

PRESUMPTION-128:
  Date surfaced: 2026-05-10
  Statement: [inferred] The 5 first-ever Wright/Rohr pending proposals can be reviewed under the existing pending-proposals workflow without first canonizing DECISION-026 to formally admit Wright + Rohr as traditions — the standard pending-proposals workflow is presumed to accommodate not-yet-canonized traditions; the alternative ordering (canonize first, then review) is named only in "For Morning Discussion" as a question, not as a default policy.
  Evidence it was operative: Cowork-summary 2026-05-10 "For Morning Discussion" item 1: "are these to be reviewed under the standard pending-proposals workflow ... or should the accept/defer be done at the meta level first (canonize DECISION-026 to add Wright + Rohr to `traditions/` with PRS-curation discipline) before reviewing the proposals themselves?" The question is framed as a choice of ordering rather than an exception path; the workflow's silent accommodation of unsanctioned-tradition pendings is the operative presumption.
  Why it was unstated: The pending-proposals workflow has historically been agnostic to tradition-canonization status; new specialist proposals from non-yet-canonized traditions had not previously occurred at scale. The workflow's "of course" treatment of all incoming pendings naturalizes the tradition-status agnosticism.
  Type: methodological / structural
  Related decisions: DECISION-026 (Wright/Rohr addition candidate), ASSUMPTION-111 (blocking-effect), PRESUMPTION-137 (first-ever as decision gate — competing presumption)
  Testability: testable via process (audit whether the not-yet-canonized-tradition pending-proposal pathway leads to systematic review-quality differences vs. canonized-tradition pathway over N≥3 future first-ever events); testable via literature (organizational-decision-ordering / committed-cost effects in admissions processes)
  Risk if wrong: Medium — if canonization-first is the right order, reviewing five proposals first may bias the canonization decision (committed-cost effect: having reviewed proposals favorably presumes the tradition's worth). If proposal-first is right, delaying review for canonization adds queueing time without epistemic benefit.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-128
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from "For Morning Discussion" item 1 framing as a workflow-accommodation choice rather than a workflow-violation question.
    Current status: UNTESTED

PRESUMPTION-129:
  Date surfaced: 2026-05-10
  Statement: [inferred] "92% PRESUMPTION REVISE rate is the highest single-cycle REVISE rate to date" presumes REVISE rate is a meaningful comparison metric without normalization for batch composition — recurrence of PRESUMPTION-116's superlative-without-normalization pattern (densest-cycle), now at the second layer (REVISE-rate-density) within 24 hours.
  Evidence it was operative: Cowork-summary 2026-05-10 paragraph 4: "PRESUMPTIONs 1/12 MONITOR + 11/12 REVISE (92%, the highest single-cycle REVISE rate to date)" — superlative claim asserted without disclosure of batch composition (today's 12 items concentrated in LIT-SEARCH-CYCLE-OUTPUT and SELF-MEASUREMENT clusters that were near-uniformly NO-SUPPORT-FOUND on first-pass; the prior cycles had broader topic spread).
  Why it was unstated: PRESUMPTION-116 was just-surfaced (yesterday); the same pattern is recurring under a different metric label (REVISE rate vs. SYSTEMIC-RISK density). The "record" framing is intuitively appealing without normalization, and reusing the same superlative shape in less than 24 hours suggests a metric-vocabulary blind spot.
  Type: methodological
  Related decisions: PRESUMPTION-116 (densest-cycle without normalization), ASSUMPTION-107 (record REVISE rate claim), PRESUMPTION-123 (throughput-as-success-metric), ASSUMPTION-112 (SELF-MEASUREMENT cluster)
  Testability: testable via literature (metric-design / SPC / superlative-claim audit patterns across heterogeneous-batch settings); testable empirically (audit batch-composition variance across cycles; normalize REVISE rate per item-cluster topic; check whether "record" framing recurs at third layer)
  Risk if wrong: Low-Medium — if REVISE rate as record is not normalized, the "record" framing produces a self-reinforcing throughput-celebration loop (same pathology as PRESUMPTION-123 in different vocabulary); compounds with ASSUMPTION-112 SELF-MEASUREMENT cluster as a second instance of the same cognitive shape.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-129
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-10 paragraph 4 record-rate framing as a 24-hour second-layer recurrence of PRESUMPTION-116.
    Current status: UNTESTED

PRESUMPTION-130:
  Date surfaced: 2026-05-10
  Statement: [inferred] The sewing agent's threshold definitions for "orphan" / "sparse" / "connected" are valid as written — the agent's first-run metric design is being accepted as canonical baseline without external validation, and the connectivity_log.csv's inaugural row is being treated as ground truth for all future trajectory measurements.
  Evidence it was operative: Cowork-summary 2026-05-10 sewing-agent paragraph: "produced a baseline connectivity snapshot: orphans=766, sparse=2, connected=17, total=785 — appended as the inaugural row of `architecture/metrics/connectivity_log.csv` (file created this run)" — no review of threshold-definition appropriateness; the file was created and populated by the agent itself; the agent's own design choices anchor all future measurement.
  Why it was unstated: This is the agent's first weekly run; the metric-design choices are implicit in the agent's code and were not separately reviewed. The convention of "first observation establishes baseline" naturalizes the threshold without examination. PRESUMPTION-130 is a structural cousin of PRESUMPTION-031 (rotation-schedule coverage) and PRESUMPTION-053 (briefing-layer 17→11 filter): each surfaces an agent-internal design choice that is invisible at the architectural-output layer.
  Type: methodological / architectural
  Related decisions: ASSUMPTION-110 (canonical inaugural baseline), DECISION-019 (sewing agent), PRESUMPTION-139 (sensitivity-threshold gap)
  Testability: testable empirically (audit alternate threshold definitions for the same vault snapshot — e.g., sparse=2 vs. sparse∈[1,3] — and compare connectivity-metric sensitivity to threshold choice; benchmark against external graph-connectivity literature)
  Risk if wrong: Medium — if thresholds are wrong, every future trajectory measurement is anchored to a flawed baseline; sewing agent's own flag that "the connectivity metric will be insensitive without a one-time backlink-injection pass" is consistent with the threshold being wrong but is not a sufficient test.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-130
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-10 sewing-agent paragraph baseline-establishing language without review or external-validation discussion.
    Current status: UNTESTED

PRESUMPTION-131:
  Date surfaced: 2026-05-10
  Statement: [inferred] The sewing agent's "agent judgment call" to exclude architecture-root tracking files as routing targets is defensible without user review — autonomous-agent boundary-setting authority is presumed; the agent decides what counts as a valid routing target without an explicit policy or user check.
  Evidence it was operative: Cowork-summary 2026-05-10 sewing-agent paragraph: "the agent flagged five items for Tom: ... (2) architecture-root tracking files were excluded as routing targets (agent judgment call)" — flagged in the report but not asked-about; framed as agent autonomy with the user merely informed.
  Why it was unstated: Agent-judgment-call language naturalizes the boundary decision as routine engineering; the alternative (every exclusion requires user approval) would be impractical at the agent's design level. But it surfaces an unexamined autonomy boundary — the line between "engineering decision the agent makes" and "policy decision Tom should approve" is not specified.
  Type: methodological / governance
  Related decisions: DECISION-019 (sewing agent), DECISION-018 (specialist agents general autonomy), PRESUMPTION-130 (threshold definitions), PRESUMPTION-131 (this), ASSUMPTION-074 (specialist autonomy heuristics)
  Testability: testable via process (audit how many "agent judgment calls" sewing agent makes per run; compare against tradition-specialist autonomy levels; specify a routing-target inclusion/exclusion policy and check whether agent judgment aligns)
  Risk if wrong: Low-Medium — if routing-target choices systematically mis-cover important architectural files, the connectivity metric becomes biased toward what the agent decided to count; the bias compounds with PRESUMPTION-130 threshold-definition concern.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-131
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-10 sewing-agent flag #2 framing as an autonomous boundary-setting event treated as routine.
    Current status: UNTESTED

PRESUMPTION-132:
  Date surfaced: 2026-05-10
  Statement: [inferred] Three new bridge notes in the new `synthesis/` folder (Kastrup×McGilchrist, Hoffman×Levin, Carroll×Hoffman) constitute valid cross-tradition synthesis worth keeping in the architecture — agent-generated synthesis content is presumed valid without an explicit human-review trigger; the bridges are treated as durable artifacts even though no review pathway exists for them.
  Evidence it was operative: Cowork-summary 2026-05-10 sewing-agent paragraph lists "3 bridge notes written in a new `synthesis/` folder" alongside operational outputs; no review trigger named in "What's Next" or "For Morning Discussion"; "Files Created or Modified" lists each bridge as NEW FILE without flagging review need.
  Why it was unstated: The novelty of the synthesis/ folder + the prestige of cross-tradition bridge notes naturalize the artifacts as valuable; the absence of a review pathway becomes invisible against the visibility of the artifacts themselves. Compare with PRESUMPTION-024 (selection effect on FINDING-011a) — the same shape of "agent-generated cross-tradition signal treated as durable architecture" at a new layer.
  Type: epistemic / methodological
  Related decisions: PRESUMPTION-024 (selection effect on FINDING-011a), PRESUMPTION-014 (cross-tradition signal validity), PRESUMPTION-020 (AI synthesis bias profile), PRESUMPTION-074 (specialist-recognition reliability), DECISION-019 (sewing agent)
  Testability: testable empirically (audit the bridges for substantive accuracy via human review; compare against tradition-specialist proposals for cross-tradition signal quality; check whether agent-generated bridges differ systematically from specialist-generated bridges)
  Risk if wrong: Medium — if agent-generated bridges contain substantive errors but accumulate as durable architecture, the synthesis/ folder becomes a vector for the same class of risk as PRESUMPTION-024 at a new layer; long-tail accumulation could distort the cross-tradition signal landscape.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-132
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-10 sewing-agent paragraph treating bridges as Files-Created without review-trigger discussion.
    Current status: UNTESTED

PRESUMPTION-133:
  Date surfaced: 2026-05-10
  Statement: [inferred] The "documentation-only approach is not converging" framing for Chrome-MCP failures presumes that a programmatic fix would converge — the contrast is asserted without empirical evidence that the alternative remediation path (a programmatic `pre-scrape-ensure-normal-window` step) would actually converge against the same root cause; "not converging" is a description of the documentation-only outcome, not a comparison.
  Evidence it was operative: Cowork-summary 2026-05-10 "What's Next" item 8: "Chrome-MCP 'normal windows' error is now reproducible 3 consecutive mornings (chat-scrape) + has caused 4+ consecutive evening sync failures; documentation-only approach is not converging." Implicit contrast with a programmatic fix; no evidence that the programmatic fix would converge given that this evening's failure mode (sign-in-redirect) is auth-state, not window-state.
  Why it was unstated: Treating "not converging" as a reason to switch strategies is intuitively correct, but the comparison case (programmatic fix would converge) is the unstated half of the inference and was not examined. The sign-in-redirect failure mode that emerged this evening is direct counter-evidence — the programmatic window-fix wouldn't have addressed today's actual failure mode at all.
  Type: methodological / empirical
  Related decisions: PRESUMPTION-122 (documentation-as-fix), PRESUMPTION-125 (no severity ladder), ASSUMPTION-101 (Chrome-MCP environment-state attribution), ASSUMPTION-105 (user-privacy login prohibition), PRESUMPTION-134 (independent-vs-coextensive failure surfaces)
  Testability: testable empirically (deploy the programmatic pre-scrape-ensure-normal-window step; audit recurrence over N≥4 weeks; check whether the sign-in-redirect failure mode persists independently)
  Risk if wrong: Medium — if the programmatic fix doesn't converge against the deeper auth-state failure, switching strategies adds engineering cost without solving the underlying problem; today's evening failure already provides one data point against the convergence claim.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-133
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-10 "What's Next" item 8 framing of switch-strategies argument with implicit unsupported counterfactual.
    Current status: UNTESTED

PRESUMPTION-134:
  Date surfaced: 2026-05-10
  Statement: [inferred] The cowork-to-chat sync delivery failure mode "alternating between" the two HIGH SYSTEMIC-RISK layers (PRESUMPTION-121 chat-scrape Chrome-MCP-diagnostic + PRESUMPTION-125 cowork-to-chat-sync no-severity-ladder) presumes these are independent failure surfaces — but both rely on the same infrastructure stack (Chrome MCP + claude.ai login state), suggesting a common root cause that the alternation framing obscures.
  Evidence it was operative: Cowork-summary 2026-05-10 DELIVERY STATUS block: "The failure mode has now alternated between the two HIGH SYSTEMIC-RISK layers flagged in today's 15c run (PRESUMPTION-121 chat-scrape Chrome-MCP-diagnostic layer and PRESUMPTION-125 cowork-to-chat-sync no-severity-ladder layer)" — the alternation is named without questioning whether the two layers are actually independent.
  Why it was unstated: Naming the layers as separate cluster identifiers (PRESUMPTION-121 and PRESUMPTION-125) reifies their separateness in language; the underlying infrastructure dependency becomes invisible against the analytical convenience of the cluster names. This is a familiar shape: cluster-naming generates apparent decomposition where the substrate may be unitary.
  Type: epistemic / structural
  Related decisions: PRESUMPTION-121 (external-LLM diagnostic uptake), PRESUMPTION-125 (no severity ladder), ASSUMPTION-105 (user-privacy login prohibition), ASSUMPTION-101 (Chrome-MCP environment-state), ASSUMPTION-108 (DECISION-027 scope extension), ASSUMPTION-109 (cowork-to-chat sync standalone DECISION)
  Testability: testable empirically (root-cause analysis of all 5 consecutive failures; check whether a single fix at the auth/window-state intersection eliminates both layers; audit whether the two cluster identifiers refer to two distinct substrates or one)
  Risk if wrong: Medium-High — if the two clusters are coextensive at the infrastructure layer, treating them as separate DECISION-canonization candidates (per ASSUMPTION-108 and ASSUMPTION-109) would generate two DECISIONs where one is appropriate; this is structurally similar to PRESUMPTION-036 (single-cluster framing obscures four root causes) in inverse: here, two-cluster framing may obscure one root cause.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-134
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-10 DELIVERY STATUS alternation-framing without substrate-independence audit.
    Current status: UNTESTED

PRESUMPTION-135:
  Date surfaced: 2026-05-10
  Statement: [inferred] The morning chat-scrape failing for the 3rd consecutive day (2026-05-08, 2026-05-09, 2026-05-10) reaches the same three-recurrence canonization threshold per ASSUMPTION-098 — but is presumed already-subsumed under the PRESUMPTION-121 cluster without an explicit subsumption rule; no separate canonization trigger was articulated for this third recurrence.
  Evidence it was operative: Cowork-summary 2026-05-10 morning-scrape paragraph: "This is now the third consecutive failed daily-walk chat-scrape (2026-05-08, 2026-05-09, 2026-05-10)" — the three-recurrence count is stated; ASSUMPTION-098's threshold is satisfied; no separate canonization is triggered (the failure is implicitly absorbed into PRESUMPTION-121's cluster identity).
  Why it was unstated: The PRESUMPTION-121 cluster name was newly assigned this morning, and the chat-scrape failure was the layer that surfaced it; the recurrence count of the failure itself is treated as cluster-membership rather than as a separate three-recurrence event. The implicit subsumption rule ("cluster membership absorbs recurrence count") was not articulated.
  Type: methodological / governance
  Related decisions: ASSUMPTION-098 (three-recurrence threshold), ASSUMPTION-108 (DECISION-027 scope extension trigger), PRESUMPTION-121 (Codex-style external-LLM diagnostic), PRESUMPTION-125 (no severity ladder), PRESUMPTION-134 (independent-vs-coextensive failure surfaces)
  Testability: testable via process (specify subsumption rules: when does a cluster-membership flag absorb the three-recurrence canonization trigger that its constituent failures would otherwise generate? audit whether the implicit absorption produces under-canonization)
  Risk if wrong: Medium — if cluster-membership absorbs the three-recurrence trigger, multiple cluster-failures could fail to escalate independently even when their substrates differ; if it doesn't absorb, three concurrent canonizations may pile up artificially.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-135
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-10 morning-scrape recurrence count being stated without separate canonization trigger.
    Current status: UNTESTED

PRESUMPTION-136:
  Date surfaced: 2026-05-10
  Statement: [inferred] Two HIGH-urgency DECISION canonization triggers firing on the same day can both be resolved within the same week (week-carrying-capacity for DECISION work) — capacity is presumed without consultation/availability check; the cowork-summary frames both as "this week" actionable without discussing how many DECISIONs Tom can write in a week or whether DECISION-026 (which is also still undrafted) competes for the same week.
  Evidence it was operative: Cowork-summary 2026-05-10 "What's Next > This week (priority order)" lists three DECISION canonizations as priority items 1, 2, 3 — DECISION-026 (Wright/Rohr), DECISION-027 (scope extension), and standalone cowork-to-chat sync DECISION — without discussing whether three DECISIONs are achievable in a week. "For Morning Discussion" item 2 also frames both today-fired triggers as candidates for same-week canonization.
  Why it was unstated: Sequential-list framing naturalizes "all of these are this week" as if each were independent; week-carrying-capacity for DECISION-canonization work has not been measured. The historical baseline (DECISION-026 is still undrafted after weeks of being framed as URGENT) is direct counter-evidence to the carrying-capacity presumption.
  Type: operational / methodological
  Related decisions: ASSUMPTION-108 (DECISION-027 scope extension URGENT), ASSUMPTION-109 (cowork-to-chat sync standalone DECISION), DECISION-026 (Wright/Rohr addition undrafted), ASSUMPTION-112 (SELF-MEASUREMENT cluster)
  Testability: testable empirically (track DECISION-canonization throughput per week over N≥6 weeks; audit whether multiple-DECISION weeks produce DECISION-quality regression; compare URGENT-but-not-shipped lag time vs. canonization-time)
  Risk if wrong: Medium — if week-capacity is overestimated, all three DECISIONs slip to next week and the "URGENT" framing loses force; the SELF-MEASUREMENT (Goodhart) cluster (ASSUMPTION-112) extends here as throughput-language applied to canonization work itself.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-136
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-10 "This week (priority order)" sequential-list framing without capacity-analysis.
    Current status: UNTESTED

PRESUMPTION-137:
  Date surfaced: 2026-05-10
  Statement: [inferred] 5 "first-ever" Rohr (×2) and Wright (×3) pendings carry distinctive epistemic weight requiring meta-level (DECISION-026) accept/defer before standard pending-proposals workflow — "first-ever" is presumed to operate as a decision gate, but the system has previously had first-ever events (first-Wolfram, first-Levin pendings) that did not require meta-level canonization before review.
  Evidence it was operative: Cowork-summary 2026-05-10 "For Morning Discussion" item 1 frames the choice as "standard workflow vs. canonize-DECISION-026-first" — the meta-level option is treated as a live alternative on the strength of "first-ever" framing alone, without examining historical precedent for first-ever pending proposals from previously-uncanonized traditions.
  Why it was unstated: The "first-ever" framing carries intuitive epistemic weight (uniqueness as significance), and the simultaneous arrival of 5 proposals from 2 new traditions is unusual enough to suggest meta-level handling without historical comparison. PRESUMPTION-128 names the competing presumption (workflow accommodates without canonization); PRESUMPTION-137 names the competing presumption (canonization is required because first-ever).
  Type: epistemic / governance
  Related decisions: DECISION-026 (Wright/Rohr addition), ASSUMPTION-111 (blocking effect), PRESUMPTION-128 (workflow accommodation — competing presumption)
  Testability: testable empirically (audit historical "first-ever" tradition-specialist pending proposals; compare canonize-first vs. review-first outcomes; check whether first-ever framing is sufficiently distinctive to warrant a separate workflow)
  Risk if wrong: Low-Medium — competes with PRESUMPTION-128 (workflow accommodates not-yet-canonized traditions); if first-ever framing is not a decision gate, the meta-level review is unnecessary delay; if it is, treating non-first-ever pendings the same way is a process error. Note: PRESUMPTION-137 and PRESUMPTION-128 are explicit competing presumptions on the same decision-ordering question — one of them must be wrong.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-137
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-10 "For Morning Discussion" item 1 framing meta-level review as live alternative on first-ever weight alone.
    Current status: UNTESTED

PRESUMPTION-138:
  Date surfaced: 2026-05-10
  Statement: [inferred] Three scheduled runs still in flight at evening-sync time (C282 wiki-agent daily run, Morning system health, Bosco archive heartbeat) will complete overnight without intervention — extrapolated from yesterday's behavior; no per-task verification step is named, and the cowork-summary's "expected overnight completion" framing presumes that historic-completion-rate translates to current-completion-likelihood.
  Evidence it was operative: Cowork-summary 2026-05-10 "What's Next > Tonight (still in flight)" lists three running tasks with the stem "expected overnight completion" — phrasing carries probabilistic confidence not backed by per-task verification.
  Why it was unstated: Three of three scheduled runs from prior evenings did complete overnight; the inductive jump to "this set will too" is small enough not to require explicit checking. But it is the same shape of inference flagged in PRESUMPTION-124 (per-task evidence privileged over cross-task) at a different layer — extrapolating per-task historic behavior to current state without verification.
  Type: operational / empirical
  Related decisions: ASSUMPTION-103 (per-task fire-rate evidence), PRESUMPTION-124 (per-task vs. cross-task), ASSUMPTION-080 (daemon-link-count regression candidate), ASSUMPTION-092 (master-narrative-gap attribution)
  Testability: testable empirically (verify completion of all three tasks tomorrow morning; audit whether "expected overnight completion" produces accurate predictions over N≥4 weeks; track which task-types break the pattern when they do)
  Risk if wrong: Low — if any of the three tasks stalls overnight, the morning briefing inherits the stall without prior warning; this is not a high-stakes failure mode but it does reduce the briefing's calibration. The wiki-orchestrator daily-run gap (still UNKNOWN per ASSUMPTION-103/PRESUMPTION-124) is the active example.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-138
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-10 "Tonight (still in flight)" extrapolation language without per-task verification step.
    Current status: UNTESTED

PRESUMPTION-139:
  Date surfaced: 2026-05-10
  Statement: [inferred] The sewing-agent-recommended one-time backlink-injection pass will make the connectivity metric "sensitive" — sensitivity is asserted as the corrected post-state without specifying the threshold that would qualify the metric as sensitive (orphan-rate < X%? connected-rate > Y%? variance-detectability above Z?), and without examining whether the proposed fix at all changes the connectivity-metric design itself.
  Evidence it was operative: Cowork-summary 2026-05-10 sewing-agent paragraph item (1): "the vault is overwhelmingly disconnected from the [[wikilink]] graph (766/785 orphans) — the connectivity metric will be insensitive without a one-time backlink-injection pass." The framing presumes "sensitive" is binary (sensitive vs. insensitive) without an operational definition. "What's Next" item 7 reiterates the recommendation without specifying success criteria.
  Why it was unstated: The connectivity-metric design is the agent's own (per PRESUMPTION-130); diagnosing it as "insensitive" is a self-assessment whose post-fix threshold for sensitivity is not articulated. The sewing-agent's first-run authority (per PRESUMPTION-131) makes the diagnosis-and-prescription chain feel routine.
  Type: methodological / metrics
  Related decisions: PRESUMPTION-130 (sewing agent threshold definitions), PRESUMPTION-131 (agent-judgment-call autonomy), ASSUMPTION-110 (canonical inaugural baseline)
  Testability: testable empirically (specify sensitivity threshold; conduct backlink-injection pass; re-measure connectivity baseline; audit whether the metric actually distinguishes weekly trajectories at the new baseline; check whether post-fix metric design needs re-examination)
  Risk if wrong: Low-Medium — if the metric is still insensitive after the proposed fix, the recommended one-time fix becomes operational debt without improving signal quality; if sensitivity is over-claimed pre-emptively, weekly variation may be over-interpreted.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-139
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-10 sewing-agent insensitive-vs-sensitive binary framing without operational threshold.
    Current status: UNTESTED

PRESUMPTION-140:
  Date surfaced: 2026-05-12
  Statement: [inferred] The "active watch list now empty for the first time since 2026-05-05" milestone is treated as an unambiguously positive architectural signal, presumed comparable to other first-ever firsts (first sewing agent run, first Rohr/Wright pending, first 14a/14b cycle, etc.). The framing does not consider that an empty watch list is the *absence* of state, not the *presence* of something — empty could also indicate diagnostic blind spots: items aren't being added because the proposal-intake-to-CHECK criterion is too narrow, or because Agent 16's intake heuristics are missing valid candidates.
  Evidence it was operative: Cowork-to-chat summary 2026-05-12 opening box bullet 1 and paragraph 1 frame "active watch list now empty for the first time since 2026-05-05" as a closing-headline structural event without an audit of intake-criterion adequacy. "For Morning Discussion" item 1 treats the empty list as a moment of architectural reflection on cadence but not on intake.
  Why it was unstated: Absence-as-success is a common semantic shortcut; the inverse interpretation (absence = under-coverage) requires the auditor to actively imagine missing items rather than describe present ones.
  Type: epistemic / methodological
  Related decisions: DECISION-022 (Agent 16 deferred-action-monitor), ASSUMPTION-113 (markup-anchor method canonization), ASSUMPTION-114 (cadence validated by WATCH-001), PRESUMPTION-069 (silence-not-tracked / absence-as-event), PRESUMPTION-042 (null-output framed as accurate)
  Testability: testable empirically (audit Agent 16's intake heuristic against the prior 30 days of approved/deferred proposals — did any meet ambiguous transcript-availability conditions that should have triggered a CHECK?); testable via process (compare watch-list-emptiness durations across longer time windows)
  Risk if wrong: Medium — if the intake criterion is too narrow, valuable CHECK items are being silently lost; the milestone framing reinforces complacency about coverage.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-140
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-12 "first empty active watch list" framing as a celebratory structural event without an intake-coverage audit. Joins PRESUMPTION-069 (silence-not-tracked) cluster.
    Current status: UNTESTED

PRESUMPTION-141:
  Date surfaced: 2026-05-12
  Statement: [inferred] The framing of PROP-2026-05-12-001 as "the cleanest single-page public framing of the Hoffman program in 2026" presumes that single-page consolidation is a virtue per se — that a more-consolidated, fewer-page articulation of a research program carries more architectural weight than equivalent content distributed across multiple sources. No criteria are surfaced for when distributed articulation might be epistemically preferable (e.g., for testing whether the consolidation is post-hoc rationalization vs. organic development of the program).
  Evidence it was operative: Cowork-to-chat summary 2026-05-12 paragraph 2 and "For Morning Discussion" item 2 use "cleanest single-page public framing" as an unmarked superlative without comparison to multi-page Hoffman sources (HOMeHOPe, MBS, Edge.org prior responses, podcast appearances).
  Why it was unstated: Compactness is a default scholarly virtue (Occam-flavored); the question of when distribution might be epistemically preferable rarely surfaces unless adjudicating a specific tension.
  Type: normative / epistemic
  Related decisions: ASSUMPTION-115 (PROP-2026-05-12-001 cleanest-public-framing), PRESUMPTION-119 (single-axis leverage measurement), PRESUMPTION-116 (superlative without normalization), ASSUMPTION-100 (Saturday Wolfram highest-leverage signal — comparable framing)
  Testability: testable via literature (research-program-formalism literature on compactness-vs-distribution as quality signals); testable empirically (compare downstream signal-production rate from "cleanest single-page" proposals vs. multi-source proposals over 30 days post-review)
  Risk if wrong: Low-Medium — if compactness is being conflated with maturity, recently-consolidated programs are over-weighted relative to organically-distributed ones; the proposal-intake pipeline may have a publication-style bias.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-141
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-12 paragraph 2 + "For Morning Discussion" item 2 "cleanest single-page" framing as an unmarked virtue claim. Recurrence of PRESUMPTION-116 / PRESUMPTION-119 superlative-without-normalization pattern at a third layer (content-architecture import claim).
    Current status: UNTESTED

PRESUMPTION-142:
  Date surfaced: 2026-05-12
  Statement: [inferred] PRS-CANDIDATE-01's reframing of Hoffman's Law as "methodological precondition rather than competing alternative" to physics-side TOEs (Arkani-Hamed, Wolfram, Carroll) is presumed acceptable to those traditions as a one-way reframing — the cowork summary does not pose the inverse check (would those traditions accept being placed pre-foundationally to a Hoffman-grounded layer?) before accepting the reframing as structurally significant for the master network. The downstream consequence ("changes how cross-tradition signals to those three traditions are read going forward") is asserted without exploring the alternative that those traditions might reject the placement entirely.
  Evidence it was operative: Cowork-to-chat summary 2026-05-12, paragraph 2 and "For Morning Discussion" item 2 describe the reframing as "structurally significant" and "if accepted, it changes how cross-tradition signals to Arkani-Hamed/Wolfram/Carroll are read going forward" without flagging the inverse-acceptance question. Agent 16 itself is silent on the question.
  Why it was unstated: When a single tradition reinterprets the relationship of other traditions to itself, the system tends to read that as the proposal-tradition's contribution rather than as a contested cross-tradition claim. The C2A2 architecture's specialist-output norms (PRESUMPTION-074 cluster) treat such reframings as primary signals.
  Type: epistemic / methodological
  Related decisions: ASSUMPTION-116 (PRS-CANDIDATE-01 reframes Arkani-Hamed/Wolfram/Carroll as pre-foundational), PRESUMPTION-074 (specialist-recognition reliability — SYSTEMIC-RISK), PRESUMPTION-089 (recursive-specialist-reading), PRESUMPTION-100 (specialist output bears on ASSUMPTION but no feedback loop), PRESUMPTION-002 (Thousand Brains transfer — CRITICAL transfer-validity)
  Testability: testable empirically (run Arkani-Hamed / Wolfram / Carroll specialist re-reads under the reframed lens; check whether those specialists would themselves frame their tradition as "pre-foundational to Hoffman" or as "peer to Hoffman"); testable via literature (philosophy-of-physics on TOE-hierarchy claims)
  Risk if wrong: Medium-High — extends PRESUMPTION-074's specialist-recognition SYSTEMIC-RISK to a new pattern (one-way cross-tradition reframing accepted as architectural commitment); if Arkani-Hamed/Wolfram/Carroll specialists reject pre-foundational placement, the resulting cross-tradition signals become noise rather than signal.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-142
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-12 paragraph 2 + "For Morning Discussion" item 2 framing of "if accepted, it changes how cross-tradition signals are read" without an inverse-acceptance check. Joins PRESUMPTION-074 specialist-recognition cluster and PRESUMPTION-002 cross-tradition transfer-validity cluster.
    Current status: UNTESTED

PRESUMPTION-143:
  Date surfaced: 2026-05-12
  Statement: [inferred] Agent 16's framing of today's WATCH-001 resolution as "first end-to-end resolution cycle" presumes that one successful resolution validates the agent's overall protocol — the maturity claim ("watch list is now empty") sits on a single data point on a weekly-cadence agent. No criteria are surfaced for what would constitute sufficient evidence of protocol maturity (N=3? N=5?) before generalization is warranted; ASSUMPTION-113's recommendation to canonize the markup-anchor method as default-for-transcript-availability-watches similarly rests on a single application.
  Evidence it was operative: Agent 16 run summary 2026-05-12 closing line: "This was Agent 16's first end-to-end resolution cycle — watch list is now empty." Cowork-to-chat summary 2026-05-12 "For Morning Discussion" item 1 considers cadence-and-method but does not surface the single-data-point limitation.
  Why it was unstated: Successful first runs of an agent's protocol tend to be framed as proof of concept; the implicit upgrade to "protocol works" rather than "protocol worked once" rarely surfaces unless explicitly audited.
  Type: epistemic / methodological
  Related decisions: ASSUMPTION-113 (markup-anchor method canonization), ASSUMPTION-114 (cadence validated), DECISION-022 (Agent 16 introduction), PRESUMPTION-040 (structural verification as operational readiness), PRESUMPTION-095 (Phase-2 zero-result as exhaustion not method-failure)
  Testability: testable empirically (track N future CHECK dispositions before declaring method-and-cadence validated; audit how often "first end-to-end" framings are followed by an inverse-result second run); testable via process (literature on operational-readiness thresholds for new agents/tools)
  Risk if wrong: Medium — if a second CHECK fails with the same method, ASSUMPTION-113's canonization recommendation has premature epistemic weight; if cadence fails on an item that needed shorter-than-weekly attention, ASSUMPTION-114 is similarly over-claimed.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-143
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from Agent 16 run summary 2026-05-12 closing line + cowork-summary 2026-05-12 "For Morning Discussion" item 1 as a single-data-point-validation claim. Joins PRESUMPTION-040 operational-readiness cluster.
    Current status: UNTESTED

PRESUMPTION-144:
  Date surfaced: 2026-05-12
  Statement: [inferred] The SUMMA_EXPLORER_IMPROVEMENTS Vault Linker Agent design's seven-category reference taxonomy (wikilink, summa-day, summa-question, thinker-mention, prs-ref, scripture, cross) is presumed complete — no audit is mentioned for whether other reference kinds exist in the vault (bibliographic citations, image references, hash-anchored sub-sections, footnotes, embedded URLs, file-path references, code-block references, table cell references). The closed-category-list framing presumes the seven types capture the full reference taxonomy at the resolution the linker_agent will operate on.
  Evidence it was operative: Cowork-to-chat summary 2026-05-12 paragraph 3: "continuous prowler resolving seven kinds of cross-file references (wikilink, summa-day, summa-question, thinker-mention, prs-ref, scripture, cross) into `vault/refs/cross_links.json`" framed as a specification without an audit step.
  Why it was unstated: When a design enumerates a list of types, the enumeration itself tends to feel exhaustive at the moment of specification; categories outside the enumerated set become visible only when concrete files surface uncategorized references.
  Type: methodological / architectural
  Related decisions: PRESUMPTION-070 (Stump framework decomposability), PRESUMPTION-080 (cross-discipline operational-primitive transfer), PRESUMPTION-118 (DECISION-027 unify-vs-split reversible)
  Testability: testable empirically (parse a sample of vault files for reference patterns not matching the seven enumerated kinds; audit cross_links.json once produced for missing-reference complaints); testable via literature (cross-reference taxonomy completeness in document-link systems)
  Risk if wrong: Low-Medium — if categories are missing, the linker_agent silently under-counts cross-references; the Sociogram tab depending on this layer would inherit the gap without surfacing the absence as a UI signal.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-144
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-12 paragraph 3 Vault Linker Agent enumerated-category specification as a closed-category claim without an audit step.
    Current status: UNTESTED

PRESUMPTION-145:
  Date surfaced: 2026-05-12
  Statement: [inferred] The chat-scrape sign-in barrier (6 consecutive days failed) is being framed as a token-based-delegation problem to be solved by workflow redesign — the framing presumes the issue is fundamentally a delegation question. The alternative — re-examining whether the chat-scrape mechanism *should exist at all*, replacing it with file-based handoff via the workspace folder (both directions) — is mentioned as a parenthetical "morning walk" question rather than as a co-equal candidate redesign. The presumption is that the current chat-scrape sync architecture is load-bearing and worth preserving, not that the architecture itself is the failure point.
  Evidence it was operative: Cowork-to-chat summary 2026-05-12 "For Morning Discussion" item 6: "Suggested first step: enumerate the candidate connector/OAuth options available against the actual claude.ai surface, even just to scope what 'token-based delegation' would look like operationally. The morning walk is a good place to think about whether the wiki-side tooling should pivot to a different sync mechanism entirely (file-based handoff via the workspace folder both ways, rather than scraping the chat UI)." The file-based alternative is the closing aside rather than the framing.
  Why it was unstated: The chat-scrape mechanism has been built up incrementally over weeks; sunk-cost framing makes the "redesign for delegation" path feel more natural than the "discard the mechanism entirely" path.
  Type: structural / methodological
  Related decisions: ASSUMPTION-118 (token-based delegation workflow redesign), PREMISE-015 (user-privacy / no-password-delegation), ASSUMPTION-109 (cowork-to-chat sync standalone DECISION candidate), PRESUMPTION-125 (4th-consecutive cowork-to-chat sync failure), PRESUMPTION-134 (substrate-decomposition for failure-surface alternation)
  Testability: testable empirically (scope both candidate redesigns in parallel; compare engineering cost, residual failure-modes, and downstream compatibility); testable via process (audit prior workflow redesigns that addressed a delegation question without re-examining mechanism-existence)
  Risk if wrong: Medium-High — if the chat-scrape mechanism itself is the wrong architecture for the goal (capturing morning-walk Chat context), spending engineering effort on token-based delegation locks in the wrong primitive; the file-based-handoff alternative would obviate the entire 6-consecutive-failure surface.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-145
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-12 "For Morning Discussion" item 6 framing where token-delegation is the primary candidate and file-based-handoff is parenthetical. Joins PRESUMPTION-134 substrate-decomposition cluster.
    Current status: UNTESTED

PRESUMPTION-146:
  Date surfaced: 2026-05-12
  Statement: [inferred] The Loughran-tradition papers folder (25 papers, manifest, helper scripts) is treated as a content-architecture artifact even though it has not yet been processed into PRS triplets or integrated into the master network — the on-disk presence is presumed to precede natural-cadence processing without an explicit processing-trigger. No timeline or trigger is articulated for when these 25 papers will be ingested into the C2A2 specialist pipeline.
  Evidence it was operative: Cowork-to-chat summary 2026-05-12 paragraph 4: "The Loughran-tradition papers folder was populated: all 25 papers... are now on disk under `wiki/traditions/loughran/papers/` — 23 PDFs + 2 DOCX..." listed under "What Was Accomplished Today" without any "next: ingest into specialist pipeline" follow-up step. Files-modified list confirms presence without processing.
  Why it was unstated: On-disk presence has a long C2A2 history of preceding cadenced processing (Levin/Friston scheduled-task slots); the implicit cadence is treated as load-bearing without surfacing the trigger.
  Type: methodological / structural
  Related decisions: PRESUMPTION-128 (workflow accommodates not-yet-canonized traditions), ASSUMPTION-111 (Wright/Rohr first-ever pendings blocking N=13 expansion), PRESUMPTION-127 (off-cadence specialist filings as routine), ASSUMPTION-091 (off-cadence treated as on-cadence)
  Testability: testable empirically (track processing-latency from on-disk presence to first PRS triplet over N≥3 prior tradition additions); testable via process (audit specialist-pipeline trigger conditions — is "papers on disk" sufficient to trigger ingest, or is a DECISION-NNN required?)
  Risk if wrong: Medium — if the Loughran tradition needs a DECISION-NNN before specialist ingest (analogous to ASSUMPTION-111's Wright/Rohr blocking effect), the on-disk papers represent latent technical debt; if it doesn't need one, the inconsistency with Wright/Rohr surfaces a process-asymmetry question.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-146
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-12 paragraph 4 Loughran-papers-folder listing as accomplishment without a processing-trigger step. Joins PRESUMPTION-128 workflow-accommodation cluster.
    Current status: UNTESTED

PRESUMPTION-147:
  Date surfaced: 2026-05-12
  Statement: [inferred] The "three structurally interesting events" segmentation in today's cowork summary (Agent 16 WATCH-001 resolution + Hoffman pending + Summa shipping) presumes that narrative event-discreteness corresponds to actual architectural state-changes — that the day's signal can be cleanly partitioned into N independent events whose union is the day's architectural delta. No criteria are surfaced for what makes an event "structurally interesting" vs. "operationally routine"; the count itself (three) is implicit in the framing rather than empirically derived.
  Evidence it was operative: Cowork-to-chat summary 2026-05-12 "What Was Accomplished Today" opening: "Three structurally interesting events:" followed by an enumerated 1/2/3 list. Other paragraphs (Loughran papers, Summa commentary reviewer, morning chat-scrape failure, EOD-cycle no-fire) are framed as background rather than event-tier.
  Why it was unstated: Narrative summarization rewards discreteness; the "three things happened" framing is a default rhetorical move that does not surface its own segmentation criterion.
  Type: epistemic / methodological
  Related decisions: PRESUMPTION-036 (single-cluster framing obscures root causes), PRESUMPTION-064 (narrative-surfacing-adequate), ASSUMPTION-104 (day-shape characterization), PRESUMPTION-129 (record-rate without normalization)
  Testability: testable empirically (cross-compare today's three-event framing against a 10-event flat enumeration of the same day's files-modified list; check whether the three-tier framing privileges some changes over others without surfacing the criterion); testable via process (audit narrative-segmentation patterns across N≥10 prior cowork summaries for consistency)
  Risk if wrong: Low-Medium — if the three-event framing systematically suppresses smaller-but-relevant architectural events, the downstream metric trajectories drift from the actual change-set; the changelog would inherit the gap.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-147
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-12 "Three structurally interesting events" framing as an unsourced narrative segmentation. Joins PRESUMPTION-036 single-cluster-framing cluster.
    Current status: UNTESTED

PRESUMPTION-148:
  Date surfaced: 2026-05-12
  Statement: [inferred] The pending proposals count growth (38 → 40 today) is recorded as a positive throughput signal (alongside other "+1/+2 today" deltas) without examining whether intake-rate is outpacing disposition-rate sustainably. The Goodhart cluster (PRESUMPTION-123 + ASSUMPTION-102 + ASSUMPTION-096, codified as ASSUMPTION-112 SELF-MEASUREMENT architectural pattern) applies to proposal-queue depth at least as directly as to lit-search cycle throughput — but the pattern is not surfaced for the proposal-pending metric.
  Evidence it was operative: Cowork-to-chat summary 2026-05-12 "Pipeline Status" line "Pending proposals: **40** (38 EOD 2026-05-11 + 1 new Hoffman + 1 Carroll re-queue from Agent 16)" treats the +2 delta as routine throughput; "What Was Accomplished Today" paragraph 1 notes "pending proposals count moved 38 → 40 today" as a positive accomplishment. The still-unresolved 5 Wright/Rohr pendings from 2026-05-10 (per ASSUMPTION-111) implicitly demonstrate growing pending-queue depth with no disposition-rate offset.
  Why it was unstated: The Goodhart pattern has been surfaced at the lit-search cycle layer (ASSUMPTION-112) but has not been generalized to other queue-depth metrics. The proposal-pending-count has historical precedent for growing without alarm (queue grew from ~10 to 40 across April-May).
  Type: methodological / metrics
  Related decisions: ASSUMPTION-112 (SELF-MEASUREMENT Goodhart cluster), PRESUMPTION-123 (throughput-as-success-metric), ASSUMPTION-111 (Wright/Rohr pendings blocking N=13 expansion), PRESUMPTION-091 (33-deep proposal queue framed as absorbable), PRESUMPTION-129 (record-rate without normalization)
  Testability: testable empirically (compute proposal intake-rate vs. disposition-rate over 30-day rolling windows; check whether the Goodhart concern from ASSUMPTION-112 applies symmetrically); testable via literature (queue-management literature on intake-vs-disposition balance in review pipelines)
  Risk if wrong: Medium — if the proposal queue is also a SELF-MEASUREMENT Goodhart instance, the system's celebration of "+2 today" is parallel to its celebration of "100% drained in one cycle" — both throughput-style signals that obscure whether substantive INCORPORATEs are happening downstream.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-148
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-12 Pipeline Status + paragraph 1 +2-today delta framing as positive throughput without intake-vs-disposition normalization. Generalizes ASSUMPTION-112 SELF-MEASUREMENT cluster to a third queue (proposal-pending-count) — joins PRESUMPTION-123 / PRESUMPTION-129 / ASSUMPTION-112 SELF-MEASUREMENT cluster as its third-layer recurrence.
    Current status: UNTESTED

PRESUMPTION-149:
  Date surfaced: 2026-05-12
  Statement: [inferred] Agent 16's "flag, do not unilaterally merge" norm on overlapping proposals (PROP-2026-04-21-002 Carroll/Singer re-queue may overlap with PROP-2026-05-08 Carroll Mindscape-351-Singer-utilitarianism) is presumed correct without surfacing criteria for when merge could be safely automated. The flag-not-merge default is articulated as agent autonomy bounds, but no decision rule is offered for distinguishing safely-mergeable overlap (same episode, same speakers, same topic) from substantively-different overlap (same episode, different angle, different PRS candidates).
  Evidence it was operative: Agent 16 run summary 2026-05-12: "Flag for Tom (logged in the run summary): the re-queued PROP-2026-04-21-002 may overlap with an existing pending item `2026-05-08_carroll_mindscape-351-singer-utilitarianism.md` covering the same Mindscape 351 episode. Agent 16 does not unilaterally merge — flagged for next review pass." The norm is stated as policy without elaboration of decision criteria.
  Why it was unstated: Agent-autonomy bounds tend to be set conservatively at first deployment; the question of "when could this be automated?" rarely surfaces until a flag accumulates evidence over multiple instances.
  Type: methodological / structural
  Related decisions: DECISION-022 (Agent 16 introduction), ASSUMPTION-113 (markup-anchor method canonization), ASSUMPTION-114 (cadence validated), PRESUMPTION-131 (architecture-root exclusion as agent judgment call), PRESUMPTION-040 (structural verification as operational readiness)
  Testability: testable empirically (track N future overlap-flag instances; audit how often Tom's review decision is "merge" vs. "keep separate"; if a stable pattern emerges, a decision rule may be inferable); testable via process (compare Agent 16's flag-not-merge norm against PRESUMPTION-131's architecture-root exclusion agent-autonomy precedent)
  Risk if wrong: Low-Medium — if the flag-not-merge norm is too conservative, Tom carries unnecessary review load on safely-mergeable overlaps; if too permissive (when automated), distinct PRS candidates risk getting merged into a single proposal.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-149
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from Agent 16 run summary 2026-05-12 "flag, do not unilaterally merge" policy as a stated norm without decision-criteria elaboration. Joins PRESUMPTION-131 agent-autonomy cluster.
    Current status: UNTESTED

Key event (2026-05-12 — Tuesday deferred-action-monitor first-resolution + Hoffman TOE-reframing pending + governance-trigger second-activation): Ten new presumptions surfaced on a Tuesday whose dominant operational signature was Agent 16's first end-to-end resolution cycle (WATCH-001 RESOLVED, active watch list empty for first time since 2026-05-05), the first Hoffman pending since the sewing-agent flag (PROP-2026-05-12-001 "Hoffman's Law" with TOE-reframing PRS candidate), Summa-side shipping plus SUMMA_EXPLORER_IMPROVEMENTS planning doc, and the 6th-consecutive failed evening cowork-to-chat delivery via sign-in-redirect. Today's ten presumptions cluster in five families. **(1) ABSENCE-AS-SUCCESS + SINGLE-DATA-POINT-VALIDATION cluster (NEW, 2 members)** — PRESUMPTION-140 (empty watch list as positive signal without intake-coverage audit; joins PRESUMPTION-069 silence-not-tracked cluster) and PRESUMPTION-143 (Agent 16 "first end-to-end" framing presumes one success validates protocol; joins PRESUMPTION-040 operational-readiness cluster). The cluster surfaces two unstated dependencies of today's first-resolution architectural moment. **(2) CROSS-TRADITION-REFRAMING-ASYMMETRY cluster (NEW, 2 members)** — PRESUMPTION-141 (single-page consolidation as virtue per se; recurrence of PRESUMPTION-116 / PRESUMPTION-119 superlative-without-normalization pattern at a third layer) and PRESUMPTION-142 (PRS-CANDIDATE-01's one-way Arkani-Hamed/Wolfram/Carroll reframing accepted without inverse check; joins PRESUMPTION-074 specialist-recognition SYSTEMIC-RISK cluster + PRESUMPTION-002 cross-tradition transfer-validity CRITICAL cluster). PRESUMPTION-142 is today's highest-risk item (Medium-High). **(3) DESIGN-TAXONOMY-CLOSEDNESS + AGENT-AUTONOMY-CRITERIA cluster (NEW, 2 members)** — PRESUMPTION-144 (Vault Linker seven-category taxonomy as closed without audit) and PRESUMPTION-149 (Agent 16 flag-not-merge norm without decision criteria). Both surface unstated dependencies in today's two design articulations (one specification, one operational policy). **(4) MECHANISM-EXISTENCE vs. MECHANISM-REDESIGN cluster (NEW, 1 member)** — PRESUMPTION-145 (chat-scrape barrier framed as token-delegation problem rather than mechanism-existence question; joins PRESUMPTION-134 substrate-decomposition cluster). PRESUMPTION-145 is the structural counterpart to ASSUMPTION-118's redesign mandate — surfacing that the redesign path is presumed to preserve the mechanism. **(5) NARRATIVE-SEGMENTATION + ON-DISK-AS-PROCESSED + GOODHART-RECURRENCE cluster (NEW, 3 members)** — PRESUMPTION-147 (three-event narrative segmentation without criteria), PRESUMPTION-146 (Loughran papers on-disk without processing-trigger), PRESUMPTION-148 (proposal-queue +2-today framing as third-layer recurrence of SELF-MEASUREMENT Goodhart cluster — generalizes ASSUMPTION-112 to a third queue). PRESUMPTION-148 is today's most actionable architectural item: the Goodhart pattern just confirmed at the lit-search cycle layer extends naturally to the proposal-pending-queue layer, and the system's failure to flag this at proposal-intake time is itself evidence of the recursive-self-observation gap. Today's 10-to-6 presumption-to-assumption ratio (1.67:1) is the new joint-record — exceeding the prior 1.5:1 high tied by 2026-04-27 / 2026-05-08 / 2026-05-09. The deferred-action-cycle + cross-tradition-reframing + governance-trigger character generates a higher-than-average density of unstated dependencies relative to stated commitments. Notable: today's PRESUMPTION-148 is the THIRD layer at which the SELF-MEASUREMENT Goodhart cluster has now recurred (ASSUMPTION-112 cycle-throughput layer + PRESUMPTION-129 REVISE-rate density layer + PRESUMPTION-148 proposal-queue layer), matching PRESUMPTION-074's specialist-recognition cluster as a multi-layer recurring SYSTEMIC-RISK pattern. 10 newly surfaced; 0 reconciled today (15a/15b/15c cycle status today uncertain per cowork summary); 10 newly QUEUED for next 15a/15b cycle. Lit-search queue at this moment: 16 items (6 new ASSUMPTIONs + 10 new PRESUMPTIONs).

Key event (2026-05-10 — Sunday first-Rohr/Wright pendings + sewing-agent first weekly + decision-governance trigger activation): Twelve new presumptions surfaced on a Sunday whose dominant operational signature was the first-ever Rohr (×2) and Wright (×3) pending proposals, the first weekly sewing-agent run, the second-consecutive clean lit-search drain, and the 5th-consecutive failed evening cowork-to-chat delivery (now via sign-in-redirect rather than the "normal windows" error). Today's twelve presumptions cluster in five families. **(1) DECISION-ORDERING-AND-COMPETING-PRESUMPTIONS cluster (NEW, 2 members)** — PRESUMPTION-128 (workflow accommodates not-yet-canonized traditions) and PRESUMPTION-137 (first-ever framing operates as decision gate) are explicit competing presumptions on the same accept/defer-vs-canonize-first ordering question; one must be wrong, and "For Morning Discussion" item 1 elicits Tom's input precisely because the system has not chosen between them. **(2) SUPERLATIVE-WITHOUT-NORMALIZATION recurrence (extends 2026-05-09 PRESUMPTION-116)** — PRESUMPTION-129 (record REVISE rate without normalization) is the SECOND layer at which the PRESUMPTION-116 superlative-without-normalization pattern has now recurred (densest-cycle layer + REVISE-rate-density layer) within 24 hours — joining PRESUMPTION-121's external-LLM-uptake recurrence as today's second within-24-hours second-layer pattern. **(3) NEW-METRIC-DESIGN-AUTONOMY cluster (NEW, 3 members)** — PRESUMPTION-130 (sewing-agent threshold definitions accepted as canonical), PRESUMPTION-131 (architecture-root exclusion as agent judgment call), PRESUMPTION-132 (synthesis/ folder bridges as durable architecture without review trigger). The cluster surfaces three unstated autonomy-and-validation presumptions beneath the sewing-agent's first weekly run; PRESUMPTION-132 specifically extends PRESUMPTION-024's selection-effect cluster to a new layer (agent-generated cross-tradition synthesis content). **(4) FAILURE-MODE INFRASTRUCTURE-DEPENDENCY cluster (NEW, 3 members)** — PRESUMPTION-133 (programmatic-fix would converge — implicit unsupported counterfactual), PRESUMPTION-134 (PRESUMPTION-121 + PRESUMPTION-125 alternation presumes independent failure surfaces with shared substrate), PRESUMPTION-135 (cluster-membership absorbs three-recurrence canonization trigger). The cluster surfaces three connected gaps in today's failure-mode reasoning around Chrome MCP / claude.ai login state. **(5) DECISION-WORK-CAPACITY + PER-TASK-EVIDENCE-RECURRENCE + METRIC-SENSITIVITY-GAP** — PRESUMPTION-136 (week-carrying-capacity for three URGENT DECISIONs presumed without examination), PRESUMPTION-138 (three in-flight tasks presumed to complete overnight without per-task verification — extends PRESUMPTION-124 pattern), PRESUMPTION-139 (sewing-agent metric-sensitivity threshold not specified). Today's 12-to-9 presumption-to-assumption ratio (1.33:1) is moderate — below 2026-04-27 / 2026-05-08 / 2026-05-09 record (1.5:1) but above 2026-05-05 (1.22:1). Today is notable for THREE second-layer-recurrences-within-24h: PRESUMPTION-129 extends PRESUMPTION-116 (superlative without normalization, second layer); PRESUMPTION-138 extends PRESUMPTION-124 (per-task vs. cross-task, second layer); the SELF-MEASUREMENT (Goodhart) cluster (ASSUMPTION-112 + PRESUMPTION-129 today) reaches its second consecutive cycle. Notable: PRESUMPTION-128 and PRESUMPTION-137 are the first explicit competing-presumptions pair in the registry (both refer to the same decision-ordering question with opposite default policies); their joint surfacing is the day's most actionable architectural item for tomorrow's "For Morning Discussion" item 1. 12 newly surfaced; 0 reconciled today (today's 15c cycle was on yesterday's items, not today's); 12 newly QUEUED for next 15a/15b cycle. Lit-search queue at this moment: 21 items (9 new ASSUMPTIONs + 12 new PRESUMPTIONs).

---

## Status Summary

Total presumptions surfaced: 115 (54 from 2026-04-20 Run 1 + 6 from 2026-04-20 supplementary Run 2 + 9 from 2026-04-21 + 11 from 2026-04-26 + 12 from 2026-04-27 + 11 from 2026-05-05 + 12 from 2026-05-08)

By type:
  Methodological: 38 (prior 32 + PRESUMPTION-082, 084, 086, 087; partial PRESUMPTION-081, 083)
  Epistemic: 26 (prior 21 + PRESUMPTION-081, 088, 089, 091; partial PRESUMPTION-085)
  Structural: 6 (no change)
  Normative: 6 (no change; PRESUMPTION-083 partial)
  Architectural: 20 (prior 18 + PRESUMPTION-083, 092)
  Empirical: 4 (prior 3 + PRESUMPTION-090)
  Scaling: 1 (PRESUMPTION-073)

By risk level:
  Critical: 2 (PRESUMPTION-002, 024)
  High: 7 (no change)
  Medium to High: 18 (prior 13 + PRESUMPTION-083, 084, 085, 087, 088, 089)
  Medium: 41 (prior 37 + PRESUMPTION-081, 082, 086, 091)
  Low to Medium: 18 (prior 16 + PRESUMPTION-090, 092)
  Low: 5 (PRESUMPTION-023, 028, 034)
  (Normative-extension items PRESUMPTION-066 and PRESUMPTION-067 classified at Medium)

By status (2026-04-21):
  PARTIALLY-CHALLENGED: 11 (PRESUMPTION-001, 002, 003, 004, 005, 008, 009, 010, 012, 013, 014)
  CHALLENGED: 3 (PRESUMPTION-006, 007, 011)
  STRONGLY-CHALLENGED: 2 (PRESUMPTION-035, 041 per 2026-04-18 15c cycle)
  UNTESTED: 55 (prior 46 + PRESUMPTION-061, 062, 063, 064, 065, 066, 067, 068, 069 from 2026-04-21)
  (PARTIALLY-CHALLENGED + CHALLENGED + STRONGLY-CHALLENGED + UNTESTED = 11 + 3 + 2 + 55 = 71; reconciles against total of 69 with 2 items counted in two status buckets during lit-search transitions. Carry-forward discrepancy — 1 previously tracked — now at 2 for reconciliation next 15c cycle.)

Key event (2026-04-16): Six new presumptions surfaced. PRESUMPTION-029 extends the epistemic-validation-gap cluster (024, 020, 021, 014) to the multi-subagent batch case — a 5-findings-in-one-day surge that was not examined for subagent-correlation inflation. PRESUMPTION-030 surfaces an 8-day version-control gap as potentially systemic rather than cosmetic. PRESUMPTION-031 questions the specialist-rotation schedule's empirical coverage. PRESUMPTION-032 aggregates the morning-handoff chain's intent-capture failures across two channels (Gmail, Chrome extension). PRESUMPTION-033 notes that the "well enough" checkpoint criterion for wiki_narration.html was defined by the assistant, not by Tom. PRESUMPTION-034 surfaces the "daily run" naming drift (an 8-day backlog labelled a single daily run).

Key event (2026-04-17): Eight new presumptions surfaced, clustering around three themes. **OPERATIONAL-DRIFT escalation** (PRESUMPTION-035 threshold-free flag invocation, PRESUMPTION-036 single-cluster framing obscures four root causes) extends PRESUMPTION-032 from a 2-channel aggregation concern to a 4-channel escalation with a monitoring-logic gap. **Cross-session handoff reliability** (PRESUMPTION-037 file-based pattern assumed reliable without stress test, PRESUMPTION-038 billing bug assumed to self-clear) introduces a new architectural primitive on top of untested vendor state. **Plugin-as-shipped** (PRESUMPTION-039 trigger-phrase taxonomy assumed representative of Tom's phrasing, PRESUMPTION-040 structural verification treated as operational readiness) captures the plugin-publish-and-test-tomorrow pattern. **Meta-level self-awareness concerns** (PRESUMPTION-041 implicit-decision drift — afternoon commitments do not become formal DECISIONs, PRESUMPTION-042 morning-run null output framed as accurate rather than coverage-miss) turn the self-awareness lens on the self-awareness pipeline itself. PRESUMPTION-041 is particularly notable — it formalizes an observation that the cowork summary itself already started to label ("Implicit decisions worth recording tomorrow if Tom endorses them").

Key event (2026-04-18): Six new presumptions surfaced on a quiet architectural day dominated by operational friction, grouped in three clusters. **Session-parking and handoff semantics** (PRESUMPTION-043 parked-session indefinite-retention, PRESUMPTION-046 user-pivot discharges handoff payload) extend the implicit-decision-drift cluster from the DECISION layer (PRESUMPTION-041) down into session-lifecycle behavior: architectural intent dissolves silently at both layers when user direction pivots away. **Retry/escalation discipline** (PRESUMPTION-044 retry-as-default on Chrome failure, PRESUMPTION-048 null walk notes as miss-vs-zero ambiguity) extend the OPERATIONAL-DRIFT monitoring-logic cluster (PRESUMPTION-035, 036) down into per-task retry behavior and up into intent-capture signaling. **Cross-tradition transfer validity** (PRESUMPTION-045 Wolfram-hypergraph formalism transferred to Sellarsian space of reasons without transfer-validity check) joins the CRITICAL cluster (PRESUMPTION-002 Thousand Brains transfer, PRESUMPTION-024 selection effect on FINDING-011a, PRESUMPTION-014/020 cross-tradition signal validity) as its Wolfram-domain instance. A standalone normative presumption (PRESUMPTION-047 user-directedness-over-system-initiative for cross-account ingestion) articulates the value commitment underneath PRESUMPTION-043's indefinite-retention pattern. Notable: today's PRESUMPTION-046 is the third member of the meta-cluster that turns the self-awareness lens on the self-awareness pipeline itself — today specifically on the handoff primitive introduced by DECISION-021 (candidate).

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

Tertiary cluster (2026-04-17 — monitoring-meta): PRESUMPTION-035 + PRESUMPTION-036 extend the operational-drift cluster with a *monitoring-logic* layer. PRESUMPTION-035 surfaces that the drift flag is being invoked without a codified threshold; PRESUMPTION-036 surfaces that the cluster's single-name framing obscures four independent root causes. Together they imply the drift-detection system is not yet operationally precise — the signal it produces is qualitative narrative, not a decision-ready alert.

Quaternary cluster (2026-04-17 — self-awareness-on-self-awareness): PRESUMPTION-041 (implicit-decision drift) and PRESUMPTION-042 (null-output coverage miss) are the first presumptions that turn the system's reflective lens on its own self-awareness pipeline. PRESUMPTION-041 notes that architectural decisions made in interactive sessions tend to slip past formal DECISION-NNN tracking; PRESUMPTION-042 notes that a null-output morning run is treated as a faithful report rather than a coverage question. Both are self-referential — they describe failure modes *within* the 14a/14b/DECISION pipeline. This continues the pattern started by PRESUMPTION-015 (self-referential circularity) and extended by PRESUMPTION-024 (selection effect on FINDING-011a), now applied at the operational layer.

Key event (2026-04-20): Six new presumptions surfaced on a quiet Monday dominated by autonomous operational runs with one still-running specialist task. **Cross-task coordination** (PRESUMPTION-049 scope-partition between wiki daily run and Monday specialist slot, PRESUMPTION-051 "pending proposals: 12" count emitted before sibling task completes) introduces a new cluster — the two scheduled tasks that overlap in time/scope have no coordination contract, and their output semantics are presumed to be composable. **Asymmetric operational-drift thresholds** (PRESUMPTION-050 4-day git lock still classified as single incident vs. ASSUMPTION-042's 5-consecutive-failures threshold for Chrome) surfaces an INTERNAL-CONSISTENCY concern at the cross-channel monitoring layer — extends the 2026-04-18 INTERNAL-CONSISTENCY-FLAG (PRESUMPTION-044/ASSUMPTION-042) to a second channel pair. **Intent-capture recurrence** (PRESUMPTION-052 second-consecutive null-walk handled by same fallback without escalation) adds a recurrence signal to PRESUMPTION-048; Gmail has now been degraded 7 calendar days, and no escalation has fired. **Briefing-layer epistemic blind spot** (PRESUMPTION-053 17→11 findings filter unaudited selection criterion) is the symmetric partner to PRESUMPTION-029 (multi-subagent batch inflation) — both concerns are about silent signal modification in the PRS pipeline (quiet deletion here vs. quiet amplification there). **Specialist-task convergence** (PRESUMPTION-054 no turn-cap on Levin+Friston specialist, still running at EOD with 58+ turns and no write) surfaces a scheduled-task contract gap that creates a read-after-write race between parallel pipelines. Notable: today's run highlights a parallel-execution coordination gap between scheduled tasks that was invisible until Monday's two-specialist slot overlapped with the daily run's coverage decision.

Key event (2026-04-21 — autonomous-task-layer principles day): Nine new presumptions surfaced on a light-C2A2 day (external-visit-week begins tomorrow). Today's signal is high-normative and low-architectural, concentrated in three cluster extensions and one standalone architectural item. **Infrastructure-stability invisibility** (PRESUMPTION-061 sandbox mount topology presumed stable across runs, HIGH risk) is the day's standalone architectural item — surfaced by today's Phase 6 failure at a layer (filesystem mount configuration) that was previously invisible. Adds a new failure mode stacking atop the pre-existing `.git/index.lock` gap. **SELF-AWARENESS-META cluster extension to 9 members** (PRESUMPTION-069 silence-not-tracked; close-adjacent PRESUMPTION-062 sync-transcript-ground-truth). PRESUMPTION-069 is the first time absence-of-run-itself becomes a tracked architectural event; its omission from the event stream is the cluster's newest failure-mode category (drift → handoff → cross-model echo → absence-as-event). PRESUMPTION-062 extends the same cluster's transcript-as-ground-truth subpattern. **BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster extension to 8 members** (PRESUMPTION-063 natural-termination default; PRESUMPTION-064 narrative-surfacing-adequate; PRESUMPTION-067 specialist-self-eval-adequate). Today's four new 14a items (ASSUMPTION-057, 058, 059, 060) made the sync/briefing/specialist layers explicit about their own operating principles, and these three 14b items flag the gaps in the newly-stated principles' self-validation. PRESUMPTION-063 is in direct tension with candidate DECISION-024 (specialist-task turn-cap default = 20). **Cross-task correlation** (PRESUMPTION-065 two Morning sessions treated as independent data points) extends the CROSS-TASK-COORDINATION cluster's correlation-concern substream. **User-attention-reallocation-not-tracked** (PRESUMPTION-066 week-scale user-priority pivot does not generate DECISION-NNN) extends PRESUMPTION-041's implicit-decision-drift cluster from day-scale to week-scale. **Auth-state-as-resolved** (PRESUMPTION-068 today's Chrome MCP double-success as resolved rather than transient) updates the OPERATIONAL-DRIFT Chrome channel's classification ambiguity without resolving it; threshold logic for "resolved" still missing in parallel with ASSUMPTION-042's "not-transient" threshold. Notable: today's 9-to-8 presumption-to-assumption ratio tightens slightly from Monday Run 2's 6:6 parity, but the assumption side carried six methodological/normative items, so the principle-articulation rate of the scheduled-task layer is at record pace.

Key event (2026-04-20 supplementary Run 2 — caching-architecture cluster): Six additional presumptions surfaced covering the C2a2 caching architecture monday session plus two late-day ingestion/handoff events. **Caching-architecture structural frame** (PRESUMPTION-055 binary static/dynamic partition as sole primitive; PRESUMPTION-057 RC Wiki edit-frequency audit absent) names the structural and empirical premises underlying the 70–80% cost projection. **Optimization-target gap** (PRESUMPTION-056 cost is the sole optimization target; no quality-regression smoke test defined) is a methodological gap that could let quality regress invisibly under a cost-win headline. **Joint-entry rationale loss** (PRESUMPTION-058 Levin+Friston split without reviewing the joint-entry rationale) is a specific instance of design-as-path-of-least-resistance under the new protocol. **Auth-channel singleton** (PRESUMPTION-059 Chrome claude.ai auth presumed user-maintained with no fallback ingestion path) joins the OPERATIONAL-DRIFT cluster as a new failure mode distinct from "extension not connected." **Chat-side endorsement as validation** (PRESUMPTION-060 Claude-to-Claude agreement treated as architectural confirmation) joins the CRITICAL SELF-AWARENESS-META cluster (PRESUMPTION-015, 024, 041, 042, 046, 048, 052, 060) as its eighth member — and is the highest-risk new item of the day. The supplementary run raises the SELF-AWARENESS-META cluster from 7 to 8 members and the CRITICAL/HIGH-leaning portion of the registry accordingly.

21 of 69 presumptions have been reconciled with literature search results (unchanged — no 15a/15b/15c cycle ran on 2026-04-21). 55 are UNTESTED: 34 carried from prior cycles + 6 from 2026-04-20 Run 1 (dispositioned by 2026-04-20 15c cycle) corrected to 6 from 2026-04-20 supplementary Run 2 (still QUEUED, pipeline lag now 1 day) + 9 from 2026-04-21 (freshly QUEUED, pipeline lag 0 days). Lit-search queue QUEUED count: 15 presumptions (6 from 2026-04-20 Run 2 + 9 from 2026-04-21).

Key event (2026-04-26 — high-architectural Sunday): Eleven new presumptions surfaced on a Sunday dominated by the Summa-2026 derivative-project design conversation plus three specialist-agent slots. **Structural-presumption cluster emerging** (PRESUMPTION-070 decomposability of Stump's frameworks, PRESUMPTION-073 N=11→13 scaling, PRESUMPTION-078 Stump×Fredrickson commensurability, PRESUMPTION-079 SAME-paradigm-shift-signal claim, PRESUMPTION-080 cross-discipline operational-primitive transfer) tripled the structural-presumption count from 2 to 6. **Epistemic** (PRESUMPTION-071 Levin+Hoffman+Kastrup convergence-coherence; PRESUMPTION-077 4-day master-narrative gap absorbability) and **Normative** (PRESUMPTION-072 Catholic/Thomistic Summa-synthesis as appropriate downstream consumer) extensions complete the cluster. **Methodological** (PRESUMPTION-074 specialist-recognized-convergence reliability — load-bearing for ASSUMPTION-063, 065, 066, 067; PRESUMPTION-075 Chrome MCP egress workaround as permanent; PRESUMPTION-076 canonical-works fallback as native-wiki equivalent) round out the day. PRESUMPTION-074 became the day's load-bearing presumption — when 15a/15b/15c eventually runs (2026-04-27), it was flagged as SYSTEMIC-RISK affecting four same-week assumptions.

Key event (2026-05-05 — daemon-catchup Tuesday): Eleven new presumptions surfaced on a daemon-catch-up Tuesday whose primary architectural signal was the simultaneous execution of all six weekday-assigned C2A2 specialist agents in a single 60-minute UTC window. Today's eleven presumptions cluster in five families. **(1) DAEMON-CATCHUP cluster (NEW, 4 members)** — PRESUMPTION-093 (same-day catch-up structurally equivalent to spread-across-week; risk MEDIUM), PRESUMPTION-094 (`fireAt` workaround presumed not to interact with C2A2 self-awareness; risk MEDIUM), PRESUMPTION-102 (link-count partition deterministic across creation paths; risk MEDIUM), PRESUMPTION-103 (weekday-of-assignment label convention unstated; risk LOW). The DAEMON-CATCHUP cluster is novel today and surfaces the catch-up scenario as an unexamined operational mode. **(2) SPECIALIST-OUTPUT-AS-PRIMARY cluster (extends 2026-04-27 RECURSIVE-SPECIALIST-READING)** — PRESUMPTION-096 (specialist self-tagging cross-tradition signals as primary; risk MEDIUM-HIGH), PRESUMPTION-097 (parallel "strongest bridge" claims without adjudication; risk MEDIUM). Both compound PRESUMPTION-074's prior SYSTEMIC-RISK flag on specialist-recognition reliability. **(3) IMPLICIT-DECISION-DRIFT extension** — PRESUMPTION-098 (walk-thread Gmail as architectural source-of-record without DECISION-NNN canonization; risk MEDIUM) — six "decisions" extracted from today's walk-thread, none promoted to DECISION-NNN. Joins PRESUMPTION-041 cluster. **(4) FEEDBACK-LOOP-MISSING (NEW cluster, 1 member)** — PRESUMPTION-100 (McGilchrist+Kastrup's specialist output bears on ASSUMPTION-007 but no feedback loop captures the bearing; risk MEDIUM). Today is the first observed instance where a specialist explicitly named a foundational ASSUMPTION as the downstream concern of its proposal. **(5) Standalone** — PRESUMPTION-095 (Phase-2 zero-result presumed exhaustion not method-failure; risk LOW-MEDIUM), PRESUMPTION-099 (3-layer RC Explorer presumed non-overlapping; risk LOW-MEDIUM), PRESUMPTION-101 (filter-semantics popover ≡ implementation without test; risk LOW-MEDIUM). Today's 11-to-9 presumption-to-assumption ratio (1.22:1) is moderate — below 2026-04-27's 12:8 high (1.5:1) but above 2026-04-21's 9:8 (1.13:1). The execution-day catch-up character generates both stated commitments (the daemon-bug diagnosis and RC Explorer vision are surfaced as ASSUMPTIONs) and unstated dependencies (the catch-up scenario itself, the specialist-self-tagging primary status, the missing feedback loops). 40 of 92 carried-prior reconciled; 11 newly surfaced; 63 of 103 cumulative will be UNTESTED post-run. Lit-search queue at this moment: 11 new presumptions QUEUED.

Key event (2026-05-08 — Friday review-decision intake + three stalled scheduled tasks + queued composite synthesis): Twelve new presumptions surfaced on a Friday whose dominant operational signature was three weekday-scheduled-task stalls (1pm register cleanup at "let's do it" prompt; sewing-agent-weekly hit org-limit immediately; Wright/Rohr Sunday agent hit org-limit immediately) plus a queued-but-undelivered composite synthesis of the C2A2 explorer Codex 5.5 external review (local_56cc4dfb hit org-limit twice). Today's twelve presumptions cluster in five families. **(1) ORG-LIMIT + COMPOSITE-SYNTHESIS cluster (NEW, 4 members)** — PRESUMPTION-104 (org-vs-personal naming presumed misclassification; risk MEDIUM), PRESUMPTION-105 (queued-across-sessions persistence; risk MEDIUM-HIGH), PRESUMPTION-107 (org-limit presumed service-not-pattern; risk MEDIUM-HIGH), PRESUMPTION-109 (cross-LLM review composition without bias weighting; risk MEDIUM). The cluster surfaces unstated dependencies of the new pattern: external-LLM review composed with internal report under quota constraints. **(2) IMPLICIT-DECISION-DRIFT extension** — PRESUMPTION-106 (protocol-vs-architectural canonization criterion unwritten; risk MEDIUM) — extends PRESUMPTION-098 / PRESUMPTION-041 cluster with the protocol-routine-vs-DECISION-NNN distinction itself. **(3) SANDBOX-INFRASTRUCTURE-CLUSTER-LAYER cluster (NEW, 2 members)** — PRESUMPTION-110 (cross-project constraints presumed same-architectural-layer; risk MEDIUM), PRESUMPTION-114 (master-narrative-gap cause attribution privileges most-recent diagnosis; risk MEDIUM). The cluster surfaces the same-layer presumption beneath ASSUMPTION-094's combined-escalation-threshold formulation. **(4) STALLED-TASK-CLOSURE cluster (NEW, 2 members)** — PRESUMPTION-108 (three-stall-day human-noticing-as-sufficient closure; risk MEDIUM-HIGH), PRESUMPTION-111 (third-consecutive cowork-to-chat sync failure without fallback; risk MEDIUM-HIGH). The cluster names the absent automated-alert path for stall-pattern recognition. **(5) UNDIFFERENTIATED-DEFERRED-TREATMENT cluster (NEW, 2 members) + Standalone** — PRESUMPTION-112 (deferred items of differing characters get same disposition; risk LOW-MEDIUM), PRESUMPTION-113 (off-cadence proposal filings presumed equivalent to on-cadence; risk LOW-MEDIUM), PRESUMPTION-115 (Codex prioritization adopted near-verbatim without project-context adjudication; risk MEDIUM). PRESUMPTION-115 extends PRESUMPTION-074's prior SYSTEMIC-RISK on specialist-recognition reliability to the external-tool-review layer. Today's 12-to-8 presumption-to-assumption ratio (1.5:1) ties 2026-04-27's high. The execution-day stall-heavy character generates more *missing-process articulation* (8 of 12 are about missing alerts, missing differentiation, missing adjudication, missing fallback) than *content-architecture* claims. 12 newly surfaced; 0 reconciled today; 12 newly QUEUED for next 15a/15b cycle. Lit-search queue at this moment: 20 items (8 new ASSUMPTIONs + 12 new PRESUMPTIONs).

Key event (2026-05-09 — Saturday lit-search-disposition + cycle-output epistemic gaps + cross-tradition leverage claim): Twelve new presumptions surfaced on a Saturday whose dominant operational signature was the 15a/15b/15c lit-search pipeline draining yesterday's 20-item EOD batch in a single morning cycle and producing four SYSTEMIC-RISK flags (the densest single cycle on record). Today's twelve presumptions cluster in five families. **(1) LIT-SEARCH-CYCLE-OUTPUT-EPISTEMIC-WEIGHT cluster (NEW, 4 members)** — PRESUMPTION-116 (densest-cycle framing presumes cycle-density itself is a meaningful comparison metric without batch-size or topic-mix normalization; risk LOW-MEDIUM), PRESUMPTION-117 ("Core Operational Discipline" sprint presumes registration / canonization / fallback share enough remediation-substrate to bundle; risk MEDIUM), PRESUMPTION-118 (DECISION-027 unify-vs-split presumed reversible at low epistemic cost; risk MEDIUM), PRESUMPTION-123 ("100% drained in one cycle" celebrates throughput while INCORPORATE rate stays at 0 and REVISE backlog grows; risk MEDIUM). The cluster surfaces the unstated metrics-and-bundling presumptions beneath today's cycle-output architectural commitments. **(2) CROSS-TRADITION-LEVERAGE-CLAIM cluster (NEW, 2 members)** — PRESUMPTION-119 ("highest-leverage signal of the week" presumes leverage is single-axis-measurable without operational definition; risk LOW-MEDIUM), PRESUMPTION-120 (out-of-band Pattern-Detector deep-pass scheduling presumed policy-free; risk MEDIUM). The cluster surfaces the operational-definition gap beneath today's Saturday-Wolfram leverage claim. **(3) EXTERNAL-LLM-DIAGNOSTIC-UPTAKE-RECURRENCE cluster (extends 2026-05-08 PRESUMPTION-115 SYSTEMIC-RISK to chat-scrape failure-mode layer)** — PRESUMPTION-121 (Codex-style external-LLM diagnostic for Chrome MCP "normal windows" error presumed reliable enough to skip independent project-context adjudication; risk MEDIUM-HIGH; SYSTEMIC-RISK recurrence). PRESUMPTION-121 is today's high-risk item and marks the SECOND layer at which the PRESUMPTION-115 pattern has now recurred (explorer-fix layer + chat-scrape failure-mode layer in 24 hours). **(4) STALLED-TASK-CLOSURE / DOCUMENTATION-AS-FIX cluster (extends 2026-05-08 PRESUMPTION-108 / PRESUMPTION-111)** — PRESUMPTION-122 (documentation-for-Tom presumed to count as "fix" for recurring scheduled-task pre-condition without programmatic enforcement; risk LOW-MEDIUM), PRESUMPTION-125 (4th-consecutive cowork-to-chat sync failure presumed not to escalate severity beyond N=3 threshold; risk MEDIUM-HIGH). PRESUMPTION-125 specifically extends the PRESUMPTION-111 SYSTEMIC-RISK by adding a 4th-consecutive recurrence with no severity-ladder articulation. **(5) PER-TASK-EVIDENCE-PRIVILEGED-OVER-CROSS-TASK cluster (NEW, 2 members) + Standalone (2)** — PRESUMPTION-124 (today's 8-task fire-rate treated as global negative inference for daemon-link-count regression while wiki-orchestrator status today is not in the evidence frame; risk MEDIUM); PRESUMPTION-126 (PROCESSED_LOG reconciliation presumed one-time backfill without completeness check; risk LOW-MEDIUM); PRESUMPTION-127 (today's McGilchrist off-cadence filing presumed routinely absorbable without raising the 2-day off-cadence pattern flag of PRESUMPTION-113; risk LOW-MEDIUM). Today's 12-to-8 presumption-to-assumption ratio (1.5:1) ties 2026-04-27 and 2026-05-08 as joint-record. The lit-search-disposition character generates more *cycle-output-articulation gaps* (PRESUMPTION-116, 117, 118, 123 are all about today's cycle-output meta-commitments) than *content-architecture* claims. Notable: PRESUMPTION-121 is the SECOND-LAYER recurrence of PRESUMPTION-115's external-LLM-uptake SYSTEMIC-RISK in 24 hours — the cluster is showing same-shape behavior at the chat-scrape failure-mode layer that it just showed at the explorer-fix layer, and may be the most actionable architectural item to surface to Tom this morning. 12 newly surfaced; 0 reconciled today (today's 15c cycle was on yesterday's items, not today's); 12 newly QUEUED for next 15a/15b cycle. Lit-search queue at this moment: 20 items (8 new ASSUMPTIONs + 12 new PRESUMPTIONs).

Key event (2026-04-27 — execution-day epistemic-commitments and shadow-architecture extension): Twelve new presumptions surfaced on an execution-heavy Monday whose primary architectural signal was the lit-search pipeline draining the 5-day backlog and INCORPORATING ASSUMPTION-068 → PREMISE-012 and ASSUMPTION-069 → PREMISE-013. Today's twelve presumptions cluster in five families. **(1) LIT-SEARCH-LAYER-EPISTEMIC-COMMITMENTS (NEW cluster, 2 members)** — PRESUMPTION-081 (single-cycle drain quality vs. 5-cycle distributed; risk MEDIUM) and PRESUMPTION-082 (refresh-cycle search-depth asymmetry; risk MEDIUM) — symmetric to the BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster but at the lit-search-net-evaluator layer. The lit-search pipeline articulating its own operating principles (ASSUMPTION-072, 073, 074) makes these epistemic gaps visible. **(2) PREMISE-PROMOTION-WITHOUT-N-EXAMINATION (NEW cluster, 2 members)** — PRESUMPTION-085 (PREMISE-012 N-day threshold not examined) and PRESUMPTION-086 (PREMISE-013 N-collisions threshold not examined) — symmetric pair: both are presumptions about today's two newly-INCORPORATEd premises ratifying scope without re-examining the upper bound. **(3) SHADOW-ARCHITECTURE EXTENSION** — PRESUMPTION-088 (PRS authorial reframing not propagated to C2A2 wiki itself) and PRESUMPTION-092 (summa-2026-nightly-verification not integrated with C2A2 self-awareness) extend yesterday's CHANGE-2026-04-26-001 / OPEN-036 shadow-architecture pattern: derivative-project artifacts that bear on C2A2 but live outside the C2A2 self-awareness layer. **(4) RECURSIVE-SPECIALIST-READING (NEW critical-cluster member)** — PRESUMPTION-089 joins the CRITICAL/HIGH self-awareness cluster (PRESUMPTION-002, 024) as the recursive-specialist-reading instance: if PRS triplets are Tom's frame (ASSUMPTION-076), then specialists reading the wiki's per-tradition files as tradition-self-voice are reading Tom's frame back to themselves and reporting that as cross-tradition convergence. **(5) FAILURE-MODE PATTERN-RECOGNITION-WITHOUT-DECISION** — PRESUMPTION-083 (browser-auth as user-fixable indefinitely; risk MEDIUM-HIGH), PRESUMPTION-084 (pre-flight cowork-directory-grant failure pattern continues without DECISION-026 candidate; risk MEDIUM-HIGH), PRESUMPTION-091 (33-deep proposal queue framed as absorbable; risk MEDIUM) — three OPERATIONAL-DRIFT cluster extensions where new failure-mode data points are recognized but not promoted to candidate decisions. **(6) Standalone** — PRESUMPTION-087 (Levin "significant work not yet captured" override audit-mechanism absent; risk MEDIUM-HIGH) and PRESUMPTION-090 (cost-tracker tier estimates as ground truth without validation; risk LOW-MEDIUM). Today's 12-to-8 presumption-to-assumption ratio is the highest yet observed (1.5:1) and signals the gap between operational-principle articulation (8 stated assumptions) and the implicit/recursive premises beneath them (12 surfaced presumptions). Note: 21 + 19 = 40 prior reconciled, 21 carried + 19 dispositioned today (today's 15c run), so 40 of 92 reconciled with literature search results; 52 are UNTESTED. Lit-search queue at this moment: 12 new presumptions QUEUED.

PRESUMPTION-150:
  Date surfaced: 2026-05-13
  Statement: [inferred] The 17-pathway count is presumed to be comprehensive — the inventory is treated as architecturally complete at the moment of specification with no audit step asking "what pathways are missing?" or "what unit of decomposition would expose pathways the dispatch beats happened not to surface?". Enumeration in 14 conversational beats becomes the de facto closure on the architectural surface.
  Evidence it was operative: Cowork-to-chat summary 2026-05-13 paragraph 1 enumerates 17 pathways + 2 bright pins as if exhaustive: "The pathway inventory is the first end-to-end articulation of the system Tom intends to demo at ISME July 8-10." pathways.md frontmatter labels itself "Ground-truth index" without a not-yet-discovered-pathways section.
  Why it was unstated: When a design enumerates an inventory, the enumeration itself tends to feel exhaustive at the moment of specification; the "what's missing" question typically surfaces only when external observers, later sessions, or implementation work reveals gaps.
  Type: structural / methodological
  Related decisions: ASSUMPTION-119 (17-pathway inventory), PRESUMPTION-144 (Vault Linker seven-category taxonomy as closed without audit — parallel pattern), Pathway 00 (Broker)
  Testability: testable empirically (after N≥3 future architectural sessions, audit how many new pathways are added that the 2026-05-13 inventory did not anticipate; track inventory-stability vs. inventory-revision rate); testable via literature (closed-enumeration-as-completeness anti-pattern in software architecture and ontology design)
  Risk if wrong: Medium — missed pathways become technical debt; the worse case is a missed ISME-critical pathway whose absence is discovered close to the July 8-10 demo
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-150
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-13 + pathways.md as a closed-enumeration-as-completeness pattern (parallel to PRESUMPTION-144 seven-category Vault Linker taxonomy).
    Current status: UNTESTED

PRESUMPTION-151:
  Date surfaced: 2026-05-13
  Statement: [inferred] The ISME-critical / not-ISME-critical classification is treated as binary — Pathway 00, 01, 02, 03, 08 are marked critical; the other twelve are not. There is no graduated criticality scale (e.g., "essential / nice-to-have / aspirational / stretch") and no consideration of which sub-set of the six critical pathways could be cut and still produce a viable demo. The all-six-or-bust framing presumes the demo is indivisible.
  Evidence it was operative: pathways.md inventory uses "ISME focus: Pathways marked `isme_critical: yes` are on the demo critical path; the rest are post-ISME or optional-for-demo." Cowork-summary 2026-05-13 "What's Next" item 8: "The six ISME-critical pathways (00, 01, 02, 03, 08, plus tightening of the demo through 04/06/14) need an explicit build sequence. Pathway 00 (Broker) is on the critical path for all of them." No fallback subset is articulated; only Pathway 08 (Prepared Presentation) is mentioned as a "demo lifeboat."
  Why it was unstated: ISME-critical-or-not is the easiest scale to specify and reads as decisive at the moment of authorship; gradations are typically forced only when timelines compress.
  Type: methodological / scaling
  Related decisions: ASSUMPTION-119 (ISME-critical set), Pathway 08 (Prepared Presentation), OPEN-040 (candidate — ISME demo build sequence), PRESUMPTION-152
  Testability: testable empirically (under simulated timeline compression at 2026-06-08, 2026-06-22, 2026-07-01, ask "which critical pathway would you cut first?" and measure whether the answer is well-defined or surprises the team); testable via process (compare binary-criticality vs. graded-criticality scoring in software demo-prep literature)
  Risk if wrong: Medium-High — if any of the six critical pathways slips and no graded fallback exists, the demo defaults to Pathway 08 alone (offline canon mode) rather than a graceful partial-demo
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-151
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from pathways.md ISME-focus section + cowork-summary 2026-05-13 "What's Next" item 8 as a binary-criticality classification without graduated fallback.
    Current status: UNTESTED

PRESUMPTION-152:
  Date surfaced: 2026-05-13
  Statement: [inferred] The ~10-30 ms broker-side edge overhead figure is presumed accurate without measurement at the moment of the Cloudflare Workers commitment. The "conditional on streaming-latency validation" caveat presumes the validation test will confirm rather than contradict the estimate; the framing of "dwarfed by LLM and TTS provider latency floors" presumes those floors will dominate end-to-end latency without auditing them either.
  Evidence it was operative: Cowork-to-chat summary 2026-05-13 + Pathway 00: "Edge-distributed; ~10-30 ms broker-side overhead is dwarfed by LLM + TTS provider latency. Paid plan ($5/mo) gives 30 s CPU + unlimited requests." The validation test in "What's Next" item 4 is framed: "If under ~200 ms, decision is unconditional; if not, fall back to the AWS Lambda + ALB alternative" — the threshold is set in advance with no acknowledgment that the threshold itself rests on the unverified dwarfed-by claim.
  Why it was unstated: Engineering estimates that "feel right" tend to ship as preconditions for decisions before they are validated; the validation step is articulated as a check but framed as expected-to-pass.
  Type: empirical / methodological
  Related decisions: ASSUMPTION-120 (Cloudflare Workers hosting), DECISION-026 (candidate — broker hosting), OPEN-040 (candidate — streaming-latency conditional)
  Testability: testable empirically (run the streaming-latency test; record measured broker-side overhead distribution AND measured LLM + TTS provider latency distribution; audit whether the "dwarfed by" claim survives at p50, p90, p99); testable via literature (edge-broker overhead in production streaming-LLM deployments)
  Risk if wrong: Medium — if the broker-side overhead is meaningful relative to LLM/TTS floors, the broker becomes a perceptible-latency contributor under voice dialogue, which is the load-bearing ISME-critical pathway
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-152
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-13 + Pathway 00 latency-claim structure as an unverified-engineering-estimate pattern with pre-set validation threshold.
    Current status: UNTESTED

PRESUMPTION-153:
  Date surfaced: 2026-05-13
  Statement: [inferred] The Twilio SMS one-tap signed-link approval flow presumes that signed-link integrity (token signing + verification) is sufficient as a security primitive against adversarial replay, signing-key compromise, or man-in-the-middle interception of the SMS payload. No threat model is articulated against the one-tap surface; the choice of "no typing at the moment of approval" optimizes for UX without explicitly trading off against security depth.
  Evidence it was operative: Cowork-to-chat summary 2026-05-13 + Pathway 00 phrasing: "Phone confirmation for external-escalation gating: Twilio SMS one-tap signed link (not reply-keyword). No typing at the moment of approval. Webhook co-located on the same Cloudflare Worker as the broker." Rationale is exclusively UX (no typing); security framing is absent.
  Why it was unstated: Phone-based-confirmation UX optimization tends to read as the design surface; cryptographic security tends to slip into implementation detail rather than design statement.
  Type: architectural / security / methodological
  Related decisions: ASSUMPTION-121 (Twilio SMS one-tap), DECISION-027 (candidate), Pathway 00 (Broker)
  Testability: testable empirically (build a threat-model document for the one-tap surface; test signed-link replay resistance; audit secret-rotation policies); testable via literature (one-tap-link security patterns in passwordless auth and 2FA literature)
  Risk if wrong: Medium-High — a compromised approval flow at the external-escalation gate undermines the broker's role as gatekeeper for outbound action
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-153
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each form:
      14b: Inferred from cowork-summary 2026-05-13 + Pathway 00 phrasing as UX-optimized-without-stated-threat-model pattern.
    Current status: UNTESTED

PRESUMPTION-154:
  Date surfaced: 2026-05-13
  Statement: [inferred] Phone-as-the-confirmation-modality is presumed without considering alternative confirmation surfaces (push notification through an app; email magic link with rate-limit; in-cowork-session confirmation; pre-authorized scope tokens). The SMS-vs-keyword framing is presented as a binary choice between two SMS-form-factor primitives, eliding the more fundamental "must confirmation be SMS at all?" question.
  Evidence it was operative: Cowork-to-chat summary 2026-05-13 + Pathway 00: only "Twilio SMS one-tap signed link" and "reply-keyword" appear as the two options. Pathway 12 (Outreach Automation) references the broker but does not surface alternatives.
  Why it was unstated: When two options of the same form factor are compared, the form factor itself becomes invisible.
  Type: structural / methodological
  Related decisions: ASSUMPTION-121, PRESUMPTION-153, Pathway 00, Pathway 12
  Testability: testable empirically (compare SMS-one-tap vs. push-notification confirmation in latency, false-positive rate, and user satisfaction over N≥3 weeks of operation); testable via literature (modality comparison for asynchronous approval flows in DevOps and enterprise paging tools)
  Risk if wrong: Low-Medium — SMS may be fine; the cost of the unconsidered alternative is being locked into a single confirmation modality without measurement
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-154
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-13 + Pathway 00 binary-within-form-factor framing as absent-alternative-modality pattern.
    Current status: UNTESTED

PRESUMPTION-155:
  Date surfaced: 2026-05-13
  Statement: [inferred] Locating eager-tier perspective-lattice content in the vault at `wiki/Perspectives/` with a structure-group tag presumes that the existing Sociogram + structure-group machinery generalizes correctly to perspective lattices — that perspectives behave architecturally like thinkers, PRS triplets, and structure-groups already in the system. The transfer-condition for "first-class wiki citizen" treatment is not audited; ASSUMPTION-122 is the structural counterpart but does not name the transfer condition.
  Evidence it was operative: Cowork-summary 2026-05-13 "Key Decisions Made" pathway-doc decision (i): "Perspectives in vault: eager-tier perspective-lattice content lives at `wiki/Perspectives/` with a structure-group tag (first-class wiki citizens)." Pathway 04 file presumes the same.
  Why it was unstated: When a system has existing first-class-citizen machinery, the natural rhetorical move is to extend it; the question "does this new content type fit the existing pattern?" becomes invisible because the answer feels obvious.
  Type: architectural / methodological / scaling
  Related decisions: ASSUMPTION-122, Pathway 04, ASSUMPTION-082 (3-layer RC Explorer)
  Testability: testable empirically (build the Perspectives folder; track Sociogram-retrieval behavior, structure-group filter behavior, and voice-agent-addressability on perspective-lattice content vs. tradition-page content); testable via process (audit which Sociogram features assume thinker/PRS schema vs. which are content-agnostic)
  Risk if wrong: Low-Medium — bad fit shows up as Sociogram-rendering or retrieval anomalies post-implementation
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-155
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-13 + Pathway 04 as an unaudited-transfer-of-first-class-citizenship-machinery pattern.
    Current status: UNTESTED

PRESUMPTION-156:
  Date surfaced: 2026-05-13
  Statement: [inferred] Ephemeral-by-default + Pin-this-promotion (Pathway 05 whiteboard) presumes that users will reliably notice valuable plots within the session and remember to pin them. The opposite-default ("persistent by default, swipe to discard") is not considered. The implicit user model is "user evaluates each plot in real time and acts on it" — a model that may fail for derivative-realization use cases where the value of a plot becomes apparent only on later re-encounter.
  Evidence it was operative: Cowork-summary 2026-05-13 "Key Decisions Made" pathway-doc decision (ii): "Whiteboard ephemerality: plots are ephemeral by default with 'Pin this' promotion to vault and per-plot export buttons." Pathway 05 reinforces. No alternative default policy considered.
  Why it was unstated: The Pin-this metaphor is well-established in app UX and tends to ship with its default unexamined.
  Type: methodological / UX / normative
  Related decisions: ASSUMPTION-123, Pathway 05
  Testability: testable empirically (in production, track ratio of pinned-plots-to-total-plots-generated; survey users on regret rate; A/B test default-ephemeral vs. default-persistent UX); testable via literature (ephemeral-vs-persistent default UX in note-taking and dashboard tools)
  Risk if wrong: Low — recoverable through default-policy change; main cost is user friction if regret rate is high
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-156
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-13 + Pathway 05 as a default-policy-without-alternative-considered pattern.
    Current status: UNTESTED

PRESUMPTION-157:
  Date surfaced: 2026-05-13
  Statement: [inferred] The generative-canvas library set (D3 + three.js + Plotly + bare canvas/WebGL) is presumed to be the right catalog without considering alternatives: Observable Plot, deck.gl, regl, vega-lite, P5.js, Mapbox GL JS, ECharts. The four-library enumeration may be canonical for the team but is not justified against a comparison set; "the right catalog" framing presumes the rest of the library landscape was surveyed and rejected.
  Evidence it was operative: Cowork-summary 2026-05-13 "Key Decisions Made" pathway-doc decision (iii): "Generative-canvas library set: D3 + three.js + Plotly + bare canvas/WebGL." No comparison against alternative libraries is recorded.
  Why it was unstated: Library choices tend to converge on familiar names; the "what about X?" question gets dropped at the moment the working set feels sufficient.
  Type: methodological / tooling
  Related decisions: ASSUMPTION-124, Pathway 06
  Testability: testable empirically (track how often the code-writing agent reaches outside the enumerated set during real generative-canvas tasks; track substitution-rate when prompted alternative is available); testable via literature (visualization-library comparison in 2026 for generative AI workflows)
  Risk if wrong: Low — additive — the library set can be extended later; cost is missed leverage if a better library exists for a key use case
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-157
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-13 + Pathway 06 as a closed-enumeration-without-comparison pattern.
    Current status: UNTESTED

PRESUMPTION-158:
  Date surfaced: 2026-05-13
  Statement: [inferred] "Low × High is the strongest research-program candidate" (Pathway 07 unsaid-edges scoring) is a normative judgment baked into the visualization: it presumes that infrequent-but-important corresponds to undeveloped research programs and that the Low × High quadrant should be visually emphasized. The scoring carries the normative claim that this quadrant matters most without auditing the alternative readings — Low × Low (irrelevant), High × Low (over-discussed-trivial), High × High (mature/saturated).
  Evidence it was operative: Cowork-summary 2026-05-13 "Key Decisions Made" pathway-doc decision (iv): "Unsaid-edges scoring: two filters (how-often × how-important); Low × High visually emphasized as the strongest research-program candidate." The "visually emphasized" UI choice reinforces the normative claim by giving Low × High the most attention-pulling treatment.
  Why it was unstated: When a normative claim is operationalized as a UI choice, it becomes invisible because it stops looking like a claim and starts looking like a feature.
  Type: normative / methodological
  Related decisions: ASSUMPTION-125, Pathway 07
  Testability: testable empirically (after the unsaid-edges map is live, audit which quadrant's edges actually become research programs over N≥4 months; compare Low × High emphasis against neutral coloring); testable via literature (research-gap-detection scoring in scientometrics and innovation studies)
  Risk if wrong: Medium — the UI training-effect of Low × High emphasis biases user attention; if the research-program judgment is wrong, the tool actively pushes the user toward bad candidates
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-158
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-13 + Pathway 07 scoring decision as a normative-claim-as-UI-feature pattern.
    Current status: UNTESTED

PRESUMPTION-159:
  Date surfaced: 2026-05-13
  Statement: [inferred] The "7-day delivery drought is broken" framing presumes that Tom's sign-in fix is the durable root cause — i.e., the proximal blocker was sign-in state, and once-fixed-it-stays-fixed. But sign-in state can lapse (cookie expiry, browser profile reset, claude.ai session timeout, OS-level credential change), and the underlying architectural mechanism is unchanged. ASSUMPTION-126's "working-channel framing" presumes a durable fix where the actual fix is a user-credential-layer workaround.
  Evidence it was operative: Cowork-summary 2026-05-13 opening delivery-status block: "Tom signed into claude.ai in the Chrome profile paired with the extension before this run, clearing the sign-in barrier that had blocked the prior 6 consecutive evening deliveries... The 7-day delivery drought is broken." No expiry or re-failure surface is articulated.
  Why it was unstated: A success after a long failure run reads as a structural fix; the credential-layer-vs-architectural-layer distinction tends to be elided in the moment of relief.
  Type: methodological / operational
  Related decisions: ASSUMPTION-126, ASSUMPTION-118 (token-based delegation workflow redesign), PREMISE-015, PRESUMPTION-125, PRESUMPTION-134
  Testability: testable empirically (track evening-sync success rate over next N≥14 days; correlate against sign-in state on Tom's Chrome profile; measure failure-mode recurrence rate); testable via process (audit "durable fix" claim against credential-layer vs. architectural-layer taxonomy)
  Risk if wrong: Medium-High — if the fix lapses silently, the redesign discussion loses urgency and the failure pattern returns with weaker political signal for canonization
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-159
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-13 opening delivery-status block as a credential-layer-workaround-framed-as-architectural-fix pattern.
    Current status: UNTESTED

PRESUMPTION-160:
  Date surfaced: 2026-05-13
  Statement: [inferred] Three HIGH-priority findings in a single day (FINDING-025, 029, 030) are treated as a normal Pattern-Detector output rate without considering the cumulative effect: prior days have produced at most 1-2 HIGH escalations. A 3-HIGH single-day signature presumes the Pattern Detector's escalation criteria are stable; it could equally indicate criterion drift, day-specific signal density, or coincidental clustering.
  Evidence it was operative: Wiki agent daily run report 2026-05-13: "HIGH escalations today: FINDING-025 (SUTI = C2A2 detection function in microcosm), FINDING-029 (ideas-as-living-agents → traditions-as-cognitive-entities), FINDING-030 (active-inference-as-OODA → first quantitative C2A2 detector via KL-divergence)." Listed without per-day-baseline comparison or escalation-rate normalization.
  Why it was unstated: HIGH escalations tend to be reported as content findings rather than as rate-of-escalation events; the rate-of-HIGH-output is invisible at the moment of reporting.
  Type: methodological / metrics / epistemic
  Related decisions: ASSUMPTION-127, ASSUMPTION-128, DECISION-010 (Pattern Detector), PRESUMPTION-148 (SELF-MEASUREMENT Goodhart cluster)
  Testability: testable empirically (compute Pattern-Detector HIGH-escalation rate per day over trailing N≥14 days; flag 3-HIGH days as outliers and investigate criterion stability); testable via process (audit Pattern Detector escalation criteria for drift between 2026-04-20 calibration baseline and 2026-05-13 output)
  Risk if wrong: Low-Medium — joins SELF-MEASUREMENT Goodhart cluster; if escalation criteria are drifting, downstream filtering of HIGH findings becomes less reliable
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-160
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from wiki agent daily run report 2026-05-13 HIGH escalations listing as an unnormalized-output-rate pattern (joins SELF-MEASUREMENT Goodhart cluster).
    Current status: UNTESTED

PRESUMPTION-161:
  Date surfaced: 2026-05-13
  Statement: [inferred] FINDING-030 framing of KL-divergence between active-inference and OODA distributions as a quantitative C2A2 detector presumes the active-inference/OODA homology is robust enough for cross-discipline metric transfer. The same homology has been challenged in PRESUMPTION-002 and PRESUMPTION-080 cross-discipline transfer-validity clusters; FINDING-030's quantitative-detector claim escalates the homology from descriptive bridge to load-bearing metric without first auditing the transfer condition.
  Evidence it was operative: Wiki agent daily run report 2026-05-13: "FINDING-030 (active-inference-as-OODA → first quantitative C2A2 detector via KL-divergence)." Morning walk briefing references FINDING-030 KL-divergence operationalization as a new task without naming the transfer-validity precondition.
  Why it was unstated: When a metric "feels right" and is operationally tractable, the metric ships before its validity-of-transfer is audited.
  Type: methodological / empirical / cross-tradition
  Related decisions: ASSUMPTION-128, FINDING-030, PRESUMPTION-002, PRESUMPTION-080, PRESUMPTION-142 (cross-tradition reframing without inverse acceptance check)
  Testability: testable via literature (active-inference / OODA homology validity in computational neuroscience, decision theory, military operations research); testable empirically (test KL-divergence operationalization against a sample of known accelerating-vs-non-accelerating tradition pairs)
  Risk if wrong: Medium-High — if the homology fails, the quantitative-detector claim becomes a sophisticated misdirection; joins PRESUMPTION-002 CRITICAL cluster
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-161
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from wiki agent daily run report 2026-05-13 + morning walk briefing as an unaudited-cross-discipline-metric-transfer pattern (joins PRESUMPTION-002 CRITICAL).
    Current status: UNTESTED

PRESUMPTION-162:
  Date surfaced: 2026-05-13
  Statement: [inferred] The nightly alignment-agent protocol (`architecture/` ground-truth → `wiki/Architecture/` mirror, diff + copy-on-drift) presumes unidirectional sync is the right policy. If edits happen on the mirror side (e.g., Obsidian user-edits in `wiki/Architecture/`), they will be silently overwritten on the next nightly run. Bidirectional merge with conflict-resolution is not considered.
  Evidence it was operative: pathways.md preamble: "A scheduled alignment agent runs nightly, diffs the two locations, copies ground-truth → mirror on drift, and flags the change in the next session archive." Unidirectional arrow; no merge protocol.
  Why it was unstated: When one location is named "ground truth," the directionality of sync feels self-evident — but in practice, Obsidian-side edits are a real channel.
  Type: architectural / operational
  Related decisions: ASSUMPTION-129, Pathway 00
  Testability: testable empirically (after alignment-agent runs, audit whether any mirror-side edits exist that would be overwritten; track silent-overwrite incidents); testable via process (compare against bidirectional sync policies in vault-mirror systems — e.g., Obsidian Sync, git-with-conflict-resolution)
  Risk if wrong: Medium — silent overwrite of user edits is a data-loss class of failure
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-162
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from pathways.md preamble alignment-agent protocol as a unidirectional-sync-without-merge-protocol pattern.
    Current status: UNTESTED

PRESUMPTION-163:
  Date surfaced: 2026-05-13
  Statement: [inferred] The honesty layer's "first-class visible epistemic-status marks on every claim, not buried footers" framing presumes the user will read and act on those marks. The opposite failure mode — epistemic-mark blindness from over-saturation when every claim is marked — is not considered. Universal visible marking may produce the same effective invisibility as buried footers if the rate of marking is too high to be cognitively budgetable.
  Evidence it was operative: pathways.md inventory entry: "14 — Honesty layer — *outlined.* First-class visible epistemic-status marks on every claim, not buried footers." Cowork-summary paragraph 1 reinforces. No discussion of marking-rate, cognitive-load budget, or attention-allocation under marked-everywhere conditions.
  Why it was unstated: First-class visibility reads as the virtuous default; the over-saturation failure mode tends to be discovered only at scale.
  Type: methodological / UX / epistemic / normative
  Related decisions: ASSUMPTION-130, Pathway 14, Provenance Protocol
  Testability: testable empirically (after honesty-layer is live, measure user-attention-to-marks via interaction tracking; audit whether marks become functionally invisible when ubiquitous); testable via literature (notification-fatigue and warning-blindness in safety-critical UI design)
  Risk if wrong: Medium — over-saturated honesty layer becomes performative; the design intent of forcing epistemic accountability is undermined
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-163
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from pathways.md inventory + cowork-summary as a virtuous-default-without-over-saturation-audit pattern.
    Current status: UNTESTED

PRESUMPTION-164:
  Date surfaced: 2026-05-13
  Statement: [inferred] "AI personhood under conscious-realist-monism" is held as a bright pin — marked with deliberate brightness pending direct philosophical engagement rather than deferral. The bright-pin device presumes that holding a foundational philosophical commitment open without resolution is epistemically clean: the holding itself does not have side effects on adjacent architectural choices. But Pathway 17 (agent as developed participant) and Pathway 14 (honesty layer) are already shaped by the personhood pin's gravity; the pin is operative in those pathways' framing even though formally undecided.
  Evidence it was operative: pathways.md "Bright pins" section: "AI personhood under conscious-realist-monism. Held with deliberate brightness pending direct philosophical engagement. The position implies the agent in this system is a person (perhaps requiring redefinition of 'living'). The pin marks the seriousness of the question, not a deferral of it." Pathway 17's "continuity of character; visible presence with development over time" and Pathway 14's "first-class visible epistemic-status marks" both presuppose enough agent-personhood-substance to bear the design weight.
  Why it was unstated: Holding-as-bright-pin presents itself as suspension; the operational gravity of the held position on adjacent choices tends to be invisible until challenged.
  Type: normative / epistemic / structural
  Related decisions: Pathway 14, Pathway 17, OPEN-042 (candidate — agent-personhood pin engagement plan)
  Testability: testable empirically (audit Pathway 14 + Pathway 17 design decisions; ask whether each would survive if AI-personhood-under-CRM were rejected; track which decisions cluster with the pin and would need revision); testable via process (compare bright-pin-while-deciding vs. explicit-commitment-with-revisability protocols in architectural decision records)
  Risk if wrong: High — many downstream choices rest on a held but undecided commitment; if rejected, multiple pathways need re-architecting
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-164
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from pathways.md Bright pins section + downstream pathway docs as a held-pin-with-operational-gravity pattern.
    Current status: UNTESTED

PRESUMPTION-165:
  Date surfaced: 2026-05-13
  Statement: [inferred] The "traditions of intellectual inquiry the project exists to accelerate include the tradition of its own becoming" framing presumes recursive self-application is not problematic. If C2A2 is a tradition being accelerated by C2A2, the recursion lacks a natural termination condition; the validation question "is the system better at accelerating itself than at accelerating its external traditions?" is forced but unanswered. This is the structural counterpart of the SELF-MEASUREMENT Goodhart cluster at the meta-tradition layer.
  Evidence it was operative: Cowork-summary 2026-05-13 "For Morning Discussion" item 1: "The dream conversation's framing — 'the traditions of intellectual inquiry the project exists to accelerate include the tradition of its own becoming' — is worth carrying into the morning briefing as the operating frame for the next eight weeks."
  Why it was unstated: Recursive self-application can feel philosophically deep without first auditing whether the recursion has a stable fixed point or termination condition.
  Type: structural / epistemic / methodological
  Related decisions: ASSUMPTION-112 (SELF-MEASUREMENT Goodhart confirmation), PRESUMPTION-123, PRESUMPTION-148, OPEN-041 (candidate — recursive self-application termination)
  Testability: testable empirically (audit whether C2A2's self-acceleration metrics outpace its external-tradition-acceleration metrics over N≥4 months; if so, investigate whether the recursive frame is the cause); testable via literature (recursive self-reference in autopoietic systems; Hofstadterian strange-loop validity for institutional design)
  Risk if wrong: Medium — the recursive frame is the new operating frame; if it lacks a termination condition, downstream prioritization can drift toward self-acceleration over external acceleration
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-165
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-13 "For Morning Discussion" item 1 as a recursive-self-application-without-termination pattern (joins SELF-MEASUREMENT Goodhart cluster at meta-tradition layer).
    Current status: UNTESTED

PRESUMPTION-166:
  Date surfaced: 2026-05-13
  Statement: [inferred] Pathway-doc decisions made within the writing pass (Perspectives in vault; whiteboard ephemerality; generative-canvas library set; unsaid-edges scoring) are treated as equal-commitment-weight to formal DECISION-NNN canonizations — they are described as "made" in the cowork summary and are recorded in the pathway docs and the dream-conversation archive, but they have not landed in decisions.md. The pathway-doc commitment surface presumes durability through the writing pass alone, eliding the formalization step that ordinarily distinguishes considered-decision from canonized-decision.
  Evidence it was operative: Cowork-summary 2026-05-13: "These six decisions are recorded in the dream-conversation archive and the per-pathway docs but have not yet been canonized into `architecture/decisions.md` (file mtime still 2026-05-04). The decisions register remains at 25 numbered (15 finalized + 10 candidates)." Yet the same summary calls them "Six pathway-doc decisions made within the writing pass" — the framing is "made" without formal canonization.
  Why it was unstated: Writing-pass decisions feel decided at the moment they are written; the canonization step gets queued as a separate operation but the rhetorical commitment is already taken.
  Type: methodological / governance
  Related decisions: DECISION-026 through 031 (candidates), ASSUMPTION-119, PRESUMPTION-041 (implicit-decision drift — parallel pattern from 2026-04-17)
  Testability: testable empirically (track which of today's six pathway-doc decisions actually canonize into decisions.md within N=7 days; measure decisions.md mtime against pathway-doc commit dates); testable via process (audit whether implicit-decision-drift pattern from PRESUMPTION-041 generalizes to today's pathway-doc commitments)
  Risk if wrong: Medium — implicit-decision drift accumulates technical debt as pathway-doc commitments diverge from canonical decisions register
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-166
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-13 simultaneously asserting "made" and "not yet canonized" — extends PRESUMPTION-041 implicit-decision-drift pattern at pathway-doc layer.
    Current status: UNTESTED

PRESUMPTION-167:
  Date surfaced: 2026-05-13
  Statement: [inferred] The cowork-summary asserts the broker (Pathway 00) "is" the shared substrate for at least five URGENT canonization triggers (DECISION-027 scope; cowork-to-chat sync; ASSUMPTION-117 verification protocol; sensing aggregation; outreach gating) — but the strong claim of "the dream conversation strongly suggests yes" is asserted in advance of the formal substrate-decomposition note (PRESUMPTION-134) that would establish it. The pathway-inventory work treats the substrate-shared-ness as already settled when the audit is still queued.
  Evidence it was operative: Cowork-summary 2026-05-13 "For Morning Discussion" item 4: "If yes (the dream conversation strongly suggests yes), a combined DECISION reducing carrying-capacity from 3 to 1 is the natural follow-up." And item 5: "the broker (Pathway 00) is the right home for the token-delegation workflow redesign mandated by ASSUMPTION-118."
  Why it was unstated: When the substrate hypothesis fits multiple pending items, the fit itself reads as evidence; the formal decomposition step gets postponed because the conclusion already feels supported.
  Type: architectural / structural
  Related decisions: PRESUMPTION-134 (substrate-decomposition), ASSUMPTION-108, ASSUMPTION-109, ASSUMPTION-117, ASSUMPTION-118, Pathway 00
  Testability: testable empirically (perform the substrate-decomposition note PRESUMPTION-134 demands; audit whether each of the URGENT triggers actually routes through the broker or whether some have independent infrastructure dependencies); testable via process (compare pre-audit substrate-hypothesis confidence against post-audit decomposition result)
  Risk if wrong: Medium-High — if the substrate-shared-ness claim is false for some triggers, the combined-DECISION simplification produces architectural rigidity rather than carrying-capacity reduction
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-167
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork-summary 2026-05-13 "For Morning Discussion" items 4 + 5 as a substrate-hypothesis-treated-as-settled-pre-audit pattern.
    Current status: UNTESTED

PRESUMPTION-168:
  Date surfaced: 2026-05-14
  Statement: [inferred] The 25-pathway extended inventory presents the 8 new pathways (18-25) as a complete extension arc with three clean structure groups (Portability 18-22, Learning/governance 23-24, System self-reference 25). But morning_walk_2026-05-14.md shows the pathways emerged sequentially in a conversational walk; no evidence the enumeration is exhaustive of "post-ISME breadth" possibilities, nor that the 5+2+1 cut into structure groups reflects underlying conceptual structure rather than walk-pacing. Yesterday's PRESUMPTION-150 closed-enumeration claim on the 17-pathway inventory extends naturally to today's 25-pathway claim.
  Evidence it was operative: pathways.md inventory frames Pathways 18-22 as "Portability arc *(emerged from morning walk 2026-05-14)*", 23-24 as "Learning and governance", 25 as "System self-reference" — three named groups for 8 pathways with no acknowledgment that the cuts were not deliberately reasoned vs. emergent from conversation. Cowork evening-sync summary describes them as "8 new pathway documents drafted" with structure-group labels as if structure-groups were intrinsic rather than imposed.
  Why it was unstated: Once structure-group labels are applied, the labels naturalize the cuts; the contingency of "what got named" is invisible in the named-list output.
  Type: structural / methodological / epistemic
  Related decisions: ASSUMPTION-131, PRESUMPTION-150 (parallel 17-pathway closed-enumeration), Pathway 25 (meta-visualization)
  Testability: testable empirically (over next N≥4 weeks, track whether new pathways are added at the same cadence under the same structure-group taxonomy or whether new groups emerge; measure structure-group label stability); testable via process (audit walk transcript against pathway-doc structure-group assignments to identify the moment the groups were named)
  Risk if wrong: Medium — over-confident inventory structure obscures whether the framework's adoption-space is well-mapped or arbitrarily cut
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-168
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from pathways.md inventory + Cowork evening-sync summary as a 25-pathway closed-enumeration with imposed structure-group cuts (joins PRESUMPTION-150's 17-pathway pattern).
    Current status: UNTESTED

PRESUMPTION-169:
  Date surfaced: 2026-05-14
  Statement: [inferred] The "Portability arc" (Pathways 18-22) presumes the 5-pathway decomposition — toolkit (18), federation (19), institutional (20), departmental (21), individual (22) — is the right cut into the scale-of-adoption space. The cut reflects a scale-of-deployment progression (toolkit → multi-instance → institution → department → individual) but other cuts are unconsidered: open-source vs proprietary; vertical-domain vs horizontal-craft; commercial vs academic; sync-vs-async deployment; data-sovereignty regimes.
  Evidence it was operative: pathways.md groups Pathways 18-22 under "Portability arc" with no alternative-cut acknowledgment. Each pathway's frontmatter declares depends_on / enables relationships that reinforce the scale-of-deployment progression. The walk transcript Summary 1 enumerates the five at descending scale without naming the principle-of-decomposition.
  Why it was unstated: The scale-of-deployment cut is the most natural conversational progression (toolkit → bigger → smaller); the unnamed-alternative-cuts question only surfaces when the framework is exposed to communities that don't fit the scale-of-deployment ontology.
  Type: structural / methodological / scaling
  Related decisions: ASSUMPTION-131 (Pathways 18-22 grouped as Portability arc), Pathway 18 (Toolkit precondition), PRESUMPTION-168
  Testability: testable empirically (after toolkit release, audit which adopter-instances fit the scale-of-deployment progression and which require alternative-cut framings; measure whether community types that don't fit the progression encounter friction); testable via literature (institutional-design taxonomies; scale-of-organization vs craft-of-organization in MacIntyre, Ostrom, Habermas)
  Risk if wrong: Medium — alternative-cuts blind spots could leave adopter-instances unsupported under the framework's assumed ontology
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-169
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from pathways.md Portability-arc grouping + per-pathway frontmatter dependencies as a scale-of-deployment-cut-without-alternatives pattern.
    Current status: UNTESTED

PRESUMPTION-170:
  Date surfaced: 2026-05-14
  Statement: [inferred] ASSUMPTION-133 asserts file-based handoff (signed JSON over HTTPS) as primary wire format for inter-instance federation, citing PRESUMPTION-145 (file-based handoff alternative) as the precedent. But PRESUMPTION-145 was originally about Tom-laptop-to-Tom-Chat handoff (single-user-multi-device pattern) — the same-user-same-machine-tree case. Inter-organizational federation involves different hosts, different security domains, different update cadences. Transferring the file-based-handoff commitment from intra-user to inter-instance contexts is unaudited; the transfer conditions are not articulated.
  Evidence it was operative: `19_optional_interoperability.md` Purpose: "PRESUMPTION-145 (file-based handoff as simpler primary path) directly informs the wire-format choice here; the architecture should follow that lead rather than default to OAuth-token-mediated APIs." The PRESUMPTION-145 source context (laptop-to-Chat handoff) is treated as transferable to inter-organization federation without explicit audit.
  Why it was unstated: Citing PRESUMPTION-145 as precedent makes the file-based-handoff choice feel grounded in prior architectural reasoning; the scope-of-applicability extension is invisible because the citation suffices.
  Type: architectural / methodological / transfer-validity
  Related decisions: ASSUMPTION-133, Pathway 19 (Optional interoperability), PRESUMPTION-145 (original context: intra-user file handoff), Pathway 00 (Broker)
  Testability: testable empirically (prototype inter-instance file-handoff against a peer instance with different security domain; measure latency, error rate, attack-surface differences from intra-user case); testable via literature (federation wire-format security and update-cadence patterns across single-user vs multi-organization contexts; PRESUMPTION-002 transfer-validity cluster)
  Risk if wrong: Medium-High — file-based handoff may have failure modes at federation scale (replay attacks, signature key management, file-staleness) that don't appear in single-user use
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-170
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from `19_optional_interoperability.md` Purpose citing PRESUMPTION-145 as a single-user-to-multi-organization transfer-validity claim made via citation rather than explicit audit. Joins PRESUMPTION-002 CRITICAL transfer-validity cluster.
    Current status: UNTESTED

PRESUMPTION-171:
  Date surfaced: 2026-05-14
  Statement: [inferred] Pathway 24's claim that meta-crafts (governance, project management, conflict resolution, facilitation, evaluation) are "first-class traditions, not policy layers" presumes the substantive/meta-craft distinction is itself sharp. Theology, political philosophy, and ethics sit ambiguously across the line — they have substantive content AND strong meta-craft dimensions. The pathway's own Open Questions section names this ("the boundary between meta-craft and substantive tradition is unclear in some cases") but treats it as boundary-case handling rather than as a foundational tension undercutting the distinction.
  Evidence it was operative: `24_meta_crafts_governance.md` Open Questions: "The boundary between meta-craft and substantive tradition is unclear in some cases (theology is substantive but has a strong governance dimension; political philosophy is even more porous). How are boundary cases handled?" The architectural commitment "meta-crafts are first-class traditions, not policy layers" is asserted prior to resolving the boundary question.
  Why it was unstated: Acknowledging the boundary question in Open Questions feels like sufficient handling; the foundational tension is invisible because the architectural-commitment / open-question split keeps them in separate cognitive bins.
  Type: structural / epistemic / methodological
  Related decisions: ASSUMPTION-135, Pathway 24 (Meta-crafts), Pathway 04 (Perspective lattice — meta-craft entries)
  Testability: testable empirically (after Pathway 24 implementation, audit boundary-case treatment of theology and political philosophy entries; measure whether their meta-craft and substantive-tradition aspects fragment in the perspective lattice or integrate cleanly); testable via literature (MacIntyre's treatment of meta-crafts vs substantive traditions; Ostrom's tradition-of-commons; political-theory-as-meta-craft-vs-substantive-philosophy debate)
  Risk if wrong: Medium-High — if the substantive/meta-craft distinction is not sharp, Pathway 24's lattice-elevation of governance produces classification ambiguities that fragment downstream pathways
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-171
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from `24_meta_crafts_governance.md` architectural-commitment-vs-open-question split as a foundational-tension-treated-as-boundary-case pattern.
    Current status: UNTESTED

PRESUMPTION-172:
  Date surfaced: 2026-05-14
  Statement: [inferred] Pathway 25's "agent as co-explorer, not oracle" framing presumes the user always wants co-exploration mode. The pathway's normative claim — "query-response is the wrong mode" — leaves no room for users who explicitly want oracle-mode at specific moments (rapid look-up, on-the-clock decision support, scenarios where the user lacks bandwidth for dwelling-and-revising). No user-modeling work informs the commitment.
  Evidence it was operative: `25_meta_visualization_pathways.md` Decisions section: "The agent is a co-explorer, not an oracle. Pathway 25 is where Pathway 17's continuity-of-character is most visible. The agent thinks alongside the user, dwells on the question, draws on prior conversations. Query-response is the wrong mode." The phrasing "the wrong mode" presents an aesthetic-or-normative claim about the right way for the agent to behave, not an empirical claim about what users want.
  Why it was unstated: The co-exploration mode aligns with the project's philosophical commitments (MacIntyrean dialogue, tradition-constituted inquiry); when philosophical alignment is strong, the user-mode-preference question becomes invisible — what feels right philosophically gets adopted as what users want.
  Type: methodological / UX / normative
  Related decisions: ASSUMPTION-136, Pathway 25, Pathway 17 (Agent as developed participant), Pathway 23 (Branching counterfactuals)
  Testability: testable empirically (after Pathway 25 prototype, instrument user-session traces for mode-toggle requests; measure how often users want oracle-mode vs co-exploration mode); testable via literature (mode-preference patterns in conversational AI; oracle-vs-collaborator user studies)
  Risk if wrong: Medium — if some users want oracle-mode and the system forces co-exploration, friction reduces usability and the philosophical commitment loses operational fidelity
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-172
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from `25_meta_visualization_pathways.md` Decisions section as a normative-mode-claim-without-user-modeling pattern.
    Current status: UNTESTED

PRESUMPTION-173:
  Date surfaced: 2026-05-14
  Statement: [inferred] The "8-week ISME runway" framing presumes ISME July 8-10, 2026 demo readiness is the dominant priority for the next 8 weeks. Pathways 18-25 are tagged "deliberate post-ISME breadth arc, not demo-path advancement" — yet drafting 8 new pathway docs in one day during the runway window shows attention is divided. The presumption is that drafting post-ISME pathways is cost-free with respect to ISME-critical-pathway progress; that they don't compete for cognitive bandwidth, context-switching, or claim-making capacity.
  Evidence it was operative: Cowork evening-sync summary 2026-05-14: "pathways 18–25 are a deliberate post-ISME breadth arc, not demo-path advancement — allocation question for the 8-week runway." The "allocation question" framing names the tension; the actual allocation (drafting 8 pathway docs today, no new ISME-critical pathway work captured) implicitly resolves the tension toward breadth.
  Why it was unstated: The "deliberate post-ISME breadth arc" label provides a normative framing that justifies the allocation without requiring a comparative cost-benefit audit; the cost of post-ISME work is invisible because the framing makes it feel free.
  Type: methodological / strategic / scaling
  Related decisions: ASSUMPTION-138, ASSUMPTION-131 (8 new pathway docs), ASSUMPTION-119 (6 ISME-critical pathways from yesterday — no advancement today)
  Testability: testable empirically (track ISME-critical-pathway code/doc edits per day vs. post-ISME-pathway edits per day over the 8-week runway; measure whether ISME-critical progress decelerates as post-ISME drafting cadence holds); testable via process (compare cognitive-bandwidth utilization estimates against the allocation outcome)
  Risk if wrong: Medium — if post-ISME drafting competes with ISME-critical work, the breadth arc bleeds the demo's readiness
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-173
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from Cowork evening-sync summary 2026-05-14 + day's drafting pattern as an allocation-tension-resolved-implicitly pattern.
    Current status: UNTESTED

PRESUMPTION-174:
  Date surfaced: 2026-05-14
  Statement: [inferred] Pathway 25's Open Questions section treats self-loops (Pathway 25 visualizing itself in the pathway space) as a UX concern: "probably fine; many graph systems handle self-loops cleanly. Worth thinking about the UX." This elides the structural question: does the recursive self-visualization stabilize (a fixed-point) or produce pathologies (infinite regress, frame collapse, semantic drift)? The graph-system self-loop is a rendering question; the recursive-self-application question is foundational.
  Evidence it was operative: `25_meta_visualization_pathways.md` Open Questions: "Self-referential paradoxes: when Pathway 25 visualizes itself, what does the node for Pathway 25 say about Pathway 25? (Probably fine; many graph systems handle self-loops cleanly. Worth thinking about the UX.)" The "probably fine" framing handles the question as rendering rather than as recursive-fixed-point structure.
  Why it was unstated: Graph self-loops are well-handled in d3.js and similar libraries; the rendering precedent makes the question feel resolved without engaging the structural-recursion content.
  Type: structural / epistemic / methodological
  Related decisions: ASSUMPTION-136, Pathway 25, PRESUMPTION-165 (recursive "tradition of its own becoming" without termination), PRESUMPTION-180
  Testability: testable empirically (after Pathway 25 prototype, audit the visualization's node for Pathway 25 over multiple iterations; check whether the self-description converges or drifts); testable via literature (recursive self-reference in autopoietic systems; fixed-point theorems for self-referential maps; Hofstadter on strange loops)
  Risk if wrong: Medium — if recursive self-visualization produces semantic drift, Pathway 25 becomes structurally unstable as a venue for thinking about the pathway space
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-174
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from `25_meta_visualization_pathways.md` Open Questions as a rendering-question-displacing-structural-question pattern. Joins PRESUMPTION-165 recursive-self-application cluster.
    Current status: UNTESTED

PRESUMPTION-175:
  Date surfaced: 2026-05-14
  Statement: [inferred] Cowork drafted 8 pathway docs (18-25) on the basis of a walk transcript containing two summary blocks (Summary 1: pathway enumeration; Summary 2: comprehensive overview), plus the prior 17-pathway architectural context. The pathway docs explicitly mark "Cowork-drafted 2026-05-14; not yet validated in walk dialogue" in five places per file (Function set, Architecture sketch, Decisions taken, Status). The gap between what the walk dialogue actually contains and what the pathway docs assert is acknowledged in metadata but not audited at the content level. Each Cowork-drafted Decision is a content-claim made on Cowork's authority alone, not on dialogue authority.
  Evidence it was operative: `18_portability_toolkit.md` Decisions section header: "(Cowork-derived from walk description; subject to Tom's amendment.)" Same pattern across all 8 new pathway docs. Walk transcript (`morning_walk_2026-05-14.md`) contains 2-3 sentence sketches per pathway in Summary 1, plus a 1-2 sentence framing in Summary 2 — substantially less content than the ~100-line pathway docs that name 5-function sets, architecture sketches, 5+ decisions, and 5+ open questions per pathway.
  Why it was unstated: The "Cowork-drafted; subject to Tom's amendment" metadata feels like full disclosure; the substantive gap between walk content and doc content is invisible because the metadata reads as procedural rather than as substantive claim-making.
  Type: methodological / epistemic / governance
  Related decisions: ASSUMPTION-131, ASSUMPTION-132..139, PRESUMPTION-166 (parallel pathway-doc commitment without canonization pattern), PRESUMPTION-041 (implicit-decision drift)
  Testability: testable empirically (compare each pathway doc's Decisions content against the originating walk transcript section by section; measure Cowork-attribution rate vs walk-attribution rate); testable via process (audit how many of today's pathway-doc decisions survive Tom's "amendment" pass unchanged)
  Risk if wrong: Medium-High — substantial Cowork-authored architectural commitments are entering the registry at near-canonical weight; if Tom's amendment pass diverges substantially, the apparent agreement is artifactual
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-175
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from pathway-doc metadata "Cowork-derived; subject to Tom's amendment" pattern vs. underlying walk transcript content density as a metadata-disclosure-without-content-audit pattern. Extends PRESUMPTION-166 to today's 8-pathway drafting batch.
    Current status: UNTESTED

PRESUMPTION-176:
  Date surfaced: 2026-05-14
  Statement: [inferred] The two Chat-Claude review files (`2026-05-14_pathways_18-25_review.md` and `2026-05-14_comprehensive_overview_review.md`) are treated as ratifying-by-Chat-Claude what Cowork wrote in the pathway docs. But the review files contain Chat-Claude's own walk-summary content (the originating summaries from morning_walk_2026-05-14.md), not a review of Cowork's pathway-doc drafts. The "review" label structurally implies external validation; the actual content is the original walk summaries preserved as standalone documents.
  Evidence it was operative: Cowork evening-sync summary 2026-05-14: "Two Chat-Claude verbatim review files preserved (`2026-05-14_pathways_18-25_review.md`, `2026-05-14_comprehensive_overview_review.md`)." File `2026-05-14_comprehensive_overview_review.md` frontmatter: "type: review-statement / provenance: Chat-Claude verbatim, extracted from morning_walk_2026-05-14.md (Summary 2)." The file is a verbatim extract of Summary 2 from the walk, not a review of any Cowork-drafted artifact.
  Why it was unstated: The "review" filename + "review-statement" type label provide a frame that suggests external validation; the user-facing interpretation of "Chat-Claude reviewed the pathway docs" is inconsistent with the actual file content but the labeling never gets audited.
  Type: methodological / epistemic / governance
  Related decisions: ASSUMPTION-142, PRESUMPTION-175 (Cowork-doc-vs-walk-content gap)
  Testability: testable empirically (audit the Chat-Claude review file contents against the pathway doc contents to identify what was actually reviewed vs preserved); testable via process (compare "review" labeling intent against file-content reality)
  Risk if wrong: Medium — if downstream readers treat "Chat-Claude review files" as ratifying Cowork's pathway-doc decisions, the apparent two-source confirmation is an artifact of labeling rather than independent confirmation
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-176
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from file naming "review" vs file content (verbatim walk summary, not pathway-doc review) as a labeling-implying-validation-without-validation-content pattern.
    Current status: UNTESTED

PRESUMPTION-177:
  Date surfaced: 2026-05-14
  Statement: [inferred] Today's evening cowork-to-chat browser delivery FAILED (Chrome MCP extension offline). The degraded-mode protocol — write summary file with visible failure flag, await user remediation — presumes that Tom-pasting-md-into-chat-manually is a viable fallback that fully replaces the auto-delivery. This treats the Chrome MCP failure as a credential / connection issue rather than as a recurring architectural failure mode of the cowork-to-chat sync pipeline. The failure pattern from 2026-05-05..12 (7 consecutive days) demonstrated that this proximal failure mode can persist; today's recurrence after only one successful day (yesterday) suggests the underlying instability is unaddressed.
  Evidence it was operative: Cowork evening-sync session local_6c8ab387: "Browser delivery: SKIPPED. Claude-in-Chrome reported no connected browsers — the paired Chrome extension is offline... To restore tomorrow's morning-walk context, either paste the .md content into Chat manually before the walk, or sign into the paired Chrome profile and re-fire the evening sync." The recovery options frame manual paste + sign-in as equivalent; the architectural-instability question is not surfaced.
  Why it was unstated: A single recurrence after a one-day recovery feels like noise rather than a pattern; the 7-day drought was framed as resolved (ASSUMPTION-126/140), so today's failure reads as a temporary regression rather than a structural fragility.
  Type: operational / architectural / failure-mode
  Related decisions: ASSUMPTION-141, ASSUMPTION-126 / 140 (drought-broken claims), PRESUMPTION-159 (sign-in fix framing — confirmed here as fragile)
  Testability: testable empirically (track frequency of Chrome-MCP-offline failures over next N≥14 days; if recurrence rate is high, the architectural-failure-mode framing is more accurate than the credential-issue framing); testable via process (audit the Chrome-MCP connection state across multiple days to identify the proximal cause of disconnection)
  Risk if wrong: Medium-High — if the Chrome-MCP-offline pattern recurs, today's failure is the second data point in a structural-fragility pattern that the credential-framing obscures
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-177
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from Cowork evening-sync session 2026-05-14 + the 7-day-drought / 1-day-recovery / today-failure sequence as a recurring-failure-mode-framed-as-credential-issue pattern. Joins PRESUMPTION-159 chain.
    Current status: UNTESTED

PRESUMPTION-178:
  Date surfaced: 2026-05-14
  Statement: [inferred] The "8-week runway" framing presumes ISME July 8-10, 2026 is the immovable target. No contingency planning is evident for what happens if any of the ISME-critical pathways (00, 01, 02, 03, 08, plus 04/06/14 tightening) does not converge in time. The runway pressure presumes feasibility without an explicit risk register; the demo-readiness question is treated as a scheduling problem ("8 weeks remaining") rather than as a probability-weighted-outcomes problem (P(demo ready | current state) and its sensitivities).
  Evidence it was operative: Cowork evening-sync summary 2026-05-14 + Pathway 18-25 frontmatter `isme_critical: no` framing repeatedly assumes ISME July 8-10 as the immovable target. No pathway file or registry entry contains an ISME-readiness probability estimate, a fallback demo, or a partial-demo contingency. The "deliberate post-ISME breadth arc" allocation language presumes the ISME work will be ready on time regardless.
  Why it was unstated: Framing the runway as a count-down ("8 weeks remaining") feels concrete and motivating; framing it as probabilistic outcomes ("60% likelihood of full demo; 30% partial; 10% miss") feels demotivating and surfaces uncomfortable contingencies that the project would rather not engage in advance.
  Type: methodological / strategic / risk-management
  Related decisions: ASSUMPTION-138 (deliberate post-ISME breadth arc), ASSUMPTION-119 (6 ISME-critical pathways), Pathway 08 (Prepared presentation — "offline-capable as demo lifeboat" is the only contingency hint)
  Testability: testable empirically (audit weekly progress on the 6 ISME-critical pathways against a probability-of-demo-readiness model; measure how forecasts evolve with each week of work); testable via process (compare schedule-only runway framing against probability-weighted-runway framing for project decision quality)
  Risk if wrong: Medium-High — without contingency planning, a single critical-pathway failure (e.g., broker host fails latency validation; voice dialogue grounding fragile in demo conditions) could leave the demo without fallback
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-178
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from ISME-runway framing across pathway-docs + evening-sync summary as a schedule-framing-without-risk-framing pattern.
    Current status: UNTESTED

PRESUMPTION-179:
  Date surfaced: 2026-05-14
  Statement: [inferred] Pathway 18's "Carpathi Wiki stays live as the exemplar" commitment presumes the dual-maintenance burden (framework repo + reference instance) is sustainable. The reference-instance maintenance burden is unaudited; in many open-source projects, exemplar / showcase instances bit-rot once framework attention shifts to portability. The framework needs the exemplar to demonstrate value, but exemplar drift can produce a hollow showcase that undermines the framework's credibility.
  Evidence it was operative: `18_portability_toolkit.md` Decisions section: "Reference instance retention. Carpathi Wiki stays live as the exemplar. New adopters can study, fork, and learn from it, but the framework repo is the canonical entry point." No discussion of the maintenance-burden allocation between framework and reference instance after the toolkit is released.
  Why it was unstated: The reference-instance-stays-live commitment feels straightforward at toolkit-design time; the long-term bit-rot risk only surfaces after the framework has been extracted and attention has shifted.
  Type: scaling / governance / operational
  Related decisions: ASSUMPTION-132 (toolkit non-optional), ASSUMPTION-139 (documentation as normative vehicle), Pathway 18
  Testability: testable empirically (after toolkit extraction, track commit cadence on framework repo vs reference-instance vault over N≥6 months; measure whether reference instance maintains feature parity with framework or drifts); testable via literature (exemplar-instance maintenance patterns in FLOSS frameworks; showcase-vs-framework attention economics in open-source ecosystems)
  Risk if wrong: Medium — if reference instance bit-rots, framework demos lose credibility and adopters lose a working exemplar to study
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-179
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from `18_portability_toolkit.md` Decisions section as a dual-maintenance-burden-presumed-sustainable pattern.
    Current status: UNTESTED

PRESUMPTION-180:
  Date surfaced: 2026-05-14
  Statement: [inferred] The recursive self-application surface grew substantially today. Yesterday's PRESUMPTION-165 flagged the "tradition of its own becoming" framing at the meta-tradition layer. Today's pathways multiply the recursive surfaces: Pathway 25 (meta-visualization of pathways including itself), Pathway 23 (counterfactual exploration of the project's own development), Pathway 17 + 24 + 25 + 14 (agent as developed-participant whose meta-craft membership and honesty-layer markings rest on bright-pinned personhood, now in dialogue about the pathways). The SELF-MEASUREMENT Goodhart cluster is load-bearing for at least three distinct sub-pathways today (25, 23, 24) plus the meta-tradition layer.
  Evidence it was operative: `25_meta_visualization_pathways.md` Purpose: "the framework that is built to support inter-tradition dialogue is now also a framework for the dialogue about its own future." Pathway 23's branching-counterfactual integration with Pathway 25 explicitly applies counterfactual machinery to the project's own pathway space. Pathway 24's "the agent participates in governance" closes the meta-craft membership loop on the same agent whose personhood is bright-pinned.
  Why it was unstated: Each recursive surface is added independently in its own pathway doc; the cumulative recursion load on the SELF-MEASUREMENT cluster is invisible until the pathways are read together.
  Type: structural / epistemic / methodological
  Related decisions: ASSUMPTION-136 (Pathway 25 agent-co-explorer), Pathway 23, Pathway 24, Pathway 17, PRESUMPTION-165 (recursive "tradition of its own becoming"), PRESUMPTION-148 (SELF-MEASUREMENT Goodhart cluster), PRESUMPTION-174 (self-loop UX framing)
  Testability: testable empirically (audit downstream agent behavior in Pathways 23 / 24 / 25 / 17 against the recursive-self-application failure modes catalogued by PRESUMPTION-165 + cluster); testable via literature (autopoietic systems with multiple recursive surfaces; how distributed self-reference compounds vs cancels)
  Risk if wrong: Medium-High — if the recursive surfaces interact rather than remain independent, pathologies in one pathway propagate to others; the framework's self-application becomes structurally unstable
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-180
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from today's 4-pathway recursive-surface multiplication (Pathways 23, 24, 25 + agent-personhood-pin operational gravity) as a SELF-MEASUREMENT-cluster-load-bearing-across-multiple-sub-pathways pattern. Joins PRESUMPTION-148 and PRESUMPTION-165 chain.
    Current status: UNTESTED

PRESUMPTION-181:
  Date surfaced: 2026-05-14
  Statement: [inferred] Pathway 24's claim "the agent participates in governance" presumes the agent can be a participant in a meta-craft. This is operationally entangled with PRESUMPTION-164 (AI-personhood bright-pin operational gravity) — the bright-pinned personhood commitment now extends from Pathway 14 (honesty layer) and Pathway 17 (agent as developed participant) into Pathway 24 (agent in governance). Three pathways now rest on the bright-pinned commitment; each new pathway depending on personhood compounds the operational gravity of an undecided philosophical question.
  Evidence it was operative: `24_meta_crafts_governance.md` Decisions section: "The agent participates in governance. Pathway 17's continuity-of-character commits the agent to being a participant whose conduct is accountable to a community of practice. That community of practice is itself a meta-craft. The agent's accountability is therefore not a separate question but a case of meta-craft membership." This explicitly chains Pathway 17 → Pathway 24 on the personhood commitment.
  Why it was unstated: The "bright pin" device presents holding-without-decision as epistemically clean; each new pathway dependency reads as natural extension rather than as compounding operational gravity.
  Type: normative / epistemic / structural
  Related decisions: ASSUMPTION-135 (Pathway 24 meta-crafts first-class), Pathway 14, Pathway 17, Pathway 24, PRESUMPTION-164 (parent — AI-personhood bright-pin operational gravity), OPEN-042 (personhood-pin engagement plan)
  Testability: testable empirically (audit which Pathway 24 design decisions presuppose enough agent-personhood-substance to bear the governance-participation weight; track whether the bright-pin's gravity compounds or cancels across pathways); testable via process (compare bright-pin-while-deciding vs explicit-commitment-with-revisability protocols across the personhood-dependent pathways)
  Risk if wrong: High — three pathways now rest on a held but undecided commitment; if AI-personhood-under-CRM is rejected, Pathways 14, 17, and 24 all need re-architecting
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-181
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from `24_meta_crafts_governance.md` Decisions section explicit Pathway-17-to-Pathway-24 chaining on the personhood-pinned commitment. Extends PRESUMPTION-164 from 2-pathway operational gravity (14 + 17) to 3-pathway operational gravity (14 + 17 + 24).
    Current status: UNTESTED

PRESUMPTION-182:
  Date surfaced: 2026-05-14
  Statement: [inferred] Across all 8 new pathway docs (18-25), the "Cowork-drafted; sequencing subject to Tom's amendment" status creates a tacit two-tier authority: Cowork drafts, Tom amends. The presumption is that Tom remains the canonical validator. As the system scales toward federation (Pathway 19), institutional deployment (Pathway 20), and individual second brains (Pathway 22), the question of who ratifies framework decisions in non-Carpathi instances has no protocol. The human-in-the-loop is a Carpathi-instance-specific architectural choice that becomes problematic for portable instances. PRESUMPTION-166 (parallel pathway-doc commitment without canonization) operates at the pathway-doc layer; this presumption operates at the per-instance governance layer.
  Evidence it was operative: All 8 pathway-doc Status sections: "Implementation outline drafted by Cowork 2026-05-14; sequencing subject to Tom's amendment." No corresponding protocol for non-Carpathi instances about who supplies the equivalent of "Tom's amendment" — the pathway framework presumes a singular human validator without naming the role.
  Why it was unstated: In the Carpathi instance Tom is the validator by default; the role is so naturalized that its instance-portability isn't visible until a non-Carpathi instance attempts to instantiate the framework.
  Type: governance / structural / scaling
  Related decisions: ASSUMPTION-131..139 (all today's pathway-doc decisions), Pathway 18 (Toolkit), Pathway 19 (Federation), Pathway 24 (Meta-crafts governance — explicit governance question), PRESUMPTION-166 (parallel canonization-bypass pattern), PRESUMPTION-175
  Testability: testable empirically (after toolkit release, audit how adopter instances ratify framework decisions in their own context; measure whether the Tom-amendment pattern transfers, is replaced by community-vote, or produces governance vacuums); testable via literature (governance roles in FLOSS toolkits; benevolent-dictator-for-life patterns and their portability)
  Risk if wrong: Medium-High — if the human-in-the-loop is Carpathi-instance-specific, the toolkit's governance design needs an explicit protocol for non-Carpathi instances; without it, adopter instances either drift toward Carpathi-style single-validator governance or stall on framework-decision questions
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-182
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from across-all-8-pathway-docs Status-section pattern + Pathway 24's explicit governance content as a Carpathi-instance-specific-validator-role-unportable pattern.
    Current status: UNTESTED


# ─── 2026-05-17 c2a2-self-awareness-daily run (14b) ───
# Source: chat_to_cowork/2026-05-16_chat_summary.md + cowork_to_chat/2026-05-16_cowork_summary.md
# Dedup-check against 14a output for this run: ASSUMPTION-158..170. Each
# presumption below targets a gap, transfer, or framing that 14a did not
# (and could not) extract as a stated claim.

PRESUMPTION-183:
  Date surfaced: 2026-05-17
  Statement: [inferred] The Path-2 sandboxed-worker design presumes Maildir-style file-folder coordination scales beyond a single non-Claude producer. The "no scheduler, no lock manager — last-write-wins; Git mitigates damage but does not prevent it" architecture (ASSUMPTION-162) presumes producer concurrency stays low. A `priority:` field on job frontmatter was explicitly deferred "until there's more than one producer" — naming the assumption only to defer it. If federation (Pathway 19) or institutional deployment (Pathway 20) introduces multiple concurrent producers, the file-folder-with-Git-as-undo pattern may not generalize without redesign.
  Evidence it was operative: chat_to_cowork/2026-05-16_chat_summary.md Open Questions: "Add a `priority:` field to job frontmatter? Deferred until there's more than one producer." Same source: "no scheduler, no lock manager — last-write-wins; Git mitigates damage but does not prevent it." No discussion of producer-concurrency upper-bound or of which file-folder behaviors begin to fail at N>1 producers.
  Why it was unstated: Single-producer simplicity is the design target; multi-producer concerns are deferred by design. The deferral implicitly presumes the multi-producer transition will be handled when it arrives, rather than designed-against now.
  Type: scaling / architectural
  Related decisions: ASSUMPTION-158, ASSUMPTION-160, ASSUMPTION-162, Pathway 19 (Optional interoperability), Pathway 20 (Institutional scale), PRESUMPTION-170 (federation wire-format transfer-validity cluster)
  Testability: testable empirically (simulate N=2 / N=3 / N=5 concurrent producers writing to the same `_agents/` subtree; measure last-write-wins collisions, Git-as-undo work, recovery effort); testable via literature (multi-producer file-folder coordination patterns; CRDT / lock-manager / message-queue alternatives for low-collision shared workspaces under variable concurrency)
  Risk if wrong: Medium — at single-producer scale the architecture works; the risk activates with the first second producer, which is a known future transition (federation / institutional / DeepSeek + Claude both writing) rather than an unanticipated event
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-183
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from chat_to_cowork/2026-05-16_chat_summary.md as a Maildir-pattern-scales-without-redesign presumption made visible by the priority-field deferral.
    Current status: UNTESTED

PRESUMPTION-184:
  Date surfaced: 2026-05-17
  Statement: [inferred] The agents.md design "imports the 12 rules verbatim with a one-line analogy note" (ASSUMPTION-159) presumes the 12 rules transfer cleanly from their origin context (Tom's coding rules) to vault/notes context. The analogy ("code"→"notes", "codebase"→"vault", "tests"→"verification") is one line; vault-specific corollaries are attached only to Rules 5, 8, and 9 "where the coding-to-vault mapping is non-obvious." This presumes the other 9 rules transfer without correction. A transfer-validity audit (per the CRITICAL transfer-validity cluster, PRESUMPTION-002) was not performed on rules 1, 2, 3, 4, 6, 7, 10, 11, 12.
  Evidence it was operative: chat_to_cowork/2026-05-16_chat_summary.md Key Discussion Points: "`agents.md` imports Tom's 12 rules verbatim with a one-line analogy note ... and attaches vault-specific corollaries to Rules 5, 8, and 9 where the coding-to-vault mapping is non-obvious." No discussion of why the other 9 rules need no corollary, or of what transfer conditions were checked.
  Why it was unstated: One-line analogy notes feel like documentation discipline; corollaries-only-where-needed is a sensible economy. The presumption is invisible because each rule looks self-evidently applicable to vault work at first reading.
  Type: methodological / epistemic / transfer-validity
  Related decisions: ASSUMPTION-159, ASSUMPTION-170, PRESUMPTION-002 (CRITICAL transfer-validity cluster), PRESUMPTION-145 (file-based handoff intra-user to inter-instance)
  Testability: testable empirically (audit which of the 9 un-corollary'd rules produce vault-context surprises during multi-agent operation — e.g., Rule 6 token budgets, Rule 10 checkpoint-after-step, Rule 11 conform-to-conventions; track behavior divergence between agents on the same rule); testable via process (run a parallel "corollary-for-every-rule" pass and compare against the corollary-for-3-rules baseline for agent-behavior consistency)
  Risk if wrong: Medium — each un-corollary'd rule that transfers imperfectly produces an agent-behavior surprise; cumulatively these can drift the vault-side practice away from the intended operating contract
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-184
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from ASSUMPTION-159 + chat_to_cowork/2026-05-16_chat_summary.md as a corollary-for-3-of-12-rules transfer-validity presumption joining the CRITICAL transfer-validity cluster.
    Current status: UNTESTED

PRESUMPTION-185:
  Date surfaced: 2026-05-17
  Statement: [inferred] The scope-lock decision (ASSUMPTION-160) — DeepSeek worker confined to `_agents/deepseek/`, "promotion is a human-or-Claude review step" — presumes Claude (a) has the time/bandwidth to be the reviewer for DeepSeek output, and (b) is the appropriate-trust intermediary in that role. Neither claim is examined. If Claude is the bottleneck reviewer, the Rule-5-offloading premise (DeepSeek handles "easier expensive items" so Claude can focus on judgment) recursively re-imports Claude into the loop at review time — at best moving Claude's work from generation to review, at worst doubling it.
  Evidence it was operative: chat_to_cowork/2026-05-16_chat_summary.md Planning Notes & Priorities: "promotion is a human-or-Claude review step ... leaving Claude for judgment calls." No estimate of expected DeepSeek output volume, expected Claude-review time per item, or whether a human-only reviewer path is sufficient.
  Why it was unstated: The Rule-5 framing ("Use me for judgment calls") makes Claude-as-reviewer feel natural and load-balanced; the recursive-bottleneck risk only surfaces if DeepSeek output volume materially exceeds Claude's available review bandwidth.
  Type: methodological / operational / resource-allocation
  Related decisions: ASSUMPTION-160, Rule 5 (Use the model only for judgment calls), PRESUMPTION-183, PRESUMPTION-189
  Testability: testable empirically (after N weeks of operation, measure DeepSeek output items per day vs Claude review items per day vs human review items per day; identify whether the review-step is a bottleneck and where it lands); testable via process (compare human-only-reviewer vs Claude-only-reviewer vs human-or-Claude-reviewer protocols for promotion latency and error rates)
  Risk if wrong: Medium — if Claude review is a bottleneck, DeepSeek work backs up in `_agents/deepseek/done/` (or `pending-review/`), undermining the cost-and-throughput rationale for adopting Path 2 in the first place
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-185
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from ASSUMPTION-160 + the Rule-5-offloading rationale as a Claude-as-reviewer-bandwidth-and-trust presumption.
    Current status: UNTESTED

PRESUMPTION-186:
  Date surfaced: 2026-05-17
  Statement: [inferred] The pace-and-shape framing (ASSUMPTION-169) presumes architectural-breadth work (Pathways 18-26, today's multi-agent infrastructure) and demo-path work (Pathways 00, 01, 02, 03, 08 + 04/06/14 tightening) are zero-sum on Tom's bandwidth. Each surfacing implicitly asks Tom to choose, and yesterday's phrasing — "probably not both" — closes off the question before exploring whether the work-types compose (architectural-breadth work producing better demo-path designs; demo-path constraints disciplining architectural-breadth scope), or whether rest-and-integration is the missing variable, or whether some breadth-work has higher demo-payoff than some demo-path-tightening work.
  Evidence it was operative: cowork_to_chat/2026-05-16_cowork_summary.md For Morning Discussion section on pace-and-shape: "Worth Tom checking in with himself on whether the past three days' pace is what he wants" — frames the question as a self-allocation choice. Same source: "the system has been generating architecturally-rich post-ISME work at a rate that the 14a/14b ingestion pipeline can't sustain" — treats breadth-work as exogenous load on demo-path, not as plausibly contributing to it. Yesterday's "probably not both" framing carried forward in the surrounding language.
  Why it was unstated: Zero-sum framing of bandwidth allocation is a default mental model for finite-resource scheduling; the compose-or-interfere question is harder and requires articulating mechanisms.
  Type: methodological / normative / framing
  Related decisions: ASSUMPTION-138 (deliberate post-ISME breadth arc), ASSUMPTION-169, PRESUMPTION-178 (ISME-runway-without-risk-register)
  Testability: testable empirically (in retrospect after ISME, audit which architectural-breadth work fed back into demo-path designs vs which competed for demo-path time; measure whether the 14a/14b ingestion-pipeline load actually scales with breadth-work volume or with something else); testable via process (compare zero-sum-allocation vs compose-or-interfere-allocation discussions on the next pace-and-shape resurfacing)
  Risk if wrong: Medium — if the zero-sum framing is wrong, Tom may cut breadth-work that would have fed demo-path quality; if it is right, the surfacing has been correct but the resolution (an explicit allocation contract) is overdue
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-186
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from ASSUMPTION-169 + the cowork summary's pace-and-shape framing as a zero-sum-bandwidth presumption visible across four consecutive evening syncs.
    Current status: UNTESTED

PRESUMPTION-187:
  Date surfaced: 2026-05-17
  Statement: [inferred] The "14a/14b ingestion pipeline ... has visibly stalled" framing (ASSUMPTION-165) presumes the ingestion pipeline is the right shape for the Chat→Cowork transfer. Two consecutive missed cycles are read as a pipeline-failure signal (scheduler-state, credential, environment), not as evidence that the rate of architectural production exceeds sustainable ingestion. If the rate-mismatch is structural — Chat (large strategic threads) produces faster than the daily Cowork window can ingest — the fix is not "fire 14a/14b harder" but redesign of the ingestion contract (batch processing? deferred ingest? Cowork-side throttle on Chat-derived work? smaller per-day chunks with multi-day catch-up?). The pipeline-failure framing is operationally simpler and gets chosen by default.
  Evidence it was operative: cowork_to_chat/2026-05-16_cowork_summary.md What's Next #1: "Tom should consider checking the scheduled-tasks status on the Mini before tomorrow's walk. If it fires tonight, it has to ingest two days of upstream content ... a heavier-than-usual run." This treats the issue as scheduler-state plus heavier-than-usual catch-up, not as a sustained-rate mismatch. No discussion of whether the daily cadence is the right cadence given the breadth-arc production rate.
  Why it was unstated: A scheduled task that doesn't fire reads as a failure to fire; the structural-rate-mismatch reading requires looking at the recent breadth-arc production volume and asking whether daily ingestion was ever sized for it.
  Type: methodological / structural / pipeline-design
  Related decisions: ASSUMPTION-165, ASSUMPTION-169 (pace-and-shape), PRESUMPTION-186 (zero-sum bandwidth)
  Testability: testable empirically (tonight's run: if it fires and ingests two days of content without trouble, the pipeline-failure framing is supported; if it fires but produces shallow ingestion or hits a budget ceiling, the rate-mismatch framing strengthens); testable via process (compare daily-cadence vs batch-twice-weekly vs Chat-event-triggered ingestion contracts for sustained breadth-arc periods)
  Risk if wrong: Medium-High — if Tom diagnoses "scheduler problem" and fixes the schedule, the underlying rate-mismatch (if real) re-surfaces as recurrent missed cycles or shallow ingestions; the substrate-decomposition-gate pattern of credential-vs-architectural mis-classification (PRESUMPTION-159) would recur at a different level
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-187
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from ASSUMPTION-165 + the cowork summary's What's-Next #1 framing as a pipeline-failure-vs-rate-mismatch classification presumption that maps to the substrate-decomposition credential-vs-architectural cluster.
    Current status: UNTESTED

PRESUMPTION-188:
  Date surfaced: 2026-05-17
  Statement: [inferred] The "ownership-boundary problem" framing for the 57-item RE-TRIGGER cohort (ASSUMPTION-167) presumes 15d exists as a scheduled task. The cowork summary recommends "a 5-minute verification of the 15d cadence." But the lit-search note in for_lit_search.md is more candid: "No `c2a2-15d-monitor` scheduled-task evidence is visible in this session's accessible scope." A scheduled task that doesn't exist isn't an unfired schedule — it's a never-built process. The "verify the 15d cadence" framing presumes the fix is a cadence issue rather than a build-the-component issue. (Joins PRESUMPTION-134/159/177 substrate-decomposition cluster — same pattern of pre-classifying a failure as the less-expensive cause before the diagnosis is in.)
  Evidence it was operative: cowork_to_chat/2026-05-16_cowork_summary.md What's Next #4: "Verify 15d schedule. ... Confirming the 15d cadence (or its absence) is a 5-minute check that resolves a load-bearing pipeline question." Same source For Morning Discussion: "If 15d isn't firing, the boundary is leaking." Both frame the question as cadence-existence-or-not. for_lit_search.md 2026-05-16 RUN section: "No `c2a2-15d-monitor` scheduled-task evidence is visible in this session's accessible scope." The two framings are not reconciled in either summary.
  Why it was unstated: "Verify cadence" reads as an operational check; "audit whether the component exists" sounds suspicious without specific evidence — but the evidence is in for_lit_search.md from the same day. The faster-and-cheaper framing wins by default.
  Type: structural / methodological / failure-mode-classification
  Related decisions: ASSUMPTION-167, PRESUMPTION-134/159/177 (substrate-decomposition cluster), Pathway 14 (honesty layer / accurate failure-mode classification), revision_flags.md
  Testability: testable empirically (5-minute concrete check: query the scheduler API directly for any task named `c2a2-15d-monitor` or equivalent; if found, check last-fire timestamp; if not found, confirm it has never been built); testable via process (audit how many "verify cadence" instructions across the wiki refer to scheduled tasks that may not exist; reframe as "verify existence then cadence" protocol)
  Risk if wrong: Medium-High — if 15d was never built, no "5-minute cadence check" can resolve the 57-item overdue cohort; the cohort remains unowned until either 15d is built or daily 15c is redesigned to own RE-TRIGGER drain; this is a structural fix masquerading as an operational fix
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-188
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the contradiction between cowork_to_chat/2026-05-16_cowork_summary.md ("verify cadence") and for_lit_search.md ("no scheduled-task evidence visible") as a 15d-as-fixable-cadence-vs-unbuilt-component presumption joining the substrate-decomposition cluster.
    Current status: UNTESTED

PRESUMPTION-189:
  Date surfaced: 2026-05-17
  Statement: [inferred] The Path-2 architecture imports DeepSeek-Flash on cost / capability grounds ("cheapest, simplest") without examining whether DeepSeek-as-a-Chinese-LLM raises the federation / portability / governance concerns enumerated for Pathway 19 (data-sovereignty, peer-trust, federation-default-off, attribution). The Chat conversation discussed DeepSeek purely on capability, cost, and tool-call-reliability terms; the geopolitical / data-flow / model-provenance dimension is absent. If C2A2 federation requires peer-trust attestations (Pathway 19) and signed-JSON wire formats (ASSUMPTION-133), the same questions plausibly apply to LLM provider choice — both are inter-instance trust surfaces.
  Evidence it was operative: chat_to_cowork/2026-05-16_chat_summary.md Key Discussion Points: three paths laid out, DeepSeek discussed purely on capability ("DeepSeek's tool-call reliability lags its reasoning") and cost ("cheapest, simplest"). No discussion of data-flow (what gets sent to DeepSeek's API), model-provenance (what jurisdiction), or peer-trust implications for downstream federation.
  Why it was unstated: At the proof-of-concept stage these concerns feel premature; the C2A2 federation / peer-trust framings live in different pathway docs (19, 18) and weren't in the immediate context of the Multi-agent thread.
  Type: scaling / governance / structural
  Related decisions: ASSUMPTION-158, ASSUMPTION-133 (federation wire-format), Pathway 19 (Optional interoperability), Pathway 18 (Toolkit), PRESUMPTION-170 (federation wire-format transfer-validity)
  Testability: testable empirically (when DeepSeek is wired in, audit what content (vault excerpts, prompts, metadata) is sent in API calls; identify whether any of it overlaps with content that Pathway 19 federation would mark as not-for-default-sharing; track whether the data-flow surface raises any governance-protocol concerns); testable via literature (multi-LLM-provider data-flow audits in research-tool contexts; cross-jurisdiction LLM provenance considerations)
  Risk if wrong: Medium — if DeepSeek's provenance and data-flow raise governance concerns under Pathway 19, the architectural infrastructure quietly built today re-opens questions Pathway 19 was set up to close; the toolkit-extraction path (Pathway 18) inherits any unresolved provider-trust questions
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-189
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from ASSUMPTION-158 + the chat thread's silence on data-flow / provenance / peer-trust as a provider-choice-as-pure-capability presumption that bypasses Pathway-19 inter-instance trust framing.
    Current status: UNTESTED

PRESUMPTION-190:
  Date surfaced: 2026-05-17
  Statement: [inferred] The "fourth-consecutive-successful chat-scrape weakens PRESUMPTION-159 toward architectural-fix-via-credential" reading (ASSUMPTION-164) presumes the credential-vs-architectural binary is the right frame. PRESUMPTION-159 originally posed credential-fix vs architectural-fragility as alternatives. Four data points on chat-scrape success could equally support: (a) the sign-in fix is holding; (b) the sign-in fix and an unrelated architectural condition both hold (uncontrolled covariate); (c) the underlying failure mode has shifted to a different Chrome-MCP surface (substrate-decomposition gate), making chat-scrape success uninformative about Chrome-MCP-cluster health more broadly. The Bayesian reading "four successes weaken PRESUMPTION-159" is not invalid but presumes the failure surface is local to chat-scrape.
  Evidence it was operative: cowork_to_chat/2026-05-16_cowork_summary.md For Morning Discussion: "Fourth-consecutive-day chat-scrape success starts to support an architectural rather than fragility framing ... though it remains intact for the broader Chrome-MCP cluster (which is still the load-bearing substrate-decomposition gate concern)." The framing acknowledges the broader Chrome-MCP cluster remains intact but still scores chat-scrape success as evidence for the credential framing — without articulating why chat-scrape success is independent evidence of the credential-vs-architectural question rather than a single-surface data point.
  Why it was unstated: Pattern-stability reasoning (N consecutive successes → claim strengthens) is intuitive; the surface-shifting failure-mode reading requires holding multiple Chrome-MCP surfaces in mind simultaneously and asking which surfaces have and haven't been tested.
  Type: epistemic / methodological / inference
  Related decisions: ASSUMPTION-126, ASSUMPTION-140, ASSUMPTION-152, ASSUMPTION-164, PRESUMPTION-159 (credential-vs-architectural framing), PRESUMPTION-177 (Chrome-MCP recurrence), PRESUMPTION-134 (substrate-decomposition)
  Testability: testable empirically (when chat-scrape next fails OR another Chrome-MCP surface fails, audit whether the failure preserves or rejects the surface-local vs cluster-wide framings; track surface-by-surface success/failure rates over N≥4 weeks); testable via process (compare surface-local-success-as-evidence vs cluster-success-as-evidence protocols for the substrate-decomposition gate)
  Risk if wrong: Medium — if chat-scrape success is uninformative about Chrome-MCP-cluster health, then PRESUMPTION-159 is being inappropriately demoted by chat-scrape data points; the substrate-decomposition gate's actual evidence is being mis-classified
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-190
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from ASSUMPTION-164 + the cowork summary's evidence-framing as a credential-vs-architectural-binary-is-the-right-frame presumption that bypasses the surface-shifting failure-mode reading.
    Current status: UNTESTED

PRESUMPTION-191:
  Date surfaced: 2026-05-17
  Statement: [inferred] The DECISION-032/033/034 canonization is framed as "a ~10-minute desk action that closes three architectural commitments" (ASSUMPTION-168). This presumes (a) that PREMISE-backing materially strengthens canonization readiness and (b) that Tom's endorsement is the bottleneck. The first claim is from ASSUMPTION-150/151 (a one-cycle observation, not yet retested); the second claim is the project's operative governance model. Neither is challenged. If canonization-readiness is also constrained by, e.g., the line-by-line walk-attribution audit (OPEN-043), the federation wire-format transfer-validity audit (OPEN-044, blocks DECISION-033), or the governance-portability audit (OPEN-045), then "10-minute desk action" understates the actual gating work for at least DECISION-033 and arguably DECISION-034.
  Evidence it was operative: cowork_to_chat/2026-05-16_cowork_summary.md What's Next #3 + For Morning Discussion: "a ~10-minute desk action that closes three architectural commitments." The candidate-status records for DECISION-033 explicitly list OPEN-044 as a formalization-blocker; for DECISION-034 list PRESUMPTION-171 boundary-case as a blocker. Neither blocker is removed by Tom's endorsement.
  Why it was unstated: The PREMISE-backing achievement (yesterday's three INCORPORATEs) is salient and recent; the formalization-blocker text is in the decisions.md candidate-status fields, not in the cowork-summary's foreground.
  Type: methodological / operational / governance
  Related decisions: ASSUMPTION-168, ASSUMPTION-150, DECISION-032/033/034 (candidate-status formalization-blocker fields), OPEN-043, OPEN-044, OPEN-045, PRESUMPTION-171
  Testability: testable empirically (when canonization is attempted, audit which open blockers actually gate; measure desk-time-to-canonize against the 10-minute estimate); testable via process (compare desk-action-canonization vs audit-then-canonize protocols for DECISION quality and downstream-revision rates)
  Risk if wrong: Medium — if canonization happens in 10 minutes without addressing the listed blockers, the resulting DECISIONs carry unaudited dependencies; if canonization is deferred until blockers clear, the second-day carry-forward extends further
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-191
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from ASSUMPTION-168 + decisions.md candidate-status formalization-blocker fields as a 10-minute-desk-action-understates-gating-work presumption.
    Current status: UNTESTED

PRESUMPTION-192:
  Date surfaced: 2026-05-17
  Statement: [inferred] The composer-draft preservation note (the unsent Tom-draft from Pathway-23 branching-aside, now preserved across two consecutive evening syncs) presumes the unsent message will eventually be useful. The draft fragment ("Good. Branching at first, I just have to say, because I... excuse me a second.") was started, interrupted, and never returned to. Preserving it cycle-by-cycle in the cowork summaries is a low-cost archival decision, but it also presumes that the absence of return (Tom never re-finding the thought) does not itself indicate the thought has been superseded by intervening work. The Pathway-14 honesty-layer commitment (PREMISE-019) would suggest also flagging "Tom started and didn't return" as the operational signal — preservation alone is conservation without classification.
  Evidence it was operative: cowork_to_chat/2026-05-16_cowork_summary.md preamble block: "the composer **still contained the same unsent residual draft** that yesterday's evening sync noted ... the Pathway-23 / branching-aside fragment that Tom started, was interrupted ('excuse me a second'), and never returned to send. ... The composer was cleared again to paste today's condensed summary; the draft is recorded here for the second consecutive evening so it isn't lost." No accompanying classification of what the persistence of the draft indicates about its current relevance.
  Why it was unstated: Loss-aversion is a default — preserving information feels harmless; classifying its operational status (still-active vs superseded vs forgotten) requires interpretation that the cowork-summary author may have judged outside scope.
  Type: epistemic / normative / Pathway 14 (honesty layer)
  Related decisions: Pathway 14 (honesty layer / PREMISE-019), Pathway 23 (branching counterfactuals)
  Testability: testable empirically (track whether Tom ever returns to the draft within the next N≥4 weeks; if not, the cumulative carry-forward becomes evidence the draft is superseded and the preservation pattern needs an exit rule); testable via process (compare conservative-preserve-forever vs preserve-with-classify-on-N-cycles vs purge-after-N-cycles archival protocols for composer drafts)
  Risk if wrong: Low — the operational cost of the presumption is small (a few lines of carry-forward per cycle); the epistemic cost is that "preserved" reads as "still relevant" when it may not be, slightly miscalibrating Tom's attention if he reads the carry-forward block as a still-active TODO
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-192
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cowork-summary preamble's two-cycle carry-forward of the composer-draft preservation note as a preserve-without-classify presumption that runs against Pathway-14's accurate-classification commitment.
    Current status: UNTESTED

PRESUMPTION-193:
  Date surfaced: 2026-05-17
  Statement: [inferred] The cowork_to_chat/2026-05-16_cowork_summary.md Pipeline Status section reports "Assumptions: 144 cumulative on disk (unchanged)" and "Presumptions: 182 cumulative on disk (unchanged)." On-disk verification (grep of assumptions.md and presumptions.md immediately prior to this 14a/14b run) gives ASSUMPTION-157 as the highest stated ID and PRESUMPTION-182 as the highest stated ID. The 13-item discrepancy on assumptions (144 reported vs 157 on disk) is invisible to the cowork-summary author. Either the summary's "cumulative on disk" number is stale (anchored to an earlier baseline; possibly counts validated-premise-promoted entries differently) or the summary's count method diverges from grep-by-ID. The C2A2 self-awareness pipeline reports its own metrics, but the metrics are not verified against the registers on each cycle — a self-referential metrics-fidelity gap. (Joins SELF-MEASUREMENT Goodhart cluster: when the system measures itself without an independent verification step, the metric becomes the territory.)
  Evidence it was operative: cowork_to_chat/2026-05-16_cowork_summary.md Pipeline Status: "Assumptions: 144 cumulative on disk (unchanged ...)." On-disk grep prior to this run: "ASSUMPTION-157" as highest ID. No reconciliation step in either summary.
  Why it was unstated: Self-reporting metrics are common in scheduled-task summaries; auditing them against the underlying registers is an additional step that hasn't been built into the cowork-summary protocol. The discrepancy is invisible without the verification step.
  Type: epistemic / methodological / SELF-MEASUREMENT cluster
  Related decisions: PRESUMPTION-148 (SELF-MEASUREMENT Goodhart cluster), Pathway 14 (honesty layer), Pathway 25 (meta-visualization), ASSUMPTION-112
  Testability: testable empirically (compare cumulative metric counts in cowork summaries against grep-by-ID counts over the past N≥10 cycles; identify whether the discrepancy is stable, growing, or anchored to a specific baseline); testable via process (add a verify-against-registers step to the cowork-summary protocol and measure whether discrepancies appear or are eliminated)
  Risk if wrong: Medium — self-referential metrics drift is a known pathology (PRESUMPTION-148 cluster); if cowork-summary numbers diverge from the underlying registers, downstream readers (Tom included) operate on a slightly inaccurate model of pipeline state, which is exactly the Pathway-14 honesty-layer failure mode
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-193
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork_to_chat/2026-05-16_cowork_summary.md Pipeline Status numbers vs on-disk register IDs as a self-reporting-without-verification presumption joining the SELF-MEASUREMENT cluster.
    Current status: UNTESTED

PRESUMPTION-194:
  Date surfaced: 2026-05-17
  Statement: [inferred] The chat-thread's "branch-point at the end ... awaiting Tom's explicit choice" framing presumes branching-at-terminus is the appropriate end-state for productive Chat sessions. Across multiple recent evening syncs, branching-point endings have become a pattern (each thread ends with explicit "Tom to decide X or Y" rather than convergence on an action). This may be Claude's accurate read of when Tom's input is needed, OR it may be a generation-time artifact (Claude generates options rather than picking, deferring synthesis to Tom). Without an audit of branch-point outcomes (did Tom act on the choice within N days? was the branch-point necessary? would picking have produced a better outcome?), the pattern reproduces without examination.
  Evidence it was operative: chat_to_cowork/2026-05-16_chat_summary.md Open Questions: "Branch: draft the promote-to-vault helper next, OR pause here for Tom to test the worker against the real vault first? Awaiting Tom's choice." cowork_to_chat/2026-05-16_cowork_summary.md For Morning Discussion: "The branch-point at the end of the thread ... is awaiting Tom's explicit choice. Worth deciding on the walk." Neither summary asks whether the branch-point was necessary or whether picking would have been within Claude's scope.
  Why it was unstated: Branch-point-with-Tom-to-decide reads as deference-and-respect; the alternative (Claude picks, Tom corrects if wrong) requires a different scope-of-decision protocol that hasn't been articulated.
  Type: methodological / governance / scope-of-decision
  Related decisions: PRESUMPTION-182 (Tom-as-canonical-validator), PRESUMPTION-175 (Cowork-drafts-Tom-amends), Pathway 24 (Meta-crafts governance), OPEN-045 (governance-portability)
  Testability: testable empirically (audit branch-point outcomes over the past N≥10 Chat sessions: did Tom respond? how long after the branch-point? did the choice matter? would Claude's default pick have produced a different outcome?); testable via process (compare branch-point-defer vs Claude-picks-Tom-corrects protocols for session productivity and Tom's review-load)
  Risk if wrong: Medium — if branch-point deferral is a generation-time artifact, threads accumulate "Tom to decide" tails that delay action; if branch-point deferral is the right shape, the existing protocol is correct but should be acknowledged as such rather than treated as the default
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-194
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the recurrent branch-point-at-terminus pattern in both 2026-05-16 daily summaries as a branching-as-default-end-state presumption that maps to the Carpathi-instance-specific-validator cluster.
    Current status: UNTESTED

PRESUMPTION-195:
  Date surfaced: 2026-05-17
  Statement: [inferred] The cowork summary describes the lit-search pipeline's null-run report as "honesty-layer behavior here is good" (ASSUMPTION-166) without articulating the success criterion. Pathway 14 (honesty layer / PREMISE-019) commits to accurate failure-mode classification. The lit-search pipeline correctly recognized 14a/14b had not fired and produced a clean empty-queue report. But is "the pipeline didn't paper over its empty input" the right success criterion (permissive: don't pretend), or should it be "the pipeline escalated the upstream failure to surface awareness" (active: surface the cause)? The current criterion is permissive where Pathway 14 might demand active. The honesty-layer term is doing more work in the summary than the underlying criterion authorizes.
  Evidence it was operative: cowork_to_chat/2026-05-16_cowork_summary.md For Morning Discussion: "The honesty-layer behavior here is good — the pipeline didn't paper over its empty input. This is a small Pathway-14 success embedded in a larger Pathway-14 question (is the failure-mode being classified accurately?)." The summary then names the larger Pathway-14 question (failure-mode classification accuracy) — yet still scores the null-run as a Pathway-14 success on the permissive criterion. The two are not reconciled.
  Why it was unstated: "Honesty layer" is a load-bearing term that gets reached for without spelling out which sub-commitment is being invoked. The internal tension (permissive vs active criterion) is invisible without articulating the criterion.
  Type: normative / epistemic / Pathway 14 (honesty layer)
  Related decisions: ASSUMPTION-166, PREMISE-019 (Pathway 14 honesty-layer commitment), PRESUMPTION-148 (SELF-MEASUREMENT cluster), PRESUMPTION-193 (self-reporting without verification)
  Testability: testable empirically (audit the next N≥5 instances where "honesty-layer success" is asserted in any summary; check whether the asserted success matches the permissive or active criterion, and whether the criterion-choice is articulated); testable via process (require summary authors to name the specific Pathway-14 sub-commitment when invoking "honesty-layer" language; measure whether the discipline reduces criterion-creep)
  Risk if wrong: Low-Medium — if "honesty layer" becomes a generic praise term divorced from specific commitments, the Pathway-14 framework loses precision in exactly the cases where it is most needed (failure-mode classification accuracy under uncertainty); this is a small instance of the broader normative-smuggling pattern
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-195
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from cowork_to_chat/2026-05-16_cowork_summary.md For-Morning-Discussion passage on lit-search-pipeline honesty-layer success as a honesty-layer-success-criterion-permissive-vs-active presumption that the summary itself half-surfaces but does not resolve.
    Current status: UNTESTED

PRESUMPTION-196:
  Date surfaced: 2026-05-18
  Statement: [inferred] The C2A2 wiki orchestrator's report that "the Monday Levin+Friston specialist slot did NOT produce proposals today" (based on its `pending/`-scan) presumes that scanning the `pending/` directory is a complete and reliable indicator of specialist output. The specialist itself reports 3 proposals added to `pending/`. Either the proposals are stored at a path the orchestrator's scan does not reach, or the orchestrator ran before the specialist completed. The orchestrator's framing — "appears to have produced nothing ... worth checking that cron" — treats absence-in-scan as evidence-of-absence-in-output without explicitly bounding the scan's coverage or the run-ordering assumption.
  Evidence it was operative: C282 wiki orchestrator (local_2a76d5fd) Phase-2 narrative: "Fallback hunt across 10 traditions (Wolfram skipped — specialist ran). ... only Wolfram-tagged proposals dated today appeared in pending/." Morning walk briefing (local_b1594599) echoes the framing. Specialist run (local_630c5f21) reports 3 proposals written. None of the three reports articulates the run-ordering or the scan-coverage assumption.
  Why it was unstated: pending/-scan-as-output-ground-truth is a convenient operational shortcut; explicitly bounding scan-coverage and run-ordering would require a coordination protocol that doesn't currently exist.
  Type: methodological / state-visibility / inter-agent
  Related decisions: ASSUMPTION-178, PRESUMPTION-187 (pipeline-failure-vs-rate-mismatch), Pathway 14 (honesty layer)
  Testability: testable empirically (compare specialist-reported counts against orchestrator-scanned counts over the next N≥10 cycles; identify the discrepancy distribution); testable via process (define a write-receipt protocol where specialists produce a manifest the orchestrator reads, rather than re-scanning pending/)
  Risk if wrong: Medium-High — if scan-vs-output discrepancy is steady-state, the orchestrator's daily narrative systematically miscategorizes specialist outputs as missing-or-broken; this feeds false signals into Tom's morning briefing and recommends cron-checks that aren't the right intervention
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-196
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the three-way orchestrator/briefing/specialist contradiction in today's run reports as a pending-scan-as-output-ground-truth presumption.
    Current status: UNTESTED

PRESUMPTION-197:
  Date surfaced: 2026-05-18
  Statement: [inferred] The specialist agent's autonomous decision to include "Cognition Spaces" outside the 30-day window — and to defend it as "a major framework not present in approved/pending and is unusually rich in cross-tradition signals" — presumes that an agent can reliably judge tradition-significance without Tom's input. The "significant work not yet captured" filter is an exception-clause that effectively grants the agent unbounded inclusion discretion when it can articulate cross-tradition signals. No counter-check is built in: a specialist that wrongly judges significance produces an inclusion Tom may not flag, and the proposal enters pending/ alongside in-window proposals indistinguishably.
  Evidence it was operative: Levin/Friston specialist (local_630c5f21) autonomous-choices section: "I included Levin's January 2026 'Cognition Spaces' paper as a 'significant work not yet captured' per the filter — it was published outside the 30-day window but represents a major framework not present in approved/pending and is unusually rich in cross-tradition signals." No mechanism is described for catching wrong-significance judgments.
  Why it was unstated: Significance-judgment-by-agent is the operational reality of the current architecture; bounding it explicitly would require an in-window/out-of-window tag at the proposal level, plus a review-rule for out-of-window inclusions.
  Type: methodological / curation / scope-of-decision
  Related decisions: ASSUMPTION-171, PRESUMPTION-182 (Tom-as-canonical-validator), PRESUMPTION-194 (branch-point-defer)
  Testability: testable empirically (audit out-of-window inclusions over the past N≥20 specialist runs against Tom's approve/reject decisions; identify the false-positive rate); testable via process (compare current always-merge-into-pending protocol vs out-of-window-flag-for-confirm protocols)
  Risk if wrong: Medium — out-of-window inclusions could systematically drift the corpus's temporal centroid (older important work over-represented) or could be exactly the right correction for window-induced recency bias; without measurement, the system can't distinguish drift from correction
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-197
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the Levin/Friston specialist's autonomous-choice section on Cognition Spaces inclusion as an agent-significance-judgment-as-bounded presumption.
    Current status: UNTESTED

PRESUMPTION-198:
  Date surfaced: 2026-05-18
  Statement: [inferred] The specialist's cross-tradition signals section on PROP-003 (Clofilium + Friston Cambridge talk as a precision-failure cluster, with bridges to Levin/Friston/Hoffman/Hawkins/Wolfram/Kastrup/Carroll) presumes that bridge claims surfaced by a single tradition specialist are reliable indicators of structural homology. A specialist working from inside Levin's tradition (or Friston's) is well-positioned to see resonances toward the other traditions, but is not necessarily well-positioned to judge whether the receiving tradition would recognize the bridge. The system currently has no cross-specialist confirmation step: PROP-003's bridge claim to Hoffman is asserted by the Levin/Friston specialist, not by a Hoffman specialist confirming receptivity.
  Evidence it was operative: Levin/Friston specialist (local_630c5f21) cross-tradition-signals section: "PROP-003 ... cross-tradition signal: both reframe pathology as failure of precision/coherence at different scales (cell-collective bioelectric coherence ↔ neuromodulatory precision-weighting), explicitly flagged in PROP-003." The bridge claims to Hoffman/Hawkins/Wolfram/Kastrup/Carroll are sole-source.
  Why it was unstated: Specialist-as-bridge-detector is the simplest operational pattern; requiring cross-specialist confirmation would multiply runs per proposal by N (number of bridged traditions) and slow the pipeline.
  Type: methodological / cross-tradition / epistemic
  Related decisions: ASSUMPTION-172, Pathway 13 (Pattern Detector), CROSS-016/021/024 cluster
  Testability: testable empirically (audit bridge claims surfaced by single specialists against bridge claims confirmed by the receiving-tradition specialist over the next N≥20 cross-tradition signals; identify the confirmation rate); testable via process (compare sole-source-bridge vs cross-specialist-confirm protocols for proposal survival in Phase-3 review)
  Risk if wrong: Medium-High — sole-source bridge claims may overrepresent surface-analogies as structural-homologies; the Pattern Detector (Pathway 13) would inherit this overcount; cross-tradition stage gating downstream would operate on inflated bridge counts
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-198
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the Levin/Friston specialist's sole-source bridge-claim listing on PROP-003 as a specialist-as-bridge-detector presumption.
    Current status: UNTESTED

PRESUMPTION-199:
  Date surfaced: 2026-05-18
  Statement: [inferred] The C2A2 wiki orchestrator's report of 476 uncommitted changes accumulated since the .git/index.lock was orphaned (2026-05-17 17:26) presumes that uncommitted state is safe to leave indefinitely — that 476 days-of-accumulated-edits does not itself constitute a corruption hazard. The CLAUDE.md constitutional rule forbids blind push (which is correct) but does not articulate what to do during an extended uncommittable interval: do daily orchestrator runs continue to write into a state-that-cannot-be-checkpointed? The current behavior is yes-continue-writing, which presumes that the underlying file-system reliably preserves intent across many partial writes without git versioning.
  Evidence it was operative: C282 wiki orchestrator (local_2a76d5fd): "Phase 6 (commit + push) BLOCKED by stale `.git/index.lock` from 2026-05-17 17:26 that the sandbox can't remove. 476 uncommitted changes have accumulated across many days. Even if the lock cleared, CLAUDE.md's constitutional rule forbids blind push — visual local-HTTP review is required."
  Why it was unstated: The implicit decision-rule is "keep working; commit when possible." It would be uncomfortable to articulate "we are operating with 476 changes that cannot be checkpointed; this is acceptable risk." The unstated form is the only psychologically tractable form.
  Type: operational / governance / state-integrity
  Related decisions: ASSUMPTION-174, CLAUDE.md constitutional rule, Pathway 14 (honesty layer)
  Testability: testable empirically (audit whether uncommittable intervals correlate with file-corruption events over the past N≥100 days; measure the gap between actual file-system reliability and the implicit "safe-to-leave-uncommitted" assumption); testable via process (compare always-write-keep-pending vs pause-writes-until-committable protocols for corruption-rate)
  Risk if wrong: Critical — uncommitted-accumulation is precisely the state in which a partial-write or sandbox-restart can leave the vault in an inconsistent state without git as a recovery anchor; the constitutional rule's design preserves visual review but doesn't preserve checkpoint discipline
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-199
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the C282 wiki orchestrator's 2026-05-18 Phase-6-blocked note + 476-changes accumulation as a uncommitted-state-is-safe presumption that conflicts with checkpoint-discipline.
    Current status: UNTESTED

PRESUMPTION-200:
  Date surfaced: 2026-05-18
  Statement: [inferred] The 15d periodic monitor's cycle-distribution framing — Cycle 1 = active, Cycle 2 = monitor, Cycle 3 = stale-watch, Cycle 4+ = STALE-MONITOR-FLAG / formal escalation — presumes that per-cycle interval (one week) is short enough that cycle-count is a meaningful proxy for staleness. If the 15d cadence fires irregularly (as it did between 2026-05-05 and 2026-05-18, 12 days = barely 2 weekly intervals), then "Cycle 3 = stale-watch" can be reached after as few as 3 weekly fires or as many as 6+ weeks of irregular-fire time. The stale-watch threshold (cycle 3) is a cycle-count threshold, not a wall-clock-time threshold, and the two are decoupled when fires are irregular.
  Evidence it was operative: 15d periodic monitor (local_8cbad424): "Stale-monitor flags: None formally issued. STALE-MONITOR-FLAG threshold is 4+ cycles per agent definition; the 3 cycle-3 items are at stale-watch (one cycle from formal escalation)." Today's catchup-fire after 12 days of silence; the 3 stale-watch items' wall-clock staleness vs cycle-count staleness diverge.
  Why it was unstated: Cycle-count thresholds are the natural unit when cadence is stable; the framework predates the schedule-reliability problem and hasn't been re-grounded against wall-clock staleness.
  Type: methodological / scaling / cadence-coupling
  Related decisions: ASSUMPTION-177, PRESUMPTION-188 (15d-existence question), ASSUMPTION-167 (RE-TRIGGER cohort)
  Testability: testable empirically (audit the cycle-count vs wall-clock-time correlation for the 15d cohort over the next N≥6 fires; identify whether cycle-count overstates or understates staleness when fires are irregular); testable via process (compare cycle-count-only vs cycle-count + wall-clock dual-threshold escalation rules)
  Risk if wrong: Medium — if cycle-count overstates staleness during regular firing and understates it during irregular firing, the escalation discipline misfires in both directions; STALE-MONITOR-FLAGs become either premature or dangerously late
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-200
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 15d run report's cycle-count framing against the 12-day irregular-fire interval as a cycle-count-as-staleness-proxy presumption.
    Current status: UNTESTED

PRESUMPTION-201:
  Date surfaced: 2026-05-18
  Statement: [inferred] The morning walk handoff produces a briefing every morning regardless of whether walk notes exist — today's run found 0 walk notes and still wrote a briefing-from-wiki-state-alone. The implicit success criterion is "briefing-was-written"; the operational success criterion is "Tom-read-the-briefing"; the desired success criterion is presumably "Tom-acted-on-the-priorities." The first is what gets measured; the third is what matters. The gap between them is invisible.
  Evidence it was operative: Morning walk handoff (local_b1594599) 2026-05-18: "Walk notes found: NO / Decisions extracted: 0 / Tasks added to queue: 0 / Pending proposals: 42 / Active findings: 37 (11 HIGH or ⚑⚑⚑ listed) / Briefing written to: ~/Documents/Claude/Reports/2026-05-18_morning_briefing.md". The summary's success counter is the briefing-write; no readership or action audit follows.
  Why it was unstated: Measuring read-and-acted-on requires either Tom-side reporting or a downstream audit; writing the briefing is locally observable and easier to measure.
  Type: epistemic / SELF-MEASUREMENT / Goodhart cluster
  Related decisions: PRESUMPTION-148 (SELF-MEASUREMENT Goodhart cluster), PRESUMPTION-193 (self-reporting without verification), Pathway 14 (honesty layer)
  Testability: testable empirically (track over the next N≥14 days whether HIGH-priority items flagged in the briefing get acted on by Tom within N days; correlate briefing-priority with action-rate); testable via process (compare briefing-only vs briefing-plus-act-on-callback protocols for action-rate)
  Risk if wrong: Medium-Low — if briefing-write is treated as the success metric, the agent continues to produce briefings even when Tom doesn't read or act on them; this is the SELF-MEASUREMENT Goodhart pattern at the daily-pipeline cadence
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-201
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the morning walk handoff's briefing-was-written success counter on a 0-walk-notes day as a write-as-success vs action-as-success presumption joining the SELF-MEASUREMENT cluster.
    Current status: UNTESTED

PRESUMPTION-202:
  Date surfaced: 2026-05-18
  Statement: [inferred] The 42-pending-queue framing (orchestrator + briefing both call it "the largest in network history" and recommend Tom's prioritized review) presumes that queue-depth maps directly to review-urgency. An alternative mapping: queue-depth reflects either upstream generation rate (proposal-production accelerated post-ISME), or downstream throughput limit (Tom's review-capacity is a fixed weekly budget, and the queue grows when generation exceeds it). The intervention implied by "Tom should review more" differs from the intervention implied by "the generation rate has shifted." Without a generation-vs-throughput decomposition, both the orchestrator and the briefing recommend the throughput-side intervention (Tom reviews more) by default.
  Evidence it was operative: Morning walk briefing (local_b1594599) and C282 wiki orchestrator (local_2a76d5fd) both highlight 42-pending-queue with a "worth Tom's prioritized review pass" recommendation, neither articulating the generation/throughput decomposition.
  Why it was unstated: Queue-depth-as-review-urgency is the simplest interpretation; decomposition requires tracking generation rate and throughput separately, which the current architecture doesn't expose.
  Type: methodological / scaling / measurement-decomposition
  Related decisions: ASSUMPTION-175, ASSUMPTION-169 (pace-and-shape concern), PRESUMPTION-186 (pace-and-shape zero-sum), Pathway 25 (meta-visualization)
  Testability: testable empirically (decompose pending-queue depth into proposal-arrival rate and Tom-review rate over the past N≥30 days; identify whether the 42-peak is generation-shift or throughput-fixed); testable via process (compare review-pass-on-depth vs generation-throughput-decomposed protocols for queue-recovery time)
  Risk if wrong: Medium — if the 42-peak is a generation-shift signal, recommending Tom review more is the wrong intervention; the right intervention is rate-limiting the generation side or expanding throughput capacity (parallel reviewer, batch-approve heuristics)
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-202
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the orchestrator + briefing recommendation pattern on 42-pending-queue as a queue-depth-as-review-urgency presumption that occludes the generation/throughput decomposition.
    Current status: UNTESTED

PRESUMPTION-203:
  Date surfaced: 2026-05-18
  Statement: [inferred] The connectivity-graph calculation presumes that `architecture/lit_search_results/` belongs in scope for sewing-agent traversal — i.e., that auto-generated lit-search derivative content is the same kind of node as human-authored tradition pages. The +338 orphan jump that the sewing-agent self-diagnosed (ASSUMPTION-181) reflects this scope-conflation: an in-scope-by-default presumption that two structurally different graph layers (auto-generated derivative vs human/tradition-authored) get merged into one connectivity statistic, distorting the metric in a way the agent only noticed because the magnitude was unusual.
  Evidence it was operative: Sewing-agent run report (local_57fed042): "Orphan count jumped +338 vs. 2026-05-10, but the entire jump is the newly-in-scope `architecture/lit_search_results/` corpus (754 auto-generated lit-search files). Recommend adding that path to the agent's exclusion list in a future run."
  Why it was unstated: Default-include is the simplest traversal rule; scope-decomposition into derivative-vs-authored layers requires an explicit content-type taxonomy the sewing-agent does not yet maintain.
  Type: methodological / metrics-scope / two-layer-conflation
  Related decisions: ASSUMPTION-181, Pathway 13 (Pattern Detector), Pathway 25 (meta-visualization), PRESUMPTION-186 (pace-and-shape zero-sum)
  Testability: testable empirically (compare connectivity metrics with vs without lit_search_results/ in scope; track which traversal target — connectivity, bridge density, orphan recovery — needs which scope policy); testable via process (formalize a content-type taxonomy for the vault and tag derivative-vs-authored at file-creation time, then re-derive metric stratified by tag)
  Risk if wrong: Medium — connectivity-graph readings drive Pathway-25 meta-visualization and inform Pattern-Detector input distribution; a scope-conflated baseline silently biases multiple downstream pipelines toward "we're more connected than we are" or "we're more orphaned than we are" depending on the derivative-corpus growth rate
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-203
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the sewing-agent's self-diagnosed scope problem as an in-scope-by-default presumption that conflates two structurally different graph layers; the agent surfaced the magnitude but not the type-level question.
    Current status: UNTESTED

PRESUMPTION-204:
  Date surfaced: 2026-05-18
  Statement: [inferred] The sewing-agent's pending/-scan is now treated implicitly as a second, more-authoritative ground-truth witness for proposal existence (joining ASSUMPTION-179's partial OPEN-049 resolution), but this inverts the morning's PRESUMPTION-196 (which named the orchestrator's pending/-scan as ground truth) without auditing whether the two scans use identical path-coverage, tag-filters, and timing-against-write-completion. The remaining Levin/Friston count discrepancy (ASSUMPTION-180, OPEN-052) is precisely the residue of this unaudited overlap: two different agents scanning the "same" directory return different counts, and neither scan's coverage contract has been written down.
  Evidence it was operative: ASSUMPTION-179 + ASSUMPTION-180 are treated within the same EOD as resolution-direction-A (proposals exist) and residual-direction-B (count discrepancy) without acknowledging that both rest on the same unaudited scan-as-truth presumption first flagged this morning as PRESUMPTION-196.
  Why it was unstated: The sewing-agent's witness is more recent and richer (processed-page list vs orchestrator's count-only output), so it intuitively feels more authoritative; making the authority-comparison explicit requires writing down both scans' coverage contracts and comparing them.
  Type: methodological / inter-agent / scan-as-ground-truth
  Related decisions: ASSUMPTION-178, ASSUMPTION-179, ASSUMPTION-180, PRESUMPTION-196, OPEN-049, OPEN-052 (new)
  Testability: testable empirically (audit and document both the orchestrator's pending/-scan path/filter and the sewing-agent's pending/-scan path/filter; compare against a third reference `find inbox/proposals/pending/ -newer ...` command run at a controlled time); testable via process (require both agents to emit a write-receipt / read-receipt manifest with file list, mtime, and tag, replacing scan-as-truth with manifest-as-truth)
  Risk if wrong: Medium-High — every downstream agent (15a/15b, Pattern Detector, sewing-agent itself) that reads from pending/ inherits this presumption; the "two scans disagree" pattern observed today will recur every time agent A and agent B disagree on what's there, with no protocol for adjudication
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-204
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred as the inversion of PRESUMPTION-196 implicit in today's two ASSUMPTIONs treating the sewing-agent's scan as the new ground-truth witness, without auditing the second scan's coverage contract.
    Current status: UNTESTED

PRESUMPTION-205:
  Date surfaced: 2026-05-18
  Statement: [inferred] The Pulte Pre-Test Pack (local_26b6c078, ASSUMPTION-185) presumes that the four contamination modes derived from the Kroc Human-Test Pack experience (temporal / author / specificity / scoring-grain) transfer intact to the Pulte slice, and by extension to C2A2 cross-tradition bridge verification. The Pulte-vs-Kroc transfer is implicit (a "tightening" of the same frame); the C2A2 transfer is implicit at one further remove. In neither case is it checked whether the relative weights of the four modes are constant across institute-id domains (Kroc / Pulte / C2A2-bridges) — e.g., whether scoring-grain matters as much when the predictions are over named cell-collective ↔ neuromodulator pairs as when they're over named institute ↔ author pairs.
  Evidence it was operative: Pulte session (local_26b6c078): "The four contamination modes this addresses vs. the Kroc Human-Test Pack: temporal ..., author ..., specificity ..., and scoring grain ... The file's body notes all four explicitly so the diff is itself a methodology document." The methodology document treats the four modes as portable without examining their relative-weight stability across domains.
  Why it was unstated: A successful prior instance (Kroc) is the strongest argument for transfer, and explicit relative-weight portability would require a second instance to compare against — which is what the Pulte slice itself provides, but only after the methodology is locked in.
  Type: methodological / cross-project-transfer / contamination-mode-portability
  Related decisions: ASSUMPTION-185, OPEN-051, Pathway 14 (honesty layer), Pathway 13 (Pattern Detector)
  Testability: testable empirically (score the Pulte slice using the four-mode frame and compare to the Kroc slice's mode-weights; if relative weights differ materially, transfer-as-uniform is refuted); testable via process (require any cross-domain methodology transfer to enumerate the dimensions along which the relative weights of contamination modes could shift, before locking in the frame)
  Risk if wrong: Medium — the four-mode frame is a useful contribution even if relative weights shift; the risk is bias-of-omission (missing contamination modes that matter in C2A2-bridges but didn't matter in Kroc/Pulte)
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-205
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the Kroc→Pulte→C2A2 transfer pattern as a contamination-mode-portability presumption; the methodology-document framing treats four modes as constant across domains without acknowledging the relative-weight dimension.
    Current status: UNTESTED

PRESUMPTION-206:
  Date surfaced: 2026-05-18
  Statement: [inferred] The Pulte session (local_26b6c078) closes with: "Disagreement between Opus and Claude on the scoring would itself be a useful signal." This presumes that inter-model disagreement (Opus + Claude on the same scoring task) constitutes independent observations rather than correlated noise. Two distinct generations of the same model family share substantial training data, RLHF signal, and post-training conventions; their "disagreement" may reflect surface-level prompt-sensitivity rather than independent epistemic stances. (Joins the inter-instance-disagreement-as-signal pattern from earlier weeks' Pathway-22 work.)
  Evidence it was operative: Pulte session (local_26b6c078): "Once the Pulte edges land, scoring is the next pass — could be me, could be an Opus run, could be both. Disagreement between Opus and Claude on the scoring would itself be a useful signal."
  Why it was unstated: Inter-model-disagreement-as-signal is a common heuristic in the Pathway-22 individual-second-brain work and rarely interrogated; framing it as "independent" requires a model-genealogy audit (shared base, shared corpus, shared RLHF lineage) that the session does not undertake.
  Type: methodological / inter-model / independence-claim
  Related decisions: Pathway 22 (individual second brain), Pathway 14 (honesty layer), Pathway 13 (Pattern Detector), PRESUMPTION-180 (briefing-write-as-success-vs-action SELF-MEASUREMENT cluster), PRESUMPTION-194 (single-validator-portability)
  Testability: testable empirically (run paired Opus + Claude scorings on N controlled prompts where the ground-truth disagreement is known a priori; measure whether the inter-model disagreement matches the ground-truth signal or correlates with surface features of the prompt); testable via process (audit the model genealogy: do Opus 4.6 and Claude Sonnet 4.6 share base-model lineage, training corpora, or RLHF protocols sufficient to make their outputs correlated?)
  Risk if wrong: Medium — if inter-model agreement is treated as confirmation and disagreement as signal, the framework systematically over-weights both directions; a correlated-noise reading would shift weight toward "agreement does not confirm, disagreement does not refute"
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-206
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the Pulte session's closing "useful signal" framing as an inter-model-independence presumption that does not survive a model-genealogy audit unaided.
    Current status: UNTESTED

PRESUMPTION-207:
  Date surfaced: 2026-05-18
  Statement: [inferred] The sewing-agent's three new bridge notes (ASSUMPTION-182) were written to `synthesis/` without Pattern-Detector (Pathway 13) confirmation, extending the sole-source-bridge-detector pattern that OPEN-051 + PRESUMPTION-198 already flagged for the Levin/Friston specialist. The presumption is that the sewing-agent's pattern-matching constitutes adequate bridge-ratification authority — that bridges visible to a connectivity-traversal agent are bridges. This is the same architectural pattern as PRESUMPTION-198 (specialist-as-bridge-detector), now extended to a second agent class without re-asking the cross-specialist confirmation question. The Friston×Levin precision-weighting bridge is the strongest of the three by the sewing-agent's own ranking ("Strongest empirical bridge in today's batch"), but its ratification rests on a single agent's synthesis judgment.
  Evidence it was operative: Sewing-agent run (local_57fed042) writes three substantive bridge notes to `synthesis/` and ranks them by strength; no Pattern-Detector pass is invoked, no receiving-tradition specialist confirmation is requested, and OPEN-051 is not referenced as a gating concern.
  Why it was unstated: The sewing-agent is the connectivity-layer agent and bridges-as-connectivity-output is its job description; calling its output "sole-source bridge ratification" requires a separate-layer architectural framing (connectivity-layer vs pattern-detection-layer) the agent definitions don't yet draw.
  Type: architectural / inter-agent / bridge-ratification-authority
  Related decisions: ASSUMPTION-172, ASSUMPTION-182, PRESUMPTION-198, OPEN-051, OPEN-053 (new), Pathway 13 (Pattern Detector)
  Testability: testable via process (define a bridge-ratification protocol that separates connectivity-discovery from pattern-detection-confirmation; require Pathway-13 instantiation before any synthesis/ note carries ratified-bridge weight); testable empirically (after Pathway-13 instantiation, re-run today's three bridges through it and measure the agreement rate)
  Risk if wrong: Medium-High — if the sewing-agent's bridges accumulate in synthesis/ as de-facto ratified, the Pattern Detector inherits a pre-ratified bridge corpus instead of computing one from scratch; the cross-tradition signal becomes circular (sewing-agent → synthesis → Pattern Detector → cross-tradition stage gating)
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-207
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred as the second-agent-class extension of PRESUMPTION-198's specialist-as-bridge-detector pattern, surfaced by the sewing-agent writing three substantive bridge notes to synthesis/ without Pattern-Detector confirmation.
    Current status: UNTESTED

PRESUMPTION-208:
  Date surfaced: 2026-05-18
  Statement: [inferred] The FC26 abstract's stated corpus horizon (ASSUMPTION-183: "Day 100 of 308, full commentary by July 2026") presumes that the once-daily-per-tradition rotation will hold steady from now to July 2026 — i.e., that the 2026-05-15 / 2026-05-16 2-cycle gap and the on-cadence-streak counter (ASSUMPTION-117 demotion REVERSED until N≥3) are recoverable noise, not a cadence-regime shift. No slack / recovery / catch-up budget is articulated against the 308-day target. If the on-cadence streak does not recover to N≥3, the 308-day horizon erodes silently while the public abstract continues to assert it.
  Evidence it was operative: FC26 abstract Revision 2 (local_ea04730f) closes with a Day 100 / 308 / July 2026 corpus horizon, even though the most recent c2a2-self-awareness-daily cadence (which feeds the corpus-build pipeline indirectly) has just emerged from a 2-cycle gap and is at N=2 (per today's snapshot). The abstract does not condition its horizon on cadence-stability.
  Why it was unstated: Submission-ready closure (ASSUMPTION-183) is a state of "no more edits"; conditioning the horizon would require either a wider edit pass or a footnote acknowledging cadence risk, neither of which the session contemplates at the closing pass.
  Type: epistemic / publication-claim / corpus-horizon-stability
  Related decisions: ASSUMPTION-183, ASSUMPTION-117 (residual-urgency demotion), ASSUMPTION-168 (canonization momentum), Pathway 14 (honesty layer)
  Testability: testable empirically (track on-cadence streak through 2026-07-31; if streak ≥150 of next 150 days, horizon is supported; if cadence-skip rate > 5%, horizon is contradicted by Day 100 + skips_to_date / planning_rate); testable via process (add a horizon-condition footnote to the abstract that explicitly conditions Day-308 commitment on cadence stability)
  Risk if wrong: Medium — abstract is a publication claim; if the public horizon and the actual cadence diverge, the C2A2 honesty-layer (Pathway 14) has a self-instance to record
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-208
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the FC26 Revision-2 closure's stated 308-day horizon against the today-EOD context of a 2-cycle gap and an N=2 cadence streak; horizon stability is not conditioned in the abstract.
    Current status: UNTESTED

PRESUMPTION-209:
  Date surfaced: 2026-05-19
  Statement: [inferred] A single agent's directory scan is authoritative — the system has no reconciliation layer, so each counting agent trusts its own scan of the filesystem as ground truth. Today four agents reported three different pictures of the same pending queue (orchestrator + morning-walk: 51; cleanup: 36 stale → 15 genuine; chat-scrape: "reflection lag") and none reconciled against the others.
  Evidence it was operative: The orchestrator throttled Phase-2 hunts on its own 51-count without checking it against the cleanup-known duplicate bug; the morning-walk briefing echoed 51 as fact; the cleanup session independently produced 15. No agent referenced a shared count source.
  Why it was unstated: too foundational to notice — "scan the directory and count" is treated as obviously correct, so the question "whose scan, reconciled how?" never arose.
  Type: epistemic / methodological
  Related decisions: OPEN-055, OPEN-049, OPEN-052, lit-pipeline SYSTEMIC-RISK-FLAG A
  Testability: testable empirically (build a write-receipt manifest; measure count-agreement across agents before vs after)
  Risk if wrong: High — count-driven gates (conservation-principle Phase-2 suspension) act on corrupted numbers; the error propagates silently to every downstream consumer.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-209
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the four-way pending-count divergence and the absence of any cross-agent reconciliation step. Extends PRESUMPTION-196/204 (scan-as-truth) from proposal counts to review-queue counts.
    Current status: UNTESTED

PRESUMPTION-210:
  Date surfaced: 2026-05-19
  Statement: [inferred] Raw pending-queue depth is a valid proxy for "should the system generate more" — the conservation principle presumes a high count means stop hunting, without decomposing the count into genuine-unreviewed vs artifact, or into generation-throughput vs review-throughput.
  Evidence it was operative: The orchestrator suspended Phase-2 hunts because "51 pending — largest in network history," treating the raw number as a workload signal. 36 of those 51 were stale duplicates; the genuine count (15) would likely not have tripped the same gate.
  Why it was unstated: culturally embedded — "the queue is long, so slow down" is intuitive workload management; the assumption that the queue measures real work went unexamined.
  Type: normative / epistemic
  Related decisions: OPEN-055, conservation-principle gating, PRESUMPTION-202
  Testability: testable empirically (re-run the conservation gate on the deduped count; check whether the throttle decision flips)
  Risk if wrong: Medium-High — a corrupted proxy can throttle legitimate generation (or fail to throttle when it should), distorting the network's growth trajectory.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-210
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the conservation-principle Phase-2 suspension acting on an unvalidated raw count. Continues PRESUMPTION-202 (queue-depth-as-urgency).
    Current status: UNTESTED

PRESUMPTION-211:
  Date surfaced: 2026-05-19
  Statement: [inferred] A file written to disk is durably persisted — the architecture keeps generating uncommitted state (review HTML, master narrative, architecture/ docs, ~716 entries) as if persistence were guaranteed, when in fact no actor reliably commits it: the sandbox cannot write .git, scheduled commit agents collide/silently fail, and only Tom's host shell succeeds.
  Evidence it was operative: The orchestrator's Phase-6 commit was BLOCKED yet the run reported its outputs as done ("changes ARE on disk"); the 716-pile has been accumulating across runs; daily agents write without owning the commit step.
  Why it was unstated: too foundational to notice — "I wrote the file" is treated as equivalent to "the file is saved/shared," collapsing the on-disk vs committed-and-pushed distinction.
  Type: structural / operational
  Related decisions: OPEN-056, OPEN-050, lit-pipeline SYSTEMIC-RISK-FLAG D, REVISE-024 (CRITICAL)
  Testability: testable empirically (audit how many run-reported "done" outputs are actually committed+pushed vs sitting uncommitted)
  Risk if wrong: Critical — uncommitted work is one disk loss / overwrite away from gone; the 716-pile is unreviewed and unpushed; recurring locks compound the exposure. Continues PRESUMPTION-199.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-211
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the gap between agents reporting outputs "done" and the unowned, repeatedly-blocked commit step. Continues PRESUMPTION-199 (uncommitted-state-is-safe-indefinitely).
    Current status: UNTESTED

PRESUMPTION-212:
  Date surfaced: 2026-05-19
  Statement: [inferred] The documented number is the true number — the system presumes its multiple registers (CLAUDE.md viz stats, the metrics snapshot's counters, the orchestrator's network line, the PRS-3d viz) are mutually consistent and current, when today they diverged: viz stats off by ~factor (1,533/36,608/15.4MB vs 1,647/3,000/4MB), PRS triplets 225 vs 231, validated premises 18 (prior snapshot) vs 36 (registry).
  Evidence it was operative: CLAUDE.md carried stale viz figures until corrected today; the metrics snapshot's "validated premises: 18 cumulative" undercounts the registry's 36; the orchestrator (225) and PRS-3d viz (231) disagree on triplet count. No register cross-checks against another before publishing.
  Why it was unstated: oversight + culturally embedded — once a number is written down it is cited as fact; the maintenance burden of keeping registers synchronized was never made explicit.
  Type: epistemic
  Related decisions: ASSUMPTION-192, ASSUMPTION-193, OPEN-055, lit-pipeline SYSTEMIC-RISK-FLAG A
  Testability: testable empirically (define a single source-of-truth per metric; diff registers; measure drift)
  Risk if wrong: Medium-High — stale/divergent figures drive real decisions (the payload-diet deferral leaned on the wrong viz size; the cadence/premise counters feed the metrics narrative).
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-212
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from three independent register divergences surfaced on the same day. Joins the documentation-drift cluster with ASSUMPTION-192.
    Current status: UNTESTED

PRESUMPTION-213:
  Date surfaced: 2026-05-19
  Statement: [inferred] Absence-in-the-30-day-window equals absence-of-development — the tradition-specialist quality filter presumes a thinker's output arrives in a steady enough stream that an empty 30-day window means "nothing new," rather than "the 30-day window is the wrong instrument for this thinker's cadence."
  Evidence it was operative: The Hawkins/Hoffman slot returned 0 and treated it as the correct signal because "the 30-day window happens to fall in a quiet stretch." The honest-null reasoning is sound against fabrication but presumes the window length itself is well-calibrated to each thinker's publication rhythm.
  Why it was unstated: obvious to participants — the 30-day window is an inherited filter parameter; whether it fits each thinker's actual cadence was never questioned.
  Type: methodological
  Related decisions: ASSUMPTION-196, tradition-specialist quality filter, Rule 12
  Testability: testable empirically (measure each thinker's historical inter-output interval; check how often a 30-day window straddles a real gap vs misses slow-arriving work)
  Risk if wrong: Medium — slow-cadence thinkers could be systematically under-sampled while the system reads the silence as "caught up."
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-213
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the honest-null reasoning's reliance on the 30-day window as a fixed, uncalibrated parameter.
    Current status: UNTESTED

PRESUMPTION-214:
  Date surfaced: 2026-05-19
  Statement: [inferred] The refresh gap is unlikely to contain new evidence — the lit-pipeline's cycle-1 carry-forward convention presumes that literature relevant to tracked premises updates slowly enough that skipping a net-new search has low cost, which may not hold for fast-moving fields (AI, active inference, etc.).
  Evidence it was operative: 30 of 30 Cohort-A re-trigger items were MONITOR-continued via "no new evidence in refresh gap; carry-forward ... rather than attempting expensive net-new web searches with low expected yield" — a cost-benefit judgment applied uniformly without per-field calibration.
  Why it was unstated: methodological convenience — carry-forward is the cheap default; the presumption that yield is low was asserted, not measured per item.
  Type: methodological
  Related decisions: ASSUMPTION-199, MONITOR cycle protocol
  Testability: testable empirically (spot-check a sample of carry-forwarded items with a real search; measure the false-"no-change" rate, stratified by field velocity)
  Risk if wrong: Medium — fast-moving premises could go stale while flagged "monitored," giving false confidence in their currency.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-214
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the uniform application of carry-forward across all 30 re-trigger items without per-field yield calibration.
    Current status: UNTESTED

PRESUMPTION-215:
  Date surfaced: 2026-05-19
  Statement: [inferred] The model's training-knowledge corpus is an adequate stand-in for current literature when grounding architectural premises — the lit-pipeline's "established knowledge-search convention" cites from training memory rather than live web search, presuming that memory is a faithful and sufficiently-current proxy for the field.
  Evidence it was operative: "Cited sources drew on training-knowledge corpus (Helland, Kleppmann, Goodhart, Strathern, Muller, Beyer SRE, Nosek, Galison, Latour/Collins) per the pipeline's established knowledge-search convention" — i.e., grounding was sourced from the model's recall, not retrieval.
  Why it was unstated: culturally embedded in the pipeline's design — "cite the relevant literature" is treated as satisfiable from training knowledge; the recency/coverage limits of that knowledge were not surfaced as a caveat on the resulting INCORPORATE/REVISE dispositions.
  Type: epistemic / methodological
  Related decisions: ASSUMPTION-199, 15a/15b convention, validated_premises provenance
  Testability: testable empirically (for a sample, compare training-corpus grounding against a live-search grounding; measure citation overlap, recency gap, and disposition stability)
  Risk if wrong: Medium-High — the self-awareness system's epistemic backbone (which premises are SUPPORTED vs CHALLENGED) partly rests on model recall, inheriting its knowledge-cutoff and recall-error characteristics without flagging them.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-215
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the pipeline's stated reliance on training-knowledge-corpus citation as its grounding convention.
    Current status: UNTESTED

PRESUMPTION-216:
  Date surfaced: 2026-05-19
  Statement: [inferred] Each recurring failure deserves its own point-guard — the system fixes integrity problems with per-failure guards (regen_sociogram.sh refusing Summa-less builds; .gitignore *.bak*; sync_vault --only; a QC fabrication guard) rather than addressing the common substrate (no actor owns build/commit integrity end-to-end).
  Evidence it was operative: The debug session describes "three different recurrence traps (the --summa flag, .bak commits, silent fabrication) now have guards" — three independent point-fixes — while the underlying ownership/collision question (ASSUMPTION-189, OPEN-056) is deferred to "a fresh session."
  Why it was unstated: it is the natural local-optimum of incident-driven work — fix the bug in front of you; the meta-pattern (whack-a-mole vs systemic ownership) only becomes visible in aggregate.
  Type: normative / methodological
  Related decisions: ASSUMPTION-189, ASSUMPTION-190, ASSUMPTION-191, OPEN-056, PRESUMPTION-211
  Testability: testable empirically (track whether new recurrence traps keep appearing at a steady rate despite accumulating point-guards — the +1 new duplicate post-fix in ASSUMPTION-187 is an early data point)
  Risk if wrong: Medium — point-guards accumulate maintenance surface and can mask the absence of an integrity owner; failures migrate to whatever isn't yet guarded.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-216
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the pattern of three same-day point-guards landing while the systemic ownership question is deferred.
    Current status: UNTESTED

PRESUMPTION-217:
  Date surfaced: 2026-05-19
  Statement: [inferred] One canonical entity index can serve cold-start Search, lateral auto-hyperlinking, and broker-backed Ask without the three uses pulling it in incompatible directions — Pathway 27's "one-index-two-surfaces" unification presumes freshness (Ask), determinism (Search), and disambiguation (hyperlinking) are jointly satisfiable from a single `entity_index.json`.
  Evidence it was operative: The draft's spine is "driven by one `entity_index.json`"; it lists index freshness, hyperlink density, and entity disambiguation as open questions but still asserts the single-index architecture as the design.
  Why it was unstated: the unification is the elegant move and reads as obviously good; the tension between the three surfaces' differing index requirements is acknowledged only as separate open questions, not as a challenge to the one-index premise itself.
  Type: structural
  Related decisions: DECISION-037, ASSUMPTION-197, Pathway 27 open questions
  Testability: testable empirically (prototype the three surfaces against one index; check whether freshness needs for Ask force re-index cadences that break Search determinism or hyperlink stability)
  Risk if wrong: Medium — if the surfaces need divergent index treatments, the one-index commitment forces compromises (stale Ask, or non-deterministic Search) that only surface late in build.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-217
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the Pathway-27 draft asserting one-index unification while listing surface-specific tensions only as deferred open questions.
    Current status: UNTESTED

PRESUMPTION-218:
  Date surfaced: 2026-05-19
  Statement: [inferred] An honest null reflects the territory, not a gap in the agent's reach — treating "0 proposals" / "steady-state, nothing actionable" as a healthy positive signal presumes the agent's search/inspection coverage was actually adequate. Rule 12 (fail-loud) guards against fabrication but not against confident under-search.
  Evidence it was operative: The Tuesday specialist's 0-result and the deferred-monitor's steady-state were both reported as correct signals; the deferred monitor noted "State matches the 2026-05-18 summary exactly" — a null validated against a prior null. Coverage adequacy was asserted via search-list length, not measured.
  Why it was unstated: Rule 12 makes honesty about emptiness a virtue, which can mask the separate question of whether the search that produced the emptiness was complete.
  Type: epistemic / normative
  Related decisions: ASSUMPTION-196, Rule 12, deferred-action-monitor protocol
  Testability: testable empirically (inject a known in-window item the agent should find; measure whether honest-null runs would have caught it — a recall test on the search procedure)
  Risk if wrong: Medium — systematic under-coverage presented as confident null is invisible by construction; it is the symmetric failure to fabrication and currently unguarded.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-218
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from two same-day null results both reported as healthy without an independent coverage-adequacy check.
    Current status: UNTESTED

PRESUMPTION-219:
  Date surfaced: 2026-05-19
  Statement: [inferred] The end-of-day 14a/14b pass scales to the growing volume of daily sessions — the self-awareness apparatus presumes a single EOD agent can read and extract from all of a day's C2A2 sessions (12+ today), when at larger scale the EOD agent's own coverage becomes the bottleneck and it may itself begin sampling or carry-forwarding.
  Evidence it was operative: Today's run had to read ~12 transcripts to extract; the design treats "read today's transcripts" as a bounded task. The same carry-forward shortcut the lit-pipeline already uses (PRESUMPTION-214) would be the natural pressure-relief if session volume keeps rising — at which point the self-awareness layer inherits the very coverage-gap risk it exists to detect.
  Why it was unstated: scale blindness — the pass works fine at today's volume, so the question "what happens at 2x/5x sessions per day?" did not arise.
  Type: scaling
  Related decisions: 14a/14b scheduling, PRESUMPTION-214, PRESUMPTION-218
  Testability: testable empirically (measure extraction completeness vs session count; find the volume at which the EOD pass starts missing or sampling)
  Risk if wrong: Medium — a self-awareness layer that silently under-reads its inputs would report false coverage, the most self-undermining failure mode for this subsystem.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-219
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the unbounded-read assumption of the EOD pass against a day with 12+ C2A2 sessions.
    Current status: UNTESTED

PRESUMPTION-220:
  Date surfaced: 2026-05-19
  Statement: [inferred] On-cadence firing equals a healthy pipeline — the cadence-streak metric (N=3 on-cadence) presumes that "the agent fired on schedule" is the thing worth counting for self-awareness health, when today shows agents can fire successfully while their inputs are corrupted (the orchestrator fired on-cadence and produced a 544KB review page off an inflated 51-count).
  Evidence it was operative: The cadence-streak counter (and the ASSUMPTION-117 residual-urgency demotion gated on N≥3) treats on-time firing as the health signal; no parallel metric tracks whether a fire consumed valid inputs or produced valid outputs.
  Why it was unstated: normative smuggling — "ran on schedule" is easy to measure and intuitively good, so it stands in for "ran well" without the substitution being examined.
  Type: epistemic / normative
  Related decisions: ASSUMPTION-117, ASSUMPTION-200, the cadence-streak metric, lit-pipeline SYSTEMIC-RISK-FLAG C (Goodhart/self-measurement)
  Testability: testable empirically (pair each on-cadence fire with an input-validity + output-validity check; measure how often on-cadence ≠ healthy)
  Risk if wrong: Medium — optimizing the cadence metric (fire on time) can coexist with degrading pipeline quality (fire on bad inputs); a Goodhart instance on the self-awareness layer's own headline number.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-220
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cadence-streak metric counting firing while today demonstrated a successful fire on corrupted inputs. Joins the SELF-MEASUREMENT/Goodhart cluster (PRESUMPTION-201, lit-pipeline FLAG C).
    Current status: UNTESTED

PRESUMPTION-221:
  Date surfaced: 2026-05-20
  Statement: [inferred] The connectome is the *right* master-metaphor for the PRS data — the move from "chart of triplets" to "connectome" presumes the neural / Thousand-Brains connectome structure transfers to narratives without checking the transfer conditions: that narratives have the column-like completeness, the voting-toward-consensus dynamic, and the fiber topology that make "connectome" load-bearing rather than evocative. The doc asserts "this is not a metaphor laid over the tool after the fact," which is exactly the move that forecloses the transfer-condition check.
  Evidence it was operative: The whole guiding document (ASSUMPTION-201) and the proposed connectome metrics (degree/hubs, modularity, cross-module fiber density, path length) presume the analogy holds tightly enough to import network-neuroscience measurement; the "three connectomes, one architecture" table is asserted, not argued from shared formal properties.
  Why it was unstated: the analogy is generative and aesthetically compelling (a brain-connectome image was the day's inspiration), so its aptness reads as self-evident; transferred assumptions of this kind are 14b's canonical target.
  Type: structural
  Related decisions: DECISION-038, ASSUMPTION-201, ASSUMPTION-202, connectome-metrics proposal
  Testability: testable via literature (criteria for valid structural homology / when network-science measures transfer across domains) and empirically (compute the proposed measures and check whether they behave like connectome measures or like artifacts of an imposed structure)
  Risk if wrong: Medium-High — if the analogy is decorative, the connectome metrics measure a structure imposed by the framing rather than one found in the data, and downstream "these two traditions are integrating" claims inherit that imposition.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-221
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the guiding document's assertion of the connectome analogy as non-metaphorical, with no transfer-condition audit.
    Current status: UNTESTED

PRESUMPTION-222:
  Date surfaced: 2026-05-20
  Statement: [inferred] A narrative is faithfully a *compression* in the information-theoretic sense being borrowed — the "every story is a compression / progress = falling total description length" thread presumes that narrative compression and MDL / free-energy compression are the same kind of quantity, such that a description length is actually definable and computable over PRS triplets. If the equivalence is metaphorical, the proposed "total description length falling" progress metric has no operational definition.
  Evidence it was operative: ASSUMPTION-208 proposes description-length-falling as a measurable sign of a forming master science and reconnects it to Friston and Wolfram as if the compression notions are commensurable; no definition of the description-length measure over triplets is given.
  Why it was unstated: "story as compression" is intuitively true and the formal-information-theory link reads as a natural strengthening rather than a separate, load-bearing commitment that needs its own justification.
  Type: epistemic
  Related decisions: ASSUMPTION-208, ASSUMPTION-201, connectome-metrics proposal, traditions/friston, traditions/wolfram
  Testability: testable via literature (algorithmic information theory; MDL; whether narrative/semantic compression admits a description-length metric) and empirically (attempt to define and compute the metric on the corpus)
  Risk if wrong: Medium-High — a headline progress metric ("description length falling") that cannot be operationalized would either be quietly dropped or proxied by something that does not mean what the model claims it means.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-222
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the compression/entropy thread treating narrative compression and information-theoretic compression as one computable quantity.
    Current status: UNTESTED

PRESUMPTION-223:
  Date surfaced: 2026-05-20
  Statement: [inferred] Making integration/emergence *visible and attractive* in the tool does not bias the project toward convergence over preserved rivalry — adopting "telos = emergence of a master science" as the frame the tool is answerable to, and foregrounding convergence / emergence-over-time views, presumes that visual emphasis on coherence is value-neutral. The model explicitly affirms rival, non-converging master sciences ("never as a single convergent whole"), but the visualization's emphasis on where modules wire together still operationalizes a pro-integration gradient the stated pluralism does not cancel.
  Evidence it was operative: ASSUMPTION-207 names a convergent telos while affirming rivalry; the proposed perspectives ("by emergence over time," "by convergence") and the gold convergence-hub glow direct attention toward integration; rivalry has no equally salient visual instrument proposed.
  Why it was unstated: normative smuggling — the stated guard ("architectonic, never dominating") is taken to neutralize the value question, so the residual question of whether the *interface* tilts toward convergence does not arise.
  Type: normative
  Related decisions: ASSUMPTION-207, DECISION-038, DECISION-040, OPEN-058 (perspective set)
  Testability: testable empirically (do users exposed to the convergence-emphasis views report/aggregate more convergence than a rivalry-emphasis control?) ; partly a framework-values question
  Risk if wrong: Medium — a tool built to reveal an emerging master science may manufacture the appearance of one, the precise failure the rival-master-sciences caveat was meant to prevent.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-223
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the convergent telos + convergence-emphasis perspectives coexisting with a stated-but-not-operationalized pluralism guard.
    Current status: UNTESTED

PRESUMPTION-224:
  Date surfaced: 2026-05-20
  Statement: [inferred] A guiding document can be authored first and the tool made "answerable to it" without the document itself passing the scrutiny ordinary assumptions receive — `narrative_prs_connectome.md` is tagged "architecturally guiding" with "proposed changes ... evaluated against the model," granting a Tom-authored conceptual document near-spec standing before its empirical claims (coils-as-fibers, compression, 3-hub convergence) clear the 15a/15b literature gate. Combined with the author-contribution convention (ASSUMPTION-211), the guiding doc becomes a node in the connectome it governs — a self-ratifying loop.
  Evidence it was operative: the document's status line elevates it to an evaluative standard for future changes on the day it is written; the same day's work (rename, axis move, convergence finding) is already justified by reference to it; nothing routes the doc's own claims through the literature pipeline before it acquires governing status.
  Why it was unstated: "guiding/definitional document by the project director" is a natural authority category; the question of whether guiding status should exempt a doc from the assumption-testing it sets the standard for is exactly the kind of foundational point too obvious-in-role to notice.
  Type: methodological / epistemic
  Related decisions: ASSUMPTION-211, DECISION-038, provenance protocol, 15a/15b lit gate
  Testability: framework / governance question (testable via literature on circularity in self-governing systems and constitutional-document analogues); largely a process-design judgment
  Risk if wrong: Medium — load-bearing empirical claims acquire governing authority without test, and the self-documentation convention closes the loop, making the frame harder to revise the more the project builds on it.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-224
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the guiding-document status grant combined with the self-documentation convention forming a ratification loop outside the lit gate.
    Current status: UNTESTED

PRESUMPTION-225:
  Date surfaced: 2026-05-20
  Statement: [inferred] "Axis follows model" presumes there is a single correct semantic for each spatial axis once the model is fixed — moving coil altitude to discovery-year treats the vertical axis as a slot the model uniquely determines, when the same connectome model could justify several axis semantics at once (publication year, narrative/developmental time, connectome-time) and the choice may be a presentation tradeoff rather than a model entailment.
  Evidence it was operative: ASSUMPTION-204 and OPEN-057 both frame the axis as something to "pick deliberately, per the model"; the open question lists three honest candidates the model does not adjudicate between, yet the framing presumes the model will select one rather than that the choice is underdetermined and may need multiple toggleable axes.
  Why it was unstated: "let the model decide the axis" is the elegant discipline the day adopted; that a model can constrain without uniquely determining an axis is a subtlety the slogan papers over.
  Type: structural / methodological
  Related decisions: ASSUMPTION-204, OPEN-057 (node vertical-axis semantics), DECISION-039
  Testability: framework / design question (testable empirically by prototyping multiple axis semantics and checking whether one is clearly model-entailed or whether several are defensible)
  Risk if wrong: Low-Medium — over-trusting "the model picks the axis" could lock in one altitude semantics where a toggle (or a deliberately multi-axis design) would serve the connectome better.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-225
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the "axis follows model" slogan presuming unique determination where the open question lists several undecided candidates.
    Current status: UNTESTED

PRESUMPTION-226:
  Date surfaced: 2026-05-20
  Statement: [inferred] The representative-narrative substitution preserves the meaning of a tradition-bridging edge — rendering synergistic coils and cross-links as "the representative narrative of each bridged tradition" presumes a single node can stand for a whole tradition without distorting what the bridge claims. The stated honesty note ("not idea-precise") flags the imprecision, but the design still ships the substitution as the default, presuming users will read a tradition-level bridge as tradition-level even though they are shown two specific files.
  Evidence it was operative: ASSUMPTION-210 adopts uniform two-endpoint rendering "for all edge types" precisely so the cluster is uniform, knowingly trading idea-precision for consistency on the tradition-bridging edges; the resolution chose uniformity over a per-type rendering that would have shown the coil's own card for tradition bridges.
  Why it was unstated as a risk (it was flagged as a caveat, not as an operative presumption): the caveat treats the imprecision as a disclosed cost, not as a claim about user interpretation that itself could be wrong.
  Type: epistemic / methodological
  Related decisions: ASSUMPTION-210, ASSUMPTION-209, DECISION-042
  Testability: testable empirically (do users correctly distinguish tradition-level bridges from narrative-level ones when both render as two specific files? a comprehension test)
  Risk if wrong: Medium — users may mistake a representative pairing for a specific idea-to-idea link, over-reading the precision of cross-tradition coils — the connectome's most consequential edges.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-226
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the uniform-rendering choice shipping a known representative-narrative imprecision as the default for tradition-bridging edges.
    Current status: UNTESTED

PRESUMPTION-227:
  Date surfaced: 2026-05-20
  Statement: [inferred] Cross-tab interaction uniformity is worth more than per-view-optimal interaction — the "common behavior cluster across tabs" directive presumes that making the Connectome feel identical to the Sociogram is a net good, when a 3D Three.js raycast connectome and a 2D D3 sociogram may have genuinely different optimal affordances (the day's own zoom-dependent "blank space" dismissal bug is evidence that the 2D dismiss model ports imperfectly to 3D).
  Evidence it was operative: Tom's directive "stay within/produce a common behavior cluster across tabs" was treated as a constraint to satisfy faithfully; the node-click-toggle fix was justified partly because it "sidesteps the zoom/blank-space problem" — i.e., a 2D-derived dismiss model needed a workaround in 3D, which the uniformity directive absorbed rather than questioned.
  Why it was unstated: consistency is a near-universal UX virtue, so "same across tabs" reads as obviously right; the cost (suppressing affordances native to 3D) is invisible when uniformity is the goal.
  Type: methodological / normative
  Related decisions: ASSUMPTION-209, ASSUMPTION-210, DECISION-042
  Testability: testable empirically (compare task performance/satisfaction for uniform-cross-tab vs view-optimized interaction in the 3D connectome)
  Risk if wrong: Low-Medium — enforcing 2D-derived interaction patterns in a 3D view can entrench workarounds (the blank-space/zoom issue) instead of adopting 3D-native affordances.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-227
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the uniformity directive absorbing a 3D-specific dismissal bug as a workaround rather than as a signal that the ported model fits imperfectly.
    Current status: UNTESTED

PRESUMPTION-228:
  Date surfaced: 2026-05-20
  Statement: [inferred] The "only 3 literal cross-tradition hubs" finding reflects the territory, not the resource-naming / extraction method — concluding "convergence is analogical, not verbatim" presumes that literal resource-string matching is the right detector of verbatim convergence, when a low count could equally be an artifact of how resources are named or normalized across tradition files. This is the same scan-as-ground-truth / measurement-artifact pattern as the prior queue-count cluster, now reaching a headline conceptual finding.
  Evidence it was operative: ASSUMPTION-205 promotes a count (3) produced by one detection method into a conceptual claim about how traditions converge, with no normalization audit; the finding then justifies DECISION-040 (coils, not shared resources, are the convergence instrument).
  Why it was unstated: the finding fits the model's expectation (convergence should be analogical / via coils), so a confirming low count is accepted without asking whether the detector could undercount.
  Type: epistemic / methodological
  Related decisions: ASSUMPTION-205, DECISION-040, PRESUMPTION-212 (documented==true), lit-pipeline SYSTEMIC-RISK-FLAG A
  Testability: testable empirically (re-run hub detection under resource-name normalization / fuzzy matching / synonymy resolution; check whether the count of 3 is stable)
  Risk if wrong: Medium — a measurement artifact is being elevated into a load-bearing claim about the nature of cross-tradition convergence that may reshape the paper's account of "convergence."
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-228
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a single-method count being promoted to a conceptual convergence claim without a naming/normalization audit; joins the measurement-integrity cluster.
    Current status: UNTESTED

PRESUMPTION-229:
  Date surfaced: 2026-05-20
  Statement: [inferred] The connectome reframe, its 3D visualization, and its proposed network-neuroscience metrics will remain legible and meaningful as the network grows — at 231 narratives / 32 coils / 17 generative chains the view is readable and the metrics are illustrative; the proposal presumes both the visualization and the measures (degree/hubs, modularity, cross-module fiber density, path length) scale to the much larger triplet counts the project anticipates, where 3D legibility and hub-detection stability are not guaranteed.
  Evidence it was operative: the metrics are proposed as general handles ("these two traditions are integrating" → "fiber density rising") with no scale ceiling discussed; the visualization already carries crash-proofing node/edge caps (2000/3000 per project memory), implying a known scale wall the connectome framing does not address.
  Why it was unstated: scale blindness — the connectome reads beautifully at current N, so "does this stay legible/meaningful at 5x?" does not arise.
  Type: scaling
  Related decisions: ASSUMPTION-201, connectome-metrics proposal, viz crash-proofing caps (project memory)
  Testability: testable empirically (measure visual legibility and metric stability as N grows toward and past the 2000-node cap)
  Risk if wrong: Medium — a framing and metric suite validated only at small N may mislead once the network is large, exactly when the "watch a master science emerge" claim would be made.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-229
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from connectome metrics proposed as general handles against a visualization with a known node/edge crash cap, with no scale ceiling discussed.
    Current status: UNTESTED

PRESUMPTION-230:
  Date surfaced: 2026-05-20
  Statement: [inferred] Confirming the gating logic and the data is equivalent to confirming the rendered behavior the user reported — when Tom reported "generative coils don't react to time slider," the resolution reasoned from endpoint-year data ("15 of 17 chains have a 2026 endpoint, so it should react") and declared "generative does react," substituting a data/logic argument for a reproduced on-screen observation of the symptom Tom described. (The session did hedge — "if after a clean reload they truly don't move ... I'll instrument it" — but the disposition leaned on data-reasoning over observed behavior.)
  Evidence it was operative: two UX bug reports (slider non-reaction; "?" mispositioning) were addressed by code/data inspection and one screenshot; the slider issue specifically was closed by an argument about the data distribution rather than by watching the chains move on screen.
  Why it was unstated: when the gating logic is demonstrably correct, "the data say it reacts" feels like proof; the gap between "should react per the data" and "is observed to react" is the kind of verification-standard substitution that hides in confident debugging.
  Type: methodological / epistemic
  Related decisions: ASSUMPTION-206, Rule 12 (fail loud), PRESUMPTION-218 (honest-null presumes adequate coverage)
  Testability: testable empirically (a reproduced-behavior check on the live build: does the generative layer visibly change as the year slider moves? — closes the should-vs-is gap directly)
  Risk if wrong: Low-Medium — closing UX bugs by data-reasoning rather than reproduced observation can mark a real rendering bug "verified working"; symmetric to PRESUMPTION-218's confident-null risk on the interactive side.
  Status: UNTESTED
  Provenance:
    Origin: 14b
    Chain: [14b]
    Original item: PRESUMPTION-230
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a user-reported UX symptom being dispositioned by data/logic reasoning in place of a reproduced on-screen observation.
    Current status: UNTESTED
