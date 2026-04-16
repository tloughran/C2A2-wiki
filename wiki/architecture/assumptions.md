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
  Status: CONTESTED
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
  Status: UNTESTED
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

---

## Status Summary

Total assumptions identified: 32

By testability:
  Testable via literature: 7 (ASSUMPTION-003, 005, 006, 007, 010, 019, 025)
  Testable empirically: 20 (ASSUMPTION-004, 008, 009, 011, 012, 013, 014, 015, 017, 020, 021, 022, 023, 024, 026, 027, 028, 029, 031, 032)
  Framework commitment: 5 (ASSUMPTION-001, 002, 016, 018, 030 — until benchmarks specified)

By status (2026-04-16):
  GROUNDED: 2 (ASSUMPTION-001, 002 — implemented in architecture)
  SUPPORTED: 1 (ASSUMPTION-005 — traditions as units, with noted caveats)
  PARTIALLY-SUPPORTED: 2 (ASSUMPTION-006, ASSUMPTION-010)
  PARTIALLY-CHALLENGED: 7 (ASSUMPTION-003, 004, 007, 008, 011, 013)
  CONTESTED: 2 (ASSUMPTION-009, ASSUMPTION-012)
  UNTESTED: 19 (3 from Apr 13 evening + 5 from Apr 14 + 6 from Apr 15 + 5 from Apr 16)

Literature search results (pipeline cycles completed through 2026-04-15):
  All 42 prior items: SEARCHED and DISPOSITIONED
  3 INCORPORATE, 23 MONITOR, 16 REVISE (REVISE cleared to 0 by Tom's batch triage Apr 15)
  Plus 11 items from Apr 15 now dispositioned (+1 INCORPORATE, +7 MONITOR, +3 REVISE) — total 53 items DISPOSITIONED

Key event (2026-04-16): Five new assumptions extracted, centered on two themes. Scaling / batch-processing: ASSUMPTION-028 (massive 45-file batch ingestion) and ASSUMPTION-031 (parallel subagent extraction) both make quality-invariance claims for large-batch processing, echoing ASSUMPTION-027 (batch REVISE triage) from April 15. Architecture and infrastructure pragmatics: ASSUMPTION-029 (HTML-as-constraint justifies modular refactor), ASSUMPTION-030 (publication-readiness benchmarks gating public release), and ASSUMPTION-032 (computer-use as Chrome-MCP fallback).

Next step: Route ASSUMPTION-028–032 to 15a/15b queue. The scaling pair (028, 031) connects to the existing PRESUMPTION-026 / ASSUMPTION-027 cluster about batch-vs-deliberate processing quality. ASSUMPTION-030 should produce OPEN-020 (benchmark-definition question). ASSUMPTION-029 should be tracked against whether the modular refactor delivers its claimed benefits.
