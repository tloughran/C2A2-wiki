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

Key event (2026-05-10): Nine new assumptions extracted on a Sunday whose dominant signature was three concurrent first-occurrences (first-ever Rohr ×2 + Wright ×3 pending proposals + first weekly sewing-agent run) plus a clean self-awareness lit-search drain (9 MONITOR + 11 REVISE + 0 INCORPORATE; densest-cycle structural pattern from 2026-05-09 replicated) plus a 5th-consecutive failed evening cowork-to-chat delivery (sign-in-redirect after the "normal windows" failure mode resolved this evening for the first time in 2 days). Today's nine new items cluster in four families. **(1) DAY-SHAPE + LOGIN-PROHIBITION cluster** — ASSUMPTION-104 (day-shape characterization with three concurrent-firsts), ASSUMPTION-105 (user-privacy rules prohibit password-based login as binding operating constraint surfacing as 5th-consecutive failure cause). **(2) DISPOSITION-PATTERN-AS-EPISTEMIC-WEIGHT cluster** — ASSUMPTION-106 (ASSUMPTION 0/8 REVISE rate stable across 2 cycles confirms operational/diagnostic-pattern characterization), ASSUMPTION-107 (92% PRESUMPTION REVISE rate as record-density disposition signal). The cluster generalizes ASSUMPTION-073's REVISE-heuristic into a cross-cycle disposition-by-item-type pattern. **(3) GOVERNANCE-TRIGGER-ACTIVATION cluster** — ASSUMPTION-108 (DECISION-027 scope extension URGENT-this-week per ASSUMPTION-098 three-recurrence threshold satisfied at N=5/30 days), ASSUMPTION-109 (PRESUMPTION-125 4th-recurrence requires standalone DECISION canonization distinct from DECISION-027). The cluster operationalizes yesterday's stated canonization protocol (ASSUMPTION-098) for the first time. **(4) NEW-METRIC + BLOCKING + SELF-MEASUREMENT cluster** — ASSUMPTION-110 (sewing agent canonical inaugural connectivity baseline 766/2/17/785), ASSUMPTION-111 (Wright/Rohr first-ever pendings blocking N=13 expansion via DECISION-026 precondition chain), ASSUMPTION-112 (SELF-MEASUREMENT Goodhart cluster confirmed as architectural recursive-self-observation pattern across two consecutive cycles at 0% INCORPORATE). The cluster combines a brand-new metrics primitive (connectivity), a new blocking-relationship claim (N=13 expansion gated by 5 pendings), and the day's headline architectural-recursive item (the system surfacing its own Goodhart-failure-candidate). Pattern note: today's 9 assumptions are dominated by methodological / metrics items (5 of 9: 104, 106, 107, 110, 112) plus 2 governance items (108, 109) — extending the methodological-heavy signature of operational-throughput days with a new governance-trigger-activation sub-signature for the first time. Today's 12-to-9 presumption-to-assumption ratio (1.33:1) is moderate — below 2026-04-27 / 2026-05-08 / 2026-05-09 record (1.5:1) but above 2026-05-05's 1.22:1. The execution-day character (clean lit-search drain + sewing-agent first-run + Wright/Rohr first-pendings + 5th-consecutive evening failure) generates both novel content-architecture commitments (ASSUMPTION-110, 111, 112 all introduce architectural primitives) and operational-principle articulations (ASSUMPTION-104, 105, 108, 109).

Key event (2026-05-09): Eight new assumptions extracted on a Saturday lit-search-disposition + Saturday-Wolfram + self-awareness-backfill day whose primary architectural signal was the lit-search 15a/15b/15c pipeline producing four SYSTEMIC-RISK flags in a single cycle (the densest single cycle on record), three of them recurrence flags. Today's eight new items cluster in three families. **(1) Lit-search-cycle-output epistemic-weight cluster** — ASSUMPTION-096 (4-SYSTEMIC-RISK density warrants cluster-level remediation), ASSUMPTION-098 (third-recurrence at fixed-cycle cadence as canonization threshold), ASSUMPTION-099 (DECISION-027 scope extension to external-tool-review layer). All three were surfaced from today's lit-search returns and the cowork-to-chat summary's "For Morning Discussion" items 1–2 questioning Tom's input on cluster-level disposition. **(2) Architectural-sprint and cross-tradition-signal cluster** — ASSUMPTION-097 (Three-recurrence discipline cluster bundleable as "Core Operational Discipline" sprint) and ASSUMPTION-100 (Saturday Wolfram three-way ontological convergence as week's highest-leverage cross-tradition signal) articulate two prioritization commitments — one for architectural-discipline track, one for content-architecture track. **(3) Operational-baseline cluster** — ASSUMPTION-101 (Chrome MCP "normal windows" error as environment-state issue, not Chrome-MCP defect, per Codex-style diagnostic), ASSUMPTION-102 (20-item EOD-batch single-cycle drain as operational baseline), ASSUMPTION-103 (today's 8-task fire-rate as positive evidence against daemon-link-count regression for THIS task). The cluster generalizes ASSUMPTION-072's single-cycle-drain claim, articulates a Chrome-MCP root-cause attribution, and locks in a per-task evidence frame for the daemon-bug hypothesis. Pattern note: today's 8 assumptions are dominated by methodological / metrics items (5 of 8: 096, 097, 098, 102, 103) — extending the methodological-heavy signature of operational-throughput days (2026-04-21, 2026-04-27, 2026-05-05, 2026-05-08). Today's standalone empirical/infrastructure item is ASSUMPTION-101 (Chrome-MCP environment-state attribution), the lit-search-disposition character generates more *cycle-output-articulation* than *content-architecture* claims — except for ASSUMPTION-100 (Saturday Wolfram cross-tradition signal) which is the day's standalone content-architecture item with cross-tradition bearing. Today's 12-to-8 presumption-to-assumption ratio (1.5:1) ties 2026-04-27 and 2026-05-08 as joint-record. The execution surface today was unusually clean (8/8 scheduled tasks fired, lit-search drained 100% in one cycle, self-awareness-backfill closed yesterday's surface), inverting yesterday's three-stall-day pattern.

