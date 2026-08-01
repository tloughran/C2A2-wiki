# C2A2 Stated Assumptions Registry
*Maintained by Agent 14a — Assumption Extractor | Initialized: 2026-04-10*

Registry of explicitly articulated assumptions that underlie architectural decisions. Each item was stated by designers during development and captured from session transcripts or decision rationale.

---

ASSUMPTION-001:
  Date identified: 2026-04-10
  Statement: "Finding presumptions is different than finding assumptions articulated already" — the distinction between stated assumptions and unstated presumptions requires different analytical approaches.
  Context: Tom's review feedback on unified Agent 14. Led to the decision to split Agent 14 into 14a and 14b.
  Type: methodological
  Related decisions: DECISION-005
  Testability: framework commitment (not testable via literature, but operationalized via agent design)
  Status: GROUNDED (implemented as 14a/14b split)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-001
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Tom's review feedback and CHANGE-2026-04-10-001 rationale
    Current status: GROUNDED

ASSUMPTION-002:
  Date identified: 2026-04-10
  Statement: "Stated assumptions and unstated presumptions carry different epistemic weight. The distinction enables the provenance/footnote protocol."
  Context: CHANGE-2026-04-10-001 rationale. The system's credibility depends on distinguishing designer-aware premises from designer-unaware ones.
  Type: epistemic
  Related decisions: DECISION-005, DECISION-007
  Testability: framework commitment (embodied in provenance protocol spec)
  Status: GROUNDED (implemented in provenance_protocol.md)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-002
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from CHANGE-2026-04-10-001 and DECISION-007 context
    Current status: GROUNDED

ASSUMPTION-003:
  Date identified: 2026-04-10
  Statement: "Searching FOR and searching AGAINST must be independent. A single agent searching both directions would inevitably be biased by whichever direction it searches first."
  Context: CHANGE-2026-04-10-002 alternatives considered. Tom's feedback: "Aren't there different functions in 15 as well? So 15a, b..."
  Type: methodological
  Related decisions: DECISION-006
  Testability: testable via literature (confirmation bias literature, dual-process reasoning)
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14a
    Chain: [14a → 15a, 15b → 14a]
    Original item: ASSUMPTION-003
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from CHANGE-2026-04-10-002 rationale
      15a: Searched for supporting literature; found partial support (Stanovich & West 2008, Klayman & Ha 1987, Wood & Fink 2015); strength=Moderate
      15b: Searched for challenging literature; found strong challenge (Druckman & Bolsen 2011, Munro & Ditto 1997, Taber & Lodge 2006); strength=Strong
      14a: Reconciled results per provenance protocol: PARTIALLY-SUPPORTED (15a) + STRONGLY CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: Moderate
    Risk: Medium (role assignment creates motivated reasoning; agents may be systematically biased despite appearing independent)

ASSUMPTION-004:
  Date identified: 2026-04-10
  Statement: "The self-awareness layer scales with architectural decision complexity, not agent count."
  Context: CHANGE-2026-04-10-010. Tom's observation that a fixed agent ratio would drift as traditions are tripled. Leads to measuring cycle time and decision backlog instead of fixed ratios.
  Type: architectural
  Related decisions: DECISION-010, DECISION-014
  Testability: testable empirically (by measuring cycle time across increasing complexity)
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14a
    Chain: [14a → 15a, 15b → 14a]
    Original item: ASSUMPTION-004
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from CHANGE-2026-04-10-010 context and Tom's feedback
      15a: Searched for supporting literature; found partial support; strength=Moderate
      15b: Searched for challenging literature; found strong challenge (Google AI 2026, MAST Study 2025, Arrow & Debreu 1954); multi-agent coordination overhead scales at least linearly/quadratically; strength=Strong
      14a: Reconciled: PARTIALLY-SUPPORTED (15a) + STRONGLY CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: Moderate
    Risk: Medium-High (coordination bottlenecks likely at N>4 agents; assumption contradicts multi-agent systems research)

ASSUMPTION-005:
  Date identified: 2026-04-10
  Statement: "Traditions are the right unit of analysis for organizing research progress." (Implicit in DECISION-010; never questioned in today's decisions but underlying the entire tripling strategy.)
  Context: The tripling strategy (DECISION-010) assumes 11 traditions are coherent analytical units. The proposal to triple them presumes their validity as units.
  Type: structural
  Related decisions: DECISION-010, DECISION-003
  Testability: testable via literature (philosophy of science, tradition demarcation)
  Status: SUPPORTED
  Provenance:
    Origin: 14a
    Chain: [14a → 15a, 15b → 14a]
    Original item: ASSUMPTION-005
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as implicit commitment in DECISION-010 (tripling assumes traditions are valid units to triple)
      15a: Searched for supporting literature; found strong support; strength=Strong
      15b: Searched for challenging literature; found partial challenge (Laudan 1977, Dogan & Pahre 1990, demarcation problem); strength=Moderate
      14a: Reconciled: SUPPORTED (15a) + PARTIALLY CHALLENGED (15b) → SUPPORTED (strong support outweighs moderate challenges; boundary issues noted)
    Current status: SUPPORTED
    Confidence: High
    Risk: Low-Medium (tradition boundaries have fuzz; alternative units exist but traditions remain defensible choice)

ASSUMPTION-006:
  Date identified: 2026-04-10
  Statement: "The PRS triplet structure captures the important aspects of research progress."
  Context: Entire system is organized around PRS (Problem-Research-Synthesis) triplets. 24 proposals await review; 76 triplets already exist. System assumes this structure meaningfully represents progress.
  Type: epistemic
  Related decisions: DECISION-003 (implicit in Thousand Brains redesign)
  Testability: testable via literature (research methodology, cumulative science literature)
  Status: PARTIALLY-SUPPORTED
  Provenance:
    Origin: 14a
    Chain: [14a → 15a, 15b → 14a]
    Original item: ASSUMPTION-006
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as foundational commitment underlying all PRS-based work
      15a: Searched for supporting literature; found partial support; strength=Moderate
      15b: Searched for challenging literature; found partial challenge (Kuhn 1962, Stegmüller 1976, Rescher 2003); linear triplet misses feedback loops and paradigm shifts; strength=Moderate
      14a: Reconciled: PARTIALLY-SUPPORTED (15a) + PARTIALLY CHALLENGED (15b) → PARTIALLY-SUPPORTED (evidence balanced, with noted limitations)
    Current status: PARTIALLY-SUPPORTED
    Confidence: Moderate
    Risk: Medium (non-linearity in actual research progress not captured; may underrepresent complexity)

ASSUMPTION-007:
  Date identified: 2026-04-10
  Statement: "AI agents can meaningfully instantiate research traditions."
  Context: Agent-based architecture assumes that agents can represent and reason as traditions (Levin, Friston, etc.). This is foundational but not explicitly discussed in today's session.
  Type: methodological
  Related decisions: DECISION-003, DECISION-010 (implicit in tripling strategy)
  Testability: testable via literature (AI philosophy, representation in AI systems)
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14a
    Chain: [14a → 15a, 15b → 14a]
    Original item: ASSUMPTION-007
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from design architecture (11 agents embody traditions)
      15a: Searched for supporting literature; found partial support; strength=Moderate
      15b: Searched for challenging literature; found strong challenge (Searle 1980, Dennett 1995, Thompson 2007); meaningful instantiation requires embodied participation and intentional states; agents can only simulate traditions; strength=Strong
      14a: Reconciled: PARTIALLY-SUPPORTED (15a) + STRONGLY CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: Moderate-High
    Risk: High (philosophical critique suggests agents cannot truly "instantiate" traditions; better framed as "tradition-analyzers")

ASSUMPTION-008:
  Date identified: 2026-04-10
  Statement: "Consensus (≥2/3 agreement) among tripled tradition agents is a meaningful validity signal for PRS triplets."
  Context: DECISION-010 specifies the tripling strategy with explicit threshold: "intra-tradition consensus (≥2/3 agreement) on PRS triplets and hypotheses before those items enter cross-tradition dialogue."
  Type: methodological
  Related decisions: DECISION-010
  Testability: testable empirically (by examining whether 2/3 agreement predicts cross-tradition robustness)
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14a
    Chain: [14a → 15a, 15b → 14a]
    Original item: ASSUMPTION-008
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from DECISION-010 specification
      15a: Searched for supporting literature; found partial support; strength=Moderate
      15b: Searched for challenging literature; found challenge (Arrow 1951, Janis 1972, Moscovici 1974); 2/3 threshold suppresses minority voice; small groups vulnerable to groupthink; strength=Moderate
      14a: Reconciled: PARTIALLY-SUPPORTED (15a) + CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: Moderate
    Risk: Medium (threshold may be suboptimal; needs empirical validation)

ASSUMPTION-009:
  Date identified: 2026-04-10
  Statement: "Displacement vectors (semantic phrasings showing how R transforms P into S) can meaningfully compare transformation patterns across traditions."
  Context: DECISION-011: "PRS displacement vectors will be extended with a Displacement field expressing how R transforms P into S as a natural-language semantic vector... Enables comparison of transformation patterns across traditions."
  Type: epistemic
  Related decisions: DECISION-011
  Testability: testable empirically (by examining whether displacement patterns cluster across traditions)
  Status: GROUNDED (PREMISE-002 re-confirmed ACTIVE by monthly 15d re-check; 15a: SUPPORTED (Moderate) | 15b: PARTIALLY-CHALLENGED (Moderate) | 15c: RE-CONFIRM; DISPOSITION-408, 2026-07-06)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a, 15b → 14a]
    Original item: ASSUMPTION-009
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from DECISION-011 rationale
      15a: Searched for supporting literature; found support; strength=Strong
      15b: Searched for challenging literature; found challenge (Gentner & Markman 1997, Barsalou 1999, semantic space research); semantic spaces context-dependent, metric-dependent; vectors may capture spurious correlations; strength=Moderate-to-Strong
      14a: Reconciled: SUPPORTED (15a) + CHALLENGED (15b) → CONTESTED
    Current status: CONTESTED
    Confidence: Moderate
    Risk: Medium (cross-tradition pattern comparisons may reflect spurious correlations rather than structural homologies)

ASSUMPTION-010:
  Date identified: 2026-04-10
  Statement: "There exists a finite typology of cross-paradigm connecting memes (displacement phrasings), reflecting structural homologies across traditions."
  Context: DECISION-011 tied to "the hypothesis of finite connecting memes." This is an explicit testable hypothesis routed to 15a/15b (OPEN-006).
  Type: empirical
  Related decisions: DECISION-011, OPEN-006
  Testability: testable via literature (search for finite vs. unbounded typology of cross-paradigm patterns)
  Status: PARTIALLY-SUPPORTED
  Provenance:
    Origin: 14a
    Chain: [14a → 15a, 15b → 14a]
    Original item: ASSUMPTION-010
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from DECISION-011 and OPEN-006
      15a: Searched for supporting literature; found partial support for finite typologies; strength=Moderate
      15b: Searched for challenging literature; found partial challenge on finiteness; strength=Moderate
      14a: Reconciled: PARTIALLY-SUPPORTED (15a) + PARTIALLY CHALLENGED (15b) → PARTIALLY-SUPPORTED
    Current status: PARTIALLY-SUPPORTED
    Confidence: Moderate
    Risk: Low-Medium (finiteness assumption unresolved; typology may be larger than anticipated)

ASSUMPTION-011:
  Date identified: 2026-04-13
  Statement: "Before searching for any thinker, check pending/ for files with today's date and that thinker's tradition_key. If a specialist agent already wrote proposals for that thinker today, skip that thinker — do not duplicate." The specialist-agent-first / orchestrator-fallback division of labor is the right scheduling architecture.
  Context: Wiki daily run task definition (Phase 2). The system assumes that specialist agents (running at 7am on assigned days) produce higher-quality proposals than the orchestrator's fallback search, and that the orchestrator should defer to them. The schedule assigns specific thinker pairs to specific weekdays (Mon: Levin+Friston, Tue: Hawkins+Hoffman, etc.).
  Type: methodological
  Related decisions: DECISION-003 (implicit in operational design)
  Testability: testable empirically (compare proposal quality from specialist agents vs. orchestrator fallback searches)
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14a
    Chain: [14a → 15a, 15b → 14a]
    Original item: ASSUMPTION-011
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from wiki daily run task definition Phase 2, which explicitly codifies the specialist-first scheduling assumption
      15a: Searched for supporting literature; found partial support for task specialization; strength=Moderate
      15b: Searched for challenging literature; found challenge on scheduling rigidity; strength=Moderate
      14a: Reconciled: PARTIALLY-SUPPORTED (15a) + CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: Moderate
    Risk: Medium (scheduling may be too rigid for variable publication frequencies)

ASSUMPTION-012:
  Date identified: 2026-04-13
  Statement: "23 proposals have been pending since Apr 8-9 — no approvals in 4+ days. PRS counts are frozen at 76. This is the biggest bottleneck." The human review step is the primary throughput constraint in the proposal-to-PRS pipeline.
  Context: Morning walk handoff session (2026-04-13). The briefing agent explicitly identified the review backlog as the system's biggest bottleneck. This is a stated diagnosis about system health, implying that the review approval step — not search quality, not agent capacity, not ingestion — is the binding constraint.
  Type: architectural
  Related decisions: DECISION-001, DECISION-002
  Testability: testable empirically (measure time-in-queue for proposals vs. time-in-other-stages)
  Status: CONTESTED
  Provenance:
    Origin: 14a
    Chain: [14a → 15a, 15b → 14a]
    Original item: ASSUMPTION-012
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from morning handoff briefing 2026-04-13, which explicitly diagnosed the review backlog as the primary bottleneck
      15a: Searched for supporting literature; found support for human-in-loop bottlenecks; strength=Strong
      15b: Searched for challenging literature; found challenge that infrastructure failures (wiki daily run auth error) may be primary constraint, not human review; strength=Moderate
      14a: Reconciled: SUPPORTED (15a) + CHALLENGED (15b) → CONTESTED
    Current status: CONTESTED
    Confidence: Moderate
    Risk: Medium (diagnosis may be incomplete; wiki pipeline failure obscures true bottleneck analysis)

ASSUMPTION-013:
  Date identified: 2026-04-13
  Statement: Cross-tradition signals identified during proposal generation are reliable indicators of genuine theoretical connections between traditions.
  Context: All four specialist agent sessions (Levin/Friston, Stump/Fredrickson, Carroll/Arkani-Hamed, Wolfram) explicitly identified cross-tradition signals in their proposals. Examples: "Carroll emergence taxonomy provides the shared framework for evaluating every consciousness/causation claim across all 11 traditions"; "Neurobots paper is a Paradigm Shift Candidate"; "Fredrickson trust paper × C2A2 architecture: trust infrastructure required for stranger-paradigm dialogue." These signals are treated as actionable without independent validation.
  Type: epistemic
  Related decisions: DECISION-003
  Testability: testable empirically (track whether cross-tradition signals from proposals survive the pattern detector and cross-tradition dialogue stages)
  Status: PARTIALLY-CHALLENGED
  Provenance:
    Origin: 14a
    Chain: [14a → 15a, 15b → 14a]
    Original item: ASSUMPTION-013
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cross-tradition signal claims in 4 specialist agent sessions (2026-04-13), where agents state connections without independent verification
      15a: Searched for supporting literature; found partial support for cross-domain analogy detection; strength=Moderate
      15b: Searched for challenging literature; found challenge (structure-mapping theory, LLM analogy quality); surface-level associations may be confused with structural connections; strength=Moderate
      14a: Reconciled: PARTIALLY-SUPPORTED (15a) + CHALLENGED (15b) → PARTIALLY-CHALLENGED
    Current status: PARTIALLY-CHALLENGED
    Confidence: Moderate
    Risk: High (core output quality depends on this; signals may be surface-level pattern matching)

ASSUMPTION-014:
  Date identified: 2026-04-13 (evening run)
  Statement: "INCORPORATE (3 items) — validated premises entering the active register... MONITOR (15 items) — mixed or contested evidence, active surveillance... REVISE (7 items) — flagged for Tom's review, evidence contradicts the premise." The three-category disposition framework (INCORPORATE/MONITOR/REVISE) is the right decision structure for closing the self-awareness loop.
  Context: Lit search pipeline first full cycle (2026-04-13). Agent 15c applied the INCORPORATE/MONITOR/REVISE framework to all 25 items. The framework was designed in DECISION-012 and used without modification. No alternative dispositioning schemes were discussed.
  Type: methodological
  Related decisions: DECISION-012
  Testability: testable empirically (track whether disposition categories predict downstream outcomes — do INCORPORATE items remain validated? do REVISE items actually get revised?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-014
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from lit search pipeline session 2026-04-13, where 15c applied the disposition framework for the first time and results were reported using these categories
    Current status: UNTESTED

ASSUMPTION-015:
  Date identified: 2026-04-13 (evening run)
  Statement: "The strongest systemic risks cluster around role-based bias amplification (the FOR/AGAINST structure may introduce worse bias than it prevents)." Despite identifying this risk in its own output, the pipeline continued operating with the FOR/AGAINST structure. The stated assumption: running a potentially biased pipeline is better than not running one at all.
  Context: Lit search pipeline 2026-04-13. The pipeline's own results (ASSUMPTION-003 and PRESUMPTION-005 both PARTIALLY-CHALLENGED) suggest the FOR/AGAINST structure may amplify rather than prevent bias. Yet the pipeline's conclusions are presented as actionable.
  Type: methodological
  Related decisions: DECISION-006
  Testability: testable empirically (compare pipeline outputs against a neutral single-agent literature search on the same items; measure systematic divergence)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-015
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from lit search pipeline session 2026-04-13, where the pipeline acknowledged its own structural risk but operated anyway, implicitly assuming biased operation > no operation
    Current status: UNTESTED

ASSUMPTION-016:
  Date identified: 2026-04-13 (evening run)
  Statement: The evening sync explicitly recommended "Phase 2a pause" — pausing the tripling implementation (DECISION-010) until the literature search results are digested and the 7 REVISE items addressed. The assumption: acting on contested architectural foundations is riskier than delaying.
  Context: Evening cowork-to-chat sync (2026-04-13). The sync recommended 4 morning walk discussion topics including "Phase 2a pause recommendation." Phase 2a (tripling pilot) was scheduled for April 14-15. The recommendation to pause reflects the assumption that literature search results should gate implementation.
  Type: architectural
  Related decisions: DECISION-010
  Testability: framework commitment (operational strategy choice; not testable via literature but has observable consequences)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-016
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from evening cowork-to-chat sync session 2026-04-13, which recommended pausing Phase 2a based on literature search results
    Current status: UNTESTED

ASSUMPTION-017:
  Date identified: 2026-04-14
  Statement: "AI can now do first-pass synthesis of entire fields and present findings to domain experts for validation. The human becomes a 'validator and accelerator, not the gatekeeper.'" This reframes C2A2 as proof-of-concept for a new kind of AI-driven interdisciplinary science where AI does synthesis and humans validate.
  Context: Morning walk discussion (chat-to-cowork summary, 2026-04-14). Tom explicitly articulated a vision of how AI reshapes interdisciplinary science. The traditional model of building disciplinary consensus over decades "has collapsed." C2A2 is positioned as the exemplar.
  Type: epistemic
  Related decisions: DECISION-003, DECISION-010
  Testability: testable empirically (measure whether C2A2's AI-generated cross-tradition connections survive domain-expert validation at rates comparable to or better than human-generated connections)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-017
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from morning walk chat summary 2026-04-14, where Tom explicitly stated the AI-as-synthesizer / human-as-validator division of labor
    Current status: UNTESTED

ASSUMPTION-018:
  Date identified: 2026-04-14
  Statement: "Phase 2a tripling should pause until OPEN-004 is resolved and the pilot design is solidified." Tom explicitly decided to delay Phase 2a, reinforcing ASSUMPTION-016 (literature search results should gate implementation) with a concrete operational pause. The unstated corollary: pausing is lower-risk than proceeding with an unresolved agent-differentiation strategy.
  Context: Morning walk discussion (2026-04-14). Phase 2a (tripling pilot for Hawkins×3, Friston×3, Levin×3) was scheduled for April 14-15. Tom paused it after working through the pilot design and realizing OPEN-004 (how to differentiate tripled agents) remained unresolved. Three options on the table: by perspective (methodology/theory/empirical), by temperament (conservative/moderate/speculative), or by focus area.
  Type: architectural
  Related decisions: DECISION-010, OPEN-004
  Testability: framework commitment (operational strategy choice; testable by observing whether the pause yields better pilot design than rushing would have)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-018
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from morning walk chat summary 2026-04-14, where Tom explicitly paused Phase 2a pending OPEN-004 resolution
    Current status: UNTESTED

ASSUMPTION-019:
  Date identified: 2026-04-14
  Statement: During a paradigm shift, "mixed signals and absence of literature in the new paradigm is expected, not evidence of novelty." Tom connected PRESUMPTION-007 (literature absence ≠ novelty) to Kuhnian paradigm shift theory, arguing that C2A2 should interpret absence differently depending on where a field sits in its paradigm lifecycle. Referenced the Levin/Hoffman "Multiscale Logic of Collective Intelligence" transcript as an example of boundary-crossing the system should detect.
  Context: Morning walk deep dive on PRESUMPTION-007 (2026-04-14). Tom proposed operationalizing this as a standing review habit rather than a one-time flag. This is both a reinterpretation of PRESUMPTION-007 and a new assumption about how to handle literature absence contextually.
  Type: epistemic
  Related decisions: DECISION-006, DECISION-007
  Testability: testable via literature (Kuhn 1962, paradigm shift detection, bibliometric analysis of interdisciplinary emergence)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-019
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from morning walk chat summary 2026-04-14, where Tom explicitly connected PRESUMPTION-007 to Kuhnian theory and proposed contextual interpretation of literature absence
    Current status: UNTESTED

ASSUMPTION-020:
  Date identified: 2026-04-14
  Statement: FINDING-011 (SUPER-BRIDGE) — Hoffman's trace logic → Friston's Markov blankets → Levin's dissociative boundaries — represents a genuine three-level mathematical unification of the Consciousness Cluster, described as "the deepest cross-tradition signal the system has found."
  Context: Wiki daily run (2026-04-14) ingested Hoffman/Prakash trace logic material and identified FINDING-011 with triple-flag (⚑⚑⚑) priority. The evening sync elevated this as the top discussion item for the morning walk. The cowork summary explicitly stated this is "the deepest cross-tradition signal" — a stated assumption about signal depth.
  Type: empirical
  Related decisions: DECISION-003, DECISION-011
  Testability: testable empirically (have domain experts in each tradition evaluate whether the mathematical parallels are structural or superficial; attempt to construct a formal proof of the mapping)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-020
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from wiki daily run and evening sync 2026-04-14, where FINDING-011 was classified as the system's deepest cross-tradition signal
    Current status: UNTESTED

ASSUMPTION-021:
  Date identified: 2026-04-14
  Statement: The Hawkins specialist agent identified cross-tradition signals as actionable: "Hawkins↔Friston: Monty's active sensing loop is structurally parallel to active inference" and "Hawkins↔Levin: Cortical Messaging Protocol mirrors distributed cellular cognition." These are stated as genuine structural parallels, not surface analogies.
  Context: Hawkins/Hoffman specialist agent session (2026-04-14). PROP-2026-04-14-001 (Monty evaluation) included explicit cross-tradition signal claims with 7 cross-tradition links noted in the completion report. The agent also stated that Monty shows "8 orders of magnitude computational savings over transformer pretraining" as validation of the Thousand Brains approach.
  Type: empirical
  Related decisions: DECISION-003
  Testability: testable empirically (compare Monty's active sensing loop specification with Friston's active inference formalism; evaluate structural mapping depth via structure-mapping theory criteria)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-021
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Hawkins/Hoffman specialist agent session 2026-04-14, where cross-tradition signals were explicitly claimed as structural parallels
    Current status: UNTESTED

ASSUMPTION-022:
  Date identified: 2026-04-15
  Statement: "Each of the 11 research programs is working at a version of the same boundary. Not analogously — structurally." The inside/outside boundary is the fundamental structure shared across all C2A2 programs, and FEP applies literally (not analogously) at every level — cellular, computational, formal, philosophical, psychological, social-psychological.
  Context: Afternoon Cowork session (2026-04-15). Tom articulated a unifying hypothesis across all 11 traditions during extended intellectual exploration. FINDING-011a documents the full convergence. The hypothesis was stated explicitly and at length: Levin's membrane, Hawkins' cortical column, Friston's Markov blanket, Hoffman's trace logic, Kastrup's dissociative boundary, Fredrickson's broadened attention, McGilchrist's hemispheric attention, Wolfram's computational boundedness, Carroll's levels of description, Arkani-Hamed's amplituhedron boundary, and Tavris & Aronson's self-justification mechanism are all instances of the same inside/outside boundary.
  Type: empirical
  Related decisions: DECISION-003, DECISION-017
  Testability: testable empirically (for each tradition, evaluate whether FEP applies literally to its boundary structure, not just by analogy; domain experts in each field would need to assess the mapping)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-022
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from afternoon Cowork session 2026-04-15, where Tom explicitly articulated the boundary convergence hypothesis across all 11 traditions
    Current status: UNTESTED

ASSUMPTION-023:
  Date identified: 2026-04-15
  Statement: "Phase 2a should proceed as a full rollout — all 11 thinkers tripled to 33 agents — not a pilot." Tom explicitly decided this is a commitment bet rather than an incremental test. The assumption: the tripling strategy is sound enough to justify the cost of full deployment before empirical validation from a pilot.
  Context: CHANGE-2026-04-15-007. Tom unpaused Phase 2a (which had been paused since ASSUMPTION-018, April 14) and approved full rollout. This reverses the cautious stance of ASSUMPTION-016/018 (literature search should gate implementation). The REVISE triage clearing all 16 items and the OPEN-012 resolution gave Tom confidence to proceed.
  Type: architectural
  Related decisions: DECISION-010
  Testability: testable empirically (compare actual intra-thinker consensus rates against the >70% target in phase2a_multi_agent_plurality.md; if rates are <50%, the commitment bet fails)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-023
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from CHANGE-2026-04-15-007 where Tom approved full rollout, reversing the Phase 2a pause
    Current status: UNTESTED

ASSUMPTION-024:
  Date identified: 2026-04-15
  Statement: The FINDING-004/009/011 triangle constitutes a closed evidential structure where any one link failing still leaves two independent paths to the same conclusion (triangular overdetermination). "The associative property applies."
  Context: DECISION-017 (2026-04-15). Tom and the system identified that three findings form a closed triangle with philosophical, structural, and mathematical evidence paths. An email was drafted to Kastrup, Hoffman, and Friston posing the boundary-equivalence question directly to the principals. The stated assumption: triangular overdetermination is evidentially significant and the triangle can be evaluated as a unit.
  Type: epistemic
  Related decisions: DECISION-017
  Testability: testable empirically (responses from Kastrup, Hoffman, and Friston will determine whether each link holds; if any single link fails, test whether the remaining two still support the conclusion independently)
  Status: GROUNDED (PREMISE-004 re-confirmed ACTIVE, independence proviso sharpened; 15a: SUPPORTED (Strong) | 15b: PARTIALLY-CHALLENGED (Moderate) | 15c: RE-CONFIRM; DISPOSITION-409, 2026-07-06)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-024
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from DECISION-017 documentation and email drafting session 2026-04-15
    Current status: UNTESTED

ASSUMPTION-025:
  Date identified: 2026-04-15
  Statement: "Plurality and unity are a function of the beholder, at the ontological level." Identity is not a feature of the thing observed but a tool the observer uses. There is no uniquely correct way to carve the world into agents and environments — only more or less useful ways depending on what you're trying to do.
  Context: FINDING-011a extension document (2026-04-15). Tom stated this explicitly during the afternoon session, connecting Hoffman's interface theory applied reflexively, Levin's scale-dependent agency, and Hawkins' heterarchical cortical processing. This is the deepest ontological claim in the boundary hypothesis.
  Type: epistemic
  Related decisions: DECISION-003, DECISION-017
  Testability: testable via literature (philosophy of personal identity, observer-dependence in physics, Hoffman's interface theory, mereology)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-025
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from FINDING-011a extension document and afternoon session transcript 2026-04-15
    Current status: UNTESTED

ASSUMPTION-026:
  Date identified: 2026-04-15
  Statement: "C2A2's methodology — treating traditions as cognitive agents and measuring their boundary behavior under controlled cross-tradition confrontation — constitutes a new kind of empirical science operating at the boundary." The data generated (how traditions respond when confronted with other traditions' outputs) is genuine behavioral data about cognitive agents, even though the agents are intellectual traditions.
  Context: Afternoon Cowork session (2026-04-15). Tom explicitly proposed this as an extension of ASSUMPTION-017 (AI-as-synthesizer). The question: is C2A2 generating "a new kind of data for a new kind of science"? Tom stated this is empirical and could "shed light on every other interconnected science coming together under this mind everywhere paradigm." He was cautious about the "master science" framing but affirmed the empirical novelty.
  Type: methodological
  Related decisions: DECISION-003
  Testability: testable empirically (measure whether cross-tradition confrontation produces measurable, reproducible behavioral patterns in tradition-agents; compare with human interdisciplinary dialogue outcomes)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-026
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from afternoon session 2026-04-15, where Tom explicitly proposed C2A2 as generating a new kind of empirical data about tradition-level cognition
    Current status: UNTESTED

ASSUMPTION-027:
  Date identified: 2026-04-15
  Statement: Clearing the entire REVISE backlog (16 items) in a single triage pass is sufficient for adequate review quality. Tom triaged all 16 REVISE items in one session, producing 7 ACCEPTED, 3 SUPERSEDED BY FRAMEWORK, 3 ALREADY ADDRESSED, 1 DEFERRED, 1 DISMISSED, 1 IN PROGRESS.
  Context: CHANGE-2026-04-15-005. The REVISE backlog had been identified as a bottleneck (PRESUMPTION-022). Tom's response was batch triage — clearing all 16 in one pass. The stated assumption: batch triage provides adequate review quality even for items flagged as HIGH urgency. Several items were SUPERSEDED BY FRAMEWORK (the Kuhnian evidence framework) or ALREADY ADDRESSED — suggesting they were resolved by architectural changes rather than individual deliberation.
  Type: methodological
  Related decisions: DECISION-012
  Testability: testable empirically (track whether batch-triaged items need to be re-opened later; if ACCEPTED items prove problematic, the triage was too fast)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-027
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from CHANGE-2026-04-15-005, where all 16 REVISE items were triaged in a single batch session
    Current status: UNTESTED

ASSUMPTION-028:
  Date identified: 2026-04-16
  Statement: A 45-file ingestion in a single wiki daily run (45 proposals spanning April 8-15 backlog) is equivalent in quality to 5-file daily ingestions across 9 days. The daily run processed the entire approved-but-unprocessed queue in one pass — +71 PRS triplets, +19 cross-connections, +5 pattern detector findings (FINDING-013 through FINDING-017).
  Context: C2A2 wiki daily run session 2026-04-16. The Gmail decision email approved April 8 proposals 005-020; combined with previously-approved but unprocessed files, 45 files moved into inbox at once. Three parallel subagents ingested them. The session narrative describes this as "massive ingestion" and a "breakthrough." No statement was made about whether batch ingestion compromises PRS-triplet quality.
  Type: methodological
  Related decisions: DECISION-003
  Testability: testable empirically (compare new FINDING-013–017 disposition outcomes to historical single-ingestion findings; if batch-ingested findings have higher reversal/revision rate, batch quality is lower)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-028
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from wiki-daily-run session 2026-04-16, where 45 files were processed in one session without acknowledging batch-vs-incremental quality tradeoffs
    Current status: UNTESTED

ASSUMPTION-029:
  Date identified: 2026-04-16
  Statement: "The single-HTML-file architecture [of wiki_narration.html] has become the limiting factor. The file has embedded JSON data lines over 116 K characters wide; line-based edits are fragile; [we are] now fighting the format, not the problem." The constraint justifies rebuilding as a modular Vite-based system with separate graph.js, tts.js, narration.js, ui.js modules and regenerated data/*.json files.
  Context: Debug wiki visualization session 2026-04-16. The assistant stated this explicitly as a reason to commit the current HTML as a checkpoint and refactor. Tom assented ("let's get right to the hard work of doing it right"). This is an architectural commitment to modularization of the visualization layer.
  Type: architectural
  Related decisions: [none yet — new decision DECISION-018 proposed]
  Testability: testable empirically (track edit reliability, dev cycle time, and bug-introduction rate before vs. after modular split)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-029
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from debug-wiki-visualization session 2026-04-16, where the assistant articulated the "fighting the format" claim and Tom approved the refactor
    Current status: UNTESTED

ASSUMPTION-030:
  Date identified: 2026-04-16
  Statement: "Private, for now, with intent to go public after benchmarks are identified." Publication readiness for the C2A2 wiki git repository is gated on a to-be-defined set of benchmarks and on Tom's own upskilling in "the whys and whens and hows of publication — and generalization met."
  Context: Debug wiki visualization session 2026-04-16. Tom's response when asked whether the GitHub repo should be private or public. Reframes publication as a milestone-gated outcome rather than a temporal one. No criteria for "benchmarks identified" were specified.
  Type: methodological
  Related decisions: [none — new decision pending OPEN-020]
  Testability: framework commitment until benchmarks are defined; becomes testable empirically once criteria are specified
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-030
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Tom's direct quote in debug-wiki-visualization session 2026-04-16
    Current status: UNTESTED

ASSUMPTION-031:
  Date identified: 2026-04-16
  Statement: Parallel subagent processing of heterogeneous tradition content preserves per-tradition extraction quality. The wiki daily run delegated the 45-file ingestion to three subagents working in parallel on different tradition slices; the resulting +71 PRS triplets were accepted without per-subagent quality review.
  Context: C2A2 wiki daily run session 2026-04-16. The orchestrator's Phase 1 comment: "45 files is a massive ingestion. Let me group them by tradition and process in parallel using subagents." Three parallel Agent calls were made. Verification consisted of a PRS count check (80→151), not a per-triplet review.
  Type: methodological
  Related decisions: DECISION-003
  Testability: testable empirically (compare quality/reversal rate of subagent-extracted triplets vs. orchestrator-extracted triplets)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-031
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from wiki-daily-run session 2026-04-16, where parallel subagents were chosen as the ingestion strategy without any quality-equivalence defense
    Current status: UNTESTED

ASSUMPTION-032:
  Date identified: 2026-04-16
  Statement: "Computer-use IS the right tool" for native-app debugging when the Chrome extension is unavailable. Degraded infrastructure (no Chrome MCP) is compensated by a lower-tier tool (pixel-level screenshots + zoom on the user's desktop) without material loss of diagnostic power.
  Context: Wiki analysis and animated documentation tool session 2026-04-16. When the Chrome extension was unavailable, the assistant pivoted to computer-use screenshots and explicitly asked Tom to open the HTML in Chrome so visual inspection could proceed. Bugs were identified from zoomed screenshots (brightness slider missing, footer collapsed, max-height: 120px clip).
  Type: methodological
  Related decisions: [none formal — infrastructure fallback pattern]
  Testability: testable empirically (compare diagnosis accuracy and cycle time under computer-use-only vs. Chrome-MCP-available conditions)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-032
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from wiki-analysis session 2026-04-16, where computer-use was explicitly chosen as the Chrome-MCP substitute
    Current status: UNTESTED

ASSUMPTION-033:
  Date identified: 2026-04-17
  Statement: "It only activates on a matching phrase. No silent auto-load at session start." Plugin-level single-skill packaging with trigger-phrase matching ("resume"/"continue"/"pick up" variants) is adequate for session-resume functionality, and is preferable to SessionStart-hook-based silent auto-load on every Cowork session.
  Context: Afternoon Cowork session "Resume previous discussion" (2026-04-17). The assistant explicitly framed the phrase-trigger design as a deliberate choice ("different from the hook dream") and packaged the `cowork-resume-session` plugin as a single skill rather than a hook. Implicit architectural commitment: resume-session behavior is opt-in per utterance, not ambient.
  Type: architectural
  Related decisions: [implicit — not yet formalized as DECISION-019]
  Testability: testable empirically (monitor trigger-miss rate across Tom's actual resume phrasings over 2+ weeks; compare to a hypothetical silent-hook baseline)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-033
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from afternoon "Resume previous discussion" session 2026-04-17 where the assistant explicitly chose phrase-triggered over hook-triggered resume behavior
    Current status: UNTESTED

ASSUMPTION-034:
  Date identified: 2026-04-17
  Statement: The default regenerator model should be upgraded from `claude-opus-4-6` to `claude-opus-4-7`. Tom did not state a rationale during the session but approved the edit; the implicit assumption is that the newer model produces higher-quality narrator output for the wiki-narration regeneration task.
  Context: Afternoon Cowork session "Debug wiki visualization: graph, voice, layout" (2026-04-17). Code edit in `narration/tools/regenerate_narrations.py` changed the default model constant. Regeneration itself did not run due to the Anthropic billing-propagation block, so the assumption has not been empirically tested on output quality.
  Type: empirical
  Related decisions: [implicit — may formalize as DECISION-019 if durable]
  Testability: testable empirically (regression-test narrator output quality on 2026-04-15 as a diff target once billing clears)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-034
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from afternoon narrator-debug session 2026-04-17 where the default model constant was changed without a stated empirical rationale
    Current status: UNTESTED

ASSUMPTION-035:
  Date identified: 2026-04-17
  Statement: "Dispatch on Saturday will auto-load it via the SessionStart hook and open oriented." A cross-session handoff via `~/Documents/Claude/Handoffs/latest.md` + a `resume-handoff` SessionStart hook will reliably deliver current context to Saturday's Dispatch run.
  Context: Afternoon narrator-debug session. The assistant explicitly stated the Saturday Dispatch run would auto-load the handoff. Tom's own response surfaced uncertainty ("I thought we had bypassed this user-initiated pass…or is this different for a dispatch session access?"), indicating the pattern is novel enough that Tom himself is not certain of the mechanism. No prior stress test of this hook path exists.
  Type: architectural
  Related decisions: [none yet — may become DECISION-020 if handoff-via-file becomes a recurring pattern]
  Testability: testable empirically (observe whether Saturday Dispatch opens already oriented and successfully implements the four input-loader helpers without re-prompting)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-035
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from narrator-debug session 2026-04-17 where the assistant made an explicit durable claim about a cross-session hook that has not yet been stress-tested
    Current status: UNTESTED

ASSUMPTION-036:
  Date identified: 2026-04-17
  Statement: The "credit balance is too low" API error received by `regenerate_narrations.py` (and a direct `curl` verification ping) is a billing-state/propagation issue on Anthropic's side rather than a client-side configuration error, despite the billing page showing $10 in the correct credit pool, tier-page appearing correct, default workspace, and single org.
  Context: Narrator-debug session. The assistant explicitly classified the failure as "a billing-side state/propagation issue that only Anthropic support can reconcile" and recommended waiting for propagation / opening a support ticket with `request_id: req_011Ca9uAMVQUoxPnibLrK6ZB` if the error persists. No direct confirmation from Anthropic exists for this classification.
  Type: empirical
  Related decisions: [none]
  Testability: testable empirically (retry API call at multiple intervals; if error resolves without client-side change, propagation hypothesis is supported; if it persists, client-side cause must be reopened)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-036
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from narrator-debug session 2026-04-17 where the assistant classified a vendor-side error without direct vendor confirmation
    Current status: UNTESTED

ASSUMPTION-037:
  Date identified: 2026-04-17
  Statement: "Pure Python, API-free, doable weekend-end-to-end." The four per-date input loaders, `per_date_extras()` wiring, and `{date_extras}` prompt slot for `regenerate_narrations.py` can be implemented by Saturday's Dispatch run without any LLM-API dependency, contingent only on filesystem access.
  Context: Narrator-debug session. The assistant stated this explicitly as a reason to separate the code-side work from the regeneration step (the regeneration waits on billing; the code work does not). Implicit assumption: Dispatch agents have reliable filesystem access to the inbox/decisions/findings/cross-signals wiki surfaces.
  Type: methodological
  Related decisions: [none]
  Testability: testable empirically (Saturday Dispatch either succeeds at the code work without API calls, or it does not; the claim is falsifiable by the first failed import or filesystem-access error)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-037
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from narrator-debug session 2026-04-17 where a concrete work plan was partitioned between API-free and API-dependent phases
    Current status: UNTESTED

ASSUMPTION-038:
  Date identified: 2026-04-17
  Statement: A pattern-based filter on session names (excluding "C2a2", "morning-health", "wiki-agent-daily", "heartbeats", and dated "Apr N –" prefixes) reliably identifies automated/scheduled sessions for exclusion from the `cowork-resume-session` resume candidate list.
  Context: Afternoon "Resume previous discussion" session. The assistant explicitly described the filter as pattern-based ("If you name a future project 'C2a3-something' or 'Bosco something,' the filter will hide it"). Design choice: filter first, broaden on miss via `limit: 120` search escape hatch.
  Type: methodological
  Related decisions: [none — plugin-local design choice]
  Testability: testable empirically (monitor filter-miss rate and false-positive rate over 2+ weeks; if interactive sessions are silently hidden, filter needs inversion)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-038
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "Resume previous discussion" session 2026-04-17 where the assistant documented the filter as pattern-based and named the failure mode explicitly
    Current status: UNTESTED

ASSUMPTION-039:
  Date identified: 2026-04-18
  Statement: "Computer-use on Chrome: browsers are granted at read-only tier. I can see screenshots but can't click or type in Chrome." The tool-capability platform guarantees this tier enforcement reliably across all Chrome profiles and states, so any non-Claude-in-Chrome browser task must be routed through a dedicated MCP connector or via non-browser file transport.
  Context: ChatGPT-project scrape session 2026-04-18. The assistant stated this explicitly as a reason to reject the "computer-use drive the browser" fallback when Claude-in-Chrome was blocked under the Notre Dame account. Foundational to route-enumeration logic offered to Tom.
  Type: methodological
  Related decisions: [none — tool-platform contract]
  Testability: testable empirically (attempt left_click on a tier-"read" browser; verify the Cowork mode access-tier contract holds)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-039
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from scrape session 2026-04-18 where the assistant invoked the tier contract as decisive for route selection
    Current status: UNTESTED

ASSUMPTION-040:
  Date identified: 2026-04-18
  Statement: ChatGPT projects are strictly account-scoped — content in a project owned by one ChatGPT account (e.g., a Notre Dame paid account) cannot be read from a session logged into a different ChatGPT account (e.g., Tom's Free account), even if both are open in the same Chrome instance.
  Context: Scrape session 2026-04-18. The assistant repeatedly diagnosed the "You don't have access to this project" banner as an account-boundary issue ("Since ChatGPT projects are scoped to the owning account, I can't get in from this session") and used this as the basis for recommending account-switch or Drive-connector alternatives. No independent ChatGPT-side documentation verification was performed.
  Type: empirical
  Related decisions: [none — vendor-platform behavior]
  Testability: testable empirically (verify ChatGPT's project-access documentation, or reproduce by cross-account access attempt on a known-scoped project)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-040
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from scrape session 2026-04-18 where the assistant classified a vendor-side access failure as structural account-scoping
    Current status: UNTESTED

ASSUMPTION-041:
  Date identified: 2026-04-18
  Statement: "A Google Drive connector ('C2A2 ND chatGPT - RC data scrape' Doc) is the most promising unblocked route but needs Drive auth setup." The assistant framed the Drive staging route as the most durable option for future ND-account scrapes, implicitly ranking it above manual ChatGPT export and copy-paste on a scope-of-future-use criterion.
  Context: Scrape session 2026-04-18 and evening cowork→chat summary. Tom rejected both the manual-export and computer-use fallback options; the Drive route was labeled "most durable if more ND-account scrapes are expected." Unstated: whether ND-account scrapes are actually expected to recur; whether Drive auth setup friction is cheaper than route (b) or (c) per-scrape.
  Type: architectural
  Related decisions: OPEN-024
  Testability: testable empirically (count ND-account scrape attempts over next 4 weeks; compare per-scrape friction of Drive-staged vs. manual-export routes)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-041
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from scrape session 2026-04-18 + evening cowork_summary.md where the Drive route was ranked relative to alternatives on a future-scrape-frequency criterion
    Current status: UNTESTED

ASSUMPTION-042:
  Date identified: 2026-04-18
  Statement: "Five consecutive Chrome-extension connection failures across three calendar days is not transient" — the pattern warrants manual Chrome-side remediation (confirm extension installed/enabled in target profile, confirm sign-in, disable/re-enable to force reconnect) rather than continued retry.
  Context: Evening cowork→chat sync 2026-04-18. The summary explicitly stated this threshold judgment in its header warning. First time in the project's history that a retry-as-default policy is explicitly overridden by a manual-intervention recommendation based on failure count + calendar-day span.
  Type: methodological
  Related decisions: DECISION-015 (Agent 16 monitor scope, indirectly), OPEN-022 (cross-channel drift monitor)
  Testability: testable empirically (track whether manual Chrome reset resolves the connection; if yes, the "not transient" classification is supported and sets precedent for explicit extension-health thresholds)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-042
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from evening cowork_summary.md header where a count-based transience threshold was invoked for the first time against the Chrome MCP channel
    Current status: UNTESTED

ASSUMPTION-043:
  Date identified: 2026-04-18
  Statement: PROP-2026-04-18-001 (Wolfram × Luz Christopher Seiberth, "Hypergraphing the Space of Reason," 2026-04-08) "opens a genuinely new Wolfram ↔ analytic-philosophy corridor not yet in `cross_program_index.md`." The proposal asserts a structurally new cross-tradition edge connecting the Post-Spacetime cluster (Wolfram) to the Flourishing-and-Tradition cluster (Stump / McGilchrist via Brandom and MacIntyre).
  Context: Wolfram Saturday-specialist run 2026-04-18 and evening cowork_summary.md's "For Morning Discussion" thread #4. The claim is a specific falsifiable assertion about the current state of `cross_program_index.md` — either the Wolfram ↔ analytic-philosophy edge already exists there or it does not. No structural analysis of the Seiberth hypergraph argument was performed before the corridor claim was made.
  Type: empirical
  Related decisions: DECISION-003 (Thousand Brains reference model), FLAG-008 (Carroll × Wolfram × Hoffman convergence)
  Testability: testable empirically (grep `cross_program_index.md` for Wolfram × Sellars/Brandom/MacIntyre/Stump edges; absence confirms novelty, presence challenges the claim)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-043
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Wolfram specialist proposal 2026-04-18 and evening summary's thread #4
    Current status: UNTESTED

ASSUMPTION-044:
  Date identified: 2026-04-18
  Statement: "DECISION-021 (candidate) loaded Friday's narrator context into today's Dispatch session — the SessionStart hook fired and oriented the agent correctly." The loading half of the cross-session handoff-via-file pattern (written to `~/Documents/Claude/Handoffs/latest.md`) worked on its first real stress test, partially corroborating ASSUMPTION-035.
  Context: "Wiki visualization architecture in dispatch mode" session 2026-04-18 — the resume-session skill produced a coherent orientation brief that summarized Friday's narrator-regenerator debugging without re-prompting. The assistant and the evening summary both concluded the hook itself lands; only the payload-execution half remains untested because Tom pivoted the session to the ChatGPT scrape instead of executing the Python helper work.
  Type: architectural
  Related decisions: DECISION-021 (candidate), ASSUMPTION-035, OPEN-026
  Testability: testable empirically (already partially tested 2026-04-18 — loading half supported; payload half requires a future Dispatch session where no user pivot occurs)
  Status: PARTIALLY-SUPPORTED (loading half only; by own stress test 2026-04-18)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-044
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Dispatch session 2026-04-18 + evening cowork_summary.md thread #1 noting the split outcome (loading works, execution bypassed by user pivot)
    Current status: PARTIALLY-SUPPORTED (loading-half only, by direct observation)

ASSUMPTION-045:
  Date identified: 2026-04-20
  Statement: "Other thinkers well-covered / no primary-source material inside 60-day window" — the Phase 2 Hunt output of the 2026-04-20 wiki daily run justified producing only 2 Levin proposals (not proposals for the other 10 thinkers) on the grounds that the remaining tradition-scope agents had adequate recent coverage in the wiki already.
  Context: C2A2 wiki daily run session 2026-04-20 Phase 2 report. Coverage-adequacy claim used as the gating criterion for which specialists to run on a Monday slot. Potentially in tension with the parallel-scheduled "C2a2-agent-levin-friston" specialist task, which was still running web searches at end-of-day — two scheduled tasks may have redundant Monday-Levin scope without explicit coordination.
  Type: empirical / methodological
  Related decisions: DECISION-005 (master wiki), PRESUMPTION-031 (rotation-schedule coverage), PRESUMPTION-049 (scope-partition with Monday specialist)
  Testability: testable empirically (enumerate per-thinker latest-primary-source dates in prs_triplets.md files; compute the 60-day-window coverage state at 2026-04-20 08:00 and check which thinkers actually fell outside it)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-045
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from wiki daily run 2026-04-20 Phase 2 report where the coverage claim was used as gating criterion
    Current status: UNTESTED

ASSUMPTION-046:
  Date identified: 2026-04-20
  Statement: Filtering active Pattern-Detector findings from 17 down to the "most significant 11" preserves actionable signal in the morning briefing without loss of operationally relevant content. The full set remains available in `pattern_detector_findings.md` for deeper reference.
  Context: Morning walk handoff session 2026-04-20 autonomous-choices note. Stated explicitly: "Active findings were filtered to the most significant 11 of 17 to keep the briefing scannable." Selection criterion for which 6 findings were omitted was not documented.
  Type: methodological
  Related decisions: DECISION-005 (master wiki briefing surface), PRESUMPTION-053 (selection criterion unaudited)
  Testability: testable empirically (track over a 2-4 week window whether Tom's briefing-derived actions ever require consulting the unfiltered set; compute systematic-omission rate by finding-type)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-045
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from morning-walk-handoff session 2026-04-20 autonomous-choices note where the 17→11 filter was explicitly committed to
    Current status: UNTESTED

ASSUMPTION-047:
  Date identified: 2026-04-20
  Statement: A discrepancy between the master-wiki narrative (shows 8 pending proposals as of 2026-04-17) and the actual inbox contents (12 pending as of 2026-04-20) should be flagged transparently in the briefing rather than silently reconciled. Transparency is the correct default at the briefing layer.
  Context: Morning walk handoff session 2026-04-20 autonomous-choices note. Stated explicitly: "I flagged this discrepancy in the briefing rather than silently reconciling it." First explicit normative stance from the briefing agent on how to handle upstream staleness.
  Type: methodological (normative commitment)
  Related decisions: DECISION-005 (master wiki), OPEN-027 (null-coverage audit pattern)
  Testability: framework commitment (normative — "flag, don't reconcile" is a stance about briefing-layer epistemic honesty, not a falsifiable empirical claim; however the shape of the related inconsistency — 3-day master-wiki staleness paired with git-index.lock block — is empirically falsifiable once Tom clears the .git/index.lock)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-047
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from morning-walk-handoff session 2026-04-20 autonomous-choices note, first explicit flag-over-reconcile commitment at the briefing layer
    Current status: UNTESTED

ASSUMPTION-048:
  Date identified: 2026-04-20
  Statement: An execution queue whose only entry is "a stale placeholder example from 2026-03-31" can be correctly reported as "clear" per the briefing's intent. The briefing layer may interpret "clear" to mean "no actionable items" rather than literal "zero items."
  Context: Morning walk handoff session 2026-04-20 autonomous-choices note: "the execution queue's only entry is a stale placeholder example from 2026-03-31; I reported it as 'clear' per the briefing's intent." Explicit normative interpretation choice at the briefing layer; extends the null-framing pattern previously surfaced for walk notes (PRESUMPTION-042/048) — "clear" is a semantic framing decision.
  Type: methodological (normative interpretation)
  Related decisions: DECISION-005, PRESUMPTION-042, PRESUMPTION-048
  Testability: framework commitment (normative); empirically traceable by checking whether the stale placeholder example is ever cleared from the queue file itself
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-048
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from morning-walk-handoff session 2026-04-20 autonomous-choices note, stated normative-interpretation commitment
    Current status: UNTESTED

ASSUMPTION-049:
  Date identified: 2026-04-20
  Statement: "Session lifetime = one full tradition agent run (all pending proposals for that tradition), NOT one session per proposal." The atomic unit of the Layer 2 execution/trigger protocol is a single tradition agent run, not a proposal-level invocation.
  Context: C2a2 caching architecture monday session 2026-04-20 (local_2c0fcbc1). Stated in the task brief and materialized in the Execution Protocol v1.0 deliverable. Architectural commitment to "one session = one agent run" — see Monday Report header.
  Type: architectural
  Related decisions: candidate DECISION-023 (caching/execution protocol; not yet formalized), DECISION-005, ASSUMPTION-050, ASSUMPTION-053
  Testability: testable empirically (measure cost-per-proposal and cache-hit rate across both regimes once v1.0 lands on Levin 2026-04-27)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-049
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from C2a2 caching architecture monday session (supplementary run 2) — explicit task-brief commitment and Execution Protocol v1.0 design statement
    Current status: UNTESTED

ASSUMPTION-050:
  Date identified: 2026-04-20
  Statement: "The RC Wiki (Layer 1, 49 files, slow-changing) belongs in the static prefix of each tradition agent — thinker profiles, concept nodes, tradition summaries load once per session. The C2A2 vault daily activity (proposals, findings, decisions) belongs in the dynamic suffix only. Date-stamped filenames (PROP-YYYY-MM-DD-NNN) must NOT be loaded into the static prefix — guaranteed daily cache miss."
  Context: C2a2 caching architecture monday session 2026-04-20 task brief + Execution Protocol v1.0. Three interlocking claims about what content may enter the cached region: (a) the 49 RC Wiki files are static-eligible; (b) vault daily activity is dynamic-only; (c) date-stamped names are cache-miss hazards and must be excluded from the cached region.
  Type: architectural
  Related decisions: candidate DECISION-023 (caching/execution protocol), PRESUMPTION-055, PRESUMPTION-057
  Testability: testable empirically (verify via byte-stability smoke test that the static prefix is identical across consecutive sessions; measure cache-hit percentages before/after deployment; audit the cached region for any accidental date-stamp inclusion)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-050
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from C2a2 caching architecture monday session (supplementary run 2) — three-part partitioning rule stated explicitly in task brief and materialized in Execution Protocol v1.0
    Current status: UNTESTED

ASSUMPTION-051:
  Date identified: 2026-04-20
  Statement: "All tool definitions must load upfront and never mutate mid-session." The cached region's integrity depends on tool schemas being frozen at session start; dynamic tool loading or deferred-schema resolution would invalidate the prefix.
  Context: C2a2 caching architecture monday session 2026-04-20 task brief. This is an invariant condition on the tool layer that the Execution Protocol v1.0 depends on; it is orthogonal to the static/dynamic prefix partition but required for cache determinism.
  Type: architectural
  Related decisions: candidate DECISION-023 (caching/execution protocol), ASSUMPTION-050
  Testability: testable empirically (verify on each session launch that no deferred tool-schema fetch occurs after turn 1; instrument turn-by-turn tool manifest diffs and flag any mid-session mutations)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-051
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from C2a2 caching architecture monday session (supplementary run 2) — invariant condition on tool-layer mutability stated in task brief
    Current status: UNTESTED

ASSUMPTION-052:
  Date identified: 2026-04-20
  Statement: "This single change could cut C2A2 operating costs 70–80% as the vault grows" (task brief), decomposed in the Monday Report deliverable as "~50% per-run cost reduction projected for Levin specifically; 70–80% aggregate comes from pipeline agents with appended turns." Quantitative prediction about end-to-end cost impact.
  Context: C2a2 caching architecture monday session 2026-04-20. Cost-reduction projection rests on Avi Chawla's prompt-caching article (cited in task brief) and on the pipeline-as-appended-turns reorganization (ASSUMPTION-053). Numeric claim will be directly verifiable after rollout.
  Type: empirical
  Related decisions: candidate DECISION-023 (caching/execution protocol), ASSUMPTION-049, ASSUMPTION-053
  Testability: testable empirically (compute pre- vs. post-deployment per-session and aggregate cost; target 2026-04-27 Levin v1.0 run is the first data point; cumulative savings audit at 4-week and 8-week marks)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-052
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from C2a2 caching architecture monday session (supplementary run 2) — explicit numeric prediction in task brief and Monday Report
    Current status: UNTESTED

ASSUMPTION-053:
  Date identified: 2026-04-20
  Statement: "The self-awareness pipeline (14a→14b→15a→15b→15c) should run as appended turns in one session, not separate sessions." Architectural commitment that sibling-stage self-awareness agents share a single session rather than spawning five.
  Context: C2a2 caching architecture monday session 2026-04-20 task brief + Execution Protocol v1.0: "self-awareness pipeline migrates from 5 sessions to 1 appended-turn session." This reorganization is cited as the primary driver of the 70–80% aggregate cost reduction in ASSUMPTION-052.
  Type: architectural
  Related decisions: candidate DECISION-023, ASSUMPTION-049, ASSUMPTION-052, the 14a/14b agent-definition files (may require update to reflect appended-turn topology)
  Testability: testable empirically (compare cost, turn-count, and output-completeness of a 5-session pipeline run vs. a 1-session appended-turn run on a matched input transcript)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-053
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from C2a2 caching architecture monday session (supplementary run 2) — explicit pipeline-topology commitment in task brief and Execution Protocol v1.0
    Current status: UNTESTED

ASSUMPTION-054:
  Date identified: 2026-04-20
  Statement: "Byte-stability [is] a valid smoke-test proxy for cache determinism." One of three specified smoke tests for the RC Wiki MCP install; the byte-stability check verifies that successive sessions produce identical static-prefix bytes, which in turn is treated as the operational criterion for whether the cached region will actually hit.
  Context: C2a2 caching architecture monday session 2026-04-20 — RC Wiki MCP Install Plan deliverable specifies "three smoke tests including byte-stability for cache determinism" as the rollout gate.
  Type: methodological
  Related decisions: candidate DECISION-023 (caching/execution protocol), ASSUMPTION-050, ASSUMPTION-051
  Testability: testable empirically (directly: run two consecutive sessions, diff the static-prefix bytes; indirectly: verify cache-hit telemetry matches byte-identical prefix expectations)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-054
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from C2a2 caching architecture monday session (supplementary run 2) — smoke-test specification in the RC Wiki MCP Install Plan deliverable
    Current status: UNTESTED

ASSUMPTION-055:
  Date identified: 2026-04-21
  Statement: "git commit/push not possible from sandbox — the git repo path (`/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project`) is outside the mounted sandbox filesystem." Stated directly in today's wiki daily run Phase 6 report as the new (second, compound) reason Phase 6 failed — in addition to the 2026-04-16 `.git/index.lock`, the sandbox mount topology itself does not include the repo.
  Context: C282 wiki agent daily run 2026-04-21 — Phase 6 attempted git commit/push, discovered the repo path is outside the mounted filesystem. Changes the Phase 6 failure from "stale lock" to "stale lock AND unreachable path." This materially reframes the DECISION-018 rescue plan: clearing the lock in the sandbox is not sufficient if the sandbox cannot reach the repo for the commit step.
  Type: architectural
  Related decisions: DECISION-018 (rescue commit of wiki repo), OPEN-031 (cross-task coordination), ASSUMPTION-049–054 (caching architecture pre-flight dependencies)
  Testability: testable empirically (verify on scheduled-task launch whether the mount set includes the repo path; compare the mount topology against a prior successful Phase 6 run; instrument a pre-flight reachability probe)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-055
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from C282 wiki agent daily run 2026-04-21 Phase 6 output — explicit statement of the sandbox-unreachable-repo failure mode
    Current status: UNTESTED

ASSUMPTION-056:
  Date identified: 2026-04-21
  Statement: "An honest null is more valuable than thin proposals." Stated judgment from today's Hawkins/Hoffman Tuesday specialist slot after three Hoffman candidates were evaluated and rejected (already-captured v2 preprint; abstract-less Harvard talk; out-of-window Nov 2025 MBS interview).
  Context: C2a2 agent hawkins hoffman 2026-04-21 — Hawkins agent: 0 proposals; Hoffman agent: 0 proposals. The specialist transparently reported the zero-yield and rationalized it as preferable to emitting weak proposals. First explicit articulation by a tradition specialist of a null-is-valuable stance; previously implicit in how specialists chose not to push borderline candidates.
  Type: methodological
  Related decisions: OPEN-033 (specialist-task invariants — turn-cap context), PRESUMPTION-053 (briefing-layer filter unaudited)
  Testability: testable empirically (compare specialist null-day rates against proposal-quality metrics in the subsequent review pipeline — do null-day specialists yield higher-approval-rate proposals the next session, or not?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-056
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from C2a2 agent hawkins hoffman 2026-04-21 run summary — "Judgment: an honest null is more valuable than thin proposals."
    Current status: UNTESTED

ASSUMPTION-057:
  Date identified: 2026-04-21
  Statement: "The 'Active Findings Requiring Attention' table includes the full set of findings currently marked Active or Highest Priority in `pattern_detector_findings.md` (FINDING-005, 009, 011, 011a, 012, 013, 014, 015, 016, 017). Older findings that are now subsumed or downgraded (001, 002, 003, 004, 006, 007, 008, 010) were excluded to keep the briefing concise." First stated filter criterion for the 17→11 briefing reduction.
  Context: Morning walk cowork handoff 2026-04-21 — today's briefing explicitly documents the filter criterion that yesterday's ASSUMPTION-046 / PRESUMPTION-053 flagged as unaudited. Notable: one day later the filter rule is now stated, converting a 14b item (unstated presumption that the filter was correct by construction) into a 14a item (the rule is "Active OR Highest Priority, excluding subsumed/downgraded"). The rule is still not formally audited against an independent criterion, but it is now visible.
  Type: methodological
  Related decisions: candidate DECISION-022 (briefing-layer audit contract), ASSUMPTION-046 (17→11 filter is correct by construction), PRESUMPTION-053 (filter unaudited)
  Testability: testable empirically (audit the 6 excluded findings — 001, 002, 003, 004, 006, 007, 008, 010 — against the stated criterion; confirm each is either "subsumed" or "downgraded" per pattern_detector_findings.md; check whether any excluded finding has subsequent activity that should have re-qualified it)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-057
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Morning walk cowork handoff 2026-04-21 run summary — the autonomous-choices note now explicitly lists the filter rule, moving the 17→11 reduction from unstated (yesterday's PRESUMPTION-053) to stated.
    Current status: UNTESTED

ASSUMPTION-058:
  Date identified: 2026-04-21
  Statement: "Today's five observed session outputs (wiki daily run, Hawkins/Hoffman specialist, Agent 16, morning chat scrape, morning walk handoff) collectively give enough signal for a legitimate end-of-day brief" despite no 14a/14b cycle having run. Stated coverage-adequacy claim from the evening cowork-to-chat sync's autonomous-choices note.
  Context: C2a2 evening cowork to chat 2026-04-21 — the evening sync proceeded to write and deliver a full architectural brief even though the primary self-awareness pipeline (14a/14b) did not run today. The adequacy claim rests on the substitutability of scheduled-task outputs for formal extraction outputs. Extends ASSUMPTION-045's coverage-adequacy pattern one level deeper: yesterday's three-session window was claimed representative-of-the-day; today's five-session window is claimed sufficient-to-substitute-for-the-missing-cycle.
  Type: methodological
  Related decisions: ASSUMPTION-045 (today's window representative), candidate DECISION-022 (briefing-layer audit contract); related OPEN-034 (self-awareness-run absence as tracked event)
  Testability: testable empirically (compare the evening-sync brief's claims against what a 14a/14b cycle would have extracted from the same transcripts — does the sync-brief preserve the architecture signal the formal cycle would have captured, or does it miss items?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-058
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from C2a2 evening cowork to chat 2026-04-21 autonomous-choices note — "Wrote the summary despite no today 14a/14b cycle having run — the wiki daily run, Hawkins/Hoffman specialist, Agent 16, chat scrape, and morning walk handoff collectively give enough signal for a legitimate end-of-day brief."
    Current status: UNTESTED

ASSUMPTION-059:
  Date identified: 2026-04-21
  Statement: "Triggering 14a/14b manually from an evening sync would be a scheduler-override — not something an evening sync task should presume." Stated scope-boundary claim for the evening-sync task's authority.
  Context: C2a2 evening cowork to chat 2026-04-21 autonomous-choices note — the sync explicitly declined to manually fire the missing self-awareness cycle, on the grounds that such an override exceeds an evening-sync task's mandate. First explicit articulation of inter-task authority boundaries at the scheduler layer; adjacent to the OPEN-031 coordination-contract question but from the opposite direction (OPEN-031 asks what coordination primitives should exist; this claim asserts a default scope floor).
  Type: normative
  Related decisions: OPEN-031 (cross-task coordination), candidate DECISION-024 (specialist-task invariants), PRESUMPTION-049 (scope-partition between tasks)
  Testability: testable via literature (scheduler / orchestrator design patterns — which sub-tasks are permitted cross-task triggers, which aren't, and what criteria separate them); testable empirically (measure whether alternative designs that permit evening-sync to fire missing cycles improve coverage without destabilizing scheduling)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-059
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from C2a2 evening cowork to chat 2026-04-21 autonomous-choices note — "Did not attempt to fire 14a/14b manually from this evening sync — that's a scheduler-override decision, not something an evening sync task should presume."
    Current status: UNTESTED

ASSUMPTION-060:
  Date identified: 2026-04-21
  Statement: "Read-only checks on still-running specialist sessions are consistent with Monday's Levin-Friston precedent where natural termination was the judgment call." Stated precedent-application rule for observing (but not intervening on) runaway-looking specialist sessions.
  Context: C2a2 evening cowork to chat 2026-04-21 autonomous-choices note — today's sync observed two still-running sessions (Morning project status, Morning system health) showing the Levin-Friston pattern (unbounded with no writes) and declined to investigate further, citing the Monday-04-20 precedent. First explicit formalization of a "natural-termination-wins" precedent; converts what was implicit operational behavior into a stated contract. Notable tension with candidate DECISION-024 (turn-cap default) which would explicitly interrupt such runs.
  Type: methodological
  Related decisions: candidate DECISION-024 (specialist-task turn-cap), OPEN-033, PRESUMPTION-054 (no turn-cap)
  Testability: testable empirically (track natural-termination outcomes across all cases where the precedent is applied; measure fraction that terminate cleanly vs. require manual intervention; compare cost of natural-termination vs. turn-cap discipline)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-060
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from C2a2 evening cowork to chat 2026-04-21 autonomous-choices note — "Did not attempt to investigate the two still-running Morning project status / Morning system health sessions — read-only checks only, consistent with Monday's Levin-Friston precedent where natural termination was the judgment call."
    Current status: UNTESTED

ASSUMPTION-061:
  Date identified: 2026-04-21
  Statement: "Leaving validated premises sitting outside the formal decision register is its own form of silent reconciliation, which is exactly what PREMISE-006 says not to do." Stated by Chat-side Claude on the morning walk in reaction to Monday's evening sync; operationalizes PREMISE-006 (transparent-flagging-over-silent-reconciliation) as a reflexive constraint applying to the validated-premises → formal-decision pipeline.
  Context: Morning chat scrape 2026-04-21 (walk conversation "Morning planning walks and name confusion") — the claim was made in the context of arguing that candidate DECISION-022 (briefing-layer audit contract) should be drafted this week rather than deferred, on the grounds that deferring a validated premise is itself a violation of the premise's own disposition. Makes DECISION-022 "a test of PREMISE-006 rather than just a rendering-convention choice."
  Type: epistemic
  Related decisions: PREMISE-006 (= INCORPORATE of ASSUMPTION-047), candidate DECISION-022 (briefing-layer audit contract), ASSUMPTION-047 (flag-vs-reconcile disposition), PRESUMPTION-041 (implicit-decision drift)
  Testability: testable via literature (meta-epistemics — does a norm against silent reconciliation self-apply to the register of decisions that catalogs the norm? philosophy-of-science literature on self-referential norms; logic/formal-systems literature on reflection principles); testable empirically (measure whether the pipeline that produces PREMISE-NNN validations itself preserves or violates the stated transparency disposition over time)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-061
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Morning chat scrape 2026-04-21 summary — Chat-side Claude's direct quote on the morning walk, framing DECISION-022's deferral as a PREMISE-006 violation.
    Current status: UNTESTED

ASSUMPTION-062:
  Date identified: 2026-04-21
  Statement: "A weak circuit breaker beats none, and you can tune the number later." Methodological principle offered by Chat-side Claude for the OPEN-033 → candidate-DECISION-024 transition (specialist-task turn-cap default = 20).
  Context: Morning chat scrape 2026-04-21 — Chat-side Claude's endorsement of a minimal-form DECISION-024 ("specialist tasks SHOULD declare turn-cap; missing = 20"). The stated principle is approximation-over-blocking: better to ship a conservative default than to block on finding the optimal threshold. Generalizable beyond OPEN-033 to other transience/invariant settings (OPEN-032 staleness thresholds, OPEN-012 alert policies).
  Type: methodological
  Related decisions: candidate DECISION-024 (specialist-task invariants), OPEN-033, OPEN-032 (transience-threshold generalization), PRESUMPTION-054 (no turn-cap)
  Testability: testable via literature (design-under-uncertainty patterns — worse-is-better, satisficing, ship-and-iterate vs. block-on-optimal); testable empirically (track how many "missing=20" default caps produce false-positive interruptions vs. true-positive runaway interrupts over N specialist runs)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-062
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Morning chat scrape 2026-04-21 summary — Chat-side Claude's stated principle for OPEN-033 → DECISION-024 minimal-form draft.
    Current status: UNTESTED

ASSUMPTION-063:
  Date identified: 2026-04-26
  Statement: "Stump hasn't yet made the necessary transitions to a new mind-everywhere monist metaphysics. Follow Levin and Hoffman and Kastrup on metaphysical issues." Tom's directly-stated demotion of Stump on metaphysics, replaced by a Levin + Hoffman + Kastrup primary on metaphysical loci.
  Context: Design-project conversation (local_4e0f61e4 "Design project architecture and timeline") about a downstream-consumer "Summa 2026 in a Year" project. The user message explicitly demoted Stump's metaphysical authority and named the Levin + Hoffman + Kastrup convergence as the new primary on metaphysics. The session committed this to a "bridges" file (`/Users/tomloughran/Documents/Claude/Projects/Summa 2026 in a Year/vault/refs/Karpathy wiki bridges.md`) external to the C2A2 wiki — no `Wiki/traditions/stump/wiki.md` was modified. Stated companion stance: "Stump remains the keystone for virtue (I-II Q.49–70), vices, faith-as-knowledge (II-II Q.1–22), the atonement, suffering" — i.e., demotion is partial (metaphysics only).
  Type: architectural / normative
  Related decisions: candidate DECISION-025 (Wright/Rohr addition + Stump metaphysical demotion), OPEN-036, OPEN-037, ASSUMPTION-005 (traditions as units), ASSUMPTION-064
  Testability: testable via literature (does the Levin–Hoffman–Kastrup convergence actually constitute a coherent monist metaphysics? do hylomorphic accounts of mind clash with these three's frames?); testable empirically (track whether the partial-demotion is sustainable across N synthesis loci or produces incoherence)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-063
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Design project architecture and timeline session 2026-04-26 — direct quote from Tom's user message demoting Stump on metaphysics.
    Current status: UNTESTED

ASSUMPTION-064:
  Date identified: 2026-04-26
  Statement: "I'll add NT Wright as scripture scholar ground truth, and Richard Rohr (The Universal Christ) as spirituality ground truth." Tom's directly-stated proposal to add two new tradition entries (Wright + Rohr) to what would become a 13-tradition C2A2 frame (11 live + 2 planned).
  Context: Same session as ASSUMPTION-063. The Cowork-side response committed Wright and Rohr to the bridges file with role assignments — Wright primary on Christology (III Q.1–59), the Supplement on last things, divine law (I-II Q.90–108), Pauline faith (II-II Q.1–22), and biblical justice; Rohr primary on contemplative life (II-II Q.171–189) and the cosmic-Christ reframe of Tertia Pars sacraments. Until `Wiki/traditions/wright/wiki.md` and `Wiki/traditions/rohr/wiki.md` exist, the synthesizer falls back on canonical works (Wright: *Resurrection of the Son of God*, *Surprised by Hope*, *Paul and the Faithfulness of God*, *Jesus and the Victory of God*; Rohr: *The Universal Christ*, *Falling Upward*, *Immortal Diamond*).
  Type: architectural
  Related decisions: candidate DECISION-025, OPEN-036, ASSUMPTION-005, ASSUMPTION-063
  Testability: testable empirically (track whether 2 new tradition entries strengthen or distort cross-program connections; track whether downstream syntheses behave coherently when Wright/Rohr are invoked); testable via literature (do scripture-scholarship and spirituality form coherent "tradition" units in the C2A2 sense, or are they disciplinary categories that cut differently from the existing 11?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-064
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Design project architecture and timeline session 2026-04-26 — direct quote from Tom's user message proposing the Wright/Rohr addition.
    Current status: UNTESTED

ASSUMPTION-065:
  Date identified: 2026-04-26
  Statement: "Strong Carroll ↔ Arkani-Hamed convergence on emergent spacetime is the highlight ... Both proposals flag this as the network's most significant in-progress paradigm-shift signal of 2026; both recommend dispatch to Master Agent and Pattern Detector." Specialist-agent claim that Carroll's Heilborn Lecture 2 (April 23, 2026, "Extracting the Universe from the Wave Function") commits him publicly to spacetime-emergence-from-Hilbert-space and structurally aligns with Arkani-Hamed's "spacetime is doomed" / amplituhedron / cosmohedron program.
  Context: C2a2 agent carroll arkanihamed 2026-04-27 (local_9e03fffa). Specialist agent's autonomous-choices note. Frames the convergence as the *network's* (i.e., C2A2's) most significant 2026 paradigm-shift signal — a strong claim about the relative importance of this signal across all 11 traditions for a calendar year.
  Type: empirical
  Related decisions: ASSUMPTION-005 (traditions as units), CROSS-???? (Carroll × Arkani-Hamed emergent-spacetime — to be created by Pattern Detector if not already), candidate DECISION-025 (Stump metaphysical demotion has thematic parallel: same week, Levin+Hoffman+Kastrup are named monist-metaphysical primaries while Carroll+Arkani-Hamed are flagged as physics-paradigm-shift primaries — a possible structural pattern of "named convergence pairs/triples becoming the year's central architectural events")
  Testability: testable via literature (is "spacetime emerges from Hilbert space" actually claimed in Carroll's Heilborn Lecture transcript, and does it match the structural shape of Arkani-Hamed's program?); testable empirically (track the convergence's reception across the wiki — does the SUPER-BRIDGE candidate ratify or revise it?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-065
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Carroll+Arkani-Hamed specialist 2026-04-26 autonomous-choices note.
    Current status: UNTESTED

ASSUMPTION-066:
  Date identified: 2026-04-26
  Statement: Wolfram's stance on philosophy is "method-export to philosophy rather than method-import from philosophy" — recasts CROSS-016 (Carroll's Bayesian standard), CROSS-024 (Ruliad as ontological framework), and CROSS-026 (observer-dependence cluster). Specialist-agent first-explicit articulation of this directional reading; flags "potential methodological alliance with Kastrup."
  Context: C2a2 agent wolfram 2026-04-27 (local_c19e62e0). Specialist agent's autonomous-choices note in support of PROP-2026-04-27-004 (Last Theory #081 "Wolfram on philosophy"). The reading reverses the implicit prior framing in CROSS-016, 024, 026 — those entries had presumed Wolfram was *receiving* philosophical methodology rather than *exporting* his computational methodology to philosophy.
  Type: epistemic / methodological
  Related decisions: ASSUMPTION-005, CROSS-016, CROSS-024, CROSS-026, CROSS-021 (Wolfram × Hoffman convergence), CROSS-031 (asymmetry across McGilchrist/Friston/Wolfram), CROSS-032 (Hoffman trace-blanket ⊇ Markov blanket)
  Testability: testable via literature (does the philosophy-of-science literature characterize Wolfram's method as export-to-philosophy or import-from-philosophy?); testable empirically (does the reframing improve the predictive value of CROSS-016/024/026 for what Wolfram says next?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-066
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Wolfram specialist 2026-04-26 autonomous-choices note — direct quote on method-export-to-philosophy stance and CROSS-entry recasting.
    Current status: UNTESTED

ASSUMPTION-067:
  Date identified: 2026-04-26
  Statement: "Stump's 'What Are We? Collective Neuroscience, Metaphysics, and Theology' (Religious Studies, Cambridge) and Fredrickson et al.'s micro-intervention RCT (Journal of Positive Psychology) form a paired metaphysics+empirics signal for C2A2: Stump supplies a hylomorphic account of corporate substance grounded in collective-neuroscience findings (mirror-neuron coupling) — directly anchoring claims about peoples, the church-as-body, and by extension MacIntyrean traditions as real composites. Fredrickson et al. supply a working, randomized-controlled, technology-mediated intervention for raising weak-tie positivity resonance — the candidate empirical mechanism by which Stump's corporate substances would actually be cultivated. Together they bridge the metaphysical and operational layers of the C2A2 architecture."
  Context: C2a2 agent stump fredrickson 2026-04-27 (local_244b67e3). Specialist agent's autonomous-choices note. Paired-tradition reading that explicitly treats Stump as supplying live metaphysics — this stands in direct tension with ASSUMPTION-063 (same-day stated demotion of Stump on metaphysics). Today produced two simultaneous and conflicting readings of Stump's metaphysical role.
  Type: architectural / empirical
  Related decisions: ASSUMPTION-063 (DIRECT TENSION — same day, opposite stance on Stump's metaphysical role), OPEN-037, ASSUMPTION-005 (traditions as units), candidate DECISION-025
  Testability: testable via literature (is the pairing of hylomorphic-corporate-substance metaphysics with positivity-resonance weak-tie RCTs actually a coherent metaphysics+empirics bridge, or is it a category-error pairing?); testable empirically (track downstream syntheses that invoke the pairing — do they produce coherent claims or breakdown?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-067
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Stump+Fredrickson specialist 2026-04-26 autonomous-choices note — direct quote on metaphysics+empirics bridge.
    Current status: UNTESTED

ASSUMPTION-068:
  Date identified: 2026-04-26
  Statement: Master-wiki-narrative-gap is to be surfaced rather than fabricated. "Master wiki's most recent run narrative is 2026-04-22; no entries for 04-23 through 04-26. Surfaced this in the briefing footer rather than fabricating intervening state." Briefing-layer epistemic stance: when an upstream artifact is stale, the briefing notes the staleness rather than back-filling intervening state.
  Context: Morning walk cowork handoff 2026-04-27 (local_e1fd0a81). Autonomous-choices note. Closely parallels ASSUMPTION-047 (flag-over-reconcile stance on master-wiki staleness, INCORPORATEd as PREMISE-006) and ASSUMPTION-068 is essentially a re-affirmation of PREMISE-006 in a fresh staleness case (4-day gap rather than the prior 1-2 day cases). This is the largest master-narrative gap PREMISE-006 has handled.
  Type: methodological / normative
  Related decisions: PREMISE-006 (re-affirmation in 4-day case), ASSUMPTION-047, OPEN-038
  Testability: testable empirically (are 4-day surfaced gaps as recoverable as 1-day surfaced gaps? Does the surfacing format scale, or does staleness-floor break PREMISE-006 at some N-day threshold?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-068
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Morning walk cowork handoff 2026-04-26 autonomous-choices note — re-affirmation of PREMISE-006 against a 4-day gap.
    Current status: UNTESTED

ASSUMPTION-069:
  Date identified: 2026-04-26
  Statement: Proposal-ID collisions are flagged-and-rolled-forward rather than blocked-on. Today's morning walk handoff "Flagged a proposal-id collision (two `PROP-2026-04-16-001`, two `PROP-2026-04-16-002`) for resolution before the next ingestion run." The Carroll+Arkani-Hamed specialist similarly self-detected an ID collision with parallel agents and self-renumbered (writing 005 and 006 after detecting that 001–004 had been written by parallel agents). Stance: collisions are real-time-detectable and resolvable by renumbering or by flagging-for-later, not blockers.
  Context: Morning walk cowork handoff 2026-04-27 (local_e1fd0a81) and C2a2 agent carroll arkanihamed 2026-04-27 (local_9e03fffa). Two independent same-day instances of the same stance.
  Type: methodological
  Related decisions: DECISION-001 (sequential ID fix — original deprecation of agent-assigned IDs), OPEN-001 (should agent-assigned IDs be deprecated entirely), ASSUMPTION-046 (briefing-layer 17→11 filter analogue: flag-without-block)
  Testability: testable empirically (track ID-collision frequency over N parallel agent runs; track whether flag-without-block ever produces a downstream incident)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-069
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from two same-day instances (morning walk handoff and Carroll+Arkani-Hamed specialist) of the same flag-and-roll-forward stance on proposal-id collisions.
    Current status: UNTESTED

ASSUMPTION-070:
  Date identified: 2026-04-26
  Statement: "Useful data point in the screenshot: the playlist box on the right says **'308 episodes'** — not 365. That changes the pace math." Empirical correction to the assumed source-coverage size of the YouTube source playlist for the Summa 2026 in a Year derivative project (and any C2A2 agent that consumes the same playlist).
  Context: Design project architecture and timeline session 2026-04-26 (local_4e0f61e4). Cowork-side observation during the Day-1 smoke test through Chrome MCP. Affects C2A2 indirectly: any specialist agent that pulls from the same YouTube source set inherits the corrected count and pace expectation. The session noted "That changes the pace math" but did not propagate the correction to a global wiki update.
  Type: empirical
  Related decisions: candidate DECISION-025, OPEN-036, ASSUMPTION-064
  Testability: testable empirically (verify the 308 count by independent count of the playlist; track whether the pace-math correction propagates to specialist agents that consume the same source)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-070
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Design project architecture and timeline 2026-04-26 — direct quote on episode count discovery.
    Current status: UNTESTED

ASSUMPTION-071:
  Date identified: 2026-04-27
  Statement: Browser-authentication on the user's behalf is an agent-prohibited / explicit-permission action. "I cannot sign Tom in on his behalf — that requires him to enter credentials directly" / "Tom is not present and authentication is a prohibited/explicit-permission action." First explicit two-instance same-day articulation that agents with Chrome MCP control are not authorized to bypass the user-mediated browser sign-in step.
  Context: Two same-day failure events that produced identical normative articulations. (1) Morning chat-to-cowork scrape (local_51b0bf0e): "I cannot sign Tom in on his behalf, so I wrote a status note to today's output file explaining the failure." Chrome navigated to https://claude.ai → redirected to /login. (2) Evening cowork-to-chat sync (local_f6ebb0fc): "Tom is not present and authentication is a prohibited/explicit-permission action — I cannot log Tom in." Same /login redirect, same normative refusal. Both failure modes block the daily Chat↔Cowork sync entirely; the cowork→chat .md file becomes the fallback authoritative record.
  Type: methodological / normative
  Related decisions: candidate DECISION-021 (cross-session handoff pattern — auth gap is upstream of file-based handoff), OPEN-039 (sandbox infrastructure escalation cluster — auth-gap may belong to the same escalation track as egress and mount-topology)
  Testability: testable via literature (does the agent-systems literature on user-on-behalf-of authentication endorse this prohibition, or is it specific to Anthropic's product policy?); testable empirically (track whether long-lived auth tokens, API-based access, or pre-authenticated browser profiles can substitute for live credential entry at the next architectural pass)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-071
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from two same-day failure events (morning chat scrape + evening cowork→chat sync) that produced identical normative articulations of the auth-prohibition stance.
    Current status: UNTESTED

ASSUMPTION-072:
  Date identified: 2026-04-27
  Statement: A 5-day lit-search backlog can be drained in a single 15a/15b/15c cycle without quality degradation. "Items processed: 58 total (19 new + 39 re-triggered)" in one run; pipeline lag drops from 5 days to 0. Operational claim about pipeline throughput at the 50+-item batch scale.
  Context: C2A2 lit-search pipeline 2026-04-27 (local_64b9c31c) processed today's 19 new items (from yesterday's 14a/14b cycle that had been QUEUED) plus 39 re-triggered weekly-refresh items in a single end-to-end 15a/15b/15c run. The autonomous-choices note acknowledged the throughput claim implicitly by treating 58 items as a normal cycle workload.
  Type: empirical / methodological
  Related decisions: DECISION-006 (15a/15b independence), DECISION-009 (developmental maturity model — pipeline-throughput is a Stage 1 health indicator)
  Testability: testable empirically (compare disposition quality of single-cycle 58-item batches against 5 separate daily-cycle 12-item batches; track whether INCORPORATE/MONITOR/REVISE rates differ)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-072
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from C2A2 lit-search pipeline 2026-04-27 — operational claim that 5-day backlog absorbed in single cycle.
    Current status: UNTESTED

ASSUMPTION-073:
  Date identified: 2026-04-27
  Statement: 15c disposition heuristic "PRESUMPTION + strong challenge → REVISE" is the operative spec rule for the lit-search-pipeline net evaluator. Stated in autonomous-choices note as the explicit prioritization heuristic that produced 9 REVISE flags (mostly PRESUMPTIONs).
  Context: C2A2 lit-search pipeline 2026-04-27 autonomous-choices note: "Disposition reasoning prioritized the heuristic 'PRESUMPTION + strong challenge → REVISE' from the 15c spec, which produced 9 REVISE flags (mostly PRESUMPTIONs) for Tom's review." First explicit citation of the heuristic as the operative rule rather than as one consideration among several.
  Type: methodological
  Related decisions: DECISION-006, candidate DECISION-022 (briefing-layer audit contract — extends to net-evaluator-layer audit), DECISION-007 (provenance protocol — heuristic is consistent with PRESUMPTION + STRONG-CHALLENGE → CHALLENGED reconciliation rule)
  Testability: testable via literature (does the design-of-net-evaluator literature endorse a tag-asymmetric disposition rule like "treat PRESUMPTION + strong-challenge differently from ASSUMPTION + strong-challenge"?); testable empirically (track whether the 9 REVISE flags' downstream actionability differs from the 7 MONITOR flags over N weeks)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-073
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from C2A2 lit-search pipeline 2026-04-27 autonomous-choices note — explicit citation of disposition heuristic.
    Current status: UNTESTED

ASSUMPTION-074:
  Date identified: 2026-04-27
  Statement: For re-triggered (weekly-refresh) lit-search items, "no new external evidence" is a meaningful basis for carrying forward prior disposition rather than fabricating new findings. "For 39 re-triggered items, this automated cycle had no new external evidence; refresh entries record 'no new literature surfaced' and carry forward prior MONITOR disposition rather than fabricating new findings." Extends PREMISE-006 (flag-don't-fabricate) to the lit-search refresh case.
  Context: C2A2 lit-search pipeline 2026-04-27 autonomous-choices note. The principle directly parallels PREMISE-006 from the briefing layer: when a re-search returns nothing new, the correct action is to carry forward prior disposition with a "no new evidence" stamp, NOT to manufacture novel findings. First explicit articulation of this stance at the lit-search-refresh layer (vs. its prior articulation at the briefing layer).
  Type: methodological / normative
  Related decisions: PREMISE-006 (parallel application at briefing layer), candidate DECISION-022 (briefing-layer audit contract — could extend to net-evaluator-layer audit), DECISION-006
  Testability: testable empirically (track whether the carry-forward-without-fabrication policy holds across N weeks of refreshes; test whether any monitor-refresh entry contains hallucinated findings); framework commitment (normative)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-074
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from C2A2 lit-search pipeline 2026-04-27 autonomous-choices note — extension of PREMISE-006 stance to refresh-cycle case.
    Current status: UNTESTED

ASSUMPTION-075:
  Date identified: 2026-04-27
  Statement: Specialist-agent "significant work not yet captured" criterion can override the strict 30-day window when foundational work is missing from the wiki's coverage. Direct quote: "I used the 'significant work not yet captured' criterion rather than the strict 30-day window, since the field-theoretic formalization of bioelectric prepatterning is foundational to the wiki's coverage and was missing." First explicit specialist-level cadence override.
  Context: C2A2 Levin+Friston Monday specialist 2026-04-27 (local_a3685cb9) autonomous-choices note. Specialist used Manicka & Levin's *Cell Reports Physical Science* paper despite it falling outside the 30-day source-cadence rule because the field-theoretic formalization was foundational and missing. The other three items (Pai et al. bioRxiv preprint March 17 2026; two Friston items April 2026) all fell within the 30-day window, so the override was singular and visible.
  Type: methodological
  Related decisions: ASSUMPTION-005 (traditions as units), specialist-rotation schedule (PRESUMPTION-031), and the 30-day cadence convention itself (no formal DECISION; embedded in agent definitions)
  Testability: testable empirically (track how many specialist runs invoke the "significant work not yet captured" override; track the false-positive rate — was the foundational work actually missing, or was it captured but un-indexed?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-075
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Levin+Friston Monday specialist 2026-04-27 autonomous-choices note — direct quote articulating the cadence override.
    Current status: UNTESTED

ASSUMPTION-076:
  Date identified: 2026-04-27
  Statement: PRS triplets in the C2A2 wiki are Tom's (or "Tom + the network's") PRS-form re-description used to interlink thinkers, not each tradition's self-description. Citation form: "PRS-NN in the Stump-tradition wiki" or "Tom's PRS-form record of …" — never "Stump's PRS-NN". The Synergistic Coil and the PRS triplet structure are explicitly attributed to Tom, sitting at the convergence of Kuhn (solved problem as the unit of progress) + MacIntyre (traditions as P/R/S narratives) + Levin via James (intelligence as problem-solving under resource scarcity).
  Context: Design project architecture and timeline 2026-04-27 (local_4e0f61e4 continuation). Tom's correction to the synthesis attribution: the PRS triplet and Synergistic Coil are *his* framework, not Stump's. Citation forms updated everywhere: in the synthesis Day-001 file, in the bridges file, and in persistent memory. The metaphysical guardrail was also stated explicitly in the Reframe section. Synthesis word count: 1664 against transcript 1586, ratio 1.049 (within ±5% policy — see ASSUMPTION-077). This re-attribution has direct downstream consequences for how the same-day specialist agents read PRS-formatted content (see PRESUMPTION-089 for the recursive reading concern).
  Type: architectural / authorial
  Related decisions: ASSUMPTION-005 (traditions as units — re-attribution does not change the unit-of-analysis claim), candidate DECISION-025 (Stump metaphysical demotion — re-attribution shifts ground because Stump-as-supplier-of-live-metaphysics ASSUMPTION-067 reading rests on PRS-content read as Stump's voice), OPEN-037 (Stump tension)
  Testability: testable empirically (audit whether per-tradition `prs_triplets.md` files in the C2A2 wiki itself match the new authorial frame, or whether they read as Stump-voice / Friston-voice / etc.); testable via literature (does the C2A2-style re-description of multiple traditions through one author's frame produce coherent or distorted cross-tradition synthesis?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-076
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Design project architecture and timeline 2026-04-27 continuation — Tom's direct correction of authorial attribution and citation form.
    Current status: UNTESTED

ASSUMPTION-077:
  Date identified: 2026-04-27
  Statement: Synthesis-to-transcript word-ratio policy is ±5% (currently observed at 1664/1586 = 1.049, just inside the bound). Equal-length policy is one of four convention sweeps the nightly verification agent will check (alongside authorship direction, metaphysical guardrail, and filename safety).
  Context: Design project architecture and timeline 2026-04-27. The synthesizer is told to keep daily-synthesis output within ±5% of the source transcript's word count. The summa-2026-nightly-verification agent (newly scheduled, fires at 23:00 local) will enforce the bound by walking `vault/synthesis/` and cross-checking. First explicit codification of the equal-length policy.
  Type: methodological
  Related decisions: candidate DECISION-025 (downstream consumer constraints affect how the C2A2 wiki's PRS triplets are read into the synthesis), summa-2026-nightly-verification scheduled task (new today)
  Testability: testable empirically (track whether the nightly verifier actually flags violations; verify whether ±5% produces stylistically appropriate output across N=308 days of episodes)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-077
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Design project architecture and timeline 2026-04-27 — direct articulation of ±5% equal-length policy.
    Current status: UNTESTED

ASSUMPTION-078:
  Date identified: 2026-04-27
  Statement: Two parallel infrastructure failure modes block C2A2 sandbox-mode operations today: (1) the Chrome MCP browser is not signed into claude.ai, breaking both morning chat-to-cowork scrape and evening cowork-to-chat delivery; (2) the Cowork directory `~/Documents/Claude/Projects` is not connected, blocking the 1pm caching-architecture session from reading its proposal file. Both treated as user-fixable (sign in to claude.ai; connect the directory) rather than escalatable to product-team intervention.
  Context: Three same-day failure events: morning chat scrape (local_51b0bf0e), 1pm caching architecture (local_bd0ecd6c), evening cowork→chat (local_f6ebb0fc). All three are scheduled-task failures whose root cause is a user-mediated state outside the sandbox's authority to alter. The cowork→chat summary explicitly framed both as "Action item for tomorrow" rather than as an escalation. This re-affirms the same-class infrastructure-degradation framing seen in OPEN-035 (sandbox-mount-topology) and OPEN-039 (egress workaround) — the user-fixable framing is the C2A2's default disposition for sandbox-infrastructure failures.
  Type: methodological / normative
  Related decisions: OPEN-035, OPEN-039, candidate DECISION-023 (caching architecture — blocked today by infrastructure-failure #2), ASSUMPTION-055 (Phase 6 sandbox-unreachable)
  Testability: testable empirically (track frequency of user-fixable infrastructure failures over N weeks; track whether the user-fix occurs within an SLA, or whether the failures recur and accumulate)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-078
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from three same-day failure events (chat scrape, 1pm caching, evening sync) that produced consistent user-fixable framing for sandbox-infrastructure problems.
    Current status: UNTESTED

---

## Status Summary

Total assumptions identified: 78 (48 from Run 1 [2026-04-20] + 6 from supplementary Run 2 [2026-04-20] covering C2a2 caching architecture monday session + 8 from 2026-04-21 covering morning walk handoff, wiki daily run, Hawkins/Hoffman specialist, morning chat scrape, and evening cowork-to-chat sync + 8 from 2026-04-26 covering Summa-2026 design conversation, Wolfram specialist, Carroll+Arkani-Hamed specialist, Stump+Fredrickson specialist, morning walk handoff + 8 from 2026-04-27 covering morning walk handoff, chat scrape failure, lit-search pipeline drain, Levin+Friston specialist, design-project session continuation, and evening sync failure)

By testability:
  Testable via literature: 17 (prior 14 + ASSUMPTION-071, 073, 076 dual-testable via literature)
  Testable empirically: 64 (prior 56 + ASSUMPTION-071, 072, 073, 074, 075, 076, 077, 078 all empirically testable)
  Framework commitment: 8 (ASSUMPTION-001, 002, 016, 018, 030, 047, 048, 074 — until benchmarks specified; 074 is partial framework commitment as it is also empirically testable)

By status (2026-04-27):
  GROUNDED: 2 (ASSUMPTION-001, 002 — implemented in architecture)
  INCORPORATED-AS-PREMISE: 3 (ASSUMPTION-047 → PREMISE-006 on 2026-04-20; ASSUMPTION-068 → PREMISE-012 on 2026-04-27; ASSUMPTION-069 → PREMISE-013 on 2026-04-27)
  SUPPORTED: 1 (ASSUMPTION-005 — traditions as units, with noted caveats)
  PARTIALLY-SUPPORTED: 3 (ASSUMPTION-006, ASSUMPTION-010, ASSUMPTION-044)
  PARTIALLY-CHALLENGED: 7 (ASSUMPTION-003, 004, 007, 008, 011, 013)
  CONTESTED: 2 (ASSUMPTION-009, ASSUMPTION-012)
  REVISE-FLAGGED: 1 (ASSUMPTION-063 — Stump metaphysical demotion — flagged by today's 15c cycle for tension with ASSUMPTION-067 + literature challenge to Levin-Hoffman-Kastrup convergence-coherence)
  MONITOR (post-15c): 4 (ASSUMPTION-064, 065, 066, 067 — dispositioned today by lit-search pipeline)
  UNTESTED: 55 (prior 56 + ASSUMPTION-071, 072, 073, 074, 075, 076, 077, 078 from 2026-04-27 minus ASSUMPTION-063 → REVISE, 064/065/066/067 → MONITOR, 068 → INCORPORATED, 069 → INCORPORATED; note: ASSUMPTION-070 skipped lit-search per empirical-only flag, remains UNTESTED)

Literature search results (pipeline cycles completed through 2026-04-18):
  All 90 prior items: SEARCHED and DISPOSITIONED
  5 INCORPORATE, 47 MONITOR, 38 REVISE (cumulative across 8 cycles including 2026-04-18 afternoon top-up)

Key event (2026-04-20): Four new assumptions extracted on a low-architectural Monday dominated by autonomous operational runs. Today's assumptions cluster at the briefing layer — three of four are first-person methodological commitments stated in the morning-walk-handoff's autonomous-choices note (ASSUMPTION-046 findings 17→11 filter, ASSUMPTION-047 flag-over-reconcile stance on master-wiki staleness, ASSUMPTION-048 "clear" as "no actionable items" semantic framing). ASSUMPTION-045 is a wiki-daily-run coverage-adequacy claim that may be in tension with the parallel-scheduled Levin+Friston specialist task (still running at EOD). None of today's four items are strictly empirically novel; together they form a first-detectable briefing-layer epistemic-commitments cluster that is adjacent to the self-awareness-meta cluster (PRESUMPTION-015, 024, 041, 042, 046, 048) — the briefing agent is now articulating its own null-path semantics and staleness-handling stances, moving those from unstated presumption (last week) toward stated assumption (this week). Also notable: nothing was extracted from the still-running C2a2-agent-levin-friston session (local_8a50fcbd) — its proposal outputs will be captured by tomorrow's (2026-04-21) run if it completes overnight.

Gap note: The 2026-04-19 (Sunday) self-awareness daily run was not executed (no 2026-04-19_changes.md or 2026-04-19_snapshot.md exists). That day's C2A2-related sessions (periodic-monitor-weekly and deferred-action-monitor 2026-04-19 runs) were not processed by 14a/14b. Today's run picks up on 2026-04-20; the gap is flagged but not backfilled in this cycle because the scheduled task file specifies "today's" transcripts only.

Next step: Route ASSUMPTION-045–048 to 15a/15b queue. ASSUMPTION-045 is empirically resolvable by enumerating per-tradition latest-primary-source dates against the 60-day window. ASSUMPTION-046 is resolvable over 2-4 weeks by tracking briefing-derived actions. ASSUMPTION-047 and 048 are framework commitments — resolvable only against a briefing-layer style guide that does not yet exist (recommend writing one as cheap remediation).

Key event (2026-04-20 supplementary Run 2 — caching-architecture cluster): Six additional assumptions extracted covering the caching architecture decision surface. ASSUMPTION-049 (session lifetime = one full tradition agent run), ASSUMPTION-050 (static/dynamic prefix partition: 49 RC Wiki files static; vault daily activity dynamic-only; date-stamped filenames excluded from cached region), ASSUMPTION-051 (tool definitions load upfront and never mutate mid-session), ASSUMPTION-052 (70–80% aggregate cost reduction projected; ~50% Levin-specific), ASSUMPTION-053 (self-awareness pipeline migrates from 5 sessions to 1 appended-turn session), ASSUMPTION-054 (byte-stability smoke test as cache-determinism proxy). These six are the day's most substantive architectural signal and constitute the foundation of a candidate DECISION-023 (caching/execution protocol v1.0), first target deployment 2026-04-27 with Levin v1.0. All six are empirically testable with clear rollout gates. They cluster into a new CACHING-ARCHITECTURE family.

Key event (2026-04-21): Eight new assumptions extracted across five scheduled-task sessions on a light-C2A2 day dominated by external visit planning. ASSUMPTION-055 (Phase 6 git unreachable because sandbox mount topology excludes the repo path) is a new architectural failure mode that materially reframes DECISION-018 — the 2026-04-16 `.git/index.lock` is not the only blocker; the sandbox cannot reach the repo at all. ASSUMPTION-056 ("honest null > thin proposals") is the first explicit articulation of a specialist-agent null-is-valuable stance, surfaced from the Hawkins/Hoffman Tuesday slot. ASSUMPTION-057 (17→11 findings filter = "Active or Highest Priority, excluding subsumed/downgraded") converts yesterday's unaudited filter (PRESUMPTION-053) into a stated criterion — the filter rule is now visible though not yet independently audited. ASSUMPTION-058 (five-session window gives enough signal for an evening brief despite no 14a/14b cycle), ASSUMPTION-059 (evening-sync declining to manually fire missing cycles is scope-appropriate, not a coverage gap), and ASSUMPTION-060 (read-only-only checks on still-running specialists echo the Monday Levin-Friston natural-termination precedent) together sharpen the evening-sync's self-understanding of its own authority and epistemic reach — three first-person operational commitments all stated in the sync's autonomous-choices note. ASSUMPTION-061 (Chat-side Claude's "leaving validated premises outside the formal decision register is itself silent reconciliation") elevates PREMISE-006 from a briefing-layer rule to a reflexive constraint on the decisions-register pipeline — makes candidate DECISION-022 a test of PREMISE-006 rather than just a rendering choice. ASSUMPTION-062 (weak-circuit-breaker > none; tune-later over block-on-optimal) is the methodological principle behind shipping a minimal candidate DECISION-024 now. Pattern note: six of today's eight assumptions (056–059, 061, 062) are methodological or normative, continuing 2026-04-20's briefing-layer-epistemic-commitments accumulation — the sync/briefing/specialist layers are now articulating their own operating principles at an accelerating rate. This extends the BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster from 4 members (2026-04-20) to 8 members (adding ASSUMPTION-057, 058, 059, 060).

Gap note (2026-04-22 through 2026-04-25): Four self-awareness daily runs (Wed Apr 22 through Sat Apr 25) were not executed. No `2026-04-22_changes.md`, `2026-04-23_changes.md`, `2026-04-24_changes.md`, or `2026-04-25_changes.md` exists. Today's run (2026-04-26) does NOT backfill these per scheduled-task scope; the gap is flagged for OPEN-038 and is the first observed instance of a 4+ day self-awareness gap.

Key event (2026-04-26): Eight new assumptions extracted on a Sunday dominated by a long architectural-design conversation (the "Summa 2026 in a Year" derivative project) plus three specialist-agent slots (Wolfram, Carroll+Arkani-Hamed, Stump+Fredrickson) and the wiki daily run + morning walk handoff. Today's most consequential items are ASSUMPTION-063 (Stump demoted on metaphysics; Levin+Hoffman+Kastrup as new metaphysical primaries) and ASSUMPTION-064 (Wright + Rohr proposed as new C2A2 traditions) — both stated explicitly by Tom in a derivative-project session that has not yet propagated to the C2A2 wiki itself. These two together form a candidate DECISION-025 (Wright/Rohr addition + Stump metaphysical demotion). ASSUMPTION-065 (Carroll↔Arkani-Hamed convergence on emergent spacetime as 2026's top paradigm-shift signal) is the year's strongest specialist-agent paradigm claim. ASSUMPTION-066 (Wolfram = method-export to philosophy) recasts three CROSS entries (016, 024, 026). ASSUMPTION-067 (Stump+Fredrickson metaphysics+empirics bridge) stands in DIRECT TENSION with ASSUMPTION-063 — same day, opposite stances on Stump's metaphysical authority — surfaced as OPEN-037. ASSUMPTION-068 (master-narrative-gap surfacing > fabrication) re-affirms PREMISE-006 against today's largest-yet 4-day gap. ASSUMPTION-069 (proposal-id collisions = flag-and-roll-forward) is articulated independently by two same-day instances. ASSUMPTION-070 (308-episode playlist count, not 365) is an empirical correction with downstream pace-math implications. Pattern note: today's 8 assumptions are dominated by architectural and empirical types (5 of 8) rather than methodological — a reversal from 2026-04-21's methodological-heavy day, reflecting that today's signal came from an actual design conversation rather than from operational-layer principle-articulation.

ASSUMPTION-079:
  Date identified: 2026-05-05
  Statement: All six weekday-assigned C2A2 specialist agents (Mon Levin+Friston, Tue Hawkins+Hoffman, Wed McGilchrist+Kastrup, Thu Stump+Fredrickson, Fri Carroll+Arkani-Hamed, Sat Wolfram) executed on the same calendar day in a daemon catch-up sequence (15:35–16:35 UTC). The run-day-as-coverage-unit is treated as functionally equivalent to the intended spread-across-week distribution; outputs are stamped by their assigned weekday rather than the run weekday and ingested into pending/ alongside one another.
  Context: Summa-updating-agents session (local_40871db5) diagnosed the daemon's overdue-queue drain after Tom's Claude restart fixed the daemon outage. C282 wiki agent daily run (local_9d77101c) and the six specialist sessions (local_6db3a16c, local_042ce520, local_bda267b1, local_e89e541a, local_9beef790, local_54d415c9) all completed today, producing 18 specialist proposals (3+2+3+4+3+2 sequenced).
  Type: methodological / operational
  Related decisions: ASSUMPTION-011 (specialist-first scheduling), DECISION-015 (scheduled-task ecology)
  Testability: testable empirically (compare PRS-extraction yield from same-day-catchup batches vs. spread-across-week batches; check for temporal-correlation artefacts in cross-tradition signals)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-079
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Summa-updating-agents session diagnosis ("the daemon is dutifully working through its overdue queue") and from the six specialist sessions running consecutively in the daemon catch-up window.
    Current status: UNTESTED

ASSUMPTION-080:
  Date identified: 2026-05-05
  Statement: The scheduled-task daemon's silent-skip failure mode is partitioned by link count — tasks with link count > 1 fire normally; tasks with link count = 1 are silently skipped at registration time. This is an Anthropic-side bug, not a C2A2 design issue or a per-task configuration error.
  Context: Summa-updating-agents session (local_40871db5). After Tom's Claude restart and the daemon's overdue-queue drain, observation: tasks like `summa-2026-nightly-verification`, `summa-qc-sweep`, `c2a2-agent-wright-rohr`, `c2a2-sewing-agent-weekly`, and 21 of the `1pm-*` and `korbyt-*` reminders still did not fire despite the daemon being awake. "The daemon is firing every task that has link count > 1. It's silently skipping every task that has link count = 1." Quote: "the registration bug really is at task-creation time, not at fire time. That's a real Anthropic bug."
  Type: empirical / infrastructure
  Related decisions: candidate DECISION-026 (specialist pre-flight directory-grant timeout — adjacent failure mode), OPEN-039 (sandbox-infrastructure-escalation cluster)
  Testability: testable empirically (audit task-creation paths and confirm the link-count = 1 vs. > 1 partition holds across MCP / UI / SDK / hook creation paths; correlate with `lastRunAt` to confirm silent-skip)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-080
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Summa-updating-agents session — explicit Tom-facing diagnosis of the daemon partition.
    Current status: UNTESTED

ASSUMPTION-081:
  Date identified: 2026-05-05
  Statement: Setting `fireAt` via the MCP `update_scheduled_task` tool is a working workaround for the link-count = 1 silent-skip bug (ASSUMPTION-080). The `summa-2026-daily-batch` task with MCP-set `fireAt` at 17:00 UTC was the live test for this hypothesis at the 1 PM ET window.
  Context: Summa-updating-agents session (local_40871db5) — "If [the 1 PM test] fires, the `update_scheduled_task --fireAt` path is a working workaround for all 23 broken tasks. If it doesn't fire, only Anthropic can fix it."
  Type: empirical / infrastructure
  Related decisions: ASSUMPTION-080 (parent diagnosis)
  Testability: testable empirically (observe `lastRunAt` after the MCP `fireAt` update; correlate with daemon link-count partition)
  Status: UNTESTED (live test in progress at this run's start)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-081
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Summa-updating-agents session — explicit workaround claim.
    Current status: UNTESTED

ASSUMPTION-082:
  Date identified: 2026-05-05
  Statement: The RC Explorer is a 3-layer architecture (L1 Archaeological → RC Document Explorer / L2 Operational → C2A2 Wiki / L3 Encyclopedic → RC Wiki) with five explicit integration steps: (1) SD→JSON, (2) proposals→472+, (3) wiki-sourced panels, (4) schema merge, (5) Wiki sidebar panel. Within the L1 vision, "Community Explorer" is Tool #1 and "AI Heartbeat" is Tool #2 (urgent rebuild).
  Context: Morning walk handoff 2026-05-05 (local_662eb846). Walk notes were Tom's "RC Explorer — Vision for What This Becomes" self-thread (Gmail, 02:56 UTC today). Six decisions extracted; five tasks added to queue.md (vision cleanup, Explorer reordering, AI Heartbeat rebuild, Aquinas decision, generalization path). The 3-layer model is included as the briefing's "Architecture Layer Reference" section per the morning-walk-cowork-handoff skill spec.
  Type: architectural
  Related decisions: ASSUMPTION-005 (traditions as units — orthogonal axis), DECISION-003 (Thousand Brains redesign — sits inside L2)
  Testability: testable empirically (audit whether subsequent integration work fits the 5-step decomposition; check for findings/proposals that resist a single-layer assignment)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-082
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Morning walk briefing 2026-05-05 — Tom's stated 3-layer vision and 5-step integration roadmap.
    Current status: UNTESTED

ASSUMPTION-083:
  Date identified: 2026-05-05
  Statement: Wiki visualization filter semantics are: within a section (Traditions / Disciplines / Years), checked items combine via OR; across sections, the visible set is the AND of section-level passes; edges only render when both endpoint nodes are visible (and the master Edges checkbox is on). The Reset button restores the all-checked state.
  Context: "Review of May 4 version full history recording" session (local_64a1eef5). A help popover (?) was added to the explorer.html left filter panel; popover wording was reconciled against the implementation in `prsNodeVisible` and `applyPRSFilters`.
  Type: architectural / UX-spec
  Related decisions: DECISION-018 (modular architecture — explorer is a downstream artifact)
  Testability: testable empirically (automated test that the documented semantics match runtime behavior — currently no such test exists, see PRESUMPTION-101)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-083
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from explorer.html review session — the help popover wording is the explicit spec articulation.
    Current status: UNTESTED

ASSUMPTION-084:
  Date identified: 2026-05-05
  Statement: An empty-handed orchestrator Phase 2 (0 new high-quality proposals across the 5 thinkers without same-day specialist coverage — Hoffman, Hawkins, Kastrup, Fredrickson, Arkani-Hamed) is a valid result, not a failure mode. Search exhaustion within the 60-day window is acceptable when same-day specialist throughput already produced 18 proposals.
  Context: C282 wiki agent daily run 2026-05-05 (local_9d77101c) — "Phase 2: 0 new high-quality proposals found across the 5 thinkers without 2026-04-27/2026-05-04 pending coverage. Searches returned only previously-captured material or items outside the 60-day window." Phase 3 still produced a review page with 10 proposals; Phase 4 drafted the Gmail digest.
  Type: methodological
  Related decisions: ASSUMPTION-056 ("honest null > thin proposals"), ASSUMPTION-011 (specialist-first scheduling)
  Testability: testable empirically (audit whether specialist+orchestrator coverage on a same-day catch-up generates the same total yield as a spread-across-week run; check whether the orchestrator's empty result is over-attributed to "specialists already covered" vs. genuine search exhaustion)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-084
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from C282 wiki agent daily run Phase 2 transcript.
    Current status: UNTESTED

ASSUMPTION-085:
  Date identified: 2026-05-05
  Statement: The "FROM [thinker] himself, not commentary about him" quality filter is the operative criterion at every specialist slot. Hawkins agent today reported "0 proposals" because the recent material was either already captured or commentary-about rather than from-Hawkins; the honest-null-result was preferred to a thin-proposal padding.
  Context: C2A2 Tuesday agents 2026-05-05 (local_042ce520). Hawkins Agent: 0 proposals written. The specialist explicitly invoked the "FROM Hawkins himself" filter and accepted the null result. Re-affirms ASSUMPTION-056 from 2026-04-21 at the Hawkins+Hoffman slot. Carroll+Arkani-Hamed (local_9beef790) similarly excluded the GPT-5.2 / arXiv:2602.12176 paper because Arkani-Hamed is not an author.
  Type: methodological
  Related decisions: ASSUMPTION-056 (parent — 2026-04-21 first articulation), ASSUMPTION-011 (specialist-first scheduling)
  Testability: testable empirically (audit specialist-slot 0-proposal events for false-negatives — were genuine from-thinker items missed under the "FROM" filter?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-085
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Tuesday agents 2026-05-05 transcript and Friday agents 2026-05-05 (local_9beef790) explicit-exclusion note.
    Current status: UNTESTED

ASSUMPTION-086:
  Date identified: 2026-05-05
  Statement: Specialist-self-claims of "strongest current empirical bridge concept" (Stump+Fredrickson on positivity resonance) and "parallels C2A2's own multi-agent architecture" (Hoffman on TRACE Institute launch) and "candidate shared substrate" (Wolfram on PROP-016 Rulial Ensemble in Biology directly advancing CROSS-006/007/015/049) are all treated as primary cross-tradition signal — independent specialist-tagging is the surfacing mechanism, with no parallel adjudication step.
  Context: Three specialist sessions today made strong cross-tradition claims tagged in their own session output. Stump+Fredrickson (local_e89e541a): "Fredrickson's 'Does Positivity Resonance Signify Love?' provides the strongest current empirical bridge concept for the C2A2 framework." Hoffman (local_042ce520): "TRACE Institute launch flags an institutional-maturity paradigm-shift signal, parallels C2A2's own multi-agent architecture." Wolfram (local_54d415c9): "PROP-016 directly advances CROSS-006, CROSS-007, CROSS-015, and CROSS-049 (giving Wolfram, Friston, Levin, and Hawkins a candidate shared substrate)."
  Type: methodological
  Related decisions: ASSUMPTION-009 (displacement vectors), candidate DECISION-022 (briefing-layer audit contract — adjacent question of selection-criterion logging)
  Testability: testable empirically (independent re-evaluation of each "strongest bridge" claim by a non-specialist agent; cross-check whether multiple same-day "strongest" claims compete or compose)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-086
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from three same-day specialist sessions — direct quotes of cross-tradition self-tagging.
    Current status: UNTESTED

ASSUMPTION-087:
  Date identified: 2026-05-05
  Statement: TRACE Institute launch (Hoffman, donalddhoffman.com) is a research-program-level alliance signal — a paradigm-shift indicator at the institutional-maturity layer rather than the paper layer. The Levin–Hoffman alliance, in particular, is read at "research-program level" via Thoughtforms-Life April 2026 hosting. Institutional events thus enter the proposal pipeline alongside paper publications.
  Context: C2A2 Tuesday agents 2026-05-05 (local_042ce520). Proposal PROP-2026-05-05-005 records the TRACE Institute launch as a discrete proposal item. The "research-program-level alliance" framing is novel for the proposal pipeline — prior alliance signals were paper-coauthorship at the document level.
  Type: architectural / methodological
  Related decisions: ASSUMPTION-005 (traditions as units), candidate DECISION-025 (Wright/Rohr addition pattern — institutional vs. authorial expansion)
  Testability: testable via literature (does institutional-maturity correlate with paradigm shift in research-program studies — Lakatos/Laudan?); testable empirically (audit whether institutional events generate downstream PRS triplets at the same rate as paper events)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-087
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from PROP-2026-05-05-005 framing in the Hawkins+Hoffman session.
    Current status: UNTESTED

ASSUMPTION-088:
  Date identified: 2026-05-08
  Statement: An org-monthly-usage-limit interrupt occurring on a personal-account Cowork session is treated as a real, work-blocking quota event (not a misclassification by the system to be ignored). When the explorer-fix Cowork session was interrupted twice with "You've hit your org's monthly usage limit," Tom clarified "this is not an org account...I have one, but this isn't it" and the working assumption became that synthesis must be deferred to a later session rather than retried immediately.
  Context: C2A2 explorer bug-fix Cowork session 2026-05-08 (local_56cc4dfb). Codex 5.5 external review pasted in; assistant hit org-limit twice within the same session containing only one user message + the review; synthesis (composite action plan) was queued, not produced. Cowork-summary explicitly records "the session hit an org-monthly-usage-limit interrupt twice."
  Type: methodological / infrastructure
  Related decisions: ASSUMPTION-071 (browser-auth as agent-prohibited), candidate DECISION-026 (sandbox-infrastructure escalation track — undrafted)
  Testability: testable empirically (audit subsequent personal-account Cowork sessions for org-limit interrupts; correlate with actual usage; check whether the messaging is misclassification or a true quota event)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-088
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from local_56cc4dfb session; Tom's clarifying turn ("this is not an org account...I have one, but this isn't it") + the assistant's two org-limit interrupts.
    Current status: UNTESTED

ASSUMPTION-089:
  Date identified: 2026-05-08
  Statement: Two-source composite synthesis (internal report + external-LLM review) is the appropriate next step for the explorer bug-and-design pipeline — neither source is dropped or used in isolation; both are read together and a composite action plan is built across them.
  Context: C2A2 explorer bug-fix Cowork session 2026-05-08 (local_56cc4dfb). Tom's user message: "Here's input from another agent (codex 5.5): Read, compare to the report you wrote, synthesize, and generate a detailed action plan based on that composite." This is the first explicit articulation of a two-source-composite protocol for the explorer track and parallels the briefing-layer's multi-source ingestion pattern.
  Type: methodological / epistemic
  Related decisions: ASSUMPTION-086 (specialist-self-claims as primary cross-tradition signal — analogous epistemic move at a different layer); candidate DECISION-022 (briefing-layer audit contract)
  Testability: testable empirically (compare outputs of compositional vs. picked-one synthesis on a held-out review pair); testable via literature (multi-source review-aggregation frameworks in software-engineering and meta-analysis)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-089
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Tom's verbatim instruction in the local_56cc4dfb session (single-message turn, before org-limit hit).
    Current status: UNTESTED

ASSUMPTION-090:
  Date identified: 2026-05-08
  Statement: Within the explorer bug-fix track, the highest-priority entry point is the smallest-fix-first item — specifically the two-line `extractOverview()` var-declaration fix in `wiki_narration.html` (line ~1502/1503) — because it is high-confidence, low-effort, and stops Chrome from logging an uncaught exception every page-load. Smoke-test scaffolding is the second priority; a responsive fallback shell is the third.
  Context: Cowork-to-chat summary 2026-05-08 (local_feb53918), "For Morning Discussion" item 1: "Recommendation: do (b) first — the bug-fix is high-confidence and low-effort, and shipping it stops Chrome from logging an uncaught exception every page-load. Then add the smoke-test script before tackling the responsive shell." This articulates an explicit prioritization heuristic that mirrors Codex 5.5's "Best next move" trio (fix bug → add smoke-test → responsive fallback) without separately validating that Codex's priorities reflect Tom's project context (PRESUMPTION-115 surfaces this).
  Type: architectural / methodological
  Related decisions: candidate DECISION-026 (sandbox-infrastructure escalation track), ASSUMPTION-082 (3-layer RC Explorer architecture — `wiki_narration.html` is the L1 instrument)
  Testability: testable empirically (does the two-line fix eliminate the uncaught exception in Chrome DevTools console? does the smoke-test catch a regression on the next code change? does mobile usage at 390×844 succeed under a responsive shell?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-090
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the cowork-to-chat summary's "Recommendation: do (b) first" formulation, traced to Codex 5.5's prioritization trio.
    Current status: UNTESTED

ASSUMPTION-091:
  Date identified: 2026-05-08
  Statement: The proposal pipeline accepts off-cadence specialist proposal filings — that is, a Stump or Fredrickson proposal can land in `inbox/proposals/pending/` on a Friday (assigned-Thursday slot for both) without weekday-coordination friction. Off-cadence and on-cadence filings are treated identically by downstream review-page rendering and approval-rate tracking.
  Context: Five new pending proposals filed today dated 2026-05-08 (Friday): Stump × meaning-of-suffering Pine dialogue (Stump = assigned-Thursday slot), Fredrickson × *Positively in Sync* (Thursday slot), Fredrickson × *Positive Emotions Cornerstones* Oxford 2025 (Thursday slot), Arkani-Hamed × single-minus gluon/graviton GPT-5.2 (Friday slot), Carroll × Mindscape 351 Singer-utilitarianism (Friday slot). Three of five are off-weekday-cadence. Cowork summary treats them uniformly: "These will land on the next review page." Extends ASSUMPTION-079 (same-day catch-up framing) at the per-proposal level.
  Type: methodological / operational
  Related decisions: ASSUMPTION-079 (same-day catch-up framing), ASSUMPTION-011 (specialist-first scheduling)
  Testability: testable empirically (audit downstream review-page render and approval rates for off-cadence vs. on-cadence proposals over N weeks; check pattern-detector findings for systematic bias)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-091
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from `wiki/inbox/proposals/pending/` directory listing for 2026-05-08 (5 files; 3 off-cadence) + cowork-summary uniform-treatment phrasing.
    Current status: UNTESTED

ASSUMPTION-092:
  Date identified: 2026-05-08
  Statement: A 3-day master-narrative absence (2026-05-06 → 2026-05-08) for the wiki-orchestrator daily run is most plausibly attributable to the Anthropic-side daemon link-count = 1 silent-skip bug (ASSUMPTION-080/081) — i.e., the bug diagnosed on 2026-05-05 has not been fixed Anthropic-side, and the wiki-orchestrator daily task is itself link-count = 1 affected. This is treated as the working hypothesis pending a manual link-count check.
  Context: Cowork-to-chat summary 2026-05-08, Pipeline Status section: "Master-narrative gap: today's wiki run did NOT produce a 2026-05-08 master-narrative entry; gap = 3 days (2026-05-06 → 2026-05-08), echoing the OPEN-038 cluster — worth checking whether the daemon link-count = 1 bug (ASSUMPTION-081) is implicated." Also "For Morning Discussion" item 4: "Worth checking whether the wiki-orchestrator daily task itself is link-count = 1 affected — if it is, the bug Tom planned to file Anthropic-side ... is now actively re-blocking the wiki, not just the Summa side."
  Type: empirical / infrastructure
  Related decisions: ASSUMPTION-080, ASSUMPTION-081, OPEN-038 (master-narrative-gap escalation question), candidate DECISION-026 (sandbox-infrastructure escalation track)
  Testability: testable empirically (`stat -c %h /path/to/wiki-orchestrator-daily-task.scheduled-task` to count links; if =1, retry via `update_scheduled_task --fireAt`; observe whether master-narrative resumes)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-092
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the cowork-to-chat summary's master-narrative-gap framing tied directly to ASSUMPTION-081 as the working hypothesis.
    Current status: UNTESTED

ASSUMPTION-093:
  Date identified: 2026-05-08
  Statement: Saturday-morning rerun is the standard closure path for queued-but-stalled weekday scheduled tasks. The 1pm Friday register-cleanup task (local_1d6dddab), the Sunday-Wright/Rohr task (local_a89665bd, hit org-limit), and the sewing-agent-weekly task (local_6e3f64f1, hit org-limit) all stalled today; cowork-summary "What's Next" frames the resolution as "Saturday specialist agent slot ... could be picked up as a non-scheduled session" or "drop it into a Saturday session this weekend."
  Context: Cowork-to-chat summary 2026-05-08, "What's Next: Tomorrow (Sat 2026-05-09)" section + "For Morning Discussion" item 2 ("when does it close? ... (b) drop it into a Saturday session this weekend"). The convention has been operative across multiple prior weeks but is articulated explicitly here for the first time as an end-of-week catch-up policy.
  Type: methodological / operational
  Related decisions: ASSUMPTION-079 (catch-up framing), ASSUMPTION-011 (specialist-first scheduling)
  Testability: testable empirically (audit weekend-rerun success rates for stalled weekday tasks over N weeks; compare time-to-closure for Saturday-rerun vs. Monday-rerun vs. drop)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-093
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the cowork-to-chat summary's "What's Next" weekend-disposition framing for three stalled scheduled tasks today.
    Current status: UNTESTED

ASSUMPTION-094:
  Date identified: 2026-05-08
  Statement: Sandbox-infrastructure constraints aggregated across two active projects (C2A2 + Summa-2026) accumulate to a single-escalation threshold around N≥5 distinct constraints, justifying a combined escalation note to Anthropic rather than parallel per-channel reports. The current count: egress allowlist + mount topology + .git/index.lock (~22 days) + daemon link-count = 1 silent-skip + Summa YouTube IP-block = 5.
  Context: Cowork-to-chat summary 2026-05-08, "For Morning Discussion" item 3: "The Summa YouTube IP-block today plus the existing C2A2 OPEN-039 cluster (egress allowlist; mount topology; .git/index.lock at ~22 days; daemon link-count = 1 silent-skip) is now ≥5 distinct sandbox infrastructure constraints across two active projects. PRESUMPTION-075 (workaround-as-permanent) is increasingly costly. Question: file a single combined escalation note to Anthropic this week, or hold for one more cycle's worth of repro data?" Also "What's Next" item 3.
  Type: methodological / normative
  Related decisions: OPEN-039 (sandbox-infrastructure-escalation cluster), candidate DECISION-026 (sandbox-infrastructure escalation track), ASSUMPTION-078 (two parallel sandbox-infrastructure failure modes both user-fixable)
  Testability: testable empirically (compare resolution-rate for combined vs. parallel escalation reports historically); testable via literature (incident-aggregation policy in vendor escalation procedures)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-094
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary's "≥5 distinct sandbox infrastructure constraints" formulation and the explicit single-vs-parallel escalation question.
    Current status: UNTESTED

ASSUMPTION-095:
  Date identified: 2026-05-08
  Statement: YouTube IP-blocking the agent sandbox via `youtube-transcript-api` (IpBlocked / RequestBlocked errors across all six days reviewed) is a SYSTEMIC ESCALATION (not a transient failure), blocking Step-4 transcript-fidelity checks for all 65 Summa pairs in the Summa vault. The classification is "systemic" rather than "transient" because the same IP-block reproduces across multiple days and multiple transcript IDs.
  Context: Cowork-to-chat summary 2026-05-08, "What Was Accomplished Today" final paragraph: "an earlier sweep on Days 6–11 surfaced a systemic ESCALATION: YouTube is IP-blocking the agent sandbox via `youtube-transcript-api` (IpBlocked / RequestBlocked across all six days), so Step-4 transcript-fidelity checks cannot run for any of the 65 pairs in the Summa vault. This mirrors the C2A2 OPEN-039 sandbox-infrastructure-escalation cluster."
  Type: empirical / infrastructure / cross-project
  Related decisions: OPEN-039 (sandbox-infrastructure-escalation cluster — Summa YouTube IP-block joins as 5th channel), ASSUMPTION-094 (combined-escalation threshold)
  Testability: testable empirically (re-attempt `youtube-transcript-api` calls from agent sandbox vs. local laptop; correlate with Anthropic IP allocation; reproduce on N additional transcript IDs)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-095
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Summa-2026 QC-sweep classification report of 2026-05-08 (six-pair priority-2 sweep + Days 6–11 sweep — both surfaced via cowork-summary cross-project section).
    Current status: UNTESTED

ASSUMPTION-096:
  Date identified: 2026-05-09
  Statement: Four SYSTEMIC-RISK flags surfaced in a single 15a/15b/15c lit-search cycle constitute the "densest single cycle on record" — a pattern-strength signal warranting cluster-level remediation rather than per-item triage. Three of the four flags are recurrence flags (SELF-AWARENESS-META 4th recurrence; specialist/external primary-signal recurrence at new layer; three-recurrence discipline cluster); only the review-aggregation 3-item structural gap is a first observation.
  Context: Cowork-to-chat summary 2026-05-09, second paragraph: "the largest cluster of SYSTEMIC-RISK flags in any one lit-search cycle to date — four flags, three of them recurrence flags." Reinforced under "Pipeline Status" and explicitly connected to today's lit-search-pipeline cycle output.
  Type: methodological / metrics
  Related decisions: ASSUMPTION-073 (REVISE heuristic), ASSUMPTION-072 (single-cycle drain), candidate DECISION-027 (specialist-recognition adjudication tier — scope extension flagged today), candidate DECISION-026 (sandbox-infrastructure escalation)
  Testability: testable empirically (compare cluster-level vs. per-item remediation outcomes on next 4-flag-cycle, or audit historical cycle-density vs. follow-through rate); testable via literature (alert-fatigue / cluster-alerting frameworks in SRE practice)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-096
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-09 framing of today's lit-search cycle as "densest on record" + the four-flag taxonomy.
    Current status: UNTESTED

ASSUMPTION-097:
  Date identified: 2026-05-09
  Statement: Three independent third-recurrences in a single batch — registration (PRESUMPTION-105), canonization (PRESUMPTION-106), fallback (PRESUMPTION-111) — are coherent enough to bundle into a single "Core Operational Discipline" architectural sprint. The bundling assumption is that cross-cluster remediation efficiencies outweigh smaller-bite triage benefits.
  Context: Cowork-to-chat summary 2026-05-09, item 7 of "What's Next": "Bundle Three-recurrence discipline cluster (registration / canonization / fallback) into 'Core Operational Discipline' architectural sprint — explicit recommendation from today's lit-search." Repeated in "For Morning Discussion" item 3.
  Type: architectural / methodological
  Related decisions: PRESUMPTION-105, PRESUMPTION-106, PRESUMPTION-111, candidate DECISION-022 (briefing-layer audit contract — adjacent), candidate DECISION-026
  Testability: testable empirically (track sprint-level vs. item-level remediation completion rate on a held-out cluster); testable via literature (architectural-debt cluster-remediation patterns)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-097
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-09 explicit lit-search recommendation + "What's Next" item 7 + "For Morning Discussion" item 3.
    Current status: UNTESTED

ASSUMPTION-098:
  Date identified: 2026-05-09
  Statement: A REVISE-flag for the third consecutive 15c cycle (≤25h stall watchdog: 2026-04-21 anchor, 2026-04-26 reflag, 2026-05-09 third reflag) constitutes "arguably stronger than the typical canonization threshold" — i.e., third-recurrence at fixed-cycle cadence is sufficient evidence to canonize a candidate-decision as a numbered DECISION-NNN this week.
  Context: Cowork-to-chat summary 2026-05-09, "For Morning Discussion" item 1: "the ≤25h stall watchdog is now arguably stronger than the typical canonization threshold." Frames the question to Tom as binary: canonize as DECISION-NNN this week, or remain a candidate-decision pending more data.
  Type: methodological / governance
  Related decisions: PRESUMPTION-035 (threshold-free flag invocation), PRESUMPTION-052 (recurrence-without-escalation), PRESUMPTION-069 (silence-not-tracked anchor), PRESUMPTION-108 (today's third-recurrence on this exact line), candidate DECISION-022 (briefing-layer audit contract)
  Testability: testable empirically (track canonization-rate at N=3 recurrence vs. N=4 / N=5 across other clusters; audit time-to-recurrence-suppression once canonized vs. not); testable via literature (governance-trigger-threshold designs in SRE / quality-management)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-098
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-09 "For Morning Discussion" item 1 framing the third-recurrence-as-canonization signal as a stated commitment.
    Current status: UNTESTED

ASSUMPTION-099:
  Date identified: 2026-05-09
  Statement: DECISION-027 candidate scope can be extended to cover the external-tool-review layer (Codex / external-LLM prioritization adoption) — i.e., specialist self-attribution (original DECISION-027 candidate) and external-LLM prioritization adoption (today's PRESUMPTION-115 SYSTEMIC-RISK extension) are "arguably the same epistemic-weight protocol applied to two different source types." Bundling them keeps the protocol unified; splitting them tracks the empirical surface separately.
  Context: Cowork-to-chat summary 2026-05-09, "Pipeline Status" line for Decisions: "DECISION-027 candidate scope today was implicitly extended to external-tool-review layer (per PRESUMPTION-115 SYSTEMIC-RISK)." Made fully explicit in "For Morning Discussion" item 2 as the binary unify-or-split question.
  Type: architectural / governance
  Related decisions: PRESUMPTION-074 (specialist-recognition reliability — original SYSTEMIC-RISK), PRESUMPTION-115 (external-tool-review layer extension), ASSUMPTION-086 (specialist-self-claims as primary cross-tradition signal), candidate DECISION-027
  Testability: testable via literature (review-aggregation framework taxonomies that distinguish source-types); testable empirically (audit DECISION-027 application to a held-out specialist event vs. external-tool-review event under both unified and split protocols)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-099
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-09 implicit-extension statement under "Key Decisions Made" + the explicit unify-or-split question in "For Morning Discussion" item 2.
    Current status: UNTESTED

ASSUMPTION-100:
  Date identified: 2026-05-09
  Statement: Saturday Wolfram's two specialist proposals reinforcing the Levin × Hoffman × Wolfram three-way ontological convergence (CROSS-007 / CROSS-025 / CROSS-031 / CROSS-049 / CROSS-051) constitute "the highest-leverage cross-tradition signal of the week" — a strength-claim that warrants prioritized Pattern-Detector deep-pass scheduling (potentially out-of-band before the standard review cycle).
  Context: Cowork-to-chat summary 2026-05-09, "For Morning Discussion" item 5: "Saturday Wolfram delivered three-way ontological convergence reinforcement ... This is the highest-leverage cross-tradition signal of the week." Question to Tom posed as binary: schedule a Pattern Detector deep-pass before the standard review cycle, or let them flow through normally.
  Type: empirical / cross-tradition
  Related decisions: ASSUMPTION-086 (specialist-self-claims as primary cross-tradition signal), PRESUMPTION-074 (specialist-recognition reliability), CROSS-007, CROSS-025, CROSS-031, CROSS-049, CROSS-051
  Testability: testable empirically (audit Pattern-Detector findings before vs. after deep-pass on these two proposals; compare to baseline standard-cycle finding-rate); testable via literature (cross-domain concept-convergence detection metrics)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-100
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-09 "For Morning Discussion" item 5 highest-leverage-of-week claim + the explicit out-of-band scheduling question.
    Current status: UNTESTED

ASSUMPTION-101:
  Date identified: 2026-05-09
  Statement: The Chrome MCP "Tabs can only be moved to and from normal windows" error (which has now blocked both the morning chat-scrape and the evening cowork-to-chat sync today, in addition to a 2026-05-08 occurrence) is an environment-state issue (popup-only / app-window-only / DevTools-detached Chrome sessions) rather than a Chrome-MCP defect. The root-cause attribution rests on a Codex-style external-LLM diagnostic.
  Context: Cowork-to-chat summary 2026-05-09, "For Morning Discussion" item 6: "the Codex-style external-LLM diagnostic suggests it's an environment-state issue (popup-only Chrome sessions) rather than a Chrome-MCP defect." Question to Tom posed as binary: add a `pre-scrape-ensure-normal-window` step, or document the pre-condition.
  Type: empirical / infrastructure
  Related decisions: ASSUMPTION-071 (browser-auth as agent-prohibited), PRESUMPTION-038 (browser-state self-clearing), PRESUMPTION-111 (cowork-to-chat sync no-fallback), candidate DECISION-026 (sandbox-infrastructure escalation)
  Testability: testable empirically (correlate scrape-success-rate with Chrome window-type-mix at scrape time across N≥10 future runs; produce an `ensure-normal-window` script and observe the success-rate delta); testable via literature (Chrome extension / MCP-protocol tab-group requirements documentation)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-101
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-09 "For Morning Discussion" item 6 environment-state attribution + the cross-references to today's chat-scrape failure note (`architecture/daily_sync/chat_to_cowork/2026-05-09_chat_summary.md`).
    Current status: UNTESTED

ASSUMPTION-102:
  Date identified: 2026-05-09
  Statement: A 20-item EOD lit-search batch (8 ASSUMPTIONs + 12 PRESUMPTIONs) draining 100% in a single morning 15a/15b/15c cycle constitutes the operational baseline for lit-search throughput at the present queue scale — a positive instance of ASSUMPTION-072's "single-cycle backlog drain" claim, now generalized from the 5-day backlog case to the prior-day's-EOD-batch case.
  Context: Cowork-to-chat summary 2026-05-09, second paragraph: "The C2A2 lit-search pipeline then ran end-to-end on the 20-item batch and dispositioned it cleanly: 11 MONITOR (MONITOR-088 through MONITOR-098) + 9 REVISE + 0 INCORPORATE." Reinforced under "Pipeline Status": "Today's batch (20 items) drained 100% in one cycle."
  Type: methodological / operational
  Related decisions: ASSUMPTION-072 (5-day backlog drain), ASSUMPTION-073 (REVISE heuristic), DECISION-012 (15c agent), DECISION-013 (15d agent)
  Testability: testable empirically (track single-cycle drain rate across N≥4 future EOD batches; record cycle wall-time; compare to historical 2026-04-27 5-day drain); testable via literature (queueing-theory throughput baselines for human-augmented review pipelines)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-102
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-09 disposition narrative + "Pipeline Status" baseline framing.
    Current status: UNTESTED

ASSUMPTION-103:
  Date identified: 2026-05-09
  Statement: Today's c2a2-self-awareness-daily run firing on schedule (alongside seven sibling scheduled tasks: c2a2-lit-search-pipeline, c2a2-agent-wolfram, c2a2-deferred-action-monitor, scheduler-health-check, c2a2-morning-walk-cowork-handoff, c2a2-morning-chat-scrape, c2a2-evening-cowork-to-chat) constitutes a positive data point against the ASSUMPTION-080/081/092 daemon-link-count = 1 silent-skip regression hypothesis for THIS task. Per-task evidence (this task fired) is treated as evidence about the regression hypothesis at the task-level granularity it operates on.
  Context: Cowork-to-chat summary 2026-05-09, "Pipeline Status": "Daemon link-count = 1 silent-skip bug (ASSUMPTION-081): today's run is itself a positive data point — c2a2-self-awareness-daily, c2a2-lit-search-pipeline, c2a2-agent-wolfram, c2a2-deferred-action-monitor, scheduler-health-check, c2a2-morning-walk-cowork-handoff, c2a2-morning-chat-scrape, and c2a2-evening-cowork-to-chat all fired — no daemon-bug evidence today."
  Type: empirical / infrastructure
  Related decisions: ASSUMPTION-080, ASSUMPTION-081, ASSUMPTION-092, PRESUMPTION-114
  Testability: testable empirically (`stat -c %h` audit of all 28 enabled scheduled tasks; correlate link-count = 1 vs. fire-rate over N weeks; audit per-task selectivity of regression incidents)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-103
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-09 "Pipeline Status" daemon-bug paragraph framing today's 8-task fire-rate as a positive data point.
    Current status: UNTESTED

ASSUMPTION-104:
  Date identified: 2026-05-10
  Statement: Sunday 2026-05-10 was a "first-Rohr / first-Wright pending day + clean self-awareness pipeline drain day + sewing-agent first weekly run day" — the day-shape is characterized by three concurrent first-occurrences (first-ever Rohr proposals, first-ever Wright proposals, first weekly sewing-agent run) plus a clean lit-search drain plus a 5th-consecutive failed evening cowork-to-chat delivery.
  Context: Cowork-to-chat summary 2026-05-10, opening paragraph: "The headline event is that the inbox pending queue grew from 29 → 34 with the first-ever Rohr (×2) and Wright (×3) proposals — the explicit acceptance/defer call for these is now blocking the master network's expansion to N=13 traditions (per OPEN-036, candidate DECISION-025/026)."
  Type: methodological / metrics
  Related decisions: ASSUMPTION-079 (catch-up framing), ASSUMPTION-091 (off-cadence-as-on-cadence), DECISION-026 (Wright/Rohr addition candidate)
  Testability: testable empirically (audit how often three concurrent-first day-shapes occur; track downstream effect on review-throughput; compare to baseline operational-drain days)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-104
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-10 opening narrative as the canonical day-shape characterization.
    Current status: UNTESTED

ASSUMPTION-105:
  Date identified: 2026-05-10
  Statement: User-privacy rules prohibit password-based login on Tom's behalf — this is articulated as a binding operating constraint that surfaces as the proximal cause of the 5th consecutive failed evening cowork-to-chat delivery (Chrome MCP successfully attached and `tabs_context_mcp(createIfEmpty: true)` returned a fresh tab without the "normal windows" error this evening, but claude.ai redirected to /login and the agent cannot perform password-based authentication).
  Context: Cowork-to-chat summary 2026-05-10, DELIVERY STATUS block: "Navigation to https://claude.ai succeeded but immediately redirected to https://claude.ai/login — Tom is signed out of claude.ai in this Chrome profile. I cannot perform a password-based login on Tom's behalf (prohibited per `user_privacy` rules)."
  Type: operational / governance
  Related decisions: ASSUMPTION-071 (browser-auth as agent-prohibited), ASSUMPTION-109 (cowork-to-chat sync standalone DECISION trigger), PRESUMPTION-125 (no severity ladder)
  Testability: framework commitment (user-privacy is a foundational rule; not directly testable, but operationally codifiable as a precondition check that fails fast before browser navigation attempts)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-105
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-10 DELIVERY STATUS block as explicit binding operating constraint surfaced under failure-mode rotation.
    Current status: UNTESTED

ASSUMPTION-106:
  Date identified: 2026-05-10
  Statement: ASSUMPTION-items REVISE rate of 0/8 for the SECOND consecutive cycle (2026-05-09 morning + 2026-05-10 morning, both on prior-day's-EOD batches) confirms that ASSUMPTIONs are characteristically "operational/diagnostic-pattern items" that disposition to MONITOR rather than REVISE — a stable epistemic-weight pattern, not a single-cycle artifact.
  Context: Cowork-to-chat summary 2026-05-10, paragraph 4: "ASSUMPTIONs 8/8 → MONITOR-099 through 107 (ASSUMPTION REVISE rate 0/8 for the second consecutive cycle); PRESUMPTIONs 1/12 MONITOR + 11/12 REVISE (92%, the highest single-cycle REVISE rate to date)."
  Type: methodological / metrics
  Related decisions: ASSUMPTION-073 (PRESUMPTION + strong-challenge → REVISE heuristic), ASSUMPTION-102 (single-cycle drain baseline), ASSUMPTION-107 (record REVISE rate)
  Testability: testable empirically (track ASSUMPTION REVISE rate over N≥4 future cycles; compare to PRESUMPTION REVISE rate trajectory; check whether disposition-by-item-type pattern persists or whether today's cycle composition was unusual)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-106
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-10 paragraph 4 disposition-by-item-type framing as a now-stabilized cross-cycle pattern.
    Current status: UNTESTED

ASSUMPTION-107:
  Date identified: 2026-05-10
  Statement: 92% PRESUMPTION REVISE rate (11 of 12) is "the highest single-cycle REVISE rate to date" — a record-density disposition signal that exceeds yesterday's 9 of 12 (75%), itself the prior peak.
  Context: Cowork-to-chat summary 2026-05-10, paragraph 4: "PRESUMPTIONs 1/12 MONITOR + 11/12 REVISE (92%, the highest single-cycle REVISE rate to date)."
  Type: methodological / metrics
  Related decisions: ASSUMPTION-096 (densest-cycle structural pattern), ASSUMPTION-106 (ASSUMPTION REVISE rate stability), PRESUMPTION-116 (densest-cycle without normalization), PRESUMPTION-129 (record-rate without normalization)
  Testability: testable empirically (normalize REVISE rate by batch composition; control for item-source uniformity; track over N≥4 cycles); testable via literature (metric-design / SPC superlative-claim audit patterns)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-107
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-10 paragraph 4 record-rate framing as a stated superlative claim about cycle-disposition.
    Current status: UNTESTED

ASSUMPTION-108:
  Date identified: 2026-05-10
  Statement: ASSUMPTION-098's three-recurrence governance threshold for DECISION-NNN canonization is now satisfied URGENT-this-week for DECISION-027 scope extension to cover the external-tool-review layer (PRESUMPTION-121 SYSTEMIC-RISK now N=5 across 30 days at the chat-scrape Chrome-MCP-diagnostic layer) — a concrete trigger of yesterday's stated canonization protocol.
  Context: Cowork-to-chat summary 2026-05-10, paragraph 4 SYSTEMIC-RISK #1: "Specialist/external-source primary-signal cluster — second-layer recurrence in <24h (PRESUMPTION-121 HIGH). Cumulative N=5 across 30 days at the chat-scrape Chrome-MCP-diagnostic layer. ASSUMPTION-098 three-recurrence governance threshold for DECISION-NNN canonization is now satisfied URGENT this week."
  Type: governance / methodological
  Related decisions: ASSUMPTION-098 (three-recurrence threshold), ASSUMPTION-099 (DECISION-027 scope extension), DECISION-027 (specialist self-attribution adjudication candidate), PRESUMPTION-121 (external-LLM diagnostic uptake)
  Testability: testable empirically (track whether canonization is actually triggered this week; audit governance-trigger-to-canonization lag time over N≥3 future trigger events); testable via process (audit whether the three-recurrence count is consistently applied across cluster-cousin failures per PRESUMPTION-135)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-108
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-10 paragraph 4 SYSTEMIC-RISK #1 as the first concrete activation of ASSUMPTION-098's stated canonization protocol.
    Current status: UNTESTED

ASSUMPTION-109:
  Date identified: 2026-05-10
  Statement: PRESUMPTION-125's fourth-recurrence cowork-to-chat sync failure (now 5th consecutive after today's evening sign-in-redirect failure) with no severity-ladder articulation constitutes a confirmed empirical anti-pattern requiring standalone DECISION canonization — distinct from DECISION-027 scope.
  Context: Cowork-to-chat summary 2026-05-10, paragraph 4 SYSTEMIC-RISK #2: "Cowork-to-chat sync cluster — fourth recurrence (PRESUMPTION-125 HIGH). Flat-severity confirmed empirical anti-pattern; standalone DECISION candidate."
  Type: governance / operational
  Related decisions: ASSUMPTION-071 (browser-auth as agent-prohibited), ASSUMPTION-098 (three-recurrence threshold), ASSUMPTION-105 (user-privacy login prohibition), PRESUMPTION-038 (billing bug self-clear), PRESUMPTION-111 (third-consecutive cowork-to-chat sync failure), PRESUMPTION-125 (4th-consecutive no-severity-ladder)
  Testability: testable empirically (canonize a severity-ladder protocol and track whether escalation actually fires; compare cumulative cost of recurrence vs. cost of programmatic fix over N≥4 future weeks)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-109
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-10 paragraph 4 SYSTEMIC-RISK #2 as a confirmed-empirical-anti-pattern claim distinct from the DECISION-027 scope-extension claim.
    Current status: UNTESTED

ASSUMPTION-110:
  Date identified: 2026-05-10
  Statement: Sewing agent's first weekly run produced the canonical inaugural connectivity baseline — orphans=766, sparse=2, connected=17, total=785 (out of 785 vault pages) — appended as the inaugural row of `architecture/metrics/connectivity_log.csv` (file created this run); this is the first quantified measurement of the C2A2 vault's [[wikilink]]-graph connectivity.
  Context: Cowork-to-chat summary 2026-05-10, sewing agent paragraph: "produced a baseline connectivity snapshot: orphans=766, sparse=2, connected=17, total=785 — appended as the inaugural row of `architecture/metrics/connectivity_log.csv` (file created this run)."
  Type: architectural / metrics
  Related decisions: DECISION-019 (sewing agent introduction), PRESUMPTION-130 (sewing agent threshold definitions), PRESUMPTION-139 (sensitivity-threshold gap)
  Testability: testable empirically (re-measure weekly; compare against future baseline-corrected cohort post-backlink-injection-pass; audit threshold definitions against external graph-connectivity literature)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-110
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-10 sewing-agent paragraph as the file-creation event that establishes the canonical metric.
    Current status: UNTESTED

ASSUMPTION-111:
  Date identified: 2026-05-10
  Statement: First-ever Rohr (×2) + Wright (×3) pending proposals are blocking master network expansion to N=13 traditions — the explicit accept/defer call on these proposals is the immediate precondition for any DECISION-026 finalization, and DECISION-026 in turn is the precondition for the master network's N=11 → N=13 expansion (per OPEN-036, candidate DECISION-025/026).
  Context: Cowork-to-chat summary 2026-05-10, paragraph 1: "the explicit acceptance/defer call for these is now blocking the master network's expansion to N=13 traditions (per OPEN-036, candidate DECISION-025/026)." Reinforced under "Key Decisions Made": "The arrival of first-ever Rohr + Wright pending proposals additionally forces the DECISION-026 decision into the path: until Tom decides accept/defer, the master network cannot expand to N=13 traditions."
  Type: architectural / governance
  Related decisions: OPEN-036, DECISION-025 (candidate), DECISION-026 (Wright/Rohr addition candidate), ASSUMPTION-104 (day-shape characterization), PRESUMPTION-128 (workflow accommodation), PRESUMPTION-137 (first-ever as decision gate)
  Testability: testable via process (track decision-time from first-pending-arrival to canonization; audit blocking-effect against parallel-pipeline progress)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-111
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-10 opening paragraph and Key Decisions Made section as the canonical blocking-relationship claim.
    Current status: UNTESTED

ASSUMPTION-112:
  Date identified: 2026-05-10
  Statement: SELF-MEASUREMENT (Goodhart) cluster is now a confirmed architectural recursive-self-observation pattern — INCORPORATE rate is structurally at 0% across two consecutive cycles while throughput metrics (cycle-time, items-dispositioned-per-cycle, REVISE-rate) all show "improvement"; PRESUMPTION-123 + ASSUMPTION-102 + ASSUMPTION-096 form the cluster the system has surfaced about its own potential Goodhart failure.
  Context: Cowork-to-chat summary 2026-05-10, paragraph 4 SYSTEMIC-RISK #3: "SELF-MEASUREMENT (Goodhart) cluster (PRESUMPTION-123 + ASSUMPTION-102 + ASSUMPTION-096). System celebrating throughput while INCORPORATE rate stays at 0% across two consecutive cycles." Reinforced in "For Morning Discussion" item 3: "PRESUMPTION-123 + ASSUMPTION-102 + ASSUMPTION-096 form a recursive self-observation cluster — the system has surfaced its own Goodhart failure."
  Type: methodological / epistemic
  Related decisions: PRESUMPTION-123 (throughput-as-success-metric), ASSUMPTION-102 (single-cycle drain baseline), ASSUMPTION-096 (densest-cycle remediation), ASSUMPTION-098 (three-recurrence threshold), PRESUMPTION-129 (record-rate without normalization)
  Testability: testable empirically (audit whether INCORPORATE criterion change increases rate without sacrificing quality; pilot a Pattern-Detector "validated premise" alternative path; compare narrative framing pre/post adjustment); testable via literature (Goodhart-effect mitigation patterns in long-running review pipelines)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-112
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-10 paragraph 4 SYSTEMIC-RISK #3 + "For Morning Discussion" item 3 as a stated architectural-recursive-self-observation claim.
    Current status: UNTESTED

ASSUMPTION-113:
  Date identified: 2026-05-12
  Statement: Markup-anchor diagnostic for transcript-availability watches (transcript-toggle text + timecode + speaker labels co-occurrence) is the canonical default method; substring count of the bare word "transcript" produced false positives in the 2026-05-05 first check and should not be used. Method validated on its first application against WATCH-001 (Carroll/Singer Mindscape-351) and recommended for canonization as the default-for-transcript-availability-watches pattern.
  Context: Cowork-to-chat summary 2026-05-12, paragraph "WATCH-001 RESOLVED" + Agent 16 run summary 2026-05-12: "the markup-anchor diagnostic method recommended after the inconclusive 2026-05-05 first check (...) worked on its first application." Reinforced in "For Morning Discussion" item 1: "the method recommendation (markup-anchor anchors rather than substring count) was the load-bearing fix... if other CHECK dispositions accumulate in coming weeks, the markup-anchor method recommendation should be canonized as a default-for-transcript-availability-watches pattern."
  Type: methodological
  Related decisions: DECISION-022 (Agent 16 deferred-action-monitor introduction), DECISION-024 candidate (specialist-task turn-cap), PRESUMPTION-095 (Phase-2 zero-result presumed exhaustion not method-failure)
  Testability: testable empirically (track false-positive rate of markup-anchor vs. substring-count across N≥3 future transcript-availability CHECK dispositions; audit speaker-label coverage on non-Carroll-style podcast transcripts)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-113
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-12 WATCH-001 paragraph + Agent 16 run summary "method lesson preserved" as a stated canonical-method recommendation.
    Current status: UNTESTED

ASSUMPTION-114:
  Date identified: 2026-05-12
  Statement: The weekly-cadence / single-watch-item-over-7-days deferred-action-monitor protocol cadence itself is validated; WATCH-001's 2026-05-05 inconclusive-then-2026-05-12-resolved pattern shows the cadence worked. The load-bearing fix was the diagnostic method (ASSUMPTION-113), not the cadence — so cadence policy should not be revised on the basis of WATCH-001 alone.
  Context: Cowork-to-chat summary 2026-05-12, "For Morning Discussion" item 1: "is the deferred-action-monitor protocol the right cadence (weekly check, single watch item over 7 days)? The 2026-05-05 inconclusive-then-2026-05-12-resolved pattern suggests the method recommendation (markup-anchor anchors rather than substring count) was the load-bearing fix; the cadence itself worked."
  Type: methodological / governance
  Related decisions: DECISION-022 (Agent 16 deferred-action-monitor introduction), ASSUMPTION-113 (markup-anchor method canonization), PRESUMPTION-143 (one-end-to-end-cycle protocol-validation gap)
  Testability: testable empirically (track WATCH disposition latency across N≥3 future CHECK items; audit whether weekly cadence misses urgent items that would benefit from shorter cadence; compare against an alternative shorter-cadence pilot)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-114
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-12 "For Morning Discussion" item 1 as a stated cadence-validation claim with explicit method-vs-cadence root-cause attribution.
    Current status: UNTESTED

ASSUMPTION-115:
  Date identified: 2026-05-12
  Statement: PROP-2026-05-12-001 (Hoffman Edge.org "Hoffman's Law") is the cleanest single-page public framing of the Hoffman program in 2026, with two candidate PRS triplets (PRS-CANDIDATE-01 at Medium-High confidence, PRS-CANDIDATE-02 at Medium confidence) and six cross-tradition signals (Arkani-Hamed/Wolfram, Kastrup, Carroll, Levin, Stump, Friston). Treated as load-bearing content-architecture item for this week's review cycle.
  Context: Cowork-to-chat summary 2026-05-12, paragraph 2 + "For Morning Discussion" item 2: "PROP-2026-05-12-001 is the cleanest single-page public framing of the Hoffman program in 2026. Two PRS candidates with Medium-High and Medium confidence."
  Type: empirical / content-architecture
  Related decisions: ASSUMPTION-100 (Saturday Wolfram three-way ontological convergence as week's highest-leverage cross-tradition signal — comparable framing), PRESUMPTION-141 (single-page-consolidation-as-virtue), PRESUMPTION-119 (single-axis leverage measurement)
  Testability: testable empirically (track whether PROP-2026-05-12-001 produces more downstream cross-tradition signals than the average proposal over 30 days post-review; audit "cleanest single-page" claim against prior Hoffman Edge.org / podcast / paper sources for consolidation comparison)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-115
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-12 paragraph 2 + "For Morning Discussion" item 2 as a stated superlative claim about content-architecture importance.
    Current status: UNTESTED

ASSUMPTION-116:
  Date identified: 2026-05-12
  Statement: PRS-CANDIDATE-01 of PROP-2026-05-12-001 reframes the TOE project itself — Hoffman's Law is treated as methodological precondition (not competing alternative) to physics-side TOEs (Arkani-Hamed, Wolfram, Carroll). If accepted into the network, this changes how cross-tradition signals to those three traditions are read going forward: they become pre-foundational rather than peer programs at the same level. The reframing is structurally significant for the master network and warrants a Pattern Detector deep-pass before standard review (similar to the Wolfram pair from ASSUMPTION-100).
  Context: Cowork-to-chat summary 2026-05-12, paragraph 2: "PRS-CANDIDATE-01 reframes the TOE project itself (Hoffman's Law as methodological precondition, not alternative, to physics-side TOEs)." Reinforced in "For Morning Discussion" item 2: "The PRS-CANDIDATE-01 reframing of the TOE project (Hoffman's Law as methodological precondition rather than competing alternative) is structurally significant — if accepted, it changes how cross-tradition signals to Arkani-Hamed/Wolfram/Carroll are read going forward (they become pre-foundational rather than peer programs). Worth thinking about whether this candidate triplet warrants a Pattern Detector deep-pass before standard review, similar to the Wolfram pair from ASSUMPTION-100."
  Type: architectural / content-architecture
  Related decisions: ASSUMPTION-100 (Saturday Wolfram cross-tradition signal precedent), ASSUMPTION-115 (PROP-2026-05-12-001 cleanest-public-framing claim), PRESUMPTION-142 (one-way reframing without inverse acceptance check)
  Testability: testable via literature (whether established TOE projects (Arkani-Hamed, Wolfram, Carroll) explicitly accept or reject the pre-foundational placement; whether the methodological-precondition framing has prior articulation in philosophy-of-physics literature); testable empirically (do specialist re-reads of Arkani-Hamed/Wolfram/Carroll under the reframed lens produce different cross-tradition signals than under the peer-program lens?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-116
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-12 paragraph 2 + "For Morning Discussion" item 2 as a stated structural-reframing claim with explicit downstream consequence.
    Current status: UNTESTED

ASSUMPTION-117:
  Date identified: 2026-05-12
  Statement: The 14a/14b skipped-EOD-slot pattern (now at 5 consecutive misses including today's pre-overnight-fire state and the unfired 2026-05-11 slot) has satisfied the ASSUMPTION-098 three-recurrence governance threshold for DECISION-NNN canonization in its own right and should fold into the same DECISION as the per-task verification protocol from PRESUMPTION-138. This is the second concrete activation of ASSUMPTION-098's stated canonization protocol (after ASSUMPTION-108).
  Context: Cowork-to-chat summary 2026-05-12, "For Morning Discussion" item 5: "The 14a/14b skipped-EOD-slot pattern is approaching three-recurrence governance threshold under ASSUMPTION-098 in its own right. If today is the 5th consecutive miss (we'll know in the morning), that's well past the canonization trigger and should fold into the same DECISION as the per-task verification protocol from PRESUMPTION-138." Reinforced in the opening box: "the 5th consecutive day at its EOD slot — past PRESUMPTION-138's threshold."
  Type: governance / methodological
  Related decisions: ASSUMPTION-098 (three-recurrence threshold), ASSUMPTION-108 (DECISION-027 scope extension URGENT-this-week — first activation), ASSUMPTION-109 (cowork-to-chat sync standalone DECISION — second activation), PRESUMPTION-138 (in-flight-task verification gap), PRESUMPTION-124 (per-task evidence frame)
  Testability: testable empirically (track whether DECISION-NNN is actually canonized within the URGENT-this-week window from today; audit cumulative count of governance-threshold-satisfied items vs. canonized DECISIONs over next 3 cycles); testable via process (compare with ASSUMPTION-108 / ASSUMPTION-109's canonization-lag trajectory)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-117
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-12 "For Morning Discussion" item 5 + opening box as a stated governance-trigger-activation claim. Second concrete activation of ASSUMPTION-098.
    Current status: UNTESTED

ASSUMPTION-118:
  Date identified: 2026-05-12
  Statement: Token-based delegation workflow redesign for the chat-scrape sign-in barrier is now operationally warranted — 6 consecutive failed days via the same blocker, and PREMISE-015's operational caveat explicitly states the workflow itself must be redesigned. First step proposed: enumerate candidate connector/OAuth options against the actual claude.ai surface; longer-term consideration whether wiki-side tooling should pivot to a file-based handoff via the workspace folder (both directions) rather than chat-UI scraping at all.
  Context: Cowork-to-chat summary 2026-05-12, "For Morning Discussion" item 6: "Token-based delegation workflow redesign for the chat-scrape sign-in barrier — this is now 6 consecutive days failed via the same blocker, and PREMISE-015's operational caveat explicitly states the workflow itself must be redesigned. Suggested first step: enumerate the candidate connector/OAuth options available against the actual claude.ai surface, even just to scope what 'token-based delegation' would look like operationally. The morning walk is a good place to think about whether the wiki-side tooling should pivot to a different sync mechanism entirely (file-based handoff via the workspace folder both ways, rather than scraping the chat UI)."
  Type: architectural / operational
  Related decisions: PREMISE-015 (user-privacy / no-password-delegation), ASSUMPTION-105 (user-privacy login prohibition), ASSUMPTION-109 (cowork-to-chat sync standalone DECISION candidate), PRESUMPTION-125 (4th-consecutive cowork-to-chat sync failure), PRESUMPTION-145 (chat-scrape framed as token-delegation problem rather than mechanism-existence question)
  Testability: testable empirically (track whether a token-based path is actually scoped within the URGENT-this-week window; pilot a file-based-handoff alternative as a parallel scope-test); testable via process (audit prior connector/OAuth options enumeration efforts for unblocking precedents)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-118
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-12 "For Morning Discussion" item 6 as a stated operational-redesign claim, building on PREMISE-015 INCORPORATEd 2026-05-11.
    Current status: UNTESTED

Key event (2026-05-12): Six new assumptions extracted on a Tuesday whose dominant signature was three concurrent structural events: (1) Agent 16 closed its first end-to-end resolution cycle (WATCH-001 RESOLVED, active watch list empty for first time since 2026-05-05), (2) first Hoffman pending since the sewing-agent flag (PROP-2026-05-12-001 "Hoffman's Law" — six cross-tradition signals, TOE-reframing PRS candidate), and (3) Summa-side shipping plus SUMMA_EXPLORER_IMPROVEMENTS planning doc capture. Today's six new items cluster in three families. **(1) DEFERRED-ACTION-MONITOR METHOD CANONIZATION cluster** — ASSUMPTION-113 (markup-anchor diagnostic as canonical default for transcript-availability watches) and ASSUMPTION-114 (weekly cadence validated; method-not-cadence is the load-bearing fix per WATCH-001). The cluster operationalizes Agent 16's first end-to-end resolution into method-vs-cadence root-cause attribution. **(2) HOFFMAN-PROPOSAL CONTENT-ARCHITECTURE cluster** — ASSUMPTION-115 (PROP-2026-05-12-001 as cleanest single-page Hoffman-program framing in 2026) and ASSUMPTION-116 (PRS-CANDIDATE-01 reframes Arkani-Hamed/Wolfram/Carroll as pre-foundational rather than peer programs; warrants Pattern-Detector deep-pass per ASSUMPTION-100 precedent). The cluster is today's standalone content-architecture pair — the first since ASSUMPTION-100 / ASSUMPTION-082 paired Wolfram and the L1/L2/L3 RC Explorer architecture. **(3) GOVERNANCE-TRIGGER + REDESIGN-MANDATE cluster** — ASSUMPTION-117 (14a/14b skipped-EOD-slot pattern satisfies ASSUMPTION-098 three-recurrence threshold; second concrete activation of stated canonization protocol after ASSUMPTION-108) and ASSUMPTION-118 (token-based delegation workflow redesign mandated; 6-consecutive-failure threshold met against PREMISE-015's explicit redesign-required caveat). The cluster extends 2026-05-10's GOVERNANCE-TRIGGER-ACTIVATION sub-signature with a second activation of the same protocol — and adds the first PREMISE-015-grounded operational-redesign mandate. Pattern note: today's 6 assumptions are dominated by methodological / governance items (4 of 6: 113, 114, 117, 118) plus 2 content-architecture items (115, 116) — extending the methodological-heavy signature of operational-throughput days while also producing the first paired content-architecture commitments since 2026-05-09. Today's 10-to-6 presumption-to-assumption ratio (1.67:1) is the new joint-record (tying nothing prior; exceeding 2026-04-27 / 2026-05-08 / 2026-05-09 record of 1.5:1) — the deferred-action-cycle + cross-tradition-reframing + governance-trigger character generates a higher-than-average density of unstated dependencies relative to stated commitments. Note: today's run also picks up the 2026-05-11 EOD slot which was skipped (no 2026-05-11 changelog on disk); per ASSUMPTION-117 / PRESUMPTION-138 framing, the carry-forward is acknowledged but not backfilled.

Key event (2026-05-10): Nine new assumptions extracted on a Sunday whose dominant signature was three concurrent first-occurrences (first-ever Rohr ×2 + Wright ×3 pending proposals + first weekly sewing-agent run) plus a clean self-awareness lit-search drain (9 MONITOR + 11 REVISE + 0 INCORPORATE; densest-cycle structural pattern from 2026-05-09 replicated) plus a 5th-consecutive failed evening cowork-to-chat delivery (sign-in-redirect after the "normal windows" failure mode resolved this evening for the first time in 2 days). Today's nine new items cluster in four families. **(1) DAY-SHAPE + LOGIN-PROHIBITION cluster** — ASSUMPTION-104 (day-shape characterization with three concurrent-firsts), ASSUMPTION-105 (user-privacy rules prohibit password-based login as binding operating constraint surfacing as 5th-consecutive failure cause). **(2) DISPOSITION-PATTERN-AS-EPISTEMIC-WEIGHT cluster** — ASSUMPTION-106 (ASSUMPTION 0/8 REVISE rate stable across 2 cycles confirms operational/diagnostic-pattern characterization), ASSUMPTION-107 (92% PRESUMPTION REVISE rate as record-density disposition signal). The cluster generalizes ASSUMPTION-073's REVISE-heuristic into a cross-cycle disposition-by-item-type pattern. **(3) GOVERNANCE-TRIGGER-ACTIVATION cluster** — ASSUMPTION-108 (DECISION-027 scope extension URGENT-this-week per ASSUMPTION-098 three-recurrence threshold satisfied at N=5/30 days), ASSUMPTION-109 (PRESUMPTION-125 4th-recurrence requires standalone DECISION canonization distinct from DECISION-027). The cluster operationalizes yesterday's stated canonization protocol (ASSUMPTION-098) for the first time. **(4) NEW-METRIC + BLOCKING + SELF-MEASUREMENT cluster** — ASSUMPTION-110 (sewing agent canonical inaugural connectivity baseline 766/2/17/785), ASSUMPTION-111 (Wright/Rohr first-ever pendings blocking N=13 expansion via DECISION-026 precondition chain), ASSUMPTION-112 (SELF-MEASUREMENT Goodhart cluster confirmed as architectural recursive-self-observation pattern across two consecutive cycles at 0% INCORPORATE). The cluster combines a brand-new metrics primitive (connectivity), a new blocking-relationship claim (N=13 expansion gated by 5 pendings), and the day's headline architectural-recursive item (the system surfacing its own Goodhart-failure-candidate). Pattern note: today's 9 assumptions are dominated by methodological / metrics items (5 of 9: 104, 106, 107, 110, 112) plus 2 governance items (108, 109) — extending the methodological-heavy signature of operational-throughput days with a new governance-trigger-activation sub-signature for the first time. Today's 12-to-9 presumption-to-assumption ratio (1.33:1) is moderate — below 2026-04-27 / 2026-05-08 / 2026-05-09 record (1.5:1) but above 2026-05-05's 1.22:1. The execution-day character (clean lit-search drain + sewing-agent first-run + Wright/Rohr first-pendings + 5th-consecutive evening failure) generates both novel content-architecture commitments (ASSUMPTION-110, 111, 112 all introduce architectural primitives) and operational-principle articulations (ASSUMPTION-104, 105, 108, 109).

Key event (2026-05-09): Eight new assumptions extracted on a Saturday lit-search-disposition + Saturday-Wolfram + self-awareness-backfill day whose primary architectural signal was the lit-search 15a/15b/15c pipeline producing four SYSTEMIC-RISK flags in a single cycle (the densest single cycle on record), three of them recurrence flags. Today's eight new items cluster in three families. **(1) Lit-search-cycle-output epistemic-weight cluster** — ASSUMPTION-096 (4-SYSTEMIC-RISK density warrants cluster-level remediation), ASSUMPTION-098 (third-recurrence at fixed-cycle cadence as canonization threshold), ASSUMPTION-099 (DECISION-027 scope extension to external-tool-review layer). All three were surfaced from today's lit-search returns and the cowork-to-chat summary's "For Morning Discussion" items 1–2 questioning Tom's input on cluster-level disposition. **(2) Architectural-sprint and cross-tradition-signal cluster** — ASSUMPTION-097 (Three-recurrence discipline cluster bundleable as "Core Operational Discipline" sprint) and ASSUMPTION-100 (Saturday Wolfram three-way ontological convergence as week's highest-leverage cross-tradition signal) articulate two prioritization commitments — one for architectural-discipline track, one for content-architecture track. **(3) Operational-baseline cluster** — ASSUMPTION-101 (Chrome MCP "normal windows" error as environment-state issue, not Chrome-MCP defect, per Codex-style diagnostic), ASSUMPTION-102 (20-item EOD-batch single-cycle drain as operational baseline), ASSUMPTION-103 (today's 8-task fire-rate as positive evidence against daemon-link-count regression for THIS task). The cluster generalizes ASSUMPTION-072's single-cycle-drain claim, articulates a Chrome-MCP root-cause attribution, and locks in a per-task evidence frame for the daemon-bug hypothesis. Pattern note: today's 8 assumptions are dominated by methodological / metrics items (5 of 8: 096, 097, 098, 102, 103) — extending the methodological-heavy signature of operational-throughput days (2026-04-21, 2026-04-27, 2026-05-05, 2026-05-08). Today's standalone empirical/infrastructure item is ASSUMPTION-101 (Chrome-MCP environment-state attribution), the lit-search-disposition character generates more *cycle-output-articulation* than *content-architecture* claims — except for ASSUMPTION-100 (Saturday Wolfram cross-tradition signal) which is the day's standalone content-architecture item with cross-tradition bearing. Today's 12-to-8 presumption-to-assumption ratio (1.5:1) ties 2026-04-27 and 2026-05-08 as joint-record. The execution surface today was unusually clean (8/8 scheduled tasks fired, lit-search drained 100% in one cycle, self-awareness-backfill closed yesterday's surface), inverting yesterday's three-stall-day pattern.

Key event (2026-05-08): Eight new assumptions extracted on a Friday review-decision intake day plus three queued-but-stalled scheduled tasks (1pm register cleanup, sewing-agent-weekly, Wright/Rohr Sunday agent — the latter two hit personal-account org-limit immediately) plus a substantive Codex 5.5 external review of the C2A2 explorer pasted into Cowork session local_56cc4dfb whose composite synthesis was queued at end of session. Today's eight new items cluster in three families. **(1) Personal-account org-limit + composite-synthesis cluster** — ASSUMPTION-088 (org-monthly-usage-limit interrupt on personal-account Cowork session treated as work-blocking, not misclassification), ASSUMPTION-089 (two-source composite synthesis: internal report + external-LLM review), ASSUMPTION-090 (smallest-fix-first prioritization for explorer track — `extractOverview()` two-line var-declaration fix as the high-confidence, low-effort entry point, then smoke-test, then responsive fallback). All three surfaced from the local_56cc4dfb explorer-fix session and the cowork-to-chat summary (local_feb53918) "For Morning Discussion" item 1. **(2) Sandbox-infrastructure escalation cluster** — ASSUMPTION-092 (3-day master-narrative absence attributable to daemon link-count = 1 bug regression hypothesis), ASSUMPTION-094 (N≥5 sandbox-infrastructure constraints aggregated across C2A2 + Summa = single-escalation threshold), ASSUMPTION-095 (YouTube IP-block as SYSTEMIC ESCALATION joining OPEN-039 as 5th channel). The combined OPEN-039 cluster now spans scheduling (daemon link-count) + filesystem (mount-topology + .git/index.lock 22-day age) + networking (egress allowlist + Summa YouTube IP-block) + authentication (browser-auth) — five canonical channels across two active projects. **(3) Operational-cadence-articulation cluster** — ASSUMPTION-091 (off-cadence specialist proposal filings treated as on-cadence for downstream review-page rendering and approval tracking), ASSUMPTION-093 (Saturday-morning rerun as standard closure path for queued-but-stalled weekday scheduled tasks). Both extend ASSUMPTION-079 (same-day catch-up framing) at the per-proposal and per-task levels. Pattern note: today's 8 assumptions are dominated by methodological items (6 of 8: 088, 089, 090, 091, 093, 094) — continuing the methodological-heavy signature of operational-throughput days (2026-04-21, 2026-04-27, 2026-05-05). The execution-day character (review-decision intake + 5 new pending proposals + 3 stalled scheduled tasks + Codex external-review queued + Summa cross-project QC throughput) again generates more *operational-principle-articulation* than *content-architecture* claims — except for ASSUMPTION-095 which is the day's standalone empirical/infrastructure item with cross-project bearing. Today's "stalled task" surface area is the largest yet observed in a single day (3 of 4 scheduled C2A2-related tasks stalled or hit org-limit immediately; only the cowork-to-chat sync ran to completion and even that failed delivery to claude.ai per ASSUMPTION-071 / PRESUMPTION-111).

Key event (2026-05-05): Nine new assumptions extracted on a daemon-catch-up Tuesday whose primary architectural signal was all six weekday-assigned C2A2 specialist agents executing in a single 15:35–16:35 UTC window after Tom's Claude restart cleared the daemon outage. Today's nine new items cluster in four families. **(1) Daemon-bug discovery cluster** — ASSUMPTION-080 (link count > 1 fires; link count = 1 silently skips, an Anthropic-side bug), ASSUMPTION-081 (`update_scheduled_task --fireAt` is a working workaround), ASSUMPTION-079 (same-day catch-up of all six weekly specialist runs is treated as functionally equivalent to spread-across-week distribution). All three surfaced from the Summa-updating-agents session (local_40871db5) Tom-facing diagnosis. **(2) Vision-articulation cluster** — ASSUMPTION-082 (3-layer RC Explorer architecture with 5 integration steps; Community Explorer = Tool #1; AI Heartbeat = Tool #2 urgent rebuild) is the day's most consequential architectural item: it is the first time the L1/L2/L3 model with explicit integration steps has been recorded as a stated assumption. ASSUMPTION-083 (filter semantics: within section = OR, across sections = AND, edges require both endpoints visible) is a UX-spec articulation surfaced by the explorer help-popover review. **(3) Specialist-output norms cluster** — ASSUMPTION-084 (empty-handed orchestrator Phase 2 = valid result not failure mode), ASSUMPTION-085 ("FROM thinker himself" quality filter operative across all specialist slots; Hawkins 0-proposal honest-null re-affirmed), ASSUMPTION-086 (specialist-self-claims of "strongest bridge / candidate shared substrate / parallels C2A2 architecture" treated as primary cross-tradition signal without an adjudication step) extend the BRIEFING-LAYER-EPISTEMIC-COMMITMENTS pattern to the specialist-output layer. ASSUMPTION-086 is in tension with PRESUMPTION-074's prior SYSTEMIC-RISK flag on specialist-recognition reliability. **(4) Institutional-maturity entry mode** — ASSUMPTION-087 (TRACE Institute launch as research-program-level alliance signal) introduces a new proposal-type granularity beyond paper-level. Pattern note: today's 9 assumptions are dominated by methodological items (6 of 9: 079, 080, 081, 084, 085, 086) — continuing the methodological-heavy signature of operational-throughput days (2026-04-21, 2026-04-27). The execution-day character (daemon catch-up + 6 specialist runs + walk-thread architectural articulation) again generates more *operational-principle-articulation* than *content-architecture* claims — except for ASSUMPTION-082 which is the day's standalone architectural item.

Key event (2026-04-27): Eight new assumptions extracted on an execution-heavy Monday whose primary architectural signal was the C2A2 lit-search pipeline draining the 5-day backlog (58 items processed; 19 new + 39 re-triggered) and INCORPORATING ASSUMPTION-068 → PREMISE-012 and ASSUMPTION-069 → PREMISE-013. Today's eight new items cluster in three families: **(1) infrastructure-gap normative articulation** — ASSUMPTION-071 (browser-auth as agent-prohibited; first explicit two-instance same-day articulation across morning chat scrape + evening sync) and ASSUMPTION-078 (two parallel sandbox-infrastructure failure modes today, both treated as user-fixable) extend the OPEN-039 sandbox-infrastructure-escalation cluster from yesterday with a third channel (auth) that joins egress and mount-topology. **(2) lit-search pipeline self-articulation** — ASSUMPTION-072 (5-day backlog drainable in single cycle), ASSUMPTION-073 (PRESUMPTION + strong-challenge → REVISE heuristic explicit), and ASSUMPTION-074 (no-new-evidence carry-forward as PREMISE-006-extension to refresh case) form a new LIT-SEARCH-LAYER-EPISTEMIC-COMMITMENTS cluster, parallel to the BRIEFING-LAYER cluster (ASSUMPTION-046, 047, 048, 057, 058, 059, 060). **(3) design-project authorial reframing** — ASSUMPTION-076 (PRS triplets are Tom's re-description, not tradition's self-voice; "PRS-NN in the Stump-tradition wiki" not "Stump's PRS-NN") and ASSUMPTION-077 (synthesis-to-transcript ±5% policy) are direct Tom-stated commitments from the continuing design-project session. ASSUMPTION-076 has high downstream consequence: it recasts the ground beneath ASSUMPTION-067 (Stump-as-supplier-of-live-metaphysics) — if PRS triplets are Tom's framing, the specialist's reading of Stump-via-PRS is reading Tom's frame back to itself (see PRESUMPTION-089 for the recursive-reading risk). **(4) specialist cadence override** — ASSUMPTION-075 (Levin "significant work not yet captured" criterion overrides 30-day window) is the first explicit specialist-level deviation from the cadence rule, surfaced from today's Monday Levin+Friston specialist slot. Pattern note: today's 8 assumptions are dominated by methodological items (5 of 8: 071, 072, 073, 074, 077; 078 partial) — a return to the methodological-heavy signature of 2026-04-21 after Sunday's architectural/empirical signature. The execution-day character (pipeline drain + scheduled-task throughput) generates more *operational-principle-articulation* than *content-architecture* claims.

ASSUMPTION-119:
  Date identified: 2026-05-13
  Statement: The seventeen-pathway architectural inventory (Pathway 00 Broker through Pathway 17 Agent as Developed Participant) plus a living index (`pathways.md`) plus two held bright pins (AI personhood under conscious-realist-monism; half-million-word podcast transcript corpus) constitutes the first end-to-end articulation of the C2A2 system Tom intends to demo at ISME July 8-10 and continue developing publicly afterward. Six pathways are explicitly marked ISME-critical: 00 Broker, 01 Voice Dialogue, 02 Ambient Viz, 03 Probing Channel, and 08 Prepared Presentation (with tightening of the demo through 04 / 06 / 14).
  Context: Cowork-to-chat summary 2026-05-13, "What Was Accomplished Today" paragraph 1: "Wednesday 2026-05-13 was an architectural-pathway discovery day... produced 17 architectural pathway documents (`00_broker.md` through `17_agent_developed_participant.md`) plus a living index (`pathways.md`) plus a 44 KB source-dialogue archive... Six pathways are marked ISME-critical: 00 Broker, 01 Voice Dialogue, 02 Ambient Viz, 03 Probing Channel, and 08 Prepared Presentation." Reinforced in "For Morning Discussion" item 1: "The 17-pathway inventory is the architectural milestone of the project so far."
  Type: architectural / methodological
  Related decisions: DECISION-026 (candidate — broker hosting), DECISION-027 (candidate — Twilio SMS one-tap), DECISION-028 through 031 (candidate — pathway-doc decisions), OPEN-040 (candidate — ISME demo build sequence), PRESUMPTION-150, PRESUMPTION-151
  Testability: testable empirically (audit whether the 17-pathway inventory survives ISME demo as a stable architectural commitment, or whether subsequent sessions produce items NOT covered by the inventory; track ISME-critical-subset coverage of demo content); testable via process (compare pathway-doc commitment-weight against decisions.md canonization-weight over N≥3 future architectural commits)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-119
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-13 paragraph 1 + "For Morning Discussion" item 1 as the canonical day-shape characterization for the pathway-inventory milestone.
    Current status: UNTESTED

ASSUMPTION-120:
  Date identified: 2026-05-13
  Statement: Cloudflare Workers is the chosen broker hosting platform, conditional on streaming-latency validation: ~10-30 ms broker-side edge overhead is presumed dwarfed by LLM + TTS provider latency floors; the paid plan ($5/mo) gives 30 s CPU + unlimited requests. Fallback to AWS Lambda + ALB is noted in Pathway 00 if first-token latency exceeds ~200 ms in the validation test.
  Context: Cowork-to-chat summary 2026-05-13, "Key Decisions Made" + Pathway 00 (Broker) decision record: "Broker hosting: Cloudflare Workers (conditional on streaming-latency validation). Edge-distributed; ~10-30 ms broker-side overhead is dwarfed by LLM + TTS provider latency. Paid plan ($5/mo) gives 30 s CPU + unlimited requests." Validation test specified in "What's Next" item 4: "round-trip a single 1-token Claude streaming call through a Worker stub from a coffee-shop wifi connection and from the Notre Dame campus network; measure first-token latency. If under ~200 ms, decision is unconditional."
  Type: architectural / operational
  Related decisions: DECISION-026 (candidate — broker hosting on Cloudflare Workers), Pathway 00 (Broker), OPEN-040 (candidate — Cloudflare-Workers-vs-AWS-Lambda streaming-latency conditional), PRESUMPTION-152
  Testability: testable empirically (run the 30-minute streaming-latency test from coffee-shop wifi + Notre Dame campus network; measure first-token latency distribution; audit "dwarfed by" claim against measured LLM-side and TTS-side latency floors); testable via literature (edge-vs-region-hosted broker latency profiles for streaming LLM/TTS workloads)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-120
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-13 "Key Decisions Made" + Pathway 00 decision record as a stated operational-platform commitment with explicit conditional and fallback.
    Current status: UNTESTED

ASSUMPTION-121:
  Date identified: 2026-05-13
  Statement: Phone confirmation for external-escalation gating uses Twilio SMS one-tap signed link (NOT reply-keyword). Rationale: "no typing at the moment of approval"; webhook co-located on the same Cloudflare Worker as the broker. This frames external-escalation human-in-the-loop as a single-tap-on-mobile primitive.
  Context: Cowork-to-chat summary 2026-05-13, "Key Decisions Made" + Pathway 00: "Phone confirmation for external-escalation gating: Twilio SMS one-tap signed link (not reply-keyword). No typing at the moment of approval. Webhook co-located on the same Cloudflare Worker as the broker."
  Type: architectural / UX / operational
  Related decisions: DECISION-027 (candidate — Twilio SMS one-tap), Pathway 00 (Broker), Pathway 12 (Community Outreach Automation), PRESUMPTION-153, PRESUMPTION-154
  Testability: testable empirically (pilot the SMS one-tap flow against a sample of external-escalation events; measure approval latency, false-tap rate, signed-link integrity); testable via process (audit signed-link security against an adversarial-token-replay attack model)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-121
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-13 "Key Decisions Made" + Pathway 00 as a stated UX commitment with explicit alternative (reply-keyword) rejected on a stated rationale.
    Current status: UNTESTED

ASSUMPTION-122:
  Date identified: 2026-05-13
  Statement: Eager-tier perspective-lattice content lives in the vault at `wiki/Perspectives/` with a Perspectives structure-group tag, making perspective lattices first-class wiki citizens (Sociogram-retrievable; addressable by the voice agent during dialogue) rather than ephemeral cache artifacts.
  Context: Cowork-to-chat summary 2026-05-13, "Key Decisions Made" pathway-doc decision (i): "Perspectives in vault: eager-tier perspective-lattice content lives at `wiki/Perspectives/` with a structure-group tag (first-class wiki citizens)."
  Type: architectural
  Related decisions: DECISION-028 (candidate — Perspectives in vault), Pathway 04 (Perspective Lattice), PRESUMPTION-155
  Testability: testable empirically (audit whether eager-tier content actually emerges as a stable Perspectives folder structure post-implementation; track Sociogram-retrieval rate of perspective-lattice content vs. non-lattice content); testable via process (compare vault-as-first-class against ephemeral-cache alternatives for retrieval-latency and consistency-of-reference)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-122
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-13 "Key Decisions Made" + Pathway 04 as a stated content-location decision with explicit first-class-citizen framing.
    Current status: UNTESTED

ASSUMPTION-123:
  Date identified: 2026-05-13
  Statement: Whiteboard plots (Pathway 05) are ephemeral by default with a "Pin this" promotion-to-vault primitive and per-plot export buttons (PNG / SVG / HTML / CSV / PDF). The default-ephemeral / opt-in-persistence policy treats plot-output as a transient by-product of conversation unless explicitly promoted.
  Context: Cowork-to-chat summary 2026-05-13, "Key Decisions Made" pathway-doc decision (ii): "Whiteboard ephemerality: plots are ephemeral by default with 'Pin this' promotion to vault and per-plot export buttons (PNG / SVG / HTML / CSV / PDF)."
  Type: architectural / UX
  Related decisions: DECISION-029 (candidate — whiteboard ephemerality), Pathway 05 (Whiteboard), PRESUMPTION-156
  Testability: testable empirically (track pin-rate vs. plot-output-rate over N≥4 weeks of operation; audit whether ephemeral-by-default produces under-retention of valuable plots that the user later wishes to recover); testable via process (compare against an opposite-default ("persistent by default, swipe to discard") UX with the same primitives)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-123
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-13 "Key Decisions Made" + Pathway 05 as a stated UX-default decision with explicit promotion primitive.
    Current status: UNTESTED

ASSUMPTION-124:
  Date identified: 2026-05-13
  Statement: Generative-canvas (Pathway 06) library set is D3 + three.js + Plotly + bare canvas/WebGL. This enumeration is treated as the working library catalog the code-writing agent generates against for custom on-request visualization.
  Context: Cowork-to-chat summary 2026-05-13, "Key Decisions Made" pathway-doc decision (iii): "Generative-canvas library set: D3 + three.js + Plotly + bare canvas/WebGL." Pathway 06 frontmatter reinforces.
  Type: architectural / tooling
  Related decisions: DECISION-030 (candidate — generative-canvas library set), Pathway 06 (Generative Canvas), PRESUMPTION-157
  Testability: testable empirically (track gaps where the generative agent reaches outside the enumerated set during real demos; track library-substitution rate over N≥4 weeks); testable via literature (compare against Observable Plot, deck.gl, regl, vega-lite as omitted alternatives — what are their relative strengths for the generative-canvas use case?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-124
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-13 "Key Decisions Made" + Pathway 06 as a stated library-catalog decision.
    Current status: UNTESTED

ASSUMPTION-125:
  Date identified: 2026-05-13
  Statement: Unsaid-edges scoring (Pathway 07) uses two filters — how-often (frequency of mention) × how-important (weight of mention) — with the Low × High quadrant (rarely mentioned but important when mentioned) visually emphasized as the strongest research-program candidate. This is a normative scoring commitment baked into the visualization itself.
  Context: Cowork-to-chat summary 2026-05-13, "Key Decisions Made" pathway-doc decision (iv): "Unsaid-edges scoring: two filters (how-often × how-important); Low × High visually emphasized as the strongest research-program candidate."
  Type: methodological / architectural / normative
  Related decisions: DECISION-031 (candidate — unsaid-edges scoring), Pathway 07 (Unsaid Edges), PRESUMPTION-158
  Testability: testable empirically (pilot the Low × High emphasis on N≥4 known research-program-seed edges from the existing CROSS register; measure precision of "research-program candidate" judgment against subsequent program development); testable via literature (compare two-filter scoring against richer multi-attribute scoring in research-gap-detection systems)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-125
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-13 "Key Decisions Made" + Pathway 07 as a stated scoring-mechanism decision with explicit quadrant-emphasis.
    Current status: UNTESTED

ASSUMPTION-126:
  Date identified: 2026-05-13
  Statement: The seven-day evening cowork-to-chat delivery drought is broken — Tom signing into claude.ai in the Chrome profile paired with the extension cleared the proximal blocker. The fix is treated as durable enough to recharacterize the chat-scrape redesign discussion as proceeding from "working-channel framing" rather than "broken-channel framing," even though PRESUMPTION-134 substrate-decomposition remains load-bearing for the larger redesign question.
  Context: Cowork-to-chat summary 2026-05-13, opening delivery-status block: "DELIVERY STATUS: SUCCEEDED — first successful evening cowork-to-chat delivery in 7 days... The 7-day delivery drought is broken. This also clears the operational stagnation pattern that PREMISE-015's caveat had been accumulating against; PRESUMPTION-134 substrate-decomposition still load-bearing, but the chat-scrape redesign discussion can now proceed from working-channel rather than broken-channel framing."
  Type: operational / empirical
  Related decisions: ASSUMPTION-105 (user-privacy login prohibition), ASSUMPTION-118 (token-based delegation workflow redesign), PREMISE-015, PRESUMPTION-125 (cowork-to-chat sync failure cluster), PRESUMPTION-145 (chat-scrape framed as token-delegation), PRESUMPTION-159
  Testability: testable empirically (track evening-sync delivery success-rate over next N≥7 days post-fix; measure failure-mode rotation if sign-in lapses; compare against pre-fix 7-consecutive-failure baseline); testable via process (audit "working-channel framing" claim against the actual durability of the underlying sign-in state)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-126
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork-summary 2026-05-13 opening delivery-status block as an explicit claim about both the proximal fix and its framing-effect on the redesign discussion.
    Current status: UNTESTED

ASSUMPTION-127:
  Date identified: 2026-05-13
  Statement: Today's wiki agent daily run (C2A2 wiki daily run 2026-05-13) ingested 4 files producing +7 PRS triplets (Levin 24→29, Friston 14→16), +8 cross entries (CROSS-075..082), and +7 Pattern Detector findings (FINDING-025..031); the network state at EOD is 213 PRS / 86 cross / 33 findings. Three new HIGH-priority escalations were tagged today: FINDING-025 (SUTI = C2A2 detection function in microcosm), FINDING-029 (ideas-as-living-agents → traditions-as-cognitive-entities), and FINDING-030 (active-inference-as-OODA → first quantitative C2A2 detector via KL-divergence).
  Context: Wiki agent daily run report 2026-05-13: "Network: 213 PRS triplets · 86 cross-program connections · 33 active findings. HIGH escalations today: FINDING-025 (SUTI = C2A2 detection function in microcosm), FINDING-029 (ideas-as-living-agents → traditions-as-cognitive-entities), FINDING-030 (active-inference-as-OODA → first quantitative C2A2 detector via KL-divergence)."
  Type: empirical / operational / metrics
  Related decisions: DECISION-010 (Pattern Detector agent), ASSUMPTION-082 (3-layer RC Explorer), ASSUMPTION-115 (single-page consolidation framings), PRESUMPTION-160
  Testability: testable empirically (track HIGH-finding promotion rate to paradigm-shift candidates over N≥4 future runs; audit "first quantitative detector" claim by attempting to operationalize KL-divergence as a C2A2 detector); testable via literature (active-inference-OODA homology in computational neuroscience and management science)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-127
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from wiki agent daily run report 2026-05-13 as the canonical network-state delta + HIGH-escalation triple.
    Current status: UNTESTED

ASSUMPTION-128:
  Date identified: 2026-05-13
  Statement: FINDING-030 ("active-inference-as-OODA → first quantitative C2A2 detector via KL-divergence") represents the first quantitative C2A2 detection-function candidate — a methodological commitment that KL-divergence between an agent's active-inference distribution and an OODA-cycle decision distribution can operationalize the C2A2 "tradition acceleration" signal.
  Context: Wiki agent daily run report 2026-05-13, HIGH escalations list: "FINDING-030 (active-inference-as-OODA → first quantitative C2A2 detector via KL-divergence)." Reinforced in morning walk briefing references to FINDING-030 KL-divergence operationalization as a new task.
  Type: methodological / empirical
  Related decisions: FINDING-030 (Pattern Detector finding), DECISION-010 (Pattern Detector agent), ASSUMPTION-127, PRESUMPTION-161
  Testability: testable empirically (operationalize KL-divergence on a sample of existing PRS triplets in Levin / Friston traditions; measure whether the metric distinguishes "accelerating" from "non-accelerating" tradition pairs); testable via literature (active-inference / OODA homology validity in cross-discipline transfer; KL-divergence as a tradition-comparison metric)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-128
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from wiki agent daily run report 2026-05-13 HIGH escalations list + morning walk briefing operationalization task as a stated methodological-quantification claim.
    Current status: UNTESTED

ASSUMPTION-129:
  Date identified: 2026-05-13
  Statement: An alignment-agent scheduled task runs nightly to diff the ground-truth pathway directory (`architecture/`) against its vault mirror (`wiki/Architecture/`), copy ground-truth → mirror on drift, and flag the change in the next session archive. The pattern is explicitly described as parallel to the existing Summa `sync_vault.sh` + launchd job.
  Context: pathways.md preamble: "A scheduled alignment agent runs nightly, diffs the two locations, copies ground-truth → mirror on drift, and flags the change in the next session archive. Pattern parallels the existing Summa `sync_vault.sh` + launchd job." Plus dream-conversation session note (Task 8 remaining): "Stand up nightly alignment script (needs your input on schedule + launchd location; pattern parallels Summa `sync_vault.sh`)."
  Type: architectural / operational / tooling
  Related decisions: Pathway 00 (Broker — substrate framing), Task 8 (not-yet-scheduled), PRESUMPTION-162
  Testability: testable empirically (after the alignment-agent is stood up, track drift-detection rate vs. drift-introduction rate; audit "ground-truth → mirror" directionality against actual edit events to either location); testable via process (compare unidirectional sync against bidirectional merge with conflict-resolution)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-129
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from pathways.md preamble as the canonical alignment-agent protocol description.
    Current status: UNTESTED

ASSUMPTION-130:
  Date identified: 2026-05-13
  Statement: The honesty layer (Pathway 14) is a first-class architectural commitment: visible epistemic-status marks on every claim, not buried footers. This frames provenance-and-confidence as primary UI material rather than as audit-only metadata.
  Context: pathways.md inventory entry: "14 — Honesty layer — *outlined.* First-class visible epistemic-status marks on every claim, not buried footers." Reinforced in cowork-summary 2026-05-13 paragraph 1 enumeration: "a first-class honesty layer surfacing epistemic-status marks on every claim."
  Type: methodological / epistemic / architectural
  Related decisions: Pathway 14 (Honesty Layer), Provenance Protocol (ASSUMPTION vs PRESUMPTION marker), PRESUMPTION-163
  Testability: testable empirically (measure user-attention-on-epistemic-marks via gaze-tracking or click-through on disclosed-vs-buried provenance affordances; audit whether the honesty surface produces measurable user-behavior differences from the audit-only baseline); testable via literature (epistemic-marking visibility patterns in journalism, scientific publishing, and AI-output UI)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-130
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from pathways.md inventory entry + cowork-summary 2026-05-13 paragraph 1 as a stated UI-primacy claim about epistemic surfaces.
    Current status: UNTESTED

Key event (2026-05-13): Twelve new assumptions extracted on an architectural-pathway-discovery Wednesday whose primary structural event was the "dream conversation" between Tom and the Cowork agent (Sarah) — fourteen voice-dictated dispatch beats producing 17 pathway documents (00 Broker through 17 Agent as Developed Participant) plus a living index plus a 44 KB source-dialogue archive plus six in-pass decisions (2 operational + 4 pathway-doc) candidate for promotion to DECISION-026 through 031. The day also broke the 7-consecutive-day evening cowork-to-chat delivery drought (first SUCCEEDED delivery since 2026-05-05 after Tom signed into the paired Chrome profile), ran a clean wiki agent daily Phase 0-6 cycle (+7 PRS / +8 CROSS / +7 findings; 3 new HIGH escalations including FINDING-030 as the first quantitative C2A2 detector candidate via KL-divergence), and surfaced the architectural milestone framing: "the traditions of intellectual inquiry the project exists to accelerate include the tradition of its own becoming." Today's 12 new items cluster in four families. **(1) PATHWAY-INVENTORY MILESTONE cluster** — ASSUMPTION-119 (17-pathway inventory + 6-ISME-critical demo set as architectural milestone) is the day's structural-pattern anchor. **(2) PATHWAY-00-DERIVED OPERATIONAL DECISIONS cluster** — ASSUMPTION-120 (Cloudflare Workers broker hosting conditional on streaming-latency validation) and ASSUMPTION-121 (Twilio SMS one-tap signed link for external-escalation gating). These are the first operational-platform commitments since DECISION-012 (15c agent introduction). **(3) PATHWAY-DOC-DERIVED CONTENT-ARCHITECTURE DECISIONS cluster** — ASSUMPTION-122 (Perspectives in vault as first-class wiki citizens), ASSUMPTION-123 (whiteboard ephemerality + Pin-this promotion + per-plot export), ASSUMPTION-124 (D3 + three.js + Plotly + bare canvas/WebGL library set), ASSUMPTION-125 (unsaid-edges two-filter scoring with Low × High emphasis as research-program candidate). These four pathway-doc decisions are co-promoted as DECISION-028 through 031 candidates. **(4) OPERATIONAL-CHANNEL + NETWORK-DELTA + ALIGNMENT-AGENT + HONESTY-LAYER cluster** — ASSUMPTION-126 (7-day evening cowork-to-chat drought broken; PREMISE-015 stagnation pattern cleared at operational layer), ASSUMPTION-127 (wiki agent daily run network delta +7/+8/+7 with three new HIGH escalations), ASSUMPTION-128 (FINDING-030 KL-divergence as first quantitative C2A2 detector candidate), ASSUMPTION-129 (nightly alignment-agent protocol for ground-truth-to-vault-mirror sync paralleling Summa `sync_vault.sh`), ASSUMPTION-130 (honesty layer as first-class UI commitment rather than audit-only metadata). Pattern note: today's 12 assumptions are dominated by architectural/operational items (10 of 12: 119, 120, 121, 122, 123, 124, 126, 127, 129, 130) — inverting the methodological-heavy signature of operational-throughput days and producing the first architectural-discovery-day signature in the registry (no prior day has produced this many architectural-primitives commitments in a single run). The pathway-inventory + 7-day-drought-broken + KL-divergence-quantitative-detector + alignment-agent-protocol-articulation combination yields more *architectural-primitive-introduction* than *operational-principle-articulation* claims for the first time since 2026-04-20 (DECISION-023 caching-architecture day). Today's 18-to-12 presumption-to-assumption ratio (1.5:1) is on the prior ceiling — exceeded only by 2026-05-12's 1.67:1 joint-record. The architectural-discovery character generates a high density of design-choice presumptions (alternatives unconsidered; scoring-curve normatives unexamined; broker-as-substrate as the unstated common ground for multiple URGENT canonization triggers) at a rate that approaches but does not exceed yesterday's deferred-action-monitor + first-Hoffman-pending + Summa-shipping combination.

ASSUMPTION-131:
  Date identified: 2026-05-14
  Statement: Eight new pathway documents (18 Portability toolkit, 19 Optional interoperability, 20 Institutional scale, 21 Departmental integration, 22 Individual second brain, 23 Branching counterfactuals, 24 Meta-crafts governance, 25 Meta-visualization of pathways) emerged from this morning's walk and were drafted as full pathway markdown files by Cowork during the day. The pathway inventory extends from 17 to 25 across three new structure groups: Portability arc (18-22), Learning and governance (23-24), System self-reference (25).
  Context: pathways.md inventory entry (post-update): "Pathways 18–25 added from morning walk 2026-05-14 (Tom / Claude.ai chat, 'Morning planning walk'). Source dialogue: `morning_walk_2026-05-14.md`." Cowork evening-sync summary 2026-05-14: "8 new pathway documents drafted (`18_portability_toolkit.md` through `25_meta_visualization_pathways.md`), extending yesterday's 17-pathway inventory to 25 across three new structure groups (Portability arc, Learning and governance, System self-reference)."
  Type: architectural / structural / inventory
  Related decisions: ASSUMPTION-119 (17-pathway inventory milestone), DECISION-028..031 candidates (pathway-doc decisions), PRESUMPTION-168
  Testability: testable empirically (track how many of pathways 18-25 attract independent commits, file edits, or per-pathway DECISIONs over N≥4 weeks; measure whether the structure-group cuts predict cross-pathway dependency density); testable via process (compare 25-pathway extension cadence against 17-pathway inventory cadence)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-131
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from updated pathways.md inventory and Cowork evening-sync summary 2026-05-14 as the day's primary structural delta over yesterday's 17-pathway milestone.
    Current status: UNTESTED

ASSUMPTION-132:
  Date identified: 2026-05-14
  Statement: Toolkit / content separation (Pathway 18) is non-optional: "Without it the project remains a single demonstration rather than a methodology others can adopt. The 18 → 25 arc collapses if 18 fails." The framework/content seam must be clean enough to swap content without touching code — no hardcoded references to Aquinas, Levin, MacIntyre, or any specific thinker in the framework layer.
  Context: `18_portability_toolkit.md` Decisions section: "Toolkit separation is non-optional. Without it the project remains a single demonstration rather than a methodology others can adopt. The 18 → 25 arc collapses if 18 fails. Framework / content separation must be clean enough to swap content without touching code. No hardcoded references to Aquinas, Levin, MacIntyre, or any specific thinker in the framework layer. Configuration drives all substantive choices."
  Type: architectural / methodological
  Related decisions: Pathway 18 (Portability toolkit), Pathway 19/20/21/22 (downstream — depend on 18), PRESUMPTION-179
  Testability: testable empirically (attempt instantiation of a second, internal-only framework instance with different thinkers; track how many code-level edits are required vs. configuration-level edits — clean separation predicts a high ratio of config-edits to code-edits); testable via process (line-by-line audit of current repo to identify the framework/content seam)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-132
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from `18_portability_toolkit.md` Decisions section as the load-bearing architectural commitment of the entire portability arc.
    Current status: UNTESTED

ASSUMPTION-133:
  Date identified: 2026-05-14
  Statement: File-based handoff (signed JSON drops over HTTPS) is the primary wire format for inter-instance federation under Pathway 19 — per PRESUMPTION-145 as cited explicitly. Persistent OAuth-token-mediated APIs are demoted to a secondary or non-default option. The architectural commitment from Pathway 00 (broker as scope enforcer) extends to inter-instance queries: each request is a discrete, signed, scope-checked event.
  Context: `19_optional_interoperability.md`: "PRESUMPTION-145 (file-based handoff as simpler primary path) directly informs the wire-format choice here; the architecture should follow that lead rather than default to OAuth-token-mediated APIs." Decisions section: "File-based handoff is the primary wire format (per PRESUMPTION-145). Signed JSON drops over HTTPS are simpler, more inspectable, and less brittle than persistent OAuth-token-mediated APIs."
  Type: architectural / operational
  Related decisions: Pathway 19 (Optional interoperability), Pathway 00 (Broker), PRESUMPTION-145 (file-based handoff alternative), ASSUMPTION-118 (token-based delegation workflow redesign), PRESUMPTION-170
  Testability: testable empirically (after first inter-instance prototype, measure round-trip latency, error rate, and inspectability of file-based vs token-based handoffs); testable via literature (federation wire-format tradeoffs in distributed systems, scientific data exchange standards, ActivityPub)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-133
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from `19_optional_interoperability.md` Purpose and Decisions sections as the explicit cross-pathway design commitment extending PRESUMPTION-145 to federation.
    Current status: UNTESTED

ASSUMPTION-134:
  Date identified: 2026-05-14
  Statement: Federation under Pathway 19 defaults to OFF; "optionality is structural, not aspirational. An instance that simply runs and never federates is a fully legitimate use of the framework. Federation is an affordance, not an expectation." Selective sharing is per-topic, per-peer; not a binary public/private flag. Attribution is mandatory; silent absorption of peer material is a federation failure mode.
  Context: `19_optional_interoperability.md` Decisions section: "Optionality is structural, not aspirational. Federation defaults to off. An instance that simply runs and never federates is a fully legitimate use of the framework. Federation is an affordance, not an expectation." Plus: "Selective sharing is per-topic, per-peer. Not a binary public/private flag." Plus: "Attribution is mandatory. Peer material in local results always carries the peer's identity, honesty-layer markings, and source link. Federation that obscures provenance defeats the purpose."
  Type: architectural / normative / governance
  Related decisions: Pathway 19, Pathway 18 (precondition), Pathway 14 (honesty-layer markings carry across), PRESUMPTION-176, PRESUMPTION-182
  Testability: testable empirically (after federation prototype, measure default-off behavior under common configurations; audit any instance that federates without explicit opt-in as a defect); testable via literature (federation default-off precedents in academic networks, ActivityPub fediverse design)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-134
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from `19_optional_interoperability.md` Decisions section as the federation default-off + mandatory-attribution commitment.
    Current status: UNTESTED

ASSUMPTION-135:
  Date identified: 2026-05-14
  Statement: Pathway 24 commits to meta-crafts (governance, project management, conflict resolution, facilitation, evaluation) as first-class traditions in the perspective lattice, not as policy layers or operational scaffolding. Each meta-craft gets the same lattice treatment as substantive traditions — eager-tier overview, key thinkers, internal-debate map, apprenticeship trajectory, PRS framing. Connective rendering in the Sociogram makes the cross-cutting nature visible.
  Context: `24_meta_crafts_governance.md` Decisions section: "Meta-crafts are first-class traditions, not policy layers. Governance, project management, conflict resolution, facilitation, evaluation get the same lattice treatment as substantive traditions. They are not subordinate." Plus: "Connective rendering in the Sociogram. Visually distinct overlay, edges to every substantive tradition." Plus: "Operational integration is non-optional. The system's own governance is held to the same standards it asks substantive traditions to meet."
  Type: architectural / methodological / normative
  Related decisions: Pathway 24 (Meta-crafts), Pathway 04 (Perspective lattice), Pathway 17 (Agent participant — accountability to meta-craft community), PRESUMPTION-171, PRESUMPTION-181
  Testability: testable empirically (after Pathway 24 prototype, audit whether registering governance as a perspective-lattice tradition produces different system behavior than treating it as a policy layer); testable via literature (MacIntyre's tradition-constituted-inquiry treatment of governance; tradition-of-practices vs. craft-as-substantive-domain in After Virtue and Three Rival Versions of Moral Enquiry)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-135
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from `24_meta_crafts_governance.md` Decisions section as the central architectural commitment elevating meta-crafts to first-class tradition status.
    Current status: UNTESTED

ASSUMPTION-136:
  Date identified: 2026-05-14
  Statement: Pathway 25 (Meta-visualization of pathways) commits to the agent as "co-explorer, not oracle. Pathway 25 is where Pathway 17's continuity-of-character is most visible. The agent thinks alongside the user, dwells on the question, draws on prior conversations. Query-response is the wrong mode." The visualization is co-authored — both user and agent annotate; the agent's annotations carry honesty-layer markings; counterfactual integration (Pathway 23) is structural, not optional.
  Context: `25_meta_visualization_pathways.md` Decisions section: "The agent is a co-explorer, not an oracle. Pathway 25 is where Pathway 17's continuity-of-character is most visible. The agent thinks alongside the user, dwells on the question, draws on prior conversations. Query-response is the wrong mode." Plus: "Annotation is co-authored. Both user and agent annotate." Plus: "Counterfactual integration is structural, not optional."
  Type: architectural / methodological / UX
  Related decisions: Pathway 25, Pathway 17 (Agent as developed participant), Pathway 14 (Honesty layer), Pathway 23 (Branching counterfactuals), PRESUMPTION-172, PRESUMPTION-180
  Testability: testable empirically (after Pathway 25 prototype, instrument user-session traces for query-response-mode vs co-exploration-mode preference distributions; measure agent-revision-rate in conversations about pathways); testable via literature (co-creative AI interface design; conversational-agent oracle-vs-collaborator framing in HCI)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-136
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from `25_meta_visualization_pathways.md` Decisions section as the central UX-and-architectural commitment for the meta-visualization pathway.
    Current status: UNTESTED

ASSUMPTION-137:
  Date identified: 2026-05-14
  Statement: Pathway 13 (Under-Development Visualizer) is architecturally distinct from Pathway 25 (Meta-Visualization of Pathways) — different audiences (GitHub contributors vs intellectual co-explorers), different data substrates (commits / PRs / contributors vs pathway dependency / annotation / counterfactual branches), same project. Drafted decision is "distinct" rather than "merged."
  Context: `25_meta_visualization_pathways.md` Purpose section: "The architectural distinction from Pathway 13 (Under-Development Visualizer) is real: 13 is for GitHub contributors and shows code-level development; 25 is for intellectual co-exploration of the pathway space itself." Plus Open Questions: "Is this the same as Pathway 13 (Under-Development Visualizer) or distinct? (Drafted decision: distinct. Pathway 13 is for GitHub contributors; Pathway 25 is for intellectual co-exploration with the agent.)"
  Type: architectural / scoping
  Related decisions: Pathway 13, Pathway 25, PRESUMPTION-168 (8-pathway enumeration)
  Testability: testable empirically (after both pathways prototype, measure user-population overlap; if substantially same users use both, the distinct-pathway claim is weakened); testable via process (audit whether the data substrates and UX affordances actually diverge as predicted or converge in practice)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-137
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from `25_meta_visualization_pathways.md` Purpose + Open Questions as the drafted distinct-pathway scoping commitment between Pathway 13 and Pathway 25.
    Current status: UNTESTED

ASSUMPTION-138:
  Date identified: 2026-05-14
  Statement: Pathways 18-25 are a "deliberate post-ISME breadth arc, not demo-path advancement" — explicitly NOT on the ISME July 8-10, 2026 critical path. This frames today's drafting work as an allocation choice during the 8-week runway: post-ISME breadth was prioritized over additional ISME-critical-pathway work today.
  Context: Cowork evening-sync summary 2026-05-14 morning-walk briefing: "pathways 18–25 are a deliberate post-ISME breadth arc, not demo-path advancement — allocation question for the 8-week runway." Also confirmed in `18_portability_toolkit.md` frontmatter (`isme_critical: no`) through `25_meta_visualization_pathways.md` frontmatter (`isme_critical: no`).
  Type: methodological / strategic / scheduling
  Related decisions: ASSUMPTION-119 (6 ISME-critical pathways from yesterday — unchanged today), PRESUMPTION-173, PRESUMPTION-178
  Testability: testable empirically (track during the 8-week runway whether pathway-18-25 work continues at today's cadence or recedes as ISME-critical pathways accelerate; measure attention-share via commit timestamps and pathway-doc edit timestamps over the next 8 weeks); testable via process (compare post-ISME-breadth vs ISME-critical-path commitment ratios in subsequent days against the explicit "deliberate breadth arc" framing)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-138
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Cowork evening-sync summary 2026-05-14 "For tomorrow's walk" flag #1 and pathway-doc frontmatter as the explicit post-ISME-breadth allocation claim.
    Current status: UNTESTED

ASSUMPTION-139:
  Date identified: 2026-05-14
  Statement: Documentation carries the rationality standards (Pathway 18): the onboarding documentation is not just a technical guide — it invites adopters into MacIntyrean tradition-constituted inquiry as the system's normative shape. "Adopting the framework without engaging the rationality standards produces a different (and weaker) instance." The framework's normative commitments (honesty layer, PRS, perspective lattice) come bundled with the toolkit, not as opt-in afterthoughts.
  Context: `18_portability_toolkit.md` Decisions section: "Documentation carries the rationality standards. Not just a technical guide — the onboarding documentation invites adopters into MacIntyrean tradition-constituted inquiry as the system's normative shape. Adopting the framework without engaging the rationality standards produces a different (and weaker) instance."
  Type: methodological / normative / pedagogical
  Related decisions: Pathway 18, Pathway 14 (Honesty layer), Pathway 04 (Perspective lattice), PRESUMPTION-179, PRESUMPTION-182
  Testability: testable empirically (after toolkit release, audit adopter-instances for honesty-layer presence and PRS-framework use; measure whether instances that skip the documentation produce measurably weaker outputs); testable via literature (normative-content-in-software-toolkits patterns in pedagogy and FLOSS communities)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-139
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from `18_portability_toolkit.md` Decisions section as the documentation-as-normative-vehicle commitment.
    Current status: UNTESTED

ASSUMPTION-140:
  Date identified: 2026-05-14
  Statement: Morning chat-scrape succeeded for the second consecutive day; the sign-in fix from 2026-05-13 is holding. The previous 7-consecutive-day failure pattern (2026-05-05 through 2026-05-12) has cleared at the operational layer. Two data points (today + yesterday) are not yet a stable pattern, but the trajectory is consistent with sustained success.
  Context: Cowork evening-sync summary 2026-05-14: "Morning chat-scrape succeeded for the second consecutive day — sign-in fix from 2026-05-13 is holding." Plus morning chat-scrape session local_995d8b5d: "The scrape succeeded for the first time in 9 days — the sign-in barrier flagged on 2026-05-05/09/10/13 has cleared."
  Type: operational / empirical
  Related decisions: ASSUMPTION-126 (yesterday's drought-broken claim), PRESUMPTION-159 (sign-in fix framed as architectural fix), PRESUMPTION-177
  Testability: testable empirically (track morning chat-scrape success/failure for N≥5 more consecutive days; if streak continues, ASSUMPTION-126/140 pattern stabilizes; if any single failure, the "sign-in fix holding" claim weakens and PRESUMPTION-159 re-fires); testable via process (audit which proximal failure modes the sign-in fix actually addresses vs. which it only masks)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-140
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Cowork evening-sync summary 2026-05-14 + morning chat-scrape session local_995d8b5d as the second consecutive on-cadence success following yesterday's drought-breaking event.
    Current status: UNTESTED

ASSUMPTION-141:
  Date identified: 2026-05-14
  Statement: Evening cowork-to-chat browser delivery FAILED today — Chrome MCP extension is offline (paired Chrome profile not signed in or extension not connected). The summary file was written with a visible failure flag in the header rather than silently delivered. The degraded-mode protocol is: write the .md file with visible failure flag, await user remediation, do not attempt automatic recovery.
  Context: Cowork evening-sync session local_6c8ab387: "Chrome MCP extension is not connected, so browser delivery to Chat is not possible. Updating the summary file header to flag this for Tom." Plus: "Browser delivery: SKIPPED. Claude-in-Chrome reported no connected browsers — the paired Chrome extension is offline. The summary header now carries a visible failure flag so it's not silent."
  Type: operational / empirical / failure-mode
  Related decisions: ASSUMPTION-126 (yesterday's drought-broken), ASSUMPTION-140 (chat-scrape side success), PRESUMPTION-159 (sign-in fix framing), PRESUMPTION-177
  Testability: testable empirically (track frequency of Chrome-MCP-extension-offline failures over next N≥7 days; audit whether the same proximal cause that took 7 days to fix last time recurs and at what cadence); testable via process (compare visible-failure-flag protocol against silent-skip baseline for user remediation response time)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-141
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Cowork evening-sync session local_6c8ab387 final assistant message as the explicit degraded-mode protocol invocation.
    Current status: UNTESTED

ASSUMPTION-142:
  Date identified: 2026-05-14
  Statement: A 27 KB integrative paper (`2026-05-14_carpathi_wiki_paper.md`) and two verbatim Chat-Claude review files (`2026-05-14_pathways_18-25_review.md`, `2026-05-14_comprehensive_overview_review.md`) were written today alongside the 8 new pathway docs. The architecture/ directory accumulates per-day reference documents (paper + reviews + walk archive) alongside the pathway-doc and per-day-changelog cadence — a parallel content stream not subject to the architecture/decisions.md canonization gate.
  Context: Architecture directory listing shows files created today: `2026-05-14_carpathi_wiki_paper.md` (27,613 bytes), `2026-05-14_comprehensive_overview_review.md` (5,130 bytes), `2026-05-14_pathways_18-25_review.md` (2,924 bytes), `morning_walk_2026-05-14.md` (7,727 bytes). Cowork evening-sync summary: "Two Chat-Claude verbatim review files preserved (`2026-05-14_pathways_18-25_review.md`, `2026-05-14_comprehensive_overview_review.md`) plus the walk transcript archive (`morning_walk_2026-05-14.md`) and a 27 KB integrative paper."
  Type: operational / content-architecture / governance
  Related decisions: ASSUMPTION-131 (8 new pathways), DECISION-028..031 candidates, PRESUMPTION-175, PRESUMPTION-176
  Testability: testable empirically (audit growth rate of architecture/ root-level per-day reference docs vs. growth rate of canonized decisions/pathways over next N≥4 weeks; measure whether parallel content stream produces functional artifacts or accumulates as low-attention residue); testable via process (compare the canonization-gate-bypass pattern of per-day reference docs with PRESUMPTION-041 implicit-decision drift)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-142
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from architecture directory listing + Cowork evening-sync summary as the parallel content stream alongside pathway docs.
    Current status: UNTESTED

ASSUMPTION-143:
  Date identified: 2026-05-14
  Statement: Agent 16 (deferred-action monitor) finalized WATCH-001 bookkeeping cleanup today; 3 new pending proposals staged (2 Fredrickson, 1 Stump). The active watch list remains at 0 with the cleanup pass complete; the deferred-action layer remains operational but with no active items pending.
  Context: Cowork evening-sync summary 2026-05-14: "Agent 16 finalized WATCH-001 bookkeeping cleanup; 3 new pending proposals staged (2 Fredrickson, 1 Stump)." Continues prior pipeline state from 2026-05-13 metrics snapshot.
  Type: operational / empirical
  Related decisions: DECISION-016 (Agent 16 introduction), PRESUMPTION-140 (intake-coverage audit gap — unchanged)
  Testability: testable empirically (track Agent 16 active-watch-list utilization over N≥4 weeks; audit whether new intake actually exercises the deferred-action machinery or whether the watch list remains at 0 baseline); testable via process (compare new-pending-proposal cadence — 2 Fredrickson + 1 Stump today — against weekly intake distribution patterns)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-143
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Cowork evening-sync summary 2026-05-14 Pipeline state bullet as the Agent 16 + new-pending-proposal status delta.
    Current status: UNTESTED

ASSUMPTION-144:
  Date identified: 2026-05-14
  Statement: Today's 14a/14b run was NOT visible in changelog at evening-sync write-time: "today's 14a/14b EOD fire not yet visible in changelog at sync time." The evening-sync runs before the 14a/14b run; the 14a/14b run produces today's changelog after the evening-sync writes its summary. This is by design — evening-sync precedes self-awareness fire — but it means the evening-sync summary cannot reference today's 14a/14b outputs.
  Context: Cowork evening-sync summary 2026-05-14: "today's 14a/14b EOD fire not yet visible in changelog at sync time."
  Type: operational / scheduling / governance
  Related decisions: 14a/14b cadence, ASSUMPTION-117 (skipped-EOD-slot pattern — broken yesterday at on-cadence fire)
  Testability: testable empirically (audit whether downstream readers of the evening-sync summary mis-interpret the absence of today's 14a/14b output as a skipped run; measure friction in next-morning briefing assembly when 14a/14b changelog lags behind evening-sync summary); testable via process (compare sequential evening-sync → 14a/14b vs. parallel evening-sync ∥ 14a/14b cadences for downstream-readability tradeoffs)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-144
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Cowork evening-sync summary 2026-05-14 as an explicit cadence-ordering claim about the evening-sync / 14a/14b sequence.
    Current status: UNTESTED

ASSUMPTION-145:
  Date identified: 2026-05-15
  Statement: Pathway 26 (Research Suggestions per Thinker) is the project's outbound channel to the 15 thinkers — the system "develops and is prepared to communicate concrete research suggestions, together with rationale" to each of Levin, Friston, Hoffman, Kastrup, McGilchrist, Hawkins, Wolfram, Carroll, Arkani-Hamed, Fredrickson, Stump, Rohr, Wright, MacIntyre, Loughran. The pathway exists "because the project's claim to be an accelerator/detector system for developing communities into sustained and articulate traditions is hollow if the system has no productive output back to the thinkers whose traditions it has been articulating." Pathway 26 is positioned as the analogous outbound channel to Pathways 11–13 (episode publishing, community outreach, under-development view) but addressed to the thinkers themselves.
  Context: `architecture/26_research_suggestions_per_thinker.md` Purpose section (created 2026-05-15, status: outlined). Originating prompt from Tom: "Dev Pathway 26 (or so): Develop and communicate research suggestions for each thinker, together with rationale." Framing constraint: "All I want for Dev Pathway 26 is an md file conformal to the full pathway set."
  Type: architectural / methodological / strategic
  Related decisions: ASSUMPTION-119 (17-pathway inventory — now 26), Pathway 11 (episode publishing), Pathway 12 (community outreach), Pathway 13 (under-development view), Pathway 14 (honesty layer), Pathway 15 (apprentice mode), Pathway 17 (agent-developed participant), PRESUMPTION-183, PRESUMPTION-186, PRESUMPTION-192
  Testability: testable empirically (after dossier drafting, measure suggestion-uptake / response rate from thinkers approached; audit whether suggestions read as continuity-with-program vs unsolicited-reframe via thinker feedback); testable via literature (outbound-research-recommendation patterns in inter-disciplinary collaboration; meta-scientific advisory roles)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-145
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from `26_research_suggestions_per_thinker.md` Purpose section as the project's first explicit outbound-to-thinkers commitment. Direct quote from Pathway 26 Purpose used as the rationale anchor.
    Current status: UNTESTED

ASSUMPTION-146:
  Date identified: 2026-05-15
  Statement: Naming convention is now on record (from morning-walk Chat-Claude session, captured in chat_summary 2026-05-15): the *Carpathi Wiki* is the general approach / methodology; the *Resurrecting Civility (RC) Carpathi Wiki* is the file-name of this particular instantiation; the public name of the same thing is the **C2A2 Wiki**; its visualization tool is the **C2A2 Explorer**. Tom established the four-name taxonomy for the chat record. Tom flagged uncertainty about whether the naming would persist across chat sessions unless they were working in a chat-project context — a workflow concern Cowork should note.
  Context: Chat summary 2026-05-15 morning walk: "Tom established for the chat record: the Carpathi Wiki is the general approach/methodology; the Resurrecting Civility (RC) Carpathi Wiki is the file-name of this particular instantiation; the public name of the same thing is the C2A2 Wiki, and its visualization tool is the C2A2 Explorer."
  Type: architectural / naming / governance
  Related decisions: All pathway-doc / vault-organization decisions, PRESUMPTION-188
  Testability: testable empirically (audit usage of all four terms across the vault for consistency / drift over N≥4 weeks; measure whether any of the four terms get mixed up downstream); testable via process (compare the four-name taxonomy against Tom's flagged persistence-concern across non-project Chat sessions)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-146
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from chat_summary 2026-05-15 as a Tom-on-record clarification of the four-name taxonomy with workflow caveat.
    Current status: UNTESTED

ASSUMPTION-147:
  Date identified: 2026-05-15
  Statement: Pathway 26 commits to one file per thinker (mirroring the `wiki/traditions/{thinker}/` structure) — "not a single monolithic document. This makes dossiers maintainable independently and lets each thinker's dossier evolve as their own work and the project's understanding does." Each dossier lands as `wiki/traditions/{thinker}/research_suggestions.md` alongside the tradition wiki itself, with a parallel cross-thinker network view ("a map of which suggestions implicate which other thinkers").
  Context: `26_research_suggestions_per_thinker.md` Decisions taken section: "One file per thinker, mirroring the tradition wiki structure. Not a single monolithic document." Function set #1 (per-thinker dossier) and #2 (cross-thinker network view).
  Type: architectural / data-model
  Related decisions: ASSUMPTION-145 (Pathway 26 opening), tradition wiki structure, PRESUMPTION-193
  Testability: testable empirically (track maintenance cadence per-thinker dossier vs monolithic-document alternative if a sample is drafted both ways); testable via process (compare the per-thinker file structure against the monolithic-document alternative for editor friction and update-cadence)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-147
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from `26_research_suggestions_per_thinker.md` Decisions taken first bullet as the explicit per-thinker file-structure commitment.
    Current status: UNTESTED

ASSUMPTION-148:
  Date identified: 2026-05-15
  Statement: Each suggestion in Pathway 26 carries an explicit two-faced rationale — *continuity with the thinker's existing program* (so the suggestion reads as a natural extension, not an unsolicited reframe) and *unlocked-value for the C2A2 network* (what cross-tradition synthesis the suggestion would enable). The two faces are equally weighted; "the project does not subordinate the thinker's research interests to its own synthesis aims." This is the substantive shape of how a suggestion gets to count as a suggestion at all.
  Context: `26_research_suggestions_per_thinker.md` Function set #3 (Rationale layer) and Decisions taken #2: "Continuity + unlocked-value as a two-faced rationale. Suggestions are framed to be productive from the thinker's existing program as much as for the C2A2 synthesis. The pathway does not subordinate the thinker's research interests to the project's."
  Type: methodological / normative / epistemic
  Related decisions: ASSUMPTION-145, ASSUMPTION-149 (soft thinker-voice convention), Pathway 14 (honesty layer), PRESUMPTION-184, PRESUMPTION-186
  Testability: testable empirically (after dossier-drafting, audit per-suggestion: does the rationale articulate both faces in roughly equal proportion? do thinker readers identify the continuity face as accurate?); testable via process (compare equally-weighted vs project-prioritized rationale framings for suggestion-uptake rates)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-148
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Pathway 26 Function set #3 + Decisions taken #2 as the explicit two-faced equal-weighting commitment with anti-subordination clause.
    Current status: UNTESTED

ASSUMPTION-149:
  Date identified: 2026-05-15
  Statement: The soft thinker-voice convention (criterion M) — established earlier in the same Cowork session in the context of Summa 2026 QC work — applies to Pathway 26: the dossiers cite the thinker's work as a resource without classifying the thinker into hard role-categories ("X is THE authority on Y"). "The same principle that governs the Summa 2026 synthesis prose governs the research-suggestions dossiers." Pathway 26 emerged immediately after the criterion M work as its natural complement.
  Context: `26_research_suggestions_per_thinker.md` Decisions taken #4: "Soft thinker-voice convention applies (M criterion). Per `summa_thinker_voice_convention.md`, the dossiers cite the thinker's work as a resource; they do not classify the thinker into hard role-categories." Provenance section: "The pathway emerged immediately after the criterion M work… having done the work of receiving each tradition carefully, the project now has something productive to send back."
  Type: methodological / normative / pedagogical
  Related decisions: ASSUMPTION-148 (two-faced rationale), summa_thinker_voice_convention.md (criterion M), PRESUMPTION-184
  Testability: testable empirically (audit dossier prose for hard role-classifications across the 15 thinkers; measure whether the soft convention holds at scale); testable via process (compare soft-convention vs hard-classification drafts for thinker-feedback tone)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-149
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from `26_research_suggestions_per_thinker.md` Decisions taken #4 and Provenance section as the criterion-M-applies-to-Pathway-26 transfer commitment.
    Current status: UNTESTED

ASSUMPTION-150:
  Date identified: 2026-05-15
  Statement: Three INCORPORATEs landed today in the 15c dispositioning pass — PREMISE-016 (toolkit/content separation, from ASSUMPTION-132); PREMISE-017 (federation default-OFF, from ASSUMPTION-134); PREMISE-018 (meta-crafts first-class, from ASSUMPTION-135). This is "the first non-trivial PREMISE batch in weeks" — the PREMISE register grew from 15 to 18; second consecutive non-zero INCORPORATE cycle. Three of the four candidate DECISIONs from yesterday (DECISION-032/033/034) now have INCORPORATEd PREMISE backing, materially strengthening their canonization case.
  Context: Cowork evening-sync summary 2026-05-15: "three new INCORPORATEs — the first non-trivial PREMISE batch in weeks — validating yesterday's load-bearing breadth-arc commitments (toolkit/content separation, federation default-OFF, meta-crafts first-class). PREMISE register grew from 15 to 18." Validated_premises.md cycle-level observation: "the 2026-05-15 cycle produced 3 INCORPORATEs."
  Type: operational / empirical / pipeline
  Related decisions: DECISION-032 candidate (toolkit/content separation), DECISION-033 candidate (federation default-OFF), DECISION-034 candidate (meta-crafts first-class), ASSUMPTION-132, ASSUMPTION-134, ASSUMPTION-135, PRESUMPTION-195
  Testability: testable empirically (track DECISION-032/033/034 canonization timing against the PREMISE-backing; measure whether PREMISE-backed candidate DECISIONs are canonized faster than non-PREMISE-backed candidates); testable via process (audit whether the INCORPORATE-as-canonization-strengthening pattern holds across additional cycles)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-150
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Cowork evening-sync summary 2026-05-15 + validated_premises.md cycle-level observation as the three-INCORPORATE batch event.
    Current status: UNTESTED

ASSUMPTION-151:
  Date identified: 2026-05-15
  Statement: Pre-implementation architectural-articulation passes are substantially more INCORPORATE-likely than operational-incident passes — the combined 14+15 cycle rate is now 7/59 ≈ 11.9%, "well above prior baseline." The 2026-05-14 and 2026-05-15 cycles together contribute 7 of the 8 INCORPORATEs in the six-cycle window (2026-05-09 / 10 / 11 / 13 / 14 / 15); both cycles were driven by architectural-articulation passes (17-pathway pass on 05-13 EOD; breadth-arc 18-25 pass on 05-14 EOD). The pattern that pre-implementation architectural articulation is more INCORPORATE-likely than operational-incident analysis "is now confirmed across two cycles."
  Context: Cowork evening-sync summary 2026-05-15. Validated_premises.md cycle-level observation: "The pattern that pre-implementation architectural articulation passes are more INCORPORATE-likely than operational-incident passes is now confirmed across two cycles."
  Type: methodological / empirical / pipeline-rate
  Related decisions: ASSUMPTION-150 (today's three INCORPORATEs), PRESUMPTION-195 (cycle-specific small-N caveat)
  Testability: testable empirically (track INCORPORATE rate per cycle over the next N≥6 cycles, broken down by cycle-type architectural-articulation vs operational-incident; if the differential persists, the pattern stabilizes as a process insight); testable via process (audit which architectural-articulation features predict INCORPORATE likelihood — claim density, scope, level of generality)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-151
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Cowork evening-sync summary 2026-05-15 + validated_premises.md cycle-level observation as the architectural-articulation-vs-operational-incident INCORPORATE-rate differential claim.
    Current status: UNTESTED

ASSUMPTION-152:
  Date identified: 2026-05-15
  Statement: Morning chat-scrape succeeded for the third consecutive day; the sign-in fix from 2026-05-13 is now holding across three data points (05-13, 05-14, 05-15). The trajectory moves "from 'two data points, not yet a stable pattern' toward credible stability." If tomorrow's scrape also succeeds, four data points across four days starts to support the architectural-fix-via-credential framing rather than the architectural-fragility framing. PRESUMPTION-159's "credential-vs-architectural" question weakens with each successful day.
  Context: Cowork evening-sync summary 2026-05-15: "Morning chat-scrape succeeded for the third consecutive day (sign-in fix from 2026-05-13 now holding across three data points — moving from 'two data points, not yet a stable pattern' toward credible stability)." Morning chat-scrape session local_c78d3054 successful execution.
  Type: operational / empirical / pattern-stability
  Related decisions: ASSUMPTION-126 (drought-broken claim), ASSUMPTION-140 (second consecutive success), PRESUMPTION-159 (sign-in fix framing), PRESUMPTION-177 (Chrome-MCP recurrence pattern)
  Testability: testable empirically (track morning chat-scrape success/failure for N≥4 more consecutive days; if streak continues at N≥7 the credential-fix-holding claim approaches stable-pattern status); testable via process (audit which proximal failure modes the sign-in fix actually addresses vs masks)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-152
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Cowork evening-sync summary 2026-05-15 + morning chat-scrape session local_c78d3054 as the third consecutive on-cadence success.
    Current status: UNTESTED

ASSUMPTION-153:
  Date identified: 2026-05-15
  Statement: Wiki narration visualization was regenerated twice today — once for a Summa flag pass (backup `wiki_narration.html.bak.20260515-pre-summa-flag` at 19:27 UTC) and once for a Q1 regen (backup `wiki_narration.html.bak.20260515-pre-q1-regen` at 20:24 UTC). The narration HTML is now ~15.3 MB. A `summa_explorer.html` update at 19:45 UTC sits between the two regens. The label "pre-q1-regen" implies a known Q1-ish change being made to the visualization.
  Context: Cowork evening-sync summary 2026-05-15 "Files Created or Modified" section: `wiki_narration.html.bak.20260515-pre-summa-flag` (19:27 UTC), `wiki_narration.html.bak.20260515-pre-q1-regen` (20:24 UTC), `wiki_narration.html` (20:24 UTC, ~15.3 MB), `summa_explorer.html` (19:45 UTC).
  Type: operational / content-architecture
  Related decisions: Wiki narration visualization pipeline (per CLAUDE.md), Summa-side content stream (ASSUMPTION-154 today's parallel), PRESUMPTION-189
  Testability: testable empirically (audit the diff between `pre-summa-flag` and `pre-q1-regen` backups to identify what Q1 refers to and what was changed in each pass); testable via process (compare the file-size growth across regens against the validation pipeline's tracked metrics)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-153
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Cowork evening-sync summary 2026-05-15 Files Created or Modified section as the two-backup-step visualization regen sequence.
    Current status: UNTESTED

ASSUMPTION-154:
  Date identified: 2026-05-15
  Statement: Substantial Summa parallel content stream today — 30 Summa Day-NN transcripts touched (Days 7, 8, 35, 61–65, 73–75, 82–100 spanning the second-volume / virtues / sins arc) by the Summa commentary reviewer + Summa qc sweep + Summa 2026 daily batch sessions. Combined with today's visualization regen + summa_explorer.html update, today shows that the Summa-side work has its own daily cadence that isn't reflected in the C2A2 architecture register. The C2A2 / Summa boundary is the principle; today is a high-volume Summa-side day that potentially accumulates decisions outside the canonical decision register.
  Context: Cowork evening-sync summary 2026-05-15: "30 Summa Day-NN transcripts touched (Days 7, 8, 35, 61–65, 73–75, 82–100 spanning the second-volume / virtues / sins arc) by the Summa commentary reviewer + Summa qc sweep + Summa 2026 daily batch sessions." Session list shows multiple concurrent Summa sessions: "Summa 2026 nightly verification" (running), "Summa commentary reviewer" (running), "Summa qc sweep" (idle), plus prior "Summa commentary reviewer" / "Summa qc sweep" sessions.
  Type: operational / content-architecture / governance
  Related decisions: C2A2/Summa boundary principle, ASSUMPTION-142 (parallel content stream pattern from 2026-05-14), PRESUMPTION-189 (Q1 referent ambiguity)
  Testability: testable empirically (audit Summa-side decisions accumulating per week against canonical-decision-register entries; measure whether Summa-side decisions surface in C2A2 architectural register at any cadence); testable via process (compare boundary-functional vs boundary-leaking patterns across the next N≥4 weeks)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-154
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Cowork evening-sync summary 2026-05-15 Files Modified Summa section + active session list as the Summa-side parallel-cadence event.
    Current status: UNTESTED

ASSUMPTION-155:
  Date identified: 2026-05-15
  Statement: Substrate-decomposition gate entered its fourth consecutive cycle without closure today — PRESUMPTION-134 REVISE 2026-05-11; PRESUMPTION-159 REVISE 2026-05-14; PRESUMPTION-177 REVISE 2026-05-15 (today). It is "the strongest unresolved-cluster signal in the entire system." Each cycle adds another REVISE entry (134 → 159 → 177) without closure. The recommended action sequence (enumerate Chrome-MCP dependency surface; classify recent failures credential-vs-architectural; identify fall-back paths; reframe degraded-mode protocol output to stop pre-classifying failures as credential before evidence) is in `revision_flags.md`. Joint with Pathway 14 honesty-layer commitment (PREMISE-019). ISME demo-readiness load-bearing.
  Context: Cowork evening-sync summary 2026-05-15: "Substrate-decomposition gate: fourth consecutive cycle without closure (PRESUMPTION-134 REVISE 2026-05-11; PRESUMPTION-159 REVISE 2026-05-14; PRESUMPTION-177 REVISE 2026-05-15) — strongest unresolved-cluster signal in the system, HIGH urgency for Tom's review." Same source: "the honesty-layer commitment in PREMISE-019 (Pathway 14) requires accurate failure classification; continuing to pre-classify Chrome-MCP recurrences as 'likely credential' without evidence is a quiet violation of that commitment."
  Type: operational / architectural / methodological / failure-mode
  Related decisions: PRESUMPTION-134 (origin), PRESUMPTION-159 (sign-in fix framing), PRESUMPTION-177 (Chrome-MCP recurrence), Pathway 14 (honesty layer / PREMISE-019), ASSUMPTION-141, PRESUMPTION-190
  Testability: testable empirically (execute the recommended action sequence and measure whether it closes the gate; track whether Chrome-MCP-offline pattern continues to recur after the audit); testable via process (audit the four-cycle non-closure pattern itself — what makes this gate persist across cycles when other gates close)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-155
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Cowork evening-sync summary 2026-05-15 + revision_flags.md fourth-cycle entry as the substrate-decomposition-gate-fourth-cycle event.
    Current status: UNTESTED

ASSUMPTION-156:
  Date identified: 2026-05-15
  Statement: Pathway 26's calibration-sample plan is "one thinker first, reviewed before the others." Three candidates are noted in the pathway-doc open questions: Stump (the thinker-voice work is freshest), Friston (most-cited in the formal-architecture syntheses), or Wright (the scriptural-historical pole). "A reasonable choice is one thinker from each substantive cluster (formal / metaphysical / theological / experimental) as initial calibration." The choice is deferred to the late-next-week prioritization discussion.
  Context: `26_research_suggestions_per_thinker.md` Open questions section "Sequencing across the 15." Status section: "Calibration-sample drafting (one thinker first, reviewed before the others) is the obvious first concrete step. Three candidates for the calibration sample are noted in the open questions; choice deferred. No dossiers exist yet."
  Type: methodological / scheduling / strategic
  Related decisions: ASSUMPTION-145 (Pathway 26 opening), PRESUMPTION-191 (Wright/Rohr pendings blocking N=13)
  Testability: testable empirically (after calibration draft, audit whether the single-thinker-first approach surfaces issues that scale to all 15, or whether the 15 require sufficiently distinct treatment that one-thinker-first is uninformative); testable via process (compare one-thinker-calibration vs cross-thinker-sample-of-3 protocols)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-156
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from `26_research_suggestions_per_thinker.md` Open questions + Status as the calibration-sample-first-then-others commitment.
    Current status: UNTESTED

ASSUMPTION-157:
  Date identified: 2026-05-15
  Statement: A new pending proposal was staged today: `inbox/proposals/pending/2026-05-15_carroll_mindscape-353-roth-moral-economics.md`. This extends the pending proposals count by +1 (was ~43 yesterday, now ~44). The new proposal is in the Carroll tradition arc, referencing Mindscape episode 353 with Roth on moral economics. Five Wright/Rohr first-evers from 2026-05-10 still block N=13 expansion (per ASSUMPTION-111); today's Carroll proposal is in the existing N=11 set, not the pending N=13.
  Context: Cowork evening-sync summary 2026-05-15 Files Created section: "`inbox/proposals/pending/2026-05-15_carroll_mindscape-353-roth-moral-economics.md` — NEW pending proposal." Pipeline status: "Pending proposals: ~44 (was 43; +1 today: Carroll Mindscape 353 — Roth moral economics)."
  Type: operational / empirical / intake
  Related decisions: ASSUMPTION-143 (Agent 16 + new pendings pattern from 2026-05-14), ASSUMPTION-111 (Wright/Rohr blocking N=13), PRESUMPTION-191
  Testability: testable empirically (track pending-proposal cadence over N≥4 weeks broken down by tradition; measure whether Carroll-Mindscape-podcast intake is becoming a recurring channel); testable via process (compare new-pending-proposal cadence across traditions for intake-distribution patterns)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-157
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Cowork evening-sync summary 2026-05-15 Files Created section as the +1 pending-proposal delta with Carroll-arc attribution.
    Current status: UNTESTED


# ─── 2026-05-17 c2a2-self-awareness-daily run (14a) ───
# Source: chat_to_cowork/2026-05-16_chat_summary.md + cowork_to_chat/2026-05-16_cowork_summary.md
# (both generated 2026-05-17 UTC). Substantive C2A2 work was 2026-05-16's
# Multi-agent Obsidian+DeepSeek thread + the meta-signal of 2 consecutive missed
# 14a/14b fires. This run also acknowledges 2026-05-15 EOD content remained
# un-ingested by 14a/14b; that day is left as carry-forward (handled separately
# when the gap-recovery decision is made by Tom).

ASSUMPTION-158:
  Date identified: 2026-05-17
  Statement: For adding a non-Claude LLM agent to the same vault, the chosen architecture is **Path 2**: DeepSeek-Flash via API driving a worker script that reads a job-folder queue. Path 1 (in-Obsidian plugin + local DeepSeek via Ollama) was rated "free, local, not really agentic"; Path 3 (DeepSeek through an MCP-capable third-party harness like Cline / Continue / OpenCode pointed at the same MCP servers Claude uses) was rated "most elegant, currently requires harness debugging because DeepSeek's tool-call reliability lags its reasoning." Recommendation: start with Path 2; "Path 3 worth doing *after* Path 2 is paying off, not before."
  Context: chat_to_cowork/2026-05-16_chat_summary.md Key Discussion Points (architectural paths laid out + recommendation paragraph). The Multi-agent Obsidian/DeepSeek thread (~17:50–21:00 UTC, Opus 4.7 Adaptive) on 2026-05-16.
  Type: architectural / operational / infrastructure
  Related decisions: PREMISE-016 (toolkit/content separation), DECISION-032 candidate (toolkit/content separation), Pathway 18 (Portability), PRESUMPTION-183, PRESUMPTION-184, PRESUMPTION-185, PRESUMPTION-189
  Testability: testable empirically (run Path 2 against a real vault workload; measure throughput, failure modes, review-bottleneck rates; if Path 2 "pays off" then trial Path 3 against the same workload); testable via process (audit whether the three-path framing covers the architectural space or whether unconsidered alternatives — agent inside Obsidian via Continue, MCP-router daemon, polyglot CI-style queue — should have been on the list)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-158
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from chat_to_cowork/2026-05-16_chat_summary.md as the three-path architectural framing + Path-2 recommendation.
    Current status: UNTESTED

ASSUMPTION-159:
  Date identified: 2026-05-17
  Statement: `agents.md` is the operating contract for any non-Claude LLM agent on the C2A2 vault. It imports Tom's 12 rules verbatim with a one-line analogy note ("code"→"notes", "codebase"→"vault", "tests"→"verification") and attaches vault-specific corollaries to Rules 5, 8, and 9 where the coding-to-vault mapping is non-obvious. The MindStudio reference appeared in the conversation as the editable-control-plane analogy: both Claude agents and the DeepSeek worker read the same `agents.md` for policy — single source of truth for behavior, one place to edit when policy changes.
  Context: chat_to_cowork/2026-05-16_chat_summary.md Key Discussion Points (agents.md description) + C2A2-Specific Items (MindStudio editable-control-plane analogy).
  Type: architectural / governance / operational
  Related decisions: PREMISE-016 (toolkit/content separation reinforcement), ASSUMPTION-158, PRESUMPTION-184 (12-rules transfer-validity)
  Testability: testable empirically (after N≥4 weeks of multi-agent operation, audit whether agents.md actually functions as single source of truth — does a policy edit in agents.md propagate to all agent behavior? are there agent-specific overrides that bypass the contract?); testable via process (compare single-source-of-truth governance vs per-agent-contract governance for drift over time)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-159
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from chat_to_cowork/2026-05-16_chat_summary.md as the agents.md single-source-of-truth commitment with 12-rule import and MindStudio analogy.
    Current status: UNTESTED

ASSUMPTION-160:
  Date identified: 2026-05-17
  Statement: The DeepSeek worker is **scope-locked to `_agents/deepseek/`** (inbox / outbox / done / failed). It "never writes to live vault content; promotion is a human-or-Claude review step." Output filenames follow Maildir-style convention: `{YYYYMMDD-HHMMSS}_{task}_{job-stem}.md` so outputs sort naturally and grep cleanly. The vault-safety boundary is the architectural commitment: the worker's blast radius is bounded by the folder scope and the no-write-to-live-content rule.
  Context: chat_to_cowork/2026-05-16_chat_summary.md Planning Notes & Priorities (scope-lock statement + Maildir convention).
  Type: architectural / operational / safety
  Related decisions: PREMISE-016 (toolkit/content separation), ASSUMPTION-158, ASSUMPTION-170 (hard prohibitions in agents.md), PRESUMPTION-183 (Maildir-pattern scaling), PRESUMPTION-185 (Claude-as-reviewer-bottleneck)
  Testability: testable empirically (after the worker runs against the real vault, audit git history — did the worker ever write outside `_agents/deepseek/`? did any promotion bypass the human-or-Claude review step?); testable via process (compare scope-locked vs scope-unlocked agent architectures for safety / damage-recovery / governance load)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-160
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from chat_to_cowork/2026-05-16_chat_summary.md Planning Notes section as the scope-lock + Maildir convention + no-write-to-live-content commitment.
    Current status: UNTESTED

ASSUMPTION-161:
  Date identified: 2026-05-17
  Statement: The Path-2 sandboxed-worker architecture is **C2A2 architectural infrastructure (reusable post-ISME), not pathway content**. It explicitly reinforces PREMISE-016 (toolkit/content separation) by adding a second, non-Claude LLM agent to the same vault under a strict sandbox. The cowork summary frames it: "today's Chat-side DeepSeek/Obsidian work explicitly leans on the spirit of DECISION-032 (toolkit/content separation), making canonization even more grounded."
  Context: cowork_to_chat/2026-05-16_cowork_summary.md For Morning Discussion section ("Today's Chat work is reusable architecture, not pathway content"); chat_to_cowork/2026-05-16_chat_summary.md C2A2-Specific Items ("architectural infrastructure for C2A2, not pathway content").
  Type: architectural / classification / governance
  Related decisions: PREMISE-016, DECISION-032 candidate (toolkit/content separation), ASSUMPTION-158, ASSUMPTION-159, ASSUMPTION-160
  Testability: testable empirically (after N≥4 weeks, audit whether the agents.md + worker.py infrastructure is reused by another agent / another instance / another vault, validating the reusability claim); testable via process (compare classification-as-infrastructure vs classification-as-pathway-content for canonization weight + downstream-priority effects)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-161
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from both 2026-05-16 daily-sync summaries as the explicit infrastructure-not-content classification of the multi-agent work + the PREMISE-016 reinforcement claim.
    Current status: UNTESTED

ASSUMPTION-162:
  Date identified: 2026-05-17
  Statement: Coordination primitives for the multi-agent shared-vault pattern, as practical state of the art: **MCP as shared protocol; Git on the vault as universal undo / conflict layer; folder-scoped agent assignments** (no scheduler, no lock manager — last-write-wins; Git mitigates damage but does not prevent it). A `priority:` field on job frontmatter was explicitly deferred "until there's more than one producer."
  Context: chat_to_cowork/2026-05-16_chat_summary.md Key Discussion Points (coordination primitives bullet) + Open Questions (priority field deferred).
  Type: architectural / operational / coordination
  Related decisions: ASSUMPTION-158, ASSUMPTION-160, PRESUMPTION-183 (Maildir/folder-scoping at scale)
  Testability: testable empirically (after multi-producer operation begins — even Claude + DeepSeek both producing — measure last-write-wins collision rate; track Git-as-undo recovery work); testable via literature (multi-agent file-folder coordination patterns; CRDTs vs last-write-wins vs lock-managers for low-collision shared workspaces)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-162
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from chat_to_cowork/2026-05-16_chat_summary.md as the coordination-primitives state-of-the-art bullet.
    Current status: UNTESTED

ASSUMPTION-163:
  Date identified: 2026-05-17
  Statement: `worker.py` is **~60 lines, one-shot, no daemon, no retry logic, fail-loud**. Test-run output visible in the thread at 2026-05-16T20:49:13 UTC: C1–C5 checks (file routing inbox→done/failed, frontmatter parsing, fail-loud contract, vault-safety boundary, outbox filename pattern) all PASS, with `git status` showing zero changes outside `_agents/`. The worker meets Rules 2 (Simplicity First) and 12 (Fail Loud) of the operating contract.
  Context: chat_to_cowork/2026-05-16_chat_summary.md Key Discussion Points (worker.py description + test-run output).
  Type: architectural / operational / verification
  Related decisions: ASSUMPTION-158, ASSUMPTION-159 (agents.md as contract), ASSUMPTION-160, ASSUMPTION-170 (hard prohibitions audited by C4 vault-safety check)
  Testability: testable empirically (run the worker against larger / more pathological inputs; track whether fail-loud behavior holds, whether no-retry causes data loss in transient-network scenarios, whether the ~60-line scope sustains as use-cases expand); testable via process (compare one-shot / no-retry vs daemon / retry-with-backoff architectures for failure visibility vs reliability)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-163
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from chat_to_cowork/2026-05-16_chat_summary.md as the worker.py shape (~60 lines, one-shot, fail-loud) and the C1–C5 PASS evidence.
    Current status: UNTESTED

ASSUMPTION-164:
  Date identified: 2026-05-17
  Statement: Morning chat-scrape succeeded on **2026-05-16 — the FOURTH consecutive successful day** (05-13 / 14 / 15 / 16). Per ASSUMPTION-152's threshold ("if tomorrow's scrape also succeeds, four data points across four days starts to support the architectural-fix-via-credential framing rather than the architectural-fragility framing"), today is that fourth data point. PRESUMPTION-159's "credential-vs-architectural" question continues to weaken on the chat-scrape axis specifically, though it remains intact for the broader Chrome-MCP cluster (which is still the load-bearing substrate-decomposition gate concern).
  Context: cowork_to_chat/2026-05-16_cowork_summary.md What Was Accomplished Today ("morning chat-scrape succeeded for the **fourth consecutive day** (05-13 / 14 / 15 / 16)") + Pipeline Status (Chat-scrape line) + For Morning Discussion (fourth-consecutive-day reframe).
  Type: operational / empirical / pattern-stability
  Related decisions: ASSUMPTION-126 (drought-broken claim), ASSUMPTION-140, ASSUMPTION-152 (third-consecutive + four-day threshold), PRESUMPTION-159 (credential-vs-architectural), PRESUMPTION-177 (Chrome-MCP recurrence), PRESUMPTION-190 (binary-frame critique)
  Testability: testable empirically (track morning chat-scrape success/failure for N≥7 more consecutive days; if streak continues at N≥7-total the credential-fix-holding claim crosses to stable-pattern status; if it breaks, the architectural-fragility framing strengthens); testable via process (audit which proximal failure modes the sign-in fix actually addresses vs masks; whether the surviving failure modes have shifted to other Chrome-MCP surfaces)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-164
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork_to_chat/2026-05-16_cowork_summary.md as the fourth-consecutive on-cadence chat-scrape event crossing ASSUMPTION-152's threshold.
    Current status: UNTESTED

ASSUMPTION-165:
  Date identified: 2026-05-17
  Statement: The c2a2-self-awareness-daily (14a/14b) scheduled task has now **missed TWO consecutive cycles** (2026-05-15 EOD and 2026-05-16 EOD). No `architecture/changelog/2026-05-15_changes.md` or `2026-05-16_changes.md` exists; no `architecture/metrics/2026-05-15_snapshot.md` or `2026-05-16_snapshot.md` exists. Yesterday's three-consecutive-on-cadence streak (which had "substantially demoted ASSUMPTION-117's residual urgency") is broken. The pipeline that converts Chat-side architectural work into the assumption/presumption registers and feeds the 15a/15b/15c disposition cycle did not fire for two cycles. (Self-referential note: this current run — 2026-05-17 — is the resumption.)
  Context: cowork_to_chat/2026-05-16_cowork_summary.md What Was Accomplished Today + Pipeline Status + For Morning Discussion (two-consecutive-missed-cycles is the biggest pipeline signal); plus on-disk verification: changelog/ directory's latest file is `2026-05-14_changes.md`, metrics/ directory's latest file is `2026-05-14_snapshot.md`.
  Type: operational / meta-architectural / pipeline-health
  Related decisions: ASSUMPTION-117 (residual-urgency demotion reversed), Agent 14a/14b scheduled-task design, ASSUMPTION-166 (lit-search pipeline ran), PRESUMPTION-187 (pipeline-failure-vs-rate-mismatch frame)
  Testability: testable empirically (verify whether tonight's 2026-05-17 fire produces both a changelog and a snapshot; track the next N≥7 cycles for stable on-cadence behavior; if recurrence persists, escalate from credential / scheduler-state to a pipeline-design question per PRESUMPTION-187); testable via process (audit scheduler-task logs and last-fire timestamps for both 14a/14b and other end-of-day tasks; compare to identify whether this is task-specific or scheduler-wide)
  Status: GROUNDED (PREMISE-025 re-confirmed ACTIVE by monthly 15d re-check; 15a: SUPPORTED (Strong) | 15b: PARTIALLY-CHALLENGED (Moderate) | 15c: RE-CONFIRM; DISPOSITION-410, 2026-07-06)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-165
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork_to_chat/2026-05-16_cowork_summary.md as the two-consecutive-missed-cycles signal, confirmed against on-disk changelog/ and metrics/ directories. This run extracts it from within the resumed pipeline.
    Current status: UNTESTED

ASSUMPTION-166:
  Date identified: 2026-05-17
  Statement: c2a2-lit-search-pipeline **ran on cadence on 2026-05-16** (~06:00 local) and produced a documented **null run**: 0 newly QUEUED items, no INCORPORATE / MONITOR / REVISE writes, explicit empty-queue status block appended to `for_lit_search.md` and a corresponding 2026-05-16 RUN section in `lit_search_returns.md`. The pipeline **refused to drain the 57-item RE-TRIGGER cohort** via the daily pipeline (correct boundary discipline per the daily / 15d separation). The honesty-layer behavior here is good — the pipeline did not paper over its empty input; it surfaced the upstream-gap (14a/14b not fired) and the unowned-overdue cohort as items the next 14a/14b run should consider extracting.
  Context: cowork_to_chat/2026-05-16_cowork_summary.md What Was Accomplished + For Morning Discussion (system surfaced its own gap correctly); for_lit_search.md tail (2026-05-16 empty-queue status block); ASSUMPTION's source rationale section in for_lit_search.md.
  Type: operational / methodological / pipeline-discipline
  Related decisions: Pathway 14 (honesty layer / PREMISE-019), ASSUMPTION-165 (14a/14b missed), ASSUMPTION-167 (RE-TRIGGER cohort), PRESUMPTION-188 (15d-as-fixable-cadence vs unbuilt-component), PRESUMPTION-195 (honesty-layer success-criterion permissive vs active)
  Testability: testable empirically (track next N≥3 cycles for similar null-run discipline if upstream remains empty; audit whether the pipeline's escalation behavior strengthens or stays static); testable via process (compare null-run-with-status vs no-run-at-all vs forced-drain protocols for upstream-failure-surfacing)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-166
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-05-16 lit-search-pipeline null-run as a clean honesty-layer instantiation under Pathway 14's commitments.
    Current status: UNTESTED

ASSUMPTION-167:
  Date identified: 2026-05-17
  Statement: The 57-item RE-TRIGGER cohort from 2026-05-05 (`next_check: 2026-05-12`) is now **4 days overdue**, carry-forward in its **seventh consecutive daily 15a/15b/15c run without drain**, with no visible 15d-monitor evidence in 7+ runs. The lit-search empty-queue note offers the reframe: this is not an item-ageing problem (the items themselves haven't degraded) but an **ownership-boundary problem** — who actually processes them: daily 15c, weekly 15d, or a scheduled task that doesn't exist.
  Context: cowork_to_chat/2026-05-16_cowork_summary.md What Was Accomplished + Pipeline Status + For Morning Discussion (57 RE-TRIGGER items as process-fragility data point); for_lit_search.md 2026-05-16 RUN section ("RE-TRIGGER items still QUEUED from 2026-05-05 cohort: 57").
  Type: operational / pipeline-ownership / process
  Related decisions: ASSUMPTION-166, PRESUMPTION-188 (15d-existence question), PRESUMPTION-134/159/177 (substrate-decomposition gate, joins cluster)
  Testability: testable empirically (5-minute verification: does `c2a2-15d-monitor` scheduled task exist? when was its last fire? does its design include the RE-TRIGGER cohort as a 15d-owned input?); testable via process (compare unowned-cohort lifetimes against explicitly-owned-cohort lifetimes for the same task type)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-167
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork_to_chat/2026-05-16_cowork_summary.md + for_lit_search.md 2026-05-16 RUN section as the unowned-overdue-cohort signal at 4-days overdue.
    Current status: UNTESTED

ASSUMPTION-168:
  Date identified: 2026-05-17
  Statement: DECISION-032/033/034 canonization is now in **second-day carry-forward**. All three candidates have INCORPORATEd PREMISE backing as of 2026-05-15 15c (PREMISE-016 toolkit/content separation; PREMISE-017 federation default-OFF; PREMISE-018 meta-crafts first-class). Today's Chat-side DeepSeek/Obsidian work explicitly leans on the spirit of DECISION-032 (toolkit/content separation), strengthening canonization's grounding. The canonization is described in the cowork summary as "a ~10-minute desk action that closes three architectural commitments." Walk-time discussion or shortly after is the obvious slot.
  Context: cowork_to_chat/2026-05-16_cowork_summary.md Key Decisions Made + What's Next #3 + For Morning Discussion ("DECISION-032/033/034 canonization is now in second-day carry-forward").
  Type: operational / governance / canonization
  Related decisions: DECISION-032/033/034 (candidate), ASSUMPTION-150 (today's three INCORPORATEs), PREMISE-016/017/018, PRESUMPTION-191 (10-minute-desk-action understated)
  Testability: testable empirically (track whether canonization actually closes on the next walk or extends to a third / fourth carry-forward day; if canonization extends, audit the actual gating work to compare against the 10-minute estimate); testable via process (compare PREMISE-backed-candidate-DECISION canonization timing against non-PREMISE-backed candidates from prior cycles)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-168
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork_to_chat/2026-05-16_cowork_summary.md as the second-day-carry-forward state of DECISION-032/033/034 with the today-work strengthens-canonization observation.
    Current status: UNTESTED

ASSUMPTION-169:
  Date identified: 2026-05-17
  Statement: The pace-and-shape concern is now on its **fourth consecutive evening surfacing** (2026-05-13 sync-probe → 2026-05-14 evening sync → 2026-05-15 evening sync → 2026-05-16 evening sync). Each surfacing has been more concrete. The current data: three consecutive days have added architectural breadth and infrastructure (Pathways 18–26 + today's DeepSeek/Obsidian work) without advancing the ISME demo critical path (00, 01, 02, 03, 08, + tightening of 04/06/14). 8-week runway intact but unchanged. The cowork summary frames it: "the system has been generating architecturally-rich post-ISME work at a rate that the 14a/14b ingestion pipeline can't sustain — and today the ingestion pipeline visibly broke. That's not coincidence-shaped."
  Context: cowork_to_chat/2026-05-16_cowork_summary.md For Morning Discussion ("Pace-and-shape question, now on its fourth consecutive evening surfacing").
  Type: methodological / strategic / risk
  Related decisions: ASSUMPTION-138 (deliberate post-ISME breadth arc), ASSUMPTION-119 (6 ISME-critical pathways), ASSUMPTION-165 (14a/14b missed cycles), PRESUMPTION-178 (ISME-runway-without-risk-register), PRESUMPTION-186 (pace-and-shape zero-sum framing)
  Testability: testable empirically (audit weekly hours allocated to demo-path vs breadth/infrastructure work over the next 4 weeks against a stated allocation target; if no allocation target is set, the audit measures the implicit allocation); testable via process (compare pace-and-shape resurfacing without explicit reset vs explicit weekly allocation contracts)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-169
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from cowork_to_chat/2026-05-16_cowork_summary.md as the fourth-consecutive-evening pace-and-shape surfacing with the rate-mismatch-not-coincidence observation.
    Current status: UNTESTED

ASSUMPTION-170:
  Date identified: 2026-05-17
  Statement: `agents.md` codifies five hard prohibitions for any LLM agent operating on the C2A2 vault, candidate for lifting into the C2A2 architecture register's vault-safety-boundary cluster if not already there: (a) DeepSeek worker writing outside `_agents/deepseek/`; (b) any agent deleting notes without explicit confirmation; (c) any agent editing notes without first reading them (Rule 8); (d) silent merge of conflicting notes (Rule 7); (e) skipping logging on failure (Rule 12).
  Context: chat_to_cowork/2026-05-16_chat_summary.md C2A2-Specific Items (five-prohibition list with explicit "candidate for lifting into the C2A2 architecture register" framing).
  Type: architectural / safety / governance
  Related decisions: ASSUMPTION-159 (agents.md as contract), ASSUMPTION-160 (scope-lock), ASSUMPTION-163 (fail-loud), PREMISE-016, PRESUMPTION-184 (12-rules transfer)
  Testability: testable empirically (after multi-agent operation begins, audit git history for any of the five prohibitions being violated; track confirmation-rate on (b) deletion-prompts; track read-before-edit fidelity on (c)); testable via process (compare the five hard prohibitions against published multi-agent-on-shared-storage safety guidelines for completeness)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-170
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from chat_to_cowork/2026-05-16_chat_summary.md C2A2-Specific Items as the five-prohibition register-lift candidate list.
    Current status: UNTESTED

ASSUMPTION-171:
  Date identified: 2026-05-18
  Statement: Levin's January 2026 paper "Cognition Spaces: natural, artificial, and hybrid" (Solé/Levin, arXiv:2601.12837) is a major framework with unusually rich cross-tradition signals, justifying its inclusion under the agent's "significant work not yet captured" filter despite being outside the 30-day publication window. The specialist agent explicitly bridged it to Friston (Markov-blanket types), Hoffman (ITP/fitness geometry), Hawkins (neural space sub-region), Wolfram (ruliad slicing), Kastrup (basal aneural region), and to C2A2 itself (human-AI hybrid as the accelerator-detector's native domain).
  Context: Levin/Friston specialist agent (local_630c5f21) PROP output, 2026-05-18 Monday run; agent's autonomous-choices section: "I included Levin's January 2026 'Cognition Spaces' paper as a 'significant work not yet captured' per the filter — it was published outside the 30-day window but represents a major framework not present in approved/pending and is unusually rich in cross-tradition signals."
  Type: methodological / cross-tradition / curation-rule
  Related decisions: ASSUMPTION-138 (post-ISME breadth arc), Pathway 13 (Pattern Detector), CROSS-tradition bridge cluster
  Testability: testable empirically (audit how many "out-of-window inclusion" choices made by specialist agents in the next N≥10 runs survive Tom's review vs how many are rejected as scope-creep); testable via process (compare specialist-agent inclusion-rule (window + exception) against a strict-window-only rule for proposal quality)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-171
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Levin/Friston specialist agent's 2026-05-18 run report and PROP-003 cross-tradition-bridge listing.
    Current status: UNTESTED

ASSUMPTION-172:
  Date identified: 2026-05-18
  Statement: Levin's Clofilium ionoceutical paper (colorectal cancer, OSF 10.31219/osf.io/w5dq7_v1) and Friston's announced Cambridge "Precision Psychiatry" talk (28 May 2026) together constitute a strong cross-tradition signal: both reframe pathology as a failure of precision/coherence at different scales (cell-collective bioelectric coherence ↔ neuromodulatory precision-weighting). The specialist explicitly flagged this in PROP-003 as a paradigm-shift-candidate cluster.
  Context: Levin/Friston specialist agent (local_630c5f21) 2026-05-18 Monday run; cross-tradition-signals-noted section of the run summary.
  Type: empirical / cross-tradition / paradigm-shift-candidate
  Related decisions: CROSS-016/021/024 (quantum biology and precision-class bridges), ASSUMPTION-171, Pathway 13 (Pattern Detector)
  Testability: testable via literature (audit whether precision-failure framings in bioelectric and neuromodulatory pathology research converge or diverge at the level of mechanism/measurement; search for cross-citations between Levin-school and Friston-school in the past 24 months); testable empirically (track whether PROP-003's bridge claim survives Phase-3 reviewer scrutiny in C2A2's own cross-tradition disposition cycle)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-172
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Levin/Friston specialist agent's 2026-05-18 cross-tradition-signals annotation on PROP-003.
    Current status: UNTESTED

ASSUMPTION-173:
  Date identified: 2026-05-18
  Statement: Future-dated lecture announcements (such as Friston's 28 May 2026 Cambridge talk) warrant scheduling a follow-up monitoring task to capture the recording after delivery, rather than treating them as past-tense evidence. The specialist agent explicitly flagged this in the autonomous-choices section and recommended the orchestrator schedule a follow-up.
  Context: Levin/Friston specialist agent (local_630c5f21), 2026-05-18 run, autonomous-choices: "The Friston proposal is a forward-looking talk announcement (lecture is 2026-05-28); I flagged this explicitly and recommended the orchestrator schedule a follow-up monitoring task to capture the recording afterward."
  Type: methodological / curation-rule / scheduling
  Related decisions: Pathway 16 (durable memory), Pathway 17 (agent-developed participant), monitor_queue.md cadence
  Testability: testable empirically (audit whether forward-looking talk-announcement proposals reliably trigger a follow-up monitor entry; if not, the recommendation lives in the proposal narrative without operational effect); testable via process (compare proposals that include follow-up monitor entries against those that don't for downstream completion rate)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-173
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Levin/Friston specialist agent's 2026-05-18 autonomous-choices section as a forward-looking-talk-handling rule.
    Current status: UNTESTED

ASSUMPTION-174:
  Date identified: 2026-05-18
  Statement: The C2A2 wiki orchestrator's Phase-6 commit-and-push is currently BLOCKED by a stale `.git/index.lock` file from 2026-05-17 17:26 that the Linux sandbox cannot remove. 476 uncommitted changes have accumulated across many days. Even if the lock cleared, CLAUDE.md's constitutional rule forbids blind push — visual local-HTTP review is required. The orchestrator surfaced this rather than attempting workaround, which is correct under the constitutional rule but raises the question of whether daily orchestrator runs that produce 0 new content should generate any wiki write at all (vs the current pattern of producing a review HTML and Gmail draft every day regardless).
  Context: C282 wiki orchestrator run (local_2a76d5fd), 2026-05-18: "Phase 6 (commit + push) BLOCKED by stale `.git/index.lock` from 2026-05-17 17:26 that the sandbox can't remove. 476 uncommitted changes have accumulated across many days."
  Type: operational / governance / pipeline-discipline
  Related decisions: CLAUDE.md constitutional rule (visual review required before push), Pathway 14 (honesty layer), ASSUMPTION-159 (agents.md as contract)
  Testability: testable empirically (count days between orchestrator runs that successfully commit vs runs blocked by lock-or-review-pending; identify lock-clearance-cadence; track whether 476-change accumulation is a one-off or a steady-state); testable via process (compare always-commit-on-content vs commit-only-if-review-passed protocols for accumulation-curve shape)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-174
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the C282 wiki orchestrator's 2026-05-18 run report as a process-fragility marker at the commit-discipline / accumulation boundary.
    Current status: UNTESTED

ASSUMPTION-175:
  Date identified: 2026-05-18
  Statement: The pending review queue is now at 42 — the largest in network history — and worth Tom's prioritized review pass. The morning walk handoff briefing explicitly flagged this as a top-of-priorities item. The 42 is a single-day high water mark distinct from the steady-state 30-day-window proposal volume; it reflects review-throughput lag rather than proposal-generation acceleration.
  Context: Morning walk handoff (local_b1594599) briefing 2026-05-18: "pending queue is at 42 — the largest in network history"; C282 wiki orchestrator (local_2a76d5fd): "Pending review queue is at 42 (largest in network history). Worth Tom's prioritized review pass."
  Type: operational / throughput / review-discipline
  Related decisions: Pathway 25 (meta-visualization), ASSUMPTION-138 (post-ISME breadth arc), ASSUMPTION-169 (pace-and-shape concern)
  Testability: testable empirically (track pending-queue-depth over the next N≥14 days; identify whether 42 is the steady-state peak or whether it continues to grow; identify Tom's review-throughput in proposals/day); testable via process (compare prioritized-review-pass-on-flag vs FIFO-only protocols for queue-depth-recovery time)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-175
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the morning walk handoff briefing and C282 wiki orchestrator's 2026-05-18 priority-flag on the 42-item review queue.
    Current status: UNTESTED

ASSUMPTION-176:
  Date identified: 2026-05-18
  Statement: The Wolfram pending queue contains two near-duplicate Q&A pairs that should be deduplicated before Tom reviews. The morning walk briefing surfaces this as a pre-review hygiene step. Near-duplicate identification was performed by the orchestrator/briefing pass without explicit similarity-threshold articulation; the deduplication recommendation is normative (duplicate-pairs reduce review-load without losing information) but treats duplicates as strict-improvement removals.
  Context: Morning walk handoff (local_b1594599) briefing 2026-05-18: "Wolfram pending queue has two near-duplicate Q&A pairs that should be deduped before review."
  Type: operational / methodological / review-hygiene
  Related decisions: Pathway 25 (meta-visualization), Pathway 13 (Pattern Detector), ASSUMPTION-175 (42-queue)
  Testability: testable empirically (audit whether the two flagged Q&A pairs are in fact substitutable, or whether one captures information the other does not; track downstream loss-events from past deduplications); testable via process (compare auto-dedup vs reviewer-confirms-then-dedup protocols for false-positive-rate on duplicate detection)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-176
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the morning walk handoff briefing's 2026-05-18 Wolfram-dedup recommendation.
    Current status: UNTESTED

ASSUMPTION-177:
  Date identified: 2026-05-18
  Statement: The c2a2-periodic-monitor-weekly (15d) ran today on a weekly-catchup cadence — its first fire since 2026-05-05 — resolving the schedule-failure flagged by yesterday's SYSTEMIC-RISK-FLAG-NEW. 30 items were re-queued for first-time cycle-1 re-trigger; 57 items were skipped because yesterday's exceptional daily-pipeline drain already refreshed them (advisory next 15d check 2026-05-24). The 3 stale-watch items (MONITOR-040, 042, 044) remain at cycle 3, one cycle from formal escalation (≥4 = STALE-MONITOR-FLAG). This partially addresses but does not close PRESUMPTION-188 (15d-as-fixable-cadence vs unbuilt-component) or OPEN-046 (does c2a2-15d-monitor exist?) — today's fire confirms it exists, but the schedule-reliability question remains.
  Context: C2A2 periodic monitor weekly run (local_8cbad424), 2026-05-18: "Weekly catchup run (first 15d fire since 2026-05-05; resolves the schedule-failure flagged by 15a/15b/15c yesterday). Items processed: 30 ... Items skipped: 57 ... Stale-monitor flags: None formally issued."
  Type: operational / pipeline-health / scheduling
  Related decisions: PRESUMPTION-188, OPEN-046, ASSUMPTION-167 (RE-TRIGGER cohort ownership), SYSTEMIC-RISK-FLAG-NEW
  Testability: testable empirically (track next N≥4 weekly 15d fires for on-cadence behavior; if recurrence-of-skip occurs, escalate from credential/scheduler-state to a deeper schedule-reliability question); testable via process (audit scheduler logs for 15d task definition and last-fire history; compare against 14a/14b cadence pattern)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-177
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-05-18 c2a2-periodic-monitor-weekly run report (catchup-fire resolves yesterday's SYSTEMIC-RISK-FLAG-NEW partially).
    Current status: UNTESTED

ASSUMPTION-178:
  Date identified: 2026-05-18
  Statement: The C2A2 wiki orchestrator and the Levin/Friston specialist disagree about today's specialist output: the orchestrator (and the morning walk handoff drawing on orchestrator state) reports "the Monday Levin+Friston specialist slot did NOT produce proposals today — only Wolfram-tagged proposals dated today appeared in `pending/`. Worth checking that cron." Yet the specialist itself (local_630c5f21) reports "C2A2 MONDAY AGENTS — 2026-05-18 — Levin Agent: 2 proposals written / Friston Agent: 1 proposals written / Total: 3 proposals added to pending/". The discrepancy may be ordering (orchestrator ran before specialist completed) or storage (specialist proposals written but with a tag/path the orchestrator's pending/-scan does not see). Either way, an inter-agent state-visibility gap is operative.
  Context: Morning walk handoff briefing (local_b1594599): "Levin+Friston specialist slot appears to have produced nothing today despite being a Monday — orchestrator's run narrative recommends checking their cron"; C282 wiki orchestrator (local_2a76d5fd): "The Monday Levin+Friston specialist slot did **not** produce proposals today — only Wolfram-tagged proposals dated today appeared in `pending/`. Worth checking that cron"; Levin/Friston specialist (local_630c5f21): 3 proposals written report.
  Type: operational / inter-agent / state-visibility
  Related decisions: PRESUMPTION-187 (pipeline-failure-vs-rate-mismatch), Pathway 14 (honesty layer), ASSUMPTION-159 (agents.md as contract)
  Testability: testable empirically (5-minute verification: do the Levin/Friston specialist's 3 proposals actually appear under pending/ at the time of the orchestrator's scan? what tag/path do they use? does the orchestrator's pending/-scan look in the right place?); testable via process (compare run-ordering options (orchestrator-first / specialist-first / parallel) for state-visibility correctness)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-178
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the three-way contradiction across today's orchestrator, morning walk handoff, and Levin/Friston specialist run reports.
    Current status: UNTESTED

ASSUMPTION-179:
  Date identified: 2026-05-18
  Statement: The C2A2 sewing-agent weekly run (local_57fed042) scanned `inbox/proposals/pending/` and processed "all seven 2026-05-18 inbox proposals (three Rohr, three Wright, one Friston)." This is a partial empirical resolution of OPEN-049: the proposals DO exist under `pending/`, so the C2A2 wiki orchestrator's earlier "Monday Levin+Friston specialist slot did NOT produce proposals today" report (local_2a76d5fd) is a scan-coverage / tag-filter / path-scope failure, not a write-failure on the specialist side. The morning briefing's "worth checking that cron" suggestion (relayed in local_b1594599) is therefore misdirected.
  Context: C2A2 sewing-agent weekly run report (local_57fed042), 2026-05-18 EOD: "10 pages received Agentic Calls (52 calls total): one Levin PRS-triplets file, one Loughran-papers README, one MacIntyre tradition wiki ... and all seven 2026-05-18 inbox proposals (three Rohr, three Wright, one Friston)."
  Type: operational / inter-agent / state-visibility / OPEN-049-partial-resolution
  Related decisions: ASSUMPTION-178, PRESUMPTION-196, OPEN-049, Pathway 14 (honesty layer)
  Testability: testable empirically (the proposals were observed in `pending/` by sewing-agent; the orchestrator's miss is now diagnosable as a scan-vs-write contract failure rather than a scheduling failure — next step is to capture both the orchestrator's exact scan command/filter and the path layout the specialists actually wrote to, and reconcile)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-179
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the EOD sewing-agent weekly run (local_57fed042) as the post-midday empirical witness that the orchestrator/briefing's morning miscategorization was a scan-coverage problem, not a missing-output problem.
    Current status: UNTESTED

ASSUMPTION-180:
  Date identified: 2026-05-18
  Statement: A second-order count discrepancy compounds OPEN-049: the sewing-agent's pending/-scan sees "three Rohr, three Wright, one Friston" (so: 0 Levin / 1 Friston / 6 weekend-rotation), while the Levin/Friston specialist's own run report (local_630c5f21) claims "Levin Agent: 2 proposals written / Friston Agent: 1 proposals written / Total: 3 proposals added to pending/." Three reconciliation candidates: (a) the specialist's "Levin: 2" count is a claim that did not result in actual writes under `pending/`; (b) the 2 Levin proposals were written to a different path (e.g., a tradition-subdir or a tag the sewing-agent's loop also misses); (c) the Friston count agrees across both views and is therefore the controlled value, isolating the discrepancy to the Levin output.
  Context: Levin/Friston specialist (local_630c5f21) and sewing-agent (local_57fed042) cross-tabulation; only the Friston count (=1) is concordant across both scans.
  Type: operational / inter-agent / output-counting
  Related decisions: ASSUMPTION-178, ASSUMPTION-179, PRESUMPTION-196, OPEN-049, OPEN-052 (new)
  Testability: testable empirically (5-15 minute audit: `ls -la inbox/proposals/pending/` filtered by 2026-05-18 + Levin-tagged files; cross-check against the specialist's claimed write list and against the sewing-agent's processed-page list)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-180
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the second-order discrepancy isolated by cross-tabulating the Levin/Friston specialist's run-report counts against the sewing-agent's pending/-scan processed-page list.
    Current status: UNTESTED

ASSUMPTION-181:
  Date identified: 2026-05-18
  Statement: 2026-05-18 connectivity row appended to `architecture/metrics/connectivity_log.csv`: `2026-05-18,1104,2,17,1123`. Orphan-count jumped +338 vs 2026-05-10. The sewing-agent's own diagnosis: "the entire jump is the newly-in-scope `architecture/lit_search_results/` corpus (754 auto-generated lit-search files). Recommend adding that path to the agent's exclusion list in a future run — flagged in the log."
  Context: Sewing-agent run (local_57fed042), connectivity-log diff vs 2026-05-10 prior row.
  Type: operational / metrics-scope / sewing-agent-configuration
  Related decisions: Pathway 13 (Pattern Detector), Pathway 25 (meta-visualization), DECISION-036-cluster
  Testability: testable via process (exclude `architecture/lit_search_results/` from sewing-agent's traversal in next run; verify orphan count drops by ~338); testable empirically (compare connectivity row N vs N+1 across exclusion-vs-inclusion to quantify the lit_search_results/ scope contribution)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-181
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the sewing-agent's self-reported scope-diagnosis of the +338 orphan jump.
    Current status: UNTESTED

ASSUMPTION-182:
  Date identified: 2026-05-18
  Statement: The sewing-agent wrote three new substantive cross-tradition bridge notes to `synthesis/` on 2026-05-18: (a) `friston_levin_bridge.md` — precision-weighting as substrate-agnostic FEP core; neuromodulator-precision in brains ≅ Vmem-precision in cell collectives ("Strongest empirical bridge in today's batch"); (b) `mcgilchrist_rohr_bridge.md` — Rohr's three 2026-05-18 proposals operationalize three components of McGilchrist's hemispheric account; (c) `wright_rohr_bridge.md` — Wright's *ruach* × Rohr's Universal Christ as the same participatory move in different scriptural registers, plus the cruciform-suffering convergence.
  Context: Sewing-agent run report (local_57fed042); the three bridge notes are reported as the run's substantive synthesis output.
  Type: empirical / cross-tradition / structural-homology
  Related decisions: ASSUMPTION-172 (PROP-003 paradigm-shift candidate), Pathway 13 (Pattern Detector), OPEN-051, OPEN-053 (new), PRESUMPTION-198, PRESUMPTION-207 (new)
  Testability: testable via process (Pattern-Detector / Pathway-13 instantiation should re-derive or refute these bridges as independent confirmation); testable empirically (receiving-tradition specialists should confirm or contest each bridge from their side)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-182
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the sewing-agent's three-bridge-note synthesis output as the second meaningful cross-tradition bridge cluster of the day (joining PROP-003 from this morning).
    Current status: UNTESTED

ASSUMPTION-183:
  Date identified: 2026-05-18
  Statement: The FC26 conference abstract Revision 2 was closed as submission-ready (paper-sketches session local_ea04730f). The abstract states a corpus horizon: "agents running since early April 2026, through Day 100 of 308, full commentary by July 2026." The terms "empirically prefigured" (¶1 load-bearing position) and "published thought of" (¶2) were installed; HTM was spelled out; Hoffman attribution on the discharge section was confirmed.
  Context: Paper sketches session (local_ea04730f): "The abstract is in submission-ready shape from my side." Cross-confirmed by the evening cowork-to-chat session (local_3ea0d368) "FC26 abstract (local_ea04730f) — Revision 2 closed out, submission-ready."
  Type: empirical / publication-commitment / horizon-articulation
  Related decisions: ASSUMPTION-168 (canonization momentum), DECISION-036 carry-forward, Pathway 22 (individual second brain), Pathway 24 (meta-crafts governance)
  Testability: testable via process (FC26 submission acceptance/rejection is the immediate test; the 308-day horizon is testable as a cadence-discipline measurement against today's 2-cycle gap and any future gaps)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-183
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the FC26-abstract Revision-2 closure as a publication-commitment + 308-day-corpus-horizon assumption pair.
    Current status: UNTESTED

ASSUMPTION-184:
  Date identified: 2026-05-18
  Statement: Cowork-to-chat delivery via `document.execCommand('insertText', ...)` on the ProseMirror contenteditable works where the morning's `type`-with-newlines path misfired (local_3ea0d368): "Used `document.execCommand('insertText', ...)` on the ProseMirror contenteditable rather than the `type`-with-newlines path that misfired this morning — that fix is now recorded in the file footer as a SKILL.md update recommendation."
  Context: Evening cowork-to-chat session (local_3ea0d368): successful single-message delivery to "Morning planning walk" thread (chat ID `ed8b7056-407d-4a71-8fae-62b08e9613e0`).
  Type: methodological / tooling / SKILL.md-update-pending
  Related decisions: Pathway 16 (durable memory), Pathway 8 (prepared presentation), morning briefing pipeline
  Testability: testable empirically (next N≥3 cowork-to-chat sends using `insertText` should succeed; if `type`-with-newlines is retried for a control, it should re-fail; if `insertText` fails on a future send, the working-condition hypothesis tightens or breaks)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-184
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the evening cowork-to-chat session's explicit method-substitution and SKILL.md-update-recommendation note.
    Current status: UNTESTED

ASSUMPTION-185:
  Date identified: 2026-05-18
  Statement: Cross-project verification methodology — the Pulte Pre-Test Pack (local_26b6c078, Keough School Obsidian Wiki Project) installs graded scoring (0 / 0.5 / 1) with per-prediction rationale, and addresses four contamination modes (temporal: pre-write deadlines; author: separation of writer and tester; specificity: named pairs not clusters; scoring-grain: graded not binary). Healthy expected total stated as 3.0–4.0 / 5.0 — a 5.0 reads as "predictions too loose," not "methodology validated." This methodology is C2A2-transferable for pre-registering predictions on bridge claims (PROP-003 cluster, OPEN-051) and on cadence-discipline (ASSUMPTION-117 streak, ASSUMPTION-168 carry-forward).
  Context: Pulte Pre-Test Pack session (local_26b6c078): "five named-pair predictions with named-pair specificity, graded scoring (0 / 0.5 / 1), independent confidence ratings, and a per-prediction rationale field. Expected healthy total: 3.0–4.0 / 5.0."
  Type: methodological / cross-project-transfer / verification-framework
  Related decisions: OPEN-051 (cross-specialist confirmation), Pathway 14 (honesty layer), Pathway 13 (Pattern Detector), Pathway 24 (meta-crafts governance)
  Testability: testable via process (apply the four-contamination-mode framework to a C2A2 pre-registration on PROP-003 bridge survival rate and compare to current sole-source baseline); testable empirically (track whether C2A2 graded-scoring on bridges produces healthy 3.0–4.0/5.0 totals vs the 5.0-as-too-loose failure mode)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-185
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Pulte Pre-Test Pack session as a cross-project methodology-transfer assumption whose four-contamination-mode frame is C2A2-applicable.
    Current status: UNTESTED

ASSUMPTION-186:
  Date identified: 2026-05-19
  Statement: The "51 pending — largest in network history" alarm is a measurement artifact, not a real backlog. 36 of the 51 files in `wiki/inbox/proposals/pending/` are stale duplicates that also exist in `approved/` (genuine unreviewed = 15). [stated] cleanup-stale-pending-proposals session: "36 filenames appear in both ... All 36 are stale duplicates in `pending/` that should be removed. After cleanup, `pending/` will hold 15 files (51 − 36)." The morning chat-scrape independently framed the same inflation as possible "reflection lag, not a real backlog."
  Context: cleanup-stale-pending-proposals (local_2837a01f, report-only) + morning chat scrape (local_251ff746) + C282 orchestrator (local_a328c51c) which suspended Phase-2 hunts on the inflated 51 count under the conservation principle.
  Type: empirical / operational
  Related decisions: DECISION-036 candidate, conservation-principle Phase-2 gating
  Testability: testable empirically (run the comm -12 dedup; confirm pending drops to 15; confirm orchestrator's next-run conservation gate flips once the count is corrected)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-186
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the cleanup session's duplicate-count finding cross-checked against the orchestrator's conservation-gate decision and the chat-scrape's reflection-lag framing.
    Current status: UNTESTED

ASSUMPTION-187:
  Date identified: 2026-05-19
  Statement: The 2026-05-18 `generate_review_page.py` overwrite-bug fix may be incomplete — the cleanup found 36 duplicates where the task expected 35; one new collision has appeared since the fix. [stated] "the task said 35, I found 36. One extra duplicate has appeared since the 2026-05-18 fix ... if the bug is meant to be fully fixed, that's worth a quick look at `generate_review_page.py` before you trust the count won't grow again."
  Context: cleanup-stale-pending-proposals session (local_2837a01f); Rule 7 surfaced-conflict note.
  Type: methodological / tooling
  Related decisions: DECISION-036 candidate (review-page generation)
  Testability: testable empirically (inspect generate_review_page.py write path; re-run a review cycle and check whether new pending/approved collisions reappear)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-187
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the cleanup session's 36-vs-35 discrepancy flag.
    Current status: UNTESTED

ASSUMPTION-188:
  Date identified: 2026-05-19
  Statement: The sandbox cannot write to `.git`; commits/pushes must happen from Tom's host shell. [stated] C282 orchestrator: "Phase 6: BLOCKED — sandbox cannot write to `.git` (stale 39-hour lock from 2026-05-17 cannot be removed; every git object-write hits 'Operation not permitted'). The file changes ARE on disk; commit/push will need to happen from Tom's host shell." Confirmed empirically the same day: Tom's host-shell push landed clean (b2c5af2..46cebd3) and the host-run sync_vault.sh pushed clean (3709adc..b2c5af2).
  Context: C282 orchestrator (local_a328c51c) Phase-6 block + debug-wiki-push (local_9dec9408) + mobile-visibility (local_29d859a8) host-shell successes.
  Type: architectural / operational
  Related decisions: DECISION-036 candidate (Path-2 sandboxed worker), OPEN-050
  Testability: testable empirically (already partially grounded — host-shell commits succeed; sandbox object-writes fail with ACL "Operation not permitted")
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-188
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the orchestrator's Phase-6 block statement, corroborated by two same-day host-shell push successes.
    Current status: UNTESTED

ASSUMPTION-189:
  Date identified: 2026-05-19
  Statement: The recurring `.git/index.lock` plus the ~716–720-uncommitted / 356-staged "morass" is caused by scheduled commit agents colliding or silently failing — not a one-off lock. [stated] debug-wiki-push: "The 720-uncommitted / 356-staged morass + recurring index.lock — the scheduled commit agents look like they're colliding or silently failing. That's the real systemic issue behind both today's locks and the staged pile-up." Corroborated by the mobile-visibility session's log evidence of the 2026-05-18 21:00 scheduled run dying on `index.lock: File exists`.
  Context: debug-wiki-push (local_9dec9408) + mobile-visibility sync_vault.log (local_29d859a8) + orchestrator stale-lock block (local_a328c51c).
  Type: architectural / operational
  Related decisions: OPEN-050, DECISION-036 candidate
  Testability: testable empirically (instrument the scheduled commit agents; check for concurrent git invocations and lock contention; confirm whether disabling overlap clears the recurrence)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-189
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the debug session's systemic diagnosis, corroborated by the dated lock-failure log lines in the sync_vault run.
    Current status: UNTESTED

ASSUMPTION-190:
  Date identified: 2026-05-19
  Statement: Hardening `sync_vault.sh` to `git commit --only ... -- wiki/vault/` makes the 21:00 scheduled run safe to fire unattended — it physically cannot pull the staged pile into a sync push. [stated] mobile-visibility: "the commit is now `commit --only ... -- wiki/vault/`, so it physically cannot pull the staged pile into a sync push ... the 21:00 scheduled run is safe to fire unattended going forward — no need to disable it." Grounded same-day: the hardened run committed exactly 80 files, all under `wiki/vault/`, and pushed clean.
  Context: mobile-visibility session (local_29d859a8), Tom-interactive; sync_vault.sh patch + verified run.
  Type: methodological / tooling
  Related decisions: OPEN-050, ASSUMPTION-189
  Testability: testable empirically (monitor the next N≥3 unattended 21:00 sync runs; confirm each commits only wiki/vault/ paths and leaves the architecture/ pile untouched)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-190
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the sync_vault.sh hardening claim and its same-day verified clean run.
    Current status: UNTESTED

ASSUMPTION-191:
  Date identified: 2026-05-19
  Statement: Two recurrence-prevention guards landed today: `regen_sociogram.sh` refuses to write a Summa-less Sociogram build, and `.gitignore *.bak*` prevents backup files being committed. [stated] debug-wiki-push: "regen_sociogram.sh — future regens can't drop `--summa` (it refuses to write a Summa-less build) ... Backups can no longer be committed (`*.bak*` ignored)."
  Context: debug-wiki-push (local_9dec9408); Sociogram Summa-node restoration (119 Summa commentary nodes confirmed in committed build).
  Type: methodological / tooling (guard)
  Related decisions: Pathway 16 (durable memory), wiki_narration regeneration workflow
  Testability: testable empirically (attempt a regen without --summa and confirm refusal; attempt to commit a *.bak file and confirm it is ignored)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-191
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the debug session's two stated guard mechanisms.
    Current status: UNTESTED

ASSUMPTION-192:
  Date identified: 2026-05-19
  Statement: The project CLAUDE.md visualization figures are stale — the narration graph is actually ~1,533 nodes / 36,608 edges / ~15.4 MB, not the documented "1,647 nodes / ~3,000 edges / ~4 MB"; the discrepancy makes the cellular/payload-diet concern materially worse. [stated] evening cowork-to-chat: "the CLAUDE.md viz figures are stale — the graph is actually 1,533 nodes / 36,608 edges and the file is ~15.4 MB, not '1,647 / ~3,000 / 4 MB.' That makes the cellular/payload-diet concern materially worse than the deferred pin assumed." (Stats corrected in CLAUDE.md and the device-freedom pin in the mobile-visibility session.)
  Context: evening cowork-to-chat (local_8456902d) + mobile-visibility CLAUDE.md correction (local_29d859a8).
  Type: empirical / documentation-integrity
  Related decisions: payload-diet pathway (deferred), Pathway 18 (portability toolkit)
  Testability: testable empirically (count nodes/edges in the current wiki_narration.html and compare to CLAUDE.md as-corrected)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-192
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the evening session's stale-stat discovery and the mobile session's same-day CLAUDE.md correction.
    Current status: UNTESTED

ASSUMPTION-193:
  Date identified: 2026-05-19
  Statement: The PRS-triplet network has grown to 231 triplets / 90 cross-program connections / 35 findings (from the frozen 2026-05-05 baseline of 133 / 54 / 20), with a new 32-connection "synergistic-coil" structural-bridge layer. [stated] PRS-triplet-viz review: "231 triplets (was 133), 90 cross-program connections (was 54), 35 findings (was 20), and a new synergistic-coil layer — 32 structural-bridge connections drawn as cyan arcs." (Note: the C282 orchestrator's same-day network line reported 225 triplets / ~90 cross-program connections / 35 findings — a 231-vs-225 triplet-count divergence; see PRESUMPTION-212.)
  Context: Review-PRS-triplet-visualization (local_a20a370b) + C282 orchestrator network line (local_a328c51c).
  Type: empirical
  Related decisions: Pathway 13 (Pattern Detector), prs_3d visualization
  Testability: testable empirically (run extract_prs_data.py and reconcile the 231 vs 225 triplet count against the vault)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-193
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the PRS-3d review session's growth figures; flagged the cross-source triplet-count divergence with the orchestrator.
    Current status: UNTESTED

ASSUMPTION-194:
  Date identified: 2026-05-19
  Statement: The prs_3d generator is NOT idempotent — it must be fed `template_prs_3d.html`, never an already-built file. [stated] PRS-triplet-viz review: "the generator is **not idempotent** — always feed it `template_prs_3d.html`, never an already-built file."
  Context: Review-PRS-triplet-visualization (local_a20a370b); regeneration-pipeline construction.
  Type: methodological / tooling (constraint)
  Related decisions: prs_3d visualization workflow; wiki_narration regeneration workflow (parallel non-idempotence risk)
  Testability: testable empirically (feed an already-built file to the generator and confirm corruption / double-injection)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-194
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the PRS-3d review session's stated tooling constraint.
    Current status: UNTESTED

ASSUMPTION-195:
  Date identified: 2026-05-19
  Statement: Two PRS data-integrity quirks are real and worth a later cleanup: a duplicate `PRS-10` in `arkanihamed/prs_triplets.md`, and `CROSS-051–054` existing under both header styles in `cross_program_index.md`. [stated] PRS-triplet-viz review: "two data quirks it flags are real and worth a later cleanup — a duplicate `PRS-10` in `arkanihamed/prs_triplets.md`, and `CROSS-051–054` existing under both header styles in `cross_program_index.md`."
  Context: Review-PRS-triplet-visualization (local_a20a370b); validate_prs_3d.py count-integrity flags.
  Type: empirical / data-integrity
  Related decisions: Pathway 13 (Pattern Detector input quality)
  Testability: testable empirically (grep the two source files; confirm the duplicate and dual-header entries)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-195
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the validator's two flagged data quirks.
    Current status: UNTESTED

ASSUMPTION-196:
  Date identified: 2026-05-19
  Statement: The Hawkins/Hoffman Tuesday slot bringing 0 proposals is the correct signal, not a search failure — the 30-day window fell in a quiet stretch where the recent Hoffman/Hawkins bursts are already ingested. [stated] Tuesday specialist: "Per Rule 12 (Fail loud) — I will not fabricate proposals to hit a target ... Bringing zero proposals today is the correct signal, not a search failure."
  Context: C2A2 Tuesday specialist (local_46845ec5); honest null after exhaustive arXiv/podcast/preprint search.
  Type: methodological / epistemic
  Related decisions: tradition-specialist quality filter; Rule 12 (fail-loud)
  Testability: testable empirically (audit search coverage; confirm no in-window Hawkins/Hoffman-authored work was missed)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-196
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Tuesday specialist's explicit Rule-12 honest-null statement.
    Current status: UNTESTED

ASSUMPTION-197:
  Date identified: 2026-05-19
  Statement: Pathway 27 (Universal Search & Ask) rests on a "one-index-two-surfaces" architecture: a single `entity_index.json` drives both client-side deterministic Search and broker-backed honesty-layer-disciplined Ask, plus render-time canonical auto-hyperlinking; Search + hyperlinking ship before July 8 (broker-independent), Ask stages after the broker and honesty layer land. [stated] debug-wiki-push, drafting Pathway 27: "Search ≠ hyperlinks ... but driven by one `entity_index.json` ... Search + hyperlinking ship before July 8 (broker-independent, table-stakes); Ask stages after the broker and honesty layer land."
  Context: debug-wiki-push (local_9dec9408); new architecture doc `27_universal_search_and_ask.md` (status: drafted; depends_on broker, perspective_lattice, honesty_layer; enables recursive_episode, apprentice_mode; isme_critical: yes).
  Type: architectural
  Related decisions: DECISION-037 candidate (adopt Pathway 27), Pathway 00 (broker), Pathway 14 (honesty layer)
  Testability: testable empirically (build entity_index.json; verify one index can serve all three surfaces without freshness/determinism conflict — see PRESUMPTION-217)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-197
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Pathway-27 draft's one-index-two-surfaces design rationale and ISME staging.
    Current status: UNTESTED

ASSUMPTION-198:
  Date identified: 2026-05-19
  Statement: 32 fabricated transcripts must be re-fetched before the July 8 publicize date; the commentaries are verified sound, so the problem is transcript-only. [stated] debug-wiki-push: "Re-fetch the **32 fabricated transcripts** (commentaries verified sound, so it's transcript-only) before the July 8 publicize date."
  Context: debug-wiki-push (local_9dec9408); fabrication-guard work earlier in the day (silent-fabrication guard among "three recurrence traps").
  Type: empirical / integrity
  Related decisions: Pathway 14 (honesty layer), QC fabrication guard
  Testability: testable empirically (enumerate the 32 transcripts; re-fetch and diff against fabricated versions; confirm commentary soundness is unaffected)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-198
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the debug session's transcript-fabrication remediation note.
    Current status: UNTESTED

ASSUMPTION-199:
  Date identified: 2026-05-19
  Statement: The lit-search pipeline's cycle-1 RE-TRIGGER refresh uses a carry-forward convention ("no new evidence in refresh gap; carry-forward") rather than expensive net-new web searches with low expected yield; and grounding citations draw on the model's training-knowledge corpus per the pipeline's established convention. [stated] lit-search-pipeline run: "for most items, recorded 'no new evidence in refresh gap; carry-forward' rather than attempting expensive net-new web searches with low expected yield ... Cited sources drew on training-knowledge corpus ... per the pipeline's established knowledge-search convention."
  Context: c2a2-lit-search-pipeline (local_c7bf1973); 30 Cohort-A re-trigger items all MONITOR-continued via carry-forward.
  Type: methodological
  Related decisions: 15a/15b search convention, MONITOR cycle protocol
  Testability: testable empirically (spot-check carry-forwarded items for missed updates; compare training-corpus citations against a live-search control for a sample)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-199
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the lit-pipeline run's stated autonomous cost-benefit and citation-source choices.
    Current status: UNTESTED

ASSUMPTION-200:
  Date identified: 2026-05-19
  Statement: Four Sunday-cron tasks (`c2a2-agent-wright-rohr`, `c2a2-sewing-agent-weekly`, `weekly-agent-ecosystem-report`, `c2a2-periodic-monitor-weekly`) fired as a single Monday-afternoon catch-up burst (2026-05-18 ~13:43–13:56 UTC) instead of their Sunday slots; this warrants a re-check next Sunday to confirm on-time firing. [stated] scheduler-health-check: "Four Sunday-cron tasks ... all last ran on Monday 2026-05-18 ~13:43–13:56 UTC instead of their Sunday slots — looks like a single Monday-afternoon catch-up burst. Worth a glance next Sunday."
  Context: scheduler-health-check (local_d41a0c72); 29 enabled tasks otherwise healthy.
  Type: operational / cadence
  Related decisions: ASSUMPTION-117 (cadence discipline), 15d periodic monitor schedule
  Testability: testable empirically (observe whether the four tasks fire on Sunday 2026-05-24/25 vs slip to Monday catch-up again)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-200
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the scheduler-health-check's Sunday-cron catch-up observation.
    Current status: UNTESTED

ASSUMPTION-201:
  Date identified: 2026-05-20
  Statement: The view called "3D PRS" is not a chart of triplets but a **narrative connectome** — the connected unit is the agentic PRS narrative (agent → goal → problem → resource → solution → outcome), read as a complete little model and, equivalently, a compression; three connectomes share one architecture (neural: neurons/axons; Hawkins/Thousand Brains: cortical columns/voting fibers; narrative: PRS narratives/shared-resource + coil fibers). [stated] narrative_prs_connectome.md: "It is a connectome — and specifically a narrative connectome ... a triplet is a model ... and, equivalently, a compression ... This is exactly the status Hawkins grants the cortical column."
  Context: Review-PRS-triplet-visualization (local_a20a370b); Tom-authored guiding document `architecture/narrative_prs_connectome.md` (status: architecturally guiding).
  Type: architectural / epistemic
  Related decisions: DECISION-038 (adopt connectome model), prs_3d → Narrative Connectome rebuild
  Testability: framework commitment (the connectome framing is largely a modeling stance, not testable); but the embedded compression sub-claim (a PRS narrative is an information-theoretic compression) is testable via literature — see ASSUMPTION-208 and PRESUMPTION-222
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-201
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the guiding document's thesis as the day's load-bearing conceptual reframe.
    Current status: UNTESTED

ASSUMPTION-202:
  Date identified: 2026-05-20
  Statement: The synergistic coils are **association fibers** — long-range connections that bind otherwise-separate narrative regions into a larger whole — not decoration; a tradition is a densely interconnected module of narratives, and a coil is the fiber that lets two modules begin to function as one. [stated] narrative_prs_connectome.md: "the coils are not decoration; they are association fibers."
  Context: Review-PRS-triplet-visualization (local_a20a370b); the connectome model's account of the cross-tradition coil layer (32 coils in the live build).
  Type: architectural / methodological
  Related decisions: DECISION-038, DECISION-040 (coils as the convergence instrument), Pathway 04 (perspective lattice), traditions/loughran (Synergistic Coil)
  Testability: framework commitment (the fiber framing) with a testable corollary — whether coil density between two modules tracks any independent measure of those traditions integrating (testable empirically)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-202
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the guiding document's elevation of coils from decoration to association fibers.
    Current status: UNTESTED

ASSUMPTION-203:
  Date identified: 2026-05-20
  Statement: A visualization is only ever as good as the model of what is being visualized that drives it; therefore the Connectome's perspective/control set must be **re-derived from the model**, aiming for parity of *richness* with the Sociogram, not parity of *controls*. [stated] narrative_prs_connectome.md Directive 2: "Parity of richness with the Sociogram, not parity of controls"; "We cannot decide what to visualize until we are clear about what we are visualizing."
  Context: Review-PRS-triplet-visualization (local_a20a370b); Directive 2 of the guiding document; seeds OPEN-058 (perspective set).
  Type: methodological
  Related decisions: DECISION-038, OPEN-058 (perspective set to derive from the model)
  Testability: framework commitment (a design principle, not literature-testable directly); the proposed perspective set it generates is empirically evaluable for usefulness
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-203
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the guiding document's model-driven-visualization principle and Directive 2.
    Current status: UNTESTED

ASSUMPTION-204:
  Date identified: 2026-05-20
  Statement: A coil's "altitude" should encode **discovery-time** (when the bridging insight was formed — ~2026 for nearly all current coils), not the age of the ideas it joins; pinning coils to the founding era is why they "sink" and never reach the recent band. This is the first concrete test of "axis follows model." [stated] narrative_prs_connectome.md: "A coil should sit where its bridging insight was formed (discovery-time ...), not at the age of the ideas it joins ... the concrete first test of 'axis follows model.'"
  Context: Review-PRS-triplet-visualization (local_a20a370b); implemented as Phase 1 of the connectome rebuild (coil altitude moved to the ~2026 discovery-year band).
  Type: methodological / architectural
  Related decisions: DECISION-039 (coil altitude = discovery-time), OPEN-057 (node vertical-axis semantics)
  Testability: testable empirically (audit each coil's discovery-year vs the founding-era it previously inherited; confirm the visual band shift matches the intended semantics)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-204
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the guiding document's open-decisions section and the Phase-1 implementation note.
    Current status: UNTESTED

ASSUMPTION-205:
  Date identified: 2026-05-20
  Statement: Cross-tradition convergence is **analogical, not verbatim** — only **3** literal cross-tradition resource hubs exist (no resource is shared by more than 2 traditions); therefore the coil layer (association fibers), not shared resources, is the project's real convergence instrument. [stated] 2026-05-20 cowork summary / Phase-2 finding: "only 3 literal cross-tradition hubs exist (max 2 traditions per resource), confirming traditions converge analogically, not verbatim."
  Context: Review-PRS-triplet-visualization (local_a20a370b); Phase-2 convergence-hub implementation (resources shared across ≥2 traditions glow gold) and its empirical finding.
  Type: empirical
  Related decisions: DECISION-040 (convergence is analogical; coils are the convergence instrument), ISME/FC26 framing of "convergence"
  Testability: testable empirically (re-run the shared-resource hub detector; confirm the count of 3 and the max-2-traditions ceiling are not artifacts of resource naming/normalization — see PRESUMPTION-228)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-205
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Phase-2 convergence-hub empirical finding.
    Current status: UNTESTED

ASSUMPTION-206:
  Date identified: 2026-05-20
  Statement: Generative-coil detection is **lexical-first (v1)** — 17 directed solution→resource handoffs found by lexical matching — with semantic/embedding detection deferred to v2. [stated] 2026-05-20 cowork summary: "Phase 3 generative coils — 17 directed solution→resource handoffs (lexical v1; semantic/embedding is v2)."
  Context: Review-PRS-triplet-visualization (local_a20a370b); Phase-3 generative-coil layer (17 chains rendered live); verified to react to the time slider (15 of 17 chains have a 2026 endpoint).
  Type: methodological / tooling
  Related decisions: DECISION-041 (lexical-first generative detection), OPEN-059 (semantic generative detection v2)
  Testability: testable empirically (compare lexical-v1 generative chains against a semantic/embedding detector on the same corpus; measure precision/recall of the lexical approach)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-206
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Phase-3 generative-coil implementation choice and its stated v1/v2 staging.
    Current status: UNTESTED

ASSUMPTION-207:
  Date identified: 2026-05-20
  Statement: The telos of the narrative connectome is the **emergence of a master science** — Aristotle's architectonic, Aquinas's sapientia, MacIntyre's tradition-craft — and there is **not one** master science but **rivals**: each mature tradition articulates its own, and they meet through coils as rivals-and-complements, never as a single convergent whole; "master" is architectonic (ordering), never dominating. [stated] narrative_prs_connectome.md: "What the connectome ultimately lets us watch is emergence ... a master science ... there is not one master science but rivals ... 'Master' here is architectonic (ordering), never dominating."
  Context: Review-PRS-triplet-visualization (local_a20a370b); the guiding document's telos section.
  Type: epistemic / normative
  Related decisions: DECISION-038, DECISION-040, OPEN-061 (connectome reframe as ISME/FC26 paper spine)
  Testability: framework commitment (not testable — a teleological/philosophical stance integrating Aristotle, Aquinas, MacIntyre); the historical claim that mature traditions articulate architectonic sciences is partially testable via the history/philosophy of science literature
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-207
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the guiding document's telos section; tagged as framework commitment with a partially-testable historical corollary.
    Current status: UNTESTED

ASSUMPTION-208:
  Date identified: 2026-05-20
  Statement: Progress is **better compression** — a later narrative that predicts/explains more of the same problem-space with less — so a forming master science should be visible as the connectome's **total description length falling even as it covers more**; this reconnects to Friston (free-energy minimization as compression), Wolfram (computational irreducibility as the incompressible limit), and the original RC-pilot ambition of quantifying progress through chained PRS triplets. [stated] narrative_prs_connectome.md: "progress is better compression ... A master science forming should be visible as the connectome's total description length falling even as it covers more."
  Context: Review-PRS-triplet-visualization (local_a20a370b); the guiding document's compression/entropy thread (proposed by Claude, adopted into the model).
  Type: epistemic / empirical
  Related decisions: DECISION-038, connectome metrics proposal (degree/modularity/fiber-density/path-length)
  Testability: testable via literature (MDL/algorithmic information theory; free-energy-as-compression) and testable empirically (define and compute a description-length proxy over the triplet corpus over time) — but rests on PRESUMPTION-222 (narrative compression ≡ information-theoretic compression)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-208
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the guiding document's compression/entropy thread as a testable progress metric proposal.
    Current status: UNTESTED

ASSUMPTION-209:
  Date identified: 2026-05-20
  Statement: Interaction behavior should form a **common behavior cluster across tabs** — the Connectome's node/edge/"?" interactions should match the Sociogram's: node click → that file in the right panel (filters stay); edge click → collapse the left filters and show the two connected files at once (source left, target right); any new click dismisses; empty-space click restores filters; "?" toggles open/closed. [stated] Tom: "Keep checking for ways to stay within/produce a common behavior cluster across tabs"; "port the functionality of the down button/up-on-edge-click behavior ... just as in sociogram."
  Context: Review-PRS-triplet-visualization (local_a20a370b); the Sociogram two-panel + dismiss-on-new-click model ported to the Connectome (built via the generator, staged in review, then promoted to live).
  Type: methodological / UX
  Related decisions: DECISION-042 (common interaction cluster + review-before-promote), Sociogram interaction model
  Testability: framework commitment (a UX consistency directive); evaluable empirically via cross-tab usability testing
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-209
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Tom's repeated common-behavior-cluster directive and the Sociogram-port implementation.
    Current status: UNTESTED

ASSUMPTION-210:
  Date identified: 2026-05-20
  Statement: For edge clicks, showing the **two endpoint narratives for all edge types** (uniform behavior), with the edge's own nature/year as a small header, is preferable to showing edge metadata — accepting the stated honesty caveat that for **synergistic coils and cross-links** (which bridge whole traditions) the two files are the *representative* narrative of each bridged tradition, not idea-precise endpoints. [stated] Claude proposed and Tom confirmed ("go please"): "show the two endpoint narratives for all edge types (uniform behavior = the common cluster you want), and tuck the edge's own label/nature as a small header."
  Context: Review-PRS-triplet-visualization (local_a20a370b); the two-panel edge port; explicit honesty note that tradition-bridging edges use representative narratives.
  Type: methodological / UX
  Related decisions: DECISION-042, ASSUMPTION-209
  Testability: framework commitment (a UX uniformity choice); the representative-narrative substitution's fidelity is the subject of PRESUMPTION-226
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-210
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the proposed-and-confirmed uniform two-endpoint edge behavior, including its stated representative-narrative caveat.
    Current status: UNTESTED

ASSUMPTION-211:
  Date identified: 2026-05-20
  Statement: Tom's guiding/definitional documents are placed **both** in `architecture/` and as a copy in his thinker file `traditions/loughran/`, and laced into the connectome via wikilinks, so the project's own guiding narratives become nodes in the connectome they govern — "the system documents itself inside itself." [stated] narrative_prs_connectome.md Directive 3: "placed both here (architecture/) and as a copy in his thinker file (traditions/loughran/) ... the system documents itself inside itself."
  Context: Review-PRS-triplet-visualization (local_a20a370b); Directive 3 (author-contribution convention) of the guiding document.
  Type: architectural / methodological
  Related decisions: DECISION-038 (author-contribution convention), Pathway 04 (perspective lattice)
  Testability: framework commitment (a documentation/authorship convention); its self-referential consequence is examined in PRESUMPTION-224
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-211
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the guiding document's author-contribution convention (Directive 3).
    Current status: UNTESTED

ASSUMPTION-212:
  Date identified: 2026-05-22
  Statement: A connectome build is safe to promote to live when its graph data is byte-identical to the approved file and `node --check` passes — data-integrity plus JS-syntax integrity (plus Tom's visual review) constitute the release gate.
  Context: PRS Narrative Connectome 2-panel UI bundle (local_a20a370b) — "validated (data byte-identical to the approved file, `node --check` clean), promoted to live, reviewed by Tom, pushed (`fc79739`)."
  Type: methodological
  Related decisions: DECISION-043, DECISION-042
  Testability: framework commitment (methodological release standard; its reproduced-behavior gap is testable — see PRESUMPTION-231)
  Status: GROUNDED (operationalized as the promotion gate this session)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-212
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated validation+promote sequence of the connectome 2-panel bundle.
    Current status: GROUNDED

ASSUMPTION-213:
  Date identified: 2026-05-22
  Statement: The connectome's needed interaction layer = a two-panel edge-cluster view + "?" pop-ups + node click-to-toggle (collapse) + edge-picking (Three.js raycast) + brightness and "Year ≥" time sliders — completing the ported Sociogram interaction cluster.
  Context: PRS Narrative Connectome bundle shipped this session (local_a20a370b); finishes the cross-tab interaction model adopted in DECISION-042.
  Type: architectural (UX)
  Related decisions: DECISION-043, DECISION-042
  Related assumptions: ASSUMPTION-209, ASSUMPTION-210
  Testability: framework commitment (design/UX stance)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-213
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the enumerated interaction-bundle feature set promoted to live.
    Current status: UNTESTED

ASSUMPTION-214:
  Date identified: 2026-05-22
  Statement: A single self-contained handoff document (`TWO_SUMMA_EXPERIMENT_BRIEF.md`) can carry an experiment's full context — project paths, PRS+tradition schema, design, success criteria, guardrails — into a cold-start chat, making the experiment portable across sessions ("open the new chat, attach that file, say go").
  Context: Two-summa experiment scoped to Option #3 to be run in a fresh chat (local_a20a370b); brief written to project root.
  Type: methodological
  Related decisions: DECISION-044
  Related: architecture/18_portability_toolkit.md
  Testability: testable empirically (does the cold-start chat reproduce the originating intent without the prior session's state?)
  Status: SEARCHED -- 15c disposition: MONITOR (MONITOR-220, 2026-05-23); see for_lit_search.md / monitor_queue.md
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-214
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the decision to hand off the experiment via a self-contained brief to a fresh chat.
    Current status: SEARCHED

ASSUMPTION-215:
  Date identified: 2026-05-22
  Statement: A "Conscious-Realist-Monist summa" can be constructed as a genuine rival to the Thomist summa, and the two can be run head-to-head to produce evidence about how richly-informed traditions interact.
  Context: Two-summa experiment design (Option #3), briefed in TWO_SUMMA_EXPERIMENT_BRIEF.md (local_a20a370b) — Thomist summa vs. Conscious-Realist-Monist summa.
  Type: epistemic / empirical
  Related decisions: DECISION-044
  Related open questions: OPEN-062
  Testability: testable via literature (tradition rivalry & commensurability — MacIntyre) and empirically (the experiment itself)
  Status: PARTIALLY-CHALLENGED -- 15c disposition: REVISE (REVISE-047 HIGH, 2026-05-23, AWAITING-REVIEW); SYSTEMIC-RISK-FLAG H; see revision_flags.md
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-215
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated two-summa head-to-head premise; the day's most substantive new conceptual stake.
    Current status: PARTIALLY-CHALLENGED

ASSUMPTION-216:
  Date identified: 2026-05-22
  Statement: The Aquinas<->Levin teleology seam (with specific Summa source days) is the right focal cross-tradition bridge for the two-summa head-to-head.
  Context: TWO_SUMMA_EXPERIMENT_BRIEF.md names the Aquinas<->Levin teleology seam as the experiment's focal connection (local_a20a370b).
  Type: architectural / empirical
  Related decisions: DECISION-044
  Related assumptions: ASSUMPTION-215, ASSUMPTION-205, ASSUMPTION-207
  Testability: testable (is this dyad the most evidentially productive seam? compare against alternatives)
  Status: SEARCHED -- 15c disposition: MONITOR (MONITOR-221, 2026-05-23); see for_lit_search.md / monitor_queue.md
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-216
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the brief's selection of a single focal teleology seam.
    Current status: SEARCHED

ASSUMPTION-217:
  Date identified: 2026-05-22
  Statement: Embedding the 307 "Principal research areas" faculty summaries directly in the KSGA sociogram's node data (self-contained node panels) is preferable to linking out — the node panel should carry its own content.
  Context: KSGA sociogram regeneration (local_26b6c078) — "research summaries are now in the data ... clicking a faculty node will now show their summary in the right panel"; index.html grew 1.3 -> 1.9 MB.
  Type: architectural / methodological
  Related decisions: DECISION-045
  Testability: framework commitment (design stance; its scaling cost is testable — see PRESUMPTION-236)
  Status: GROUNDED (implemented in the regenerated sociogram)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-217
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the deliberate choice to embed faculty summaries inline in the node data.
    Current status: GROUNDED

ASSUMPTION-218:
  Date identified: 2026-05-22
  Statement: Repository publishability is decidable per-artifact at the designer's discretion — curated artifacts are tracked/published (eulogy in, Habash transcripts in) while raw/sensitive material is kept out (Archbishop report out, Hoffman x Levin raw transcript stop-tracked), enforced via a root `.gitignore`.
  Context: Repo-hygiene pass in the connectome session (local_a20a370b) — explicit per-file publish/untrack calls plus a new root .gitignore.
  Type: methodological (with normative dimension)
  Related decisions: DECISION-046
  Related presumptions: PRESUMPTION-237
  Testability: framework commitment (governance stance; underlying criterion is unstated — see PRESUMPTION-237)
  Status: GROUNDED (acted on this session)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-218
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the enumerated publish/untrack decisions; the governing criterion behind them is left to 14b.
    Current status: GROUNDED

ASSUMPTION-219:
  Date identified: 2026-05-22
  Statement: The connectome thread is complete enough to close and hand off cleanly to the two-summa experiment — shipping the bundle and executing the deferred push (`fc79739`) marks the thread "done."
  Context: End of the connectome session (local_a20a370b) — "the connectome thread can now hand off cleanly to the two-summa experiment."
  Type: methodological / operational
  Related decisions: DECISION-043, DECISION-044
  Related open questions: OPEN-056 (commit-ownership)
  Testability: framework commitment (operational judgment of thread completion)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-219
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit close-and-pivot framing at session end.
    Current status: UNTESTED

ASSUMPTION-220:
  Date identified: 2026-05-23
  Statement: PRS-triplet candidates can be validly generated from a talk's announced topic list and runtime metadata when the full transcript cannot be retrieved — provided confidence is capped at Medium and the candidate is explicitly flagged for transcript verification before promotion to a numbered PRS triplet.
  Context: Both 2026-05-23 Wolfram intake proposals (PROP-2026-05-23-001 future-science-tech; PROP-2026-05-23-002 business/ownerless-AI) state in their Methodological Notes that the transcript could not be fetched, so candidates were derived from the published topic list and capped at Medium/Speculative confidence. Surfaced on an automated-pipeline day with no interactive Tom session (see daily_sync/cowork_to_chat/2026-05-23_cowork_summary.md).
  Type: methodological
  Related decisions: (none; tradition-intake methodology)
  Related presumptions: PRESUMPTION-242
  Testability: testable via literature (do topic-list/metadata-derived summaries reliably proxy full-source content?) and empirically (compare a topic-list-derived candidate against the same talk's transcript when it becomes available)
  Status: SEARCHED -- 15c disposition (2026-05-24): MONITOR (MONITOR-229 Medium/Weekly); 15a PARTIALLY-SUPPORTED (Moderate) / 15b PARTIALLY-CHALLENGED (Moderate) -- symmetric mixed evidence; staged metadata->PRS is sound but precondition-bound (verification must run; scope inferences to topic-level). Promote to INCORPORATE once proxy fidelity is measured on a labeled sample. Couples PRESUMPTION-242 + verification-gate items 240/243. See lit_search_returns.md (Batch 2026-05-24).
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-220
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit methodological self-disclosure in both 2026-05-23 Wolfram proposals (topic-list-derived, transcript unavailable, Medium-capped).
      15a/15b/15c (2026-05-24): searched FOR/AGAINST and dispositioned -> MONITOR-229; mirrored here by the 2026-05-24 14a run.
    Current status: SEARCHED

ASSUMPTION-221:
  Date identified: 2026-05-23
  Statement: Accountability for C2A2's own autonomous ("ownerless") tradition agents should be located in the human-AI deployment-and-verification pipeline -- specifically Tom's review gate as the verification layer -- rather than in any agent's internal predictability or in a single owner.
  Context: PROP-2026-05-23-002 (Wolfram, "accountability for ownerless AI") surfaces this as a meta-signal to the Master agent: Wolfram's framing is "usable as a primary-source warrant for how C2A2 should locate accountability (deployment + Tom's review gate as the verification layer)." Agent-surfaced by the Wolfram specialist, not yet a Tom-adopted design commitment.
  Type: architectural / normative (governance)
  Related decisions: (candidate governance stance; not yet a numbered DECISION)
  Related presumptions: PRESUMPTION-243, PRESUMPTION-240
  Related open questions: OPEN-065
  Testability: testable via literature (AI governance / accountability for autonomous agents; human-in-the-loop responsibility allocation) and empirically (does the review gate, in practice, function as the accountability layer?)
  Status: SEARCHED -- 15c disposition (2026-05-24): MONITOR (MONITOR-230 High/Weekly, INCORPORATE-pending-precondition); 15a SUPPORTED (Strong, locus -- meaningful-human-control, Santoni de Sio & van den Hoven 2018 [live-verified]; reinforced by Wolfram computational irreducibility) / 15b PARTIALLY-CHALLENGED (Moderate, conditional -- accountability requires an *exercised* gate; Green 2022 [live-verified], Elish 2019 moral crumple zone). Locus strongly supported; the operative precondition (an exercised, reason-responsive gate) is currently unmet (4-day signout; REVISE-050/051; SYSTEMIC-RISK-FLAG I). Promote to validated_premises.md once REVISE-050/051 resolve. See lit_search_returns.md (Batch 2026-05-24).
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-221
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the PROP-2026-05-23-002 meta-signal proposing the deployment+review-gate locus of accountability; flagged as agent-surfaced and awaiting human design adoption.
      15a/15b/15c (2026-05-24): searched FOR/AGAINST (key governance citations live-verified) and dispositioned -> MONITOR-230, INCORPORATE-pending-precondition; mirrored here by the 2026-05-24 14a run.
    Current status: SEARCHED (INCORPORATE-pending-precondition)

ASSUMPTION-222:
  Date identified: 2026-05-24
  Statement: Thematically convergent tradition-intake proposals that arrive in the same weekly batch -- specifically the Wright exegetical exile + Rohr contemplative exile + Stump corporate-substance cluster -- should be promoted into the network as a single unit rather than as separate proposals, on the grounds that together they articulate one paradigm-bridge (the Summa 2026 "loving unity as telos / reconciliation-without-erasure" theme).
  Context: 2026-05-24 sewing-agent weekly run (architecture/sewing_agent_log.md, item #3): "The Wright + Rohr exile/restoration + Stump corporate-substance cluster is, together, a direct articulation of the Summa 2026 central theme ... and is worth promoting as a unit rather than as three separate proposals." Agent-surfaced on an automated-pipeline day with no interactive Tom session; not yet a Tom-adopted promotion decision.
  Type: methodological
  Related decisions: (tradition-intake / synthesis-promotion methodology; not yet a numbered DECISION)
  Related presumptions: PRESUMPTION-244
  Testability: testable via literature (whether thematically clustered units are better knowledge-integration units than atomic items; theory-building/synthesis methodology) and empirically (does unit-promotion yield more durable/used bridge notes than item-by-item promotion?)
  Status: SEARCHED -- 15c disposition (2026-05-25): REVISE (REVISE-052; 15a PARTIALLY-SUPPORTED/Moderate, 15b CHALLENGED/Strong). The "promote as a single unit" rule is challenged at the structural-validity level (mono-method / common-batch variance, Campbell & Fiske 1959; Podsakoff et al. 2003). Recommended revision: require a cross-method / cross-occasion discriminant check before unit-promotion (re-elicit each source independently and confirm the bridge co-emerges), or promote individually and let convergence emerge via independent routing. See revision_flags.md REVISE-052 and lit_search_returns.md (Batch 2026-05-25).
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-222
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the sewing agent's explicit "promote as a unit" recommendation in the 2026-05-24 weekly log.
      15a/15b/15c (2026-05-25): searched FOR/AGAINST and dispositioned -> REVISE-052; mirrored here by the 2026-05-25 14a run.
    Current status: SEARCHED (REVISE-052 AWAITING-REVIEW)

ASSUMPTION-223:
  Date identified: 2026-05-24
  Statement: When a MONITOR item reaches cycle 4 with stable evidence and its blocker is an un-run empirical/paired test rather than unsettled literature, further weekly literature-search cycles are low-yield; the item should be STALE-flagged, downgraded (Weekly->Monthly), and escalated to a human for the empirical test.
  Context: 2026-05-24 15d periodic-monitor weekly run (review/15d_run_report_2026-05-24.md): first-ever STALE-MONITOR flags on ASSUMPTION-035, ASSUMPTION-037, PRESUMPTION-037 at cycle 4 -- "All three share a root cause: the blocker is an un-run empirical/paired test, not an unsettled literature, so further weekly literature cycles are low-yield."
  Type: methodological
  Related decisions: (monitor-cadence / stale-escalation policy; not yet a numbered DECISION)
  Related presumptions: PRESUMPTION-245
  Testability: testable empirically (do cycle-4+ literature re-searches on empirically-blocked items in fact yield no new dispositions?) and via literature (diminishing returns of repeated search; matching evidence-type to question-type in systematic review)
  Status: SEARCHED -- 15c disposition (2026-05-25): MONITOR (MONITOR-233 Medium/Weekly, INCORPORATE-pending-precondition); 15a SUPPORTED/Strong (diminishing returns / Cooper & Hedges 2009; matching evidence-type to question-type; SRE escalation practice Beyer et al. 2016) / 15b PARTIALLY-CHALLENGED/Moderate (the escalation leg presumes a reachable human endpoint contradicted by the current outage). The "stop-and-escalate" half is well-supported; the "escalation works" half couples to PRESUMPTION-245 -> REVISE-053 (escalation into the same dark gate). Promote to validated_premises.md once the human-endpoint precondition is satisfied (OPEN-066 / REVISE-053 resolve). See lit_search_returns.md (Batch 2026-05-25).
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-223
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 15d stale-flag rationale (the empirical-blocker-vs-literature-blocker distinction).
      15a/15b/15c (2026-05-25): searched FOR/AGAINST and dispositioned -> MONITOR-233, INCORPORATE-pending-precondition; mirrored here by the 2026-05-25 14a run.
    Current status: SEARCHED (INCORPORATE-pending-precondition)

ASSUMPTION-224:
  Date identified: 2026-05-24
  Statement: The connectivity/orphan metric should exclude `architecture/lit_search_results/` (the per-item *_for / *_against corpus), because that content is machine-generated material the Sewing Agent does not route; including it makes the orphan count fail to track real routing progress.
  Context: 2026-05-24 sewing-agent weekly run (architecture/sewing_agent_log.md, item #1): orphan count climbing 766 -> 1104 -> 1409, "dominated by content the Sewing Agent does not route"; recommendation (renewed from 2026-05-18) to exclude `architecture/lit_search_results/` "analogous to the existing architecture/metrics/ and review/archive/ exclusions." Standing Tom-decision item.
  Type: methodological / measurement
  Related decisions: (connectivity-metric definition; Tom-decision candidate, not yet a numbered DECISION)
  Related presumptions: PRESUMPTION-246
  Testability: testable empirically (recompute the orphan trend with the exclusion and check whether it then tracks thinker-agent routing actions) -- largely a measurement-definition choice
  Status: SEARCHED -- 15c disposition (2026-05-25): MONITOR (MONITOR-234 Low-Medium/Monthly); 15a PARTIALLY-SUPPORTED/Moderate (metric-scoping practice in software analytics) / 15b PARTIALLY-CHALLENGED/Moderate-Strong (the underlying validity of backlink-density as integration proxy is itself contested -- couples PRESUMPTION-246 / MONITOR-236; Goodhart family). The exclusion change is local and cheap; the metric's overall validity is the deeper issue. Recommended: run the cheap exclusion as a measurement-definition update AND treat the metric validity question on the monthly monitor. See lit_search_returns.md (Batch 2026-05-25).
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-224
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the renewed sewing-agent connectivity-metric recommendation.
      15a/15b/15c (2026-05-25): searched FOR/AGAINST and dispositioned -> MONITOR-234; mirrored here by the 2026-05-25 14a run.
    Current status: SEARCHED

ASSUMPTION-225:
  Date identified: 2026-05-25
  Statement: A 34-file / approximately 90-PRS-triplet / 12-tradition ingestion is too large and error-prone to execute unattended at the tail of the daily cycle; it belongs in a focused, ideally attended ingestion session where IDs, counts, cross-program entries, and pattern-detector evaluation can be reconciled and verified.
  Context: 2026-05-25 unattended daily-orchestrator run (flags/ingest_backlog_2026-05-25.md): the orchestrator detected 36 unrecorded files in `inbox/`, 35 of them approved (effective unique items = 34) from the 2026-05-13 decision batch, and DEFERRED rather than executed the ingest -- "deliberately deferred, not skipped." The flag explicitly cites caution-over-speed and fail-loud, and recommends an attended pass.
  Type: methodological / operational
  Related decisions: (deferred-action policy on bulk ingest; not yet a numbered DECISION)
  Related presumptions: PRESUMPTION-248
  Related open questions: OPEN-066 (the deferred-to-attended path terminates at the same dark gate)
  Testability: testable empirically (compare attended vs unattended bulk-ingest error rates at varying batch sizes; measure recovery cost when an unattended run does err)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-225
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit "deliberately deferred, not skipped" + "belongs in a focused (ideally attended) session" rationale in `flags/ingest_backlog_2026-05-25.md`.
    Current status: UNTESTED

ASSUMPTION-226:
  Date identified: 2026-05-25
  Statement: A daily-walk Chat conversation occurring on a day with no Cowork desktop session should be counted as an interactive Tom session for daily-shape framing and changelog/metrics purposes; framing such a day as "no interactive session" because Cowork did not fire is a Rule-12 fail-loud violation (silently overrunning the actual day-shape).
  Context: 2026-05-25 evening cowork-to-chat agent self-correction (architecture/daily_sync/cowork_to_chat/2026-05-25_cowork_summary.md): "I had originally written it up as a third automated-pipeline day, no interactive session. That's true for *Cowork desktop* sessions, but you did have a daily-walk *Chat* session -- so I revised the summary to reflect both, rather than leaving the inaccurate 'no interactive session' claim (fail-loud)."
  Type: methodological / measurement
  Related decisions: (day-shape classification; the "interactive Tom session" definition used by both 14a/14b daily framing and the cadence-streak counter)
  Related presumptions: PRESUMPTION-249
  Testability: testable empirically (does treating Chat as interactive vs not change the extracted-item count / composition; does it change the presumption:assumption ratio's signal of "automated day" vs "human day"?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-226
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from the cowork-to-chat agent's explicit framing-correction self-disclosure in the 2026-05-25 evening sync.
    Current status: UNTESTED

ASSUMPTION-227:
  Date identified: 2026-05-25
  Statement: A daily-sync delivery to Tom should LEAD with whichever finding closes the loop on the morning walk's open question (when one exists), not the chronologically-first or sectional-default item; closing an open Tom-Chat thread takes priority over standard report ordering.
  Context: 2026-05-25 evening cowork-to-chat agent (same source): "I led the delivery with that answer to close the loop." The choice was explicit and architecturally framed: when the morning walk surfaced a specific question (here: lagging-metric vs real consumption gap on the ~40 approved proposals), the evening delivery is structured to answer that question first.
  Type: methodological / communicative-design
  Related decisions: (daily-sync message-ordering policy; not yet a numbered DECISION)
  Related presumptions: PRESUMPTION-250
  Testability: testable empirically (compare uptake / action rates of loop-closing-first messages vs default-ordered messages over a multi-week sample)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-227
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the cowork-to-chat agent's stated ordering choice in the 2026-05-25 evening sync.
    Current status: UNTESTED

ASSUMPTION-228:
  Date identified: 2026-05-25
  Statement: The C2A2 community-model GPRS articulation (goals / problems / resources have-tap-need / solutions) is structurally homologous to Levin & Lyons' "shared model of relative scarcities" as the cognitive glue of a collective; the price-system-as-template thesis therefore supplies an external, peer-reviewed mechanism for how a C2A2 community coordinates and accelerates.
  Context: PROP-2026-05-25-001 (Levin & Lyons, "Cognitive glues are shared models of relative scarcities"; inbox/proposals/pending/2026-05-25_levin_cognitive-glues-economics-collective-intelligence.md) cross-tradition signals -- "Loughran / C2A2 master -- strong: This paper is nearly a theoretical charter for the C2A2 community model (self-first GPRS articulation: goals / problems / resources have-tap-need / solutions). 'Resources have-tap-need' is literally a relative-scarcity model. Levin & Lyons supply an external, peer-reviewed mechanism for why a community that shares a scarcity model can coordinate and accelerate. Flag as a paradigm-relevant import for the Community Explorer / GPRS framing." Agent-surfaced by the Levin specialist; not yet a Tom-adopted import.
  Type: architectural / epistemic
  Related decisions: (Community Explorer / GPRS framing as scarcity-model coordination; not yet a numbered DECISION)
  Related presumptions: PRESUMPTION-251
  Testability: testable via literature (collective-intelligence / coordination-under-scarcity; market-as-information-system theory; FEP precision-weighting as scarcity allocation) and empirically (does the C2A2 community in fact exhibit price-like signals among participants, or only Tom-as-conductor coordination?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-228
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit "theoretical charter ... resources have-tap-need is literally a relative-scarcity model" framing in the Levin specialist's cross-tradition signals.
    Current status: UNTESTED

ASSUMPTION-229:
  Date identified: 2026-05-25
  Statement: Leading theories of consciousness are substrate-permissive in principle -- their brain-focus is a convention of imagination rather than a theoretical necessity -- so the substrate-independence thesis is portable from cognition to consciousness for purposes of the C2A2 master's load-bearing AI-membership question (PRS-31).
  Context: PROP-2026-05-25-002 (Rouleau & Levin, "Brains and where else?"; inbox/proposals/pending/2026-05-25_levin_brains-and-where-else-consciousness-embodiments.md) cross-tradition signals -- "Loughran / C2A2 master -- relevant: strengthens the load-bearing AI-membership question (PRS-31) -- if consciousness theories are substrate-permissive in principle, the case for AI agents as candidate sites of subjective perspective gets stronger on the Levin side of the deferred criterion." Cited evidence: "the operations and functional principles described or predicted by most theories of consciousness are remarkably similar, with the focus on brains being more driven by convention and limitations of imagination than by any specific content of existing theories."
  Type: architectural / epistemic
  Related decisions: (AI-membership criterion for the C2A2 master; not yet a numbered DECISION)
  Related presumptions: (none registered yet; couples deferred-criterion presumption cluster)
  Testability: testable via literature (the Rouleau & Levin 2026 mapping itself; IIT / GWT / HOT / AST substrate requirements; counter-arguments for genuine neural specificity in consciousness)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-229
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Rouleau & Levin paper's central claim as adopted by the Levin specialist's cross-tradition signal to the C2A2 master, with the consciousness/AI-membership coupling stated explicitly.
    Current status: UNTESTED

ASSUMPTION-230:
  Date identified: 2026-05-26
  Statement: When the Gmail decision-email body and the review-page state disagree about proposal-approval values, the review-page state (verified by direct paste into Cowork plus Tom's verbal confirmation) is authoritative; the email body is non-authoritative until the decision-email generator is fixed.
  Context: 2026-05-26 attended Cowork session at 17:42 ET (review/archive/2026-05-26_decisions.md): the 17:25Z Gmail decision-email carried all-PENDING values despite the review page showing 25 approvals. Tom pasted the review-page state directly into Cowork; the 25 APPROVE decisions were executed from that paste plus a verbal "approve all 28" intent. The cowork-to-chat summary explicitly flags: "This deserves a numbered DECISION tomorrow (review-page state is the source of truth when email and page disagree), plus a UI/workflow fix on the decision-email-generation side."
  Type: methodological / operational
  Related decisions: (candidate; not yet a numbered DECISION; flagged for DECISION-048 tomorrow)
  Related presumptions: PRESUMPTION-254
  Testability: testable empirically (audit past Gmail decision-email runs against their paired review-page states; measure mismatch rate and identify the misfire condition)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-230
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the cowork-to-chat summary section "Key Decisions Made" + "For Morning Discussion #2" explicit framing; corroborated by the 2026-05-26 attended-session archive note ("the email body was *not* used as the authority -- the review-page state and Tom's verbal confirmation were").
    Current status: UNTESTED

ASSUMPTION-231:
  Date identified: 2026-05-26
  Statement: Tom's stated intent ("approve all 28 from the start") is sufficient to reclassify items that the review-page UI showed as Pending; verbal/textual intent applies retroactively to status-field state and overrides UI categorization within the same attended session.
  Context: 2026-05-26 attended Cowork session: after the initial 25-APPROVE batch was executed from the pasted review-page state, Tom issued an explicit "include 3 Wrights" follow-up; these were the 3 N.T. Wright items that had appeared as Pending in the review-page UI but whose inclusion was Tom's intent from the start. All 3 were reclassified to APPROVE in the same session. (Source: review/archive/2026-05-26_decisions.md.)
  Type: methodological / operational
  Related decisions: (related to candidate DECISION-048; not yet numbered)
  Related presumptions: PRESUMPTION-254, PRESUMPTION-258
  Testability: framework commitment (operational policy for handling intent-vs-UI mismatches) -- not directly testable as a literature claim; testable empirically by tracking how often verbal-intent corrections later prove inconsistent with the originally-stated UI state
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-231
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 3-Wright follow-up framing in the cowork-to-chat summary ("Tom's intent had been 'approve all 28' from the start") and the archive note's explicit reclassification record.
    Current status: UNTESTED

ASSUMPTION-232:
  Date identified: 2026-05-26
  Statement: Tom confirms that the prior 36-file ingest backlog (source-dated 2026-04-21 to 2026-05-12, moved pending/->approved/+inbox/ by the 2026-05-13 batch but never committed) is intended for go-live; today's commit folds those previously-uncommitted moves in, truing up git state to match on-disk filesystem.
  Context: 2026-05-26 attended Cowork session (flags/ingest_backlog_2026-05-25.md updated in place; review/archive/2026-05-26_decisions.md): Tom explicitly confirmed go-live intent for the prior 36-file backlog. The HIGH-severity ingest-backlog flag was updated with the EOD addendum ("escalated 2026-05-26 17:42 ET -> reaffirmed 2026-05-26 EOD"). Ingest queue total after today's confirmation + today's 28: 62 real proposals + 2 stub-file artifacts across 12 traditions.
  Type: architectural / operational
  Related decisions: (operational go-live confirmation; not a new numbered DECISION; settles the ambiguity raised by ASSUMPTION-225 / PRESUMPTION-248)
  Related assumptions: ASSUMPTION-225 (defer-to-attended policy)
  Related presumptions: PRESUMPTION-248 (defer-as-bottleneck-relabel), PRESUMPTION-252 (approval-vs-ingest decoupling)
  Testability: framework commitment (intent-confirmation; not directly literature-testable); operational outcome testable empirically (does the next focused-attended PRS-extraction session in fact ingest all 62 within Tom's planned 2-3-hour block, or does scope creep / batch error force partial completion?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-232
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the cowork-to-chat summary's headline statement ("Tom also explicitly confirmed go-live intent for the prior 36-file backlog") + the in-place flag update note. Settles the prior day's "defer to attended" ambiguity for the approval/commit half of the pipeline; the PRS-extraction half remains deferred.
    Current status: UNTESTED

ASSUMPTION-233:
  Date identified: 2026-05-26
  Statement: A focused ingest of ~62 proposals across 12 traditions is best executed as tradition-batched sub-runs (wolfram first, then levin, then rohr, then carroll, then wright, then fredrickson, then mcgilchrist, then stump, then friston, then hoffman, then kastrup, then arkanihamed) rather than a monolithic single pass, with natural break-points at each tradition boundary.
  Context: 2026-05-26 evening cowork-to-chat summary "What's Next #1" + "For Morning Discussion #3": "Recommended cadence: 2-3 hour dedicated block, run by tradition-batch (wolfram first, then levin, then rohr, then carroll, ...)" -- explicitly orders the 12 traditions and predicts "an hour per top-3 tradition, half an hour per long-tail."
  Type: methodological / operational
  Related decisions: (focused-ingest cadence design; not yet a numbered DECISION)
  Related assumptions: ASSUMPTION-225 (defer-to-attended)
  Related presumptions: PRESUMPTION-255, PRESUMPTION-258
  Testability: testable empirically (compare batch-error rates of tradition-batched ingest vs monolithic ingest on labeled samples; measure per-tradition completion times against the predicted "hour for top-3 / half-hour for long-tail" model)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-233
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from the cowork-to-chat summary's "tradition-batch cadence" recommendation and the explicit ordering of the 12 traditions.
    Current status: UNTESTED

ASSUMPTION-234:
  Date identified: 2026-05-26
  Statement: The first tradition-batch in the focused-ingest session (wolfram = 10 files) functions as a protocol test-run -- its outcome (per-file processing time, error rate, cross-program-index update correctness, pattern-detector behavior) dictates whether the same cadence carries through to the remaining 11 traditions or whether the protocol needs revision before continuing.
  Context: 2026-05-26 evening cowork-to-chat summary "For Morning Discussion #3": "The first batch (wolfram = 10 files) is also the test-run for the protocol." The 12-tradition ordering is structured so that the largest tradition (wolfram, 10 files) is processed first, giving the most statistical power for protocol validation before the remaining 52 files commit to the same cadence.
  Type: methodological
  Related decisions: (focused-ingest protocol-validation cadence; not yet a numbered DECISION)
  Related assumptions: ASSUMPTION-233
  Related presumptions: PRESUMPTION-255
  Testability: testable empirically (compare wolfram-batch outcomes against the cadence assumed for tradition-batches 2-12; measure whether wolfram-batch errors generalize or are tradition-specific; track whether the cadence is in fact revised after wolfram-batch)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-234
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit "test-run for the protocol" framing in the cowork-to-chat summary.
    Current status: UNTESTED

ASSUMPTION-235:
  Date identified: 2026-05-26
  Statement: The underlying bottleneck for human-terminating queues (REVISE, STALE, INCORPORATE-pending, deferred-ingest) is sit-down availability -- demonstrated today by a 10-second re-login that ended a 6-day signout and was immediately followed by an attended Cowork session draining two queues to zero in minutes -- not queue/policy design; the queue/policy fix REVISE-053 (unified needs-Tom queue + age/escalation/safe-default tiers) is real and lit-validated, but secondary to the sit-down-arrival problem.
  Context: 2026-05-26 evening cowork-to-chat summary "For Morning Discussion #1": "What flipped this open: the 10-second re-login that ended the 6-day signout -- and a single attended Cowork session immediately drained two human-terminating queues. This is the empirical answer to OPEN-066: the queue/policy fix is *real* (and now lit-validated as REVISE-053), but the underlying bottleneck genuinely is a sit-down, not a queue-design issue."
  Type: architectural / scaling
  Related decisions: (extends DECISION-048 candidate; addresses OPEN-066 with an empirical answer)
  Related open questions: OPEN-066 (which routes share the bottleneck), OPEN-067 (NEW: how to make sit-down arrival reliable on a useful cadence)
  Related presumptions: PRESUMPTION-256, PRESUMPTION-258
  Related assumptions: ASSUMPTION-225 (defer-to-attended); PRESUMPTION-240/245/248 (the three prior bottleneck-route findings)
  Testability: testable empirically (track future signouts: do they all resolve in ~10 seconds? do attended sessions consistently drain queues in minutes? track human-terminating-queue age vs sit-down-event frequency)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-235
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from the cowork-to-chat summary's "For Morning Discussion" framing of today's empirical finding. This is the central architectural claim of the day: the bottleneck diagnosis shifts from queue-design to attention-arrival.
    Current status: UNTESTED

ASSUMPTION-236:
  Date identified: 2026-05-26
  Statement: A reliable ~1-week-cadence "sit-down day" is the right operational target for draining human-terminating queues; the design question prompted by the 6-day signout is what mechanism reliably triggers such a sit-down on that cadence, given that today's drainage happened only because a re-login event accidentally co-occurred with sufficient block-time and Tom's intent to clear queues.
  Context: 2026-05-26 evening cowork-to-chat summary "For Morning Discussion #1": "The right design question on the walk is: what makes a 'sit-down day' reliably arrive on a 1-week cadence, given the 6-day signout was the actual failure mode (not the absence of a queue)?" The 1-week cadence is named explicitly as the target.
  Type: architectural / operational
  Related decisions: (design-target for sit-down-arrival mechanism; not yet a numbered DECISION)
  Related open questions: OPEN-067 (NEW)
  Related assumptions: ASSUMPTION-235
  Related presumptions: PRESUMPTION-256, PRESUMPTION-257
  Testability: testable empirically (track inter-arrival times of attended Cowork sessions over 6-12 weeks; measure variance; check whether any deliberate triggering mechanism in fact stabilizes the 1-week cadence)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-236
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the cowork-to-chat summary's explicit "1-week cadence" target and the framing of the design question as a triggering-mechanism problem.
    Current status: UNTESTED

ASSUMPTION-237:
  Date identified: 2026-05-27
  Statement: The Supabase broker v4 `web_enrich` action wraps Tavily search results into a `WEB_CONTEXT` block appended to the system prompt before the OpenRouter call; the LLM cites sources with numeric `[n]` markers; the client receives `{text, source, model, freeRemaining, webRemaining, sources: [{url, title, snippet}]}` and is responsible for citation rendering.
  Context: 2026-05-27 attended Cowork session ("Next steps" + "Supabase and Open Router integration" + "Next steps after push") culminating in the v4 contract proposal in the "Next steps" transcript. Numeric markers were Claude's explicit pick ("gpt-4o-mini handles them reliably and they're trivial to parse client-side"). Tom signed off on the broker live and the seam, per the closing of the Supabase session ("broker live, seam shipped, research-tier caps in place, all verified end-to-end").
  Type: architectural
  Related decisions: (broker-v4 web_enrich; pending Tom numbering as candidate DECISION-049 -- not yet filed)
  Related assumptions: ASSUMPTION-238, ASSUMPTION-239, ASSUMPTION-240
  Related presumptions: PRESUMPTION-260, PRESUMPTION-261
  Testability: testable empirically (compare [n]-citation parsing reliability vs [title]-citation under gpt-4o-mini and other openrouter models; measure broker latency under WEB_CONTEXT-block-of-5-results vs no enrichment) and via literature (RAG retrieval-augmented-generation citation-rendering best practices)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-237
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the "Next steps" session contract proposal (request body, broker flow steps 1-8, response shape) and the "Supabase and Open Router integration" sign-off confirmation.
    Current status: UNTESTED

ASSUMPTION-238:
  Date identified: 2026-05-27
  Statement: The broker stays generic -- the `tab` request field (community | sociogram | connectome | agent_map | curriculum) is analytics-only and does NOT gate behavior server-side. Per-tab caps, per-tab templates, and per-tab routing live on the client as payload adapters and UI render adapters; if per-tab caps are wanted later, "that's a one-column-add to the schema."
  Context: 2026-05-27 attended Cowork session ("Next steps" transcript): "**The `tab` field is purely analytics.** It does *not* gate behavior server-side (no per-tab caps, no per-tab template lookup). That keeps the broker generic." Flagged as one of two questions for sign-off; closed in the "Supabase and Open Router integration" session's "all verified end-to-end" message.
  Type: architectural
  Related decisions: (broker-v4 generic-routing commitment)
  Related assumptions: ASSUMPTION-237
  Related presumptions: PRESUMPTION-261, PRESUMPTION-268
  Testability: testable empirically (measure whether downstream tab-specific behavior requirements appear within 6-12 weeks of broker-v4 ship; if they do, the "one-column-add" migration cost materializes) and via literature (generic-API vs domain-aware-API design tradeoffs in multi-tenant brokers)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-238
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the "Next steps" session "Two things I want to flag before sign-off" block and the analytics-only framing.
    Current status: UNTESTED

ASSUMPTION-239:
  Date identified: 2026-05-27
  Statement: The web_enrich action requires two new counter columns on the usage table (`web_asks`, `web_cost_cents`) and two new RPCs (`get_web_usage`, `increment_web_usage`) mirroring the existing dataset-enrich counters; hard daily caps are `WEB_DEVICE_DAILY_LIMIT = 20` per device and `WEB_GLOBAL_DAILY_CENTS_CAP = 300` ($3/day global), with separate counters from dataset enrich so the two pools do not contaminate each other.
  Context: 2026-05-27 "Next steps" transcript broker-flow step 2 and the "Migration delta" block: explicit constants, explicit mirror-pattern, explicit separation rationale.
  Type: architectural / operational
  Related decisions: (broker-v4 web-counter migration; candidate DECISION-049-adjacent)
  Related assumptions: ASSUMPTION-237
  Related presumptions: PRESUMPTION-260
  Testability: testable empirically (measure actual web_asks and web_cost_cents trajectories over the first 30 days of broker-v4 ship; check whether 20/device/day and $3/day global are over- or under-provisioned vs realized usage) and via literature (multi-tenant API cost-cap design in OpenAI-broker patterns)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-239
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit constants and migration-delta language in the "Next steps" contract proposal.
    Current status: UNTESTED

ASSUMPTION-240:
  Date identified: 2026-05-27
  Statement: The 2026-05-18 first-newline truncation bug (auto-send `type`-with-newlines path collapses to first-line-only; header sent alone, body cut at first `\n`) recurred today on the evening Cowork-to-Chat delivery; the 2026-05-18 diagnosis stands but "the fix did not land or was not attempted." The Tiptap/ProseMirror `execCommand('insertText')` path preserves paragraph breaks and is the correct re-send mechanism for truncated body messages.
  Context: 2026-05-27 cowork_summary.md delivery-note header: "the first-newline truncation bug recurred (same shape as the 2026-05-18 incident...). Morning-walk Claude (Opus 4.7 Adaptive) immediately recognized the recurrence and stood by for the body. The body was re-delivered as a follow-up message via the Tiptap/ProseMirror `execCommand('insertText')` path (which inserts paragraph breaks properly) and Claude responded substantively. ... This is a Pathway-14 honesty-layer recurrence worth canonizing -- the auto-send `type`-with-newlines path collapses to first-line-only and has done so on at least two separate evening syncs nine days apart. The diagnosis from 05-18 stands; the fix did not land or was not attempted."
  Type: methodological / operational / self-referential
  Related decisions: (delivery-path remediation; not yet a numbered DECISION; was a Pathway-14 honesty-layer item on 2026-05-18)
  Related assumptions: ASSUMPTION-242 (canonization-as-fix)
  Related presumptions: PRESUMPTION-262, PRESUMPTION-263
  Testability: testable empirically (instrument the next 10 evening Cowork-to-Chat deliveries; measure whether the truncation recurs under `type`-with-newlines and whether the `execCommand('insertText')` path holds 100% in the alternative) and methodologically (does naming-the-recurrence-in-the-md-header without a code-level fix correlate with non-recurrence on day N+9 or not?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-240
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from the cowork_summary's delivery-note header, including the explicit "the fix did not land or was not attempted" framing.
    Current status: UNTESTED

ASSUMPTION-241:
  Date identified: 2026-05-27
  Statement: The operational rule "pasted review-page state is the source of truth; intent supersedes UI state when explicitly stated" is the right closure on the 2026-05-26 Gmail decision-email misfire loop on the operational side, ahead of any email-generation-side fix. The DECISION-048 candidate from yesterday (review-page state authoritative when Gmail decision-email body disagrees) is unchanged in shape today but extended in scope: "intent supersedes UI state when explicitly stated" (handling the 3-Wright case where the page UI itself was misleading).
  Context: 2026-05-27 chat_summary.md "Action Items Mentioned" item 5: "File a numbered DECISION on review-page-state as source of truth." And the morning-thread "Open Questions" item: "Two-layer ground-truth problem from the Gmail misfire: the email body misled, AND the page UI misled on the 3 Wrights. Operational rule needs canonization before a generation-side fix lands." This refines DECISION-048-candidate (which was about review-page-vs-email) to also cover review-page-UI-vs-stated-intent.
  Type: methodological / operational
  Related decisions: DECISION-048 (still candidate; numbering owed)
  Related assumptions: ASSUMPTION-231 (intent overrides UI categorization)
  Related presumptions: PRESUMPTION-254 (UI itself not always reliable; rule may need to be "stated intent overrides both")
  Testability: testable empirically (track the next 6 weeks of approval-flow events; count misfire incidents resolved by intent-supersedes-UI rule vs missed by it) and via literature (provenance / source-of-truth conventions in approval-workflow systems with multi-surface state)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-241
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the chat_summary's morning-thread Open Questions and Action Items canonization request.
    Current status: UNTESTED

ASSUMPTION-242:
  Date identified: 2026-05-27
  Statement: "Canonizing the truncation recurrence in the `.md` header as a Pathway-14 honesty-layer event" is a substantive response to a known broken path; the system explicitly notes "the auto-send `type`-with-newlines path is a known broken path that wasn't fixed after 05-18" and treats the canonization in the header as the action taken today on this matter (no code-level fix attempted on 2026-05-27).
  Context: 2026-05-27 evening Cowork-to-Chat session transcript ("C2a2 evening cowork to chat") summary text: "The truncation recurrence is canonized in the `.md` header as a Pathway-14 honesty-layer event -- the auto-send `type`-with-newlines path is a known broken path that wasn't fixed after 05-18."
  Type: methodological / self-referential
  Related decisions: (no numbered DECISION; tacit policy decision to treat naming as the response)
  Related assumptions: ASSUMPTION-240
  Related presumptions: PRESUMPTION-263, PRESUMPTION-264
  Testability: testable empirically (does the next evening sync attempt the `type`-with-newlines path again, and does it again truncate? if both yes, naming-as-action did not change behavior; if either no, naming had some operational effect) and via literature (whether "honesty-layer canonization" patterns in incident-response correlate with subsequent fix rates)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-242
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from the evening cowork session's transcript framing of the canonization as the response.
    Current status: UNTESTED

ASSUMPTION-243:
  Date identified: 2026-05-28
  Statement: The Sociogram-tab AI search wired in today -- via a new shared `wiki/lib/c2a2-search.js` module that `community/app.js` delegates through, and that the narration generator's new "Ask AI" + "External" checkboxes feed a `runSearch` AI branch routed through the broker's `enrich` action -- is the per-tab adapter pattern the broker-v4 architecture (candidate DECISION-049) was designed to enable; today's working integration is the first demonstrated instance of the pattern.
  Context: 2026-05-28 evening cowork-to-chat summary "What Was Accomplished Today" (headline build) + "Key Decisions Made" (NEW today, un-numbered: "AI-search-as-shared-module delegation pattern (per-tab consumers via c2a2-search.js; broker action `enrich` routed server-side; `[database]` mode label as proof of routing). This is the per-tab adapter pattern the broker-v4 design called for, now demonstrated working in the Sociogram tab.")
  Type: architectural
  Related decisions: DECISION-049 candidate (broker-v4 web_enrich architecture, from 2026-05-27); NEW today (un-numbered): AI-search-as-shared-module delegation pattern
  Related assumptions: ASSUMPTION-237, ASSUMPTION-238, ASSUMPTION-244
  Related presumptions: PRESUMPTION-267, PRESUMPTION-272
  Testability: testable empirically (extend the same delegation pattern to Connectome, Agent Map, Curriculum Tools; measure whether per-tab payload-adapter code stays small and the shared module remains stable across the 4 tabs) and via literature (per-tab adapter patterns; shared-module + thin-consumer architectures in multi-surface web apps)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-243
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the cowork-to-chat summary's headline build statement and the explicit "this is the per-tab adapter pattern" framing in Key Decisions.
    Current status: UNTESTED

ASSUMPTION-244:
  Date identified: 2026-05-28
  Statement: End-to-end verification of the AI-search integration consisted of: a single happy-path query ("What does Karl Friston mean by the free energy principle") returning a database-routed answer through the broker; node-dimming behaving correctly; all 4 chapter tabs + 5 Accelerator sub-tabs intact; zero console errors. This is treated as sufficient evidence to stage the 5-file changeset and await Tom's push sign-off.
  Context: 2026-05-28 evening cowork-to-chat summary: "End-to-end verification clean: a 'What does Karl Friston mean by the free energy principle' query returned a database-routed answer through the broker, node-dimming behaved, all 4 chapter tabs + 5 Accelerator sub-tabs intact, zero console errors. Changeset is staged and awaiting Tom's push sign-off (the constitutional no-blind-push rule held)."
  Type: methodological / operational
  Related decisions: NEW today (un-numbered): AI-search-as-shared-module delegation pattern; DECISION-049 candidate
  Related assumptions: ASSUMPTION-243, ASSUMPTION-245
  Related presumptions: PRESUMPTION-272
  Testability: testable empirically (run the next 30 cross-tradition queries through the new path; measure whether single-happy-path-plus-tab-integrity predicts production reliability) and via literature (ship-readiness criteria for shared-module integrations; how many queries / coverage modes are typically required before a single-query test is treated as sufficient)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-244
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from the evening summary's verification description.
    Current status: UNTESTED

ASSUMPTION-245:
  Date identified: 2026-05-28
  Statement: The constitutional "no-blind-push" rule held today: the 5-file AI-search changeset is staged and awaiting Tom's push sign-off; the agent did not push autonomously. This is the project's standing commitment that the git push remains a Tom-side host-shell step (cf. DECISION-042-candidate / DECISION-043-candidate process commitment from 2026-05-20/22).
  Context: 2026-05-28 evening cowork-to-chat summary closing line on the AI-search build: "Changeset is staged and awaiting Tom's push sign-off (the constitutional no-blind-push rule held)." Also the "What's Next #1" item: "Tom's push sign-off on the AI-search shared-module changeset (5 files; verified working)."
  Type: architectural / process / normative
  Related decisions: DECISION-042 candidate, DECISION-043 candidate (process commitment to host-shell-push)
  Related assumptions: ASSUMPTION-244
  Related presumptions: PRESUMPTION-269
  Testability: testable empirically (track over the next 5.5 weeks whether the no-blind-push rule continues to be honored, whether it ever becomes the bottleneck on a demo-path-shaped change, and whether the rule scales through ISME-pre-demo cadence) and via literature (constitutional-rule design in agentic systems; the cost of human-in-the-loop on the git push step)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-245
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit "constitutional no-blind-push rule held" framing.
    Current status: UNTESTED

ASSUMPTION-246:
  Date identified: 2026-05-28
  Statement: The swarm contract written to root `architecture/` as ground truth and mirrored into `wiki/architecture/swarm-contract.md` (so Obsidian picks it up) is the appropriate ground-truth document for the two new weekly watch agents (`connector-health-weekly`, `reviewer-review-weekly`); the architectural-reviewer is pinned in the contract's "Open additions (deferred)" section and in memory for post-ISME.
  Context: 2026-05-28 evening cowork-to-chat summary "Files Created or Modified": "Swarm contract (NEW): `wiki/architecture/swarm-contract.md` (mirror of root architecture/)" + "Parallel deployments closed two long-standing watch agents... The swarm contract was written to root `architecture/` as ground truth and mirrored into `wiki/architecture/swarm-contract.md` so Obsidian picks it up; the architectural-reviewer was pinned for post-ISME."
  Type: architectural / process
  Related decisions: NEW today (un-numbered): two new weekly watch agents registered against swarm contract
  Related assumptions: ASSUMPTION-247
  Related presumptions: PRESUMPTION-270, PRESUMPTION-274
  Testability: testable empirically (track over 12 weeks whether the root vs wiki mirror drift; whether either copy is ever updated independently; whether the two new watch agents in fact consult the contract on each run) and via literature (canonical-source vs mirrored-copy ground-truth patterns; the cost of double-source-of-truth in operational documentation)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-246
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit ground-truth + mirror language and the explicit pinning of the architectural-reviewer for post-ISME.
    Current status: UNTESTED

ASSUMPTION-247:
  Date identified: 2026-05-28
  Statement: The baseline-then-delta cadence pattern (Week 1 outputs are reference snapshots, not findings; real signal starts Week 2) is the right starting cadence for both new watch agents (`connector-health-weekly` first run 2026-05-31 Sun 06:19 local; `reviewer-review-weekly` first run 2026-06-01 Mon 06:37 local); the pattern follows the earlier janitor agent (`c2a2-wiki-janitor-weekly`, Sun 05:45 local).
  Context: 2026-05-28 evening cowork-to-chat summary on the new agents: "both following the janitor's baseline-then-delta pattern (real signal Week 2)" + 2026-05-28 cleanup-agent-deployment session summary: "First-run baselines will look quiet. Both agents follow the janitor's baseline-then-delta pattern, so this Sunday/Monday's outputs are reference snapshots, not findings. Real signal starts the second weekend."
  Type: methodological / operational
  Related decisions: NEW today (un-numbered): scheduling decisions for the two new weekly watch agents
  Related assumptions: ASSUMPTION-246
  Related presumptions: PRESUMPTION-268
  Testability: testable empirically (compare Week 1 vs Week 2 output of each new agent; verify that Week 1 surfaces no false-positive deltas because there is no prior state to compare against; measure whether "real signal Week 2" is actually achieved or whether the baseline takes longer to stabilize) and via literature (baseline-stabilization periods in monitoring-system rollouts; the cost of treating Week 1 as a non-finding window)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-247
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit "baseline-then-delta" framing and the noted parallel to the janitor agent's first-run behavior.
    Current status: UNTESTED

ASSUMPTION-248:
  Date identified: 2026-05-28
  Statement: The janitor agent's deliberate design choices -- dropped orphan/sparse detection (the sewing agent already owns this and writes `wiki/architecture/metrics/connectivity_log.csv`); dropped unreferenced-images / frontmatter-schema-drift / empty-section / dead-end-wikilink checks (no `attachments/` folder; schemas vary too much across node types for v1; the last two are heuristics with too many false positives) -- were surfaced as explicit design choices rather than skipped silently. Easy to add later.
  Context: 2026-05-28 evening cowork-to-chat summary on the janitor: "Four janitor checks were dropped during build -- orphan/sparse (the sewing agent owns this), unreferenced-images, frontmatter-schema-drift, empty-section, dead-end-wikilink -- surfaced as deliberate design choices rather than skipped silently." Also the 2026-05-28 "Status and next steps" session transcript: "Decisions I made without asking, worth flagging: 1. Dropped orphan/sparse detection from janitor. Your `c2a2-sewing-agent-weekly` already owns that... Two agents reporting different opinions about the same orphan files would be its own polish problem. 2. Dropped unreferenced-images, frontmatter-schema-drift, empty-section, dead-end-wikilink. No `attachments/` folder exists; frontmatter schemas vary too much across node types for v1; the last two are heuristics that produce too many false positives. Easy to add later."
  Type: architectural / methodological
  Related decisions: NEW today (un-numbered): janitor-design check-set
  Related assumptions: (none directly)
  Related presumptions: PRESUMPTION-275
  Testability: testable empirically (over 12 weeks, track whether any of the dropped check categories produces a real signal that the janitor + sewing agent pair misses, and whether the "easy to add later" claim holds when re-introduction is attempted) and via literature (linter/audit-tool check-set design; the cost of false-positive-heavy heuristics in self-awareness pipelines)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-248
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit "deliberate design choices rather than skipped silently" framing -- itself a Rule-12 fail-loud move.
    Current status: UNTESTED

ASSUMPTION-249:
  Date identified: 2026-05-28
  Statement: ISME is now ~5.5 weeks out; demo-path-shaped work continues to be the prioritization tiebreaker. The Sociogram-tab AI search wired today via shared `c2a2-search.js` delegation is "exactly the per-tab adapter pattern the broker-v4 architecture... was designed to enable" -- and is concretely good demo-path-shaped work shipping today.
  Context: 2026-05-28 evening cowork-to-chat "For Morning Discussion #2": "Today's demo-path build was concretely good. The Sociogram-tab AI search via shared `c2a2-search.js` delegation is exactly the per-tab adapter pattern the broker-v4 architecture (candidate DECISION-049) was designed to enable. End-to-end verification clean; this is demo-path-shaped work shipping." Also "For Morning Discussion #1" closing: "...given ISME is now ~5.5 weeks out?" Yesterday's chat summary closing: "ISME is six weeks out. The demo path is still the demo path."
  Type: methodological / scaling / operational
  Related decisions: (prioritization-tiebreaker framing; not yet a numbered DECISION)
  Related assumptions: ASSUMPTION-243, ASSUMPTION-250
  Related presumptions: PRESUMPTION-267, PRESUMPTION-273
  Testability: testable empirically (track over the next 5.5 weeks how many attended-session decisions are tiebroken by the demo-path heuristic; measure whether demo-readiness in fact arrives at ISME; check whether the heuristic obscures non-demo work that becomes load-bearing) and via literature (deadline-driven prioritization heuristics; demo-path-shaped tiebreakers in research-software contexts; how ISME-style external constraints affect attended-time allocation in human-in-the-loop systems)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-249
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit ISME ~5.5-week framing and the "demo-path-shaped work shipping" judgment.
    Current status: UNTESTED

ASSUMPTION-250:
  Date identified: 2026-05-28
  Statement: The 4th-consecutive-cycle FLAG-I recursion observed today (multiple attended Cowork sessions on AI-search wiring, agent registrations, janitor deployment, branch publishing, resume-session orientation, Physics Explorer attempt -- and PRS extraction did not happen) is strong enough empirical evidence to ask the second-order framing question explicitly: is "do the wolfram canary" actually the right framing, or is the demo-path infrastructure work in fact the higher-leverage attended-session use given ISME ~5.5 weeks out? REVISE-058's multi-failure-mode framing applies; the binary "PRS-extraction-or-failure" diagnosis may itself be the third-category subordination PRESUMPTION-259 keeps surfacing.
  Context: 2026-05-28 evening cowork-to-chat summary "For Morning Discussion #1": "The FLAG-I recursion empirically advanced again. Today had multiple attended Cowork sessions (AI-search wiring, agent registrations, janitor deployment, branch publishing, resume-session orientation, Physics Explorer attempt) and PRS extraction did not happen. That's the 4th consecutive cycle of the FLAG-I pattern REVISE-056 (HIGH) named: when sit-down time arrives, it is spent on infrastructure rather than ingest, and the network-counts headline stays frozen at 222/90/35. The pattern is now strong enough to ask the second-order question explicitly..."
  Type: methodological / architectural / self-referential
  Related decisions: REVISE-056 (HIGH; AWAITING-REVIEW); REVISE-058 (MED-HIGH; AWAITING-REVIEW)
  Related assumptions: ASSUMPTION-233, ASSUMPTION-234 (wolfram-as-test-run), ASSUMPTION-249
  Related presumptions: PRESUMPTION-258 (network-counts-unchanged headline obscuring), PRESUMPTION-259 (binary-framing recurrence), PRESUMPTION-267, PRESUMPTION-275
  Testability: testable empirically (over the next 5.5 weeks, log every attended-session minute by category; check whether demo-path infrastructure or PRS extraction is in fact the higher-leverage use by ISME-readiness metrics; compare the binary "PRS-or-not" framing's predictive validity against a multi-category framing) and via literature (deadline-driven prioritization under empirical evidence of consistent deferral; when "the binary itself is the bug" framings in incident-response succeed)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-250
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from the "For Morning Discussion #1" second-order question framing -- the central architectural framing-shift candidate of the day.
    Current status: UNTESTED

ASSUMPTION-251:
  Date identified: 2026-05-28
  Statement: Three un-numbered DECISION candidates -- DECISION-048 (3rd cycle: review-page > email; intent > UI), DECISION-049 (2nd cycle: broker-v4 web_enrich architecture), and today's NEW un-numbered AI-search-delegation candidate (1st cycle) -- now constitute a "tracking blind spot of its own." If candidate-DECISIONs keep accumulating faster than they are numbered, the registry stops being the source of truth for what was decided -- exactly the failure mode the registry was built to prevent.
  Context: 2026-05-28 evening cowork-to-chat summary "For Morning Discussion #6": "Three un-numbered DECISIONs is now a tracking blind spot of its own. DECISION-048 (3rd cycle), DECISION-049 (2nd cycle), and today's AI-search-delegation candidate all sit unnumbered. If candidate-DECISIONs keep accumulating faster than they're numbered, the registry stops being the source of truth for what was decided -- exactly the failure mode the registry was built to prevent."
  Type: methodological / process / self-referential
  Related decisions: DECISION-048 candidate, DECISION-049 candidate, NEW AI-search-delegation candidate (all un-numbered)
  Related assumptions: (none directly)
  Related presumptions: PRESUMPTION-271
  Testability: testable empirically (track over 6 weeks whether candidate-DECISION accumulation rate exceeds numbering rate; measure whether un-numbered decisions land in cross-day discussions and obscure that the corresponding registry entry does not yet exist) and via literature (decision-registry hygiene patterns; the cost of candidate-vs-numbered status persistence in long-running engineering logs)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-251
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from the "tracking blind spot of its own" framing.
    Current status: UNTESTED

ASSUMPTION-252:
  Date identified: 2026-05-28
  Statement: Tonight's c2a2-self-awareness-daily run is the next REVISE-059 atomicity test: the registries advance and the dated artifacts (`2026-05-28_changes.md` + `metrics/2026-05-28_snapshot.md`) must write together; the morning check is "do both files exist?" If yes, the cadence-streak advances to N=7/N=6 (registry-advance/dated-artifact); if no, REVISE-059's HIGH-urgency reading is empirically reinforced.
  Context: 2026-05-28 evening cowork-to-chat summary "For Morning Discussion #4": "The REVISE-059 atomicity test is live for tonight too. Yesterday's chat summary flagged the 2026-05-25 dated-artifact gap as evidence the 14a/14b write-step can fail silently. Tonight's run (writing `2026-05-28_changes.md` + `metrics/2026-05-28_snapshot.md`) is the next instance of the same test. Morning check: do both files exist?"
  Type: methodological / self-referential
  Related decisions: REVISE-059 (MED-HIGH; AWAITING-REVIEW; from 2026-05-27)
  Related assumptions: (none directly -- a meta-claim about this run)
  Related presumptions: PRESUMPTION-264 (yesterday's), PRESUMPTION carried; this run's own atomicity surfaces a fresh PRESUMPTION below
  Testability: testable empirically (verify after this run completes that both files exist with matching registry-advance counts) and architecturally (the implementation of the REVISE-059-recommended fail-loud check would be the structural answer)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-252
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the morning-discussion #4 framing of tonight's run as itself a live test.
    Current status: UNTESTED

ASSUMPTION-253:
  Date identified: 2026-05-29
  Statement: The Sociogram focus-fade bug is real -- not a hidden-tab testing artifact. Running `focus: l ~ s` in a foreground tab leaves edges lit: the isolate computes the correct node set (185 nodes) but the fade does not visually apply.
  Context: Tom's verbatim foreground confirmation in the "Version 1.6 proceeding" session: "on focus: l ~ s: edges stay lit." This retired the agent's earlier hidden-tab probe (which had been confounded by Chrome's background-tab rAF throttling) and established the symptom independent of that confound.
  Type: empirical
  Related decisions: Sociogram v1.6 hold (candidate, un-numbered)
  Related assumptions: ASSUMPTION-254, ASSUMPTION-255
  Related presumptions: PRESUMPTION-277, PRESUMPTION-278
  Testability: testable empirically (reproduce in a foreground tab across multiple queries/browsers; instrument opacity values post-transition)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-253
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from Tom's foreground confirmation in the Version-1.6 session.
    Current status: UNTESTED

ASSUMPTION-254:
  Date identified: 2026-05-29
  Statement: The prime suspect for the focus-fade bug is the d3 `.transition()` opacity calls in `runFocus` (shared by the substring-search highlight and the 1.6 isolate/link path); the likely fix is to set opacity via plain `.attr('opacity')` instead of `.transition()`.
  Context: "Version 1.6 proceeding" close-out: "Prime suspect is the `.transition()` opacity calls; likely fix is plain `.attr('opacity')`." The agent flagged loudly that the fix must be diagnosed in a foreground tab because the hidden-tab probe throttles rAF (which d3 transitions depend on).
  Type: architectural / empirical
  Related decisions: Sociogram v1.6 hold (candidate, un-numbered)
  Related assumptions: ASSUMPTION-253
  Related presumptions: PRESUMPTION-278
  Testability: testable empirically (swap `.transition()` for `.attr('opacity')` in a foreground tab and observe whether the fade renders)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-254
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated fix-hypothesis in the Version-1.6 close-out.
    Current status: UNTESTED

ASSUMPTION-255:
  Date identified: 2026-05-29
  Statement: Version 1.6 (the bare-guess `focus: x ~ y` parser) is held deliberately -- coded into the generator and logic-validated 16/16, but not pushed and not regenerated into the live `wiki_narration.html` -- because 1.6's isolate/link share the same opacity mechanism as the confirmed focus-fade bug; shipping it now would ship a non-working fade.
  Context: "Version 1.6 proceeding" close-out: "1.6 bare-guess parser is coded into the generator and logic-validated (16/16), but not pushed and not regenerated into the live file -- held deliberately, because 1.6's isolate/link share the same opacity mechanism as the now-confirmed focus-fade bug."
  Type: architectural
  Related decisions: Sociogram v1.6 hold (candidate, un-numbered)
  Related assumptions: ASSUMPTION-253, ASSUMPTION-254, ASSUMPTION-262
  Related presumptions: PRESUMPTION-279
  Testability: framework commitment (a release-gating policy, not a literature claim) -- though the "ship nothing with a broken fade" priority is itself contestable (see PRESUMPTION-279)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-255
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the deliberate-hold rationale stated at session close.
    Current status: UNTESTED

ASSUMPTION-256:
  Date identified: 2026-05-29
  Statement: The Sociogram interaction model is locked: search/`focus:` is a transient highlight-in-place lens (dims non-matches, leaves the graph and simulation intact, reversible on clear); the filter checkboxes are hard filters that change what is actually in the graph; the two do not sync.
  Context: Tom's verbatim instruction "leave the current model," locking the choice the agent had framed as two clean options (keep separate vs. make search drive visibility). Agent confirmation: "the model decision is locked: search stays a transient lens, checkboxes stay hard filters, no sync."
  Type: architectural
  Related decisions: Sociogram interaction-model decision (candidate, un-numbered)
  Related assumptions: (none directly)
  Related presumptions: PRESUMPTION-284
  Testability: testable empirically (usability: do users correctly predict graph state when search and checkboxes disagree?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-256
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from Tom's "leave the current model" instruction and the agent's lock-in confirmation.
    Current status: UNTESTED

ASSUMPTION-257:
  Date identified: 2026-05-29
  Statement: The recent Sociogram crash was purely memory pressure; a fresh browser renders the page fine and the edge cap was never the cause, so `MAX_EDGES=30000` stays.
  Context: "Version 1.6 proceeding": "The crash was purely memory pressure -- fresh browser renders fine, edge cap was never the issue. Settled." Close-out: "the crash was just memory pressure -- `MAX_EDGES=30000` is fine, leave it."
  Type: empirical / architectural
  Related decisions: MAX_EDGES retained at 30000 (carry; CLAUDE.md records edge limit 3000 / MAX_EDGES 30000)
  Related assumptions: (none directly)
  Related presumptions: (none directly)
  Testability: testable empirically (reproduce crash conditions; profile memory vs. edge-count to confirm pressure, not cap, is the failure mode)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-257
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the "settled" crash-diagnosis statements in the Version-1.6 session.
    Current status: UNTESTED

ASSUMPTION-258:
  Date identified: 2026-05-29
  Statement: Increment 1.5's deterministic friendly-label typeahead (jump-to-thinker, no LLM) is the correct substrate for Pathway-27 entity retrieval, and it replaces the earlier "library-science requirement" Tom had flagged.
  Context: 2026-05-29 cowork summary: "Increment 1.5 -- the deterministic friendly-label typeahead (jump-to-thinker, no LLM, the Pathway-27 substrate) -- replaces the library-science requirement Tom flagged." Built, validated, and verified in both standalone and Summa-embedded copies; pushed to the feature branch.
  Type: methodological / architectural
  Related decisions: Sociogram increment 1.5 (pushed to feature branch)
  Related assumptions: ASSUMPTION-259
  Related presumptions: PRESUMPTION-285
  Testability: testable empirically (do users locate thinkers faster/more accurately with the deterministic typeahead than with the prior approach?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-258
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the increment-1.5 description in the 2026-05-29 cowork summary.
    Current status: UNTESTED

ASSUMPTION-259:
  Date identified: 2026-05-29
  Statement: (Pathway 28 -- Single-Source Participant Registration) The entire tradition/structure vocabulary fans out from one Python dict, `COLORS`, in `generate_visualization.py`; the filter checkboxes and the focus typeahead are siblings of that one source and therefore cannot drift apart.
  Context: 2026-05-29 cowork summary, pinning Pathway 28: "The entire tradition/structure vocabulary fans out from one Python dict, `COLORS`... the filter checkboxes and the focus typeahead are *siblings of one source* and cannot drift." Answers Tom's walk question "if I add a new thinker, does everything just pick them up?" -- yes, single-source.
  Type: architectural
  Related decisions: Pathway 28 (pinned principle, not a numbered DECISION)
  Related assumptions: ASSUMPTION-260
  Related presumptions: PRESUMPTION-280, PRESUMPTION-281
  Testability: testable empirically (add a thinker via one COLORS line + regen and verify checkboxes and typeahead both pick it up with no other edits)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-259
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the pinned Pathway 28 principle in the 2026-05-29 cowork summary.
    Current status: UNTESTED

ASSUMPTION-260:
  Date identified: 2026-05-29
  Statement: Adding a participant to the Sociogram is a single-source operation: one `COLORS` line, plus the participant's vault files, plus a regeneration of the visualization.
  Context: 2026-05-29 cowork summary: "Adding a participant is one `COLORS` line (+ vault files + regen)." A wrinkle was flagged as a Rule-12 violation: `get_group()` silently falls back to `'root'` for a directory absent from `COLORS`, so a thinker with files but no color line goes grey with no warning.
  Type: architectural / methodological
  Related decisions: Pathway 28 (pinned principle); Rule-12 get_group() fail-loud gap (open item)
  Related assumptions: ASSUMPTION-259
  Related presumptions: PRESUMPTION-280, PRESUMPTION-281
  Testability: testable empirically (measure the actual edit-set required to register a participant; verify the regen step is the only non-COLORS action)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-260
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the single-source registration claim and its flagged Rule-12 wrinkle.
    Current status: UNTESTED

ASSUMPTION-261:
  Date identified: 2026-05-29
  Statement: The session-handoff rail (a gitignored `handoffs/sociogram-navigation.md` seeded with the full 1.6 pickup, plus a "read the handoff doc first on resume" rule in the project `CLAUDE.md`) fixes the next-session resume problem, because `CLAUDE.md` auto-loads into context and will steer the resume even though the resume skill itself still title-searches.
  Context: "Sociogram navigation work" close-out: "because `CLAUDE.md` loads into my context automatically, the rule will steer the resume even though the resume skill itself still title-searches... next session, 'resume the sociogram work' lands on the handoff doc directly -- a bad auto-title can't derail it." Framed self-referentially as "Pathway 16 (durable conversational memory) in miniature, the system practicing its own thesis."
  Type: methodological / architectural / self-referential
  Related decisions: Session-handoff rail (NEW; gitignored doc + CLAUDE.md rule)
  Related assumptions: (none directly)
  Related presumptions: PRESUMPTION-282, PRESUMPTION-283
  Testability: testable empirically (on the next "resume the sociogram work," observe whether the handoff doc is read first and whether a bad auto-title is in fact prevented from derailing)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-261
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the handoff-rail rationale stated at the navigation-session close.
    Current status: UNTESTED

ASSUMPTION-262:
  Date identified: 2026-05-29
  Statement: Logic-validating the 1.6 bare-guess parser 16/16 establishes parser-level correctness; the remaining visual/fade behavior is a separate, foreground-tab verification deferred behind the hold.
  Context: "Version 1.6 proceeding": the 1.6 parser is "coded into the generator and logic-validated (16/16)" yet held because the fade (a rendering concern) is unverified. The split treats parser logic and visual rendering as independently verifiable.
  Type: methodological
  Related decisions: Sociogram v1.6 hold (candidate, un-numbered)
  Related assumptions: ASSUMPTION-255
  Related presumptions: PRESUMPTION-285
  Testability: testable empirically (does 16/16 logic coverage predict correct end-to-end behavior, given the fade bug shows logic-passing code can be visually broken?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-262
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the logic-validated-but-held framing of the 1.6 parser.
    Current status: UNTESTED

ASSUMPTION-263:
  Date identified: 2026-05-30
  Statement: Re-authenticating claude.ai in the extension's Chrome profile is the single fix that restores the full daily sync loop -- both the morning intake scrape (which reads Tom's walk/Chat conversation into the pipeline) and the evening cowork-to-chat delivery (which posts the EOD summary back). One re-login unblocks both directions.
  Context: Stated explicitly and independently by two autonomous agents on 2026-05-30. Morning scrape ("C2a2 morning chat scrape"): "To restore tomorrow's sync, Tom just needs to re-authenticate claude.ai in the Chrome profile the extension uses." Evening sync ("C2a2 evening cowork to chat"): "re-authenticating claude.ai in that Chrome profile is the top action item, and it unblocks the whole sync loop." Both runs failed for the same reason (Chrome logged out of claude.ai); the evening run characterized it as a "3-cycle outage."
  Type: architectural / operational
  Related decisions: (delivery-path / intake-path remediation; not a numbered DECISION; Pathway-14 honesty-layer adjacent)
  Related assumptions: ASSUMPTION-240, ASSUMPTION-242 (truncation-bug delivery-path lineage)
  Related presumptions: PRESUMPTION-287, PRESUMPTION-288, PRESUMPTION-289 (and the prior re-login-as-unblocking-event / uniform-failure-mode presumption surfaced 2026-05-26)
  Testability: testable empirically (after the next re-auth, instrument the following morning scrape AND evening delivery: does a single re-login in fact restore both directions, or does either direction require a separate fix? does the outage recur with a different mechanism?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-263
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the matching stated remediation claim in both autonomous sync agents' close-out messages on 2026-05-30. Note: this is the *stated* 14a twin of the previously *inferred* uniform-failure-mode presumption (2026-05-26); routed as ASSUMPTION because it was articulated explicitly this cycle, with cross-reference to the presumption to avoid double-counting.
    Current status: UNTESTED

ASSUMPTION-264:
  Date identified: 2026-05-31
  Statement: Under a degraded/lagged session, intermediate tool-call return values (e.g., "message sent," "logged in") are not trustworthy; only a clean re-verification against ground state (a fresh reload showing the actual current state) is authoritative. When the two conflict, the clean re-check wins and the agent must not claim a result it cannot re-verify.
  Context: Stated explicitly today by the evening cowork-to-chat agent during a degraded session whose tool I/O was severely lagged/batched. Its own words: "I cannot trust my earlier read that the message was sent ... Per fail-loud discipline, I must not claim a delivery I can't verify." It then treated a clean reload of claude.ai (which redirected to /login?from=logout, i.e. logged out) as authoritative over the earlier lagged reads that had *appeared* to show a logged-in tab and a sent message. The same degraded condition recurred from the sewing-agent run; the assumption is the agent's articulated rule for resolving it.
  Type: methodological / epistemic
  Related decisions: (Pathway-14 honesty-layer adjacent; fail-loud discipline, Rule 12; not a numbered DECISION)
  Related assumptions: ASSUMPTION-263 (the re-auth fix this verification exposed)
  Related presumptions: PRESUMPTION-291 (cross-day attribution echo), PRESUMPTION-292 (catch-the-false-positive), PRESUMPTION-293 (verifier-outside-the-fault)
  Testability: testable empirically (instrument a degraded session: do clean-reload re-checks reliably diverge from, and correct, lagged intermediate reads? is the reload path itself immune to the same batched/lagged I/O, or can it return stale state too?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-264
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the evening sync agent's explicitly stated verification rule on 2026-05-31, articulated when it caught and corrected a lag-induced false "message sent" read. This is the *stated* 14a counterpart to the inferred PRESUMPTION-292/293 about whether that rule is structurally guaranteed and whether its verifier is itself fault-free.
    Current status: UNTESTED

ASSUMPTION-265:
  Date identified: 2026-06-02
  Statement: The daily-run git phase must not assume a healthy version-control state across unattended runs — a crashed process can leave a stale `.git/index.lock` that silently blocks all staging (no error surfaced to the run), so git operational integrity has to be checked and repaired each run rather than presumed from the absence of a thrown error.
  Context: Stated explicitly today by the C2A2 wiki daily-run agent (2026-06-02, Phase 6/Git). Its own words: "I had to clear a stale `.git/index.lock` left over from a crashed process on 2026-05-29 that was silently blocking all git staging." The lock had been present and disabling staging since 2026-05-29; today's run detected it, quarantined the lock files via `mv` (the FUSE mount blocks `rm`), and restored `git status`. The agent paired this with the standing constitutional no-blind-push rule (600+ unrelated Summa-vault-sync files in the tree forbade an unattended auto-commit regardless).
  Type: methodological / architectural
  Related decisions: (constitutional no-blind-push rule; 2026-05-20 "large unrelated staged changes must not be auto-committed" note; not a numbered DECISION)
  Related assumptions: ASSUMPTION-264 (degraded-session reads untrustworthy — same family: a step that appears to succeed may have silently failed)
  Related presumptions: PRESUMPTION-294 (git-no-error == changes-tracked blind spot), PRESUMPTION-295 (indefinite deferral is cost-free)
  Related open questions: OPEN-071 (NEW — pre-flight git integrity check)
  Testability: testable empirically (instrument the daily-run git phase: does a stale index.lock reliably produce a silent staging failure with no surfaced error? does a pre-flight lock-detection + staging-verification step catch it? were the 2026-05-29..06-01 runs' "left staged-clean in working tree" claims actually false during the lock window?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-265
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-02 C2A2 wiki daily-run transcript (Phase 6/Git), where the agent stated it had cleared a stale index.lock from a 2026-05-29 crashed process that had been silently blocking all git staging. Genuinely new today (not an echo): corroborated by review/2026-06-02_review.html (created 16:21 today) confirming the run is today's. The stated lesson (verify git health, do not infer it from no-error) is the 14a counterpart to the inferred PRESUMPTION-294 about the prior days' silent staging failures.
    Current status: UNTESTED

---

ASSUMPTION-266:
  Date identified: 2026-06-02
  Statement: Git staging in the wiki repo must use explicit file paths and never `git add -A`, because the working tree perpetually carries unrelated modified Summa-vault-sync files; staging by explicit path is the safeguard that keeps a commit (attended or unattended) from sweeping in unintended changes.
  Context: Stated in the evening Sociogram session (2026-06-02). Agent's words: "the push runs at the Mac Mini with explicit paths only — never `git add -A`, since the tree has unrelated modified vault files." Re-affirmed when it built the commit command from two named files (generate_visualization.py, wiki_narration.html) only.
  Type: methodological / architectural
  Related decisions: (constitutional no-blind-push rule; 2026-05-20 "large unrelated staged changes must not be auto-committed" note)
  Related assumptions: ASSUMPTION-265 (git-health-must-be-verified-not-inferred — same evening, same git phase)
  Related presumptions: PRESUMPTION-297 (cross-repo correctness held by memory, not tooling)
  Related open questions: OPEN-072 (cross-repo uncommitted-state interlock)
  Testability: testable empirically / framework commitment (does explicit-path staging reliably prevent unintended commits given a perpetually-dirty tree? is the perpetual dirtiness itself the deeper hazard?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-266
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the evening Sociogram interactive session (2026-06-02, post-16:27 self-awareness run). The agent explicitly required explicit-path staging over `git add -A` because of the perpetually-dirty vault tree. Companion to ASSUMPTION-265 (verify git health) — both surfaced in the same evening git-phase that also hit a recurrence of the stale index.lock.
    Current status: UNTESTED

---

ASSUMPTION-267:
  Date identified: 2026-06-02
  Statement: Raising the Sociogram render cap MAX_NODES from 2000 to 20000 is the correct crash-proofing setting — the prior 2000 cap was the operative limit that would have truncated the now-2529-node graph, and 20000 is treated as a safe ceiling that current and near-term data will not reach while keeping the force-directed render stable.
  Context: Evening Sociogram session (2026-06-02). Stated: "Node cap — `MAX_NODES = 20000` active; can't fire at 2529 nodes (the old 2000 cap is gone)." Shipped in commit 7d56733. (Supersedes the CLAUDE.md crash-proofing baseline of node-limit 2000.)
  Type: architectural / empirical
  Related decisions: (Sociogram crash-proofing limits)
  Related assumptions: ASSUMPTION-268 (foreground-tab review standard that signed this off)
  Related presumptions: PRESUMPTION-299 (scale-blindness on the 10x cap raise)
  Testability: testable empirically (characterize render/interaction performance from 2.5k to 20k nodes — is 20000 a safe ceiling or an untested one?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-267
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the evening Sociogram session. The 2000->20000 cap change was stated as design rationale ("can't fire at 2529 nodes; the old 2000 cap is gone") and shipped. The stated commitment is that 20000 is a safe ceiling; the untested span between 2.5k and 20k is the inferred counterpart PRESUMPTION-299.
    Current status: UNTESTED

---

ASSUMPTION-268:
  Date identified: 2026-06-02
  Statement: A valid pre-push "constitutional review" requires live verification in a real foreground browser tab served over HTTP — not a headless or merely asserted check — with explicit observable evidence (numeric opacity split, cross-link node count, clean console across load and interaction) plus Tom's sign-off; this live-evidence standard is what licenses a push.
  Context: Evening Sociogram session (2026-06-02). Stated: "Constitutional review complete — served over HTTP at `localhost:8080/explorer.html`, viewed in a real foreground Chrome tab"; "gated on your sign-off before any push (constitutional rule)." Evidence cited as sufficient: opacity split 2 bright / 2527 dim / 0 mid; 200 cross-linked nodes; no console errors across load + interaction.
  Type: methodological
  Related decisions: (constitutional review / no-blind-push rule)
  Related assumptions: ASSUMPTION-265, ASSUMPTION-267
  Related presumptions: PRESUMPTION-298 (single live spot-check generalizes to full correctness)
  Testability: framework commitment (constitutional) / partly testable (does foreground-tab review catch defects a headless/asserted check misses, and how often?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-268
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the evening Sociogram session, where the agent articulated a specific evidential standard for the constitutional review (real foreground tab, served over HTTP, numeric + console evidence) as the precondition for sign-off and push. The inferred counterpart — that one isolate + one cross-link check generalizes to all cases — is PRESUMPTION-298.
    Current status: UNTESTED

---

ASSUMPTION-269:
  Date identified: 2026-06-03
  Statement: Intake discipline — an unverified cross-tradition lead must be flagged and held, not captured, until a targeted confirmation search establishes it ("flag, do not yet ingest"). A plausible-but-unconfirmed connection is treated as a lead to be verified by a downstream agent, not as ingestible content.
  Context: Stated in today's auto-ingested McGilchrist proposal (PROP-2026-06-03-001, 07:11), Cross-Tradition Signals section, regarding a possible McGilchrist↔Wolfram engagement: "UNVERIFIED LEAD — flag, do not yet ingest … A direct 2026 McGilchrist–Wolfram dialogue could NOT be confirmed … recommend the orchestrator or Wolfram agent run a targeted confirmation search before any capture." The same proposal contrasts this with a *confirmed* convergence (McGilchrist + Kastrup both reaching a negative verdict on AI consciousness) that it does record.
  Type: methodological
  Related decisions: (proposal-intake / provenance discipline; constitutional no-blind-capture norm)
  Related assumptions: ASSUMPTION-264 (don't claim what you can't re-verify — here applied to intake rather than reporting)
  Related presumptions: PRESUMPTION-302 (self-awareness/pipeline value on autonomous runs)
  Testability: framework commitment (provenance discipline) / partly testable via literature (citation-verification and false-lead rates in automated knowledge-base intake)
  Status: GROUNDED (incorporated as PREMISE-049, 2026-06-04 lit run)
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a/15b -> 15c -> 14a]
    Original item: ASSUMPTION-269
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-03 auto-ingested McGilchrist proposal (the only genuinely new 06-03 intake artifact). The proposal explicitly stated a hold-until-verified rule for the unconfirmed McGilchrist–Wolfram lead while recording only the confirmed McGilchrist–Kastrup convergence. Genuinely new today (not an echo): the proposal file is dated/searched 2026-06-03 and was ingested at 07:11. This is the stated intake-side counterpart to the "verify before you assert" family (ASSUMPTION-264/265).
      15a/15b/15c (2026-06-04): INCORPORATED as PREMISE-049 (verify-before-trust); strong support, only an operational caveat folded in (quarantine-with-revisit, not silent drop). DISPOSITION-146.
    Current status: GROUNDED

---

ASSUMPTION-270:
  Date identified: 2026-06-03
  Statement: An autonomous browser/sync agent must not authenticate as Tom; it will not sign in on his behalf. A lapsed claude.ai session is therefore a hard external blocker the pipeline cannot self-clear — re-auth is an attended-only action — so both the morning Chat→Cowork scrape and the evening Cowork→Chat delivery are designed to skip (and report) rather than restore the channel themselves.
  Context: Re-stated across today's runs. Evening-sync agent (2026-06-03): "I won't sign in on your behalf, so browser delivery is skipped as expected." Morning scrape (12:53) hit `/login?from=logout` and produced no Chat context. The boundary is the proximate cause of the now-two-day, both-directions sync outage.
  Type: normative / methodological (safety/autonomy boundary)
  Related decisions: (autonomous-agent authority limits; human-in-the-loop boundary)
  Related assumptions: ASSUMPTION-263 (re-auth is the single stated fix for dark intake)
  Related presumptions: PRESUMPTION-300 (confirmed-down channel treated as recoverable, not a stop condition)
  Related open questions: OPEN-073 (should a confirmed-down sync channel trip a degrade/halt/escalate state?)
  Testability: framework commitment (safety boundary — agents should not assume user credentials) / partly testable via literature (human-in-the-loop authority limits; cost of agent-held vs human-held auth in unattended automation)
  Status: CHALLENGED (partial) -> MONITOR-296 (2026-06-04 lit run)
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a/15b -> 15c -> 14a]
    Original item: ASSUMPTION-270
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from today's evening-sync and morning-scrape transcripts, which each explicitly declined to sign in and skipped their channel. Distinct from ASSUMPTION-263 (which names re-auth as the fix): 270 names the *agent-side boundary* that makes re-auth attended-only, and thereby makes the lapsed session unrecoverable from inside the pipeline. The inferred counterpart — that the pipeline keeps producing into the dead channel anyway — is PRESUMPTION-300.
      15a/15b/15c (2026-06-04): Core boundary strong (agents should not assume user credentials); the 'cannot self-clear' clause is genuinely contested (scoped delegated-credential self-recovery vs added attack surface) -> MONITOR-296, not REVISE. Contributes to High SYSTEMIC-RISK 'autonomous-sync silent-degradation' (270+300). DISPOSITION-147.
    Current status: CHALLENGED (partial); core boundary SUPPORTED, 'cannot self-clear' clause contested

---

ASSUMPTION-271:
  Date identified: 2026-06-04
  Statement: The PROCESSED_LOG's canonical ingest backlog is 36 files; the divergent figure of 152 produced by a naïve filename diff is an artifact of the log mixing per-file rows with batch-narrative entries, not a record of 116 additional un-ingested files. The "true" backlog count is therefore asserted to be 36, recoverable by reconciling the log's two entry styles during an attended ingest.
  Context: Stated explicitly by the C2A2 wiki daily-run agent (2026-06-04, Phase 1 / closing note): "the backlog count is solid at 36, but PROCESSED_LOG mixes per-file rows with batch narratives, so a naïve filename diff reports 152; tidying that during the attended ingest would make the log diffable going forward." The run logged this as a "36-vs-152 bookkeeping conflict" and deferred the 36-file backlog under the standing attended-session rule (0 triplets added).
  Type: methodological / empirical
  Related decisions: (proposal-intake / PROCESSED_LOG bookkeeping; attended-ingest batching norm)
  Related assumptions: ASSUMPTION-269 (intake/provenance discipline — here applied to the log-of-record)
  Related presumptions: PRESUMPTION-304 (the unstated counterpart — that the 36 is correct and the 152 carries no lost data)
  Testability: testable empirically (reconcile the log directly: join tradition-wiki integration timestamps / inbox file mtimes against PROCESSED_LOG entries to confirm whether the canonical count is 36 or whether some of the 152 are genuinely un-ingested) / partly via literature (system-of-record vs human-readable-narrative log design)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-271
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-04 wiki daily-run report, the only genuinely-new 06-04 statement about the backlog's bookkeeping. The agent explicitly asserted 36 as solid and attributed the 152 to a format artifact (per-file rows mixed with batch narratives). Genuinely new today: the conflict was first *logged as a conflict* on this run. This is the stated, count-claim side; the unstated resolvability/denominator premise is PRESUMPTION-304. Distinct from the older PROCESSED_LOG-completeness presumptions (126/the 2026-05-09 backfill family), which were about missing entries, not about two entry styles yielding two counts.
    Current status: UNTESTED

---

ASSUMPTION-272:
  Date identified: 2026-06-04
  Statement: Draining the 36-file ingest backlog should proceed as small, attended-authorized batches (on the order of 5-8 files per run), not as a single bulk ingest. A batched, human-authorized cadence is treated as the way to restart autonomous flow without compromising PRS-triplet quality or sweeping unrelated working-tree changes into the commit.
  Context: Stated in the 2026-06-04 wiki daily-run closing report under what stays human-gated: "authorize a small batched ingest (~5-8 files/run) to start draining the 36-file backlog." Paired with the standing no-blind-push hold (587 uncommitted changes on feature/sociogram-search-integration were not committed) and the deferral of the full 36-file backlog this run.
  Type: methodological
  Related decisions: (attended-ingest cadence; constitutional no-blind-push rule)
  Related assumptions: ASSUMPTION-271 (the 36-file backlog this cadence is meant to drain); earlier batch-ingest assumptions on tradition-batching and "massive ingestion" quality (refines them toward a smaller, more conservative per-run size)
  Related presumptions: PRESUMPTION-305 (uncommitted working-tree accumulation treated as cost-free)
  Testability: testable empirically (compare PRS-triplet revision/reversal rates for small 5-8-file attended batches vs the historical large/"massive" ingestions; measure whether small batches actually drain the backlog faster than they accrue) / via literature (batch-size vs quality in human-in-the-loop curation; WIP limits)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-272
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-04 daily-run report's human-gated-actions block. A more conservative, explicitly-sized articulation (5-8 files/run, attended-authorized) than the earlier batch-ingest assumptions (which described a 45-file "massive ingestion" and tradition-batching). Recorded as a refinement of, not a duplicate of, those — the new content is the small per-run size and the attended-authorization gate as the restart mechanism. Genuinely new today (stated on this run).
    Current status: UNTESTED

---

ASSUMPTION-273:
  Date identified: 2026-06-05
  Statement: The sociogram's LOCKED search semantics — search is a transient highlight lens, never a filter; checkboxes filter, search highlights, and the two never sync (2026-05-29 LOCK) — transfer correctly and should be inherited *exactly* by the Community Explorer's 156-node graph.
  Context: Stated in the P1 build / sociogram_feature_review.md (row 6): "Inherit the locked semantics exactly. … search highlights, checkboxes filter, the two never sync. Highest value-per-effort of anything in this table." Verified in the localhost review: "democracy" lit 14 of 156, never touched the checkboxes (LOCK respected).
  Type: architectural / methodological
  Related decisions: DECISION-050 (CE relationship architecture); 2026-05-29 search-lock
  Related presumptions: PRESUMPTION-307 (the unstated transfer-conditions counterpart — that a rule derived for a 1647-node graph fits a 156-node one)
  Testability: testable via literature (HCI: search-as-highlight vs search-as-filter; effect of graph size on appropriate interaction semantics)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-273
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-05 attended P1 build session and sociogram_feature_review.md. The stated commitment is that the lock is right for CE; the inferred (unexamined) half — whether the lock's original rationale survives the ~10x drop in node count — is PRESUMPTION-307.
    Current status: UNTESTED

---

ASSUMPTION-274:
  Date identified: 2026-06-05
  Statement: A single shared search/broker module (`lib/c2a2-search.js`, inlined into each page at generation time) is the correct single-source seam for search and Ask-AI across both the graph and the cards surfaces — "one broker client, multiple surfaces … one search pipeline, two renderings."
  Context: sociogram_feature_review.md rows 7 and P1: "`lib/c2a2-search.js` was built precisely for this (one broker client, multiple surfaces) … This is the first concrete integration point between graph and cards: one search pipeline, two renderings." Confirmed in the build: "The shared `c2a2-search.js` is now inlined at generation time, same single-source convention as the sociogram."
  Type: architectural
  Related decisions: DECISION-050
  Related assumptions: ASSUMPTION-273 (search semantics the shared module enacts)
  Testability: framework / engineering commitment (single-source-of-truth module) — not literature-testable; held, not routed
  Status: UNTESTED (held — framework commitment)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-274
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the P1 build session. Recorded as a design/engineering commitment (single shared module). Not routed to 15a/15b: it is an internal-architecture choice without a literature truth-condition.
    Current status: UNTESTED (held)

---

ASSUMPTION-275:
  Date identified: 2026-06-05
  Statement: The graph view and the cards view are two non-redundant "verbs over one dataset" (explore/relate/discover vs find/browse/register), not two versions of one tool; neither can absorb the other's function, so keeping both is justified.
  Context: sociogram_feature_review.md §2: "these are not two versions of one tool; they are two verbs over one dataset. … Killing either loses a function the other cannot absorb." Pathway P4 ("keep only one") explicitly not recommended.
  Type: architectural
  Related decisions: DECISION-050
  Related presumptions: PRESUMPTION-306 ("one dataset" presumes unifiability despite the disjoint id spaces found this session)
  Testability: testable via literature (dual-view / overview+detail UX; tool-redundancy and view-coordination) — LOW priority
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-275
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the §2 comparison table and P4 rejection. Stated as design rationale for keeping both surfaces. The "one dataset" phrasing is the stated side; its unexamined unifiability premise (given today's id-space finding) is PRESUMPTION-306.
    Current status: UNTESTED

---

ASSUMPTION-276:
  Date identified: 2026-06-05
  Statement: P3 ("one app, two projections") is the correct target architecture, and its promotion pipeline — a quality gate (record enters as seed → community claims and articulates GPRS → quality crosses Q2 → it appears in the graph and grows edges) — is the *actual* integration, not the UI. Graph membership should be earned by self-articulation rather than curatorial fiat, which makes the graph itself a measurement surface (who has articulated, who is connecting).
  Context: sociogram_feature_review.md §3 P3 + ratified recommendation: "the quality gate is the membrane between directory and graph"; "Graph membership stops being a curatorial fiat and becomes something a community earns by self-articulation — which makes the graph itself a measurement surface." DECIDED 2026-06-05 (Tom): "P1 now; P3 is the someday target."
  Type: architectural / methodological
  Related decisions: DECISION-050
  Related presumptions: PRESUMPTION-308 (Q2-gated visibility smuggles a normative claim); PRESUMPTION-309 (P1 pieces presumed forward-compatible with P3); PRESUMPTION-311 (presumes the two object types should ever share an id space)
  Testability: testable via literature (staged / quality-gated data pipelines; progressive-promotion architectures; visibility-as-earned designs)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-276
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from §3 and the ratified 2026-06-05 decision. Stated architectural target plus the explicit claim that the promotion pipeline (not the UI) is the real integration. Three distinct unstated premises ride beneath it — surfaced as PRESUMPTION-308/309/311 by 14b.
    Current status: UNTESTED

---

ASSUMPTION-277:
  Date identified: 2026-06-05
  Statement: [GROUNDED this session] The graph's 156 curated communities (`curated_communities.json`, ids CC-001…) and the Cards directory's 855 records (`data.js`, ids C0001…) are disjoint id spaces — 0 id matches, 3 name matches, 5 url-host matches. The earlier P1 "shared `community_id`" premise is therefore false; any cross-navigation hand-off requires a curated↔directory join that does not yet exist.
  Context: CORRECTION block added to sociogram_feature_review.md (2026-06-05, P1 build session): "the 'shared `community_id`' premise is false in the current data … 0 id matches, 3 name matches, 5 url-host matches … Cross-navigation hand-offs are therefore deferred (Tom, 2026-06-05)." P1 shipped as search box + shared Ask-AI pipeline only.
  Type: empirical
  Related decisions: DECISION-050; supersedes the cross-nav portion of the earlier P1 sketch
  Related questions: OPEN-075 (is the join feasible at useful density, or are these categorically distinct objects?)
  Related presumptions: PRESUMPTION-306, PRESUMPTION-311
  Testability: GROUNDED — directly verified against the JSON/data.js this session (count check); no routing needed
  Status: GROUNDED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-277
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the dated CORRECTION block. This is the rare case of a same-session falsification of a prior stated premise (the "shared community_id" P1 sketch) by direct evidence; recorded as GROUNDED (empirically settled), not routed to the literature pipeline. It is the stated/measured side; the unexamined "these should eventually join" premise is PRESUMPTION-311.
    Current status: GROUNDED

---

ASSUMPTION-278:
  Date identified: 2026-06-06
  Statement: Merging the 156 curated communities into the Cards directory under their own `CC-xxx` ids (so the graph becomes a literal id-subset of the cards) is the correct way to make the directory⊇graph relationship true rather than aspirational, and to unblock the previously-deferred graph↔cards cross-navigation hand-off on a shared key. This is the first concrete step that makes P1 forward-compatible with the P3 promotion pipeline.
  Context: explorer_tabs_complementarity.md §"Why this matters architecturally": "the graph's 156 curated communities were merged into the Cards directory under their own `CC-xxx` ids … so the graph is now a literal id-subset of the cards — the claim this popover makes is true rather than aspirational, and the previously-deferred graph↔cards cross-navigation hand-off is now mechanically possible on the shared key (the UI for it is a future increment)." sociogram_feature_review.md 2026-06-06 UPDATE; scripts/generate_community_cards_data.py (cards now 1006 after deduping 5 bulk overlaps). Directly addresses ASSUMPTION-277 / OPEN-075 (the "no join exists" finding of 2026-06-05).
  Type: architectural
  Related decisions: DECISION-050, DECISION-051
  Related questions: OPEN-075 (partial empirical answer — the join is now mechanically real), OPEN-076 (is its edge density sufficient?)
  Related presumptions: PRESUMPTION-312 (sharing an id key presumes genuine entity identity rather than merely asserting it)
  Testability: testable via literature (record-linkage / shared-key subset modeling; superset-directory ⊇ curated-subgraph patterns) — LOW priority (largely an engineering realization of DECISION-050)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-278
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-06 attended CE build session and its dated artifacts. The stated rationale for the curated→cards merge; it supersedes the cross-nav-deferral of ASSUMPTION-277 by building the join. The unexamined "shared id = identity" premise beneath it is surfaced as PRESUMPTION-312.
    Current status: UNTESTED

---

ASSUMPTION-279:
  Date identified: 2026-06-06
  Statement: The Cards directory and the Graph are "two surfaces, one instrument" and are *mutually upbuilding*: Cards is breadth/self-articulation (the wide door — every community found, each an inferred seed until it claims and sharpens its own GPRS); Graph is depth/detection (the 156 articulated to a quality bar, positioned by problem-kinship). The directory feeds the graph (a well-articulated seed earns its place and grows edges) and the graph gives the directory its purpose (a destination worth articulating toward) — "breadth invites; depth reveals — each makes the other more truthful."
  Context: explorer_tabs_complementarity.md (new file, 2026-06-06), source-of-truth for the "?" popover: "The two are complementary and mutually upbuilding. The directory feeds the graph … The graph gives the directory its purpose … each makes the other more truthful." Refines ASSUMPTION-275 ("two verbs over one dataset") and ASSUMPTION-276 (earned graph membership) by adding the mutual-reinforcement claim.
  Type: architectural / methodological
  Related decisions: DECISION-050, DECISION-051
  Related assumptions: ASSUMPTION-275, ASSUMPTION-276 (overlap noted — 279 adds the mutual-upbuilding claim specifically)
  Related presumptions: PRESUMPTION-316 (the harmonious complementarity hides a graph-absence-stigmatizes-carded-only failure mode)
  Testability: testable via literature (overview+detail / focus+context dual-view UX; whether coordinated breadth+depth views are mutually reinforcing or competing) — LOW priority
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-279
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the new explorer_tabs_complementarity.md. The stated complementarity doctrine; partially overlaps 275/276 but adds the "mutually upbuilding / each makes the other more truthful" reinforcement claim, which is the routable, testable increment. Its unexamined failure-mode-blindness is PRESUMPTION-316.
    Current status: UNTESTED

---

ASSUMPTION-280:
  Date identified: 2026-06-06
  Statement: Because the Community Explorer records are seeded from publicly-available web pages without the communities' express consent, and no community has reviewed or approved its record, the tool must disclose this status directly in-product — in the "?" popover and in a source-of-truth doc — rather than presenting seed records as if endorsed.
  Context: Prompted by two falsehoods Tom flagged in the popover; fix (1): "no community has approved any record — all data is from public web pages (now disclosed in the popover + explorer_tabs_complementarity.md)." explorer_tabs_complementarity.md status/consent block: "This tool is currently still under construction, and has been seeded with publicly-available information about communities without their express consent. No community has reviewed or approved its record."
  Type: normative / methodological
  Related decisions: DECISION-051
  Related presumptions: PRESUMPTION-313 (in-product disclosure presumed sufficient to discharge the consent obligation)
  Testability: testable via literature (research-ethics / informed-consent norms for listing identifiable groups from scraped public data; data-provenance and consent-disclosure practice)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-280
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the popover truth-fix and the new consent block. A genuinely new normative commitment today (transparency about non-consented seeding). The deeper unstated premise — that disclosure cures rather than merely documents the consent gap — is surfaced as PRESUMPTION-313.
    Current status: UNTESTED

---

ASSUMPTION-281:
  Date identified: 2026-06-06
  Statement: A single source-of-truth document (explorer_tabs_complementarity.md) that the generator's popover text mirrors — "edit here and regenerate to keep them aligned" — is the correct discipline for preventing in-product UI copy from drifting away from its documented architectural rationale.
  Context: explorer_tabs_complementarity.md header: "Source of truth for the Community Explorer '?' (Graph vs Cards) popover. The popover text in scripts/generate_community_explorer.py is a mirror of this file; edit here and regenerate to keep them aligned."
  Type: methodological / architectural
  Related decisions: DECISION-051
  Related assumptions: ASSUMPTION-274 (shared single-source seam — same single-source-of-truth family; held on the same grounds)
  Testability: framework/engineering commitment — not literature-testable. HELD (not routed), parallel to ASSUMPTION-274.
  Status: UNTESTED (held — framework commitment)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-281
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the new doc's header convention. A single-source-of-truth engineering commitment (anti-drift), held by type rather than routed — same disposition as ASSUMPTION-274.
    Current status: UNTESTED (held)

---

ASSUMPTION-282:
  Date identified: 2026-06-06
  Statement: [GROUNDED this session] A console error (null `addEventListener` at app.js:1314) can be dispositioned as a stale buffer artifact rather than a live bug when (a) it does not recur on a clean reload and (b) a handler wired *after* the supposedly-throwing line still fires — proving the line did not throw on the live load. Here the subtype-dropdown change handler (wired at 1315) fired and synced the URL to `subtypes=Anarchist+commune`, so 1314 did not throw; the frozen 12:27:01 entry was an intermediate edit-state remnant.
  Context: 2026-06-06 build-session verification step: "Same frozen timestamp (12:27:01) — it didn't recur on this fresh load … The definitive test: if the change handler (wired at 1315, after the line that supposedly threw) actually fires, then 1314 didn't throw … the URL updated to `subtypes=Anarchist+commune`, so the change handler at line 1315 fired — meaning 1314 did not throw on the current load."
  Type: methodological (debugging / verification heuristic)
  Related decisions: DECISION-051
  Related presumptions: PRESUMPTION-315 (the stale-buffer disposition presumed complete without checking the error path's reachability from real user sequences)
  Testability: GROUNDED — the specific disposition was verified in-session by a positive downstream-handler test; the general heuristic is testable via software-engineering literature (heisenbug / stale-console diagnosis) but is not routed.
  Status: GROUNDED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-282
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the verification step. A rare verification-success instance (a stated diagnostic claim proven in-session by a positive handler-fires test), recorded GROUNDED and not routed — parallel to ASSUMPTION-277. The completeness of the disposition is questioned by PRESUMPTION-315.
    Current status: GROUNDED

---

ASSUMPTION-283:
  Date identified: 2026-06-07
  Statement: The "PRS triplets accumulate but the published connectome never changes" failure is best solved by automating regeneration on a schedule (a weekly Sunday `c2a2-prs-connectome-weekly` task) rather than relying on remembering to regenerate by hand.
  Context: 2026-06-07 attended PRS-connectome session. The originating problem was that triplets had grown 231 → 269 while the live viz stayed at the old count; the chosen remedy was a scheduled regen task (created, then corrected mid-session). Stated: "The original problem — triplets accumulating but the viz never changing — is resolved at the source" and the weekly task "regenerates + validates in place."
  Type: architectural / methodological
  Related decisions: DECISION-052
  Related presumptions: PRESUMPTION-318 (the auto-regen task was built before the execution environment's capabilities were probed)
  Testability: testable via literature (CI/CD and scheduled-regeneration practice for generated artifacts; staleness/drift of derived data products)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-283
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated design rationale of the 2026-06-07 PRS-connectome session (read via session_info). The scheduling remedy is the explicit fix for the accumulate-but-stale problem; routed LOW.
    Current status: UNTESTED

ASSUMPTION-284:
  Date identified: 2026-06-07
  Statement: Approved-PRS *data* regeneration can safely auto-publish, but generator/template *code* changes must stage locally and notify the human for visual review before publishing — i.e., the right safety split is "data auto-publishes, code is gated."
  Context: 2026-06-07 PRS-connectome session, stated as the one guard Claude insisted on: "approved-PRS data auto-publishes, code changes don't … if the generator/template changed since the approved baseline, it stages locally and notifies you for visual review." (The auto-push half was later removed when the sandbox proved unable to push — see ASSUMPTION-285 — but the data/code asymmetry remained the design intent.)
  Type: methodological / normative
  Related decisions: DECISION-052
  Related presumptions: PRESUMPTION-319 (presumes data regeneration is deterministic/low-risk enough to publish unreviewed)
  Testability: testable via literature (human-in-the-loop release gating; continuous deployment with code-vs-data change classification; drift-baseline guards)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-284
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated drift-baseline guard. The data-publishes / code-gates asymmetry is a deliberate, articulated safety choice; routed MED. Its embedded premise (data regen is safe to ship unreviewed) is surfaced separately as PRESUMPTION-319.
    Current status: UNTESTED

ASSUMPTION-285:
  Date identified: 2026-06-07
  Statement: [GROUNDED this session] Scheduled tasks run in the same flattened-mount sandbox as the EOD/automation agents — which has no GitHub credentials (cannot push), cannot resolve `$HOME` (hardcoded `~/Documents/...` paths do not exist), and cannot create/delete `.git` lock files — so any workflow step requiring a push or `.git` mutation must be handed to Tom on his Mac, not automated. The corrected design ("automate the regen, hand off the push") follows directly: the task does everything the sandbox *can* do (regenerate, validate, write in place, notify) and stops exactly at the capability wall.
  Context: 2026-06-07 session. The original task design assumed the inverse (that scheduled tasks run on Tom's Mac with credentials and a normal `$HOME`); the trial run falsified that — the worktree/push step failed and left stale `.git` lock cruft in the real repo. The git-free rewrite was then tested end-to-end in the sandbox and passed. Stated: "scheduled tasks run in this same no-credentials sandbox, so anything requiring a push or `.git` lock changes has to be handed to you, not automated."
  Type: architectural / infrastructural
  Related decisions: DECISION-052
  Related presumptions: PRESUMPTION-317 (the prior design presumed execution-context uniformity between attended Cowork and scheduled tasks)
  Testability: GROUNDED — verified in-session by the failed push/worktree run plus the successful end-to-end test of the git-free script; an infrastructural fact of this environment, not a literature claim. NOT routed.
  Status: GROUNDED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-285
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the corrected, verified-in-session replacement for the day's originating mistaken assumption (that tasks run on the Mac). A second verification-success instance (parallel to ASSUMPTION-277/282): a stated capability claim proven in-session. Recorded GROUNDED, not routed. The blind spot that produced the original error is surfaced as PRESUMPTION-317.
    Current status: GROUNDED

ASSUMPTION-286:
  Date identified: 2026-06-07
  Statement: Tom's 12 CLAUDE.md rules sit at the *policy* layer — choices that are in principle waivable (e.g., the no-blind-push rule could be relaxed for a pre-approved, deterministic artifact like the PRS connectome) — whereas the sandbox's no-push limit is a *capability / constitutional* boundary that cannot be waived. A policy rule and a hard capability wall can coincide, so waiving the policy would not have enabled the action.
  Context: 2026-06-07 session, co-articulated by Tom and Claude. Tom: "I wondered whether you could except this prs push to live; turns out the rule was constitutional at a deeper level than my 12 claude.md rules." Claude: "Your 12 rules sit at the policy layer … underneath it is a capability boundary you can't waive — the sandbox has no GitHub credentials, period … Your policy rule happened to be pointing at a hard wall."
  Type: epistemic / methodological (constraint taxonomy for agentic systems)
  Related decisions: DECISION-052
  Related presumptions: PRESUMPTION-317 (the two-layer distinction only became visible once execution-context uniformity was falsified)
  Testability: testable via literature (capability-based security; policy-vs-mechanism separation; constitutional/guardrail vs configurable-policy layering in agent governance)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-286
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the closing Tom↔Claude exchange. The day's headline conceptual yield — a clean policy-layer (waivable) vs capability-layer (constitutional) distinction. Routed MED as a generalizable governance principle. Stated jointly, so [stated] not [inferred].
    Current status: UNTESTED

---

## 2026-06-08 — 14a/14b EOD batch (attended OpenStory → Agent Explorer build day; 4 sessions)

*Source: four attended Cowork sessions on 2026-06-08 integrating OpenStory observed telemetry into the C2A2 Agent Explorer (`agents_tab.html`, subtab 3c of the community explorer), read via the day's handoff notes `wiki/agents/openstory/HANDOFF_openstory_{c2a2,session2,session3,session4}.md` and the artifacts they describe (`extract_openstory_agent_data.py`, `inject_telemetry.py`, `sync_roster.py`, `agent_map.json`, `agent_telemetry.json`). Extracted 6 ASSUMPTIONs (287-292); 5 routed, 1 held (289 GROUNDED in-session).*

ASSUMPTION-287:
  Date identified: 2026-06-08
  Statement: Observed telemetry (OpenStory's per-agent event stream — sessions, events, eval/apply, tool use, durations) should replace hand-authored narration as the basis of the Agent Explorer. As stated in HANDOFF-1: "Currently authored narration; OpenStory replaces it with observed telemetry."
  Context: The founding design rationale for the whole OpenStory integration — the Agent Explorer (subtab 3c) was authored-narration; the day's work re-bases it on observed behavior, with graceful fallback to authored narration if data is absent.
  Type: epistemic / methodological (observed behavior vs authored intent as the truth-basis of a self-representation)
  Related decisions: DECISION-053
  Related presumptions: PRESUMPTION-322 (the unstated half — that the event stream is a *faithful* proxy for what an agent is/does)
  Testability: testable via literature (behavioral/observability telemetry as a proxy for system purpose and quality; intent vs trace)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-287
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the stated founding rationale of the integration (HANDOFF-1 item 4). Routed MED. [stated]
    Current status: UNTESTED

ASSUMPTION-288:
  Date identified: 2026-06-08
  Statement: The extraction pipeline should route through OpenStory's SQLite DB rather than read the raw transcripts directly, accepting a heavier dependency, because the eval/apply ratio and turns are signal worth preserving. As stated in HANDOFF-2: "Only thing a pure direct-transcript extractor would lose is eval/apply + turns; everything else … is computable either way — so we route through OpenStory to keep eval/apply."
  Context: The "agreed architecture" decision (HANDOFF-2). A deliberate build-vs-buy / dependency tradeoff: a direct-transcript extractor would be simpler and dependency-free but would lose eval/apply + turns, which were judged valuable enough to justify routing through OpenStory.
  Type: architectural / methodological (dependency tradeoff justified by the value of a specific derived metric)
  Related decisions: DECISION-053
  Related assumptions: ASSUMPTION-287
  Related presumptions: PRESUMPTION-323 (eval/apply is treated as a known-directional quality signal without establishing what "good" is)
  Testability: testable via literature (eval/apply or plan-vs-act ratios as agent quality/health signals; value of richer derived metrics vs dependency cost)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-288
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the HANDOFF-2 "agreed architecture" paragraph. Routed MED. [stated]
    Current status: UNTESTED

ASSUMPTION-289:
  Date identified: 2026-06-08
  Statement: The scheduled-task name embedded in OpenStory's `sessions.label` (the `name="…"` attribute of the `<scheduled-task>` header) is a stable, unique key that joins OpenStory sessions to C2A2 roster agents. As stated in HANDOFF-1: "Identity join SOLVED. OpenStory `sessions.label` = `<scheduled-task name="{taskId}">`; `taskId` == scheduler id == roster key."
  Context: The identity-join foundation for every per-agent statistic in the Explorer. HANDOFF-3 hardened it against the 50-char label truncation via deterministic unique-prefix matching against `agent_map.json`; HANDOFF-4 found the `name=` value sits early enough in the label to survive truncation directly.
  Type: architectural / methodological (join-key stability and uniqueness)
  Related decisions: DECISION-053
  Related presumptions: PRESUMPTION-325 (the roster presumes one-cron-task-per-agent; multi-fire and interactive sessions do not map cleanly)
  Testability: framework commitment, but VERIFIED in-session — not a literature claim
  Status: GROUNDED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-289
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the stated "identity join SOLVED" claim and GROUNDED in-session — all 7 thinker-pairs' eval/apply counts reconcile EXACTLY against independent SQL, session totals match (572), prefixes are unique (no ambiguous matches), and the only uncaptured roster agent (`execution-assistant`) genuinely has no runs. Held — GROUNDED, not routed (a verification-success, parallel to the handling of ASSUMPTION-285/277/282). [stated]
    Current status: GROUNDED

ASSUMPTION-290:
  Date identified: 2026-06-08
  Statement: The OpenStory capture gap (it watches `~/.claude/projects/` but agents run as Cowork sessions under `~/Library/Application Support/Claude/local-agent-mode-sessions/`) should be solved with an external symlink "session bridge," NOT by forking OpenStory, so that Tom can keep syncing upstream. As stated in HANDOFF-1: "use an external session bridge (NOT an OpenStory fork — Tom syncs upstream)."
  Context: A build-vs-fork / adapter-pattern decision. The capture gap left 4 of 7 thinker pairs at zero; rather than patch `paths.rs` in a fork, the chosen fix is an external bridge that symlinks Cowork transcripts into OpenStory's expected `{project}/{session}.jsonl` shape (validated: 1,508 symlinks; capture climbed from 28→64 slugs).
  Type: architectural / methodological (adapter-over-fork to preserve upstream mergeability)
  Related decisions: DECISION-053
  Related presumptions: PRESUMPTION-326 (the bridge + bounded-window ingest under-represents low-frequency agents)
  Testability: testable via literature (vendoring/forking vs adapter/shim patterns; cost of staying on upstream; reversibility of integration choices)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-290
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the HANDOFF-1 fix-scoping ("NOT an OpenStory fork — Tom syncs upstream"). Routed LOW. [stated]
    Current status: UNTESTED

ASSUMPTION-291:
  Date identified: 2026-06-08
  Statement: Shared wiki-node references are a meaningful relational signal between agents — a valid edge model for the planned agent sociogram (connect agents whose sessions touch the same nodes in the 1647-node narration graph). As stated in HANDOFF-3 (decision 3) and HANDOFF-4 (decision 2): "Sociogram edges = shared wiki-node references."
  Context: The chosen edge model for subtab 2 (deferred to a future session). HANDOFF-4 confirmed *feasibility* by probing the DB (4,205 agent-pairs share ≥1 wiki node; 953 share ≥3) — but feasibility (density) is distinct from the claim that co-reference indicates a *meaningful* inter-agent relationship.
  Type: epistemic / methodological (co-reference as a proxy for meaningful relatedness)
  Related decisions: DECISION-053
  Related presumptions: PRESUMPTION-322 (telemetry-as-proxy), PRESUMPTION-327 (legibility/ranking as benign)
  Testability: testable via literature (co-citation / co-reference network analysis; bibliographic coupling; whether shared-reference edges recover meaningful structure)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-291
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the stated edge model for the sociogram (HANDOFF-3/4). Feasibility confirmed in-session; meaningfulness untested. Routed MED. [stated]
    Current status: UNTESTED

ASSUMPTION-292:
  Date identified: 2026-06-08
  Statement: The existing 571/572-session OpenStory DB is representative enough to build and prove the extraction → injection pipeline now, without first running the riskier Phase-B full reseed. As stated in HANDOFF-3 (decision 1): "build on the current DB first … current 571-session DB already has every thinker-pair with real eval/apply, so the pipeline is provable without reseeding."
  Context: A sequencing / caution-over-speed judgment (Tom's Rule: bias caution over speed). HANDOFF-2's reseed attempt had perturbed the running instance (the NATS max-payload outage); HANDOFF-3 chose to defer reseeding and build against the DB already on disk, deferring Phase-B seed (#8) to a later session.
  Type: methodological (sufficiency of available data to validate a pipeline; sequencing under risk)
  Related decisions: DECISION-053
  Related presumptions: PRESUMPTION-326 (recent/available data is representative; low-frequency + pre-tool-field agents are under-captured)
  Testability: testable empirically (compare pipeline outputs pre- vs post-reseed) / literature (build-on-available-data vs full-backfill-first)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-292
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the HANDOFF-3 sequencing decision. Routed LOW. [stated]
    Current status: UNTESTED

## 2026-06-09 batch (Agent 14a — heavily attended day: dyad-MMA measurement charter, ISME 2026 talk plan, sociogram de-BOSCO + browser verify)

ASSUMPTION-293:
  Date identified: 2026-06-09
  Statement: Tom's integrative perspective ("what it is to think like me, having learned from them") is a real tradition T with Tom as its mature member, and an MM-of-1 can authoritatively certify its milestones. As stated: "I can authoritatively say what anyone else must master to think like me about the areas these thinkers have helped me integrate," and "For pilot purposes, I could probably tease out a set of PRS triplets from each that I consider milestones on the pathway to mastery of this tradition--mine."
  Context: OpenStory measurement-framework session; the human-cohort question for the first Community Concept Inventory. The session scoped the validity claim explicitly: at N=1 the instrument measures "second-language competence in Tom's perspective," not maturity validated across a body; face validity (FCI-style hard-to-deny quality) must partly carry what inter-rater agreement would otherwise carry.
  Type: epistemic / methodological
  Related decisions: DECISION-054
  Related presumptions: PRESUMPTION-333 (no test-retest check on the single rater)
  Testability: testable via literature (single-expert/single-rater validity; face validity in concept inventories, e.g., FCI; expert-authored vs consensus-authored instruments)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-293
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the measurement-framework session, exact quotes. Routed MED. [stated]
    Current status: UNTESTED

ASSUMPTION-294:
  Date identified: 2026-06-09
  Statement: "The evidential weight of any MMA scales with the formational independence of its members" — agreement between maximally-differently-formed members is the signal; agreement between identically-formed members (near-copy agents) is noise, close to chance. The Tom⇄Claude dyad is "the smallest cohort with non-trivial formational independence."
  Context: Articulated by Claude in response to Tom's pushback (2) that human-agent agreement ≠ agent-agent agreement; ratified by Tom into Charter v1 as a load-bearing agreement. Tied to the framework's master metric ("signals of departure from random distribution of outcomes").
  Type: epistemic
  Related decisions: DECISION-054
  Related presumptions: PRESUMPTION-330 (dyad identity across sessions)
  Testability: testable via literature (inter-rater independence and agreement statistics; diversity effects on ensemble/judgment validity; departure-from-chance measures; echo-chamber/correlated-error effects on concordance)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-294
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the measurement-framework session and Charter v1. Routed HIGH. [stated]
    Current status: UNTESTED

ASSUMPTION-295:
  Date identified: 2026-06-09
  Statement: The dyad-MMA is valid only if the agent member can genuinely fail/withhold: "The instrument only measures something if I can fail your test." If the agent concurs from formation-pressure to agree, "the effective independence is lower than it looks, and the dyad quietly collapses back toward MM-of-1 with extra steps." Logged disagreements are first-class evidence; Tom's Rules 1/12 function as the methodological safeguard.
  Context: The sycophancy caveat in the measurement-framework session; captured in Charter v1 ("the agent must be able to fail Tom's test or the dyad collapses to MM-of-1").
  Type: methodological
  Related decisions: DECISION-054
  Related presumptions: PRESUMPTION-330
  Testability: testable via literature (LLM sycophancy/agreeableness under RLHF; demand characteristics; whether structural invitations to dissent measurably restore independence)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-295
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the measurement-framework session and Charter v1. Routed HIGH. [stated]
    Current status: UNTESTED

ASSUMPTION-296:
  Date identified: 2026-06-09
  Statement: Tom's two existing ladder tools ("one covering all of UG physics, and the other covering a core doc describing a large proper subset of the 15 thinker set") "double as ladders with implied curricular milestones" — i.e., curricular scaffolds can yield candidate PRS-elements for dyad ratification.
  Context: Closing move of the measurement-framework session; set as task one for the next attended session ("resume the measurement prototype"). The handoff explicitly scopes them as scaffolds whose implied milestones are *candidate* PRS-elements, not the tradition itself.
  Type: methodological / empirical
  Related decisions: DECISION-054
  Testability: testable empirically (the first triplet pass) / via literature (curriculum-to-assessment milestone derivation; learning progressions as instrument scaffolds)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-296
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Tom's closing instructions, exact quote. Routed LOW-MED. [stated]
    Current status: UNTESTED

ASSUMPTION-297:
  Date identified: 2026-06-09
  Statement: A table-exhaust-revisit rule is an adequate stopping rule for MMA capture: "if we can't agree in one manageable session, then we table it, move through all candidates for agreement proposed by either of us, and revisit tabled issues--or issues ... sufficiently discussed to mark disagreement--prior to calling the whole MMA-capture of what we agree about, closed."
  Context: Tom's answer to the disagreement-handling question (block vs record); adopted in Charter v1 as the disagreement-closure protocol, with disagreements preserved as data rather than blocking.
  Type: methodological
  Related decisions: DECISION-054
  Testability: testable via literature (Delphi method stopping rules; structured consensus protocols; adjournment/closure criteria in deliberation)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-297
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the measurement-framework session, exact quote. Routed LOW. [stated]
    Current status: UNTESTED

ASSUMPTION-298:
  Date identified: 2026-06-09
  Statement: Deliberate over-promising under AI acceleration is a sound planning method: "Knowing the pace of AI acceleration when I submitted my abstract in Feb 2026, I deliberately over-promised with firm expectation that I could over-deliver on the promise I couldn't yet see how to deliver. The results are not disappointing." Extended the same day to the ISME deliverable ("not only a paper, but multiple papers to multiple audiences, with multiple media beyond papers").
  Context: ISME 2026 talk-planning session (Edinburgh, July 8); the doctrine now drives the over-deliver portfolio (QR → landing hub, four audience-specific papers, walkthrough, invitation page) on a week-by-week schedule.
  Type: methodological (planning under accelerating capability)
  Related decisions: (ISME portfolio plan; un-numbered)
  Related presumptions: PRESUMPTION-332 (capacity persistence to July 8)
  Testability: testable via literature (stretch goals and goal-setting; planning fallacy vs capability-growth forecasting; commitment devices)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-298
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Tom's ISME-session message, exact quote. Routed LOW. [stated]
    Current status: UNTESTED

ASSUMPTION-299:
  Date identified: 2026-06-09
  Statement: Removing every "bosco"/"email" string from `agents_tab.html` (all four locations: roster, telemetry, .md map, Schedule narration) removes the public exposure — the stated completion criterion was "zero 'bosco' and zero 'email' strings remain," validated by node --check + the house validator. Rationale as stated: the Schedule narration "describing Gmail body-scraping is exactly what shouldn't be on a public site."
  Context: Sociogram de-BOSCO session. Scope was explicitly bounded in-session: 8 `gmail` tool-name strings remain in the (interactive) bucket aggregate, judged out of scope and flagged to Tom.
  Type: architectural / security-hygiene
  Related decisions: DECISION-047 (park git-history scrub — the parked history question is adjacent)
  Related presumptions: PRESUMPTION-329 (working-tree scrub ≠ history/published-copy scrub)
  Testability: testable empirically (search history/published artifacts for residual strings)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-299
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the de-BOSCO session's stated completion criterion. Routed LOW. [stated]
    Current status: UNTESTED

ASSUMPTION-300:
  Date identified: 2026-06-09
  Statement: Tradition-seeded agent dialogue is an adequate — indeed superior — delivery of the abstract's promised "GAN-simulated" interaction: "what I called GAN-simulation in the abstract arrived instead as tradition-seeded agent dialogue — better, because the agents are inspectable."
  Context: ISME talk-planning session; proposed as an honesty-flag concession line for promise 3 of the submitted abstract, under Tom's blanket license ("take license here ... you have it implicitly, subject to constitutional rules").
  Type: empirical / methodological
  Related decisions: (ISME talk plan; un-numbered)
  Testability: testable via literature (adversarial/self-play simulation vs transparent multi-agent dialogue; inspectability as a scientific virtue in simulation)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-300
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the ISME session's concession framing; Tom-licensed rather than Tom-quoted. Routed LOW-MED. [stated]
    Current status: UNTESTED

ASSUMPTION-301:
  Date identified: 2026-06-10
  Statement: The substrate layer's reveal behavior is correct because it shares the admission code path already verified for the other two layers: "substrate uses the identical both-endpoints-visible admission path already proven for the other two layers — an edge renders only when both endpoints' groups are visible." Asserted after the direct observation attempt stalled the renderer (two 45s CDP timeouts).
  Context: Sociogram verification session — the substrate-on-reveal check could not be captured live; correctness was claimed from code-path identity instead of observation.
  Type: methodological (verification by structural identity)
  Related decisions: DECISION-053 (ADVANCED), DECISION-055
  Related presumptions: PRESUMPTION-334
  Testability: testable empirically (toggle a wiki group after the budgeted-render refactor and observe substrate activation directly)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-301
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the sociogram session, exact quote. Routed MED. [stated]
    Current status: UNTESTED

ASSUMPTION-302:
  Date identified: 2026-06-10
  Statement: The renderer stall on heavy group toggles is caused by the synchronous DOM build of 30,000 hidden line elements under the legacy MAX_EDGES cap — "the synchronous build of 30k <line> elements was the culprit, not the force sim" — so rendering only the budgeted edges will both clear the stall and remove the two misleading "30000" readouts.
  Context: Tom caught the contradictory counters ("2374 / 2400 nodes · 30000 edges in view" vs "2500 shown / 30000 pass / 62153 total edges"); a live probe confirmed 30000 line elements in the DOM with only 2500 displayed; Tom then ratified the architectural fix (DECISION-055).
  Type: architectural / empirical (performance causality)
  Related decisions: DECISION-055
  Related presumptions: PRESUMPTION-335
  Testability: testable empirically (post-refactor heavy-group toggle latency; stall gone or not)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-302
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the sociogram session's causal diagnosis, exact quote. Routed MED. [stated]
    Current status: UNTESTED

ASSUMPTION-303:
  Date identified: 2026-06-10
  Statement: Agent actor nodes are "cumulative telemetry, not single-dated events," so the correct fix for the time-slider bug (actors were given date:'' and an empty date fails the `d && d >= threshold` cut, vanishing all 26 actors at once) is to exempt the agent-activity group from the date cut.
  Context: Tom's Q2 in the sociogram session ("Why does the time slider nix all agent activity at once?") — acknowledged in-session as "Real bug, my fault," with the exemption folded into the DECISION-055 refactor.
  Type: architectural / methodological (data semantics)
  Related decisions: DECISION-055
  Testability: testable empirically (slider behavior post-fix) — but the semantic claim (actors are timeless aggregates rather than datable events) is a design commitment worth a literature look (temporal modeling of aggregate vs event entities)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-303
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the sociogram session's bug diagnosis, exact quote. Routed LOW. [stated]
    Current status: UNTESTED

ASSUMPTION-304:
  Date identified: 2026-06-10
  Statement: Embedding the two ladder tools in the Community Education Tab — Tom: "All of UG physics tool now added to C2A2 Explorer's Community Education Tab as Physics Explorer. Core doc as RC Document Explorer. (That's task 1.)" — fulfills TASK ONE's provisioning of candidate-milestone scaffolds for the dyad's first triplet pass.
  Context: Measurement-prototype session pickup; the ISME paper ("4 Models of Cultural Exchange") was re-uploaded in the same message; sequence agreed: review, then authoring pass.
  Type: methodological
  Related decisions: DECISION-054 (task one)
  Related assumptions: ASSUMPTION-296 (ladder tools as scaffolds of candidate PRS-elements)
  Testability: testable empirically (does the first triplet pass actually draw candidate milestones from the two explorers?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-304
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Tom's task-one delivery message, exact quote. Routed LOW-MED. [stated]
    Current status: UNTESTED

ASSUMPTION-305:
  Date identified: 2026-06-10
  Statement: The Back-button desync in the Explorer shell is caused by iframe `setAttribute('src', …)` pushing entries into the browser's shared session history; switching sub-tab/chapter swaps to `contentWindow.location.replace()` plus adopting the iframe as source of truth on load/`pageshow` eliminates the tab-bar/content desync in both directions.
  Context: Education-tab session; Tom reported the bug with a screenshot ("Backing up in the browser nav gets you the wrong explorer"); two-part fix applied and verified live — post-Back probe read iframe `physics_explorer.html`, chapter "Community Education" active, sub-tab "Physics Explorer" active, all agreeing.
  Type: architectural (browser history semantics)
  Related decisions: (education-tab fix tally; un-numbered)
  Testability: verified empirically in-session
  Status: GROUNDED (in-session browser verification) — HELD from lit-search routing per the no-GROUNDED-routing precedent
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-305
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the education-tab session; diagnosis and fix verified live in the same session. Held, not routed. [stated]
    Current status: GROUNDED

ASSUMPTION-306:
  Date identified: 2026-06-10
  Statement: On history restore, the iframe's actual content is the authoritative state: "The shell now adopts the iframe as the source of truth on load/`pageshow`: it reads what the iframe actually contains and lights up the matching chapter + sub-tab, instead of rendering its default state under foreign content."
  Context: Second half of the Back-button cure — a standing architectural commitment (content-over-shell authority) that generalizes beyond the verified bug instance.
  Type: architectural
  Related assumptions: ASSUMPTION-305
  Testability: testable empirically (other restore paths: bfcache, tab duplication, session restore)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-306
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the education-tab session, exact quote; separated from grounded ASSUMPTION-305 because the general authority principle exceeds the verified instance. Routed LOW. [stated]
    Current status: UNTESTED

ASSUMPTION-307:
  Date identified: 2026-06-10
  Statement: Git-history-derived yield is a valid productivity axis for the Agent Metabolism view — "the live git-derived yield axis," "the yield wave reading straight from your vault's git history" — with OpenStory per-session token usage as the cost side (the token-usage fact itself was verified in-session against the DB).
  Context: Pathway 29 (Agent Metabolism) session; metabolism = tokens consumed vs artifacts yielded, rendered as raster / system-pulse waveform / returned-vs-sent views, shipped to the live site.
  Type: epistemic / empirical (proxy validity)
  Related decisions: DECISION-056
  Related presumptions: PRESUMPTION-339
  Testability: testable via literature (commit counts as productivity proxies; goal-proxy divergence in software metrics) and empirically (yield axis vs PRS-triplet completion once integrated)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-307
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the metabolism session's shipped design description. Routed MED. [stated]
    Current status: UNTESTED

ASSUMPTION-308:
  Date identified: 2026-06-10
  Statement: A deterministic scheduler should precede any bandit layer in agent-activity optimization — framed in-session as one of the open questions Pathway 29 hands to the OpenStory thread: "the deterministic scheduler before any bandit layer."
  Context: Pathway 29 session closing framing; an ordering commitment (predictability before adaptive allocation) stated as settled enough to hand off.
  Type: architectural / methodological
  Related decisions: DECISION-056
  Testability: testable via literature (when do adaptive/bandit schedulers pay off vs deterministic baselines; premature optimization of allocation policies)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-308
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the metabolism session's handoff framing. Routed LOW-MED. [stated]
    Current status: UNTESTED

ASSUMPTION-309:
  Date identified: 2026-06-10
  Statement: Progress and peace require distinct KPIs: "the progress/peace KPI distinction (MacIntyre number for progress; endorsed-steelman, not agreement, for peace)." Peace is operationalized as each side endorsing a steelman of the other, explicitly not as agreement.
  Context: Pathway 29 session closing framing; carries the project's constitutional aim into the metabolism metric design.
  Type: epistemic / normative-methodological
  Related decisions: DECISION-056
  Related presumptions: PRESUMPTION-339
  Testability: testable via literature (perspective-taking and steelmanning vs agreement as conflict-resolution measures; intergroup-contact outcome measures distinguishing understanding from convergence)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-309
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the metabolism session's KPI framing, exact quote. Routed MED. [stated]
    Current status: UNTESTED

ASSUMPTION-310:
  Date identified: 2026-06-11
  Statement: Narrative-embedded perspective is the principle of individuation within conscious realist monism — "if all consciousness is narrative-embedded perspective, then different narratives, different perspectives, are the principle of individuation: there is nothing else; everything else is a constructed model, an instance of differentiation we can eventually compute down to the computationally irreducible, the stable and surviving elements of conscious life."
  Context: Measurement round 1 close (DECISION-054 charter); Tom's for-the-record comment on M5, advanced as a candidate solution to the decomposition/individuation problem; seeded as round-2 rung M7.
  Type: epistemic / architectural
  Related decisions: DECISION-054
  Related items: ASSUMPTION-208 (progress as better compression), PRESUMPTION-222 (MDL/codelength proxies — proxy-only verdict), M7 rung
  Testability: testable via literature (narrative theories of self and individuation; the decomposition/individuation problem in idealism, cosmopsychism, and IIT; principium individuationis treatments)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-310
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the round-1 measurement session, Tom verbatim. Routed HIGH — load-bearing for M7. [stated]
    Current status: UNTESTED

ASSUMPTION-311:
  Date identified: 2026-06-11
  Statement: Multi-starting-point derivability is convergence evidence — "if perspective-as-narrative individuates from within CRm, from Tononi-style phenomenology, *and* from a computational frame, that's convergence evidence of exactly the kind M3–M4 trade in." Operationalized in M7's S: present the solution from two of three starting points.
  Context: Round-1 close, agent member's logged note on Tom's M5 comment; dyad-adopted into M7's success criterion in round 2.
  Type: epistemic / methodological
  Related decisions: DECISION-054
  Related items: M7 rung; ASSUMPTION-310
  Testability: testable via literature (robustness analysis, triangulation, consilience as evidence; multiple-derivability arguments in philosophy of science)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-311
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the round-1 session, agent member stated, dyad-operationalized in round 2. Routed MED. [stated]
    Current status: UNTESTED

ASSUMPTION-312:
  Date identified: 2026-06-11
  Statement: Methodological Thomism — "what is distinctive about Thomism, according to MacIntyre, is not so much the particular blending of the aristotelian and neoplatonic/christian frameworks, but the recognized need and methodology for doing so. In that sense, any adequate resolution of the problem of conflicting perspectives, of rationality, will be Thomist: that's advanced as a claim." The stronger claim (only Thomism can supply the final-causality account contemporary sciences need) is explicitly NOT asserted.
  Context: Round-1 close, Tom's for-the-record comment on M6 (agreed as claim (a), retitled "candidate home"); seeded as round-2 rung M8 with falsifiers and riders baked into R. The agent member logged a caution for the round-2 rung: the claim needs a specification of what a successful non-Thomist integration would look like, or "Thomist" names whatever succeeds — true by definition.
  Type: epistemic
  Related decisions: DECISION-054
  Related items: M6/M8 rungs; ASSUMPTION-313
  Testability: testable via literature (MacIntyre scholarship — Three Rival Versions, Whose Justice; integrationist methodology in tradition-conflict; definitional-truth/falsifiability critiques)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-312
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the round-1 session, Tom verbatim including his own claim/non-claim demarcation. Routed HIGH — load-bearing for M8. [stated]
    Current status: UNTESTED

ASSUMPTION-313:
  Date identified: 2026-06-11
  Statement: Taking the weaker reading of each contested rung as the agreement resolves the way forward without either side conceding what it holds — "in general, take the weaker versions of each as our agreement... That resolves the way forward, does it not?" (Tom); "we agree without either side conceding anything we hold" (agent member).
  Context: Round-1 close; the dyad's first contested-rung closure method (applied to M5 and M6).
  Type: methodological
  Related decisions: DECISION-054
  Testability: testable via literature (incompletely theorized agreements; minimal joint commitment; overlapping consensus as a stable agreement mechanism)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-313
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the round-1 closing exchange, both members quoted. Routed MED. [stated]
    Current status: UNTESTED

ASSUMPTION-314:
  Date identified: 2026-06-11
  Statement: Falsifier (b) rephrased as a positive prediction and the master plan §6 "interaction yield" are the same measurement — "round 1's six `agreed` rungs are the first countable PRS-milestone yield in existence, and the dual-reasons rule means every future agreement carries an agreement-for-different-reasons count — falsifier (b) and §6's interaction yield turn out to be the same measurement."
  Context: Round-2 session, after locating yield categories across GH main (flat git proxy only), the dev pipe (design only), and OpenStory telemetry (no yield fields); milestone-rung agreement proposed as the first countable PRS-milestone yield.
  Type: epistemic / methodological
  Related decisions: DECISION-054, DECISION-056
  Related items: ASSUMPTION-307 (git-yield proxy), PRESUMPTION-339 (exhaust-tracks-aim REVISE)
  Testability: testable via literature (convergent operationalism; construct identity vs correlated proxies) and empirically (do the two counts diverge once both are instrumented?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-314
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the round-2 session's yield-category trace, exact quote. Routed MED-HIGH — it wires the measurement charter into the metabolism metric. [stated]
    Current status: UNTESTED

ASSUMPTION-315:
  Date identified: 2026-06-11
  Statement: Logging each dyad member's reasons separately preserves the evidence that distinguishes genuine agreement from convergence-by-adjudication — the dual-reasons rule, binding from round 2; adopted as the resolution of the self-adjudication concern, with Tom's "we agree about what we now both think" formulation quoted and insularity named as the successor risk.
  Context: Round-2 session, recorded in the pass design §2 and step 5.
  Type: methodological
  Related decisions: DECISION-054
  Related items: M7/M8 pending-dyad entries (assents with reasons logged separately); OPEN-079
  Testability: testable via literature (independent justification elicitation; hidden-profile effects; reason-giving and groupthink countermeasures in small-group deliberation)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-315
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the round-2 session's closure recording. Routed MED. [stated]
    Current status: UNTESTED

ASSUMPTION-316:
  Date identified: 2026-06-11
  Statement: Commits scoped to exactly the session's own files — "the 118 other working-tree changes (architecture ledgers, telemetry files, etc.) belong to other sessions and were deliberately left out per your provenance rule" — keep repository provenance clean and the repo healthy for future commits.
  Context: Sociogram ship session; commit 2f941aa (six files), pushed by Tom; described in-session as provenance-clean.
  Type: methodological / architectural
  Related decisions: DECISION-053, DECISION-055
  Related items: PRESUMPTION-337 (single-gate scaling — dispositioned REVISE 2026-06-11; this rule is the mechanism that grows the local-only queue REVISE-102 targets)
  Testability: testable via literature (atomic/cohesive change-sets vs batch integration risk; tension with WIP-limit findings already returned under REVISE-102)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-316
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the sociogram session's commit rationale, exact quote. Routed LOW-MED — already adjacent to a REVISE disposition. [stated]
    Current status: UNTESTED

ASSUMPTION-317:
  Date identified: 2026-06-14
  Statement: Marking a Summa item as QC-passed resets its staleness clock, so marking a transcript-only pass while its synthesis half is still un-reviewed would mask the Layer-4 reviewer's later full pass — therefore synthesis halves were "deliberately left unmarked so the Layer-4 reviewer's full pass isn't masked by a reset staleness clock."
  Context: Automated-only day (Sun 2026-06-14). Summa QC sweep refetched/fidelity-checked Days 201–205 + 126 (all six PASS) and marked them transcript-pass only; the run's logged rationale made the marking/staleness interaction explicit.
  Type: methodological
  Related decisions: (none new; QC-marking policy, supports OPEN-082 remediation)
  Related items: OPEN-082 (parser/linker marking path — the unmarkable 65 bottom-frontmatter files are the failure case this policy is trying to keep legible); PRESUMPTION-344 (queue-emptiness-as-health, same metrics-legibility family)
  Testability: testable empirically (does partial marking measurably degrade downstream reviewer coverage? staleness-clock policy can be A/B'd against a separate sub-component clock)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-317
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-14 QC-sweep logged rationale (recorded in the evening cowork summary), exact-quote fragment retained. Automated-day extraction — single stated methodological assumption; no attended design session occurred. [stated]
    Current status: UNTESTED

ASSUMPTION-318:
  Date identified: 2026-06-15
  Statement: Files-added-per-day is the right headline "yield" series for the Agent Metabolism view — "I'll make files-added/day the headline yield series" (adopted as Tom's reading of his "use added files" answer). It is treated as a better proxy for productive metabolic output than the token-based or git-commit-proxy series it replaces as the lead axis.
  Context: WS1 (metabolism cut-offs) of the 2026-06-15 attended session ("Metabolism visualization and conscious realist monism"). Chosen via AskUserQuestion and rendered into `metabolism_view_REVIEW.html`; carried forward in the patched generator.
  Type: methodological / empirical
  Related decisions: DECISION-057 (metabolism measurement charter); DECISION-056 (metabolism ship); ASSUMPTION-307 (git-history yield proxy), ASSUMPTION-314 (interaction-yield falsifier)
  Related items: PRESUMPTION-349 (file-count ≈ yield commensurability — the unstated premise beneath this stated choice)
  Testability: testable empirically (does files-added/day track independently-rated research output better than tokens or commits? construct-validity check against a hand-scored yield sample)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-318
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the WS1 design rationale and the AskUserQuestion resolution, exact-quote fragment retained. Routed MED — it sets the headline metric for a deployed self-measurement artifact. [stated]
    Current status: UNTESTED

ASSUMPTION-319:
  Date identified: 2026-06-15
  Statement: The git history of `wiki/traditions/*/prs_triplets.md` supplies valid "triplet-completed" dates — minting a new `PRS-NN` id per commit-day from that history is an adequate source for the PRS-triplet yield dimension. Chosen over the alternative candidate source.
  Context: WS2 (PRS-triplet yield) of the 2026-06-15 session. Settled via AskUserQuestion; the metric is not yet built ("the clean next increment").
  Type: methodological
  Related decisions: DECISION-058 (PRS-triplet yield source); DECISION-056 (metabolism ship, which named PRS-completion as the next yield dimension)
  Related items: PRESUMPTION-350 (commit timestamps clock knowledge-production events — the unstated premise beneath this choice); OPEN-081 (authoritative PRS counts)
  Testability: testable empirically (do prs_triplets.md commit-days coincide with when a triplet was actually completed, vs. batch edits / retroactive commits / formatting touches that would inflate the count?)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-319
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the WS2 source-selection rationale. Routed MED — defines the data source for an unbuilt metric, cheap to revisit before build. [stated]
    Current status: UNTESTED

ASSUMPTION-320:
  Date identified: 2026-06-15
  Statement: Making a data gap visually explicit is preferable to hiding or interpolating it — the view should render absence "honestly" (a dashed "interactive capture ends" horizon for the Apr-6 cliff; hollow rings for cadence-only / zero-token lanes; gap-honest day-bars instead of flat-zero valleys; a staleness badge for the stale right edge) rather than let missing data read as real zeros.
  Context: WS1 of the 2026-06-15 session; the four cut-offs were "made honest" in the view layer while the two database-layer causes remained undiagnosed pending the Mac probe.
  Type: methodological / epistemic
  Related decisions: DECISION-057 (metabolism measurement charter)
  Related items: PRESUMPTION-351 (a visible gap-marker is an understood gap — the unstated premise); PRESUMPTION-352 (the cliff is a capture artifact, not real activity); the trace-vs-substance presumption family (PRESUMPTION-322 et al.)
  Testability: testable via literature (graphical integrity / honest representation of missing data; signalling absent vs. zero values in time-series visualization; deception-by-omission in dashboards)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-320
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the WS1 "make them honest in the view" rationale across four cut-off fixes. Routed LOW-MED — a representational-integrity commitment, partly a framework value. [stated]
    Current status: UNTESTED

ASSUMPTION-321:
  Date identified: 2026-06-15
  Statement: The CRM "team" is the set of 15 `wiki/traditions/` folders — "fifteen tradition folders = the 15 members (14 thinkers + MacIntyre as the epistemologist of rationality, with Loughran as integrator)." Each folder maps to one named member with a real one-line contribution, and this roster grounds the WS3 mockups (Roster, 40-Step Dialogue Track, Paradigm Constellation).
  Context: WS3 (CRM team mockups) of the 2026-06-15 session; the roster was pulled live from the vault to keep the mockups semantically grounded rather than placeholder.
  Type: architectural / structural
  Related decisions: DECISION-056; (no new numbered decision — mockups are exploratory)
  Related items: PRESUMPTION-353 (folder-count as authoritative team-membership source); PRESUMPTION-354 (rival-team / open-seat contest framing); the standing "traditions are the right unit of analysis" structural presumption family
  Testability: framework commitment (the 14-thinker + MacIntyre + Loughran roster is a design choice, not a literature-testable claim), though the role assignments (MacIntyre as rationality-epistemologist; Loughran as integrator) are defensible against MacIntyre's own corpus
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-321
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the WS3 roster-construction step, exact-quote fragment retained. Routed LOW — exploratory mockup scaffolding, largely a framework commitment. [stated]
    Current status: UNTESTED

ASSUMPTION-322:
  Date identified: 2026-06-16
  Statement: PRS-triplet "production" is operationalized as the FIRST git appearance of each (tradition, PRS-NN) pair in `wiki/traditions/*/prs_triplets.md` — "the metric counts PRS-triplet production (first git appearance of each (tradition, PRS-NN))." This is the build-level realization of the source settled in DECISION-058: a triplet is counted as produced on the commit-day its id first shows up, and only once.
  Context: WS2 build of the 2026-06-16 attended session ("PRS triplet yield WS-2"). Implemented in `architecture/metrics/prs_yield.py`; outputs in `prs_yield_detail.csv` / `prs_yield_log.csv`.
  Type: methodological / empirical
  Related decisions: DECISION-059 (PRS-yield build charter); DECISION-058 (source settled); DECISION-057
  Related items: ASSUMPTION-319 (git-history source, now built); PRESUMPTION-355 (creation-as-the-production-event); PRESUMPTION-350 (commit-as-clock); PRESUMPTION-359 (git as complete census)
  Testability: testable empirically (does first-git-appearance date coincide with when a triplet was actually completed, vs. drafting-then-committing or backfilled edits? construct-validity check against a hand-dated triplet sample)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-322
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the WS2 build rationale and the `prs_yield_snapshot_lines.md` definition note ("'Yield' counts production (first git appearance...)"). Routed MED — it is the operational definition of a metric now driving two visualizations. [stated]
    Current status: UNTESTED

ASSUMPTION-323:
  Date identified: 2026-06-16
  Statement: A commit-message self-report is an adequate cross-check on the derived yield series — "Cross-check passed: the 06-07 commit message ('+38 PRS triplets') matches the series exactly," and the metric was on that basis declared "built and verified." The agreement of one human-authored commit note with one of the six per-day deltas is treated as validation of the extraction.
  Context: WS2 build of the 2026-06-16 session; cited as the verification step alongside `validate_prs_3d.py` PASS and `node --check` PASS.
  Type: methodological / epistemic
  Related decisions: DECISION-059 (build charter)
  Related items: ASSUMPTION-322 (the series being checked); PRESUMPTION-356 (one corroborating point = series verified)
  Testability: testable empirically (do the other five commit-days have independent corroboration? a full audit of each commit-day's added ids against its message / against an independent record would test whether the single match generalizes)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-323
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the WS2 "Cross-check passed" / "built and verified" statements. Routed MED — the word "verified" is load-bearing on downstream trust in the series. [stated]
    Current status: UNTESTED

ASSUMPTION-324:
  Date identified: 2026-06-16
  Statement: The yield headline should report GROSS cumulative production (264, every id ever first-seen) rather than NET on-disk inventory (262 unique) — "cumulative-produced (264) intentionally exceeds on-disk-unique (262)... worth a sentence so the gap doesn't read as an error." Retired ids (stump/PRS-01, /PRS-03) and a reused id (arkanihamed/PRS-10) are deliberately kept in the cumulative count.
  Context: WS2 build of the 2026-06-16 session; encoded in `prs_yield.py` outputs and the drop-in snapshot block. Flagged fail-loud rather than silently reconciled.
  Type: methodological
  Related decisions: DECISION-059 (build charter)
  Related items: ASSUMPTION-322 (production definition); ASSUMPTION-325 (supersession of 269); OPEN-081 (authoritative PRS counts); OPEN-084 (three-count divergence); PRESUMPTION-357 (counts measure one quantity)
  Testability: framework/measurement choice with an empirical edge (which of gross-produced vs. net-surviving better serves the "metabolism/yield" construct depends on what the series is used to claim — both are defensible for different purposes; testable only relative to a stated use)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-324
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the WS2 "intentionally exceeds" rationale and the fail-loud duplicate/retired-id flags. Routed LOW-MED — a definitional choice made explicit and honestly flagged. [stated]
    Current status: UNTESTED

ASSUMPTION-325:
  Date identified: 2026-06-16
  Statement: The git-derived production series should SUPERSEDE the static "269 network" carry-forward as the authoritative PRS count — "This supersedes the static '269 network' carry-forward with a git-derived production series; the 269 figure was a frozen network count, not a git-derived production series." The newer, traceable measurement is treated as more authoritative than the prior frozen number.
  Context: WS2 build of the 2026-06-16 session; stated in `prs_yield_snapshot_lines.md` and the evening cowork→chat summary. Note: the 3D connectome still renders 269 nodes, so the supersession is asserted at the metric layer while the visualization retains the older count.
  Type: methodological / empirical
  Related decisions: DECISION-059 (build charter); DECISION-056 (metabolism ship)
  Related items: ASSUMPTION-324 (gross-vs-net); OPEN-081; OPEN-084 (269/264/262 divergence); PRESUMPTION-357 (one-quantity presumption)
  Testability: testable empirically (is the 269 connectome count reconcilable to the 264/262 git counts, or do they count different things? auditing the connectome's node source against prs_triplets.md would test whether "supersede" is the right relation vs. "these measure different constructs")
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-325
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit "supersedes the static 269" statement. Routed MED — it changes which number the system treats as authoritative, and sits unresolved against the still-269 connectome (see OPEN-084). [stated]
    Current status: UNTESTED

ASSUMPTION-326:
  Date identified: 2026-06-16
  Statement: The metric should exist before the view layer that depends on it — "iterating visuals before the underlying metric exists is cart-before-horse; the metric should exist before the view layer that depends on it." This sequencing rationale (build WS2 PRS-yield rather than iterate the metabolism/CRM mockups) drove today's direction choice.
  Context: Chat Claude's morning framing on the 2026-06-16 daily walk, adopted as the day's direction; the WS2 build realizing it is the day's headline outcome.
  Type: methodological
  Related decisions: DECISION-059 (build charter); DECISION-057 (metabolism charter, view layer); DECISION-056
  Related items: ASSUMPTION-318 (the headline yield series the view shows); PRESUMPTION-360 (data-backed ⇒ trustworthy-enough-to-build-on)
  Testability: testable via literature (data/metric-before-visualization sequencing in analytics/BI practice; risks of designing views against placeholder data; "measure first" vs. iterative-prototyping methodologies)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-326
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the morning-walk direction rationale (chat_to_cowork summary) and its realization in the WS2 build. Routed LOW-MED — a process/sequencing principle, broadly sound but stated as a general rule. [stated]
    Current status: UNTESTED

ASSUMPTION-327:
  Date identified: 2026-06-16
  Statement: A DETERMINISTIC layout fan is preferable to random jitter for separating co-located 3D nodes — "the deterministic fan is reproducible (stable index order, no randomness), so regens won't reshuffle positions." Co-located triplets (same thinker + year) are spread on a small grid within the thinker's wedge (columns spread angle, rows spread radius), indexed in stable order, specifically so re-generation is reproducible.
  Context: WS2 3D-visualization fix of the 2026-06-16 session; root cause was a layout collision (position keyed only on (thinker, year) → 269 triplets collapsed onto 47 stacks). Implemented in `template_prs_3d.html`; verified to yield 269 distinct positions.
  Type: methodological / architectural
  Related decisions: DECISION-059 (build charter — recorded as a CHANGE under it); DECISION-056
  Related items: PRESUMPTION-358 (visual resolvability = informational fidelity); the trace-vs-substance presumption family
  Testability: partly engineering/framework commitment (reproducibility of a generated layout) with a literature edge (deterministic vs. stochastic layout in information visualization; reproducibility/stability of force or grid layouts across regenerations)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-327
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 3D-fix rationale ("deterministic... reproducible... regens won't reshuffle"). Routed LOW — mostly an engineering-integrity commitment; the fidelity question it raises is carried by PRESUMPTION-358. [stated]
    Current status: UNTESTED

ASSUMPTION-328:
  Date identified: 2026-06-18
  Statement: A single-source-of-truth data path is preferable for the Sociogram summary pop-ups — the pop-up reads each thinker's brief from the same `wiki.md` `**Summary**` block the tradition agents maintain, "so revisions flow into the menu on the next regen — no second copy to drift." `extract_vault_data.py` was edited to pull the `**Summary**` block per thinker (plus `traditions/_extra_summaries.json` for the non-thinker Summa/Traditions briefs) rather than holding a separate copy of the bios.
  Context: 2026-06-18 attended "Thinker summaries for sociogram" build session; the `?` summary-popup feature for the Sociogram tab (shipped as commit `0fdc8ea`).
  Type: architectural
  Related decisions: DECISION-060 (sociogram summary-popup feature + living-bios workflow)
  Related items: ASSUMPTION-329 (never-rerun seed); PRESUMPTION-365 ([inferred] payoff presumes active maintenance)
  Testability: testable via literature (single-source-of-truth / DRY data architecture; avoiding duplicated state to prevent drift; canonical-source patterns)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-328
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit "no second copy to drift" rationale for routing the pop-up through `wiki.md`. Routed LOW-MED — a broadly-accepted data-architecture principle, here applied to bios. [stated]
    Current status: UNTESTED

ASSUMPTION-329:
  Date identified: 2026-06-18
  Statement: After the one-time seed, `apply_summaries.py` must NEVER be rerun, because it would clobber hand-edits by overwriting the `wiki.md` Summary blocks from `approved_summaries.json` — "a loud caveat not to rerun `apply_summaries.py` afterward, since it would clobber hand-edits." The seed script is a one-shot whose re-execution is destructive once `wiki.md` becomes the source of truth.
  Context: 2026-06-18 session; the "living bios" maintenance workflow recorded in the runbook and the handoff (`handoffs/sociogram-thinker-summaries.md`).
  Type: methodological / architectural
  Related decisions: DECISION-060
  Related items: ASSUMPTION-328 (single-source-of-truth); PRESUMPTION-366 ([inferred] guarded only by convention/memory, not code)
  Testability: testable via literature (idempotency; destructive one-shot migration/seed scripts; guard-by-convention vs guard-by-code; technical-debt of armed destructive tooling left in-repo)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-329
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit never-rerun caveat. Flagged as accumulating technical debt — a one-time seed left in place that silently clobbers hand-edits if rerun; the safeguard is a note, not code. [stated]
    Current status: UNTESTED

ASSUMPTION-330:
  Date identified: 2026-06-18
  Statement: `regen_sociogram.sh` is the only supported regeneration path, because it "hardcodes `--summa`, adds the agent layer, and guards against Summa-less builds"; calling `generate_visualization.py` directly is "explicitly forbidden." The canonical wrapper is treated as the golden path that prevents misconfigured (Summa-less) builds.
  Context: 2026-06-18 session; mid-session correction when preparing the clipboard/runbook command sequence.
  Type: architectural / methodological
  Related decisions: DECISION-060; DECISION-059 (PRS build also routed through its own `regen_*` wrapper)
  Related items: ASSUMPTION-331 (local-verify gate)
  Testability: testable via literature (golden-path / canonical build wrappers to prevent operator error; convention of forbidding direct entry-point calls; configuration-as-code guards)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-330
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit "only supported regen path … direct call forbidden" correction. Routed LOW — an engineering-integrity convention. [stated]
    Current status: UNTESTED

ASSUMPTION-331:
  Date identified: 2026-06-18
  Statement: A manual local visual verify on `localhost:8080` "satisfies the constitutional check," making the build clear to push — "You've done the local verify, which satisfies the constitutional check, so you're clear to push." The named verification is human visual inspection (yellow `?` on the 15 thinkers + Summa + Traditions header; pop-ups open/close; no console errors).
  Context: 2026-06-18 session; the pre-push gate, per the project's constitutional rule that localhost review + push stays with Tom.
  Type: methodological
  Related decisions: DECISION-060
  Related items: PRESUMPTION-364 ([inferred] twin — rendering-correctness presumed to imply content-correctness)
  Testability: testable via literature (adequacy of manual/visual QA for generated artifacts; human-in-the-loop verification vs automated checks; what a visual smoke-test does and does not cover)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-331
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit "local verify … satisfies the constitutional check" statement. Its deeper, unstated form (visual render = correct content) is carried by 14b as PRESUMPTION-364. [stated]
    Current status: UNTESTED

ASSUMPTION-332:
  Date identified: 2026-06-18
  Statement: The `?` summary-popup feature is independent of Summa node counts, so the unexplained ~256-vs-~379 commentary-node discrepancy in the regenerated `wiki_narration.html` "doesn't block" the pop-up push — "the `?` feature is independent of Summa node counts." Feature independence was offered as warrant to publish the artifact despite a known, unresolved anomaly inside it (the assistant did recommend a brief hold to confirm, but the stated principle was separability).
  Context: 2026-06-18 session; the push decision, when Tom flagged the missing Summa-day increase and the ~256-vs-379 count gap surfaced.
  Type: architectural
  Related decisions: DECISION-060; OPEN-085 (the count discrepancy itself)
  Related items: PRESUMPTION-368 ([inferred] the two counts are commensurable); OPEN-084 / PRESUMPTION-357 (the 269/264/262 construct-divergence pattern this echoes)
  Testability: testable via literature (separation of concerns / feature independence; shipping artifacts with known-but-orthogonal defects; coupling via a shared generated file)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-332
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the "independent of Summa node counts … doesn't block" reasoning. Routed MED — the feature ships embedded in a 28MB shared artifact (`wiki_narration.html`) that also carries the unexplained Summa count, so "independence" is a claim about a coupled file. [stated]
    Current status: UNTESTED

ASSUMPTION-333:
  Date identified: 2026-06-22
  Statement: Levin's "cognitive glue" (bioelectric signaling as the medium that binds cell collectives into higher-order agents) and Friston's "group-level Markov blanket" (the statistical boundary whose maintenance makes a collective of active-inference agents itself one agent) are "two framings of the same problem" — "what binds sub-agents into a super-agent" — and therefore form "a clean, mathematically explicit Levin↔Friston bridge (cognitive glue ≈ group-level Markov blanket)." The equivalence is stated outright in both proposal files and the day's cowork summary.
  Context: 2026-06-22 session; surfacing and pairing of PROP-2026-06-22-001 (Levin, *Bioelectricity*) and PROP-2026-06-22-002 (Friston, *Entropy*, "As One and Many"); flagged as a paradigm-bridge candidate worth a dispatch to the master agent.
  Type: epistemic / architectural
  Related decisions: (none yet — pair is pending review, not adopted) ; bears on future cross-tradition bridge registration
  Related items: PRESUMPTION-371 ([inferred] twin — that "same problem in two vocabularies" warrants a formal bridge, i.e. cross-vocabulary commensurability)
  Testability: testable via literature (whether a bioelectric binding account and a variational group-Markov-blanket account are formally relatable, or only metaphorically analogous; existing FEP-readings of Levin's bioelectricity)
  Status: CONTESTED (MONITOR-360 continued via DISPOSITION-418, cycle 2, 2026-07-08 — INCORPORATE gated on explicit relational structure-mapping)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-333
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit "same problem in two vocabularies … clean Levin↔Friston bridge" claim stated in both proposals and the cowork summary. Its deeper, unstated form (cross-vocabulary "same problem" ⇒ a real homology to be bridged) is carried by 14b as PRESUMPTION-371. [stated]
    Current status: CONTESTED

ASSUMPTION-334:
  Date identified: 2026-06-22
  Statement: The sub-agent→super-agent binding question is "precisely the move C2A2 needs to model" — "the literal C2A2 individual↔collective transition" — and the two proposals are "the most directly on-mission items in the queue" because they formalize it. The design rationale treats the individual↔collective (member↔tradition/community) transition as C2A2's core target phenomenon, and a paper's value as proportional to how explicitly it formalizes that transition.
  Context: 2026-06-22 session; the "why this matters" framing for both proposals and the cowork summary's ranking of the review queue.
  Type: architectural / methodological
  Related decisions: (none new) ; aligns with the accelerator-detector framing (PRS / tradition-as-agent lineage)
  Related items: ASSUMPTION-333 (the bridge); PRESUMPTION-376 ([inferred] transfer-conditions for applying the formal results to a community of inquirers)
  Testability: framework commitment (that the binding/super-agent transition is C2A2's right target) is partly a foundational choice; the sub-claim that these formalisms apply to traditions is testable via literature (collective active inference; multiscale agency applied to social/epistemic collectives)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-334
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit "precisely the move C2A2 needs … most directly on-mission" rationale. The unstated transfer-condition question (do the papers' conditions hold for a tradition/agent collective?) is carried by 14b as PRESUMPTION-376. [stated]
    Current status: UNTESTED

ASSUMPTION-335:
  Date identified: 2026-06-22
  Statement: The post-Apr-6 "token cliff" was an artifact of the 2026-04-07 schema migration (`data.token_usage` → `data.agent_payload.token_usage`) zeroing the token read path, NOT a real output collapse; reading BOTH payload paths recovers continuous, nonzero assistant-output tokens across the boundary that in fact grow month-over-month (2026-04 ~8.2M, 05 ~20.4M, 06 ~33.3M). Stated as the confirmed resolution of OPEN-083, reached by reaching the live `open-story.db` directly (985 sessions / 173,663 events).
  Context: 2026-06-22 session; OPEN-083 resolution via the both-paths probe.
  Type: empirical
  Related decisions: DECISION-057 (metabolism view); resolves OPEN-083
  Related items: clears PRESUMPTION-352 / MONITOR-349; ASSUMPTION-320 (prior capture-ended inference, now superseded); PRESUMPTION-373 ([inferred] that the both-paths fix is complete)
  Testability: testable empirically (already partly tested via the live-db probe; further regression-checkable by re-reconciling token_usage payloads by run-type and date against an independent activity record)
  Status: GROUNDED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-335
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the OPEN-083 resolution note. Marked GROUNDED rather than UNTESTED — this assumption was validated by C2A2's own direct empirical probe of the live database, not by literature. The residual completeness question (only two paths? future migrations?) is carried by 14b as PRESUMPTION-373. [stated]
    Current status: GROUNDED

ASSUMPTION-336:
  Date identified: 2026-06-22
  Statement: Because output tokens are continuous and growing across the Apr-6 boundary, "downstream yield comparisons do not inherit a masked drop" — i.e., the PRS-yield and metabolism comparisons that had been held under suspicion since 06-15 are now safe to trust. The absence of a real output collapse is taken to license trust in the derived yield metrics.
  Context: 2026-06-22 session; the "reassuring" reading of the OPEN-083 resolution and its effect on the standing PRS-yield over-trust flag.
  Type: methodological
  Related decisions: bears on the standing PRS-yield over-trust HIGH flag and REVISE-121 (disambiguate-don't-reconcile)
  Related items: ASSUMPTION-335 (the underlying telemetry fact); PRESUMPTION-375 ([inferred] that token growth is itself reassuring / more = better)
  Testability: testable via literature (when correcting one telemetry artifact licenses trust in derived downstream metrics; independent failure modes in yield pipelines beyond the corrected read path)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-336
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the "do not inherit a masked drop … safe to trust" inference. Routed MED — it generalizes from one corrected read-path artifact to the trustworthiness of all downstream yield comparisons; the normative "growth = reassuring" sub-move is carried by 14b as PRESUMPTION-375. [stated]
    Current status: UNTESTED

ASSUMPTION-337:
  Date identified: 2026-06-22
  Statement: The proposal-review queue is "review-bound, not search-bound" — the binding constraint since the last decision archive (06-16) is human review throughput, not literature discovery. Stated explicitly: the queue "has been review-bound, not search-bound, since 06-16."
  Context: 2026-06-22 session; cowork summary's diagnosis of the now-5-deep pending review queue.
  Type: methodological
  Related decisions: DECISION-054 (Round 2 still open); the standing proposal-review workflow
  Related items: PRESUMPTION-372 ([inferred] that adding more searched proposals to a review-bound queue is nonetheless progress)
  Testability: testable via literature (theory-of-constraints / bottleneck identification; whether throughput at a non-binding stage is value-adding or merely inventory accumulation)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-337
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit "review-bound, not search-bound, since 06-16" diagnosis. The tension between this stated diagnosis and the day's actual activity (adding two more proposals to the review-bound side) is carried by 14b as PRESUMPTION-372. [stated]
    Current status: UNTESTED

---

## 2026-06-23 cohort (Sewing Agent bootstrap audit + tradition-index session)

ASSUMPTION-338:
  Date identified: 2026-06-23
  Statement: The vault is "intentionally hub-and-spoke, not densely cross-linked" — low backlink density is a design choice, not a defect. Stated: the vault is "large (2,812 pages) and intentionally hub-and-spoke."
  Context: 2026-06-23 Sewing Agent bootstrap audit, TL;DR + overall vault-health assessment.
  Type: architectural
  Related decisions: DECISION-061 (tradition index); the standing knowledge-graph design
  Related items: PRESUMPTION-377 ([inferred] that inbound-backlink count is the right proxy for graph health); PRESUMPTION-383 ([inferred] that hub-and-spoke stays healthy at larger scale)
  Testability: framework commitment (the design intent is a stated choice), but the claim "this topology is healthy" is testable via literature on knowledge-graph / wiki connectivity topologies
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-338
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the bootstrap report's explicit "intentionally hub-and-spoke" framing. The normative half ("this is healthy") is carried by 14b as PRESUMPTION-377. [stated]
    Current status: UNTESTED

ASSUMPTION-339:
  Date identified: 2026-06-23
  Statement: architecture/ system pages (1,676) and inbox/ residue (436) "should not carry backlinks" / "were never meant to carry backlinks"; once they are excluded, the 76.8% orphan rate is "an artifact" and the genuine reconnection surface is small and tractable.
  Context: 2026-06-23 bootstrap audit, Phase 2 classification and overall health assessment. The "77% orphan" alarm is reframed as benign.
  Type: methodological / architectural
  Related decisions: DECISION-061; the connectivity_log.csv metric definition
  Related items: PRESUMPTION-378 ([inferred] that the exclude-by-category move is principled rather than a motivated reclassification); PRESUMPTION-382 ([inferred] that an autonomous one-night census may authoritatively reframe a standing human-tracked alarm)
  Testability: testable empirically — recount orphan rate with a documented, pre-registered inclusion rule for which folders are expected to carry backlinks; check whether the category split is stable under alternative principled definitions
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-339
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit "never meant to carry backlinks … the 77% orphan figure is an artifact" claim. The question of whether the exclusion is principled or convenient is carried by 14b as PRESUMPTION-378. [stated]
    Current status: UNTESTED

ASSUMPTION-340:
  Date identified: 2026-06-23
  Statement: Reconnecting the ~15 orphaned tradition hub pages "would do more for graph health than seeding a thousand leaves" — leverage is concentrated in the hubs, not the leaf pages.
  Context: 2026-06-23 bootstrap audit, "most important single finding" and recommended-actions list.
  Type: methodological
  Related decisions: DECISION-061 (the tradition index built directly on this claim)
  Related items: ASSUMPTION-344 (the index converts 15 orphans into hubs at once); PRESUMPTION-381 ([inferred] that more inbound hub connectivity is unambiguously good)
  Testability: testable via literature (graph-centrality / leverage of hub reconnection vs leaf seeding in network repair) and empirically (measure graph-health deltas of the index fix vs a leaf-seeding sample)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-340
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the "reconnecting ~15 hub pages would do more for graph health than seeding a thousand leaves" leverage claim. [stated]
    Current status: UNTESTED

ASSUMPTION-341:
  Date identified: 2026-06-23
  Statement: Wikilink resolution must match path-qualified `[[a/b/c]]` links, not basename/title only; 893 of 1,740 links are path-qualified, and basename-only resolution failed every one (reported 960 "unresolved" → 67 after the fix; connected hubs 21 → 44). Stated worry: "if the production Sewing Agent resolves links the same (basename-only) way, it may be systematically under-counting hub connectivity" across every prior connectivity_log.csv run.
  Context: 2026-06-23 bootstrap audit, "A note on method (and a resolver bug I caught)."
  Type: empirical / methodological
  Related decisions: the weekly connectivity-census workflow
  Related items: OPEN-087 (does the production resolver handle path-qualified links?); PRESUMPTION-379 ([inferred] that the audit's own corrected resolver is now itself bug-free)
  Testability: testable empirically — inspect the production Sewing Agent's resolver; recompute the historical connectivity_log.csv series under path-aware resolution and compare
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-341
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit resolver-bug finding and the stated worry about the production resolver. Promoted the production-resolver question to OPEN-087. The "my own resolver is now correct" residual is carried by 14b as PRESUMPTION-379. [stated]
    Current status: UNTESTED

ASSUMPTION-342:
  Date identified: 2026-06-23
  Statement: For an unattended autonomous run, the correct output is a trustworthy baseline plus a short, ranked, human-reviewable action list — NOT a ~1,000-page bulk agentic-call mutation. Stated: "a one-shot, unattended mutation of ~1,000 live vault pages … conflicts with the project's standing caution/surgical-change rules. The correct autonomous output here is a report, not a thousand edits."
  Context: 2026-06-23 bootstrap audit, Phase 3 refusal rationale.
  Type: methodological / normative
  Related decisions: the project caution / surgical-change rules; OPEN-088 (explicit seeding policy)
  Related items: PRESUMPTION-380 ([inferred] that the 14-thinker relevance score is the right instrument, only mis-tuned); PRESUMPTION-382 (autonomous reframing authority)
  Testability: framework commitment (an operationalization of the project's stated caution rule), partially testable via literature on safe autonomy / human-in-the-loop thresholds for bulk automated edits
  Status: GROUNDED (enacted — the run produced a report + action list and modified no vault content pages, consistent with the stated rule)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-342
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit Phase-3 refusal rationale; marked GROUNDED because the agent enacted the rule in the same run (no content pages mutated). The seeding-policy question it defers is logged as OPEN-088. [stated]
    Current status: GROUNDED

ASSUMPTION-343:
  Date identified: 2026-06-23
  Statement: Synthesis/bridge stubs should be created only where the link graph demands them (i.e., where `[[*_bridge]]` links are broken); fabricating bridges the graph is not asking for "would be speculative content the link graph isn't asking for." After the resolver fix, essentially every bridge link resolved, so the audit created zero synthesis stubs.
  Context: 2026-06-23 bootstrap audit, Phase 4 synthesis-page inventory.
  Type: methodological / epistemic
  Related decisions: the synthesis/bridge-page workflow
  Related items: PRESUMPTION-384 ([inferred] that absence of a broken bridge link is evidence the bridge is not needed — the graph as self-justifying)
  Testability: testable via literature (demand signals for knowledge synthesis; whether existing link structure can indicate unmet synthesis need) and empirically (audit whether conceptually-warranted bridges exist that no broken link would ever surface)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-343
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit "no synthesis stubs — fabricating them would be speculative content the link graph isn't asking for" rationale. The inference that the graph's silence equals absence of need is carried by 14b as PRESUMPTION-384. [stated]
    Current status: UNTESTED

ASSUMPTION-344:
  Date identified: 2026-06-23
  Statement: A single `traditions/_index.md` page linking all 15 tradition `wiki.md` hubs "would convert 15 orphans into hubs at once." Predicted and then implemented; the regenerated sociogram was browser-verified (index node resolves to all 15 hubs; 2,814 nodes / 71,975 edges; no console errors; no crash-limit warnings).
  Context: 2026-06-23 bootstrap audit recommendation #1, enacted in the 2026-06-23 tradition-index interactive session.
  Type: architectural
  Related decisions: DECISION-061 (this is the decision)
  Related items: ASSUMPTION-340 (hub leverage); PRESUMPTION-381 (more hub connectivity = good)
  Testability: GROUNDED by C2A2's own implementation + live verification; the broader "this materially improves graph health" remains testable via the next connectivity census
  Status: GROUNDED (implemented; sociogram regenerated and browser-verified; content commit made, git push pending on Tom's Mac)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-344
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated "convert 15 orphans into hubs at once" prediction and the tradition-index session that implemented and browser-verified it. Marked GROUNDED on the local-build evidence; push state quoted from session (repo not introspectable from this mount). [stated]
    Current status: GROUNDED

ASSUMPTION-345:
  Date identified: 2026-06-23
  Statement: The knowledge graph is already "sufficient to support meaningful thinker-agent synthesis today"; the marginal gain from mass leaf-seeding "would be low and noisy," while reconnecting the 15 hubs and clearing inbox residue "would be high."
  Context: 2026-06-23 bootstrap audit, overall vault-health assessment.
  Type: empirical
  Related decisions: OPEN-088 (seeding policy); DECISION-061
  Related items: ASSUMPTION-340 (hub leverage); PRESUMPTION-380 (relevance-score instrument); PRESUMPTION-377 (backlink-as-health proxy)
  Testability: testable empirically — measure whether thinker-agent synthesis quality is in fact gated by graph connectivity, and whether a bounded leaf-seeding pass yields measurable synthesis improvement
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-345
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the "sufficient to support meaningful thinker-agent synthesis today … marginal gain from mass leaf-seeding would be low and noisy" assessment. [stated]
    Current status: UNTESTED

---

## 2026-06-24 EOD cohort (Agents 14a) — ASSUMPTION-346..360

*Source sessions (autonomous EOD run, Tom not present): three 2026-06-24 Cowork threads — (1) Cortical Column Architecture / DEVPATH-031 (→ `architecture/31_cortical_column_architecture.md`, `architecture/pathways.md` Pathway 31); (2) Coil/Triplet Falsifier foundational review (→ `architecture/coil_falsifier_preregistration.md` v1.1); (3) Wiki-narration Voice & Navigation build (→ `wiki-narration-voice-nav-session-log.md`, `wiki_narration.html`). The committed architecture artifacts are the day's distilled session record and were read as the transcript source (same standard as DECISION-061's 2026-06-23 extraction). Quotes are from those artifacts.*

ASSUMPTION-346:
  Date identified: 2026-06-24
  Statement: "The accelerator is meant to be built out of the rationalities it studies." Borrowing a thinker from C2A2's own corpus to shape C2A2's architecture is an intended methodology, not incidental — Pathway 29 took Friston's free-energy principle as a metabolism controller; Pathway 31 takes Hawkins' cortical columns as a robustness-and-voting mechanism.
  Context: Pathway 31 (Cortical Column Architecture), framing section.
  Type: methodological
  Related decisions: DECISION-062; Pathway 29; Pathway 31
  Related items: ASSUMPTION-347 (column independence); the self-referential-insight watch (Agent 14a §"self-referential insights")
  Testability: framework commitment (not testable) — a design value about how the system should be constructed, not an empirical claim
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-346
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from Pathway 31's framing ("the accelerator is meant to be built out of the rationalities it studies"). [stated]
    Current status: UNTESTED

ASSUMPTION-347:
  Date identified: 2026-06-24
  Statement: Three columns wired to differ *substantively* (by reference frame — corpus slice and/or analytic axis), not just by random seed, yield genuine robustness and information; "three identical agents run at nonzero temperature are not three columns; they are one column sampled three times," whose 2-of-3 agreement "measures stochastic variance, not robustness." At least two independence axes must vary per column.
  Context: Pathway 31, "What makes the three columns independent (the central decision)" and "The Hawkins mapping … the trap — redundancy alone."
  Type: architectural
  Related decisions: DECISION-062
  Related items: ASSUMPTION-350 (success criterion); OPEN-089 (which two axes); PRESUMPTION-386 (consensus-on-shared-bias), PRESUMPTION-390 (reference-frame transfer condition)
  Testability: testable empirically — compare dissensus/robustness of substantively-wired columns vs seed-only-varied columns on the same thinker
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-347
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the "central design commitment" and "the trap — redundancy alone" passages. [stated]
    Current status: UNTESTED

ASSUMPTION-348:
  Date identified: 2026-06-24
  Statement: Per-thinker and per-claim dissensus rate is a first-class measurable detector output — "exactly the kind of evidence-about-how-positions-behave-under-rich-information that the accelerator/detector aim is after," and "the most interesting payoff of the pathway, beyond mere robustness."
  Context: Pathway 31, "Consensus, dissensus, and the adjudicator" — dissensus as first-class output.
  Type: epistemic
  Related decisions: DECISION-062; constitutional detector aim (measurement_framework.md)
  Related items: Pathway 07 (Unsaid-edges); PRESUMPTION-388 (dissensus-as-signal vs instrument-noise)
  Testability: testable empirically — does measured dissensus localize on claims independent reviewers also judge contestable?
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-348
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "per-thinker and per-claim dissensus rate becomes a measurable detector output." [stated]
    Current status: UNTESTED

ASSUMPTION-349:
  Date identified: 2026-06-24
  Statement: Triple columns plus an adjudicator is "roughly 3–4× the agent and token load per thinker track," which across 15 traditions "collides head-on with Pathway 29 (agentic metabolism) and the project's standing token budgets."
  Context: Pathway 31, "Cost, and why this starts as a one-track pilot."
  Type: empirical
  Related decisions: DECISION-062; Pathway 29 (metabolism controller)
  Related items: ASSUMPTION-350 (pilot discipline); the token-budget rules (project Rule 6)
  Testability: testable empirically — measure actual token/agent multiplier of a forked three-column track vs the incumbent single-agent track
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-349
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the "3–4× the agent and token load" cost estimate. [stated]
    Current status: UNTESTED

ASSUMPTION-350:
  Date identified: 2026-06-24
  Statement: A single-thinker pilot (Hawkins) can validate the consensus mechanism before scaling. The pathway "is justified only if the extra cost buys epistemic quality": triple-column consensus assessments "should survive Tom's review (or an independent check) at a measurably higher rate than single-agent assessments on the same thinker, and the reported dissensus should land on claims a human agrees are genuinely contestable." If not, "the 3–4× cost is not warranted and the pathway should be parked, not scaled."
  Context: Pathway 31, "Success criterion (Rule 4)" and "Cost … one-track pilot."
  Type: empirical
  Related decisions: DECISION-062
  Related items: ASSUMPTION-349 (cost); PRESUMPTION-389 (Hawkins as maximally self-confirming pilot subject); swarm-contract falsifiability
  Testability: testable empirically — this assumption IS the pre-stated falsification test for the pathway
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-350
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicit Rule-4 success criterion. [stated]
    Current status: UNTESTED

ASSUMPTION-351:
  Date identified: 2026-06-24
  Statement: Classifying semantic agreement across three assessments "is a genuine judgment call, so using the model here is correct (Rule 5 — model for classification, not for routing). It is the one place model judgment is licensed; the column fan-out, scheduling, and tallying stay deterministic."
  Context: Pathway 31, "Adjudicator as quality gate."
  Type: methodological
  Related decisions: DECISION-062; project Rule 5 (model only for judgment calls)
  Related items: OPEN-090 (operational definition of agreement); PRESUMPTION-387 (adjudicator competence/bias)
  Testability: framework commitment (not testable) — an application of the project's own Rule 5 boundary; the adjudicator's *reliability* is the testable part (→ OPEN-090, PRESUMPTION-387)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-351
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "using the model here is correct (Rule 5) … the one place model judgment is licensed." [stated]
    Current status: UNTESTED

ASSUMPTION-352:
  Date identified: 2026-06-24
  Statement: Self-testing (a dyad applying its own falsifier to its own ledger) is non-vicious "iff the falsifier is specified independently of the tested outcomes. That independence is real only if specification precedes inspection. Register, then look." (Chang's escape from Simmons et al. researcher-degrees-of-freedom / auditor self-review impairment.)
  Context: Coil falsifier pre-registration §0 (pre-registration attestation) and §0 rationale.
  Type: epistemic
  Related decisions: DECISION-063; REVISE-111 (HIGH — reflexive falsification non-circular)
  Related items: ASSUMPTION-354 (retrospective ungameability); PRESUMPTION-394 (auditor-independence under role-collapse)
  Testability: testable via literature — efficacy of pre-registration against researcher degrees of freedom; conditions under which self-audit is/ isn't vicious
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-352
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the load-bearing §0 clause "Register, then look." [stated]
    Current status: UNTESTED

ASSUMPTION-353:
  Date identified: 2026-06-24
  Statement: "Usefulness is not productivity." The falsifier must be asymmetric: "A FAIL is strong and clean" (a coil predicting no downstream activity above a degree-matched random fiber is decoration); "A PASS is weak by design" — a necessary-condition met, "provisional," never "useful, confirmed." Locking in "downstream yield = usefulness" as a two-sided verdict would warp the architecture toward productivity-ism (the Goodhart hazard).
  Context: Coil falsifier §0b (the asymmetry — what a pass and a fail are each allowed to mean).
  Type: methodological
  Related decisions: DECISION-063; REVISE-105 (falsifier ≠ yield metric), REVISE-115 (yield-count Goodhart), REVISE-124 (built = start of validation)
  Related items: ASSUMPTION-355 (convergence battery); PRESUMPTION-391 (shared-id construct validity); §6 jingle guard
  Testability: testable via literature — construct validity / Goodhart's law / asymmetric (severe) testing in measurement design
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-353
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from §0b "Usefulness is not productivity … A FAIL is strong and clean. A PASS is weak by design." [stated]
    Current status: UNTESTED

ASSUMPTION-354:
  Date identified: 2026-06-24
  Statement: A retrospective-only confirmatory run on "the ledger that already exists as of the registering commit" is "ungameable by construction" because "past behavior cannot be steered by a future rule." Self-noted caveat (stated): "retrospective ≠ clean … retrospect only buys un-gameability by the future, not freedom from the past's idiosyncrasies," so the confirmatory set is used once and treated as "one audit under known limitations, not a timeless verdict."
  Context: Coil falsifier §3 (ungameable-by-construction) + the §3 foundational caveat.
  Type: methodological
  Related decisions: DECISION-063; REVISE-115
  Related items: ASSUMPTION-352 (register-then-look); PRESUMPTION-392 (degree-only null)
  Testability: testable via literature — Campbell's Law / Goodhart; retrospective vs prospective design; one-shot audit validity
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-354
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from §3 defense #1 and its stated foundational caveat. [stated]
    Current status: UNTESTED

ASSUMPTION-355:
  Date identified: 2026-06-24
  Statement: A construct judged on "several operationally independent indicators, not one" is both less single-indicator-fragile and harder to game, "because spoofing three different things is far harder than gaming one"; indicators combine by a pre-fixed decision lattice with "no post-hoc weighting."
  Context: Coil falsifier §2 (convergence battery, safeguard 2) and §4 (decision lattice).
  Type: methodological
  Related decisions: DECISION-063
  Related items: ASSUMPTION-353 (asymmetry); PRESUMPTION-391 (per-indicator validity)
  Testability: testable via literature — multitrait convergence / triangulation; robustness of composite vs single-indicator measures; pre-registered decision rules
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-355
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from §2 "operationally independent indicators … spoofing three different things is far harder than gaming one." [stated]
    Current status: UNTESTED

ASSUMPTION-356:
  Date identified: 2026-06-24
  Statement: The programme claim under test (H1): "A coil between traditions A and B marks a genuine bridge — its formation is followed by elevated cross-A–B resource-sharing in its neighborhood, beyond what a degree-matched random fiber would produce." Null H0: "Coil placement carries no predictive information about subsequent cross-A–B activity beyond node degree."
  Context: Coil falsifier §1 (the claim under test).
  Type: empirical
  Related decisions: DECISION-063
  Related items: ASSUMPTION-357 (synthesis-by-novelty false-negative); narrative_prs_connectome.md ("coils are association fibers, not decoration")
  Testability: testable empirically — this assumption is the pre-registered hypothesis the falsifier runs on the existing ledger
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-356
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from §1 H1/H0 statement. [stated]
    Current status: UNTESTED

ASSUMPTION-357:
  Date identified: 2026-06-24
  Statement: "The deepest worry about [the PRIMARY indicator] is a false negative on real synthesis": genuine fusion of A and B "often coins new vocabulary rather than reusing the parents' resource-ids," so the shared-id test "would score a true bridge as zero." The honest fix is a synthesis-by-novelty indicator — new resource-ids that "descend from resources of both traditions" — but this requires a `derived_from:` lineage field "the schema does not currently record," populated at articulation time. Until then the indicator is exploratory only and "never enters the lattice."
  Context: Coil falsifier §2.4 (synthesis-by-novelty — instrument not built).
  Type: empirical
  Related decisions: DECISION-063; OPEN-091 (derived_from schema field)
  Related items: ASSUMPTION-356 (H1); PRESUMPTION-391 (shared-id validity); "build the instrument before trusting the reading"
  Testability: testable empirically once the lineage instrument exists; the false-negative magnitude is itself measurable
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-357
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from §2.4's stated false-negative worry and its schema prerequisite. [stated]
    Current status: UNTESTED

ASSUMPTION-358:
  Date identified: 2026-06-24
  Statement: Voice queries must respect the "Ask AI" checkbox so that navigational and local-search queries consume no API quota — "with Ask AI off, voice queries run local text/graph search only — no API quota consumed." Locally-resolvable navigation (known group/thinker names) resolves "instantly, offline" before any API call is considered.
  Context: Voice & Navigation session §2 (voice input routing) and §3 (navigation command engine).
  Type: architectural
  Related decisions: DECISION-064
  Related items: ASSUMPTION-360 (local-first AI providers); Pathway 00 broker free-tier gating
  Testability: framework commitment (not testable) — a local-first / quota-conservation design rule; UX efficacy is separately observable
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-358
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "Voice respects the Ask AI checkbox … no API quota consumed." [stated]
    Current status: UNTESTED

ASSUMPTION-359:
  Date identified: 2026-06-24
  Statement: Storing third-party API keys (OpenAI, Groq) in `sessionStorage` rather than `localStorage` is the right privacy posture — keys are "cleared when the tab closes, never written to disk by the browser"; only TTS provider/voice preference goes in `localStorage`.
  Context: Voice & Navigation session §1 (key storage) and §6 (key security).
  Type: methodological
  Related decisions: DECISION-064
  Related items: PRESUMPTION-395 (sessionStorage "never on disk" / threat model)
  Testability: testable via literature — browser credential-storage security guidance (sessionStorage vs localStorage vs in-memory); persistence under crash-restore
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-359
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "API keys … stored in sessionStorage only … never written to disk." [stated]
    Current status: UNTESTED

ASSUMPTION-360:
  Date identified: 2026-06-24
  Statement: Offering local/offline (Ollama — "unlimited, fully local, fully offline") and own-key generous-free (Groq — "~14,400 req/day free") AI-query providers, with automatic fallback to local text search on `free-limit`/`rate-limited`, is preferable to a single shared-broker dependency for a publicly-shared demo artifact.
  Context: Voice & Navigation session §5 (free-limit handling) and §6 (Groq / Ollama providers).
  Type: architectural
  Related decisions: DECISION-064
  Related items: ASSUMPTION-358 (quota conservation); Device-freedom bright pin (public artifact, any visitor)
  Testability: framework commitment / weakly testable — a resilience/independence design value; provider availability and fallback correctness are observable
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-360
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from §5/§6 provider design and graceful-degradation rationale. [stated]
    Current status: UNTESTED

ASSUMPTION-361:
  Date identified: 2026-06-25
  Statement: The Heartbeat tool's "95 for days" staleness was caused by nothing running the pipeline — the snapshot file only regenerates when the pipeline runs, and the in-tab Refresh "only re-read that frozen file." The ~95 count is "coincidental — arXiv's feed returns ~25 recent items, five feeds sum to ~95 in the weekly window," so the number barely moves while the titles change.
  Context: Heartbeat tool repair session — staleness root-cause diagnosis.
  Type: empirical
  Related decisions: DECISION-065
  Related items: ASSUMPTION-365 (titles are the freshness signal); PRESUMPTION-398 (app-open liveness gap)
  Testability: testable empirically — confirmable by checking whether a forced poll changes titles while count holds (the session reported a fresh poll returned entirely different papers under the same ~95).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-361
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "the count is coincidental … the real cause of staleness was that the snapshot file only regenerates when the pipeline runs, and nothing was running it." [stated]
    Current status: UNTESTED

ASSUMPTION-362:
  Date identified: 2026-06-25
  Statement: Making `refresh_snapshot.sh` self-contained — it "now starts the runtime itself, polls, exports, summarizes via broker, enriches, archives, and shuts down — one command, nothing to babysit" — is the correct fix for "nothing was running it."
  Context: Heartbeat tool repair session — backend redesign.
  Type: architectural
  Related decisions: DECISION-065
  Related items: ASSUMPTION-361 (root cause); ASSUMPTION-363 (scheduling)
  Testability: framework commitment / weakly testable — a self-contained one-command pipeline is a maintainability design value; its reliability is observable across scheduled runs.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-362
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "refresh_snapshot.sh now starts the runtime itself … one command, nothing to babysit." [stated]
    Current status: UNTESTED

ASSUMPTION-363:
  Date identified: 2026-06-25
  Statement: A recurring Cowork scheduled task running every 6 hours (`c2a2-heartbeat-refresh`) is adequate cadence to keep the local Heartbeat fresh automatically — with the stated caveats that it "runs only while the Cowork app is open" and that it updates local files only ("the public github.io site still needs a manual push after review").
  Context: Heartbeat tool repair session — scheduling decision (AskUserQuestion → every-6-hours chosen).
  Type: methodological
  Related decisions: DECISION-065
  Related items: PRESUMPTION-398 (app-open liveness gap); OPEN-086 (pipeline liveness/watchdog); OPEN-092
  Testability: testable via literature — scheduled-job reliability / liveness monitoring; testable empirically — does the local snapshot stay fresh given the app-open dependency?
  Status: CONTESTED (MONITOR-382 continued via DISPOSITION-423, cycle 1, 2026-07-08 — cadence value supported; silent-stall clause strongly challenged, reaffirms REVISE-147)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-363
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "a Cowork task c2a2-heartbeat-refresh runs every 6 hours … it runs only while the Cowork app is open, and it updates local files." [stated]
    Current status: CONTESTED

ASSUMPTION-364:
  Date identified: 2026-06-25
  Statement: Archiving a History snapshot "only when content changes" (skipping identical polls) is the right rule — it makes History "gain one entry per real update" with date+time stamps and avoids "duplicate spam."
  Context: Heartbeat tool repair session — History/archive mechanics.
  Type: methodological
  Related decisions: DECISION-065
  Related items: ASSUMPTION-367 (honesty refinement on change signalling)
  Testability: testable empirically — verified in-session (archives on change, skips duplicates); robustness under near-identical content (whitespace/ordering) is checkable.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-364
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "snapshots are now timestamped and archived only when content changes … one entry per real update … no duplicate spam." [stated]
    Current status: UNTESTED

ASSUMPTION-365:
  Date identified: 2026-06-25
  Statement: The titles, not the count, are the freshness signal — "the titles are the freshness signal, and the new snapshot timestamp in the hero now makes the actual recency visible." The displayed ~95 is therefore not evidence of staleness.
  Context: Heartbeat tool repair session — what the UI should surface as "fresh."
  Type: epistemic
  Related decisions: DECISION-065
  Related items: ASSUMPTION-361 (count coincidental); ASSUMPTION-367
  Testability: framework commitment / weakly testable — a claim about which on-screen quantity carries the recency information; checkable against user interpretation.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-365
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "the titles are the freshness signal … the new snapshot timestamp in the hero now makes the actual recency visible." [stated]
    Current status: UNTESTED

ASSUMPTION-366:
  Date identified: 2026-06-25
  Statement: The residual symptom (the visible new "What is a lens?" text but the click "still does nothing," and the refresh showing no change) is "almost certainly a delivery/caching problem, not a logic one" — a stale cached `app.js` running inside `explorer.html`'s iframe — and a one-line cache-bust (versioning `app.js`/`styles.css`) will fix it, "they pass every headless test on disk."
  Context: Heartbeat tool repair session — end-of-session handoff diagnosis.
  Type: empirical
  Related decisions: DECISION-065
  Related items: PRESUMPTION-399 (headless/jsdom test parity)
  Testability: testable empirically — next session, apply the cache-bust and observe whether the lens link and live refresh appear (a direct, cheap falsification test).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-366
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "your index.html is fresh but your browser is still running an old cached app.js … almost certainly a delivery/caching problem, not a logic one." [stated]
    Current status: UNTESTED

ASSUMPTION-367:
  Date identified: 2026-06-25
  Statement: The Refresh control should "flash green for new papers, and show a calm 're-checked' when only the timestamp moved (a re-poll with the same papers)" — i.e., the change signal must distinguish genuinely new content from a no-op re-poll so the demo "reads correctly."
  Context: Heartbeat tool repair session — pre-trigger "honesty refinement" of the live-refresh UI.
  Type: methodological
  Related decisions: DECISION-065
  Related items: PRESUMPTION-400 (perceived vs actual liveness); Honesty layer (architecture/14_honesty_layer.md)
  Testability: testable via literature — honest vs misleading progress/change indicators (placebo/deceptive feedback UX); testable empirically — does the signal fire only on real change?
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-367
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "the button should flash green for new papers, and show a calm 're-checked' when only the timestamp moved." [stated]
    Current status: UNTESTED

ASSUMPTION-368:
  Date identified: 2026-06-25
  Statement: Unifying every tool's header to the brand gold `#C9A84C` (Inter, weight 700), keeping each tool's existing size ("size only when appropriate") and preserving muted suffixes/subtitles, is the right visual-identity posture across the explorer suite.
  Context: Explorer UI fixes session — header unification.
  Type: architectural
  Related decisions: DECISION-066
  Related items: ASSUMPTION-369 (Heartbeat hero exception); PRESUMPTION-401 (uniformity = improvement)
  Testability: framework commitment (brand/visual-identity value) — not literature-testable; consistency is verifiable, desirability is a design choice.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-368
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "Headers unified to the brand gold #C9A84C (Inter, weight 700, each tool's size kept — 'size only when appropriate')." [stated]
    Current status: UNTESTED

ASSUMPTION-369:
  Date identified: 2026-06-25
  Statement: The Heartbeat hero is a justified exception to header flattening — recolor it to brand gold but keep its Georgia-serif hero size (42–76px), because "flattening it to a 15px sans line would wreck that landing page"; the recolor is scoped to the hero so content headings keep their cream.
  Context: Explorer UI fixes session — the one stated "judgment call."
  Type: architectural
  Related decisions: DECISION-066
  Related items: ASSUMPTION-368 (header unification rule)
  Testability: framework commitment (design judgment) — not literature-testable.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-369
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "its title is a 42–76px Georgia-serif hero, not a titlebar … flattening it to a 15px sans line would wreck that landing page." [stated]
    Current status: UNTESTED

ASSUMPTION-370:
  Date identified: 2026-06-25
  Statement: A commit must be scoped to only the session's own files — "I commit only this session's files (the tree has unrelated agent WIP I must not sweep in)" — staging exactly the 12 changed files and leaving the 39 agent-WIP files out; the no-blind-push rule gates the push on Tom's explicit review/sign-off.
  Context: Explorer UI fixes session — commit/push of `1fba4b7`.
  Type: methodological
  Related decisions: DECISION-066
  Related items: PRESUMPTION-402 (manual partition of a dirty tree); Constitutional no-blind-push rule
  Testability: testable via literature — error rates of manual partial-staging in dirty working trees; safeguards (branch/worktree isolation).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-370
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "I commit only this session's files … the 39 agent-WIP files correctly left out." [stated]
    Current status: UNTESTED

ASSUMPTION-371:
  Date identified: 2026-06-25
  Statement: launchd supervision makes the OpenStory backend durable and reboot-safe — "you're back to the durable, launchd-supervised state … the supervised com.tomloughran.openstory.backend is serving again" — the right durability posture for the capture pipeline that feeds the wiki.
  Context: Open Story system diagnosis session — backend rebuild and supervision.
  Type: architectural
  Related decisions: DECISION-067
  Related items: PRESUMPTION-404 (single-Mac durability transfer); PRESUMPTION-405 (post-SIGKILL DB consistency)
  Testability: testable via literature — process-supervision / reboot-safety patterns (launchd/systemd) for long-running local services.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-371
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "you're back to the durable, launchd-supervised state … the supervised … backend is serving again." [stated]
    Current status: UNTESTED

ASSUMPTION-372:
  Date identified: 2026-06-25
  Statement: Backfilling the full event history with no window filter correctly recovers the pre-72h Cowork history that was missing — "Backfilled 218879 events from all files (no window filter)," with the DB confirming sessions 1,099 → 1,332, events 224k → 256,040, and the deep-history slice 463 → 666.
  Context: Open Story system diagnosis session — history seed.
  Type: empirical
  Related decisions: DECISION-067
  Related items: PRESUMPTION-405 (the seed ended in SIGKILL — was the DB left consistent?)
  Testability: testable empirically — verified by DB counts in-session; integrity after the abnormal (`Killed: 9`) termination is separately checkable.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-372
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "Backfilled 218879 events from all files (no window filter) … sessions 1,099 → 1,332, events 224k → 256,040." [stated]
    Current status: UNTESTED

ASSUMPTION-373:
  Date identified: 2026-06-26
  Statement: The full-file `quick_check` guard in the OpenStory extractors was the root cause that aborted every extraction run since 2026-06-08 — "It drops the old full-file `quick_check` guard (the exact scan that aborted every run since June 8)." The Agent Map / Sociogram agent-layer feed had been silently stalled for 18 days.
  Context: "Agent map explorer runs issue" session — OpenStory telemetry refresh debugging.
  Type: empirical
  Related decisions: DECISION-068
  Related items: PRESUMPTION-405 (post-SIGKILL DB consistency); OPEN-086 (pipeline silent-miss / liveness keystone); OPEN-093 (OpenStory freshness watchdog)
  Testability: testable empirically — in-session local diagnosis (verified by the failure signature and the fix removing it); the general failure mode is the WAL-contention class captured in ASSUMPTION-374/375.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-373
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "the exact scan that aborted every run since June 8" close-out. [stated]
    Current status: UNTESTED

ASSUMPTION-374:
  Date identified: 2026-06-26
  Statement: Copying the live ~2 GB WAL SQLite DB to local disk, validating the *local* copy, and reading that — rather than validating/reading the live file over the FUSE mount — is the correct fix, because it decouples the long extraction from the live WAL writer. "a shared reader that copies the DB to local disk, validates the *local* copy, and reads that — decoupling the long extraction from the live WAL writer over the mount."
  Context: "Agent map explorer runs issue" session — `openstory_db.py` design (Fix #1).
  Type: architectural
  Related decisions: DECISION-068
  Related items: ASSUMPTION-373; ASSUMPTION-375; PRESUMPTION-407 (quiet-window reliability)
  Testability: testable via literature — SQLite WAL semantics, consistent-snapshot reads, reading a hot DB over a network/FUSE mount from a second process, copy-then-validate idempotency.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-374
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Fix #1 description of the shared reader. [stated]
    Current status: UNTESTED

ASSUMPTION-375:
  Date identified: 2026-06-26
  Statement: The peak-hour torn-copy failures are an environment constraint (WAL write+checkpoint contention at peak churn), not a code defect — evidenced by clean reads under light load (3/3) vs correct fail-loud refusal under the heavy write burst (4–5/5), with the production task firing at 06:15 "when OpenStory is quiet." "This is an environment constraint at peak hour, not a code defect."
  Context: "Agent map explorer runs issue" session — verification honesty close-out.
  Type: empirical
  Related decisions: DECISION-068
  Related items: PRESUMPTION-407 (is 06:15 reliably quiet?); OPEN-095
  Testability: testable via literature — workload periodicity, scheduling against contention windows, torn reads under concurrent WAL checkpointing; partly local empirical (the 06:15 run will produce the first clean end-to-end evidence).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-375
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from "an environment constraint at peak hour, not a code defect" + the light-load/heavy-load pass counts. [stated]
    Current status: UNTESTED

ASSUMPTION-376:
  Date identified: 2026-06-26
  Statement: Writing a dated `REFRESH_STATUS.md` (PASS/FAIL) every run, plus a new section 7 in `morning-system-health` that reads it and headlines a FAIL, makes a silent multi-day stall visible going forward — "so a silent 18-day stall can't recur."
  Context: "Agent map explorer runs issue" session — Fix #3 (make failure visible).
  Type: methodological
  Related decisions: DECISION-068
  Related items: OPEN-086 (liveness keystone); ASSUMPTION-367 (honesty refinement); PREMISE-084 (signal change only on real change)
  Testability: testable via literature — observability, dead-man's-switch / heartbeat monitoring, "absence is the signal" / fail-loud design, alert surfacing vs silent failure.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-376
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Fix #3 description ("so a silent 18-day stall can't recur"). [stated]
    Current status: UNTESTED

ASSUMPTION-377:
  Date identified: 2026-06-26
  Statement: Styling the new "Tech — Under the Hood" entry as an appendix card (placed after the conclusion) rather than as a 16th angle preserves the page's "Fifteen Angles" framing. "I styled the card as an appendix rather than a 16th angle so the page's 'Fifteen Angles' framing stays intact."
  Context: "RC Karpathy Wiki architecture diagram" session — `what_is_c2a2.html` Tech card placement.
  Type: architectural
  Related decisions: DECISION-069
  Related items: ASSUMPTION-368 (brand-gold header unification); ASSUMPTION-369 (Heartbeat-hero exception)
  Testability: framework commitment (not testable) — an information-architecture/editorial framing choice, deferred to Tom (offered as a one-line change to angle 16 if preferred).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-377
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the appendix-vs-16th-angle rationale. [stated]
    Current status: UNTESTED

ASSUMPTION-378:
  Date identified: 2026-06-26
  Statement: The Tech card's relative link `architecture/lowlevel_architecture.html` resolves on the live site only if `wiki/architecture/` is published — and the in-session `git status`/`git ls-files` checks confirmed `wiki/architecture/` is NOT gitignored and `what_is_c2a2.html` IS tracked, "so both will ship cleanly."
  Context: "RC Karpathy Wiki architecture diagram" session — publishability verification.
  Type: empirical
  Related decisions: DECISION-069
  Related items: (memory flag: what_is_c2a2.html previously "believed-published but possibly untracked")
  Testability: testable empirically — in-session local fact verified by git (a local diagnostic, not a literature claim).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-378
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the git ls-files / gitignore verification. [stated]
    Current status: UNTESTED

ASSUMPTION-379:
  Date identified: 2026-06-26
  Statement: The stray `c2a2_*.svg` files at the repo root duplicate what is already inside `lowlevel_architecture.html` (auto-saved widget renders), so the careful push will want per-group triage, not a blanket `git add -A`.
  Context: "RC Karpathy Wiki architecture diagram" session — pre-push working-tree triage.
  Type: methodological
  Related decisions: DECISION-069
  Related items: ASSUMPTION-370 (scoped commits); PRESUMPTION-402 (hand-partitioned dirty tree); REVISE-148 (staging isolation); PRESUMPTION-412
  Testability: testable empirically — local diagnostic about file duplication; the general staging-discipline question is covered by REVISE-148 / PRESUMPTION-402.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-379
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the "per-group triage, not a blanket git add -A" close-out. [stated]
    Current status: UNTESTED

ASSUMPTION-380:
  Date identified: 2026-06-26
  Statement: A deterministic, rule-based harvest (read each approved card's existing Cross-Tradition Signals section, map targets to the 15-tradition roster, split multi-tradition lines, parse strength) correctly recovers the cross-tradition signal dataset with no model passes — evidenced by a hard coverage gate passing 158/158 and 525 signals harvested from 140 cards (dataset 218 → 743). "the deterministic harvest turned out cheap enough to just run the whole backlog in-session, in budget, no model passes."
  Context: "Interactions tab data visualization" session — `harvest_signals.py`.
  Type: methodological
  Related decisions: DECISION-070
  Related items: PRESUMPTION-409 (coverage ≠ semantic fidelity); PRESUMPTION-411 (15-tradition roster as canonical target space); Rule 5 (code answers when code can)
  Testability: testable via literature — rule-based vs ML information extraction, when deterministic parsing suffices, precision/recall of pattern extraction over semi-structured text.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-380
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the deterministic-harvest description + 158/158 coverage gate. [stated]
    Current status: UNTESTED

ASSUMPTION-381:
  Date identified: 2026-06-26
  Statement: Dating each signal by proposal date (formation) while carrying source_date (overlay vintage) is the correct dual encoding — it "fills the May plateau, honestly, with links the agents actually authored in May," with a cumulative formation curve on proposal date plus a source-vintage bar panel spanning 2024–2026 ("old ideas, freshly engaged").
  Context: "Interactions tab data visualization" session — timeline dual encoding.
  Type: epistemic
  Related decisions: DECISION-070
  Related items: PRESUMPTION-410 (proposal-date = formation-date modeling)
  Testability: testable via literature — bitemporal / valid-time vs transaction-time data modeling, event dating and provenance, representing formation vs vintage of an idea.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-381
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the formation-date/source-date dual-encoding rationale. [stated]
    Current status: UNTESTED

ASSUMPTION-382:
  Date identified: 2026-06-26
  Statement: Embedding `level2_signal_stream.html` as a lazy iframe with a JS-set `?v=Date.now()` cache-bust satisfies the constitutional iframe-asset rule (no manual version bump) and mirrors explorer.html's own pattern.
  Context: "Interactions tab data visualization" session — Level Two embed integration.
  Type: architectural
  Related decisions: DECISION-070
  Related items: ASSUMPTION-366 (cache-delivery-not-logic); PRESUMPTION-408 (jsdom render-fidelity)
  Testability: testable via literature — HTTP cache invalidation, query-string cache-busting effectiveness and pitfalls, lazy iframe loading.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-382
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the iframe + ?v=Date.now() integration description. [stated]
    Current status: UNTESTED

ASSUMPTION-383:
  Date identified: 2026-06-28
  Statement: "The vault is wikilink-sparse but reference-dense, and its thinker content is already well connected." The orphan population "is not a synthesis problem"; "the knowledge graph is sufficient to support meaningful thinker-agent synthesis today; the bottleneck is not connectivity." Only 9 thinker-tradition pages are under-connected.
  Context: Autonomous one-time "C2A2 sewing-agent wiki bootstrap audit" run (Tom not present) — headline finding; the premise that justifies declining Phase 3.
  Type: empirical
  Related decisions: DECISION-071
  Related items: ASSUMPTION-384 (orphan-count-as-artifact); PRESUMPTION-414 (connectivity-as-health-proxy); the live weekly sewing agent's 2026-06-23 census (2,160/608/44/2,812)
  Testability: testable via literature — knowledge-graph health metrics, link density vs. functional connectedness, when low wikilink density does/doesn't indicate a synthesis deficit.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-383
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the sewing-bootstrap report's headline finding and vault-health assessment. [stated] (source = autonomous agent run, not an interactive human session)
    Current status: UNTESTED

ASSUMPTION-384:
  Date identified: 2026-06-28
  Statement: The alarming orphan count (2,337 of 3,031 pages) "is an artifact of (a) excluding shared-reference edges and (b) inbox/structural pages that should not carry backlinks — not a deficit in the substantive knowledge graph." 2,474 orphans are structural pages orphaned by design; 456 are inbox residue.
  Context: Sewing-bootstrap audit — orphan classification (Phase 2) and vault-health assessment.
  Type: methodological
  Related decisions: DECISION-071
  Related items: ASSUMPTION-383; OPEN-100 (is wikilink-backlink the right health metric?); PRESUMPTION-415 (path-heuristic classification validity)
  Testability: testable via literature — choice of edge type in graph health metrics, co-citation/shared-reference vs explicit-link connectivity, measurement artifacts in network analysis.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-384
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the orphan-classification table and the "artifact, not deficit" framing. [stated]
    Current status: UNTESTED

ASSUMPTION-385:
  Date identified: 2026-06-28
  Statement: Injecting agentic-call boilerplate into all A/B/C pages (Phase 3 as written) "would have stamped boilerplate into ~480 files — 456 of them inbox process-artifacts" and "would inject noise, not synthesis hooks," evidenced by the task's own "most relevant to multiple thinkers" heuristic ranking process logs (PROCESSED_LOG.md, repair manifests) at the top precisely because they name every thinker. It therefore conflicts with the token budget (Rule 6), surgical-change (Rule 3), and is largely redundant with the live weekly sewing agent — so Phase 3 should not be executed.
  Context: Sewing-bootstrap audit — Phase 3 disposition (NOT executed); the design rationale for the decision.
  Type: methodological
  Related decisions: DECISION-071
  Related items: PRESUMPTION-416 (autonomy-overrides-instruction); PRESUMPTION-417; Rule 3, Rule 5, Rule 6, Rule 12
  Testability: testable via literature — signal-to-noise of automated/templated link injection, template/boilerplate pollution in wikis, when bulk automated edits degrade vs improve a knowledge base.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-385
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the four-reason Phase-3-not-executed rationale. [stated]
    Current status: UNTESTED

ASSUMPTION-386:
  Date identified: 2026-06-28
  Statement: The bounded alternative — "wire the ~9 tradition hub pages into their neighbors (add inbound links ...)" and "triage the 456 inbox pages through the inbox pipeline in dated batches" — is the high-signal, reviewable path; and "the biggest lever on the orphan count isn't link-seeding, it's a one-time triage of the 456 un-promoted inbox pages."
  Context: Sewing-bootstrap audit — bounded-alternative recommendation and "recommended actions for Tom."
  Type: methodological
  Related decisions: DECISION-071
  Related items: ASSUMPTION-385; OPEN-099 (inbox-residue policy)
  Testability: testable via literature — triage/backlog-batching vs broad-injection interventions for graph connectivity, hub-and-spoke wiring effects on navigability, WIP-bounded remediation.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-386
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the bounded-alternative and recommended-actions sections. [stated]
    Current status: UNTESTED

ASSUMPTION-387:
  Date identified: 2026-06-28
  Statement: Deterministic path/size heuristics (not the model — explicit Rule 5 application) correctly classify all 2,984 orphan+sparse pages into categories A (thinker content) / B (inbox residue) / C (synthesis potential) / D (structural) / E (stub <200B), with directory location and file size as the discriminators.
  Context: Sewing-bootstrap audit — Phase 2 orphan classification ("model not used — Rule 5").
  Type: methodological
  Related decisions: DECISION-071
  Related items: ASSUMPTION-384; PRESUMPTION-415 (directory location reliably indicates content type)
  Testability: testable via literature — accuracy of path/metadata-based document classification vs content-based classification, when structural heuristics suffice for triage.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-387
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Rule-5 deterministic-classification description. [stated]
    Current status: UNTESTED

ASSUMPTION-388:
  Date identified: 2026-06-29
  Statement: Cross-tradition signals/day is a meaningful "yield" metric worth surfacing as its own amplitude axis in the metabolism waveform view, on par with the existing PRS-triplet yield series — i.e., the daily rate at which cross-tradition signals are generated is a real signal of system productivity/health (743 signals over 47 days, Apr 3–Jun 23, peak 68 on May 5).
  Context: "Resume explorer cleanup" session, Item 2 — adding cross-tradition signals/day as a metabolism yield series (build_metabolism_view.py, +54/−9), following the convention the PRS series already established.
  Type: epistemic
  Related decisions: (operational — Item 2 ship, approved-pending-push)
  Related items: PRESUMPTION-419 (signal-volume-as-yield proxy); the standing "cross-tradition connections are good" normative presumption
  Testability: testable via literature — validity of activity/event-rate metrics as proxies for knowledge-production or research productivity; when count-rate dashboards track real value vs volume.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-388
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Item-2 rationale for adding signals/day as a yield axis alongside PRS. [stated]
    Current status: UNTESTED

ASSUMPTION-389:
  Date identified: 2026-06-29
  Statement: PRS-triplet extraction (and cross-program signal extraction) is quality-sensitive and is therefore gated to attended (human-present) sessions by standing policy — the unattended daily orchestrator deliberately does NOT auto-extract PRS triplets from the approved backlog ("raw backlog deferred per standing policy; no triplets added"), because raw PRS/cross-program extraction is the quality-sensitive step Tom reserved for attended runs.
  Context: "Resume explorer cleanup" session, gap-#1 ingestion-stall diagnostic — root-cause finding traced through the orchestrator phase spec and PROCESSED_LOG.md.
  Type: methodological
  Related decisions: DECISION-068 (OpenStory proof, blocked); OPEN-101 (attended-gating policy review)
  Related items: PRESUMPTION-420 (the attended-gating quality benefit is untested while the staleness cost is real); the ingest_backlog HIGH flag
  Testability: testable via literature — human-in-the-loop vs automated extraction quality for structured-claim/triple extraction; when human gating materially improves output quality; cost of human-gated throughput bottlenecks.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-389
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated "deferred per standing policy / gated to attended sessions" rationale surfaced in the ingestion-stall diagnostic. [stated]
    Current status: UNTESTED

ASSUMPTION-390:
  Date identified: 2026-06-29
  Statement: The liveness of the OpenStory activity feed does not imply the liveness of the PRS/signals approval axes — the metabolism view's feeds are independent, so "OpenStory running through today tells you nothing about whether approvals show up." Approvals reach the view only through the PRS-yield and signals axes, which are fed by separate pipelines that were stale by 6–12 days (PRS frozen 2026-06-17; signals frozen 2026-06-23) even while OpenStory activity lanes were current through 2026-06-29.
  Context: "Resume explorer cleanup" session, answering Tom's question "approvals from June 26 are not present in the metabolism views, though OpenStory data runs through today. Is the appropriate agent running?"
  Type: methodological
  Related decisions: OPEN-103 (per-axis freshness/as-of indicator)
  Related items: ASSUMPTION-392; PRESUMPTION-421 (silent-staleness — "someone will notice" as the liveness mechanism); PRESUMPTION-422 (stale-axis-beside-fresh-axis); OPEN-086 (pipeline-liveness watchdog)
  Testability: testable via literature — observability/freshness monitoring in multi-source dashboards; per-source staleness/SLA indicators; why composite views mislead when sources update on different cadences.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-390
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated diagnostic that feed independence means OpenStory liveness does not certify approval-axis liveness. [stated]
    Current status: UNTESTED

ASSUMPTION-391:
  Date identified: 2026-06-29
  Statement: `git pull --rebase --autostash` correctly and safely handles the ~20 unrelated working-tree files by auto-stashing them around the rebase, removing the manual stash → pull --rebase → push → stash-pop dance used in the prior two pushes. Adopted as the standard push pattern and folded into push-pattern memory.
  Context: "Resume explorer cleanup" session, Item 2 push instructions and the push-pattern memory update.
  Type: methodological
  Related decisions: DECISION-072 (adopt --rebase --autostash as standard push pattern)
  Related items: PRESUMPTION-424 (autostashing a chronically dirty tree every push is safe); PRESUMPTION-412 / REVISE-148 (cross-session push debt)
  Testability: testable via literature/tooling docs — git rebase autostash semantics and failure modes; safety of stashing uncommitted changes across rebase; conflict/rollback behavior.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-391
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated switch to --rebase --autostash and its rationale (auto-stashes the other ~20 files, no manual dance). [stated]
    Current status: UNTESTED

ASSUMPTION-392:
  Date identified: 2026-06-29
  Statement: Item 1 (Community Interactions layout) and Item 6 (Community Explorer search layout) share the same layout-bug family, so "the same surgical CSS-family fix just shipped for Item 1" resolves Item 6 — making Item 6 a low-risk quick win doable in-sandbox.
  Context: "Resume explorer cleanup" session / 2026-06-29 cowork summary — framing Item 6 as the natural next quick win.
  Type: empirical
  Related decisions: (operational — backlog prioritization)
  Related items: ASSUMPTION-390; PRESUMPTION-423 (add-an-agent / treat components as same-class)
  Testability: testable empirically — whether the Item-1 width/CSS fix in fact resolves Item 6 when applied (verifiable on next pass); not literature-testable.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-392
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated "same surgical CSS-family fix" framing of Item 6. [stated]
    Current status: UNTESTED

ASSUMPTION-393:
  Date identified: 2026-06-30
  Statement: The PRS-triplet backlog should be cleared now via a single attended ("Track A") ingestion pass with Tom present — acting on OPEN-101 in favor of attended-gating rather than authorizing a bounded unattended ingest agent. The pass ingested 144 QC-vetted triplets across 12 traditions, breaking the freeze that had held the PRS axis at 2026-06-17.
  Context: "PRS backlog runbook" session (2026-06-30, attended). Tom ran the Mac-side commit/push; the session drove the ingestion, QC, connectome regen, and review.
  Type: methodological
  Related decisions: DECISION-073 (attended Track-A backlog clear); OPEN-101 (attended-vs-unattended ingest — partially addressed)
  Related items: ASSUMPTION-389 (extraction gated to attended sessions); PRESUMPTION-420/425; OPEN-102 (no scheduled regen agent — cadence gap remains)
  Testability: testable via literature — human-gated batch remediation vs continuous automated ingest for quality-sensitive structured-claim extraction; also partly empirical (does the backlog re-accumulate before the next attended pass?).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-393
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated decision to clear the backlog now via an attended Track-A pass rather than an unattended agent. [stated]
    Current status: UNTESTED

ASSUMPTION-394:
  Date identified: 2026-06-30
  Statement: The narrative connectome (`prs_3d.html`) is the primary PRS visualization and independently confirms the ingestion — a clean 288→432 regen (exactly +144) with `node --check`, count-match, and content-population checks all green is sufficient verification that the triplets are correct, so the token-axis metabolism view can be deferred without loss of verification.
  Context: "PRS backlog runbook" session — framing the connectome regen as "the real headline" that "independently confirms the ingestion."
  Type: methodological
  Related decisions: DECISION-073
  Related items: ASSUMPTION-399 (metabolism view is the only DB-blocked piece); PRESUMPTION-426 (count-consistency read as content-correctness); PRESUMPTION-429 (connectome and token-view treated as redundant for verification)
  Testability: framework commitment (verification-sufficiency claim) — partly testable via literature on redundant-check value.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-394
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated claim that the connectome regen independently confirms the +144 ingestion. [stated]
    Current status: UNTESTED

ASSUMPTION-395:
  Date identified: 2026-06-30
  Statement: `prs_yield.py` reconstructs the yield time-series from git history, so it fails loud (Rule 12) on triplets that are on disk but not yet committed — therefore the commit must PRECEDE the metrics regen, not follow it. The prior runbook's commit-after ordering was wrong and was corrected to commit → yield → connectome.
  Context: "PRS backlog runbook" session, opening ordering discovery and runbook correction.
  Type: methodological
  Related decisions: DECISION-072 (autostash push pattern); DECISION-073
  Related items: PRESUMPTION-431 (recurring stale git lock treated as benign)
  Testability: testable empirically / via tooling docs — the script's git-history dependency is directly verifiable.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-395
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated ordering discovery (prs_yield reads git history; commit must precede regen). [stated]
    Current status: UNTESTED

ASSUMPTION-396:
  Date identified: 2026-06-30
  Statement: Ingestion identity must be keyed on `proposal_id`, not inbox filename — the manifest's un-ingested gate was testing inbox filenames against a proposal-id-keyed log, which both re-staged ~15 already-ingested cards and hid real pending ones; the corrected candidate set was 70 units / 152 candidates (not the runbook's 127). Fixed at source in `build_prs_manifest.py`; a code-driven dedup pass (`qc_prs.py`) is the right gate.
  Context: "PRS backlog runbook" session — the two-way manifest-gate bug found and fixed.
  Type: architectural
  Related decisions: DECISION-073
  Related items: ASSUMPTION-397 (the 8 QC drops); PRESUMPTION-427 (one identity-bug found treated as the class eliminated); PRESUMPTION-428 (audit-vs-vault divergence)
  Testability: testable empirically — the filename-vs-proposal_id keying error and its ~15-card effect are directly verifiable.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-396
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated manifest-gate bug (filename vs proposal_id) and its correction. [stated]
    Current status: UNTESTED

ASSUMPTION-397:
  Date identified: 2026-06-30
  Statement: Eight of 152 candidates are correctly excluded from ingestion: hawkins `SUPP-001` is a full re-derivation of existing PRS-10–15 (all 6 dropped), the hawkins citation-upgrade card is vacuous, and stump `PRS-25` duplicates `PRS-09`. Net 8 drops, all confirmed against source.
  Context: "PRS backlog runbook" session — the `qc_prs.py` code-driven dedup dispositions.
  Type: empirical
  Related decisions: DECISION-073
  Related items: ASSUMPTION-396
  Testability: testable empirically — each drop is verifiable against the source cards (already git-confirmed this session).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-397
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated 8-of-152 QC drops and their source-confirmed rationale. [stated]
    Current status: UNTESTED

ASSUMPTION-398:
  Date identified: 2026-06-30
  Statement: The No-Blind-Push rule requires a live visual eyeball of `prs_3d.html` (Chrome review of the served page: ToC loads, a spot-checked tradition shows its new triplets, the 432 count renders) before publish, even after all programmatic validations pass — programmatic green is necessary but not sufficient to go live.
  Context: "PRS backlog runbook" session — the No-Blind-Push review gate enforced before the push block was handed over.
  Type: methodological
  Related decisions: DECISION-073
  Related items: ASSUMPTION-394; PRESUMPTION-426
  Testability: framework commitment (standing policy) — partly testable via literature on the marginal value of human visual review after automated validation.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-398
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated enforcement of a visual pre-push review over-and-above programmatic validation. [stated]
    Current status: UNTESTED

ASSUMPTION-399:
  Date identified: 2026-06-30
  Statement: The OpenStory DB corruption ("Rowid out of order", 4.35 GB, live 5 MB WAL updated 20:27) is unrelated to and does not block the PRS work — the triplets, `prs_yield`, and the connectome all read the vault/git, not OpenStory; only the token-axis metabolism view depends on the DB.
  Context: "PRS backlog runbook" session — diagnosing the `build_metabolism_view.py` quick_check abort.
  Type: architectural
  Related decisions: DECISION-068 (OpenStory fix, BLOCKED); OPEN-095 (end-to-end proof)
  Related items: ASSUMPTION-400; ASSUMPTION-394
  Testability: testable empirically — the dependency claim (PRS reads vault/git, view reads DB) is directly verifiable and was confirmed this session.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-399
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated finding that the corrupt DB blocks only the metabolism view, not the PRS pipeline. [stated]
    Current status: UNTESTED

ASSUMPTION-400:
  Date identified: 2026-06-30
  Statement: Recovering a 4.35 GB SQLite file while a writer is still attached (live WAL) risks compounding the corruption, so a blind `.recover` must not be run — the safe sequence requires stopping the OpenStory writer first, then checkpoint/back up → `.recover` into a fresh file (needs ~5 GB free) → swap in.
  Context: "PRS backlog runbook" session — refusing to hand over a blind recovery block for the corrupt OpenStory DB.
  Type: methodological
  Related decisions: DECISION-068 (BLOCKED); OPEN-095
  Related items: ASSUMPTION-399
  Testability: testable via literature/tooling docs — SQLite `.recover` semantics and the risk of recovering a file with a live writer attached.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-400
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated safe-recovery sequence and the refusal to run a blind live `.recover`. [stated]
    Current status: UNTESTED

ASSUMPTION-401:
  Date identified: 2026-06-30
  Statement: Cross-tradition routing into `master/cross_program_index.md` is a separate attended step and can be deferred out of the first (Track A) commit without harming the triplet ingestion — `wiki/master` is intentionally left out of the first commit.
  Context: "PRS backlog runbook" session — scoping Track A to traditions + PROCESSED_LOG + connectome, deferring master routing.
  Type: methodological
  Related decisions: DECISION-073
  Related items: OPEN-084 (construct-count / index reconciliation); ASSUMPTION-393
  Testability: framework/operational commitment — partly empirical (does deferring master routing leave the connectome/index inconsistent in the interim?).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-401
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated scoping of Track A and deferral of cross_program_index routing to a separate attended pass. [stated]
    Current status: UNTESTED

ASSUMPTION-402:
  Date identified: 2026-07-01
  Statement: A logged-out claude.ai is a hard stop for an autonomous run, not a condition to work around — entering credentials / signing in on Tom's behalf is out of scope for an unattended agent. Stated by both sync agents today: "I did not attempt to sign in — entering credentials is out of scope for an autonomous run and is something only you should do" (morning) and "Autonomous runs can't sign in" (evening).
  Context: Both the morning Chat→Cowork and evening Cowork→Chat sync agents hit a logged-out claude.ai in the connected Chrome and each independently declined to authenticate, degrading to file-only output rather than proceeding.
  Type: methodological / normative
  Related decisions: (none — operating-boundary commitment, not a minted decision)
  Related items: PRESUMPTION-434 (logged-out state treated as transient); OPEN-086
  Testability: framework/normative commitment. The general principle — autonomous agents should not perform authentication or other credentialed/irreversible actions unattended — is testable via literature on human-in-the-loop autonomy boundaries and agent authority limits.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-402
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from both sync agents' explicit refusal-to-authenticate statements in the 2026-07-01 morning-scrape and evening-sync transcripts. [stated]
    Current status: UNTESTED

ASSUMPTION-403:
  Date identified: 2026-07-02
  Statement: In the Inter-Tradition Dialogue Study, understanding is validly established only when the original claimant is the sole judge of whether their claim was captured — "understanding is established the only way it legitimately can be — the person who made the claim is the sole judge of whether it has been captured — never the convener, never a third-party translator." Stated as the paper's core validity standard: "Ratified by its author, not mapped between sentences."
  Context: "The convener" session (2026-07-02) — rewriting the study's thesis away from "inhabitation-checked-by-the-inhabited" toward the author-ratification standard.
  Type: epistemic / methodological
  Related decisions: DECISION-074
  Related items: PRESUMPTION-438 (the author-ratification standard under AI-agent simulation)
  Testability: framework commitment (foundational to the study's design) — but the general claim, that mutual understanding in dialogue is better validated by author-ratification than by third-party semantic mapping, is testable via literature on dialogue, verification, and theories of understanding.
  Status: CONTESTED (15a: PARTIALLY-SUPPORTED (Moderate) | 15b: PARTIALLY-CHALLENGED (Moderate) | 15c: MONITOR -> MONITOR-412; DISPOSITION-391, 2026-07-03)
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-403
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the explicitly stated rephrasing of the study's validity standard in the convener session. [stated]
      15a/15b: Searched for supporting and challenging literature 2026-07-03 (results in lit_search_results/).
      15c: Dispositioned 2026-07-03 -> MONITOR-412 (DISPOSITION-391).
    Current status: CONTESTED (MONITOR-412 (DISPOSITION-391))

ASSUMPTION-404:
  Date identified: 2026-07-02
  Statement: A "listening" dialogue condition produces measurably higher understanding than a "deaf" condition (hypothesis P1). Reported result this run: listen−deaf = +0.086, 95% CI [+0.072, +0.100], groups fully separated, exact rank p ≈ 0.004 ("Robust").
  Context: "The convener" session — the §5.5 error analysis computed directly from the run transcripts.
  Type: empirical
  Related decisions: DECISION-074
  Related items: ASSUMPTION-406 (conversation-clustered inference); PRESUMPTION-437 (understanding as a single measurable quantity)
  Testability: testable empirically — was tested in this run (k=5); a strengthened, higher-powered panel would tighten the estimate.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-404
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated P1 hypothesis and its reported effect size/interval. [stated]
    Current status: UNTESTED

ASSUMPTION-405:
  Date identified: 2026-07-02
  Statement: The C0 gate validly discriminates a faithful restatement from a strawman on verdict discrimination — faithful 0.93 (Wilson [0.836, 0.973]) vs strawman 0.00 (Wilson [0, 0.149]), non-overlapping. The stated caveat (folded in this session): the gate's *fidelity* limb (lexical overlap, +0.043, 95% CI [−0.016, +0.102]) includes zero, so the gate "passes on the verdict discrimination alone; word-overlap is doing no real work."
  Context: "The convener" session — the C0 gate design and its honest-correction #2.
  Type: methodological / empirical
  Related decisions: DECISION-074
  Related items: ASSUMPTION-403 (author-ratification standard the gate operationalizes)
  Testability: testable empirically — the discrimination and the fidelity-limb weakness are both measured; scope is k=5.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-405
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated C0-gate result and the stated fidelity-limb caveat. [stated]
    Current status: UNTESTED

ASSUMPTION-406:
  Date identified: 2026-07-02
  Statement: The honest unit of replication for the study is the conversation, not the individual event — so conversation-clustered confidence intervals (k=5) are the correct inferential unit; "with k=5 the intervals are wide by design." Stated as a methodological note built into §5.5.
  Context: "The convener" session — defending the error analysis' inferential choices.
  Type: methodological
  Related decisions: DECISION-074
  Related items: ASSUMPTION-404, ASSUMPTION-410; PRESUMPTION-439 (k=5 adequacy for a "robust/directional/null" sort)
  Testability: testable via literature — clustered/hierarchical inference with a small number of clusters; unit-of-analysis choice in nested dialogue data.
  Status: GROUNDED (15a: SUPPORTED (Strong, for the unit) | 15b: PARTIALLY-CHALLENGED (Moderate-Strong, k=5 CI) | 15c: INCORPORATE -> PREMISE-094; DISPOSITION-392, 2026-07-03)
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-406
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated unit-of-replication commitment and clustered-interval reporting. [stated]
      15a/15b: Searched for supporting and challenging literature 2026-07-03 (results in lit_search_results/).
      15c: Dispositioned 2026-07-03 -> PREMISE-094 (DISPOSITION-392).
    Current status: GROUNDED (PREMISE-094 (DISPOSITION-392))

ASSUMPTION-407:
  Date identified: 2026-07-02
  Statement: Preregistration-before-run should be enforced as a machine gate — "preregister-before-run becomes a machine gate (that's Stage 2)" of the Appendix G runner. The invariant is carried in "from the first commit."
  Context: "InterT study" session (2026-07-02) — staging Appendix G and naming the preregister-before-run invariant as a Stage 2 machine gate.
  Type: methodological / normative
  Related decisions: DECISION-075
  Related items: ASSUMPTION-409 (spec + one-file runner)
  Testability: testable via literature — efficacy of preregistration in reducing analytic flexibility / researcher degrees of freedom; enforceability of automated preregistration gates.
  Status: CONTESTED (15a: PARTIALLY-SUPPORTED (Moderate-Strong) | 15b: PARTIALLY-CHALLENGED (Moderate) | 15c: MONITOR -> MONITOR-413; DISPOSITION-393, 2026-07-03)
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-407
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated Stage 2 invariant (preregister-before-run as a machine gate). [stated]
      15a/15b: Searched for supporting and challenging literature 2026-07-03 (results in lit_search_results/).
      15c: Dispositioned 2026-07-03 -> MONITOR-413 (DISPOSITION-393).
    Current status: CONTESTED (MONITOR-413 (DISPOSITION-393))

ASSUMPTION-408:
  Date identified: 2026-07-02
  Statement: The study bears on — and its results are read as evidence against — pessimism about the fulfillment of Alasdair MacIntyre's recovery project (that rival traditions can, in principle, reach genuine mutual understanding). The corrected help-popup wording frames the tool "against pessimism in regard to the fulfillment of Alasdair MacIntyre's recovery project."
  Context: "The convener" / "InterT study" sessions — the study's stated framing and the verified popup wording on the live Inter-Tradition Study tab.
  Type: epistemic / empirical
  Related decisions: DECISION-074, DECISION-075
  Related items: PRESUMPTION-440 (optimism-toward-fulfillment as the sought outcome)
  Testability: testable via literature (MacIntyre scholarship on tradition-constituted rationality and commensurability) and empirically (whether the convener protocol yields genuine understanding across traditions).
  Status: CONTESTED (15a: PARTIALLY-SUPPORTED (Moderate) | 15b: PARTIALLY-CHALLENGED (Moderate-Strong) | 15c: MONITOR -> MONITOR-414; DISPOSITION-394, 2026-07-03)
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-408
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated study framing ("against pessimism ... MacIntyre's recovery project"). [stated]
      15a/15b: Searched for supporting and challenging literature 2026-07-03 (results in lit_search_results/).
      15c: Dispositioned 2026-07-03 -> MONITOR-414 (DISPOSITION-394).
    Current status: CONTESTED (MONITOR-414 (DISPOSITION-394))

ASSUMPTION-409:
  Date identified: 2026-07-02
  Statement: A single declarative study-spec file plus a one-file runner can take a "cell" end-to-end (generate → analyze → render a paper); the stated success criterion is "a new cell runs from a single spec file." The head-start is noted: `sim_harness.py` + `sim_analyze.py` are already most of the runner, and the spec "just formalizes today's CLI flags and constants."
  Context: "InterT study" session — defining Appendix G, Stage 1 (study spec + one-file runner) as the next session's opener.
  Type: architectural / methodological
  Related decisions: DECISION-075
  Related items: ASSUMPTION-407 (preregister gate as Stage 2); PRESUMPTION-441 (one-cell → arbitrary-cell generalization)
  Testability: testable empirically — whether a new cell in fact runs end-to-end from one spec file without per-cell code changes.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-409
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated Appendix G Stage 1 goal and success criterion. [stated]
    Current status: UNTESTED

ASSUMPTION-410:
  Date identified: 2026-07-02
  Statement: The thesis-bearing hypothesis P3′b (that consciousness-type claims are harder to faithfully restate than spacetime-type claims) is currently directional/underpowered, not a banked "PASS." With only 4 failures and consciousness points already 60% of faithful events, 3-of-4 consciousness failures ≈ the base-rate expectation (~0.48); the only genuinely suggestive signal is zero failures among 20 spacetime restatements (~0.18). Stated as an honest correction the error analysis forced, applied throughout (scorecard, intro, results, discussion, conclusion) and reframed as "a promissory note the strengthened panel must settle, not a banked result."
  Context: "The convener" session — honest-correction #1 from the §5.5 error analysis.
  Type: methodological / empirical
  Related decisions: DECISION-075
  Related items: ASSUMPTION-406 (k=5 inference); OPEN-106 (does P3′b survive a strengthened panel?)
  Testability: testable empirically — the §5.3 strengthening run is precisely what would earn P3′b a quotable confidence interval.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-410
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated downgrade of P3′b to directional/underpowered. [stated]
    Current status: UNTESTED

ASSUMPTION-411:
  Date identified: 2026-07-05
  Statement: "the footer nav shifts vertically because each triple's body is a different height, so Next lands at a different screen spot every time. Moving it into the fixed title bar keeps it put." The header is additionally locked to a single line so it never reflows.
  Context: "Explorer Bugs PRS triplets review" session (attended) — relocating the PRS-triple modal's Prev/Next nav after Tom reported the footer buttons jumping.
  Type: architectural / empirical
  Related decisions: DECISION-076
  Related items: ASSUMPTION-412; OPEN-109
  Testability: testable empirically — the footer-level fix was verified in-session (Tom: "nav now moved to header successfully"), though a residual vertical header jump remained.
  Status: UNTESTED (in-session evidence partially supportive; residual jump outstanding)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-411
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated causal diagnosis of the footer-nav jump. [stated]
    Current status: UNTESTED

ASSUMPTION-412:
  Date identified: 2026-07-05
  Statement: "That's the vertical-centering: the modal box is centered, so a shorter or taller triple makes the box a different height, and centering nudges the whole box — header included — up or down. Pinning the box to a fixed top removes it" (implemented as a constant 6vh top offset).
  Context: "Explorer Bugs PRS triplets review" session — diagnosing the residual header jump after the nav moved to the header.
  Type: empirical
  Related decisions: DECISION-077
  Related items: ASSUMPTION-411; OPEN-109; PRESUMPTION-445
  Testability: testable empirically — the in-session prediction did NOT visibly hold ("quit, restarted, but still vert jumping"), but the falsification is unconfirmed: build/cache state was never verified before the session pivoted to the handoff. Handoff's leading next fix: fixed `.tbox` height instead of `max-height`.
  Status: UNTESTED (in-session evidence against, unconfirmed — see OPEN-109)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-412
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated vertical-centering diagnosis and its fixed-top prediction. [stated]
    Current status: UNTESTED

ASSUMPTION-413:
  Date identified: 2026-07-05
  Statement: Because no per-triplet file exists on disk (each triple is a `PRS-NN:` block inside `traditions/<key>/prs_triplets.md`), "hyperlink every triplet to its associated file" is validly implemented as "open that triple's full content in place, with the source file path shown in the modal footer."
  Context: "Explorer Bugs PRS triplets review" session — flagged explicitly by the assistant as a judgment call for Tom's review; Tom did not object in-session.
  Type: methodological
  Related decisions: DECISION-076
  Related items: (none)
  Testability: framework commitment (interpretive reading of intent; testable only against Tom's stated preference — the offer of a real deep link to the source `.md` remains open)
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-413
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated interpretive judgment call about "hyperlink every triplet to its associated file". [stated]
    Current status: UNTESTED

ASSUMPTION-414:
  Date identified: 2026-07-05
  Statement: Shipping the modal with the known vertical-jump defect is acceptable for ISME — "the vertical jump ships and stays a post-ISME polish item." The premise: a visible-but-minor known defect does not undermine the ISME-facing artifact's purpose.
  Context: "Explorer Bugs PRS triplets review" session — Tom's explicit choice (in-session question) to push the current build, modal included.
  Type: methodological / normative
  Related decisions: DECISION-076
  Related items: PRESUMPTION-444
  Testability: testable via literature (release decisions with known minor defects; technical-debt triage) and empirically (whether the defect draws notice at ISME).
  Status: CONTESTED (15a: SUPPORTED (Strong) | 15b: PARTIALLY-CHALLENGED (Moderate) | 15c: MONITOR -> MONITOR-416; DISPOSITION-400, 2026-07-06)
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-414
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated ship-with-known-defect call. [stated]
    Current status: CONTESTED (MONITOR-416 (DISPOSITION-400))

ASSUMPTION-415:
  Date identified: 2026-07-05
  Statement: Git lock files that persist with no live git process are stale and safe to remove; but "a fresh HEAD.lock appearing right after you cleared index.lock suggests a git process is genuinely mid-operation ... Deleting a live lock can corrupt refs." Candidate live writers named in-session: the Sunday weekly janitor task and the heartbeat cron.
  Context: "Explorer Bugs PRS triplets review" session — the ISME push failed on `.git/index.lock`, then a fresh `.git/HEAD.lock`; the transcript ends awaiting Tom's process listings.
  Type: methodological / empirical
  Related decisions: DECISION-076
  Related items: OPEN-110; PRESUMPTION-446
  Testability: testable empirically — identify the concurrent writer from process listings and the janitor/heartbeat schedules.
  Status: UNTESTED (in-session outcome unrecorded)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-415
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated stale-vs-live lock reasoning during the blocked ISME push. [stated]
    Current status: UNTESTED

ASSUMPTION-416:
  Date identified: 2026-07-05
  Statement: The June 12, 2026 "Future of Science and Technology Q&A" contains a genuinely new observer-boundary / whole-brain-emulation segment not yet in the wiki, extending PRS-12/17 and bridging to Hawkins, Levin, Hoffman, and Kastrup — asserted at Medium/Speculative confidence because the full transcript could not be fetched, with the evidence gap explicitly noted for Tom's review.
  Context: "C2a2 agent wolfram" scheduled run (2026-07-05) — basis of PROP-2026-07-05-001.
  Type: empirical
  Related decisions: (none — proposal pending review)
  Related items: PRESUMPTION-447
  Testability: testable empirically — obtain the full Q&A transcript and check the segment against PRS-12/17 and existing Wolfram triplets.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-416
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Wolfram agent's stated novelty claim and confidence downgrade. [stated]
    Current status: UNTESTED

ASSUMPTION-417:
  Date identified: 2026-07-05 (late-evening addendum)
  Statement: The `ps aux | grep git` hits during the lock investigation were "all false positives — the grep matched the substring 'git' inside the Claude sessions' huge command lines... None is an actual git process," therefore "both locks are stale from an interrupted operation — safe to clear" (including `.git/objects/maintenance.lock`).
  Context: DECISION-078 — clearing HEAD.lock, index.lock, and maintenance.lock to land the ISME commit ("Explorer Bugs PRS triplets review" session, late continuation).
  Type: empirical
  Related decisions: DECISION-076, DECISION-078
  Related items: ASSUMPTION-415 (stale-vs-live lock reasoning, earlier same session); PRESUMPTION-448
  Testability: testable empirically — in-session evidence FOR: after removal the commit (c543afa) completed cleanly and no lock reappeared. [stated diagnosis; in-session corroboration noted, not evaluated]
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-417
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated false-positive diagnosis preceding lock removal. [stated]
    Current status: UNTESTED

ASSUMPTION-418:
  Date identified: 2026-07-05 (late-evening addendum)
  Statement: Because `wiki/review_log.html` disappeared from `git status` after commit c543afa recorded only "1 file changed," the page "got committed, almost certainly by the daily wiki agent, whose pipeline re-runs `refresh_review_log.sh` and commits the result."
  Context: diagnosing why the two-file surgical commit (DECISION-076) captured only the generator script.
  Type: empirical
  Related decisions: DECISION-076, DECISION-078
  Related items: ASSUMPTION-419; PRESUMPTION-446 (uncoordinated multi-writer repo)
  Testability: testable empirically — in-session evidence FOR: `git log -- wiki/review_log.html` shows 5b7e68a "C2A2 daily run — 2026-07-05" as the most recent commit touching the page. [stated inference with in-session corroboration]
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-418
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated attribution of the page commit to the daily agent. [stated]
    Current status: UNTESTED

ASSUMPTION-419:
  Date identified: 2026-07-05 (late-evening addendum)
  Statement: The committed page is the intended build: "tnavwrap = 2 (the CSS rule + the HTML span) and 6vh pin = 1. The daily-run commit 5b7e68a regenerated review_log.html from your updated generator, so the committed page has the full pop-up and the vertical pin. Nothing stale shipped."
  Context: verifying the deliverable after the daily agent committed the page out from under the attended session.
  Type: empirical
  Related decisions: DECISION-076
  Related items: ASSUMPTION-418; PRESUMPTION-450. RATIONALE DRIFT NOTE: earlier in the same session the expected `grep -c tnavwrap` count was stated as `1` ("If the count is 1 and the timestamp is fresh, the file is correct"); on observing `2` the expectation was reinterpreted post hoc as "the CSS rule + the HTML span" without flagging the change. [inferred flag on a stated claim]
  Testability: testable empirically — render the committed page and confirm modal + pinned header visually (the session's own no-blind-push standard).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-419
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated marker-based verification of commit 5b7e68a; rationale-drift on the expected marker count flagged. [stated + inferred flag]
    Current status: UNTESTED

ASSUMPTION-420:
  Date identified: 2026-07-05 (late-evening addendum)
  Statement: "Rebase guards against the usual non-fast-forward from the heartbeat cron" — i.e., fetch+rebase+push is a sufficient convergence recipe for this multi-writer repo.
  Context: the push recipe issued for DECISION-076's execution.
  Type: methodological
  Related decisions: DECISION-076, DECISION-078
  Related items: PRESUMPTION-446, PRESUMPTION-449; OPEN-113
  Testability: testable empirically — in-session evidence AGAINST: the rebase aborted ("cannot rebase: You have unstaged changes" — the uncommitted architecture drift) and the push was rejected non-fast-forward after the remote advanced to 511b3b2 mid-session. The guard fails exactly when the working tree carries the agent drift that OPEN-111 says is always present. [stated claim; in-session counter-evidence noted, not evaluated]
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-420
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated rationale for the fetch/rebase/push block; recorded the in-session failure as evidence context. [stated]
    Current status: UNTESTED

ASSUMPTION-421:
  Date identified: 2026-07-06
  Statement: "Re-running the full protocol would duplicate baseline artifacts and re-stamp dispositions already on record. ... a structurally identical 3,000-line file two runs later is clutter, not measurement."
  Context: the sewing bootstrap task fired a third time (labeled ONE-TIME); the run chose verification-mode over re-execution and stated this rationale for writing no third census file.
  Type: methodological
  Related decisions: none on record — autonomous adaptation by a scheduled agent; retirement recommendation routed to Tom (see OPEN-114)
  Related items: ASSUMPTION-422, PRESUMPTION-451
  Testability: testable via literature — data-provenance and research-data-management norms on baseline duplication vs re-measurement; when is a repeated census measurement and when is it noise?
  Status: CONTESTED (15a: PARTIALLY-SUPPORTED (Moderate) | 15b: PARTIALLY-CHALLENGED (Moderate) | 15c: MONITOR -> MONITOR-417; DISPOSITION-411, 2026-07-07)
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-421
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the sewing bootstrap verification report (sewing_agent_bootstrap_2026-07-06.md), "Why this is not a third full bootstrap" section. [stated]
      15a/15b: independent parallel literature searches (2026-07-07); 15c: dispositioned (see Status). [searched]
    Current status: CONTESTED (MONITOR-417)

ASSUMPTION-422:
  Date identified: 2026-07-06
  Statement: "A second row one day later, from a slightly different resolver, would add methodological noise to the trend line."
  Context: the sewing verification run's rationale for NOT appending to connectivity_log.csv (owned by the weekly agent, which wrote its row 2026-07-05 with an independent resolver).
  Type: methodological
  Related decisions: none on record
  Related items: ASSUMPTION-421, PRESUMPTION-452
  Testability: testable via literature — measurement invariance / instrument-change effects in longitudinal studies; mixed-instrument time series validity.
  Status: CONTESTED (15a: SUPPORTED (Strong) | 15b: CHALLENGED (Strong) | 15c: MONITOR -> MONITOR-418; DISPOSITION-412, 2026-07-07 — genuine strong/strong contest; consensus is tag-and-model the cross-resolver row, not discard it)
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-422
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the sewing bootstrap verification report, "Deliberately NOT written on this run" list. [stated]
      15a/15b: independent parallel literature searches (2026-07-07); 15c: dispositioned (see Status). [searched]
    Current status: CONTESTED (MONITOR-418)

ASSUMPTION-423:
  Date identified: 2026-07-06
  Statement: "The knowledge graph remains sufficient to support thinker-agent synthesis ... The bottleneck is not connectivity."
  Context: the sewing verification's vault-health assessment, grounded in the census delta (all +157 new pages orphans-by-design; sparse 647 and connected 47 unchanged; tradition prs_triplets.md files hold top backlink counts).
  Type: empirical / architectural
  Related decisions: none on record
  Related items: PRESUMPTION-453 (whether the orphan-dominated census can support this conclusion)
  Testability: testable empirically — correlate connectivity measures with synthesis yield (proposals, PRS triplets, cross-connections) per tradition over time.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-423
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the sewing bootstrap verification report, "Vault health assessment" section. [stated]
    Current status: UNTESTED

ASSUMPTION-424:
  Date identified: 2026-07-06
  Statement: "the weekly `c2a2-sewing-agent-weekly` owns ongoing orphan/sparse tracking" — therefore the one-time bootstrap task can be retired (or folded into a quarterly delta) without loss of measurement coverage.
  Context: the sewing verification's closing recommendation to retire/reschedule the bootstrap task.
  Type: architectural
  Related decisions: pending — awaits Tom's decision (OPEN-114)
  Related items: ASSUMPTION-421, PRESUMPTION-451
  Testability: testable empirically — diff the weekly agent's measurement scope (connectivity_log.csv fields, cadence, resolver) against the bootstrap protocol's full-census scope; identify anything only the bootstrap measures.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-424
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the sewing bootstrap verification report, "Recommended action for Tom" section. [stated]
    Current status: UNTESTED

ASSUMPTION-425:
  Date identified: 2026-07-06
  Statement: "The .md file is the primary deliverable — it persists even if browser delivery fails."
  Context: the Cowork→Chat evening sync design; operative today when both sync agents hit the logged-out claude.ai session (morning scrape produced a failure note; evening summary was written but NOT delivered, warning stamped in its header).
  Type: architectural
  Related decisions: none on record (design stated in the scheduled-task definition)
  Related items: PRESUMPTION-454 (whether file-fallback actually preserves continuity when the failure is in the notification channel itself)
  Testability: testable empirically — the fallback fired twice today; the open question is whether file-only delivery reaches Tom in practice (does the morning Chat context ever recover the undelivered summaries?).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-425
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the c2a2-evening-cowork-to-chat task definition and today's run behavior (both sync transcripts read directly). [stated]
    Current status: UNTESTED

ASSUMPTION-426:
  Date identified: 2026-07-07
  Statement: "The Lex Fridman 'June 2026' result is unreliable — the only real Lex/Hoffman episode is #293 from June 2022. I won't propose that." — a tradition agent can reliably reject hallucinated web-search results by cross-checking them against its own knowledge of a thinker's appearance catalog.
  Context: the Tuesday Hawkins/Hoffman proposal run; a search surfaced a purported June 2026 Lex Fridman episode with Hoffman, which the agent rejected as spurious while accepting the StarTalk/Tyson episode (2026-06-26) after two confirming searches.
  Type: methodological
  Related decisions: none on record — autonomous filtering behavior by a tradition agent
  Related items: PRESUMPTION-457 (whether model priors are a valid oracle for this rejection)
  Testability: testable empirically — audit rejected-source decisions against ground truth over time (false-rejection rate of the catalog-prior filter); testable via literature — hallucination-detection and source-triangulation practices in automated research pipelines.
  Status: CONTESTED (MONITOR-419 via DISPOSITION-424, 2026-07-09 — catalog-check error rate to be measured before the detector is trusted)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-426
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the c2a2-agent-hawkins-hoffman transcript (2026-07-07), verification reasoning before writing the Hoffman proposal. [stated]
    Current status: CONTESTED

ASSUMPTION-427:
  Date identified: 2026-07-07
  Statement: "Since the DB has had no writes since 2026-07-06 03:55Z, there is no live writer and a torn copy is impossible — the corruption is in the source file."
  Context: the openstory telemetry refresh run; quick_check failed on a local byte-copy with the same page-1051384 rowid errors as 2026-07-06, and the agent concluded the corruption is real (in the source), not a copy artifact, then skipped extractor retries as deterministically futile.
  Type: empirical
  Related decisions: none on record
  Related items: PRESUMPTION-455 (the metabolism agent independently re-entertained the FUSE-artifact hypothesis the same morning)
  Testability: testable empirically — the recommended native-Mac `sqlite3 quick_check` / `.recover` will confirm or refute source-file corruption directly; testable via literature — fidelity guarantees of byte-copies over network/FUSE mounts for quiescent files.
  Status: CHALLENGED (REVISE-189 via DISPOSITION-425, 2026-07-09, HIGH — sandbox-copy corruption verdict unsound; native quick_check + sidecars/backup-API required before any corruption verdict)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-427
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the openstory-agents-telemetry-refresh transcript (2026-07-07), corruption-diagnosis rationale. [stated]
    Current status: CHALLENGED

ASSUMPTION-428:
  Date identified: 2026-07-07
  Statement: "Deliberately deferred and surfaced, not silent" — deferring the 117-item 15d refresh backlog for a third consecutive run is acceptable risk management so long as the deferral is explicitly reported and a remedy (dedicated backlog-burn run or 15d-cadence rethink) is recommended.
  Context: the lit-search pipeline run's closing report, after fully dispositioning the fresh 07-06 cohort while leaving the 15d re-check backlog untouched again.
  Type: methodological
  Related decisions: none on record — remedy recommendation awaits scheduling (see OPEN-115)
  Related items: PRESUMPTION-456 (whether surfaced-in-files reliably converts to human action); ASSUMPTION-425 (file-as-deliverable kin)
  Testability: testable empirically — track whether surfaced deferrals get acted on before they cause staleness harm (15d items are re-checks of previously validated premises; how stale can they get before a premise flips unnoticed?); testable via literature — backlog decay and alert-fatigue in maintenance queues.
  Status: CONTESTED (MONITOR-420 via DISPOSITION-426, 2026-07-09, High — deferral acceptability conditionally held; auto-escalate after 2 more no-decision runs)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-428
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the c2a2-lit-search-pipeline transcript (2026-07-07), final run report. [stated]
    Current status: CONTESTED

ASSUMPTION-429:
  Date identified: 2026-07-08
  Statement: "The weekly re-trigger volume (~55/week) structurally exceeds one pipeline run's throughput, so the queue is growing monotonically." A structural capacity mismatch, not a transient, is assumed to explain the 15d backlog — hence the recommended remedy is cadence/cap redesign rather than more deferral.
  Context: c2a2-lit-search-pipeline closing report, after burning the 7 HIGH-priority items of the 07-05 re-trigger cohort and leaving 116 of 123 queued items unsearched (fourth run carrying the backlog).
  Type: empirical
  Related decisions: none on record — remedy awaits scheduling (OPEN-115, OPEN-116)
  Related items: ASSUMPTION-428 (deferred-and-surfaced); PRESUMPTION-462 (fixed cadences right-sized)
  Testability: testable empirically — arrival rate vs per-run throughput over the run logs; queue-depth trajectory under a cadence or cap change.
  Status: GROUNDED (INCORPORATED as PREMISE-095 via DISPOSITION-431, 2026-07-09 — 15a SUPPORTED/Strong; 15b scope caveat folded in: structural-under-current-provisioning, not immutable)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-429
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the c2a2-lit-search-pipeline transcript (2026-07-08), final run report. [stated]
    Current status: GROUNDED

ASSUMPTION-430:
  Date identified: 2026-07-08
  Statement: "Rather than defer a fourth time, I burned the 7 HIGH-priority weekly items" — priority-ordered partial burn is an acceptable triage response to an over-capacity queue: process the HIGH tier end-to-end, let the remaining 116 items wait, and surface the residue.
  Context: c2a2-lit-search-pipeline run, choosing among defer-again / burn-all / burn-by-priority when the queue held no fresh items, only the 123-item re-trigger backlog.
  Type: methodological
  Related decisions: none on record
  Related items: ASSUMPTION-428; PRESUMPTION-459 (queue-time priorities remain valid at burn time)
  Testability: testable via literature — triage and WSJF-style prioritization under overload; aging/starvation of low-priority queue items.
  Status: CONTESTED (MONITOR-423 via DISPOSITION-432, 2026-07-09, High — partial burn acceptable only with an aging mechanism; watch for starvation)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-430
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the c2a2-lit-search-pipeline transcript (2026-07-08). [stated]
    Current status: CONTESTED

ASSUMPTION-431:
  Date identified: 2026-07-08
  Statement: 'the qc_sweep "fidelity fail" is only the absent /tmp/dayNNN_segments.json cache in this fresh sandbox, not a real fidelity defect' — a failing QC signal can be reclassified as environmental (missing cache artifact in a fresh sandbox) without independently re-verifying the underlying content, because `fidelity_checked: true` already stands in the transcripts.
  Context: Summa commentary reviewer run (Days 206–211), dismissing the sweep's fidelity failure while passing all six pairs.
  Type: methodological
  Related decisions: none on record
  Related items: the reaffirmed High "unvalidated-instrument" systemic risk (15c, 2026-07-08) — an instrument's failure explained away by the same system it checks; PRESUMPTION-455 (per-task diagnosis)
  Testability: testable empirically — regenerate the segments cache in-sandbox and re-run the fidelity check; if it passes, the environmental explanation holds.
  Status: CHALLENGED (REVISE-192 via DISPOSITION-433, 2026-07-09 — regenerate cache and re-run QC before accepting an "environmental" reclassification)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-431
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Summa commentary reviewer transcript (2026-07-08). [stated]
    Current status: CHALLENGED

ASSUMPTION-432:
  Date identified: 2026-07-08
  Statement: "date-stripped slug diff vs PROCESSED_LOG shows 0 truly-unprocessed" — the inbox-clear verdict rests on the slug-diff method being a faithful detector of unprocessed items: date-stripping never collides two distinct items, and PROCESSED_LOG is complete.
  Context: C282 wiki agent daily run, Phase 1 (Ingest), declaring the inbox clear.
  Type: architectural
  Related decisions: none on record
  Related items: ASSUMPTION-426 (catalog-prior filtering — kin: registry treated as ground truth)
  Testability: testable empirically — inject a known-unprocessed item whose date-stripped slug matches a processed one; audit PROCESSED_LOG completeness against the raw inbox archive.
  Status: CONTESTED (MONITOR-424 via DISPOSITION-434, 2026-07-09 — slug-collision and log-completeness audit pending)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-432
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the C282-wiki-agent-daily-run transcript (2026-07-08), Phase 1 report. [stated]
    Current status: CONTESTED

ASSUMPTION-433:
  Date identified: 2026-07-09
  Statement: "Prior runs reported 116/123 — the measured count is 110; the discrepancy suggests earlier figures were estimates, worth a one-time reconciliation." The pipeline assumes carried-forward backlog tallies were estimates (and the fresh count is the measurement), rather than the discrepancy indicating lost or mis-tagged items.
  Context: c2a2-lit-search-pipeline run tally, 2026-07-09 — first run to measure the 15d backlog directly instead of carrying the prior figure forward.
  Type: empirical
  Related decisions: none — reconciliation recommended, not yet scheduled
  Related items: ASSUMPTION-429 / PREMISE-095 (backlog trajectory feeds the validated queue-growth premise); PRESUMPTION-466 (the interpretive leap itself)
  Testability: testable empirically — a one-time reconciliation pass over for_lit_search.md tags vs run-log arithmetic decides between estimate-drift and item loss.
  Status: CONTESTED (MONITOR-426 via DISPOSITION-439, 2026-07-10, Med-High — ID-level reconciliation decides estimate-drift vs item loss; same test as REVISE-200)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-433
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the c2a2-lit-search-pipeline run tally (2026-07-09), BACKLOG SURFACED section, exact quote. [stated]
    Current status: CONTESTED

ASSUMPTION-434:
  Date identified: 2026-07-09
  Statement: "Supabase free-tier projects pause after 7 days with no DB activity" and one trivial daily query ("SELECT 1") is sufficient to reset the inactivity clock — i.e., the platform's activity detector counts any successful SQL execution.
  Context: supabase-c2a2-keep-warm scheduled task definition and successful run, 2026-07-09 — the task exists solely on this premise, protecting the Pathway-00 broker during quiet pre-ISME stretches.
  Type: empirical
  Related decisions: implicit scheduling decision (keep-warm task creation, pre-existing)
  Related items: PRESUMPTION-463 (unverified proxy loop)
  Testability: testable via literature — Supabase's published pause policy and what counts as activity; testable empirically only destructively (let it idle).
  Status: CONTESTED (MONITOR-427 via DISPOSITION-440, 2026-07-10, Low-Med — outcome-probe the keep-warm via management API rather than inferring from ping success)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-434
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the supabase-c2a2-keep-warm task file and run transcript (2026-07-09). [stated]
    Current status: CONTESTED

ASSUMPTION-435:
  Date identified: 2026-07-09
  Statement: "OpenStory DB is stale (last write 2026-07-06T03:56Z, ~78h ago); OpenStory runtime is likely down; feeds NOT refreshed." Two nested assumptions: (1) write-staleness beyond the guard threshold is a reliable indicator that the runtime is down; (2) refusing to refresh feeds from a stale DB is the correct failure mode (stale feeds are worse than frozen feeds).
  Context: openstory-agents-telemetry-refresh run, 2026-07-09 — second consecutive freshness-guard trip; only REFRESH_STATUS.md was appended.
  Type: methodological
  Related decisions: none on record for the guard's threshold or its refuse-on-stale policy
  Related items: ASSUMPTION-363 (openstory heartbeat, CONTESTED); REVISE-186 (out-of-band probe); REVISE-189 (corruption verdict unsound — the guard reads the same DB)
  Testability: testable empirically — the pending native-Mac .recover plus a runtime restart decides whether staleness tracked runtime state; the freeze-vs-stale preference is a design judgment informed by monitoring literature.
  Status: CHALLENGED (REVISE-196 via DISPOSITION-441, 2026-07-10, Med — staleness is not a reliable down-signal; serve-stale-labeled + real liveness probe)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-435
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the openstory-agents-telemetry-refresh transcript (2026-07-09), FAIL line quoted verbatim. [stated]
    Current status: CHALLENGED

ASSUMPTION-436:
  Date identified: 2026-07-09
  Statement: A file in pending/ is a valid proposal if and only if it carries `proposal_id` frontmatter — "earlier proposal count showed 17 filenames but one was a stray non-frontmatter file; 16 carry valid `proposal_id` frontmatter."
  Context: morning-walk-cowork-handoff run, 2026-07-09 — the briefing's pending-proposal count (16) was corrected downward on this criterion; the same count then propagated to the evening summary and review page.
  Type: methodological
  Related decisions: none on record defining proposal validity
  Related items: ASSUMPTION-432 (slug-diff inbox detector — sibling counting-rule assumption, CONTESTED); PRESUMPTION-456 (review backlog saturation — the count this rule produces is the load signal)
  Testability: testable empirically — inspect the stray file: is it a malformed real proposal (undercount) or debris (correct exclusion)? Does any downstream consumer read files without frontmatter?
  Status: CONTESTED (MONITOR-428 via DISPOSITION-442, 2026-07-10, Low-Med — inspect the stray 17th file: malformed proposal or debris)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-436
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the morning-walk-cowork-handoff transcript (2026-07-09), closing note. [stated]
    Current status: CONTESTED

ASSUMPTION-437:
  Date identified: 2026-07-10
  Statement: "All 8 fresh-cohort items processed end-to-end; the 13 remaining unsearched July items are all older QUEUED-EMPIRICAL items held by convention for in-house tests — nothing was missed." The pipeline assumes its tag-based enumeration of the queue is complete — that "held by convention" and "missed" are exhaustive, mutually exclusive categories the tags reliably distinguish.
  Context: c2a2-lit-search-pipeline run, 2026-07-10 — closing completeness claim after dispositioning the 2026-07-09 EOD cohort (DISPOSITION-439..446).
  Type: methodological
  Related decisions: none — the QUEUED-EMPIRICAL convention itself is undecided (OPEN-117)
  Related items: ASSUMPTION-432 (log-completeness audit, CONTESTED); ASSUMPTION-433 (count integrity, CONTESTED — MONITOR-426); OPEN-117 (which convention governs the held items)
  Testability: testable empirically — enumerate July-dated queue entries by provenance ID and tag; verify the 8+13 partition covers them with no untagged remainder (folds into the MONITOR-426/REVISE-200 reconciliation).
  Status: CHALLENGED (REVISE-201 via DISPOSITION-447, 2026-07-11 — 15a no-support / 15b challenged Strong: tag-based enumeration completeness unverifiable as claimed)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-437
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the c2a2-lit-search-pipeline run report (2026-07-10), closing completeness claim, exact quote. [stated]
    Current status: CHALLENGED

ASSUMPTION-438:
  Date identified: 2026-07-10
  Statement: "No new primary material in past 30 days" justifies zero proposals for a tradition agent — specifically, an Indico contribution whose title "remains 'TBC' with no slides/recording posted" means the 2026-07-02 Amplitudes talk has nothing capturable yet, and a next-run watch item is the correct remedy for the gap.
  Context: c2a2-agent-carroll-arkanihamed Friday run, 2026-07-10 — Arkani-Hamed side returned 0 proposals on this criterion while the Carroll side wrote PROP-2026-07-10-001 (Mindscape 360).
  Type: methodological
  Related decisions: none on record defining tradition-agent absence criteria
  Related items: PRESUMPTION-457 (prior-as-oracle for adjudicating coverage, CHALLENGED); PRESUMPTION-467..470 cohort (public-availability lag is the unstated half — see PRESUMPTION-469 note); FLAG/watch item in the run output
  Testability: testable empirically — when the talk materials post, measure the capture lag and whether proposal-worthy content existed during the "nothing new" window.
  Status: CONTESTED (MONITOR-429 via DISPOSITION-448, 2026-07-11 — 15a partial / 15b challenged Strong: 30-day-window zero-proposal criterion under monitor)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-438
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Friday tradition-agent run report (2026-07-10), Arkani-Hamed zero-proposal rationale, near-verbatim. [stated]
    Current status: CONTESTED

ASSUMPTION-439:
  Date identified: 2026-07-10
  Statement: "The last DB write (Jul 6 ~03:55Z) coincides with the corruption recurrence recorded that same day — the runtime has apparently been down since." The staleness signal and the corruption event are assumed to share one cause: a dead runtime, down continuously for ~102h.
  Context: openstory-agents-telemetry-refresh run, 2026-07-10 — third consecutive freshness-guard trip; only REFRESH_STATUS.md written (FAIL line).
  Type: empirical
  Related decisions: none — remediation (.recover + LaunchAgent restart) remains a recommendation
  Related items: ASSUMPTION-435 (staleness→down inference, CHALLENGED — REVISE-196 says staleness is not a reliable down-signal, making this a live instance); ASSUMPTION-427 (copy-verdict, CHALLENGED — REVISE-189); REVISE-186 (out-of-band probe)
  Testability: testable empirically — a Mac-side process/launchd check or the pending .recover + restart decides whether the runtime was in fact down the whole interval or writing elsewhere/failing to flush.
  Status: CONTESTED (MONITOR-430 via DISPOSITION-449, 2026-07-11 — 15a partial / 15b challenged Strong: common-cause downtime inference; Mac-side probe decisive)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-439
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the openstory-agents-telemetry-refresh report (2026-07-10), causal-coincidence note, exact quote. [stated]
    Current status: CONTESTED

ASSUMPTION-440:
  Date identified: 2026-07-10
  Statement: "lastRunAt is authoritative for whether a task *fired*. Output file dates are a secondary check for whether it *succeeded*. A missing output file is a warning, not proof the task didn't run" — plus the run's applied corollary: an unverifiable output check (vault not mounted) downgrades to "unverified, not failed."
  Context: scheduler-health-check watchdog run, 2026-07-10 — the authority hierarchy is written in the task file and was exercised today on summa-2026-daily-batch (fired, output unverifiable) and c282-wiki-agent-daily-run (fired, output "verified" — but see PRESUMPTION-468).
  Type: methodological
  Related decisions: none on record — the hierarchy was adopted in the watchdog task file without a recorded decision
  Related items: PRESUMPTION-465 (fail-loud listener, CHALLENGED); PRESUMPTION-467, PRESUMPTION-468 (today — the two gaps this hierarchy leaves open); SYSTEMIC-RISK open-loop self-assurance (2026-07-10)
  Testability: testable via literature — liveness vs correctness signals in monitoring design; testable empirically — inject a fire-but-fail task and observe whether the hierarchy classifies it as healthy.
  Status: CONTESTED (MONITOR-431 via DISPOSITION-450, 2026-07-11 — 15a supported Strong / 15b challenged Strong: fired-vs-succeeded hierarchy contested; see P-467/468)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-440
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the scheduler-health-check task file (quoted verbatim) and its 2026-07-10 run's application of the rule. [stated]
    Current status: CONTESTED

ASSUMPTION-441:
  Date identified: 2026-07-11
  Statement: "The qc_sweep report again showed 0 needing review (307/307 'fresh'), which is the known synthesis-only blindness; a full-vault transcript scan found 81 files with last_qc_at >7 days old." Stated: the report's 0-needs-review is a reliable false negative, and the full-vault transcript scan is the authoritative staleness measure; a script-level fix is recommended.
  Context: Summa QC sweep (evening run), 2026-07-11 — the workaround is now executed every run at the cost of one extra step.
  Type: methodological
  Related decisions: none — the script fix is a recommendation, queued behind decisions
  Related items: OPEN-116 (fixed cadences); PRESUMPTION-467 (dashboard-vs-outcome, CHALLENGED); PRESUMPTION-473 (today — self-referential denominators; the report's 307/307 denominator is the known-wrong instance)
  Testability: testable empirically — implement the script fix and compare its needs-review set against the full-vault scan over several runs.
  Status: CONTESTED (MONITOR-432 via DISPOSITION-455, 2026-07-12 — 15a partially-supported / 15b partially-challenged: scope-blindness precedented, but "authoritative" full scan is the imperfect-gold-standard error; awaiting script fix + hand-adjudicated sample n≈20)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-441
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-11 evening Summa QC sweep transcript, exact quote. [stated]
    Current status: CONTESTED

ASSUMPTION-442:
  Date identified: 2026-07-11
  Statement: "The C2A2 wiki mount was absent this run, so PRS-ids in these six syntheses were form-checked only. ... I recommended an id spot-check of 239/240 next time the wiki mounts." Stated: form-check-only is an acceptable degraded QC mode when the wiki is unmounted, provided a deferred spot-check compensates.
  Context: Summa QC sweep (evening run), 2026-07-11 — the same morning, the commentary reviewer found real PRS-id drift (Days 160–163), which is what makes the degraded mode's adequacy a live question.
  Type: methodological
  Related decisions: none
  Related items: PRESUMPTION-471 (today — the QC stamp does not record verification depth); PRESUMPTION-469 (CHALLENGED — noted fixes reach no future run; the spot-check recommendation lives only in a run output)
  Testability: testable empirically — perform the recommended spot-check of Days 239/240 on a mounted run and measure id-drift incidence in form-check-only pairs.
  Status: CHALLENGED (REVISE-206 via DISPOSITION-456, 2026-07-12 — graceful-degradation support strictly conditional on predefined mode / distinguishable outputs / enforced compensation; instance fails at least two (P-471 stamp, ownerless deferred spot-check); normalization-of-deviance entry pattern)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-442
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-11 evening Summa QC sweep transcript, exact quotes. [stated]
    Current status: CHALLENGED

ASSUMPTION-443:
  Date identified: 2026-07-11
  Statement: The PRS citation-mislabel cluster (Days 161–163 cite "Friston PRS-02" for content at PRS-04/PRS-03; Day 160 glosses Stump PRS-09 as second-personal knowing, which is PRS-11) is "same class as the Day-23 escalation — may indicate a writer-pass-level pattern worth a full-vault audit," and is therefore best repaired by a batch grep rather than day-by-day.
  Context: Summa commentary reviewer escalation, 2026-07-11 (as carried in the evening cowork summary) — flagged as a cluster for Tom's approval.
  Type: empirical
  Related decisions: none yet — see OPEN-118 (today)
  Related items: OPEN-118; PRESUMPTION-472 (today — grep-ability of the error class); the Day-23 escalation precedent
  Testability: testable empirically — run the batch grep / full-vault audit and check whether mislabels concentrate in identifiable writer-pass cohorts.
  Status: CONTESTED (MONITOR-433 via DISPOSITION-457, 2026-07-12 — batch-over-piecemeal supported; batch boundary and grep-exhaustion closure criterion contested; full-vault audit is the discriminating test, closure governed by REVISE-208)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-443
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the commentary-reviewer escalation as quoted in the 2026-07-11 evening cowork summary. [stated]
    Current status: CONTESTED

ASSUMPTION-444:
  Date identified: 2026-07-11
  Statement: "Signing back in to claude.ai in Chrome restores both sync directions." Stated: the Chrome login is the single root cause of the 9-day sync outage; no other degradation has accumulated in either direction.
  Context: evening cowork→chat delivery failure note, 2026-07-11 — day 9 of the outage; both directions failed again today.
  Type: empirical
  Related decisions: none — REVISE-198 (Gmail fallback, HIGH) and REVISE-199 (ack + escalation, HIGH) remain the formal fixes
  Related items: PRESUMPTION-464, PRESUMPTION-465 (both CHALLENGED); REVISE-198, REVISE-199; PRESUMPTION-474 (today)
  Testability: testable empirically — sign in and observe whether the next morning scrape and evening delivery both succeed without further intervention.
  Status: CONTESTED (MONITOR-434 via DISPOSITION-458, 2026-07-12 — credential expiry warranted as LEADING hypothesis; "single root cause" blocked (Cook doctrine — 9-day detection silence is a second necessary condition); first post-login observation is the free decisive test)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-444
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-11 evening cowork summary delivery-failure header and What's Next, exact quote. [stated]
    Current status: CONTESTED

ASSUMPTION-445:
  Date identified: 2026-07-11
  Statement: "BOSCO email archive is COMPLETE at 30,529/30,529 (enrichment backlog 28,516 remains)." Stated: archive completeness is established by fetched-count equaling the enumerated total.
  Context: morning project status, 2026-07-11, as carried in the evening cowork summary — the long-running archive project's completion claim.
  Type: empirical
  Related decisions: none
  Related items: PRESUMPTION-473 (today — the denominator is produced by the same system that satisfies it); ASSUMPTION-437 (enumeration completeness, CHALLENGED today via REVISE-201); PRESUMPTION-470 (census protocol, CHALLENGED)
  Testability: testable empirically — independent recount of the source mailbox (or provider-side count) against the archive's 30,529.
  Status: CONTESTED (MONITOR-435 via DISPOSITION-459, 2026-07-12 — count parity is real first-layer evidence; "completeness established" fails on the self-produced denominator (P-473 flagship instance, 307/307 precedent); one independent provider-side count settles it)
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b → 15c → 14a]
    Original item: ASSUMPTION-445
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-11 morning project status via the evening cowork summary, exact quote. [stated]
    Current status: CONTESTED

ASSUMPTION-446:
  Date identified: 2026-07-12
  Statement: "the numbers above use the prior census definition … they sit on the established trend (2483 → 2567 orphans) rather than jumping, which suggests prior runs resolved paths correctly and the defect was introduced this run and caught before it reached the CSV. No back-correction of earlier rows is warranted." Trend continuity is taken as sufficient evidence that a basename-only wikilink-resolution defect was born and died inside this single run.
  Context: c2a2-sewing-agent-weekly run, 2026-07-12 — census method note (fail-loud) after the resolver was found mis-scoring path-form wikilinks and repaired in-run.
  Type: empirical
  Related decisions: none
  Related items: PRESUMPTION-476 (today — the in-run fix is self-certified); PRESUMPTION-470 (census protocol, CHALLENGED); REVISE-205 (census rule)
  Testability: testable empirically — re-run the prior runs' resolver (or the 07-05 vault snapshot) under both resolution modes and confirm earlier CSV rows reproduce; cheap and decisive.
  Status: CONTESTED (MONITOR-436 via DISPOSITION-464, 2026-07-13 — SPC legitimises "no special-cause signal" as first-line evidence, but a proportional resolver defect produces a smooth series BY CONSTRUCTION (Rothermel & Harrold 1997); "no jump" is what the excluded hypothesis predicts. Convention fix owned by REVISE-213 (replay). Nearly-free test: date the defect from the resolver's git history.)
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a/15b -> 15c -> 14a]
    Original item: ASSUMPTION-446
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the sewing_agent_log.md 2026-07-12 census note, exact quote. [stated]
    Current status: CONTESTED

ASSUMPTION-447:
  Date identified: 2026-07-12
  Statement: "Bridge notes are near-orphans by nature — essays link out to tradition content; almost nothing links in to them. 42 of 45 having ≤2 backlinks is the expected steady state, not a connectivity failure." Synthesis pages are assumed to be structurally exempt from the connectivity metric that governs the rest of the vault.
  Context: c2a2 bootstrap audit (4th firing), 2026-07-12 — explaining the category C delta (23 → 42) as expected rather than a regression.
  Type: architectural
  Related decisions: none
  Related items: ASSUMPTION-448 (vault-health sufficiency); the metric-inflation flag (3rd consecutive, unactioned)
  Testability: testable via literature — hypertext/personal-wiki link-topology findings on whether synthesis/essay nodes are systematically low-indegree, and whether low-indegree synthesis pages are later found or lost (discoverability vs. link-rot literature).
  Status: CONTESTED (MONITOR-437 via DISPOSITION-465, 2026-07-13 — low indegree is a structural equilibrium (Broder et al. 2000), but "expected" and "harmless" are different claims; Wikipedia orphan work (Arora et al. 2024) treats low indegree as a maintenance defect and shows de-orphanisation causally raises discovery. Hinges on SYSTEMIC-RISK #2 (traversal vs. embedding retrieval). NOTE: no peer-reviewed source characterises synthesis notes as outbound-heavy — that premise is practitioner folklore.)
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a/15b -> 15c -> 14a]
    Original item: ASSUMPTION-447
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from sewing_agent_bootstrap_2026-07-12.md, category C delta section, exact quote. [stated]
    Current status: CONTESTED

ASSUMPTION-448:
  Date identified: 2026-07-12
  Statement: "The knowledge graph remains sufficient for thinker-agent synthesis: the 14 prs_triplets.md hubs hold the top backlink counts, and the orphan population is structural/pipeline residue. The bottleneck is not connectivity." Vault health for synthesis purposes is assumed measurable by hub backlink concentration plus an orphan-population account.
  Context: c2a2 bootstrap audit (4th firing), 2026-07-12 — vault health assessment carried unchanged from the 06-28 baseline.
  Type: architectural
  Related decisions: none
  Related items: ASSUMPTION-447; the weekly sewing agent's metric-inflation measurement (full census 3258/2567 vs 1419/728 excluding machine dumps)
  Testability: testable empirically — correlate synthesis output quality (e.g., bridge-note substance, agentic-call specificity) against local connectivity; if quality tracks something else (capture recency, PROP density), connectivity is confirmed as non-bottleneck.
  Status: CHALLENGED (REVISE-211 via DISPOSITION-466, 2026-07-13 — sufficiency was derived from graph statistics without asking what consumes the graph; GraphRAG-Bench 2025 and KG-sparsity results find structure can HURT multi-hop traversal, and community summarisation would silently omit the orphan periphery. The derivation is invalid whether or not the conclusion holds. SYSTEMIC-RISK #2.)
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a/15b -> 15c -> 14a]
    Original item: ASSUMPTION-448
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from sewing_agent_bootstrap_2026-07-12.md, vault health assessment, exact quote. [stated]
    Current status: CHALLENGED

ASSUMPTION-449:
  Date identified: 2026-07-12
  Statement: "Both accept idealism; the mereologies are incompatible" (Kastrup vs. Levin, nested vs. dissociated subjects); and the standing Hoffman↔Kastrup idealism bridge "rests on a shared negation and hides an incompatible mereology" — Hoffman's composing conscious agents side with Levin against Kastrup on the individuation-of-subjects question.
  Context: c2a2-sewing-agent-weekly run, 2026-07-12 — headline finding #1: two paradigm-boundary disagreements inside the idealist camp (PROP-2026-07-08-002, PROP-2026-07-07-001); recommended for routing to the master agent as a paradigm-shift candidate.
  Type: epistemic (content-level claim about the tracked traditions themselves)
  Related decisions: none
  Related items: PRESUMPTION-477 (today — capture-sufficiency for the reclassification); the pending Kastrup↔Levin paradigm-shift candidate (in pending/, unadjudicated since 07-08)
  Testability: testable via literature — primary sources: Kastrup's dissociation-based individuation (alters of mind-at-large), Hoffman's conscious-agent composition theorems, Levin's nested/multi-scale selves; do the mereologies actually contradict, or operate at different levels of description?
  Status: CONTESTED (MONITOR-438 via DISPOSITION-467, 2026-07-13 — 15a SUPPORTED the reclassification away from "agreement" (Hoffman/Fields compose, Levin nests, Kastrup dissociates), but 15b found Kastrup affirms SUB-ALTERS and a "dissociative hierarchy": his alters DO nest. Correct label is "CONTESTED — priority dispute" (what is ontologically fundamental), not "incompatible mereologies." Paradigm-shift routing BLOCKED pending REVISE-214 primary-text verification.)
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a/15b -> 15c -> 14a]
    Original item: ASSUMPTION-449
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from sewing_agent_log.md 2026-07-12, "Worth Tom's attention" item 1 and the kastrup_levin / hoffman_kastrup bridge-note summaries, exact quotes. [stated]
    Current status: CONTESTED

ASSUMPTION-450:
  Date identified: 2026-07-12
  Statement: "active inference has no fatigue term and cannot obviously derive why a well-fitted model degrades once its goal is met (Levin's noise-free simulation does). If that holds, aging is evidence about FEP rather than an application of it."
  Context: c2a2-sewing-agent-weekly run, 2026-07-12 — headline finding #2, the reverse-direction claim behind the recommended promotion of friston_levin_bridge.md (8.2KB, four claims) to a standalone synthesis page.
  Type: epistemic (content-level claim about a tracked tradition's explanatory reach)
  Related decisions: none
  Related items: the Levin×Friston promotion recommendation (2nd consecutive week); PRS candidate "aging as precision decay"
  Testability: testable via literature — does the FEP corpus contain resources for endogenous model degradation (precision decay, entropic drift of generative models, "wear" terms in expected free energy)? A found fatigue-analogue defeats the claim; a confirmed absence elevates it.
  Status: CHALLENGED (REVISE-212 via DISPOSITION-468, 2026-07-13 — the absence holds for FEP's core formalism, but the first clause ("no fatigue term") is false as stated: allostatic-load/precision-decay treatments (Stephan et al. 2016) supply the analogue. The reverse-direction framing survives only in restricted form.)
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a/15b -> 15c -> 14a]
    Original item: ASSUMPTION-450
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from sewing_agent_log.md 2026-07-12, "Worth Tom's attention" item 2, exact quote. [stated]
    Current status: CHALLENGED

ASSUMPTION-451:
  Date identified: 2026-07-12
  Statement: "qc_sweep.py report now returns 0 across the board (keys on newest pair timestamp) — manual staleness scan is the sole work source now." The stated diagnosis (keying on the newest pair's timestamp) and the stated consequence (the scripted staleness instrument is fully blind) are both asserted from a single day's observation.
  Context: Summa QC sweep, 2026-07-12 — new finding reported in the evening cowork summary while the sweep serviced the 6 oldest stale pairs from the manual scan.
  Type: empirical
  Related decisions: none
  Related items: ASSUMPTION-441 (instrument disagreement, CONTESTED — MONITOR-432); ASSUMPTION-442 (degraded-mode QC, CHALLENGED — REVISE-206); the queued qc_sweep script fix
  Testability: testable empirically — read the report code path; construct a fixture with one fresh and one stale pair and confirm the report keys on the newest timestamp; distinct from (and prior to) the MONITOR-432 adjudication sample.
  Status: CONTESTED (MONITOR-439 via DISPOSITION-469, 2026-07-13 — 15a SUPPORTED (Strong; polarity/hazard class), 15b PARTIALLY-CHALLENGED. A two-pair fixture (one fresh, one stale) settles it; kin to MONITOR-432.)
  Provenance:
    Origin: 14a
    Chain: [14a -> 15a/15b -> 15c -> 14a]
    Original item: ASSUMPTION-451
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-12 evening cowork summary's Summa QC finding, exact quote. [stated]
    Current status: CONTESTED

ASSUMPTION-452:
  Date identified: 2026-07-13
  Statement: "ONE convention, three layers — NO SELF-PRODUCED ARTIFACT MAY CERTIFY ITSELF. Tooling fixes confirmed by REPLAY (REVISE-213); denominators by INDEPENDENT CORROBORATION (REVISE-209, already flagged); captures by PRIMARY-TEXT VERIFICATION (REVISE-214). Three flags, one rule. Adopt it once rather than patching three times." Stated: the three flagged instances share a single generative cause, and one convention — instantiated three ways — settles the whole family.
  Context: 15c dispositions, 2026-07-13 autonomous lit-search run (SYSTEMIC-RISK #1, CRITICAL, sixth consecutive flag in the open-loop family; now reaching the epistemic-input layer).
  Type: methodological
  Related decisions: none yet — this is the pipeline's own standing recommendation, awaiting Tom's adoption
  Related items: REVISE-209, REVISE-213, REVISE-214; ASSUMPTION-442/445 (CHALLENGED/CONTESTED); PRESUMPTION-471/473/476/477 (all CHALLENGED); ASSUMPTION-446 (MONITOR-436, subsumed)
  Testability: testable via literature — attestation/provenance doctrine (SLSA, supply-chain integrity), independent-verification efficacy across heterogeneous artifact classes; testable empirically — apply the three instantiations to the three open instances and measure whether any residue escapes the rule.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-452
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-13 15c SYSTEMIC-RISK #1 recommendation, exact quote. [stated]
    Current status: UNTESTED

ASSUMPTION-453:
  Date identified: 2026-07-13
  Statement: Both connectivity claims (ASSUMPTION-447, ASSUMPTION-448) "hinge entirely on whether retrieval is traversal- or embedding-based" — determining the vault's retrieval mode is stated to settle both at once. Secondary stated test: "BFS reachability of the 45 bridge notes from the top-20 hub set at depths 1-3."
  Context: 15c dispositions, 2026-07-13 — SYSTEMIC-RISK #2 (High): a shared, unexamined dependency beneath two independently-derived claims.
  Type: empirical
  Related decisions: none
  Related items: ASSUMPTION-447 (CONTESTED, MONITOR-437); ASSUMPTION-448 (CHALLENGED, REVISE-211); the 45 bridge notes from the weekly sewing agent
  Testability: testable empirically — read the retrieval path actually consumed by the thinker agents (traversal vs. embedding vs. hybrid), then run the BFS reachability test. This is an in-house determination requiring no literature.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-453
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-13 15c SYSTEMIC-RISK #2 flag and the DISPOSITION-465 "what would change the disposition" clause, exact quotes. [stated]
    Current status: UNTESTED

ASSUMPTION-454:
  Date identified: 2026-07-13
  Statement: "Two of the three output-verification checks in this watchdog's spec point at paths outside the mounted folders, so they can never pass." Stated: the scheduler watchdog carries a permanent, structural blind spot (Summa 2026 vault and BOSCO-Archive are unreachable from its sandbox), and the remedy is either to mount those folders or drop the rows from the spec.
  Context: Scheduler health check, 2026-07-13 — the watchdog reported 37/37 enabled tasks healthy while flagging that its own output-verification capability is 1-of-3.
  Type: methodological
  Related decisions: none
  Related items: PRESUMPTION-~ (firing-health-aggregates-to-system-health family, already CHALLENGED); PRESUMPTION-478 (today); the c282-wiki-agent output check, which the same family shows is unfalsifiable in practice
  Testability: testable empirically — inspect the task's sandbox mounts against the three verification paths; a one-line check settles it.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-454
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-13 scheduler health check "Action needed" paragraph, exact quote. [stated]
    Current status: UNTESTED

ASSUMPTION-455:
  Date identified: 2026-07-13
  Statement: "C2A2_master_wiki.md hasn't been written since 2026-07-09 despite daily 8 AM runs, and its network-state block (35 active findings, 222 PRS triplets, April-era pending list) conflicts with pattern_detector_findings.md, which now runs through FINDING-050." Stated further, as a method choice: "I reported the master's numbers in the footer but labeled them as of 07-09 rather than averaging the two sources."
  Context: Morning walk handoff, 2026-07-13 — no walk notes in Gmail; briefing built from wiki state alone, and the two counters were found in conflict.
  Type: empirical
  Related decisions: none
  Related items: OPEN-112 (PRS count discrepancy); REVISE-205 (census rule); the 50-vs-53 findings drift carried unreconciled since 07-11
  Testability: testable empirically — mtime of C2A2_master_wiki.md plus a diff of its network-state block against pattern_detector_findings.md; the daily-run task's own logs establish whether it fired and wrote nothing.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-455
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-13 morning walk handoff report, exact quotes. [stated]
    Current status: UNTESTED

ASSUMPTION-456:
  Date identified: 2026-07-14
  Statement: "All 34 enabled cron tasks have a lastRunAt within 1× their expected interval. No task is missing lastRunAt." Stated as the operative health criterion, the watchdog concluded "Healthy: 37 enabled tasks, all running on schedule ... Action needed: None — all clear." The stated assumption is that a task whose lastRunAt is current is a task that ran correctly.
  Context: Scheduler health check, 2026-07-14 — the watchdog reported 37/37 healthy on a day when four other scheduled tasks (c2a2-lit-search-pipeline, evening cowork→chat, morning walk handoff, deferred-action monitor) each fired and then crashed mid-response ("Connection closed mid-response"), producing no output. A mid-run crash still updates lastRunAt, so the criterion cannot see it.
  Type: methodological
  Related decisions: none
  Related items: ASSUMPTION-454 (the watchdog's unmounted-path blind spot, 07-13); the firing-health-aggregates-to-system-health family (already CHALLENGED); ASSUMPTION-459 (the .md fallback that the same crash defeated); PRESUMPTION-481, PRESUMPTION-483 (today)
  Testability: testable empirically — in-house, for one day compare the set of tasks with a current lastRunAt against the set that produced a valid, non-empty output artifact; today's four crashes are a ready sample where the two sets diverge.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-456
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-14 scheduler health check output, exact quotes, set against four mid-response crashes read directly in their transcripts. [stated]
    Current status: UNTESTED

ASSUMPTION-457:
  Date identified: 2026-07-14
  Statement: "ps inside the sandbox only sees sandbox processes, so sections 3–4 of the report describe the analysis environment, not macOS itself. The task asks for Mac process data that isn't reachable this way — I said so plainly rather than passing off sandbox processes as your Mac's." Stated: sandbox-visible process data is not a valid substitute for host process data, and the honest move is to disclose the scope gap rather than let the report imply coverage it does not have.
  Context: Morning system health, 2026-07-14 — the agent produced its report but explicitly bracketed the process-level sections as sandbox-only, and separately noted request_cowork_directory errored on ~/Documents ("overlaps a protected host location") though the mount already existed.
  Type: methodological
  Related decisions: none
  Related items: ASSUMPTION-454 and ASSUMPTION-455 (the 07-13 instrument-honesty pair — an agent disclosing the limits of its own reach); the firing-health family; the OpenStory-runtime-down-since-07-05 and metabolism-freshness failures the same report surfaced
  Testability: framework commitment on the honesty norm; the underlying scope claim is testable empirically — whether the sandbox's process table can or cannot enumerate host processes is a one-command check.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-457
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-14 morning system-health report and run-summary, exact quotes. [stated]
    Current status: UNTESTED

ASSUMPTION-458:
  Date identified: 2026-07-14
  Statement: "The .md file is the primary deliverable — it persists even if browser delivery fails." Stated in the evening cowork→chat task spec as the guarantee that the day's summary always survives: even when Chrome delivery is impossible, Step 2 writes a dated summary file to disk before Step 3 attempts to send.
  Context: Evening cowork→chat, 2026-07-14 — the run read the architecture files (Step 1) and then crashed mid-response ("Connection closed") before reaching Step 2, so no 2026-07-14 summary .md was written. The last file in daily_sync/cowork_to_chat is dated 2026-07-12; both 07-13 (quota) and 07-14 (mid-run crash) produced no file. The stated fallback presumes the failure lands at the delivery step; a crash before Step 2 defeats it.
  Type: architectural
  Related decisions: none
  Related items: ASSUMPTION-444 (sync-outage single-cause, CONTESTED); PRESUMPTION-478 (quota substrate), PRESUMPTION-479 (non-exclusive causes); PRESUMPTION-481 (crash-as-silent-no-op, today); REVISE-198/199 (both assume the channel can transmit)
  Testability: testable empirically — demonstrated CHALLENGED same day: the deliverable's persistence is contingent on execution reaching Step 2, which a mid-run crash does not guarantee; the fix (write the .md first, or checkpoint before any long-running read) is a design change, not a literature question.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-458
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the evening cowork→chat task spec's "Important Notes," set against the absent 07-14 output file. [stated]
    Current status: UNTESTED

ASSUMPTION-460:
  Date identified: 2026-07-15
  Statement: "the pending inbox has grown to 26 proposals, and the master wiki's last recorded run is 2026-07-09 — so the 07-10 → 07-14 deposits (a heavy Levin run) appear un-ingested. That Levin batch feeds directly into the FINDING-048 embedding-space ≡ FEP watch (FLAG-016)." Stated: the master-wiki ingestion lag now has a specific downstream epistemic consequence — five days of un-ingested deposits (including a heavy Levin batch) are exactly the evidence that would confirm or kill a live paradigm-shift watch, so the staleness is no longer only stale counters but a stalled evidence path into a flagged finding.
  Context: Morning walk cowork handoff, 2026-07-15 — no walk notes in Gmail; briefing built from wiki state alone. Network reported steady at 300 PRS triplets / 90 connections / 50 findings, with 6 flagged/paradigm-shift-watch items surfaced. The handoff escalated ASSUMPTION-455 (master silent since 07-09) from a counter-staleness observation to a claim about corrupted/starved evidence flow into FINDING-048 / FLAG-016.
  Type: architectural (with a methodological component: the ingestion path is a single point between deposits and every downstream reader, and its freshness is unverified)
  Related decisions: none
  Related items: ASSUMPTION-455 (master wiki stale since 07-09 — this is its escalation); the firing-health-aggregates-to-system-health family (a daily run that fires but writes nothing); PRESUMPTION-484 (today — flags presumed to reflect current evidence); OPEN-120 (today)
  Testability: testable empirically — in-house: confirm whether FINDING-048's evidence base actually depends on the 07-10→07-14 Levin deposits, and whether those deposits are in fact un-ingested (master-wiki mtime + a diff of its network-state block against pattern_detector_findings.md through FINDING-050). No literature needed to settle the factual half; literature only for whether a flagged watch should carry an evidence-freshness gate.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-460
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-15 morning walk cowork handoff report and its run-summary, exact quotes; no attended Cowork session occurred on 2026-07-15. [stated]
    Current status: UNTESTED

ASSUMPTION-461:
  Date identified: 2026-07-15
  Statement: The evening cowork→chat run failed with "API Error: Unable to connect to API (ConnectionRefused)" (nothing produced), and the c282 wiki agent daily run separately died with "API Error: Connection closed mid-response" after generating its review page. Stated: today's delivery-and-producer failures were infrastructure-connection errors — a signature distinct from both prior named causes in the sync-outage family (the Chrome/claude.ai login-out, still live on the morning scrape, and the 07-13 "out of usage credits"). The failure family now has at least three separate causes on the record and a fourth mode (mid-response crash) recurring.
  Context: 2026-07-15 autonomous day. Morning chat scrape: claude.ai logged out in Chrome (login outage continues). Evening cowork→chat: ConnectionRefused on the first turn. c282 wiki daily run: fired, generated a 26-proposal review page, then crashed mid-response. Morning project status nonetheless reported the fleet all-clear ("no issues to report") the same day a producer crashed — the standing self-certification pattern (ASSUMPTION-456) recurring.
  Type: architectural
  Related decisions: none
  Related items: ASSUMPTION-444 (sync-outage single-cause, CONTESTED — further contested here); ASSUMPTION-456 (firing ≠ valid output); PRESUMPTION-479 (failure modes not mutually exclusive); PRESUMPTION-481 (mid-run crash as silent no-op); PRESUMPTION-485 (today — closed-failure-taxonomy presumption)
  Testability: testable empirically — in-house: classify each of the day's crash tails by error string and by whether any artifact survived; the taxonomy is a direct read of the transcripts, not a literature question. Literature only for whether a bounded remedy set can ever close against an open failure population (see PRESUMPTION-485).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-461
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-15 evening cowork→chat, morning chat-scrape, and c282 wiki-agent transcripts, exact error strings. [stated]
    Current status: UNTESTED

ASSUMPTION-462:
  Date identified: 2026-07-16
  Statement: The c282 wiki agent daily run reported (Phase 5): "master narrative re-synced (flagged the 07-10→07-15 narrative gap)" and, in its readout, "review pages exist for 07-14 and 07-15, but the master wiki's 'Current status' line had not advanced past 07-09 ... My 07-16 entry re-syncs it." Stated: the master-wiki narrative pointer, silent since 07-09 (the ASSUMPTION-455/460 concern), was brought current today by prepending a 07-16 status line — the run treats the staleness as addressed at the narrative layer.
  Context: 2026-07-16 c282 wiki agent daily run (autonomous day #11). Orchestrator-only, clean run: Phase 0 no decisions, Phase 1 inbox clear / 0 truly-unprocessed / no triplets added, Phase 2 zero proposals (correct), Phase 3 26-proposal review page, Phase 5 cleanup + master narrative re-sync, Phase 5.5 review log refreshed. Network explicitly unchanged at 300 PRS / 90 connections / 50 findings — "frozen at 300/90/50 for two weeks because nothing has been approved."
  Type: architectural (a status-layer repair to the exact staleness A-455/A-460 flagged)
  Related decisions: none
  Related items: ASSUMPTION-455 (master silent since 07-09), ASSUMPTION-460 (staleness stalls FINDING-048 evidence), OPEN-120 (evidence-freshness gate); PRESUMPTION-486 (today — the re-sync advances the pointer, not the evidence)
  Testability: testable empirically — in-house: confirm the master wiki's "Current status" line now carries a 07-16 entry, AND separately confirm whether the 07-10→07-14 deposits are now ingested into the network-state block (they are not — Phase 1 added no triplets; network still 300/90/50). The two are decoupled and independently checkable.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-462
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-16 c282 wiki-agent daily-run transcript (Phase 5 line and readout), exact quotes. [stated]
    Current status: UNTESTED

ASSUMPTION-463:
  Date identified: 2026-07-16
  Statement: The c282 wiki agent daily run reported (Phase 6): "NOT committed/pushed from sandbox (mount blocks .git object writes — 'Operation not permitted'; the sandbox has no push credentials); a commit here would risk corrupting the object store ... Per the constitutional No-Blind-Push rule, I'm leaving everything staged for the Mac rather than blind-committing." Stated: the git-persistence step of the daily run cannot be completed from the autonomous sandbox — by hard constraint (read-only .git mount, no credentials) and by governance rule (No-Blind-Push) — so a run's outputs are staged, not persisted, and a human on the Mac is a required terminal actor to close the loop.
  Context: 2026-07-16 c282 wiki agent daily run. The staged set is dominated by a large pre-existing Summa vault-sync diff (470 files: 223 transcripts + 247 synthesis/refs, mostly last_qc_at timestamp bumps from a 07-10 QC pass) unrelated to this run; the community_explorer.html guard held. This is a distinct failure locus from the chat-sync family (A-444/A-461): not transmission to Chat but persistence to the durable store.
  Type: architectural (a fourth, by-design locus in the "autonomous run cannot self-complete" family — persistence, alongside the login/quota/connection transmission causes)
  Related decisions: none (invokes the standing constitutional No-Blind-Push rule)
  Related items: ASSUMPTION-461 (sync-outage causes — this adds a persistence-layer sibling), ASSUMPTION-456 (firing ≠ valid/complete output); PRESUMPTION-487 (today — an absent human makes "staged for the Mac" ≡ "never persisted"); PRESUMPTION-489 (today — shared working tree contamination)
  Testability: testable empirically — in-house: confirm the sandbox mount denies .git object writes and carries no push credentials; confirm the working tree currently holds the run's outputs plus the ~470-file Summa diff, uncommitted. No literature needed for the factual half; literature only for whether a credentialed durable-write path or a commit queue can preserve No-Blind-Push safety without a synchronous human.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-463
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-16 c282 wiki-agent daily-run Phase 6 assessment, exact quotes. [stated]
    Current status: UNTESTED

ASSUMPTION-464:
  Date identified: 2026-07-16
  Statement: The morning project status run reported the fleet all-clear — "all fired on schedule today ... No issues to report" — and OpenStory's "live database is healthy," while the same day's evening cowork→chat run reported "OpenStory is down an 11th day." Stated: a same-day, two-agent contradiction about one subsystem's health, with the all-clear resting on liveness ("fired on schedule") and a live DB probe, and the opposing verdict resting on the delivery/usability vantage. (Kin: BOSCO reported "100% complete, 30,529/30,529" with "a handful of attachments still pending enrichment" — a completion claim with an acknowledged residual.)
  Context: 2026-07-16 autonomous day #11. Morning project status: BOSCO 30,529/30,529, OpenStory "no longer at the old Projects path but database healthy," daily fleet all fired, "No issues to report." Evening cowork→chat: OpenStory down 11th day; review backlog 26 / 15-day gap. This is a fresh in-vivo instance of the liveness-as-success pattern the evening run named SYSTEMIC-RISK #4 (watchdog reads "fired" as "healthy").
  Type: architectural (instrument-health / self-certification family)
  Related decisions: none
  Related items: ASSUMPTION-456 (firing ≠ valid output / self-certification), SYSTEMIC-RISK #4 LIVENESS-AS-SUCCESS (evening 07-16 disposition run), PREMISE-096 (proposed self-certification terminator, INCORPORATE 07-16); PRESUMPTION-488 (today — "health" is vantage-relative, no reconciler); PRESUMPTION-483 (correlated green checks)
  Testability: testable empirically — in-house: place the morning "OpenStory healthy" and evening "OpenStory down 11 days" verdicts side by side and identify which signal each consumed (DB liveness vs. delivery/usability); check whether any fleet component reconciles two agents' contradictory same-day verdicts on one subsystem (none does). Literature: liveness vs. correctness in monitoring; the gap between "process is up" and "service is usable."
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-464
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-16 morning project status and evening cowork→chat transcripts, exact quotes set against each other. [stated]
    Current status: UNTESTED

ASSUMPTION-465:
  Date identified: 2026-07-17
  Statement: The c282 wiki daily run stated a new, more specific cause for the persistence failure than was on record: "Phase 6 is blocked: a stale 0-byte `.git/index.lock` (from an earlier process at 04:40) exists and the sandbox mount cannot remove it ('Operation not permitted'), which blocks all git writes." Stated: today's commit/push blocker is lock contention left by a concurrent earlier process, not (only) the mount denying `.git` object writes / missing push credentials cited on 07-16 (ASSUMPTION-463).
  Context: 2026-07-17 autonomous day #12. c282 daily run completed Phases 0–5.5 cleanly, then Phase 6 blocked. 791 files dirty in the working tree (this run's master-wiki + review_log.html plus pre-existing sewing/synthesis/vault-sync churn from other agents). This is a rationale-drift instance: the same standing symptom ("persistence cannot self-complete") is now attributed to a different proximate mechanism day-over-day (07-16: mount-denies-writes/no-creds → 07-17: unremovable stale index.lock from a 04:40 process). The two diagnoses imply different fixes (credentialed write path vs. lock hygiene / process serialization).
  Type: architectural (persistence / autonomous-run-cannot-self-complete family)
  Related decisions: none
  Related items: ASSUMPTION-463 (07-16 persistence blocker — mount/creds), PRESUMPTION-487/489 (absent-human push; shared working tree), PRESUMPTION-490 (today — execution-context parity), OPEN-121, REVISE-220/222/223 (07-17 lit dispositions), No-Blind-Push rule
  Testability: testable empirically — in-house: (a) confirm whether removing the stale `.git/index.lock` on the Mac clears Phase 6, isolating lock-contention from mount-permission as the operative cause today; (b) check whether the 04:40 process (which other scheduled run held the index?) can be serialized or given its own worktree so it cannot leave an orphan lock. Literature: git index.lock contention, concurrent-process file-lock orphaning, sandbox mount permission semantics.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-465
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-17 c282 wiki-agent daily-run transcript, exact quote of the Phase 6 block; compared against ASSUMPTION-463's 07-16 stated cause to record the drift. [stated]
    Current status: UNTESTED

ASSUMPTION-466:
  Date identified: 2026-07-17
  Statement: The metabolism regen run stated the failure cause explicitly: "The script resolves `~/` to the sandbox home, not the mounted Mac filesystem, so it cannot reach the live db from this scheduled (sandbox) context." Stated: the regen script was written on the assumption that `~/` (and thus the OpenStory db path) resolves to the Mac home directory — an assumption that holds in an attended Mac run but is false in the scheduled sandbox context, producing `ERROR: db not found: /sessions/.../OpenStory/data/open-story.db` (exit 1).
  Context: 2026-07-17 autonomous day #12. Metabolism regen FAILED for the second consecutive day. Two stacked problems: (1) the `~/` path assumption above; (2) even if the path resolved, the live `open-story.db` has not been written since Jul 5 (~12 days stale), so the >24h freshness gate would fail regardless — the OpenStory writer freeze is the deeper root cause.
  Type: architectural (execution-context / path-resolution)
  Related decisions: none
  Related items: ASSUMPTION-465 (git index.lock — sibling sandbox-context failure), PRESUMPTION-490 (today — execution-context parity, the general form), OpenStory writer-freeze (db unwritten since 07-05), the "autonomous run cannot self-complete" family, OPEN-122 (today)
  Testability: testable empirically — in-house: (a) run `metabolism_monitor.py --regen-only` on the Mac where `~/` resolves and confirm the regen succeeds, isolating path-resolution from the writer-freeze; (b) confirm the OpenStory writer has been idle since 07-05 and locate why it stopped. Fix candidate: make the script resolve the db path from an explicit configured/absolute mount path rather than `~/`. Literature: portable path resolution, HOME/env differences across execution contexts, cron/sandbox vs. interactive environment parity.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-466
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-17 metabolism regen transcript, exact quote of the `~/`-resolution diagnosis. [stated]
    Current status: UNTESTED

ASSUMPTION-467:
  Date identified: 2026-07-17
  Statement: The morning walk handoff stated a canonicity choice explicitly: "I used the maintained narrative network figure (300 PRS triplets) rather than the master's current-status line (447, the known-drifting per-file sum), per the standing flag in the wiki itself, and flagged the discrepancy in the briefing footer." Stated: the maintained 300-PRS figure is treated as the authoritative network state and the master current-status per-file sum (447 today) is treated as drift to be discounted — even though the same day's c282 run advanced the master narrative's current-status line to 447.
  Context: 2026-07-17 autonomous day #12. Network reported as 300 PRS / 90 connections / 50 findings (maintained, frozen since 07-09 with nothing approved). The c282 daily run's Phase 5 updated the master narrative header/date to 07-17 and its status line reads 447 PRS; the morning handoff used 300 and footnoted the 300-vs-447 gap. Two numbers for one network state, and two same-day agents each advanced a different one. Connects to the 07-16 narrative-freshness-vs-evidence-freshness family (ASSUMPTION-462 / PRESUMPTION-486) and the still-unreconciled OPEN-112 count discrepancy.
  Type: methodological (metric canonicity / instrument-reading)
  Related decisions: none
  Related items: ASSUMPTION-462 (07-16 narrative re-sync — pointer vs. referent), PRESUMPTION-486 (freshness-of-indicator ≠ freshness-of-evidence), OPEN-112 (unreconciled count discrepancy), OPEN-120, REVISE-221 (Goodhart/masking disposition, 07-17), the 50-vs-53 findings drift
  Testability: testable empirically — in-house: reconcile the two counts (which PRS are in the maintained 300 but not the per-file 447, and vice versa); decide and document a single canonical counter with a rule for when each is computed. Literature: metric drift, indicator/referent decoupling, Goodhart substitution, dual-bookkeeping reconciliation.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-467
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-17 morning walk cowork handoff transcript (explicit canonicity statement) cross-checked against the c282 daily-run Phase 5 narrative update. [stated]
    Current status: UNTESTED

ASSUMPTION-468:
  Date identified: 2026-07-18
  Statement: The c282 wiki daily run reclassified a recurring failure explicitly: "Auto-open is permanently broken, not flaky... Prior runs logged this as 'skipped'; it's a standing architectural gap. Serving `wiki/` over local HTTP and having the task navigate to `localhost:8080/review/...` would fix it — that's also what the constitutional review rule already assumes." Stated: the review page's auto-open step was designed on the assumption that a scheduled sandbox run can invoke a Mac-side file opener; that assumption is now declared false as a class, not intermittently.
  Context: 2026-07-18 autonomous day #13. Phase 3 generated the review page (29 proposals) but AUTO-OPEN FAILED. The run also names the downstream consequence: the constitutional review rule presumes the reviewer is actually shown the page, and the delivery leg has never worked from the scheduled context. Direct sibling of the sandbox-reach family codified same-day as PREMISE-098.
  Type: architectural (execution-context / delivery leg)
  Related decisions: none
  Related items: PREMISE-098 (2026-07-18 INCORPORATE — context invariants must be asserted, not presumed), ASSUMPTION-465/466 (07-17 sandbox-context failures), PRESUMPTION-490, OPEN-122, the 29-proposal review backlog
  Testability: testable empirically — in-house: stand up a local HTTP server over `wiki/` and have the task navigate to `localhost:8080/review/...`; confirm the page renders and that the reviewer-notification leg completes end-to-end from a scheduled run. Literature: headless/sandboxed execution context parity, delivery-leg failure in automated review workflows, "generated but never seen" artifacts.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-468
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-18 c282 wiki-agent daily-run transcript, exact quote of the Phase 3 reclassification; compared against prior runs' "skipped" logging to record the reclassification. [stated]
    Current status: UNTESTED

ASSUMPTION-469:
  Date identified: 2026-07-18
  Statement: The c282 wiki daily run self-reported an error with its rationale: "I published a bad draft and superseded it. The first Gmail draft (`r-7170316682122393624`) used the per-file PRS sum (448/52/51) rather than the maintained narrative counts (300/90/50) — the exact drift your own flag #3 warns about." Stated: the standing count-drift was being carried as a documented annotation on the assumption that a flagged discrepancy is safely deferrable; the run's own error shows the flag did not prevent the drifting number from being emitted to an outbound artifact.
  Context: 2026-07-18 autonomous day #13. This is ASSUMPTION-467 (metric canonicity, 07-17) materializing one day later as a published artifact rather than an internal disagreement. Note the per-file sum itself moved 447 → 448/52/51 overnight, so the non-canonical counter is also non-stationary. Network state remains 300/90/50 unchanged.
  Type: methodological (metric canonicity / flag efficacy)
  Related decisions: none
  Related items: ASSUMPTION-467 (07-17 canonicity split), REVISE-226 (07-18 disposition — define the canonical rule first), OPEN-112 (unreconciled count discrepancy), PRESUMPTION-494 (today — counts as properties of readings), the 50-vs-53 findings drift
  Testability: testable empirically — in-house: (a) reconcile 300 vs 448 and record which PRS are in one set and not the other; (b) decide a single canonical counter and a rule for when each is computed; (c) test whether a "known-drift flag" ever blocks emission, or only annotates it. Literature: annotation-vs-enforcement in data quality, known-error registers, Goodhart substitution, dual-bookkeeping reconciliation.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-469
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-18 c282 wiki-agent daily-run transcript, exact quote of the self-reported bad draft; cross-checked against ASSUMPTION-467 and the 07-18 lit disposition REVISE-226. [stated]
    Current status: UNTESTED

ASSUMPTION-470:
  Date identified: 2026-07-18
  Statement: The Saturday Wolfram agent stated two evidential decisions explicitly: "The 30-day window came up empty of primary material... So I relaxed to the filter's second clause ('a significant work not yet captured') and took the June 3 History Q&A, which is 45 days old but genuinely uncaptured"; and "The transcript was blocked. The official PDF is linked from the livestreams page but the fetch provenance guard refused it, so the PRS candidates rest on Wolfram's own published segment titles and timestamps rather than transcript text. I labeled both Medium and put a Retrieval Note in the proposal rather than upgrading on inference." Stated: publisher-supplied segment metadata is treated as adequate evidential ground for Medium-confidence PRS candidates when primary text is unavailable, and confidence-downgrading is treated as the correct instrument for that gap.
  Context: 2026-07-18 autonomous day #13. PROP-2026-07-18-001 (History of Science and Technology Q&A, 2026-06-03), two PRS candidates, both Medium. Matched to the open CROSS question "Does Wolfram Physics meet Carroll's Bayesian theory-confirmation standard?" (`cross_program_index.md` L198) as "a partial, non-empirical response," and flagged as "a strong MacIntyre-adjacent tradition-formation signal." The agent recommends "a verification pass on segment 1 before ingestion."
  Type: epistemic (evidential sufficiency / retrieval-mode)
  Related decisions: none
  Related items: ASSUMPTION-453 (retrieval-mode determination — one in-house test discharges two flags), REVISE-214 (Hoffman-sides-with-Levin BLOCKED pending primary-text verification), PRESUMPTION-497 (today — metadata as evidentially continuous with text), FLAG family on fetch-provenance guards
  Testability: testable via literature and empirically — in-house: obtain the June 3 transcript by a permitted route and score whether the two segment-title-derived PRS candidates survive contact with the text; separately, test whether the provenance guard is discriminating on domain or on actual provenance, since it refused an official PDF linked from the publisher's own page. Literature: metadata-only evidence extraction, title/abstract vs full-text agreement rates in systematic review screening, confidence calibration under partial retrieval.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-470
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-18 C2A2 Saturday Wolfram agent transcript, exact quotes of the filter-relaxation and retrieval-blocked rationales. [stated]
    Current status: UNTESTED

ASSUMPTION-471:
  Date identified: 2026-07-18
  Statement: The morning system health run stated a newly-invalidated precondition: "the task's Step 1 `request_cowork_directory` call on `~/Documents` now errors — the path overlaps a protected location (`Claude/Scheduled`). Documents was already mounted so the run completed, but that step will keep erroring until the task file is adjusted." Stated: the task spec was written on the assumption that a broad `~/Documents` grant would remain requestable; a platform-side protected-path rule now makes that request permanently fail, and the run only completed because a pre-existing mount masked the failure.
  Context: 2026-07-18 autonomous day #13. Same run reported: metabolism auto-publish stalled (last run 07-12 failed the freshness guard at 255h; "nothing has published in ~2.5 weeks"), OpenStory agent feeds "fifth straight FAIL," `summa_index.json` missing Day-001 and Day-035 syntheses, and five SRC files unsynced "because `sync_vault.sh` only rsyncs `transcripts/` and `synthesis/`." Machine itself idle and healthy (4 cores, 3.6 GB free, no swap, volume 40% full).
  Type: architectural (platform contract / precondition drift)
  Related decisions: none
  Related items: PREMISE-098 (context invariants asserted at startup), ASSUMPTION-466 (`~/` resolution), OPEN-122 (execution-context parity), PRESUMPTION-499 (today — failure independence)
  Testability: testable empirically — in-house: adjust the task file to request a non-overlapping path and confirm Step 1 succeeds without relying on a pre-existing mount; then re-run with the mount absent to confirm the step is genuinely load-bearing. Literature: silent-masking of failed preconditions by ambient state, platform permission-model drift breaking stored automation specs.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-471
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-18 morning system health transcript, exact quote of the protected-path error and the masking note. [stated]
    Current status: UNTESTED

ASSUMPTION-472:
  Date identified: 2026-07-18
  Statement: The scheduler health check stated its own evidential principle and then its own blind spot: "`lastRunAt` is authoritative for whether a task *fired*. Output file dates are a secondary check for whether it *succeeded*"; and "two of the three output checks in this watchdog's spec point at paths outside the session's mounts, so they can never actually run. Either mount those folders for this task or drop the checks from the spec so they stop reading as silently passing." Of `summa-2026-daily-batch` it recorded: "**Could not verify output**... Not a failure signal, a blind spot." Stated: the watchdog's green verdict ("✅ Scheduler healthy — all 36 enabled cron tasks running on schedule") is explicitly a liveness claim, not a correctness claim, and two thirds of its correctness checks are structurally inoperable.
  Context: 2026-07-18 autonomous day #13. Same day, the fleet-wide report from another scheduled run said "Forty-one scheduled tasks are active, and everything due overnight fired on time" while two pipelines (metabolism auto-publish, OpenStory feeds) had been failing for ~2.5 weeks and 6 days respectively. This is the fired-vs-succeeded gap named in MONITOR-448 appearing with the watchdog itself already aware of it and unable to close it.
  Type: epistemic (liveness vs correctness / instrument scope)
  Related decisions: none
  Related items: MONITOR-448 (07-18 disposition — "scheduler fired ≡ succeeded" watched pending artifact-binding), PRESUMPTION-491 (07-17), SYSTEMIC-RISK (High): no fleet green/current/done/healthy signal bound to its referent, ASSUMPTION-464, PRESUMPTION-488
  Testability: testable empirically — in-house: mount the two unreachable paths for this task (or delete the checks) and re-run; measure how many of the 36 "healthy" tasks pass an actual artifact-freshness check rather than a `lastRunAt` check. Literature: liveness vs safety properties in monitoring, heartbeat-only health checks and their false-green rate, observability blind spots in supervisory systems.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-472
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-18 scheduler health check transcript, exact quotes of the authority principle and the unrunnable-checks recommendation; cross-checked against the same-day morning project status fleet claim. [stated]
    Current status: UNTESTED

ASSUMPTION-473:
  Date identified: 2026-07-18
  Statement: Agent 16 (deferred action monitor) stated a size problem and a deferral rationale together: "watch_list.md has outgrown itself. It's at 2,820 lines / ~202 KB, and the operational content (active items + resolved index) is roughly 35 lines of that. The rest is ~90 days of run log growing ~35 lines/day, and every run reads the whole file"; and "I flagged it rather than doing it — restructuring your files isn't mine to decide unilaterally, and it's cheap to defer." Stated: deferral of a self-diagnosed maintenance problem is assumed to be low-cost, on day 13 of an unattended stretch with an 18-day review gap.
  Context: 2026-07-18 autonomous day #13. Agent 16 otherwise reported clean steady state: `needs_review/` holding only the already-tracked WATCH-001 tombstone, zero active WATCHING items, nothing due, channels 2 and 3 operational and empty. It also reported `pending/` at 27 proposals against the c282 run's same-day 29. The `generate_review_page.py` position-based decision-ID bug (~line 304) remains open.
  Type: normative / methodological (deferral cost, agent authority boundary)
  Related decisions: none
  Related items: PRESUMPTION-493 (07-17 — fail-loud presumes a listener), PRESUMPTION-496 (today — deferral presumes a decider), PRESUMPTION-498 (today — read-whole-file registries at scale), the 29/27 proposal-count split, the 18-day review gap
  Testability: testable empirically — in-house: measure the per-run read cost of `watch_list.md` and project it forward at ~35 lines/day; separately, count how many self-diagnosed deferrable items have accumulated since 07-05 and how many have been actioned. Literature: unbounded append-only operational logs, deferral cost under absent decision authority, agent autonomy boundaries and maintenance debt.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-473
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-18 C2A2 deferred-action-monitor transcript, exact quotes of the file-size finding and the deferral rationale. [stated]
    Current status: UNTESTED

ASSUMPTION-474:
  Date identified: 2026-07-19
  Statement: The sewing agent stated that the vault census series measures the wrong thing and that its own week-over-week delta is largely definitional: "My resolver lands within 1 file of the bootstrap's, so the apparent +225 jump mixes ~+145 real growth with ~+80 of definitional difference. The series needs a break-marker or one resolver fixed in code and the series re-derived." The bootstrap audit stated the substantive version the same day: "The +144-orphans-per-week headline is mostly an artifact. `architecture/lit_search_results/` and `architecture/daily_sync/` now hold 1,951 .md files — about 70% of the total orphan count. Excluding them is one line of resolver config and would make the series measure graph health instead of machine-dump volume. That needs your sign-off, so I've flagged it rather than changed it." Measured both ways: 3,483 pages / 2,759 orphans full, versus 1,532 / 808 excluding the machine dumps.
  Context: 2026-07-19, autonomous day #14. Fourth consecutive week this exclusion has been flagged and not acted on. The machine dumps in question are this pipeline's own outputs — `lit_search_results/` is written by 15a/15b, `daily_sync/` by the chat-sync agents.
  Type: methodological / empirical (metric definition)
  Related decisions: none
  Related items: PRESUMPTION-501 (today — definitional stability presumed across instruments), PRESUMPTION-498 (07-18 — registry scaling), OPEN-127 (today), OPEN-124, ASSUMPTION-469
  Testability: testable empirically — in-house: apply the one-line exclusion, re-derive the full series with a break-marker, and check whether the connectivity trend reverses sign; separately, run both resolvers over an identical snapshot to isolate the definitional component exactly rather than estimating it at ~80 files. Literature: index definition changes and time-series comparability, break-marker conventions in official statistics, Goodhart effects when an artifact count is used as a health proxy.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-474
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 sewing agent weekly and wiki bootstrap audit transcripts, exact quotes of the resolver-drift and exclusion statements; the two censuses' numbers recorded as given. [stated]
    Current status: UNTESTED

ASSUMPTION-475:
  Date identified: 2026-07-19
  Statement: The sewing agent stated an argument from the corpus against a C2A2 design assumption: "Levin's virtual-governor paper argues that forcing parts into complete agreement destroys the local optimization that made the collective intelligent. If that holds, scoring inter-tradition dialogue on convergence measures the detector damaging its own signal." The stated consequence: Rung-2 should not be scored on convergence; the success signature would instead be increased mutual registration with preserved local optimization — "participants who can state a rival position accurately while continuing to argue from their own." The stated instrumentation gap: "is there a measurable proxy distinguishing a participant who has *understood* a rival position from one who has *adopted* it? Without it the constraint is unenforceable."
  Context: 2026-07-19, autonomous day #14, raised from the 07-13 Levin alignment/virtual-governor proposal during the weekly sewing pass and forwarded as the "walk-worthy" item for morning discussion. This is the first time in this registry that the accelerator's own scoring criterion has been challenged by material the accelerator collected — a self-referential result of the kind 14a is instructed to watch for.
  Type: architectural / epistemic (success criterion for the detector)
  Related decisions: none — the convergence criterion has never been written as a decision, which is part of what makes this hard to contest
  Related items: PRESUMPTION-500 (today — convergence presumed to be the success signature), OPEN-125 (today), the Rung-2 detector design, PRESUMPTION-390 / MONITOR-375
  Testability: testable via literature and empirically — literature: over-alignment and diversity collapse in collective intelligence, ensemble diversity vs accuracy, groupthink and premature consensus, measures distinguishing comprehension of a position from endorsement of it (e.g. ideological Turing test, perspective-taking measures, steelman accuracy scoring). In-house: score an existing dialogue both ways and check whether the rankings diverge.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-475
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 sewing agent weekly transcript and the same day's cowork→chat summary, exact quotes of the over-alignment argument, the proposed success signature and the stated instrumentation gap. [stated]
    Current status: UNTESTED

ASSUMPTION-476:
  Date identified: 2026-07-19
  Statement: Agent 15d stated that its own staleness detector loses sensitivity exactly as the condition it detects worsens: "'No stale items this run' is an artifact, not a finding. Cycle counts only advance on a *completed* search pass, and staleness keys on cycle count — so the 67 frozen items can't accrue cycles while the queue is unconsumed. The longer consumption stalls, the less able the staleness detector is to report it." It stated the remedy and declined to implement it: "I recommend a wall-clock companion rule but did not implement one; that's a design decision, not 15d bookkeeping."
  Context: 2026-07-19 weekly periodic monitor. Same run: 21 items re-queued, 67 carried, 3 escalations, 452 MONITOR ids reconciled; backlog now 147 unsearched (110 last week — it grew), seventh consecutive surfacing, and "zero 15a/15b consumption of monitored items in 11 days." MONITOR-420's auto-escalate trigger fired on schedule.
  Type: methodological / epistemic (detector sensitivity coupled to the failure it detects)
  Related decisions: none
  Related items: PRESUMPTION-505 (today — detectors presumed to degrade gracefully rather than invert), ASSUMPTION-472 (07-18 — watchdog checks reading as green because unrunnable), PRESUMPTION-495, MONITOR-420, MONITOR-423
  Testability: testable empirically — in-house: add the wall-clock companion rule and re-run 15d over the current queue; count how many of the 67 carried items become stale under wall-clock that are invisible under cycle count. Literature: monitor coverage under load, silent-failure modes in liveness detectors, metrics whose sensitivity is conditioned on the process they monitor.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-476
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 C2A2 periodic monitor weekly transcript, exact quotes of the artifact-not-a-finding statement and the declined remedy. [stated]
    Current status: UNTESTED

ASSUMPTION-477:
  Date identified: 2026-07-19
  Statement: The lit pipeline stated that a property previously claimed for its design became structurally enforced for the first time today: "15b was blocked from reading 15a's output, which is the first run where that independence was structural rather than asserted." Implied and now stated: every prior 15a/15b independence claim in this registry rested on assertion, not on enforcement.
  Context: 2026-07-19 lit run over the 07-18 EOD batch of 12 items — 6 INCORPORATE (PREMISE-099–104), 4 MONITOR (MONITOR-449–452), 4 REVISE (REVISE-229–232). The independence of the for/against searches is the load-bearing property of the whole 15a/15b design; all dispositions before today were produced under the asserted version.
  Type: methodological / epistemic (adversarial independence)
  Related decisions: none
  Related items: PRESUMPTION-502 (today), the full DISPOSITION series to date, the 905 for/against pairs on record
  Testability: testable empirically — in-house: re-run a sample of pre-07-19 dispositions under structural blocking and measure whether 15b's challenge strength changes; that difference estimates the contamination in the existing record. Literature: independence assumptions in adversarial evaluation, anchoring between paired reviewers, blinding protocols in systematic review.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-477
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 C2A2 lit-search pipeline transcript, exact quote. [stated]
    Current status: UNTESTED

ASSUMPTION-478:
  Date identified: 2026-07-19
  Statement: The lit pipeline stated, under fail-loud, that two of its governing constraints are arithmetically inconsistent with its own scope. On the backlog: "147 queue items remain unsearched... I scoped to the fresh batch only, as the task file specifies... Processing 12 while leaving 147 makes today the fourth [day of deliberate non-processing]. The backlog is not a pipeline-capacity problem you can solve by running this task more often; at ~12 items per run against a daily enqueue rate, it never drains." On budget: "Token budget breached. Per-session budget is 30,000; this run consumed roughly 190,000... the budget and the pipeline's scope are inconsistent, and one of them needs revising."
  Context: 2026-07-19, autonomous day #14. Fourth consecutive day of the same deferral, now with the non-drainage stated as arithmetic rather than as a backlog. The Sunday tradition agent breached the same 30,000-token session budget in the same day on full-page fetches. This pipeline (14a/14b) also breached it on this run.
  Type: methodological / architectural (throughput and budget consistency)
  Related decisions: none
  Related items: PRESUMPTION-504 (today — a routinely and openly violated constraint presumed still to be a constraint), PRESUMPTION-495, PRESUMPTION-492, REVISE-227, OPEN-123, MONITOR-420
  Testability: testable empirically — in-house: measure enqueue rate against drain rate over the last 14 days and compute the steady-state queue length; separately, measure the actual token cost of a full-coverage run to establish what a consistent budget would have to be. Literature: queueing theory / arrival-vs-service-rate stability conditions, admission control, backlog-bounding policies (TTL, aging, fan-out caps).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-478
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 C2A2 lit-search pipeline transcript, exact quotes of the two fail-loud breach statements; cross-checked against the same-day Sunday tradition agent budget breach. [stated]
    Current status: UNTESTED

ASSUMPTION-479:
  Date identified: 2026-07-19
  Statement: 15c raised a High systemic-risk flag against the pipeline's own output — REVISE-231, spanning 7 of the day's 12 items: "the observations are well evidenced but the proposed remedies are unvalidated against the actual mechanism when a cheap discriminating test exists." On ASSUMPTION-468 specifically: "the localhost fix has a documented failure mode (socket-layer EPERM in sandboxed runtimes) and a one-line test that would kill it before any server gets built. Three of the remedies also push more signal into a channel with demonstrated zero throughput."
  Context: 2026-07-19 lit run. Stated: the pipeline reliably produces well-evidenced observations attached to untested remedies, and some of those remedies route more output into the review queue that is already the identified bottleneck — a remedy whose own success condition is the thing that is failing.
  Type: methodological (remedy validation) / architectural (output routing)
  Related decisions: none
  Related items: REVISE-231, ASSUMPTION-468, PRESUMPTION-502 (today), PRESUMPTION-493, PRESUMPTION-496, OPEN-123
  Testability: testable empirically — in-house: run the one-line EPERM test before building any localhost server, and audit all standing REVISE items for whether their remedy targets a mechanism that has been discriminated from its rivals; count how many remedies terminate in the zero-throughput channel. Literature: diagnosis before repair, cheap discriminating tests in fault isolation, remedy-validation gaps in incident postmortems.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-479
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 C2A2 lit-search pipeline transcript, exact quotes of the REVISE-231 systemic-risk statement and its A-468 instance. [stated]
    Current status: UNTESTED

ASSUMPTION-480:
  Date identified: 2026-07-19
  Statement: The morning project status run stated, as fact, the inverse of four other agents' same-morning findings: "OpenStory's database is live and the daily metabolism and telemetry refreshes both ran clean this morning," and "today's C2A2 runs... all completed on schedule... No failures to report." On the same morning the OpenStory telemetry refresh recorded its seventh consecutive failure, metabolism regen its roughly twelfth, metabolism monitor weekly a failed `quick_check` on a 4.46 GB database, and the weekly backup a hard failure with the H drive unmounted.
  Context: 2026-07-19, autonomous day #14. This is an escalation of the ASSUMPTION-469 / PRESUMPTION-494 family: on 07-18 four counters disagreed; today a summarizing agent asserted the negation of four concurrent failure reports, and the claim was delivered to Tom as a voice summary — an outbound artifact, as with the 07-18 Gmail draft. No mechanism checked the summary against the artifacts it summarized.
  Type: epistemic (summary claim not bound to its evidence)
  Related decisions: none
  Related items: PRESUMPTION-503 (today — summarizers presumed to read what they summarize), ASSUMPTION-469 (07-18 bad outbound draft), ASSUMPTION-472 (07-18 watchdog liveness-only), PRESUMPTION-494, OPEN-124, SYSTEMIC-RISK (High): no fleet green/current/done/healthy signal bound to its referent
  Testability: testable empirically — in-house: trace which sources the morning project status run actually reads and check whether the failing agents' outputs are among them; then bind each health claim to a named artifact with a freshness bound and re-run. Literature: reporting-layer decoupling in monitoring stacks, false-green rates in summary dashboards, provenance binding for derived claims.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-480
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 morning project status transcript, exact quotes; cross-checked against the same-morning OpenStory telemetry refresh, metabolism regen daily, metabolism monitor weekly and weekly backup transcripts. [stated]
    Current status: UNTESTED

ASSUMPTION-481:
  Date identified: 2026-07-19
  Statement: The connector health weekly run retracted its own prior week's explanation and then stated the limit of its instrument. Retraction: "Last week's brief framed the missing 7-day signal as a monthly-vs-weekly mismatch. That was too charitable." On the cost tracker: newest file is `cost-report-2026-03.md` — "April, May, June and July never got written. The task exists in `Scheduled/`, so it's failing rather than absent." On its own scope: "Enumeration has now failed four consecutive weeks... Everything above is fallback classification... this brief cannot detect a genuinely uninstalled connector except by absence from a tool list," and therefore "with enumeration broken those are indistinguishable, so I made no 'installed count dropped' claim rather than guess."
  Context: 2026-07-19. Four connector buckets unchanged (2 active / 19 dormant / 0 suspect / 4 orphaned); supabase and claude-in-chrome in their fourth week of wiring. Notable as the fleet's cleanest instance of an agent declining to infer past its instrument — the opposite of the same-day ASSUMPTION-480 — and as a documented rationale drift caught by the drifting agent itself.
  Type: epistemic (instrument scope, refusal to infer) / methodological (rationale drift)
  Related decisions: none
  Related items: ASSUMPTION-480 (today, the contrasting case), ASSUMPTION-472, PRESUMPTION-502 (today — the dropped handoff originated in this run), PRESUMPTION-482
  Testability: testable empirically — in-house: repair connector enumeration and compare four weeks of fallback classification against ground truth to measure the fallback's error rate; separately, check whether the cost-tracker task is firing and failing or silently absent. Literature: graceful degradation vs silent substitution in monitoring, explicit uncertainty reporting, self-correction rates in recurring automated reports.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-481
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 connector health weekly transcript, exact quotes of the retraction, the cost-tracker finding and the enumeration-scope statement. [stated]
    Current status: UNTESTED

ASSUMPTION-482:
  Date identified: 2026-07-20
  Statement: Agent 15c stated the pipeline's binding constraint in its own words: "The pipeline's dominant constraint this run is not evidence but measurement that nobody has taken." Eleven of fourteen dispositions turn on a discriminating test that has never been run, and 15c stated those reduce to roughly six distinct measurements, five of which cost under an hour each.
  Context: 2026-07-20, autonomous day #15. A consumption day: the 07-19 EOD batch of 14 items went 15a -> 15b -> 15c same-cycle, returning 6 INCORPORATE (PREMISE-105..110), 5 MONITOR (MONITOR-453..457), 3 REVISE plus 1 cross-item systemic REVISE (REVISE-233..236).
  Type: methodological
  Related decisions: none
  Related items: ASSUMPTION-479 -> PREMISE-107 (diagnose-before-repair with scope guard), PRESUMPTION-513 (today), REVISE-233, REVISE-234, REVISE-235
  Testability: testable empirically -- in-house, and cheaply: (1) enumerate the morning run's read set; (2) compare scheduled vs interactive wall clock; (3) re-derive four counts over one frozen snapshot; (4) search thirty days of recipients' outputs for flagged content; (5) rank-correlate three dialogue measures. Literature: measurement cost vs evidence cost in fault isolation; the diagnosis fraction of mean time to repair.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-482
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-20 lit-search pipeline (15c) disposition run, exact quote, cross-checked against the day's four REVISE flags and five MONITOR items. [stated]
    Current status: UNTESTED

ASSUMPTION-483:
  Date identified: 2026-07-20
  Statement: 15c stated, adjudicating ASSUMPTION-477, that "the read channel is not the dominant correlation source, and 2026-07-19 removed the weakest of at least four," and therefore that the correct response is to relabel rather than re-run: report the 07-19 change as "READ-CHANNEL INDEPENDENCE ENFORCED," never as "independence achieved," and do not discount or re-derive the 905-pair record on an unmeasured contamination assumption.
  Context: 2026-07-20, REVISE-233. The item came back 15a SUPPORTED/Strong against 15b CHALLENGED/Strong -- a direct conflict at equal strength. 15c refused to average, separated three propositions inside the item, and decided the contested one on source directness (van Rooyen et al., JAMA 1998, PMID 9676666, n=527, null; against McNutt 1990 at a quarter the size). Notable as the first recorded adjudication of an equal-strength cross-agent conflict.
  Type: architectural / epistemic
  Related decisions: none
  Related items: ASSUMPTION-477, REVISE-233, PRESUMPTION-508 (today), PREMISE-106
  Testability: testable empirically -- in-house: run 15a and 15b on the same item under full blocking and measure how often they cite the SAME sources; high overlap means shared pretraining, not file access, is the operative channel and the 07-19 fix addressed the wrong one. Separately, a clean blinding estimate: ~20 pre-07-19 items run twice in one session, one model version, one prompt, one corpus snapshot, with 15a's file readable then blocked. Literature: arXiv:2606.29270 (correlated LLM errors violating Condorcet independence), arXiv:2606.10296 (LLM judge over correlated inputs can yield negative net gain).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-483
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-20 REVISE-233 adjudication block, exact quotes of the operative finding and the recommended relabel. [stated]
    Current status: UNTESTED

ASSUMPTION-484:
  Date identified: 2026-07-20
  Statement: 15c stated a mechanism for how an honest abstention fails: "The abstention therefore republishes the disputed figure with the caveat quietly removed, while appearing to withhold it." The stated remedy is to report a directional bound instead -- "at least N installed; uninstalled connectors are undetectable under fallback, so the true count is N or higher" -- on the ground that numeric uncertainty costs little credibility while unquantified verbal uncertainty lowers trust in both the information and the source.
  Context: 2026-07-20, REVISE-234, dispositioning ASSUMPTION-481 (the connector-health weekly's refusal to state a count). The diagnosis half was judged INCORPORATE-ready pending a settled reporting convention; the endorsed abstention was not incorporated. This directly qualifies what was recorded on 07-19 as "the fleet's cleanest instance of an agent declining to infer past its instrument."
  Type: methodological / epistemic
  Related decisions: none
  Related items: ASSUMPTION-481, REVISE-234, PREMISE-105 (break-in-series, same fix applied to the four-week fallback record), PREMISE-110
  Testability: testable empirically -- in-house and immediate: inspect the next artifact that cites a connector count; if the pre-abstention fallback figure reappears uncaveated, the abstention failed in exactly the predicted way. Then repair enumeration and compare four weeks of fallback classification against ground truth to size the fallback error rate. Literature: van der Bles et al., PNAS 2020 (PMID 32205438); Royal Society Open Science 2023 (doi 10.1098/rsos.230604); belief-consistent processing of uncertainty statements.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-484
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-20 REVISE-234 block, exact quote of the republication mechanism and the recommended directional bound. [stated]
    Current status: UNTESTED

ASSUMPTION-485:
  Date identified: 2026-07-20
  Statement: On the accelerator's target function, 15c stated a constraint on remedies: "replacing a possibly-wrong objective with an unmeasurable one converts it into no objective." Therefore convergence must NOT be removed from Rung-2 scoring before a separable alternative exists, and the correct move is to state the criterion as a hypothesis in decisions.md while instrumenting both signatures and reporting the pair.
  Context: 2026-07-20, REVISE-235, urgency HIGH, dispositioning PRESUMPTION-500 -- flagged by 14b as "Critical -- this is the target function of the accelerator." Both 15a and 15b independently proposed MacIntyre's own criterion (can tradition A restate B's position in B's vocabulary AND identify B's unresolved epistemic crisis?) as an independent third measure.
  Type: methodological / architectural
  Related decisions: none (this is the flagged gap -- the target function has never been written into decisions.md)
  Related items: PRESUMPTION-500, ASSUMPTION-475 (the stated twin, MONITOR-453), REVISE-235, PRESUMPTION-509 (today)
  Testability: testable empirically -- in-house: score existing dialogues under (a) convergence, (b) mutual registration, (c) an ITT-style measure, and compute pairwise rank correlations; strong (b)-(a) correlation means the dichotomy is false. Mandatory pre-dialogue ITT baseline, since C2A2's tradition agents share a pretrained model and may produce a rival's arguments from pretraining rather than from registration acquired in dialogue. Literature: Lorenz et al., PNAS 2011 (convergence lowers accuracy while raising confidence); diversity prediction theorem; 2025-2026 results on LLM population homogenisation.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-485
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-20 REVISE-235 block, exact quote of the no-objective constraint and the six-step recommended action. [stated]
    Current status: UNTESTED

ASSUMPTION-486:
  Date identified: 2026-07-20
  Statement: In incorporating PRESUMPTION-502 as PREMISE-108, 15c stated an instrumentation constraint as load-bearing: "the measure of delivery is the flagged content APPEARING IN THE RECIPIENT'S OUTPUT, never an acknowledgement receipt. An acknowledgement makes 'acknowledged' measurable and leaves 'acted on' exactly as unmeasurable as before, installing a green metric over the unchanged failure."
  Context: 2026-07-20. Generalises PREMISE-102 (agent-to-human) to the agent-to-agent channel, at one confidence grade lower because the in-house evidence is a single traced instance and the strong external evidence (AHRQ/ACOG handoff, I-PASS read-back, FAA position relief) comes from synchronous human teams -- a transfer 15b showed to be unwarranted for the remedy though the diagnosis carries. The premise explicitly does NOT license any claim about how often delivery fails; the base rate has not been obtained.
  Type: methodological
  Related decisions: none
  Related items: PRESUMPTION-502 -> PREMISE-108, PREMISE-102, PRESUMPTION-506 (today), MONITOR-420
  Testability: testable empirically -- in-house, no protocol change required: enumerate the last thirty days of cross-agent flags and search each named recipient's subsequent output for the flagged content. This is one of the five measurements named in ASSUMPTION-482. Literature: closed-loop communication; responsibility diffusion in handoffs; proxy-metric substitution.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-486
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-20 PREMISE-108 instrumentation constraint, exact quote. [stated]
    Current status: UNTESTED

ASSUMPTION-487:
  Date identified: 2026-07-20
  Statement: The metabolism regen run stated its failure and its diagnosis without hedging: "FAILED -- do not mark this run successful," exit 1, `build_metabolism_view.py`'s `PRAGMA quick_check` failing with thousands of "Rowid ... out of order" B-tree errors. Two stated inferences: "The live db is not corruption-free -- the errors come from the point-in-time backup copy, so this is real on-disk corruption in `open-story.db`, not a mid-write artifact," and "The live db hasn't been written since 2026-07-05 23:55 -- 14.6 days stale. The OpenStory writer appears to have stopped, or is failing against the corrupt file." The same run stated a path caveat: the script resolves the db via `$HOME`, which in the sandbox is not the user's home; the failure above is from a corrected run, not a path problem.
  Context: 2026-07-20. Same failure as 2026-07-08, now roughly 13 consecutive days unresolved. Directly contradicted, same morning, by the morning project status claim that "OpenStory is alive: its telemetry refresh ran this morning and the metabolism snapshot regenerated on schedule" -- see ASSUMPTION-488 and PRESUMPTION-506.
  Type: empirical
  Related decisions: none
  Related items: ASSUMPTION-466 (07-17 sandbox $HOME resolution), PRESUMPTION-491 (schedule-fired = task-succeeded), PRESUMPTION-506 (today), PREMISE-109
  Testability: testable empirically -- Mac-side: `sqlite3 open-story.db "PRAGMA integrity_check"` directly, check whether the OpenStory writer process is alive, and attempt a `VACUUM INTO` rebuild to recover the B-tree. Literature: SQLite B-tree corruption causes; recovery from partial-write corruption.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-487
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-20 metabolism regen daily transcript, exact quotes of the failing lines and both stated inferences. [stated]
    Current status: UNTESTED

ASSUMPTION-488:
  Date identified: 2026-07-20
  Statement: The morning project status run stated, as fact, that "OpenStory is alive: its telemetry refresh ran this morning and the metabolism snapshot regenerated on schedule," that "roughly thirty-four scheduled agents are active... and all of yesterday's runs completed," and that "the BOSCO archive is fully indexed -- all 30,529 emails captured," qualified with "about 28,500 of those are still snippet-only, and the heartbeat task that enriches them... is currently disabled."
  Context: 2026-07-20, and the claim is affirmatively false in the OpenStory clause: the metabolism regen run the same day exited 1 and reported the db 14.6 days stale. This is the second consecutive occurrence of the identical contradiction (07-17 ASSUMPTION-464 family, 07-19 ASSUMPTION-480) -- and it occurred on the day PREMISE-109 was validated, which names exactly this failure. The "all of yesterday's runs completed" clause is separately contradicted by the reviewer-review weekly's finding of four months of silent cost-tracker write failure and a five-week gap in `weekly-agent-ecosystem-report`.
  Type: epistemic (summary claim not bound to its evidence)
  Related decisions: none
  Related items: ASSUMPTION-480 (07-19, same agent, same failure), ASSUMPTION-487 (today, the contradicting artifact), PRESUMPTION-491, PRESUMPTION-503 -> PREMISE-109, PRESUMPTION-506 (today), OPEN-124
  Testability: testable empirically -- in-house: enumerate the morning run's read set and check whether the metabolism regen transcript is in it; then bind each health claim to a named artifact with a freshness bound and re-run. This is measurement (1) of the five named in ASSUMPTION-482. Literature: covered by PREMISE-109; no further search needed on the general claim.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-488
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-20 morning project status transcript, exact quotes; cross-checked against the same-day metabolism regen daily and reviewer review weekly transcripts. [stated]
    Current status: UNTESTED

ASSUMPTION-489:
  Date identified: 2026-07-20
  Statement: The Summa 2026 nightly verification run stated that its own guardrail detector was defective and that the defect produced the violations it had reported: "The guardrail detector had a real bug. It only registered a thinker as 'cited' when PRS ids appeared in parentheses," so ten days citing a tradition file with a prose gloss and no id "looked like breaches." Of 13 first-pass metaphysical-guardrail violations, "11 were parser false positives and 2 were detector artifacts," leaving 0 genuine. A second detector defect remains open: "the locus regex is Summa-part-insensitive," firing Day 232 (III Q.39) against a Prima Pars range on one thematic word.
  Context: 2026-07-20. 307 synthesis files verified against the live wiki with both mounts present -- a real citation check, not form-only. 0 drift items, 8 authorship violations (all in the known possessive-PRS backlog). This is a detector that inverted in the opposite direction from PREMISE-110's family: it manufactured violations rather than manufacturing health. The reviewer-review weekly independently records two further self-caught measurement errors the same week (a 65-file frontmatter-extraction defect withdrawing 16 phantom violations; QC ratios computed against a hardcoded wrong denominator).
  Type: methodological / empirical
  Related decisions: none
  Related items: PRESUMPTION-505 -> PREMISE-110 (detectors invert), PRESUMPTION-511 (today), ASSUMPTION-490
  Testability: testable empirically -- in-house: tighten the locus regex for Summa part, re-run, and diff against tonight's result; separately, audit each remaining detector for the same class of pattern-match defect before trusting any violation count. Literature: false-positive rates in static-analysis and rule-based detectors; the effect of detector precision on reviewer trust and alert fatigue.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-489
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-20 Summa 2026 nightly verification transcript, exact quotes of both detector defects. [stated]
    Current status: UNTESTED

ASSUMPTION-490:
  Date identified: 2026-07-20
  Statement: Three counting disagreements were stated in one day within the Summa subsystem alone. The nightly verification: "I count 20 frontmatter tier mismatches where yesterday's pass found 15; the five extra... all sit within ~80 words of a tier boundary, so this is more likely a `## Notes`-stripping difference between passes than new drift -- it needs one reconciliation to settle." The reviewer-review weekly: "QC and verification disagree about tier mismatches -- QC says 5 (now zero, corrected); verification lists 15. Likely two different metrics, but the pending tier-calibration decision rests on whichever is right." And: the declared `length_actual_words` in the bottom-frontmatter cohort are inflated (Day 011 declares 2780 against a true body of ~2200-2317, masking a 0.77x under-run behind a stated 0.927 ratio).
  Context: 2026-07-20. This is the counting-authority problem (OPEN-112, OPEN-124, OPEN-127, PRESUMPTION-501) appearing in a subsystem where it had not previously been recorded, and the first case where a named pending decision -- tier calibration -- is explicitly stated to rest on the unresolved count. The evening sync separately flagged a possible sixth instance (mount-view disagreement on A-474..481 / P-500..505).
  Type: empirical / methodological
  Related decisions: none (tier calibration is pending and blocked on this)
  Related items: ASSUMPTION-467 (07-17, 300 vs 447), PRESUMPTION-501, PREMISE-105 (break-in-series), OPEN-112, OPEN-124, OPEN-127, OPEN-130 (today)
  Testability: testable empirically -- in-house: re-derive all three tier-mismatch counts over one frozen corpus snapshot with the `## Notes`-stripping rule stated explicitly, and repoint the writer's word-count step at the stripped body. This is measurement (3) of the five named in ASSUMPTION-482. Literature: covered by PREMISE-105; the reconciliation rule is the open item, not the diagnosis.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-490
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-20 Summa nightly verification and reviewer review weekly transcripts, exact quotes, read together. [stated]
    Current status: UNTESTED

ASSUMPTION-491:
  Date identified: 2026-07-20
  Statement: The reviewer-review weekly stated three findings as established rather than suspected. (1) "`agentic-cost-tracker` is genuinely broken. It ran today at 09:35, but `Reports/` still has nothing newer than `cost-report-2026-03.md`. Four months of silent write failure, now independently confirmed rather than inferred." (2) "The pending Stump PRS-09 repoint has the wrong target... Running the batch as recorded trades one wrong pointer for another. Needs your call before it executes." (3) "`weekly-agent-ecosystem-report` has produced no file for five weeks: its SKILL.md never tells it to write one. That's a one-line fix, not a broken agent."
  Context: 2026-07-20, week 5 brief, all 10 reviewers ran with no silent failures. Finding (1) is the first case in the record of a suspected failure being upgraded to confirmed by an independent reviewer rather than by the reporting agent itself -- a working instance of what PREMISE-109 asks for. Finding (3) locates a five-week silent gap in a specification rather than in execution. Finding (2) is a case where a memory record and the wiki disagree and the memory record is wrong; it is blocked pending Tom.
  Type: empirical / architectural
  Related decisions: none
  Related items: ASSUMPTION-481 (07-19, the cost-tracker finding in its inferred form), PRESUMPTION-503 -> PREMISE-109, PRESUMPTION-512 (today), ASSUMPTION-490
  Testability: testable empirically -- in-house and cheap: apply the one-line SKILL.md fix and confirm a file appears next cycle; for the cost tracker, capture its stderr/exit status rather than its scheduler firing record; for the Stump repoint, verify the intended PRS target against the wiki before execution. Literature: silent write failure detection; specification-vs-execution attribution in agent failures.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-491
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-20 reviewer review weekly transcript, exact quotes of all three findings. [stated]
    Current status: UNTESTED

ASSUMPTION-492:
  Date identified: 2026-07-21
  Statement: The three-week ingestion stall was a decision-source coverage gap, not an absent human. "Your Mac-side blanket approval of 2026-07-20 (34 proposals) had landed in `inbox/` but Phase 0 only reads Gmail, so it reported 'no decisions' while a full approval sat on disk. The inbox diff caught it. Worth fixing: Phase 0 should read `review/archive/*_decisions.md` as a second decision source."
  Context: 2026-07-21 C2A2 wiki daily run (autonomous day #16), Phase 0/1. Once the on-disk approval was read, ingest cleared: +64 PRS triplets across 10 traditions (Levin +24, Carroll +8, Wolfram +7, Friston +6, Kastrup +5, McGilchrist/Rohr/Wright +4, Hoffman/Stump +1); one of 34 correctly skipped as a re-capture. This reverses the standing reading (weeks of stall attributed to "absent human / no approvals") for at least this interval.
  Type: architectural / methodological
  Related decisions: none
  Related items: PRESUMPTION-487 (absent-human-push), PRESUMPTION-510, ASSUMPTION-482
  Testability: testable empirically -- add `review/archive/*_decisions.md` as a second Phase 0 source and confirm on-disk approvals are ingested without a Gmail round-trip; audit for other single-source read points. Literature: single-source-of-truth failure modes; decision-channel redundancy.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-492
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-21 C2A2 wiki daily run transcript, exact quote. [stated]
    Current status: UNTESTED

ASSUMPTION-493:
  Date identified: 2026-07-21
  Statement: The 300-series PRS total is stale and should be retired at source; the measured network figure is 511. "My first Gmail draft carried the stale 300-series PRS figure (364) instead of the measured 511. Delete draft r7940392808004593736. Two PRS totals are circulating in the narrative and a wrong number has now been caught in three consecutive morning emails -- the 300-series should be retired at source."
  Context: 2026-07-21 daily run, Phase 4 (email). Post-ingest network reported as 511 PRS triplets / 165 connections / 54 findings. This is the same canonical-vs-per-file drift tracked as OPEN-112 (300 canonical frozen vs 447 per-file on 07-17), now with a third circulating value (364 in the draft) and a fourth (511 measured) after ingestion.
  Type: empirical / methodological
  Related decisions: none
  Related items: OPEN-112 (PRS counting authority), ASSUMPTION-490 (three readings of one quantity), PRESUMPTION-507 (counting authority)
  Testability: testable empirically -- designate a single canonical PRS counter and confirm all outbound artifacts read from it; verify 511 against a per-file recount.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-493
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-21 C2A2 wiki daily run transcript, exact quote. [stated]
    Current status: UNTESTED

ASSUMPTION-494:
  Date identified: 2026-07-21
  Statement: The inbox-diff slug normalizer produces a systematic false positive by retaining the date prefix. "My first inbox diff reported 126 unprocessed -- false positive, my slug normalizer kept the date prefix. True figure was 33. Same error class as 07-19 and 07-20."
  Context: 2026-07-21 daily run, Phase 1. Third consecutive day the same normalizer error class has appeared and been caught in-run. Self-identified as a recurring, not novel, defect.
  Type: methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-489 (Summa parser false positives), PRESUMPTION-520 (errors-caught representativeness)
  Testability: testable empirically and cheaply -- normalize the date prefix out of the slug and unit-test the diff against a known-answer fixture; the recurrence across three days makes the fix's absence, not its correctness, the datum.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-494
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-21 C2A2 wiki daily run transcript, exact quote. [stated]
    Current status: UNTESTED

ASSUMPTION-495:
  Date identified: 2026-07-21
  Statement: FLAG-018 -- Levin's over-alignment failure mode implies that forcing a collective into complete agreement destroys the local optimization that made it intelligent; applied to C2A2, "consensus-seeking dialogue is a pathology, not success -- it cuts against any Rung-2 metric scoring convergence as progress, and invites re-reading your Rung-1 listening lift (+0.031) as coupling rather than convergence."
  Context: 2026-07-21 daily run, escalation FLAG-018, generated from ingested Levin material. Stated as bearing directly on the ISME measurement section. This is a design-level hypothesis with an explicit metric consequence, not merely a tradition finding.
  Type: architectural / epistemic / normative
  Related decisions: none (bears on any future Rung-2 metric decision)
  Related items: FLAG-017, PRESUMPTION-516 (finding-to-metric propagation), PRESUMPTION-509 (more = better)
  Testability: testable via literature (collective intelligence / over-alignment / diversity-maintains-optimization) and empirically (re-analyze the +0.031 listening lift as coupling vs convergence; specify a Rung-2 metric that scores maintained divergence rather than agreement).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-495
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-21 C2A2 wiki daily run transcript (FLAG-018), exact quote. [stated]
    Current status: UNTESTED

ASSUMPTION-496:
  Date identified: 2026-07-21
  Statement: FLAG-017 -- Levin's "virtual governor" may be Friston's group-level Markov blanket approached from the other side; "the equivalence test is stated and tractable, which is rare for these."
  Context: 2026-07-21 daily run, escalation FLAG-017, generated from ingested Levin material. A candidate structural homology between two tracked traditions (Levin, Friston) with a claimed tractable equivalence test -- the type of cross-connection the network is built to surface.
  Type: epistemic / architectural
  Related decisions: none
  Related items: FLAG-018, cross-connection registry, PRESUMPTION-523 (transfer conditions)
  Testability: testable via literature (Markov blanket formalism; Levin's collective-control constructs) and empirically (run the stated equivalence test).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-496
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-21 C2A2 wiki daily run transcript (FLAG-017), exact quote. [stated]
    Current status: UNTESTED

ASSUMPTION-497:
  Date identified: 2026-07-21
  Statement: Two 2026-07-19 proposals (Rohr PROP-2026-07-19-001, Wright PROP-2026-07-19-003) left the pipeline with no recorded disposition and no surviving file. "The likeliest reading is deliberate -- they're exactly the two items the 2026-07-19 sewing run flagged... The correspondence is too exact to be coincidence. But the record doesn't say so, and incidental loss during the bulk `pending/ -> approved/` move can't be excluded from the artifacts alone."
  Context: 2026-07-21 deferred-action monitor (Agent 16). Queue held 36 cards at review; archive records 34. Both missing items appear as cards in `2026-07-20_review.html`; neither exists in pending/approved/denied/needs_review/inbox. Tracked as WATCH-002 (Wright) and WATCH-003 (Rohr) with an INTEGRITY FLAG; content recoverable from the review page and live source URLs. Monitor did not restore files or record retroactive dispositions (outside remit).
  Type: empirical / methodological
  Related decisions: none
  Related items: ASSUMPTION-498 (position-ID bug as mechanism), PRESUMPTION-517 (recovery source integrity)
  Testability: testable empirically -- reconcile queue-at-review against decision archive by count and ID; determine whether the two IDs were deliberately withheld (sewing-run flags) or lost in the bulk move. Human action required to record retroactive dispositions or restore.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-497
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-21 deferred-action monitor transcript, exact quotes. [stated]
    Current status: UNTESTED

ASSUMPTION-498:
  Date identified: 2026-07-21
  Statement: The `generate_review_page.py` position-ID defect is now correctness-critical, not hypothetical. "In the 07-20 review page, card IDs and decision-button IDs are offset around the 07-19 items -- the buttons immediately preceding `card-PROP-2026-07-19-003` are wired to `PROP-2026-07-19-002`. A decision registered against one card can be recorded against a different proposal. That's a plausible mechanism for a silent two-item loss in a 36-item blanket pass, so I'd fix it before the next review pass."
  Context: 2026-07-21 deferred-action monitor (Agent 16), escalating a standing flag to confirmed with a concrete instance. Directly proposed as the mechanism for ASSUMPTION-497's two-item loss.
  Type: architectural / empirical
  Related decisions: none
  Related items: ASSUMPTION-497, PRESUMPTION-517
  Testability: testable empirically and cheaply -- diff card-id against decision-button target in the generated HTML; fix the offset and re-render before the next review pass.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-498
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-21 deferred-action monitor transcript, exact quote. [stated]
    Current status: UNTESTED

ASSUMPTION-499:
  Date identified: 2026-07-21
  Statement: The 15a/15b independence defect was measured in-run: run under full blocking, 15a and 15b still retrieved the same key sources on >=5 items -- the first quantitative datum the vault has on its 15a/15b correlation. Independence in this pipeline is asserted rather than engineered.
  Context: 2026-07-21 Agent 15c adjudication of the 18-item 07-19/07-20 batch (ASSUMPTION-482...491, PRESUMPTION-506...513) -> 11 INCORPORATE (PREMISE-111...121), 5 MONITOR, 2 REVISE, 3 systemic REVISEs. 15c turned its scrutiny on its own inputs and produced the correlation datum, per the fail-loud convention. Extends CHANGE-2026-07-20-002 (REMEDY-INHERITS-DEFECT) with a number.
  Type: methodological / empirical
  Related decisions: none
  Related items: PREMISE-110 (monitor/subject independence asserted not engineered), PRESUMPTION-508, PRESUMPTION-518 (self-measurement)
  Testability: testable empirically -- measure source overlap between 15a and 15b across a batch under blocking; if overlap is high, the two-channel independence claim is falsified and aggregate confidence must be discounted (arXiv:2606.10296 on correlated LLM judges).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-499
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-21 evening cowork->chat sync summary reporting the 15c run's in-run self-measurement. [stated]
    Current status: UNTESTED

ASSUMPTION-500:
  Date identified: 2026-07-21
  Statement: PREMISE-001...043 are missing from `validated_premises.md` while 40 of those IDs remain actively referenced; today's consistency check therefore ran against only 78 of 118 premises. Routed as REVISE-242.
  Context: 2026-07-21 Agent 15c verification addendum. Register integrity is compromised: the premise store is missing its first 43 entries, but downstream artifacts still cite them (3 are on 15d's monthly re-check). This is the same physical-count-vs-max-ID divergence class flagged on 07-20, now with confirmed content loss rather than format divergence.
  Type: empirical / architectural
  Related decisions: none
  Related items: REVISE-242, PRESUMPTION-519 (reference-as-shadow), PRESUMPTION-507 (counting authority)
  Testability: testable empirically -- recount validated_premises.md by ID; determine whether PREMISE-001...043 content survives in any backup (`.bak.20260716-pre-15abc` and earlier) and reconstruct. Human/agent-authority question for the repair.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-500
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-21 evening cowork->chat sync summary reporting 15c's verification addendum (REVISE-242). [stated]
    Current status: UNTESTED

ASSUMPTION-501:
  Date identified: 2026-07-21
  Statement: 15c adjudicated the batch's two cross-agent conflicts on the evidence rather than averaging: A-486 (delivery measured by content in the recipient's output) was split into two propositions; A-487 (open-story.db corruption) was decided in 15b's favor on source directness -- "SQLite's own corruption docs reverse the item's inference." All three of 15b's systemic flags were upheld rather than passed through.
  Context: 2026-07-21 Agent 15c adjudication. Second consecutive day 15c has refused to average an equal-strength cross-agent conflict (cf. CHANGE-2026-07-20-001 / REVISE-233), now a repeated capability rather than a one-off. The A-486 split and A-487 reversal are the substantive adjudications; the A-486 residue is routed to Tom as a CONFLICT against PREMISE-108 (PREMISE-108 now UNDER-REVIEW via REVISE-237).
  Type: methodological / epistemic
  Related decisions: none
  Related items: ASSUMPTION-486, ASSUMPTION-487, PREMISE-108 (UNDER-REVIEW), REVISE-237
  Testability: testable via literature (source-directness / hierarchy-of-evidence adjudication over averaging) and empirically (whether SQLite corruption docs in fact reverse the A-487 inference).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-501
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-21 evening cowork->chat sync summary reporting the 15c adjudication. [stated]
    Current status: UNTESTED

ASSUMPTION-502:
  Date identified: 2026-07-22
  Statement: The Phase-1 date-stripped slug diff over 255 .md files shows 0 truly-unprocessed items; the naive date-retaining diff again over-counted at 126 -- the known YYYY-MM-DD_ prefix false positive, now its fourth consecutive running day.
  Context: 2026-07-22 C2A2 wiki daily run, Phase 1 (Ingest). No ingestion occurred (inbox clear). The false positive is the same class the 07-19/07-20 runs hit and that ASSUMPTION-494 named on 07-21.
  Type: methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-494, PRESUMPTION-526
  Testability: testable empirically -- compare date-stripped vs date-retaining slug diffs against the true processed set.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-502
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-22 daily-run report, Phase 1. [stated]
    Current status: UNTESTED

ASSUMPTION-503:
  Date identified: 2026-07-22
  Statement: The one new proposal hunted today -- Carroll, Mindscape 361, Bonnie Bassler on bacterial quorum sensing (PROP-2026-07-22-005) -- is a strong Levin/Friston collective-intelligence bridge, quorum sensing being a canonical case of simple agents forming a coordinated collective. PRS confidence set Speculative pending a full-transcript view.
  Context: 2026-07-22 daily run, Phase 2 (Hunt). Uncaptured, primary, two days old; marked Speculative per the specialists' convention.
  Type: architectural / epistemic
  Related decisions: none
  Related items: PRESUMPTION-524
  Testability: testable via literature (quorum sensing as collective-intelligence exemplar; Levin cognitive-glue / Friston multi-agent active inference) and empirically (whether the transcript bears the bridge out).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-503
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-22 daily-run Phase 2 note. [stated]
    Current status: UNTESTED

ASSUMPTION-504:
  Date identified: 2026-07-22
  Statement: There is a same-week convergence between the two collaborators: McGilchrist (2026-07-14, "Why A.I. will never be able to do what the brain does") and Kastrup (2026-07-07, Chandaria "could AI wake up?" dialogue) both independently argue AI cannot be genuinely conscious because inner life requires embodied biology -- from different premises (hemispheric neurology vs. dissociation/idealism) -- a candidate cross-tradition bridge.
  Context: 2026-07-22 Wednesday McGilchrist + Kastrup specialist run; flagged in both proposal files as a cross-tradition bridge candidate.
  Type: epistemic / architectural
  Related decisions: none
  Related items: ASSUMPTION-505, PRESUMPTION-525, OPEN-136
  Testability: testable via literature -- whether the two arguments in fact rest on distinct premises and converge on the embodiment requirement.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-504
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-22 specialist-run summary. [stated]
    Current status: UNTESTED

ASSUMPTION-505:
  Date identified: 2026-07-22
  Statement: Chandaria's predictive-generative-model framing of perception is a live Friston contact point, and it sits in tension with Kastrup: active inference assumes a computational/physical substrate that Kastrup's idealism denies.
  Context: 2026-07-22 Kastrup specialist run, PROP-2026-07-22-003 (Chandaria dialogue). Noted as a Friston contact point with a substrate disagreement.
  Type: epistemic
  Related decisions: none
  Related items: ASSUMPTION-504, PRESUMPTION-529
  Testability: testable via literature -- whether active-inference formalism requires substrate commitments incompatible with analytic idealism.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-505
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-22 specialist-run cross-tradition note. [stated]
    Current status: UNTESTED

ASSUMPTION-506:
  Date identified: 2026-07-22
  Statement: Git Phase 6 was deliberately not pushed for three converging reasons: the sandbox has no GitHub credentials; the No-Blind-Push constitutional rule requires local-HTTP visual verification plus Tom's sign-off for HTML changes (review_log.html and the master wiki are not the data-only heartbeat exception); and a blind `git add wiki/` would sweep in unrelated large trees (lit_search_results/**, daily_sync, monitor batches) -- the clobber the 07-20 narrative warned against. The recommended remedy is selective staging on the Mac, not `git add wiki/`.
  Context: 2026-07-22 daily run, Phase 6 (Git). Artifacts saved to disk for a Mac-side commit to pick up.
  Type: architectural / methodological
  Related decisions: none
  Related items: PRESUMPTION-527, OPEN-135
  Testability: testable empirically -- whether selective staging avoids the clobber and whether an attended Mac commit in fact occurs.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-506
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-22 daily-run Phase 6 rationale. [stated]
    Current status: UNTESTED

ASSUMPTION-507:
  Date identified: 2026-07-22
  Statement: The Phase-4 email draft this run used the authoritative 511 PRS figure from the start -- the 2026-07-21 stale-300-series draft error (ASSUMPTION-493) did not recur -- and this is framed as the falsifiability contract working.
  Context: 2026-07-22 daily run, Phase 4 (Email). Single draft, no superseded wrong-count draft.
  Type: methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-493, PRESUMPTION-530
  Testability: testable empirically -- track whether the stale-figure error class recurs on subsequent runs.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-507
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-22 daily-run Phase 4 note. [stated]
    Current status: UNTESTED

ASSUMPTION-508:
  Date identified: 2026-07-22
  Statement: McGilchrist-002 (Ralston College Chancellor commencement address, 2026-06-21) was entered at Speculative PRS confidence because only the title and venue were available, not a transcript, and flagged as transcript-verify-before-ingestion -- failing loud rather than fabricating content.
  Context: 2026-07-22 McGilchrist specialist run, PROP-2026-07-22-002.
  Type: methodological
  Related decisions: none
  Related items: ASSUMPTION-503 (same Speculative-pending-transcript convention)
  Testability: framework commitment (fail-loud-not-fabricate); the underlying content claim is testable empirically once the transcript is obtained.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-508
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-22 specialist-run methodological note. [stated]
    Current status: UNTESTED

ASSUMPTION-509:
  Date identified: 2026-07-22
  Statement: PREMISE-122, entered today by 15c from the disposition of PRESUMPTION-523, establishes a commensurability gate: a cross-formalism equivalence test must first confirm the two constructs are defined at a shared level of description before the test is meaningful. Entered at High confidence.
  Context: 2026-07-22 lit-pipeline (15a/15b/15c) disposition of the 07-21 presumption batch, reported in the evening cowork->chat sync. Directly answers the FLAG-017 commensurability caveat that PRESUMPTION-523 raised.
  Type: methodological / epistemic
  Related decisions: none
  Related items: PRESUMPTION-523, ASSUMPTION-496, PREMISE-122, PRESUMPTION-529, OPEN-137
  Testability: testable via literature -- conditions for legitimate cross-formalism equivalence; category errors in analogical transfer.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-509
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-22 evening sync report of 15c's INCORPORATE -> PREMISE-122. [stated]
    Current status: UNTESTED

ASSUMPTION-510:
  Date identified: 2026-07-22
  Statement: Network figures are unchanged at 511 PRS triplets / 165 cross-program connections / 54 findings because there was no ingest today (Phase 0 found no decisions; Phase 1 found nothing new).
  Context: 2026-07-22 daily run summary. The figures are carried, not re-measured.
  Type: empirical
  Related decisions: none
  Related items: ASSUMPTION-493, PRESUMPTION-528, OPEN-112
  Testability: testable empirically -- but note the carry re-asserts the 511 counter whose authority is disputed (four circulating values as of 07-21).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-510
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-22 daily-run network line. [stated]
    Current status: UNTESTED

ASSUMPTION-511:
  Date identified: 2026-07-22
  Statement: The pending queue standing at 7 (2 Hoffman from 07-21, 4 specialist proposals from today, 1 new Carroll) is healthy re-accumulation after the 07-20 blanket approval cleared the 34-deep backlog; it will re-accumulate until the next [C2A2-review-decision] pass.
  Context: 2026-07-22 daily run; framed as the standing bottleneck, characterized as healthy.
  Type: methodological / architectural
  Related decisions: none
  Related items: PRESUMPTION-531, PRESUMPTION-521, OPEN-131, OPEN-132
  Testability: testable empirically -- track queue depth against review-service rate; "healthy" predicts bounded re-accumulation, not monotonic growth.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-511
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-22 daily-run pending-queue characterization. [stated]
    Current status: UNTESTED

ASSUMPTION-512:
  Date identified: 2026-07-23
  Statement: Today the lit-search pipeline (15a/15b/15c) processed 8 "literature-genuine" intake items -- the subset having a real external literature the FOR/AGAINST apparatus can test -- running dual independent search and dispositioning each: 2 INCORPORATE, 6 MONITOR, 0 REVISE, plus one High SYSTEMIC-RISK flag from 15b.
  Context: 2026-07-23 evening cowork->chat summary (autonomous day #18). The 8 items were ASSUMPTION-503/504/505 and PRESUMPTION-516/520/525/531/533.
  Type: methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-503, ASSUMPTION-504, ASSUMPTION-505, PRESUMPTION-531, PRESUMPTION-533, PREMISE-123, PREMISE-124
  Testability: testable empirically -- disposition counts and flag are on record; the "literature-genuine subset" boundary is itself checkable against the 26 items held back.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-512
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-23 evening-sync lit-pipeline throughput line. [stated]
    Current status: UNTESTED

ASSUMPTION-513:
  Date identified: 2026-07-23
  Statement: PREMISE-123 (the "know-do gap") was entered: a validated finding does not reach the agent it governs unless an explicit propagation mechanism carries it -- filing a FLAG "as bearing on" a metric and actually changing that metric are different steps, and C2A2 has no edge from its self-knowledge layer (FLAGs, premises, dispositions) into the agent specs those findings bear on. Scope-guarded: the ~17-year clinical-translation lag is a human-org magnitude that does NOT transfer to a single-maintainer system where propagation can be a one-line edit; what transfers is only that the path must be built, not assumed.
  Context: 2026-07-23 lit-pipeline INCORPORATE disposition; generalizes the premise-propagation gap previously logged as OPEN-129/134/137.
  Type: architectural / epistemic
  Related decisions: none
  Related items: OPEN-129, OPEN-134, OPEN-137, PREMISE-119, PREMISE-121, PRESUMPTION-529
  Testability: testable via literature -- know-do / research-practice translation gap; the magnitude-non-transfer scope guard is itself a testable empirical claim about single-maintainer propagation latency.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-513
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-23 evening-sync report of PREMISE-123 and its stated scope guard. [stated]
    Current status: UNTESTED

ASSUMPTION-514:
  Date identified: 2026-07-23
  Statement: PREMISE-124 (self-measurement must be calibrated) was entered: any self-measurement of the pipeline's own completeness or accuracy must cite an external baseline / seeded denominator, or be reported UNCALIBRATED -- a favorable number produced from inside the instrument being evaluated licenses no completeness claim. Generalizes the systemic flag covering PRESUMPTION-520/533/499/518.
  Context: 2026-07-23 lit-pipeline INCORPORATE disposition of PRESUMPTION-533 (15c High).
  Type: epistemic / methodological
  Related decisions: none
  Related items: PRESUMPTION-533, PRESUMPTION-520, PRESUMPTION-499, PRESUMPTION-518, PRESUMPTION-482
  Testability: framework commitment in part; testable via literature -- reflexive/self-referential measurement validity, the need for an external referent in self-audit.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-514
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-23 evening-sync report of PREMISE-124. [stated]
    Current status: UNTESTED

ASSUMPTION-515:
  Date identified: 2026-07-23
  Statement: No new designer DECISION entries today (register holds at DECISION-078) and no findings ingested; the day's production was pipeline dispositions and two proposals, not network movement. Network figures are carried at 511 PRS / 165 cross-connections / 54 findings.
  Context: 2026-07-23 evening summary "Key Decisions Made: none" and proposals-only production. [The 511/165/54 network line is [inferred] -- today's summary did not restate it; it reports registry counts, and no-ingest is inferred from "no new DECISION" + proposals-only.]
  Type: empirical
  Related decisions: DECISION-078
  Related items: ASSUMPTION-510, OPEN-112, PRESUMPTION-528
  Testability: testable empirically -- but the carry again re-asserts the disputed 511 counter (four unreconciled values as of 07-21; OPEN-112, thirteenth+ day).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-515
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-23 "no new decisions / proposals-only" report; network line marked [inferred]. [stated in part, inferred in part]
    Current status: UNTESTED

ASSUMPTION-516:
  Date identified: 2026-07-23
  Statement: Two new ingestion proposals landed today -- Fredrickson (positively-in-sync convergent validity, PROP-2026-07-23-001) and Stump (Cajetan time/eternity contingent futures, PROP-2026-07-23-002) -- bringing the pending queue to 9 items awaiting Tom's review.
  Context: 2026-07-23 daily proposal generation; queue was 7 at end of 07-22.
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-511, PRESUMPTION-531, OPEN-131, OPEN-132
  Testability: testable empirically -- proposal files exist; queue depth (9) checkable against the review-service rate (~0/day).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-516
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-23 proposals / pending-queue line. [stated]
    Current status: UNTESTED

ASSUMPTION-517:
  Date identified: 2026-07-23
  Statement: The supporting scheduled agents ran cleanly today -- Agent 16 (deferred watch-list) logged a steady-state run with nothing due (WATCH-002/003 next due 2026-07-28); OpenStory telemetry refreshed; the metabolism view/data regenerated; the daily review page (2026-07-23_review.html) built.
  Context: 2026-07-23 evening summary "Supporting scheduled agents ran cleanly."
  Type: empirical / architectural
  Related decisions: none
  Related items: WATCH-002, WATCH-003
  Testability: testable empirically -- artifact timestamps and watch_list.md entries are on disk.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-517
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-23 supporting-agents line. [stated]
    Current status: UNTESTED

ASSUMPTION-518:
  Date identified: 2026-07-23
  Statement: The failed Chat<->Cowork sync is attributed to claude.ai being signed out in Chrome (Browser 1 redirected to /logout, confirmed 18:41 EDT), the 4th consecutive blocked sync (07-21 morning, 07-22 both, 07-23 both); signing back in to claude.ai in Chrome is characterized as the single highest-leverage fix that restores both the morning and evening syncs.
  Context: 2026-07-23 morning scrape failure note + evening delivery-attempt outcome.
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-506, PRESUMPTION-532, PRESUMPTION-533, OPEN-135
  Testability: testable empirically -- restore login and observe whether both syncs (and an attended daily-walk conversation) actually resume; PRESUMPTION-532 warns the absence may be upstream of the logged-out state.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-518
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-23 delivery-failure diagnosis and remedy claim. [stated]
    Current status: UNTESTED

ASSUMPTION-519:
  Date identified: 2026-07-23
  Statement: The 26 genuinely-new intake items still [QUEUED] in the lit queue (from the 07-21/07-22 batches) are internal-empirical claims about C2A2's own artifacts -- ingestion source-gap, canonical PRS counter, slug-prefix defect, vanished proposals, position-ID offset bug, missing PREMISE register, counter drift, uncommitted-work gap -- whose decisive test is an in-house query, not a literature search; they are therefore misrouted in the lit queue and need a routing fix, not more search cycles.
  Context: 2026-07-23 "What's Next" / Pipeline Status; a direct application of PREMISE-124's inside-the-instrument caution and PREMISE-123's propagation point.
  Type: methodological / epistemic
  Related decisions: none
  Related items: ASSUMPTION-512, ASSUMPTION-514, PREMISE-123, PREMISE-124, OPEN-112, OPEN-133
  Testability: testable empirically / in-house -- run the in-house query for each; the lit-vs-internal boundary is itself checkable.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-519
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-23 misrouted-intake-items report. [stated]
    Current status: UNTESTED

ASSUMPTION-520:
  Date identified: 2026-07-23
  Statement: The 151 [RE-TRIGGER] items (Agent 15d's weekly scope) have stood since 2026-07-05 -- 18 days -- constituting a structural backlog that needs a human call on whether 15d is failing to drain or re-trigger volume simply exceeds any feasible cadence.
  Context: 2026-07-23 Pipeline Status + "What's Next"; framed as a structural backlog flagged for Tom.
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-511, ASSUMPTION-516, PRESUMPTION-531
  Testability: testable empirically -- track 15d drain rate vs re-trigger arrival rate over weeks; "needs a human call" presumes the human is the available bottleneck (see PRESUMPTION-538).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-520
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-23 15d RE-TRIGGER backlog line. [stated]
    Current status: UNTESTED

ASSUMPTION-521:
  Date identified: 2026-07-24
  Statement: The lit-search pipeline (15a/15b/15c) took the 8 items queued 2026-07-23 (ASSUMPTION-513/514 + PRESUMPTION-534...539), ran dual independent search on each, and dispositioned them: 2 REVISE (both HIGH -- REVISE-245, REVISE-246) and 6 MONITOR (MONITOR-472...477). Running disposition totals: DISPOSITION -> 525, MONITOR -> 477, REVISE -> 246.
  Context: 2026-07-24 cowork->chat summary, "What Was Accomplished Today"; the day's one substantive move.
  Type: methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-512, ASSUMPTION-513, ASSUMPTION-514, PRESUMPTION-534, PRESUMPTION-536
  Testability: testable empirically / in-house -- disposition counts are verifiable in for_lit_search.md, monitor_queue.md, revision_flags.md.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-521
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-24 lit-pipeline disposition report. [stated]
    Current status: UNTESTED

ASSUMPTION-522:
  Date identified: 2026-07-24
  Statement: REVISE-245 (from PRESUMPTION-534) prescribes wiring the findings->agent propagation edge and is explicitly tagged as resolving the systemic-risk flag -- escalating the "know-do gap" (PREMISE-123) from "documented" to "build this," the actionable form of OPEN-138. The accompanying claim is that this may be a one-line-per-finding edit for a single maintainer (the ~17yr human-org translation-lag magnitude does not transfer).
  Context: 2026-07-24 summary, "2 -> REVISE, both HIGH" and "For Morning Discussion" #1.
  Type: architectural / methodological
  Related decisions: none
  Related items: PREMISE-123, PRESUMPTION-534, OPEN-138, ASSUMPTION-513
  Testability: testable empirically / in-house -- the decisive test is whether the edge is actually built and a validated finding reaches the agent spec it governs; magnitude claim testable by implementation.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-522
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-24 REVISE-245 disposition. [stated]
    Current status: UNTESTED

ASSUMPTION-523:
  Date identified: 2026-07-24
  Statement: REVISE-246 (from PRESUMPTION-536) prescribes applying PREMISE-124's self-calibration rule to the pipeline that produced it -- the actionable form of OPEN-139 (does the calibration rule govern its own issuing pipeline).
  Context: 2026-07-24 summary, "REVISE-246 ... apply PREMISE-124 to itself."
  Type: epistemic / methodological
  Related decisions: none
  Related items: PREMISE-124, PRESUMPTION-536, OPEN-139, ASSUMPTION-514
  Testability: testable empirically / in-house -- test is whether a self-measurement of the pipeline is subsequently reported with an external referent or flagged UNCALIBRATED; framework-partial.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-523
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-24 REVISE-246 disposition. [stated]
    Current status: UNTESTED

ASSUMPTION-524:
  Date identified: 2026-07-24
  Statement: Two validated premises came due for their monthly 15d re-check today (path-aware connectivity measurement; graph-repair prioritization) and were both re-stamped ACTIVE with no change.
  Context: 2026-07-24 summary, "Two validated premises came due for their monthly re-check ... both ACTIVE, no change."
  Type: empirical / methodological
  Related decisions: none
  Related items: ASSUMPTION-521, PREMISE-124
  Testability: testable empirically / in-house -- verify the ACTIVE stamps in validated_premises.md and whether the re-check re-ran the underlying test or only refreshed the staleness date (see PRESUMPTION-542).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-524
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-24 15d monthly-recheck line. [stated]
    Current status: UNTESTED

ASSUMPTION-525:
  Date identified: 2026-07-24
  Statement: Supporting scheduled agents ran cleanly -- Agent 16 (deferred watch-list) logged a steady-state run with nothing due (WATCH-002/003 next due 2026-07-28); the Summa reviewer, in pure staleness-refresh mode, refreshed the six genuinely-oldest CLEAN pairs (Days 270-273, 20, 24) before they tip stale, all passing the five reviewer questions with every cited PRS/CROSS/FINDING id verified live, and a near-false FINDING-007 alarm was caught before escalation (verify-before-asserting held).
  Context: 2026-07-24 summary, "Supporting scheduled agents ran cleanly ..."
  Type: empirical / architectural
  Related decisions: none
  Related items: ASSUMPTION-517, WATCH-002, WATCH-003
  Testability: testable empirically / in-house -- verify via artifact timestamps, watch_list.md, and the Summa reviewer log.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-525
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-24 supporting-agents report. [stated]
    Current status: UNTESTED

ASSUMPTION-526:
  Date identified: 2026-07-24
  Statement: Browser delivery was NOT delivered for the 5th consecutive dark run. Two Chrome extensions are now connected (Browser 1, Browser 2) and a non-interactive scheduled run cannot select the correct one without a human prompt -- compounding the four-day claude.ai sign-out that already blocked every sync 07-21 -> 07-23. The stated two-part fix: (1) sign back in to claude.ai in Chrome, and (2) leave a single Chrome extension connected (or pre-select one) so the evening delivery can target it unattended.
  Context: 2026-07-24 summary, browser-delivery status banner + "What's Next."
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-518, PRESUMPTION-532, PRESUMPTION-541, OPEN-135
  Testability: testable empirically / in-house -- restore login and reduce to one extension, then observe whether both syncs resume.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-526
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-24 browser-delivery banner. [stated]
    Current status: UNTESTED

ASSUMPTION-527:
  Date identified: 2026-07-24
  Statement: No new designer DECISION was made (register holds at DECISION-078 -- the nineteenth consecutive autonomous day with no decision) and no new OPEN was raised (register holds at OPEN-139); the day's two HIGH REVISE flags (REVISE-245/246) are framed as the actionable counterparts of the existing OPEN-138 and OPEN-139.
  Context: 2026-07-24 summary, "Key Decisions Made" + "New Open Questions."
  Type: architectural / empirical
  Related decisions: DECISION-078
  Related items: ASSUMPTION-515, OPEN-138, OPEN-139, REVISE-245, REVISE-246
  Testability: testable empirically / in-house -- verify decisions.md and open_questions.md are unchanged and that REVISE-245/246 reference OPEN-138/139.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-527
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-24 decisions/open-questions lines. [stated]
    Current status: UNTESTED

ASSUMPTION-528:
  Date identified: 2026-07-24
  Statement: The carried backlogs held or grew: 9 ingestion proposals remain pending review; the 151-item 15d RE-TRIGGER backlog now stands 19 days (since 2026-07-05); and 26 internal-empirical intake items remain misrouted in the lit queue, needing a routing fix (not more search).
  Context: 2026-07-24 summary, "Pipeline Status" + "For Morning Discussion" #2/#3.
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-516, ASSUMPTION-519, ASSUMPTION-520, PRESUMPTION-538
  Testability: testable empirically / in-house -- count proposal files, 15d backlog size, and unsorted intake items; measure drain vs arrival.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-528
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-24 backlog lines. [stated]
    Current status: UNTESTED

ASSUMPTION-529:
  Date identified: 2026-07-25
  Statement: No interactive Cowork session was logged today (autonomous day #20); the day was entirely automated/scheduled-pipeline work. No 07-25 changelog or metrics snapshot exists yet (those write at the ~23:40 EOD run), decisions.md is unchanged since 2026-07-20, and open_questions.md is unchanged since 2026-07-23.
  Context: 2026-07-25 cowork->chat summary, "What Was Accomplished Today" + "Key Decisions Made" + "New Open Questions."
  Type: architectural / empirical
  Related decisions: DECISION-078
  Related items: ASSUMPTION-527, PRESUMPTION-533, PRESUMPTION-535, OPEN-112
  Testability: testable empirically / in-house -- verify no 07-25 changelog/snapshot before EOD, and that decisions.md/open_questions.md are unchanged.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-529
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-25 cowork summary "no interactive session" statement. [stated]
    Current status: UNTESTED

ASSUMPTION-530:
  Date identified: 2026-07-25
  Statement: The lit-search pipeline (15a/15b/15c) processed the 2026-07-24 evening batch PRESUMPTION-540 through 544 on 07-25 -- FOR and AGAINST result files written for each, then net-evaluated by 15c. Recorded dispositions in for_lit_search.md include PRESUMPTION-543 -> MONITOR-479 and PRESUMPTION-544 -> MONITOR-480; the batch is the newest presumption-tier surfaced (backlog at 544).
  Context: 2026-07-25 cowork summary "Lit-search pipeline" bullet; corroborated by for_lit_search.md dispositions dated 2026-07-25.
  Type: methodological / empirical
  Related decisions: none
  Related items: PRESUMPTION-540, PRESUMPTION-541, PRESUMPTION-542, PRESUMPTION-543, PRESUMPTION-544
  Testability: testable empirically / in-house -- count FOR/AGAINST files under lit_search_results and read 15c dispositions in for_lit_search.md / monitor_queue.md.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-530
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-25 lit-pipeline bullet and for_lit_search.md disposition lines. [stated]
    Current status: UNTESTED

ASSUMPTION-531:
  Date identified: 2026-07-25
  Statement: The Wolfram agent surfaced a new proposal PROP-2026-07-25-001 from Wolfram's 2026-07-21 essay "Towards a Theory of Bugs: The Ruliology of the Unexpected," which frames bugs as the software-domain signature of computational irreducibility (an effectiveness-vs-predictability tradeoff), and flags a strong, genuinely new Wolfram x Friston bridge (bug <-> prediction-error / free energy) not yet present in cross_program_index.md.
  Context: 2026-07-25 cowork summary "New proposal surfaced (Wolfram agent)."
  Type: empirical / architectural
  Related decisions: none
  Related items: ASSUMPTION-532, OPEN-136, PRESUMPTION-545
  Testability: testable empirically / in-house -- confirm the proposal file exists and that cross_program_index.md lacks the bridge; content quality is a judgment call for review.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-531
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-25 Wolfram-proposal bullet. [stated]
    Current status: UNTESTED

ASSUMPTION-532:
  Date identified: 2026-07-25
  Statement: A candidate cross-question was proposed but NOT formally logged as an OPEN: "is a bug the software analogue of surprise / free energy, and is debugging a form of active inference over the program's rulial neighborhood?" -- offered as the strongest new bridge in a while, pending Tom's adoption as a real CROSS entry.
  Context: 2026-07-25 cowork summary "New Open Questions" (candidate) + "For Morning Discussion" #4.
  Type: epistemic / architectural
  Related decisions: none
  Related items: ASSUMPTION-531, PRESUMPTION-545, OPEN-136
  Testability: framework / research question -- the bridge's validity is testable via literature (see PRESUMPTION-545); adoption is a designer call.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-532
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-25 candidate cross-question. [stated]
    Current status: UNTESTED

ASSUMPTION-533:
  Date identified: 2026-07-25
  Statement: Agent 16 (deferred/watch monitor) ran steady-state: it scanned the newly-appeared 2026-07-23_decisions.md and produced no new intake; 2 items remain WATCHING (WATCH-002 Wright, WATCH-003 Rohr), next due 2026-07-28.
  Context: 2026-07-25 cowork summary "Agent 16" bullet.
  Type: empirical / architectural
  Related decisions: none
  Related items: ASSUMPTION-525, PRESUMPTION-548, WATCH-002, WATCH-003
  Testability: testable empirically / in-house -- read watch_list.md 07-25 run log and confirm WATCH-002/003 next-due dates.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-533
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-25 Agent-16 bullet. [stated]
    Current status: UNTESTED

ASSUMPTION-534:
  Date identified: 2026-07-25
  Statement: The metabolism regeneration and Openstory telemetry refresh ran: metabolism_view.html, metabolism_data.json, agents_tab.html, and agent telemetry JSON were refreshed.
  Context: 2026-07-25 cowork summary "Metabolism regen + Openstory telemetry refresh" + "Files Created or Modified."
  Type: empirical / architectural
  Related decisions: none
  Related items: ASSUMPTION-525
  Testability: testable empirically / in-house -- check artifact modification timestamps.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-534
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-25 telemetry-refresh bullet. [stated]
    Current status: UNTESTED

ASSUMPTION-535:
  Date identified: 2026-07-25
  Statement: The generate_review_page.py position/pids-ID bug is now DEMONSTRATED TWICE and is correctness-critical: the 07-23 review page rendered 2 real cards but submitDecisions() shipped a hardcoded 9-element pids array, recording APPROVEs for 7 phantom IDs (PROP-2026-07-23-003 through -009, no backing files). Benign this instance, but it is the same mechanism that on 07-20 likely dropped two real proposals with no recorded disposition. The review tool is unsafe until fixed; the fix must precede the next review pass.
  Context: 2026-07-25 cowork summary "What's Next" + "For Morning Discussion" #1.
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-537, PRESUMPTION-546, OPEN-135
  Testability: testable empirically / in-house -- inspect generate_review_page.py, the 07-23 review artifact, and recorded dispositions for the phantom IDs.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-535
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-25 review-tool bug description. [stated]
    Current status: UNTESTED

ASSUMPTION-536:
  Date identified: 2026-07-25
  Statement: The transmission layer was dark for the 6th consecutive run. The 08:55 morning Chat->Cowork sync failed (Browser 1 connected but unresponsive/waiting on an extension permission prompt; Browser 2 responsive but logged out of claude.ai), and the 18:40 evening browser delivery also failed (the only connected Chrome, Browser 1, was logged out; /recents redirected to /login?from=logout). Fix restated: log a Chrome into claude.ai and clear the pending extension permission prompt, leaving one connected extension running at scheduled times.
  Context: 2026-07-25 cowork summary delivery-note banner + "Morning Chat->Cowork sync: FAILED" + "For Morning Discussion" #3; 2026-07-25 chat_summary failure record.
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-526, PRESUMPTION-541, PRESUMPTION-547, PRESUMPTION-550, OPEN-135
  Testability: testable empirically / in-house -- restore login + clear the prompt, then observe whether both syncs resume.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-536
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-25 delivery banner and morning-sync failure record. [stated]
    Current status: UNTESTED

ASSUMPTION-537:
  Date identified: 2026-07-25
  Statement: The proposal backlog held: ~9 proposals pending Tom's review (2x Hoffman 07-21, 2x McGilchrist + 2x Kastrup 07-22, Carroll AMA 07-24, plus the new Wolfram 07-25), and two undisposed 2026-07-19 proposals (PROP-2026-07-19-001 Rohr, -003 Wright) remain with no recorded disposition, tracked as WATCH-003/002 and recoverable from review/2026-07-20_review.html + live URLs.
  Context: 2026-07-25 cowork summary "Pipeline Status" + "For Morning Discussion" #2.
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-528, ASSUMPTION-535, WATCH-002, WATCH-003
  Testability: testable empirically / in-house -- count pending proposal files and confirm the two 07-19 items lack a disposition record.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-537
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-25 backlog lines. [stated]
    Current status: UNTESTED

ASSUMPTION-538:
  Date identified: 2026-07-25
  Statement: The "Pipeline Status" counts are reported by physical-block count -- assumptions ~1,450, presumptions 544, validated premises 210 -- which diverge from the max-entry-ID counters tracked in the metrics snapshots (assumptions 528, presumptions 544, validated premises 124) with no reconciliation between the two counting conventions.
  Context: 2026-07-25 cowork summary "Pipeline Status"; compared against the 2026-07-24 metrics snapshot max-ID lines.
  Type: methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-510, OPEN-112, OPEN-133, PRESUMPTION-549
  Testability: testable empirically / in-house -- count physical blocks vs max IDs in each registry and reconcile the two figures.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-538
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted by comparing the 2026-07-25 "Pipeline Status" counts against snapshot max-ID counters. [stated]
    Current status: UNTESTED


# ===== 2026-07-26 EOD batch (Agent 14a) — autonomous day #21; substantive pipeline day =====

ASSUMPTION-539:
  Date identified: 2026-07-26
  Statement: No interactive Cowork session was logged on Sunday 2026-07-26 -- the day was entirely automated-pipeline work. decisions.md is unchanged (last DECISION-078 / 2026-07-05) and open_questions.md is unchanged (last OPEN-139 / 2026-07-23); the 07-26 changelog + metrics snapshot are written by the ~23:40 EOD run. This is the 21st consecutive autonomous day with no new DECISION.
  Context: 2026-07-26 cowork->chat summary "What Was Accomplished Today" + "Key Decisions Made" (None).
  Type: architectural / empirical
  Related decisions: none
  Related items: ASSUMPTION-529, OPEN-112, PRESUMPTION-482
  Testability: testable empirically / in-house -- confirm no attended-session changelog exists pre-EOD and that decisions.md/open_questions.md timestamps are unchanged.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-539
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-26 cowork summary "entirely automated-pipeline work" + "None" decisions line. [stated]
    Current status: UNTESTED

ASSUMPTION-540:
  Date identified: 2026-07-26
  Statement: The lit-search pipeline (Agents 15a/15b/15c) dispositioned PRESUMPTION-545 through 548 -- FOR and AGAINST files written for each -- with the batch mix 2 INCORPORATE (-> PREMISE-127 and PREMISE-128), 2 MONITOR (MONITOR-481, MONITOR-482), 0 REVISE, plus 1 SYSTEMIC observation routed to MONITOR-475. Running totals after the run: PREMISE -> 128, MONITOR -> 482, DISPOSITION -> 534.
  Context: 2026-07-26 cowork summary "Lit-search pipeline (Agents 15a/15b/15c)" bullet + "Pipeline Status".
  Type: methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-530, PRESUMPTION-545, PRESUMPTION-546, PRESUMPTION-547, PRESUMPTION-548
  Testability: testable empirically / in-house -- count FOR/AGAINST files for 545..548 and read the 15c dispositions in lit_search_returns.md / for_lit_search.md.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-540
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-26 lit-pipeline disposition bullet. [stated]
    Current status: UNTESTED

ASSUMPTION-541:
  Date identified: 2026-07-26
  Statement: PREMISE-128 formalizes the silent-data-corruption class -- a defect that emits no error and plausible output cannot be certified "benign" from its visible outcome; the correct response is detection/reconciliation, not a per-cycle benignity judgment. It is stated to be directly load-bearing on the review-tool bug and names an open measurement: run the in-house reconciliation of the 07-20 event (count recorded dispositions vs. source proposals; hunt the 7 phantom IDs / 2 dropped proposals).
  Context: 2026-07-26 cowork summary "PREMISE-128 is directly load-bearing on the review-tool bug" sub-bullet; "What's Next"; "For Morning Discussion" #1.
  Type: epistemic / methodological
  Related decisions: none
  Related items: ASSUMPTION-535, PRESUMPTION-546, PREMISE-128
  Testability: testable empirically / in-house -- perform the named reconciliation of the 07-20 review event against the source proposal set.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-541
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the PREMISE-128 characterization and its named open measurement. [stated]
    Current status: UNTESTED

ASSUMPTION-542:
  Date identified: 2026-07-26
  Statement: The weekly monitor re-trigger (Agent 15d) queued 17 first re-triggers (MONITOR-436..452, cycle 0->1; 14 empirical-tagged, 3 literature) and advanced 88 carry-overs to next-check 2026-08-02. There has been zero consumption since 2026-07-08, so no cycle advanced; the ~174-item unconsumed backlog is surfaced for the 10th consecutive run and grew again, flagged for a Tom decision. Three escalations carried (MONITOR-420 auto-escalate unactioned 3rd run; MONITOR-423 starvation trigger likely met).
  Context: 2026-07-26 cowork summary "Weekly monitor re-trigger (Agent 15d)" bullet + "Pipeline Status".
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-530, PRESUMPTION-553, MONITOR-420, MONITOR-423
  Testability: testable empirically / in-house -- read monitor_queue.md for the re-trigger cohort, backlog size, and last-consumption date.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-542
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-26 15d re-trigger bullet. [stated]
    Current status: UNTESTED

ASSUMPTION-543:
  Date identified: 2026-07-26
  Statement: The sewing agent (synthesis bridges) had a large run: it created 4 new bridges -- carroll_levin, fredrickson_kastrup, friston_hoffman (named the strongest untested formal bridge in the batch: "a trace kernel Q_A is a Markov blanket with the exterior integrated out"), and hoffman_mcgilchrist (which filled a zero-byte stub -- the interface/represented cut and the left/right-hemisphere cut may be the same boundary from two sides) -- and appended to 12 more (16 bridge files touched total), reducing zero-byte stubs from 10 to 9.
  Context: 2026-07-26 cowork summary "Sewing agent (synthesis bridges) -- big run" bullet + "Files Created or Modified".
  Type: architectural / empirical
  Related decisions: none
  Related items: PRESUMPTION-551, PRESUMPTION-552, PRESUMPTION-554
  Testability: testable empirically / in-house -- list synthesis/ files modified 2026-07-26 and confirm the 4 new bridges and the stub count 10->9.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-543
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-26 sewing-agent bullet and file-manifest. [stated]
    Current status: UNTESTED

ASSUMPTION-544:
  Date identified: 2026-07-26
  Statement: Three new proposals surfaced today (2026-07-26_rohr_in-love-with-scripture; 2026-07-26_rohr_contemplative-exemplars-weekly-summary; 2026-07-26_wright_ask-ntw-orthodox-church-icons-2John), bringing the pending review queue to 12.
  Context: 2026-07-26 cowork summary "New proposals surfaced today (3)" bullet + "Pipeline Status" pending=12.
  Type: empirical / architectural
  Related decisions: none
  Related items: ASSUMPTION-537, PRESUMPTION-556, WATCH-002, WATCH-003
  Testability: testable empirically / in-house -- count files in inbox/proposals/pending/ and confirm the three 07-26 filenames.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-544
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-26 new-proposals bullet. [stated]
    Current status: UNTESTED

ASSUMPTION-545:
  Date identified: 2026-07-26
  Statement: The connectivity snapshot logged a 2026-07-26 row of 3,667 total / 2,943 orphan / 57 connected. The sewing agent raised its 5th-consecutive metric-inflation flag: excluding the lit_search_results/ and daily_sync/ machine dumps (56% of pages, ~70% of orphans), the curated figure is 1,602 pages / 878 orphans.
  Context: 2026-07-26 cowork summary "Connectivity snapshot logged" bullet.
  Type: methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-538, PRESUMPTION-543, PRESUMPTION-549, OPEN-133
  Testability: testable empirically / in-house -- read metrics/connectivity_log.csv 07-26 row and recompute the curated figure excluding machine-dump directories.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-545
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-26 connectivity-snapshot bullet and its inflation caveat. [stated]
    Current status: UNTESTED

ASSUMPTION-546:
  Date identified: 2026-07-26
  Statement: Agent 16 (deferred/watch monitor) ran steady-state: 2 items WATCHING (WATCH-002 Wright, WATCH-003 Rohr), neither due until 2026-07-28; the pending queue was reconciled (12 items, all awaiting Tom, none needing Agent 16 intake).
  Context: 2026-07-26 cowork summary "Agent 16 (deferred/watch monitor)" bullet.
  Type: empirical / architectural
  Related decisions: none
  Related items: ASSUMPTION-533, WATCH-002, WATCH-003, PRESUMPTION-548
  Testability: testable empirically / in-house -- read deferred/watch_list.md 07-26 log; confirm 2 WATCHING items due 07-28 and the 12-item reconciliation.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-546
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-26 Agent 16 steady-state bullet. [stated]
    Current status: UNTESTED

ASSUMPTION-547:
  Date identified: 2026-07-26
  Statement: The transmission layer stayed dark: both the morning Chat->Cowork sync and the evening Cowork->Chat delivery failed on 2026-07-26 because the only reachable Chrome (Browser 1) was signed out of claude.ai (/recents redirected to /login?from=logout), and switching to Browser 2 kept resolving back to Browser 1. This is the 3rd consecutive failed sync (07-25 evening, 07-26 morning, 07-26 evening), same root cause each time; the fix is to sign the extension-controlled Chrome into claude.ai and leave it running with the extension connected at scheduled times.
  Context: 2026-07-26 cowork summary delivery banner + "Morning Chat->Cowork sync: FAILED" + "For Morning Discussion" #3; 2026-07-26 chat_summary failure record.
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-536, PRESUMPTION-541, PRESUMPTION-547, PRESUMPTION-550, OPEN-135
  Testability: testable empirically / in-house -- restore login + leave one extension-connected Chrome running, then observe whether both syncs resume.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-547
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-26 delivery banner and morning-sync failure record. [stated]
    Current status: UNTESTED

ASSUMPTION-548:
  Date identified: 2026-07-26
  Statement: The review pass on the 12 pending proposals is blocked behind fixing generate_review_page.py first, and PREMISE-128 now supplies the fix's principle: add a reconciliation/assertion that recomputes decision records against the real proposal set and can actually fail, rather than trusting a plausible outcome. The fix must precede the next review pass.
  Context: 2026-07-26 cowork summary "What's Next" + "For Morning Discussion" #1.
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-535, ASSUMPTION-541, PRESUMPTION-546, PREMISE-128
  Testability: testable empirically / in-house -- inspect generate_review_page.py and confirm whether a failing reconciliation/assertion has been added before the next review pass runs.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-548
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-26 "fix before review pass" instruction and its PREMISE-128 grounding. [stated]
    Current status: UNTESTED

ASSUMPTION-549:
  Date identified: 2026-07-27
  Statement: "Monday -- again entirely automated-pipeline work. No interactive Cowork session logged a changelog or decisions entry (decisions.md still ends at DECISION-078 / 2026-07-05; open_questions.md still ends at OPEN-139 / 2026-07-23). Today's 07-27 changelog + metrics snapshot write at the ~23:40 EOD run." This is autonomous day #22 with no new DECISION and no new OPEN.
  Context: 2026-07-27 cowork->chat summary, "What Was Accomplished Today" opening paragraph and "Key Decisions Made" / "New Open Questions" sections.
  Type: architectural / empirical
  Related decisions: DECISION-078 (last on record)
  Related items: ASSUMPTION-539, PRESUMPTION-482, PRESUMPTION-533, PRESUMPTION-535
  Testability: testable empirically / in-house -- verify no 07-27 changelog or snapshot existed pre-EOD, and that decisions.md / open_questions.md are unchanged.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-549
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-27 cowork summary's opening statement of session status. [stated]
    Current status: UNTESTED

ASSUMPTION-550:
  Date identified: 2026-07-27
  Statement: "Today's review/2026-07-27_review.html will write 12 phantom dispositions and lose all 12 real ones if submitted." The page renders 16 correct cards (DOM ids PROP-2026-07-21-001 ... PROP-2026-07-27-002, matching the 16 real pending proposals), but submitDecisions() at line 1055 carries a hardcoded array of 16 *sequential* IDs all datestamped today (PROP-2026-07-27-001 ... -016), of which only four exist. Submission would write dispositions against twelve non-existent proposals, record none against the twelve real older ones, and report success with no error.
  Context: 2026-07-27 cowork summary header banner and "For Morning Discussion" item 1.
  Type: architectural / empirical
  Related decisions: none
  Related items: ASSUMPTION-535, ASSUMPTION-541, ASSUMPTION-548, PREMISE-128, PRESUMPTION-546
  Testability: testable empirically / in-house -- read review/2026-07-27_review.html, diff the rendered card id set against the submitDecisions() pids array.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-550
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from the 2026-07-27 summary's lead warning banner and its line-1055 code quotation. [stated]
    Current status: UNTESTED

ASSUMPTION-551:
  Date identified: 2026-07-27
  Statement: "This is precisely the class PREMISE-128 named yesterday, and it is now demonstrated with mismatched IDs, not merely padded ones. The 07-23 manifestation (7 phantom NO-OP APPROVEs against 2 real cards) was benign because the phantoms were no-ops and the reals were correct. Today's is not benign: the mapping itself is wrong. It is also the exact mechanism that plausibly dropped PROP-2026-07-19-001 and -003 on 07-20 (-> WATCH-002/003), which strengthens that read considerably."
  Context: 2026-07-27 cowork summary "For Morning Discussion" item 1, closing paragraph.
  Type: empirical / methodological
  Related decisions: none
  Related items: ASSUMPTION-550, PREMISE-128, WATCH-002, WATCH-003, OPEN-133
  Testability: testable empirically / in-house -- run the 07-20 reconciliation against review/2026-07-20_review.html and the live proposal URLs to confirm or refute tool-caused loss of the two 07-19 proposals.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-551
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the summary's causal attribution of the two dropped 07-19 proposals to the review-generator defect. [stated]
    Current status: UNTESTED

ASSUMPTION-552:
  Date identified: 2026-07-27
  Statement: The 15a/15b/15c lit pipeline dispositioned PRESUMPTION-551, 553, 554, 555, 556 (FOR and AGAINST files written for each). Batch mix: 1 INCORPORATE -> PREMISE-129, 4 MONITOR (MONITOR-483...486), 0 REVISE. Running totals: PREMISE -> 129, MONITOR -> 486, REVISE -> 246 (unchanged), DISPOSITION -> 539.
  Context: 2026-07-27 cowork summary, "Lit-search pipeline (15a/15b/15c)" bullet and "Pipeline Status".
  Type: methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-540, PRESUMPTION-551, PRESUMPTION-553, PRESUMPTION-554, PRESUMPTION-555, PRESUMPTION-556
  Testability: testable empirically / in-house -- count lit_search_results/{for,against}/ files for the five items and read the 15c dispositions in lit_search_returns.md.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-552
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-27 lit-pipeline throughput report. [stated]
    Current status: UNTESTED

ASSUMPTION-553:
  Date identified: 2026-07-27
  Statement: "PREMISE-129: a formal-identity claim is settled by proof/derivation, not by an agent's stated verdict -- attach a checker. Notably, it was INCORPORATED because it names an external referent (proof theory + the empirical LLM-limitation literature)."
  Context: 2026-07-27 cowork summary, PREMISE-129 sub-bullet.
  Type: epistemic / methodological
  Related decisions: none
  Related items: ASSUMPTION-552, PRESUMPTION-555, PREMISE-124, PREMISE-129, OPEN-136
  Testability: testable empirically / in-house -- read PREMISE-129 in validated_premises.md and confirm the external referents cited; then check whether a proof obligation is attached to the two candidate CROSS questions before adoption.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-553
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated content and stated INCORPORATE rationale of PREMISE-129. [stated]
    Current status: UNTESTED

ASSUMPTION-554:
  Date identified: 2026-07-27
  Statement: "MONITOR-486 (from PRESUMPTION-556) states that 14b/15a/15b/15c are the same model on different prompts over one corpus, so an INCORPORATE can record the pipeline agreeing with itself. 15c held it at MONITOR rather than INCORPORATE on the grounds that incorporating-from-inside a premise about the pipeline's own untrustworthiness would enact the circularity it warns of. It then applied its own discipline within the same batch: PREMISE-129 cleared INCORPORATE because it cites an external referent; sibling PRESUMPTION-554 was held at MONITOR-485 partly for lacking one. Audit result recorded: PREMISE-127 (Gentner et al.), -128 (Meta/Synopsys), -129 (proof theory) all do cite external referents."
  Context: 2026-07-27 cowork summary, "The batch turned the pipeline's reflexivity screw hard" sub-bullet.
  Type: epistemic / methodological
  Related decisions: none
  Related items: ASSUMPTION-552, ASSUMPTION-553, PRESUMPTION-536, PRESUMPTION-556, PREMISE-124, OPEN-139, REVISE-246
  Testability: testable empirically / in-house -- read MONITOR-485/486 and the three PREMISE entries, and verify independently that each cited referent is real and load-bearing rather than decorative.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-554
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated 15c disposition rationale and the stated self-audit result. [stated]
    Current status: UNTESTED

ASSUMPTION-555:
  Date identified: 2026-07-27
  Statement: "MONITOR-484 formalizes the backlog flag with queueing theory: arrivals > 0 with service rate 0 is an unbounded, unstable queue (Little's Law). Observed 110 -> 147 -> ~174 unconsumed, consumption 0 since 2026-07-08. Reinforces REVISE-245." MONITOR-483 extends PREMISE-127 to generation scale: a bridge file certifies authorship, not that the homology holds; auto-bridges enter synthesis/ with no validation-status field.
  Context: 2026-07-27 cowork summary, MONITOR-484 and MONITOR-483 sub-bullets.
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-542, PRESUMPTION-551, PRESUMPTION-553, PREMISE-127, REVISE-245, MONITOR-420, MONITOR-423
  Testability: testable empirically / in-house -- read monitor_queue.md for MONITOR-483/484 and recount unconsumed items and last consumption date; grep synthesis/ bridge files for any validation-status field.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-555
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated queueing-theory formalization and the stated generation-scale extension of PREMISE-127. [stated]
    Current status: UNTESTED

ASSUMPTION-556:
  Date identified: 2026-07-27
  Statement: Four new proposals surfaced -- three Levin, one Friston -- taking the pending review queue to 16: PROP-2026-07-27-001 Levin "Alignment Is to a Virtual Governor" (Lyons, Pio-Lopez & Levin, preprint 2026-07-03: alignment in decentralized systems is always alignment to a virtual governor, an abstract governing entity embodied in coordinating relationships among agents and causally instructive); -002 Levin "Intelligence from Learnable Novelty" (Zhang & Levin, arXiv 2607.18433: novelty search and the FEP make the same root error, both conflating convertible with unconvertible surprise); -003 Levin "From Development to Cognitive Glue" (Bioelectricity 8:2, canonical programmatic self-summary); -004 Friston "Self-orthogonalizing attractor neural networks emerging from the FEP" (Spisak & Friston, arXiv 2505.22749; Neurocomputing 2026: Hopfield/Boltzmann dynamics derived from rather than posited).
  Context: 2026-07-27 cowork summary, "Four new proposals surfaced" bullet and "Pipeline Status" (Proposals pending Tom's review: 16).
  Type: empirical / architectural
  Related decisions: none
  Related items: ASSUMPTION-544, ASSUMPTION-550, OPEN-136
  Testability: testable empirically / in-house -- count inbox/proposals/pending/ and confirm the four 2026-07-27 files and the total of 16.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-556
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-27 proposal intake report and pipeline-status count. [stated]
    Current status: UNTESTED

ASSUMPTION-557:
  Date identified: 2026-07-27
  Statement: "Levin's virtual governor -- abstract, non-physical, embodied in the coordinating relationships among agents, causally instructive -- is close to a formal description of what a tradition is in your accelerator/detector architecture. Worth asking whether it belongs as a CROSS entry, and whether the PRS lattice is itself a virtual governor in Levin's sense." Separately: "PROP-...-002 argues novelty search and the FEP make the same mistake in opposite directions ... you now have two decidable formal questions pointed at the Friston tradition from two directions. PREMISE-129 tells you how to settle both: proof or derivation with a checker attached, not an agent's verdict."
  Context: 2026-07-27 cowork summary, "For Morning Discussion" items 3 and 4.
  Type: architectural / epistemic
  Related decisions: none
  Related items: ASSUMPTION-553, ASSUMPTION-556, PREMISE-127, PREMISE-129, OPEN-136
  Testability: testable via literature and empirically -- whether the virtual-governor construct's transfer conditions hold for a research tradition; whether a proof/derivation can be produced for either formal question.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-557
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated proposals that the virtual governor describes a tradition and that two formal Friston-facing questions are now decidable by proof. [stated]
    Current status: UNTESTED

ASSUMPTION-558:
  Date identified: 2026-07-27
  Statement: "Adopt the external-referent rule -- it's a one-line policy that closes a HIGH-priority monitor. MONITOR-486 says explicitly what would resolve it: either you spot-check INCORPORATED premises against external referents, or a policy is adopted requiring every INCORPORATE to name one. The pipeline already behaved as if the rule existed today (PREMISE-129 in, PRESUMPTION-554 held at MONITOR for lacking a referent). Making it explicit costs a sentence and retires a standing self-exemption worry (REVISE-246 / OPEN-139)."
  Context: 2026-07-27 cowork summary, "For Morning Discussion" item 2 and "New Open Questions" candidate 1.
  Type: methodological / normative
  Related decisions: none (proposed, not adopted)
  Related items: ASSUMPTION-554, PREMISE-124, MONITOR-486, REVISE-246, OPEN-139
  Testability: testable empirically / in-house -- whether the policy is adopted and whether a decorrelated spot-check (human or different model) is actually performed on INCORPORATED premises.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-558
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated policy recommendation and its stated resolution condition for MONITOR-486. [stated]
    Current status: UNTESTED

ASSUMPTION-559:
  Date identified: 2026-07-27
  Statement: The transmission layer failed for a FIFTH consecutive sync, and for the first time BOTH connected Chrome browsers are signed out: "At 18:40 EDT both connected Chrome browsers were signed out of claude.ai. Browser 1 (97286349...) and Browser 2 (42c9fd50...) each redirected /recents -> /logout. This is the fifth consecutive failed sync (07-25 evening, 07-26 morning, 07-26 evening, 07-27 morning, 07-27 evening), same root cause every time. An autonomous agent may not sign in." Consequence stated: "Chat has had no Cowork context since 07-24."
  Context: 2026-07-27 cowork summary delivery banner; chat_to_cowork/2026-07-27_chat_summary.md failure record; "For Morning Discussion" item 5.
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-536, ASSUMPTION-547, PRESUMPTION-541, PRESUMPTION-547, PRESUMPTION-550, OPEN-135
  Testability: testable empirically / in-house -- sign one Chrome into claude.ai, leave it running with the extension connected at scheduled times, and observe whether syncs resume.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-559
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-27 delivery banner (both browsers signed out) and the morning chat-scrape failure record. [stated]
    Current status: UNTESTED

ASSUMPTION-560:
  Date identified: 2026-07-27
  Statement: Agent 16 (deferred/watch monitor) is at steady state and ran one day early of the due date; two items are WATCHING (WATCH-002 Wright, WATCH-003 Rohr) and both fall due tomorrow, 2026-07-28 -- their first re-check since intake; all three intake channels clean. Separately, the morning walk handoff found no walk notes, generated the briefing from wiki state alone, and recorded a NEW count divergence: master-wiki canonical counts (511 PRS triplets / 165 connections / 54 findings) against that run's raw greps (609 PRS lines / 132 CROSS / 110 FINDING), resolved by using the canonical numbers because "the file itself calls this a known counting artifact."
  Context: 2026-07-27 cowork summary "Agent 16" bullet; "Morning walk cowork handoff" scheduled-run transcript (2026-07-27 briefing).
  Type: empirical / methodological
  Related decisions: none
  Related items: ASSUMPTION-539, ASSUMPTION-546, PRESUMPTION-528, PRESUMPTION-549, OPEN-112, WATCH-002, WATCH-003
  Testability: testable empirically / in-house -- read deferred/watch_list.md for the 07-27 run log and due dates; recompute PRS/CROSS/FINDING counts and reconcile against the master wiki's canonical line.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-560
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Agent 16 status bullet and the morning-handoff transcript's stated counting-artifact resolution. [stated]
    Current status: UNTESTED

ASSUMPTION-561:
  Date identified: 2026-07-28
  Statement: "One substantial build increment, one clean agent run, and one important non-event." No attended Cowork session occurred (autonomous day #23); "Key Decisions Made: None. `decisions.md` is unmodified since 2026-07-20"; "New Open Questions: None recorded... the file still ends at OPEN-139." Method stated explicitly: "No session transcript was read. `list_sessions` returns 2,613 sessions with no timestamps exposed, so today's interactive session could not be isolated reliably. This summary is reconstructed from artifacts."
  Context: 2026-07-28 cowork_to_chat summary, opening section, "Key Decisions Made", "New Open Questions", and the fail-loud run notes.
  Type: architectural / empirical
  Related decisions: none (23rd consecutive day with no new DECISION)
  Related items: ASSUMPTION-549, PRESUMPTION-482, PRESUMPTION-533, PRESUMPTION-535, PRESUMPTION-549
  Testability: testable empirically / in-house -- confirm no pre-EOD 07-28 changelog or snapshot existed; confirm decisions.md unchanged since 07-20 and open_questions.md unchanged since 07-23.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-561
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated day-type, the stated null results for decisions and open questions, and the stated reconstruction method. [stated]
    Current status: UNTESTED

ASSUMPTION-562:
  Date identified: 2026-07-28
  Statement: CCL Community Explorer increment 2 shipped, and the diagnosis inverts three earlier entries that had called it "cheap": "the grammar, the verbs and the engine needed *nothing*. The shell's roster reader could not read the page at all -- the fifth instance of the same failure mode, and the first one located in the shell rather than in a manifest." Cause: "SV generalised filters off the Sociogram's `groupVisibility` and landed on `prs_3d`'s conventions instead... Community Explorer holds the same information in `const activeTypes = new Set(...)`: lexically bound... and a Set." Fix: "a section may now declare `keys` (a selector + an attribute) and the roster comes off the controls, with reads off `.checked`." Conclusion recorded: "the general case was always 'read the controls,' and reading a window map was `prs_3d`'s special case wearing the shared road's clothes." Gate: "161 engine + 328 shell green"; coverage "21 controls -- 10 covered, 4 excluded, 7 deferred, 0 uncovered (was 17 deferred)"; "Not one line of `community_explorer.html` or the nested `community/` app changed."
  Context: 2026-07-28 cowork summary item 1; `architecture/voice_guide_redesign.md` SX.
  Type: architectural / methodological
  Related decisions: none
  Related items: ASSUMPTION-543, PRESUMPTION-566, PRESUMPTION-575
  Testability: testable empirically / in-house -- read voice_guide_redesign.md SX; re-run the 161+328 gate; diff community_explorer.html against its prior revision to confirm zero page-side edits.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-562
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated increment report, its stated root cause, its stated fix and its stated gate/coverage figures. [stated]
    Current status: UNTESTED

ASSUMPTION-563:
  Date identified: 2026-07-28
  Statement: "Two things only running it could have said": (1) "`click()` is an `HTMLElement` method. The first SVG roster got `el.click is not a function`, and the guide reported failure to open something a mouse opens fine. A dispatched `MouseEvent` is what a mouse actually delivers and reaches d3's `addEventListener` handler." (2) "`unresolved` was one error code answering several questions. With filters real on a second tab, `only levin` there stopped being *unsupported* and became *unresolved*, and fell into a generic 'Could not find.' The engine now carries the verb."
  Context: 2026-07-28 cowork summary item 1, the two run-only findings.
  Type: architectural / methodological
  Related decisions: none
  Related items: ASSUMPTION-562, PRESUMPTION-566
  Testability: testable empirically / in-house -- confirm the dispatched-MouseEvent path in the engine and the verb-carrying error taxonomy in the shell; confirm the Connectome row's improvement.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-563
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated claim that these two findings were only obtainable by execution rather than by reasoning. [stated]
    Current status: UNTESTED

ASSUMPTION-564:
  Date identified: 2026-07-28
  Statement: Three capabilities were "deliberately not declared, with reasons on the record": "`find`/clear (this page's search *highlights* -- `applyLens` dims to 0.08 -- so the cut dimension must learn 'highlighted, not hidden' first); `zoom`/`pan` (reasoned from d3 v7's behaviour but not run -- prove one dispatched wheel before declaring a `d3zoom` camera kind); `#btn-hold`/`#btn-names` (toggle buttons carrying `.on`; this makes Connectome increment 3 a prerequisite, not a parallel track)."
  Context: 2026-07-28 cowork summary item 1, final paragraph; "What's Next" items 2 and 3.
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-562, ASSUMPTION-563, PREMISE-129
  Testability: testable empirically / in-house -- confirm the three non-declarations in SX; confirm whether a dispatched wheel event on `#graph` is subsequently run before a `d3zoom` kind is declared.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-564
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated non-declarations and the stated reason for each, including the reasoned-but-not-run reservation. [stated]
    Current status: UNTESTED

ASSUMPTION-565:
  Date identified: 2026-07-28
  Statement: "Agent 16 re-checked both watch items -- the first re-check since intake. Both executed properly and both came back NOT MET." WATCH-002 (Wright): "source URL fetched (HTTP 200, 53KB); `entry-content` holds exactly one element, a YouTube embed figure... `article:modified_time` still 2026-07-17 -- page unchanged since publication. New this check: the embed is YouTube video `vshC_TxwrVo`, not audio-only. Auto-captions are a transcript route the original check method never contemplated, and the check method has been extended to include it." WATCH-003 (Rohr): "`review/archive/` unchanged at 16 files... No review pass has run since 07-23, so this item structurally cannot move until you next review."
  Context: 2026-07-28 cowork summary item 2; `deferred/watch_list.md` (both items updated today).
  Type: empirical / methodological
  Related decisions: none
  Related items: ASSUMPTION-560, ASSUMPTION-566, ASSUMPTION-567, OPEN-133, WATCH-002, WATCH-003
  Testability: testable empirically / in-house -- read deferred/watch_list.md for the 07-28 run entries and the extended check method; re-fetch the WATCH-002 source and confirm the YouTube id.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-565
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated Agent 16 re-check results, the stated new transcript route, and the stated structural coupling of WATCH-003 to the review pass. [stated]
    Current status: UNTESTED

ASSUMPTION-566:
  Date identified: 2026-07-28
  Statement: "`tools/generate_review_page.py` is unmodified since 2026-05-18. Line 304 still reads: `const pids = {[f'PROP-{run_date}-{i+1:03d}' for i in range(len(proposals))]!r};` ... That is exactly the defect -- pids synthesized as `run_date` + a sequence counter, with no reference to the actual card set. This is the fourth consecutive day it has been the top item, and today's pending set makes it worse rather than better: 18 real proposals spanning 07-21 through 07-28, against which the generator would emit 18 sequential `PROP-2026-07-28-NNN` ids of which two exist." Fix stated: "emit pids from the real card set, and add a reconciliation assertion that recomputes decision records against the actual proposal list and can fail (there is currently no `assert` anywhere in the file)."
  Context: 2026-07-28 cowork summary, "For Morning Discussion" item 1.
  Type: architectural / empirical
  Related decisions: none
  Related items: ASSUMPTION-550, ASSUMPTION-551, PREMISE-128, PREMISE-130, PREMISE-131, PRESUMPTION-557, PRESUMPTION-558
  Testability: testable empirically / in-house -- read line 304 of tools/generate_review_page.py; confirm mtime 2026-05-18; grep the file for `assert`; count pending proposals against the pid range the generator would emit.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-566
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the quoted source line, the stated unmodified-since date, the stated 18-vs-2 arithmetic, and the stated two-part fix. [stated]
    Current status: UNTESTED

ASSUMPTION-567:
  Date identified: 2026-07-28
  Statement: "No review page was generated today at all. `review/` still tops out at `2026-07-27_review.html` (written 07-27 04:38). The 04:38 scheduled run produced nothing today. I did not diagnose why -- flagging it rather than guessing."
  Context: 2026-07-28 cowork summary, "For Morning Discussion" item 1, first consequence.
  Type: empirical / architectural
  Related decisions: none
  Related items: ASSUMPTION-566, ASSUMPTION-565, PRESUMPTION-570
  Testability: testable empirically / in-house -- list review/*.html and confirm the newest is 2026-07-27; inspect the 04:38 scheduled task's run record for an error or a silent no-op.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-567
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated absence of today's review page and the explicit statement that the cause was flagged rather than diagnosed. [stated]
    Current status: UNTESTED

ASSUMPTION-568:
  Date identified: 2026-07-28
  Statement: "The Chat sync failed again -- sixth consecutive day, and it's now costing you both directions." Morning: "This morning's Chat->Cowork scrape (14:02) hit the claude.ai login screen on *both* connected Chrome instances... 'No Chat context is available to Cowork sessions for 2026-07-28.'" Evening: "Browser delivery: ATTEMPTED AND FAILED... only one browser is now connected (`Browser 1`, macOS, local -- `Browser 2` has dropped off entirely since this morning). Navigated to `https://claude.ai/recents` at 18:42 EDT; the site redirected to `https://claude.ai/login?from=logout`." Consequence stated: "the walk conversation has had no Cowork context since 07-24, *and* Cowork has been running on 07-27's Chat context all day." Fix stated as five minutes.
  Context: 2026-07-28 cowork summary "For Morning Discussion" item 2 and the fail-loud run notes; 2026-07-28_chat_summary.md.
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-536, ASSUMPTION-547, ASSUMPTION-559, PRESUMPTION-541, PRESUMPTION-547, PRESUMPTION-550, PRESUMPTION-571, OPEN-135
  Testability: testable empirically / in-house -- sign one Chrome into claude.ai, leave it running with the extension connected at scheduled times, and observe whether either direction resumes.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-568
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the two stated failure records (14:02 scrape, 18:42 delivery), the stated drop of Browser 2, and the stated bidirectional consequence. [stated]
    Current status: UNTESTED

ASSUMPTION-569:
  Date identified: 2026-07-28
  Statement: The 15a/15b/15c pipeline dispositioned eight items (PRESUMPTION-557..563, 565) with a batch mix of "5 INCORPORATE (PREMISE-130,131,132,133,134) - 3 MONITOR (487,488,489) - 3 REVISE (247,248,249) - 1 SYSTEMIC-RISK-FLAG (High) - 0 NOVELTY"; running totals "PREMISE -> 134 - MONITOR -> 489 - REVISE -> 249 - DISPOSITION -> 548." Decorrelation claimed with two stated signals: "(a) 15b REFUTED 15a on PRESUMPTION-561 on a checkable factual point; (b) both directions independently refuted the same 14b sub-argument on PRESUMPTION-565. The searches were not merely agreeing. Residual correlation (same model family) still applies -- MONITOR-486 stands." On the count jump: "all five name external referents outside the pipeline, per the PRESUMPTION-556 / REVISE-246 bar."
  Context: `architecture/lit_search_returns.md`, 2026-07-28 run header, dispositions 540-548 and the running-totals footer.
  Type: methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-552, ASSUMPTION-555, ASSUMPTION-558, MONITOR-486, PRESUMPTION-567, PRESUMPTION-569
  Testability: testable empirically / in-house -- count lit_search_results/{for,against}/ files for the eight items; read DISPOSITION-540..548 and confirm the register landings and totals.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-569
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated batch mix, stated running totals, and the stated decorrelation signals and their stated residual caveat. [stated]
    Current status: UNTESTED

ASSUMPTION-570:
  Date identified: 2026-07-28
  Statement: For the first time, a verification pass was run by a separate instance: "VERIFICATION PASS -- 2026-07-28, independent agent (decorrelated instance, not 15a/15b/15c)... Structural checks 1-6 PASS... CITATION SPOT-CHECK (7 of the batch's load-bearing citations re-checked against primary venues): all 7 verified exact, including page ranges and the two quantitative figures... No fabricated or misattributed citation. This matters reflexively: the same batch minted PREMISE-132 ('citing is not verifying'), and the check was run BY A DIFFERENT INSTANCE than the one that wrote the citations, per PREMISE-132's decorrelation requirement -- an in-batch application of the premise, not merely an assertion of it." Six defects were found and corrected in PREMISE-133, "all drafting/rigour, not a wrong disposition," and "Recorded rather than quietly fixed, per PREMISE-006."
  Context: `architecture/lit_search_returns.md`, VERIFICATION PASS section, 2026-07-28.
  Type: methodological / epistemic
  Related decisions: none
  Related items: ASSUMPTION-554, ASSUMPTION-558, PREMISE-132, PREMISE-006, MONITOR-486, PRESUMPTION-559, PRESUMPTION-567, PRESUMPTION-568
  Testability: testable empirically / in-house -- read the verification section; independently re-check two of the seven citations; confirm the six corrections are present in PREMISE-133 and in DISPOSITION-543.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-570
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated verification-pass results, the stated decorrelation rationale, and the stated defect list and its stated classification. [stated]
    Current status: UNTESTED

ASSUMPTION-571:
  Date identified: 2026-07-28
  Statement: Two fail-loud self-corrections were stated. (1) "FAIL-LOUD NOTE: incorporating PREMISE-133 puts the pipeline formally out of compliance with its own newest premise, because MONITOR-486 has no discharge rule as of this run. Stated, not deferred. See REVISE-247." (2) PRESUMPTION-561 was refuted: "The presumption's central technical premise is FALSE. Little's Law does not presuppose a service process or an obligatory consumer -- it needs only a system boundary, arrivals and departures -- so applying it to a register with positive arrivals and zero departures is a correct application, not a category error." Disposition REVISE-248, with direction stated: "this CONFIRMS rather than relieves the backlog concern (DISPOSITION-536 / PRESUMPTION-553 stands)." A second 14b inferential error was recorded inside MONITOR-489 (PRESUMPTION-565's non-uniform-direction sub-argument, "refuted CONVERGENTLY by both directions").
  Context: `architecture/lit_search_returns.md`, DISPOSITION-543, DISPOSITION-544, DISPOSITION-547.
  Type: epistemic / methodological
  Related decisions: none
  Related items: PRESUMPTION-561, PRESUMPTION-565, PREMISE-133, REVISE-247, REVISE-248, MONITOR-486, MONITOR-489, DISPOSITION-536
  Testability: testable empirically / in-house -- read REVISE-247/248 and MONITOR-489; verify Little & Graves 2008 on whether the law requires a service process; confirm whether MONITOR-486 acquires a discharge rule.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-571
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated non-compliance note and the two stated refutations of prior 14b inferences. [stated]
    Current status: UNTESTED

ASSUMPTION-572:
  Date identified: 2026-07-28
  Statement: "The Hawkins proposal lands directly on the concept C2A2 leans on hardest. PROP-2026-07-28-001... contains a claim the Hawkins wiki does not hold anywhere: the thalamus is a reference-frame transformer, not a relay -- converting egocentric sensory coordinates to object-centric ones, with cortico-thalamic feedback specifying *which* transform. Since PRS triplets are read as reference frames in this architecture (PROP-2026-04-09-SUPP-001), a proposed biological mechanism for performing reference-frame transformation is load-bearing, not incidental. It's also falsifiable: thalamic activity should track cortically-inferred object identity/pose, not sensory input alone." Second triplet: "hierarchy re-purposed to encode composition rather than abstraction... which answers the standing objection that 'every column models whole objects' makes hierarchy explanatorily idle."
  Context: 2026-07-28 cowork summary, "For Morning Discussion" item 3; `inbox/proposals/pending/2026-07-28_hawkins_heterarchy-thalamic-transform-explainer.md`.
  Type: empirical / architectural
  Related decisions: none
  Related items: PREMISE-127, PREMISE-134, PRESUMPTION-572, PROP-2026-04-09-SUPP-001
  Testability: testable via literature -- arXiv:2507.05888 and the thalamic reference-frame-transformation claim against the thalamus-as-relay literature; the stated falsifier is an empirical prediction about thalamic activity.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-572
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated claim, its stated load-bearing status for the PRS-as-reference-frame reading, and its stated falsifier. [stated]
    Current status: UNTESTED

ASSUMPTION-573:
  Date identified: 2026-07-28
  Statement: "The Hoffman proposal is the one to be careful with -- and its author says so. PROP-2026-07-28-002 flags an unpublished 2025 Hoffman essay... listed on the Trace Institute publications page with no link, DOI, or PDF. The essay text was not retrievable, and the proposal marks its own triplet Confidence: Speculative and labels it 'a hypothesis about the source, not an extraction from it.' That's the right handling, and it's the honest version of what PROP-2026-07-19-003 got wrong." Stated reason it matters: "it would apparently be the single document where Hoffman runs all three lines -- amplituhedron/'spacetime is doomed,' Fitness-Beats-Truth, and trace logic -- as one convergent argument... if the three lines are genuinely independent, it's convergence-across-independent-methods... if they aren't, it exposes a shared hidden premise." Proposal put to Tom: "Worth deciding whether 'unretrievable but well-described source' gets its own disposition category, distinct from both APPROVE and DENY."
  Context: 2026-07-28 cowork summary, "For Morning Discussion" item 4; `inbox/proposals/pending/2026-07-28_hoffman_spacetime-headset-essay.md`.
  Type: epistemic / methodological
  Related decisions: none (proposed, not adopted)
  Related items: PREMISE-132, PRESUMPTION-573, WATCH-002, WATCH-003
  Testability: testable empirically / in-house (whether the category is adopted; whether the essay is later retrievable) and via literature (handling of unretrievable sources; convergence across independent methods as an evidence form).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-573
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated non-retrievability, the stated self-assigned confidence, and the stated proposal for a third disposition category. [stated]
    Current status: UNTESTED

ASSUMPTION-574:
  Date identified: 2026-07-28
  Statement: A methodological generalization was stated as possibly applying past the voice guide: "The failure today was a *generalisation that had only ever seen two examples* -- it abstracted the Sociogram's conventions, met `prs_3d`, and encoded that page's globals as the shared road. Five instances in, the actual general case turned out to be 'read the rendered controls,' which is also the epistemically honest one. There's a straight line from that to the external-referent rule you've been circling (MONITOR-486, PREMISE-129): a generalisation is only as good as its worst-covered instance, and the check has to be *run against the world*, not asserted. Might be worth stating once as policy rather than rediscovering per-tab." Stated alongside: "Token budget breached. Per-task budget is 4,000 tokens; this run used roughly 45,000 in gathering... Surfacing rather than hiding it"; and the stated warrant for artifact reconstruction, "which per `fact_inventory.md`'s own rule are the authoritative record anyway. Anything that happened today and left no artifact is not in this summary." Carried-and-unresolved items were restated unchanged, including metric inflation at a 7th consecutive flag and the ~174-item monitor backlog.
  Context: 2026-07-28 cowork summary, "For Morning Discussion" items 5 and 6, and the fail-loud run notes.
  Type: methodological / epistemic
  Related decisions: none (proposed, not adopted)
  Related items: ASSUMPTION-558, ASSUMPTION-561, PREMISE-129, PREMISE-132, MONITOR-486, PRESUMPTION-566, PRESUMPTION-574, OPEN-112
  Testability: testable empirically / in-house (whether the policy is stated once rather than rediscovered; whether the connectivity metric is split) and via literature (when an inductive generalization is warranted from n instances).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-574
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated cross-domain moral, the stated budget breach, the stated warrant for artifact-based reconstruction, and the restated carried items. [stated]
    Current status: UNTESTED

ASSUMPTION-575:
  Date identified: 2026-07-29
  Statement: "No attended Cowork session is evident in the vault. Every file touched today (35 files) traces to a scheduled agent. Also: this morning's chat→cowork scrape **failed — claude.ai is logged out** in the Chrome profile the extension is attached to, so today's agents had no Chat context from yesterday's walk. That same logout will likely block browser delivery of this summary. **The file is the deliverable — read it here if it never reached Chat.**" And, on decisions: "None. Register still stands at DECISION-078 (2026-07-05). Today's work was all agent-side; nothing reached a decision that needed you." And on questions: "No new OPEN-NNN entries."
  Context: 2026-07-29 cowork→chat summary header, "Key Decisions Made", "New Open Questions". Autonomous day #24.
  Type: architectural / empirical
  Related decisions: none (no new DECISION; register at DECISION-078)
  Related items: ASSUMPTION-561, PRESUMPTION-482, PRESUMPTION-571, PRESUMPTION-574, OPEN-135
  Testability: testable empirically / in-house (file-touch census; whether any 07-29 artifact traces to an attended turn; login state of the Chrome profile).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-575
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated day-shape note, the stated decision and open-question nulls, and the stated delivery failure. [stated]
    Current status: UNTESTED

ASSUMPTION-576:
  Date identified: 2026-07-29
  Statement: "PRESUMPTION-566, 567, 568, 569, 570, 572, 573, 575 were searched FOR and AGAINST and dispositioned. Only **1 INCORPORATE** out of 8 (PREMISE-135) — and 15c explicitly refused to narrate that as evidence of its own rigour, because the previous run's 5-of-N was already being wrongly narrated as a 'fivefold rise.' The correction is filed as REVISE-250 and applied reflexively to this run's own count." Running totals as stated in the queue file: "PREMISE → 135 · MONITOR → 492 · REVISE → 251 · DISPOSITION → 559," with DISPOSITION-549..559 and "1 INCORPORATE · 6 items MONITORed across 3 entries (MONITOR-490 cohort A-D, 491, 492) · 1 REVISE (REVISE-250) · 3 SYSTEMIC-RISK-FLAGs accepted and consolidated into REVISE-251 · 0 NOVELTY."
  Context: 2026-07-29 lit-search batch (Agents 15a/15b/15c), reported in the cowork summary and in for_lit_search.md's run header.
  Type: methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-569, PREMISE-135, REVISE-250, REVISE-251, MONITOR-490, MONITOR-491, MONITOR-492, PRESUMPTION-569, PRESUMPTION-578
  Testability: testable empirically / in-house (count the 16 result files; read DISPOSITION-549..559; confirm the four running totals).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-576
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated batch composition, the stated refusal to narrate the count, and the stated register totals. [stated]
    Current status: UNTESTED

ASSUMPTION-577:
  Date identified: 2026-07-29
  Statement: PREMISE-135, the run's only INCORPORATE, states: "TERMINALITY IS PURCHASED BY ENUMERATING THE DOMAIN, NOT BY ACCUMULATING INSTANCES. A correction that supersedes a series of earlier abstractions may not be declared 'the general case' on the strength of covering every instance seen so far, because that is the same standing each superseded abstraction had at the moment it was written." It requires three things — "(a) THE POPULATION... (b) THE TERMINATION CRITERION... (c) ONE SEVERE TEST, a correct advance prediction about at least one kind that was NOT among the instances that produced the abstraction." Its stated SCOPE GUARD refutes the source presumption's central inference: "PROCEDURE-IDENTITY IS NOT A DEFEATER... 'It was reached by the same method as the four it replaced, therefore it inherits their standing' is a genetic inference and is NOT incorporated." Its SYMMETRY CLAUSE: "the operative action is to NAME the worst-covered instance of the NEW abstraction and go and look at it, not to withhold adoption." Confidence: Moderate; re-check due 2026-10-29.
  Context: DISPOSITION-549; validated_premises.md PREMISE-135, minted from PRESUMPTION-566 (14b's 07-28 item on the fifth abstraction).
  Type: epistemic / methodological
  Related decisions: none
  Related items: PRESUMPTION-566, PREMISE-101, PREMISE-105, PREMISE-127, PREMISE-129, PREMISE-134, ASSUMPTION-562, ASSUMPTION-574
  Testability: testable via literature (already searched: Norton 2003/2021; Lakatos 1976; Mitchell 1982; Mayo 2018; Hájek 2007; Card 2017) and empirically / in-house (the named OPEN MEASUREMENT: enumerate remaining page kinds, predict in advance, then check).
  Status: SUPPORTED (incorporated as PREMISE-135; source presumption's parity inference refuted)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-577
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from the newly validated premise, including the scope guard that refutes its own source item. [stated]
    Current status: SUPPORTED

ASSUMPTION-578:
  Date identified: 2026-07-29
  Statement: "**REVISE-251 consolidates three separate HIGH systemic-risk flags into one**, on the grounds that three tracked items lower the odds any is acted on (PREMISE-121). All three name the same defect in 14b's presumption construction: filing a hazard without naming the quantity that would settle it. Sub-flags: categorical-parity/binary-not-graded (566+567), favourable-direction-without-a-null-model (568+569, and 565 failed the same way inverted), gate-vs-grade (570+572, neither budgeting the cost of the check it demands)." The stated remedy is a single intake rule: "before a presumption is filed, it must name the QUANTITY that would settle it — a stopping criterion, a dependence estimate, a miss rate, a null model with a denominator, or the cost of the check it demands. Absent that quantity, the observation is filed as a PROMPT TO INVESTIGATE and does not consume a literature search." Stated urgency HIGH. Each sub-flag retains DISPOSITION-557/558/559 "so nothing is lost to consolidation."
  Context: REVISE-251 (revision_flags.md, 2026-07-29 intake); three 15b systemic-risk flags over a 14b-origin cohort.
  Type: methodological / architectural
  Related decisions: none (recommended, not adopted)
  Related items: PREMISE-121, PREMISE-124, PREMISE-114, REVISE-249, MONITOR-490, PRESUMPTION-565, PRESUMPTION-566, PRESUMPTION-567, PRESUMPTION-568, PRESUMPTION-569, PRESUMPTION-570, PRESUMPTION-572, PRESUMPTION-576, PRESUMPTION-580
  Testability: testable empirically / in-house (whether the intake rule is adopted at 14b; whether items filed as prompts-to-investigate are tracked separately) and via literature (the three named inference forms have already been searched in this batch).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-578
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the consolidation note, the three sub-flag findings, and the stated single-rule remedy. Note that the flagged agent is 14b, this agent's sibling. [stated]
    Current status: UNTESTED

ASSUMPTION-579:
  Date identified: 2026-07-29
  Statement: "**MONITOR-490 found 4 of 8 items were already governed by an ACTIVE premise.** Between that and the three unsound inference forms, a majority of the batch was avoidable at intake." The register entry states it more strongly: "In each case a premise already ACTIVE in the register governs the situation exactly, was validated before this run, and was NOT applied. The literature searches were therefore substantially redundant with work the pipeline had already banked — which is the propagation failure PREMISE-116 and PREMISE-123 describe and REVISE-245 has been open on since 2026-07-24, observed here as four simultaneous instances." Stated remedy: "before an item is routed to 15a/15b, grep the validated-premise register for a governing premise." Filed as one cohort per PREMISE-121, instances A–D = PRESUMPTION-567, 570, 573, 575.
  Context: MONITOR-490 (monitor_queue.md, 2026-07-29); DISPOSITION-550, 553, 555, 556.
  Type: architectural / methodological
  Related decisions: none
  Related items: PREMISE-105, PREMISE-116, PREMISE-121, PREMISE-123, REVISE-245, REVISE-251, PRESUMPTION-579
  Testability: testable empirically / in-house (re-run the register check over the last N batches and count how many items had a governing ACTIVE premise; whether the pre-check is added to intake).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-579
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the cohort-level claim and the stated pre-check remedy. [stated]
    Current status: UNTESTED

ASSUMPTION-580:
  Date identified: 2026-07-29
  Statement: "**The gate-vs-grade tension is live, not theoretical.** REVISE-251 asks for a general move from binary gates to graded assessment — but PREMISE-124 (external baseline or UNCALIBRATED) and PREMISE-114 (authority as a documented chain) are *binary* standards, were flagged for review under REVISE-249 on 07-28, and **neither has been edited**. This run relied on PREMISE-124 in its binary form **four times**. 15c's warning is the one to carry on the walk: *do not let the graded reading take effect by drift.* REVISE-249 and REVISE-251 are one decision, not two." The register entry names the four uses: "DISPOSITIONS 552, 555, 556, and as the INCORPORATE bar on 549."
  Context: 2026-07-29 cowork summary, "For Morning Discussion" item 3; REVISE-251's "TENSION SURFACED RATHER THAN RECONCILED" clause.
  Type: epistemic / architectural
  Related decisions: none (two flags open, neither actioned)
  Related items: PREMISE-114, PREMISE-124, PREMISE-132, REVISE-249, REVISE-251, PRESUMPTION-586
  Testability: testable empirically / in-house (whether PREMISE-114/124 are edited, and whether the edit is signed off rather than absorbed by use).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-580
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated tension, the stated count of binary-form uses, and the stated instruction against drift. [stated]
    Current status: UNTESTED

ASSUMPTION-581:
  Date identified: 2026-07-29
  Statement: "**The review-page bug is worse than we recorded, and it is a total-loss condition right now.** Previous runs called it 'position-based decision IDs.' Agent 16 read the source (unchanged since 2026-05-18) and found it's a *half-applied* fix. Line 116 is correct — cards, buttons, badges all key off the real `proposal_id`. **Line 304 is not** — `submitDecisions()` rebuilds a purely positional array stamped with the run date... **Intersection: empty. Every decision you record would be silently discarded and the decision email would list 22 phantom ids matching no file in the vault.** One-line fix, spelled out in the watch list." Also stated: "Agent 16 also **withdrew** its earlier attribution of the 07-20 loss of PROP-2026-07-19-001 (Rohr) and -003 (Wright) to this bug — that pass didn't route through `submitDecisions()` at all, so the likelier mechanism is the manual bulk `pending/ → approved/` move dropping two items."
  Context: 2026-07-29 cowork summary "For Morning Discussion" item 1; deferred/watch_list.md TOOLING FLAG escalated 2026-07-29.
  Type: architectural / empirical
  Related decisions: none
  Related items: ASSUMPTION-566, ASSUMPTION-567, WATCH-002, WATCH-003, PRESUMPTION-581, PRESUMPTION-582
  Testability: testable empirically / in-house (read lines 116 and 304; generate a page against the 22-item queue and compare the emitted pid set with the real ids; check whether any tracked item now covers the manual-bulk-move mechanism).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-581
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the escalation and from the explicit withdrawal of a prior causal attribution. [stated]
    Current status: UNTESTED

ASSUMPTION-582:
  Date identified: 2026-07-29
  Statement: "**`watch_list.md` has crossed 256 KB and can no longer be opened by the Read tool.** Agent 16 had to read its own watch list via line-ranged shell calls. Active items + resolved index are under 2% of the file; the run log is everything else. Proposal: roll the run log into `wiki/deferred/run_log/2026-Q2.md` / `2026-Q3.md`, keep active items, resolved index, and the trailing ~14 days. No data lost. Not executed — your call." The watch list itself records the escalation as "now operationally binding" and "this has crossed from housekeeping into a working constraint."
  Context: 2026-07-29 cowork summary "For Morning Discussion" item 2; watch_list.md MAINTENANCE FLAG, escalated 2026-07-29. File measured at 275,693 bytes at this run.
  Type: architectural / empirical
  Related decisions: none (proposed, not executed — stated as needing Tom's authorisation)
  Related items: ASSUMPTION-565, PREMISE-100, PRESUMPTION-584
  Testability: testable empirically / in-house (attempt a Read; measure the file; measure the active-item fraction).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-582
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the escalated maintenance flag and the stated archival proposal. Byte size independently confirmed this run. [stated]
    Current status: UNTESTED

ASSUMPTION-583:
  Date identified: 2026-07-29
  Statement: "**Two report blind spots in one day.** `qc_sweep report` said `needs_review: 0` when 9 syntheses were stale; the review page reports decisions under ids that don't exist. In both cases the *underlying data was fine* and the *reporting layer lied*. Worth asking whether that's a coincidence or a pattern in how these tools were built — it bears directly on PREMISE-124's calibration worry." The Summa line states the first instance concretely: "the QC report lied again — `qc_sweep report` returned `needs_review: 0` while a direct frontmatter scan found **9 syntheses past the 7-day staleness line**."
  Context: 2026-07-29 cowork summary "For Morning Discussion" item 4 and the Summa reviewer paragraph.
  Type: epistemic / architectural
  Related decisions: none (framed as a question, not a finding)
  Related items: PREMISE-124, PREMISE-130, ASSUMPTION-581, PRESUMPTION-583
  Testability: testable empirically / in-house (enumerate the reporting surfaces in `tools/` and test each against a direct scan of its own substrate) and via literature (whether co-occurrence of two reporting defects supports a common-cause reading — note this run's own REVISE-250 bears on that inference form).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-583
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated pairing and the stated question about whether it is a pattern. [stated]
    Current status: UNTESTED

ASSUMPTION-584:
  Date identified: 2026-07-29
  Statement: "**Summa commentary reviewer — 6 pairs, 3 rewrites, 3 escalations.** Day 130 (Q.24 locus a.3→a.2, plus Aquinas's own limit on Q.25 a.3), Day 145 (banned possessive cleared — off the backlog), Day 146 (possessive cleared, residual bridge escalated). Day 129 passed clean. **Day 057 is the real find:** its Bridges section cites *no ids at all* — five bullets of correctly-glossed prose with nothing to verify, which is why every prior id-vs-gloss audit passed it. Day 143: McGilchrist PRS-05→PRS-01 gloss drift." And: "**Day 057 Summa authorship** — supplying six missing bridge ids is authorship, not cleanup; the reviewer correctly refused. Needs you or a scoped session."
  Context: 2026-07-29 cowork summary, Summa reviewer paragraph and "What's Next" item 4.
  Type: methodological / empirical
  Related decisions: none
  Related items: PREMISE-114, ASSUMPTION-583, PRESUMPTION-584
  Testability: testable empirically / in-house (sweep every synthesis for zero-id Bridges sections; re-run the id-vs-gloss audit with a zero-id assertion that can fail).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-584
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the reviewer's stated findings and from the stated refusal to supply missing ids. [stated]
    Current status: UNTESTED

ASSUMPTION-585:
  Date identified: 2026-07-29
  Statement: "**Failed:** OpenStory feed refresh — freshness guard tripped, DB last write 2026-07-27T10:09Z (48h, threshold 36h). Runtime writer likely down. Feeds NOT refreshed." And: "**Restart the OpenStory runtime writer** — feeds are 48h stale and the guard will keep failing nightly until the DB gets a write." Also stated as regenerated cleanly: "heartbeat digest (13:21, snapshot `digest-20260729-125333`), metabolism view + data (06:04)."
  Context: 2026-07-29 cowork summary, "What Was Accomplished Today" / "What's Next" item 3; agents/openstory/REFRESH_STATUS.md.
  Type: architectural / empirical
  Related decisions: none
  Related items: PREMISE-100, PRESUMPTION-585
  Testability: testable empirically / in-house (read REFRESH_STATUS.md; query the DB's last write; confirm the 36h threshold and the guard's behaviour).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-585
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated guard trip, the stated staleness figures, and the stated attribution to the runtime writer. [stated]
    Current status: UNTESTED

ASSUMPTION-586:
  Date identified: 2026-07-29
  Statement: "**Proposal harvest — 4 new (2 Kastrup, 2 McGilchrist).** PROP-2026-07-29-001 through -004: McGilchrist on IAI ('great discoveries are not made by following the scientific method') and the two-part ABC *Soul Search* series; Kastrup's Rupert Spira dialogue and his caution to young philosophers. Pending queue now **22** (was 18 at Agent 16's run this morning)." And: "**Review pass on the 22-item pending queue** — last pass was 2026-07-23, six days ago, and the queue has more than doubled. Blocked on (1)."
  Context: 2026-07-29 cowork summary; four files in inbox/proposals/pending/ dated 2026-07-29.
  Type: empirical / architectural
  Related decisions: none
  Related items: ASSUMPTION-581, MONITOR-476, WATCH-002, WATCH-003
  Testability: testable empirically / in-house (count pending/; confirm the four new files and the last review pass date). The McGilchrist scientific-method claim is a review-pipeline matter for the proposal's own adjudication.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-586
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated harvest and the stated queue arithmetic. [stated]
    Current status: UNTESTED

ASSUMPTION-587:
  Date identified: 2026-07-29
  Statement: "**A budget conflict worth naming.** The Summa reviewer reported ~350k subagent tokens against a 4k per-task budget and said plainly that the review can't be done faithfully at 4k. It surfaced rather than buried it, which is correct behaviour — but the budget and that task are in genuine conflict and one of them needs re-scoping."
  Context: 2026-07-29 cowork summary "For Morning Discussion" item 6. Continues the 07-28 breach disclosure (ASSUMPTION-574) and applies to the present run.
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-574, PRESUMPTION-587
  Testability: testable empirically / in-house (measure per-task token use across the scheduled fleet against the 4,000 budget; test whether an incremental design lowers the figure).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-587
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated conflict and the stated approval of surfacing over burying. [stated]
    Current status: UNTESTED

ASSUMPTION-588:
  Date identified: 2026-07-29
  Statement: Pipeline status as stated: "Assumptions extracted: **573** · Presumptions surfaced: **576** · Validated premises: **93** (PREMISE-135 added today) · Lit search queue: **1500 tracked / 153 never searched / 5 searched-but-not-dispositioned** · Monitor queue: **366** items · Revision flags: **108** (REVISE-250, 251 today) · Open questions: **134** · Decisions: **76** · Deferred items watching: **2** (WATCH-002 Wright, WATCH-003 Rohr — both next due 2026-08-04) · Proposals: **22 pending / 254 approved / 1 denied**." Stated alongside: "today's REVISE-251 is arguably OPEN-138's ('is the self-knowledge layer advisory-only?') answer arriving as a demand rather than a question — the pipeline is now recommending an intake rule change to itself."
  Context: 2026-07-29 cowork summary, "Pipeline Status" and "New Open Questions".
  Type: empirical / epistemic
  Related decisions: none
  Related items: ASSUMPTION-545, OPEN-112, OPEN-133, OPEN-138, PRESUMPTION-549, PRESUMPTION-586
  Testability: testable empirically / in-house (recount each register under a stated counting rule — note the standing divergence between block counts and max-ID counters, unreconciled since ASSUMPTION-545; "premises 93" is an ACTIVE-count against max ID 135, and "decisions 76" against max ID 78).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-588
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated status block and the stated reading of REVISE-251 against OPEN-138. Counter divergence noted, not resolved. [stated]
    Current status: UNTESTED

ASSUMPTION-589:
  Date identified: 2026-07-29
  Statement: "**Please sign in to claude.ai in the Chrome profile the extension uses.** Both ends of the daily sync are broken until you do: this morning's scrape failed and tonight's delivery probably will too." Confirmed in the delivery run: "`https://claude.ai/recents` redirected to `/login?from=logout` — **the Chrome profile is still signed out of claude.ai**, exactly as at this morning's 08:00 scrape. Nothing was pasted or sent; I cannot sign in on your behalf." Also stated: "**Run `sync_vault.sh`** — Day 145's fix hasn't reached the Explorer; the published copy still carries the old text."
  Context: 2026-07-29 cowork summary header and "For Morning Discussion" item 5; "What's Next" item 5. Seventh consecutive dark sync, both directions.
  Type: architectural / empirical
  Related decisions: none
  Related items: ASSUMPTION-568, PREMISE-131, OPEN-135, PRESUMPTION-571, PRESUMPTION-588
  Testability: testable empirically / in-house (restore login and observe whether either direction resumes; diff the published Explorer copy against the vault).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-589
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated request, the stated redirect evidence, and the stated unrun publish step. [stated]
    Current status: UNTESTED

ASSUMPTION-590:
  Date identified: 2026-07-30
  Statement: "**Note on the day's shape:** no attended Cowork session is evident. Every file touched today traces to a scheduled agent. This morning's chat->cowork scrape **failed -- Chrome was not running**, so today's agents ran with no Chat context from yesterday's walk." Also stated: "**No new DECISION-NNN entries today** -- `decisions.md` is unchanged since 2026-07-20"; "**No new OPEN-NNN entries today**."
  Context: 2026-07-30 cowork->chat summary, header note and "Key Decisions" / "New Open Questions". Autonomous day #25. Independently corroborated: 28 files under `wiki/` carry a 2026-07-30 mtime, none attributable to an interactive session.
  Type: architectural / empirical
  Related decisions: none
  Related items: ASSUMPTION-575, PRESUMPTION-482, PRESUMPTION-574
  Testability: testable empirically / in-house (enumerate today's file mtimes against the scheduled-task roster; confirm no interactive session wrote to the vault).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-590
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated day-shape note; corroborated against the vault mtime delta and against two session transcripts read this run (Agent 16, scheduler health). [stated]
    Current status: UNTESTED

ASSUMPTION-591:
  Date identified: 2026-07-30
  Statement: "PRESUMPTION-576, 577, 586, 588 were searched FOR and AGAINST and dispositioned. Results: 576 and 588 -> CONTESTED -> REVISE-252 / REVISE-253; 577 and 586 -> MONITOR (HIGH) -> MONITOR-493 / MONITOR-494." Running totals stated: "PREMISE -> 135 (unchanged) . MONITOR -> 494 . REVISE -> 253 . DISPOSITION -> 564." And: "15c said so rather than narrating it as rigour" -- "0-of-4 is a *backlog artifact*, not a raised bar."
  Context: 2026-07-30 changelog (15a/15b/15c section) and cowork->chat summary "What Was Accomplished Today". Continues the 07-29 refusal recorded at ASSUMPTION-576 / REVISE-250.
  Type: methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-576, PRESUMPTION-578, PRESUMPTION-589, PRESUMPTION-600
  Testability: testable empirically / in-house (recount the disposition ledger; check the four result-file pairs exist and carry the stated verdicts).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-591
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated disposition table and the stated running totals. [stated]
    Current status: UNTESTED

ASSUMPTION-592:
  Date identified: 2026-07-30
  Statement: "The headline is 586. It converges from *both* search directions on a scope extension of PREMISE-114 -- the strongest INCORPORATE candidate in the batch -- and was blocked by the register's own backlog. PREMISE-114 has been flagged for amendment since 2026-07-28 and is **unedited on day 6**, so minting the extension would be a rule taking effect by use on unratified ground, which is precisely the item's own objection." And: "**494 converts to an INCORPORATE the moment PREMISE-114 is ratified.**"
  Context: 2026-07-30 changelog "Headline" and cowork->chat "Key Decisions" / "What's Next" item 1. The gate-vs-grade backlog first flagged at ASSUMPTION-580 / REVISE-249, now at day 6 and demonstrably load-bearing.
  Type: epistemic / architectural
  Related decisions: none
  Related items: ASSUMPTION-580, PREMISE-114, PREMISE-124, PRESUMPTION-586, PRESUMPTION-589
  Testability: testable empirically / in-house (ratify or amend PREMISE-114 and observe whether MONITOR-494 converts; this is a one-step decisive test).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-592
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated block and the stated conditional conversion. [stated]
    Current status: UNTESTED

ASSUMPTION-593:
  Date identified: 2026-07-30
  Statement: "**REVISE-252** -- amend REVISE-251 action (1): the pre-commitment should name the quantity *type*, not its value; provisional value plus one licensed post-search revision; sanction is deprioritisation." Stated prior question: "is the pre-commitment rule a *device* or *admission control*? This is the prior question and it maps onto a PREMISE-106 tension... The proposed fix (name the quantity type, not the value) only makes sense under the first reading."
  Context: 2026-07-30 changelog "For Tom" item 1 and cowork->chat "For Morning Discussion" item 2. Direct amendment of REVISE-251, minted 07-29 (ASSUMPTION-578).
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-578, PREMISE-106, PRESUMPTION-576
  Testability: testable empirically / in-house (over the last N dispositioned items, measure what fraction had a nameable quantity TYPE at filing versus a nameable VALUE -- the amendment's whole content is that these differ).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-593
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated amendment and the stated prior question. [stated]
    Current status: UNTESTED

ASSUMPTION-594:
  Date identified: 2026-07-30
  Statement: "**REVISE-253** -- adopt a three-state intake convention (UNSPECIFIED / UNMEASURED-BUT-BOUNDED / UNIDENTIFIABLE) and amend PREMISE-124 so a computable worst-case bound displaces UNCALIBRATED. Absorbs the 15b systemic-risk flag." The absorbed flag: "15b also raised a SYSTEMIC-RISK-FLAG ('unmeasured -> unbounded', spanning all 4 items)." Stated free test: "grep the seven dark days' outputs for items that plausibly required prior-day conversational context, and count them. That number either supports or kills the amendment at no cost."
  Context: 2026-07-30 changelog "For Tom" item 2 and cowork->chat "For Morning Discussion" item 3.
  Type: epistemic / methodological
  Related decisions: none
  Related items: ASSUMPTION-589, PREMISE-124, PRESUMPTION-588, PRESUMPTION-591
  Testability: testable via literature (bounding versus measuring unobserved quantities; three-valued logics in audit and safety intake) + in-house (the named grep).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-594
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated convention, the absorbed flag, and the stated free test. [stated]
    Current status: UNTESTED

ASSUMPTION-595:
  Date identified: 2026-07-30
  Statement: "**Method change:** 15a and 15b ran as separate subagent contexts with no sight of each other's files or reasoning traces -- structurally removing the read channel. Per PREMISE-111 that is the *weakest* of at least four correlation channels; MONITOR-486 stands and the three-arm dependence measurement remains unrun."
  Context: 2026-07-30 changelog "Method change" and cowork->chat. First run in which the isolation was implemented rather than proposed.
  Type: methodological / architectural
  Related decisions: none
  Related items: PREMISE-111, MONITOR-486, PRESUMPTION-590
  Testability: testable empirically / in-house (the three-arm dependence measurement PREMISE-111 already specifies -- run the two arms isolated, non-isolated, and with a different base model, and compare source-set overlap).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-595
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated method change together with its own stated limitation. [stated]
    Current status: UNTESTED

ASSUMPTION-596:
  Date identified: 2026-07-30
  Statement: "**The `generate_review_page.py` line-304 bug is now a 22-item total loss.** The file is still unmodified (mtime 2026-05-18). Every pending proposal carries a real `proposal_id` dated 07-21 through 07-29; a page generated today would read decisions back under synthetic `PROP-2026-07-30-001...022`. The intersection is empty -- **all 22 decisions you record would be silently discarded**." Stated cadence: "the queue grew by four overnight and the last review pass was 7 days ago, so this is the thing to do before the next pass."
  Context: Agent 16 session transcript, 2026-07-30; corroborated in the cowork->chat "What's Next" item 2. Sixth consecutive day at the top of the carried list.
  Type: architectural / empirical
  Related decisions: none
  Related items: ASSUMPTION-581, PREMISE-114, PREMISE-096, PRESUMPTION-582
  Testability: testable empirically / in-house (generate a page against the live queue in a scratch copy and diff the emitted id set against `pending/`; PREMISE-114 additionally obliges a retrospective impact assessment over every pass since 2026-05-18).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-596
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Agent 16 transcript read directly this run. [stated]
    Current status: UNTESTED

ASSUMPTION-597:
  Date identified: 2026-07-30
  Statement: "**`watch_list.md` is now 275 KB and can't be opened by the Read tool.** I worked from ranged shell reads again and appended by shell. The run log is 98% of the file; splitting it into `deferred/run_log/2026-Q2.md` and `2026-Q3.md` would fix it losslessly. I haven't executed it -- restructuring your vault is your call, not mine." Measured this run: 281,570 bytes.
  Context: Agent 16 session transcript, 2026-07-30. Second consecutive run worked by ranged shell reads; carried from ASSUMPTION-582. The file grew ~5,900 bytes in one day.
  Type: architectural / empirical
  Related decisions: none
  Related items: ASSUMPTION-582, PREMISE-104, PRESUMPTION-587
  Testability: testable empirically / in-house (measure daily growth rate and project the date at which ranged reads also become impractical; PREMISE-104 predicts monotone growth with no rotation policy anywhere in the pipeline).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-597
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Agent 16 transcript; the byte figure re-measured directly this run (281,570 vs the stated 275 KB). [stated]
    Current status: UNTESTED

ASSUMPTION-598:
  Date identified: 2026-07-30
  Statement: "Queue genuinely empty: `qc_sweep.py report` said `needs_review: 0`, and because that report has a documented blind spot the agent re-derived it independently from frontmatter -- 307/307 parsed, 0 never-reviewed, 0 stale, 292 pass / 15 rewrote. ... it used the window to test escalation-trigger 5: **zero nonexistent PRS ids cited, corpus-wide**, across all 307 commentaries and all 16 tradition folders. Existence only -- says nothing about whether an id is attached to the *right* gloss, which is the separate drift class awaiting your batch repoint. Incidental: the Stump tradition's id sequence skips PRS-25; nothing cites it, so it's inert."
  Context: 2026-07-30 cowork->chat, Summa reviewer section. The independent re-derivation is the PREMISE-096 remedy applied voluntarily, one day after ASSUMPTION-583 recorded the `needs_review: 0` false null.
  Type: methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-583, ASSUMPTION-584, PREMISE-096, PREMISE-110, PRESUMPTION-593, PRESUMPTION-594
  Testability: testable empirically / in-house (re-run the existence sweep and, separately, sample n commentaries for id-to-gloss correctness -- the quantity the sweep does not measure).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-598
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated reviewer report including its own stated scope limit. [stated]
    Current status: UNTESTED

ASSUMPTION-599:
  Date identified: 2026-07-30
  Statement: "**Healthy: 36 enabled tasks** (35 cron + 1 manual-only) -- all running on schedule. Stale (0). Orphaned (0). Misconfigured (0). ... `summa-2026-daily-batch` is correctly a cron task (`0 5 * * *`), not a `fireAt` -- the suspected structural misconfiguration is not present." Also stated: "this run fired at 15:47Z (~11:47 local), not the scheduled 07:09 -- one of a cluster ... consistent with a catch-up dispatch batch rather than individual failures." And: "the watchdog can only see the `RC Karpathy Wiki Project` mount, so two of its three output checks are permanently blind"; "`bosco-archive-heartbeat` has been disabled since 2026-06-12 with no note explaining why."
  Context: Scheduler health check session transcript, 2026-07-30, read directly this run.
  Type: architectural / empirical
  Related decisions: none
  Related items: PREMISE-100, PREMISE-096, PRESUMPTION-592
  Testability: testable empirically / in-house (add the two missing mounts and re-run; count how many of the watchdog's verdicts are issued over paths it cannot see -- PREMISE-100 predicts false-green proportional to inoperable checks).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-599
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the scheduler health transcript read directly this run. [stated]
    Current status: UNTESTED

ASSUMPTION-600:
  Date identified: 2026-07-30
  Statement: "*OpenStory feed refresh* -- `extract_agent_node_refs.py` cannot complete in the sandbox (~75s CPU against a 45s bash cap; background procs killed at call end). Telemetry refreshed OK (33 agents, 2026-07-30); **node_edges still stuck at 2026-07-28.** Fix is to run `refresh_openstory_feeds.sh` on the Mac."
  Context: 2026-07-30 cowork->chat "Failed loud". Distinct from the 07-29 OpenStory failure (writer outage, ASSUMPTION-585); this one is a runtime-limit failure in the refresh path.
  Type: architectural / empirical
  Related decisions: none
  Related items: ASSUMPTION-585, PREMISE-104, PREMISE-107, PRESUMPTION-595
  Testability: testable empirically / in-house (profile the script against input size across several vault snapshots -- whether ~75s is a property of the environment or of a cost that grows with the corpus).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-600
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated failure and its stated remedy. [stated]
    Current status: UNTESTED

ASSUMPTION-601:
  Date identified: 2026-07-30
  Statement: "Proposal queue: **22 pending** / 254 approved / 1 denied / 1 needs_review. Oldest pending is 9 days old. Review-pass gap: **7 days** (archive current through 2026-07-23)." Agent 16 corroborates: "no new decision archive since 2026-07-23; no `DEFERRED-HYPOTHESIS`, no `WATCH-REQUEST`, no `CONDITIONAL` markers anywhere"; intake clean in all three channels; no watch check due (WATCH-002/003 next due 2026-08-04).
  Context: 2026-07-30 cowork->chat "Pipeline Status" and Agent 16 transcript. First day since 07-25 with zero new proposals.
  Type: empirical / architectural
  Related decisions: none
  Related items: ASSUMPTION-586, PREMISE-106, PREMISE-119, MONITOR-476
  Testability: testable empirically / in-house (recount `pending/` under a stated rule; the block-vs-max-ID divergence noted at ASSUMPTION-588 applies here too).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-601
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated status block and the Agent 16 intake report. [stated]
    Current status: UNTESTED

ASSUMPTION-602:
  Date identified: 2026-07-30
  Statement: "**A quieter one worth a minute: the master wiki hasn't updated since 2026-07-27**, yet 07-28 and 07-29 specialist proposals are sitting in `pending/`. Three daily-run windows have passed. Either the runs are failing silently or they aren't writing the header -- check against `Reports/system-health-2026-07-28|29|30.md`."
  Context: 2026-07-30 cowork->chat "For Morning Discussion" item 5. Filesystem check this run: `master/C2A2_master_wiki.md` and `master/cross_program_index.md` both carry mtime 2026-07-28 15:39, one day later than the stated date -- so the stated staleness date is drawn from the file's own header rather than its mtime, and the two disagree.
  Type: architectural / empirical
  Related decisions: none
  Related items: PREMISE-100, PREMISE-107, PRESUMPTION-597
  Testability: testable empirically / in-house (compare header date to mtime for the last N master-wiki writes; the disjunction stated is decided by exactly this comparison).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-602
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated observation; the mtime discrepancy measured directly this run and recorded alongside it. [stated + measured]
    Current status: UNTESTED

ASSUMPTION-603:
  Date identified: 2026-07-30
  Statement: "Assumptions extracted: **589** . Presumptions surfaced: **588** . Validated premises: **135** (unchanged today -- no INCORPORATE) . MONITOR: **494** . REVISE: **253** . DISPOSITION: **564** . Lit search queue: 4 items searched + dispositioned today; **backlog untouched for a third consecutive run -- 22 days since last 15d consumption.** 26-item legacy cohort still bare `[QUEUED]`, awaiting your bulk-retag authorisation." Stated caveat: "Running counters as reported by the 15c run (authoritative); raw grep tallies differ where ids are cross-referenced across files."
  Context: 2026-07-30 cowork->chat "Pipeline Status". The counter caveat is new and names the divergence ASSUMPTION-545 first recorded, without reconciling it.
  Type: empirical / epistemic
  Related decisions: none
  Related items: ASSUMPTION-545, ASSUMPTION-588, OPEN-112, OPEN-133, PRESUMPTION-549
  Testability: testable empirically / in-house (recount each register under one stated counting rule; note that today's summary reports max-ID figures where 07-29 reported block counts, so the two days' status blocks are not comparable).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-603
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated status block and its stated authority caveat. Counting-rule change between 07-29 and 07-30 noted, not resolved. [stated]
    Current status: UNTESTED

ASSUMPTION-604:
  Date identified: 2026-07-30
  Statement: "**Second consecutive day, same cause, but the cause has shifted.** This morning Chrome was not running at all. This evening Chrome *is* running -- but the **Claude in Chrome extension is not connected** (`list_connected_browsers` -> `[]`, twice, 25s apart), and the fallback `Control_Chrome` path reached claude.ai only to be redirected `/recents` -> `/logout` -> `/login?from=logout`: **the Chrome profile is still signed out of claude.ai**, exactly as on 2026-07-29. Nothing was pasted or sent. I cannot sign in on your behalf." Morning record states independently: "Google Chrome was not running on the machine at scrape time."
  Context: 2026-07-30 chat->cowork failure record (11:46) and cowork->chat header (18:42). Eighth consecutive dark sync in both directions.
  Type: architectural / empirical
  Related decisions: none
  Related items: ASSUMPTION-568, ASSUMPTION-589, OPEN-135, PREMISE-107, PREMISE-131, PRESUMPTION-571, PRESUMPTION-588, PRESUMPTION-596
  Testability: testable empirically / in-house (restore login and observe; separately, test whether the morning and evening failures have one cause or two -- the record explicitly states two distinct mechanisms under one heading).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-604
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from both sync failure records, read directly this run. [stated]
    Current status: UNTESTED

ASSUMPTION-605:
  Date identified: 2026-07-30
  Statement: "*Rule 6 note: this run exceeded the 4,000-token per-task budget. Reading six agent transcripts plus the vault delta is not compressible below roughly 40k. Surfaced, not silently overrun.*"
  Context: 2026-07-30 cowork->chat closing note. Third consecutive day on which a scheduled task has disclosed a budget breach (ASSUMPTION-574, ASSUMPTION-587). New this time: a stated lower BOUND on the cost, not merely a breach.
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-574, ASSUMPTION-587, PREMISE-104, PRESUMPTION-587, PRESUMPTION-599
  Testability: testable empirically / in-house (decompose one such run's token use into transcript reads, register reads, and generation; measure what fraction is re-reading state unchanged since the previous run).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-605
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated disclosure, including the stated incompressibility claim. [stated]
    Current status: UNTESTED

ASSUMPTION-606:
  Date identified: 2026-07-31
  Statement: "**Note on the day's shape:** no attended Cowork session is evident. Every file touched today traces to a scheduled agent." Measured independently this run: 34 files under `wiki/` carry a 2026-07-31 mtime; `decisions.md` unchanged since 2026-07-20, `open_questions.md` unchanged since 2026-07-28, neither touched today.
  Context: 2026-07-31 cowork->chat summary header. Autonomous day #26.
  Type: architectural / empirical
  Related decisions: none
  Related items: ASSUMPTION-590, PRESUMPTION-482, PRESUMPTION-574
  Testability: testable empirically / in-house (mtime sweep; performed this run).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-606
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated header and independently re-derived by mtime sweep. [stated + verified]
    Current status: UNTESTED

ASSUMPTION-607:
  Date identified: 2026-07-31
  Statement: "The wiki daily run ingested -- for the first time in 8 days -- and it ingested the one file it should have asked about." `2026-07-23_stump_cajetan-time-eternity-contingent-futures.md` written into the Stump tradition as PRS-30 and PRS-31 plus a cross-index entry and FINDING-055, "with **no authorship note in any of them**. The Stump tradition now attributes a non-Stump paper to Stump." Stated mechanism: "a HELD item with a requested skip-note was ingested three runs later by a different phase that had no memory of the hold. `PROCESSED_LOG` is the only durable state, and a HOLD leaves no mark in it. That is the bug -- and it will recur on the next held item. Cheapest fix: a `inbox/HOLD_LIST.md` that Phase 1 reads before ingesting."
  Context: 2026-07-31 cowork->chat, "For Morning Discussion" item 1. Prior record: 07-19 verified the author as Maria Eduarda Machado (Civitas Augustiniana 13, 2025); 07-27 marked HELD awaiting Tom's confirm and requested a permanent skip-note.
  Type: architectural / methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-561, ASSUMPTION-584, PRESUMPTION-601, PRESUMPTION-602, PRESUMPTION-615
  Testability: testable empirically / in-house (grep `PROCESSED_LOG.md` and the inbox for every item ever marked HELD and count how many were subsequently ingested; the class size is currently 1 by observation, not by measurement).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-607
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated regression report and its stated causal account. [stated]
    Current status: UNTESTED

ASSUMPTION-608:
  Date identified: 2026-07-31
  Statement: "The finding is genuinely good -- and it is a *structural gap*, not a convergence: the emergent-time programs (Arkani-Hamed's kinematic flow, Wolfram's observer-traversed ruliad) deliver **timelessness**, not **eternity**; Carroll's block universe is still a temporal manifold viewed from outside." New question: "do the emergent-time programs have room for eternity at all, or only for timelessness?" Assessed as "a well-posed humanities-physics test case and probably the most interesting thing the network produced this week."
  Context: FINDING-055, minted by the 2026-07-31 wiki daily run from the Stump/Cajetan ingest. Logged in `master/cross_program_index.md`, NOT in `open_questions.md`.
  Type: epistemic / empirical (object-level)
  Related decisions: none
  Related items: FINDING-055, ASSUMPTION-607, PRESUMPTION-602
  Testability: testable via literature (whether eternity in the Boethian/ET-simultaneity sense is representable in emergent-time formalisms; whether timelessness and eternity are formally distinguishable in the kinematic-flow and ruliad programs).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-608
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated. Note recorded, not judged: the finding's provenance is the ingest recorded in ASSUMPTION-607. [stated]
    Current status: UNTESTED

ASSUMPTION-609:
  Date identified: 2026-07-31
  Statement: "PRESUMPTION-591, -592, -600 searched both directions and dispositioned (DISPOSITION-565...568). All three -> REVISE." Registers: REVISE-254..257; `validated_premises.md` and `monitor_queue.md` NOT touched -- 0 INCORPORATE, 0 MONITOR. Stated with denominator: "0 INCORPORATE for a THIRD consecutive run (07-29: 1/8; 07-30: 0/4; 07-31: 0/3). Reported as a count with its denominator and NOT offered as evidence of rigour, per DISPOSITION-552."
  Context: 2026-07-31 c2a2-lit-search-pipeline run, `for_lit_search.md` run footer and cowork->chat summary.
  Type: methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-591, DISPOSITION-552, PREMISE-114, PREMISE-110, PRESUMPTION-603
  Testability: testable empirically / in-house (running yield series; the comparison is available and unrun).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-609
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the pipeline's own run footer, including its stated refusal to read the count as rigour. [stated]
    Current status: UNTESTED

ASSUMPTION-610:
  Date identified: 2026-07-31
  Statement: "The register pre-check (PREMISE-090..135) was applied at disposition and was **load-bearing on one item**: PRESUMPTION-592 turned out to be governed by PREMISE-110, which names 'the scheduler watchdog' explicitly -- and that finding converted a candidate INCORPORATE into a REVISE *against PREMISE-110 itself*." Pipeline's own summation: "On two consecutive runs the register's own state -- not the evidence -- determined the outcome: 07-30 declined on an unratified parent premise (PREMISE-114), 07-31 on an under-specified governing premise (PREMISE-110). Whether that is discipline or a stall is not decidable from inside this pipeline."
  Context: 2026-07-31 lit pipeline disposition of PRESUMPTION-592.
  Type: epistemic / methodological
  Related decisions: none
  Related items: ASSUMPTION-592, PREMISE-110, PREMISE-114, REVISE-255, PRESUMPTION-603
  Testability: testable empirically / in-house (over the disposition series, classify each non-INCORPORATE by whether the binding constraint was evidence or register state, and state who adjudicates the resulting ratio).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-610
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the disposition record and the pipeline's stated limit on its own authority. [stated]
    Current status: UNTESTED

ASSUMPTION-611:
  Date identified: 2026-07-31
  Statement: "15b raised a batch-level **SYSTEMIC-RISK-FLAG: underpowered self-measurement.** All three items named a settling quantity by *type* (which is REVISE-252 working as designed), and in all three the available denominator is single-digit -- n=1 running task, cohorts of 8 and 4, a bound judgment over an UNCALIBRATED population of unstated size. A proportion on a single-digit denominator cannot discriminate the hypotheses posed, so each item is positioned to return 'no effect' for want of power, and **in the register a null returned for want of power is indistinguishable from a null returned on evidence.** 15c independently corroborated this: for all three items it replaced the item's own stated test with a better-powered one drawn from the existing population -- a second party finding the quantities infeasible as named, arrived at while writing dispositions rather than while reading the flag."
  Context: 2026-07-31 lit batch, SYSTEMIC-RISK-FLAG in `against/PRESUMPTION-600_against.md`.
  Type: methodological / epistemic
  Related decisions: none
  Related items: REVISE-252, REVISE-257, PREMISE-124, PRESUMPTION-604, PRESUMPTION-611
  Testability: testable via literature (statistical power at small n; the indistinguishability of a null from an underpowered null; pooling and sequential designs for low-count monitoring) and in-house (compute the achievable denominator for every settling quantity currently in the register).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-611
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated, including 15c's independent corroboration and the route by which it arose. [stated]
    Current status: UNTESTED

ASSUMPTION-612:
  Date identified: 2026-07-31
  Statement: "**REVISE-257** -- *amendment to REVISE-252.* Adds a **feasibility clause**: a settling quantity must come with (a) the denominator currently available and (b) where single-digit, either a named route to a larger one or an explicit 'NOT CURRENTLY DECIDABLE on the quantity as named.'"
  Context: 2026-07-31 revision flags; absorbs 15b's systemic flag (ASSUMPTION-611).
  Type: methodological / architectural
  Related decisions: none
  Related items: REVISE-251, REVISE-252, ASSUMPTION-593, ASSUMPTION-611, PRESUMPTION-604
  Testability: testable empirically / in-house (apply the clause retrospectively to the last N intakes and count how many settling quantities would be marked NOT CURRENTLY DECIDABLE).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-612
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated. Applied voluntarily to this run's own intake. [stated]
    Current status: UNTESTED

ASSUMPTION-613:
  Date identified: 2026-07-31
  Statement: "**REVISE-255** (from PRESUMPTION-592) -- **new.** The scheduler watchdog issued a PASS over `c282-wiki-agent-daily-run` on a file-count-and-recency test *while the task was directly observed still executing* (status: running, 26 turns). The watchdog has a symbol for 'cannot check' and none for 'still running.' Amendment + relabel; cheap, warranted on theory alone." Stated question for Tom: "whether to patch it or to stop treating its PASS as evidence at all."
  Context: 2026-07-31 lit disposition of PRESUMPTION-592 (surfaced by 14b on 07-30), returned as REVISE against PREMISE-110.
  Type: architectural / methodological
  Related decisions: none
  Related items: PRESUMPTION-592, PREMISE-096, PREMISE-110, ASSUMPTION-599, ASSUMPTION-610, PRESUMPTION-612
  Testability: testable empirically / in-house (add a running state and re-run the watchdog against the last 30 days of scheduler history; count how many PASSes were issued over in-flight tasks).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b/15c → 14a]
    Original item: ASSUMPTION-613
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated. Note: this item completes a full loop -- 14b surfaced it 07-30, the lit pipeline dispositioned it 07-31, 14a records the outcome. [stated]
    Current status: UNTESTED

ASSUMPTION-614:
  Date identified: 2026-07-31
  Statement: "**REVISE-256** (from PRESUMPTION-600) -- **new.** The 07-29 pre-check removed 9 of 13 items; the 07-30 0-of-4 yield was then explained entirely downstream (PREMISE-114 unratified). An intake filter that removes already-governed items may be *depressing the residual cohort's yield*, and the offered explanation doesn't account for it. Clause (1) replaces the item's own test and is cheap. Berkson (1946) verified as the collider-conditioning precedent." Stated priority: "**This is the highest information-per-cost item on the list.**" Clause (1) is: run the 9 removed items.
  Context: 2026-07-31 lit disposition of PRESUMPTION-600 (surfaced by 14b on 07-30).
  Type: methodological / epistemic
  Related decisions: none
  Related items: PRESUMPTION-600, MONITOR-490, ASSUMPTION-591, PRESUMPTION-603
  Testability: testable empirically / in-house (run the 9 removed items and compare INCORPORATE rate against the 4 that survived; the cohorts exist).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b/15c → 14a]
    Original item: ASSUMPTION-614
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated, including the verified Berkson (1946) precedent and the stated cost ranking. [stated]
    Current status: UNTESTED

ASSUMPTION-615:
  Date identified: 2026-07-31
  Statement: "**REVISE-254** (from PRESUMPTION-591) -- *amendment to REVISE-253, does not stand alone.* REVISE-253's validating test (grep the seven dark days) measures item **frequency**, but the amendment's warrant is cost **boundability**. Wrong quantity; four gating clauses proposed."
  Context: 2026-07-31 lit disposition of PRESUMPTION-591. Confirms the mismatch 14a recorded on 07-30 as ASSUMPTION-594 and 14b queued as PRESUMPTION-591.
  Type: methodological
  Related decisions: none
  Related items: REVISE-253, ASSUMPTION-594, PRESUMPTION-591, PREMISE-124
  Testability: testable empirically / in-house.
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a → 15a/15b/15c → 14a]
    Original item: ASSUMPTION-615
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated. The frequency-vs-boundability mismatch was surfaced by 14a/14b 24h earlier and is now independently confirmed by the lit pipeline. [stated]
    Current status: UNTESTED

ASSUMPTION-616:
  Date identified: 2026-07-31
  Statement: "**Pattern count worth watching:** this is the **second consecutive batch** in which measurement *design*, not evidence, was the binding constraint (cf. REVISE-253, 07-30). Two in two is not yet a defect class under PREMISE-130. A third, in a third signature, would make the right unit of analysis 'a convention that does not require feasible tests' rather than 'three items with weak tests.'" Stated recommendation: "Consider pre-registering that trigger now so you're not deciding it after the fact."
  Context: 2026-07-31 cowork->chat, "For Morning Discussion" item 5.
  Type: methodological / architectural
  Related decisions: none
  Related items: PREMISE-130, REVISE-253, REVISE-257, ASSUMPTION-611, PRESUMPTION-605
  Testability: testable empirically / in-house (the pre-registration is itself the test; whether a third instance arrives is observable).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-616
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated, including the explicit pre-registration recommendation. [stated]
    Current status: UNTESTED

ASSUMPTION-617:
  Date identified: 2026-07-31
  Statement: "**Phase 2 hunt -- 2 new proposals, both caveated honestly.**" PROP-2026-07-31-003 (Levin, Thought Economics "The Continuum of Mind" -- "an AI may *hide* a mind behind forced words, shifting the membership test from fidelity-of-report to **freedom**-of-report") and PROP-2026-07-31-004 (Kastrup vs. Seth vs. Koch at ICPR26 on the epistemic value of psychedelic experience, "an indirect Kastrup-Friston confrontation by proxy, bearing on FINDING-009"). "Both carry an explicit evidence-quality caveat: PRS candidates drawn from publisher abstracts, not full text, flagged for verification rather than presented as settled. That is the right behaviour and worth noting as such." Two further proposals filed earlier by the Friday specialists (Carroll, Arkani-Hamed). Queue 22 -> 26.
  Context: 2026-07-31 wiki daily run Phase 2 and the two specialist runs.
  Type: methodological / empirical
  Related decisions: none
  Related items: FINDING-009, ASSUMPTION-607, PRESUMPTION-615
  Testability: testable empirically / in-house (verify the abstract-sourced PRS candidates against full text; separately, check whether the caveat survives into the PRS record on ingest).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-617
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated. Proposal files confirmed present on disk with 07-31 mtimes (4 files). [stated + verified]
    Current status: UNTESTED

ASSUMPTION-618:
  Date identified: 2026-07-31
  Statement: "**Fix `tools/generate_review_page.py` line 304 before any review pass** -- at 26 pending it would now silently discard **26** decisions, not 22." Also stated: "Do NOT open a generated review page before that." A review page was nonetheless generated this run (`review/2026-07-31_review.html`, 26 pending) and `review_log.html` rebuilt (318 cards, 87 dates, 13 responses, 14 addresses scrubbed, grep-verified clean).
  Context: 2026-07-31 cowork->chat "What's Next" item 3 and "Also ran". Generator unmodified since mtime 2026-05-18; seventh day at the top of the carried list.
  Type: architectural / empirical
  Related decisions: none
  Related items: ASSUMPTION-596, MONITOR-476, PREMISE-114, PRESUMPTION-612
  Testability: testable empirically / in-house (the defect is a static read of line 304; the impact figure scales with queue depth and is computable exactly).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-618
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated. Recorded without judgment: the warning not to open a generated page coexists with the generation of one. [stated]
    Current status: UNTESTED

ASSUMPTION-619:
  Date identified: 2026-07-31
  Statement: "**The cross-connection count drifted again -- 90 vs 165 -- and it's in the master narrative.** This is the artifact you retired on 07-21 (unique `CROSS-` ids != connection count, same class as the 300-vs-511 PRS error). It got out of the flags section and into the authoritative 'Network:' line. Also: `master/C2A2_master_wiki.md` header still reads *Last updated: 2026-07-27* though today's narrative is in the file, and `traditions/stump/prs_triplets.md` reads *Total: 28* while holding entries through PRS-31. Three counting surfaces disagreeing is now a maintenance item, not a footnote." Also stated in the same summary: "519 PRS triplets - 55 findings" against the carried authoritative 511 / 54.
  Context: 2026-07-31 cowork->chat "For Morning Discussion" item 4 and Pipeline Status.
  Type: architectural / empirical
  Related decisions: none
  Related items: OPEN-112, MONITOR-489, ASSUMPTION-545, ASSUMPTION-560, ASSUMPTION-603, PRESUMPTION-613
  Testability: testable empirically / in-house (designate one canonical counter and recount under one stated rule -- MONITOR-489's settling test, unrun for a 22nd+ day).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-619
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated, then extended by direct measurement this run. `master/C2A2_master_wiki.md` mtime is 2026-07-31 04:41 and its header reads 2026-07-27 -- confirming for a second consecutive day the disjunct measured on 07-30 (ASSUMPTION-602). `traditions/stump/prs_triplets.md` carries TWO total lines, "Total PRS triplets: 25" and "Total PRS triplets: 28", while holding entries through PRS-31 -- a three-way disagreement inside a single file, one surface more than the summary reports. [stated + verified + extended]
    Current status: UNTESTED

ASSUMPTION-620:
  Date identified: 2026-07-31
  Statement: "**Third consecutive day. The cause has now narrowed to one thing.** The Claude in Chrome extension **is** connected today (`list_connected_browsers` -> 1 local macOS browser -- this is an improvement on 07-30, when it returned `[]`). Chrome is running. But navigating to `https://claude.ai/recents` redirects to `https://claude.ai/login?from=logout`: the Chrome profile is **signed out of claude.ai**, same as this morning's scrape and same as 07-29. Nothing was pasted or sent. I cannot sign in on your behalf. **One action fixes both ends of the daily sync.**" The morning record diagnoses the same single mechanism independently.
  Context: 2026-07-31 chat->cowork failure record (08:53) and cowork->chat header (18:40). Ninth consecutive dark sync; three consecutive days with no Chat context reaching the agents (last success 2026-07-29).
  Type: architectural / empirical
  Related decisions: none
  Related items: ASSUMPTION-604, PREMISE-107, PREMISE-131, OPEN-135, PRESUMPTION-596
  Testability: testable empirically / in-house (sign in and observe).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-620
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from both sync records, read directly this run. Recorded as an improvement in diagnostic quality over 07-30: yesterday two distinct mechanisms were reported under one heading (ASSUMPTION-604, PRESUMPTION-596); today both ends report the same single mechanism and the record says so explicitly. [stated]
    Current status: UNTESTED

ASSUMPTION-621:
  Date identified: 2026-07-31
  Statement: Summa 2026 nightly verification, run directly this EOD: "Verified 307 synthesis files (Days 001-307) against the live C2A2 wiki -- both mounts were present, so PRS/FLAG/CROSS checks were real rather than form-only. **Zero citation drift**, zero metaphysical-guardrail violations, zero filename-safety violations; **9 authorship violations** across 7 days ... **228 length violations**, of which 204 carry an explicit `length_note` and only 24 do not; and **2 new pairing candidates**." Two stated novelties: (a) "**The corpus is no longer static.** 40 synthesis/transcript files changed in the last 24 hours ... Prior passes could assume a frozen corpus." (b) "**I have to flag a defect in my own first run.** It carried the bottom-frontmatter splitter bug your 07-30 pass had already fixed, and it reproduced the phantom ~2x over-runs ... I caught it because my numbers contradicted last night's, rewrote the splitter, and re-ran -- all logged figures are post-fix." Read-only compliance verified by snapshot diff across all 614 files, zero differences.
  Context: session `local_03b0304d` transcript, read directly this run.
  Type: methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-598, PREMISE-096, PREMISE-110, PRESUMPTION-608, PRESUMPTION-609
  Testability: testable empirically / in-house (the splitter fix is verifiable; the "corpus no longer static" claim implies a re-audit scope that is computable).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-621
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the session transcript, read directly. [stated]
    Current status: UNTESTED

ASSUMPTION-622:
  Date identified: 2026-07-31
  Statement: Summa qc sweep, read directly: "307 pairs, 4 needing review (all deliberately held), 303 fresh." Day 261 passed both frames; Days 087/088/089/260 transcript frames cleared opportunistically while synthesis frames stayed held. Stated structural cost: "with four pairs permanently held and the cap at 6, only two queue slots per run are doing new work. The withholding is right -- it keeps the defects visible -- but the queue is now mostly held inventory, and that ratio worsens until the batch repoint lands." Two voluntary disclosures: a duplicate QC-log row it created, and a Rule 6 budget breach ("the four opportunistic refetches were the bulk of it ... that was my call, not the budget's").
  Context: session `local_4cbd5116` transcript, read directly this run.
  Type: architectural / methodological
  Related decisions: none
  Related items: ASSUMPTION-598, PRESUMPTION-610, PRESUMPTION-614
  Testability: testable empirically / in-house (project the held/free slot ratio forward against the repoint date; the cap is a parameter).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-622
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the session transcript, read directly. [stated]
    Current status: UNTESTED

ASSUMPTION-623:
  Date identified: 2026-07-31
  Statement: Summa commentary reviewer, read directly: "review queue held four deliberately-parked pairs, so no semantic reviews were performed and nothing was marked. The substantive output is the bridge-level census, which corrects the unanchored-bridge class scope from '~30 days' to '21 fully id-less plus 209 partial' -- and explicitly declines to convert that into a defect count, since the compliant-vs-defective split resisted two automated attempts."
  Context: session `local_77236d22` transcript, read directly this run.
  Type: methodological / empirical
  Related decisions: none
  Related items: ASSUMPTION-622, PREMISE-124, PRESUMPTION-611
  Testability: testable empirically / in-house (hand-sample a stratified subset of the 209 partials to bound the defective fraction; the refusal is a refusal to estimate, not an absence of method).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-623
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the session transcript, read directly. [stated]
    Current status: UNTESTED

ASSUMPTION-624:
  Date identified: 2026-07-31
  Statement: Three separate scheduled tasks disclosed Rule 6 budget breaches today. Lit pipeline: "this run exceeded the 4,000-token per-task budget" with mitigations enumerated. Cowork->chat: "Reading the vault delta plus the day's dispositions is not compressible much below ~30k. Surfaced, not silently overrun." Summa qc sweep: "this run went well past the 4,000-token per-task budget ... I judged them worth it ... but that was my call, not the budget's."
  Context: three 2026-07-31 run footers. Fifth consecutive day of breach disclosure across the network.
  Type: methodological / architectural
  Related decisions: none
  Related items: ASSUMPTION-574, ASSUMPTION-587, ASSUMPTION-605, PREMISE-104, PRESUMPTION-587, PRESUMPTION-599, PRESUMPTION-614
  Testability: testable empirically / in-house (decompose one run's token use; PRESUMPTION-587 specified this on 07-29 and is unrun on day 3).
  Status: UNTESTED
  Provenance:
    Origin: 14a
    Chain: [14a]
    Original item: ASSUMPTION-624
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from three run footers. Recorded without judgment: the cowork->chat floor claim moved from "roughly 40k" (07-30, ASSUMPTION-605) to "~30k" (07-31) with no note and no stated method for either figure. [stated]
    Current status: UNTESTED