Key event (2026-05-08): Eight new assumptions extracted on a Friday review-decision intake day plus three queued-but-stalled scheduled tasks (1pm register cleanup, sewing-agent-weekly, Wright/Rohr Sunday agent — the latter two hit personal-account org-limit immediately) plus a substantive Codex 5.5 external review of the C2A2 explorer pasted into Cowork session local_56cc4dfb whose composite synthesis was queued at end of session. Today's eight new items cluster in three families. **(1) Personal-account org-limit + composite-synthesis cluster** — ASSUMPTION-088 (org-monthly-usage-limit interrupt on personal-account Cowork session treated as work-blocking, not misclassification), ASSUMPTION-089 (two-source composite synthesis: internal report + external-LLM review), ASSUMPTION-090 (smallest-fix-first prioritization for explorer track — `extractOverview()` two-line var-declaration fix as the high-confidence, low-effort entry point, then smoke-test, then responsive fallback). All three surfaced from the local_56cc4dfb explorer-fix session and the cowork-to-chat summary (local_feb53918) "For Morning Discussion" item 1. **(2) Sandbox-infrastructure escalation cluster** — ASSUMPTION-092 (3-day master-narrative absence attributable to daemon link-count = 1 bug regression hypothesis), ASSUMPTION-094 (N≥5 sandbox-infrastructure constraints aggregated across C2A2 + Summa = single-escalation threshold), ASSUMPTION-095 (YouTube IP-block as SYSTEMIC ESCALATION joining OPEN-039 as 5th channel). The combined OPEN-039 cluster now spans scheduling (daemon link-count) + filesystem (mount-topology + .git/index.lock 22-day age) + networking (egress allowlist + Summa YouTube IP-block) + authentication (browser-auth) — five canonical channels across two active projects. **(3) Operational-cadence-articulation cluster** — ASSUMPTION-091 (off-cadence specialist proposal filings treated as on-cadence for downstream review-page rendering and approval tracking), ASSUMPTION-093 (Saturday-morning rerun as standard closure path for queued-but-stalled weekday scheduled tasks). Both extend ASSUMPTION-079 (same-day catch-up framing) at the per-proposal and per-task levels. Pattern note: today's 8 assumptions are dominated by methodological items (6 of 8: 088, 089, 090, 091, 093, 094) — continuing the methodological-heavy signature of operational-throughput days (2026-04-21, 2026-04-27, 2026-05-05). The execution-day character (review-decision intake + 5 new pending proposals + 3 stalled scheduled tasks + Codex external-review queued + Summa cross-project QC throughput) again generates more *operational-principle-articulation* than *content-architecture* claims — except for ASSUMPTION-095 which is the day's standalone empirical/infrastructure item with cross-project bearing. Today's "stalled task" surface area is the largest yet observed in a single day (3 of 4 scheduled C2A2-related tasks stalled or hit org-limit immediately; only the cowork-to-chat sync ran to completion and even that failed delivery to claude.ai per ASSUMPTION-071 / PRESUMPTION-111).

Key event (2026-05-05): Nine new assumptions extracted on a daemon-catch-up Tuesday whose primary architectural signal was all six weekday-assigned C2A2 specialist agents executing in a single 15:35–16:35 UTC window after Tom's Claude restart cleared the daemon outage. Today's nine new items cluster in four families. **(1) Daemon-bug discovery cluster** — ASSUMPTION-080 (link count > 1 fires; link count = 1 silently skips, an Anthropic-side bug), ASSUMPTION-081 (`update_scheduled_task --fireAt` is a working workaround), ASSUMPTION-079 (same-day catch-up of all six weekly specialist runs is treated as functionally equivalent to spread-across-week distribution). All three surfaced from the Summa-updating-agents session (local_40871db5) Tom-facing diagnosis. **(2) Vision-articulation cluster** — ASSUMPTION-082 (3-layer RC Explorer architecture with 5 integration steps; Community Explorer = Tool #1; AI Heartbeat = Tool #2 urgent rebuild) is the day's most consequential architectural item: it is the first time the L1/L2/L3 model with explicit integration steps has been recorded as a stated assumption. ASSUMPTION-083 (filter semantics: within section = OR, across sections = AND, edges require both endpoints visible) is a UX-spec articulation surfaced by the explorer help-popover review. **(3) Specialist-output norms cluster** — ASSUMPTION-084 (empty-handed orchestrator Phase 2 = valid result not failure mode), ASSUMPTION-085 ("FROM thinker himself" quality filter operative across all specialist slots; Hawkins 0-proposal honest-null re-affirmed), ASSUMPTION-086 (specialist-self-claims of "strongest bridge / candidate shared substrate / parallels C2A2 architecture" treated as primary cross-tradition signal without an adjudication step) extend the BRIEFING-LAYER-EPISTEMIC-COMMITMENTS pattern to the specialist-output layer. ASSUMPTION-086 is in tension with PRESUMPTION-074's prior SYSTEMIC-RISK flag on specialist-recognition reliability. **(4) Institutional-maturity entry mode** — ASSUMPTION-087 (TRACE Institute launch as research-program-level alliance signal) introduces a new proposal-type granularity beyond paper-level. Pattern note: today's 9 assumptions are dominated by methodological items (6 of 9: 079, 080, 081, 084, 085, 086) — continuing the methodological-heavy signature of operational-throughput days (2026-04-21, 2026-04-27). The execution-day character (daemon catch-up + 6 specialist runs + walk-thread architectural articulation) again generates more *operational-principle-articulation* than *content-architecture* claims — except for ASSUMPTION-082 which is the day's standalone architectural item.

Key event (2026-04-27): Eight new assumptions extracted on an execution-heavy Monday whose primary architectural signal was the C2A2 lit-search pipeline draining the 5-day backlog (58 items processed; 19 new + 39 re-triggered) and INCORPORATING ASSUMPTION-068 → PREMISE-012 and ASSUMPTION-069 → PREMISE-013. Today's eight new items cluster in three families: **(1) infrastructure-gap normative articulation** — ASSUMPTION-071 (browser-auth as agent-prohibited; first explicit two-instance same-day articulation across morning chat scrape + evening sync) and ASSUMPTION-078 (two parallel sandbox-infrastructure failure modes today, both treated as user-fixable) extend the OPEN-039 sandbox-infrastructure-escalation cluster from yesterday with a third channel (auth) that joins egress and mount-topology. **(2) lit-search pipeline self-articulation** — ASSUMPTION-072 (5-day backlog drainable in single cycle), ASSUMPTION-073 (PRESUMPTION + strong-challenge → REVISE heuristic explicit), and ASSUMPTION-074 (no-new-evidence carry-forward as PREMISE-006-extension to refresh case) form a new LIT-SEARCH-LAYER-EPISTEMIC-COMMITMENTS cluster, parallel to the BRIEFING-LAYER cluster (ASSUMPTION-046, 047, 048, 057, 058, 059, 060). **(3) design-project authorial reframing** — ASSUMPTION-076 (PRS triplets are Tom's re-description, not tradition's self-voice; "PRS-NN in the Stump-tradition wiki" not "Stump's PRS-NN") and ASSUMPTION-077 (synthesis-to-transcript ±5% policy) are direct Tom-stated commitments from the continuing design-project session. ASSUMPTION-076 has high downstream consequence: it recasts the ground beneath ASSUMPTION-067 (Stump-as-supplier-of-live-metaphysics) — if PRS triplets are Tom's framing, the specialist's reading of Stump-via-PRS is reading Tom's frame back to itself (see PRESUMPTION-089 for the recursive-reading risk). **(4) specialist cadence override** — ASSUMPTION-075 (Levin "significant work not yet captured" criterion overrides 30-day window) is the first explicit specialist-level deviation from the cadence rule, surfaced from today's Monday Levin+Friston specialist slot. Pattern note: today's 8 assumptions are dominated by methodological items (5 of 8: 071, 072, 073, 074, 077; 078 partial) — a return to the methodological-heavy signature of 2026-04-21 after Sunday's architectural/empirical signature. The execution-day character (pipeline drain + scheduled-task throughput) generates more *operational-principle-articulation* than *content-architecture* claims.
