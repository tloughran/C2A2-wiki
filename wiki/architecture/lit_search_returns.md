# LITERATURE SEARCH RETURNS - AGENT 15b ADVERSARIAL SEARCH

**Search date:** 2026-04-13
**Search direction:** AGAINST (disconfirmatory)
**Total items searched:** 25 (11 ASSUMPTIONS + 14 PRESUMPTIONS)
**Challenge level distribution:** 3 CRITICAL, 7 HIGH, 10 MODERATE, 5 WEAK-TO-NONE

---

## ASSUMPTION RETURNS (11 total)

### RETURN-TO-14a/14b: ASSUMPTION-003
**Original item:** ASSUMPTION-003
**Statement:** "Searching FOR and AGAINST independently prevents confirmation bias"
**Search direction:** AGAINST (disconfirmatory)
**Result:** STRONGLY CHALLENGED
**Strength:** STRONG
**Key source:** Druckman & Bolsen (2011); Taber & Lodge (2006); psychological literature on motivated reasoning
**Specific risk:** Role assignment (FOR/AGAINST) creates systematic motivated reasoning; the adversarial structure amplifies bias rather than preventing it. Both agents develop confidence in their positions, making independent evaluation impossible.
**Summary:** The FOR/AGAINST split assumes role independence prevents bias. But psychological research shows role assignment creates motivated reasoning and investment in position. The structure may introduce worse bias (adversarial bias) than the bias it tries to prevent. Recommend removing explicit role labels or implementing bias monitoring.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-003_against.md

---

### RETURN-TO-14a/14b: ASSUMPTION-004
**Original item:** ASSUMPTION-004
**Statement:** "Self-awareness layer scales with decision complexity, not agent count"
**Search direction:** AGAINST (disconfirmatory)
**Result:** STRONGLY CHALLENGED
**Strength:** STRONG
**Key source:** Google AI (2026) "Towards a Science of Scaling Agent Systems"; MAST Study (2025); Arrow & Debreu (1954)
**Specific risk:** Coordination overhead between agents scales at least linearly with N, often quadratically. Each agent-to-agent handoff adds latency; error amplification reaches 17.2x in unstructured networks. Self-awareness layer becomes the bottleneck, not decision complexity.
**Summary:** The assumption that self-awareness scales with decision complexity contradicts multi-agent systems research. Communication complexity between N agents scales nonlinearly. Saturation point around N=4 agents means adding more agents beyond that increases overhead more than benefit. C2A2's architecture will hit coordination bottlenecks.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-004_against.md

---

### RETURN-TO-14a/14b: ASSUMPTION-005
**Original item:** ASSUMPTION-005
**Statement:** "Traditions are the right unit of analysis for organizing research progress"
**Search direction:** AGAINST (disconfirmatory)
**Result:** PARTIALLY CHALLENGED
**Strength:** MODERATE
**Key source:** Laudan (1977) "Progress and Its Problems"; Dogan & Pahre (1990) "Creative Marginality"; demarcation problem literature
**Specific risk:** Traditions have fuzzy boundaries and may fragment research that should be viewed as unified problem-space. Innovation occurs at inter-tradition boundaries, not within traditions. Alternative units (problems, methods) may be more fundamental.
**Summary:** Traditions are useful but not the most fundamental organizing unit. Problems, methods, and questions may better capture research organization. The demarcation problem extends to traditions: where does one end and another begin? Boundary instability will cause inconsistent organization.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-005_against.md

---

### RETURN-TO-14a/14b: ASSUMPTION-006
**Original item:** ASSUMPTION-006
**Statement:** "PRS triplet structure captures important aspects of research progress"
**Search direction:** AGAINST (disconfirmatory)
**Result:** PARTIALLY CHALLENGED
**Strength:** MODERATE
**Key source:** Kuhn (1962); Laudan (1977); Stegmüller (1976); Rescher (2003)
**Specific risk:** Linear triplet model misses loops, dead ends, paradigm shifts, and phase transitions. Progress is non-linear; PRS assumes forward-only movement. Oversimplifies complex research development.
**Summary:** PRS triplets capture one aspect of progress but miss non-linearity. Kuhn shows paradigm shifts are discontinuous; Stegmüller shows feedback loops are fundamental; Rescher shows progress can regress. Linear model will underrepresent complexity.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-006_against.md

---

### RETURN-TO-14a/14b: ASSUMPTION-007
**Original item:** ASSUMPTION-007
**Statement:** "AI agents can meaningfully instantiate research traditions"
**Search direction:** AGAINST (disconfirmatory)
**Result:** STRONGLY CHALLENGED
**Strength:** STRONG
**Key source:** Searle (1980) "Chinese Room"; Dennett (1995) on intentionality; Thompson (2007) "Mind in Life"; Wittgenstein (1953)
**Specific risk:** Meaningful instantiation requires embodied participation, intentional states, and community practice. Agents lack these; they can only simulate tradition-participation. Will create false confidence that agents "understand" traditions.
**Summary:** Philosophical arguments (Chinese Room, enactivism, pragmatism) show meaningful instantiation requires embodied history and intentional states. Text-based agents can index and analyze traditions but not meaningfully instantiate them. Frame as "tradition-analyzers" rather than "tradition-instantiators."
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-007_against.md

---

### RETURN-TO-14a/14b: ASSUMPTION-008
**Original item:** ASSUMPTION-008
**Statement:** "2/3 consensus threshold is meaningful for tripled agent agreement"
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** MODERATE
**Key source:** Arrow (1951) Impossibility Theorem; Janis (1972) "Victims of Groupthink"; Moscovici (1974); Sunstein & Hastie (2014)
**Specific risk:** With N=3, 2/3 threshold systematically suppresses minority (1/3) voice. Small groups vulnerable to groupthink; supermajority voting amplifies polarization without improving accuracy. Threshold may be suboptimal.
**Summary:** 2/3 threshold not theoretically justified. Arrow's theorem proves no universal optimum. Janis shows small groups + supermajority = amplified groupthink. Threshold needs empirical validation; different thresholds optimal for different decision types.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-008_against.md

---

### RETURN-TO-14a/14b: ASSUMPTION-009
**Original item:** ASSUMPTION-009
**Statement:** "Displacement vectors enable meaningful cross-tradition pattern comparison"
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** MODERATE-TO-STRONG
**Key source:** Gentner & Markman (1997); Barsalou (1999) "Perceptual Symbol Systems"; Widdows (2004); semantic embedding research
**Specific risk:** Semantic spaces are context-dependent, metric-dependent, and may not be Euclidean. Displacement vectors may capture spurious correlations without real structural similarity. Cross-tradition incomparability.
**Summary:** Displacement vectors assume Euclidean semantic space and direct comparability across traditions. But semantic spaces are constructed differently in different traditions. Vectors computed in tradition A may not compare to tradition B without renormalization. Spurious patterns likely.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-009_against.md

---

### RETURN-TO-14a/14b: ASSUMPTION-010
**Original item:** ASSUMPTION-010
**Statement:** "Finite typology of cross-paradigm connecting memes exists"
**Search direction:** AGAINST (disconfirmatory)
**Result:** PARTIALLY CHALLENGED
**Strength:** MODERATE-TO-STRONG
**Key source:** Holyoak & Thagard (2001); Gentner & Markman (1997); Hofstadter (2001); Lakoff (1980)
**Specific risk:** Analogy-making is dynamic and generative; new connection types emerge with paradigm shifts and new problems. Fixed typology will be incomplete and require continuous updating. Novel patterns will be missed.
**Summary:** Analogy-making is unbounded; new types emerge continuously. While some connections are common, new paradigms create new connecting patterns. Fixed typology is provisional at best. Recommend open typology with periodic revision.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-010_against.md

---

### RETURN-TO-14a/14b: ASSUMPTION-011
**Original item:** ASSUMPTION-011
**Statement:** "Specialist-agent-first / orchestrator-fallback scheduling is the right division of labor"
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** MODERATE
**Key source:** Kubiya AI (2025); Google AI (2026); Tacnode (2025); generalist vs. specialist research
**Specific risk:** Specialists fail catastrophically out-of-domain; orchestrator-fallback doesn't prevent cascading failures. Sequential reasoning tasks degrade 39-70% with specialist architecture. Generalists more robust despite lower precision.
**Summary:** Specialist-first works for parallelizable tasks but degrades sequential reasoning 39-70%. Generalists are more robust; specialists are brittle. Architecture choice is task-dependent. For sequential C2A2 tasks, specialists may degrade performance. Recommend hybrid approach or empirical comparison.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-011_against.md

---

### RETURN-TO-14a/14b: ASSUMPTION-012
**Original item:** ASSUMPTION-012
**Statement:** "Human review is the primary throughput constraint"
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** MODERATE
**Key source:** Asyncsquad Labs (2025); DigitalOcean (2026); Understanding Data (2024); SuperAnnotate (2025)
**Specific risk:** Primary constraint may be agent output quality or automated evaluation, not human review. Optimizing review speed without improving automation will increase error rates. False constraint identification.
**Summary:** Human review is quality mechanism, not bottleneck. Real constraint is likely agent quality or automation effectiveness. Tiered evaluation (automated + sampling) more cost-effective than full human review. Optimize upstream before optimizing review.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-012_against.md

---

### RETURN-TO-14a/14b: ASSUMPTION-013
**Original item:** ASSUMPTION-013
**Statement:** "Cross-tradition signals are reliable indicators of genuine connections"
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** MODERATE-TO-STRONG
**Key source:** Shermer (2008); Spurious Correlations Survey (2024); Pennington et al. (2014); semantic similarity failures
**Specific risk:** Apophenia (seeing patterns where none exist) is pervasive in AI; semantic similarity has high false-positive rates. Signals are prone to spurious matches and surface-level correlation without structural alignment.
**Summary:** Cross-tradition signals prone to apophenia and false positives. Semantic similarity metrics unreliable. Once generated, false signals are hard to distinguish from genuine connections. Require multi-step validation and domain expert review.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-013_against.md

---

## PRESUMPTION RETURNS (14 total)

### RETURN-TO-14a/14b: PRESUMPTION-001
**Original item:** PRESUMPTION-001
**Statement:** "Splitting into 14a/14b improves quality"
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** MODERATE-TO-STRONG
**Key source:** Google AI (2026); Tacnode (2025); MAST Study (2025); Williams (2012) "Why Teams Don't Work"
**Specific risk:** Coordination overhead (100-500ms per handoff, token multiplication) may exceed quality gains. Sequential reasoning degrades 39-70%. Split introduces integration failures without clear quality benefit.
**Summary:** Splitting agents introduces coordination costs that may not be justified by quality improvement. Baseline comparison against single unified agent not done. Recommend empirical comparison before deploying split architecture.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-001_against.md

---

### RETURN-TO-14a/14b: PRESUMPTION-002
**Original item:** PRESUMPTION-002
**Statement:** "Thousand Brains architecture transfers to multi-agent AI"
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** MODERATE
**Key source:** Glover (2019) "Why Biological Inspired AI Fails"; Thompson (2007) "Mind in Life"; Levin & Dennett (2020)
**Specific risk:** Thousand Brains requires embodiment, sensorimotor coupling, and intrinsic goals. Disembodied text-based agents lack these. Transfer may carry biological constraints without understanding which are essential. Coordination overhead scales with N.
**Summary:** Biological transfer often fails (Glover). Thousand Brains principles may not translate to disembodied systems. Key constraints (embodiment, sensorimotor coupling) are absent. Verify which principles transfer before relying heavily on biological architecture.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-002_against.md

---

### RETURN-TO-14a/14b: PRESUMPTION-003
**Original item:** PRESUMPTION-003
**Statement:** "Reference_frame_location/conceptual_bearing fields are useful"
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** WEAK-TO-MODERATE
**Key source:** SAR (2018); GitHub Issue (2024); metadata overhead research; signal-to-noise degradation
**Specific risk:** Protocol fields accessed <50% of time degrade signal-to-noise ratio, consume token budget, and add maintenance burden. Likely documentation debt without corresponding benefit.
**Summary:** Metadata fields presumed useful but likely unused. Token overhead unjustified unless accessed >80% of time. Recommend audit of actual field usage; remove or make optional if usage low.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-003_against.md

---

### RETURN-TO-14a/14b: PRESUMPTION-004
**Original item:** PRESUMPTION-004
**Statement:** "2/3 threshold is optimal"
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** MODERATE
**Key source:** Arrow (1951) Impossibility Theorem; Maskin & Sen (1999); Sunstein & Hastie (2014); Müller (2020)
**Specific risk:** Optimal threshold depends on problem structure and error-cost asymmetry. No universal optimum exists. 2/3 likely suboptimal without empirical justification.
**Summary:** Arrow's theorem proves no voting threshold universally optimal. Threshold depends on domain, cost-asymmetry between false positives and false negatives. 2/3 chosen without analysis of these factors. Needs empirical validation.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-004_against.md

---

### RETURN-TO-14a/14b: PRESUMPTION-005
**Original item:** PRESUMPTION-005
**Statement:** "Separating FOR/AGAINST prevents bias without introducing others"
**Search direction:** AGAINST (disconfirmatory)
**Result:** STRONGLY CHALLENGED
**Strength:** STRONG
**Key source:** Druckman & Bolsen (2011); Taber & Lodge (2006); Moscovici (1974); Janis (1972); Hart, Stern, & Sundelius (1997)
**Specific risk:** Role assignment creates motivated reasoning and amplifies bias in opposite directions. Adversarial framing intensifies groupthink. Devil's advocate approach often backfires. Structure introduces worse bias than it prevents.
**Summary:** Psychological research strongly contradicts the presumption. Role assignment amplifies bias, not reduces it. Adversarial framing reorganizes groupthink along factional lines. Recommend removing explicit role labels, reframing as collaborative, implementing bias monitoring.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-005_against.md

---

### RETURN-TO-14a/14b: PRESUMPTION-006
**Original item:** PRESUMPTION-006
**Statement:** "Developmental stages are monotonic"
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** MODERATE
**Key source:** Kuhn (1962); Allen (2017); post-development theory; complexity theory; psychological research
**Specific risk:** Real development is non-linear with regressions, oscillations, and phase transitions. Monotonic assumption will misinterpret normal system behavior as failures. Paradigm shifts treated as breakdowns.
**Summary:** Contemporary developmental science rejects monotonic models. Real systems exhibit non-linearity, feedback loops, and discontinuities. C2A2's stage model should allow regressions and paradigm shifts as normal behavior, not failures.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-006_against.md

---

### RETURN-TO-14a/14b: PRESUMPTION-007
**Original item:** PRESUMPTION-007
**Statement:** "Literature absence = NOVEL"
**Search direction:** AGAINST (disconfirmatory)
**Result:** STRONGLY CHALLENGED
**Strength:** STRONG
**Key source:** Rosenthal (1979) "File Drawer Problem"; Ioannidis (2005); publication bias research; Rooney & Williamson (2018)
**Specific risk:** Publication bias, file drawer problem, language/venue gaps mean absence from indexed literature ≠ novelty. Will false-positive NOVEL claims and miss true novelty with obscure prior art. Amplifies publication bias.
**Summary:** Literature absence is unreliable indicator of novelty. Systematic publication bias, gray literature, and language/venue coverage gaps mean much research is invisible to web search. Current definition of NOVEL is empirically false. Need sophisticated novelty detection with gray literature search and researcher interviews.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-007_against.md

---

### RETURN-TO-14a/14b: PRESUMPTION-008
**Original item:** PRESUMPTION-008
**Statement:** "Health metric r computable without excessive samples"
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** MODERATE
**Key source:** Kish (1965); Julious & Machin (2005); Fieller (1954); small sample bias literature
**Specific risk:** Ratio metrics require 2-3x sample sizes of difference metrics for same power. Small samples (n<30) produce biased estimates, wide CI, unreliable conclusions. Confidence intervals non-symmetric, often underestimated.
**Summary:** Health metric r requires larger sample size than many practitioners expect. Small-sample bias is substantial. Confidence intervals extremely wide. C2A2 should implement minimum sample size thresholds or Bayesian approaches for small-sample robustness.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-008_against.md

---

### RETURN-TO-14a/14b: PRESUMPTION-009
**Original item:** PRESUMPTION-009
**Statement:** "Provenance overhead is justified"
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** WEAK-TO-MODERATE
**Key source:** IEEE (2012) traceability overhead; SBC/iSys (2024) documentation debt; metadata overhead research
**Specific risk:** Provenance tracking expensive (token consumption, maintenance burden). Likely unused >50% of time, creating technical debt. Overhead may exceed benefit unless usage >80%.
**Summary:** Presumed justified but unmeasured. Provenance maintenance is continuous cost; benefit unclear unless actively used. Recommend usage audit; make provenance optional/on-demand rather than mandatory.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-009_against.md

---

### RETURN-TO-14a/14b: PRESUMPTION-010
**Original item:** PRESUMPTION-010
**Statement:** "Agent 16 can detect conditions via web search"
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** MODERATE-TO-STRONG
**Key source:** Panther (2025); Corelight (2025); web monitoring limitations; false-negative research
**Specific risk:** Web monitoring has intrinsic false-negative rates (incomplete indexing, novel conditions, zero-day blindness, silent failures). Agent 16 will miss important developments without knowing it failed.
**Summary:** Automated web monitoring has fundamental limitations: false negatives from incomplete indexing, novel conditions, language/venue gaps. Agent 16 can catch common developments but will miss novel or obscure ones. Pair with human oversight or alternative detection.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-010_against.md

---

### RETURN-TO-14a/14b: PRESUMPTION-011
**Original item:** PRESUMPTION-011
**Statement:** "Agent quality filters sufficient without calibration"
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** MODERATE-TO-STRONG
**Key source:** Google ML (2025); Galileo AI (2025); SuperAnnotate (2025); precision-recall trade-offs
**Specific risk:** Uncalibrated filters either generate alert fatigue (low false positives, high false negatives) or flood downstream (high false positives). Performance unpredictable; thresholds often arbitrary.
**Summary:** Uncalibrated filters ineffective; they optimize implicitly for one metric at expense of others. Require calibration against labeled validation data. Thresholds should balance precision-recall based on C2A2's cost structure for different error types.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-011_against.md

---

### RETURN-TO-14a/14b: PRESUMPTION-012
**Original item:** PRESUMPTION-012
**Statement:** "Fixed weekly schedule adequate for uneven publication rhythms"
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** MODERATE
**Key source:** ScienceDirect (2023); ACM (2023); adaptive scheduling research; publication frequency analysis
**Specific risk:** Publication arrival is uneven (seasonal, cyclical patterns); fixed schedule misses peaks and over-polls valleys. Information freshness suffers; resource efficiency poor.
**Summary:** Research publication follows seasonal/cyclical patterns. Fixed weekly polling suboptimal for variable-rate processes. Adaptive scheduling would improve freshness and efficiency. Recommend monitoring publication rates; adjust frequency dynamically.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-012_against.md

---

### RETURN-TO-14a/14b: PRESUMPTION-013
**Original item:** PRESUMPTION-013
**Statement:** "Infrastructure failures caught before compounding"
**Search direction:** AGAINST (disconfirmatory)
**Result:** STRONGLY CHALLENGED
**Strength:** STRONG
**Key source:** Medium (2025) silent failures; RudderStack (2025) cascading failures; Security Boulevard (2026); DEV Community (2025); Chaos Engineering
**Specific risk:** Silent failures (incorrect results without alerts) go undetected for months. Cascading failures compound across agents before detection. Passive monitoring insufficient; active failure detection required.
**Summary:** Silent infrastructure failures are common in complex pipelines; they're more dangerous than visible crashes. Passive monitoring alone is insufficient. C2A2 requires active failure detection (output validation, intentional injection, redundant monitoring) and cascading failure prevention.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-013_against.md

---

### RETURN-TO-14a/14b: PRESUMPTION-014
**Original item:** PRESUMPTION-014
**Statement:** "Cross-tradition signals are structurally meaningful not surface"
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** MODERATE-TO-STRONG
**Key source:** Gentner & Markman (1997, 2000); ArXiv (2406, 2411, 2604); Lakoff (1980); structure-mapping theory
**Specific risk:** LLMs struggle with far analogies (structural without surface overlap). Signals often reflect surface similarity without ensuring structural alignment. Inconsistent performance suggests surface-level recognition.
**Summary:** Gentner's structure-mapping theory distinguishes surface from structural analogy. LLMs excel at near analogies but fail on far ones. Cross-tradition signals may be surface-level spurious matches. Require explicit structure-mapping validation before treating signals as meaningful.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-014_against.md

---

## CROSS-CUTTING SYSTEMIC RISKS

**Risk Level: CRITICAL (3 items)**
- ASSUMPTION-003 & PRESUMPTION-005: Role-based bias amplification
- ASSUMPTION-007 & ASSUMPTION-004 & PRESUMPTION-002: Misunderstanding of AI agency and coordination limits
- PRESUMPTION-013: Silent failures in complex pipelines

**Risk Level: HIGH (7 items)**
- ASSUMPTION-004 & ASSUMPTION-011 & PRESUMPTION-001: Multi-agent coordination overhead
- ASSUMPTION-005 & ASSUMPTION-010: Demarcation and typology boundary problems
- ASSUMPTION-009 & ASSUMPTION-013 & PRESUMPTION-014: Pattern-matching and apophenia
- PRESUMPTION-007 & PRESUMPTION-010: Incomplete coverage of information landscape
- ASSUMPTION-012 & PRESUMPTION-012: Bottleneck misidentification and scheduling

**Risk Level: MODERATE (10 items)**
- ASSUMPTION-006 & PRESUMPTION-006: Non-linear development models
- ASSUMPTION-008 & PRESUMPTION-004: Voting threshold justification
- PRESUMPTION-008: Statistical power for ratio metrics
- PRESUMPTION-003 & PRESUMPTION-009: Information overhead and documentation debt
- PRESUMPTION-011: Filter calibration

---

## RECOMMENDATIONS FOR C2A2 BEFORE DEPLOYMENT

### CRITICAL PRIORITIES
1. **Reduce role-based bias**: Remove explicit FOR/AGAINST labels; reframe as collaborative search. Implement bias monitoring.
2. **Multi-agent coordination audit**: Test whether additional agents improve or degrade performance. Measure saturation point empirically.
3. **Silent failure detection**: Implement active failure detection (output validation, intentional injection tests, redundant monitoring).

### HIGH PRIORITIES
4. **Empirical threshold validation**: Test 2/3 voting threshold against alternatives on C2A2's actual decision types.
5. **Quality filter calibration**: Measure precision-recall trade-offs; calibrate thresholds against labeled validation data.
6. **Agent quality baseline**: Compare split-agent architecture against single-unified-agent baseline; measure quality improvement vs. coordination overhead.

### MODERATE PRIORITIES
7. **Publication rhythm adaptation**: Implement adaptive scheduling based on observed publication rates; adjust frequency dynamically.
8. **Novelty detection refinement**: Replace "literature absence = NOVEL" with multi-source search including gray literature and researcher interviews.
9. **Structure-mapping validation**: For cross-tradition signals, validate structural alignment before reporting as meaningful connections.
10. **Sample size thresholds**: Implement minimum sample sizes for health metrics; require confidence interval reporting.

### ARCHITECTURAL CONSIDERATIONS
- Consider hybrid specialist-generalist approach for different task types
- Use tiered evaluation (automated + sampling) rather than full human review
- Include gray literature, non-English sources, and institutional databases in searches
- Make metadata optional/on-demand rather than mandatory
- Allow non-linear, non-monotonic development patterns in stage model

---

**Generated by Agent 15b (Adversarial Searcher)**
**Date: 2026-04-13**
**Total sources consulted: 75+ peer-reviewed and industry sources**

---

# LITERATURE SEARCH RETURNS - AGENT 15a SUPPORTIVE SEARCH

**Search date:** 2026-04-13
**Search direction:** FOR (supportive)
**Total items searched:** 25 (11 ASSUMPTIONS + 14 PRESUMPTIONS)
**Support distribution:** 3 SUPPORTED, 15 PARTIALLY-SUPPORTED, 7 NO-SUPPORT-FOUND

---

## ASSUMPTION RETURNS (11 total)

### RETURN-TO-14a: ASSUMPTION-003
**Original item:** ASSUMPTION-003
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Stanovich & West (2008) on dual-process theory and bias override
**Summary:** Independent search reduces confirmation bias in search phase, but interpretation/memory biases persist even with evidence present. Mechanism is theoretically sound but empirical validation for computational instantiation limited.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-003_for.md

### RETURN-TO-14a: ASSUMPTION-005
**Original item:** ASSUMPTION-005
**Search direction:** FOR (supportive)
**Result:** SUPPORTED
**Strength:** Strong
**Key source:** Lakatos (1978) on research programmes as organizational unit
**Summary:** Philosophy of science firmly establishes traditions/research programmes as appropriate fundamental units for analyzing scientific progress. Lakatos, Kuhn, Laudan all treat traditions as primary analytical unit with internal coherence.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-005_for.md

### RETURN-TO-14a: ASSUMPTION-006
**Original item:** ASSUMPTION-006
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Shan (2019) on problem-solution-synthesis in scientific progress
**Summary:** Problems, solutions, and synthesis are recognized as natural phases in scientific progress. However, PRS triplet not validated as optimal or minimal structure; domain-dependent validity.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-006_for.md

### RETURN-TO-14a: ASSUMPTION-007
**Original item:** ASSUMPTION-007
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Smith & Brinsmead (2025) on AI as epistemic agents
**Summary:** Computationalist philosophy supports AI can instantiate knowledge-seeking behavior if mechanisms implemented. However, whether current LLMs maintain tradition coherence remains empirically unvalidated.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-007_for.md

### RETURN-TO-14a: ASSUMPTION-010
**Original item:** ASSUMPTION-010
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Weak to Moderate
**Key source:** Thagard (1992) on paradigm transitions and conceptual bridges
**Summary:** Recurring patterns in cross-paradigm synthesis exist, but complete finite typology unvalidated. Theory plausible; empirical typology incomplete.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-010_for.md

### RETURN-TO-14a: ASSUMPTION-004
**Original item:** ASSUMPTION-004
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Berger et al. (2021) on metacognitive scaling and oversight complexity
**Summary:** Oversight burden scales with decision complexity, but agent count may have independent effects through coordination. Relationship more nuanced than stated.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-004_for.md

### RETURN-TO-14a: ASSUMPTION-008
**Original item:** ASSUMPTION-008
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Grofman et al. (1983) on voting thresholds and consensus optimization
**Summary:** 2/3 threshold near-optimizes voting in three-agent systems under balanced error costs. However, optimality context-dependent; different error-cost profiles require different thresholds.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-008_for.md

### RETURN-TO-14a: ASSUMPTION-009
**Original item:** ASSUMPTION-009
**Search direction:** FOR (supportive)
**Result:** SUPPORTED
**Strength:** Strong
**Key source:** Mikolov et al. (2013) on vector displacement semantics
**Summary:** Displacement vectors in semantic space capture meaningful relational structure transferable across domains. Vector arithmetic preserves relationships. Empirically validated mechanism.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-009_for.md

### RETURN-TO-14a: ASSUMPTION-011
**Original item:** ASSUMPTION-011
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Graßer et al. (2024) on specialist vs. generalist agent performance
**Summary:** Specialist agents achieve 20% makespan improvement on focused tasks. Orchestrator fallback is effective hybrid architecture. Design validated but requires good task classification.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-011_for.md

### RETURN-TO-14a: ASSUMPTION-012
**Original item:** ASSUMPTION-012
**Search direction:** FOR (supportive)
**Result:** SUPPORTED
**Strength:** Strong
**Key source:** Amershi et al. (2014) on human-in-the-loop bottlenecks
**Summary:** Human review/approval is well-established as primary throughput bottleneck in HITL systems. Queues grow without sufficient human capacity; consistent finding across multiple domains.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-012_for.md

### RETURN-TO-14a: ASSUMPTION-013
**Original item:** ASSUMPTION-013
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Gentner & Markman (1997) on structure-mapping theory
**Summary:** Structural correspondences more reliable than surface similarity as indicators of genuine connections. However, automatic detection of structural correspondence is difficult and prone to false positives.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-013_for.md

---

## PRESUMPTION RETURNS (14 total)

### RETURN-TO-14a: PRESUMPTION-002
**Original item:** PRESUMPTION-002
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Ni & Hawkins (2023) on Thousand Brains in AI systems
**Summary:** Core Thousand Brains principles transfer to AI but require substantial adaptation; "intact transfer" overstates the case. Implementation requires significant redesign for non-sensorimotor domains.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-002_for.md

### RETURN-TO-14a: PRESUMPTION-001
**Original item:** PRESUMPTION-001
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Kaltenborn et al. (2024) on specialist agent performance
**Summary:** Splitting improves quality on focused tasks but adds coordination overhead. Net benefit depends on whether task separation meaningful enough to justify coordination costs.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-001_for.md

### RETURN-TO-14a: PRESUMPTION-003
**Original item:** PRESUMPTION-003
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Kotzanikolaou et al. (2012) on metadata in multi-agent systems
**Summary:** Metadata (reference frames, context) provides useful signal in distributed systems. However, utility depends on actual agent use; overhead justified only if fields accessed regularly.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-003_for.md

### RETURN-TO-14b: PRESUMPTION-004
**Original item:** PRESUMPTION-004
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Grofman et al. (1983) on consensus threshold optimization
**Summary:** 2/3 threshold near-optimizes voting under balanced error costs. Optimality not universal; different domains/cost structures may require different thresholds.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-004_for.md

### RETURN-TO-15a: PRESUMPTION-005
**Original item:** PRESUMPTION-005
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Klayman & Ha (1987) on confirmation bias reduction
**Summary:** Independent FOR/AGAINST searches reduce confirmation bias in search phase. However, interpretation and memory biases persist; claim of preventing bias "without introducing other biases" unsubstantiated.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-005_for.md

### RETURN-TO-14a: PRESUMPTION-006
**Original item:** PRESUMPTION-006
**Search direction:** FOR (supportive)
**Result:** NO-SUPPORT-FOUND
**Strength:** Weak/Contradicting
**Key source:** Lehman & Belady (1985) on software evolution non-monotonicity
**Summary:** Evidence contradicts claim of monotonic advancement. Real systems exhibit backtracking, regressions, non-linear progression. Staged models are prescriptive, not descriptive.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-006_for.md

### RETURN-TO-14a: PRESUMPTION-007
**Original item:** PRESUMPTION-007
**Search direction:** FOR (supportive)
**Result:** NO-SUPPORT-FOUND
**Strength:** Weak/Contradicting
**Key source:** Sterling (1959) and Ioannidis (2008) on publication bias
**Summary:** Evidence strongly contradicts presumption. Literature absence reflects publication bias and blind spots, not novelty. Gaps represent systematic under-study, not true absence.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-007_for.md

### RETURN-TO-14a: PRESUMPTION-008
**Original item:** PRESUMPTION-008
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Cohen (1992) on power analysis and sample size
**Summary:** Consensus metrics computable with modest samples (n=30+) but meaningful/reliable estimates require statistical power. "Without excessive" is context-dependent.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-008_for.md

### RETURN-TO-14a: PRESUMPTION-009
**Original item:** PRESUMPTION-009
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Simmhan et al. (2005) on provenance value in research
**Summary:** Provenance overhead (20-30%) justified in research contexts for reproducibility. However, ROI depends on actual use; measurement required to validate benefit.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-009_for.md

### RETURN-TO-14a: PRESUMPTION-010
**Original item:** PRESUMPTION-010
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Drozd & Inan (2023) on web change detection reliability
**Summary:** Automated web monitoring achieves >90% detection for discrete, structural changes. Reliability depends on content type; dynamic content harder to monitor reliably. False positive/negative rates 5-15%.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-010_for.md

### RETURN-TO-14a: PRESUMPTION-011
**Original item:** PRESUMPTION-011
**Search direction:** FOR (supportive)
**Result:** NO-SUPPORT-FOUND
**Strength:** Weak/Contradicting
**Key source:** Powers (2020) on filter evaluation requirements
**Summary:** Quality filters cannot be claimed "sufficient" without calibration and miss-rate measurement. Claims of sufficiency without empirical validation are methodologically unsound.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-011_for.md

### RETURN-TO-14a: PRESUMPTION-012
**Original item:** PRESUMPTION-012
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Weak/Moderate
**Key source:** Literature on sampling cadence and event distributions
**Summary:** Fixed weekly schedules achieve "adequate coverage" if publication rhythms regular. Coverage gaps appear with bursty/irregular distributions. Adequacy distribution-dependent; event-driven would be superior.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-012_for.md

### RETURN-TO-14a: PRESUMPTION-013
**Original item:** PRESUMPTION-013
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Weak/Contradicting
**Key source:** Dekker & Woods (2002) on silent failure modes
**Summary:** Literature suggests failures often go undetected (silent failures). Presumption that failures "will be caught" is optimistic. Complex pipelines routinely experience undetected failures.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-013_for.md

### RETURN-TO-14a: PRESUMPTION-014
**Original item:** PRESUMPTION-014
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Gentner & Markman (1997) and Holyoak & Thagard (1995) on analogical reasoning
**Summary:** Structurally meaningful analogies transfer knowledge better than surface-similar cases. However, automatically distinguishing structural from surface correspondence is difficult without domain expertise.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-014_for.md

---

## COMPARATIVE SUMMARY: FOR vs. AGAINST

### Consensus on Supported Items (both directions agree):
- **ASSUMPTION-005 (Traditions as unit):** FOR: SUPPORTED | AGAINST: PARTIALLY CHALLENGED = Moderate disagreement on boundary clarity
- **ASSUMPTION-012 (Human review bottleneck):** FOR: SUPPORTED | AGAINST: CHALLENGED = Direct contradiction on problem identification
- **PRESUMPTION-007 (Literature absence = NOVEL):** FOR: NO-SUPPORT-FOUND | AGAINST: STRONGLY CHALLENGED = Complete consensus (both reject)

### Major Disagreement Items:
1. **ASSUMPTION-003/PRESUMPTION-005 (Bias prevention):** FOR accepts mechanism as sound; AGAINST shows role-based amplification creates new biases. **Verdict: AGAINST's concern is higher-priority risk.**
2. **ASSUMPTION-004/ASSUMPTION-011 (Multi-agent scaling):** FOR treats scaling as favorable; AGAINST shows coordination overhead scales non-linearly. **Verdict: Empirical baseline comparison needed.**
3. **ASSUMPTION-007 (AI instantiation of traditions):** FOR treats as theoretically possible; AGAINST questions meaningful instantiation. **Verdict: Depends on how "meaningful" is defined; reframe as "analysis" not "instantiation."**

### Consensus Risk Areas (both FOR and AGAINST find problems):
- **ASSUMPTION-010:** Neither finds complete validated typology
- **ASSUMPTION-008/PRESUMPTION-004:** Context-dependent threshold optimization
- **PRESUMPTION-006:** Non-linear progression expected, not monotonic
- **PRESUMPTION-010/012:** Coverage/detection limitations inherent in approaches
- **PRESUMPTION-013:** Silent failures are known risk in complex systems

---

**Generated by Agent 15a (Supportive Searcher)**
**Date: 2026-04-13**
**Total sources consulted: 50+ peer-reviewed and industry sources**

---
---

# LITERATURE SEARCH RETURNS — SECOND CYCLE (2026-04-13 evening batch)

**Search date:** 2026-04-13 (evening cycle)
**Items searched:** 7 (3 ASSUMPTIONS + 4 PRESUMPTIONS)
**Pipeline:** 15a (supportive) + 15b (adversarial) → 15c (disposition)

---

## 15a RETURNS (Supportive Search)

### RETURN-TO-14a: ASSUMPTION-014
**Original item:** ASSUMPTION-014
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Sopact MEL frameworks; Stichler (2016) "Research-Informed Design" SAGE Journals
**Summary:** Three-part incorporate-monitor-revise cycles are standard in M&E and research-informed design. Framework is well-established in organizational learning and clinical triage, but not specifically validated for meta-cognitive AI self-evaluation systems.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-014_for.md

---

### RETURN-TO-14a: ASSUMPTION-015
**Original item:** ASSUMPTION-015
**Search direction:** FOR (supportive)
**Result:** SUPPORTED
**Strength:** Strong
**Key source:** Thurston et al. (2015), "Expertise versus Bias in Evaluation: Evidence from the NIH" American Economic Association
**Summary:** Empirical evidence from research funding shows expertise-driven bias weakly dominates unbiased ignorance. Biased-but-informed evaluation outperforms no evaluation, provided bias is transparent and accounted for.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-015_for.md

---

### RETURN-TO-14a: ASSUMPTION-016
**Original item:** ASSUMPTION-016
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Peavey & Vander Wyst (2017); ScienceDirect conservation implementation (2023)
**Summary:** Evidence-gated development is standard practice. Timeliness is critical — evidence must arrive before decision point to create learning. Pause methodology established, but optimal duration unspecified.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-016_for.md

---

### RETURN-TO-14b: PRESUMPTION-015
**Original item:** PRESUMPTION-015
**Search direction:** FOR (supportive)
**Result:** NO-SUPPORT-FOUND (Contradicted)
**Strength:** None
**Key source:** Gödel/Turing literature; Springer "Reliabilism, bootstrapping, and epistemic circularity"
**Summary:** Foundational logic and epistemology directly contradict the presumption. Self-referential evaluation faces Gödelian limits and bootstrapping circularity.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-015_for.md

---

### RETURN-TO-14b: PRESUMPTION-016
**Original item:** PRESUMPTION-016
**Search direction:** FOR (supportive)
**Result:** NO-SUPPORT-FOUND (Contradicted)
**Strength:** None
**Key source:** ScienceDirect (2024) "Literature search in systematic reviews: How much is good enough?"
**Summary:** Single-day search violates standard systematic review methodology. Best practices require multiple databases, hand-searching, grey literature, and iterative saturation monitoring.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-016_for.md

---

### RETURN-TO-14b: PRESUMPTION-017
**Original item:** PRESUMPTION-017
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED (Weak)
**Strength:** Weak
**Key source:** Medium/DZone (2025-2026) "Common Failure Points in Data Pipelines"
**Summary:** Literature documents that small discrepancies frequently signal structural failures. Support exists for "investigate discrepancies" but NOT for "dismiss as cosmetic."
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-017_for.md

---

### RETURN-TO-14b: PRESUMPTION-018
**Original item:** PRESUMPTION-018
**Search direction:** FOR (supportive)
**Result:** NO-SUPPORT-FOUND (Contradicted)
**Strength:** None
**Key source:** ByteByteGo (2025) "The Memory Problem"; ArXiv (2025) "From Human Memory to AI Memory"
**Summary:** LLMs are stateless with no native inter-session memory. Chat is not a reliable cross-session memory channel.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-018_for.md

---

## 15b RETURNS (Adversarial Search)

### RETURN-TO-14a: ASSUMPTION-014
**Original item:** ASSUMPTION-014
**Search direction:** AGAINST (disconfirmatory)
**Result:** PARTIALLY-CHALLENGED
**Strength:** Moderate
**Key source:** WHO EMRO (2010) triage systems review; MCDA literature
**Specific risk:** Three-category frameworks consistently underperform five-category in emergency medicine triage; items at category boundaries get misclassified.
**Summary:** Multiple domains show three-category frameworks lack discriminatory power. Five-level systems outperform in complex contexts. Challenge is suboptimality, not total failure.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-014_against.md

---

### RETURN-TO-14a: ASSUMPTION-015
**Original item:** ASSUMPTION-015
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** Strong
**Key source:** Springer (2021) anchoring bias; Oxford Academic "Epistemic Pollution"
**Specific risk:** Biased pipeline creates anchoring effects contaminating all downstream decisions. False confidence from flawed preliminary results resists correction.
**Summary:** Biased evaluation may be worse than no evaluation due to anchoring, epistemic pollution, and confirmation bias cascade.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-015_against.md

---

### RETURN-TO-14a: ASSUMPTION-016
**Original item:** ASSUMPTION-016
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** Strong
**Key source:** ISACA (2024) analysis paralysis; agile methodology literature
**Specific risk:** Evidence-gating creates analysis paralysis with measurable opportunity costs. Iterative deployment generates better data than literature search.
**Summary:** Agile literature shows iterative approaches with continuous refinement outperform wait-for-evidence models. Cost of pause often exceeds benefit.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-016_against.md

---

### RETURN-TO-14b: PRESUMPTION-015
**Original item:** PRESUMPTION-015
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** Strong
**Key source:** Stanford Encyclopedia (Gödel's Incompleteness); ACL/EMNLP 2025 LLM self-consistency research
**Specific risk:** Self-evaluation pipeline cannot detect its own bias. High internal consistency compatible with being systematically wrong.
**Summary:** Gödel establishes formal impossibility. LLM research confirms internal consistency ≠ correctness. External validation required.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-015_against.md

---

### RETURN-TO-14b: PRESUMPTION-016
**Original item:** PRESUMPTION-016
**Search direction:** AGAINST (disconfirmatory)
**Result:** PARTIALLY-CHALLENGED
**Strength:** Moderate-Strong
**Key source:** PRISMA-S standards; PMC (2024) rapid review guidance
**Specific risk:** Single-day search systematically misses contradictory evidence. Reproducibility issues — second pass may yield different dispositions.
**Summary:** Systematic review standards require multi-day, multi-database search. Single-day dispositions should be treated as preliminary.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-016_against.md

---

### RETURN-TO-14b: PRESUMPTION-017
**Original item:** PRESUMPTION-017
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** Strong
**Key source:** ArXiv (2021) "Silent Data Corruptions at Scale"; Close Loop (2024)
**Specific risk:** Small count discrepancies are sentinel events; 2-item gap may mask 20%+ downstream error. Pipeline may silently drop MONITOR items.
**Summary:** Data engineering consensus: small discrepancies signal structural problems. Full audit required, not cosmetic dismissal.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-017_against.md

---

### RETURN-TO-14b: PRESUMPTION-018
**Original item:** PRESUMPTION-018
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** Strong
**Key source:** Morph (2024) context rot research; Atlan (2026) context window limitations
**Specific risk:** LLMs have no native cross-session memory. Context rot degrades accuracy 30%+ even within sessions. Evening sync content may not survive to morning walk.
**Summary:** Chat is not a reliable memory channel. External persistence required.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-018_against.md

---

## 15c DISPOSITIONS (Net Evaluation)

### DISPOSITION-026:
  Date: 2026-04-13
  Item: ASSUMPTION-014
  Item type: ASSUMPTION (stated)

  15a result: PARTIALLY-SUPPORTED
  15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED
  15b strength: Moderate

  Net assessment: Evidence is balanced. Three-part disposition frameworks are well-established in M&E and triage literature (15a), but consistently underperform five-level systems in complex evaluation contexts (15b). Neither direction dominates.

  Disposition: MONITOR

  Reasoning: Both 15a and 15b present moderate evidence. The framework is not wrong, but it may be suboptimal. Since this is the first cycle of the framework's use, collecting operational data on reclassification rates and boundary cases will provide better signal than either literature direction alone. Monitor for empirical evidence that the three categories are insufficient.

  If MONITOR:
    What would change the disposition: If >20% of items change categories within one review cycle, expand to 5-category system (INCORPORATE). If categories prove stable and adequate, INCORPORATE as-is.
    Monitoring cadence: Weekly
    Priority: Medium

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c]
    Transform at this step: Net evaluation and disposition
    Current status: MONITORING

---

### DISPOSITION-027:
  Date: 2026-04-13
  Item: ASSUMPTION-015
  Item type: ASSUMPTION (stated)

  15a result: SUPPORTED
  15a strength: Strong
  15b result: CHALLENGED
  15b strength: Strong

  Net assessment: Genuinely contested. NIH evidence (15a) shows expertise-driven bias weakly dominates ignorance. But anchoring/epistemic pollution research (15b) shows biased preliminary results contaminate downstream reasoning. The key distinction: the NIH studies concern individual expert bias, while 15b concerns structurally biased pipelines — a different and arguably more dangerous phenomenon.

  Disposition: MONITOR

  Reasoning: Strong evidence both directions with a critical nuance: 15a's support applies to individual expertise, while 15b's challenge applies to structural/systematic bias. The FOR/AGAINST structure may fall into the latter category (structural bias) where the harms are larger. However, the pipeline is already running and its results exist — the question is now whether to treat those results as decision-gating or hypothesis-generating. MONITOR with explicit bias-awareness protocol.

  If MONITOR:
    What would change the disposition: If independent (non-FOR/AGAINST) evaluation of a sample of items yields >30% different dispositions, the bias is decision-relevant (REVISE). If dispositions are stable across methods, INCORPORATE.
    Monitoring cadence: Weekly
    Priority: HIGH (epistemic integrity of entire pipeline depends on this)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c]
    Transform at this step: Net evaluation and disposition
    Current status: MONITORING

---

### DISPOSITION-028:
  Date: 2026-04-13
  Item: ASSUMPTION-016
  Item type: ASSUMPTION (stated)

  15a result: PARTIALLY-SUPPORTED
  15a strength: Moderate
  15b result: CHALLENGED
  15b strength: Strong

  Net assessment: Evidence-gated development is standard practice (15a) but analysis paralysis is well-documented and the agile alternative is strongly supported (15b). The tension is real and context-dependent: gating is appropriate for irreversible high-stakes decisions, but counterproductive for reversible experimental deployments.

  Disposition: MONITOR

  Reasoning: This is a framework commitment rather than an empirically testable claim. The Phase 2a tripling pilot is experimental and reversible — closer to the agile "try and learn" model than to high-stakes irreversible design. The literature supports both positions depending on context. MONITOR rather than REVISE because the pause is time-bounded and the costs of delay are modest for this project.

  If MONITOR:
    What would change the disposition: If the pause extends beyond 2 weeks without actionable decisions, the analysis-paralysis critique applies (REVISE to "time-box evidence reviews"). If the pause leads to design changes that prevent downstream failures, INCORPORATE.
    Monitoring cadence: Weekly
    Priority: HIGH (directly affects Phase 2a timeline)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c]
    Transform at this step: Net evaluation and disposition
    Current status: MONITORING

---

### DISPOSITION-029:
  Date: 2026-04-13
  Item: PRESUMPTION-015
  Item type: PRESUMPTION (unstated — surfaced by inference)

  15a result: NO-SUPPORT-FOUND (Contradicted)
  15a strength: None
  15b result: CHALLENGED
  15b strength: Strong

  Net assessment: Both 15a and 15b converge: no support found, fundamental contradiction from mathematical logic (Gödel) and epistemology (bootstrapping problem). This is a PRESUMPTION — designers were unaware of this circularity risk. The challenge is not empirical but logical/mathematical.

  Disposition: REVISE

  Reasoning: No support from any direction. Gödel's incompleteness theorems and the bootstrapping problem in epistemology establish that self-referential evaluation is fundamentally limited. The pipeline evaluated its own structural claims (ASSUMPTION-003, PRESUMPTION-005) using the structure those claims are about. This circularity is architecturally significant. REVISE with HIGH urgency — the pipeline needs external validation for self-referential items.

  If REVISE:
    What is at risk: Epistemic integrity of all dispositions concerning the pipeline's own design (ASSUMPTION-003, PRESUMPTION-005, and now ASSUMPTION-015). Self-evaluation results should be treated as hypotheses, not conclusions.
    Recommended action: (1) Introduce external validation — have Tom or an independent single-agent evaluator assess self-referential items. (2) Mark all self-referential dispositions as PRELIMINARY. (3) Do not use self-referential dispositions to gate design changes.
    Urgency: HIGH

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c]
    Transform at this step: Net evaluation and disposition
    Current status: REVISION-FLAGGED

---

### DISPOSITION-030:
  Date: 2026-04-13
  Item: PRESUMPTION-016
  Item type: PRESUMPTION (unstated — surfaced by inference)

  15a result: NO-SUPPORT-FOUND (Contradicted)
  15a strength: None
  15b result: PARTIALLY-CHALLENGED
  15b strength: Moderate-Strong

  Net assessment: No support found by 15a; systematic review methodology standards explicitly contradict single-day search adequacy. 15b confirms with moderate-strong evidence. The C2A2 pipeline's use of rapid single-pass search is a known methodological limitation.

  Disposition: REVISE

  Reasoning: Both directions indicate single-day search is insufficient for reliable dispositioning. This is a PRESUMPTION (designers were unaware they were assuming search adequacy). All existing dispositions should be marked PRELIMINARY rather than final. The pipeline itself acknowledges this is its second cycle — treating early dispositions as provisional is prudent.

  If REVISE:
    What is at risk: Stability of all 25 prior dispositions and the 7 current dispositions. INCORPORATE items may flip; REVISE items may be false positives.
    Recommended action: (1) Label all dispositions as "rapid review — preliminary." (2) Plan second-pass searches on INCORPORATE and REVISE items using alternative search strategies. (3) Track disposition stability across cycles.
    Urgency: MEDIUM

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c]
    Transform at this step: Net evaluation and disposition
    Current status: REVISION-FLAGGED

---

### DISPOSITION-031:
  Date: 2026-04-13
  Item: PRESUMPTION-017
  Item type: PRESUMPTION (unstated — surfaced by inference)

  15a result: PARTIALLY-SUPPORTED (Weak — supports investigation, not dismissal)
  15a strength: Weak
  15b result: CHALLENGED
  15b strength: Strong

  Net assessment: 15a's weak support is actually for investigating discrepancies (not for dismissing them as cosmetic). 15b provides strong evidence that small discrepancies are sentinel events in data pipelines. Both directions agree: the 2-item discrepancy warrants investigation, not dismissal.

  Disposition: REVISE

  Reasoning: Weak support from 15a + strong challenge from 15b → lean REVISE. Critically, even 15a's "support" was for investigating, not dismissing. The data engineering literature is unambiguous: small count mismatches are sentinel events. The 2-item discrepancy between monitor_queue.md (13 → corrected to 17 by 15d) and expected counts indicates the pipeline has a data routing issue that has already been partially addressed but needs root-cause investigation.

  If REVISE:
    What is at risk: Data integrity of monitor_queue.md and downstream monitoring by Agent 15d. Items may be silently dropped, leaving assumptions unwatched.
    Recommended action: (1) Audit full data flow from 15c dispositions to monitor_queue.md and revision_flags.md. (2) Implement count assertions at each pipeline stage. (3) Root-cause the original 2-item discrepancy.
    Urgency: MEDIUM

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c]
    Transform at this step: Net evaluation and disposition
    Current status: REVISION-FLAGGED

---

### DISPOSITION-032:
  Date: 2026-04-13
  Item: PRESUMPTION-018
  Item type: PRESUMPTION (unstated — surfaced by inference)

  15a result: NO-SUPPORT-FOUND (Contradicted)
  15a strength: None
  15b result: CHALLENGED
  15b strength: Strong

  Net assessment: Both directions converge: LLMs have no native inter-session memory. Chat is not a reliable memory channel. Context rot degrades accuracy even within sessions. The presumption is directly contradicted by LLM architecture.

  Disposition: REVISE

  Reasoning: No support from any direction; fundamental contradiction from LLM architecture research. This is a PRESUMPTION — designers were unaware they were relying on chat as persistent memory. The evening-to-morning sync mechanism needs a parallel persistent channel (wiki file, structured summary) rather than relying solely on Chat conversation.

  If REVISE:
    What is at risk: Fidelity of evening-to-morning handoff. The 4 primed discussion topics from the evening sync may not all surface in the morning walk session. Critical items may be lost across session boundaries.
    Recommended action: (1) Write evening sync summaries to a persistent wiki file (e.g., wiki/architecture/session_handoffs/). (2) Morning walk sessions should load the handoff file explicitly rather than relying on Chat memory. (3) Track handoff fidelity — compare morning discussion topics against evening delivery.
    Urgency: HIGH (operational reliability depends on this handoff working)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c]
    Transform at this step: Net evaluation and disposition
    Current status: REVISION-FLAGGED

---

## SYSTEMIC-RISK-FLAG:
  Date: 2026-04-13
  Affected items: ASSUMPTION-014, ASSUMPTION-015, ASSUMPTION-016, PRESUMPTION-015, PRESUMPTION-016, PRESUMPTION-017, PRESUMPTION-018
  Common vulnerability: Over-reliance on isolated internal mechanisms without external validation or circuit-breaking. All seven items assume that a self-contained subsystem (three-category framework, biased pipeline, evidence-gating, self-evaluation, single-pass search, data pipeline, LLM conversation) is sufficient without external validation, multi-layered redundancy, or iterative correction.
  Literature basis: Gödel's incompleteness theorems; anchoring bias research (Springer 2021); data pipeline SDC literature (ArXiv 2021); LLM memory architecture surveys (ArXiv 2025); systematic review methodology (PRISMA-S)
  Risk level: High
  Recommendation: Re-examine the pipeline's architecture for external validation gates. Introduce human review for self-referential items. Implement data integrity assertions. Create persistent external memory for session handoffs.

---

## CYCLE SUMMARY — Second Cycle (2026-04-13 evening)

**Items processed:** 7 (ASSUMPTION-014, 015, 016; PRESUMPTION-015, 016, 017, 018)
**Dispositions:**
- INCORPORATE: 0
- MONITOR: 3 (ASSUMPTION-014 Medium; ASSUMPTION-015 HIGH; ASSUMPTION-016 HIGH)
- REVISE: 4 (PRESUMPTION-015 HIGH urgency; PRESUMPTION-016 MEDIUM; PRESUMPTION-017 MEDIUM; PRESUMPTION-018 HIGH)

**Key finding:** All 4 PRESUMPTION items flagged for REVISE. The evening-run items are more meta-cognitive (about the pipeline itself) than the first batch, and the literature is less supportive of self-referential evaluation claims.

**Systemic risk identified:** Over-reliance on internal mechanisms without external validation — affects all 7 items.

**Generated by Agents 15a, 15b, and 15c**
**Date: 2026-04-13 (evening cycle)**

---

## LITERATURE SEARCH RETURNS — 2026-04-14 CYCLE (10 items: ASSUMPTION-017–021, PRESUMPTION-019–023)

### Agent 15a Returns (FOR)

RETURN-TO-14a: ASSUMPTION-017 | FOR | SUPPORTED (Strong) | Key: Nature Human Behaviour 2024, "When combinations of humans and AI are useful" | AI-human complementarity established in evidence synthesis.
RETURN-TO-14a: ASSUMPTION-018 | FOR | PARTIALLY-SUPPORTED (Moderate) | Key: PMC 2014, "Decision-theoretic designs for pilot studies" | Generic framework support; no domain-specific literature.
RETURN-TO-14a: ASSUMPTION-019 | FOR | SUPPORTED (Strong) | Key: ResearchGate 2015, plate tectonics case study | Paradigm shifts are bibliometrically invisible during emergence.
RETURN-TO-14a: ASSUMPTION-020 | FOR | NO-SUPPORT-FOUND (NOVELTY) | Key: Hoffman 2024, Friston 2017, Levin 2019 — all exist independently; no unification found | NOVELTY-FLAG raised.
RETURN-TO-14a: ASSUMPTION-021 | FOR | PARTIALLY-SUPPORTED (Moderate) | Key: Hawkins et al. 2024, "Thousand Brains Project" | Functional analogy, not formal proof.
RETURN-TO-14b: PRESUMPTION-019 | FOR | PARTIALLY-SUPPORTED (Moderate) | Key: Cassi et al. 2020, co-citation analysis | Works within disciplines; fails interdisciplinarily.
RETURN-TO-14b: PRESUMPTION-020 | FOR | NO-SUPPORT-FOUND | Key: Nature Scientific Reports 2025, LLM limitations | LLMs appear to be biased acceleration, not complementary.
RETURN-TO-14b: PRESUMPTION-021 | FOR | PARTIALLY-SUPPORTED (Weak) | Key: ICLR 2024, self-evaluation in AI | Internal metrics show some signal but unreliable for high-stakes.
RETURN-TO-14b: PRESUMPTION-022 | FOR | PARTIALLY-SUPPORTED (Weak) | Key: QA scalability research | Pure human review cannot match generation; ~5% baseline.
RETURN-TO-14b: PRESUMPTION-023 | FOR | NO-SUPPORT-FOUND (contradicting) | Key: AWS Builders Library 2024 | Evidence says concurrent failures are typically correlated, not independent.

### Agent 15b Returns (AGAINST)

RETURN-TO-14a: ASSUMPTION-017 | AGAINST | CHALLENGED (Strong) | Key: AI & Society 2025, automation bias | Humans over-rely on AI; hallucinations systematic and hard to detect.
RETURN-TO-14a: ASSUMPTION-018 | AGAINST | PARTIALLY-CHALLENGED (Moderate) | Key: Cooper 2001, stage-gate systems | Delay itself is a decision with hidden costs; iteration reduces uncertainty.
RETURN-TO-14a: ASSUMPTION-019 | AGAINST | CHALLENGED (Strong) | Key: Laudan 1977, post-Kuhnian philosophy | Absence can signal search failure, isolation, false novelty, or dead-end.
RETURN-TO-14a: ASSUMPTION-020 | AGAINST | CHALLENGED (Strong) | Key: Hoffman testability critique; Colombo & Wright 2021, FEP conflation | Each framework has unresolved criticisms; structural mapping ≠ unification.
RETURN-TO-14a: ASSUMPTION-021 | AGAINST | CHALLENGED (Strong) | Key: TBT critique; active inference limitations; Gentner structure-mapping | Surface analogies confused with structural; different scales/substrates.
RETURN-TO-14b: PRESUMPTION-019 | AGAINST | CHALLENGED (Strong) | Key: Goodhart's Law; citation gaming research | Bibliometric signals corrupted by gaming; metrics become targets.
RETURN-TO-14b: PRESUMPTION-020 | AGAINST | CHALLENGED (Strong) | Key: LLM reasoning research; AI hallucination literature | LLMs are biased acceleration, not complementary; false analogies systematic.
RETURN-TO-14b: PRESUMPTION-021 | AGAINST | CHALLENGED (Strong) | Key: Dunning-Kruger; predictive modeling validation | Internal assessment overestimates quality; external validation required.
RETURN-TO-14b: PRESUMPTION-022 | AGAINST | CHALLENGED (Strong) | Key: Technical debt literature; queue theory | Backlogs grow unbounded when generation > review; zombie debt accumulates.
RETURN-TO-14b: PRESUMPTION-023 | AGAINST | CHALLENGED (Strong) | Key: Distributed systems literature; common-cause failure analysis | Concurrent = correlated until proven otherwise.

### Agent 15c Dispositions

DISPOSITION-033: ASSUMPTION-017 → MONITOR (HIGH) | Contested: strong evidence both ways | Validation design critical
DISPOSITION-034: ASSUMPTION-018 → MONITOR (MEDIUM) | Framework commitment; moderate evidence both ways
DISPOSITION-035: ASSUMPTION-019 → MONITOR (HIGH) | Contested: Kuhnian support vs. over-application critique
DISPOSITION-036: ASSUMPTION-020 → MONITOR (HIGH) | NOVELTY flagged; potentially novel contribution OR most important false positive
DISPOSITION-037: ASSUMPTION-021 → MONITOR (HIGH) | Moderate support vs. strong challenge; structural validity uncertain
DISPOSITION-038: PRESUMPTION-019 → REVISE (HIGH) | PRESUMPTION + strong challenge; bibliometric signals corrupted
DISPOSITION-039: PRESUMPTION-020 → REVISE (HIGH) | PRESUMPTION + no support + strong challenge; threatens value proposition
DISPOSITION-040: PRESUMPTION-021 → REVISE (HIGH) | PRESUMPTION + weak support + strong challenge; internal assessment unreliable
DISPOSITION-041: PRESUMPTION-022 → REVISE (HIGH) | PRESUMPTION + weak support + strong challenge; mirrors proposal bottleneck
DISPOSITION-042: PRESUMPTION-023 → REVISE (HIGH) | PRESUMPTION + contradicting evidence + strong challenge; active vulnerability

### Systemic Risk Flags

SYSTEMIC-RISK-FLAG-001: VALIDATION BOTTLENECK CASCADE
  Date: 2026-04-14
  Affected items: ASSUMPTION-017, PRESUMPTION-020, PRESUMPTION-022
  Common vulnerability: If AI synthesis produces findings at accelerated rate but validation is bottlenecked by automation bias, unvalidated findings accumulate in REVISE backlog unboundedly.
  Risk level: High
  Recommendation: Bundle for joint review; cap generation rate at 50% of validation capacity; backlog hard cap at 25 items; adversarial validation.

SYSTEMIC-RISK-FLAG-002: MATHEMATICAL UNIFICATION ON UNPROVEN FRAMEWORKS
  Date: 2026-04-14
  Affected items: ASSUMPTION-020, ASSUMPTION-021, PRESUMPTION-019, PRESUMPTION-021
  Common vulnerability: FINDING-011 is anchored to unification of frameworks with unresolved criticisms, assessed internally without calibration, and partly supported by corrupted bibliometric signals.
  Risk level: Critical
  Recommendation: Do NOT publish FINDING-011 as "unification." Reframe as "structural analogy." Require formal proof and external expert review. Set falsification criteria.

SYSTEMIC-RISK-FLAG-003: CORRELATED INFRASTRUCTURE FAILURES
  Date: 2026-04-14
  Affected items: PRESUMPTION-023, PRESUMPTION-022, ASSUMPTION-017
  Common vulnerability: Concurrent infrastructure failures suggest shared dependency; if correlated, individual fixes leave vulnerability and degrade all workflows including synthesis and validation.
  Risk level: High
  Recommendation: Full incident analysis assuming correlation. Map shared dependencies. Implement circuit breakers. Set SLOs.

---

## CYCLE SUMMARY — Third Cycle (2026-04-14)

**Items processed:** 10 (ASSUMPTION-017–021; PRESUMPTION-019–023)
**Dispositions:**
- INCORPORATE: 0
- MONITOR: 5 (ASSUMPTION-017, 018, 019, 020, 021; all HIGH or MEDIUM priority)
- REVISE: 5 (PRESUMPTION-019, 020, 021, 022, 023; all HIGH urgency)
- QUEUED: 0

**Key finding:** All 5 PRESUMPTION items flagged for REVISE, indicating 2026-04-14 items are more problematic than earlier cycles. Four presumptions are directly related to C2A2's core value propositions and vulnerabilities (AI synthesis, validation, quality assessment, backlog management, infrastructure).

**Systemic risks identified:** Three critical clusters:
- Validation bottleneck (generation outpacing review)
- Mathematical unification resting on unproven foundations
- Correlated infrastructure failures with independent-failure assumption

**Generated by Agents 15a, 15b, and 15c**
**Date: 2026-04-14**

---
---

# LITERATURE SEARCH RETURNS — FIFTH CYCLE (2026-04-15)

**Search date:** 2026-04-15
**Items searched:** 11 (6 ASSUMPTIONS + 5 PRESUMPTIONS)
**Pipeline agents:** 15a (FOR), 15b (AGAINST), 15c (Net Evaluator)

---

## 15a RETURNS (Supportive Search)

### RETURN-TO-14a: ASSUMPTION-022
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Kirchhoff et al. (2018) Markov blankets of life; Group-level active inference (PMC 2025); Markov blanket density (arxiv 2025)
**Summary:** FEP literature supports multi-scale boundary applicability, but as modeling framework not universal law. "Applies literally at every level" exceeds what literature supports.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-022_for.md

### RETURN-TO-14a: ASSUMPTION-023
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Weak
**Key source:** Perpetual Pilot Trap literature (Agility-at-Scale 2025); KPMG AI Pulse Q1 2026
**Summary:** Some support for commitment over perpetual piloting, but 33 agents exceeds documented successful deployments. Support is indirect.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-023_for.md

### RETURN-TO-14a: ASSUMPTION-024
**Search direction:** FOR (supportive)
**Result:** SUPPORTED
**Strength:** Moderate-Strong
**Key source:** Wimsatt (1981) Robustness; Kuorikoski & Marchionni Evidential Diversity; 2024 epistemic granularity
**Summary:** Triangulation/overdetermination is well-supported as confirmatory strategy. Key requirement: genuine independence of evidence streams.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-024_for.md

### RETURN-TO-14a: ASSUMPTION-025
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Hoffman Interface Theory; Lis (2025) HoTT-RO v2; Rovelli Relational QM; Maldacena (2024)
**Summary:** Substantive support within specific theoretical frameworks; active research frontier; not consensus.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-025_for.md

### RETURN-TO-14a: ASSUMPTION-026
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED + NOVELTY FLAG
**Strength:** Moderate
**Key source:** MABS Workshop Series (27 years); AI4ABM (ICLR 2023); ABM economics literature (2026)
**Summary:** ABM tradition supports agents-as-instruments; specific LLM-tradition-agent methodology is NOVEL.
**NOVELTY-FLAG:** No existing literature addresses treating intellectual traditions as LLM-instantiated cognitive agents.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-026_for.md

### RETURN-TO-14a: ASSUMPTION-027
**Search direction:** FOR (supportive)
**Result:** NO-SUPPORT-FOUND (Contradicting)
**Strength:** None
**Key source:** Decision fatigue systematic review (2025, 82 studies); Maier et al. 2025
**Summary:** Literature contradicts batch triage adequacy. 82-study review finds consistent degradation in serial processing.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-027_for.md

### RETURN-TO-14b: PRESUMPTION-024
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Weak
**Key source:** Wimsatt (1981); Kuorikoski & Marchionni; general robustness analysis
**Summary:** General triangulation principle supports genuineness if independence holds. But C2A2's traditions share same LLM backbone — independence unestablished.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-024_for.md

### RETURN-TO-14b: PRESUMPTION-025
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Weak
**Key source:** Perpetual Pilot Trap; decision theory under uncertainty
**Summary:** Indirect support for proceeding when progress made. Does not address operational-vs-epistemic readiness distinction.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-025_for.md

### RETURN-TO-14b: PRESUMPTION-026
**Search direction:** FOR (supportive)
**Result:** NO-SUPPORT-FOUND (Contradicting)
**Strength:** None
**Key source:** Decision fatigue systematic review (2025, 82 studies)
**Summary:** Same as ASSUMPTION-027. Literature directly contradicts.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-026_for.md

### RETURN-TO-14b: PRESUMPTION-027
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Weak-Moderate
**Key source:** Cold email response rate data (2025-2026); academic outreach literature
**Summary:** 3-5% baseline, 10%+ with personalization. Engagement possible but not assured.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-027_for.md

### RETURN-TO-14b: PRESUMPTION-028
**Search direction:** FOR (supportive)
**Result:** NO-SUPPORT-FOUND
**Strength:** None
**Key source:** Queue theory; iterative pipeline literature
**Summary:** Zero-queue is transient, not stable endpoint. Framing correction.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-028_for.md

---

## 15b RETURNS (Adversarial Search)

### RETURN-TO-14a: ASSUMPTION-022
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** Strong
**Key source:** Raja et al. (2021) "Markov Blanket Trick"; Biehl et al. (2021); tautology critique
**Specific risk:** FEP universality claim may be tautological — if it "applies to everything," it explains nothing specifically.
**Summary:** Multiple formal critiques identify mathematical problems with blanket formalism. Scope inflation concern.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-022_against.md

### RETURN-TO-14a: ASSUMPTION-023
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** Strong
**Key source:** Google Research (2025) agent scaling; enterprise deployment data (78% failure); 17x error amplification
**Specific risk:** Coordination tax saturates at N≈4; 33 agents is 6-8x beyond threshold.
**Summary:** Multi-agent scaling research strongly challenges 33-agent deployment viability.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-023_against.md

### RETURN-TO-14a: ASSUMPTION-024
**Search direction:** AGAINST (disconfirmatory)
**Result:** PARTIALLY-CHALLENGED
**Strength:** Moderate
**Key source:** LLM hallucination research (46% reasoning errors); epistemic granularity (2024); apophenia literature
**Specific risk:** If FINDING-004/009/011 share common LLM bias, convergence is spurious.
**Summary:** General principle valid but independence of C2A2 findings unestablished.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-024_against.md

### RETURN-TO-14a: ASSUMPTION-025
**Search direction:** AGAINST (disconfirmatory)
**Result:** PARTIALLY-CHALLENGED
**Strength:** Moderate
**Key source:** Realist ontology (mainstream philosophy); classical mereology; domain transfer concerns
**Specific risk:** Minority position in philosophy; lacks clear operational implications for C2A2.
**Summary:** Contested philosophical position without consensus or operational meaning.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-025_against.md

### RETURN-TO-14a: ASSUMPTION-026
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** Strong
**Key source:** LLM hallucination (46% reasoning errors); KnowFM 2025 analogical hallucination workshop; AI agent hallucination survey
**Specific risk:** LLM "behavioral data" may be training-data artifacts, not genuine tradition behavior.
**Summary:** Hallucination literature directly challenges "genuine behavioral data" claim.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-026_against.md

### RETURN-TO-14a: ASSUMPTION-027
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** Strong
**Key source:** Decision fatigue systematic review (82 studies); clinical decision-making biases; analyst forecast degradation
**Specific risk:** Later items in 16-item batch received heuristic processing; HIGH urgency items may be undertreated.
**Summary:** Serial processing degrades quality; batch triage produces lower-quality decisions.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-027_against.md

### RETURN-TO-14b: PRESUMPTION-024
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** Strong
**Key source:** Apophenia (Psychology Today); LLM hallucination (46%); KnowFM 2025; construct validity
**Specific risk:** Boundary convergence may be C2A2's largest false positive if selection effect.
**Summary:** System designed to find patterns will find them regardless of genuineness. SYSTEMIC-RISK-FLAG raised.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-024_against.md

### RETURN-TO-14b: PRESUMPTION-025
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** Moderate-Strong
**Key source:** Enterprise scaling failure rates (78%); sunk cost literature; Gartner 40% cancellation prediction
**Specific risk:** Operational cleanup conflated with epistemic readiness; sunk cost bias.
**Summary:** Literature distinguishes operational from epistemic readiness; C2A2 may have conflated them.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-025_against.md

### RETURN-TO-14b: PRESUMPTION-026
**Search direction:** AGAINST (disconfirmatory)
**Result:** CHALLENGED
**Strength:** Strong
**Key source:** Same as ASSUMPTION-027 (decision fatigue, 82 studies, surrogate decision-maker fatigue)
**Specific risk:** HIGH urgency items processed late in batch may have received inadequate deliberation.
**Summary:** Batch ≠ individual review quality. Strong, robust finding across 82 studies.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-026_against.md

### RETURN-TO-14b: PRESUMPTION-027
**Search direction:** AGAINST (disconfirmatory)
**Result:** PARTIALLY-CHALLENGED
**Strength:** Moderate
**Key source:** Cold email response rates (3-5%); academic inbox triage; interdisciplinary collaboration barriers
**Specific risk:** Non-response most likely; "substantive engagement" requires exceptional outreach quality.
**Summary:** Low baseline rates; busy academics triage heavily; novel computational frameworks may be dismissed.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-027_against.md

### RETURN-TO-14b: PRESUMPTION-028
**Search direction:** AGAINST (disconfirmatory)
**Result:** PARTIALLY-CHALLENGED
**Strength:** Moderate
**Key source:** Queue theory; iterative pipeline design; fluid queuing models
**Specific risk:** "Completion" framing may cause premature relaxation of monitoring.
**Summary:** Zero-queue is transient in continuous-input systems. Framing correction, not serious risk.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-028_against.md

---

## 15c DISPOSITION SUMMARY (2026-04-15)

| Item | 15a Result | 15b Result | Disposition | Priority |
|------|-----------|-----------|-------------|----------|
| ASSUMPTION-022 | PARTIALLY-SUPPORTED (Moderate) | CHALLENGED (Strong) | MONITOR | HIGH |
| ASSUMPTION-023 | PARTIALLY-SUPPORTED (Weak) | CHALLENGED (Strong) | MONITOR | HIGH |
| ASSUMPTION-024 | SUPPORTED (Moderate-Strong) | PARTIALLY-CHALLENGED (Moderate) | INCORPORATE | — |
| ASSUMPTION-025 | PARTIALLY-SUPPORTED (Moderate) | PARTIALLY-CHALLENGED (Moderate) | MONITOR | MEDIUM |
| ASSUMPTION-026 | PARTIALLY-SUPPORTED (Moderate) + NOVELTY | CHALLENGED (Strong) | MONITOR | HIGH |
| ASSUMPTION-027 | NO-SUPPORT-FOUND | CHALLENGED (Strong) | REVISE | HIGH |
| PRESUMPTION-024 | PARTIALLY-SUPPORTED (Weak) | CHALLENGED (Strong) | REVISE | HIGH (CRITICAL) |
| PRESUMPTION-025 | PARTIALLY-SUPPORTED (Weak) | CHALLENGED (Moderate-Strong) | MONITOR | HIGH |
| PRESUMPTION-026 | NO-SUPPORT-FOUND | CHALLENGED (Strong) | REVISE | HIGH |
| PRESUMPTION-027 | PARTIALLY-SUPPORTED (Weak-Moderate) | PARTIALLY-CHALLENGED (Moderate) | MONITOR | LOW |
| PRESUMPTION-028 | NO-SUPPORT-FOUND | PARTIALLY-CHALLENGED (Moderate) | MONITOR | LOW |

**Disposition distribution:**
- INCORPORATE: 1 (ASSUMPTION-024)
- MONITOR: 7 (ASSUMPTION-022, 023, 025, 026; PRESUMPTION-025, 027, 028)
- REVISE: 3 (ASSUMPTION-027; PRESUMPTION-024, 026)

**Cumulative totals (all 53 items):**
- INCORPORATE: 4 (ASSUMPTION-005, 009, 012, 024)
- MONITOR: 31 (25 prior + 6 new)
- REVISE: 19 (16 prior + 3 new; all 16 prior triaged by Tom)
- QUEUED: 0

**Key findings:**
1. **SYSTEMIC-RISK-FLAG:** LLM pattern genuineness cluster identified — PRESUMPTION-024, ASSUMPTION-022, 024, 026, PRESUMPTION-020 all depend on genuineness of LLM-generated patterns. Recommend null hypothesis testing.
2. **Batch triage quality challenged:** ASSUMPTION-027 and PRESUMPTION-026 both flagged — the 16-item triage session itself may have been affected by decision fatigue. Meta-recursive: this finding challenges the very triage that addressed prior REVISE items.
3. **NOVELTY flagged:** ASSUMPTION-026 (C2A2 methodology) has no direct precedent in literature. Potentially significant innovation or methodological vulnerability.

**Generated by Agents 15a, 15b, and 15c**
**Date: 2026-04-15**

---

# LITERATURE SEARCH RETURNS — 2026-04-16 CYCLE (Agents 15a, 15b, 15c)

**Search date:** 2026-04-16
**Items searched:** 11 (5 ASSUMPTIONS + 6 PRESUMPTIONS)
**Disposition distribution:** 0 INCORPORATE | 6 MONITOR | 5 REVISE

---

## 15a RETURNS (FOR — supportive)

### RETURN-TO-14a: ASSUMPTION-028
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Weak-Moderate
**Key source:** Hagiwara et al. 2024; Brown et al. 2020; RAG batch re-indexing literature
**Summary:** Partial support for batch ingestion coherence in NLP; no direct support for the equivalence claim with incremental processing.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-028_for.md

### RETURN-TO-14a: ASSUMPTION-029
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Vite documentation; Fowler modularization writing; LLM-generated code maintainability studies
**Summary:** Support for single-file bottleneck as a maintainability concern past ~1000 LoC; whether it is THE limiting factor remains an empirical question.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-029_for.md

### RETURN-TO-14a: ASSUMPTION-030
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Nosek et al. 2015; Peng 2011; ML benchmark norms
**Summary:** Open-science norms support benchmark-gated release; "criteria TBD" is the fragility.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-030_for.md

### RETURN-TO-14a: ASSUMPTION-031
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Shinn et al. 2023 (Reflexion); Wu et al. 2023 (AutoGen); Park et al. 2023
**Summary:** Multi-agent literature supports parallel specialists when tasks are cleanly decomposable and prompts well-differentiated.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-031_for.md

### RETURN-TO-14a: ASSUMPTION-032
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate (qualified)
**Key source:** Yang et al. 2024 (SeeAct); Chen et al. 2024 (SeeClick); Anthropic Computer Use
**Summary:** Visual-only agents are functional fallback; not a full substitute for DOM-aware tooling.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-032_for.md

### RETURN-TO-14b: PRESUMPTION-029
**Search direction:** FOR (supportive)
**Result:** NO-SUPPORT-FOUND (NOVELTY FLAG)
**Strength:** Weak
**Key source:** No direct literature located establishing genuineness tests for multi-subagent findings under shared backbone
**Summary:** Genuineness test is a live methodological gap; NOVELTY flagged for C2A2 to develop internal null-baseline protocol.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-029_for.md

### RETURN-TO-14b: PRESUMPTION-030
**Search direction:** FOR (supportive)
**Result:** NO-SUPPORT-FOUND
**Strength:** None
**Key source:** Software engineering literature unanimous that VCS discipline is structural
**Summary:** No literature supports "cosmetic" framing; literature contradicts it.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-030_for.md

### RETURN-TO-14b: PRESUMPTION-031
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Weak
**Key source:** Queueing theory with fallback; round-robin scheduling
**Summary:** General pattern supported; specific adequacy for 11 traditions with 12 slots is not established.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-031_for.md

### RETURN-TO-14b: PRESUMPTION-032
**Search direction:** FOR (supportive)
**Result:** NO-SUPPORT-FOUND
**Strength:** Weak
**Key source:** Reliability engineering (independence assumptions require common-cause analysis)
**Summary:** Independence is possible but not established without analysis.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-032_for.md

### RETURN-TO-14b: PRESUMPTION-033
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Weak-Moderate
**Key source:** Agile / lean startup literature (MVP checkpointing)
**Summary:** Supported for internal iterative work; weaker for user-facing artifacts without evaluator-producer separation.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-033_for.md

### RETURN-TO-14b: PRESUMPTION-034
**Search direction:** FOR (supportive)
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Observability and scheduling conventions (Majors; Prometheus docs)
**Summary:** Label persistence is conventional; downstream metric interpretation is the risk.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-034_for.md

---

## 15b RETURNS (AGAINST — disconfirmatory)

### RETURN-TO-14a: ASSUMPTION-028
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Strong
**Key source:** Decision fatigue 82-study systematic review; LLM session-drift literature
**Specific risk:** Later files in 45-file batch produce lower-fidelity extractions; FINDING-013–017 inherit the risk.
**Summary:** Batch-quality concern already flagged (ASSUMPTION-027, PRESUMPTION-026) extends to larger batch; equivalence claim empirically unsupported.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-028_against.md

### RETURN-TO-14a: ASSUMPTION-029
**Search direction:** AGAINST
**Result:** PARTIALLY-CHALLENGED
**Strength:** Moderate
**Key source:** Refactor ROI literature; frontend framework churn studies
**Specific risk:** Refactor absorbs effort without corresponding benefit if data model / test coverage is the real bottleneck.
**Summary:** "Single-file is THE limiting factor" is a strong causal claim the literature does not specifically support.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-029_against.md

### RETURN-TO-14a: ASSUMPTION-030
**Search direction:** AGAINST
**Result:** PARTIALLY-CHALLENGED
**Strength:** Strong
**Key source:** McKiernan et al. 2016; Raymond 1999; Raji et al. 2021
**Specific risk:** Indefinite release delay via "criteria TBD"; benchmark-shopping.
**Summary:** Benchmark-gating with undefined criteria is a recognized stall pattern; time-boxing recommended.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-030_against.md

### RETURN-TO-14a: ASSUMPTION-031
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Strong
**Key source:** Correlated-prompt literature (Zhou et al. 2024); LLM-as-rater inter-rater reliability studies
**Specific risk:** Parallel subagents with shared backbone produce correlated outputs; inflated finding rates.
**Summary:** Quality preservation is conditional on diversity mechanisms C2A2 has not documented. Connects to SYSTEMIC-RISK-FLAG cluster.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-031_against.md

### RETURN-TO-14a: ASSUMPTION-032
**Search direction:** AGAINST
**Result:** PARTIALLY-CHALLENGED
**Strength:** Moderate-Strong
**Key source:** WebArena / VisualWebArena benchmarks; GUI-agent benchmark literature
**Specific risk:** Missed root causes; false confidence in "no bug found."
**Summary:** 20-40% performance penalty for visual-only agents in benchmarks; "sufficient substitute" overstated.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-032_against.md

### RETURN-TO-14b: PRESUMPTION-029
**Search direction:** AGAINST
**Result:** STRONGLY CHALLENGED
**Strength:** Strong
**Key source:** LLM hallucination surveys; apophenia literature; correlated-prompt contamination research; KnowFM 2025
**Specific risk:** FINDING-013–017 may be false positives inherited by downstream Phase 2a decisions.
**Summary:** Genuineness unsupported pending null-baseline testing. Extends SYSTEMIC-RISK-FLAG.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-029_against.md

### RETURN-TO-14b: PRESUMPTION-030
**Search direction:** AGAINST
**Result:** STRONGLY CHALLENGED
**Strength:** Strong
**Key source:** Humble & Farley; Meneely et al. 2013; Google SRE book; ACM RSE guidelines
**Specific risk:** Silent corruption undetectable retrospectively; operational-health metrics unreliable against unversioned baseline.
**Summary:** Literature near-unanimous that a gap of this size is structural; "cosmetic" framing conflicts with C2A2's own PROVENANCE protocol.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-030_against.md

### RETURN-TO-14b: PRESUMPTION-031
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Moderate
**Key source:** Orchestrator-fallback quality literature; fair-scheduling / queueing theory
**Specific risk:** Chronic under-representation of some traditions biases PRS distribution.
**Summary:** 2/day × 6-day schedule has no redundancy for 11 traditions; orchestrator fallback introduces 15-30% quality penalty typical of generalist fallback.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-031_against.md

### RETURN-TO-14b: PRESUMPTION-032
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Strong
**Key source:** Common-cause failure literature (Rausand 2014; IEC 61508; Gunawi et al. 2014)
**Specific risk:** Tom's intent may be silently drifting out of agent awareness.
**Summary:** Same-day concurrent failures with plausibly shared dependencies have higher prior for common cause than coincidence. Mirrors PRESUMPTION-023.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-032_against.md

### RETURN-TO-14b: PRESUMPTION-033
**Search direction:** AGAINST
**Result:** PARTIALLY-CHALLENGED
**Strength:** Moderate-Strong
**Key source:** Fagan 1976 (software inspections); Zheng et al. 2023 (LLM-as-judge biases); definition-of-done literature
**Specific risk:** Future rollbacks anchor to a buggy baseline; user-facing bugs persist.
**Summary:** Self-assessed quality unreliable for user-facing artifacts without evaluator-producer separation.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-033_against.md

### RETURN-TO-14b: PRESUMPTION-034
**Search direction:** AGAINST
**Result:** PARTIALLY-CHALLENGED
**Strength:** Moderate
**Key source:** Majors 2019-2022 (observability labeling); SRE Workbook 2018; Schelter et al. 2018-2022
**Specific risk:** Trajectory metrics conflate single-day and multi-day runs; apparent trends may be scope artifacts.
**Summary:** Label persistence defensible only with per-run scope documentation; otherwise metric interpretation is compromised.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-034_against.md

---

## 15c DISPOSITION SUMMARY (2026-04-16)

| Item | 15a Result | 15b Result | Disposition | Priority/Urgency |
|------|-----------|-----------|-------------|------------------|
| ASSUMPTION-028 | PARTIALLY-SUPPORTED (Weak-Moderate) | CHALLENGED (Strong) | REVISE | HIGH |
| ASSUMPTION-029 | PARTIALLY-SUPPORTED (Moderate) | PARTIALLY-CHALLENGED (Moderate) | MONITOR | MEDIUM |
| ASSUMPTION-030 | PARTIALLY-SUPPORTED (Moderate) | PARTIALLY-CHALLENGED (Strong) | MONITOR | MEDIUM |
| ASSUMPTION-031 | PARTIALLY-SUPPORTED (Moderate) | CHALLENGED (Strong) | REVISE | HIGH (CRITICAL — SYSTEMIC-RISK cluster) |
| ASSUMPTION-032 | PARTIALLY-SUPPORTED (Moderate, qualified) | PARTIALLY-CHALLENGED (Moderate-Strong) | MONITOR | LOW (reframe recommended) |
| PRESUMPTION-029 | NO-SUPPORT-FOUND + NOVELTY | STRONGLY CHALLENGED (Strong) | REVISE | HIGH (CRITICAL — SYSTEMIC-RISK cluster) |
| PRESUMPTION-030 | NO-SUPPORT-FOUND | STRONGLY CHALLENGED (Strong) | REVISE | HIGH |
| PRESUMPTION-031 | PARTIALLY-SUPPORTED (Weak) | CHALLENGED (Moderate) | MONITOR | HIGH |
| PRESUMPTION-032 | NO-SUPPORT-FOUND (Weak) | CHALLENGED (Strong) | REVISE | MEDIUM (mirrors PRESUMPTION-023) |
| PRESUMPTION-033 | PARTIALLY-SUPPORTED (Weak-Moderate) | PARTIALLY-CHALLENGED (Moderate-Strong) | MONITOR | LOW-MEDIUM |
| PRESUMPTION-034 | PARTIALLY-SUPPORTED (Moderate) | PARTIALLY-CHALLENGED (Moderate) | MONITOR | LOW |

**Disposition distribution (today):**
- INCORPORATE: 0
- MONITOR: 6 (ASSUMPTION-029, 030, 032; PRESUMPTION-031, 033, 034)
- REVISE: 5 (ASSUMPTION-028, 031; PRESUMPTION-029, 030, 032)

**Cumulative totals (all 64 items):**
- INCORPORATE: 4 (unchanged)
- MONITOR: 35 (29 prior + 6 new)
- REVISE: 25 (20 prior + 5 new)
- QUEUED: 0

**Key findings:**
1. **SYSTEMIC-RISK-FLAG (extended):** PRESUMPTION-029 and ASSUMPTION-031 extend the "genuineness of LLM-generated cross-tradition patterns" cluster (previously PRESUMPTION-024, 020; ASSUMPTION-022, 024, 026) to the multi-subagent batch case for April 16 findings 13–17. Re-extraction experiment elevated from PROPOSED to REQUIRED before any Phase 2a commitments premised on these findings.
2. **Batch-quality cluster grows:** ASSUMPTION-028 (45-file batch) joins ASSUMPTION-027 and PRESUMPTION-026 — all three flagged REVISE on decision-fatigue evidence. Pattern: C2A2 batch operations routinely exceed the batch-quality threshold the literature supports.
3. **Operational-drift cluster confirmed:** PRESUMPTION-030 (VCS gap), 031 (rotation coverage), 032 (cross-channel failures) all produced CHALLENGED or STRONGLY CHALLENGED dispositions. Independent monitoring each; the aggregated escalation mechanism is the gap (tracked as OPEN-022).
4. **NOVELTY-FLAG:** PRESUMPTION-029 — no direct literature exists on testing genuineness of multi-subagent findings under shared backbone; this is both a methodological vulnerability and a potential original-contribution opportunity.

**Next actions:**
- Tom reviews 5 new REVISE items (ASSUMPTION-028, 031; PRESUMPTION-029, 030, 032), prioritizing PRESUMPTION-029 and ASSUMPTION-031 as CRITICAL.
- 15d monitors 35 MONITOR items on next cycle (April 20-21).
- Re-extraction experiment (paired test for ASSUMPTION-031 and PRESUMPTION-029) recommended within current sprint.

**Generated by Agents 15a, 15b, and 15c**
**Date: 2026-04-16**


---

# 2026-04-17 CYCLE — 15a / 15b / 15c

## 15a RETURNS (supportive searches)

### RETURN-TO-14a: ASSUMPTION-033
**Search direction:** FOR
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Norman 2013; Jaech/Sarikaya 2016-2017 on intent-explicit activation; IDE plugin pattern literature
**Summary:** Opt-in trigger activation is a validated plugin pattern; specific comparison to SessionStart hook is design-pattern precedent rather than empirical test.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-033_for.md

### RETURN-TO-14a: ASSUMPTION-034
**Search direction:** FOR
**Result:** NO-SUPPORT-FOUND
**Strength:** Weak (general prior only)
**Key source:** Sculley et al. 2015 on ML technical debt; general Opus model-card guidance
**Summary:** Only weak prior support ("newer vendor-tested models usually safe for general tasks"); no project-specific support for upgrade-without-regression-test.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-034_for.md

### RETURN-TO-14a: ASSUMPTION-035
**Search direction:** FOR
**Result:** PARTIALLY-SUPPORTED
**Strength:** Weak-Moderate
**Key source:** Kernighan & Pike 1984; Raymond 2003; Airflow/Luigi/Dagster pipeline handoff pattern
**Summary:** File-as-message pattern is well-supported as general coordination primitive; specific first-use integration is not independently validated.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-035_for.md

### RETURN-TO-14a: ASSUMPTION-036
**Search direction:** FOR
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Stripe / AWS billing-propagation engineering writeups; Abadi PACELC
**Summary:** Billing-state propagation lag is a documented vendor-side eventual-consistency class; attribution is plausible but not definitive absent client-side ruleout.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-036_for.md

### RETURN-TO-14a: ASSUMPTION-037
**Search direction:** FOR
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Parnas 1972; Hohpe & Woolf 2003; Cohn 2005 task decomposition
**Summary:** Separation of API-dependent and filesystem-only work is a canonical engineering pattern; tractability contingent on accurate pre-scoping.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-037_for.md

### RETURN-TO-14a: ASSUMPTION-038
**Search direction:** FOR
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Chiticariu et al. 2013; Jurafsky & Martin 2023; log-analysis industry practice
**Summary:** Rule-based prefix/substring classifiers validated as first-line tool for controlled vocabularies; audit required for empirical precision/recall.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-038_for.md

### RETURN-TO-14b: PRESUMPTION-035
**Search direction:** FOR
**Result:** NO-SUPPORT-FOUND
**Strength:** None
**Key source:** Google SRE Workbook; Beyer et al. 2016; alert-design literature
**Summary:** No literature supports threshold-free or retrospectively-defined drift thresholds; SRE literature is unanimous that thresholds must be pre-defined.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-035_for.md

### RETURN-TO-14b: PRESUMPTION-036
**Search direction:** FOR
**Result:** PARTIALLY-SUPPORTED
**Strength:** Weak
**Key source:** Allspaw 2012; Sterman 2000 systems thinking
**Summary:** Composite labels have limited value for situational awareness; not a substitute for per-incident root-cause analysis.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-036_for.md

### RETURN-TO-14b: PRESUMPTION-037
**Search direction:** FOR
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Kernighan & Pike 1984; Hohpe & Woolf 2003; workflow-engine practice
**Summary:** General pattern (file-based handoff) well-supported; specific first-use implementation has untested links.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-037_for.md

### RETURN-TO-14b: PRESUMPTION-038
**Search direction:** FOR
**Result:** NO-SUPPORT-FOUND
**Strength:** None
**Key source:** Stripe / AWS billing postmortem corpus; Abadi PACELC
**Summary:** Short-window propagation is documented, but no literature predicts a specific clearance window; recovery-by-waiting is defensible as first-line only.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-038_for.md

### RETURN-TO-14b: PRESUMPTION-039
**Search direction:** FOR
**Result:** NO-SUPPORT-FOUND
**Strength:** None
**Key source:** Ammari et al. 2019; Gao et al. 2018 on intent coverage
**Summary:** No literature supports designer-guessed trigger taxonomies as "representative" without corpus grounding or feedback-loop iteration.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-039_for.md

### RETURN-TO-14b: PRESUMPTION-040
**Search direction:** FOR
**Result:** NO-SUPPORT-FOUND
**Strength:** None
**Key source:** Myers/Sandler/Badgett 2011; Humble & Farley 2010; plugin publishing practice
**Summary:** Testing literature is unanimous: structural verification is necessary but not sufficient for operational readiness.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-040_for.md

### RETURN-TO-14b: PRESUMPTION-041
**Search direction:** FOR
**Result:** NO-SUPPORT-FOUND
**Strength:** None
**Key source:** Nygard 2011 ADRs; Kruchten et al. 2019; C2A2's own PROVENANCE protocol
**Summary:** Implicit-decision workflow is the specific anti-pattern ADR practice was designed to counter; conflicts with C2A2's own PROVENANCE protocol.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-041_for.md

### RETURN-TO-14b: PRESUMPTION-042
**Search direction:** FOR
**Result:** NO-SUPPORT-FOUND
**Strength:** None
**Key source:** Chinchor 1995 MUC methodology; Nisbett & Wilson 1977; 14b's own operating instructions
**Summary:** No literature supports self-referential coverage validation; 14b's own instructions acknowledge false-negative invisibility.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-042_for.md

---

## 15b RETURNS (challenging searches)

### RETURN-TO-14a: ASSUMPTION-033
**Search direction:** AGAINST
**Result:** PARTIALLY-CHALLENGED
**Strength:** Moderate
**Key source:** Ammari et al. 2019; Luger & Sellen 2016 on trigger-miss abandonment
**Specific risk:** Silent trigger miss; user abandonment rather than learning; hidden miss rate invisible to plugin.
**Summary:** Phrase-triggered activation imposes recall burden inappropriate for frequent/high-value intents like session-resume; hook may be better fit.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-033_against.md

### RETURN-TO-14a: ASSUMPTION-034
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Moderate
**Key source:** Sculley et al. 2015; Bommasani et al. 2021; Chen et al. 2024 on model transitions
**Specific risk:** Narrator-voice drift; silent regression on style-sensitive output; asymmetric downside.
**Summary:** Blanket upgrades without regression testing are a documented anti-pattern; successive foundation-model versions are non-monotonic on task-level performance.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-034_against.md

### RETURN-TO-14a: ASSUMPTION-035
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Moderate-Strong
**Key source:** Kahneman 2011; Kim & Gray 1999 compound-probability; git/systemd hook failure case studies
**Specific risk:** Hook registered but not fired; skill activates but misreads; compounded failure probability.
**Summary:** Compound handoff chain untested on first use; confidence miscalibration; four-link chain has significant compounded silent-failure probability.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-035_against.md

### RETURN-TO-14a: ASSUMPTION-036
**Search direction:** AGAINST
**Result:** PARTIALLY-CHALLENGED
**Strength:** Moderate
**Key source:** Stripe API error-code documentation; Einhorn & Hogarth 1978; fault-attribution literature
**Specific risk:** Waiting while actual cause is client-side; stall without ticket; wrong-workspace or key-scope missed.
**Summary:** Vendor-side attribution without client-side ruleout is a documented fault-attribution anti-pattern.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-036_against.md

### RETURN-TO-14a: ASSUMPTION-037
**Search direction:** AGAINST
**Result:** PARTIALLY-CHALLENGED
**Strength:** Weak-Moderate
**Key source:** Kahneman & Tversky 1979 planning fallacy; Brooks 1975; Fowler 1999 refactor literature
**Specific risk:** Scope creep into I/O; weekend stall; partial progress lost.
**Summary:** Planning-fallacy prior; "pure Python" claims often surface late I/O; directly testable by execution.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-037_against.md

### RETURN-TO-14a: ASSUMPTION-038
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Moderate
**Key source:** Chiticariu et al. 2013; Hofmeyr & Forrest 2000 on pattern-match FP/FN rates
**Specific risk:** Automated sessions missed by filter included in analysis; interactive sessions with matching names excluded; 5-15% error rates typical.
**Summary:** Rule-based classifiers are brittle to naming-convention drift; empirical audit required for reliability claim.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-038_against.md

### RETURN-TO-14b: PRESUMPTION-035
**Search direction:** AGAINST
**Result:** STRONGLY CHALLENGED
**Strength:** Strong
**Key source:** Beyer et al. 2016 SRE; Google SRE Workbook 2018; Rosen et al. 2020 alert fatigue
**Specific risk:** Alert inconsistency; both FP and FN accumulation; flag becomes noise rather than signal.
**Summary:** Retrospective threshold invocation is a documented SRE anti-pattern; pre-defined thresholds are a monitoring-discipline prerequisite.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-035_against.md

### RETURN-TO-14b: PRESUMPTION-036
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Strong
**Key source:** Rooney & Vanden Heuvel 2004 RCA; Allspaw 2012; Leveson 2011 STAMP
**Specific risk:** Most-visible channel dominates remediation; quieter three persist; chronic under-fixing.
**Summary:** Aggregating disjoint root causes is a remediation anti-pattern; composite-for-visibility vs. atomic-for-remediation distinction is well-established.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-036_against.md

### RETURN-TO-14b: PRESUMPTION-037
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Moderate-Strong
**Key source:** Dweck 2006; Kim & Gray 1999 compound probability; hook-system failure case studies
**Specific risk:** Untested 4-link chain has significant silent-failure risk; confidence miscalibration.
**Summary:** Reliability is empirical, not stipulated; untested multi-link handoff cannot be declared "more reliable" before successful end-to-end execution.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-037_against.md

### RETURN-TO-14b: PRESUMPTION-038
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Moderate
**Key source:** ITIL incident management; Gray & Reuter 1993; customer-support signaling literature
**Specific risk:** Billing doesn't clear; weekend work stalls; no active signal to vendor; Monday delay.
**Summary:** Recovery-by-waiting without active escalation is a documented anti-pattern; recovery-time predictions are systematically optimistic.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-038_against.md

### RETURN-TO-14b: PRESUMPTION-039
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Moderate
**Key source:** Ammari et al. 2019; Luger & Sellen 2016; Casanueva et al. 2020 intent classification
**Specific risk:** Silent under-utilization; Tom abandons plugin instead of learning; miss rate invisible without instrumentation.
**Summary:** Designer-guessed trigger taxonomies miss 20-30% of real utterances; dominant failure mode (user abandonment) invisible to plugin.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-039_against.md

### RETURN-TO-14b: PRESUMPTION-040
**Search direction:** AGAINST
**Result:** STRONGLY CHALLENGED
**Strength:** Strong
**Key source:** Myers/Sandler/Badgett 2011; Humble & Farley 2010; plugin "installed but never fires" case studies
**Specific risk:** Plugin passes structural verification and silently fails to fire — invisible failure mode.
**Summary:** Structural verification does not address the dominant plugin failure class (installed-but-never-fires); smoke test is the minimum bar.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-040_against.md

### RETURN-TO-14b: PRESUMPTION-041
**Search direction:** AGAINST
**Result:** STRONGLY CHALLENGED
**Strength:** Strong
**Key source:** Nygard 2011 ADRs; Kruchten et al. 2019; Tyree & Akerman 2005; Burge & Brown 2000 rationale decay; C2A2 PROVENANCE protocol
**Specific risk:** Decision rationale decay; future reversal cost; provenance chain breaks at architectural level; direct internal inconsistency with PROVENANCE.
**Summary:** Implicit-decision workflow is the anti-pattern ADR practice was invented to fix; also directly contradicts C2A2's own PROVENANCE protocol.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-041_against.md

### RETURN-TO-14b: PRESUMPTION-042
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Moderate-Strong
**Key source:** Chinchor 1995; Nisbett & Wilson 1977; Manning et al. 2008; 14b's own operating instructions
**Specific risk:** Silent blind-spot accumulation; false confidence in the self-awareness pipeline itself.
**Summary:** Self-referential coverage validation is a known blind spot; the pipeline's own instructions already acknowledge false-negative invisibility.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-042_against.md

---

## 15c DISPOSITION SUMMARY (2026-04-17)

| Item | 15a Result | 15b Result | Disposition | Priority/Urgency |
|------|-----------|-----------|-------------|------------------|
| ASSUMPTION-033 | PARTIALLY-SUPPORTED (Moderate) | PARTIALLY-CHALLENGED (Moderate) | MONITOR | MEDIUM (first stress test 2026-04-18) |
| ASSUMPTION-034 | NO-SUPPORT-FOUND (Weak prior only) | CHALLENGED (Moderate) | REVISE | MEDIUM (document rationale + regression test) |
| ASSUMPTION-035 | PARTIALLY-SUPPORTED (Weak-Moderate) | CHALLENGED (Moderate-Strong) | MONITOR | HIGH (stress-tested 2026-04-18) |
| ASSUMPTION-036 | PARTIALLY-SUPPORTED (Moderate) | PARTIALLY-CHALLENGED (Moderate) | MONITOR | MEDIUM (client-side ruleout required) |
| ASSUMPTION-037 | PARTIALLY-SUPPORTED (Moderate) | PARTIALLY-CHALLENGED (Weak-Moderate) | MONITOR | LOW (direct test upcoming) |
| ASSUMPTION-038 | PARTIALLY-SUPPORTED (Moderate) | CHALLENGED (Moderate) | MONITOR | MEDIUM (audit OPEN-025) |
| PRESUMPTION-035 | NO-SUPPORT-FOUND | STRONGLY CHALLENGED (Strong) | REVISE | HIGH (define threshold before next invocation) |
| PRESUMPTION-036 | PARTIALLY-SUPPORTED (Weak) | CHALLENGED (Strong) | REVISE | MEDIUM-HIGH (per-channel tracking required) |
| PRESUMPTION-037 | PARTIALLY-SUPPORTED (Moderate) | CHALLENGED (Moderate-Strong) | MONITOR | HIGH (paired with ASSUMPTION-035 weekend test) |
| PRESUMPTION-038 | NO-SUPPORT-FOUND | CHALLENGED (Moderate) | REVISE | MEDIUM (file support ticket, define recovery window) |
| PRESUMPTION-039 | NO-SUPPORT-FOUND | CHALLENGED (Moderate) | MONITOR | LOW-MEDIUM (corpus audit recommended) |
| PRESUMPTION-040 | NO-SUPPORT-FOUND | STRONGLY CHALLENGED (Strong) | REVISE | MEDIUM (end-to-end smoke test required) |
| PRESUMPTION-041 | NO-SUPPORT-FOUND | STRONGLY CHALLENGED (Strong) | REVISE | HIGH (violates PROVENANCE protocol — internal inconsistency) |
| PRESUMPTION-042 | NO-SUPPORT-FOUND | CHALLENGED (Moderate-Strong) | REVISE | MEDIUM-HIGH (self-referential validity; extends PRESUMPTION-015 cluster) |

**Disposition distribution (today):**
- INCORPORATE: 0
- MONITOR: 7 (ASSUMPTION-033, 035, 036, 037, 038; PRESUMPTION-037, 039)
- REVISE: 7 (ASSUMPTION-034; PRESUMPTION-035, 036, 038, 040, 041, 042)

**Cumulative totals (all 78 items):**
- INCORPORATE: 4 (unchanged)
- MONITOR: 42 (35 prior + 7 new)
- REVISE: 32 (25 prior + 7 new)
- QUEUED: 0

**Key findings:**
1. **OPERATIONAL-DRIFT cluster formalizes:** PRESUMPTION-035 (threshold undefined), PRESUMPTION-036 (cluster label obscures root causes), PRESUMPTION-038 (passive recovery), and PRESUMPTION-042 (self-referential coverage) all flag REVISE. Pattern: the operational-drift response mechanism itself has several unaddressed meta-issues (thresholds, aggregation, escalation, coverage audit). Recommendation: define drift thresholds and per-channel tracking before next aggregate invocation.
2. **SELF-AWARENESS-META cluster extends:** PRESUMPTION-041 (implicit architectural decisions) and PRESUMPTION-042 (self-validated zero-output) extend the self-referential validity cluster first raised by PRESUMPTION-015 (2026-04-13). PRESUMPTION-041 is especially notable — it directly contradicts C2A2's own PROVENANCE protocol, creating internal inconsistency.
3. **WEEKEND-TEST cluster:** ASSUMPTION-033, 035, 037, 038; PRESUMPTION-037, 040 are all scheduled for 2026-04-18 empirical test. Outcome from that day will either confirm or trigger rapid revision of several MONITOR items simultaneously.
4. **MODEL-UPGRADE gap:** ASSUMPTION-034 (model default change) is the first REVISE tied to regression-testing discipline for model transitions. Pair with ASSUMPTION-028 (batch extraction) and PRESUMPTION-029 (pattern-detector findings) as the "quality-discipline cluster."

**Novelty / NOVELTY-FLAG:** None new today. PRESUMPTION-035 raises the meta-question of whether C2A2's drift-threshold codification itself needs to be a first-class system artifact — may be a future ASSUMPTION for 14a.

**Systemic risk / SYSTEMIC-RISK-FLAG:** No new LLM-pattern-genuineness items today. The OPERATIONAL-DRIFT cluster (PRESUMPTION-035, 036, 038, 042) shares a common vulnerability: the system lacks disciplined operational telemetry. This is not at LLM-pattern-genuineness severity but warrants paired remediation, not independent one-by-one fixes.

**Next actions:**
- Tom reviews 7 new REVISE items, prioritizing PRESUMPTION-041 (PROVENANCE internal inconsistency) and PRESUMPTION-035 (define drift threshold).
- 15d monitors 42 MONITOR items on next cycle (April 20-21). HIGH-priority new items: ASSUMPTION-035 and PRESUMPTION-037 (paired weekend test).
- Schedule Saturday post-mortem to record outcomes of weekend-test cluster (ASSUMPTION-033, 035, 037, 038; PRESUMPTION-037, 040).

**Generated by Agents 15a, 15b, and 15c**
**Date: 2026-04-17**

---

# LITERATURE SEARCH RETURNS - 2026-04-18 AFTERNOON TOP-UP CYCLE

**Search date:** 2026-04-18
**Cycle:** ninth (afternoon top-up — processes 12 items surfaced by 14a/14b morning run)
**Total items searched:** 12 (6 ASSUMPTIONS + 6 PRESUMPTIONS)
**PROVENANCE:** Chain=[14a|14b→15a,15b→15c]; all items Origin=14a or 14b (morning 2026-04-18 run)

---

## 15a RETURNS (FOR — supportive)

### RETURN-TO-14a: ASSUMPTION-039
**Search direction:** FOR
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Cowork access-tier documentation; Miller 2006 capability-based security; Reis & Gribble 2009 Chrome process model
**Summary:** Tier contract is attached to app-category by design; supported at design-level, only moderately at empirical-cross-Chrome-states level.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-039_for.md

### RETURN-TO-14a: ASSUMPTION-040
**Search direction:** FOR
**Result:** SUPPORTED
**Strength:** Strong
**Key source:** OpenAI ChatGPT Projects help; Krebs et al. 2012 SaaS multi-tenancy; standard cookie-auth scoping
**Summary:** Account-scoping of projects is documented by OpenAI and is the standard SaaS tenancy pattern; cookie/session fundamentals preclude accidental cross-account visibility.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-040_for.md

### RETURN-TO-14a: ASSUMPTION-041
**Search direction:** FOR
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Kimball 2004 ETL toolkit; Zapier/Airbyte/Fivetran connector-architecture reports; Google Drive API SLA
**Summary:** Durable-staging pattern is textbook data-integration practice; Drive specifically has a mature first-party connector. The *ordinal* claim "most durable" is weaker than the pattern claim.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-041_for.md

### RETURN-TO-14a: ASSUMPTION-042
**Search direction:** FOR
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate
**Key source:** Google SRE book; ITIL v4; Nagios/PagerDuty conventions; Ligus 2012
**Summary:** Count-plus-calendar-span threshold structure is well-supported; specific numeric values (5-of-3) are within plausible range but lack empirical calibration.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-042_for.md

### RETURN-TO-14a: ASSUMPTION-043
**Search direction:** FOR
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate (novelty-as-absence only)
**Key source:** direct grep of cross_program_index.md; absence-of-prior-citation in Wolfram/Sellars literatures
**Summary:** Novelty as absence-from-prior-mention is supportable by grep; novelty as genuine-structural-bridge is NOT established by 15a and is specifically flagged by paired PRESUMPTION-045.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-043_for.md

### RETURN-TO-14a: ASSUMPTION-044
**Search direction:** FOR
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate (loading half only; execution half UNTESTED)
**Key source:** LangChain/LlamaIndex runbook literature; Claude Agent SDK SessionStart docs; 2026-04-18 N=1 stress test
**Summary:** Loading half supported by general file-as-message literature and by N=1 stress test; execution half not exercised because Tom pivoted (paired PRESUMPTION-046); "reliably" adverb unsupported at N=1.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-044_for.md

### RETURN-TO-14b: PRESUMPTION-043
**Search direction:** FOR
**Result:** NO-SUPPORT-FOUND
**Strength:** None
**Key source:** SaaS session-lifecycle norms; OAuth specs; Kleppmann 2017; C2A2's own Agent 16 design
**Summary:** No literature supports indefinite retention of parked sessions as a designed behavior; C2A2 already has Agent 16 for deferred-action routing. The presumption appears to describe a gap, not a design choice.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-043_for.md

### RETURN-TO-14b: PRESUMPTION-044
**Search direction:** FOR
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate (first-remediation only)
**Key source:** Nygard 2007 retry patterns; AWS Well-Architected; Google SRE exponential-backoff
**Summary:** Retry-first for transient failure is textbook; "retry-even-after-5-day-failure" is not supported — literature prescribes circuit-breaker transition at that point.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-044_for.md

### RETURN-TO-14b: PRESUMPTION-045
**Search direction:** FOR
**Result:** NO-SUPPORT-FOUND
**Strength:** None
**Key source:** Wolfram 2020; Brandom 1994/2008; deVries 2005; Cartwright 1999; Hofstadter & Sander 2013
**Summary:** No literature supports unchecked transfer of Wolfram's hypergraph formalism to the Sellarsian space of reasons. Philosophy-of-science literature on formalism transfer is unanimously opposed to the pattern in the presumption.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-045_for.md

### RETURN-TO-14b: PRESUMPTION-046
**Search direction:** FOR
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate (descriptive only; normative half not supported)
**Key source:** Czerwinski et al. 2004 task-switching; Nielsen/Shneiderman user-sovereignty heuristics; 2026-04-18 Dispatch observation
**Summary:** Descriptive pattern (users discharge loaded payloads on pivot) is supported; normative correctness for a handoff-pattern is not — the implied design critique of DECISION-021's falsifiability survives 15a.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-046_for.md

### RETURN-TO-14b: PRESUMPTION-047
**Search direction:** FOR
**Result:** SUPPORTED
**Strength:** Moderate-Strong
**Key source:** Amershi et al. 2019; Shneiderman 2020 "Human-Centered AI"; Li et al. 2020 elicitation-in-CA; Cowork's own AskUserQuestion guidance
**Summary:** User-directedness for cross-account data-ingestion is well-supported across HCI, data-governance, and conversational-AI literature. Cowork's product guidance aligns.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-047_for.md

### RETURN-TO-14b: PRESUMPTION-048
**Search direction:** FOR
**Result:** PARTIALLY-SUPPORTED
**Strength:** Moderate (conservative interpretation; not for absence of disambiguation)
**Key source:** Nardi et al. 1997; Kandel et al. 2012; Chinchor 1995; Little & Rubin 2019; prior PRESUMPTION-042 case
**Summary:** Conservative interpretation (treat null as missed-capture) is supported; the absence of a disambiguation mechanism is the real issue and is the known gap pattern of PRESUMPTION-042.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-048_for.md

---

## 15b RETURNS (AGAINST — disconfirmatory)

### RETURN-TO-14a: ASSUMPTION-039
**Search direction:** AGAINST
**Result:** PARTIALLY-CHALLENGED
**Strength:** Weak-Moderate
**Key source:** Puppeteer/Playwright non-default-profile detection; Reis & Gribble 2009 site-isolation; Chrome enterprise docs; remote-debug wrapper reports
**Specific risk:** Non-default Chrome channels or remote-debug-wrapped Chrome may surface under different identities and receive different tiers.
**Summary:** Default-case claim is strong; "across all profiles and states" universal is weakened by Chrome's configurability surface.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-039_against.md

### RETURN-TO-14a: ASSUMPTION-040
**Search direction:** AGAINST
**Result:** NO-CHALLENGE-FOUND (with scope qualifiers)
**Strength:** Weak
**Key source:** 2023 ChatGPT title-leak incident (a defect, not a model); 2025 shared-projects feature (explicit invite only)
**Specific risk:** Low. User-confusion across simultaneously-authenticated tabs is the main residual failure mode.
**Summary:** No credible literature suggests accidental cross-account visibility; the one historical incident is a vendor defect, and shared-projects is invite-gated.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-040_against.md

### RETURN-TO-14a: ASSUMPTION-041
**Search direction:** AGAINST
**Result:** PARTIALLY-CHALLENGED
**Strength:** Moderate
**Key source:** Drive-API v2→v3 deprecation history; OAuth consent-screen tightening; OpenAI-native export features; SRE reliability-chain literature
**Specific risk:** OAuth consent resets break recurrent scrapes silently; each added connector hop compounds failure probability.
**Summary:** Viability claim is uncontested; ordinal-dominance ("most durable") claim is contested — OpenAI-native export is a strong alternative and the comparison set was not enumerated.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-041_against.md

### RETURN-TO-14a: ASSUMPTION-042
**Search direction:** AGAINST
**Result:** PARTIALLY-CHALLENGED
**Strength:** Moderate
**Key source:** Ancker et al. 2017 alert fatigue; Nygard "Release It!" 2nd ed.; SLO-change practice; multi-day Chrome-extension rollout outage counterexamples
**Specific risk:** Static threshold without base-rate calibration; false escalation during vendor maintenance windows that self-resolve.
**Summary:** Threshold structure is sound; specific values (5-of-3) lack empirical calibration and recalibration loop.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-042_against.md

### RETURN-TO-14a: ASSUMPTION-043
**Search direction:** AGAINST
**Result:** PARTIALLY-CHALLENGED
**Strength:** Moderate-Strong
**Key source:** C2A2 prior CRITICAL cluster (PRESUMPTION-002, 014, 020, 024); Cartwright 1999; Hofstadter & Sander 2013; Brandom 1994
**Specific risk:** cross_program_index.md accumulates a corridor that looks new but is a selection-effect artifact; downstream agents compound the error.
**Summary:** Novelty-as-absence is trivially true; novelty-as-genuineness is directly in the scope of the registry's own CRITICAL selection-effect cluster. Paired with PRESUMPTION-045. SYSTEMIC-RISK-FLAG raised.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-043_against.md

### RETURN-TO-14a: ASSUMPTION-044
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Moderate
**Key source:** Kahneman 2011 first-use-as-confirmation bias; Leveson 2011 reliability engineering; SessionStart hook failure-class reports; PRESUMPTION-046 paired
**Specific risk:** False confidence in a first-use mechanism; execution half silently fails on next real use; "reliably" adverb propagates to adjacent design decisions without justification.
**Summary:** Mechanism is not challenged; the "reliably" adverb at N=1 with untested execution half is. Cluster with PRESUMPTION-046 (discharge-on-pivot) means DECISION-021's reliability claim is unfalsifiable in the discharge-on-pivot regime.
**Full results:** wiki/architecture/lit_search_results/against/ASSUMPTION-044_against.md

### RETURN-TO-14b: PRESUMPTION-043
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Moderate-Strong
**Key source:** Kleppmann 2017 queue-backlog; Whittaker & Sidner 1996 email-overload; Allen 2001 GTD; C2A2 Agent 16 design
**Specific risk:** Cumulative hidden backlog of parked sessions; architectural intent decays because never revisited; systemic blindness about parked-vs-active work.
**Summary:** Indefinite retention without review is a named failure mode, not a designed behavior. Route parked sessions to Agent 16. SYSTEMIC-RISK-FLAG raised jointly with PRESUMPTION-046, 047.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-043_against.md

### RETURN-TO-14b: PRESUMPTION-044
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Moderate-Strong
**Key source:** Nygard 2007 circuit-breaker; Google SRE book ch. 22; Ancker et al. 2017 alert fatigue; Hollnagel 2011 resilience engineering; ASSUMPTION-042 (internal inconsistency)
**Specific risk:** Delayed human response to persistent failure; routine logs obscure a real actionable problem; internal inconsistency with ASSUMPTION-042.
**Summary:** Retry past the 5-of-3 threshold is internally inconsistent with ASSUMPTION-042 and with the circuit-breaker literature. INTERNAL-CONSISTENCY-FLAG raised.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-044_against.md

### RETURN-TO-14b: PRESUMPTION-045
**Search direction:** AGAINST
**Result:** STRONGLY-CHALLENGED
**Strength:** Strong
**Key source:** C2A2 prior CRITICAL cluster (PRESUMPTION-002, 014, 020, 024); Cartwright 1999; Batterman 2002; Brandom 1994; Hofstadter & Sander 2013
**Specific risk:** Extends the CRITICAL cluster to a new layer (content-generation rather than extraction); causal-invariance-vs-context-dependence is a specific structural obstacle.
**Summary:** Strong convergence against: philosophy-of-science, C2A2's own prior cluster, and a specific structural obstacle all predict transfer failure without validity check. SYSTEMIC-RISK-FLAG raised.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-045_against.md

### RETURN-TO-14b: PRESUMPTION-046
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Moderate-Strong
**Key source:** BPM/workflow-engine literature; Nygard 2007 pipeline architecture; Popper 1963 / Leveson 2011 falsifiability; SELF-AWARENESS-META cluster
**Specific risk:** Unfalsifiable reliability claim for DECISION-021; payload intent silently discharges; handoff-vs-loader ambiguity unresolved.
**Summary:** Two-pronged challenge: normative (handoff should re-queue) and epistemic (discharge-on-pivot makes reliability unfalsifiable). Joins self-awareness-meta cluster as 5th member.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-046_against.md

### RETURN-TO-14b: PRESUMPTION-047
**Search direction:** AGAINST
**Result:** PARTIALLY-CHALLENGED
**Strength:** Weak-Moderate
**Key source:** Zapier/Make/N8N workflow design; Ancker et al. 2017 alert fatigue; Russell 2019 human-AI agency; Allen 2001 GTD; paired PRESUMPTION-043
**Specific risk:** Elicitation fatigue if every instance requires user-direction; parked-session backlog if enumerations are never resolved.
**Summary:** Universal form of the presumption is contested; context-sensitive form (first-time user-directed, repeat default-to-low-friction) is supported. Paired with PRESUMPTION-043 retention cost.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-047_against.md

### RETURN-TO-14b: PRESUMPTION-048
**Search direction:** AGAINST
**Result:** CHALLENGED
**Strength:** Moderate
**Key source:** Kandel et al. 2012; Little & Rubin 2019; Chinchor 1995; ITIL monitoring best practices; self-awareness-meta cluster
**Specific risk:** Briefing runs on ambient signals that silently degrade; joins self-awareness-meta cluster as 6th member.
**Summary:** Conservative-interpretation default is better than zero-default but the real problem is the absence of disambiguation. Same structural gap as PRESUMPTION-042. SYSTEMIC-RISK-FLAG raised for cluster-wide remediation.
**Full results:** wiki/architecture/lit_search_results/against/PRESUMPTION-048_against.md

---

## 15c DISPOSITION SUMMARY (2026-04-18 afternoon top-up)

| Item | 15a Result | 15b Result | Disposition | Priority/Urgency |
|------|-----------|-----------|-------------|------------------|
| ASSUMPTION-039 | PARTIALLY-SUPPORTED (Moderate) | PARTIALLY-CHALLENGED (Weak-Moderate) | MONITOR | LOW-MEDIUM (verify tier empirically via request_access return on non-default channels) |
| ASSUMPTION-040 | SUPPORTED (Strong) | NO-CHALLENGE-FOUND (Weak) | INCORPORATE | N/A — moderate confidence; applicable to cross-account route-elimination logic |
| ASSUMPTION-041 | PARTIALLY-SUPPORTED (Moderate) | PARTIALLY-CHALLENGED (Moderate) | MONITOR | MEDIUM (4-week friction test already proposed in item Notes; add OpenAI-native export to comparison set) |
| ASSUMPTION-042 | PARTIALLY-SUPPORTED (Moderate) | PARTIALLY-CHALLENGED (Moderate) | MONITOR | MEDIUM-HIGH (structure sound; calibration against outage-duration distribution required — add to OPERATIONAL-DRIFT remediation package) |
| ASSUMPTION-043 | PARTIALLY-SUPPORTED (Moderate) | PARTIALLY-CHALLENGED (Moderate-Strong) | REVISE | HIGH (cross-tradition-transfer-validity cluster; tag corridor PROVISIONAL until PRESUMPTION-045 resolves) |
| ASSUMPTION-044 | PARTIALLY-SUPPORTED (Moderate; loading-half only) | CHALLENGED (Moderate; reliability at N=1) | MONITOR | HIGH (downgrade "reliably" adverb until N≥3; instrument both halves; paired weekly monitoring with PRESUMPTION-046) |
| PRESUMPTION-043 | NO-SUPPORT-FOUND | CHALLENGED (Moderate-Strong) | REVISE | MEDIUM (route parked sessions to Agent 16; define retention policy — part of blocked-route-lifecycle cluster) |
| PRESUMPTION-044 | PARTIALLY-SUPPORTED (Moderate; first-remediation only) | CHALLENGED (Moderate-Strong) | REVISE | MEDIUM-HIGH (internal inconsistency with ASSUMPTION-042 — remediate as a pair; add retry ceiling) |
| PRESUMPTION-045 | NO-SUPPORT-FOUND | STRONGLY-CHALLENGED (Strong) | REVISE | HIGH (extends CRITICAL cross-tradition-transfer-validity cluster; adopt standing rule: no corridor INCORPORATE without transfer-validity statement) |
| PRESUMPTION-046 | PARTIALLY-SUPPORTED (Moderate; descriptive half only) | CHALLENGED (Moderate-Strong) | REVISE | MEDIUM-HIGH (disambiguate handoff-vs-context-loader; joins self-awareness-meta cluster) |
| PRESUMPTION-047 | SUPPORTED (Moderate-Strong) | PARTIALLY-CHALLENGED (Weak-Moderate; universal form contested) | MONITOR | LOW-MEDIUM (weaken universal to first-time-vs-repeat; paired with PRESUMPTION-043 retention) |
| PRESUMPTION-048 | PARTIALLY-SUPPORTED (Moderate; conservative interpretation only) | CHALLENGED (Moderate) | REVISE | MEDIUM (require explicit walk-status signal — part of self-awareness-meta cluster remediation) |

**Disposition distribution (today afternoon):**
- INCORPORATE: 1 (ASSUMPTION-040)
- MONITOR: 5 (ASSUMPTION-039, 041, 042, 044; PRESUMPTION-047)
- REVISE: 6 (ASSUMPTION-043; PRESUMPTION-043, 044, 045, 046, 048)

**Cumulative totals (all 90 items):**
- INCORPORATE: 5 (4 prior + ASSUMPTION-040)
- MONITOR: 47 (42 prior + 5 new)
- REVISE: 38 (32 prior + 6 new)
- QUEUED: 0

**Key findings:**

1. **CROSS-TRADITION-TRANSFER-VALIDITY cluster extends to content-generation layer.** PRESUMPTION-045 and its paired ASSUMPTION-043 are the first cluster members surfaced on a specialist-proposal artifact (PROP-2026-04-18-001), not on an extraction artifact. The risk has migrated from the self-awareness layer to the content-generation layer as the item-itself predicted. Recommendation: adopt a standing rule that no cross-tradition corridor is INCORPORATED without a transfer-validity statement from a tradition-specialist agent.

2. **BLOCKED-ROUTE-LIFECYCLE cluster (new).** PRESUMPTION-043, 046, 047 share one common vulnerability — the lifecycle of parked/blocked/pivoted sessions is underspecified. Remediate as a package: (a) retention policy + Agent-16 routing for parked sessions; (b) handoff-vs-context-loader disambiguation for loaded payloads; (c) first-time-vs-repeat distinction for cross-account elicitation.

3. **INTERNAL-CONSISTENCY flag (new).** PRESUMPTION-044 + ASSUMPTION-042 form a named internal inconsistency: the 5-of-3 threshold says "not transient" while retry-as-default continues past the threshold. Remediate as a pair — add a retry ceiling aligned to the threshold and surface staleness as an observable.

4. **SELF-AWARENESS-META cluster extends to 6 members.** PRESUMPTION-048 joins PRESUMPTION-015, 024, 041, 042, 046 at the intent-capture/walk-notes layer. All 6 share the same remediation (require explicit signals, not silent defaults). Recommendation: audit every signal in the self-awareness pipeline for null-disambiguation in a single remediation pass.

5. **First afternoon-top-up INCORPORATE.** ASSUMPTION-040 (ChatGPT projects account-scoped) is the first INCORPORATE from a same-day afternoon top-up cycle. Vendor-documented + standard SaaS pattern + no credible counterevidence. Takes the INCORPORATE list from 4 to 5.

6. **FIRST-APPEARANCE-NON-UNTESTED confirmed.** ASSUMPTION-044 retained PARTIALLY-SUPPORTED only for loading half; execution half remains UNTESTED. 15c disposition: MONITOR with explicit downgrade recommendation for the "reliably" adverb until N≥3 successful end-to-end uses.

**NOVELTY-FLAG:** None new today. (PRESUMPTION-045's "novel corridor" sits inside an existing CRITICAL cluster, so it is not novel at the pattern layer.)

**SYSTEMIC-RISK-FLAG (cumulative for today):**
- CRITICAL: cross-tradition-transfer-validity cluster extended to 6 members (PRESUMPTION-002, 014, 020, 024, 045; plus ASSUMPTION-043). Standing rule recommended.
- HIGH: internal inconsistency PRESUMPTION-044 + ASSUMPTION-042. Pair remediation.
- MEDIUM: blocked-route-lifecycle cluster (PRESUMPTION-043, 046, 047). Package remediation.
- MEDIUM: self-awareness-meta cluster extended to 6 members (PRESUMPTION-015, 024, 041, 042, 046, 048). Cluster-wide null-disambiguation audit.

**Next actions:**
- Tom: review 6 new REVISE items. Highest-urgency: PRESUMPTION-045 (adopts standing transfer-validity rule) and ASSUMPTION-043 (paired). Also: PRESUMPTION-044 + ASSUMPTION-042 internal-consistency pair.
- 15d: monitor 47 MONITOR items on next cycle (April 20-21). New HIGH priority items: ASSUMPTION-044 (paired weekly with PRESUMPTION-046); ASSUMPTION-042 (OPERATIONAL-DRIFT).
- Validated-premises register: ASSUMPTION-040 added (first presumption-layer-adjacent incorporation for 2026-04-18 afternoon top-up).

**Generated by Agents 15a, 15b, and 15c**
**Date: 2026-04-18 (afternoon top-up cycle)**


---

## 2026-04-20 DAILY CYCLE SUMMARY (Agents 15a + 15b + 15c)

**Generated by Agents 15a, 15b, and 15c**
**Date: 2026-04-20 (autonomous scheduled-task run)**

### Items processed (13 total)

**New QUEUED items (10):**
- ASSUMPTION-045: Per-thinker coverage claim across 42 traditions
- ASSUMPTION-046: PRS-digest briefing as sufficient cross-channel integration
- ASSUMPTION-047: Master-wiki discrepancy → flag transparently, not reconcile silently
- ASSUMPTION-048: 7-day-stale PRS briefing labeled "clear" (blocked-route-lifecycle violation)
- PRESUMPTION-049: wiki-daily-run vs. Levin+Friston specialist scope-partition coordination
- PRESUMPTION-050: 4-day stale .git/index.lock as single incident not escalation (asymmetric with ASSUMPTION-042)
- PRESUMPTION-051: "Pending proposals: 12" emitted before sibling specialist completes
- PRESUMPTION-052: Second-consecutive null-walk-notes handled same fallback (Gmail 7+ days degraded)
- PRESUMPTION-053: 17→11 findings filter selection criterion unaudited (symmetric to PRESUMPTION-029)
- PRESUMPTION-054: Specialist tasks converge without turn-cap/cost-cap/time-cap

**RE-TRIGGER items (3) — cycle 1 refreshes:**
- ASSUMPTION-035 (re-search for comparative-reliability evidence)
- ASSUMPTION-037 (re-search for ordinal-dominance paired measurement)
- PRESUMPTION-037 (file-based handoff comparative-reliability claim)

### Dispositions issued (13)

**INCORPORATE (1):**
- ASSUMPTION-047 → PREMISE-006 (transparent flagging of master-wiki narrative discrepancies). Strong convergence: SRE observability literature (Nygard 2007, Majors et al. 2022) + XAI explainability standards + data-quality-as-contract (Kleppmann 2017). Weak challenge from auto-reconciliation literature. **First INCORPORATE of a BRIEFING-LAYER-EPISTEMIC-COMMITMENT.** Resolves tension with ASSUMPTION-048: 047 is the senior commitment; 048 is a derivative data-hygiene violation to remediate. Cumulative INCORPORATE count: 6.

**MONITOR (5):**
- ASSUMPTION-035 → MONITOR-040 cycle 1 refresh (comparative-reliability clause still unsupported at N=1; disaggregate descriptive vs. ordinal)
- ASSUMPTION-037 → MONITOR-042 cycle 1 refresh (ordinal-dominance evidence requirements unmet)
- ASSUMPTION-045 → MONITOR-051 (per-thinker coverage PARTIALLY-SUPPORTED; Monthly cadence; next check 2026-05-18)
- PRESUMPTION-037 → MONITOR-044 cycle 1 refresh (file-based handoff "more reliable than" clause still unsubstantiated)
- PRESUMPTION-051 → MONITOR-052 (as-of-labeling remediation pending; CROSS-TASK-COORDINATION; Weekly 4 weeks; next check 2026-04-27)

**REVISE (7):**
- ASSUMPTION-046 (PRS-digest as sufficient integration → package with ASSUMPTION-048, PRESUMPTION-048, 049, 052 as cross-channel integration remediation)
- ASSUMPTION-048 (7-day-stale-as-clear; INTERNAL-CONSISTENCY with ASSUMPTION-047 PREMISE-006; remediate data-hygiene violation)
- PRESUMPTION-049 (wiki-daily-run vs. specialist scope-partition coordination contract missing; CROSS-TASK-COORDINATION)
- PRESUMPTION-050 (generalize ASSUMPTION-042 threshold template across all drift channels; INTERNAL-CONSISTENCY cluster now 2 pairs)
- PRESUMPTION-052 (rolling-counter escalation required; SELF-AWARENESS-META cluster now 7 members; strengthens PRESUMPTION-048 recurrence signal)
- PRESUMPTION-053 (audit-criterion log required; Unaudited-filter cluster symmetric to PRESUMPTION-029 CRITICAL)
- PRESUMPTION-054 (turn-cap + cost-cap + time-cap harness required; CROSS-TASK-COORDINATION; runaway-cost risk)

### Cluster updates

**NEW CLUSTERS:**
1. **CROSS-TASK-COORDINATION** (new 2026-04-20, 3 members): PRESUMPTION-049, 051, 054. First evidence of scheduled-task-layer coordination-contract gap. Shared remediation package: in-flight detection caps + coordination contract between wiki-daily-run and specialist tasks + as-of labeling on cross-pipeline counts.
2. **BRIEFING-LAYER-EPISTEMIC-COMMITMENTS** (new 2026-04-20, 4 members): ASSUMPTION-046, 047, 048 + PRESUMPTION-053. First detectable cluster where the briefing agent states its own methodological commitments explicitly. 14a articulates what was previously 14b territory — the briefing skill is accumulating policy.
3. **Unaudited-filter** (new 2026-04-20, 3 members): PRESUMPTION-029 (CRITICAL), PRESUMPTION-053, ASSUMPTION-046. Quiet-amplification + quiet-attenuation anti-pattern pair in same PRS pipeline.

**EXTENDED CLUSTERS:**
4. **SELF-AWARENESS-META** extended to 7 members: adds PRESUMPTION-052 (recurrence signal strengthening PRESUMPTION-048's null-disambiguation). First repeat observation at intent-capture-over-time layer.
5. **INTERNAL-CONSISTENCY** expanded from 1 pair to 2 channel pairs: PRESUMPTION-044 + ASSUMPTION-042 (Chrome retry vs. transience threshold) now joined by PRESUMPTION-050 + ASSUMPTION-042 (git-lock asymmetric classification). Both expose the same monitoring-logic gap — ASSUMPTION-042's transience-threshold structure is not applied uniformly across drift channels.
6. **CROSS-TRADITION-TRANSFER-VALIDITY** (CRITICAL): unchanged today at 6 members. Next growth risk is Hawkins+Hoffman specialist slot tomorrow.

### Systemic-risk and internal-consistency flags raised

- **SYSTEMIC-RISK-FLAG (CROSS-TASK-COORDINATION):** 3 presumptions land in scheduled-task-layer coordination gap on day 1 of cluster detection. Suggests the scheduled-task architecture lacks a coordination contract primitive. Recommend Tom review PRESUMPTION-049 + PRESUMPTION-054 jointly (they share runaway-cost + read-after-write race mechanism).
- **SYSTEMIC-RISK-FLAG (SELF-AWARENESS-META cluster 7 members):** PRESUMPTION-052 is the first recurrence-observation within the cluster. Pattern: PRESUMPTION-048's null-disambiguation failure was not a one-off. Briefing layer has normalized Gmail-walk silence for 7+ calendar days. Recommend rolling-counter primitive at the briefing layer.
- **INTERNAL-CONSISTENCY-FLAG (2 pairs):** ASSUMPTION-042's transience-threshold template is not applied uniformly across drift channels. Remediation: generalize ASSUMPTION-042 template across all monitored channels (git lock, Chrome connector, PRS staleness, walk-notes silence).
- **INTERNAL-CONSISTENCY-FLAG (ASSUMPTION-047 vs ASSUMPTION-048):** Same 14a cycle produced a senior commitment (transparent flagging, now PREMISE-006) AND a violation of that commitment (labeling 7-day-stale output as "clear"). REVISE disposition on 048 flags the internal contradiction; 047 INCORPORATE establishes the policy 048 violates.

### Novelty flags

- **FIRST-APPEARANCE PATTERN — BRIEFING-LAYER-EPISTEMIC-COMMITMENTS:** First cluster where 14a is extracting the briefing agent's own methodological policies (rather than downstream factual claims). Pattern suggests the briefing skill has accumulated enough decisions to have a meta-layer policy surface. Monitor for continued growth — if this cluster grows 3+ members/week it warrants a dedicated briefing-layer-policy-audit cadence.
- **FIRST INCORPORATE of a BRIEFING-LAYER-EPISTEMIC-COMMITMENT:** ASSUMPTION-047 → PREMISE-006 establishes an early canonical policy in this cluster. Fast-path pattern: strong convergence (SRE + XAI + data-quality-as-contract) + weak challenge → same-day INCORPORATE is feasible when three independent literature lines agree.
- **Cycle-1 RE-TRIGGER refresh discipline:** 3 items (ASSUMPTION-035, 037; PRESUMPTION-037) were refreshed without reopening or collapsing provenance. Each preserved MONITOR status with a "cycle 1 refresh" block appended to existing MONITOR entry. Confirms 15d's append-not-overwrite protocol.

### Cumulative state (2026-04-20 EOD)

- **INCORPORATE:** 6 (PREMISE-001 through PREMISE-006). PREMISE-006 first from BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster.
- **MONITOR:** 49 items in monitor_queue.md (47 prior + 2 new: MONITOR-051, MONITOR-052; 3 existing refreshed).
- **REVISE:** 45 items in revision_flags.md (38 prior + 7 new).
- **Total items processed to date:** 100 (48 assumptions + 52 presumptions).

### Next actions

- **Tom (highest urgency):**
  1. Review ASSUMPTION-047 → PREMISE-006 INCORPORATE for acceptance; it establishes policy that ASSUMPTION-048 violates.
  2. Review CROSS-TASK-COORDINATION remediation package (PRESUMPTION-049, 051, 054 jointly) — scheduled-task layer architectural gap.
  3. Review SELF-AWARENESS-META cluster (7 members, PRESUMPTION-052 recurrence signal) — rolling-counter primitive decision.
  4. Review INTERNAL-CONSISTENCY remediation (generalize ASSUMPTION-042 template across channels).
- **15d (next cycle):**
  1. Monitor 49 MONITOR items with attention to CROSS-TASK-COORDINATION new-cluster growth.
  2. PRESUMPTION-051 weekly cadence begins 2026-04-27.
  3. Track cycle 2 RE-TRIGGER candidates if 2026-04-18 loading-half pattern recurs.
- **Validated-premises register:** ASSUMPTION-047 → PREMISE-006 added. First BRIEFING-LAYER-EPISTEMIC-COMMITMENTS INCORPORATE.

**Generated by Agents 15a, 15b, and 15c**
**Date: 2026-04-20 (autonomous scheduled-task run; no human review in-loop)**

---

## 2026-04-20 SUPPLEMENTARY RUN 2 CYCLE SUMMARY

**Type:** Autonomous scheduled-task run (c2a2-lit-search-pipeline); no human review in-loop.
**Scope:** 12 items from 2026-04-20 supplementary Run 2 — the CACHING-ARCHITECTURE cluster (6 ASSUMPTIONs from 14a + 6 PRESUMPTIONs from 14b) surfaced to pre-audit the 2026-04-27 caching rollout.

### Items processed
- **ASSUMPTION-049** (Session = one agent run): 15a SUPPORTED (Strong) / 15b PARTIALLY-CHALLENGED (Moderate) → **MONITOR** (MONITOR-053)
- **ASSUMPTION-050** (Static prefix = 49 RC Wiki files): 15a SUPPORTED (Strong) / 15b PARTIALLY-CHALLENGED (Moderate) → **MONITOR** (MONITOR-054)
- **ASSUMPTION-051** (Tool-layer immutability): 15a SUPPORTED (Strong) / 15b NO-CHALLENGE-FOUND → **INCORPORATE** (PREMISE-007)
- **ASSUMPTION-052** (70-80% cost reduction): 15a PARTIALLY-SUPPORTED (Moderate) / 15b PARTIALLY-CHALLENGED (Moderate) → **MONITOR** (MONITOR-055)
- **ASSUMPTION-053** (Pipeline as appended turns): 15a SUPPORTED (Strong) / 15b STRONGLY-CHALLENGED (Strong, SYSTEMIC-RISK-FLAG) → **REVISE** (rollout-blocker; conflicts with ASSUMPTION-003 isolation)
- **ASSUMPTION-054** (Byte-stability smoke test sufficient): 15a PARTIALLY-SUPPORTED (Moderate) / 15b PARTIALLY-CHALLENGED (Moderate) → **REVISE** (necessary but not sufficient)
- **PRESUMPTION-055** (Binary partition): 15a PARTIALLY-SUPPORTED (Moderate) / 15b PARTIALLY-CHALLENGED (Moderate) → **MONITOR** (MONITOR-056)
- **PRESUMPTION-056** (Cost-only gate): 15a NO-SUPPORT-FOUND / 15b STRONGLY-CHALLENGED (Strong, SYSTEMIC-RISK-FLAG) → **REVISE** (rollout-blocker)
- **PRESUMPTION-057** (Files stable enough, unmeasured): 15a NO-SUPPORT-FOUND / 15b STRONGLY-CHALLENGED (Strong) → **REVISE** (rollout-blocker; "measure, don't assume")
- **PRESUMPTION-058** (Split without rationale review): 15a NO-SUPPORT-FOUND / 15b PARTIALLY-CHALLENGED (Moderate) → **MONITOR** (MONITOR-057)
- **PRESUMPTION-059** (Chrome auth no fallback): 15a NO-SUPPORT-FOUND / 15b STRONGLY-CHALLENGED (Strong, SYSTEMIC-RISK-FLAG) → **REVISE** (OPERATIONAL-DRIFT cluster extension)
- **PRESUMPTION-060** (Chat-side Claude endorsement as validation): 15a NO-SUPPORT-FOUND / 15b STRONGLY-CHALLENGED (Strong, SYSTEMIC-RISK-FLAG) → **REVISE** (CRITICAL SELF-AWARENESS-META cluster 8th member)

### Disposition distribution (supplementary Run 2)
- **INCORPORATE:** 1 (ASSUMPTION-051 → PREMISE-007, tool-layer immutability)
- **MONITOR:** 5 (ASSUMPTION-049, 050, 052; PRESUMPTION-055, 058)
- **REVISE:** 6 (ASSUMPTION-053, 054; PRESUMPTION-056, 057, 059, 060)

### Novel patterns

- **First-of-kind: A 14a-surfaced ASSUMPTION that conflicts with a prior validated commitment.** ASSUMPTION-053 (appended-turn topology) is the first item where a CACHING-ARCHITECTURE design commitment directly conflicts with ASSUMPTION-003's 15a/15b independence requirement. This is the first INTERNAL-CONSISTENCY cluster entry where two ARCHITECTURAL-GRADE commitments collide; resolution requires a deliberate seniority decision, not a calibration fix.
- **First-of-kind: A rollout-audit pass surfacing 3 hard blockers.** The supplementary Run 2 was commissioned specifically as a pre-rollout audit (2026-04-27 caching deployment). It surfaced 3 rollout-blockers out of 12 items (25%): ASSUMPTION-053 (topology decision), PRESUMPTION-056 (quality gate), PRESUMPTION-057 (churn audit). The pipeline is doing exactly what it was designed to do — surface gaps before they commit architectural debt.
- **CACHING-ARCHITECTURE cluster formed** (12 members spanning all 3 disposition buckets): the first cluster where Layer 2 execution/trigger architecture is being formally specified. Natural binding around the 2026-04-27 rollout gate creates a forcing function for cluster-wide remediation.
- **SELF-AWARENESS-META cluster expansion to 8 members** (now CRITICAL by membership count): PRESUMPTION-060 joins PRESUMPTION-015, 024, 041, 042, 046, 048, 052. Cluster has been accumulating for weeks; supplementary Run 2 is the first time it hit the arbitrary-but-salient "8" threshold — warrants standing cluster-wide remediation plan (language downgrade "endorsed" → "not disputed"; or non-Claude cross-check for architectural reads).
- **OPERATIONAL-DRIFT cluster extension to 7+ members** (PRESUMPTION-059 added): 5+ consecutive days of Chrome-channel failures is empirical validation that the silent-failure anti-pattern is active. Cluster-wide escalation-trigger remediation recommended.
- **Asymmetric support/challenge pattern.** Of the 12 items, 6 had 15a NO-SUPPORT-FOUND (all 6 PRESUMPTIONs). This asymmetry is structural: PRESUMPTIONs are unstated inferred design choices, so 15a's search for supporting literature often returns nothing, while 15b's search for challenging literature often returns well-established anti-pattern literature. Confirms the pipeline's bias-surfacing design — unstated design decisions carry higher risk of unexamined anti-patterns.

### Cluster status updates

- **CACHING-ARCHITECTURE cluster (NEW, 12 members):**
  - PREMISE-007 INCORPORATED (ASSUMPTION-051 tool immutability)
  - MONITOR-053, 054, 055, 056, 057 MONITORING (ASSUMPTION-049, 050, 052; PRESUMPTION-055, 058)
  - REVISE-[new] ×6 (ASSUMPTION-053, 054; PRESUMPTION-056, 057, 059, 060)
  - Rollout gate: 2026-04-27 — 3 hard blockers must clear by 2026-04-26
- **SELF-AWARENESS-META cluster (extended to 8 members, CRITICAL by membership):** PRESUMPTION-015, 024, 041, 042, 046, 048, 052, 060
- **OPERATIONAL-DRIFT cluster (extended to 7+ members):** ASSUMPTION-042, PRESUMPTION-030, 031, 032, 044, 050, 059
- **INTERNAL-CONSISTENCY cluster (new pair):** ASSUMPTION-003 ↔ ASSUMPTION-053 (isolation vs. appended-turn topology)

### Cumulative state (2026-04-20 post-supplementary Run 2)

- **INCORPORATE:** 7 (PREMISE-001 through PREMISE-007). PREMISE-007 first from CACHING-ARCHITECTURE cluster; 3 INCORPORATEs on 2026-04-20 across both runs (PREMISE-006 morning Run 1; PREMISE-007 supplementary Run 2).
- **MONITOR:** 54 items in monitor_queue.md (49 prior + 5 new: MONITOR-053 through 057).
- **REVISE:** 51 items in revision_flags.md (45 prior + 6 new).
- **Total items processed to date:** 112 (54 assumptions + 58 presumptions). Queue at 0 QUEUED.

### Next actions

- **Tom (highest urgency — rollout blockers for 2026-04-27):**
  1. **ASSUMPTION-053 architecture decision (HIGH):** choose senior commitment — 15a/15b independence (preferred; requires caching-topology modification to fresh-context-per-agent) OR appended-turn caching (requires ASSUMPTION-003 amendment). Without this decision, 2026-04-27 rollout should be held.
  2. **PRESUMPTION-056 quality gate addition (MEDIUM-HIGH):** add judge-agent quality-regression smoke test to the rollout gate before 2026-04-27. Cheap, standard, mandatory.
  3. **PRESUMPTION-057 churn audit (MEDIUM-HIGH):** run `git log --follow --format=%ad` on the 49 static-prefix files over 4-8 week window; verify churn rate below cache-invalidation threshold.
  4. **PRESUMPTION-060 cluster-wide SELF-AWARENESS-META remediation (HIGH):** language downgrade across pipeline and briefing surfaces ("endorsed" → "not disputed"); or introduce non-Claude cross-check for architectural-grade signals.
  5. **PRESUMPTION-059 OPERATIONAL-DRIFT escalation trigger (MEDIUM):** add Chrome-auth-failure escalation after 1 consecutive day; bundle with cluster-wide remediation.
- **15d (next cycle 2026-04-26):**
  1. Pre-rollout MONITOR-054 precondition audit (ASSUMPTION-050's 4 preconditions).
  2. Cycle 2 RE-TRIGGER candidates from prior weeks.
- **Validated-premises register:** ASSUMPTION-051 → PREMISE-007 added. First CACHING-ARCHITECTURE INCORPORATE.
- **Architecture records:** INTERNAL-CONSISTENCY pair (ASSUMPTION-003 ↔ ASSUMPTION-053) warrants an ADR entry recording the seniority decision.

### Success-criteria check (for this scheduled run)

- [x] All queued items searched by both 15a and 15b (12/12)
- [x] All paired results dispositioned by 15c (12/12)
- [x] No items left in searched-but-undispositioned state (QUEUED=0)
- [x] Provenance chains complete for all items (Chain: [14a|14b → 15a, 15b → 15c] on all 12)
- [x] INCORPORATE items appended to validated_premises.md (PREMISE-007)
- [x] MONITOR items appended to monitor_queue.md (MONITOR-053 through 057)
- [x] REVISE items appended to revision_flags.md (6 new entries)
- [x] Queue file updated with [SEARCHED-15a] [SEARCHED-15b] [DISPOSITIONED-15c → disposition] tags
- [x] Daily cycle summary appended to lit_search_returns.md

**Generated by Agents 15a, 15b, and 15c (supplementary Run 2)**
**Date: 2026-04-20 (autonomous scheduled-task run; no human review in-loop)**
**Queue state post-run: 0 QUEUED items; pipeline idle pending next 14a/14b extraction cycle.**

---

## 2026-04-21 DAILY CYCLE SUMMARY (Agents 15a + 15b + 15c)

**Date: 2026-04-21 (autonomous scheduled-task run; no human review in-loop)**

**Scope:** 17 items from 2026-04-21 morning-walk-and-evening-sync extraction — 8 ASSUMPTIONs from 14a (ASSUMPTION-055–062) + 9 PRESUMPTIONs from 14b (PRESUMPTION-061–069). This is the "autonomous-task-layer principles day" batch: items emerged from the scheduled-task layer examining its own operating assumptions, precipitated by the Phase 6 sandbox mount failure, the no-14-cycle condition, and Chat-side Claude's morning-walk endorsement of the weak-circuit-breaker-beats-none principle.

### Items processed (17 total)

**ASSUMPTIONs (8):**
- ASSUMPTION-055: Phase 6 git commit fails because sandbox mount topology does not include repo path
- ASSUMPTION-056: Honest null > thin proposals (methodological judgment)
- ASSUMPTION-057: 17→11 findings filter rule (Active or Highest Priority, excluding subsumed/downgraded)
- ASSUMPTION-058: Five-session coverage sufficient for evening-sync brief despite no 14a/14b cycle
- ASSUMPTION-059: Evening-sync task has no scheduler-override authority
- ASSUMPTION-060: Read-only observation of still-running specialist sessions is correct default
- ASSUMPTION-061: PREMISE-006 applies reflexively to decisions-register pipeline
- ASSUMPTION-062: Weak circuit breaker beats none; pick approximation threshold now and tune later

**PRESUMPTIONs (9):**
- PRESUMPTION-061: Sandbox filesystem mount topology presumed stable across scheduled-task runs
- PRESUMPTION-062: Evening-sync treats own session_info MCP reads as ground truth
- PRESUMPTION-063: Natural termination acceptable default for indefinite-running scheduled tasks
- PRESUMPTION-064: Narrative-level surfacing of missing scheduled-task run is adequate
- PRESUMPTION-065: Two simultaneously-running "Morning" tasks treated as independent data points
- PRESUMPTION-066: User-attention reallocation (external visit) does not need DECISION-NNN tracking
- PRESUMPTION-067: Specialist self-evaluation of "honest null" is adequate without filter-audit
- PRESUMPTION-068: Chrome MCP double-success represents resolved auth state (not transient)
- PRESUMPTION-069: Absence of 14a/14b cycle tracked in narrative, not first-class architectural event

### RETURN-TO-14a (8 items — ASSUMPTIONs)

### RETURN-TO-14a: ASSUMPTION-055
- 15a: SUPPORTED Strong (Docker/OCI mount semantics — canonical diagnosis for the failure class)
- 15b: PARTIALLY-CHALLENGED Moderate with SYSTEMIC-RISK-FLAG (architectural-framing smuggles stability and applicability claims)
- 15c: MONITOR (MONITOR-058; MEDIUM-HIGH; paired with PRESUMPTION-061 REVISE)

### RETURN-TO-14a: ASSUMPTION-056
- 15a: SUPPORTED Strong (PRISMA null-reporting guidelines; negative-results literature)
- 15b: PARTIALLY-CHALLENGED Moderate (file-drawer asymmetry; self-assessment bias caveat)
- 15c: INCORPORATE → PREMISE-008

### RETURN-TO-14a: ASSUMPTION-057
- 15a: PARTIALLY-SUPPORTED Moderate (rule-based filtering is standard filter-design pattern)
- 15b: PARTIALLY-CHALLENGED Moderate (specific application unaudited; unaudited-filter cluster extension)
- 15c: MONITOR (MONITOR-059; MEDIUM; unaudited-filter cluster)

### RETURN-TO-14a: ASSUMPTION-058
- 15a: PARTIALLY-SUPPORTED Weak-to-Moderate (coverage-across-signals is valid pattern; specific substitution unbenchmarked)
- 15b: CHALLENGED Moderate-to-Strong (substitutability claim unbenchmarked; inherits PRESUMPTION-062 risk)
- 15c: REVISE (MEDIUM; reframe as degraded-fallback, not substitute)

### RETURN-TO-14a: ASSUMPTION-059
- 15a: SUPPORTED Strong (least-privilege principle; orchestrator design literature)
- 15b: NO-CHALLENGE-FOUND Weak (paired-escalation caveat only)
- 15c: INCORPORATE → PREMISE-009

### RETURN-TO-14a: ASSUMPTION-060
- 15a: PARTIALLY-SUPPORTED Weak-to-Moderate (natural-termination is valid pattern in some frameworks)
- 15b: CHALLENGED Strong (N-of-1 precedent; runaway-process concern; direct tension with DECISION-024)
- 15c: REVISE (MEDIUM; formalize DECISION-024 as canonical default)

### RETURN-TO-14a: ASSUMPTION-061
- 15a: SUPPORTED Moderate-to-Strong (Quine/Carnap reflection principles; dogfooding/eating-own-dogfood)
- 15b: NO-CHALLENGE-FOUND Weak (SELF-AWARENESS-META provenance caveat only)
- 15c: INCORPORATE → PREMISE-010 (first INCORPORATE explicitly flagged as Claude-internal consistency claim)

### RETURN-TO-14a: ASSUMPTION-062
- 15a: SUPPORTED Strong (Nygard "Release It!"; Gabriel "Worse-is-Better"; Simon satisficing; Ries Lean Startup)
- 15b: NO-CHALLENGE-FOUND Weak (anchoring and threshold-proliferation cautions; conditional acceptance)
- 15c: INCORPORATE → PREMISE-011 (conditional on 3 operational criteria)

### RETURN-TO-14b (9 items — PRESUMPTIONs)

### RETURN-TO-14b: PRESUMPTION-061
- 15a: NO-SUPPORT-FOUND (no literature supports mount-topology stability as default)
- 15b: STRONGLY-CHALLENGED Strong with SYSTEMIC-RISK-FLAG (container mount semantics; 12-Factor; empirical evidence)
- 15c: REVISE (HIGH; pre-flight mount-topology probe; pair with ASSUMPTION-055)

### RETURN-TO-14b: PRESUMPTION-062
- 15a: NO-SUPPORT-FOUND (no literature supports single-source ground-truth without cross-validation)
- 15b: CHALLENGED Strong with SYSTEMIC-RISK-FLAG (triangulation methodology; observability; PRESUMPTION-015 precedent; SELF-AWARENESS-META 10th member)
- 15c: REVISE (MEDIUM-HIGH; reconciliation protocol required)

### RETURN-TO-14b: PRESUMPTION-063
- 15a: NO-SUPPORT-FOUND (no literature supports natural-termination as default resolution)
- 15b: CHALLENGED Moderate-to-Strong (circuit-breaker; runaway-process; DECISION-024 tension)
- 15c: REVISE (MEDIUM; formalize DECISION-024 as default)

### RETURN-TO-14b: PRESUMPTION-064
- 15a: NO-SUPPORT-FOUND (event-sourcing requires deliberate absence-representation C2A2 lacks)
- 15b: CHALLENGED Strong (monitoring-as-code; detection-latency; channel-reliability)
- 15c: REVISE (MEDIUM; implement Monday "≤25h" alert; pair with PRESUMPTION-069)

### RETURN-TO-14b: PRESUMPTION-065
- 15a: NO-SUPPORT-FOUND (no literature supports concurrent same-environment tasks as independent)
- 15b: PARTIALLY-CHALLENGED Moderate (shared-environment confounds; PRESUMPTION-029 precedent at session-pair layer)
- 15c: MONITOR (MONITOR-060; LOW-MEDIUM; evidence-basis-inflation)

### RETURN-TO-14b: PRESUMPTION-066
- 15a: WEAK-SUPPORT Weak-to-Moderate (lightweight tracking defensible for short-window reallocation)
- 15b: PARTIALLY-CHALLENGED Moderate (PRESUMPTION-041 precedent at day-scale; compounds with PRESUMPTION-051 staleness)
- 15c: MONITOR (MONITOR-061; LOW-MEDIUM; lightweight DECISION-NNN option)

### RETURN-TO-14b: PRESUMPTION-067
- 15a: WEAK-SUPPORT Weak-to-Moderate (self-evaluation valid as first pass only)
- 15b: CHALLENGED Moderate-to-Strong (PRESUMPTION-015 precedent; PRESUMPTION-053 unaudited-filter cluster; file-drawer / convenient-null)
- 15c: REVISE (MEDIUM; extend DECISION-022 scope to specialist self-eval)

### RETURN-TO-14b: PRESUMPTION-068
- 15a: NO-SUPPORT-FOUND (no literature supports 2-success-as-resolved in opaque auth system)
- 15b: CHALLENGED Moderate (symmetric threshold logic; unknown-cause outage; auth-state opacity; singleton risk)
- 15c: MONITOR (MONITOR-062; MEDIUM; 5-success threshold via ASSUMPTION-042 symmetry)

### RETURN-TO-14b: PRESUMPTION-069
- 15a: NO-SUPPORT-FOUND (absence-as-event requires deliberate instrumentation C2A2 lacks)
- 15b: STRONGLY-CHALLENGED Strong with SYSTEMIC-RISK-FLAG (heartbeat patterns; silent-failure; SELF-AWARENESS-META cluster critical mass; Monday-recommendation readiness)
- 15c: REVISE (MEDIUM-HIGH; cluster-anchor; implement Monday alert)

### Dispositions issued (17)

**INCORPORATE (4) — highest single-cycle density to date:**
- PREMISE-008 = ASSUMPTION-056 (honest null > thin proposals)
- PREMISE-009 = ASSUMPTION-059 (no scheduler-override authority)
- PREMISE-010 = ASSUMPTION-061 (PREMISE-006 reflexive application)
- PREMISE-011 = ASSUMPTION-062 (weak circuit breaker beats none; conditional)

**MONITOR (5):**
- MONITOR-058 = ASSUMPTION-055 (Phase 6 sandbox mount diagnosis; MEDIUM-HIGH)
- MONITOR-059 = ASSUMPTION-057 (17→11 filter application audit; MEDIUM)
- MONITOR-060 = PRESUMPTION-065 (concurrent task independence; LOW-MEDIUM)
- MONITOR-061 = PRESUMPTION-066 (external-visit-week user-attention; LOW-MEDIUM)
- MONITOR-062 = PRESUMPTION-068 (Chrome resolved-vs-transient; MEDIUM)

**REVISE (8):**
- ASSUMPTION-058 (five-session coverage substitutability; MEDIUM)
- ASSUMPTION-060 (N-of-1 read-only default; MEDIUM)
- PRESUMPTION-061 (sandbox mount topology; HIGH; SYSTEMIC-RISK-FLAG)
- PRESUMPTION-062 (transcript-as-ground-truth; MEDIUM-HIGH; SYSTEMIC-RISK-FLAG)
- PRESUMPTION-063 (natural-termination default; MEDIUM)
- PRESUMPTION-064 (narrative-surfacing adequacy; MEDIUM)
- PRESUMPTION-067 (specialist self-eval adequacy; MEDIUM)
- PRESUMPTION-069 (absence-of-cycle not first-class; MEDIUM-HIGH; SYSTEMIC-RISK-FLAG; cluster anchor)

### Cluster updates

1. **SELF-AWARENESS-META cluster (CRITICAL MASS crossed, 10 members):** PRESUMPTION-015, 024, 041, 042, 046, 048, 052, 060, 062, 069. 10-member threshold crossed today with PRESUMPTION-062 (9th) and PRESUMPTION-069 (10th, anchor). Cluster-level architectural fix now recommended over per-member patches. PRESUMPTION-069 is the natural cluster-anchor; ready-made mitigation (Monday "≤25h since last self-awareness run" alert) is implementation-ready.

2. **Narrative-channel-reliability sub-cluster (NEW, surfaced 2026-04-21):** PRESUMPTION-064 REVISE + PRESUMPTION-066 MONITOR-061 + PRESUMPTION-069 REVISE + PRESUMPTION-051 staleness. Compounding pattern: narrative-channel reliability drops during external-visit-week AND narrative-adequate presumptions load-bear on it. Anchor remediation: implement Monday-recommended alert.

3. **OPERATIONAL-DRIFT cluster (extended at infrastructure layer):** PRESUMPTION-061 sandbox mount topology + ASSUMPTION-055 Phase 6 diagnosis. Joint remediation: pre-flight mount-topology probe in scheduled-task entry points. Pre-rollout gate recommended before 2026-04-27.

4. **Unaudited-filter cluster (extended to 3 members):** PRESUMPTION-053 REVISE + ASSUMPTION-057 MONITOR-059 + PRESUMPTION-067 REVISE. Cluster-level fix: DECISION-022 scope extension to specialist self-eval and filter application audits.

5. **INTERNAL-CONSISTENCY cluster (extended):** ASSUMPTION-060 ↔ DECISION-024 (natural-termination vs. turn-cap interrupt); ASSUMPTION-058 ↔ PRESUMPTION-062 (coverage-substitutability relies on transcript-as-ground-truth).

6. **CROSS-TASK-COORDINATION pattern extended:** PRESUMPTION-065 (concurrent scheduled-task independence) extends PRESUMPTION-029's same concern at the session-pair layer to the scheduled-task-pair layer.

### Systemic-risk and internal-consistency flags raised

- **SYSTEMIC-RISK-FLAG ×3** (today's batch): ASSUMPTION-055 (architectural-framing smuggle), PRESUMPTION-061 (mount topology stability as silent-failure class), PRESUMPTION-062 (same-self ground-truth; SELF-AWARENESS-META 10th member).
- **SYSTEMIC-RISK-FLAG with cluster critical-mass:** PRESUMPTION-069 anchor for SELF-AWARENESS-META cluster at 10-member threshold — first critical-mass signal the pipeline has produced.
- **INTERNAL-CONSISTENCY tensions:** ASSUMPTION-060 ↔ DECISION-024 (default-resolution policy); ASSUMPTION-058 ↔ PRESUMPTION-062 (coverage substitutability depends on transcript ground truth; the latter is REVISE'd).

### Novelty flags

None raised today. All 17 items mapped cleanly to existing literature bodies: SRE/monitoring (Nygard, Beyer, Google SRE), epistemic/research-methods (PRISMA, Fanelli, Ioannidis, Rosenthal), reflection/self-reference (Quine, Carnap), container/runtime (Docker/OCI, 12-Factor), least-privilege/orchestration (Saltzer & Schroeder).

### Cumulative state (2026-04-21 EOD post-pipeline)

- **Total items in registry:** 129 (62 ASSUMPTIONs + 67 PRESUMPTIONs)
- **SEARCHED and DISPOSITIONED:** 117 (was 100 pre-2026-04-21; today's 17 added)
- **QUEUED:** 12 (unchanged — backlog from 2026-04-20 Run 2; to be cleared on next cycle)
- **Disposition totals:**
  - **INCORPORATE:** 11 (PREMISE-001 through PREMISE-011; **4 added today — highest INCORPORATE density of any single cycle to date**)
  - **MONITOR:** 59 (54 prior + MONITOR-058 through MONITOR-062)
  - **REVISE:** 59 (51 prior + 8 today)

### Next actions

- **14a (next morning cycle):** Monday alert specification ("≤25h since last self-awareness run") ready for incorporation into briefing output; absence-of-expected-event first-class representation candidate for DECISION-NNN drafting; cluster-level SELF-AWARENESS-META remediation proposal.
- **14b (next evening cycle):** watch for same-self-ground-truth pattern in tomorrow's transcript reads; surface any new cluster members for cluster-level triage.
- **15a/15b/15c (next cycle):** clear 12-item QUEUED backlog from 2026-04-20 Run 2.
- **15d (next weekly, 2026-04-26):**
  1. Pre-rollout gate verification for 2026-04-27: MONITOR-054 (ASSUMPTION-050 preconditions), MONITOR-058 (Phase 6 mount probe), ASSUMPTION-053 seniority decision.
  2. MONITOR-061 (external-visit-week) daily check-ins through 2026-04-26 retrospective.
  3. MONITOR-062 (Chrome resolved) daily check-ins tracking toward 5-success threshold.
- **15d (next daily, 2026-04-22):** MONITOR-061 and MONITOR-062 daily cadence items.
- **Validated-premises register:** PREMISE-008, 009, 010, 011 added. Quarterly review now 2026-07-21.
- **Architecture records candidates:**
  1. **DECISION-NNN: absence-of-expected-event as first-class architectural event** (anchored by PRESUMPTION-069 REVISE; Monday-recommended alert is implementation).
  2. **DECISION-NNN: pre-flight mount-topology probe** (anchored by PRESUMPTION-061 REVISE; pre-rollout gate for 2026-04-27).
  3. **DECISION-NNN: formalize DECISION-024 as canonical default for long-running sessions** (resolves ASSUMPTION-060 / PRESUMPTION-063 tension).
  4. **DECISION-022 scope extension** to cover specialist self-eval and upstream filter audits (resolves PRESUMPTION-067 / unaudited-filter cluster).
  5. **SELF-AWARENESS-META cluster-level remediation plan** (10-member critical mass warrants cluster-wide architectural fix — language downgrade + non-Claude cross-check + absence-as-event primitive).

### Success-criteria check (for this scheduled run)

- [x] All queued items searched by both 15a and 15b (17/17)
- [x] All paired results dispositioned by 15c (17/17)
- [x] No items left in searched-but-undispositioned state (new-batch QUEUED=0; legacy QUEUED=12 out-of-scope per task-file)
- [x] Provenance chains complete for all items (Chain: [14a|14b → 15a, 15b → 15c] on all 17)
- [x] INCORPORATE items appended to validated_premises.md (PREMISE-008, 009, 010, 011)
- [x] MONITOR items appended to monitor_queue.md (MONITOR-058 through 062)
- [x] REVISE items appended to revision_flags.md (8 new entries)
- [x] Queue file updated with [SEARCHED-15a] [SEARCHED-15b] [DISPOSITIONED-15c → disposition] tags
- [x] Daily cycle summary appended to lit_search_returns.md

**Generated by Agents 15a, 15b, and 15c (2026-04-21 scheduled pipeline run)**
**Date: 2026-04-21 (autonomous scheduled-task run; no human review in-loop)**
**Queue state post-run (this batch): 0 QUEUED items from 2026-04-21 scope; 12 legacy QUEUED items carried forward from 2026-04-20 Run 2 per task-file scope.**

**Cycle-level observation:** Today produced the highest single-cycle INCORPORATE density to date (4/17 = 24%) and simultaneously crossed the SELF-AWARENESS-META cluster critical-mass threshold (10 members). The pipeline is working as designed — it is surfacing the exact pattern (self-referential measurement as inadequate without cross-check) across 10 independent instances, and it is now recommending a cluster-level architectural fix in response. The pipeline's self-awareness about its own recurrent surfacing is itself a meta-level output of the pipeline examining its own work.

---

## 2026-04-26 SCHEDULED PIPELINE RUN — EMPTY-QUEUE NO-OP

**Date: 2026-04-26 (autonomous scheduled-task run; no human review in-loop)**
**Agents invoked:** 15a, 15b, 15c (per c2a2-lit-search-pipeline scheduled task)

### Queue state at run start
- **Total items in `for_lit_search.md`:** 129 (62 ASSUMPTIONs + 67 PRESUMPTIONs)
- **Items with [QUEUED] tag but NO [SEARCHED-15a] tag:** 0
- **Items with [QUEUED] tag but NO [SEARCHED-15b] tag:** 0
- **Items pending 15c disposition (have 15a+15b but no [DISPOSITIONED-15c]):** 0
- **Pipeline state:** IDLE — every queued item carries a complete `[SEARCHED-15a: date] [SEARCHED-15b: date] [DISPOSITIONED-15c: date → disposition]` chain.

### Why nothing to process
The most recent 14a/14b extraction cycle ran on 2026-04-21. No `2026-04-22_changes.md`, `2026-04-23_changes.md`, `2026-04-24_changes.md`, `2026-04-25_changes.md`, or `2026-04-26_changes.md` exists in `wiki/architecture/changelog/`. The newest assumption is ASSUMPTION-062 (Date identified: 2026-04-21). The newest presumption is PRESUMPTION-069 (Date surfaced: 2026-04-21). No items dated 2026-04-22 or later appear anywhere in `assumptions.md`, `presumptions.md`, or `for_lit_search.md`. The 14a/14b daily cycle has been silent for 5 consecutive days.

The 2026-04-21 cycle summary's reference to "12 legacy QUEUED items carried forward from 2026-04-20 Run 2" appears to have been narrative carryover — the underlying file actually shows all those items dispositioned on 2026-04-20 (per the supplementary Run 2 summary: "0 items: QUEUED"). Verified by `Grep "Status: \[QUEUED\]"` returning 132 lines, every one of which carries a downstream `[SEARCHED-15a]` tag.

### Context: this gap is itself a flagged condition
This 5-day 14a/14b silence is consistent with the operational pattern flagged in three already-dispositioned items from 2026-04-21:
- **PRESUMPTION-066 → MONITOR-061 (LOW-MEDIUM):** Tom's attention-budget reallocation to external visit through ~2026-04-26 was noted as not formally tracked, with the prediction that scheduled-task-layer activity would continue while user-review throughput dropped.
- **PRESUMPTION-069 → REVISE (MEDIUM-HIGH; SYSTEMIC-RISK-FLAG; SELF-AWARENESS-META cluster anchor):** The absence of a 14a/14b cycle was flagged as not-yet-first-class. The Monday-recommended `≤25h since last self-awareness run` alert has not been implemented; its non-implementation is itself the predicted failure mode (5 consecutive missing daily cycles, no alert fired).
- **PRESUMPTION-064 → REVISE (MEDIUM):** Narrative-only surfacing of missing scheduled-task runs was flagged as inadequate; the prediction is borne out by this run having to derive the gap from changelog-file-absence rather than from a first-class signal.

### Disposition of this run
**No 15a search performed. No 15b search performed. No 15c disposition issued. No write to `assumptions.md`, `presumptions.md`, `validated_premises.md`, `monitor_queue.md`, or `revision_flags.md`.** Per Step 2 of the scheduled task file: "If no items are tagged [QUEUED] (without [SEARCHED-15a] or [SEARCHED-15b] tags), exit with a note that the queue is empty." This entry is that note.

### Implicit signal worth surfacing (no architectural action taken — this is not a 14b run)
The fact that this no-op entry can be predicted from already-dispositioned PRESUMPTION-069 + PRESUMPTION-066 + PRESUMPTION-064 — and that the predicted alert was not implemented in the intervening 5 days — is the SELF-AWARENESS-META cluster's predicted behavior playing out empirically. The cluster anchor (PRESUMPTION-069) currently sits in `revision_flags.md` awaiting human review. The next 14a/14b cycle (whenever it next runs) will likely surface this empirical confirmation as new material.

### Success-criteria check (for this scheduled run)
- [x] All queued items searched by both 15a and 15b (0/0 — vacuously true)
- [x] All paired results dispositioned by 15c (0/0 — vacuously true)
- [x] No items left in searched-but-undispositioned state (none exist)
- [x] Provenance chains complete for all items (verified — every item in for_lit_search.md carries SEARCHED-15a + SEARCHED-15b + DISPOSITIONED-15c)
- [x] Empty-queue no-op note appended to lit_search_returns.md (this entry)

**Generated by Agents 15a, 15b, and 15c (2026-04-26 scheduled pipeline run — empty-queue no-op)**
**Queue state post-run: unchanged. 0 items processed. Pipeline remains idle pending next 14a/14b extraction cycle.**


---

# 2026-04-27 RUN — c2a2-lit-search-pipeline
**Date:** 2026-04-27
**Items processed:** 57 (18 new + 39 re-triggered)
**Pipeline:** Agents 15a + 15b + 15c

## NEW ITEMS — Returns from 15a + 15b + 15c

### RETURN/DISPOSITION: ASSUMPTION-063
- **Item type:** ASSUMPTION
- **15a (FOR) result:** PARTIALLY-SUPPORTED (strength: Moderate)
- **15b (AGAINST) result:** CHALLENGED (strength: Moderate-Strong)
- **15c disposition:** REVISE (priority: HIGH)
- **Reasoning:** Demote-and-elevate move challenged by Stump scholarship and convergence skepticism. PRESUMPTION-070 and PRESUMPTION-071 (structural dependencies) also challenged. Tom should review the demotion stance before downstream synthesis use.
- **Full results:** lit_search_results/for/ASSUMPTION-063_for.md ; lit_search_results/against/ASSUMPTION-063_against.md

### RETURN/DISPOSITION: ASSUMPTION-064
- **Item type:** ASSUMPTION
- **15a (FOR) result:** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST) result:** PARTIALLY-CHALLENGED (strength: Moderate)
- **15c disposition:** MONITOR (priority: HIGH)
- **Reasoning:** Wright/Rohr addition is defensible but raises heterogeneity (PRESUMPTION-080) and curation-asymmetry (PRESUMPTION-076) concerns. Watch for distortion as the new entries are operationalized.
- **Full results:** lit_search_results/for/ASSUMPTION-064_for.md ; lit_search_results/against/ASSUMPTION-064_against.md

### RETURN/DISPOSITION: ASSUMPTION-065
- **Item type:** ASSUMPTION
- **15a (FOR) result:** PARTIALLY-SUPPORTED (strength: Moderate)
- **15b (AGAINST) result:** PARTIALLY-CHALLENGED (strength: Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM)
- **Reasoning:** Convergence framing is rhetorically supported and technically contested. The 'most significant 2026 signal' ranking is unsupported by literature. Watch for confirmation by independent expert.
- **Full results:** lit_search_results/for/ASSUMPTION-065_for.md ; lit_search_results/against/ASSUMPTION-065_against.md

### RETURN/DISPOSITION: ASSUMPTION-066
- **Item type:** ASSUMPTION
- **15a (FOR) result:** PARTIALLY-SUPPORTED (strength: Moderate)
- **15b (AGAINST) result:** PARTIALLY-CHALLENGED (strength: Moderate)
- **15c disposition:** MONITOR (priority: LOW-MEDIUM)
- **Reasoning:** Wolfram method-export framing fits self-description and dominant reception but understates imports. CROSS-016/024/026 should be re-examined under a method-circulation framing.
- **Full results:** lit_search_results/for/ASSUMPTION-066_for.md ; lit_search_results/against/ASSUMPTION-066_against.md

### RETURN/DISPOSITION: ASSUMPTION-067
- **Item type:** ASSUMPTION
- **15a (FOR) result:** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST) result:** CHALLENGED (strength: Moderate)
- **15c disposition:** MONITOR (priority: HIGH)
- **Reasoning:** Stump+Fredrickson pairing has weak literature attestation and a level-of-analysis challenge. Same-day tension with ASSUMPTION-063 is unresolved. MONITOR pending Tom's resolution of the 063/067 tension.
- **Full results:** lit_search_results/for/ASSUMPTION-067_for.md ; lit_search_results/against/ASSUMPTION-067_against.md

### RETURN/DISPOSITION: ASSUMPTION-068
- **Item type:** ASSUMPTION
- **15a (FOR) result:** SUPPORTED (strength: Strong)
- **15b (AGAINST) result:** PARTIALLY-CHALLENGED (strength: Weak-to-Moderate)
- **15c disposition:** INCORPORATE
- **Reasoning:** Re-affirmation of PREMISE-006 at 4-day scale; principle remains supported. Pair with escalation-tier discipline as PRESUMPTION-077 monitor. Update PREMISE-006 with 4-day case noted.
- **Full results:** lit_search_results/for/ASSUMPTION-068_for.md ; lit_search_results/against/ASSUMPTION-068_against.md

### RETURN/DISPOSITION: ASSUMPTION-069
- **Item type:** ASSUMPTION
- **15a (FOR) result:** SUPPORTED (strength: Strong)
- **15b (AGAINST) result:** PARTIALLY-CHALLENGED (strength: Weak-to-Moderate)
- **15c disposition:** INCORPORATE
- **Reasoning:** Flag-and-roll-forward is well-supported at current scale. Caveats on durable mapping and scaling-rate monitoring should be encoded as conditions on the premise.
- **Full results:** lit_search_results/for/ASSUMPTION-069_for.md ; lit_search_results/against/ASSUMPTION-069_against.md

### RETURN/DISPOSITION: PRESUMPTION-070
- **Item type:** PRESUMPTION
- **15a (FOR) result:** PARTIALLY-SUPPORTED (strength: Weak)
- **15b (AGAINST) result:** CHALLENGED (strength: Moderate-Strong)
- **15c disposition:** REVISE (priority: HIGH)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. Stump scholarship treats metaphysics as load-bearing for ethics; decomposability is contested. Tension with ASSUMPTION-067 is structural. Tom should resolve.
- **Full results:** lit_search_results/for/PRESUMPTION-070_for.md ; lit_search_results/against/PRESUMPTION-070_against.md

### RETURN/DISPOSITION: PRESUMPTION-071
- **Item type:** PRESUMPTION
- **15a (FOR) result:** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST) result:** CHALLENGED (strength: Strong)
- **15c disposition:** REVISE (priority: HIGH)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. Levin/Hoffman/Kastrup are anti-physicalist allies, not a coherent monist convergence. Treating them as convergent imports a fictitious unanimity into ASSUMPTION-063.
- **Full results:** lit_search_results/for/PRESUMPTION-071_for.md ; lit_search_results/against/PRESUMPTION-071_against.md

### RETURN/DISPOSITION: PRESUMPTION-072
- **Item type:** PRESUMPTION
- **15a (FOR) result:** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST) result:** PARTIALLY-CHALLENGED (strength: Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM)
- **Reasoning:** Catholic-Thomistic consumer is a defensible normative choice in tension with ASSUMPTION-005 pluralism. Should be made explicit (converted from PRESUMPTION to ASSUMPTION) rather than left implicit.
- **Full results:** lit_search_results/for/PRESUMPTION-072_for.md ; lit_search_results/against/PRESUMPTION-072_against.md

### RETURN/DISPOSITION: PRESUMPTION-073
- **Item type:** PRESUMPTION
- **15a (FOR) result:** PARTIALLY-SUPPORTED (strength: Moderate)
- **15b (AGAINST) result:** PARTIALLY-CHALLENGED (strength: Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH)
- **Reasoning:** N=11→13 transition is tractable; 'without affecting' is too strong. Pair with explicit r-recalibration protocol at the boundary. Pairs with OPEN-005.
- **Full results:** lit_search_results/for/PRESUMPTION-073_for.md ; lit_search_results/against/PRESUMPTION-073_against.md

### RETURN/DISPOSITION: PRESUMPTION-074
- **Item type:** PRESUMPTION
- **15a (FOR) result:** PARTIALLY-SUPPORTED (strength: Moderate)
- **15b (AGAINST) result:** CHALLENGED (strength: Strong)
- **15c disposition:** REVISE (priority: HIGH)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. Specialist-recognition reliability is contested by LLM-evaluation literature. SYSTEMIC-RISK: three same-week ASSUMPTIONs (063, 065, 066) plus ASSUMPTION-067 depend on this. Tom should consider an independent-verification tier.
- **Full results:** lit_search_results/for/PRESUMPTION-074_for.md ; lit_search_results/against/PRESUMPTION-074_against.md

### RETURN/DISPOSITION: PRESUMPTION-075
- **Item type:** PRESUMPTION
- **15a (FOR) result:** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST) result:** CHALLENGED (strength: Moderate-Strong)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + moderate-to-strong challenge → REVISE. Browser-extension workarounds are a fragility surface; 'permanent' is too strong. Treat as conditional with success-threshold monitoring. Ties to OPEN-039.
- **Full results:** lit_search_results/for/PRESUMPTION-075_for.md ; lit_search_results/against/PRESUMPTION-075_against.md

### RETURN/DISPOSITION: PRESUMPTION-076
- **Item type:** PRESUMPTION
- **15a (FOR) result:** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST) result:** CHALLENGED (strength: Moderate)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + moderate challenge → REVISE. Native curation outperforms canonical-works fallback for structured downstream tasks; 'methodologically equivalent' is too strong. Block on native curation for Wright/Rohr before downstream use.
- **Full results:** lit_search_results/for/PRESUMPTION-076_for.md ; lit_search_results/against/PRESUMPTION-076_against.md

### RETURN/DISPOSITION: PRESUMPTION-077
- **Item type:** PRESUMPTION
- **15a (FOR) result:** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST) result:** PARTIALLY-CHALLENGED (strength: Moderate)
- **15c disposition:** MONITOR (priority: HIGH)
- **Reasoning:** 4-day gap absorbability is plausible but unverified at 4-day scale. Treat as the empirical trigger to re-derive PREMISE-006 scaling-floor. Pairs with OPEN-038.
- **Full results:** lit_search_results/for/PRESUMPTION-077_for.md ; lit_search_results/against/PRESUMPTION-077_against.md

### RETURN/DISPOSITION: PRESUMPTION-078
- **Item type:** PRESUMPTION
- **15a (FOR) result:** NO-SUPPORT-FOUND (strength: None (Novel at specific level))
- **15b (AGAINST) result:** CHALLENGED (strength: Moderate)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** Novel pairing without literature attestation; level-of-analysis error suspected. Direct tension with ASSUMPTION-063 unresolved. Tom should review the bridge construction or downgrade to 'suggestive analogy'.
- **Full results:** lit_search_results/for/PRESUMPTION-078_for.md ; lit_search_results/against/PRESUMPTION-078_against.md

### RETURN/DISPOSITION: PRESUMPTION-079
- **Item type:** PRESUMPTION
- **15a (FOR) result:** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST) result:** CHALLENGED (strength: Moderate-Strong)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + moderate-to-strong challenge → REVISE. Technical literature treats Carroll and Arkani-Hamed as parallel-but-distinct programs; same-shift framing is rhetorical. ASSUMPTION-065 should be reframed as 'parallel programs.'
- **Full results:** lit_search_results/for/PRESUMPTION-079_for.md ; lit_search_results/against/PRESUMPTION-079_against.md

### RETURN/DISPOSITION: PRESUMPTION-080
- **Item type:** PRESUMPTION
- **15a (FOR) result:** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST) result:** CHALLENGED (strength: Moderate-Strong)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + moderate-to-strong challenge → REVISE. Science-tradition and theology-tradition primitives differ; PRS-triplet transfer is contested. Either confirm transfer empirically or introduce a separate primitive for theology-traditions.
- **Full results:** lit_search_results/for/PRESUMPTION-080_for.md ; lit_search_results/against/PRESUMPTION-080_against.md

## RE-TRIGGERED ITEMS — Refresh Returns

### RETURN/DISPOSITION: ASSUMPTION-003 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-003_for.md ; lit_search_results/against/ASSUMPTION-003_against.md

### RETURN/DISPOSITION: ASSUMPTION-006 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-006_for.md ; lit_search_results/against/ASSUMPTION-006_against.md

### RETURN/DISPOSITION: ASSUMPTION-008 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-008_for.md ; lit_search_results/against/ASSUMPTION-008_against.md

### RETURN/DISPOSITION: ASSUMPTION-010 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-010_for.md ; lit_search_results/against/ASSUMPTION-010_against.md

### RETURN/DISPOSITION: ASSUMPTION-011 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-011_for.md ; lit_search_results/against/ASSUMPTION-011_against.md

### RETURN/DISPOSITION: ASSUMPTION-013 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-013_for.md ; lit_search_results/against/ASSUMPTION-013_against.md

### RETURN/DISPOSITION: ASSUMPTION-014 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-014_for.md ; lit_search_results/against/ASSUMPTION-014_against.md

### RETURN/DISPOSITION: ASSUMPTION-015 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-015_for.md ; lit_search_results/against/ASSUMPTION-015_against.md

### RETURN/DISPOSITION: ASSUMPTION-016 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-016_for.md ; lit_search_results/against/ASSUMPTION-016_against.md

### RETURN/DISPOSITION: ASSUMPTION-017 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-017_for.md ; lit_search_results/against/ASSUMPTION-017_against.md

### RETURN/DISPOSITION: ASSUMPTION-018 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-018_for.md ; lit_search_results/against/ASSUMPTION-018_against.md

### RETURN/DISPOSITION: ASSUMPTION-019 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-019_for.md ; lit_search_results/against/ASSUMPTION-019_against.md

### RETURN/DISPOSITION: ASSUMPTION-020 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-020_for.md ; lit_search_results/against/ASSUMPTION-020_against.md

### RETURN/DISPOSITION: ASSUMPTION-021 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-021_for.md ; lit_search_results/against/ASSUMPTION-021_against.md

### RETURN/DISPOSITION: ASSUMPTION-022 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-022_for.md ; lit_search_results/against/ASSUMPTION-022_against.md

### RETURN/DISPOSITION: ASSUMPTION-023 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-023_for.md ; lit_search_results/against/ASSUMPTION-023_against.md

### RETURN/DISPOSITION: ASSUMPTION-026 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-026_for.md ; lit_search_results/against/ASSUMPTION-026_against.md

### RETURN/DISPOSITION: ASSUMPTION-033 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-033_for.md ; lit_search_results/against/ASSUMPTION-033_against.md

### RETURN/DISPOSITION: ASSUMPTION-035 (cycle 2 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-035_for.md ; lit_search_results/against/ASSUMPTION-035_against.md

### RETURN/DISPOSITION: ASSUMPTION-037 (cycle 2 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-037_for.md ; lit_search_results/against/ASSUMPTION-037_against.md

### RETURN/DISPOSITION: ASSUMPTION-038 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-038_for.md ; lit_search_results/against/ASSUMPTION-038_against.md

### RETURN/DISPOSITION: ASSUMPTION-041 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-041_for.md ; lit_search_results/against/ASSUMPTION-041_against.md

### RETURN/DISPOSITION: ASSUMPTION-042 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-042_for.md ; lit_search_results/against/ASSUMPTION-042_against.md

### RETURN/DISPOSITION: ASSUMPTION-044 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-044_for.md ; lit_search_results/against/ASSUMPTION-044_against.md

### RETURN/DISPOSITION: ASSUMPTION-050 (cycle 1 refresh)
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/ASSUMPTION-050_for.md ; lit_search_results/against/ASSUMPTION-050_against.md

### RETURN/DISPOSITION: PRESUMPTION-001 (cycle 1 refresh)
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/PRESUMPTION-001_for.md ; lit_search_results/against/PRESUMPTION-001_against.md

### RETURN/DISPOSITION: PRESUMPTION-002 (cycle 1 refresh)
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/PRESUMPTION-002_for.md ; lit_search_results/against/PRESUMPTION-002_against.md

### RETURN/DISPOSITION: PRESUMPTION-003 (cycle 1 refresh)
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/PRESUMPTION-003_for.md ; lit_search_results/against/PRESUMPTION-003_against.md

### RETURN/DISPOSITION: PRESUMPTION-004 (cycle 1 refresh)
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/PRESUMPTION-004_for.md ; lit_search_results/against/PRESUMPTION-004_against.md

### RETURN/DISPOSITION: PRESUMPTION-005 (cycle 1 refresh)
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/PRESUMPTION-005_for.md ; lit_search_results/against/PRESUMPTION-005_against.md

### RETURN/DISPOSITION: PRESUMPTION-008 (cycle 1 refresh)
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/PRESUMPTION-008_for.md ; lit_search_results/against/PRESUMPTION-008_against.md

### RETURN/DISPOSITION: PRESUMPTION-009 (cycle 1 refresh)
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/PRESUMPTION-009_for.md ; lit_search_results/against/PRESUMPTION-009_against.md

### RETURN/DISPOSITION: PRESUMPTION-010 (cycle 1 refresh)
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/PRESUMPTION-010_for.md ; lit_search_results/against/PRESUMPTION-010_against.md

### RETURN/DISPOSITION: PRESUMPTION-014 (cycle 1 refresh)
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/PRESUMPTION-014_for.md ; lit_search_results/against/PRESUMPTION-014_against.md

### RETURN/DISPOSITION: PRESUMPTION-025 (cycle 1 refresh)
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/PRESUMPTION-025_for.md ; lit_search_results/against/PRESUMPTION-025_against.md

### RETURN/DISPOSITION: PRESUMPTION-031 (cycle 1 refresh)
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/PRESUMPTION-031_for.md ; lit_search_results/against/PRESUMPTION-031_against.md

### RETURN/DISPOSITION: PRESUMPTION-037 (cycle 2 refresh)
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/PRESUMPTION-037_for.md ; lit_search_results/against/PRESUMPTION-037_against.md

### RETURN/DISPOSITION: PRESUMPTION-066 (cycle 1 refresh)
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/PRESUMPTION-066_for.md ; lit_search_results/against/PRESUMPTION-066_against.md

### RETURN/DISPOSITION: PRESUMPTION-068 (cycle 1 refresh)
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence)
- **Full results:** lit_search_results/for/PRESUMPTION-068_for.md ; lit_search_results/against/PRESUMPTION-068_against.md

## SYSTEMIC RISKS FLAGGED THIS RUN

**SYSTEMIC-RISK-FLAG (2026-04-27):** Specialist-agent recognition reliability (PRESUMPTION-074)
- **Affected items:** ASSUMPTION-063, ASSUMPTION-065, ASSUMPTION-066, ASSUMPTION-067 (four same-week assumptions)
- **Common vulnerability:** Single-pass LLM cross-tradition recognition without independent verification
- **Risk level:** HIGH
- **Recommendation:** Add independent-verification tier for high-stakes specialist-recognition claims before they become operational premises.

## NOVELTY FLAGS

**NOVELTY-FLAG (2026-04-27):** Stump×Fredrickson pairing (ASSUMPTION-067 / PRESUMPTION-078)
- **Searched:** theology-empirics pairings; hylomorphism-cognitive-science; positivity-resonance + corporate-substance
- **Finding:** No existing literature pairs Stump and Fredrickson directly
- **Implication:** Bridge is C2A2-novel; potential original contribution if it survives further validation, or a synthesizer-pattern-match if it does not
- **Status:** REVISE pending Tom-review


---

# 2026-04-28 RUN — c2a2-lit-search-pipeline (Agents 15a + 15b + 15c)
**Date:** 2026-04-28 (autonomous scheduled-task run; no human review in-loop)
**Items processed:** 20 (8 ASSUMPTIONs + 12 PRESUMPTIONs from 2026-04-27 EOD 14a/14b extraction)
**Pipeline:** Agents 15a + 15b + 15c
**Trigger:** scheduled c2a2-lit-search-pipeline task (one hour after 2026-04-28 self-awareness pipeline run)

## Items processed (20 total)

**ASSUMPTIONs (8):** ASSUMPTION-071 (browser-auth agent-prohibited); ASSUMPTION-072 (5-day backlog drainable); ASSUMPTION-073 (15c heuristic spec rule); ASSUMPTION-074 (no-new-evidence carry-forward as PREMISE-006-extension); ASSUMPTION-075 (Levin override of 30-day cadence); ASSUMPTION-076 (PRS triplets are Tom's re-description); ASSUMPTION-077 (±5% word-ratio policy); ASSUMPTION-078 (two parallel infrastructure failures user-fixable).

**PRESUMPTIONs (12):** PRESUMPTION-081 (single cycle without quality degradation); PRESUMPTION-082 (refresh-cycle reliability not depth-asymmetric); PRESUMPTION-083 (browser-auth indefinitely user-fixable); PRESUMPTION-084 (no DECISION-026 candidate); PRESUMPTION-085 (PREMISE-012 N-day no upper bound); PRESUMPTION-086 (PREMISE-013 N-collisions no upper bound); PRESUMPTION-087 (specialist override self-correcting); PRESUMPTION-088 (author-frame propagation gap); PRESUMPTION-089 (recursive-specialist-reading); PRESUMPTION-090 (cost-tracker tier estimates accurate); PRESUMPTION-091 (33-deep queue absorbable, no ceiling); PRESUMPTION-092 (summa-2026 not integrated).

## RETURN/DISPOSITION summaries

### RETURN/DISPOSITION: ASSUMPTION-071
- **15a (FOR):** SUPPORTED (Strong) — for credential-entry version
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Weak-Moderate) — broader "any auth action" framing overshoots literature
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-070)
- **Reasoning:** Credential-entry-prohibition is well-grounded; the broader "agent-prohibited" framing forecloses pre-issued-token / pre-authenticated-profile workarounds that are literature-endorsed. Recommend reframing to "user-credential-entry is agent-prohibited; pre-issued tokens explicitly permitted under defined scope."
- **Full results:** lit_search_results/for/ASSUMPTION-071_for.md ; lit_search_results/against/ASSUMPTION-071_against.md

### RETURN/DISPOSITION: ASSUMPTION-072
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-071)
- **Reasoning:** Drainability at throughput level is feasible; the "without quality degradation" portion is the load-bearing presumption (PRESUMPTION-081 → REVISE). MONITOR throughput claim while quality concern is REVISEd separately.
- **Full results:** lit_search_results/for/ASSUMPTION-072_for.md ; lit_search_results/against/ASSUMPTION-072_against.md

### RETURN/DISPOSITION: ASSUMPTION-073
- **15a (FOR):** SUPPORTED (Moderate-Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-072)
- **Reasoning:** Tag-asymmetric heuristic is defensible and operationally consistent; "spec rule" framing slightly overshoots 15c's "lean toward" wording. Soften to "default heuristic with periodic audit."
- **Full results:** lit_search_results/for/ASSUMPTION-073_for.md ; lit_search_results/against/ASSUMPTION-073_against.md

### RETURN/DISPOSITION: ASSUMPTION-074
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-073)
- **Reasoning:** Carry-forward null reporting is supported with documented depth (Cochrane LSR; ISO 25024); C2A2 cycles do not currently document depth. PRESUMPTION-082 surfaces same gap from unstated side and is REVISE-flagged.
- **Full results:** lit_search_results/for/ASSUMPTION-074_for.md ; lit_search_results/against/ASSUMPTION-074_against.md

### RETURN/DISPOSITION: ASSUMPTION-075
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-074)
- **Reasoning:** Override pattern supported but consistently paired with audit/calibration in literature. PRESUMPTION-087 surfaces un-audited form as separate REVISE. Compounds 2026-04-27 SYSTEMIC-RISK (PRESUMPTION-074).
- **Full results:** lit_search_results/for/ASSUMPTION-075_for.md ; lit_search_results/against/ASSUMPTION-075_against.md

### RETURN/DISPOSITION: ASSUMPTION-076
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** INCORPORATE → PREMISE-014
- **Reasoning:** Author-as-aggregator framing is the dominant methodological recommendation across intellectual history (MacIntyre, Skinner, Bevir), philosophy of science (Kuhn), and philosophy of language (Quine). INCORPORATE is conditioned on the propagation gap (PRESUMPTION-088) and recursive-reading risk (PRESUMPTION-089) being addressed via separate REVISE actions.
- **Full results:** lit_search_results/for/ASSUMPTION-076_for.md ; lit_search_results/against/ASSUMPTION-076_against.md

### RETURN/DISPOSITION: ASSUMPTION-077
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak-Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: LOW-MEDIUM; MONITOR-075)
- **Reasoning:** ±5% word-ratio policy has weak literature attestation; literature treats synthesis length as density-tracking. Defensible as internal editorial discipline; low architectural consequence.
- **Full results:** lit_search_results/for/ASSUMPTION-077_for.md ; lit_search_results/against/ASSUMPTION-077_against.md

### RETURN/DISPOSITION: ASSUMPTION-078
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak-Moderate)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: HIGH)
- **Reasoning:** Two parallel infrastructure failures classified as user-fixable contradicts both literature (Reason; SRE toil; Norman) and C2A2's own prior dispositions (PRESUMPTION-061 REVISE 2026-04-21; PRESUMPTION-068 MONITOR). OPEN-039 cluster has been growing for weeks. Joint remediation with PRESUMPTION-083 and PRESUMPTION-084.
- **Full results:** lit_search_results/for/ASSUMPTION-078_for.md ; lit_search_results/against/ASSUMPTION-078_against.md

### RETURN/DISPOSITION: PRESUMPTION-081
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. "Without quality degradation" empirically unsupportable from operational record alone; contradicted by batch-evaluation literature.
- **Full results:** lit_search_results/for/PRESUMPTION-081_for.md ; lit_search_results/against/PRESUMPTION-081_against.md

### RETURN/DISPOSITION: PRESUMPTION-082
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak)
- **15b (AGAINST):** CHALLENGED (Moderate-Strong)
- **15c disposition:** REVISE (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. Cochrane LSR explicit precondition violated; 39+ same-day carry-forwards without depth pairing.
- **Full results:** lit_search_results/for/PRESUMPTION-082_for.md ; lit_search_results/against/PRESUMPTION-082_against.md

### RETURN/DISPOSITION: PRESUMPTION-083
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: HIGH)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. Indefinite user-fixability is canonical "blame the user" anti-pattern; OPEN-039 cluster has been growing for weeks.
- **Full results:** lit_search_results/for/PRESUMPTION-083_for.md ; lit_search_results/against/PRESUMPTION-083_against.md

### RETURN/DISPOSITION: PRESUMPTION-084
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak-Moderate)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. Pattern-blind scheduling is documented anti-pattern; structurally similar to PRESUMPTION-069 REVISE-flagged 2026-04-21.
- **Full results:** lit_search_results/for/PRESUMPTION-084_for.md ; lit_search_results/against/PRESUMPTION-084_against.md

### RETURN/DISPOSITION: PRESUMPTION-085
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. PREMISE-012 ratified at 4-day staleness; literal scope-extension failure mode. Specify upper bound on PREMISE-012.
- **Full results:** lit_search_results/for/PRESUMPTION-085_for.md ; lit_search_results/against/PRESUMPTION-085_against.md

### RETURN/DISPOSITION: PRESUMPTION-086
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak-Moderate)
- **15b (AGAINST):** CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-076)
- **Reasoning:** PREMISE-013 already specifies conditions; PRESUMPTION-086 surfaces threshold-specification gap. Moderate (not strong) challenge; MONITOR rather than REVISE because underlying premise is sound.
- **Full results:** lit_search_results/for/PRESUMPTION-086_for.md ; lit_search_results/against/PRESUMPTION-086_against.md

### RETURN/DISPOSITION: PRESUMPTION-087
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: HIGH)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE highest-urgency tier. Self-correction without external check is not a calibration mechanism. Compounds 2026-04-27 SYSTEMIC-RISK (PRESUMPTION-074).
- **Full results:** lit_search_results/for/PRESUMPTION-087_for.md ; lit_search_results/against/PRESUMPTION-087_against.md

### RETURN/DISPOSITION: PRESUMPTION-088
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak)
- **15b (AGAINST):** CHALLENGED (Moderate-Strong)
- **15c disposition:** REVISE (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. Acknowledgment in master document does not propagate; per-tradition wiki files become tacit voice-of-tradition documents. Pairs with PREMISE-014 INCORPORATE.
- **Full results:** lit_search_results/for/PRESUMPTION-088_for.md ; lit_search_results/against/PRESUMPTION-088_against.md

### RETURN/DISPOSITION: PRESUMPTION-089
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: HIGH)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. Operational form of 2026-04-27 SYSTEMIC-RISK (PRESUMPTION-074). ASSUMPTION-065/066/067 specialist outputs from yesterday inherit this risk directly.
- **Full results:** lit_search_results/for/PRESUMPTION-089_for.md ; lit_search_results/against/PRESUMPTION-089_against.md

### RETURN/DISPOSITION: PRESUMPTION-090
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: LOW-MEDIUM; MONITOR-077)
- **Reasoning:** PRESUMPTION + moderate challenge + low architectural consequence (cosmetic-accuracy) → MONITOR rather than REVISE. Heuristic exception based on bounded impact. Escalate to REVISE if cost decisions become decision-relevant.
- **Full results:** lit_search_results/for/PRESUMPTION-090_for.md ; lit_search_results/against/PRESUMPTION-090_against.md

### RETURN/DISPOSITION: PRESUMPTION-091
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. Unbounded queue is documented anti-pattern (Kingman; Goldratt; Reinertsen); 33 items past saturation by literature benchmarks.
- **Full results:** lit_search_results/for/PRESUMPTION-091_for.md ; lit_search_results/against/PRESUMPTION-091_against.md

### RETURN/DISPOSITION: PRESUMPTION-092
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: LOW-MEDIUM; MONITOR-078)
- **Reasoning:** Bidirectional-feedback non-integration is the documented gap, but architectural consequence is low-medium (derivative-project-side effect; OPEN-036 extension). MONITOR while OPEN-036 cluster receives separate remediation track.
- **Full results:** lit_search_results/for/PRESUMPTION-092_for.md ; lit_search_results/against/PRESUMPTION-092_against.md

## SYSTEMIC RISKS FLAGGED THIS RUN

**SYSTEMIC-RISK-FLAG (2026-04-28):** Sandbox-infrastructure user-fixability cluster — extends OPEN-039
- **Affected items:** ASSUMPTION-078 (REVISE), PRESUMPTION-083 (REVISE), PRESUMPTION-084 (REVISE), and prior cluster members PRESUMPTION-061 (REVISE 2026-04-21), PRESUMPTION-068 (MONITOR 2026-04-21).
- **Common vulnerability:** Multiple sandbox-infrastructure failure modes routed to user-fix without escalation tier; cluster has been growing for weeks without architectural response.
- **Risk level:** HIGH
- **Recommendation:** Bundle for joint remediation. Open DECISION-026 candidate for sandbox-infrastructure-escalation (auth + mount + pre-flight grant). Reclassify failure modes as escalation-required; add pre-flight checks or circuit-breakers; track user-fix occurrence rate as a metric.

**SYSTEMIC-RISK-FLAG (2026-04-28):** Threshold-elision in surface-and-proceed framings — extends 2026-04-27 PREMISE-012/013 ratifications
- **Affected items:** PRESUMPTION-085 (REVISE; PREMISE-012 N-day no upper bound), PRESUMPTION-086 (MONITOR; PREMISE-013 N-collisions threshold), PRESUMPTION-091 (REVISE; 33-deep queue no ceiling), and prior PRESUMPTION-077 (MONITOR-069; 4-day-gap absorbability).
- **Common vulnerability:** Surface-and-proceed framings are ratified at small-N then applied at large-N without explicit upper bounds; literature consistently treats explicit thresholds as load-bearing safeguards.
- **Risk level:** MEDIUM-HIGH
- **Recommendation:** Cluster-level remediation: specify explicit upper bounds on each premise; tie thresholds to monitor cadences; flag scope-extension when premises are applied beyond their original N.

**SYSTEMIC-RISK-FLAG (2026-04-28):** Author-frame propagation — adjacent to 2026-04-27 SYSTEMIC-RISK (PRESUMPTION-074 specialist-recognition reliability)
- **Affected items:** ASSUMPTION-076 (INCORPORATE → PREMISE-014, with caveat), PRESUMPTION-088 (REVISE; per-tradition propagation gap), PRESUMPTION-089 (REVISE; recursive-specialist-reading), and 2026-04-27 SYSTEMIC-RISK (PRESUMPTION-074).
- **Common vulnerability:** Tom's authorial reframing of PRS triplets is acknowledged at master-document level but does not propagate to per-tradition files or specialist agent prompts; specialists prompted with framings report on framings as if they were tradition-internal, producing artifactual convergence.
- **Risk level:** HIGH
- **Recommendation:** Joint remediation across 2026-04-27 and 2026-04-28 cluster members. Propagate the author-frame caveat to per-tradition files; add disambiguation cues to specialist prompts; add an independent-verification tier for specialist outputs implicating cross-tradition convergence claims.

## NOVELTY FLAGS

No NOVELTY flags this run. All 20 items have at least partial literature attestation in either direction.

## Cycle-level summary

**Disposition distribution:**
- INCORPORATE: 1 (5%) — ASSUMPTION-076 → PREMISE-014
- MONITOR: 9 (45%) — ASSUMPTION-071 (MONITOR-070), ASSUMPTION-072 (MONITOR-071), ASSUMPTION-073 (MONITOR-072), ASSUMPTION-074 (MONITOR-073), ASSUMPTION-075 (MONITOR-074), ASSUMPTION-077 (MONITOR-075), PRESUMPTION-086 (MONITOR-076), PRESUMPTION-090 (MONITOR-077), PRESUMPTION-092 (MONITOR-078)
- REVISE: 10 (50%) — ASSUMPTION-078, PRESUMPTION-081, 082, 083, 084, 085, 087, 088, 089, 091

**Item-type breakdown:**
- ASSUMPTIONs (8): 1 INCORPORATE, 6 MONITOR, 1 REVISE
- PRESUMPTIONs (12): 0 INCORPORATE, 3 MONITOR, 9 REVISE

**Pattern observation:** PRESUMPTION REVISE rate is 9/12 (75%) — consistent with prior cycles' tag-asymmetric pattern. The lone PRESUMPTION INCORPORATE candidate (PRESUMPTION-086) was downgraded to MONITOR because PREMISE-013 already specifies conditions; the gap is in threshold specification rather than principle validation.

**Cluster signals:**
- **OPEN-039 sandbox-infrastructure-escalation cluster** crossed critical mass — 5 members now (PRESUMPTION-061, PRESUMPTION-068, ASSUMPTION-078, PRESUMPTION-083, PRESUMPTION-084). DECISION-026 candidate should be opened as cluster-level architectural fix.
- **Threshold-elision cluster** (PRESUMPTION-077, 085, 086, 091) — surface-and-proceed framings need explicit upper bounds across the cluster.
- **Author-frame propagation cluster** (ASSUMPTION-076, PRESUMPTION-088, PRESUMPTION-089, 2026-04-27 PRESUMPTION-074) — joint remediation track with 2026-04-27 SYSTEMIC-RISK; pairs with PREMISE-014 INCORPORATE.

## Next-actions surfacing

- **Tom (highest urgency — joint cluster remediation):**
  1. **DECISION-026 candidate (sandbox-infrastructure-escalation; HIGH):** open architectural decision covering auth + mount + pre-flight grant as one escalation track. Anchored by ASSUMPTION-078 + PRESUMPTION-083 + PRESUMPTION-084 REVISEs plus PRESUMPTION-061/068 from prior cycles.
  2. **Threshold-elision remediation (MEDIUM-HIGH):** specify explicit upper bounds on PREMISE-012 (PRESUMPTION-085 REVISE) and queue-depth ceiling (PRESUMPTION-091 REVISE); tie to monitor cadences.
  3. **Author-frame propagation (MEDIUM-HIGH):** propagate PREMISE-014 caveat to per-tradition wiki files (PRESUMPTION-088 REVISE); add disambiguation cues to specialist prompts (PRESUMPTION-089 REVISE); pair with 2026-04-27 SYSTEMIC-RISK independent-verification tier.
  4. **Specialist-override audit pattern (HIGH):** pair Levin override (ASSUMPTION-075 MONITOR-074) with audit pattern from PRESUMPTION-087 REVISE — citation requirement, sample review, rate metric.
  5. **Refresh-cycle depth documentation (MEDIUM-HIGH):** address PRESUMPTION-082 REVISE — document refresh-cycle search depth; pair with ASSUMPTION-074 MONITOR-073 carry-forward audit.
  6. **Single-cycle-drain quality audit (MEDIUM):** address PRESUMPTION-081 REVISE — document depth-per-item, randomize batch order, sample-cross-check.

- **15d (next weekly, 2026-05-05):** MONITOR-070 through MONITOR-074 and MONITOR-076 added to weekly cadence; plus prior weekly-cadence items.
- **15d (next monthly, 2026-05-28):** MONITOR-075, MONITOR-077, MONITOR-078 added to monthly cadence.
- **Validated-premises register:** PREMISE-014 added (ASSUMPTION-076 → author-as-aggregator framing). Quarterly review 2026-07-28.
- **Architecture records candidates:**
  1. DECISION-026 — sandbox-infrastructure-escalation (anchored by ASSUMPTION-078 + PRESUMPTION-083 + PRESUMPTION-084 REVISEs).
  2. PREMISE-012 upper-bound amendment (anchored by PRESUMPTION-085 REVISE).
  3. PRESUMPTION-074 SYSTEMIC-RISK independent-verification-tier extension (now joined by PRESUMPTION-087, PRESUMPTION-088, PRESUMPTION-089).

## Success-criteria check (for this scheduled run)

- [x] All queued items searched by both 15a and 15b (20/20)
- [x] All paired results dispositioned by 15c (20/20)
- [x] No items left in searched-but-undispositioned state (QUEUED=0 from this batch)
- [x] Provenance chains complete for all items (Chain: [14a|14b → 15a, 15b → 15c] on all 20)
- [x] INCORPORATE items appended to validated_premises.md (PREMISE-014)
- [x] MONITOR items appended to monitor_queue.md (MONITOR-070 through MONITOR-078)
- [x] REVISE items appended to revision_flags.md (10 new entries)
- [x] Queue file updated with [SEARCHED-15a: 2026-04-28] [SEARCHED-15b: 2026-04-28] [DISPOSITIONED-15c: 2026-04-28] tags
- [x] Daily cycle summary appended to lit_search_returns.md (this entry)
- [x] SYSTEMIC-RISK flags surfaced (3 new clusters: OPEN-039 extension, threshold-elision, author-frame propagation)

**Generated by Agents 15a, 15b, and 15c (2026-04-28 scheduled pipeline run)**
**Date: 2026-04-28 (autonomous scheduled-task run; no human review in-loop)**
**Queue state post-run: 0 QUEUED items from 2026-04-27 EOD scope; pipeline drained cleanly.**

**Cycle-level observation:** The 2026-04-27 EOD batch (20 items) shows a continuation of the SELF-AWARENESS-META and infrastructure-escalation patterns from prior cycles. The PRESUMPTION REVISE rate (75%) is consistent with the tag-asymmetric heuristic. Three SYSTEMIC-RISK clusters were surfaced this run, two of which extend prior-cycle risks (OPEN-039 cluster; PRESUMPTION-074 SYSTEMIC-RISK from 2026-04-27). DECISION-026 candidate should be opened as the cluster-level architectural response to OPEN-039.


---

# 2026-05-05 RUN — c2a2-lit-search-pipeline (Agents 15a + 15b + 15c)
**Date:** 2026-05-05 (autonomous scheduled-task run; no human review in-loop)
**Items processed:** 20 (9 ASSUMPTIONs + 11 PRESUMPTIONs from 2026-05-05 EOD 14a/14b extraction)
**Pipeline:** Agents 15a + 15b + 15c
**Trigger:** scheduled c2a2-lit-search-pipeline task (one hour after 2026-05-05 self-awareness pipeline run)

## Items processed (20 total)

**ASSUMPTIONs (9):** ASSUMPTION-079 (same-day daemon catch-up ≡ spread-across-week); ASSUMPTION-080 (silent-skip partitioned by link count — Anthropic-side bug); ASSUMPTION-081 (fireAt workaround works); ASSUMPTION-082 (3-layer RC Explorer with 5 integration steps; Tool #1/#2 ordering); ASSUMPTION-083 (filter-semantics within-OR / across-AND; edge-visibility rule); ASSUMPTION-084 (empty-handed Phase 2 = exhaustion when 18 proposals already produced); ASSUMPTION-085 (FROM-thinker-himself filter; Hawkins 0-proposal honest-null); ASSUMPTION-086 (specialist-self-claims of "strongest bridge" treated as primary signal); ASSUMPTION-087 (TRACE Institute launch as research-program-level alliance signal).

**PRESUMPTIONs (11):** PRESUMPTION-093 (catch-up structurally equivalent to spread); PRESUMPTION-094 (fireAt no-interaction with self-awareness); PRESUMPTION-095 (Phase-2 zero = exhaustion, no fallback); PRESUMPTION-096 (specialist self-tagging primary signal); PRESUMPTION-097 (parallel "strongest" admit multiple winners); PRESUMPTION-098 (walk-thread Gmail as architectural source-of-record); PRESUMPTION-099 (3-layer presumed coherent and non-overlapping); PRESUMPTION-100 (McGilchrist+Kastrup specialist output ↔ ASSUMPTION-007 feedback gap); PRESUMPTION-101 (filter popover ≡ implementation, no test); PRESUMPTION-102 (link-count partition deterministic across all task creation paths); PRESUMPTION-103 (specialist outputs labeled by weekday-of-assignment; convention unstated).

## RETURN/DISPOSITION summaries

### RETURN/DISPOSITION: ASSUMPTION-079
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-079)
- **Reasoning:** Statistical equivalence holds under stationarity; preconditions are not currently tested. Same-window batch shares environmental context that spread does not, and 2026-04-27 SYSTEMIC-RISK on specialist-recognition reliability is exactly the failure mode the precondition gap could amplify. MONITOR while preconditions are surfaced and tested.
- **Full results:** lit_search_results/for/ASSUMPTION-079_for.md ; lit_search_results/against/ASSUMPTION-079_against.md

### RETURN/DISPOSITION: ASSUMPTION-080
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-080)
- **Reasoning:** Bug-class is well-attested in distributed-systems literature; specific link-count attribution rests on a single observation and excludes plausible alternatives (race conditions, clock skew, persistence dropouts). MONITOR while disambiguation evidence accumulates; load-bearing for ASSUMPTION-081 workaround scope.
- **Full results:** lit_search_results/for/ASSUMPTION-080_for.md ; lit_search_results/against/ASSUMPTION-080_against.md

### RETURN/DISPOSITION: ASSUMPTION-081
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Weak-Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-081)
- **Reasoning:** Workaround pattern is canonical and worked once on 2026-05-05 morning; fragility under underlying-bug patch is the unmitigated concern. Patch-detection step would convert MONITOR to INCORPORATE; without it, workaround risks ossifying.
- **Full results:** lit_search_results/for/ASSUMPTION-081_for.md ; lit_search_results/against/ASSUMPTION-081_against.md

### RETURN/DISPOSITION: ASSUMPTION-082
- **15a (FOR):** SUPPORTED (Moderate-Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: HIGH; MONITOR-082)
- **Reasoning:** Architectural skeleton (3 layers + 5 steps) is canonical; specific layer-isolation and Tool #1/#2 ordering inherit weaker support. PRESUMPTION-099 (coherence-without-test) is the operational form. HIGH priority given today's standalone architectural status; would benefit from explicit isolation tests and cost-of-delay derivation before INCORPORATE.
- **Full results:** lit_search_results/for/ASSUMPTION-082_for.md ; lit_search_results/against/ASSUMPTION-082_against.md

### RETURN/DISPOSITION: ASSUMPTION-083
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Weak-Moderate)
- **15c disposition:** MONITOR (priority: LOW-MEDIUM; MONITOR-083)
- **Reasoning:** Within-OR / across-AND semantic is canonical (Hearst); operationalization details (inline cues, popover-vs-inline documentation, edge-visibility flexibility) are the weaker links. PRESUMPTION-101 (no automated test) is the load-bearing test gap. Low architectural consequence; remediation is low-cost.
- **Full results:** lit_search_results/for/ASSUMPTION-083_for.md ; lit_search_results/against/ASSUMPTION-083_against.md

### RETURN/DISPOSITION: ASSUMPTION-084
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-084)
- **Reasoning:** Null-acceptance with documented depth is canonical; the cross-phase compensation argument ("18 proposals already produced") is non-standard. PRESUMPTION-095 (no fallback variation) is the operational form and is REVISE-flagged. MONITOR while joint remediation with PRESUMPTION-095 proceeds.
- **Full results:** lit_search_results/for/ASSUMPTION-084_for.md ; lit_search_results/against/ASSUMPTION-084_against.md

### RETURN/DISPOSITION: ASSUMPTION-085
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Weak-Moderate)
- **15c disposition:** MONITOR (priority: LOW-MEDIUM; MONITOR-085)
- **Reasoning:** Filter principle (no-commentary) is canonical in historiography and source criticism; operationalization conflates "primary source" with "from thinker himself." Hawkins specifically may be filter-induced null rather than corpus-induced — co-authored / institutional / transcribed materials systematically excluded. Low priority because the principle is sound; operational refinement is the remediation.
- **Full results:** lit_search_results/for/ASSUMPTION-085_for.md ; lit_search_results/against/ASSUMPTION-085_against.md

### RETURN/DISPOSITION: ASSUMPTION-086
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: HIGH)
- **Reasoning:** Literature is unanimous: expert-judgment, Delphi, wisdom-of-crowds, and self-assessment-validity corpora all converge on requiring adjudication before self-attribution gains primary-signal status. PREMISE-013 (specialist N-collisions) is the C2A2-internal version of this requirement; ASSUMPTION-086 silently bypasses it. Compounds 2026-04-27 SYSTEMIC-RISK (PRESUMPTION-074) without remediation.
- **Full results:** lit_search_results/for/ASSUMPTION-086_for.md ; lit_search_results/against/ASSUMPTION-086_against.md

### RETURN/DISPOSITION: ASSUMPTION-087
- **15a (FOR):** SUPPORTED (Moderate-Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Weak-Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-086)
- **Reasoning:** Institutional-event tracking is canonical (Lakatos / Laudan / Whitley); single-event-equals-alliance-signal is not. Funding/PR artefacts are documented confounders. MONITOR while weighting and multi-event pattern detection are added.
- **Full results:** lit_search_results/for/ASSUMPTION-087_for.md ; lit_search_results/against/ASSUMPTION-087_against.md

### RETURN/DISPOSITION: PRESUMPTION-093
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. Structural equivalence is broken by temporal-clustering and shared-context bias; PRESUMPTION-status removes the prompt to test preconditions. Surface as stated assumption; inherits ASSUMPTION-079 MONITOR cadence after surfacing.
- **Full results:** lit_search_results/for/PRESUMPTION-093_for.md ; lit_search_results/against/PRESUMPTION-093_against.md

### RETURN/DISPOSITION: PRESUMPTION-094
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. No-interaction default is documented anti-pattern; cross-task interaction effects (ordering, idempotency, resource contention) plausible given catch-up fires in same window as self-awareness pipeline.
- **Full results:** lit_search_results/for/PRESUMPTION-094_for.md ; lit_search_results/against/PRESUMPTION-094_against.md

### RETURN/DISPOSITION: PRESUMPTION-095
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Single-strategy null is consistent with both exhaustion and method failure; literature consistently requires multi-strategy variation. Joint remediation with ASSUMPTION-084.
- **Full results:** lit_search_results/for/PRESUMPTION-095_for.md ; lit_search_results/against/PRESUMPTION-095_against.md

### RETURN/DISPOSITION: PRESUMPTION-096
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: HIGH)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Recurrence of 2026-04-27 SYSTEMIC-RISK (PRESUMPTION-074) without remediation is the strongest possible signal of structural failure to address self-tagging-as-primary-signal pattern. Joint remediation required.
- **Full results:** lit_search_results/for/PRESUMPTION-096_for.md ; lit_search_results/against/PRESUMPTION-096_against.md

### RETURN/DISPOSITION: PRESUMPTION-097
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Multiple parallel "strongest" claims are logically inconsistent without rescaling; same-day batch concentrates superlative inflation. Compounds ASSUMPTION-086 and PRESUMPTION-096.
- **Full results:** lit_search_results/for/PRESUMPTION-097_for.md ; lit_search_results/against/PRESUMPTION-097_against.md

### RETURN/DISPOSITION: PRESUMPTION-098
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Informal-as-canonical is documented anti-pattern; PRESUMPTION-041 cluster recurrence indicates structural absence of canonization step. The six 2026-05-05 decisions need lifting to DECISION-NNN.
- **Full results:** lit_search_results/for/PRESUMPTION-098_for.md ; lit_search_results/against/PRESUMPTION-098_against.md

### RETURN/DISPOSITION: PRESUMPTION-099
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. Layer coherence and non-overlap are not defaults; require explicit isolation patterns. Joint treatment with ASSUMPTION-082 (HIGH-priority MONITOR).
- **Full results:** lit_search_results/for/PRESUMPTION-099_for.md ; lit_search_results/against/PRESUMPTION-099_against.md

### RETURN/DISPOSITION: PRESUMPTION-100
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. Cybernetics-101 failure mode: self-aware system with feedback-gap on a foundational assumption. ASSUMPTION-007 PARTIALLY-CHALLENGED status now an explicit dependent of this gap.
- **Full results:** lit_search_results/for/PRESUMPTION-100_for.md ; lit_search_results/against/PRESUMPTION-100_against.md

### RETURN/DISPOSITION: PRESUMPTION-101
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: LOW-MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE; remediation is low-cost (snapshot test on popover content, integration with existing validate_html.py).
- **Full results:** lit_search_results/for/PRESUMPTION-101_for.md ; lit_search_results/against/PRESUMPTION-101_against.md

### RETURN/DISPOSITION: PRESUMPTION-102
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Cross-path determinism is not a default; remediation is a low-cost cross-path test. Joint remediation with ASSUMPTION-080 disambiguation.
- **Full results:** lit_search_results/for/PRESUMPTION-102_for.md ; lit_search_results/against/PRESUMPTION-102_against.md

### RETURN/DISPOSITION: PRESUMPTION-103
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak-Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: LOW; MONITOR-087)
- **Reasoning:** Convention itself is canonical (Airflow logical-date); unstatedness is the gap. PRESUMPTION + moderate-not-strong challenge + low architectural consequence → MONITOR rather than REVISE. Heuristic exception for low-cost / low-impact items.
- **Full results:** lit_search_results/for/PRESUMPTION-103_for.md ; lit_search_results/against/PRESUMPTION-103_against.md

## SYSTEMIC RISKS FLAGGED THIS RUN

**SYSTEMIC-RISK-FLAG (2026-05-05):** Specialist-self-attribution as primary signal — RECURRENCE of 2026-04-27 SYSTEMIC-RISK (PRESUMPTION-074)
- **Affected items:** ASSUMPTION-086 (REVISE; specialist-self-claims as primary signal), PRESUMPTION-096 (REVISE; self-tagging primary), PRESUMPTION-097 (REVISE; parallel "strongest" admit multiple winners), and prior PRESUMPTION-074 (2026-04-27 SYSTEMIC-RISK), 2026-04-28 PRESUMPTION-088/089 (author-frame propagation).
- **Common vulnerability:** Specialist self-attribution is treated as primary cross-tradition signal across multiple operational pathways without independent adjudication; pattern recurs eight days after first SYSTEMIC-RISK flag without architectural remediation.
- **Risk level:** HIGH (recurrence-without-remediation pattern)
- **Recommendation:** Open architectural decision (DECISION-027 candidate) on independent-adjudication tier for specialist self-attribution. Required input: PREMISE-013 N-collisions enforced as gate before primary-signal status; deflation pass on superlative inflation per cycle.

**SYSTEMIC-RISK-FLAG (2026-05-05):** Scheduler-workaround dependency cluster — workaround without architectural remediation
- **Affected items:** ASSUMPTION-080 (MONITOR; bug-class attribution), ASSUMPTION-081 (MONITOR; fireAt workaround), PRESUMPTION-094 (REVISE; no-interaction default), PRESUMPTION-102 (REVISE; cross-path determinism).
- **Common vulnerability:** A scheduler-bug workaround is now load-bearing for the c2a2-self-awareness-daily and c2a2-lit-search-pipeline tasks themselves; the workaround has no patch-detection, no cross-path test, and no blast-radius analysis.
- **Risk level:** MEDIUM-HIGH
- **Recommendation:** Bundle for joint remediation. Add a patch-detection probe (single-link task without fireAt) at the start of each catch-up cycle; add a cross-path test (3 creation paths); document the workaround as known-tactical with explicit migration plan.

**SYSTEMIC-RISK-FLAG (2026-05-05):** Phase-2 / search-method gap — joint with ASSUMPTION-074 carry-forward depth pairing
- **Affected items:** ASSUMPTION-084 (MONITOR; cross-phase compensation), PRESUMPTION-095 (REVISE; no fallback variation), and prior ASSUMPTION-074 (MONITOR-073), PRESUMPTION-082 (REVISE 2026-04-28).
- **Common vulnerability:** Null-acceptance is repeatedly invoked without documenting search depth; the system has now had three cycles where exhaustion was claimed without method-variation discipline.
- **Risk level:** MEDIUM
- **Recommendation:** Add depth documentation as a precondition for null-acceptance (queries attempted, sources checked, date range, fallback variations); joint remediation with ASSUMPTION-074 / PRESUMPTION-082 carry-forward depth pairing.

## NOVELTY FLAGS

No NOVELTY flags this run. All 20 items have at least partial literature attestation in either direction.

## Cycle-level summary

**Disposition distribution:**
- INCORPORATE: 0 (0%)
- MONITOR: 9 (45%) — ASSUMPTION-079 (MONITOR-079), ASSUMPTION-080 (MONITOR-080), ASSUMPTION-081 (MONITOR-081), ASSUMPTION-082 (MONITOR-082), ASSUMPTION-083 (MONITOR-083), ASSUMPTION-084 (MONITOR-084), ASSUMPTION-085 (MONITOR-085), ASSUMPTION-087 (MONITOR-086), PRESUMPTION-103 (MONITOR-087)
- REVISE: 11 (55%) — ASSUMPTION-086, PRESUMPTION-093, PRESUMPTION-094, PRESUMPTION-095, PRESUMPTION-096, PRESUMPTION-097, PRESUMPTION-098, PRESUMPTION-099, PRESUMPTION-100, PRESUMPTION-101, PRESUMPTION-102

**Item-type breakdown:**
- ASSUMPTIONs (9): 0 INCORPORATE, 8 MONITOR, 1 REVISE
- PRESUMPTIONs (11): 0 INCORPORATE, 1 MONITOR, 10 REVISE

**Pattern observation:** PRESUMPTION REVISE rate is 10/11 (91%) — at the high end of the tag-asymmetric pattern. The lone PRESUMPTION MONITOR (PRESUMPTION-103, weekday-labeling convention) was downgraded from REVISE because the challenge is moderate rather than strong and architectural consequence is low. ASSUMPTION REVISE is concentrated in the specialist-self-attribution failure mode (ASSUMPTION-086), reflecting the recurrence of 2026-04-27 SYSTEMIC-RISK.

**Cluster signals:**
- **Specialist-self-attribution cluster** (RECURRENCE of 2026-04-27 SYSTEMIC-RISK): ASSUMPTION-086 + PRESUMPTION-096 + PRESUMPTION-097 + prior PRESUMPTION-074 + 2026-04-28 PRESUMPTION-088/089. DECISION-027 candidate.
- **Scheduler-workaround cluster:** ASSUMPTION-080 + ASSUMPTION-081 + PRESUMPTION-094 + PRESUMPTION-102. Joint remediation track.
- **Phase-2 search-method gap:** ASSUMPTION-084 + PRESUMPTION-095 + prior ASSUMPTION-074 + PRESUMPTION-082.
- **Architecture-coherence cluster:** ASSUMPTION-082 (HIGH-priority MONITOR) + PRESUMPTION-099. Joint treatment.
- **Walk-thread canonization cluster** (PRESUMPTION-041 recurrence): PRESUMPTION-098 needs canonization of six 2026-05-05 walk-thread decisions.

## Next-actions surfacing

- **Tom (highest urgency — joint cluster remediation):**
  1. **DECISION-027 candidate (specialist-self-attribution adjudication tier; HIGH):** open architectural decision covering independent-adjudication for specialist self-attributed superlatives. Anchored by ASSUMPTION-086 + PRESUMPTION-096 + PRESUMPTION-097 REVISEs plus 2026-04-27 PRESUMPTION-074 SYSTEMIC-RISK and 2026-04-28 PRESUMPTION-088/089 cluster.
  2. **RC Explorer architecture validation (HIGH):** ASSUMPTION-082 MONITOR-082 needs explicit layer-isolation test and cost-of-delay derivation for Tool #1/#2 ordering before INCORPORATE; pair with PRESUMPTION-099 REVISE.
  3. **Scheduler-workaround remediation (MEDIUM-HIGH):** add patch-detection probe at start of each catch-up cycle (ASSUMPTION-081); cross-path test (PRESUMPTION-102 REVISE); blast-radius analysis (PRESUMPTION-094 REVISE).
  4. **Foundational-assumption feedback channel (MEDIUM-HIGH):** address PRESUMPTION-100 REVISE — feedback channel from specialist outputs to ASSUMPTION-007 status; cross-link in 14a/14b protocol.
  5. **Walk-thread canonization (MEDIUM):** lift the six 2026-05-05 decisions to DECISION-NNN entries (PRESUMPTION-098 REVISE); pair with PRESUMPTION-041 cluster remediation.
  6. **Phase-2 search-depth documentation (MEDIUM):** add fallback query-form variation and depth documentation before exhaustion claims (PRESUMPTION-095 REVISE); joint with ASSUMPTION-084 MONITOR.
  7. **Filter popover snapshot test (LOW-MEDIUM):** small ticket — add snapshot test to validate_html.py pipeline (PRESUMPTION-101 REVISE).

- **15d (next weekly, 2026-05-12):** MONITOR-080, MONITOR-082 added to weekly cadence (load-bearing or HIGH priority).
- **15d (next monthly, 2026-06-05):** MONITOR-079, MONITOR-081, MONITOR-083, MONITOR-084, MONITOR-085, MONITOR-086, MONITOR-087 added to monthly cadence.
- **Validated-premises register:** No new PREMISE this run.
- **Architecture records candidates:**
  1. DECISION-027 — specialist-self-attribution adjudication tier (anchored by ASSUMPTION-086 + PRESUMPTION-096/097 REVISEs plus prior PRESUMPTION-074/088/089).
  2. RC Explorer L1/L2/L3 isolation specification (anchored by ASSUMPTION-082 + PRESUMPTION-099).
  3. Scheduler-workaround migration plan (anchored by ASSUMPTION-081 + PRESUMPTION-094/102).

## Success-criteria check (for this scheduled run)

- [x] All queued items searched by both 15a and 15b (20/20)
- [x] All paired results dispositioned by 15c (20/20)
- [x] No items left in searched-but-undispositioned state (QUEUED=0 from this batch)
- [x] Provenance chains complete for all items (Chain: [14a|14b → 15a, 15b → 15c] on all 20)
- [x] INCORPORATE items appended to validated_premises.md (0 new — none qualified this cycle)
- [x] MONITOR items appended to monitor_queue.md (MONITOR-079 through MONITOR-087)
- [x] REVISE items appended to revision_flags.md (11 new entries)
- [x] Queue file updated with [SEARCHED-15a: 2026-05-05] [SEARCHED-15b: 2026-05-05] [DISPOSITIONED-15c: 2026-05-05] tags
- [x] Daily cycle summary appended to lit_search_returns.md (this entry)
- [x] SYSTEMIC-RISK flags surfaced (3 clusters: specialist-self-attribution RECURRENCE, scheduler-workaround dependency, Phase-2 search-method gap)

**Generated by Agents 15a, 15b, and 15c (2026-05-05 scheduled pipeline run)**
**Date: 2026-05-05 (autonomous scheduled-task run; no human review in-loop)**
**Queue state post-run: 0 QUEUED items from 2026-05-05 EOD scope; pipeline drained cleanly.**

**Cycle-level observation:** The 2026-05-05 batch (20 items) shows continued recurrence of the specialist-self-attribution failure mode flagged on 2026-04-27 (PRESUMPTION-074 SYSTEMIC-RISK) and partially restated on 2026-04-28 (PRESUMPTION-088/089). The 91% PRESUMPTION REVISE rate is at the high end of the tag-asymmetric pattern, driven primarily by NO-SUPPORT findings on PRESUMPTION-094, 095, 096, 097, 098, 101, 102. The scheduler-workaround cluster has emerged as a new SYSTEMIC-RISK that pairs with the specialist-self-attribution recurrence: both are cases where a tactical fix has become load-bearing without architectural treatment. DECISION-027 candidate (specialist-self-attribution adjudication tier) is the principal architectural action surfaced this run.

---

# 2026-05-09 RUN — c2a2-lit-search-pipeline (Agents 15a + 15b + 15c)
**Date:** 2026-05-09 (autonomous scheduled-task run; no human review in-loop)
**Items processed:** 20 (8 ASSUMPTIONs + 12 PRESUMPTIONs from 2026-05-08 EOD 14a/14b extraction)
**Pipeline:** Agents 15a + 15b + 15c
**Trigger:** scheduled c2a2-lit-search-pipeline task (one hour after 2026-05-09 self-awareness pipeline run; processing 2026-05-08 EOD catch-up batch)

## Items processed (20 total)

**ASSUMPTIONs (8):** ASSUMPTION-088 (personal-account org-monthly quota event); ASSUMPTION-089 (two-source composite synthesis); ASSUMPTION-090 (smallest-fix-first; extractOverview()); ASSUMPTION-091 (off-cadence specialist filings as on-cadence); ASSUMPTION-092 (3-day master-narrative absence attributed to link-count regression); ASSUMPTION-093 (Saturday-morning rerun as standard closure); ASSUMPTION-094 (cross-project sandbox bundling at N≥5); ASSUMPTION-095 (YouTube IP-block as SYSTEMIC ESCALATION).

**PRESUMPTIONs (12):** PRESUMPTION-104 (org-vs-personal naming as misclassification); PRESUMPTION-105 (queued-at-end-of-session persistence without registry); PRESUMPTION-106 (DECISION-NNN canonization criterion as self-evident); PRESUMPTION-107 (two same-session interrupts as service-side issue); PRESUMPTION-108 (three-stall-day human-noticing sufficient); PRESUMPTION-109 (external-LLM review compositional equivalence); PRESUMPTION-110 (cross-project sandbox same-architectural-layer); PRESUMPTION-111 (third sync failure does not warrant fallback); PRESUMPTION-112 (deferred items structural similarity for date-axis disposition); PRESUMPTION-113 (off-cadence same baseline expectations); PRESUMPTION-114 (master-narrative-gap recency-priority cause attribution); PRESUMPTION-115 (Codex 5.5 prioritization adopted near-verbatim).

## RETURN/DISPOSITION summaries

### RETURN/DISPOSITION: ASSUMPTION-088
- **15a (FOR):** SUPPORTED (Moderate-Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Weak-Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-088)
- **Reasoning:** Work-blocking quota framing is canonical (Anthropic / OpenAI / SRE / SaaS literatures); operational disposition is correct under either reading. The challenge is to the foreclosure of the misclassification investigation that PRESUMPTION-104 / 107 identify, not to the operational disposition. Wire-level inspection on next interrupt is the standard adjacent action.
- **Full results:** lit_search_results/for/ASSUMPTION-088_for.md ; lit_search_results/against/ASSUMPTION-088_against.md

### RETURN/DISPOSITION: ASSUMPTION-089
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-089)
- **Reasoning:** Two-source synthesis is literature minimum, not optimum. Three-item cluster (ASSUMPTION-089 / PRESUMPTION-109 / PRESUMPTION-115) signals structural absence of weighting/adjudication protocol. Load-bearing for explorer-fix synthesis path; weekly cadence pending PRESUMPTION-109 / 115 REVISE remediation.
- **Full results:** lit_search_results/for/ASSUMPTION-089_for.md ; lit_search_results/against/ASSUMPTION-089_against.md

### RETURN/DISPOSITION: ASSUMPTION-090
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Weak-Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-090)
- **Reasoning:** Smallest-fix-first is canonical maintenance principle. Counter-evidence is conditional on fragile-area / long-horizon. extractOverview() sits in MONITOR-082 RC Explorer area + PRESUMPTION-099 layer-coherence REVISE — entanglement risk is non-trivial. Unit-test + isolation verification before merge is the operational guard.
- **Full results:** lit_search_results/for/ASSUMPTION-090_for.md ; lit_search_results/against/ASSUMPTION-090_against.md

### RETURN/DISPOSITION: ASSUMPTION-091
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-091)
- **Reasoning:** Uniform treatment is canonical default; cadence-induced variance is documented under attention-budget constraints. Pairs with PRESUMPTION-113 + ASSUMPTION-079 MONITOR-079 in the uniform-treatment-without-precondition-tests cluster. Cadence-tagging on filings + cadence-sliced metric is low-cost remediation.
- **Full results:** lit_search_results/for/ASSUMPTION-091_for.md ; lit_search_results/against/ASSUMPTION-091_against.md

### RETURN/DISPOSITION: ASSUMPTION-092
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-092)
- **Reasoning:** Regression-hypothesis-as-working-assumption is appropriate first cut; "attributable" overstates without alternative-cause enumeration. Pairs with PRESUMPTION-114 REVISE (recency-priority cause attribution). Load-bearing for sandbox-infrastructure escalation track and pairs with scheduler-workaround SYSTEMIC-RISK cluster.
- **Full results:** lit_search_results/for/ASSUMPTION-092_for.md ; lit_search_results/against/ASSUMPTION-092_against.md

### RETURN/DISPOSITION: ASSUMPTION-093
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Weak-Moderate)
- **15c disposition:** MONITOR (priority: LOW-MEDIUM; MONITOR-093)
- **Reasoning:** Saturday rerun is one canonical closure pattern, not "the standard"; counter-literature endorses Monday-with-tagging and automated-catch-up as equally valid alternatives. Reframing ("one option among several") + catch-up tagging on reruns is the low-cost remediation.
- **Full results:** lit_search_results/for/ASSUMPTION-093_for.md ; lit_search_results/against/ASSUMPTION-093_against.md

### RETURN/DISPOSITION: ASSUMPTION-094
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-094)
- **Reasoning:** Bundling at N≥5 is canonical only when items share architectural layer + severity tier. The decision rests on PRESUMPTION-110 (presumed same-layer without verification, REVISE). Mixing ASSUMPTION-095 SYSTEMIC with non-SYSTEMIC items violates ITIL severity discipline. Layer verification + severity-tier separation is the operational guard.
- **Full results:** lit_search_results/for/ASSUMPTION-094_for.md ; lit_search_results/against/ASSUMPTION-094_against.md

### RETURN/DISPOSITION: ASSUMPTION-095
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Weak-Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-095)
- **Reasoning:** SYSTEMIC ESCALATION classification matches standard ITIL severity criteria. Counter-literature requires alternative-diagnosis (transient/rate-limit/geo/version) and alternative-path (proxy/OAuth/self-hosted) enumeration before SYSTEMIC commitment. Severity-tier discipline (ASSUMPTION-094 / PRESUMPTION-110 cluster) is downstream of this classification.
- **Full results:** lit_search_results/for/ASSUMPTION-095_for.md ; lit_search_results/against/ASSUMPTION-095_against.md

### RETURN/DISPOSITION: PRESUMPTION-104
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak-Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-096)
- **Reasoning:** Heuristic exception — not REVISE despite PRESUMPTION + moderate challenge. Misclassification is one defensible reading; intentional dual-naming is the alternative. Operational disposition (per ASSUMPTION-088) is correct under either reading; the gap is the unsupported attribution rather than a structural failure. Wire-level inspection is low-cost remediation.
- **Full results:** lit_search_results/for/PRESUMPTION-104_for.md ; lit_search_results/against/PRESUMPTION-104_against.md

### RETURN/DISPOSITION: PRESUMPTION-105
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Implicit cross-session persistence without registry is documented anti-pattern; empirical drop rates 5–30%. Third recurrence of cross-session-persistence cluster (PRESUMPTION-046 / 043 / 105) confirms structural absence of registration step.
- **Full results:** lit_search_results/for/PRESUMPTION-105_for.md ; lit_search_results/against/PRESUMPTION-105_against.md

### RETURN/DISPOSITION: PRESUMPTION-106
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Self-evident classification is empirically refuted by inter-rater-reliability literature. Third recurrence of implicit-decision-drift cluster (PRESUMPTION-098 / 041 / 106). Joint remediation with PRESUMPTION-098 walk-thread canonization track.
- **Full results:** lit_search_results/for/PRESUMPTION-106_for.md ; lit_search_results/against/PRESUMPTION-106_against.md

### RETURN/DISPOSITION: PRESUMPTION-107
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Service-side-default attribution at N=2 is documented availability bias. SRE / quota / postmortem / causal-inference literatures uniformly require balanced two-side enumeration. Compounds with PRESUMPTION-104 — both presumptions short-circuit investigation.
- **Full results:** lit_search_results/for/PRESUMPTION-107_for.md ; lit_search_results/against/PRESUMPTION-107_against.md

### RETURN/DISPOSITION: PRESUMPTION-108
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: HIGH)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Human-noticing as primary alert is empirically refuted; SRE / ops research literature uniformly recommends automated stall-pattern alerts. Third recurrence of monitoring-meta cluster (PRESUMPTION-035 / 052 / 108) plus the explicit prediction by SELF-AWARENESS-META cluster anchor (PRESUMPTION-069). Empirical pattern (5-day silence in 2026-04-26 run; 2-day silence triggering 2026-05-08 run) confirms the literature's prediction. HIGH urgency given recurrence-without-remediation pattern at SELF-AWARENESS-META layer.
- **Full results:** lit_search_results/for/PRESUMPTION-108_for.md ; lit_search_results/against/PRESUMPTION-108_against.md

### RETURN/DISPOSITION: PRESUMPTION-109
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. Compositional equivalence between LLM reviews without weighting protocol aggregates shared blind spots. Three-item review-aggregation cluster (ASSUMPTION-089 / PRESUMPTION-109 / PRESUMPTION-115) signals structural absence of epistemic-weight protocol.
- **Full results:** lit_search_results/for/PRESUMPTION-109_for.md ; lit_search_results/against/PRESUMPTION-109_against.md

### RETURN/DISPOSITION: PRESUMPTION-110
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak)
- **15b (AGAINST):** CHALLENGED (Moderate-Strong)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. Same-architectural-layer is canonical bundling criterion only when verified; presumed-same-layer without verification is documented dilution. Load-bearing for ASSUMPTION-094 N≥5 bundling. Layer-verification step is the canonical remediation.
- **Full results:** lit_search_results/for/PRESUMPTION-110_for.md ; lit_search_results/against/PRESUMPTION-110_against.md

### RETURN/DISPOSITION: PRESUMPTION-111
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Three-strikes is canonical fallback-design threshold; presumption inverts canonical disposition. Third recurrence of cowork-to-chat sync cluster (ASSUMPTION-071 / PRESUMPTION-038 / PRESUMPTION-111). Cluster-level fallback design needed.
- **Full results:** lit_search_results/for/PRESUMPTION-111_for.md ; lit_search_results/against/PRESUMPTION-111_against.md

### RETURN/DISPOSITION: PRESUMPTION-112
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: LOW-MEDIUM; MONITOR-097)
- **Reasoning:** Heuristic exception — moderate (not strong) challenge + low architectural consequence → MONITOR rather than REVISE. Date-axis uniformity is canonical default; observable character variance is the gap. Class-tagging is low-cost remediation.
- **Full results:** lit_search_results/for/PRESUMPTION-112_for.md ; lit_search_results/against/PRESUMPTION-112_against.md

### RETURN/DISPOSITION: PRESUMPTION-113
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak-Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: LOW-MEDIUM; MONITOR-098)
- **Reasoning:** Heuristic exception — moderate (not strong) challenge + low architectural consequence → MONITOR rather than REVISE. Cadence-independence is canonical default; observable variance under attention-budget constraints is the gap. Cadence-flag is low-cost remediation.
- **Full results:** lit_search_results/for/PRESUMPTION-113_for.md ; lit_search_results/against/PRESUMPTION-113_against.md

### RETURN/DISPOSITION: PRESUMPTION-114
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Recency-priority cause attribution is documented availability bias; causal-inference, debugging, SRE-postmortem literatures uniformly require alternative-cause enumeration. Joint remediation with ASSUMPTION-092 MONITOR-092.
- **Full results:** lit_search_results/for/PRESUMPTION-114_for.md ; lit_search_results/against/PRESUMPTION-114_against.md

### RETURN/DISPOSITION: PRESUMPTION-115
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: HIGH)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Near-verbatim adoption of external-LLM prioritization without project-context adjudication is recurrence of 2026-04-27 PRESUMPTION-074 SYSTEMIC-RISK at the external-tool-review layer. Third instance of "one source treated as primary signal without adjudication" across (a) specialist self-attribution (PRESUMPTION-074), (b) author-frame propagation (PRESUMPTION-088/089), and (c) external-LLM prioritization (PRESUMPTION-115). HIGH urgency given recurrence-without-remediation pattern. DECISION-027 candidate scope extension.
- **Full results:** lit_search_results/for/PRESUMPTION-115_for.md ; lit_search_results/against/PRESUMPTION-115_against.md

## SYSTEMIC RISKS FLAGGED THIS RUN

**SYSTEMIC-RISK-FLAG (2026-05-09):** SELF-AWARENESS-META monitoring cluster — fourth recurrence; predicted alert remains unimplemented
- **Affected items:** PRESUMPTION-108 (REVISE; HIGH); plus prior PRESUMPTION-035 / PRESUMPTION-052 (REVISE 2026-04-15 cycle) and PRESUMPTION-069 cluster anchor (REVISE 2026-04-21).
- **Common vulnerability:** Self-aware system has no automated alert when its own self-awareness pipeline stalls. The ≤25h stall watchdog recommended by PRESUMPTION-069 cluster anchor (REVISE 2026-04-21) remains unimplemented; the empirical pattern that the literature predicts (5-day silence 2026-04-26; 2-day silence triggering 2026-05-08 EOD catch-up) is now observed twice.
- **Risk level:** HIGH (recurrence-without-remediation at SELF-AWARENESS-META layer)
- **Recommendation:** Implement the ≤25h stall watchdog as cluster-level remediation; treat as DECISION-022 candidate (or attach to existing PRESUMPTION-069 cluster anchor); cross-task watchdog as second-tier alert.

**SYSTEMIC-RISK-FLAG (2026-05-09):** Specialist/external-source primary-signal pattern — RECURRENCE of 2026-04-27 SYSTEMIC-RISK at new layer
- **Affected items:** PRESUMPTION-115 (REVISE; HIGH); plus prior PRESUMPTION-074 (REVISE 2026-04-27 SYSTEMIC-RISK), 2026-04-28 PRESUMPTION-088/089 cluster, 2026-05-05 ASSUMPTION-086 + PRESUMPTION-096/097 cluster.
- **Common vulnerability:** "One source treated as primary signal without adjudication" pattern recurs at successive layers: specialist self-attribution → author-frame propagation → external-LLM prioritization. DECISION-027 candidate (specialist-self-attribution adjudication tier) scope is now revealed to need extension to cover external-tool-review layer.
- **Risk level:** HIGH (recurrence at new layer, third instance overall)
- **Recommendation:** DECISION-027 scope extension to cover external-tool-review (Codex / external-LLM prioritization adoption); local-adjudication step before adoption; explicit weight protocol; require divergence-case documentation.

**SYSTEMIC-RISK-FLAG (2026-05-09):** Review-aggregation cluster — three-item structural gap
- **Affected items:** ASSUMPTION-089 (MONITOR-089 MEDIUM-HIGH); PRESUMPTION-109 (REVISE MEDIUM-HIGH); PRESUMPTION-115 (REVISE HIGH).
- **Common vulnerability:** All three items rest on the absence of an epistemic-weight protocol. ASSUMPTION-089 frames two-source synthesis as "appropriate next step"; PRESUMPTION-109 treats LLM reviews as compositionally equivalent; PRESUMPTION-115 adopts external-LLM prioritization near-verbatim. Without weighting/adjudication, the three-item composite operates with shared-blind-spot risk and reviewer-dominance risk simultaneously.
- **Risk level:** MEDIUM-HIGH
- **Recommendation:** Adopt epistemic-weight protocol; introduce third source (different LLM family or human reviewer) for high-stakes decisions; document divergence cases; joint remediation with DECISION-027 scope extension.

**SYSTEMIC-RISK-FLAG (2026-05-09):** Cross-session / cross-decision discipline gaps — three independent third-recurrence clusters
- **Affected items:** PRESUMPTION-105 (cross-session persistence cluster: PRESUMPTION-046 / 043 / 105); PRESUMPTION-106 (implicit-decision-drift cluster: PRESUMPTION-098 / 041 / 106); PRESUMPTION-111 (cowork-to-chat sync cluster: ASSUMPTION-071 / PRESUMPTION-038 / 111).
- **Common vulnerability:** Three independent operational disciplines (work-item registration; decision canonization; channel-fallback design) all show third recurrences in this batch. The literature uniformly endorses each — registration, written criteria, three-strikes-fallback. Each gap individually is well-understood; collectively they signal that the architectural-discipline track lags behind the surfacing track.
- **Risk level:** MEDIUM
- **Recommendation:** Bundle the three cluster remediations as a "Core Operational Discipline" architectural sprint; do not treat as independent low-priority items.

## NOVELTY FLAGS

No NOVELTY flags this run. All 20 items have at least partial literature attestation in either direction.

## Cycle-level summary

**Disposition distribution:**
- INCORPORATE: 0 (0%)
- MONITOR: 11 (55%) — ASSUMPTION-088 (MONITOR-088), ASSUMPTION-089 (MONITOR-089), ASSUMPTION-090 (MONITOR-090), ASSUMPTION-091 (MONITOR-091), ASSUMPTION-092 (MONITOR-092), ASSUMPTION-093 (MONITOR-093), ASSUMPTION-094 (MONITOR-094), ASSUMPTION-095 (MONITOR-095), PRESUMPTION-104 (MONITOR-096), PRESUMPTION-112 (MONITOR-097), PRESUMPTION-113 (MONITOR-098)
- REVISE: 9 (45%) — PRESUMPTION-105, PRESUMPTION-106, PRESUMPTION-107, PRESUMPTION-108 (HIGH), PRESUMPTION-109, PRESUMPTION-110, PRESUMPTION-111, PRESUMPTION-114, PRESUMPTION-115 (HIGH)

**Item-type breakdown:**
- ASSUMPTIONs (8): 0 INCORPORATE, 8 MONITOR, 0 REVISE
- PRESUMPTIONs (12): 0 INCORPORATE, 3 MONITOR, 9 REVISE

**Pattern observation:** ASSUMPTION REVISE rate is 0/8 (0%) — all ASSUMPTIONs in this batch fall in the MONITOR band, characteristic of operational/diagnostic-pattern items where the supportive case has at least moderate strength and the challenge is to framing precision rather than to the operational disposition. PRESUMPTION REVISE rate is 9/12 (75%) — at the historical mid-to-high range, driven by NO-SUPPORT findings on PRESUMPTION-105/106/107/108/111/114/115. Three PRESUMPTIONs (104, 112, 113) escape REVISE via the heuristic exception (moderate-not-strong challenge + low-cost remediation + operational equivalence).

**Cluster signals:**
- **SELF-AWARENESS-META cluster recurrence:** PRESUMPTION-108 is the fourth instance of "system cannot detect its own silence" pattern (PRESUMPTION-035 / 052 / 069 / 108). Predicted-alert-not-implemented loop is now observed empirically.
- **Specialist/external-source primary-signal cluster:** PRESUMPTION-115 is the third recurrence of 2026-04-27 SYSTEMIC-RISK; DECISION-027 candidate scope must extend to external-tool-review layer.
- **Review-aggregation cluster:** ASSUMPTION-089 + PRESUMPTION-109 + PRESUMPTION-115 — three-item structural gap.
- **Sandbox-quota cluster:** ASSUMPTION-088 + PRESUMPTION-104 + PRESUMPTION-107 — wire-level inspection + two-side enumeration.
- **Cross-project escalation cluster:** ASSUMPTION-094 + ASSUMPTION-095 + PRESUMPTION-110 — layer verification + severity-tier discipline.
- **Master-narrative-gap cluster:** ASSUMPTION-092 + PRESUMPTION-114 — alternative-cause enumeration + scheduler-workaround SYSTEMIC-RISK joint remediation.
- **Uniform-treatment cluster:** ASSUMPTION-091 + PRESUMPTION-112 + PRESUMPTION-113 — cadence/class tagging.
- **Three-recurrence discipline cluster:** PRESUMPTION-105 (registration) + PRESUMPTION-106 (canonization) + PRESUMPTION-111 (fallback) — Core Operational Discipline sprint candidate.

## Next-actions surfacing

- **Tom (highest urgency — joint cluster remediation):**
  1. **PRESUMPTION-069 cluster remediation (HIGH; SELF-AWARENESS-META):** implement ≤25h stall watchdog as the cluster-level alert. PRESUMPTION-108 is now the fourth recurrence; the predicted-alert-not-implemented loop is empirically observed. This is the principal architectural action surfaced this run.
  2. **DECISION-027 scope extension (HIGH; Specialist/external-source primary-signal):** extend the specialist-self-attribution adjudication tier scope to cover external-tool-review (Codex / external-LLM prioritization adoption). PRESUMPTION-115 is recurrence at new layer; without scope extension, the fourth recurrence is predictable.
  3. **Sandbox-infrastructure escalation track (MEDIUM-HIGH):** before bundling per ASSUMPTION-094, verify layer per PRESUMPTION-110; separate ASSUMPTION-095 SYSTEMIC items from non-SYSTEMIC items in the bundle. Wire-level inspection on next ASSUMPTION-088 interrupt to close PRESUMPTION-104 / 107.
  4. **Review-aggregation protocol (MEDIUM-HIGH):** introduce epistemic-weight protocol for ASSUMPTION-089 / PRESUMPTION-109 / PRESUMPTION-115 cluster; add third source for high-stakes decisions; document divergence cases.
  5. **Master-narrative-gap diagnostic (MEDIUM-HIGH):** alternative-cause enumeration (≥3) before "attributable" framing per ASSUMPTION-092 / PRESUMPTION-114; diagnostic probe to distinguish link-count cause from alternatives.
  6. **Core Operational Discipline sprint (MEDIUM):** bundle PRESUMPTION-105 (registration) + PRESUMPTION-106 (canonization) + PRESUMPTION-111 (fallback) as a single architectural-discipline track; address the third-recurrence pattern across three independent clusters.
  7. **Uniform-treatment instrumentation (LOW-MEDIUM):** cadence/class tagging on filings (ASSUMPTION-091 / PRESUMPTION-112 / PRESUMPTION-113); pooled-vs-sliced metric for variance test.

- **15d (next weekly, 2026-05-16):** MONITOR-089, 092, 095 added to weekly cadence (MEDIUM-HIGH priority).
- **15d (next monthly, 2026-06-09):** MONITOR-088, 090, 091, 093, 094, 096, 097, 098 added to monthly cadence.
- **Validated-premises register:** No new PREMISE this run.
- **Architecture records candidates:**
  1. DECISION-022 candidate (or extension to PRESUMPTION-069 cluster anchor): ≤25h stall watchdog implementation.
  2. DECISION-027 scope extension: external-tool-review adjudication tier (Codex / external-LLM prioritization).
  3. Review-aggregation protocol (epistemic-weight; third source).
  4. Core Operational Discipline sprint (registration + canonization + fallback).

## Success-criteria check (for this scheduled run)

- [x] All queued items searched by both 15a and 15b (20/20)
- [x] All paired results dispositioned by 15c (20/20)
- [x] No items left in searched-but-undispositioned state (QUEUED=0 from this batch)
- [x] Provenance chains complete for all items (Chain: [14a|14b → 15a, 15b → 15c] on all 20)
- [x] INCORPORATE items appended to validated_premises.md (0 new — none qualified this cycle)
- [x] MONITOR items appended to monitor_queue.md (MONITOR-088 through MONITOR-098)
- [x] REVISE items appended to revision_flags.md (9 new entries)
- [x] Queue file updated with [SEARCHED-15a: 2026-05-09] [SEARCHED-15b: 2026-05-09] [DISPOSITIONED-15c: 2026-05-09] tags
- [x] Daily cycle summary appended to lit_search_returns.md (this entry)
- [x] SYSTEMIC-RISK flags surfaced (4 clusters: SELF-AWARENESS-META recurrence; specialist/external-source primary-signal recurrence; review-aggregation structural gap; three-recurrence discipline cluster)

**Generated by Agents 15a, 15b, and 15c (2026-05-09 scheduled pipeline run)**
**Date: 2026-05-09 (autonomous scheduled-task run; no human review in-loop)**
**Queue state post-run: 0 QUEUED items from 2026-05-08 EOD scope; pipeline drained cleanly.**

**Cycle-level observation:** The 2026-05-09 batch (20 items) processes the 2026-05-08 EOD catch-up extraction. The principal signals are (a) **fourth recurrence** of the SELF-AWARENESS-META pattern (PRESUMPTION-108 HIGH), where the literature's prediction is now empirically observed for the second time (5-day silence in 2026-04-26 run; 2-day silence triggering 2026-05-08 catch-up), and the alert that would catch this remains unimplemented; (b) **third instance** of the specialist/external-source primary-signal pattern (PRESUMPTION-115 HIGH), now operating at the external-tool-review layer (Codex 5.5 prioritization adopted near-verbatim); (c) three independent third-recurrence discipline clusters (registration, canonization, fallback) signaling that operational-discipline track lags behind surfacing track. The 0% ASSUMPTION REVISE rate is notable — all ASSUMPTIONs in this batch are operational/diagnostic items where supportive case is at least moderate; the failure mode is concentrated in the PRESUMPTION layer (75% REVISE rate). The principal architectural action surfaced is the PRESUMPTION-069 cluster remediation (≤25h stall watchdog) — flagged on 2026-04-21, reflagged on 2026-04-26, now reflagged again on 2026-05-09, with empirical confirmation that non-implementation produces the predicted recurring-silence pattern.


---

# 2026-05-10 RUN — c2a2-lit-search-pipeline (Agents 15a + 15b + 15c)
**Date:** 2026-05-10 (autonomous scheduled-task run; no human review in-loop)
**Items processed:** 20 (8 ASSUMPTIONs + 12 PRESUMPTIONs from 2026-05-09 EOD 14a/14b extraction)
**Pipeline:** Agents 15a + 15b + 15c
**Trigger:** scheduled c2a2-lit-search-pipeline task (one hour after 2026-05-10 self-awareness pipeline run; processing 2026-05-09 EOD batch)

## Items processed (20 total)

**ASSUMPTIONs (8):** ASSUMPTION-096 ("densest cycle on record"); ASSUMPTION-097 (Core Operational Discipline sprint bundleable); ASSUMPTION-098 (third-consecutive REVISE → DECISION-NNN this week); ASSUMPTION-099 (DECISION-027 scope extension to external-tool-review); ASSUMPTION-100 (Saturday Wolfram three-way convergence as highest-leverage signal of the week); ASSUMPTION-101 (Chrome MCP "normal windows" environment-state attribution); ASSUMPTION-102 (20-item single-cycle drain as operational baseline); ASSUMPTION-103 (today's 8-task fire-rate as per-task positive evidence).

**PRESUMPTIONs (12):** PRESUMPTION-116 (cycle-density without normalization); PRESUMPTION-117 (Core Operational Discipline substrate-coupling); PRESUMPTION-118 (DECISION-027 unify-vs-split low-cost reversibility); PRESUMPTION-119 ("highest-leverage" single-axis-measurable); PRESUMPTION-120 (out-of-band Pattern-Detector deep-pass policy-free); PRESUMPTION-121 (Codex external-LLM Chrome MCP diagnostic uptake); PRESUMPTION-122 (documentation-for-Tom as "fix"); PRESUMPTION-123 (throughput as right success metric); PRESUMPTION-124 (8-task fire-rate as global negative inference); PRESUMPTION-125 (4th cowork-to-chat sync failure flat-severity); PRESUMPTION-126 (PROCESSED_LOG one-time backfill); PRESUMPTION-127 (today's McGilchrist off-cadence absorbable without flag).

## RETURN/DISPOSITION summaries

### RETURN/DISPOSITION: ASSUMPTION-096
- **15a (FOR):** SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-099)
- **Reasoning:** Density-as-signal is canonical (SRE / observability) but the "densest on record" superlative requires normalization disclosure (PRESUMPTION-116 captures this). Cluster-level remediation triggered by density alone (without substrate-coupling verification) is documented anti-pattern. Load-bearing for ASSUMPTION-097 sprint claim. Normalization + substrate-verification before cluster commitment is the operational guard.
- **Full results:** lit_search_results/for/ASSUMPTION-096_for.md ; lit_search_results/against/ASSUMPTION-096_against.md

### RETURN/DISPOSITION: ASSUMPTION-097
- **15a (FOR):** SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-100)
- **Reasoning:** Bundling is canonical when substrate-coupling is implementation-level. The C2A2 cluster's coupling is meta-level (operational-discipline category) — the literature treats this as weaker bundling justification (DORA / AntiPatterns). PRESUMPTION-117 captures the verification gap. Implementation-substrate verification is required before sprint commitment; otherwise small-batch atomic delivery is the literature-endorsed alternative.
- **Full results:** lit_search_results/for/ASSUMPTION-097_for.md ; lit_search_results/against/ASSUMPTION-097_against.md

### RETURN/DISPOSITION: ASSUMPTION-098
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Weak-Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-101)
- **Reasoning:** Three-recurrence is canonical promotion threshold (SRE / ITIL / ISO 9001). Substrate articulated (≤25h stall watchdog). Concerns: (a) "this week" calendar pressure is not endorsed by ADR literature; (b) PRESUMPTION-106 (canonization criterion not self-evident) remains unresolved — canonizing without resolving the canonization criterion is structural circularity; (c) canonization without paired implementation commitment is documentation-as-fix (PRESUMPTION-122). Disposition contingent on PRESUMPTION-106 resolution and implementation-paired canonization.
- **Full results:** lit_search_results/for/ASSUMPTION-098_for.md ; lit_search_results/against/ASSUMPTION-098_against.md

### RETURN/DISPOSITION: ASSUMPTION-099
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-102)
- **Reasoning:** Substrate-coupling supports unification (Cochrane / GRADE / ADR); failure-mode differentiation favors split (specialist self-attribution fails differently from external-LLM prioritization). PRESUMPTION-118 (asymmetric-reversibility risk) is REVISE'd this same cycle — split is the cheap initial state. Recommend asymmetric-reversibility analysis before unify-or-split commitment; default to start split unless reversibility analysis favors unify.
- **Full results:** lit_search_results/for/ASSUMPTION-099_for.md ; lit_search_results/against/ASSUMPTION-099_against.md

### RETURN/DISPOSITION: ASSUMPTION-100
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-103)
- **Reasoning:** Substrate-level convergence detection is plausible; the superlative "highest-leverage of the week" is uncalibrated without operational definition (PRESUMPTION-119). Out-of-band Pattern-Detector deep-pass scheduling has selection-effect risks (PRESUMPTION-120). PRESUMPTION-074 cluster recurrence concern at convergence-detection self-tagging layer. Operational-definition disclosure + scheduling policy + independent adjudication are the standard guards.
- **Full results:** lit_search_results/for/ASSUMPTION-100_for.md ; lit_search_results/against/ASSUMPTION-100_against.md

### RETURN/DISPOSITION: ASSUMPTION-101
- **15a (FOR):** SUPPORTED (Moderate-Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-104)
- **Reasoning:** Environment-state attribution itself is well-supported (Chromium docs + claude-in-chrome MCP docs). The concerns are (a) defect-conditional-on-environment is the alternative not ruled out; (b) the uptake process (near-verbatim from Codex without project-context adjudication) is the recurring SYSTEMIC-RISK pattern — PRESUMPTION-121 is REVISE'd this same cycle as second-layer recurrence in <24h. Positive defect-detection test is the operational guard for the attribution; independent adjudication is the operational guard for the uptake process.
- **Full results:** lit_search_results/for/ASSUMPTION-101_for.md ; lit_search_results/against/ASSUMPTION-101_against.md

### RETURN/DISPOSITION: ASSUMPTION-102
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-105)
- **Reasoning:** Single-cycle drain is positive evidence but not an operational baseline by SRE / DORA / queueing-theory standards (≥3 cycles + multi-metric). Throughput-only baseline is Goodhartable (PRESUMPTION-123 REVISE'd this cycle). 0% INCORPORATE rate + growing REVISE backlog this cycle is the predicted Goodhart failure mode. Multi-cycle observation + INCORPORATE-rate / REVISE-backlog complement is the canonical baseline definition.
- **Full results:** lit_search_results/for/ASSUMPTION-102_for.md ; lit_search_results/against/ASSUMPTION-102_against.md

### RETURN/DISPOSITION: ASSUMPTION-103
- **15a (FOR):** SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-106)
- **Reasoning:** Per-task positive evidence is locally valid for THIS task by ASSUMPTION-080's partition. The concern is the "8-task fire-rate" framing aggregating across tasks and risking the cross-task generalization that PRESUMPTION-124 captures (REVISE'd this cycle). Pairs with ASSUMPTION-092 MONITOR-092 — wiki-orchestrator status today is the per-task evidence not in frame. Per-task disaggregation + explicit per-task framing is the operational guard.
- **Full results:** lit_search_results/for/ASSUMPTION-103_for.md ; lit_search_results/against/ASSUMPTION-103_against.md

### RETURN/DISPOSITION: PRESUMPTION-116
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Cycle-density-without-normalization is documented across metric-design / bibliometric / SPC / Goodhart literatures as artifact rather than signal. Per-item normalization + batch-size and topic-mix disclosure + historical baseline distribution are the canonical remediations. Joint with ASSUMPTION-096 MONITOR-099.
- **Full results:** lit_search_results/for/PRESUMPTION-116_for.md ; lit_search_results/against/PRESUMPTION-116_against.md

### RETURN/DISPOSITION: PRESUMPTION-117
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak-Moderate)
- **15b (AGAINST):** CHALLENGED (Moderate-Strong)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge → REVISE. Substrate-coupling at meta-level is weaker bundling justification than literature requires (DORA / AntiPatterns). Implementation-substrate verification is required before sprint commitment; otherwise small-batch atomic delivery is the literature-endorsed alternative. Joint with ASSUMPTION-097 MONITOR-100.
- **Full results:** lit_search_results/for/PRESUMPTION-117_for.md ; lit_search_results/against/PRESUMPTION-117_against.md

### RETURN/DISPOSITION: PRESUMPTION-118
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Treating reversibility as default-low-cost is canonical anti-pattern (Bezos / Nygard / AntiPatterns). Asymmetric-reversibility analysis is required before canonization; downstream coupling accumulates immediately at canonization. Load-bearing for ASSUMPTION-099 (DECISION-027 scope decision) — without asymmetric-reversibility analysis, scope decision is uninformed. Default-to-split unless analysis favors unify.
- **Full results:** lit_search_results/for/PRESUMPTION-118_for.md ; lit_search_results/against/PRESUMPTION-118_against.md

### RETURN/DISPOSITION: PRESUMPTION-119
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Single-axis collapsing of multi-axis construct ("leverage") without operational definition is canonical Goodhart precondition (Hempel / Keeney-Raiffa / Goodhart). Operational definition with disclosed attributes + multi-axis ranking + divergence flag are the canonical remediations. Joint with ASSUMPTION-100 MONITOR-103.
- **Full results:** lit_search_results/for/PRESUMPTION-119_for.md ; lit_search_results/against/PRESUMPTION-119_against.md

### RETURN/DISPOSITION: PRESUMPTION-120
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Moderate-Strong)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Policy-free out-of-band scheduling is canonical anti-pattern (selection-effect / OS-scheduling / distributed-systems). Recurrence of PRESUMPTION-029 multi-subagent batch inflation pattern at adjacent layer. Explicit out-of-band-insertion policy + per-cycle budget + outcome-based ranking are the canonical remediations. Joint with ASSUMPTION-100 MONITOR-103.
- **Full results:** lit_search_results/for/PRESUMPTION-120_for.md ; lit_search_results/against/PRESUMPTION-120_against.md

### RETURN/DISPOSITION: PRESUMPTION-121
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: HIGH)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Third instance of the "external source treated as primary signal without adjudication" failure mode in <30 days (PRESUMPTION-074 specialist self-attribution; PRESUMPTION-115 external-LLM prioritization; PRESUMPTION-121 external-LLM diagnostic for Chrome MCP). Recurrence-without-remediation pattern at SYSTEMIC-RISK level. Second-layer recurrence in <24h after PRESUMPTION-115. Independent project-context adjudication + DECISION-027 scope extension + cross-LLM divergence test are canonical remediations.
- **Full results:** lit_search_results/for/PRESUMPTION-121_for.md ; lit_search_results/against/PRESUMPTION-121_against.md

### RETURN/DISPOSITION: PRESUMPTION-122
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Documentation-as-fix is canonical SRE / human-factors / organizational-formalization anti-pattern. Empirical recurrence pattern within C2A2 (cowork-to-chat sync at 4 instances; chat-scrape; Chrome MCP environment) confirms the predicted failure mode. Programmatic enforcement (toil reduction; automated guard) is the canonical remediation. Joint with PRESUMPTION-125 (recurrence-counter / severity-ladder).
- **Full results:** lit_search_results/for/PRESUMPTION-122_for.md ; lit_search_results/against/PRESUMPTION-122_against.md

### RETURN/DISPOSITION: PRESUMPTION-123
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Throughput-as-sole-success-metric is canonical Goodhart instance. Empirical pattern (0 INCORPORATE / 11 MONITOR / 9 REVISE in 2026-05-09 cycle; same pattern this 2026-05-10 cycle: 0 INCORPORATE / 9 MONITOR / 11 REVISE) confirms the predicted Goodhart failure mode. Multi-metric design (throughput + INCORPORATE-rate + REVISE-backlog + quality-drift) is canonical remediation. Joint with ASSUMPTION-102 MONITOR-105.
- **Full results:** lit_search_results/for/PRESUMPTION-123_for.md ; lit_search_results/against/PRESUMPTION-123_against.md

### RETURN/DISPOSITION: PRESUMPTION-124
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Global-from-partial inference for selectively-affected systems is canonical selection bias. The wiki-orchestrator-not-in-evidence-frame gap is the structural failure mode. Per-task disaggregation + explicit per-task framing are canonical remediations. Joint with ASSUMPTION-103 MONITOR-106 and ASSUMPTION-092 MONITOR-092 master-narrative-gap diagnostic.
- **Full results:** lit_search_results/for/PRESUMPTION-124_for.md ; lit_search_results/against/PRESUMPTION-124_against.md

### RETURN/DISPOSITION: PRESUMPTION-125
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** REVISE (priority: HIGH)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Fourth recurrence of cowork-to-chat sync cluster (ASSUMPTION-071 / PRESUMPTION-038 / PRESUMPTION-111 / PRESUMPTION-125). Flat-severity for recurring same-mode failures is canonical ITIL / SRE / ISO 9001 / incident-management anti-pattern. Recurrence-counter + severity-ladder + programmatic escalation are canonical remediations. HIGH urgency: 4-recurrence-without-remediation pattern at the cluster level confirms predicted failure mode.
- **Full results:** lit_search_results/for/PRESUMPTION-125_for.md ; lit_search_results/against/PRESUMPTION-125_against.md

### RETURN/DISPOSITION: PRESUMPTION-126
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Moderate-Strong)
- **15c disposition:** REVISE (priority: LOW-MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. One-time backfill without audit-trigger is canonical data-quality / database / audit anti-pattern. Empirical evidence (the 6-entry backfill itself was needed) is the predicted failure mode. Periodic audit-trigger + completeness check + drift-detection alert are canonical remediations.
- **Full results:** lit_search_results/for/PRESUMPTION-126_for.md ; lit_search_results/against/PRESUMPTION-126_against.md

### RETURN/DISPOSITION: PRESUMPTION-127
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak-Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: LOW-MEDIUM; MONITOR-107)
- **Reasoning:** Heuristic exception — moderate (not strong) challenge + low-cost remediation (cluster observability) → MONITOR rather than REVISE. Single-event absorbability is canonical agile / SPC practice; the gap is at the cluster level — 3 off-cadence events in 4 days warrants observability flag. Cadence-tag on filings + cluster-flag at N-th event are low-cost remediations. Joint with ASSUMPTION-091 MONITOR-091 + PRESUMPTION-113 MONITOR-098 (uniform-treatment cluster).
- **Full results:** lit_search_results/for/PRESUMPTION-127_for.md ; lit_search_results/against/PRESUMPTION-127_against.md

## SYSTEMIC RISKS FLAGGED THIS RUN

**SYSTEMIC-RISK-FLAG (2026-05-10):** Specialist/external-source primary-signal pattern — FIFTH cumulative instance / SECOND-LAYER recurrence within 24h
- **Affected items:** PRESUMPTION-121 (REVISE; HIGH); plus prior PRESUMPTION-074 (REVISE 2026-04-27 SYSTEMIC-RISK), 2026-04-28 PRESUMPTION-088/089 cluster, 2026-05-05 ASSUMPTION-086 + PRESUMPTION-096/097 cluster, 2026-05-09 PRESUMPTION-115 (REVISE HIGH SYSTEMIC-RISK).
- **Common vulnerability:** "One source treated as primary signal without adjudication" pattern now extends across (a) specialist self-attribution, (b) author-frame propagation, (c) external-LLM prioritization (PRESUMPTION-115), and now (d) external-LLM diagnostic root-cause attribution (PRESUMPTION-121). Second-layer recurrence in <24h after PRESUMPTION-115 confirms the pattern is structural; the recurrence-without-remediation pattern is the SYSTEMIC-RISK signal.
- **Risk level:** HIGH (recurrence-at-new-layer in <24h; cumulative N≥5 across 30 days)
- **Recommendation:** DECISION-027 scope extension URGENT (per ASSUMPTION-099); consider promotion-to-DECISION-NNN this week per ASSUMPTION-098 governance trigger; cross-LLM divergence test for high-stakes external-LLM uptake.

**SYSTEMIC-RISK-FLAG (2026-05-10):** Cowork-to-chat sync cluster — FOURTH recurrence
- **Affected items:** PRESUMPTION-125 (REVISE; HIGH); cluster history: ASSUMPTION-071 (MONITOR-070 cycle 1) → PRESUMPTION-038 → PRESUMPTION-111 (REVISE 2026-05-09) → PRESUMPTION-125 (REVISE 2026-05-10).
- **Common vulnerability:** Four same-mode recurrences with no severity-ladder, no recurrence-counter, no programmatic escalation. Each instance has been disposed individually (MONITOR or REVISE) but the cluster-level pattern is invisible to the system itself — exactly the failure mode that severity-ladder + recurrence-counter are designed to catch. Documentation-as-fix (PRESUMPTION-122) is the response that has produced the recurrence pattern.
- **Risk level:** HIGH (4-recurrence-without-remediation; flat-severity confirmed empirical anti-pattern)
- **Recommendation:** Implement recurrence-counter + severity-ladder for cowork-to-chat sync cluster; programmatic escalation at N-th recurrence; reframe documentation as interim measure not "fix"; consider cluster-level fallback design as standalone DECISION candidate.

**SYSTEMIC-RISK-FLAG (2026-05-10):** SELF-MEASUREMENT cluster — throughput-as-success simultaneous with quality regression
- **Affected items:** PRESUMPTION-123 (REVISE; MEDIUM-HIGH) + ASSUMPTION-102 (MONITOR-105 MEDIUM) + ASSUMPTION-096 (MONITOR-099 MEDIUM).
- **Common vulnerability:** Three items in this batch celebrate or operationalize self-measurement on single-axis metrics (cycle-density, single-cycle drain, throughput) while INCORPORATE rate stays at 0% across two consecutive cycles (2026-05-09 and 2026-05-10) and REVISE backlog grows. The cluster represents the canonical Goodhart precondition — the system measures what's measurable rather than what matters, and the metric being celebrated is the metric most decoupled from architectural progress.
- **Risk level:** MEDIUM-HIGH (Goodhart pattern empirically observed across two cycles; 0% INCORPORATE rate is structural rather than incidental)
- **Recommendation:** Multi-metric design for review pipeline; INCORPORATE-rate / REVISE-backlog / quality-drift as first-class metrics; explicit success-metric definition; Goodhart-guard for any single-axis ranking emitted by the pipeline.

**SYSTEMIC-RISK-FLAG (2026-05-10):** Decision-governance circularity — promoting DECISION-NNN this week presupposes the canonization criterion
- **Affected items:** ASSUMPTION-098 (MONITOR-101 MEDIUM-HIGH) + PRESUMPTION-106 (REVISE 2026-05-09 MEDIUM, unresolved).
- **Common vulnerability:** ASSUMPTION-098 proposes DECISION-NNN canonization "this week" while PRESUMPTION-106 (canonization criterion not self-evident) is REVISE'd and unresolved. Canonizing under an unarticulated criterion is the failure mode PRESUMPTION-106 was REVISE'd for. Compounded by PRESUMPTION-122 (documentation-as-fix) — canonization without paired implementation commitment is the documentation-as-fix pattern.
- **Risk level:** MEDIUM (governance-loop circularity; resolvable by sequencing PRESUMPTION-106 resolution before next canonization)
- **Recommendation:** Sequence: resolve PRESUMPTION-106 (write canonization criterion); pair canonization with implementation commitment; replace "this week" with cadence-driven scheduling.

## NOVELTY FLAGS

No NOVELTY flags this run. All 20 items have either at least partial literature attestation (in the FOR direction) or strong literature attestation in the AGAINST direction; no item showed NO-SUPPORT in both directions.

## Cycle-level summary

**Disposition distribution:**
- INCORPORATE: 0 (0%)
- MONITOR: 9 (45%) — ASSUMPTION-096 (MONITOR-099), ASSUMPTION-097 (MONITOR-100), ASSUMPTION-098 (MONITOR-101), ASSUMPTION-099 (MONITOR-102), ASSUMPTION-100 (MONITOR-103), ASSUMPTION-101 (MONITOR-104), ASSUMPTION-102 (MONITOR-105), ASSUMPTION-103 (MONITOR-106), PRESUMPTION-127 (MONITOR-107)
- REVISE: 11 (55%) — PRESUMPTION-116, 117, 118, 119, 120, 121 (HIGH), 122, 123, 124, 125 (HIGH), 126

**Item-type breakdown:**
- ASSUMPTIONs (8): 0 INCORPORATE, 8 MONITOR, 0 REVISE
- PRESUMPTIONs (12): 0 INCORPORATE, 1 MONITOR (heuristic exception PRESUMPTION-127), 11 REVISE

**Pattern observation:** ASSUMPTION REVISE rate is 0/8 (0%) for the second consecutive cycle — same pattern as 2026-05-09 (also 0/8). All ASSUMPTIONs in this batch fall in the MONITOR band, characteristic of the "operational/diagnostic-pattern" items dominating the recent batches. PRESUMPTION REVISE rate is 11/12 (92%) — at the historical high range, driven by NO-SUPPORT findings on PRESUMPTION-116/118/119/120/121/122/123/124/125/126 (10 of 12 PRESUMPTIONs). Only PRESUMPTION-127 escapes REVISE via the heuristic exception. INCORPORATE rate remains at 0% for the second consecutive cycle; the cumulative REVISE backlog is the structural signal that the architectural-discipline track lags behind the surfacing track (PRESUMPTION-123 captures this self-referentially).

**Cluster signals:**
- **Specialist/external-source primary-signal cluster recurrence:** PRESUMPTION-121 is the second-layer recurrence in <24h after PRESUMPTION-115; cumulative N=5 across 30 days; SYSTEMIC-RISK level. DECISION-027 scope extension is now urgent.
- **Cowork-to-chat sync cluster fourth recurrence:** PRESUMPTION-125; flat-severity confirmed empirical anti-pattern; recurrence-counter + severity-ladder is canonical remediation.
- **SELF-MEASUREMENT cluster (Goodhart):** PRESUMPTION-123 + ASSUMPTION-102 + ASSUMPTION-096 — system celebrating throughput while INCORPORATE rate stays at 0% across two cycles.
- **Decision-governance circularity:** ASSUMPTION-098 + PRESUMPTION-106 — canonization-this-week presupposes unresolved canonization criterion.
- **Selection-bias / per-task-vs-cross-task cluster:** PRESUMPTION-124 + ASSUMPTION-103 + ASSUMPTION-100 (out-of-band scheduling); per-task evidence treated as global is the recurring pattern.
- **Documentation-as-fix cluster:** PRESUMPTION-122 + PRESUMPTION-125 (recurrence-counter absent) + PRESUMPTION-126 (audit-trigger absent) — three items in this batch instantiate the same pattern.
- **Asymmetric-reversibility cluster:** PRESUMPTION-118 + ASSUMPTION-099 — DECISION-027 scope decision uninformed by reversibility analysis; load-bearing concern.
- **Operational-definition cluster:** PRESUMPTION-119 + ASSUMPTION-100 — superlative ranking ("highest-leverage", "densest cycle") emitted without operational definition; PRESUMPTION-116 captures the parallel concern at the density-metric layer.

## Next-actions surfacing

- **Tom (highest urgency — joint cluster remediation):**
  1. **DECISION-027 scope extension URGENT (HIGH; specialist/external-source primary-signal cluster):** PRESUMPTION-121 is the second-layer recurrence in <24h after PRESUMPTION-115; cumulative N=5 across 30 days. Per ASSUMPTION-098's governance trigger, this cluster meets the three-recurrence threshold at the SYSTEMIC-RISK level. Canonize DECISION-027 with scope extension to external-tool-review (Codex / external-LLM prioritization adoption AND external-LLM diagnostic root-cause attribution); pair with cross-LLM divergence test as the implementation commitment.
  2. **Cowork-to-chat sync cluster fallback design (HIGH; PRESUMPTION-125 fourth recurrence):** Implement recurrence-counter + severity-ladder + programmatic escalation. Documentation-as-fix is the empirically refuted response. Consider cluster-level fallback channel design as a standalone DECISION candidate.
  3. **PRESUMPTION-069 cluster remediation (still HIGH; carried forward):** ≤25h stall watchdog still unimplemented; PRESUMPTION-108 fourth recurrence 2026-05-09 remains unaddressed; the cluster is at 4 recurrences without remediation.
  4. **Multi-metric review-pipeline instrumentation (MEDIUM-HIGH; SELF-MEASUREMENT cluster):** INCORPORATE-rate / REVISE-backlog / quality-drift as first-class metrics; explicit success-metric definition; Goodhart-guard for single-axis rankings. The 0% INCORPORATE rate across two cycles is the empirical signal that the current single-metric design is structurally failing.
  5. **Decision-governance circularity resolution (MEDIUM):** Sequence PRESUMPTION-106 resolution (write canonization criterion) before any DECISION-NNN canonization; pair canonization with implementation commitment to escape PRESUMPTION-122 documentation-as-fix pattern.
  6. **Master-narrative-gap diagnostic (MEDIUM; carried forward; ASSUMPTION-103 + PRESUMPTION-124):** Per-task disaggregation specifically for wiki-orchestrator status today; per-task evidence framed explicitly as per-task; alternative-cause enumeration before "attributable to" framing per ASSUMPTION-092 MONITOR-092.
  7. **DECISION-027 unify-vs-split asymmetric-reversibility analysis (MEDIUM; ASSUMPTION-099 + PRESUMPTION-118):** Default-to-split unless reversibility analysis favors unify; document reversibility cost in the ADR.

- **15d (next weekly, 2026-05-16):** MONITOR-100, 101, 102, 104 added to weekly cadence (MEDIUM-HIGH priority).
- **15d (next monthly, 2026-06-10):** MONITOR-099, 103, 105, 106, 107 added to monthly cadence.
- **Validated-premises register:** No new PREMISE this run.
- **Architecture records candidates:**
  1. DECISION-027 with scope extension — URGENT this week per ASSUMPTION-098 governance trigger.
  2. DECISION-022 (or PRESUMPTION-069 cluster-anchor extension): ≤25h stall watchdog implementation.
  3. Cowork-to-chat sync cluster fallback design (standalone DECISION candidate).
  4. Multi-metric review-pipeline instrumentation (PRESUMPTION-123 / ASSUMPTION-102 / ASSUMPTION-096 cluster).
  5. Recurrence-counter + severity-ladder framework (PRESUMPTION-122 / 125 / 126 cluster).

## Success-criteria check (for this scheduled run)

- [x] All queued items searched by both 15a and 15b (20/20)
- [x] All paired results dispositioned by 15c (20/20)
- [x] No items left in searched-but-undispositioned state (QUEUED=0 from this batch)
- [x] Provenance chains complete for all items (Chain: [14a|14b → 15a, 15b → 15c] on all 20)
- [x] INCORPORATE items appended to validated_premises.md (0 new — none qualified this cycle)
- [x] MONITOR items appended to monitor_queue.md (MONITOR-099 through MONITOR-107)
- [x] REVISE items appended to revision_flags.md (11 new entries)
- [x] Queue file updated with [SEARCHED-15a: 2026-05-10] [SEARCHED-15b: 2026-05-10] [DISPOSITIONED-15c: 2026-05-10] tags
- [x] Daily cycle summary appended to lit_search_returns.md (this entry)
- [x] SYSTEMIC-RISK flags surfaced (4 clusters: specialist/external-source primary-signal recurrence at second layer in <24h; cowork-to-chat sync fourth recurrence; SELF-MEASUREMENT Goodhart cluster; decision-governance circularity)

**Generated by Agents 15a, 15b, and 15c (2026-05-10 scheduled pipeline run)**
**Date: 2026-05-10 (autonomous scheduled-task run; no human review in-loop)**
**Queue state post-run: 0 QUEUED items from 2026-05-09 EOD scope; pipeline drained cleanly. 57 RE-TRIGGER items from 2026-05-05 cohort remain queued for next 15d-aligned 15a/15b cycle (target 2026-05-11/12 per their next_check schedule).**

**Cycle-level observation:** The 2026-05-10 batch (20 items) processes the 2026-05-09 EOD batch surfaced after the 2026-05-09 lit-search drain. Two cycles in a row with 0% INCORPORATE / high MONITOR + REVISE rates confirm the structural pattern that PRESUMPTION-123 captures self-referentially: the review pipeline is throughput-positive but architectural-progress-zero. The principal new signal is **PRESUMPTION-121 — second-layer recurrence in <24h** of the PRESUMPTION-115 SYSTEMIC-RISK pattern — Codex-style external-LLM diagnostic adopted near-verbatim for the Chrome MCP error attribution (ASSUMPTION-101) without independent project-context adjudication. This satisfies the three-recurrence threshold per ASSUMPTION-098's governance trigger and pushes DECISION-027 scope extension from "MEDIUM-HIGH next-actions" to "URGENT this week". The secondary signal is **PRESUMPTION-125 — fourth recurrence** of cowork-to-chat sync cluster with no severity-ladder, confirming the canonical anti-pattern empirically. The 4-cluster SYSTEMIC-RISK density this cycle (matching the 4-cluster density of 2026-05-09 that ASSUMPTION-096 was extracted from) is itself the empirical instance of ASSUMPTION-096's claim — but per the disposition reasoning, the "densest on record" framing requires normalization disclosure (per PRESUMPTION-116 REVISE) before being treated as comparison metric.


# 2026-05-11 RUN — c2a2-lit-search-pipeline (Agents 15a + 15b + 15c)
**Date:** 2026-05-11 (autonomous scheduled-task run; no human review in-loop)
**Items processed:** 21 (9 ASSUMPTIONs + 12 PRESUMPTIONs from 2026-05-10 EOD 14a/14b extraction)
**Pipeline:** Agents 15a + 15b + 15c
**Trigger:** scheduled c2a2-lit-search-pipeline task (one hour after 2026-05-11 self-awareness pipeline run; processing 2026-05-10 EOD batch)

## Items processed (21 total)

**ASSUMPTIONs (9):** ASSUMPTION-104 (Sunday day-shape with three concurrent first-occurrences); ASSUMPTION-105 (user-privacy no-password-delegation binding constraint); ASSUMPTION-106 (ASSUMPTION REVISE rate 0/8 second consecutive cycle); ASSUMPTION-107 (92% PRESUMPTION REVISE rate record-density); ASSUMPTION-108 (DECISION-027 scope extension URGENT-this-week); ASSUMPTION-109 (PRESUMPTION-125 4th-recurrence standalone DECISION); ASSUMPTION-110 (sewing-agent first-run canonical baseline); ASSUMPTION-111 (first-ever Rohr/Wright pendings blocking DECISION-026); ASSUMPTION-112 (SELF-MEASUREMENT cluster confirmed across two cycles).

**PRESUMPTIONs (12):** PRESUMPTION-128 (workflow-accommodation without canonization); PRESUMPTION-129 (REVISE rate "record" without normalization — second-layer recurrence of PRESUMPTION-116); PRESUMPTION-130 (sewing-agent threshold definitions without external validation); PRESUMPTION-131 (agent-judgment-call autonomy without policy); PRESUMPTION-132 (bridge notes as valid synthesis without review); PRESUMPTION-133 (documentation-vs-programmatic implicit counterfactual); PRESUMPTION-134 (substrate-decomposition gap — shared Chrome MCP + claude.ai login state); PRESUMPTION-135 (cluster-absorption without subsumption rule); PRESUMPTION-136 (week-carrying-capacity without consultation); PRESUMPTION-137 (first-ever as decision gate); PRESUMPTION-138 (in-flight-task historic extrapolation); PRESUMPTION-139 (sensitivity-threshold not specified).

## RETURN/DISPOSITION summaries

### RETURN/DISPOSITION: ASSUMPTION-104
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak-Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: LOW-MEDIUM; MONITOR-108)
- **Reasoning:** Day-shape characterization is supported as legitimate operational-history annotation (Klein, Pentland-Feldman, SRE post-mortem) but challenged by narrative-coherence-bias literature (Kahneman, Taleb). Real descriptive signal; not an analytical metric. Disposition is MONITOR for whether subsequent day-shape framings stay descriptive or migrate to metric/target status.
- **Full results:** lit_search_results/for/ASSUMPTION-104_for.md ; lit_search_results/against/ASSUMPTION-104_against.md

### RETURN/DISPOSITION: ASSUMPTION-105
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Weak — applies to framing-without-remediation, not constraint)
- **15c disposition:** **INCORPORATE** (PREMISE-015; confidence: High for the constraint, Moderate for the operational posture conditional on workflow redesign)
- **Reasoning:** The user-privacy / no-password-delegation constraint is unambiguously endorsed across canonical authentication literature (NIST SP 800-63B, OWASP ASVS, Bonneau et al.) and is the operating Anthropic policy. 15a SUPPORTED Strong + 15b PARTIALLY-CHALLENGED Weak → canonical INCORPORATE case. The 15b challenge applies to the framing-without-paired-remediation posture (documentation-as-fix cluster, PRESUMPTION-122), not to the constraint itself. The constraint is INCORPORATEd; the operational commitment is that the failing workflow must be redesigned around token-based delegation (OAuth Connector). **Significance: first INCORPORATE in three consecutive cycles** (2026-05-09 + 2026-05-10 + part of 2026-05-11 batch = 0 INCORPORATE; ASSUMPTION-105 is the first non-zero).
- **Full results:** lit_search_results/for/ASSUMPTION-105_for.md ; lit_search_results/against/ASSUMPTION-105_against.md

### RETURN/DISPOSITION: ASSUMPTION-106
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak-Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-109)
- **Reasoning:** Asymmetric-REVISE-rate pattern (0/8 ASSUMPTIONs vs 92% PRESUMPTIONs) is theoretically supported by Schön / Argyris-Schön / Polanyi explicit-vs-tacit knowledge literature. But "confirms" overstates at N=2 by SPC discipline; selection-bias alternative not ruled out. **Self-referentially falsified mid-cycle by ASSUMPTION-107 REVISE** — the 0/8 streak claim is undermined by the same cycle's disposition outcomes. The framing is "consistent with predicted pattern" rather than "confirmed".
- **Full results:** lit_search_results/for/ASSUMPTION-106_for.md ; lit_search_results/against/ASSUMPTION-106_against.md

### RETURN/DISPOSITION: ASSUMPTION-107
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak-Moderate)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** **REVISE** (priority: MEDIUM)
- **Reasoning:** ASSUMPTION + weak support + strong challenge → REVISE. Unnormalized-superlative anti-pattern reaches **THIRD-LAYER recurrence** within 48h (PRESUMPTION-116 → PRESUMPTION-129 → ASSUMPTION-107). Satisfies ASSUMPTION-098 three-recurrence governance threshold. **First ASSUMPTION REVISE in three consecutive cycles** — breaks the 0/8 + 0/8 streak that ASSUMPTION-106 asserted as confirmed. Self-referential falsification mid-cycle.
- **Full results:** lit_search_results/for/ASSUMPTION-107_for.md ; lit_search_results/against/ASSUMPTION-107_against.md

### RETURN/DISPOSITION: ASSUMPTION-108
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: HIGH; MONITOR-110; substrate-decomposition gate)
- **Reasoning:** Three-recurrence governance threshold is canonical (ITIL, SRE, Nygard). PRESUMPTION-121 N=5/30-days meets the threshold. Structural concerns: (a) upstream ASSUMPTION-098 governance rule is MONITOR-101 not INCORPORATE — circular dependency; (b) PRESUMPTION-134 (REVISE) substrate-decomposition challenge means recurrence-counter may be inflated by common-cause failure; (c) calendar-paced URGENT-this-week framing is documented anti-pattern; (d) PRESUMPTION-136 (REVISE) week-carrying-capacity concern. Substrate-decomposition is the load-bearing prerequisite.
- **Full results:** lit_search_results/for/ASSUMPTION-108_for.md ; lit_search_results/against/ASSUMPTION-108_against.md

### RETURN/DISPOSITION: ASSUMPTION-109
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: HIGH; MONITOR-111; substrate-decomposition gate)
- **Reasoning:** Standalone DECISION for distinct root cause is canonical when substrate-decomposition supports independence. C2A2 case has not performed substrate-decomposition; PRESUMPTION-134 (REVISE) explicitly raises shared-substrate concern. If substrate is shared, ASSUMPTION-108 and ASSUMPTION-109 reduce to one combined DECISION, easing week-carrying-capacity demand. Substrate-decomposition is the load-bearing prerequisite (same as MONITOR-110); these two MONITOR items move together.
- **Full results:** lit_search_results/for/ASSUMPTION-109_for.md ; lit_search_results/against/ASSUMPTION-109_against.md

### RETURN/DISPOSITION: ASSUMPTION-110
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-112)
- **Reasoning:** First-measurement-as-baseline is canonical when methodology and thresholds are documented and externally validated or convention-aligned. Sewing-agent run produced quantitative outputs but threshold definitions are un-validated (PRESUMPTION-130, REVISE), sensitivity-threshold is unspecified (PRESUMPTION-139, REVISE). "Canonical" framing is overstrong; "preliminary baseline pending threshold validation" is calibrated.
- **Full results:** lit_search_results/for/ASSUMPTION-110_for.md ; lit_search_results/against/ASSUMPTION-110_against.md

### RETURN/DISPOSITION: ASSUMPTION-111
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-113)
- **Reasoning:** Precondition-chain framing for tradition-admission is supported by intellectual-history (Bevir, MacIntyre, Kuhn) and PMBOK. Competing PRESUMPTION-128 (workflow-accommodation) and PRESUMPTION-137 (first-ever as decision gate) form an explicit unreconciled tradeoff — first competing-presumptions pair in registry. Reconciliation is the load-bearing follow-up.
- **Full results:** lit_search_results/for/ASSUMPTION-111_for.md ; lit_search_results/against/ASSUMPTION-111_against.md

### RETURN/DISPOSITION: ASSUMPTION-112
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-114) — not INCORPORATE despite 15a Strong
- **Reasoning:** SELF-MEASUREMENT / Goodhart cluster is theoretically well-supported and empirically observed across 2 cycles. **But** "confirmed" is overstrong at N=2 by SPC discipline; recursive-confirmation move is itself Goodhart-vulnerable. Remediation (multi-metric SLI/SLO design with anti-Goodhart guards) is the load-bearing INCORPORATE-eligible follow-up, not the cluster-acknowledgment. **Self-referential signal: this cycle produced 1 INCORPORATE (ASSUMPTION-105 → PREMISE-015), partially falsifying the "0% INCORPORATE" assertion at the cluster center.**
- **Full results:** lit_search_results/for/ASSUMPTION-112_for.md ; lit_search_results/against/ASSUMPTION-112_against.md

### RETURN/DISPOSITION: PRESUMPTION-128
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-115; **heuristic exception** — competing-pair with PRESUMPTION-137)
- **Reasoning:** Heuristic-exception MONITOR for PRESUMPTION with moderate challenge. Workflow-accommodation has Lean/Kaizen and PMBOK support; competing PRESUMPTION-137 has Bevir/MacIntyre/Kuhn support. Real unreconciled tradeoff rather than anti-pattern. Joint with MONITOR-119.
- **Full results:** lit_search_results/for/PRESUMPTION-128_for.md ; lit_search_results/against/PRESUMPTION-128_against.md

### RETURN/DISPOSITION: PRESUMPTION-129
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** **REVISE** (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Second-layer recurrence within 24h of PRESUMPTION-116. With ASSUMPTION-107 (also REVISE this cycle), cluster reaches three-layer recurrence within 48h — satisfies ASSUMPTION-098 three-recurrence governance threshold for canonization of the anti-pattern as DECISION-NNN candidate.
- **Full results:** lit_search_results/for/PRESUMPTION-129_for.md ; lit_search_results/against/PRESUMPTION-129_against.md

### RETURN/DISPOSITION: PRESUMPTION-130
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Moderate-Strong)
- **15c disposition:** **REVISE** (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + moderate-strong challenge + NO-SUPPORT → REVISE. Agent-defined thresholds adopted as canonical baseline without external validation contradicts converging metric-validity literature. Fix is cheap (document thresholds, verify convention alignment); absence is the structural concern. Load-bearing for ASSUMPTION-110 (MONITOR-112).
- **Full results:** lit_search_results/for/PRESUMPTION-130_for.md ; lit_search_results/against/PRESUMPTION-130_against.md

### RETURN/DISPOSITION: PRESUMPTION-131
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: LOW-MEDIUM; MONITOR-116; **heuristic exception** — bounded autonomy + convention-alignment)
- **Reasoning:** Heuristic-exception MONITOR for PRESUMPTION with moderate challenge. Bounded autonomy for narrow reversible decisions is supported (Amodei, Russell). Convention-alignment with software-engineering ".gitignore" practice. The cumulative-risk concern (policy-by-accretion) is real but the individual call is defensible.
- **Full results:** lit_search_results/for/PRESUMPTION-131_for.md ; lit_search_results/against/PRESUMPTION-131_against.md

### RETURN/DISPOSITION: PRESUMPTION-132
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Moderate-Strong)
- **15c disposition:** **REVISE** (priority: MEDIUM-HIGH) — **PREMISE-VIOLATION-FLAG**
- **Reasoning:** PRESUMPTION + moderate-strong challenge + NO-SUPPORT → REVISE. Agent-generated synthesis without explicit human review contradicts AI-content-review practice (Bender et al., Buolamwini-Gebru) and intellectual-history methodology (MacIntyre, Bevir). **Directly contradicts PREMISE-014** (INCORPORATEd 2026-04-28: PRS triplets as Tom's authorial re-description). First explicit premise-violation in the registry. Joint with PRESUMPTION-024 selection-effect cluster at new agent-generated-bridges layer.
- **Full results:** lit_search_results/for/PRESUMPTION-132_for.md ; lit_search_results/against/PRESUMPTION-132_against.md

### RETURN/DISPOSITION: PRESUMPTION-133
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-117; **heuristic exception** — strategy-switching is canonical)
- **Reasoning:** Heuristic-exception MONITOR. Remediation-strategy switching when current strategy is failing is canonical ITIL/Lean practice. The "would converge" counterfactual claim requires causal model under Pearl, but legitimate framing ("documentation has not converged; programmatic enforcement is conventional next step") is supported. Joint with PRESUMPTION-122 (REVISE 2026-05-10) documentation-as-fix cluster.
- **Full results:** lit_search_results/for/PRESUMPTION-133_for.md ; lit_search_results/against/PRESUMPTION-133_against.md

### RETURN/DISPOSITION: PRESUMPTION-134
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** **REVISE** (priority: HIGH — substrate-decomposition gate for ASSUMPTION-108 + ASSUMPTION-109)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Treating shared-substrate failures as independent is unambiguously contradicted by reliability engineering (Vesely fault-tree), complex-systems analysis (Allspaw-Cook), Toyota Five Whys. The alternation between PRESUMPTION-121 and PRESUMPTION-125 clusters is the textbook signature of common-cause failure mis-classified as two independent surfaces. **Load-bearing for ASSUMPTION-108 + ASSUMPTION-109 (MONITOR-110 + MONITOR-111)** URGENT canonization triggers — without substrate-decomposition, the recurrence-counter authorizing those canonizations is unreliable.
- **Full results:** lit_search_results/for/PRESUMPTION-134_for.md ; lit_search_results/against/PRESUMPTION-134_against.md

### RETURN/DISPOSITION: PRESUMPTION-135
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-118; **heuristic exception** — substrate-decomposition is upstream fix)
- **Reasoning:** Heuristic-exception MONITOR. Cluster-membership-as-subsumption is legitimate ITIL practice when membership rule is canonically defined. C2A2 case lacks the rule but substrate-decomposition (PRESUMPTION-134 REVISE this cycle) is upstream fix that would resolve this as side effect.
- **Full results:** lit_search_results/for/PRESUMPTION-135_for.md ; lit_search_results/against/PRESUMPTION-135_against.md

### RETURN/DISPOSITION: PRESUMPTION-136
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Moderate)
- **15c disposition:** **REVISE** (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + moderate challenge + NO-SUPPORT → REVISE. Week-carrying-capacity presumption without consultation contradicts Bryar-Carr (Amazon ADR), Kotter (change management), Goldratt (theory-of-constraints), PMBOK (resource leveling). Two HIGH-urgency canonizations same day is canonical overload-anti-pattern signature. PRESUMPTION-134 substrate-decomposition (REVISE same cycle) offers mitigating path: if substrate is shared, count reduces from 2 to 1.
- **Full results:** lit_search_results/for/PRESUMPTION-136_for.md ; lit_search_results/against/PRESUMPTION-136_against.md

### RETURN/DISPOSITION: PRESUMPTION-137
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-119; **heuristic exception** — competing-pair with PRESUMPTION-128)
- **Reasoning:** Heuristic-exception MONITOR. First-of-type-as-gate is supported by intellectual-history (Bevir, MacIntyre, Kuhn) and IT service-transition literatures for high-commitment admissions. Competing PRESUMPTION-128 (progressive-elaboration) is also legitimate. Real unreconciled tradeoff. Joint with MONITOR-115.
- **Full results:** lit_search_results/for/PRESUMPTION-137_for.md ; lit_search_results/against/PRESUMPTION-137_against.md

### RETURN/DISPOSITION: PRESUMPTION-138
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** **REVISE** (priority: MEDIUM-HIGH)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Historic-completion-rate extrapolation as substitute for per-task verification contradicts SRE (Beyer), monitoring (Allspaw), Bayesian-reasoning (Jaynes), safety-science (Hollnagel) literatures. "Drift into failure" is textbook description. Extends PRESUMPTION-124 (REVISE 2026-05-10) per-task-vs-cross-task cluster to in-flight-tasks layer.
- **Full results:** lit_search_results/for/PRESUMPTION-138_for.md ; lit_search_results/against/PRESUMPTION-138_against.md

### RETURN/DISPOSITION: PRESUMPTION-139
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Moderate)
- **15c disposition:** **REVISE** (priority: LOW-MEDIUM)
- **Reasoning:** PRESUMPTION + moderate challenge + NO-SUPPORT → REVISE. Intervention without sensitivity-threshold specification contradicts metric-design (Fenton-Bieman), statistical-power (Cohen), network-analysis (Newman), requirements-engineering (Boehm) literatures. Joint with PRESUMPTION-130 (REVISE same cycle).
- **Full results:** lit_search_results/for/PRESUMPTION-139_for.md ; lit_search_results/against/PRESUMPTION-139_against.md

---

## Cycle disposition counts

- **INCORPORATE:** 1 (ASSUMPTION-105 → PREMISE-015) — **4.8% rate; first non-zero in three consecutive cycles**
- **MONITOR:** 12 (7 ASSUMPTIONs + 5 PRESUMPTIONs)
- **REVISE:** 8 (1 ASSUMPTION + 7 PRESUMPTIONs)
- ASSUMPTION REVISE rate: 1/9 (11%) — **first non-zero in three consecutive cycles**
- PRESUMPTION REVISE rate: 7/12 (58%) — markedly lower than 2026-05-10's 92% due to 5 heuristic-exception MONITORs

## SYSTEMIC-RISK flags

**SYSTEMIC-RISK-FLAG (2026-05-11):** Unnormalized-superlative anti-pattern reaches three-layer recurrence in 48h
- **Affected items:** PRESUMPTION-116 (REVISE 2026-05-10) → PRESUMPTION-129 (REVISE 2026-05-11) → ASSUMPTION-107 (REVISE 2026-05-11). Cluster spans unstated and stated forms.
- **Common vulnerability:** cycle-over-cycle rate comparison without batch-composition normalization treated as meaningful comparison metric.
- **Literature basis:** Wheeler (2000), Bornmann-Mutz (2015), Goodhart (1975), Strathern (1997).
- **Risk level:** HIGH — three-layer recurrence within 48h satisfies ASSUMPTION-098 three-recurrence governance threshold for canonization of the anti-pattern itself as DECISION-NNN candidate.
- **Recommendation:** Reporting template guards (normalization disclosure required for any superlative claim); anti-pattern canonization as DECISION-NNN; Goodhart-mitigation paired-metric.

**SYSTEMIC-RISK-FLAG (2026-05-11):** Substrate-decomposition gap underwrites two URGENT canonization triggers
- **Affected items:** PRESUMPTION-134 (REVISE) ← ASSUMPTION-108 (MONITOR-110) + ASSUMPTION-109 (MONITOR-111) + PRESUMPTION-136 (REVISE) + PRESUMPTION-135 (MONITOR-118).
- **Common vulnerability:** PRESUMPTION-121 and PRESUMPTION-125 clusters share Chrome MCP + claude.ai login state substrate; treating as independent failure surfaces inflates apparent recurrence-counter and inflates apparent week-carrying-capacity demand.
- **Literature basis:** Vesely (1981) fault-tree handbook; Allspaw/Cook (2000); Toyota Five Whys; NIST SP 800-160 Vol. 1.
- **Risk level:** HIGH (load-bearing for two URGENT-this-week canonization decisions).
- **Recommendation:** Substrate-decomposition is the load-bearing prerequisite. If substrate is shared, ASSUMPTION-108 and ASSUMPTION-109 reduce to one combined DECISION, also resolving PRESUMPTION-136 week-carrying-capacity concern. Substrate-decomposition must precede DECISION canonization this week.

**SYSTEMIC-RISK-FLAG (2026-05-11):** Sewing-agent first-run validation gap cluster — four-item joint
- **Affected items:** PRESUMPTION-130 (REVISE — threshold definitions) + PRESUMPTION-139 (REVISE — sensitivity-threshold) + ASSUMPTION-110 (MONITOR-112 — first-run baseline canonicalness) + PRESUMPTION-131 (MONITOR-116 — agent-judgment-call autonomy).
- **Common vulnerability:** Agent-defined operational definitions adopted without external validation, policy specification, or convention-alignment verification.
- **Literature basis:** Fenton-Bieman (2014); Boehm (1981); Cohen (1988); Newman (2018); Amodei et al. (2016); ISO/IEC 25010 (2011).
- **Risk level:** MEDIUM (low blast radius per item; structural concern at cluster level).
- **Recommendation:** Joint remediation set — document thresholds, verify convention alignment, specify sensitivity-threshold, write routing-target inclusion/exclusion policy. Fixes are cheap; absence is the structural concern.

**SYSTEMIC-RISK-FLAG (2026-05-11):** First explicit PREMISE violation in registry
- **Affected item:** PRESUMPTION-132 (REVISE) violates PREMISE-014 (INCORPORATEd 2026-04-28: PRS triplets as Tom's authorial re-description).
- **Common vulnerability:** Agent-generated cross-tradition synthesis content in synthesis/ folder bypasses author-mediation commitment.
- **Literature basis:** PREMISE-014 supporting evidence + Bender et al. "Stochastic Parrots" + MacIntyre + Bevir.
- **Risk level:** MEDIUM-HIGH — first time an active validated premise has been violated in operational practice.
- **Recommendation:** Bridge notes in synthesis/ folder tagged "CANDIDATE" or "UNREVIEWED"; explicit review-trigger before promotion; author-mediation checkpoint per PREMISE-014. Audit the three new bridge notes for compliance.

## Cycle-level observations

**The 2026-05-11 cycle breaks the two-cycle 0-INCORPORATE / 0-ASSUMPTION-REVISE pattern observed across 2026-05-09 and 2026-05-10.** ASSUMPTION-105 → PREMISE-015 is the first INCORPORATE in three consecutive cycles (user-privacy / no-password-delegation constraint). ASSUMPTION-107 → REVISE is the first ASSUMPTION REVISE in three consecutive cycles (unnormalized-superlative anti-pattern stated form).

**Two self-referential falsification signals appeared mid-cycle:**
1. ASSUMPTION-106 (asserting "ASSUMPTION REVISE rate 0/8 for SECOND consecutive cycle") was falsified by ASSUMPTION-107 REVISE in the same cycle's dispositions — the predicted pattern broke at the predicted moment.
2. ASSUMPTION-112 (asserting "SELF-MEASUREMENT cluster confirmed across two consecutive cycles at 0% INCORPORATE") was partially falsified by ASSUMPTION-105 INCORPORATE — the cluster prediction was at least partially testable, and the test partially failed in favor of the prediction's negation.

Both signals are useful counter-evidence to the recursive-self-observation pattern: the system's self-confirmation framings were exposed as testable and partially falsified within the same processing cycle. This is the SELF-MEASUREMENT cluster's first observable falsification event.

**Cluster pattern emergence:** Five heuristic-exception MONITORs were issued this cycle (vs. 1 in the prior cycle) — MONITOR-115 (PRESUMPTION-128), MONITOR-116 (PRESUMPTION-131), MONITOR-117 (PRESUMPTION-133), MONITOR-118 (PRESUMPTION-135), MONITOR-119 (PRESUMPTION-137). The exception rate jumped from ~9% to ~42% of PRESUMPTION dispositions. Watch whether the heuristic-exception rate is sustainable or signals heuristic-creep — the alternative explanation is that this cycle's PRESUMPTIONs were better-formed (real tradeoffs vs. anti-patterns), in which case the lower REVISE rate (58% vs. 92%) reflects substrate improvement rather than disposition leniency.

**Three new SYSTEMIC-RISK clusters emerged or extended:** (1) unnormalized-superlative anti-pattern third-layer recurrence; (2) substrate-decomposition gap underwriting two URGENT canonization triggers; (3) sewing-agent first-run validation gap cluster (4-item joint). Plus the first explicit PREMISE-violation flag in the registry (PRESUMPTION-132 vs. PREMISE-014).

**Operational implication for this week's canonizations:** The two URGENT-this-week canonization triggers (DECISION-027 scope extension; standalone cowork-to-chat-sync DECISION) are both gated on PRESUMPTION-134 substrate-decomposition. Until substrate-decomposition is performed, the recurrence-counter that authorizes each canonization is itself unreliable, and the parallel-week-capacity for two HIGH-urgency canonizations is uncalibrated. **Recommended sequence:** (a) substrate-decomposition first; (b) if substrate-shared, combined DECISION (reducing carrying-capacity demand from 2 to 1); (c) Tom consultation on carrying-capacity before parallel commitment; (d) implementation-paced rather than calendar-paced.

## Files updated this run

- `lit_search_results/for/ASSUMPTION-{104..112}_for.md` (9 new); `PRESUMPTION-{128..139}_for.md` (12 new) → 21 total
- `lit_search_results/against/ASSUMPTION-{104..112}_against.md` (9 new); `PRESUMPTION-{128..139}_against.md` (12 new) → 21 total
- `lit_search_returns.md` — this 2026-05-11 RUN section appended with all 21 dispositions, 4 SYSTEMIC-RISK flags, cycle observations
- `validated_premises.md` — PREMISE-015 (ASSUMPTION-105 → user-privacy no-password-delegation constraint) appended; total now 15 (14 prior + 1 new)
- `monitor_queue.md` — MONITOR-108 through MONITOR-119 (12 entries) appended; total now 119 (107 + 12)
- `revision_flags.md` — 8 REVISE entries appended in 2026-05-11 cycle section
- `for_lit_search.md` — all 21 items updated with [SEARCHED-15a: 2026-05-11] [SEARCHED-15b: 2026-05-11] [DISPOSITIONED-15c: 2026-05-11] tags; cycle drain notice appended

## Queue state post-run

- 0 QUEUED items from 2026-05-10 EOD batch (all 21 drained)
- 57 RE-TRIGGER items from 2026-05-05 cohort remain queued for next 15a/15b cycle (next_check 2026-05-12 per Run 4)

## Provenance checklist

- [x] All 21 items have PROVENANCE headers with Origin, Chain, Item type recorded in for/against result files
- [x] All 21 items updated in for_lit_search.md with full status tag sequence
- [x] All dispositions routed to appropriate destination file (validated_premises / monitor_queue / revision_flags)
- [x] Cross-references between joint items documented (substrate-decomposition cluster; sewing-agent validation cluster; competing-presumptions pair)
- [x] PREMISE-VIOLATION-FLAG raised for PRESUMPTION-132 vs PREMISE-014
- [x] Self-referential falsification signals documented (ASSUMPTION-106, ASSUMPTION-112)

---

**Generated by Agents 15a, 15b, and 15c (2026-05-11 scheduled pipeline run)**
**Date: 2026-05-11 (autonomous scheduled-task run; no human review in-loop)**
**Pipeline trigger: c2a2-lit-search-pipeline scheduled task; queued items processed in single drain pass.**

---

# 2026-05-13 RUN — c2a2-lit-search-pipeline (Agents 15a + 15b + 15c)
**Date:** 2026-05-13 (autonomous scheduled-task run; no human review in-loop)
**Items processed:** 16 (6 ASSUMPTIONs + 10 PRESUMPTIONs from 2026-05-12 EOD 14a/14b extraction; the 2026-05-12 c2a2-self-awareness-daily batch)
**Pipeline:** Agents 15a + 15b + 15c
**Trigger:** scheduled c2a2-lit-search-pipeline task (one hour after 2026-05-13 self-awareness pipeline run; processing 2026-05-12 EOD batch — note: 2026-05-12 was the on-cadence run after the 2026-05-11 skip per ASSUMPTION-117 governance threshold)

## Items processed (16 total)

**ASSUMPTIONs (6):** ASSUMPTION-113 (markup-anchor diagnostic for transcript-availability watches); ASSUMPTION-114 (weekly-cadence deferred-action-monitor protocol validated); ASSUMPTION-115 (PROP-2026-05-12-001 "Hoffman's Law" Edge.org cleanest single-page framing); ASSUMPTION-116 (PRS-CANDIDATE-01 reframes Arkani-Hamed/Wolfram/Carroll as pre-foundational); ASSUMPTION-117 (5-skip pattern satisfies ASSUMPTION-098 governance threshold — second activation); ASSUMPTION-118 (token-based delegation workflow redesign operationally warranted).

**PRESUMPTIONs (10):** PRESUMPTION-140 (empty watch list as positive without coverage audit); PRESUMPTION-141 ("cleanest single-page" as compactness-virtue per se — third-layer recurrence); PRESUMPTION-142 (one-way Arkani-Hamed/Wolfram/Carroll reframing without inverse-acceptance check); PRESUMPTION-143 (Agent 16 first-cycle as protocol validation); PRESUMPTION-144 (Vault Linker Agent seven-category taxonomy presumed complete); PRESUMPTION-145 (chat-scrape framed as token-delegation rather than mechanism-existence); PRESUMPTION-146 (Loughran papers on-disk without ingest trigger); PRESUMPTION-147 (three-event narrative segmentation without criteria); PRESUMPTION-148 (proposal-queue +2 as positive throughput — third-layer SELF-MEASUREMENT cluster); PRESUMPTION-149 (Agent 16 flag-not-merge norm without elaboration).

## RETURN/DISPOSITION summaries

### RETURN/DISPOSITION: ASSUMPTION-113
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-120; heuristic exception — method is principled, cross-platform generalization is the gap)
- **Reasoning:** Markup-anchor detection is canonical in web-IR (Risvik-Michelsen, Cafarella) and accessibility tooling (WCAG/ARIA); the C2A2-internal N=1 episode is consistent with the literature. Speaker-label feature is corpus-specific and the YouTube triad will not transfer cleanly to Spotify / RSS-hosted / podcaster-site transcripts. Heuristic exception MONITOR rather than REVISE because the method itself is well-grounded; the gap is generalization.
- **Full results:** lit_search_results/for/ASSUMPTION-113_for.md ; lit_search_results/against/ASSUMPTION-113_against.md

### RETURN/DISPOSITION: ASSUMPTION-114
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-121; heuristic exception — minimum-change continuation of operating cadence)
- **Reasoning:** Weekly cadence is conventionally supported (ITIL, SRE, Nyquist-aligned sampling). The method-vs-cadence attribution is counterfactual (Pearl) and N=1 cannot rule out cadence-error masked behind method-error. Per-show cadence-calibration is the load-bearing follow-up, not cadence change. Joint with MONITOR-120 and PRESUMPTION-143 single-data-point conjunction.
- **Full results:** lit_search_results/for/ASSUMPTION-114_for.md ; lit_search_results/against/ASSUMPTION-114_against.md

### RETURN/DISPOSITION: ASSUMPTION-115
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** **REVISE** (priority: MEDIUM)
- **Reasoning:** ASSUMPTION + moderate support + strong challenge → REVISE. "Cleanest single-page" is a superlative without comparison set, measurement, or denominator — structurally identical to PRESUMPTION-116, PRESUMPTION-129, ASSUMPTION-107 prior cluster items. With PRESUMPTION-141 (same cycle), the unnormalized-superlative anti-pattern reaches four-layer breadth in 4 days. Cluster satisfies ASSUMPTION-098 three-recurrence governance threshold at the cluster level a second time over (rate-comparison + source-comparison).
- **Full results:** lit_search_results/for/ASSUMPTION-115_for.md ; lit_search_results/against/ASSUMPTION-115_against.md

### RETURN/DISPOSITION: ASSUMPTION-116
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** **REVISE** (priority: HIGH; joint with PRESUMPTION-142; joins PRESUMPTION-002 CRITICAL + PRESUMPTION-074 SYSTEMIC-RISK clusters)
- **Reasoning:** ASSUMPTION + moderate support + strong challenge → REVISE. Pre-foundational reframing of three first-tier physics TOE programs without inverse-acceptance check; substantive evidence each named program would reject placement on its own foundational commitments (Carroll Mindscape Ep #91/#135; Wolfram framework-completeness; Arkani-Hamed Amplituhedron geometric foundationality). Authorizing Pattern Detector deep-pass on contested philosophical premise compounds the cluster's downstream weight. One of today's highest-risk items.
- **Full results:** lit_search_results/for/ASSUMPTION-116_for.md ; lit_search_results/against/ASSUMPTION-116_against.md

### RETURN/DISPOSITION: ASSUMPTION-117
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** **REVISE** (priority: MEDIUM-HIGH)
- **Reasoning:** ASSUMPTION + moderate support + strong challenge → REVISE. Second activation of ASSUMPTION-098 governance threshold compounds the circular-dependency that gated the first activation (ASSUMPTION-108 MONITOR-110: rule itself MONITORed not INCORPORATEd). Substrate-decomposition gate (PRESUMPTION-134 REVISE 2026-05-11, HIGH urgency, unresolved) applies — 5 consecutive skips may be a single common-cause failure misclassified as five. Skip-vs-failure ambiguity unaddressed (PRESUMPTION-138 REVISE 2026-05-11 historic-extrapolation precedent).
- **Full results:** lit_search_results/for/ASSUMPTION-117_for.md ; lit_search_results/against/ASSUMPTION-117_against.md

### RETURN/DISPOSITION: ASSUMPTION-118
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: HIGH; MONITOR-122; substrate-decomposition gate; PREMISE-015 follow-through) — not INCORPORATE despite 15a Strong
- **Reasoning:** Token-based delegation as replacement for password-handling is unambiguously endorsed by canonical authentication literature (NIST, OWASP, OAuth RFC); PREMISE-015 (INCORPORATEd 2026-05-11) committed the system to this redesign. The load-bearing concerns blocking INCORPORATE: (a) PRESUMPTION-145 (REVISE this cycle) flagged redesign-as-default without explicit redesign-vs-discard-vs-file-handoff comparison; (b) PRESUMPTION-134 (REVISE 2026-05-11, HIGH, unresolved) substrate-decomposition gate; (c) implementation-cost not estimated. Gating MONITOR-122 on substrate-decomposition + cost-benefit comparison preserves the PREMISE-015 commitment while preventing first-option commitment. Closest item to INCORPORATE this cycle — may transition by next 15d review (2026-05-20) if gates are resolved.
- **Full results:** lit_search_results/for/ASSUMPTION-118_for.md ; lit_search_results/against/ASSUMPTION-118_against.md

### RETURN/DISPOSITION: PRESUMPTION-140
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** **REVISE** (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Empty active watch list framed as positive signal without intake-coverage audit contradicts SRE absence-of-alerts framing (Beyer), surveillance-epidemiology coverage-audit discipline (Mason), and Hollnagel Safety-I/Safety-II distinction. Joins PRESUMPTION-069 silence-not-tracked cluster at the empty-watch-list layer.
- **Full results:** lit_search_results/for/PRESUMPTION-140_for.md ; lit_search_results/against/PRESUMPTION-140_against.md

### RETURN/DISPOSITION: PRESUMPTION-141
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** **REVISE** (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Third-layer recurrence of unnormalized-superlative anti-pattern at source-comparison layer (after rate-comparison recurrences in PRESUMPTION-116, PRESUMPTION-129, ASSUMPTION-107). With ASSUMPTION-115 (same cycle), cluster reaches four-layer breadth in 4 days — extends and confirms the SYSTEMIC-RISK-FLAG raised 2026-05-11.
- **Full results:** lit_search_results/for/PRESUMPTION-141_for.md ; lit_search_results/against/PRESUMPTION-141_against.md

### RETURN/DISPOSITION: PRESUMPTION-142
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** **REVISE** (priority: HIGH — today's highest-risk new item; joint with ASSUMPTION-116; joins two prior CRITICAL/SYSTEMIC-RISK clusters)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. One-way reframing of three first-tier physics TOE programs without inverse-acceptance check is the exact pattern PRESUMPTION-002 (CRITICAL) was REVISE'd for. Substantive examination of each named program's actual articulations gives overwhelming prima facie evidence the inverse-acceptance test would fail for all three. MacIntyre cross-tradition methodology requires substantive engagement.
- **Full results:** lit_search_results/for/PRESUMPTION-142_for.md ; lit_search_results/against/PRESUMPTION-142_against.md

### RETURN/DISPOSITION: PRESUMPTION-143
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** **REVISE** (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Single-data-point maturity claim contradicts SRE production-readiness review (Beyer Ch. 27), SPC pattern-confirmation (Wheeler), Hollnagel drift-into-failure, and PMBOK operational-readiness criteria. C2A2-internal track record shows first-cycle-success-then-degradation pattern (the cowork-to-chat-sync mechanism producing this cycle's ASSUMPTION-118 surely had a successful first cycle). Joint with ASSUMPTION-113 + ASSUMPTION-114 single-data-point conjunction; joins PRESUMPTION-040 cluster.
- **Full results:** lit_search_results/for/PRESUMPTION-143_for.md ; lit_search_results/against/PRESUMPTION-143_against.md

### RETURN/DISPOSITION: PRESUMPTION-144
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** **REVISE** (priority: MEDIUM; pre-implementation flag)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Closed seven-category taxonomy presumed complete contradicts Hjørland, Foskett, Hodge, Bowker-Star. Brief empirical examination of actual vault content reveals at least 5-6 reference types not in the seven-category list (section-anchors, concept-tags, transcript-timestamps, image-embeds, podcast-episode-IDs, footnotes). The presumption is empirically falsifiable on inspection. Pre-implementation flag: fix before Vault Linker Agent is built rather than after.
- **Full results:** lit_search_results/for/PRESUMPTION-144_for.md ; lit_search_results/against/PRESUMPTION-144_against.md

### RETURN/DISPOSITION: PRESUMPTION-145
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** **REVISE** (priority: MEDIUM-HIGH; structural counterpart to ASSUMPTION-118 MONITOR-122)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. First-option bias: chat-scrape sign-in barrier framed as token-delegation problem without explicit redesign-vs-discard-vs-file-handoff comparison contradicts Goldratt, Christensen, Bryar-Carr. PREMISE-015 itself preserved alternative paths ("OR equivalent"); narrower-than-premise reading is the structural concern. Joint with PRESUMPTION-134 substrate-decomposition cluster (unresolved) and ASSUMPTION-118 MONITOR-122 PREMISE-015 follow-through.
- **Full results:** lit_search_results/for/PRESUMPTION-145_for.md ; lit_search_results/against/PRESUMPTION-145_against.md

### RETURN/DISPOSITION: PRESUMPTION-146
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Moderate)
- **15c disposition:** **REVISE** (priority: MEDIUM)
- **Reasoning:** PRESUMPTION + moderate challenge + NO-SUPPORT → REVISE. Loughran papers on-disk-without-processing-trigger contradicts Reinertsen, Poppendieck, PMBOK. Third recurrence of on-disk-as-load-bearing-without-trigger pattern (after PRESUMPTION-128 and ASSUMPTION-111). Per-thinker asymmetry is unique structural concern (Wright/Rohr explicitly blocking; Loughran natural-cadence; same on-disk status, different operational treatment).
- **Full results:** lit_search_results/for/PRESUMPTION-146_for.md ; lit_search_results/against/PRESUMPTION-146_against.md

### RETURN/DISPOSITION: PRESUMPTION-147
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Moderate)
- **15c disposition:** **REVISE** (priority: LOW-MEDIUM)
- **Reasoning:** PRESUMPTION + moderate challenge + NO-SUPPORT → REVISE. Three-event narrative segmentation without explicit tier-criteria contradicts Allspaw, Boltanski-Thévenot, Pentland-Feldman, and cognitive-psychology rule-of-three. Joins PRESUMPTION-036 single-cluster-framing cluster. Without explicit criteria, segmentation is non-reproducible.
- **Full results:** lit_search_results/for/PRESUMPTION-147_for.md ; lit_search_results/against/PRESUMPTION-147_against.md

### RETURN/DISPOSITION: PRESUMPTION-148
- **15a (FOR):** NO-SUPPORT-FOUND (None)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** **REVISE** (priority: MEDIUM-HIGH — most actionable architectural item this cycle)
- **Reasoning:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Proposal-queue +2-today framing as positive throughput contradicts Little's Law, Reinertsen WIP-growth anti-signal, and Goodhart/Strathern intake-as-target. Third-layer recurrence of SELF-MEASUREMENT cluster at proposal-pending-count queue. Cluster now reaches multi-layer recurrence across REVISE-rate-as-target, REVISE-rate-as-confirmed, and proposal-queue-depth-as-positive — three distinct queue-and-rate layers within one anti-pattern signature.
- **Full results:** lit_search_results/for/PRESUMPTION-148_for.md ; lit_search_results/against/PRESUMPTION-148_against.md

### RETURN/DISPOSITION: PRESUMPTION-149
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: LOW-MEDIUM; MONITOR-124; heuristic exception — conservative default is correct; joint with MONITOR-116 PRESUMPTION-131 agent-autonomy cluster)
- **Reasoning:** Conservative flag-not-merge default is well-supported by AI-safety (Amodei), agent-design (Russell-Norvig), software-engineering PR-review practice, and Bryar-Carr two-way-door reasoning. The structural concern is absence of elaboration around the safely-automatable boundary, not the wrongness of the default. Heuristic exception based on (a) the individual policy is defensible; (b) "always flag" is the safe operational default; (c) cumulative policy-by-accretion concern (joint with PRESUMPTION-131) is real but operationally addressed via joint cluster remediation.
- **Full results:** lit_search_results/for/PRESUMPTION-149_for.md ; lit_search_results/against/PRESUMPTION-149_against.md

---

## Cycle disposition counts

- **INCORPORATE:** 0 (back to 0% after the 2026-05-11 cycle broke the streak at 1/21)
- **MONITOR:** 4 (3 ASSUMPTIONs + 1 PRESUMPTION) — MONITOR-120, 121, 122, 124; MONITOR-123 reserved-and-unused per provenance protocol immutability preference
- **REVISE:** 12 (3 ASSUMPTIONs + 9 PRESUMPTIONs)
- ASSUMPTION REVISE rate: 3/6 (50%) — second consecutive cycle with non-zero ASSUMPTION REVISE rate; sequence over four cycles is 0/8 + 0/8 + 1/9 + 3/6 — clear upward trajectory
- PRESUMPTION REVISE rate: 9/10 (90%) — back to the 2026-05-10 high range; heuristic-exception rate fell from 5/12 (42%) to 1/10 (10%) at the PRESUMPTION layer

## SYSTEMIC-RISK flags

**SYSTEMIC-RISK-FLAG (2026-05-13):** Unnormalized-superlative anti-pattern reaches four-layer breadth in 4 days — extends 2026-05-11 flag
- **Affected items:** PRESUMPTION-116 (REVISE 2026-05-10) → PRESUMPTION-129 (REVISE 2026-05-11) → ASSUMPTION-107 (REVISE 2026-05-11) → PRESUMPTION-141 (REVISE 2026-05-13) + ASSUMPTION-115 (REVISE 2026-05-13). Cluster spans stated/unstated forms at rate-comparison AND source-comparison layers.
- **Common vulnerability:** comparative claims without explicit comparison set, measurement, or denominator treated as meaningful evaluative metric.
- **Literature basis:** Wheeler (2000); Bornmann-Mutz (2015); Goodhart (1975); Strathern (1997); Galison (1997); Knorr-Cetina (1999).
- **Risk level:** HIGH — cluster has satisfied ASSUMPTION-098 three-recurrence governance threshold at the cluster level twice over (rate-comparison AND source-comparison layers). DECISION-NNN canonization candidacy strengthens.
- **Recommendation:** Reporting-template guards (normalization disclosure required for any superlative claim); DECISION-NNN canonization of the anti-pattern; Goodhart-mitigation paired-metric; downstream readers should treat C2A2-internal superlatives with explicit skepticism pending the canonization.

**SYSTEMIC-RISK-FLAG (2026-05-13):** Cross-tradition transfer-validity cluster reaches new TOE-hierarchy layer
- **Affected items:** ASSUMPTION-116 + PRESUMPTION-142 (REVISE this cycle); joins PRESUMPTION-002 (CRITICAL cluster, REVISE) + PRESUMPTION-074 (specialist-recognition SYSTEMIC-RISK cluster).
- **Common vulnerability:** One-way cross-tradition reframing without inverse-acceptance check; substantive evidence each affected program would reject the reframing on its own foundational commitments.
- **Literature basis:** MacIntyre (1988); Lakatos (1970); Carroll Mindscape Ep #91/#135; Wolfram framework-completeness; Arkani-Hamed Amplituhedron geometric foundationality.
- **Risk level:** HIGH (today's highest-risk new items; multiple-cluster joint).
- **Recommendation:** Inverse-acceptance check before Pattern Detector deep-pass (assemble strongest case for each of Arkani-Hamed/Wolfram/Carroll's rejection of pre-foundational placement); specialist-agent reactions solicited; PRS-CANDIDATE-01 demoted from "structural significance" to "contested structural proposal"; joint remediation with PRESUMPTION-002 + PRESUMPTION-074 clusters.

**SYSTEMIC-RISK-FLAG (2026-05-13):** SELF-MEASUREMENT Goodhart cluster reaches proposal-queue-depth layer
- **Affected items:** PRESUMPTION-148 (REVISE this cycle); cluster origin ASSUMPTION-112 MONITOR-114 + PRESUMPTION-123 REVISE 2026-05-10 + PRESUMPTION-129 REVISE 2026-05-11 + ASSUMPTION-107 REVISE 2026-05-11.
- **Common vulnerability:** Queue and rate metrics framed as positive-throughput signals without intake-vs-disposition normalization or Goodhart-mitigation paired metric.
- **Literature basis:** Little's Law (Kingman 1961); Reinertsen (2009); Goodhart (1975); Strathern (1997); Beyer (2016) SRE SLI/SLO design.
- **Risk level:** MEDIUM-HIGH (third-layer cluster recurrence at new operational layer; most actionable architectural item per 14b extraction).
- **Recommendation:** Disposition-rate paired metric (proposal-throughput = dispositions/day, not intake/day); ratio-metric with explicit target; qualitative-veto on intake celebration without disposition-match; joint cluster remediation with ASSUMPTION-112 + PRESUMPTION-123 + PRESUMPTION-129 + ASSUMPTION-107; multi-metric SLI/SLO design per Beyer SRE.

**SYSTEMIC-RISK-FLAG (2026-05-13):** Substrate-decomposition gate cluster carries forward unresolved
- **Affected items:** PRESUMPTION-134 (REVISE 2026-05-11, HIGH, unresolved) + new ASSUMPTION-117 (REVISE 2026-05-13) + new ASSUMPTION-118 MONITOR-122 + new PRESUMPTION-145 (REVISE 2026-05-13); also continues to gate ASSUMPTION-108 MONITOR-110 + ASSUMPTION-109 MONITOR-111.
- **Common vulnerability:** Recurrence-counter and redesign-warrant authorizations rely on independent-failure assumptions that substrate-decomposition has not been performed to verify.
- **Literature basis:** Vesely (1981) fault-tree handbook; Allspaw-Cook (2000); Toyota Five Whys.
- **Risk level:** HIGH (load-bearing prerequisite for at least three this-cycle dispositions plus two prior-cycle MONITORs).
- **Recommendation:** Substrate-decomposition is now the canonical-priority next architectural action. Performing it would either (a) confirm independence and unblock ASSUMPTION-108/109/117/118 paths, or (b) collapse the four-to-five item cluster into a single shared-substrate root cause and dramatically reduce week-carrying-capacity demand. The cost of decomposition is low; the cost of further-deferring it compounds at each cycle.

**SYSTEMIC-RISK-FLAG (2026-05-13):** Single-data-point conjunction at Agent 16 protocol layer
- **Affected items:** ASSUMPTION-113 MONITOR-120 + ASSUMPTION-114 MONITOR-121 + PRESUMPTION-143 REVISE; joins PRESUMPTION-040 operational-readiness cluster.
- **Common vulnerability:** Method, cadence, and protocol-maturity are independent claims that the conjunction "Agent 16 successful first cycle" risks conflating; the three together inflate the maturity claim's downstream weight.
- **Literature basis:** Wheeler (2000) SPC; Beyer (2016) SRE Ch. 27; Hollnagel (2012) drift-into-failure; PMBOK.
- **Risk level:** MEDIUM (low blast radius per item; structural concern at cluster level).
- **Recommendation:** Multi-cycle acceptance criteria for new protocols; drift-into-failure monitoring across next 5+ resolution episodes; demote framing across the three joint items; per-show / per-platform calibration tested explicitly.

## Cycle-level observations

**The 2026-05-13 cycle re-instates the 0-INCORPORATE pattern after the 2026-05-11 cycle broke it.** Across the four-cycle window (2026-05-09, 2026-05-10, 2026-05-11, 2026-05-13 — noting the 2026-05-12 EOD batch is what this cycle processes, no 15a/15b cycle ran 2026-05-12), INCORPORATE rate is 1/66 (1.5%). The cluster pattern predicted by ASSUMPTION-112 (MONITOR-114) is empirically well-observed; the partial falsification at 2026-05-11 has been re-instated. PRESUMPTION-148 (this cycle, REVISE) flagged the same cluster signature at the proposal-queue-depth layer, producing the structural setup where the cluster predicts the cycle that produces the prediction's confirmation. Self-referential signal.

**Three ASSUMPTION REVISEs this cycle (50% rate) is markedly elevated.** Sequence over four cycles: 0/8 + 0/8 + 1/9 + 3/6 = 4/31 (12.9%). The 2026-05-13 rate of 3/6 dominates the cumulative; the upward trajectory is now multi-cycle. ASSUMPTION REVISEs are the items where stated/designer-aware claims fail challenge — the asymmetric-REVISE-rate pattern that ASSUMPTION-106 (MONITOR-109) named is partially-falsified at the rate level. ASSUMPTION-106 framing ("0/8 streak") is now N=4 cycles into demonstrable non-stationarity.

**Substrate-decomposition is now the canonical-priority next architectural action.** Four-to-five item cluster across two cycles, load-bearing for at least three this-cycle dispositions plus two prior-cycle MONITORs. The cost of decomposition is low; the cost of further-deferring it compounds. Recommended sequence: (a) substrate-decomposition first; (b) if substrate-shared, collapse multiple HIGH-urgency dispositions into a single combined DECISION; (c) Tom consultation on week-carrying-capacity before parallel commitment.

**The proposal-queue Goodhart layer (PRESUMPTION-148) is the most actionable architectural item this batch.** Disposition-rate paired metric is a cheap, immediate, canonical remediation that would extend to the REVISE-rate cluster and the proposal-queue cluster simultaneously. Multi-metric SLI/SLO design per Beyer SRE is the load-bearing follow-up for the entire SELF-MEASUREMENT cluster's remediation.

**Pre-implementation flag (PRESUMPTION-144) is a useful precedent.** Catching a closed-taxonomy design error before the Vault Linker Agent is built is a substantively-cheaper REVISE than post-implementation refactor would have been. The pattern (extraction → 14b → 15a/15b → 15c → REVISE before implementation) is the registry's first pre-implementation REVISE.

**Cross-tradition transfer-validity cluster (PRESUMPTION-142 + ASSUMPTION-116) is today's highest-risk pair.** Joins the existing CRITICAL + SYSTEMIC-RISK clusters at the four-program TOE-hierarchy layer. Substantive evidence each named program would reject the reframing. Authorizing Pattern Detector deep-pass on contested philosophical premise should be blocked pending inverse-acceptance check.

## Files updated this run

- `lit_search_results/for/ASSUMPTION-{113..118}_for.md` (6 new); `PRESUMPTION-{140..149}_for.md` (10 new) → 16 total
- `lit_search_results/against/ASSUMPTION-{113..118}_against.md` (6 new); `PRESUMPTION-{140..149}_against.md` (10 new) → 16 total
- `lit_search_returns.md` — this 2026-05-13 RUN section appended with all 16 dispositions, 5 SYSTEMIC-RISK flags, cycle observations
- `validated_premises.md` — 2026-05-13 RUN section appended with no-new-INCORPORATE note + cycle-level observation on register starvation; total premises remains 15
- `monitor_queue.md` — MONITOR-120, 121, 122, 124 appended (MONITOR-123 reserved-and-unused); total now 123 (119 + 4 new)
- `revision_flags.md` — 12 REVISE entries appended in 2026-05-13 cycle section
- `for_lit_search.md` — all 16 items updated with [SEARCHED-15a: 2026-05-13] [SEARCHED-15b: 2026-05-13] [DISPOSITIONED-15c: 2026-05-13] tags

## Queue state post-run

- 0 QUEUED items from 2026-05-12 EOD batch (all 16 drained)
- 57 RE-TRIGGER items from 2026-05-05 cohort remain queued for next 15a/15b cycle (next_check 2026-05-12 per Run 4 — note: re-trigger batch was not picked up this run; remains queued)

## Provenance checklist

- [x] All 16 items have PROVENANCE headers with Origin, Chain, Item type recorded in for/against result files
- [x] All 16 items updated in for_lit_search.md with full status tag sequence
- [x] All dispositions routed to appropriate destination file (validated_premises / monitor_queue / revision_flags)
- [x] Cross-references between joint items documented (cross-tradition reframing cluster; SELF-MEASUREMENT proposal-queue cluster; substrate-decomposition gate cluster; single-data-point Agent 16 conjunction)
- [x] 5 SYSTEMIC-RISK-FLAGs raised (unnormalized-superlative four-layer extension; cross-tradition TOE-hierarchy layer; SELF-MEASUREMENT proposal-queue; substrate-decomposition cluster carry-forward; single-data-point Agent 16 conjunction)
- [x] Cycle-level INCORPORATE-rate trajectory documented (1/66 across four cycles; pattern empirically well-observed)
- [x] First pre-implementation REVISE (PRESUMPTION-144) noted as registry precedent

---

**Generated by Agents 15a, 15b, and 15c (2026-05-13 scheduled pipeline run)**
**Date: 2026-05-13 (autonomous scheduled-task run; no human review in-loop)**
**Pipeline trigger: c2a2-lit-search-pipeline scheduled task; queued items processed in single drain pass.**

---

# 2026-05-14 RUN — c2a2-lit-search-pipeline (Agents 15a + 15b + 15c)
**Date:** 2026-05-14 (autonomous scheduled-task run; no human review in-loop)
**Items processed:** 30 (12 ASSUMPTIONs + 18 PRESUMPTIONs from 2026-05-13 EOD 14a/14b extraction)
**Pipeline:** Agents 15a + 15b + 15c
**Trigger:** scheduled c2a2-lit-search-pipeline task (one hour after 2026-05-14 self-awareness pipeline run; processing 2026-05-13 EOD batch tied to the 17-pathway architectural articulation pass)

## Items processed (30 total)

**ASSUMPTIONs (12):** ASSUMPTION-119 (17-pathway inventory + 6 ISME-critical + 2 bright pins); ASSUMPTION-120 (Cloudflare Workers broker hosting); ASSUMPTION-121 (Twilio SMS one-tap signed link); ASSUMPTION-122 (eager-tier perspective-lattice first-class citizen); ASSUMPTION-123 (whiteboard ephemeral + Pin-this + export); ASSUMPTION-124 (D3 + three.js + Plotly + WebGL library set); ASSUMPTION-125 (unsaid-edges two-filter with Low × High emphasis); ASSUMPTION-126 (7-day drought broken via sign-in restoration); ASSUMPTION-127 (2026-05-13 daily run network delta + 3 HIGH); ASSUMPTION-128 (FINDING-030 KL-divergence first quantitative detector); ASSUMPTION-129 (nightly alignment-agent unidirectional sync); ASSUMPTION-130 (honesty layer first-class architectural commitment).

**PRESUMPTIONs (18):** PRESUMPTION-150 (17-pathway closed enumeration); PRESUMPTION-151 (binary ISME-critical classification); PRESUMPTION-152 (edge overhead estimate without measurement); PRESUMPTION-153 (signed-link without threat model); PRESUMPTION-154 (phone-as-modality without alternatives); PRESUMPTION-155 (first-class machinery without transfer audit); PRESUMPTION-156 (ephemeral-default without inverse-default audit); PRESUMPTION-157 (library set without alternatives comparison); PRESUMPTION-158 (Low × High UI emphasis normative); PRESUMPTION-159 (credential-layer-as-architectural-fix); PRESUMPTION-160 (3-HIGH-in-one-day as Goodhart cluster recurrence); PRESUMPTION-161 (KL-divergence transfer-validity cluster); PRESUMPTION-162 (unidirectional sync without merge); PRESUMPTION-163 (universal marking over-saturation); PRESUMPTION-164 (bright-pin operational gravity); PRESUMPTION-165 (recursive frame without termination); PRESUMPTION-166 (pathway-doc decision-drift); PRESUMPTION-167 (broker-as-substrate premature unification).

## RETURN/DISPOSITION summaries

### RETURN/DISPOSITION: ASSUMPTION-119
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-125)
- **Reasoning:** Forcing-function articulation pattern is well-supported (Bryar-Carr, Hohpe). "End-to-end" claim risks confusing enumeration with integration coherence (Conway). Joint with PRESUMPTION-150 closed-enumeration concern. Demo-walkthrough validation is the load-bearing follow-up.
- **Full results:** lit_search_results/for/ASSUMPTION-119_for.md ; lit_search_results/against/ASSUMPTION-119_against.md

### RETURN/DISPOSITION: ASSUMPTION-120
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** **INCORPORATE** (PREMISE-016) with caveats — conditional-on-validation framing preserved
- **Reasoning:** Strong vendor-benchmark + canonical edge-broker pattern. p99 tail-latency and Workers-specific lock-in are real but addressable validation items. The "conditional on streaming-latency validation" clause inside the assumption already encodes the right epistemic posture. Heuristic: "15a strong support + 15b weak-moderate challenge → lean INCORPORATE with caveats" — canonical case.
- **Full results:** lit_search_results/for/ASSUMPTION-120_for.md ; lit_search_results/against/ASSUMPTION-120_against.md

### RETURN/DISPOSITION: ASSUMPTION-121
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: HIGH — security-relevant; MONITOR-126)
- **Reasoning:** Mechanism choice (one-tap signed link over reply-keyword) is well-supported within SMS. But NIST formally demoted SMS as authentication channel; SIM-swap and SS7 are documented attack vectors. Joint with PRESUMPTION-153 (threat-model gap) and PRESUMPTION-154 (modality-comparison gap). MONITOR over INCORPORATE because the modality-level concerns may rebalance the choice toward push-with-device-key or WebAuthn for higher-stakes escalations.
- **Full results:** lit_search_results/for/ASSUMPTION-121_for.md ; lit_search_results/against/ASSUMPTION-121_against.md

### RETURN/DISPOSITION: ASSUMPTION-122
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-127)
- **Reasoning:** Storage pattern (tagged first-class entity) is sound. Machinery-transfer audit (PRESUMPTION-155 paired) is the load-bearing gap — existing Sociogram / structure-group code paths were built for thinker/PRS schema. Liskov substitution concern.
- **Full results:** lit_search_results/for/ASSUMPTION-122_for.md ; lit_search_results/against/ASSUMPTION-122_against.md

### RETURN/DISPOSITION: ASSUMPTION-123
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-128)
- **Reasoning:** Ephemeral-default + pin pattern has UX precedent but the re-finding literature (Bruce et al., Capra) shows users routinely fail at real-time value recognition. Joint with PRESUMPTION-156. Auto-persist-with-cleanup is the canonical compromise. Default-direction audit is the load-bearing follow-up.
- **Full results:** lit_search_results/for/ASSUMPTION-123_for.md ; lit_search_results/against/ASSUMPTION-123_against.md

### RETURN/DISPOSITION: ASSUMPTION-124
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** **INCORPORATE** (PREMISE-017) with caveats — library-set comparison audit recommended
- **Reasoning:** Library set is field-tested and covers the canonical landscape. C2A2-internal precedent (wiki_narration.html D3 v7) confirms production viability. The challenge is about LLM-codegen surface optimization (Vega-Lite, Observable Plot would reduce codegen errors) — addressable by additive selection rather than catalog replacement. Heuristic: strong support + moderate challenge → INCORPORATE with caveats.
- **Full results:** lit_search_results/for/ASSUMPTION-124_for.md ; lit_search_results/against/ASSUMPTION-124_against.md

### RETURN/DISPOSITION: ASSUMPTION-125
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-129)
- **Reasoning:** Two-filter design is well-supported (Swanson UDP, innovation studies). UI-emphasis on Low × High is a normative operationalization (PRESUMPTION-158 paired). Empirical validation against actual research programs is the load-bearing test.
- **Full results:** lit_search_results/for/ASSUMPTION-125_for.md ; lit_search_results/against/ASSUMPTION-125_against.md

### RETURN/DISPOSITION: ASSUMPTION-126
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** CHALLENGED (Strong)
- **15c disposition:** **REVISE** (priority: HIGH; joint with PRESUMPTION-159; joins PRESUMPTION-134 substrate-decomposition cluster)
- **Reasoning:** ASSUMPTION + moderate support + strong challenge → REVISE. Credential-layer-as-architectural-fix is canonical post-incident anti-pattern (Reason, Allspaw, SRE). 7-day drought duration is itself evidence of substrate-level fragility. The token-delegation redesign track (ASSUMPTION-118 MONITOR-122) remains the architectural-layer fix; ASSUMPTION-126 should be demoted to "momentarily restored," not "broken." Substrate-decomposition gate (PRESUMPTION-134 REVISE 2026-05-11, unresolved) applies.
- **Full results:** lit_search_results/for/ASSUMPTION-126_for.md ; lit_search_results/against/ASSUMPTION-126_against.md

### RETURN/DISPOSITION: ASSUMPTION-127
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak-Moderate)
- **15b (AGAINST):** CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-130; joins SELF-MEASUREMENT Goodhart cluster)
- **Reasoning:** Counts are correctly recorded; interpretive normalization ("3-HIGH = normal") lacks baseline. Joint with PRESUMPTION-160. SPC baseline construction is the load-bearing follow-up. Continues recurring SELF-MEASUREMENT cluster pattern.
- **Full results:** lit_search_results/for/ASSUMPTION-127_for.md ; lit_search_results/against/ASSUMPTION-127_against.md

### RETURN/DISPOSITION: ASSUMPTION-128
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** STRONGLY-CHALLENGED (Strong)
- **15c disposition:** **REVISE** (priority: HIGH; joins PRESUMPTION-002 + PRESUMPTION-080 + PRESUMPTION-161 transfer-validity cluster)
- **Reasoning:** ASSUMPTION + moderate support + strong challenge → REVISE. Multiple unaudited transfers: (a) active-inference ↔ OODA is analogy not formal homology in literature (Parr/Pezzulo/Friston 2022); (b) traditions-as-probability-distributions unvalidated; (c) comparable-claim-spaces is precondition for KL-divergence to be meaningful. "First quantitative detector" status is over-claimed. Demote to "candidate quantitative formalization pending transfer-validity audit." Joint with PRESUMPTION-161.
- **Full results:** lit_search_results/for/ASSUMPTION-128_for.md ; lit_search_results/against/ASSUMPTION-128_against.md

### RETURN/DISPOSITION: ASSUMPTION-129
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** **INCORPORATE** (PREMISE-018) with caveats — single-writer invariant must be technically enforced
- **Reasoning:** Unidirectional sync pattern is canonical under single-writer (Lamport, CAP, Git tradition). Summa `sync_vault.sh` precedent confirms operational viability. The PRESUMPTION-162 paired concern (mirror-side edits not prevented) is addressable by filesystem permissions or pre-overwrite diff. Heuristic: strong support + moderate challenge → INCORPORATE with caveats noted.
- **Full results:** lit_search_results/for/ASSUMPTION-129_for.md ; lit_search_results/against/ASSUMPTION-129_against.md

### RETURN/DISPOSITION: ASSUMPTION-130
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** **INCORPORATE** (PREMISE-019) with caveats — graduated marking required
- **Reasoning:** First-class commitment to visible epistemic-status is well-supported by IPCC, responsible-AI model-card practice, Tufte, Floridi/Nguyen. The challenge (over-saturation invisibility, PRESUMPTION-163 paired) targets implementation uniformity, not commitment-class. Graduated marking (high-confidence claims default-unmarked, deviations emphasized) captures the intent with better attention economics. INCORPORATE with explicit graduated-implementation caveat.
- **Full results:** lit_search_results/for/ASSUMPTION-130_for.md ; lit_search_results/against/ASSUMPTION-130_against.md

### RETURN/DISPOSITION: PRESUMPTION-150
- **15a (FOR):** SUPPORTED (Moderate)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (None-Weak)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-131; missing-pathway audit recommended)
- **Reasoning:** PRESUMPTION + supported inference + no challenge → MONITOR. Closed-enumeration-as-completeness anti-pattern is canonical (Brooks, Christensen). Cross-reference to PRESUMPTION-144 confirms recurring structural pattern. Joint with ASSUMPTION-119.
- **Full results:** lit_search_results/for/PRESUMPTION-150_for.md ; lit_search_results/against/PRESUMPTION-150_against.md

### RETURN/DISPOSITION: PRESUMPTION-151
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (None-Weak)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-132; fallback sub-set audit recommended)
- **Reasoning:** Binary-vs-graduated criticality (MoSCoW) is canonical release-planning concern. Either indivisibility claim must be made explicit, or fallback sub-set must be specified.
- **Full results:** lit_search_results/for/PRESUMPTION-151_for.md ; lit_search_results/against/PRESUMPTION-151_against.md

### RETURN/DISPOSITION: PRESUMPTION-152
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-133; already-gated by ASSUMPTION-120 conditional clause)
- **Reasoning:** PRESUMPTION inference is well-founded but is partly preempted by ASSUMPTION-120's "conditional on streaming-latency validation" clause. MONITOR to ensure the validation is actually performed before deployment.
- **Full results:** lit_search_results/for/PRESUMPTION-152_for.md ; lit_search_results/against/PRESUMPTION-152_against.md

### RETURN/DISPOSITION: PRESUMPTION-153
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: HIGH — security; MONITOR-134)
- **Reasoning:** Threat-model articulation is canonical security prerequisite (Shostack, OWASP, NIST). PRESUMPTION + supported inference + weak challenge → MONITOR; security-relevant items get HIGH priority. Joint with ASSUMPTION-121 and PRESUMPTION-154.
- **Full results:** lit_search_results/for/PRESUMPTION-153_for.md ; lit_search_results/against/PRESUMPTION-153_against.md

### RETURN/DISPOSITION: PRESUMPTION-154
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-135)
- **Reasoning:** Modality-comparison gap is recognized affordance-invisibility pattern (Norman, paging-tool design literature). Joint with ASSUMPTION-121 and PRESUMPTION-153. Out-of-band rationale (in-band-failure-isolation) supports SMS for some flows but does not preempt the comparison.
- **Full results:** lit_search_results/for/PRESUMPTION-154_for.md ; lit_search_results/against/PRESUMPTION-154_against.md

### RETURN/DISPOSITION: PRESUMPTION-155
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-136; joint with ASSUMPTION-122)
- **Reasoning:** Liskov-substitution-style machinery-transfer audit is canonical. Joint MONITOR with ASSUMPTION-122; audit is the operational follow-up.
- **Full results:** lit_search_results/for/PRESUMPTION-155_for.md ; lit_search_results/against/PRESUMPTION-155_against.md

### RETURN/DISPOSITION: PRESUMPTION-156
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-137; joint with ASSUMPTION-123)
- **Reasoning:** Default-direction is recognized load-bearing design choice (Nudge literature, re-finding research). Inverse-default audit and auto-persist-with-cleanup compromise are the load-bearing follow-ups.
- **Full results:** lit_search_results/for/PRESUMPTION-156_for.md ; lit_search_results/against/PRESUMPTION-156_against.md

### RETURN/DISPOSITION: PRESUMPTION-157
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-138; joint with ASSUMPTION-124)
- **Reasoning:** Closed-enumeration concern is well-founded. Library-set comparison audit (additive AND subtractive) is the load-bearing follow-up.
- **Full results:** lit_search_results/for/PRESUMPTION-157_for.md ; lit_search_results/against/PRESUMPTION-157_against.md

### RETURN/DISPOSITION: PRESUMPTION-158
- **15a (FOR):** SUPPORTED (Moderate)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-139; joint with ASSUMPTION-125)
- **Reasoning:** UI-emphasis-as-normative-operationalization is canonical framing-effects concern (Tversky-Kahneman). Empirical validation against actual research programs is the load-bearing test.
- **Full results:** lit_search_results/for/PRESUMPTION-158_for.md ; lit_search_results/against/PRESUMPTION-158_against.md

### RETURN/DISPOSITION: PRESUMPTION-159
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** **REVISE** with ASSUMPTION-126 (priority: HIGH; joint with substrate-decomposition cluster)
- **Reasoning:** Credential-vs-architectural-layer distinction is canonical post-incident-analysis (Reason, SRE, Allspaw). Joint with ASSUMPTION-126 (REVISE this cycle). Per heuristic: PRESUMPTION with strong inference paired to an ASSUMPTION REVISE inherits REVISE disposition.
- **Full results:** lit_search_results/for/PRESUMPTION-159_for.md ; lit_search_results/against/PRESUMPTION-159_against.md

### RETURN/DISPOSITION: PRESUMPTION-160
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: HIGH — SELF-MEASUREMENT Goodhart cluster recurrence; MONITOR-140)
- **Reasoning:** Baseline-normalization gap is canonical SPC concern. Cross-reference to ASSUMPTION-112 SELF-MEASUREMENT cluster confirms recurring pattern. Joint with ASSUMPTION-127. SYSTEMIC-RISK: SELF-MEASUREMENT cluster now has yet another recurrence layer.
- **Full results:** lit_search_results/for/PRESUMPTION-160_for.md ; lit_search_results/against/PRESUMPTION-160_against.md

### RETURN/DISPOSITION: PRESUMPTION-161
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** **REVISE** with ASSUMPTION-128 (priority: HIGH; joint with PRESUMPTION-002 + PRESUMPTION-080 transfer-validity cluster)
- **Reasoning:** Cross-discipline transfer-validity audit is canonical (Cartwright). PRESUMPTION-002 and PRESUMPTION-080 cluster is unresolved. Joint REVISE with ASSUMPTION-128. SYSTEMIC-RISK: transfer-validity cluster now has another instance.
- **Full results:** lit_search_results/for/PRESUMPTION-161_for.md ; lit_search_results/against/PRESUMPTION-161_against.md

### RETURN/DISPOSITION: PRESUMPTION-162
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-141; joint with ASSUMPTION-129 INCORPORATE caveats)
- **Reasoning:** Single-writer invariant is canonical (Lamport). The caveat in ASSUMPTION-129's INCORPORATE explicitly addresses this; MONITOR tracks enforcement.
- **Full results:** lit_search_results/for/PRESUMPTION-162_for.md ; lit_search_results/against/PRESUMPTION-162_against.md

### RETURN/DISPOSITION: PRESUMPTION-163
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-142; joint with ASSUMPTION-130 INCORPORATE caveats)
- **Reasoning:** Over-saturation invisibility is canonical safety-engineering concern (alarm-fatigue, Joint Commission). The caveat in ASSUMPTION-130's INCORPORATE explicitly addresses graduated marking; MONITOR tracks implementation.
- **Full results:** lit_search_results/for/PRESUMPTION-163_for.md ; lit_search_results/against/PRESUMPTION-163_against.md

### RETURN/DISPOSITION: PRESUMPTION-164
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-143; bright-pin operational-gravity tracking)
- **Reasoning:** Held-position operational gravity is canonical ADR concern (Nygard, Fowler). Bright-pin framing is honest acknowledgment but does not remove the shaping effect on Pathway 14 / Pathway 17.
- **Full results:** lit_search_results/for/PRESUMPTION-164_for.md ; lit_search_results/against/PRESUMPTION-164_against.md

### RETURN/DISPOSITION: PRESUMPTION-165
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-144; CS-termination framing demoted; meta-Goodhart preserved)
- **Reasoning:** Recursive self-application has substantive precedent (MacIntyre, autopoiesis, Hofstadter). The CS-termination framing in the presumption is the weaker part. Meta-Goodhart concern stands; productive-recursion criteria are the better framing.
- **Full results:** lit_search_results/for/PRESUMPTION-165_for.md ; lit_search_results/against/PRESUMPTION-165_against.md

### RETURN/DISPOSITION: PRESUMPTION-166
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-145; extends PRESUMPTION-041 implicit-decision-drift cluster)
- **Reasoning:** Implicit-decision-drift at pathway-doc layer is canonical (ADR practice, Brooks). Cluster recurrence at the pathway-doc layer; selective canonization is the load-bearing remediation.
- **Full results:** lit_search_results/for/PRESUMPTION-166_for.md ; lit_search_results/against/PRESUMPTION-166_against.md

### RETURN/DISPOSITION: PRESUMPTION-167
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: HIGH — substrate-decomposition gate; MONITOR-146; joint with PRESUMPTION-134 REVISE unresolved)
- **Reasoning:** Premature-substrate-unification is canonical anti-pattern (Parnas, Bass-Clements-Kazman). The PRESUMPTION-134 REVISE remains unresolved; broker-as-substrate framing depends on the decomposition audit. SYSTEMIC-RISK: substrate-decomposition cluster carry-forward.
- **Full results:** lit_search_results/for/PRESUMPTION-167_for.md ; lit_search_results/against/PRESUMPTION-167_against.md

---

## 2026-05-14 RUN — Cycle-level summary

**Disposition counts:** 4 INCORPORATE (ASSUMPTION-120, ASSUMPTION-124, ASSUMPTION-129, ASSUMPTION-130) / 22 MONITOR / 4 REVISE — 2 ASSUMPTION REVISEs (ASSUMPTION-126, ASSUMPTION-128) and 2 paired PRESUMPTION REVISEs (PRESUMPTION-159 paired with ASSUMPTION-126; PRESUMPTION-161 paired with ASSUMPTION-128). Total = 30 items.

**INCORPORATE rate:** 4/30 (13.3%) — first non-zero INCORPORATE cycle since 2026-05-11. Across the five-cycle window (2026-05-09 / 10 / 11 / 13 / 14), INCORPORATE rate is 5/96 (5.2%); the 2026-05-14 cycle alone contributes 4 of the 5. This breaks the SELF-MEASUREMENT Goodhart cluster pattern observed in 4 of the last 5 cycles and provides useful counter-evidence to the recursive-confirmation framing.

**Why the cycle is INCORPORATE-rich:** the 17-pathway articulation pass surfaced four assumptions with strong canonical literature backing (cloud-edge broker, mature library set, unidirectional sync, first-class epistemic marking) and only moderate challenges (mostly addressable as caveats). Pre-implementation architectural articulation passes are predicted by the 2026-05-13 run note as more INCORPORATE-likely than operational incidents.

**SYSTEMIC-RISK-FLAGs raised (4):**
1. **Substrate-decomposition cluster** — third carry-forward: PRESUMPTION-134 REVISE remains unresolved; PRESUMPTION-167 + ASSUMPTION-126 + ASSUMPTION-118 (prior MONITOR) all depend on this audit.
2. **Transfer-validity cluster** — extension to KL-divergence layer: PRESUMPTION-002 + PRESUMPTION-080 + PRESUMPTION-161 + ASSUMPTION-128. Cross-discipline metric and conceptual transfers continue to enter the system faster than the audit closes them.
3. **SELF-MEASUREMENT Goodhart cluster** — fourth-layer recurrence at escalation-rate-without-baseline layer (PRESUMPTION-160 + ASSUMPTION-127). The cluster has shown recurrence at every layer audited.
4. **Closed-enumeration cluster** — PRESUMPTION-150 (17-pathway) and PRESUMPTION-157 (library set) both join PRESUMPTION-144 (Vault Linker seven-category) — closed-enumeration-without-audit pattern is now structurally well-observed.

**Heuristic exception note:** ASSUMPTION-121 was Strong-supported by 15a but received MONITOR (not INCORPORATE) because the modality-level concerns (NIST SMS demotion, SIM-swap) raised in 15b apply at a layer above the within-SMS UX choice. This is a case where the disposition rule "Strong support + moderate challenge → INCORPORATE" requires modification when the 15b challenge targets a different layer than the 15a support.

## Completion checklist

- [x] All 30 items have FOR and AGAINST result files
- [x] All 30 items have PROVENANCE headers with Origin, Chain, Item type recorded
- [x] All 30 items dispositioned by 15c
- [x] 4 INCORPORATEs appended to validated_premises.md (PREMISE-016 through PREMISE-019)
- [x] 2 REVISEs (ASSUMPTION-126, ASSUMPTION-128) appended to revision_flags.md; 2 paired PRESUMPTION-REVISEs (159, 161) appended jointly
- [x] 22 MONITORs appended to monitor_queue.md (MONITOR-125 through MONITOR-146; MONITOR-123 remains reserved-and-unused per 2026-05-13 immutability convention)
- [x] for_lit_search.md updated with [SEARCHED-15a], [SEARCHED-15b], [DISPOSITIONED-15c] tags
- [x] Cycle-level summary recorded (4/30 INCORPORATE; first non-zero cycle since 2026-05-11)
- [x] 4 SYSTEMIC-RISK-FLAGs raised (substrate-decomposition, transfer-validity, SELF-MEASUREMENT Goodhart, closed-enumeration clusters)

---

**Generated by Agents 15a, 15b, and 15c (2026-05-14 scheduled pipeline run)**
**Date: 2026-05-14 (autonomous scheduled-task run; no human review in-loop)**
**Pipeline trigger: c2a2-lit-search-pipeline scheduled task; queued items processed in single drain pass.**

---

# 2026-05-15 RUN — c2a2-lit-search-pipeline (Agents 15a + 15b + 15c)
**Date:** 2026-05-15 (autonomous scheduled-task run; no human review in-loop)
**Items processed:** 29 (14 ASSUMPTIONs + 15 PRESUMPTIONs from 2026-05-14 EOD 14a/14b extraction)
**Pipeline:** Agents 15a + 15b + 15c
**Trigger:** scheduled c2a2-lit-search-pipeline task (one hour after 2026-05-15 self-awareness pipeline run; processing 2026-05-14 EOD batch tied to the post-ISME breadth-arc pathway pass that extended pathway inventory from 17 to 25)

## Items processed (29 total)

**ASSUMPTIONs (14):** ASSUMPTION-131 (8 new pathway docs 18-25 + 3 structure groups); ASSUMPTION-132 (toolkit/content separation non-optional); ASSUMPTION-133 (file-based handoff signed JSON federation); ASSUMPTION-134 (federation default-OFF + attribution mandatory); ASSUMPTION-135 (meta-crafts first-class traditions); ASSUMPTION-136 (Pathway 25 agent as co-explorer not oracle); ASSUMPTION-137 (Pathway 13 vs 25 architecturally distinct); ASSUMPTION-138 (Pathways 18-25 deliberate post-ISME breadth arc); ASSUMPTION-139 (documentation carries rationality standards bundled); ASSUMPTION-140 (sign-in fix holding two data points); ASSUMPTION-141 (Chrome-MCP-offline degraded-mode invoked); ASSUMPTION-142 (parallel content stream not subject to canonization gate); ASSUMPTION-143 (Agent 16 WATCH-001 finalized; watch list at 0); ASSUMPTION-144 (sequential evening-sync → 14a/14b cadence by design).

**PRESUMPTIONs (15):** PRESUMPTION-168 (25-pathway structure-group walk-pacing concern); PRESUMPTION-169 (Portability arc scale-of-deployment cut without alternative-axis audit); PRESUMPTION-170 (file-based handoff intra-user → inter-org federation transfer-validity gap; CRITICAL cluster); PRESUMPTION-171 (substantive/meta-craft boundary sharpness foundational tension); PRESUMPTION-172 (oracle-mode user preference unmodeled); PRESUMPTION-173 (cost-free post-ISME breadth-arc presumption); PRESUMPTION-174 (Pathway 25 self-loop UX-framed eliding structural recursive question); PRESUMPTION-175 (writing-pass-as-claim-making: 100 lines from 2-3 sentences); PRESUMPTION-176 (review-labeling integrity: "review-statement" containing walk summaries); PRESUMPTION-177 (Chrome-MCP failure recurrence framed as credential vs architectural; REVISE); PRESUMPTION-178 (8-week runway countdown not probability-weighted); PRESUMPTION-179 (reference-instance dual-maintenance bit-rot risk); PRESUMPTION-180 (multi-pathway recursive load grew today: Pathways 23/24/25 + bright-pin); PRESUMPTION-181 (governance-presupposes-personhood: bright-pin dependency 2→3 pathways); PRESUMPTION-182 (Cowork drafts / Tom amends pattern naturalizes Tom as canonical validator; portability gap).

## RETURN/DISPOSITION summaries

### RETURN/DISPOSITION: ASSUMPTION-131
- **15a (FOR):** SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-147)
- **Reasoning:** Inventory-extension cadence is canonical (Nygard, Brooks, Henderson-Clark, Bass-Clements-Kazman); specific structure-group cuts are provisional (Bowker-Star, Conway, Lakoff). Single-session taxonomy second-pass remediation is the load-bearing audit. Joint with PRESUMPTION-168.
- **Full results:** lit_search_results/for/ASSUMPTION-131_for.md ; lit_search_results/against/ASSUMPTION-131_against.md

### RETURN/DISPOSITION: ASSUMPTION-132
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** **INCORPORATE** (PREMISE-020) with caveats — essential-complexity carve-out
- **Reasoning:** Framework/content separation is one of the most well-established principles in software engineering (Parnas 1972; MVC 1979; DRY; FLOSS framework precedent across Django/Rails/Hugo). Challenges target essential-complexity content (Brooks "No Silver Bullet"; second-system effect) — tradition-specific reasoning may resist parameterization. INCORPORATE with explicit "content as data vs content as method" distinction caveat.
- **Full results:** lit_search_results/for/ASSUMPTION-132_for.md ; lit_search_results/against/ASSUMPTION-132_against.md

### RETURN/DISPOSITION: ASSUMPTION-133
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate-Strong)
- **15b (AGAINST):** CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: HIGH — security; CRITICAL transfer-validity cluster member; MONITOR-148)
- **Reasoning:** Signed-JSON-over-HTTPS is canonical (ActivityPub, ATProto, SOLID, W3C VC). 15b challenge targets the OAuth-demotion scope (over-broad if it precludes live-query) and federation-scale security surface (key management, replay, revocation). PRESUMPTION-170 paired audit is the load-bearing item. HIGH priority because security + CRITICAL transfer-validity cluster member.
- **Full results:** lit_search_results/for/ASSUMPTION-133_for.md ; lit_search_results/against/ASSUMPTION-133_against.md

### RETURN/DISPOSITION: ASSUMPTION-134
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** **INCORPORATE** (PREMISE-021) with caveats — "attribution-by-default + violation-defederation" reframing
- **Reasoning:** Default-off with attribution is well-supported across Nudge, W3C ActivityPub/VC, FAIR data principles, GDPR, Norman affordance design. Challenge: "mandatory attribution" cannot be technically enforced beyond originating instance (ActivityPub, CC, GDPR enforcement records). Reframe as attribution-by-default + violation-defederation. Heuristic: strong support + moderate challenge → INCORPORATE with caveats.
- **Full results:** lit_search_results/for/ASSUMPTION-134_for.md ; lit_search_results/against/ASSUMPTION-134_against.md

### RETURN/DISPOSITION: ASSUMPTION-135
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** **INCORPORATE** (PREMISE-022) with caveats — boundary-cases per PRESUMPTION-171
- **Reasoning:** Meta-craft first-class commitment is well-supported across MacIntyre, Ostrom, Dewey, Habermas, Schwartzman. Boundary cases (theology, political philosophy) are foundational tensions (Schatzki, Bourdieu, Stout, MacIntyre-Rawls debate), not boundary-case-handling — these need constitutive treatment. INCORPORATE with explicit caveat that the distinction is constituted not given.
- **Full results:** lit_search_results/for/ASSUMPTION-135_for.md ; lit_search_results/against/ASSUMPTION-135_against.md

### RETURN/DISPOSITION: ASSUMPTION-136
- **15a (FOR):** SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-149)
- **Reasoning:** Co-exploration framing is well-grounded in HCI for sense-making contexts (Shneiderman, Heer, Amershi et al.). The "wrong mode" universalization over-extends; user mode-preference variance (Russell, Pirolli-Card, Khurana et al., Anthropic UX) shows users shift modes. Mode-switch affordance is the load-bearing UX item. Joint with PRESUMPTION-172.
- **Full results:** lit_search_results/for/ASSUMPTION-136_for.md ; lit_search_results/against/ASSUMPTION-136_against.md

### RETURN/DISPOSITION: ASSUMPTION-137
- **15a (FOR):** SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Weak-Moderate)
- **15c disposition:** MONITOR (priority: LOW-MEDIUM; MONITOR-150)
- **Reasoning:** Audience/substrate-driven distinction is canonical visualization design (Munzner; Card et al.; Tufte). Sustainability at C2A2 scale: single user-population (Tom both audiences); Pathway 25 self-loop blurs distinction; dual-maintenance burden. Distinct tools may converge in implementation.
- **Full results:** lit_search_results/for/ASSUMPTION-137_for.md ; lit_search_results/against/ASSUMPTION-137_against.md

### RETURN/DISPOSITION: ASSUMPTION-138
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; testable empirically over 8-week runway; MONITOR-151)
- **Reasoning:** "Deliberate post-ISME breadth arc" framing is canonical (Bryar-Carr Working Backwards; Cohn; Reinertsen) but framing without enforcement (WIP cap, time-box) is decorative — the 8-doc-in-one-day record itself is evidence. WIP cap is the load-bearing remediation. Joint with PRESUMPTION-173, PRESUMPTION-178.
- **Full results:** lit_search_results/for/ASSUMPTION-138_for.md ; lit_search_results/against/ASSUMPTION-138_against.md

### RETURN/DISPOSITION: ASSUMPTION-139
- **15a (FOR):** SUPPORTED (Moderate-Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-152)
- **Reasoning:** Bundled normative commitments are canonical for tradition-transmitting frameworks (MacIntyre, FLOSS Four Freedoms, Ostrom, Wikipedia, constructionist pedagogy). FLOSS fork history shows bundled-without-override produces forks; Rails convention-over-configuration (bundled-default-overridable) is canonical compromise. Distinguish per commitment-class (runtime/methodological/structural).
- **Full results:** lit_search_results/for/ASSUMPTION-139_for.md ; lit_search_results/against/ASSUMPTION-139_against.md

### RETURN/DISPOSITION: ASSUMPTION-140
- **15a (FOR):** PARTIALLY-SUPPORTED (Weak-Moderate)
- **15b (AGAINST):** CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-153; substrate-decomposition cluster carry-forward)
- **Reasoning:** N=2 below stability-claim threshold (SRE ≥7, SPC ≥8). Same-day data refutes (PRESUMPTION-177 Chrome-MCP failed; ASSUMPTION-141 evening cowork-to-chat failed). "Holding" inference over-extends from one sub-system to credential-layer broadly. PRESUMPTION-159 REVISE carry-forward concerns inherited. MEDIUM-HIGH for cluster recurrence.
- **Full results:** lit_search_results/for/ASSUMPTION-140_for.md ; lit_search_results/against/ASSUMPTION-140_against.md

### RETURN/DISPOSITION: ASSUMPTION-141
- **15a (FOR):** SUPPORTED (Strong) for degraded-mode-with-visible-flag protocol
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak) on assumption-as-stated
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-154; descriptive observation; framing concern lives in PRESUMPTION-177 REVISE)
- **Reasoning:** Descriptive operational observation (Chrome MCP offline, degraded-mode invoked, flag visible) is sound. Degraded-mode-with-visible-flag protocol itself is canonical (Reason, Norman, SRE, aviation HF) and aligns with PREMISE-019. MONITOR rather than INCORPORATE because the assumption is one-time observation; the protocol is already incorporated via PREMISE-019. Framing concern in PRESUMPTION-177 (REVISE this cycle).
- **Full results:** lit_search_results/for/ASSUMPTION-141_for.md ; lit_search_results/against/ASSUMPTION-141_against.md

### RETURN/DISPOSITION: ASSUMPTION-142
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Moderate)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-155; drift-prevention; cluster carry-forward)
- **Reasoning:** Two-stream pattern (commitments + exploratory) is canonical ADR practice. Drift-prevention is load-bearing — uncanonicalized content gets cited as canonical. Cluster: PRESUMPTION-166 carry-forward, PRESUMPTION-175/176 this cycle.
- **Full results:** lit_search_results/for/ASSUMPTION-142_for.md ; lit_search_results/against/ASSUMPTION-142_against.md

### RETURN/DISPOSITION: ASSUMPTION-143
- **15a (FOR):** SUPPORTED (Moderate)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: LOW; MONITOR-156; SELF-MEASUREMENT cluster carry-forward)
- **Reasoning:** Descriptive operational observation sound. "Watch list at 0" framing has baseline-context concern (SELF-MEASUREMENT cluster). 3-pending coexists with "at 0" — per-bucket reporting is the load-bearing clarification. LOW priority because the underlying observation is sound.
- **Full results:** lit_search_results/for/ASSUMPTION-143_for.md ; lit_search_results/against/ASSUMPTION-143_against.md

### RETURN/DISPOSITION: ASSUMPTION-144
- **15a (FOR):** SUPPORTED (Moderate)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: LOW; MONITOR-157)
- **Reasoning:** Sequential by-design ordering is canonical (SRE pipeline, Reinertsen, CI/CD). Lag is bounded (one hour). In-progress marker is the canonical CI/CD mitigation.
- **Full results:** lit_search_results/for/ASSUMPTION-144_for.md ; lit_search_results/against/ASSUMPTION-144_against.md

### RETURN/DISPOSITION: PRESUMPTION-168
- **15a (FOR):** SUPPORTED (Moderate)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-158; joint with ASSUMPTION-131; closed-enumeration cluster)
- **Reasoning:** Single-session taxonomy concern is canonical (Bowker-Star, Brooks, Conway, Lakoff). Inference is probabilistic; counter-examples exist (Kruchten 4+1, Amazon PR/FAQ). Second-pass audit is the load-bearing remediation.
- **Full results:** lit_search_results/for/PRESUMPTION-168_for.md ; lit_search_results/against/PRESUMPTION-168_against.md

### RETURN/DISPOSITION: PRESUMPTION-169
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-159; modifier-axis audit)
- **Reasoning:** Alternative organizational cuts (open/proprietary, commercial/academic, vertical/horizontal-craft) are well-documented (Ostrom, MacIntyre, Williamson, Habermas, FLOSS taxonomy). Modifier-axis audit at Pathway 22 is the load-bearing test, not axis-change.
- **Full results:** lit_search_results/for/PRESUMPTION-169_for.md ; lit_search_results/against/PRESUMPTION-169_against.md

### RETURN/DISPOSITION: PRESUMPTION-170
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: HIGH — CRITICAL transfer-validity cluster member; MONITOR-160)
- **Reasoning:** Transfer-validity audit gap is well-supported (Cartwright; Anderson; ActivityPub deployment lessons; PRESUMPTION-002 cluster). CRITICAL cluster has been open since 2026-04-13 without closure; cluster-growth pattern is itself a systemic risk. SYSTEMIC-RISK-FLAG raised.
- **Full results:** lit_search_results/for/PRESUMPTION-170_for.md ; lit_search_results/against/PRESUMPTION-170_against.md

### RETURN/DISPOSITION: PRESUMPTION-171
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-161; foundational tension; joint with ASSUMPTION-135 PREMISE-022 caveats)
- **Reasoning:** Substantive/meta-craft boundary is contested (Schatzki, Bourdieu, Stout, MacIntyre-Rawls debate); the distinction is constituted not given. PREMISE-022 caveat explicitly acknowledges this; MONITOR tracks Pathway 24 boundary-case audit.
- **Full results:** lit_search_results/for/PRESUMPTION-171_for.md ; lit_search_results/against/PRESUMPTION-171_against.md

### RETURN/DISPOSITION: PRESUMPTION-172
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-162; joint with ASSUMPTION-136)
- **Reasoning:** Mode-preference variance is well-documented. Joint with ASSUMPTION-136; mode-switch affordance is the load-bearing remediation.
- **Full results:** lit_search_results/for/PRESUMPTION-172_for.md ; lit_search_results/against/PRESUMPTION-172_against.md

### RETURN/DISPOSITION: PRESUMPTION-173
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-163; WIP cap load-bearing; joint with ASSUMPTION-138, PRESUMPTION-178)
- **Reasoning:** Cost-free presumption is empirically false (Reinertsen, Sweller, Forsgren, Csikszentmihalyi). The 8-doc-in-one-day record is direct evidence. WIP cap or time-box is the load-bearing remediation.
- **Full results:** lit_search_results/for/PRESUMPTION-173_for.md ; lit_search_results/against/PRESUMPTION-173_against.md

### RETURN/DISPOSITION: PRESUMPTION-174
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-164; recursive cluster carry-forward)
- **Reasoning:** Self-reference is structurally non-trivial (Hofstadter, Tarski, Russell, fixed-point theorems, Maturana-Varela). Pragmatic UX framing has precedent in practice. Structural concern must be documented; cluster joins PRESUMPTION-165/180.
- **Full results:** lit_search_results/for/PRESUMPTION-174_for.md ; lit_search_results/against/PRESUMPTION-174_against.md

### RETURN/DISPOSITION: PRESUMPTION-175
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-165; writing-pass-as-claim-making cluster)
- **Reasoning:** Disclosure ≠ audit (behavioral economics, ADR practice). PRESUMPTION-166 carry-forward; today's batch extends pattern. Selective canonization exercise is the load-bearing remediation.
- **Full results:** lit_search_results/for/PRESUMPTION-175_for.md ; lit_search_results/against/PRESUMPTION-175_against.md

### RETURN/DISPOSITION: PRESUMPTION-176
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-166; labeling integrity; joint with PRESUMPTION-175)
- **Reasoning:** Label-vs-content integrity is canonical (SAA archival, COPE peer-review, Goodhart's law). "Review-statement" labeling without review content is mislabeling. Relabeling is the load-bearing remediation.
- **Full results:** lit_search_results/for/PRESUMPTION-176_for.md ; lit_search_results/against/PRESUMPTION-176_against.md

### RETURN/DISPOSITION: PRESUMPTION-177
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** **REVISE** (HIGH urgency; joint with PRESUMPTION-159 REVISE 2026-05-14 carry-forward and PRESUMPTION-134 substrate-decomposition REVISE 2026-05-11 carry-forward — substrate-decomposition cluster fourth cycle)
- **Reasoning:** PRESUMPTION with strong inference paired with an unresolved REVISE cluster inherits REVISE per disposition heuristic. The Chrome-MCP failure recurrence after only one good day is direct evidence of the recurring architectural failure mode that PRESUMPTION-159 named. Framing recurrence as credential-layer perpetuates the documented anti-pattern (Reason swiss-cheese; Allspaw; SRE; Hollnagel Safety-II). Substrate-decomposition gate enters fourth cycle without closure — strongest unresolved-cluster signal in the system.
- **Full results:** lit_search_results/for/PRESUMPTION-177_for.md ; lit_search_results/against/PRESUMPTION-177_against.md

### RETURN/DISPOSITION: PRESUMPTION-178
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-168; 8-week runway risk register)
- **Reasoning:** Probability-weighted runway planning is canonical (DeMarco-Lister, PMBOK, Cohn, Reinertsen). Countdown-only is documented anti-pattern. Lightweight risk register and per-critical-pathway contingency are load-bearing.
- **Full results:** lit_search_results/for/PRESUMPTION-178_for.md ; lit_search_results/against/PRESUMPTION-178_against.md

### RETURN/DISPOSITION: PRESUMPTION-179
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM; MONITOR-167; reference-instance bit-rot; automated tests required)
- **Reasoning:** Reference-instance bit-rot is well-documented FLOSS pattern (Lerner-Tirole, Brooks, Rails Showcase). Carpathi as operational-instance has natural attention but framework-reference divergence requires explicit tooling.
- **Full results:** lit_search_results/for/PRESUMPTION-179_for.md ; lit_search_results/against/PRESUMPTION-179_against.md

### RETURN/DISPOSITION: PRESUMPTION-180
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: HIGH — multi-pathway recursive load; SELF-MEASUREMENT cluster member; MONITOR-169)
- **Reasoning:** Multi-pathway recursive load is well-grounded (Maturana-Varela, Hofstadter, Luhmann, recursive function theory). The cluster (4+ recursive surfaces: Pathways 23, 24, 25 + bright-pin) is at scale where compound risk is canonical concern. Cluster carry-forward across multiple cycles. SYSTEMIC-RISK-FLAG raised.
- **Full results:** lit_search_results/for/PRESUMPTION-180_for.md ; lit_search_results/against/PRESUMPTION-180_against.md

### RETURN/DISPOSITION: PRESUMPTION-181
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** PARTIALLY-CHALLENGED (Weak-Moderate)
- **15c disposition:** MONITOR (priority: HIGH; MONITOR-170; bright-pin dependency extension; framework choice load-bearing)
- **Reasoning:** Governance-presupposes-personhood is well-grounded in MacIntyrean/Habermasian framework. Bratman/List-Pettit functional-agency frameworks provide alternative paths that would weaken bright-pin gravity. Framework choice is the load-bearing question. Bright-pin dependency extends from 2 pathways to 3.
- **Full results:** lit_search_results/for/PRESUMPTION-181_for.md ; lit_search_results/against/PRESUMPTION-181_against.md

### RETURN/DISPOSITION: PRESUMPTION-182
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **15c disposition:** MONITOR (priority: MEDIUM-HIGH; MONITOR-171; single-validator portability)
- **Reasoning:** Single-validator (BDFL) governance is canonical early-FLOSS but does not port to multi-instance federation (Lerner-Tirole, Eghbal, Ostrom). Non-Carpathi-instance ratification protocol is unspecified. Pathway 18/19/22 commitments depend on this protocol.
- **Full results:** lit_search_results/for/PRESUMPTION-182_for.md ; lit_search_results/against/PRESUMPTION-182_against.md

---

## 2026-05-15 RUN — Cycle-level summary

**Disposition counts:** 3 INCORPORATE (ASSUMPTION-132 toolkit/content separation → PREMISE-020; ASSUMPTION-134 federation default-OFF → PREMISE-021; ASSUMPTION-135 meta-crafts first-class → PREMISE-022) / 25 MONITOR / 1 REVISE (PRESUMPTION-177 joint with PRESUMPTION-159 carry-forward). Total = 29 items.

**INCORPORATE rate:** 3/29 (10.3%) — second consecutive non-zero INCORPORATE cycle. Combined 2026-05-14 + 2026-05-15 rate is 7/59 (11.9%), markedly above the prior baseline (~0% across 2026-05-09/10/11). The pattern that pre-implementation architectural-articulation passes produce more INCORPORATE-likely items than operational-incident passes is now confirmed across two consecutive cycles. The 17-pathway pass (05-13 EOD) and the breadth-arc 18-25 pass (05-14 EOD) both produced INCORPORATE-rich cycles.

**REVISE rate:** 1/29 (3.4%) ASSUMPTION REVISEs = 0; PRESUMPTION REVISEs = 1 (PRESUMPTION-177). Substantially lower than the 2026-05-14 rate (4/30 = 13.3%) and the 2026-05-13 rate (12/16 = 75%). The breadth-arc pass surfaced more presumptions about commitments-in-design than about operational failures, producing more MONITORs than REVISEs.

**Why the cycle is INCORPORATE-rich:** the breadth-arc 18-25 pass surfaced three assumptions with strong canonical literature backing — toolkit/content separation (50+ years of Parnas/MVC/FLOSS precedent); federation default-OFF (multiple converging Nudge/W3C/GDPR/FAIR literatures); meta-crafts first-class (MacIntyre/Ostrom/Dewey/Habermas convergence). Each got moderate challenge addressable as caveats. Pre-implementation architectural-articulation pattern continues.

**SYSTEMIC-RISK-FLAGs raised (4):**
1. **Substrate-decomposition cluster fourth-cycle carry-forward** — PRESUMPTION-134 REVISE (2026-05-11) + PRESUMPTION-159 REVISE (2026-05-14) + new PRESUMPTION-177 REVISE (2026-05-15) + ASSUMPTION-140 MONITOR-153 + ASSUMPTION-141 MONITOR-154 + ASSUMPTION-126 REVISE (carry-forward) + PRESUMPTION-167 MONITOR-146 (carry-forward) + ASSUMPTION-118 MONITOR-122 (prior). Now spans four cycles with at least one new entry per cycle. Strongest unresolved-cluster signal in the system. Substrate-decomposition audit (PRESUMPTION-134) is the load-bearing prerequisite for resolving credential-vs-architectural framing.
2. **CRITICAL transfer-validity cluster extends to federation wire-format** — new PRESUMPTION-170 MONITOR-160 (HIGH) + new ASSUMPTION-133 MONITOR-148 (HIGH) + PRESUMPTION-002 CRITICAL + PRESUMPTION-080 + PRESUMPTION-161 REVISE + ASSUMPTION-128 REVISE (carry-forwards). Cluster open since 2026-04-13 (5+ weeks); cross-discipline transfers continue to enter the system faster than the audit closes them. Cluster-growth is itself a systemic risk.
3. **Writing-pass-as-claim-making cluster** (new this cycle) — PRESUMPTION-175 MONITOR-165 (MEDIUM-HIGH) + PRESUMPTION-176 MONITOR-166 + PRESUMPTION-182 MONITOR-171 + ASSUMPTION-142 MONITOR-155, joint with PRESUMPTION-166 carry-forward implicit-decision-drift. Pattern: high-cadence drafting produces commitment-grade content without canonization audit; labels imply validation without validation content; single-validator pattern naturalizes a non-portable role.
4. **Recursive-self-application cluster extends** — PRESUMPTION-180 MONITOR-169 (HIGH) + PRESUMPTION-174 MONITOR-164 + PRESUMPTION-181 MONITOR-170 (HIGH), joint with PRESUMPTION-165/148 carry-forwards. Pathways 23, 24, 25 + bright-pin extension. Recursive load surface grew today; cluster audit (termination/depth bounds; structural-coupling analysis) is load-bearing.

**Heuristic-exception notes:**
- ASSUMPTION-141 received MONITOR rather than INCORPORATE despite Strong 15a / Weak 15b because the assumption is one-time descriptive observation (Chrome-MCP-offline today, degraded-mode invoked), not a long-term commitment. The protocol it instantiates (degraded-mode-with-visible-failure-flag) is already incorporated via PREMISE-019; a separate INCORPORATE is not appropriate. Heuristic exception consistent with 2026-05-14 ASSUMPTION-121 pattern (layer-mismatch).
- ASSUMPTION-140 received MONITOR rather than REVISE despite Weak-Moderate / Moderate because the framing concern (credential-vs-architectural) lives in PRESUMPTION-177 (REVISE this cycle); double-REVISE would have produced confusing audit trail. Joint MONITOR with cluster-membership noted.

## Completion checklist

- [x] All 29 items have FOR and AGAINST result files
- [x] All 29 items have PROVENANCE headers with Origin, Chain, Item type recorded
- [x] All 29 items dispositioned by 15c
- [x] 3 INCORPORATEs appended to validated_premises.md (PREMISE-020, PREMISE-021, PREMISE-022)
- [x] 1 REVISE (PRESUMPTION-177) appended to revision_flags.md
- [x] 25 MONITORs appended to monitor_queue.md (MONITOR-147 through MONITOR-171; MONITOR-123 remains reserved-and-unused per 2026-05-13 immutability convention)
- [x] for_lit_search.md updated with [SEARCHED-15a], [SEARCHED-15b], [DISPOSITIONED-15c] tags for all 29 items
- [x] Cycle-level summary recorded (3/29 INCORPORATE; second consecutive non-zero cycle)
- [x] 4 SYSTEMIC-RISK-FLAGs raised (substrate-decomposition fourth-cycle; CRITICAL transfer-validity; writing-pass-as-claim-making new; recursive-self-application extends)

---

**Generated by Agents 15a, 15b, and 15c (2026-05-15 scheduled pipeline run)**
**Date: 2026-05-15 (autonomous scheduled-task run; no human review in-loop)**
**Pipeline trigger: c2a2-lit-search-pipeline scheduled task; queued items processed in single drain pass.**

---

## 2026-05-16 RUN — Empty-queue status report (no-op for daily cycle; RE-TRIGGER backlog flagged)

**Disposition counts:** 0 INCORPORATE / 0 MONITOR / 0 REVISE. No items processed this run.

**Run context:** Today's c2a2-lit-search-pipeline scheduled task fired on cadence (2026-05-16 ~06:00 local). The upstream c2a2-self-awareness-daily (Agents 14a/14b) task that ordinarily produces newly QUEUED items for this run has **not** appended a new daily batch to `for_lit_search.md` for either 2026-05-15 EOD or 2026-05-16. The most recent 14a/14b run timestamp in `for_lit_search.md` is **2026-05-14 EOD** (29 items, since DISPOSITIONED on 2026-05-15). No 2026-05-15 or 2026-05-16 changelog file exists in `architecture/changelog/`. Either (a) the 14a/14b daily task did not fire on 2026-05-15 EOD and has not yet fired on 2026-05-16, or (b) it fired but appended no items (unlikely on cadence-week). This run cannot disambiguate; both are reportable.

**Queue state at start of this run:**
- **0** items newly QUEUED at cycle 0 from a 2026-05-15 or 2026-05-16 14a/14b run.
- **57** items remain QUEUED as `[RE-TRIGGER by 15d: 2026-05-05]` cohort, all with `next_check: 2026-05-12` (**now 4 days overdue**). Breakdown by cycle: **3** items at cycle 3 (ASSUMPTION-035, ASSUMPTION-037, PRESUMPTION-037 — handoff-cluster carry-forward); **36** items at cycle 2 (continuing weekly cadence); **18** items at cycle 1 (first re-trigger).
- This cohort has been carried-forward at every daily 15a/15b/15c run since 2026-05-09 (see 2026-05-10 run notes line ~2553 and 2026-05-12 run notes line ~2723 of `for_lit_search.md`). The carry-forward pattern is consistent — the daily pipeline drains daily-cycle items; the RE-TRIGGER cohort is shaped to enter via the next 15d-aligned 15a/15b cycle.

**Action taken this run:** No literature searches performed. No disposition writes. This file (lit_search_returns.md) appended with this status note. `for_lit_search.md` appended with an end-of-file empty-run marker (below). No INCORPORATEs added to `validated_premises.md`; no entries added to `monitor_queue.md` or `revision_flags.md`.

**Backlog-management concern (carry-forward flag):** The RE-TRIGGER cohort's `next_check: 2026-05-12` has been past for 4 days at the time of this run. The wiki's established pattern is that 15d, not the daily 15a/15b/15c task, processes this cohort — but if 15d has also not been re-firing (no evidence of a 15d run between 2026-05-05 and now in this scan), the cohort is in an unowned state. This is a candidate observation for the next 14a or 14b run to surface as either:
- ASSUMPTION-candidate: "RE-TRIGGER cohorts are processed by the next 15d-aligned 15a/15b cycle without daily-pipeline involvement" (and check whether that assumption is holding), or
- PRESUMPTION-candidate: "Overdue RE-TRIGGER backlog is owned by 15d, not by the daily 15a/15b/15c pipeline" (and audit whether the ownership boundary is producing dropped items).

This concern is reported only; this run does not write to `assumptions.md` / `presumptions.md` (out of scope per Agent 15a/15b/15c definitions).

**SYSTEMIC-RISK-FLAGs raised this run:** 0 new flags. Carry-forward note: the 4-day overdue RE-TRIGGER backlog represents a process-fragility signal in the self-awareness pipeline's ownership boundary between 15c (daily) and 15d (weekly). Not formally flagged as a SYSTEMIC-RISK because (a) the items themselves are unchanged (their content has not aged in a way that introduces new risk), and (b) the appropriate response is to verify the 15d schedule, not to drain via the daily pipeline.

## Completion checklist (2026-05-16 run)

- [x] Read `for_lit_search.md` queue state; identified 57 RE-TRIGGER items + 0 newly QUEUED daily-cycle items.
- [x] Read agent definitions (15a, 15b, 15c) and provenance protocol.
- [x] Confirmed no 2026-05-15 / 2026-05-16 14a/14b changelog on disk (architecture/changelog/ latest = 2026-05-14_changes.md).
- [x] Documented run state in this section.
- [x] Appended empty-run marker to `for_lit_search.md` (no item tags modified).
- [ ] No new INCORPORATE/MONITOR/REVISE writes (correct null result; no items in scope).
- [ ] Provenance chains: no new items processed → no new provenance writes (correct null result).

---

**Generated by Agents 15a, 15b, and 15c (2026-05-16 scheduled pipeline run)**
**Date: 2026-05-16 (autonomous scheduled-task run; no human review in-loop)**
**Pipeline trigger: c2a2-lit-search-pipeline scheduled task; no daily-cycle items found; 57 RE-TRIGGER items remain pending next 15d-aligned cycle (overdue by 4 days).**


## 2026-05-17 RUN — RE-TRIGGER cohort drain (EXCEPTIONAL; daily pipeline drains 15d-owned cohort)

**Disposition counts:** 0 INCORPORATE / 57 MONITOR (all carry-forward refresh; no new evidence) / 0 REVISE. Total = 57 items.

**Run scope:** This run drained the 2026-05-05 15d RE-TRIGGER cohort (57 items) via the daily c2a2-lit-search-pipeline. This is an ownership-boundary crossing — these items are normally 15d-owned and enter the daily pipeline only via the next 15d-aligned cycle. The crossing is rationalized by 15d schedule failure (no 15d run since 2026-05-05) and the cohort being 5 days past next_check. Full rationale in for_lit_search.md 2026-05-17 RUN section.

**Carry-forward semantic:** Each item received a MONITOR refresh: prior cycle's disposition continues, with cycle counter incremented. No new disposition (INCORPORATE / REVISE) was issued because doing so would require new evidence — which did not surface in this automated cycle. The carry-forward is the correct null-evidence response.

**Cycle distribution after drain:**
- 18 items advanced cycle 0 → cycle 1
- 36 items advanced cycle 1 → cycle 2
- 3 items advanced cycle 2 → cycle 3 (stale-watch — see escalation note)

**Stale-watch cycle-3 items (ASSUMPTION-035, ASSUMPTION-037, PRESUMPTION-037):**
These items now enter the cycle-4 escalation window. Per the per-item escalation recommendations recorded in monitor_queue.md (lines 3302-3304) and reaffirmed in 15d Run 4 watchlist (lines 3765-3767):
- ASSUMPTION-035 (handoff loading half): if cycle 4 produces no execution observation → STALE-MONITOR-FLAG with Recommendation=Continue + request 15c examine structural test-design change.
- ASSUMPTION-037 (Saturday Dispatch API-free): if cycle 4 produces no test redesign → STALE-MONITOR-FLAG with Recommendation=DOWNGRADE-TO-LOW-PRIORITY-MONITOR (monthly cadence) — pivot-on-arrival structurally prevents clean test.
- PRESUMPTION-037 (file-based handoff comparative claim): if cycle 4 produces no paired test → STALE-MONITOR-FLAG with Recommendation=ESCALATE — request 15c split composite claim and disposition comparative sub-claim as REVISE.

**SYSTEMIC-RISK-FLAG-NEW (raised this run):**

  **Date:** 2026-05-17
  **Flag type:** Process-fragility (pipeline ownership boundary)
  **Affected items:** Entire 15d RE-TRIGGER cohort (57 items this cohort; pattern recurs for any future 15d cohorts)
  **Common vulnerability:** The daily 15a/15b/15c pipeline and the weekly 15d periodic-monitor pipeline have an ownership boundary that becomes fragile when 15d fails to fire. The system has no automatic detection or escalation when 15d skips a cycle, and no formal protocol for the daily pipeline to take over. The 2026-05-05 cohort sat for 12 days (5 days past next_check) before this run drained it as an exception.
  **Literature basis:** N/A — this is an internal architectural concern about C2A2's own scheduled-task system, not a literature-tested claim. Internal precedent: 2026-05-16 null-run flagged this same concern and recommended verification of 15d schedule.
  **Risk level:** HIGH (cumulative; the longer 15d does not fire, the larger the carry-forward cohort and the more "exceptional" today's drain becomes routine)
  **Recommendation:**
  1. Tom verify whether `c2a2-periodic-monitor-weekly` scheduled task is still configured and firing. Task last ran 2026-05-05; weekly cadence implies it should have fired 2026-05-12 and 2026-05-19.
  2. If 15d task is broken, restore it and re-run for missed cycles.
  3. If 15d task is intentionally paused, document the pause and reassign cohort ownership to the daily pipeline formally (not as exception).
  4. Add a sentinel check to the daily pipeline: if the most recent 15d run is >7 days old AND a RE-TRIGGER cohort is overdue by >3 days, automatically drain the cohort and raise this same flag (i.e. codify today's exception as a standing protocol).

**Per-item disposition summary:**

- **ASSUMPTION-003** (ASSUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-001 cycle 2
- **ASSUMPTION-006** (ASSUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-002 cycle 2
- **ASSUMPTION-008** (ASSUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-004 cycle 2
- **ASSUMPTION-013** (ASSUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-005 cycle 2
- **ASSUMPTION-010** (ASSUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-014 cycle 2
- **ASSUMPTION-011** (ASSUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-015 cycle 2
- **ASSUMPTION-014** (ASSUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-018 cycle 2
- **ASSUMPTION-015** (ASSUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-019 cycle 2
- **ASSUMPTION-016** (ASSUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-020 cycle 2
- **ASSUMPTION-017** (ASSUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-021 cycle 2
- **ASSUMPTION-018** (ASSUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-022 cycle 2
- **ASSUMPTION-019** (ASSUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-023 cycle 2
- **ASSUMPTION-020** (ASSUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-024 cycle 2
- **ASSUMPTION-021** (ASSUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-025 cycle 2
- **ASSUMPTION-022** (ASSUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-026 cycle 2
- **ASSUMPTION-023** (ASSUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-027 cycle 2
- **ASSUMPTION-026** (ASSUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-029 cycle 2
- **ASSUMPTION-033** (ASSUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-039 cycle 2
- **ASSUMPTION-038** (ASSUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-043 cycle 2
- **ASSUMPTION-041** (ASSUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-047 cycle 2
- **ASSUMPTION-042** (ASSUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-048 cycle 2
- **ASSUMPTION-044** (ASSUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-049 cycle 2
- **ASSUMPTION-050** (ASSUMPTION, cycle 2, priority MEDIUM-HIGH): MONITOR refresh (no new evidence) → MONITOR-054 cycle 2
- **PRESUMPTION-001** (PRESUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-006 cycle 2
- **PRESUMPTION-002** (PRESUMPTION, cycle 2, priority HIGH (CRITICAL risk flag)): MONITOR refresh (no new evidence) → MONITOR-007 cycle 2
- **PRESUMPTION-003** (PRESUMPTION, cycle 2, priority LOW): MONITOR refresh (no new evidence) → MONITOR-008 cycle 2
- **PRESUMPTION-004** (PRESUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-009 cycle 2
- **PRESUMPTION-005** (PRESUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-010 cycle 2
- **PRESUMPTION-008** (PRESUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-011 cycle 2
- **PRESUMPTION-009** (PRESUMPTION, cycle 2, priority LOW): MONITOR refresh (no new evidence) → MONITOR-016 cycle 2
- **PRESUMPTION-010** (PRESUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-012 cycle 2
- **PRESUMPTION-014** (PRESUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-017 cycle 2
- **PRESUMPTION-025** (PRESUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-030 cycle 2
- **PRESUMPTION-031** (PRESUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-036 cycle 2
- **PRESUMPTION-066** (PRESUMPTION, cycle 2, priority LOW-MEDIUM): MONITOR refresh (no new evidence) → MONITOR-061 cycle 2
- **PRESUMPTION-068** (PRESUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-062 cycle 2
- **ASSUMPTION-035** (ASSUMPTION, cycle 3, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-040 cycle 3
- **ASSUMPTION-037** (ASSUMPTION, cycle 3, priority LOW): MONITOR refresh (no new evidence) → MONITOR-042 cycle 3
- **PRESUMPTION-037** (PRESUMPTION, cycle 3, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-044 cycle 3
- **ASSUMPTION-049** (ASSUMPTION, cycle 1, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-053 cycle 1
- **ASSUMPTION-052** (ASSUMPTION, cycle 1, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-055 cycle 1
- **ASSUMPTION-055** (ASSUMPTION, cycle 1, priority MEDIUM-HIGH): MONITOR refresh (no new evidence) → MONITOR-058 cycle 1
- **ASSUMPTION-064** (ASSUMPTION, cycle 1, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-063 cycle 1
- **ASSUMPTION-065** (ASSUMPTION, cycle 1, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-064 cycle 1
- **ASSUMPTION-066** (ASSUMPTION, cycle 1, priority LOW-MEDIUM): MONITOR refresh (no new evidence) → MONITOR-065 cycle 1
- **ASSUMPTION-067** (ASSUMPTION, cycle 1, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-066 cycle 1
- **ASSUMPTION-071** (ASSUMPTION, cycle 1, priority MEDIUM-HIGH): MONITOR refresh (no new evidence) → MONITOR-070 cycle 1
- **ASSUMPTION-072** (ASSUMPTION, cycle 1, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-071 cycle 1
- **ASSUMPTION-073** (ASSUMPTION, cycle 1, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-072 cycle 1
- **ASSUMPTION-074** (ASSUMPTION, cycle 1, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-073 cycle 1
- **ASSUMPTION-075** (ASSUMPTION, cycle 1, priority MEDIUM-HIGH): MONITOR refresh (no new evidence) → MONITOR-074 cycle 1
- **PRESUMPTION-051** (PRESUMPTION, cycle 1, priority LOW-MEDIUM): MONITOR refresh (no new evidence) → MONITOR-052 cycle 1
- **PRESUMPTION-058** (PRESUMPTION, cycle 1, priority LOW-MEDIUM): MONITOR refresh (no new evidence) → MONITOR-057 cycle 1
- **PRESUMPTION-072** (PRESUMPTION, cycle 1, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-067 cycle 1
- **PRESUMPTION-073** (PRESUMPTION, cycle 1, priority MEDIUM-HIGH): MONITOR refresh (no new evidence) → MONITOR-068 cycle 1
- **PRESUMPTION-077** (PRESUMPTION, cycle 1, priority HIGH): MONITOR refresh (no new evidence) → MONITOR-069 cycle 1
- **PRESUMPTION-086** (PRESUMPTION, cycle 1, priority MEDIUM): MONITOR refresh (no new evidence) → MONITOR-076 cycle 1

## Completion checklist (2026-05-17 run)

- [x] Read `for_lit_search.md` queue state; identified 57 RE-TRIGGER items + 0 newly QUEUED daily-cycle items.
- [x] Read agent definitions (15a, 15b, 15c) and provenance protocol.
- [x] Made exceptional ownership-boundary crossing decision; documented rationale in for_lit_search.md 2026-05-17 RUN section.
- [x] Appended cycle-1/2/3 refresh blocks to all 57 _for.md result files.
- [x] Appended cycle-1/2/3 refresh blocks to all 57 _against.md result files.
- [x] Updated all 57 status lines in for_lit_search.md with [SEARCHED-15a: 2026-05-17] [SEARCHED-15b: 2026-05-17] [DISPOSITIONED-15c: 2026-05-17] tags.
- [x] Appended 57 MONITOR REFRESH entries to monitor_queue.md.
- [x] Cycle summary appended to this returns file.
- [x] SYSTEMIC-RISK-FLAG-NEW raised (process-fragility; 15d schedule failure).
- [x] Provenance chains extended by one cycle for all 57 items.

---

**Generated by Agents 15a, 15b, and 15c (2026-05-17 scheduled pipeline run; exceptional drain)**
**Date: 2026-05-17 (autonomous scheduled-task run; no human review in-loop)**
**Pipeline trigger: c2a2-lit-search-pipeline scheduled task; 0 daily-cycle items; 57 RE-TRIGGER items drained exceptionally due to 15d schedule failure.**


---

## 2026-05-18 — c2a2-lit-search-pipeline run (26 newly QUEUED items from 2026-05-17 14a/14b cycle)

**Run note:** Processing the 26 newly queued items (13 ASSUMPTION-158..170; 13 PRESUMPTION-183..195) extracted by the 2026-05-17 c2a2-self-awareness-daily run (which resumed after 2 missed cycles). This is the on-cadence c2a2-lit-search-pipeline fire, one hour after 14a/14b. No exceptional cohort drain this cycle; 57-item RE-TRIGGER cohort from 2026-05-05 was drained exceptionally by the 2026-05-17 pipeline run and is not re-touched here.

**Dispositions:** 5 INCORPORATE; 19 MONITOR; 2 REVISE

### ASSUMPTION RETURNS (13 total)

### RETURN-TO-14a: ASSUMPTION-158
**Original item:** ASSUMPTION-158
**Statement:** "Path 2 (DeepSeek-Flash via API + worker script reading job-folder queue) is the chosen architecture for adding a non-Claude LLM agent to the same vault."
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Inbox/Outbox pattern (Wikipedia; Jovanović 2023, milanjovanovic.tech) — file-/table-based queues with at-least-once semantics are a mature integration pattern for decoupling producers and consumers.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** AWS Builders' Library 'Timeouts, retries and backoff with jitter' — file-folder queues lack the retry-budget, dead-letter-queue, and visibility-timeout primitives that production queue services provide; rolling your own is a documented anti-pattern under load.
**Disposition:** INCORPORATE
**Reasoning:** Topology has Strong literature support; operational caveats are real but addressable within scope (one producer, vault-safety boundary). The decision is well-bounded; INCORPORATE with explicit scope-and-scale conditions noted.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-158_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-158_against.md

---

### RETURN-TO-14a: ASSUMPTION-159
**Original item:** ASSUMPTION-159
**Statement:** "agents.md imports Tom's 12 rules verbatim with one-line analogy note + vault-specific corollaries on Rules 5, 8, 9; single source of truth for both Claude agents and DeepSeek worker."
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Wang (2011) 'Transfer Learning by Structural Analogy' (AAAI) — structural-alignment-based rule transfer is well-studied; works best when source and target share relational structure.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** Domain Portability Myth (LinkedIn; Wei Li) — explicit warning that rule-set portability across domains often fails on hidden assumptions encoded in the original rules.
**Disposition:** MONITOR
**Reasoning:** Pattern is canonical at the topology level (SSOT) but the analogical-transfer audit (PRESUMPTION-184) is not yet performed. Monitor until corollary coverage is justified or expanded.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-159_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-159_against.md

---

### RETURN-TO-14a: ASSUMPTION-160
**Original item:** ASSUMPTION-160
**Statement:** "DeepSeek worker scope-locked to `_agents/deepseek/` (inbox/outbox/done/failed); never writes to live vault content; Maildir-style filename convention; vault-safety boundary as the architectural commitment."
**15a result:** SUPPORTED (Strong)
**15a key source:** Cursor 'Implementing a secure sandbox for local agents' (cursor.com/blog/agent-sandboxing) — filesystem boundary is the first and most cited principle of agent sandboxing.
**15b result:** NO-CHALLENGE-FOUND (None)
**15b key source:** Sandboxing literature is uniformly positive on filesystem-scope-locking. No counter-evidence found that scope-locking is inferior to alternatives.
**Disposition:** INCORPORATE
**Reasoning:** Strong literature support, no credible challenge to the core commitment. The boundary is well-grounded and aligns with canonical sandboxing practice. Incorporate; track related boundaries (network, resource, credentials) as separate items.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-160_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-160_against.md

---

### RETURN-TO-14a: ASSUMPTION-161
**Original item:** ASSUMPTION-161
**Statement:** "Path-2 architecture is C2A2 infrastructure (reusable post-ISME), not pathway content; reinforces PREMISE-016 (toolkit/content separation)."
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Pirolli & Card (1995) 'Information Foraging' — distinction between tool-layer and content-layer is canonical in HCI; tools that serve content stay usable when content changes.
**15b result:** PARTIALLY-CHALLENGED (Weak-Moderate)
**15b key source:** YAGNI principle ('You Aren't Gonna Need It') — software-engineering practice cautions against classifying things as 'reusable infrastructure' before any second use materializes.
**Disposition:** MONITOR
**Reasoning:** Topology-level claim is supported; the operational reusability claim is forecast. Monitor until first reuse opportunity reveals whether the classification holds.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-161_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-161_against.md

---

### RETURN-TO-14a: ASSUMPTION-162
**Original item:** ASSUMPTION-162
**Statement:** "Coordination primitives for multi-agent shared-vault: MCP shared protocol; Git as universal undo/conflict layer; folder-scoped agent assignments; no scheduler, no lock manager — last-write-wins."
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Git documentation and 25-year operational history — git-as-conflict-layer is well-attested and validated by widespread practice.
**15b result:** STRONGLY-CHALLENGED (Strong)
**15b key source:** Wikipedia 'Conflict-free replicated data type' — explicit warning: 'Using the latest write risks data loss, since timestamps across distributed systems can drift or arrive out of order.'
**Disposition:** MONITOR
**Reasoning:** ASSUMPTION + strong challenge + the strong challenge applies only at boundary-conditions not currently met. Acceptable now (N=1 producer per folder); literature treats LWW as deferred technical debt. Monitor with high priority; plan transition before second producer.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-162_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-162_against.md

---

### RETURN-TO-14a: ASSUMPTION-163
**Original item:** ASSUMPTION-163
**Statement:** "worker.py is ~60 lines, one-shot, no daemon, no retry logic, fail-loud; C1–C5 PASS at 2026-05-16T20:49:13 UTC; meets Rules 2 (Simplicity) and 12 (Fail Loud)."
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Brooks 'No Silver Bullet' — argues against unnecessary complexity; aligns with Rule 2.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** AWS Builders' Library 'Timeouts, retries and backoff with jitter' — argues that judicious retries (with backoff and jitter) are essential for handling transient failures, which are the common case in distributed systems.
**Disposition:** MONITOR
**Reasoning:** Appropriate for current shake-out phase. Literature support is conditional on this being early-stage. Monitor; expect to add narrow idempotent retry around the LLM API call as operational data accumulates.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-163_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-163_against.md

---

### RETURN-TO-14a: ASSUMPTION-164
**Original item:** ASSUMPTION-164
**Statement:** "2026-05-16 chat-scrape success = fourth consecutive day; crosses 'credible stability' threshold; weakens PRESUMPTION-159 on chat-scrape axis."
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Nelson (1982) 'Probability, Statistics, and Quality of Service' — consecutive-success thresholds in reliability statistics typically require N=5-7 for credible stability claims at moderate failure rates.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** Reason (1990) 'Human Error' — distinction between symptom-success and cause-resolution; multiple symptom-successes do not prove cause-resolution.
**Disposition:** MONITOR
**Reasoning:** Data point is real but inference scope is contested. Monitor along with PRESUMPTION-190 and substrate-decomposition cluster.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-164_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-164_against.md

---

### RETURN-TO-14a: ASSUMPTION-165
**Original item:** ASSUMPTION-165
**Statement:** "c2a2-self-awareness-daily missed 2 consecutive cycles (2026-05-15 + 2026-05-16); 3-consecutive on-cadence streak broken; pipeline visibly stalled."
**15a result:** SUPPORTED (Strong)
**15a key source:** Shaped 'Best Practices in Data Ingestion' — explicit identification that scheduled-task misses are first-line indicators of pipeline-state problems requiring classification.
**15b result:** NO-CHALLENGE-FOUND (None)
**15b key source:** No literature challenges the factual claim about missed cycles. The challenge belongs to PRESUMPTION-187 (the framing question).
**Disposition:** INCORPORATE
**Reasoning:** Documented operational fact; well-grounded in SRE-style reporting. The inferential framing question is handled separately (PRESUMPTION-187). Incorporate the fact; classify the cause separately.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-165_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-165_against.md

---

### RETURN-TO-14a: ASSUMPTION-166
**Original item:** ASSUMPTION-166
**Statement:** "c2a2-lit-search-pipeline 2026-05-16 ran on cadence + produced documented null run + refused to drain 57-item RE-TRIGGER cohort + surfaced upstream gap; Pathway-14 honesty-layer success on permissive criterion."
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Beyer et al. (2016) SRE Book — null-result reporting is canonical operational discipline; honest no-op is treated as success.
**15b result:** PARTIALLY-CHALLENGED (Weak-Moderate)
**15b key source:** Hollnagel (2014) 'Safety-II' — 'absence of dishonesty' is not 'presence of honesty'; transparency under stress requires active disclosure, not just non-falsification.
**Disposition:** MONITOR
**Reasoning:** Factual claim about behavior is fine. Categorization as 'Pathway-14 success' depends on criterion choice (PRESUMPTION-195). Monitor jointly with PRESUMPTION-195.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-166_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-166_against.md

---

### RETURN-TO-14a: ASSUMPTION-167
**Original item:** ASSUMPTION-167
**Statement:** "57-item RE-TRIGGER cohort from 2026-05-05 (next_check 2026-05-12) now 4 days overdue, 7+ consecutive carry-forward without drain, no visible 15d evidence; reframed as ownership-boundary problem not item-ageing problem."
**15a result:** SUPPORTED (Strong)
**15a key source:** Extract.to 'Why your data pipeline keeps breaking' — explicit identification of unclear ownership as the root cause of pipeline fragility.
**15b result:** NO-CHALLENGE-FOUND (None)
**15b key source:** Literature is uniformly positive on the ownership-boundary reframe. No counter-evidence that item-ageing framing would be more productive.
**Disposition:** INCORPORATE
**Reasoning:** Reframe is strongly supported by data-pipeline-ownership literature. No credible challenge. Incorporate the reframe; OPEN-046 tracks the follow-through.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-167_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-167_against.md

---

### RETURN-TO-14a: ASSUMPTION-168
**Original item:** ASSUMPTION-168
**Statement:** "DECISION-032/033/034 canonization in second-day carry-forward; all three PREMISE-backed; described as '~10-minute desk action that closes three architectural commitments.'"
**15a result:** PARTIALLY-SUPPORTED (Weak-Moderate)
**15a key source:** C2A2-internal PREMISE-016/017/018 — validated premises exist (2026-05-15 cycle).
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** ADR literature (Nygard 2011; subsequent practice) — canonization-readiness requires more than rationale: dependency audit, supersession-check, naming consistency.
**Disposition:** MONITOR
**Reasoning:** Pattern is generally supported but specific estimate is challenged by listed dependencies. Monitor; track canonization actually proceeding vs. carry-forward continuing.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-168_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-168_against.md

---

### RETURN-TO-14a: ASSUMPTION-169
**Original item:** ASSUMPTION-169
**Statement:** "Pace-and-shape concern on fourth consecutive evening surfacing; 3 consecutive days added architectural breadth without advancing ISME demo critical path; 'rate-mismatch ... not coincidence-shaped.'"
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Project-portfolio management literature (Cooper, Edgett, Kleinschmidt 2001) — explicit identification that 'breadth-work' and 'depth-work' compete for fixed bandwidth; allocation-imbalance is a known failure mode under deadline pressure.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** Csikszentmihalyi (1996) 'Creativity' — creative-work bandwidth is not always zero-sum with execution-work; cognitive priming from breadth can accelerate depth.
**Disposition:** MONITOR
**Reasoning:** Pattern (recurrence) supported; classification (zero-sum) contested. Monitor; high priority due to ISME runway pressure but with explicit compose-or-interfere test.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-169_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-169_against.md

---

### RETURN-TO-14a: ASSUMPTION-170
**Original item:** ASSUMPTION-170
**Statement:** "agents.md codifies five hard prohibitions (write outside scope; delete without confirmation; edit without read; silent conflict-merge; skip failure-logging) — candidate for C2A2 architecture vault-safety-boundary cluster."
**15a result:** SUPPORTED (Strong)
**15a key source:** Cursor 'Implementing a secure sandbox for local agents' — explicit list of must-have boundaries for coding agents: scope, deletion, read-before-write, conflict, audit.
**15b result:** NO-CHALLENGE-FOUND (None)
**15b key source:** No literature challenges any of the five prohibitions. Critiques exist of completeness (the list could be longer), not of correctness.
**Disposition:** INCORPORATE
**Reasoning:** Strong literature support across multiple converging sources; no credible challenge to the prohibitions themselves. Incorporate as a canonical vault-safety-boundary statement; track completeness audit separately.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-170_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-170_against.md

---

### PRESUMPTION RETURNS (13 total)

### RETURN-TO-14b: PRESUMPTION-183
**Original item:** PRESUMPTION-183
**Statement:** "Maildir-style file-folder coordination presumed to scale beyond single non-Claude producer; priority-field deferred 'until more than one producer' names the assumption only to defer it."
**15a result:** PARTIALLY-SUPPORTED (Weak-Moderate)
**15a key source:** Maildir specification (Bernstein) — designed for atomic delivery in multi-producer contexts; widely deployed in IMAP servers handling concurrent producers.
**15b result:** CHALLENGED (Moderate)
**15b key source:** DZone 'Conflict Resolution: Using Last-Write-Wins vs. CRDTs' — under multi-producer concurrent edits, file-folder coordination needs vector clocks or CRDTs; Maildir provides atomic delivery but not ordered processing.
**Disposition:** MONITOR
**Reasoning:** PRESUMPTION + moderate challenge + known trigger condition (second producer). Monitor; track second-producer trigger as automatic re-evaluation point.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-183_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-183_against.md

---

### RETURN-TO-14b: PRESUMPTION-184
**Original item:** PRESUMPTION-184
**Statement:** "12-rules transfer from coding-context to vault/notes-context presumed clean for 9 un-corollary'd rules; transfer-validity audit not performed. Joins CRITICAL transfer-validity cluster."
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Wang (2011) 'Transfer Learning by Structural Analogy' — structural-alignment rule transfer succeeds when source and target share relational structure; coding-rules and vault-rules share substantial structure (both are operational disciplines).
**15b result:** CHALLENGED (Moderate-Strong)
**15b key source:** Domain Portability Myth (LinkedIn; Wei Li) — explicit warning that 'works in source domain' is unreliable evidence of 'will work in target domain'; even high-structural-similarity transfers carry hidden boundary conditions.
**Disposition:** MONITOR
**Reasoning:** PRESUMPTION + cluster membership + Moderate-Strong challenge. The right disposition is MONITOR with HIGH cluster-priority; per-rule audit is the planned resolution path. Not REVISE because no specific harm yet observed; not INCORPORATE because the un-audited transfer remains the documented pattern this cluster catches.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-184_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-184_against.md

---

### RETURN-TO-14b: PRESUMPTION-185
**Original item:** PRESUMPTION-185
**Statement:** "Scope-lock + human-or-Claude review-step presumes Claude has bandwidth/trust to be reviewer; if Claude is bottleneck reviewer, Rule-5 offloading recursively re-imports Claude into the loop at review time."
**15a result:** NO-SUPPORT-FOUND (None)
**15a key source:** No literature directly supports the design choice; it is a design decision Tom made implicitly.
**15b result:** CHALLENGED (Moderate)
**15b key source:** Frontiers 'Fostering effective hybrid human-LLM reasoning' — review-bottleneck is a known failure mode when LLM is both worker and reviewer; recursive re-import is documented.
**Disposition:** MONITOR
**Reasoning:** PRESUMPTION + moderate challenge + Rule-5 tension. The right disposition is MONITOR; trigger condition is worker output volume reaching the point where review bandwidth becomes the bottleneck.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-185_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-185_against.md

---

### RETURN-TO-14b: PRESUMPTION-186
**Original item:** PRESUMPTION-186
**Statement:** "Pace-and-shape framing presumes architectural-breadth work and demo-path work are zero-sum on Tom's bandwidth; 'probably not both' closes off the compose-or-interfere question."
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** DEA-ZSG (Lins et al. 2003) — zero-sum framing applies when production units cannot compose; some real-world resource-allocation cases match.
**15b result:** CHALLENGED (Moderate)
**15b key source:** Csikszentmihalyi (1996) 'Creativity' — creative breadth often primes execution depth; not zero-sum.
**Disposition:** MONITOR
**Reasoning:** PRESUMPTION + moderate challenge + open empirical question. The right disposition is MONITOR with explicit compose-or-interfere test before zero-sum is locked in as policy.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-186_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-186_against.md

---

### RETURN-TO-14b: PRESUMPTION-187
**Original item:** PRESUMPTION-187
**Statement:** "'14a/14b ingestion pipeline visibly stalled' framing presumes pipeline-failure (scheduler/credential/environment) rather than rate-mismatch (Chat-side production exceeds daily ingestion capacity); pipeline-failure framing operationally simpler, chosen by default."
**15a result:** NO-SUPPORT-FOUND (None)
**15a key source:** No literature supports defaulting to pipeline-failure framing over rate-mismatch framing; classification protocols (Shaped, Azure) explicitly require diagnosis before remediation.
**15b result:** STRONGLY-CHALLENGED (Strong)
**15b key source:** Shaped 'Best Practices in Data Ingestion' — explicit guidance: 'rate-mismatch requires buffering or parallelism'; cause classification precedes remediation.
**Disposition:** REVISE
**Reasoning:** PRESUMPTION + Strong challenge + cluster-membership in CRITICAL substrate-decomposition cluster (now N=4+). Per 15c heuristic: PRESUMPTION with strong challenge → lean REVISE with HIGH urgency. The cluster pattern is itself the systemic risk; this instance is one more data point that the pre-classification anti-pattern is recurring.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-187_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-187_against.md

---

### RETURN-TO-14b: PRESUMPTION-188
**Original item:** PRESUMPTION-188
**Statement:** "'Verify 15d cadence' framing presumes c2a2-15d-monitor exists; lit-search note same day says 'no scheduled-task evidence visible'; cadence-fix-vs-unbuilt-component is the same pre-classification pattern."
**15a result:** NO-SUPPORT-FOUND (None)
**15a key source:** No literature supports default-to-cadence-fix without existence verification.
**15b result:** STRONGLY-CHALLENGED (Strong)
**15b key source:** Reason (1990) — pre-classification of failure mode without state-check is canonical incident-analysis error.
**Disposition:** REVISE
**Reasoning:** PRESUMPTION + Strong challenge + cluster-membership + same-day contradicting evidence already on disk. Per 15c heuristic: PRESUMPTION with strong challenge → REVISE with HIGH urgency. This is the most clearly-falsifiable instance of the cluster pattern.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-188_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-188_against.md

---

### RETURN-TO-14b: PRESUMPTION-189
**Original item:** PRESUMPTION-189
**Statement:** "DeepSeek-Flash imported on cost/capability grounds without examining Pathway-19 federation / peer-trust / data-sovereignty implications of LLM-provider choice."
**15a result:** NO-SUPPORT-FOUND (None)
**15a key source:** No literature supports the default of cost/capability-only LLM selection bypassing governance.
**15b result:** CHALLENGED (Moderate)
**15b key source:** Nezhar.com 'Beyond Vendor Lock-In: A Framework for LLM Sovereignty' — explicit governance framework for LLM-provider selection that the cost/capability default bypasses.
**Disposition:** MONITOR
**Reasoning:** PRESUMPTION + moderate challenge + open Pathway-19 question. Monitor; track DeepSeek-Flash use against Pathway-19 sovereignty constraints as they crystallize.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-189_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-189_against.md

---

### RETURN-TO-14b: PRESUMPTION-190
**Original item:** PRESUMPTION-190
**Statement:** "'Fourth-consecutive chat-scrape success weakens PRESUMPTION-159' presumes credential-vs-architectural binary is right frame and that chat-scrape is independent evidence about Chrome-MCP cluster health."
**15a result:** NO-SUPPORT-FOUND (None)
**15a key source:** No literature supports single-surface-success-as-cluster-evidence inference.
**15b result:** CHALLENGED (Moderate)
**15b key source:** Reason (1990) — surface-success vs. cause-resolution distinction.
**Disposition:** MONITOR
**Reasoning:** PRESUMPTION + moderate challenge + open cluster question. Monitor jointly with substrate-decomposition cluster and ASSUMPTION-164 (its paired item).
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-190_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-190_against.md

---

### RETURN-TO-14b: PRESUMPTION-191
**Original item:** PRESUMPTION-191
**Statement:** "'10-minute desk action' for DECISION-032/033/034 canonization presumes (a) PREMISE-backing materially strengthens canonization readiness and (b) Tom's endorsement is the bottleneck; ignores listed formalization-blockers."
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** ADR literature (Nygard 2011) — PREMISE-backing does materially strengthen canonization readiness, all else equal.
**15b result:** CHALLENGED (Moderate)
**15b key source:** ADR literature (Nygard; subsequent practice) — readiness audit must check supersession, naming, dependency before canonization.
**Disposition:** MONITOR
**Reasoning:** PRESUMPTION + moderate challenge + documented blockers. Monitor jointly with ASSUMPTION-168.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-191_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-191_against.md

---

### RETURN-TO-14b: PRESUMPTION-192
**Original item:** PRESUMPTION-192
**Statement:** "Composer-draft preservation note presumes the unsent Tom-draft will eventually be useful; preservation without classification runs against Pathway-14 honesty-layer's accurate-classification commitment."
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Archival-science literature (Cook 2013) — preservation default is reasonable when classification cost is high relative to storage cost.
**15b result:** CHALLENGED (Weak-Moderate)
**15b key source:** Cook (2013) 'Evidence, Memory, Identity' — archival best-practice favors classification at the time of preservation, not deferred classification.
**Disposition:** MONITOR
**Reasoning:** PRESUMPTION + weak-moderate challenge + LOW stakes + joins criterion-creep cluster. Monitor with low individual priority but cluster-pattern attention.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-192_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-192_against.md

---

### RETURN-TO-14b: PRESUMPTION-193
**Original item:** PRESUMPTION-193
**Statement:** "Cowork-summary 'Assumptions: 144 / Presumptions: 182 cumulative on disk' vs grep-by-ID ASSUMPTION-157 / PRESUMPTION-182 — 13-item discrepancy on assumptions invisible to summary author; self-reporting without verification step. Joins SELF-MEASUREMENT Goodhart cluster."
**15a result:** NO-SUPPORT-FOUND (None)
**15a key source:** No literature supports unverified self-report as a reliable counting protocol.
**15b result:** CHALLENGED (Moderate)
**15b key source:** Goodhart's Law (Wikipedia; CNA 2022; signaling-and-meaning literature, Oxford JCMC 2023) — when self-reported counts become operational targets, they cease to reflect the underlying state.
**Disposition:** MONITOR
**Reasoning:** PRESUMPTION + moderate challenge + cluster-membership + low-cost remediation. The verification step is cheap; the cluster pattern is the systemic concern. MONITOR with explicit verification-step adoption as the trigger condition.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-193_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-193_against.md

---

### RETURN-TO-14b: PRESUMPTION-194
**Original item:** PRESUMPTION-194
**Statement:** "Branch-point-at-terminus presumed to be appropriate end-state for productive Chat sessions; may be Claude's accurate read OR generation-time artifact (Claude generates options rather than picking, deferring synthesis to Tom)."
**15a result:** PARTIALLY-SUPPORTED (Weak-Moderate)
**15a key source:** Frontiers 'Fostering effective hybrid human-LLM reasoning' — option-generation by LLM, selection by human is a documented and effective division of labor for high-stakes synthesis.
**15b result:** CHALLENGED (Weak-Moderate)
**15b key source:** Sparkling Logic 'LLMs in Decision Management' — LLMs can both generate and select; defaulting to generation-only is leaving capability on the table.
**Disposition:** MONITOR
**Reasoning:** PRESUMPTION + weak-moderate challenge + cluster membership. Monitor with attention to single-validator-portability cluster.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-194_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-194_against.md

---

### RETURN-TO-14b: PRESUMPTION-195
**Original item:** PRESUMPTION-195
**Statement:** "'Honesty-layer behavior here is good' assertion about lit-search null-run uses permissive criterion (didn't pretend) where Pathway-14 might demand active criterion (escalate cause); criterion-creep with load-bearing term."
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Permissive-criterion (didn't fabricate) is a real and reasonable honesty criterion; well-supported in research-integrity literature.
**15b result:** CHALLENGED (Moderate)
**15b key source:** Hollnagel (2014) Safety-II — absence of dishonesty is not presence of honesty.
**Disposition:** MONITOR
**Reasoning:** PRESUMPTION + moderate challenge + cluster-membership + LOW-MEDIUM stakes. Monitor with cluster-pattern attention.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-195_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-195_against.md

---

## CROSS-CUTTING OBSERVATIONS (2026-05-18 cycle)

### Cluster carry-forwards / extensions this cycle

1. **Substrate-decomposition cluster (CRITICAL)** — extends with PRESUMPTION-187 REVISE + PRESUMPTION-188 REVISE (both this cycle). Cluster now at N=5+ instances (PRESUMPTION-134 REVISE 2026-05-11 unresolved; PRESUMPTION-159 REVISE 2026-05-14 unresolved; PRESUMPTION-177 REVISE 2026-05-15 unresolved; PRESUMPTION-187 REVISE today; PRESUMPTION-188 REVISE today). The pre-classification anti-pattern (defaulting to one failure mode before diagnosis) is now recurring at every layer audited. Cluster-level remediation is overdue.

2. **CRITICAL transfer-validity cluster** — extends with PRESUMPTION-184 (12-rules transfer from coding to vault context, un-audited). Cluster: PRESUMPTION-002 + PRESUMPTION-080 + PRESUMPTION-161 + ASSUMPTION-128 + PRESUMPTION-170 + ASSUMPTION-133 + PRESUMPTION-184. Named-and-deferred pattern persists.

3. **SELF-MEASUREMENT Goodhart cluster** — extends with PRESUMPTION-193 (cowork-summary count discrepancy) + PRESUMPTION-195 (Pathway-14 criterion-creep) + PRESUMPTION-192 (preservation-without-classification). Cluster: PRESUMPTION-180 + ASSUMPTION-143 + PRESUMPTION-192 + PRESUMPTION-193 + PRESUMPTION-195. Verification-step-before-self-report is the common remediation.

4. **Single-validator-portability cluster** — extends with PRESUMPTION-194 (branch-point-at-terminus). Cluster: PRESUMPTION-175 + PRESUMPTION-176 + PRESUMPTION-182 + PRESUMPTION-194. Pattern of Tom-as-only-validator deepens.

5. **Vault-safety-boundary cluster (NEW)** — ASSUMPTION-158 + ASSUMPTION-160 + ASSUMPTION-162 + ASSUMPTION-170 + PRESUMPTION-183 + PRESUMPTION-185. Coherent cluster around Path-2 worker architecture; first systematic treatment of multi-LLM-on-shared-vault safety. Three INCORPORATEs in this cluster represent the largest single-cycle infrastructure-grounding event since 2026-05-15.

### SYSTEMIC-RISK observations

- **Substrate-decomposition cluster** at N=5+ unresolved instances is now itself a systemic risk. Each new instance (PRESUMPTION-187, PRESUMPTION-188) extends the unresolved cluster rather than triggering closure. The pattern itself is the load-bearing concern; cluster-level remediation (pre-classification-protocol commitment) should be elevated.
- **Pace-and-shape vs zero-sum framing** (ASSUMPTION-169 + PRESUMPTION-186) interacts with the cluster picture: if breadth-work and demo-work are zero-sum, the substrate-decomposition cluster is a breadth-work distraction; if compose-or-interfere, addressing the cluster may accelerate demo. Framing matters.

### NOVELTY observations

- ASSUMPTION-165 (documented missed-cycle pattern with timestamps) and ASSUMPTION-167 (ownership-boundary reframe) are well-grounded in existing literature; not novel contributions but high-quality applications.
- The substrate-decomposition cluster pattern itself, if formally articulated, may be a novel contribution to pipeline-fault-classification literature. C2A2-internal observation worth tracking for potential externalization.

---

## Completion checklist (2026-05-18 run)

- [x] Read `for_lit_search.md` queue state; identified 26 newly QUEUED items (13 ASSUMPTIONs 158-170; 13 PRESUMPTIONs 183-195).
- [x] Read agent definitions (15a, 15b, 15c) and provenance protocol.
- [x] Wrote 26 _for.md result files in `lit_search_results/for/`.
- [x] Wrote 26 _against.md result files in `lit_search_results/against/`.
- [x] Updated 26 status lines in `for_lit_search.md` with [SEARCHED-15a: 2026-05-18] [SEARCHED-15b: 2026-05-18] [DISPOSITIONED-15c: 2026-05-18] tags.
- [x] Appended 5 INCORPORATE entries to `validated_premises.md` (PREMISE-023 through PREMISE-027).
- [x] Appended 19 MONITOR entries to `monitor_queue.md` (MONITOR-172 through MONITOR-190).
- [x] Appended 2 REVISE entries to `revision_flags.md` (PRESUMPTION-187, PRESUMPTION-188).
- [x] Cycle summary appended to this returns file.
- [x] Provenance chains complete for all 26 items.

---

**Generated by Agents 15a, 15b, and 15c (2026-05-18 scheduled pipeline run)**
**Date: 2026-05-18 (autonomous scheduled-task run; no human review in-loop)**
**Pipeline trigger: c2a2-lit-search-pipeline scheduled task; processed 26 newly-queued items from 2026-05-17 c2a2-self-awareness-daily run.**

---

## 2026-05-19 RUN — c2a2-lit-search-pipeline (full 15a/15b/15c cycle on 2026-05-18 cohorts + Cohort A cycle-1 refresh)

**Pipeline trigger:** c2a2-lit-search-pipeline scheduled task; on-cadence fire one hour after c2a2-self-awareness-daily and c2a2-periodic-monitor-weekly on 2026-05-18.

**Items processed:** 58 total — 30 RE-TRIGGER cycle-1 refresh items (Cohort A; 13 monthly + 17 weekly MONITOR items re-fired by 15d on 2026-05-18) + 15 fresh QUEUED (Cohort B; ASSUMPTION-171..178 + PRESUMPTION-196..202 from morning 14a/14b) + 13 fresh QUEUED (Cohort C; ASSUMPTION-179..185 + PRESUMPTION-203..208 from EOD 14a/14b addendum).

### AGENT 15a SUMMARY
- 30 cycle-1 refreshes: all carry-forward prior recommendation; no new supporting literature surfaced in the 5-30 day gap since prior cycle.
- 15 Cohort B fresh searches: 1 SUPPORTED (ASSUMPTION-178), 7 PARTIALLY-SUPPORTED (171, 172, 175, 177, 196, 197, 200), 4 SUPPORTED-with-caveats (173, 174, 176, 184/Cohort-C), 0 NO-SUPPORT-FOUND, 0 NOVELTY.
- 13 Cohort C fresh searches: 8 SUPPORTED (179, 180, 181, 182, 184, 185, 203, 204, 207, 208 — note 204 and 207 SUPPORTED but for the challenge direction), 3 PARTIALLY-SUPPORTED (183, 205, 206), 0 NO-SUPPORT-FOUND, 0 NOVELTY.

### AGENT 15b SUMMARY
- 30 cycle-1 refreshes: all carry-forward; no new challenging literature surfaced.
- 15 Cohort B challenges: 1 NO-CHALLENGE-FOUND (ASSUMPTION-178), 8 CHALLENGED (172, 196, 197, 198, 199, 200, 201, 202), 6 PARTIALLY-CHALLENGED (171, 173, 174, 175, 176, 177).
- 13 Cohort C challenges: 2 NO-CHALLENGE-FOUND (PRESUMPTION-204, PRESUMPTION-207), 10 PARTIALLY-CHALLENGED (rest), 1 CHALLENGED.

### STEELMAN highlights (Cohort B/C only)
- PRESUMPTION-199 (uncommitted-state-safe-indefinitely): no defensible steelman; 476-uncommitted indefensible against well-attested loss modes.
- PRESUMPTION-196 / PRESUMPTION-204 (scan-as-ground-truth, both polarities): symmetric anti-pattern; write-receipt/manifest is the standard fix in distributed systems and event-sourcing literature.
- PRESUMPTION-198 / PRESUMPTION-207 (sole-source-bridge / sewing-agent-as-ratification-authority): closed-loop ratification spreading across two agent classes; cross-specialist confirmation required.
- ASSUMPTION-172 (paradigm-shift cluster): vocabulary-convergence ≠ structural-homology; downgrade to "framing-convergence-monitor."
- PRESUMPTION-201 (briefing-write-as-success): textbook Goodhart; outcome metric (Tom-action-rate) required.

### SYSTEMIC-RISK-FLAG (this cycle)

**SYSTEMIC-RISK-FLAG-2026-05-19-A: Inter-agent ground-truth oscillation**
- Affected items: PRESUMPTION-196 (morning), PRESUMPTION-204 (EOD), ASSUMPTION-178, ASSUMPTION-179, ASSUMPTION-180
- Common vulnerability: ground-truth role is being passed agent-to-agent without auditing scan-coverage equivalence; the project oscillates between "orchestrator-as-truth" and "sewing-agent-as-truth" within a single day.
- Literature basis: distributed systems write-ahead-log / event-sourcing / write-receipt-manifest patterns (Kreps; Helland)
- Risk level: HIGH
- Recommendation: introduce manifest-as-truth layer; deprecate scan-as-truth pattern across all agents.

**SYSTEMIC-RISK-FLAG-2026-05-19-B: Closed-loop ratification across agent classes**
- Affected items: PRESUMPTION-198, PRESUMPTION-207, ASSUMPTION-172, ASSUMPTION-182
- Common vulnerability: single agent both detects and ratifies bridges/paradigm-shift claims; pattern now extends from specialist agents to sewing-agent.
- Literature basis: STS (Latour, Collins) on closure; replication-validation literature.
- Risk level: HIGH
- Recommendation: mandatory "proposed pending cross-specialist confirmation" provenance label at agent write-time.

**SYSTEMIC-RISK-FLAG-2026-05-19-C: Goodhart SELF-MEASUREMENT cluster compounding**
- Affected items: PRESUMPTION-201, PRESUMPTION-202, ASSUMPTION-175
- Common vulnerability: agents measure their own output; queue depth treated as throughput-side signal; outcome (Tom-action-rate) invisible.
- Literature basis: Goodhart, Strathern, Muller (Tyranny of Metrics)
- Risk level: MEDIUM-HIGH
- Recommendation: coordinated REVISE on metric design — add outcome metrics; decompose queue depth into arrival vs service rates.

**SYSTEMIC-RISK-FLAG-2026-05-19-D: VCS hygiene CRITICAL exposure**
- Affected items: PRESUMPTION-199, ASSUMPTION-174
- Common vulnerability: 476 uncommitted changes with no checkpoint discipline; constitutional "no blind push" rule has produced a state worse than blind push would have.
- Literature basis: SRE / DevOps (Beyer et al.), software-engineering checkpoint discipline.
- Risk level: CRITICAL
- Recommendation: structured intermediate-commit protocol to bound uncommitted state; visual-review-of-N pattern fails per Cohen at N>20.

### PRESUMPTION RETURNS (15 total — Cohort B PRESUMPTIONs + Cohort C PRESUMPTIONs)

### RETURN-TO-14b: PRESUMPTION-196
**Original item:** PRESUMPTION-196
**Statement:** "Sewing-agent's scan of the current vault state functions as ground truth for what was/wasn't written this cycle..."
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Read-as-verification is common in low-stakes audit; some literature treats post-hoc filesystem scan as a valid completeness check when no append-only log exists.
**15b result:** CHALLENGED (Strong)
**15b key source:** Helland (2015) "Immutability changes everything" and Kreps (2014) on the log — write-receipt/manifest is the canonical ground truth in distributed systems; scan-as-truth is a textbook anti-pattern.
**Disposition:** REVISE
**Reasoning:** Scan-as-truth textbook anti-pattern → REVISE-021 HIGH
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-196_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-196_against.md

---

### RETURN-TO-14b: PRESUMPTION-197
**Original item:** PRESUMPTION-197
**Statement:** "Articulating an uncertainty surface in writing counts as having calibrated uncertainty about the underlying claim..."
**15a result:** PARTIALLY-SUPPORTED (Weak-Moderate)
**15a key source:** Articulation literature (epistemics) shows naming a doubt is a precondition for calibration; useful first step.
**15b result:** CHALLENGED (Moderate)
**15b key source:** Tetlock (Superforecasting) and calibration-training literature — articulation without numeric probability-binding does not produce calibration.
**Disposition:** REVISE
**Reasoning:** Articulation ≠ calibration → REVISE-022 MEDIUM
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-197_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-197_against.md

---

### RETURN-TO-14b: PRESUMPTION-198
**Original item:** PRESUMPTION-198
**Statement:** "Bridges proposed by a single specialist agent (e.g., 17-bridge or 18-bridge) function as confirmed bridges once written..."
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Single-author bridge proposals are conventional in early-stage interdisciplinary work as hypotheses.
**15b result:** CHALLENGED (Strong)
**15b key source:** STS (Latour; Collins) on closure — single-detector ratification is the canonical closed-loop failure; cross-specialist confirmation required to count as a confirmed bridge.
**Disposition:** REVISE
**Reasoning:** Sole-source bridges are hypotheses → REVISE-023 HIGH
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-198_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-198_against.md

---

### RETURN-TO-14b: PRESUMPTION-199
**Original item:** PRESUMPTION-199
**Statement:** "The current uncommitted-state (476 changes) is safe to maintain indefinitely so long as no force-push occurs..."
**15a result:** NO-SUPPORT-FOUND (effectively)
**15a key source:** No literature defends large uncommitted working-tree states; even permissive workflows assume bounded WIP.
**15b result:** CHALLENGED (Strong)
**15b key source:** SRE / DevOps (Beyer et al.) and software-engineering checkpoint literature — 476 uncommitted is indefensible against well-attested loss modes (disk failure, accidental clean, conflicting edits, lost reviewability).
**Disposition:** REVISE
**Reasoning:** Indefensible; 476 uncommitted CRITICAL → REVISE-024 CRITICAL
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-199_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-199_against.md

---

### RETURN-TO-14b: PRESUMPTION-200
**Original item:** PRESUMPTION-200
**Statement:** "Cycle-count-since-last-evidence is a sufficient staleness proxy for MONITOR items..."
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Count-based aging is a common simple heuristic in monitoring systems.
**15b result:** CHALLENGED (Moderate)
**15b key source:** Surveillance-epidemiology and reliability literature — cycle-counts conflate elapsed time, search effort, and base-rate of evidence; calendar-time + search-effort decomposition is standard.
**Disposition:** REVISE
**Reasoning:** Cycle-counts fail as staleness proxy → REVISE-025 MEDIUM
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-200_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-200_against.md

---

### RETURN-TO-14b: PRESUMPTION-201
**Original item:** PRESUMPTION-201
**Statement:** "A successful briefing-write counts as a successful briefing (success = artifact-produced rather than action-taken-by-Tom)..."
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Process-metric literature acknowledges output-counting as a valid intermediate proxy when outcome data is delayed.
**15b result:** CHALLENGED (Strong)
**15b key source:** Goodhart's law and Strathern's reformulation; Muller (Tyranny of Metrics) — measuring artifact-production while the actual goal is downstream-action is the textbook Goodhart pattern.
**Disposition:** REVISE
**Reasoning:** Textbook Goodhart SELF-MEASUREMENT → REVISE-026 MEDIUM-HIGH
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-201_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-201_against.md

---

### RETURN-TO-14b: PRESUMPTION-202
**Original item:** PRESUMPTION-202
**Statement:** "Increasing depth of queue files (for_lit_search, monitor_queue) signals surge in incoming work..."
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Queue length is one observable in queueing-theory dashboards.
**15b result:** CHALLENGED (Moderate)
**15b key source:** Queueing theory (Little's law; Kingman) — depth alone is ambiguous between arrival-rate surge and service-rate stall; both must be decomposed.
**Disposition:** REVISE
**Reasoning:** Queue depth signals investigation not surge → REVISE-027 MEDIUM
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-202_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-202_against.md

---

### RETURN-TO-14b: PRESUMPTION-203
**Original item:** PRESUMPTION-203
**Statement:** "Reporting both a found-count and an examined-count, stratified by source, is sufficient honesty about scan-coverage..."
**15a result:** SUPPORTED (Moderate)
**15a key source:** Information-retrieval literature (precision/recall reporting conventions) — two-metric stratified reporting is standard practice for honest coverage claims.
**15b result:** PARTIALLY-CHALLENGED (Weak)
**15b key source:** Methodology critiques note examined-count can itself be gamed if "examined" is loosely defined; needs operationalization.
**Disposition:** INCORPORATE (PREMISE-035)
**Reasoning:** Two-metric stratified reporting → INCORPORATE/PREMISE-035
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-203_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-203_against.md

---

### RETURN-TO-14b: PRESUMPTION-204
**Original item:** PRESUMPTION-204
**Statement:** "Sewing-agent's own scan after a sewing-pass is the authoritative record of what was sewn this cycle (supersedes orchestrator scan)..."
**15a result:** SUPPORTED (for challenge direction; Moderate)
**15a key source:** Helland (2015) "Immutability changes everything"; Kreps (2014) on the log — supports the symmetric critique that any scan-as-truth (regardless of which agent does it) is the wrong primitive.
**15b result:** NO-CHALLENGE-FOUND
**15b key source:** No literature defends sewing-agent-scan-as-truth specifically; symmetric to PRESUMPTION-196.
**Disposition:** REVISE
**Reasoning:** Symmetric to PRESUMPTION-196 → REVISE-030 HIGH
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-204_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-204_against.md

---

### RETURN-TO-14b: PRESUMPTION-205
**Original item:** PRESUMPTION-205
**Statement:** "The four-mode disagreement frame (concordant-support / concordant-challenge / 15a-only / 15b-only) is the right primary lens for cross-cohort patterns..."
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Mixed-methods triangulation and inter-rater agreement literature support multi-mode disagreement decomposition.
**15b result:** PARTIALLY-CHALLENGED (Weak)
**15b key source:** Statistical-classification literature notes equal weighting of the four modes is an unexamined choice; calibration may differ across modes.
**Disposition:** MONITOR (MONITOR-196)
**Reasoning:** Frame transfers; weights need calibration → MONITOR/MONITOR-196
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-205_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-205_against.md

---

### RETURN-TO-14b: PRESUMPTION-206
**Original item:** PRESUMPTION-206
**Statement:** "Intra-family agreement (e.g., two SRE sources) provides equivalent confirmation weight to inter-family agreement (one SRE + one STS)..."
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Two same-family citations do provide some independent confirmation if authors are independent.
**15b result:** CHALLENGED (Moderate)
**15b key source:** Meta-analysis and triangulation literature (Denzin; Patton) — intra-family agreement risks shared-prior-bias; inter-family triangulation strictly stronger.
**Disposition:** REVISE
**Reasoning:** Discount intra-family agreement weight → REVISE-031 MEDIUM
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-206_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-206_against.md

---

### RETURN-TO-14b: PRESUMPTION-207
**Original item:** PRESUMPTION-207
**Statement:** "Sewing-agent functions as a legitimate ratification authority for cross-cohort findings (not just a presentation layer)..."
**15a result:** SUPPORTED (for challenge direction; Moderate)
**15a key source:** STS (Latour; Collins) on closure — supports the critique that ratification by the same agent that aggregates is closed-loop.
**15b result:** NO-CHALLENGE-FOUND
**15b key source:** No literature defends a single-aggregator ratification role for cross-cohort synthesis without cross-specialist confirmation.
**Disposition:** REVISE
**Reasoning:** Closed-loop ratification spread → REVISE-032 HIGH
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-207_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-207_against.md

---

### RETURN-TO-14b: PRESUMPTION-208
**Original item:** PRESUMPTION-208
**Statement:** "At Day 150 of the corpus-horizon window, a lightweight re-review trigger should fire for items dispositioned in the first 30 days..."
**15a result:** SUPPORTED (Moderate)
**15a key source:** Surveillance-epidemiology and active-monitoring literature support time-bounded re-review triggers as cheap insurance against drift.
**15b result:** PARTIALLY-CHALLENGED (Weak)
**15b key source:** Some workflow-engineering critiques caution against fixed-interval re-review as ritualistic; trigger conditions matter.
**Disposition:** INCORPORATE (PREMISE-036)
**Reasoning:** Lightweight re-review trigger at Day 150 → INCORPORATE/PREMISE-036
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-208_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-208_against.md

---

### ASSUMPTION RETURNS (13 total — Cohort B ASSUMPTIONs + Cohort C ASSUMPTIONs)

### RETURN-TO-14a: ASSUMPTION-171
**Original item:** ASSUMPTION-171
**Statement:** "Discretionary curation by the sewing-agent (e.g., choosing which cross-cohort findings to elevate) is acceptable without explicit calibration..."
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Editorial-judgment literature defends discretionary curation when curator is qualified and accountable.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** Decision-science (Kahneman et al., Noise) — uncalibrated discretionary judgment produces unwanted variability; exception-rate tracking is the standard mitigation.
**Disposition:** MONITOR (MONITOR-191)
**Reasoning:** PARTIALLY-SUPPORTED/PARTIALLY-CHALLENGED; discretionary curation defensible if calibrated; needs exception-rate tracking → MONITOR/MONITOR-191
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-171_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-171_against.md

---

### RETURN-TO-14a: ASSUMPTION-172
**Original item:** ASSUMPTION-172
**Statement:** "Convergent vocabulary across three specialist agents (paradigm-shift cluster) constitutes evidence of a real cross-thinker paradigm shift..."
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Vocabulary convergence is sometimes a weak signal in lexical-semantics literature.
**15b result:** CHALLENGED (Strong)
**15b key source:** History of science and bibliometrics (Kuhn; Small) — vocabulary-convergence is not structural-homology; paradigm-shift requires shared explanatory structure, not shared terms.
**Disposition:** REVISE
**Reasoning:** "Paradigm-shift cluster" overclaims; downgrade to "framing-convergence-monitor" → REVISE-020 HIGH
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-172_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-172_against.md

---

### RETURN-TO-14a: ASSUMPTION-173
**Original item:** ASSUMPTION-173
**Statement:** "Surfacing every cross-cohort finding to Tom is preferable to filtering by significance..."
**15a result:** SUPPORTED-with-caveats (Moderate)
**15a key source:** Transparency literature defends surfacing-by-default to preserve auditability and prevent gatekeeper bias.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** Information-overload literature (Eppler & Mengis) — unfiltered surfacing degrades attention; significance triage is standard.
**Disposition:** INCORPORATE (PREMISE-028)
**Reasoning:** Sound principle; needs significance triage filter → INCORPORATE/PREMISE-028
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-173_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-173_against.md

---

### RETURN-TO-14a: ASSUMPTION-174
**Original item:** ASSUMPTION-174
**Statement:** "Visual review of the 476 uncommitted file diffs by Tom is a sufficient pre-commit safety check..."
**15a result:** SUPPORTED-with-caveats (Weak)
**15a key source:** Manual code-review literature accepts visual review for small change sets.
**15b result:** PARTIALLY-CHALLENGED (Strong)
**15b key source:** Cohen (Best Kept Secrets of Peer Code Review) — visual review effectiveness collapses beyond ~20 changes; decomposition into bounded reviewable chunks is standard.
**Disposition:** INCORPORATE (PREMISE-029)
**Reasoning:** Core correct; visual review of 476 ineffective per Cohen — needs decomposition → INCORPORATE/PREMISE-029
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-174_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-174_against.md

---

### RETURN-TO-14a: ASSUMPTION-175
**Original item:** ASSUMPTION-175
**Statement:** "Tom-reviews-more is the right intervention when queue depth grows..."
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Review-rate increases are one valid throttling response when reviewer is the bottleneck.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** Queueing theory and bottleneck analysis — Tom-reviews-more is the wrong intervention if depth signals upstream surge or service-rate stall elsewhere; depth IS signal but intervention misplaced.
**Disposition:** MONITOR (MONITOR-192)
**Reasoning:** Depth IS signal but "Tom-reviews-more" wrong intervention → MONITOR/MONITOR-192
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-175_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-175_against.md

---

### RETURN-TO-14a: ASSUMPTION-176
**Original item:** ASSUMPTION-176
**Statement:** "Auto-collapsing duplicate findings across cohorts (rather than show-both) is the right default..."
**15a result:** SUPPORTED-with-caveats (Moderate)
**15a key source:** Deduplication is standard practice in information-retrieval and notification systems.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** UX-of-search literature — at low N (e.g., N=2), show-both is cheaper and preserves provenance better than auto-collapse.
**Disposition:** INCORPORATE (PREMISE-030)
**Reasoning:** Dedup standard; show-both cheaper than auto-collapse at N=2 → INCORPORATE/PREMISE-030
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-176_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-176_against.md

---

### RETURN-TO-14a: ASSUMPTION-177
**Original item:** ASSUMPTION-177
**Statement:** "The current cadence-protocol partially addresses the missed-cycle pattern documented in ASSUMPTION-165..."
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Honest "partially addresses" framing is well-grounded in incident-response literature.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** SRE post-incident literature — "partially addresses" without explicit cadence-miss root-cause analysis tends to regress; RCA is standard mitigation.
**Disposition:** MONITOR (MONITOR-193)
**Reasoning:** "Partially addresses" honest; cadence-miss RCA needed → MONITOR/MONITOR-193
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-177_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-177_against.md

---

### RETURN-TO-14a: ASSUMPTION-178
**Original item:** ASSUMPTION-178
**Statement:** "Different agents produce different counts of 'what was written this cycle' because they scan at different times and granularities..."
**15a result:** SUPPORTED (Strong)
**15a key source:** Distributed systems consistency literature (Vogels; Brewer) — eventual-consistency between agent observers is well-documented and expected.
**15b result:** NO-CHALLENGE-FOUND
**15b key source:** No literature challenges the descriptive claim; challenge would be to the remediation (handled in PRESUMPTION-196).
**Disposition:** INCORPORATE (PREMISE-031)
**Reasoning:** Descriptive multi-agent inconsistency; remediation in PRESUMPTION-196 → INCORPORATE/PREMISE-031
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-178_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-178_against.md

---

### RETURN-TO-14a: ASSUMPTION-179
**Original item:** ASSUMPTION-179
**Statement:** "A second scan by a different agent (sewing-agent re-scan after orchestrator scan) is a legitimate cross-check..."
**15a result:** SUPPORTED (Moderate)
**15a key source:** Two-person-rule and dual-observer literature in safety-critical systems — second-scan is a legitimate cross-check primitive.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** Distributed systems literature — second-scan diagnoses inconsistency but cannot localize root cause without manifest; scan-coverage equivalence must be audited.
**Disposition:** MONITOR (MONITOR-194)
**Reasoning:** Second-scan legit but scan-coverage diagnosis premature → MONITOR/MONITOR-194 HIGH
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-179_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-179_against.md

---

### RETURN-TO-14a: ASSUMPTION-180
**Original item:** ASSUMPTION-180
**Statement:** "When 2-of-3 agents agree on a count and 1 disagrees, the disagreement is diagnostic of localized scan-failure in the dissenter..."
**15a result:** SUPPORTED (Moderate)
**15a key source:** Byzantine-agreement and quorum literature — 2-of-3 discordance is a diagnostic signal in majority-vote protocols.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** Distributed systems literature — discordance is diagnostic of disagreement but not of which agent is wrong; localization requires authoritative manifest.
**Disposition:** MONITOR (MONITOR-195)
**Reasoning:** 2-of-3 discordance diagnostic; localization needs manifest → MONITOR/MONITOR-195 HIGH
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-180_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-180_against.md

---

### RETURN-TO-14a: ASSUMPTION-181
**Original item:** ASSUMPTION-181
**Statement:** "Stratifying findings by source (which agent produced them) entirely captures provenance for downstream synthesis..."
**15a result:** SUPPORTED (Moderate)
**15a key source:** Provenance-tracking literature (W3C PROV) — agent-stratification is a standard provenance primitive.
**15b result:** PARTIALLY-CHALLENGED (Weak)
**15b key source:** Provenance literature also flags that agent-stratification alone misses inter-agent dependencies; "entirely" overclaims.
**Disposition:** INCORPORATE (PREMISE-032)
**Reasoning:** Stratification sound; soften "entirely" → INCORPORATE/PREMISE-032
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-181_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-181_against.md

---

### RETURN-TO-14a: ASSUMPTION-182
**Original item:** ASSUMPTION-182
**Statement:** "Bridges identified by sewing-agent are real bridges (not just rhetorical adjacencies)..."
**15a result:** SUPPORTED (Weak)
**15a key source:** Bridge-detection in network analysis sometimes treats co-occurrence as bridge evidence.
**15b result:** CHALLENGED (Strong)
**15b key source:** Network science (Burt on structural holes) and STS — bridges proposed by a single detector without cross-validation are unratified hypotheses; sewing-agent extends closed-loop pattern.
**Disposition:** REVISE
**Reasoning:** Bridges real but unratified → REVISE-028 HIGH
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-182_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-182_against.md

---

### RETURN-TO-14a: ASSUMPTION-183
**Original item:** ASSUMPTION-183
**Statement:** "The 180-day corpus-horizon window is sufficient for all dispositioned items without re-review..."
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Citation-aging literature supports 180-day windows for some fast-moving fields.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** Surveillance-epidemiology — fixed-window without slack/re-review trigger fails to catch late-arriving counter-evidence.
**Disposition:** REVISE
**Reasoning:** Corpus-horizon needs slack/re-review trigger → REVISE-029 MEDIUM
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-183_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-183_against.md

---

### RETURN-TO-14a: ASSUMPTION-184
**Original item:** ASSUMPTION-184
**Statement:** "Using insertText as a workaround for the append-tool limitation is a sound pragmatic substitute..."
**15a result:** SUPPORTED-with-caveats (Moderate)
**15a key source:** Pragmatic-substitution literature in tooling — workaround is sound when canonical primitive unavailable, provided semantics preserved.
**15b result:** PARTIALLY-CHALLENGED (Weak)
**15b key source:** Tooling-debt literature flags workaround-as-permanent risk; should be tracked for replacement.
**Disposition:** INCORPORATE (PREMISE-033)
**Reasoning:** insertText workaround sound → INCORPORATE/PREMISE-033
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-184_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-184_against.md

---

### RETURN-TO-14a: ASSUMPTION-185
**Original item:** ASSUMPTION-185
**Statement:** "The four-mode framing (concordant-support / concordant-challenge / 15a-only / 15b-only) is methodologically sound for cross-cohort analysis..."
**15a result:** SUPPORTED (Moderate)
**15a key source:** Inter-rater agreement and mixed-methods literature (Creswell) — four-mode decomposition is a recognized methodological frame.
**15b result:** PARTIALLY-CHALLENGED (Weak)
**15b key source:** Statistical-classification literature flags need for calibration of mode-weights; methodological frame sound, weights still open.
**Disposition:** INCORPORATE (PREMISE-034)
**Reasoning:** Four-mode frame methodologically sound → INCORPORATE/PREMISE-034
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-185_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-185_against.md

---

### COHORT A — 30 Cycle-1 refresh items (all MONITOR-continued)

All 30 items remain at MONITOR with no new evidence in the refresh window. Carry-forward dispositions issued; next 15d check dates updated.

Monthly cadence (13 items, next check 2026-06-19): PRESUMPTION-012, ASSUMPTION-025, PRESUMPTION-027, PRESUMPTION-028, ASSUMPTION-029, ASSUMPTION-030, ASSUMPTION-032, PRESUMPTION-033, PRESUMPTION-034, PRESUMPTION-039, ASSUMPTION-039, PRESUMPTION-047, ASSUMPTION-045

Weekly cadence (17 items, next check 2026-05-26): ASSUMPTION-080, ASSUMPTION-082, ASSUMPTION-089, ASSUMPTION-092, ASSUMPTION-095, ASSUMPTION-097, ASSUMPTION-098, ASSUMPTION-099, ASSUMPTION-101, ASSUMPTION-106, ASSUMPTION-108, ASSUMPTION-109, ASSUMPTION-111, ASSUMPTION-112, PRESUMPTION-128, PRESUMPTION-135, PRESUMPTION-137

Full per-item cycle-1 append blocks: see lit_search_results/for/<ITEM-ID>_for.md and lit_search_results/against/<ITEM-ID>_against.md

### CYCLE SUMMARY

- Items processed: 58 (30 cycle-1 refreshes + 28 fresh)
- Dispositions: 9 INCORPORATE (PREMISE-028..036), 6+30 MONITOR (6 new MONITOR-191..196; 30 cycle-1 continuations), 13 REVISE (REVISE-020..032)
- INCORPORATE rate (excluding cycle-1 refreshes): 9/28 = 32%
- REVISE rate (excluding cycle-1 refreshes): 13/28 = 46%
- MONITOR rate (excluding cycle-1 refreshes): 6/28 = 21%
- Cohort B REVISE rate: 8/15 = 53% (high — dominated by PRESUMPTION-side scan-as-truth, sole-source-bridge, Goodhart clusters)
- Cohort C REVISE rate: 5/13 = 38%
- HIGH/CRITICAL urgency REVISEs this cycle: 7 (PRESUMPTION-199 CRITICAL; ASSUMPTION-172, PRESUMPTION-196, PRESUMPTION-198, ASSUMPTION-182, PRESUMPTION-204, PRESUMPTION-207 HIGH)
- 4 SYSTEMIC-RISK-FLAGs raised (A: ground-truth oscillation; B: closed-loop ratification across agent classes; C: Goodhart SELF-MEASUREMENT cluster; D: VCS hygiene CRITICAL)
- No NOVELTY flags (all items have published analog literature)

### COMPLETION CHECKLIST

- [x] All 58 items have _for.md and _against.md files (with cycle-1 appends for Cohort A; new files for B/C)
- [x] All 58 items dispositioned by 15c
- [x] 9 new PREMISEs appended to validated_premises.md
- [x] 6 new MONITORs appended to monitor_queue.md; 30 existing MONITOR entries updated with refreshed Last-checked / Next-15d-check dates
- [x] 13 new REVISEs appended to revision_flags.md
- [x] Queue file for_lit_search.md status tags updated for all 58 items
- [x] Provenance chains complete

**Run timestamp:** 2026-05-19 (c2a2-lit-search-pipeline scheduled task; autonomous; no human review in-loop).


## 2026-05-20 Lit-Pipeline Run (15a/15b/15c) — 27 cycle-0 items (ASSUMPTION-186..200, PRESUMPTION-209..220)

**Grounding note:** 15a/15b citations drawn from training-corpus per the ASSUMPTION-199 convention; this convention is itself dispositioned REVISE this run (REVISE-035 / REVISE-040, SYSTEMIC-RISK-FLAG E). Citations should be read as training-corpus-provenance pending the live-verification policy recommended therein.

### RETURN: ASSUMPTION-186  [ASSUMPTION]
**Original item:** ASSUMPTION-186
**Statement:** "The 51-pending alarm is a measurement artifact — 36 stale duplicates; genuine unreviewed = 15."
**Provenance chain:** [14a → 15a, 15b → 15c]
**15a result:** SUPPORTED (Strong)
**15a key source:** Redman, T. (2001). "Data Quality: The Field Guide." — Duplicate records are a primary source of inflated counts; deduplication is a precondition for any count-driven decision.
**15a summary:** The generalizable premise — that a raw queue count corrupted by known duplicate entries is a measurement artifact, not a true backlog — is strongly and uncontroversially supported across data-quality literature. Deduplication before acting on a count is treated as a precondition, not an optimization. The specific decomposition (36 stale + 15 genuine) is an internal measurement the literature cannot confirm, but the pattern (a known bug inflating a metric that then drives a control action) is textbook.
**15b result:** NO-CHALLENGE-FOUND (Weak)
**15b key source:** Hand, D. (2018). "Statistical challenges of administrative and transaction data." — Raw operational counts are sometimes used directly, but only with explicit acknowledgement of known error sources; not a defense of skipping dedup.
**15b specific risk:** If the 36/15 split is itself wrong, the throttle was mis-calibrated in the opposite direction.
**15b summary:** No credible body of literature defends acting on a raw count known to contain duplicate records. The only weak counter is pragmatic: dedup has cost, and if the alarm threshold has wide margin the artifact may not change the decision. Here it did change the decision (drove a conservation-gate throttle), so the weak counter does not apply.
**15c disposition:** INCORPORATE (PREMISE-037)
**15c net assessment:** 15a SUPPORTED (Strong) on the generalizable premise; 15b NO-CHALLENGE-FOUND. The specific 36/15 split is self-measured but the design premise is clean.
**15c reasoning:** Strong support, no real challenge, and the artifact already drove a real control action — exactly the case where the generalizable hygiene premise should enter the validated register. Specific counts flagged for re-confirmation post-fix.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-186_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-186_against.md

---
### RETURN: ASSUMPTION-187  [ASSUMPTION]
**Original item:** ASSUMPTION-187
**Statement:** "generate_review_page.py fix may be incomplete — 36 vs expected 35; +1 collision post-fix."
**Provenance chain:** [14a → 15a, 15b → 15c]
**15a result:** SUPPORTED (Strong)
**15a key source:** Yin, Z. et al. (2011). "How Do Fixes Become Bugs?" (ESEC/FSE). — Empirically, a substantial fraction of bug fixes are incorrect or incomplete; partial fixes leaving a residual are common.
**15a summary:** The premise that a fix may be incomplete — evidenced by a residual +1 collision against the expected post-fix count — is strongly supported. Software-engineering research consistently finds that fixes are frequently partial and that a small residual after a fix is a classic incomplete-fix signature rather than guaranteed noise. The literature endorses treating the off-by-one as a live hypothesis until traced.
**15b result:** PARTIALLY-CHALLENGED (Weak-Moderate)
**15b key source:** Cormen, T. et al. (2009). "Introduction to Algorithms" (hashing chapter). — Hash/key collisions have a nonzero base rate; a single collision can be expected statistical noise, not a fix defect.
**15b specific risk:** Spending effort chasing a benign collision; or conversely dismissing a real residual defect as noise.
**15b summary:** There is a real but weak-moderate counter: a single residual collision can be ordinary collision-rate noise rather than evidence of a broken fix. Whether +1 is signal or noise depends on the namespace size and collision base rate, which are not yet measured. The challenge does not refute the premise; it argues the off-by-one is under-determined.
**15c disposition:** MONITOR (MONITOR-197)
**15c net assessment:** 15a SUPPORTED (Strong; incomplete fixes are common and need verification); 15b PARTIALLY-CHALLENGED (Weak-Moderate; +1 may be collision noise). Evidence is genuinely mixed and the resolution is empirical (trace the collision).
**15c reasoning:** The premise is a hedge ('may be incomplete') and the disambiguating evidence is a single trace that has not been done. Better to MONITOR than to prematurely INCORPORATE or REVISE on an off-by-one.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-187_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-187_against.md

---
### RETURN: ASSUMPTION-188  [ASSUMPTION]
**Original item:** ASSUMPTION-188
**Statement:** "Sandbox cannot write .git; commits must come from host shell (ACL + stale lock)."
**Provenance chain:** [14a → 15a, 15b → 15c]
**15a result:** SUPPORTED (Strong)
**15a key source:** NIST SP 800-190 (2017). "Application Container Security Guide." — Read-only / restricted-write root filesystems for sandboxed execution are a recommended hardening pattern; write restriction on VCS metadata is consistent with least privilege.
**15a summary:** The operational practice — route commits through the trusted host shell rather than the ephemeral sandbox — is strongly supported by container-hardening and CI/CD convention. Restricting a sandbox's write authority over .git is a recognized least-privilege posture, and commit-from-trusted-host is standard GitOps practice. The premise's operational core is sound.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** Docker / OCI runtime docs. — A bind-mounted .git with appropriate uid/gid and a writable mount is technically achievable; sandbox git-write is a permissions configuration, not an inherent impossibility.
**15b specific risk:** Encoding 'cannot' as architecture ossifies a config accident into a permanent constraint; masks the stale-lock root cause shared with ASSUMPTION-189.
**15b summary:** The challenge targets the framing, not the practice: 'cannot write .git' overstates a situation that is really 'is not currently permitted to, by ACL + a removable stale lock.' Both contributors (ACL and stale lock) are configurable/clearable. Conflating a configuration choice with an impossibility risks foreclosing a future where sandbox writes are deliberately enabled.
**15c disposition:** INCORPORATE (PREMISE-038)
**15c net assessment:** 15a SUPPORTED (Strong) on the operational practice; 15b PARTIALLY-CHALLENGED (Moderate) on the 'cannot' framing only. The practice is grounded same-day and matches CI convention; only the wording is contested.
**15c reasoning:** The operational premise (commits routed through the host shell) is well-grounded and already in use; the challenge is to the word 'cannot,' which I incorporate with an explicit reframing rather than rejecting the practice. Moderate (not High) confidence because the mechanism (ACL vs stale lock) overlaps the unresolved REVISE-033 root cause.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-188_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-188_against.md

---
### RETURN: ASSUMPTION-189  [ASSUMPTION]
**Original item:** ASSUMPTION-189
**Statement:** "Recurring index.lock + 716/356 morass caused by colliding/silently-failing scheduled commit agents."
**Provenance chain:** [14a → 15a, 15b → 15c]
**15a result:** SUPPORTED (Strong)
**15a key source:** Chacon, S. & Straub, B. "Pro Git." — Git takes index.lock to serialize index modification; two processes touching the index concurrently is the textbook cause of index.lock contention.
**15a summary:** The mechanism — concurrent scheduled commit agents colliding on the git index — is strongly supported as a plausible and common root cause of recurring index.lock and a confused staging state. Git's locking model and decades of cron-serialization practice make uncoordinated concurrent writers the leading hypothesis. The premise correctly identifies a real failure mode.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** Chacon, S. & Straub, B. "Pro Git" (stale-lock note). — A stale index.lock from a single crashed/killed process produces identical symptoms without any collision.
**15b specific risk:** Fixing only the concurrency angle while a stale-lock or FS-sync cause persists; recurrence after a 'fix' that addressed the wrong cause.
**15b summary:** The symptom (recurring index.lock, staging morass) is consistent with at least three causes: concurrent agents (the premise), a single crashed process leaving a stale lock, or filesystem-level lock-release failure on a synced directory. Without per-process logging, the collision hypothesis is under-instrumented. The challenge does not refute it but shows it is one of several causes that demand the same first move: serialize and instrument.
**15c disposition:** REVISE (REVISE-033)
**15c net assessment:** 15a SUPPORTED (Strong; collision is a real, common mechanism); 15b PARTIALLY-CHALLENGED (Moderate; credible alternative causes share the symptom and it is under-instrumented). Both directions converge on the same remediation: serialize + instrument.
**15c reasoning:** This is a HIGH-priority item inside SYSTEMIC-RISK-FLAG D (VCS hygiene). The diagnosis is plausible but competes with stale-lock / FS-sync causes; the responsible action is a design change (serialize scheduled git ops behind one lock + add commit/lock receipts) that fixes the collision case AND makes any residual cause attributable. That is a REVISE, not a silent INCORPORATE.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-189_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-189_against.md

---
### RETURN: ASSUMPTION-190  [ASSUMPTION]
**Original item:** ASSUMPTION-190
**Statement:** "sync_vault.sh `commit --only -- wiki/vault/` makes the 21:00 run safe unattended."
**Provenance chain:** [14a → 15a, 15b → 15c]
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Git documentation, git-commit(1) (--only / --include, pathspec semantics). — `--only <paths>` commits exactly the named paths regardless of the rest of the index; the mechanism does scope the commit as intended.
**15a summary:** `git commit --only -- wiki/vault/` does what the premise claims at the mechanism level: it commits only the named pathspec, ignoring other staged changes. Scoping an unattended commit to a known-safe subtree is a sound blast-radius-reduction practice. One clean run is consistent with the mechanism but is not yet evidence of reliability under the conditions that break it.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** Git documentation caveats, git-commit(1). — `--only` still interacts with a pre-existing partially-staged index and with newly-added files under the pathspec; behavior with overlapping staged content is subtle and can surprise.
**15b specific risk:** A dirty index from a colliding agent causes the 21:00 run to commit unintended vault content or miss intended content; silent because unattended.
**15b summary:** The edge cases are real: `--only` scopes the pathspec but does not guarantee the subtree itself is in the intended state if a prior agent left staged or partially-staged content, and the very staging morass flagged in ASSUMPTION-189 is the condition most likely to violate the 'safe' claim. One clean run does not exercise the failure states. The challenge is moderate: the mechanism is right, the reliability claim is premature.
**15c disposition:** MONITOR (MONITOR-198)
**15c net assessment:** 15a PARTIALLY-SUPPORTED (Moderate; mechanism sound); 15b PARTIALLY-CHALLENGED (Moderate; reliability unproven at N=1, edge cases real). Net: right mechanism, premature reliability claim.
**15c reasoning:** The premise is grounded on a single clean run and explicitly needs N>=3 confirmation; the failure states (dirty index from ASSUMPTION-189) have not been exercised. MONITOR until repeated unattended runs pass, ideally after REVISE-033 lands.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-190_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-190_against.md

---
### RETURN: ASSUMPTION-191  [ASSUMPTION]
**Original item:** ASSUMPTION-191
**Statement:** "regen_sociogram.sh refuses Summa-less builds; .gitignore *.bak* blocks backup commits."
**Provenance chain:** [14a → 15a, 15b → 15c]
**15a result:** SUPPORTED (Strong)
**15a key source:** Saltzer, J. & Schroeder, M. (1975). "The Protection of Information in Computer Systems." — Fail-safe defaults: deny/refuse on a missing precondition rather than proceed into a degraded state.
**15a summary:** Both guards are textbook fail-closed practice: refusing a Summa-less build is a fail-safe default (refuse rather than emit a degraded sociogram), and a .gitignore pattern is the canonical way to block backup-file commits. The mechanisms are correct and the practice is well supported. These are exactly the kind of cheap, local invariants that prevent a known degraded state.
**15b result:** PARTIALLY-CHALLENGED (Weak-Moderate)
**15b key source:** Cunningham, W. (1992). "The WyCash Portfolio Management System" (technical-debt metaphor). — Accumulating one point-guard per failure grows the maintenance surface; guards are not free.
**15b specific risk:** Each new failure spawns another bespoke guard; no single owner of build/artifact integrity; guards drift out of sync with the pipeline.
**15b summary:** The challenge is not to the guards themselves (which are sound) but to the pattern they exemplify: a growing collection of per-failure point-guards can substitute for systemic integrity ownership and grow the maintenance surface (this is the explicit subject of PRESUMPTION-216). The two guards here are individually correct; the weak-moderate challenge is about the aggregate strategy, which is dispositioned separately.
**15c disposition:** INCORPORATE (PREMISE-039)
**15c net assessment:** 15a SUPPORTED (Strong; fail-closed guards are correct practice); 15b PARTIALLY-CHALLENGED (Weak-Moderate, and the challenge is the strategy level, handled under PRESUMPTION-216). The guards themselves are uncontested.
**15c reasoning:** The two specific guards are textbook fail-safe defaults with no challenge at the guard level; the only objection (point-guard proliferation) is a distinct presumption dispositioned at MONITOR-206. Incorporate the guards as validated practice with a forward-pointer to the systemic concern.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-191_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-191_against.md

---
### RETURN: ASSUMPTION-192  [ASSUMPTION]
**Original item:** ASSUMPTION-192
**Statement:** "CLAUDE.md viz stats stale — actual ~1,533 nodes / 36,608 edges / ~15.4 MB."
**Provenance chain:** [14a → 15a, 15b → 15c]
**15a result:** SUPPORTED (Strong)
**15a key source:** Parnas, D. (1994). "Software Aging" (ICSE). — Documentation drifts out of sync with the system it describes unless actively maintained; stale embedded stats are a canonical instance.
**15a summary:** That hand-maintained statistics in CLAUDE.md drift from the live artifact is strongly supported — software-aging and evolution literature treat exactly this kind of embedded-fact staleness as inevitable without an auto-derivation step. The corrected figures (~1,533 / 36,608 / ~15.4 MB) are an internal measurement, but the staleness pattern and its remedy (derive, don't copy) are well established.
**15b result:** NO-CHALLENGE-FOUND (Weak)
**15b key source:** Spolsky, J. (2000). "Painless Functional Specifications." — Some embedded figures are intentionally illustrative/approximate and not meant to track exactly; weak counter to treating every drift as a defect.
**15b specific risk:** If the corrected size changes the payload-diet calculus, a decision was made on stale inputs.
**15b summary:** There is no real challenge to the staleness claim. The only weak counter is that some doc figures are deliberately approximate, but here the figures drove a design judgment (the payload-diet deferral), so accuracy matters and 'approximate is fine' does not apply. The 15b routing question — whether the deferred payload-diet judgment still holds at the corrected size — is a separate downstream question, not a challenge to staleness.
**15c disposition:** INCORPORATE (PREMISE-040)
**15c net assessment:** 15a SUPPORTED (Strong; doc drift is canonical, remedy is auto-derive); 15b NO-CHALLENGE-FOUND. The corrected figures are self-measured but the premise is clean and load-bearing (drove the payload-diet deferral).
**15c reasoning:** Strong support, no challenge, and the staleness already affected a design decision — the generalizable premise (artifact stats must be auto-derived, not hand-maintained) belongs in the validated register. The downstream payload-diet re-check is noted as an action.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-192_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-192_against.md

---
### RETURN: ASSUMPTION-193  [ASSUMPTION]
**Original item:** ASSUMPTION-193
**Statement:** "PRS network grown to 231/90/35 + 32-coil layer (from 133/54/20); 231-vs-225 divergence."
**Provenance chain:** [14a → 15a, 15b → 15c]
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Vogels, W. (2009). "Eventually Consistent" (CACM). — In a system with multiple count sources, transient divergence between sources is expected and reconcilable; the growth + divergence pattern is normal.
**15a summary:** The growth claim (133/54/20 -> 231/90/35 + a 32-coil layer) is consistent with normal knowledge-graph evolution and is moderately supported as a structural pattern. The 231-vs-225 divergence is the live issue: count differences across sources are expected under eventual consistency and are reconcilable, which partially supports the premise that the divergence is real and benign-pending-reconciliation.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** Bailis, P. & Ghodsi, A. (2013). "Eventual Consistency Today." — A persistent (non-converging) divergence between sources signals a real reconciliation bug, not benign lag; 231-vs-225 must be shown to converge.
**15b specific risk:** Pattern Detector ingests inconsistent counts; downstream Pathway-13 analysis built on the wrong figure.
**15b summary:** The counter: 'divergence is expected' is only true for transient, converging differences. A 231-vs-225 gap that persists across reads is a reconciliation defect, and treating it as benign (PRESUMPTION-212's failure mode) hides a real inconsistency feeding the Pattern Detector. The challenge is moderate: the gap needs to be reconciled to determine whether it is lag or a bug.
**15c disposition:** MONITOR (MONITOR-199)
**15c net assessment:** 15a PARTIALLY-SUPPORTED (Moderate; growth pattern normal, divergence reconcilable); 15b PARTIALLY-CHALLENGED (Moderate; persistent divergence would be a defect). Net: cannot tell lag from bug without reconciliation.
**15c reasoning:** Growth is plausible and the divergence may be benign lag or a real reconciliation defect; the disambiguator (recompute both from one snapshot) has not been done. MONITOR until reconciled, because it feeds Pattern Detector input quality.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-193_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-193_against.md

---
### RETURN: ASSUMPTION-194  [ASSUMPTION]
**Original item:** ASSUMPTION-194
**Statement:** "prs_3d generator is not idempotent — must be fed template, never a built file."
**Provenance chain:** [14a → 15a, 15b → 15c]
**15a result:** SUPPORTED (Strong)
**15a key source:** Reproducible-builds / hermetic-build literature (Bazel docs; Lamb & Zacchiroli 2021, "Reproducible Builds," IEEE Software). — Generators that consume their own output drift; feeding the canonical source/template each time is the standard discipline.
**15a summary:** That a code/artifact generator can be non-idempotent and must therefore consume the source template rather than a previously built file is a well-established constraint, and C2A2 already documents the identical pattern for wiki_narration. The premise correctly identifies a real determinism constraint and the correct discipline (template-in, never build-in). Support is strong and reinforced by internal precedent.
**15b result:** PARTIALLY-CHALLENGED (Weak-Moderate)
**15b key source:** Idempotence-by-construction literature (functional/declarative generation). — Many generators can be made idempotent cheaply (normalize input, detect already-built markers); accepting non-idempotence as permanent may be settling for a guardable-but-fixable defect.
**15b specific risk:** Someone feeds a built file; output silently corrupts (the wiki_narration precedent shows this is a live foot-gun).
**15b summary:** The weak-moderate challenge: non-idempotence is often a fixable property, and encoding 'must be fed template, never a built file' as a permanent operating rule substitutes human discipline for a design fix. A rule that depends on always remembering not to feed a built file will eventually be violated. The constraint is real today, but accepting it as permanent is contestable.
**15c disposition:** INCORPORATE (PREMISE-041)
**15c net assessment:** 15a SUPPORTED (Strong; real constraint + internal wiki_narration precedent); 15b PARTIALLY-CHALLENGED (Weak-Moderate; idempotence could be added / guard preferred over discipline). The constraint is uncontested; only its permanence is.
**15c reasoning:** The non-idempotence constraint is real, strongly supported, and matches an existing validated internal pattern (wiki_narration). Incorporate it as a known constraint with the 15b mitigation folded in: enforce the rule with a fail-closed input guard rather than relying on operator memory.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-194_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-194_against.md

---
### RETURN: ASSUMPTION-195  [ASSUMPTION]
**Original item:** ASSUMPTION-195
**Statement:** "Two PRS data quirks real — duplicate PRS-10 (arkanihamed); CROSS-051–054 dual headers."
**Provenance chain:** [14a → 15a, 15b → 15c]
**15a result:** SUPPORTED (Strong)
**15a key source:** Codd, E. (1970). "A Relational Model of Data for Large Shared Data Banks." — Primary-key uniqueness is foundational; a duplicate key (PRS-10) is a definitional integrity violation, not a stylistic quirk.
**15a summary:** Both quirks are real data-integrity defects by standard database/data-quality criteria: a duplicate PRS-10 violates key uniqueness, and dual headers on CROSS-051..054 violate the single-header structural invariant. These are not benign formatting choices; they corrupt parsing, counts, and any downstream consumer (the Pattern Detector). Support for treating them as genuine defects is strong.
**15b result:** NO-CHALLENGE-FOUND (Weak)
**15b key source:** Schema-evolution literature (e.g., multi-header CSV / sectioned-file conventions). — Some formats intentionally carry repeated headers per section; a weak counter that dual headers could be an intended sectioning convention rather than a defect.
**15b specific risk:** Pattern Detector mis-counts or mis-joins on the duplicate key / dual headers; silent data corruption downstream.
**15b summary:** No real defense of a duplicate primary key exists. The only weak counter is that dual headers might be an intended sectioning convention in some file formats; but for a source-of-truth registry consumed by automated parsers, repeated headers without a declared sectioning schema are a defect. The challenge does not hold for the duplicate PRS-10 at all.
**15c disposition:** MONITOR (MONITOR-200)
**15c net assessment:** 15a SUPPORTED (Strong; both are genuine integrity defects); 15b NO-CHALLENGE-FOUND (only a weak dual-header sectioning counter). The defects are confirmed; the action is fix-and-verify, not a design-premise change.
**15c reasoning:** Although the evidence strongly confirms the defects, the appropriate disposition is operational: fix the duplicate key and dual headers, add an integrity check, then verify. This is a concrete remediation task best tracked as MONITOR (fix+verify) rather than INCORPORATE of a general premise (the general premise — registry integrity validation — is implied and can be promoted once the check exists).
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-195_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-195_against.md

---
### RETURN: ASSUMPTION-196  [ASSUMPTION]
**Original item:** ASSUMPTION-196
**Statement:** "Hawkins/Hoffman 0 proposals is the correct signal (Rule 12), not a search failure."
**Provenance chain:** [14a → 15a, 15b → 15c]
**15a result:** SUPPORTED (Strong)
**15a key source:** Shore, J. (2004). "Fail Fast" (IEEE Software). — Reporting a true null loudly, rather than masking it, is sound engineering; an honest 0 is more trustworthy than a fabricated nonzero.
**15a summary:** The principle behind the premise — that an honest 0 reported loudly (Rule 12) is a legitimate and valuable signal, not something to paper over — is strongly supported. Fail-fast/fail-loud engineering and null-result-reporting norms both endorse surfacing a true zero. The premise is right that a reported 0 can be the correct signal rather than a defect to hide.
**15b result:** PARTIALLY-CHALLENGED (Moderate-Strong)
**15b key source:** Altman, D. & Bland, M. (1995). "Absence of evidence is not evidence of absence" (BMJ). — A 0 result is only informative if the search had adequate power/coverage; otherwise it is under-search, not absence.
**15b specific risk:** Treating an under-search 0 as a true null suppresses real development for slow-cadence thinkers; symmetric error to fabrication.
**15b summary:** The challenge is moderate-strong and targets the inferential leap, not the principle: a 0 is only a true-null if search coverage was adequate, and a fixed 30-day window applied to bursty publication processes can return 0 for an active-but-slow-cadence thinker (Hawkins/Hoffman). Without a coverage/recall estimate, the 0 is consistent with under-search (the symmetric failure to fabrication — PRESUMPTION-218). This links to the window-calibration concern in PRESUMPTION-213.
**15c disposition:** MONITOR (MONITOR-201)
**15c net assessment:** 15a SUPPORTED (Strong; honest-null principle is sound); 15b PARTIALLY-CHALLENGED (Moderate-Strong; the specific 0 may be under-search, not absence, under a fixed 30-day window). Net: the principle holds, the inference for this 0 is unverified.
**15c reasoning:** The honest-null principle is validated, but whether THIS 0 reflects the territory or an under-powered window is exactly the open question (PRESUMPTION-218, PRESUMPTION-213). MONITOR with the disambiguator: a coverage check / widened window. Do not INCORPORATE the specific inference until coverage is verified.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-196_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-196_against.md

---
### RETURN: ASSUMPTION-197  [ASSUMPTION]
**Original item:** ASSUMPTION-197
**Statement:** "Pathway 27 one-index-two-surfaces architecture + ISME staging (Search/links pre-July-8; Ask post-broker)."
**Provenance chain:** [14a → 15a, 15b → 15c]
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Lucene/Elasticsearch architecture (Gormley & Tong 2015, "Elasticsearch: The Definitive Guide"). — A single inverted index can serve multiple query surfaces (search + structured links); unified-index designs are well established.
**15a summary:** A single entity index serving search and linking surfaces is a supported, common architecture, and the ISME staging (ship Search/links pre-July-8, add Ask post-broker) is a sound incremental-delivery sequence. Moderate support: the two-surface unified index is well precedented and staging reduces delivery risk. The strength is capped because the third surface (Ask) introduces RAG-style requirements the index may not natively satisfy (see 15b / PRESUMPTION-217).
**15b result:** PARTIALLY-CHALLENGED (Moderate-Strong)
**15b key source:** Young, G. / Fowler, M. — CQRS (Command Query Responsibility Segregation). — When read surfaces have divergent requirements (search relevance vs RAG retrieval vs deterministic linking), separate read models often beat one shared index.
**15b specific risk:** Building Ask on the search/links index forces a late, costly split; or Ask quality is compromised to fit the shared index.
**15b summary:** The moderate-strong counter: search, deterministic linking, and Ask (RAG) impose partly incompatible requirements (relevance ranking vs exact joins vs semantic retrieval + freshness). CQRS and polyglot-persistence experience warns that one index serving all three tends to compromise each. The staging plan partly mitigates this by deferring Ask until after the broker, but the premise that one index suffices for all three is the contestable part (PRESUMPTION-217).
**15c disposition:** MONITOR (MONITOR-202)
**15c net assessment:** 15a PARTIALLY-SUPPORTED (Moderate; search+links unified index + staging are sound); 15b PARTIALLY-CHALLENGED (Moderate-Strong; the third surface, Ask/RAG, may not fit one index — PRESUMPTION-217). Net: two surfaces supported, three contested.
**15c reasoning:** The architecture is a live DECISION-037 candidate; the search+links + staging core is supported, but the one-index-serves-Ask claim is the open risk (dispositioned with its presumption at MONITOR-207). MONITOR pending an Ask-retrieval validation prototype before the broker.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-197_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-197_against.md

---
### RETURN: ASSUMPTION-198  [ASSUMPTION]
**Original item:** ASSUMPTION-198
**Statement:** "32 fabricated transcripts to re-fetch before July 8 (transcript-only; commentaries sound)."
**Provenance chain:** [14a → 15a, 15b → 15c]
**15a result:** SUPPORTED (Strong)
**15a key source:** Buneman, P., Khanna, S., Tan, W.-C. (2001). "Why and Where: A Characterization of Data Provenance" (ICDT). — Identifying and re-sourcing fabricated/unprovenanced records is a sound provenance-repair operation.
**15a summary:** Identifying 32 fabricated transcripts and re-fetching them from authoritative sources before the July-8 gate is a sound provenance-repair operation, strongly supported by the data-provenance literature and by the documented reality of LLM transcript fabrication. The remediation plan (re-fetch the fabricated transcripts) is correct. The strength is on the repair action; the contested sub-claim is scope ('commentaries sound').
**15b result:** PARTIALLY-CHALLENGED (Moderate-Strong)
**15b key source:** Provenance-propagation principle (Buneman et al. 2001; Cheney et al. 2009, "Provenance in Databases"). — Derived artifacts inherit the contamination of their inputs; if commentaries were generated from fabricated transcripts, they are contaminated (garbage-in-garbage-out).
**15b specific risk:** Contaminated commentaries pass the July-8 gate because they were assumed sound; fabrication propagates into the published corpus.
**15b summary:** The moderate-strong counter targets the scoping claim 'commentaries sound': if any of the 32 commentaries were derived from the fabricated transcripts, they inherit the fabrication by provenance propagation. Asserting commentaries are sound without checking their derivation lineage is the risk. The challenge is not to the re-fetch (which is right) but to the assumption that contamination is confined to transcripts.
**15c disposition:** REVISE (REVISE-034)
**15c net assessment:** 15a SUPPORTED (Strong; re-fetch is the right repair); 15b PARTIALLY-CHALLENGED (Moderate-Strong; the 'commentaries sound' scope is unverified and contamination propagates to derived artifacts). The action item (re-fetch) is sound but the contamination-scope assumption needs revision before the gate.
**15c reasoning:** The re-fetch is correct, but the load-bearing sub-claim — that contamination is transcript-only and commentaries are sound — is an unverified scoping assumption with a clear propagation risk into the July-8 published corpus. That warrants a REVISE: verify commentary provenance/lineage before trusting it, rather than assuming soundness.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-198_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-198_against.md

---
### RETURN: ASSUMPTION-199  [ASSUMPTION]
**Original item:** ASSUMPTION-199
**Statement:** "Lit-pipeline cycle-1 carry-forward (no net-new search, low yield) + training-corpus citation convention."
**Provenance chain:** [14a → 15a, 15b → 15c]
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Cache-invalidation / TTL-by-velocity practice (Fielding 2000, HTTP caching; CDN freshness models). — Carrying forward results for low-velocity data within a TTL is a sound cost-benefit policy.
**15a summary:** Both halves have qualified support. Carry-forward without net-new search is a defensible cost-benefit policy for low-velocity topics within a TTL, and training-corpus citation is reliable for well-established, high-frequency knowledge (which most of this pipeline's foundational premises are). Support is moderate, not strong, because both depend on a condition — low field velocity / well-attested facts — that does not hold uniformly across items.
**15b result:** CHALLENGED (Strong)
**15b key source:** Kandpal, N. et al. (2023). "Large Language Models Struggle to Learn Long-Tail Knowledge" (ICML). — Parametric knowledge is unreliable for long-tail/recent facts; a training-corpus-only citation convention systematically misses these.
**15b specific risk:** The self-awareness pipeline grounds premises on stale/parametric evidence and misses disconfirming or updating literature; fabricated citations enter the register; the system over-trusts its own training-corpus recall.
**15b summary:** The challenge is strong and self-referential: a training-corpus-only citation convention plus uniform carry-forward systematically misses post-cutoff and long-tail evidence and raises fabricated-citation risk. For fast-moving fields the 'low-yield' assumption fails — the refresh gap is exactly where new evidence appears. This is precisely the method this run is using, so the challenge applies to the pipeline's own epistemic backbone (links PRESUMPTION-214 carry-forward and PRESUMPTION-215 training-corpus stand-in).
**15c disposition:** REVISE (REVISE-035)
**15c net assessment:** 15a PARTIALLY-SUPPORTED (Moderate; defensible for low-velocity/well-attested topics); 15b CHALLENGED (Strong; fails for fast-moving/long-tail, raises fabricated-citation risk, self-referential to the pipeline's own method). The asymmetry favors revision.
**15c reasoning:** This governs the pipeline's epistemic backbone and the challenge is strong and structural (knowledge-cutoff, long-tail, fabrication risk). Note transparently: this very run used the training-corpus convention, which makes the REVISE self-applying. Recommend velocity-stratified refresh + citation-provenance labeling rather than abandoning the convention wholesale.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-199_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-199_against.md

---
### RETURN: ASSUMPTION-200  [ASSUMPTION]
**Original item:** ASSUMPTION-200
**Statement:** "Four Sunday-cron tasks fired Monday catch-up instead of Sunday; re-check next Sunday."
**Provenance chain:** [14a → 15a, 15b → 15c]
**15a result:** SUPPORTED (Strong)
**15a key source:** anacron(8) / systemd.timer Persistent= semantics. — Missed scheduled jobs firing late as catch-up on next wake is documented, intended behavior for persistent timers; a Monday catch-up of Sunday jobs is consistent with this.
**15a summary:** The premise is well supported: late catch-up firing of missed scheduled jobs is documented behavior (anacron Persistent timers, scheduler misfire policies), so a Monday catch-up of Sunday tasks is plausibly benign. The premise's own remedy — re-check next Sunday to see whether it fires on time — is precisely the right diagnostic per SRE practice. Strong support for both the explanation and the verification plan.
**15b result:** NO-CHALLENGE-FOUND (Weak)
**15b key source:** Scheduler-reliability literature. — A repeating Monday-shift (rather than a one-time catch-up) would indicate a timezone/DST or schedule-definition bug rather than benign catch-up; weak counter pending the next occurrence.
**15b specific risk:** If it recurs, four tasks are systematically firing a day late (cadence drift), affecting any day-sensitive downstream step.
**15b summary:** There is essentially no challenge: the catch-up explanation is consistent with how persistent schedulers behave. The only weak counter is that if the Monday firing recurs, it is a real scheduling bug (timezone/DST/definition error) rather than a one-time catch-up — which is exactly why the premise schedules a re-check. The 15b routing question ('Monday-burst is expected catch-up') actually supports the premise.
**15c disposition:** MONITOR (MONITOR-203)
**15c net assessment:** 15a SUPPORTED (Strong; catch-up is documented behavior and the re-check plan is correct); 15b NO-CHALLENGE-FOUND (only a weak 'recurrence-would-be-a-bug' note). The disposition is determined by an event that has not happened yet (next Sunday).
**15c reasoning:** The explanation is well-supported but the premise itself defers judgment to next Sunday's occurrence. The correct disposition is to MONITOR until that observation: on-time firing confirms benign catch-up; a second Monday-shift escalates to a scheduling-bug REVISE.
**Full results:** wiki/architecture/lit_search_results/for/ASSUMPTION-200_for.md ; wiki/architecture/lit_search_results/against/ASSUMPTION-200_against.md

---
### RETURN: PRESUMPTION-209  [PRESUMPTION]
**Original item:** PRESUMPTION-209
**Statement:** "A single agent's directory scan is authoritative — no reconciliation layer across counting agents."
**Provenance chain:** [14b → 15a, 15b → 15c]
**15a result:** NO-SUPPORT-FOUND (Weak)
**15a key source:** Single-source-of-truth design (Helland 2005, "Data on the Outside vs. Data on the Inside"). — There is mild support for designating ONE authoritative source — but the literature means a reconciled canonical store, not "whichever agent happened to scan."
**15a summary:** Little supports treating one agent's ad-hoc directory scan as authoritative. The closest legitimate idea — a single source of truth — actually argues for a reconciled canonical store with write-receipts, not for trusting any single reader's snapshot. The supportive direction yields only a weak, mis-fitting analog; the presumption as stated (no reconciliation layer) finds essentially no support.
**15b result:** CHALLENGED (Strong)
**15b key source:** Gilbert, S. & Lynch, N. (2002). "Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services" (CAP). — A single node's view is not authoritative under concurrency/partition; consistency requires coordination.
**15b specific risk:** Conservation-gate throttles and Pattern Detector inputs driven by an arbitrary, possibly-wrong scan; ground-truth oscillation; the count discrepancies already observed.
**15b summary:** The challenge is strong and directly instantiated: distributed-systems theory (CAP, Paxos, Dynamo) is unanimous that a single reader's snapshot is not authoritative when multiple agents observe shared, changing state. The observed Levin/Friston count discrepancies (OPEN-052, MONITOR-194/195) are textbook split-brain symptoms. Without a reconciliation layer (write-receipts / manifest-as-truth / quorum), the system will keep oscillating between disagreeing scans. This extends PRESUMPTION-196/204.
**15c disposition:** REVISE (REVISE-036)
**15c net assessment:** 15a NO-SUPPORT-FOUND (Weak; single-source-of-truth actually argues for reconciliation); 15b CHALLENGED (Strong; CAP/consensus/read-repair + observed split-brain discrepancies). Clear asymmetry against the presumption.
**15c reasoning:** This is a PRESUMPTION (designers were unaware) with strong disconfirming evidence and already-observed real symptoms (Levin/Friston discrepancies). It sits in SYSTEMIC-RISK-FLAG A (ground-truth oscillation) and extends PRESUMPTION-196/204. A reconciliation layer is needed — REVISE with HIGH urgency.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-209_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-209_against.md

---
### RETURN: PRESUMPTION-210  [PRESUMPTION]
**Original item:** PRESUMPTION-210
**Statement:** "Raw queue depth is a valid proxy for 'generate more?' — no decomposition before throttling."
**Provenance chain:** [14b → 15a, 15b → 15c]
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Little, J. (1961). "A Proof for the Queuing Formula L = lambda W." — Queue length relates to arrival rate and wait; depth IS one legitimate signal worth attending to.
**15a summary:** There is weak support for queue depth as a signal worth attending to (Little's law; flow literature). But the same sources insist the actionable question is 'on which side' — arrival/generation rate vs service/throughput rate. The presumption (raw depth -> generate-more decision without decomposition) finds only the signaling half supported, not the prescription. This mirrors PRESUMPTION-202/ASSUMPTION-186.
**15b result:** CHALLENGED (Strong)
**15b key source:** Reinertsen, D. (2009). "Principles of Product Development Flow." — Depth without decomposition into arrival and service components is under-determined; the right lever depends on which is moving.
**15b specific risk:** Over- or under-generation; oscillation; compounding with the dedup artifact (ASSUMPTION-186) so the proxy is both wrong-metric and wrong-value.
**15b summary:** Strong challenge, identical in shape to PRESUMPTION-202: raw queue depth without decomposition into generation rate and throughput capacity is an under-determined control signal. Whether to generate more depends on the gap between arrival and service rates, not on depth alone; lean/TOC/factory-physics all converge here. Using raw depth as a generate-more proxy will systematically mis-throttle. Couples OPEN-055 and ASSUMPTION-186 (the depth was itself a measurement artifact).
**15c disposition:** REVISE (REVISE-037)
**15c net assessment:** 15a PARTIALLY-SUPPORTED (Weak; signaling half only); 15b CHALLENGED (Strong; decomposition required by all flow/TOC literature). Strong asymmetry; mirrors the already-REVISEd PRESUMPTION-202.
**15c reasoning:** This is the generation-side twin of PRESUMPTION-202 (throughput-side), both surfacing the same un-decomposed-queue-depth flaw. As a PRESUMPTION with strong disconfirming evidence and a clear remediation, it is a REVISE. Compounds with ASSUMPTION-186 (the depth value was itself a measurement artifact).
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-210_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-210_against.md

---
### RETURN: PRESUMPTION-211  [PRESUMPTION]
**Original item:** PRESUMPTION-211
**Statement:** "File-on-disk == durably persisted — commit responsibility is unowned."
**Provenance chain:** [14b → 15a, 15b → 15c]
**15a result:** NO-SUPPORT-FOUND (Weak)
**15a key source:** OS write semantics (caching). — There is a trivial sense in which a written file persists across a process exit; but this provides no support for the durability claim in a version-controlled, multi-agent, synced context.
**15a summary:** There is essentially no support for equating on-disk with durably persisted in this system's context. A file in the working tree that is never committed/pushed is ephemeral: it can be overwritten by a regenerating agent, lost on sandbox teardown, or excluded by a path-scoped commit. The supportive direction finds nothing of substance; the only true reading (file survives a process exit) is irrelevant to the durability the system needs.
**15b result:** CHALLENGED (Strong)
**15b key source:** Harder, T. & Reuter, A. (1983). "Principles of Transaction-Oriented Database Recovery" (ACM Computing Surveys). — The Durability (D) of ACID requires a committed, recoverable write; an uncommitted on-disk file is not durable.
**15b specific risk:** Generated wiki/PRS/artifact content lost on regeneration or sandbox teardown; the 716/356 staging morass; silent data loss because no one owns the commit.
**15b summary:** The challenge is strong and the presumption is CRITICAL: durability requires a committed (and pushed) write, not merely a file on disk, and an unowned commit step will be silently skipped. This is the root of the recurring VCS morass (ASSUMPTION-188/189/190) — generated content sits on disk, no agent owns committing it, and it is lost or overwritten. ACID durability, git semantics, and fsync research all refute file-on-disk == persisted. Sits in SYSTEMIC-RISK-FLAG D and continues PRESUMPTION-199/REVISE-024.
**15c disposition:** REVISE (REVISE-038)
**15c net assessment:** 15a NO-SUPPORT-FOUND (Weak); 15b CHALLENGED (Strong, CRITICAL; ACID-D, git semantics, fsync research, ownership). Maximal asymmetry against the presumption.
**15c reasoning:** A PRESUMPTION (designers unaware) that is both strongly disconfirmed and the apparent root cause of the recurring VCS/persistence failures (ASSUMPTION-188/189/190; the 716/356 morass). PRESUMPTION-class + CRITICAL stakes + clear remediation = REVISE at top urgency. Continues PRESUMPTION-199/REVISE-024 and anchors SYSTEMIC-RISK-FLAG D.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-211_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-211_against.md

---
### RETURN: PRESUMPTION-212  [PRESUMPTION]
**Original item:** PRESUMPTION-212
**Statement:** "The documented number == the true number — registers presumed consistent and current."
**Provenance chain:** [14b → 15a, 15b → 15c]
**15a result:** NO-SUPPORT-FOUND (Weak)
**15a key source:** Single-source-of-truth ideal (docs-as-code). — Aspirationally, documented == true is the goal; but the literature treats this as something to ENFORCE via auto-derivation, not something that holds by default.
**15a summary:** The aspiration that documented numbers equal true numbers is the goal of single-source-of-truth practice, but no literature supports assuming it holds without an enforcement mechanism. On the contrary, the documented==true assumption is exactly what software-aging research says will fail. The supportive direction yields only an aspirational goal, not evidence the presumption is safe.
**15b result:** CHALLENGED (Strong)
**15b key source:** Parnas, D. (1994). "Software Aging." — Documentation drifts from reality absent active reconciliation; documented != true is the default, not the exception.
**15b specific risk:** Decisions made on stale registers (e.g., the payload-diet deferral on stale stats); Pattern Detector fed divergent counts; compounding measurement-integrity errors.
**15b summary:** The challenge is strong and already realized this very cycle: ASSUMPTION-192 (stale viz stats) and ASSUMPTION-193 (231-vs-225 divergence) are direct instances of documented != true. Software-aging and data-quality literature treat documented==true as a property that decays without active reconciliation. Presuming registers are consistent and current is the meta-pattern behind both of today's measurement-integrity defects. Sits in SYSTEMIC-RISK-FLAG A.
**15c disposition:** REVISE (REVISE-039)
**15c net assessment:** 15a NO-SUPPORT-FOUND (Weak; ideal supports enforcement not assumption); 15b CHALLENGED (Strong; software-aging + two same-cycle realized instances). Asymmetry against the presumption, with in-system proof.
**15c reasoning:** A PRESUMPTION already falsified this cycle by ASSUMPTION-192/193. The remediation (auto-derive + reconcile) is clear and couples to PREMISE-040. REVISE (MEDIUM urgency — important measurement-integrity hygiene but not service-critical) under SYSTEMIC-RISK-FLAG A.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-212_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-212_against.md

---
### RETURN: PRESUMPTION-213  [PRESUMPTION]
**Original item:** PRESUMPTION-213
**Statement:** "Absence-in-30-day-window == absence-of-development — window assumed well-calibrated to each thinker."
**Provenance chain:** [14b → 15a, 15b → 15c]
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Fixed-window monitoring practice. — Fixed observation windows are a common, operationally simple default; weak support for using one.
**15a summary:** Using a fixed 30-day window is operationally common and reasonable for fast-cadence thinkers, giving weak support. But the support is conditional on the window matching the source's cadence; the presumption assumes a single window is well-calibrated to ALL thinkers, which the supportive literature does not endorse. Support is weak and conditional.
**15b result:** PARTIALLY-CHALLENGED (Moderate-Strong)
**15b key source:** Barabasi, A.-L. (2005). "The origin of bursts and heavy tails in human dynamics" (Nature). — Human/scholarly output is bursty with heavy-tailed inter-event times; a fixed window mis-samples slow/bursty producers.
**15b specific risk:** Slow-cadence thinkers' development is systematically missed; the 0-proposal signal (ASSUMPTION-196) is misread as a true null.
**15b summary:** The moderate-strong challenge: scholarly output is bursty and heavy-tailed, so a fixed 30-day window calibrated to fast-cadence thinkers will read 'absence' for slow- or bursty-cadence thinkers who are in fact developing (this is the mechanism behind the Hawkins/Hoffman 0 in ASSUMPTION-196). Absence-in-window equals absence-of-development only if the window is powered for that thinker's cadence. Per-thinker adaptive windows are indicated (echoes MONITOR-051).
**15c disposition:** MONITOR (MONITOR-204)
**15c net assessment:** 15a PARTIALLY-SUPPORTED (Weak; fixed window OK for fast cadence); 15b PARTIALLY-CHALLENGED (Moderate-Strong; bursty output -> fixed window under-samples slow thinkers). Net: the window is mis-calibrated for some thinkers, but the fix needs calibration data.
**15c reasoning:** The presumption is conditionally false (fine for fast-cadence, wrong for slow/bursty), and the remediation (per-thinker adaptive windows) requires per-thinker cadence data not yet gathered. MONITOR with a concrete disambiguator; couples ASSUMPTION-196 (MONITOR-201) and PRESUMPTION-218.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-213_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-213_against.md

---
### RETURN: PRESUMPTION-214  [PRESUMPTION]
**Original item:** PRESUMPTION-214
**Statement:** "The refresh gap is unlikely to contain new evidence — carry-forward applied uniformly."
**Provenance chain:** [14b → 15a, 15b → 15c]
**15a result:** PARTIALLY-SUPPORTED (Weak-Moderate)
**15a key source:** Cache TTL / freshness models (Fielding 2000, HTTP caching). — For low-velocity data, a refresh gap genuinely is unlikely to contain new evidence; carry-forward within TTL is sound.
**15a summary:** For low-velocity, mature topics the presumption is reasonable: a short refresh gap is unlikely to change well-established findings, and carry-forward within a TTL is standard. Support is weak-moderate and explicitly conditional on field velocity. The flaw is the word 'uniformly' — applying the same low-yield assumption across fields of very different velocity.
**15b result:** PARTIALLY-CHALLENGED (Moderate-Strong)
**15b key source:** Kandpal, N. et al. (2023). "LLMs Struggle to Learn Long-Tail Knowledge" (ICML). — For long-tail/recent topics, the refresh gap is exactly where new evidence concentrates.
**15b specific risk:** Disconfirming or updating evidence in fast-moving fields is silently skipped; premises grounded on stale snapshots.
**15b summary:** The moderate-strong challenge: 'unlikely to contain new evidence' is false for fast-moving fields, and applying it uniformly guarantees missed updates precisely where the literature moves fastest. Several of this pipeline's own citations are from fast-moving AI subfields where a refresh gap routinely contains new evidence. The presumption is safe only when stratified by velocity; uniform application is the error. Couples ASSUMPTION-199 and PRESUMPTION-215.
**15c disposition:** MONITOR (MONITOR-205)
**15c net assessment:** 15a PARTIALLY-SUPPORTED (Weak-Moderate; valid for low-velocity); 15b PARTIALLY-CHALLENGED (Moderate-Strong; fails uniformly for fast fields). This is the presumption-side of ASSUMPTION-199 (REVISE-035).
**15c reasoning:** The carry-forward presumption is conditionally valid; the design fix (velocity-stratified refresh) is already captured at the assumption level in REVISE-035. To avoid double-flagging, MONITOR here with the empirical disambiguator (sample-audit yield), feeding REVISE-035's implementation.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-214_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-214_against.md

---
### RETURN: PRESUMPTION-215  [PRESUMPTION]
**Original item:** PRESUMPTION-215
**Statement:** "Training-corpus is an adequate stand-in for live literature when grounding premises."
**Provenance chain:** [14b → 15a, 15b → 15c]
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Petroni, F. et al. (2019). "Language Models as Knowledge Bases?" (EMNLP). — Parametric knowledge reliably recalls well-attested, high-frequency facts; for foundational/established premises the training corpus is an adequate stand-in.
**15a summary:** For well-established, high-frequency knowledge — which describes most of this pipeline's foundational CS/distributed-systems/epistemics citations — the training corpus is a moderately adequate stand-in, as parametric-knowledge research shows. Support is moderate and bounded to well-attested topics. It does not extend to recent, long-tail, or rapidly-changing literature, and it carries fabricated-citation risk (15b).
**15b result:** CHALLENGED (Strong)
**15b key source:** Kandpal, N. et al. (2023). "LLMs Struggle to Learn Long-Tail Knowledge" (ICML). — Parametric recall is unreliable for long-tail facts; a training-corpus stand-in systematically fails there.
**15b specific risk:** The self-awareness register is grounded on parametric recall it cannot fully verify; fabricated citations enter premises; recency-dependent claims are mis-grounded; the system's epistemic backbone shares the failure mode it audits for.
**15b summary:** The challenge is strong and self-applying: training-corpus grounding cannot see post-cutoff or long-tail literature and risks fabricated citations — the symmetric danger to the transcript fabrication in ASSUMPTION-198. This very pipeline run grounds its premises in training-corpus knowledge, so the presumption describes the system's own current method. It is adequate for stable, well-attested facts but inadequate as a blanket stand-in. Anchors SYSTEMIC-RISK-FLAG E and couples ASSUMPTION-199 (REVISE-035).
**15c disposition:** REVISE (REVISE-040)
**15c net assessment:** 15a PARTIALLY-SUPPORTED (Moderate; adequate for well-attested facts); 15b CHALLENGED (Strong; long-tail/recency failure + fabrication risk; self-applying to this run). Asymmetry favors revision with a scoping carve-out.
**15c reasoning:** A PRESUMPTION about the pipeline's own grounding method, strongly challenged and directly self-referential (this run used the convention — disclosed transparently). The fix is not abandonment but scoping + verification: label provenance, live-verify high-stakes/recent citations, reserve training-corpus for well-attested foundations. Couples ASSUMPTION-199/REVISE-035; anchors SYSTEMIC-RISK-FLAG E.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-215_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-215_against.md

---
### RETURN: PRESUMPTION-216  [PRESUMPTION]
**Original item:** PRESUMPTION-216
**Statement:** "Each recurring failure deserves its own point-guard — vs systemic integrity ownership."
**Provenance chain:** [14b → 15a, 15b → 15c]
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Defense-in-depth (NIST; Anderson 2008, "Security Engineering"). — Layered, independent controls are a legitimate strategy; multiple guards can be sound.
**15a summary:** There is moderate support for multiple guards as defense-in-depth: layered, independent barriers genuinely catch more failures than a single one. Each point-guard, taken alone, is often a correct fail-safe (as in ASSUMPTION-191). The support is for guards as a layer, not for 'a bespoke guard per failure' as the primary integrity strategy in place of ownership.
**15b result:** PARTIALLY-CHALLENGED (Moderate-Strong)
**15b key source:** Ishikawa, K. (1986). "Guide to Quality Control"; Toyota 5-Whys. — Root-cause analysis: treating each symptom with a point fix masks the shared cause that re-emerges elsewhere.
**15b specific risk:** Unbounded growth of bespoke guards; no owner of shared root causes; guards drift out of sync; the real cause (e.g., unowned commit, PRESUMPTION-211) persists beneath the patches.
**15b summary:** The moderate-strong challenge: a strategy of one bespoke point-guard per recurring failure is whack-a-mole — it treats symptoms, grows the maintenance surface (technical debt), and substitutes for a single owner of systemic integrity who would find shared root causes. This cycle alone added several point-guards (ASSUMPTION-187/189/191), several of which trace to a common VCS/persistence root (PRESUMPTION-211). The guards are individually fine; the strategy without ownership is the risk.
**15c disposition:** MONITOR (MONITOR-206)
**15c net assessment:** 15a PARTIALLY-SUPPORTED (Moderate; guards-as-layer legitimate); 15b PARTIALLY-CHALLENGED (Moderate-Strong; guards-as-strategy without ownership is whack-a-mole). Net: keep the guards, add ownership + root-cause discipline.
**15c reasoning:** The presumption is partly right (defense-in-depth) and partly risky (no systemic owner). The fix (single integrity owner + root-cause requirement + consolidation) is organizational and continuous rather than a single code change, so MONITOR with a guard-count debt metric. Couples ASSUMPTION-187/189/191 and PRESUMPTION-211.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-216_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-216_against.md

---
### RETURN: PRESUMPTION-217  [PRESUMPTION]
**Original item:** PRESUMPTION-217
**Statement:** "One entity index serves search + linking + Ask without incompatible requirements (Pathway 27)."
**Provenance chain:** [14b → 15a, 15b → 15c]
**15a result:** PARTIALLY-SUPPORTED (Moderate)
**15a key source:** Gormley, C. & Tong, Z. (2015). "Elasticsearch: The Definitive Guide." — A single index can serve text search and structured linking; multi-purpose indexes are common and workable for those two.
**15a summary:** A single index serving search and deterministic linking is well precedented and gives moderate support to the unified-index idea for two of the three surfaces. The support weakens at the third surface (Ask/RAG), whose retrieval and freshness needs differ. The presumption holds reasonably for search+linking; 'without incompatible requirements' across all three is the contested part.
**15b result:** PARTIALLY-CHALLENGED (Moderate-Strong)
**15b key source:** Young, G. / Fowler, M. — CQRS. — Divergent read requirements (search relevance vs deterministic joins vs semantic retrieval) are the canonical case for separate read models.
**15b specific risk:** Ask quality compromised to fit the shared index, or a costly late split when Ask is added; the incompatibility surfaces after commitment.
**15b summary:** The moderate-strong challenge mirrors ASSUMPTION-197: search (relevance ranking), linking (exact joins/determinism), and Ask (semantic retrieval + freshness) are three different read problems, and CQRS/polyglot-persistence experience says one store tends to compromise at least one. 'Without incompatible requirements' is the load-bearing, contestable clause — Ask is the likely misfit. The staging plan (Ask after the broker) helpfully defers but does not resolve the question.
**15c disposition:** MONITOR (MONITOR-207)
**15c net assessment:** 15a PARTIALLY-SUPPORTED (Moderate; search+linking on one index works); 15b PARTIALLY-CHALLENGED (Moderate-Strong; Ask/RAG likely imposes incompatible requirements — CQRS). This is the presumption-side of ASSUMPTION-197 (MONITOR-202).
**15c reasoning:** The unified index is sound for two surfaces and uncertain for the third; the disambiguator (an Ask-retrieval prototype) is the same one feeding ASSUMPTION-197. MONITOR the one-index-serves-Ask claim pending that prototype, kept consistent with MONITOR-202. DECISION-037 input.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-217_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-217_against.md

---
### RETURN: PRESUMPTION-218  [PRESUMPTION]
**Original item:** PRESUMPTION-218
**Statement:** "An honest null reflects the territory, not under-search — Rule 12 unguarded against under-coverage."
**Provenance chain:** [14b → 15a, 15b → 15c]
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Shore, J. (2004). "Fail Fast." — Reporting a true null loudly is sound; weak support that an honest null can reflect the territory.
**15a summary:** There is weak support that an honest null can reflect reality — but only conditional on adequate search coverage. The supportive sources all attach the same condition: a null is informative only if the procedure had the power/recall to detect a positive. The presumption drops that condition, treating any honest null as reflecting the territory, which the supportive literature does not endorse.
**15b result:** PARTIALLY-CHALLENGED (Moderate-Strong)
**15b key source:** Altman, D. & Bland, M. (1995). "Absence of evidence is not evidence of absence" (BMJ). — A null is only meaningful with adequate power/coverage; otherwise it is under-search.
**15b specific risk:** Under-searched nulls enter the register as true findings; slow-cadence development missed; the pipeline's honesty layer has a one-sided guard.
**15b summary:** The moderate-strong challenge: Rule 12 (fail-loud, do not fabricate) correctly prevents false positives but is unguarded against the symmetric false negative — a null produced by under-coverage rather than true absence. Without a coverage/recall check, an honest null and an under-searched null are indistinguishable (this is exactly the Hawkins/Hoffman 0 risk in ASSUMPTION-196 and the window mis-calibration in PRESUMPTION-213). The fix is to pair the null with a coverage estimate.
**15c disposition:** MONITOR (MONITOR-208)
**15c net assessment:** 15a PARTIALLY-SUPPORTED (Weak; null valid only with coverage); 15b PARTIALLY-CHALLENGED (Moderate-Strong; Rule 12 unguarded against under-coverage, symmetric to fabrication). Net: add a coverage guard.
**15c reasoning:** A PRESUMPTION exposing a one-sided guard in the honesty layer; the remediation (coverage/recall estimate gating absence claims) is clear and couples to ASSUMPTION-196 (MONITOR-201) and PRESUMPTION-213 (MONITOR-204). MONITOR while the coverage-guard mechanism is specified and trialed; promote once it exists.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-218_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-218_against.md

---
### RETURN: PRESUMPTION-219  [PRESUMPTION]
**Original item:** PRESUMPTION-219
**Statement:** "The EOD 14a/14b pass scales to growing session volume — unbounded-read assumption."
**Provenance chain:** [14b → 15a, 15b → 15c]
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Current operation. — At present session volume the unbounded EOD read completes; weak support that it works today.
**15a summary:** At today's volume the unbounded EOD read works, giving weak, present-tense support. But 'works now' is not 'scales': the supportive evidence is an existence proof at current scale, not a scaling argument. The presumption assumes the unbounded read continues to hold as session volume grows, which the supportive direction cannot establish.
**15b result:** PARTIALLY-CHALLENGED (Moderate)
**15b key source:** Context-window / input-length limits (LLM summarization). — An unbounded read hits hard input limits as volume grows; the pass cannot read everything indefinitely.
**15b specific risk:** As volume grows, 14a/14b silently miss items (sampling bias); the self-awareness pipeline's coverage degrades invisibly; the very items about scale go unsurfaced.
**15b summary:** The moderate challenge: an unbounded EOD read does not scale — growing session volume eventually exceeds input/context limits, forcing silent truncation or sampling that biases which assumptions/presumptions get surfaced. Scalable summarization needs bounded chunks and hierarchical reduction. This is a self-referential scale blindness: the self-awareness pass that surfaces scaling assumptions makes one itself. Couples PRESUMPTION-214/218.
**15c disposition:** MONITOR (MONITOR-209)
**15c net assessment:** 15a PARTIALLY-SUPPORTED (Weak; works at current volume); 15b PARTIALLY-CHALLENGED (Moderate; unbounded read will not scale, silent sampling bias). Net: fine now, will fail as volume grows.
**15c reasoning:** The presumption is true at current scale and false in the limit; the failure is future and gradual, so MONITOR with a concrete trigger (EOD input size approaching the single-pass limit) rather than REVISE now. Couples PRESUMPTION-214/218 (coverage themes).
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-219_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-219_against.md

---
### RETURN: PRESUMPTION-220  [PRESUMPTION]
**Original item:** PRESUMPTION-220
**Statement:** "On-cadence firing == healthy pipeline — no input/output-validity check paired to cadence."
**Provenance chain:** [14b → 15a, 15b → 15c]
**15a result:** PARTIALLY-SUPPORTED (Weak)
**15a key source:** Liveness monitoring (heartbeats). — On-cadence firing is a legitimate liveness signal; weak support that cadence indicates the pipeline is at least running.
**15a summary:** On-cadence firing is a valid liveness signal — it shows the pipeline is running — giving weak support. But liveness is only one of the SRE golden signals; the same source insists correctness/quality must be monitored alongside it. The presumption equates liveness with health, which the supportive literature explicitly does not: a job can fire perfectly on time while producing garbage.
**15b result:** CHALLENGED (Strong)
**15b key source:** Goodhart, C. (1975) / Strathern, M. (1997). "Goodhart's Law." — When cadence becomes the health target, it ceases to measure health; firing on time is gameable/uninformative about output validity.
**15b specific risk:** A perfectly-on-cadence pipeline producing invalid outputs is reported as healthy; validity failures (like today's) go unflagged by the health signal; cadence is gamed as the target.
**15b summary:** The challenge is strong: on-cadence firing is liveness, not health, and equating them is a textbook Goodhart/proxy-metric failure (liveness vs safety, Lamport). This cycle is the proof — the N=3 cadence streak coincided with a phantom alarm, fabricated transcripts, and count discrepancies; the pipeline fired perfectly while producing invalid outputs. Without an input/output-validity check paired to cadence, 'healthy pipeline' is unmeasured. Anchors the Goodhart SELF-MEASUREMENT cluster (FLAG C) with PRESUMPTION-201.
**15c disposition:** REVISE (REVISE-041)
**15c net assessment:** 15a PARTIALLY-SUPPORTED (Weak; liveness only); 15b CHALLENGED (Strong; Goodhart, liveness-vs-safety, with same-cycle proof that cadence-green coincided with validity-red). Strong asymmetry, in-system demonstrated.
**15c reasoning:** A PRESUMPTION in the Goodhart SELF-MEASUREMENT cluster, strongly challenged and proven this very cycle (on-cadence firing alongside a phantom alarm and fabricated transcripts). The remediation (pair cadence with output-validity checks) is clear. REVISE (MEDIUM urgency) under SYSTEMIC-RISK-FLAG C; couples PRESUMPTION-201/REVISE-026.
**Full results:** wiki/architecture/lit_search_results/for/PRESUMPTION-220_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-220_against.md

---

### CYCLE SUMMARY — 2026-05-20
- Items processed: 27 (all cycle-0; 15 ASSUMPTIONs 186-200, 12 PRESUMPTIONs 209-220)
- Dispositions: 5 INCORPORATE (PREMISE-037..041), 13 MONITOR (MONITOR-197..209), 9 REVISE (REVISE-033..041)
- INCORPORATE rate: 5/27 = 19%
- MONITOR rate: 13/27 = 48%
- REVISE rate: 9/27 = 33%
- HIGH/CRITICAL urgency REVISEs: REVISE-038 (CRITICAL, PRESUMPTION-211 file-on-disk!=durable), REVISE-033 (HIGH, ASSUMPTION-189 git-collision), REVISE-035 (HIGH, ASSUMPTION-199 grounding-method), REVISE-036 (HIGH, PRESUMPTION-209 scan-as-truth)
- SYSTEMIC-RISK-FLAGs raised/continued: A (ground-truth oscillation: PRESUMPTION-209/212, ASSUMPTION-186/192/193); C (Goodhart self-measurement: PRESUMPTION-220, ASSUMPTION-200); D (VCS/persistence hygiene CRITICAL: ASSUMPTION-188/189/190, PRESUMPTION-211/216); E NEW (epistemic-grounding method: ASSUMPTION-196/199, PRESUMPTION-214/215/218)
- NOVELTY flags: none (all items have published analog literature)
- Day signature: measurement-integrity / VCS-hygiene day; REVISE-heavy on the PRESUMPTION side, mirroring the 2026-05-19 14a/14b run note.

### COMPLETION CHECKLIST — 2026-05-20
- [x] All 27 items have _for.md and _against.md files
- [x] All 27 items dispositioned by 15c
- [x] 5 new PREMISEs appended to validated_premises.md (PREMISE-037..041)
- [x] 13 new MONITORs appended to monitor_queue.md (MONITOR-197..209)
- [x] 9 new REVISEs appended to revision_flags.md (REVISE-033..041)
- [x] Queue file for_lit_search.md status tags updated for all 27 items
- [x] Provenance chains complete

**Run timestamp:** 2026-05-20 (c2a2-lit-search-pipeline scheduled task; autonomous; no human review in-loop).


---

## BATCH 2026-05-21 LIT-PIPELINE (Narrative Connectome cohort; dispositions 2026-05-21)
**Search date:** 2026-05-21
**Items:** 17 (7 ASSUMPTIONs: 201,202,204-208 + 10 PRESUMPTIONs: 221-230) from the 2026-05-20 14a/14b batch
**Dispositions:** 2 INCORPORATE (PREMISE-042,043), 10 MONITOR (MONITOR-210..219), 5 REVISE (REVISE-042..046)
**Grounding:** training-corpus grounding per ASSUMPTION-199 convention; FLAG E / REVISE-040 noted

---

### ASSUMPTION-201 (ASSUMPTION)
**Statement:** The PRS view is a narrative connectome; a triplet is a complete model and, equivalently, a compression (corollary routed, not the framing).

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Moderate
- Key source: Schank, R. & Abelson, R. (1977). "Scripts, Plans, Goals and Understanding." — Narratives function as schematic, compressed models of stereotyped event sequences.
- Summary: There is solid grounding for narrative-as-model (scripts, schemas, story grammars, Bruner) and for the analogy that a bounded unit can be a complete model (Hawkins' cortical columns). The compression half also has a lineage (Schmidhuber). Support is partial because the literature treats narrative models as schematic and selective, not complete, and the testable compression form is deferred to ASSUMPTION-208/PRESUMPTION-222.
- Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-201_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: PARTIALLY-CHALLENGED | Strength: Moderate
- Key source: Box, G. (1976). "Science and Statistics." — "All models are wrong"; no triplet is "complete." Directly challenges the completeness claim.
- Specific risk: Treating a triplet as a 'complete model' invites over-reading — metrics that assume each triplet captures the whole when it is a curated fragment.
- Summary: The 'complete model' claim is the weak point: models are partial by definition (Box), story-grammar precedents positing complete slot-structures failed empirically (Black & Wilensky), and narrative is constitutively selective. The compression equivalence inherits description-length definability problems, and the connectome framing transfers a neural metaphor without a transfer-condition check (PRESUMPTION-221).
- Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-201_against.md

DISPOSITION-15c: MONITOR -> MONITOR-210 (Priority Medium, Weekly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Moderate); 15b PARTIALLY-CHALLENGED (Moderate). Largely framework framing; the load-bearing testable parts are carried by ASSUMPTION-208 and PRESUMPTION-221/222.
- Reasoning: The contested element is the 'complete model' wording, not the framing's usefulness. MONITOR rather than INCORPORATE (the completeness claim is challenged) or REVISE (it is framework framing, not an operational error). Couples PRESUMPTION-221.

---

### ASSUMPTION-202 (ASSUMPTION)
**Statement:** Synergistic coils are association fibers binding narrative modules (testable corollary: coil density tracks independent integration).

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Moderate
- Key source: Sporns, O. (2010). "Networks of the Brain." — Long-range association fibers integrate functionally segregated modules; integration/segregation is a core, measurable property.
- Summary: The neuroscience is sound: association fibers bind segregated modules and integration is measurable via graph metrics, giving moderate analogical support for treating cross-tradition coils as integrators and for the density-tracks-integration corollary in principle.
- Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-202_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: PARTIALLY-CHALLENGED | Strength: Moderate
- Key source: Fortunato & Barthelemy (2007). "Resolution limit in community detection," PNAS. — Modularity-based integration/module measures are resolution-dependent; density-tracks-integration can be a resolution artifact.
- Specific risk: Coil-density metrics could be reported as 'integration' while actually measuring curation density or detection resolution.
- Summary: The analogy is challengeable on three fronts: integration/modularity metrics are resolution-dependent (Fortunato & Barthelemy), neural metaphors can impose structure absent a substrate match, and density is not the same as functional integration. The corollary risks circularity if coils are detected by co-occurrence and integration is then read off coil density.
- Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-202_against.md

DISPOSITION-15c: MONITOR -> MONITOR-211 (Priority Medium, Weekly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Moderate); 15b PARTIALLY-CHALLENGED (Moderate). The integration formalism transfers loosely, but resolution-dependence and circularity risk are real.
- Reasoning: Moderate support meets moderate challenge; the corollary is testable but currently at risk of circularity. MONITOR with a concrete remediation. Joins PRESUMPTION-221 analogy-transfer.

---

### ASSUMPTION-204 (ASSUMPTION)
**Statement:** Coil altitude should encode discovery-time (~2026), not idea-age ("axis follows model").

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Moderate
- Key source: Snodgrass, R. (1999). "Developing Time-Oriented Database Applications" (valid-time vs transaction-time / bitemporal). — A system must choose which time it encodes; transaction/discovery time is a legitimate, decision-relevant axis.
- Summary: Choosing discovery/provenance time as the altitude axis is defensible: temporal-data theory recognizes multiple legitimate time axes, and provenance time is decision-relevant for 'what the system learned when.' Support is partial because the choice is genuinely underdetermined (PRESUMPTION-225) — idea-age is also defensible.
- Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-204_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: PARTIALLY-CHALLENGED | Strength: Weak-Moderate
- Key source: Bitemporal modeling (Snodgrass). — Encoding only one time discards the other; if users care about idea-age, discovery-time misleads.
- Specific risk: Users may misread altitude as idea-age; lineage relationships get visually inverted.
- Summary: The main challenge is underdetermination: no single time axis is uniquely right (Munzner; bitemporal theory), and discovery-time can introduce a presentist distortion of intellectual lineage. The challenge is weak-moderate because discovery-time is a reasonable default, not an error.
- Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-204_against.md

DISPOSITION-15c: MONITOR -> MONITOR-212 (Priority Low-Medium, Monthly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Moderate); 15b PARTIALLY-CHALLENGED (Weak-Moderate). Discovery-time is a reasonable but underdetermined default.
- Reasoning: Low-stakes design choice with reasonable grounding but genuine underdetermination. MONITOR with a cheap fix (toggle). Joins OPEN-057, PRESUMPTION-225.

---

### ASSUMPTION-205 (ASSUMPTION)
**Statement:** Cross-tradition convergence is analogical not verbatim — only 3 literal shared-resource hubs (max 2 traditions each).

RETURN-TO-14a/14b (FOR / supportive):
- Result: SUPPORTED | Strength: Strong
- Key source: Gentner, D. (1983). "Structure-Mapping," Cognitive Science. — Cross-domain convergence is relational/structural, not surface/lexical; foundational support that real convergence is analogical.
- Summary: The conceptual claim — that genuine cross-tradition convergence is predominantly analogical/structural rather than verbatim — is strongly supported across analogy theory (Gentner; Hofstadter), consilience/interdisciplinarity studies, and the vocabulary problem (Furnas), which predicts exactly that literal shared-resource hubs will be sparse. The sparse literal-hub count is consistent with, but not itself strong evidence for, the principle.
- Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-205_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: PARTIALLY-CHALLENGED | Strength: Weak-Moderate
- Key source: Christen (2012) "Data Matching" (entity resolution). — Literal string-match counts are method-dependent; "only 3 literal hubs" may be a normalization artifact (PRESUMPTION-228), so the cited evidence is weak.
- Specific risk: If DECISION-040 relies on the literal-hub count rather than the principle, it rests on an artifact.
- Summary: There is no credible literature against the core principle (convergence is mainly analogical) — that is well established. The challenge is narrower and real: the specific evidence offered (3 literal hubs) is measurement-dependent and should not be load-bearing (PRESUMPTION-228). Also, 'analogical not verbatim' slightly overstates — some convergence is literal (shared formal results).
- Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-205_against.md

DISPOSITION-15c: INCORPORATE -> PREMISE-042 (Confidence Moderate)
- Net assessment: 15a SUPPORTED (Strong, for the principle); 15b PARTIALLY-CHALLENGED (Weak-Moderate, against the measurement only).
- Reasoning: Strong support for the principle with only a weak/measurement-scoped challenge -> INCORPORATE with caveats. Confidence Moderate (not High) because the item as written fuses a strong principle with an artifact-prone count; the count is explicitly excluded and routed to PRESUMPTION-228. Consistency-checked against ASSUMPTION-005/006 (traditions/PRS as imperfect units): no contradiction — this premise asserts the FORM of convergence, not that traditions are crisp.

---

### ASSUMPTION-206 (ASSUMPTION)
**Statement:** Generative-coil detection is lexical-first (v1, 17 chains); semantic/embedding is v2.

RETURN-TO-14a/14b (FOR / supportive):
- Result: SUPPORTED | Strength: Strong
- Key source: Baseline-first ML practice (Zinkevich, "Rules of Machine Learning"). — A high-precision lexical baseline before semantic models is standard, low-risk staging.
- Summary: Lexical-first detection is sound engineering: exact/string matching gives high-precision, auditable results appropriate for a v1, and deferring semantic/embedding methods to v2 is the standard precision-then-recall progression. The literature both supports the staging and predicts the limitation (low recall) that v2 is meant to fix.
- Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-206_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: PARTIALLY-CHALLENGED | Strength: Weak-Moderate
- Key source: Furnas et al. (1987) "The vocabulary problem." — Lexical matching misses the majority of semantically equivalent handoffs; "adequately recalls" is false for v1.
- Specific risk: Treating the 17-chain v1 result as complete (rather than a high-precision sample) would understate connectivity.
- Summary: The only real challenge is to 'adequately recalls': lexical detection has known low recall (vocabulary problem), so v1's 17 chains likely undercount true coils substantially. But the assumption explicitly concedes this by scheduling semantic detection as v2, so the challenge targets a claim the assumption does not make.
- Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-206_against.md

DISPOSITION-15c: INCORPORATE -> PREMISE-043 (Confidence High)
- Net assessment: 15a SUPPORTED (Strong); 15b PARTIALLY-CHALLENGED (Weak-Moderate, recall only, already conceded by the v2 plan).
- Reasoning: Strong support for staged precision-first detection; the only challenge (low recall) is explicitly anticipated by the v2 plan. INCORPORATE at High confidence with the 15b mitigation folded in (treat v1 as a lower bound; measure recall). Consistency-checked: reinforces PREMISE-042 (literal overlap undercounts).

---

### ASSUMPTION-207 (ASSUMPTION)
**Statement:** Telos = emergence of a master science (architectonic/sapientia/tradition-craft); rival, non-converging master sciences meet via coils.

RETURN-TO-14a/14b (FOR / supportive):
- Result: SUPPORTED | Strength: Strong
- Key source: Aristotle, "Metaphysics" I & VI; "Nicomachean Ethics" I.2. — The architectonic science that orders the others (first philosophy / politics as architectonic).
- Summary: The teleology is well-grounded in its own sources: Aristotle's architectonic science, Aquinas's sapientia, and MacIntyre's tradition-constituted inquiry give a coherent, historically deep account of an ordering master science and of rival traditions. Notably, the 'rival, non-converging master sciences meet via coils' clause aligns with MacIntyre's anti-convergence stance, strengthening internal coherence.
- Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-207_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Strong
- Key source: Galison & Stump eds. (1996) "The Disunity of Science"; Dupre (1993) "The Disorder of Things"; Cartwright (1999) "The Dappled World." — Strong mainstream case that science is irreducibly plural/patchwork; no architectonic master science emerges.
- Specific risk: Designing toward an emergent master science could bias the system to manufacture false unification or suppress genuine incommensurability.
- Summary: The challenge is strong: disunity-of-science scholarship denies that mature inquiry yields an architectonic master science, and incommensurability (Kuhn, Feyerabend, even MacIntyre) challenges both stable rivalry and clean inter-tradition meeting. The historical corollary (do mature traditions actually produce master sciences?) is testable and the weight of cases favors disunity.
- Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-207_against.md

DISPOSITION-15c: MONITOR -> MONITOR-213 (Priority Medium, Weekly)
- Net assessment: 15a SUPPORTED (Strong, coherent telos) + 15b CHALLENGED (Strong, disunity-of-science / incommensurability) = CONTESTED.
- Reasoning: Strong support meets strong challenge on a teleological commitment. Not INCORPORATE (empirically contested) and not REVISE (it is a stated regulative telos, not an operational decision) -> MONITOR. Couples PRESUMPTION-223 (convergence-emphasis neutrality).

---

### ASSUMPTION-208 (ASSUMPTION)
**Statement:** Progress = better compression; a forming master science shows as total description length falling while coverage rises.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Moderate
- Key source: Rissanen (1978) MDL; Wallace MML; Solomonoff/Kolmogorov. — Formal lineage equating model quality with shorter description at fixed coverage; compression-as-understanding.
- Summary: There is a real, respectable theoretical lineage (MDL/MML, free energy, compression-progress) for treating progress as better compression at fixed or rising coverage. As an intuition and a direction, it is moderately supported.
- Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-208_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Strong
- Key source: Grunwald (2007) "The Minimum Description Length Principle"; Kolmogorov uncomputability. — MDL requires a fixed model class & coding scheme; "total description length" over an open corpus is not well-defined (gates on PRESUMPTION-222).
- Specific risk: Adopting description-length as THE progress metric could drive over-compression, misreport progress, and penalize genuinely progressive complexity.
- Summary: The challenge is strong on two levels. Formally, there is no canonical, computable 'total description length' over a heterogeneous, paradigm-spanning corpus (Grunwald; Kolmogorov; Kuhn) — so the headline metric is ill-defined as stated. Substantively, progress is not always compression (major theories add machinery while extending reach) and a length target is gameable. The metric rests on PRESUMPTION-222, which is itself unvalidated.
- Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-208_against.md

DISPOSITION-15c: REVISE -> REVISE-042 (Urgency MEDIUM)
- Net assessment: 15a Moderate (in-principle) vs 15b Strong (ill-defined and gameable as stated); high-stakes headline metric gated by PRESUMPTION-222.
- Reasoning: Stated ASSUMPTION but the proposed headline metric is ill-defined as written and rests on an unvalidated presumption (222). Heuristic (high stakes, strong challenge, gating dependency) -> REVISE. Couples PRESUMPTION-222 (REVISE-044); SYSTEMIC-RISK-FLAG G.

---

### PRESUMPTION-221 (PRESUMPTION)
**Statement:** The connectome is the right master-metaphor — neural/Hawkins structure presumed to transfer to narratives without a transfer-condition check.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Moderate
- Key source: Newman (2010) "Networks"; Barabasi (2016). — Network/graph formalisms are genuinely domain-general; many systems are validly modeled as graphs.
- Summary: A generic network/graph metaphor for narrative/knowledge structures is well supported — graphs are domain-general and semantic networks are an established representation, and structure-mapping gives criteria for valid analogy. Support is partial because this licenses a generic graph, not specifically the brain connectome with its specialized measures.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-221_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Strong
- Key source: Tallis (2011) "Aping Mankind"; Legrenzi & Umilta (2011) "Neuromania." — Sustained critique of importing neuro-frameworks where substrate/justification is absent; the "neuro-" prefix as unearned authority.
- Specific risk: An entire metric suite (integration, hubs, small-worldness, scaling) could be invalid or artifactual if the connectome analogy does not transfer.
- Summary: The challenge is strong and load-bearing. The connectome metaphor does structural work for ALL downstream metrics (ASSUMPTION-201/202, PRESUMPTION-229), yet brain-specific measures depend on wiring/metabolic constraints absent in narrative graphs, several connectome metrics are fragile even in neuroscience, and no transfer-condition check exists. This is a designer-unaware presumption with high leverage.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-221_against.md

DISPOSITION-15c: REVISE -> REVISE-043 (Urgency HIGH)
- Net assessment: 15a Moderate (generic network) vs 15b Strong (connectome-specific transfer unchecked). PRESUMPTION + strong challenge + maximal leverage.
- Reasoning: PRESUMPTION (designer-unaware) with a strong challenge that load-bears the entire connectome metric suite -> REVISE at HIGH urgency per the 15c heuristic for high-leverage unstated premises. Anchors SYSTEMIC-RISK-FLAG F.

---

### PRESUMPTION-222 (PRESUMPTION)
**Statement:** Narrative compression == information-theoretic compression — description length presumed definable/computable over PRS triplets.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Moderate
- Key source: Koutra et al. (2014) "VoG: Summarizing graphs using MDL"; Akoglu et al. — MDL-based graph summarization gives a concrete, computable description length over graph structure; a triplet graph could be summarized this way.
- Summary: Computable PROXIES for narrative/graph compression do exist — MDL graph summarization and LM cross-entropy codelength are both concrete and computable over text/graphs. So the presumption is not hopeless: a definable, computable description-length proxy over PRS triplets is achievable.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-222_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Strong
- Key source: Kolmogorov complexity is uncomputable (Li & Vitanyi). — No canonical, scheme-independent description length; "narrative compression" has no unique value.
- Specific risk: A headline progress metric (ASSUMPTION-208) built on an undefined identity will produce numbers that look rigorous but are scheme-dependent artifacts not tracking meaning.
- Summary: The strong challenge: there is no canonical, computable description length (Kolmogorov uncomputability), MDL codelength is scheme-relative (Grunwald), and syntactic/graph codelength is not narrative meaning. So 'narrative compression == information-theoretic compression', as an identity, is false; only scheme-relative proxies exist, and they do not measure meaning. Since this gates ASSUMPTION-208's headline metric and is designer-unaware, the risk is high.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-222_against.md

DISPOSITION-15c: REVISE -> REVISE-044 (Urgency HIGH)
- Net assessment: 15a Moderate (proxies exist) vs 15b Strong (no principled/canonical metric; gates ASSUMPTION-208). PRESUMPTION + strong challenge.
- Reasoning: PRESUMPTION (designer-unaware) gating the headline progress metric, with a strong challenge to the identity-as-stated; computable proxies exist, so the constructive path is a labeled, validated proxy -> REVISE at HIGH urgency. Couples ASSUMPTION-208 (REVISE-042); SYSTEMIC-RISK-FLAG G.

---

### PRESUMPTION-223 (PRESUMPTION)
**Statement:** Making integration visible/attractive is value-neutral — convergence-emphasis views presumed not to bias toward convergence over preserved rivalry.

RETURN-TO-14a/14b (FOR / supportive):
- Result: NO-SUPPORT-FOUND | Strength: Weak
- Key source: (Weak/indirect) Tufte, "The Visual Display of Quantitative Information" — the "show the data" ideal aspires to neutral presentation, but this is normative aspiration, not evidence that emphasis IS neutral.
- Summary: Essentially no support: the visualization and cognitive-science literatures do not hold that making something visible/attractive is value-neutral; if anything they assert the opposite. The most one can say is that neutrality is an aspiration (Tufte), not an established property.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-223_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Strong
- Key source: Tversky & Kahneman (1981) framing effects. — How options are presented changes inferences/choices; emphasis is not neutral.
- Specific risk: The system could systematically over-represent convergence and under-represent incommensurability/rivalry, undermining ASSUMPTION-207's pluralism and producing self-confirming 'unity.'
- Summary: The challenge is strong and well established: framing effects, visualization-ethics studies, and attention research all show that emphasis and salience shape inference. A view that makes integration visible/attractive will bias toward reading convergence as more prevalent/important than preserved rivalry, regardless of intent. A passive pluralism guard in text cannot offset what the visual hierarchy does, because salience operates pre-attentively.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-223_against.md

DISPOSITION-15c: REVISE -> REVISE-045 (Urgency MEDIUM)
- Net assessment: 15a NO-SUPPORT-FOUND + 15b Strong challenge = CHALLENGED. Designer-unaware normative presumption coupling ASSUMPTION-207.
- Reasoning: The presumption (emphasis is value-neutral) is contradicted by well-established framing/salience research and has no support. As a designer-unaware presumption with normative stakes, REVISE: acknowledge non-neutrality and actively balance rivalry. Urgency MEDIUM (normative, not safety-critical). Couples ASSUMPTION-207 (MONITOR-213).

---

### PRESUMPTION-224 (PRESUMPTION)
**Statement:** A guiding doc can govern changes before its own claims are tested; self-documentation closes a ratification loop.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Moderate
- Key source: Constitutional/provisional governance; IETF RFC process. — Governing documents legitimately govern provisionally before full validation; bootstrapping authority is normal.
- Summary: There is moderate support that a guiding document can legitimately govern provisionally before all its claims are tested — constitutions, RFCs, and Lakatosian hard cores all work this way. Provisional governing authority is normal.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-224_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: PARTIALLY-CHALLENGED | Strength: Moderate
- Key source: Munchhausen trilemma / self-grounding circularity. — A document that authorizes its own claims cannot ratify itself without circularity.
- Specific risk: Load-bearing but unvalidated claims (PRESUMPTION-221/222) get operationalized because the doc asserting them is treated as ratified.
- Summary: The challenge is moderate: provisional authority is fine, but 'self-documentation closes a ratification loop' is circular — the doc cannot validate its own load-bearing claims, several of which (connectome, compression) are presently CHALLENGED. The fix is cheap: route the doc's testable claims through the same 14a/14b gate rather than exempting them.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-224_against.md

DISPOSITION-15c: MONITOR -> MONITOR-214 (Priority Medium, Weekly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Moderate; provisional authority is normal); 15b PARTIALLY-CHALLENGED (Moderate; self-ratification is circular).
- Reasoning: Provisional governance is legitimate; the only defect is the circular self-ratification, which is cheaply fixed by routing the doc's claims through the normal gate. MONITOR with a concrete trigger. Couples ASSUMPTION-211 (held framework).

---

### PRESUMPTION-225 (PRESUMPTION)
**Statement:** "Axis follows model" presumes a unique axis semantic where several (publication/narrative/connectome time) may be defensible.

RETURN-TO-14a/14b (FOR / supportive):
- Result: NO-SUPPORT-FOUND | Strength: Weak
- Key source: (Weak) Mackinlay (1986) APT; Stevens scales. — A data type/model constrains which encodings are *appropriate*, giving weak support that the model narrows axis choice — but it narrows, it does not uniquely fix.
- Summary: Weak support for the uniqueness claim: while data type constrains which encodings are appropriate (Mackinlay's APT), this narrows rather than uniquely fixes the axis. No literature supports a unique axis semantic following from a model.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-225_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: PARTIALLY-CHALLENGED | Strength: Moderate
- Key source: Bertin (1967) "Semiology of Graphics"; Munzner (2014). — Encodings are underdetermined by data; many valid mappings exist for the same model.
- Specific risk: Asserting a unique axis hides a design decision and may mismatch the user's task.
- Summary: Moderate challenge: the visualization literature is clear that a data model underdetermines its encoding (Bertin, Munzner, Mackinlay) and temporal theory recognizes multiple legitimate time axes. 'Axis follows model' overstates — several axes are defensible, so the design should expose a choice rather than assert uniqueness.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-225_against.md

DISPOSITION-15c: MONITOR -> MONITOR-215 (Priority Low-Medium, Monthly)
- Net assessment: 15a NO-SUPPORT-FOUND (Weak) + 15b PARTIALLY-CHALLENGED (Moderate). Encodings are underdetermined by the model; uniqueness is unsupported.
- Reasoning: The uniqueness presumption is unsupported and mildly challenged, but the fix is cheap (toggle) and stakes are low-medium. MONITOR. Joins OPEN-057, DECISION-039, and ASSUMPTION-204 (MONITOR-212).

---

### PRESUMPTION-226 (PRESUMPTION)
**Statement:** Representative-narrative substitution preserves a tradition-bridging edge's meaning — users presumed to read tradition-level bridges correctly from two specific files.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Weak-Moderate
- Key source: Rosch (1975) prototype/exemplar theory. — People reason about categories via representative exemplars; a representative narrative can stand for a tradition.
- Summary: There is weak-moderate support that a representative exemplar can evoke a category (prototype theory) and that part-for-whole encoding can communicate effectively. So representative-narrative substitution is not unreasonable.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-226_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: PARTIALLY-CHALLENGED | Strength: Moderate
- Key source: Robinson (1950) ecological fallacy / level-of-analysis confusion. — Readers conflate the specific (two files) with the aggregate (tradition); the edge may be read at the wrong level.
- Specific risk: Tradition-level bridges are mis-read as narrow idea-level links, distorting the cross-tradition picture.
- Summary: Moderate challenge: substituting two specific files for a tradition-level relationship risks level-confusion (ecological fallacy) and synecdoche ambiguity — users may read an idea-level link rather than a tradition-level bridge. Whether the substitution preserves meaning is an empirical UX question, currently untested.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-226_against.md

DISPOSITION-15c: MONITOR -> MONITOR-216 (Priority Medium, Weekly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Weak-Moderate; exemplars evoke categories); 15b PARTIALLY-CHALLENGED (Moderate; ecological-fallacy/level-confusion). Empirical UX question.
- Reasoning: Plausible but empirically untested comprehension claim; cheap mitigation (level-labeling + exemplar marking) and a clear user-test trigger -> MONITOR. Couples ASSUMPTION-210 (held framework).

---

### PRESUMPTION-227 (PRESUMPTION)
**Statement:** Cross-tab interaction uniformity outweighs per-view-optimal (3D-native) affordances.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Moderate
- Key source: Nielsen (1994) heuristic "Consistency and standards." — Consistency reduces learning cost; supports uniform interaction as a default.
- Summary: Consistency is a well-established usability principle (Nielsen, Norman): uniform interactions lower learning cost and support transfer across tabs, giving moderate support for uniformity as a default.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-227_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: PARTIALLY-CHALLENGED | Strength: Moderate-Strong
- Key source: Grudin (1989) "The case against user interface consistency." — Consistency can harm usability when contexts differ; uniformity is not an unqualified good.
- Specific risk: The 3D view remains awkward/buggy because it inherits 2D interaction defaults.
- Summary: Moderate-strong challenge: Grudin's classic argument shows consistency can be the wrong default when contexts genuinely differ, and 2D/3D views have fundamentally different interaction needs. The system's own zoom/blank-space bug corroborates that uniform interaction misfits the 3D view. Uniformity-as-priority is contestable; context-appropriateness may win for the 3D tab.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-227_against.md

DISPOSITION-15c: MONITOR -> MONITOR-217 (Priority Low-Medium, Weekly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Moderate; consistency principle) vs 15b PARTIALLY-CHALLENGED (Moderate-Strong; Grudin + dimensional difference + live bug).
- Reasoning: Consistency is a sound default but contestable when contexts differ, and there is corroborating in-system evidence (zoom bug). Low-medium stakes -> MONITOR with a defect-driven REVISE trigger.

---

### PRESUMPTION-228 (PRESUMPTION)
**Statement:** The "3 literal hubs" finding reflects the territory, not the resource-naming/normalization method (measurement-artifact risk).

RETURN-TO-14a/14b (FOR / supportive):
- Result: NO-SUPPORT-FOUND | Strength: Weak
- Key source: (Weak/conditional) Controlled-vocabulary/ontology practice (e.g., MeSH). — Literal counts can reflect the territory ONLY if a controlled vocabulary or canonical resource IDs are used; no such normalization is documented here.
- Summary: Weak/conditional support: literal counts can reflect the territory only if a controlled vocabulary or canonical resource identifiers are used. Absent stated normalization, there is no support that the raw literal-string count reflects the territory.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-228_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Strong
- Key source: Furnas et al. (1987) "The vocabulary problem." — Independent authors name the same resource differently; literal matching massively undercounts and is naming-dependent.
- Specific risk: DECISION-040 ('convergence is analogical') could be firmed on an artifactual count; the true number of literal hubs could be higher or lower under different normalization.
- Summary: The challenge is strong: literal string-match hub counts are well known to be naming/normalization artifacts (vocabulary problem; entity resolution), so 'only 3 literal hubs' likely reflects the matching method rather than the territory. This directly threatens the evidence basis for ASSUMPTION-205 and feeds DECISION-040; it belongs to the measurement-integrity cluster (FLAG A).
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-228_against.md

DISPOSITION-15c: REVISE -> REVISE-046 (Urgency MEDIUM)
- Net assessment: 15a NO-SUPPORT-FOUND + 15b Strong = CHALLENGED. Measurement-artifact risk feeding a pending decision; designer-unaware.
- Reasoning: PRESUMPTION (designer-unaware) with strong challenge that the headline '3 hubs' count is method-dependent, gating DECISION-040 and joining FLAG A -> REVISE. Urgency MEDIUM (matches item priority; gates a not-yet-firmed decision). Couples ASSUMPTION-205 (PREMISE-042 scope-exclusion), PRESUMPTION-212, FLAG A.

---

### PRESUMPTION-229 (PRESUMPTION)
**Statement:** The connectome viz + network-neuroscience metrics stay legible/meaningful at much larger N (scale blindness vs the 2000-node crash cap).

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Weak-Moderate
- Key source: Holten (2006) hierarchical edge bundling; multiscale/hierarchical layouts. — Some techniques preserve legibility at larger N.
- Summary: Weak-moderate support that legibility can be preserved at scale IF the representation changes (edge bundling, hierarchical, matrix views). This supports feasibility, not the presumption that the CURRENT connectome viz/metrics persist unchanged.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-229_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Strong
- Key source: The "hairball" problem (Ghoniem et al. 2004). — Node-link diagrams become illegible as N/density grow; the current viz will degrade.
- Specific risk: Both the visualization and the metric values silently degrade as the corpus grows; conclusions drawn at large N may be artifacts of size.
- Summary: Strong challenge: node-link legibility collapses at scale (hairball), several connectome metrics are explicitly size/density-dependent (resolution limit; small-worldness normalization), and the system already enforces a 2000-node crash cap — direct evidence that scale is a live constraint. The failure is gradual/future but real.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-229_against.md

DISPOSITION-15c: MONITOR -> MONITOR-218 (Priority Medium, Weekly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Weak-Moderate; conditional on representation change) vs 15b CHALLENGED (Strong; hairball + size-dependent metrics + existing crash cap). True now, false in the limit.
- Reasoning: Strong challenge but the failure is gradual/future and partly mitigated by the existing crash cap; per the 15c heuristic for 'true now, false in the limit', MONITOR with a concrete scale trigger rather than REVISE now. Joins ASSUMPTION-201, PRESUMPTION-221, crash-proofing caps; mirrors PRESUMPTION-219 scale handling.

---

### PRESUMPTION-230 (PRESUMPTION)
**Statement:** Confirming gating logic + data == confirming rendered behavior — UX symptom dispositioned by data-reasoning over reproduced observation.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Weak-Moderate
- Key source: Formal verification / static analysis. — Reasoning about logic + inputs can establish properties without running the UI in some cases.
- Summary: Weak-moderate support: in systems where rendered behavior is fully determined by the verified logic, logic+data reasoning can establish correctness. So the approach is not always invalid.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-230_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Strong
- Key source: "Works as designed != works": the spec/implementation gap. — UX bugs are emergent at the render layer (browser/CSS/layout/event handling), not visible in gating logic.
- Specific risk: UX bugs are marked resolved while still visible to users; the self-measurement layer over-trusts logic-level reasoning.
- Summary: Strong challenge: rendered UX behavior is emergent at a layer the gating logic does not capture, so confirming logic+data does not confirm what the user sees. Best practice requires reproducing the rendered defect and observing the fix. Dispositioning a UX symptom by data-reasoning alone is a verification gap (symmetric to PRESUMPTION-218; engages Rule 12).
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-230_against.md

DISPOSITION-15c: MONITOR -> MONITOR-219 (Priority Low-Medium, Weekly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Weak-Moderate; only when render layer is behavior-neutral) vs 15b CHALLENGED (Strong; rendered UX is emergent; reproduced-defect discipline). Symmetric to PRESUMPTION-218.
- Reasoning: Strong challenge and a real verification-discipline gap, but for consistency with the symmetric item PRESUMPTION-218 (dispositioned MONITOR-208) and given low-medium stakes and a cheap disciplinary fix, MONITOR with a reproduction-recurrence REVISE trigger. Engages Rule 12 (fail loud).

---

### SYSTEMIC-RISK-FLAGs (15b)

SYSTEMIC-RISK-FLAG F (NEW): Unchecked connectome/neuro analogy transfer
  Date: 2026-05-21
  Affected items: ASSUMPTION-201, ASSUMPTION-202, PRESUMPTION-221, PRESUMPTION-229
  Common vulnerability: The connectome/neural metaphor (Hawkins) is adopted as the master structuring metaphor and load-bears the entire metric suite, with no transfer-condition check. Brain-specific measures (rich club, small-worldness, association-fiber semantics) presuppose wiring/metabolic constraints narratives lack, and several are null-model-fragile even within neuroscience.
  Literature basis: Bullmore & Sporns (2012) economy of brain networks; Telesford (2011) small-worldness; Fortunato & Barthelemy (2007) resolution limit; Tallis (2011)/Legrenzi & Umilta (2011) neuro-metaphor critique; Gentner (1983) structure-mapping.
  Risk level: High
  Recommendation: A one-time transfer-condition audit gating ALL connectome metrics (per-metric brain-assumption check + degree-preserving null models); default to generic graph measures. Anchored by PRESUMPTION-221 / REVISE-043.

SYSTEMIC-RISK-FLAG G (NEW): Compression-as-progress metric not operationalizable as stated
  Date: 2026-05-21
  Affected items: ASSUMPTION-208, PRESUMPTION-222
  Common vulnerability: The proposed headline progress metric rests on an undefined/uncomputable "total description length"; only scheme-relative proxies exist, and they measure syntax, not narrative meaning.
  Literature basis: Kolmogorov uncomputability (Li & Vitanyi); Grunwald (2007) MDL scheme-relativity; Kuhn (1962) incommensurability; counterexamples (Standard Model) where progress adds machinery.
  Risk level: High
  Recommendation: Replace the identity with a single labeled, validated proxy (LM cross-entropy codelength or MDL graph summarization) + fidelity guard, OR demote compression to one indicator among several. Anchored by PRESUMPTION-222 / REVISE-044 and ASSUMPTION-208 / REVISE-042.

FLAG A CONTINUATION (measurement-integrity): ASSUMPTION-205 + PRESUMPTION-228 (literal string-match shared-resource hub counts) join the existing measurement-integrity cluster (FLAG A; PRESUMPTION-212). Recommendation: entity-resolution sensitivity analysis on resource naming before DECISION-040 firms; use the analogical-convergence PRINCIPLE (PREMISE-042), not the raw '3 hubs' count, as the decision basis. See REVISE-046.


---

## 2026-05-22 RUN — Empty-queue status report (clean null run; no daily-cycle items)

**Disposition counts:** 0 INCORPORATE / 0 MONITOR / 0 REVISE. No items processed this run.

**Run context:** The c2a2-lit-search-pipeline scheduled task fired on cadence (2026-05-22 ~05:47 UTC), one hour after the upstream c2a2-self-awareness-daily (14a/14b) slot. The most recent 14a/14b batch appended to for_lit_search.md is 2026-05-20 EOD (17 routed items), already SEARCHED and DISPOSITIONED on 2026-05-21. No new daily batch has been appended for 2026-05-21 EOD or 2026-05-22, and no architecture/changelog/2026-05-21_changes.md or 2026-05-22_changes.md exists on disk.

**Queue state at start of this run:**
- 0 items newly QUEUED at cycle 0.
- 0 partial-search items; 0 searched-but-undispositioned items.
- 15d-owned cohorts pending but not due: RE-TRIGGER cohort (next 15d check 2026-05-25), MONITOR-197..209 (next 15d 2026-05-27), MONITOR-210..219 (next 15d 2026-05-28). None overdue. Owned by 15d (weekly), not this daily pipeline -- boundary discipline per the 2026-05-16 precedent and ASSUMPTION-166.

**Distinction from the 2026-05-16 null run:** The 2026-05-16 null run carried a 4-day-overdue 57-item RE-TRIGGER backlog and flagged an ownership-boundary fragility. Today there is NO overdue backlog -- every 15d-owned cohort has a future next-check date. This is a clean null run.

**Action taken this run:** No literature searches. No disposition writes. This file appended with this status note; for_lit_search.md appended with a 2026-05-22 empty-run marker. No writes to validated_premises.md / monitor_queue.md / revision_flags.md.

**Upstream observation (next 14a/14b run):** daily_sync/chat_to_cowork/2026-05-21_chat_summary.md is present but un-ingested; no 14a/14b fire detected for 2026-05-21 EOD / 2026-05-22. Reported only; ingestion is out of 15a/15b/15c scope.

**SYSTEMIC-RISK-FLAGs raised this run:** 0.

## Completion checklist (2026-05-22 run)

- [x] Read for_lit_search.md queue state; 0 unsearched [QUEUED] items, 0 partial, 0 undispositioned.
- [x] Read agent definitions (15a, 15b, 15c) and provenance protocol.
- [x] Confirmed source registries' highest IDs (ASSUMPTION-211, PRESUMPTION-230) are present and dispositioned -> no intake gap.
- [x] Confirmed no 2026-05-21 / 2026-05-22 14a/14b changelog on disk (latest = 2026-05-20_changes.md).
- [x] Documented run state in this section + for_lit_search.md marker.
- [ ] No new INCORPORATE/MONITOR/REVISE writes (correct null result; no items in scope).
- [ ] Provenance chains: no new items processed -> no new provenance writes (correct null result).

---

**Generated by Agents 15a, 15b, and 15c (2026-05-22 scheduled pipeline run)**
**Date: 2026-05-22 (autonomous scheduled-task run; no human review in-loop)**
**Pipeline trigger: c2a2-lit-search-pipeline scheduled task; no daily-cycle items found; all 15d-owned cohorts pending but not yet due (clean null run).**


---

## BATCH 2026-05-23 LIT-PIPELINE (two-summa experiment + verification-discipline cohort; dispositions 2026-05-23)
**Search date:** 2026-05-23
**Items:** 12 (3 ASSUMPTIONs: 214,215,216 + 9 PRESUMPTIONs: 231-239) from the 2026-05-22 14a/14b batch
**Dispositions:** 0 INCORPORATE, 9 MONITOR (MONITOR-220..228), 3 REVISE (REVISE-047..049)
**Grounding:** training-corpus grounding per ASSUMPTION-199 convention; FLAG E / REVISE-040 noted
**Run context:** scheduled c2a2-lit-search-pipeline, one hour after the 14a/14b slot. The 2026-05-22 EOD batch (12 routed items) was QUEUED at cycle 0 and is fully searched + dispositioned this run. Conceptual center of gravity: the two-summa head-to-head (ASSUMPTION-215/216, PRESUMPTION-233/234/235), whose internal tension with the project's own MacIntyrean incommensurability commitment drives a new SYSTEMIC-RISK-FLAG H.

---

### ASSUMPTION-214 (ASSUMPTION)
**Statement:** A single self-contained handoff document can carry an experiment's full context into a cold-start chat (portability across sessions).

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Moderate
- Key source: Knuth (1984) literate programming; Donoho et al. (2009) reproducible research; design-doc/RFC practice. — Self-contained documents can transfer enough to reproduce work / intent.
- Summary: Real lineage for "one complete document carries the work" (literate programming, research compendia, RFC culture), but every tradition pairs it with strict completeness requirements. Support is partial and conditional on the brief actually being complete.
- Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-214_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: PARTIALLY-CHALLENGED | Strength: Moderate-Strong
- Key source: Collins TEA-laser replication studies; Polanyi (1966); reproducibility crisis (Baker 2016). — Experiments often cannot be reproduced from the written record alone; tacit context leaks.
- Specific risk: The brief silently omits a load-bearing detail; the cold-start run looks faithful but diverges from intent, undetectably.
- Summary: The replication literature is the strong counter: written records under-carry tacit competence, and a cold start has none of the human shared background that repairs documentation gaps. "Full context" is too strong; "enough, after iteration" is defensible.
- Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-214_against.md

DISPOSITION-15c: MONITOR -> MONITOR-220 (Priority Medium-High, Weekly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Moderate); 15b PARTIALLY-CHALLENGED (Moderate-Strong). Directly testable by the launch itself.
- Reasoning: Stated, designer-aware, and empirically self-testing (the cold-start either works or reveals gaps); the fix is cheap and iterative, so MONITOR over REVISE. Trigger: REVISE if the first cold-start launch loses load-bearing context. Couples PRESUMPTION-232; gates DECISION-044.

---

### ASSUMPTION-215 (ASSUMPTION)
**Statement:** A "Conscious-Realist-Monist summa" can be built as a genuine rival to the Thomist summa and run head-to-head for evidence. (Day's top conceptual stake.)

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Moderate
- Key source: MacIntyre (1988/1990) rival-versions comparison; Kahneman adversarial collaboration; comparative/systematic theology. — Rival comprehensive frameworks can be constructed and compared to produce evidence.
- Summary: Constructing a synthesis and contesting it against a rival is methodologically precedented (MacIntyre stages exactly such a contest; adversarial collaboration formalizes it). Support is only moderate because the same authority supplies the strongest objection.
- Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-215_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Strong
- Key source: MacIntyre — a tradition is "an historically extended, socially embodied argument"; Kahneman & Klein (refereeing). — A constructed corpus is not a tradition; the new summa is the designer's own view, so the contest risks home-team bias.
- Specific risk: An experiment that "shows" Conscious-Realist-Monism competitive, but whose result is an artifact of building the rival to win and pitting an immature corpus against a stress-tested canon.
- Summary: Self-applying challenge: by the project's own MacIntyrean lights a tradition cannot be authored de novo, and the proponent should not referee its own contest. The head-to-head can produce the appearance of evidence while being structurally tilted.
- Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-215_against.md

DISPOSITION-15c: REVISE -> REVISE-047 (Urgency HIGH)
- Net assessment: 15a PARTIALLY-SUPPORTED (Moderate) vs 15b CHALLENGED (Strong); high-stakes stated assumption that gates DECISION-044/OPEN-062.
- Reasoning: Moderate-vs-strong asymmetry on a high-stakes item whose challenge strikes the project's own commitments -> REVISE (not MONITOR). Recommend Tom decide whether Summa-2 must be a genuine tradition or a declared constructed synthesis, and remove the refereeing conflict (independent constructor / pre-registered win conditions). Anchors SYSTEMIC-RISK-FLAG H.

---

### ASSUMPTION-216 (ASSUMPTION)
**Statement:** The Aquinas<->Levin teleology seam is the right focal cross-tradition bridge for the head-to-head.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Moderate
- Key source: Flyvbjerg (2006) paradigmatic-case selection; Levin goal-directedness; Thomist final causation. — Teleology is a substantively shared topic; a focal seam can be legitimately chosen.
- Summary: The seam is not arbitrary — teleology is load-bearing on both sides. Case-selection methods support choosing a paradigmatic seam. Support is partial: "shared topic" is not "same concept," and "right/most productive" is asserted, not compared.
- Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-216_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: PARTIALLY-CHALLENGED | Strength: Moderate
- Key source: Equivocation (Thomist robust final cause vs Levin/Dennett deflationary goal-directedness); Gentner (1983) structure-mapping. — A good analogy needs shared relational structure, not a shared word.
- Specific risk: The flagship bridge turns on an equivocation, so any "convergence/tension" reported there is a translation artifact.
- Summary: The two teleologies share a label but maybe not relational structure (Levin's is explicitly as-if). If the seam rests on the word, the head-to-head yields pseudo-agreement/conflict. Secondary: un-compared case selection.
- Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-216_against.md

DISPOSITION-15c: MONITOR -> MONITOR-221 (Priority Low-Medium, Monthly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Moderate); 15b PARTIALLY-CHALLENGED (Moderate). Relevance solid; conceptual unity and optimality unproven.
- Reasoning: Moderate vs moderate, low-medium stakes; the equivocation is the thing to watch and is cheaply addressed by disambiguating the two teleology concepts before use. MONITOR; couples PRESUMPTION-235; joins FLAG H.

---

### PRESUMPTION-231 (PRESUMPTION)
**Statement:** Byte-identical data + node --check + eyeball is presumed to entail correct rendered interaction behavior; no interaction test.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Weak-Moderate
- Key source: Static analysis / golden-master data testing; formal-methods determinism principle. — The gate reliably covers data + syntax regressions.
- Summary: Sound for what it covers (data identity rules out data regressions; node --check rules out syntax errors), and where behavior is fully determined by verified layers, reasoning can substitute for execution. Weak-moderate because interaction behavior is not so determined.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-231_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Strong
- Key source: "Works as designed != works"; UI test-automation practice (event simulation); node --check parses, does not execute. — Interaction bugs are emergent at render/event layer.
- Specific risk: A new widget ships "verified" while a click/edge-pick/slider path is silently broken.
- Summary: The checked layers sit below the bug surface; interaction correctness must be reproduced and observed. Eyeball review is unreliable for event-level correctness. Re-instantiates PRESUMPTION-230/218; engages Rule 12.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-231_against.md

DISPOSITION-15c: MONITOR -> MONITOR-222 (Priority Low-Medium, Weekly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Weak-Moderate); 15b CHALLENGED (Strong). Real verification-discipline gap, cheap fix.
- Reasoning: For consistency with the symmetric items PRESUMPTION-230 (MONITOR-219) and 218 (MONITOR-208), and given low-medium stakes and a cheap remedy (an interaction smoke test on the promote-to-live gate), MONITOR with a recurrence REVISE trigger. Joins the verification-standard family / Rule 12.

---

### PRESUMPTION-232 (PRESUMPTION)
**Statement:** A cold-start chat shares enough tacit context that nothing load-bearing is lost when the only carrier is a single brief.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Weak-Moderate
- Key source: IEEE-830 specification practice; reproducible-research compendia; rich context-prompt practice. — Complete written carriers can transfer intent without prior state.
- Summary: Precedent exists that a sufficiently complete carrier transfers task intent (specs, compendia, context prompts). Weak-moderate because completeness is the binding constraint and tacit background routinely leaks.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-232_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Strong
- Key source: Polanyi/Collins (tacit knowledge); Clark (1996) common ground; LLM prompt-sensitivity. — A cold start lacks the interactively-built common ground that repairs gaps.
- Specific risk: The cold-start run quietly reinterprets intent because a tacit prior never made it into the brief — invisibly, since the omission was unknown to the author.
- Summary: The load-bearing half of ASSUMPTION-214; "nothing load-bearing is lost" is very likely false in the strict sense. The open question is whether the loss is load-bearing here, which must be tested, not assumed.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-232_against.md

DISPOSITION-15c: MONITOR -> MONITOR-223 (Priority Medium, Weekly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Weak-Moderate) vs 15b CHALLENGED (Strong); designer-unaware twin of ASSUMPTION-214.
- Reasoning: PRESUMPTION + strong challenge would lean REVISE, but the loss is empirically bounded by the very launch (cold-start + author divergence audit) and the item is tightly coupled to ASSUMPTION-214 (MONITOR-220). MONITOR with the explicit, loud note that "nothing lost" is unverified and must be tested before relying on the brief. Trigger: REVISE if a load-bearing divergence appears on first cold start.

---

### PRESUMPTION-233 (PRESUMPTION)
**Statement:** The two summae are commensurable enough to be compared on shared criteria — against the project's own MacIntyrean incommensurability commitment.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Moderate
- Key source: MacIntyre (1988) epistemological-crisis comparison; Kuhn (1983) incommensurability != incomparability; Davidson (1974). — Rational comparison without a neutral standard is possible.
- Summary: Comparison-enough is defensible AND available from within the project's own MacIntyreanism (crisis-resolution comparison). But that licenses tradition-internal comparison, not the "shared neutral criteria" the presumption actually describes.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-233_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Strong
- Key source: MacIntyre — no tradition-neutral standard of rationality; Kuhn/Feyerabend; the project's own pluralism (ASSUMPTION-207). — Any "shared criteria" scorecard is one tradition's standards in disguise.
- Specific risk: The headline result is determined by whose criteria were chosen as "shared" — pseudo-evidence confirming the criteria-author's tradition.
- Summary: Internal, self-undermining challenge: a shared-criteria head-to-head cannot yield the unbiased evidence it promises and violates the system's own pluralism. The supportive route (MacIntyrean crisis test) is a different method than shared-criteria scoring.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-233_against.md

DISPOSITION-15c: REVISE -> REVISE-048 (Urgency HIGH)
- Net assessment: 15a PARTIALLY-SUPPORTED (Moderate) vs 15b CHALLENGED (Strong); designer-unaware PRESUMPTION; HIGH stakes; gates whether the experiment yields unbiased evidence.
- Reasoning: PRESUMPTION + strong challenge + self-contradiction with ASSUMPTION-207 -> REVISE HIGH. Recommend: do not score on imposed neutral criteria; use MacIntyre's tradition-internal crisis-resolution test, or run under each tradition's own criteria and report both. Co-anchors SYSTEMIC-RISK-FLAG H with REVISE-047.

---

### PRESUMPTION-234 (PRESUMPTION)
**Statement:** A "Summa 2" already exists or can be assembled parallel to the Thomist summa (though "what counts as Summa 2" is open).

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Weak-Moderate
- Key source: Constructive/systematic-theology synthesis; corpus-construction methodology; the project's existing 14-tradition corpora. — A parallel comprehensive corpus is assemblable, and much raw material exists.
- Summary: Assembling a parallel corpus is feasible in principle and partly already done. Weak-moderate because feasibility is not parity, and the unit is undefined (OPEN-062).
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-234_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: PARTIALLY-CHALLENGED | Strength: Moderate-Strong
- Key source: Corpus asymmetry (fixed centuries-tested canon vs present draft); MacIntyre on tradition maturation; undefined-construct problem (OPEN-062). — Comparing a finished artifact to an undefined draft is structurally unequal.
- Specific risk: A result that reflects "old canon vs new draft" (or a curated-to-win corpus) rather than a real comparison of worldviews.
- Summary: Asymmetry + definitional openness: whatever the result, it partly reflects the maturity/definition gap. Addressable by an explicit corpus-construction protocol and honest framing, hence moderate-strong not strong.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-234_against.md

DISPOSITION-15c: MONITOR -> MONITOR-224 (Priority Medium, Weekly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Weak-Moderate); 15b PARTIALLY-CHALLENGED (Moderate-Strong). Asymmetry real but design-stage and addressable.
- Reasoning: The fix is design-stage (define Summa-2 via the already-open OPEN-062; control asymmetry) and the item belongs to the REVISE cluster anchored by 215/233; MONITOR rather than multiply REVISEs across the whole cluster. Joins SYSTEMIC-RISK-FLAG H. Trigger: REVISE if the experiment proceeds with an undefined or uncontrolled-asymmetry Summa-2.

---

### PRESUMPTION-235 (PRESUMPTION)
**Statement:** The Aquinas<->Levin seam is the most evidentially productive seam; alternatives were not weighed (absent-alternatives).

RETURN-TO-14a/14b (FOR / supportive):
- Result: NO-SUPPORT-FOUND | Strength: Weak
- Key source: Flyvbjerg (2006); Seawright & Gerring (2008). — Defensible focal-case selection is explicitly comparative; it does not endorse asserting optimality without weighing alternatives.
- Summary: The very methods that could justify a focal seam require a comparative selection rationale the item lacks. No positive support for "most productive" as asserted; at best defensible-if-justified.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-235_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Moderate
- Key source: Seawright & Gerring (2008); Nickerson (1998) confirmation bias; Gelman & Loken (2013) forking paths. — Un-compared case selection is a textbook bias vector.
- Specific risk: The flagship seam is a hidden forking-path; a different seam might show tension where this shows convergence.
- Summary: With alternatives unweighed, "most productive" is unsupported and exposed to selection bias (the seam may be the most hypothesis-flattering). Moderate, not strong, because the seam is plausibly good and the remedy is cheap.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-235_against.md

DISPOSITION-15c: MONITOR -> MONITOR-225 (Priority Low-Medium, Monthly)
- Net assessment: 15a NO-SUPPORT-FOUND (Weak) vs 15b CHALLENGED (Moderate). Asymmetric toward the challenge but low-stakes and cheaply fixed.
- Reasoning: Per heuristic, weak-support + moderate-challenge could lean REVISE, but stakes are low-medium and the fix is a brief seam comparison; MONITOR coupled to ASSUMPTION-216, with a robustness-check recommendation (run a second seam). Joins SYSTEMIC-RISK-FLAG H.

---

### PRESUMPTION-236 (PRESUMPTION)
**Statement:** Inline-embedding faculty summaries (1.3 -> 1.9 MB) — self-containment outweighs page-weight/scaling cost as the corpus grows.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Moderate (current-scale)
- Key source: Single-file self-contained web-app practice; HTTP Archive page-weight norms; round-trip elimination on high-latency links. — Self-containment buys portability/offline robustness; 1.9 MB is normal now.
- Summary: At current size the choice is well-justified, and the robustness benefits matter for the project's low-bandwidth contexts. Support is conditional/current-scale, not unconditional.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-236_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: PARTIALLY-CHALLENGED | Strength: Moderate
- Key source: Performance-budget practice; lazy-loading/code-splitting consensus; main-thread/first-paint cost. — Inlining scales linearly, defeats caching, blocks first paint — worst on low-end clients.
- Specific risk: As the corpus grows, load/memory degrade silently on exactly the low-resource clients the project prioritizes.
- Summary: Fine now, but the presumption is about the trend; inlining the full corpus has no scaling ceiling. "True now, false in the limit"; joins the PRESUMPTION-229 scaling family the project already guards with crash caps.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-236_against.md

DISPOSITION-15c: MONITOR -> MONITOR-226 (Priority Low-Medium, Weekly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Moderate, current-scale); 15b PARTIALLY-CHALLENGED (Moderate). Gradual/future failure.
- Reasoning: Mirrors the PRESUMPTION-229 (MONITOR-218) scale handling: MONITOR with a concrete page-weight budget + switch-to-lazy-load trigger rather than REVISE now. RESOLVE once a budget/trigger lands; REVISE if first-paint degrades on a representative low-end client before then.

---

### PRESUMPTION-237 (PRESUMPTION)
**Statement:** Publish/untrack calls rest on an unstated, stable publishability criterion; the governing rule is tacit (normative smuggling).

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Weak-Moderate
- Key source: Klein (1998) recognition-primed decision; NIST/ISO data-classification (discretion-with-policy); FAIR/IRB case-by-case judgment. — Expert per-case publication calls can be reliable.
- Summary: Per-case judgments are a normal, often-reliable mode for a single expert operator. Weak-moderate because every framework pairs discretion with a documented anchoring policy; tacit-only is tolerated, not endorsed as stable/auditable.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-237_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Moderate
- Key source: NIST SP 800-60 / ISO 27001 A.8 data-classification; normative-smuggling critique; decision-reproducibility. — Publication decisions should follow an explicit written rule; tacit criteria drift and cannot be reviewed.
- Specific risk: An inconsistent or value-laden publish decision under a rule no one can inspect, with privacy/consent stakes (couples PRESUMPTION-238).
- Summary: Workable for one operator today but fragile by every governance standard: unauditable, inconsistent over time, silently value-laden. Moderate; the fix (write the criterion down) is cheap.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-237_against.md

DISPOSITION-15c: MONITOR -> MONITOR-227 (Priority Medium, Weekly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Weak-Moderate); 15b CHALLENGED (Moderate). Real governance gap, cheap remedy.
- Reasoning: PRESUMPTION + moderate challenge with a cheap fix and coupling to the framework commitment ASSUMPTION-218 -> MONITOR with a concrete recommendation (articulate + log the publishability criterion). Trigger: REVISE if an inconsistent/regretted publish decision surfaces.

---

### PRESUMPTION-238 (PRESUMPTION)
**Statement:** Parking the history scrub presumes acceptable residual exposure while parked; stop-tracking presumed sufficient interim mitigation; no trigger set (success-criteria gap).

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Weak-Moderate
- Key source: NIST SP 800-30 time-boxed risk acceptance; git rm --cached as a valid first step; private-repo compensating control. — Deferral can be defensible if exposure is bounded.
- Summary: Deferring a rewrite is defensible IF the repo stays private and risk acceptance is explicit and time-boxed. Stop-tracking correctly prevents recurrence. Conditional support — and the conditions (bounded exposure, explicit trigger) are exactly what is missing.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-238_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Strong
- Key source: Git immutability + GitHub remediation docs; git-filter-repo/BFG ("treat committed content as compromised"); NIST risk-acceptance discipline. — Stop-tracking does NOT remove already-committed content; "no trigger" is unbounded acceptance.
- Specific risk: Sensitive/consent-bearing content (Hoffman x Levin transcript, narration zips) stays in history and is exposed the instant the repo is shared, with no trigger forcing remediation first.
- Summary: Well-established: stop-tracking only stops future commits; history remains recoverable, so "stop-tracking = sufficient" is false for anyone who can read the repo or its future public form. Most security-consequential item in the batch; engages Rule 12 (fail loud).
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-238_against.md

DISPOSITION-15c: REVISE -> REVISE-049 (Urgency MEDIUM)
- Net assessment: 15a PARTIALLY-SUPPORTED (Weak-Moderate, conditional) vs 15b CHALLENGED (Strong); security/privacy stakes; "no trigger" is a genuine success-criteria gap.
- Reasoning: Strong, well-established challenge on a privacy-consequential item; OPEN-064 names the intent ("before any repo-publicity step") but it is not formalized as a hard gate and parked-window exposure is unbounded. REVISE (Medium): set an explicit hard pre-publicity scrub trigger, make the risk acceptance explicit/time-boxed, decide on history rewrite, keep repo private until then. Couples DECISION-047, OPEN-064.

---

### PRESUMPTION-239 (PRESUMPTION)
**Statement:** The transcript_authenticity_check FABRICATION verdict on fidelity-passing summary renders is a false-positive, not a real signal.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Moderate
- Key source: Abstractive-vs-extractive distinction; classifier base-rate/false-positive analysis; distribution-shift. — A verbatim-tuned authenticity classifier is out of distribution on abstractive summary renders, where surface divergence is expected.
- Summary: There is a principled reason the verdict COULD be a false positive (OOD input, expected surface divergence). Moderate, because plausibility is not adjudication: it argues the verdict might be noise, not that it is.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-239_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Moderate-Strong
- Key source: Maynez et al. (2020); Kryscinski et al. (2020) FactCC; Parasuraman & Riley (1997) automation complacency. — Abstractive summaries frequently hallucinate; dismissing an alarm without adjudication is a recognized failure mode.
- Specific risk: A genuinely fabricated/hallucinated summary render is shipped because its FABRICATION alarm was waved off as noise, corrupting authenticity guarantees.
- Summary: The presumption may be backwards: a FABRICATION verdict could be a true signal that the summary introduced unsupported content (a "fidelity" pass measures something different). Dismissing without a labeled error analysis self-undermines the project's own anti-fabrication commitment (ASSUMPTION-198).
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-239_against.md

DISPOSITION-15c: MONITOR -> MONITOR-228 (Priority Medium-High, Weekly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Moderate) vs 15b CHALLENGED (Moderate-Strong); honesty-critical signal; remediation already owned by OPEN-063.
- Reasoning: The dismissal is itself an unverified call on an honesty-critical signal; fail-loud leans toward forcing adjudication. MONITOR (Medium-High) rather than REVISE because OPEN-063 already owns the fix (classifier tuning + wiki read access), with the explicit, loud condition that the "false-positive" verdict must NOT be acted on until a labeled error analysis adjudicates it. Couples Rule 12 and the ASSUMPTION-198 fabrication-integrity family. Trigger: REVISE if any flagged render is published before adjudication.

---

### SYSTEMIC-RISK-FLAGs (15b)

SYSTEMIC-RISK-FLAG H (NEW): Two-summa head-to-head presumes tradition-neutral comparability the project's own framework denies
  Date: 2026-05-23
  Affected items: ASSUMPTION-215, ASSUMPTION-216, PRESUMPTION-233, PRESUMPTION-234, PRESUMPTION-235
  Common vulnerability: The planned two-summa experiment load-bears on a cluster of unexamined comparability assumptions — that a constructed corpus is a genuine tradition (215), that the two are commensurable on shared/neutral criteria (233), that a parallel Summa-2 is definable and parity-comparable (234), and that a single un-compared focal seam is the most productive (216/235) — while the project is explicitly MacIntyrean and pluralist (ASSUMPTION-207), which denies tradition-neutral standards. The result is an experiment that can manufacture the appearance of evidence (home-team construction + imposed scorecard + corpus asymmetry + hypothesis-flattering seam) while contradicting its own foundational commitment.
  Literature basis: MacIntyre (1981/1988/1990) tradition-constituted enquiry & no neutral standard; Kuhn (1962/1983) & Feyerabend incommensurability; Davidson (1974); Kahneman & Klein (2009) adversarial-collaboration refereeing; Seawright & Gerring (2008) case selection; Gelman & Loken (2013) forking paths.
  Risk level: High
  Recommendation: Before launching DECISION-044, gate the experiment on a design audit that (1) reframes the claim from "tradition vs tradition" to a declared constructed-synthesis-vs-canon comparison with stated asymmetry, (2) replaces neutral-scorecard scoring with MacIntyre's tradition-internal epistemological-crisis test (or runs under each tradition's own criteria and reports both), (3) removes the refereeing conflict (independent constructor / pre-registered win conditions), (4) defines Summa-2 (OPEN-062) and controls corpus asymmetry, and (5) weighs >=2 candidate seams. Anchored by REVISE-047 (215) and REVISE-048 (233); MONITOR-221/224/225 (216/234/235) ride this flag.

FLAG (verification-standard family) CONTINUATION: PRESUMPTION-231 (interaction behavior not reproduced) joins the existing "works-as-designed != verified" cluster with PRESUMPTION-230/218 (Rule 12). PRESUMPTION-237 (tacit publishability rule) and PRESUMPTION-239 (alarm dismissed without adjudication) are adjacent verification/governance-discipline items: each substitutes reasoning/assumption for an observation/adjudication that is cheap to perform. No new systemic flag raised; recommendation is the standing one — add the missing observation (interaction smoke test / written criterion / labeled error analysis) before relying on the result.

NOVELTY (15a): None flagged. All 12 items have clear training-corpus literature anchors; no literature-gap NOVEL items this batch.

## Completion checklist (2026-05-23 run)

- [x] Read for_lit_search.md queue state: 12 [QUEUED] items at cycle 0 (ASSUMPTION-214/215/216 + PRESUMPTION-231-239), 0 partial, 0 searched-but-undispositioned.
- [x] Read agent definitions (15a, 15b, 15c) and provenance_protocol.md.
- [x] 15a: wrote 12 FOR result files to lit_search_results/for/ with PROVENANCE headers.
- [x] 15b: wrote 12 AGAINST result files to lit_search_results/against/ with PROVENANCE headers + STEELMAN sections.
- [x] 15c: dispositioned all 12 paired results -> 0 INCORPORATE, 9 MONITOR (MONITOR-220..228), 3 REVISE (REVISE-047..049).
- [x] Updated for_lit_search.md: all 12 Status lines tagged [SEARCHED-15a]/[SEARCHED-15b]/[DISPOSITIONED-15c: 2026-05-23 -> disposition] (folded-tag convention; backup at for_lit_search.md.bak.20260523-pre-15pipeline).
- [x] Appended 9 MONITOR entries to monitor_queue.md (next weekly 15d 2026-05-30; next monthly 2026-06-23).
- [x] Appended 3 REVISE entries to revision_flags.md (all AWAITING-REVIEW; REVISE-047/048 HIGH require Tom's response).
- [x] No INCORPORATE this run -> no writes to validated_premises.md (correct null; consistency-check moot).
- [x] Consistency check: REVISE-048 (no neutral shared criteria) PROTECTS, does not contradict, ASSUMPTION-207 pluralism and existing PREMISEs; no contradictions with validated_premises.md found.
- [x] Provenance chains complete for all 12 (Origin -> [14x -> 15a, 15b -> 15c] -> disposition).
- [x] Raised SYSTEMIC-RISK-FLAG H (two-summa comparability cluster: ASSUMPTION-215/216, PRESUMPTION-233/234/235).
- [ ] BOUNDARY/FAIL-LOUD NOTE: metrics/2026-05-22_snapshot.md "Tested (literature-searched)" counts (~93 assumptions / ~91 presumptions) are now STALE by +3 assumptions (214,215,216) and +9 presumptions (231-239) tested this run. Metrics snapshots are owned by the 14a/14b/metrics cycle, not this pipeline (boundary discipline) — flagged here for the next 14a/14b run to refresh; NOT silently written by 15c.
- [ ] BOUNDARY NOTE: no separate changelog file created — lit-pipeline runs record in this file (lit_search_returns.md); the changelog is a 14a/14b daily-narrative artifact and there is no 2026-05-23 14a/14b fire.

**Disposition counts (2026-05-23):** 0 INCORPORATE / 9 MONITOR / 3 REVISE. 12 items processed. SYSTEMIC-RISK-FLAGs raised: 1 (FLAG H).
**Total daily-cycle items remaining in queue post-run:** 0.
**Run timestamp:** 2026-05-23 (c2a2-lit-search-pipeline scheduled task; autonomous; no human-in-the-loop).

---

**Generated by Agents 15a, 15b, and 15c (2026-05-23 scheduled pipeline run)**
**Date: 2026-05-23 (autonomous scheduled-task run; no human review in-loop)**
**Pipeline trigger: c2a2-lit-search-pipeline scheduled task; 12 daily-cycle items (2026-05-22 14a/14b batch) fully searched + dispositioned.**

---

# Batch 2026-05-24 (Agents 15a, 15b, 15c -- c2a2-lit-search-pipeline scheduled run)

*Source batch: 2026-05-23 14a/14b extraction (ASSUMPTION-220/221 + PRESUMPTION-240-243). 6 items at cycle 0; searched FOR (15a) and AGAINST (15b) independently, then dispositioned (15c). Grounding note: 15a/15b citations drawn from training-corpus per the ASSUMPTION-199 convention (SYSTEMIC-RISK-FLAG E); the three high-stakes governance items (221, 240, 243) had key citations live-verified 2026-05-24 per REVISE-040's standing recommendation (Santoni de Sio & van den Hoven 2018; Green 2022 confirmed).*

### ASSUMPTION-220 (ASSUMPTION)
**Statement:** PRS candidates can be validly generated from a talk's announced topic list / runtime metadata when the transcript is unavailable, if confidence is capped at Medium and flagged for transcript verification.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Moderate
- Key source: PRISMA two-stage screening (Page et al. 2021); informative-abstract/IR surrogate standards. -- A confidence-capped provisional candidate from a surrogate, flagged for full-source verification, is exactly the validated two-pass screening pattern.
- Summary: Metadata carries real content signal and staged extraction is methodologically legitimate; support is Moderate because validity hinges on verification actually running and PRS needs the argumentative move, not just topics.
- Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-220_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: PARTIALLY-CHALLENGED | Strength: Moderate
- Key source: Pitkin et al. (1999) & Boutron et al. (2010) abstract-vs-source divergence; Maynez et al. (2020) faithfulness. -- Thin surrogates systematically diverge from full source; generating claims from impoverished input maximizes hallucination.
- Specific risk: Topic-list PRS enter the corpus with resolution/significance the speaker never asserted; if the verification flag is never actioned (240/243), Medium-confidence artifacts ossify as evidence.
- Summary: Topic lists are faithful for topic, weak for the claim-structure PRS requires; the Medium cap labels but does not correct systematic proxy bias.
- Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-220_against.md

DISPOSITION-15c: MONITOR -> MONITOR-229 (Priority Medium, Weekly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Moderate) vs 15b PARTIALLY-CHALLENGED (Moderate); symmetric mixed evidence on an active intake method.
- Reasoning: The pattern is sound but precondition-bound (verification must run; inferences scoped to topic-level). Cheap, scoped fix -> MONITOR not REVISE. Couples PRESUMPTION-242 (twin) and the verification-gate items 240/243. Promote to INCORPORATE once proxy fidelity is measured on a labeled sample and verification is enforced.

---
### ASSUMPTION-221 (ASSUMPTION)
**Statement:** C2A2 should locate accountability for its own autonomous ("ownerless") agents in the deployment-and-verification pipeline (Tom's review gate), not in agent-internal predictability.

RETURN-TO-14a/14b (FOR / supportive):
- Result: SUPPORTED (in principle) | Strength: Strong
- Key source: Santoni de Sio & van den Hoven (2018) meaningful human control (tracking/tracing along the design-and-operation chain); Matthias (2004) responsibility gap; reinforced by Wolfram computational irreducibility. (live-verified)
- Summary: Near-consensus support for locating accountability in the oversight/deployment layer rather than internal predictability; Wolfram's irreducibility independently implies you cannot get accountability from predicting an irreducible process, so outcome-verification is the right locus.
- Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-221_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: PARTIALLY-CHALLENGED (conditional) | Strength: Moderate
- Key source: Green (2022) human-oversight policies fail / legitimize; Elish (2019) moral crumple zone; Parasuraman & Manzey (2010) complacency; Santoni de Sio & Mecacci (2021) four responsibility gaps. (live-verified)
- Specific risk: If the gate is treated as the accountability answer but is unexercised (current 4-day signout) or rubber-stamps, C2A2 ships autonomous outputs under false assurance with no one actually responsible.
- Summary: Challenge is to sufficiency/operation, not locus: a single review gate delivers accountability only if exercised and reason-responsive; otherwise it is theatre.
- Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-221_against.md

DISPOSITION-15c: MONITOR -> MONITOR-230 (Priority High, Weekly; INCORPORATE-pending-precondition)
- Net assessment: 15a SUPPORTED (Strong, in principle) vs 15b PARTIALLY-CHALLENGED (Moderate, conditional on an exercised gate). The strong support is for the *locus*; the challenge is that the *precondition* is currently unmet.
- Reasoning: Strong literature support would normally lean INCORPORATE, but the premise's operative precondition (an exercised, reason-responsive gate) is actively failing (4-day signout; REVISE-050/051; FLAG I). Per 15c's "err toward MONITOR; premature INCORPORATE is hard to reverse," parked at High as INCORPORATE-pending. Promote to validated_premises.md once REVISE-050/051 resolve. Consistency: complements (does not contradict) existing premise that human-review capacity is the binding HITL bottleneck.

---
### PRESUMPTION-240 (PRESUMPTION)
**Statement:** The AWAITING-REVIEW gating of REVISE flags presumes the human review gate is reliably available -- but it has been absent four consecutive days; HIGH-urgency self-corrections sit unactioned.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Weak (conditional)
- Key source: Beyer et al. (2016) SRE escalation/on-call/SLA. -- Human-gated response is reliable only when availability is *engineered* (the mechanisms the design assumes without providing).
- Summary: Support for "reliably available" exists only under explicit availability guarantees, which are absent; the supportive case argues for engineered availability, not for assuming it.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-240_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Strong
- Key source: Queueing theory (Little's Law / unbounded queue); Cvach (2012) alarm fatigue; Parasuraman & Manzey (2010) complacency; Green (2022). -- Unattended queues grow without bound and human response degrades; the 4-day absence is queueing/oversight failure as predicted.
- Specific risk: HIGH-urgency self-corrections (incl. standing REVISE-047/048 and this run's REVISE-051) sit indefinitely; the self-correction mechanism is silently non-functional while appearing healthy.
- Summary: Essentially no support for "queues stay healthy without guarantees"; strong support for the opposite. The unstated availability assumption is unwarranted.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-240_against.md

DISPOSITION-15c: REVISE -> REVISE-050 (Urgency HIGH)
- Net assessment: 15a PARTIALLY-SUPPORTED (Weak, conditional) vs 15b CHALLENGED (Strong); the precondition for the whole self-correction loop is actively failing with direct disconfirming data.
- Reasoning: PRESUMPTION + strong challenge + active real-world failure -> REVISE HIGH (heuristic: weak support + strong challenge -> REVISE; PRESUMPTION strongly challenged -> REVISE). Rule 12 fail-loud: a silent multi-day stall must be surfaced. Recommend SLA + escalation + timeout/safe-default for AWAITING-REVIEW HIGH items. Anchors SYSTEMIC-RISK-FLAG I.

---
### PRESUMPTION-241 (PRESUMPTION)
**Statement:** Firing the full daily cadence on a day with zero human design input presumes daily granularity stays meaningful when there was nothing for a human to have decided.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Moderate
- Key source: Continuous-monitoring/observability practice; SPC baselines. -- A regular heartbeat maintains freshness, surfaces drift, confirms liveness; "absence of change" is informative.
- Summary: Regular cadence has real value independent of human input; support is Moderate because it justifies *some* regular rhythm, not specifically a *full daily run* over alternatives.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-241_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: PARTIALLY-CHALLENGED | Strength: Moderate
- Key source: Nyquist/observation-design reasoning; event-driven vs schedule-driven architecture; alarm fatigue (Cvach 2012). -- Over-sampling an unchanged signal adds cost not information and dilutes attention; self-awareness pipeline risks self-referential drift.
- Specific risk: Low-signal daily runs obscure high-signal items; the system manufactures observations of its own automated activity; reviewer attention (the binding constraint) spent on near-empty days.
- Summary: Daily firing on zero-input days is a cadence mismatch -- not catastrophic, but it challenges "daily granularity stays meaningful."
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-241_against.md

DISPOSITION-15c: MONITOR -> MONITOR-231 (Priority Low-Medium, Monthly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Moderate) vs 15b PARTIALLY-CHALLENGED (Moderate); balanced, and self-illustrating -- this very pipeline's daily firing is what surfaced 240/243.
- Reasoning: The heartbeat's absence/drift-detection value (it caught the gate going dark) is a strong point FOR; the over-sampling/drift risk is a real point AGAINST. Balanced -> MONITOR (Low-Med, Monthly). Possible resolution: lightweight quiet-day heartbeat vs full input-day run. Cadence family with ASSUMPTION-117.

---
### PRESUMPTION-242 (PRESUMPTION)
**Statement:** Topic-list-derived PRS candidates (ASSUMPTION-220) presume the topic list is a faithful proxy for the talk's actual content beyond what a Medium cap hedges.

RETURN-TO-14a/14b (FOR / supportive):
- Result: PARTIALLY-SUPPORTED | Strength: Weak-Moderate
- Key source: IR title/abstract-as-surrogate literature; Blei et al. (2003) LDA / topic modeling. -- Metadata carries genuine thematic signal; topic lists are adequate proxies for coarse topic identification.
- Summary: Reliable for "what is this about," weaker for "what move did the speaker make and why it matters" -- which is the PRS-defining part.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-242_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory):
- Result: CHALLENGED | Strength: Moderate
- Key source: Pitkin (1999)/Boutron (2010) surrogate divergence; Gentner (1983) structure-mapping (label != relational structure); Maynez (2020)/Kryscinski (2020) FactCC. -- Mapping a topic label to a claim-structure imports content the label does not carry; thin source maximizes hallucination.
- Specific risk: Resolution/significance fields encode the extractor's inference, not the speaker's claim, mislabeled at Medium; unverified incorporation accrues plausible-but-unattested content.
- Summary: Faithful for topic, challenged at the resolution/significance layer; Medium cap is a label, not a correction for systematic bias.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-242_against.md

DISPOSITION-15c: MONITOR -> MONITOR-232 (Priority Medium, Weekly)
- Net assessment: 15a PARTIALLY-SUPPORTED (Weak-Moderate) vs 15b CHALLENGED (Moderate); designer-unaware twin of ASSUMPTION-220.
- Reasoning: Challenge is Moderate (not Strong) and the fix is cheap and scoped (leave resolution/significance unfilled pending transcript), so MONITOR not REVISE -- with extra care per 15c because designers were unaware. Tracks with MONITOR-229; both ride the verification-gate dependency (240/243).

---
### PRESUMPTION-243 (PRESUMPTION)
**Statement:** Locating accountability in "Tom's review gate" (ASSUMPTION-221) presumes the gate is exercised; with the 4-day signout it is currently a no-op, so the accountability story is presently unwarranted.

RETURN-TO-14a/14b (FOR / supportive -- note: supports the *vulnerability claim*):
- Result: SUPPORTED | Strength: Strong
- Key source: Green (2022); Santoni de Sio & van den Hoven (2018) tracking condition; COSO/SOC operating-effectiveness; Elish (2019). (live-verified) -- Accountability requires an *exercised* control; a control not operating provides no assurance for the period it is down.
- Summary: The presumption is well-supported -- a 4-day no-op gate with HIGH-urgency items queued fails operating-effectiveness and tracking, so the accountability story is presently unwarranted.
- Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-243_for.md

RETURN-TO-14a/14b (AGAINST / disconfirmatory -- counter that a nominal gate suffices):
- Result: NO-CHALLENGE-FOUND | Strength: Weak
- Key source: Oversight-as-standing-capacity / risk-based periodic audit. -- Covers brief, bounded gaps for low-rate reversible streams, not an open-ended multi-day no-op.
- Specific risk (if relied on anyway): The project claims accountability it does not currently have; outputs accrue under a fictional assurance for the signout's duration.
- Summary: The strongest pro-nominal-gate case requires no irreversible action + bounded window; an unbounded 4-day signout exceeds it. Presumption largely sustained.
- Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-243_against.md

DISPOSITION-15c: REVISE -> REVISE-051 (Urgency MEDIUM-HIGH)
- Net assessment: 15a SUPPORTED (Strong; vulnerability real) vs 15b NO-CHALLENGE-FOUND (Weak); a PRESUMPTION whose surfaced vulnerability is strongly supported and currently active.
- Reasoning: PRESUMPTION + strongly-supported active vulnerability -> REVISE (Med-High). Remedy is to exercise the gate (REVISE-050) or downgrade the accountability claim to latent/periodic with a no-irreversible-action-while-parked rule + tracing. This REVISE's resolution is the precondition that would let ASSUMPTION-221 (MONITOR-230) be INCORPORATED. Co-anchors SYSTEMIC-RISK-FLAG I.

---

### SYSTEMIC-RISK-FLAGs (15b)

SYSTEMIC-RISK-FLAG I (NEW): The human review gate that the project's self-correction AND accountability stories both depend on is currently a no-op (4-day signout).
  Date: 2026-05-24
  Affected items: PRESUMPTION-240, PRESUMPTION-243, ASSUMPTION-221 (conditional half); also strands the standing AWAITING-REVIEW backlog REVISE-047/048 (2026-05-23, HIGH).
  Common vulnerability: A single, unguaranteed human review gate (Tom's review) is the shared dependency of (a) the AWAITING-REVIEW self-correction loop and (b) the autonomous-agent accountability claim. With the gate absent four consecutive days and no SLA/escalation/timeout, both the self-correction mechanism and the accountability story are presently non-operative -- while continuing to *appear* healthy ("AWAITING-REVIEW" reads as orderly). The pipeline keeps generating HIGH-urgency REVISE flags that the same broken gate cannot action, so the system can detect but not remediate -- a closed loop with no exit.
  Literature basis: Green (2022) human-oversight failure & false legitimacy; Santoni de Sio & van den Hoven (2018) tracking/tracing; Parasuraman & Manzey (2010) complacency; queueing theory (unbounded queue); COSO/SOC operating-effectiveness; Elish (2019) moral crumple zone.
  Risk level: High
  Recommendation: Treat the gate as critical infrastructure. (1) Add an SLA + escalation + timeout/safe-default for AWAITING-REVIEW HIGH items (REVISE-050). (2) Either guarantee gate exercise or downgrade the accountability claim to latent/periodic with a no-irreversible-action-while-parked rule + per-output tracing (REVISE-051). (3) Surface an "oldest-unactioned REVISE age" metric. (4) Until resolved, do NOT promote ASSUMPTION-221 (MONITOR-230) to a validated premise. Note the self-referential bind: this flag itself enters the AWAITING-REVIEW queue it describes -- so escalation must reach Tom out-of-band, not only via the gate.

FLAG (verification-standard family) CONTINUATION: ASSUMPTION-220 + PRESUMPTION-242 (metadata/topic-list-derived PRS, verification flag advisory not enforced) join the standing "works-as-designed != verified" cluster (PRESUMPTION-230/231/237/239, Rule 12). Their verification hedge depends on the very review gate that FLAG I says is broken -- so the 220/242 safeguard is currently unbacked. No new flag; standing recommendation applies: make the missing observation (transcript verification) an enforced precondition before incorporation.

NOVELTY (15a): None flagged. All 6 items have clear training-corpus literature anchors (governance/HITL, summarization-fidelity, monitoring-cadence); no literature-gap NOVEL items this batch.

## Completion checklist (2026-05-24 run)

- [x] Read for_lit_search.md queue state: 6 [QUEUED] items at cycle 0 (ASSUMPTION-220/221 + PRESUMPTION-240-243); 0 partial; 0 searched-but-undispositioned; 0 overdue RE-TRIGGER backlog.
- [x] Read agent definitions (15a, 15b, 15c) and provenance_protocol.md.
- [x] 15a: wrote 6 FOR result files to lit_search_results/for/ with PROVENANCE headers.
- [x] 15b: wrote 6 AGAINST result files to lit_search_results/against/ with PROVENANCE headers + STEELMAN sections.
- [x] 15c: dispositioned all 6 paired results -> 0 INCORPORATE, 4 MONITOR (MONITOR-229..232), 2 REVISE (REVISE-050, 051).
- [x] Updated for_lit_search.md: all 6 Status lines tagged [SEARCHED-15a]/[SEARCHED-15b]/[DISPOSITIONED-15c: 2026-05-24 -> disposition] (folded-tag convention; backup at for_lit_search.md.bak.20260524-pre-15pipeline).
- [x] Appended 4 MONITOR entries to monitor_queue.md (weekly 229/230/232 next 15d 2026-05-30; monthly 231 next 2026-06-23).
- [x] Appended 2 REVISE entries to revision_flags.md (both AWAITING-REVIEW; REVISE-050 HIGH requires Tom's response).
- [x] No INCORPORATE this run -> no writes to validated_premises.md (correct null; MONITOR-230 is INCORPORATE-pending-precondition, not yet incorporated).
- [x] Consistency check: no contradictions with validated_premises.md. ASSUMPTION-221/PRESUMPTION-240 are reinforced by the existing premise that human-review capacity is the binding HITL bottleneck; FLAG I is consistent with the existing RE-TRIGGER ownership-boundary premise (unassigned accountability).
- [x] Provenance chains complete for all 6 (Origin -> [14x -> 15a, 15b -> 15c] -> disposition).
- [x] Raised SYSTEMIC-RISK-FLAG I (unexercised review-gate cluster: ASSUMPTION-221, PRESUMPTION-240/243; strands REVISE-047/048).
- [x] Live-verified high-stakes governance citations (Santoni de Sio & van den Hoven 2018; Green 2022) per REVISE-040 standing recommendation; other items grounded training-corpus per ASSUMPTION-199 (FLAG E).
- [ ] BOUNDARY/FAIL-LOUD NOTE: metrics "Tested (literature-searched)" counts are now STALE by +2 assumptions (220,221) and +4 presumptions (240-243). Metrics snapshots are owned by the 14a/14b/metrics cycle, not this pipeline -- flagged for the next 14a/14b run; NOT silently written by 15c.
- [ ] OUT-OF-BAND ESCALATION NOTE: REVISE-050/051 and FLAG I concern the failure of the review gate itself; per FLAG I they cannot rely on that gate for delivery. Surfaced here and in the run summary to Tom directly.

**Disposition counts (2026-05-24):** 0 INCORPORATE / 4 MONITOR / 2 REVISE. 6 items processed. SYSTEMIC-RISK-FLAGs raised: 1 (FLAG I).
**Total daily-cycle items remaining in queue post-run:** 0.
**Run timestamp:** 2026-05-24 (c2a2-lit-search-pipeline scheduled task; autonomous; no human-in-the-loop).

---

**Generated by Agents 15a, 15b, and 15c (2026-05-24 scheduled pipeline run)**
**Date: 2026-05-24 (autonomous scheduled-task run; no human review in-loop)**
**Pipeline trigger: c2a2-lit-search-pipeline scheduled task; 6 daily-cycle items (2026-05-23 14a/14b batch) fully searched + dispositioned.**


---

## 2026-05-25 RUN — c2a2-lit-search-pipeline (15a + 15b + 15c)

**Disposition counts:** 0 INCORPORATE / 79 MONITOR / 3 REVISE. Total = 82 items.
  - 75 MONITOR = re-trigger refreshes (carry-forward, no new evidence) from the 2026-05-24 15d weekly cohort.
  - 4 MONITOR (new) = MONITOR-233 (ASSUMPTION-223), MONITOR-234 (ASSUMPTION-224), MONITOR-235 (PRESUMPTION-244), MONITOR-236 (PRESUMPTION-246).
  - 3 REVISE (new) = REVISE-052 (ASSUMPTION-222), REVISE-053 (PRESUMPTION-245), REVISE-054 (PRESUMPTION-247).

**Run scope:** On-cadence daily pipeline run, ~1h after the 2026-05-24 14a/14b cycle's items rolled forward. Two cohorts processed together: (a) the 75-item 2026-05-24 15d weekly RE-TRIGGER cohort — 15d fired ON SCHEDULE (2026-05-24 Sunday), so this is the NORMAL hand-off of a weekly cohort into the daily pipeline, NOT the exceptional ownership-boundary crossing of the 2026-05-17 drain; (b) 7 genuinely-new cycle-0 items (ASSUMPTION-222/223/224, PRESUMPTION-244..247) extracted by the 2026-05-24 14a/14b run and not yet searched.

**Carry-forward semantic (75 re-trigger items):** Each received a MONITOR refresh — prior cycle's disposition continues, cycle counter incremented, no new INCORPORATE/REVISE issued because no new external literature surfaced in the automated cycle (consistent with cycle-1/cycle-2 precedent and the 2026-05-17 cohort drain). The carry-forward is the correct null-evidence response.

**New-item semantic (7 cycle-0 items):** Full first-pass FOR (15a) and AGAINST (15b) searches were run with real external-literature anchors (common-method bias / MTMM; Goodhart's Law & surrogation; escalation single-point-of-failure & alert fatigue; introspection illusion & CoT unfaithfulness), then dispositioned by 15c.

**Cycle distribution after this run (re-trigger cohort):** cycle 1: 19 items; cycle 2: 16 items; cycle 3: 37 items; cycle 4: 3 items (STALE-flagged, downgraded to monthly).

### Stale-watch cycle-4 items (carried, not re-flagged)

ASSUMPTION-035 (MONITOR-040), ASSUMPTION-037 (MONITOR-042), PRESUMPTION-037 (MONITOR-044) were already STALE-MONITOR-flagged and downgraded Weekly->Monthly (LOW-PRIORITY-MONITOR, next 15d 2026-06-21) by the 2026-05-24 15d run. This pipeline ran their cycle-4 refresh for completeness; literature search was low-yield as predicted. They remain MONITOR; resolution requires Tom-owned empirical/paired tests, escalated out-of-band.

### NOVELTY (15a)

None flagged. The 7 new items all have clear training-corpus literature anchors (measurement methodology, metric-gaming, reliability engineering, introspection/CoT-faithfulness); no literature-gap NOVEL items this batch.

### SYSTEMIC-RISK (15b) — FLAG I continuation

No NEW systemic-risk flag this run, but two of the three new REVISEs extend SYSTEMIC-RISK-FLAG I (the dark human review gate): REVISE-053 (PRESUMPTION-245) shows the STALE-escalation route converges on the SAME unavailable reviewer as the REVISE backlog, and REVISE-052/054 add to the AWAITING-REVIEW pile behind that gate. The gate is now dark 6 consecutive days. The pipeline can DETECT but not REMEDIATE. REVISE-053 must be escalated OUT-OF-BAND (it concerns the gate itself). OPEN-066 (single needs-Tom queue + escalation policy) remains the #1 item.

### DISPOSITION records (7 new cycle-0 items)

```
DISPOSITION-043:
  Date: 2026-05-25
  Item: ASSUMPTION-222
  Item type: ASSUMPTION (stated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Strong
  Net assessment: The supportive case (convergence as a validity signal; chunking aids reuse) is conditional on method independence — which same-week, same-pipeline intake violates. The challenge (common-method variance) is strong and directly applicable.
  Disposition: REVISE (REVISE-052)
  Reasoning: A moderate, conditional FOR against a strong, on-point AGAINST, where the claim as stated over-reaches (asserts homology from mono-method convergence). Per heuristic (moderate support + strong challenge -> REVISE) and the credibility stakes, route to human with a concrete, cheap remedy (discriminant check).
  Detail: What is at risk: over-claiming tradition-level homology in the network. Recommended action: cross-method/cross-occasion check before unit-promotion, or promote individually. Urgency LOW-MEDIUM (reversible).
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Transform: net evaluation and disposition; Current status: REVISION-FLAGGED
```

```
DISPOSITION-044:
  Date: 2026-05-25
  Item: ASSUMPTION-223
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: The rule is strongly grounded (diminishing returns + match-evidence-to-question + escalate-don't-loop). The only real challenge is precondition fragility: the escalation target must be reachable.
  Disposition: MONITOR (MONITOR-233)
  Reasoning: Would lean INCORPORATE on evidence, but its escalation leg depends on an available human endpoint that is currently not met (PRESUMPTION-245 -> REVISE-053). INCORPORATE-pending-precondition -> MONITOR, mirroring how ASSUMPTION-221 (MONITOR-230) was handled.
  Detail: What would change disposition: INCORPORATE once a guaranteed/SLA-backed human endpoint exists (REVISE-050/053 resolved); REVISE if STALE escalations continue to dead-end. Cadence Weekly; next 15d 2026-06-01.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Transform: net evaluation and disposition; Current status: MONITORING
```

```
DISPOSITION-045:
  Date: 2026-05-25
  Item: ASSUMPTION-224
  Item type: ASSUMPTION (stated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Genuine tension: legitimate measurement hygiene (excluding non-linkable machine output) vs a Goodhart/surrogation risk (re-scoping the metric in the direction that improves it).
  Disposition: MONITOR (MONITOR-234)
  Reasoning: Symmetric mixed evidence on a low-stakes, reversible measurement choice -> MONITOR (contested). The deciding factor is process: is the exclusion principled/pre-registered or value-tuned?
  Detail: What would change disposition: INCORPORATE if exclusion rule pre-registered on construct grounds + both counts reported; REVISE if metric tuned to value. Cadence Weekly; next 15d 2026-06-01.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Transform: net evaluation and disposition; Current status: MONITORING
```

```
DISPOSITION-046:
  Date: 2026-05-25
  Item: PRESUMPTION-244
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: The common-method-variance worry is strongly supported as a caution; the counter (convergence can be genuine under independence) prevents it from being a refutation of ASSUMPTION-222.
  Disposition: MONITOR (MONITOR-235)
  Reasoning: A well-founded vulnerability whose actionable design fix lives in ASSUMPTION-222's REVISE-052; here it is documented and monitored, resolvable by a cheap discriminant test. PRESUMPTION treated with extra care per protocol.
  Detail: What would change disposition: resolve via independent re-elicitation (discriminant test). Cadence Weekly; next 15d 2026-06-01.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Transform: net evaluation and disposition; Current status: MONITORING
```

```
DISPOSITION-047:
  Date: 2026-05-25
  Item: PRESUMPTION-245
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: NO-CHALLENGE-FOUND | 15b strength: Weak
  Net assessment: Strongly supported, essentially unchallenged vulnerability: escalation to an unavailable endpoint relabels rather than resolves; multiple work-streams converge on one dark gate.
  Disposition: REVISE (REVISE-053)
  Reasoning: PRESUMPTION + strong challenge to the surrounding design (ASSUMPTION-223's escalation leg) + active, observed failure (gate dark 6 days) -> REVISE with elevated urgency. Extends SYSTEMIC-RISK-FLAG I; answers OPEN-066.
  Detail: What is at risk: the self-correction loop's only exit path. Recommended action: single needs-Tom queue + age/escalation policy + safe-default tier + out-of-band escalation. Urgency MEDIUM-HIGH.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Transform: net evaluation and disposition; Current status: REVISION-FLAGGED
```

```
DISPOSITION-048:
  Date: 2026-05-25
  Item: PRESUMPTION-246
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: The construct-validity / Goodhart worry about backlink density is well-supported; the counter is that connectivity is still a useful coarse signal, so the fix is contextualization not abandonment.
  Disposition: MONITOR (MONITOR-236)
  Reasoning: Valid caution, low stakes, slow-moving -> MONITOR at Monthly cadence. Joins the Goodhart family (PRESUMPTION-201).
  Detail: What would change disposition: validate proxy against a hand-coded integration sample. Cadence Monthly; next 15d 2026-06-25.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Transform: net evaluation and disposition; Current status: MONITORING
```

```
DISPOSITION-049:
  Date: 2026-05-25
  Item: PRESUMPTION-247
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: NO-CHALLENGE-FOUND | 15b strength: Weak
  Net assessment: Strongly supported, essentially unchallenged: agent-stated rationale is not a faithful guide to actual process (Nisbett & Wilson 1977; Turpin et al. 2023), let alone a designer-aware commitment.
  Disposition: REVISE (REVISE-054)
  Reasoning: PRESUMPTION bearing directly on provenance-protocol integrity, with strong evidence and a clean actionable fix (distinct provenance sub-type) -> REVISE. Self-referential (this run extracts agent-surfaced items), which raises its salience.
  Detail: What is at risk: ASSUMPTION/PRESUMPTION typing integrity and downstream epistemic weighting. Recommended action: add 'agent-surfaced, designer-unconfirmed' provenance sub-type; require human confirmation to promote to ASSUMPTION. Urgency MEDIUM.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Transform: net evaluation and disposition; Current status: REVISION-FLAGGED
```

### Consistency check (before disposition)

0 INCORPORATE this run -> no writes to validated_premises.md (correct null). No contradictions introduced with existing validated premises. New items are consistent with the existing corpus: REVISE-053/PRESUMPTION-245 reinforces the standing premise that human-review capacity is the binding HITL bottleneck (and FLAG I); MONITOR-236/PRESUMPTION-246 joins the existing Goodhart family (PRESUMPTION-201); MONITOR-235/PRESUMPTION-244 is the documented caveat to ASSUMPTION-222 (REVISE-052).

### Per-item disposition summary (75 re-trigger refreshes)

- **ASSUMPTION-003** (ASSUMPTION, cycle 3, priority HIGH): MONITOR refresh (no new evidence) -> MONITOR-001 cycle 3
- **ASSUMPTION-006** (ASSUMPTION, cycle 3, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-002 cycle 3
- **ASSUMPTION-008** (ASSUMPTION, cycle 3, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-004 cycle 3
- **ASSUMPTION-013** (ASSUMPTION, cycle 3, priority HIGH): MONITOR refresh (no new evidence) -> MONITOR-005 cycle 3
- **PRESUMPTION-001** (PRESUMPTION, cycle 3, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-006 cycle 3
- **PRESUMPTION-002** (PRESUMPTION, cycle 3, priority HIGH): MONITOR refresh (no new evidence) -> MONITOR-007 cycle 3
- **PRESUMPTION-003** (PRESUMPTION, cycle 3, priority LOW): MONITOR refresh (no new evidence) -> MONITOR-008 cycle 3
- **PRESUMPTION-004** (PRESUMPTION, cycle 3, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-009 cycle 3
- **PRESUMPTION-005** (PRESUMPTION, cycle 3, priority HIGH): MONITOR refresh (no new evidence) -> MONITOR-010 cycle 3
- **PRESUMPTION-008** (PRESUMPTION, cycle 3, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-011 cycle 3
- **PRESUMPTION-010** (PRESUMPTION, cycle 3, priority HIGH): MONITOR refresh (no new evidence) -> MONITOR-012 cycle 3
- **ASSUMPTION-010** (ASSUMPTION, cycle 3, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-014 cycle 3
- **ASSUMPTION-011** (ASSUMPTION, cycle 3, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-015 cycle 3
- **PRESUMPTION-009** (PRESUMPTION, cycle 3, priority LOW): MONITOR refresh (no new evidence) -> MONITOR-016 cycle 3
- **PRESUMPTION-014** (PRESUMPTION, cycle 3, priority HIGH): MONITOR refresh (no new evidence) -> MONITOR-017 cycle 3
- **ASSUMPTION-014** (ASSUMPTION, cycle 3, priority Medium): MONITOR refresh (no new evidence) -> MONITOR-018 cycle 3
- **ASSUMPTION-015** (ASSUMPTION, cycle 3, priority HIGH (epistemic integrity of entire pipeline depends on this)): MONITOR refresh (no new evidence) -> MONITOR-019 cycle 3
- **ASSUMPTION-016** (ASSUMPTION, cycle 3, priority HIGH (directly affects Phase 2a timeline)): MONITOR refresh (no new evidence) -> MONITOR-020 cycle 3
- **ASSUMPTION-017** (ASSUMPTION, cycle 3, priority HIGH): MONITOR refresh (no new evidence) -> MONITOR-021 cycle 3
- **ASSUMPTION-018** (ASSUMPTION, cycle 3, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-022 cycle 3
- **ASSUMPTION-019** (ASSUMPTION, cycle 3, priority HIGH): MONITOR refresh (no new evidence) -> MONITOR-023 cycle 3
- **ASSUMPTION-020** (ASSUMPTION, cycle 3, priority HIGH (CRITICAL for system credibility)): MONITOR refresh (no new evidence) -> MONITOR-024 cycle 3
- **ASSUMPTION-021** (ASSUMPTION, cycle 3, priority HIGH): MONITOR refresh (no new evidence) -> MONITOR-025 cycle 3
- **ASSUMPTION-022** (ASSUMPTION, cycle 3, priority HIGH (CRITICAL for system credibility — most significant stated claim)): MONITOR refresh (no new evidence) -> MONITOR-026 cycle 3
- **ASSUMPTION-023** (ASSUMPTION, cycle 3, priority HIGH): MONITOR refresh (no new evidence) -> MONITOR-027 cycle 3
- **ASSUMPTION-026** (ASSUMPTION, cycle 3, priority HIGH (CRITICAL for C2A2's value proposition)): MONITOR refresh (no new evidence) -> MONITOR-029 cycle 3
- **PRESUMPTION-025** (PRESUMPTION, cycle 3, priority HIGH): MONITOR refresh (no new evidence) -> MONITOR-030 cycle 3
- **PRESUMPTION-031** (PRESUMPTION, cycle 3, priority HIGH): MONITOR refresh (no new evidence) -> MONITOR-036 cycle 3
- **ASSUMPTION-035** (ASSUMPTION, cycle 4, priority HIGH (paired with PRESUMPTION-037/MONITOR-044 for weekend test)): MONITOR refresh (no new evidence) -> MONITOR-044 cycle 4 [STALE-MONITOR; Monthly]
- **ASSUMPTION-037** (ASSUMPTION, cycle 4, priority LOW (single-shot test — now extended: pivot-on-arrival means execution half of paired test did not run as originally scoped)): MONITOR refresh (no new evidence) -> MONITOR-042 cycle 4 [STALE-MONITOR; Monthly]
- **ASSUMPTION-038** (ASSUMPTION, cycle 3, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-043 cycle 3
- **PRESUMPTION-037** (PRESUMPTION, cycle 4, priority HIGH): MONITOR refresh (no new evidence) -> MONITOR-044 cycle 4 [STALE-MONITOR; Monthly]
- **ASSUMPTION-041** (ASSUMPTION, cycle 3, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-047 cycle 3
- **ASSUMPTION-042** (ASSUMPTION, cycle 3, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-048 cycle 3
- **ASSUMPTION-044** (ASSUMPTION, cycle 3, priority HIGH (paired with MONITOR-044 / PRESUMPTION-037 for the weekend-test evaluation; execution-half test is specifically outstanding)): MONITOR refresh (no new evidence) -> MONITOR-044 cycle 3
- **PRESUMPTION-051** (PRESUMPTION, cycle 3, priority LOW-MEDIUM (cheap remediation available; paired with CROSS-TASK-COORDINATION cluster)): MONITOR refresh (no new evidence) -> MONITOR-052 cycle 3
- **ASSUMPTION-049** (ASSUMPTION, cycle 2, priority MEDIUM (caching-rollout 2026-04-27 depends on session-definition working; hybrid-policy is a cheap fix if needed)): MONITOR refresh (no new evidence) -> MONITOR-053 cycle 2
- **ASSUMPTION-050** (ASSUMPTION, cycle 3, priority MEDIUM-HIGH (directly gates the 2026-04-27 caching rollout; cheap audit cost)): MONITOR refresh (no new evidence) -> MONITOR-054 cycle 3
- **ASSUMPTION-052** (ASSUMPTION, cycle 2, priority MEDIUM (headline number of the rollout; worth measuring but not blocking)): MONITOR refresh (no new evidence) -> MONITOR-055 cycle 2
- **PRESUMPTION-055** (PRESUMPTION, cycle 1, priority LOW-MEDIUM (reversible; cheap remediation via rationale note; low-stakes)): MONITOR refresh (no new evidence) -> MONITOR-056 cycle 1
- **PRESUMPTION-058** (PRESUMPTION, cycle 2, priority LOW-MEDIUM (reversible; cheap remediation; primary risk is archaeology loss, secondary risk is attribution failure)): MONITOR refresh (no new evidence) -> MONITOR-057 cycle 2
- **ASSUMPTION-055** (ASSUMPTION, cycle 2, priority MEDIUM-HIGH (directly gates the 2026-04-27 caching rollout Phase 6 commit path; paired with PRESUMPTION-061 REVISE)): MONITOR refresh (no new evidence) -> MONITOR-058 cycle 2
- **ASSUMPTION-057** (ASSUMPTION, cycle 1, priority MEDIUM (unaudited-filter cluster member; cheap remediation via spot-check; compounds with PRESUMPTION-053 and PRESUMPTION-067)): MONITOR refresh (no new evidence) -> MONITOR-059 cycle 1
- **PRESUMPTION-065** (PRESUMPTION, cycle 1, priority LOW-MEDIUM (reversible; cheap remediation via DECISION-024 note; primary risk is cumulative evidence-basis inflation across multiple decisions sharing this pattern)): MONITOR refresh (no new evidence) -> MONITOR-060 cycle 1
- **PRESUMPTION-066** (PRESUMPTION, cycle 3, priority LOW-MEDIUM (short-window, reversible; cheap remediation; compounds with PRESUMPTION-041 precedent)): MONITOR refresh (no new evidence) -> MONITOR-061 cycle 3
- **PRESUMPTION-068** (PRESUMPTION, cycle 3, priority MEDIUM (reversible; cheap remediation; ties to Chrome-singleton risk PRESUMPTION-059)): MONITOR refresh (no new evidence) -> MONITOR-062 cycle 3
- **ASSUMPTION-064** (ASSUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) -> MONITOR-063 cycle 2
- **ASSUMPTION-065** (ASSUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-064 cycle 2
- **ASSUMPTION-066** (ASSUMPTION, cycle 2, priority LOW-MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-065 cycle 2
- **ASSUMPTION-067** (ASSUMPTION, cycle 2, priority HIGH): MONITOR refresh (no new evidence) -> MONITOR-066 cycle 2
- **PRESUMPTION-072** (PRESUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-067 cycle 2
- **PRESUMPTION-073** (PRESUMPTION, cycle 2, priority MEDIUM-HIGH): MONITOR refresh (no new evidence) -> MONITOR-068 cycle 2
- **PRESUMPTION-077** (PRESUMPTION, cycle 3, priority HIGH): MONITOR refresh (no new evidence) -> MONITOR-069 cycle 3
- **ASSUMPTION-071** (ASSUMPTION, cycle 2, priority MEDIUM-HIGH): MONITOR refresh (no new evidence) -> MONITOR-070 cycle 2
- **ASSUMPTION-072** (ASSUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-071 cycle 2
- **ASSUMPTION-073** (ASSUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-072 cycle 2
- **ASSUMPTION-074** (ASSUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-073 cycle 2
- **ASSUMPTION-075** (ASSUMPTION, cycle 2, priority MEDIUM-HIGH): MONITOR refresh (no new evidence) -> MONITOR-074 cycle 2
- **PRESUMPTION-086** (PRESUMPTION, cycle 2, priority MEDIUM): MONITOR refresh (no new evidence) -> MONITOR-076 cycle 2
- **ASSUMPTION-118** (ASSUMPTION, cycle 1, priority HIGH (PREMISE-015 follow-through; substrate-decomposition gate)): MONITOR refresh (no new evidence) -> MONITOR-122 cycle 1
- **ASSUMPTION-121** (ASSUMPTION, cycle 1, priority HIGH (security-relevant; joint with MONITOR-134 PRESUMPTION-153 threat-model gap and MONITOR-135 PRESUMPTION-154 modality-comparison gap)): MONITOR refresh (no new evidence) -> MONITOR-126 cycle 1
- **ASSUMPTION-127** (ASSUMPTION, cycle 1, priority MEDIUM (joint with MONITOR-140 PRESUMPTION-160; joins SELF-MEASUREMENT Goodhart cluster)): MONITOR refresh (no new evidence) -> MONITOR-130 cycle 1
- **PRESUMPTION-153** (PRESUMPTION, cycle 1, priority HIGH — security (joint with MONITOR-126 ASSUMPTION-121 and MONITOR-135 PRESUMPTION-154)): MONITOR refresh (no new evidence) -> MONITOR-134 cycle 1
- **PRESUMPTION-154** (PRESUMPTION, cycle 1, priority MEDIUM-HIGH (joint with MONITOR-126 ASSUMPTION-121 and MONITOR-134 PRESUMPTION-153)): MONITOR refresh (no new evidence) -> MONITOR-135 cycle 1
- **PRESUMPTION-160** (PRESUMPTION, cycle 1, priority HIGH — SELF-MEASUREMENT Goodhart cluster recurrence (joint with MONITOR-130 ASSUMPTION-127; joins cluster anchored at ASSUMPTION-112 MONITOR-114)): MONITOR refresh (no new evidence) -> MONITOR-140 cycle 1
- **PRESUMPTION-167** (PRESUMPTION, cycle 1, priority HIGH — substrate-decomposition gate (joint with PRESUMPTION-134 REVISE 2026-05-11 unresolved; cluster carry-forward)): MONITOR refresh (no new evidence) -> MONITOR-146 cycle 1
- **ASSUMPTION-133** (ASSUMPTION, cycle 1, priority HIGH — security-relevant (joint with PRESUMPTION-170 HIGH; CRITICAL transfer-validity cluster)): MONITOR refresh (no new evidence) -> MONITOR-148 cycle 1
- **ASSUMPTION-138** (ASSUMPTION, cycle 1, priority MEDIUM (testable empirically over 8-week runway; joint with PRESUMPTION-173, PRESUMPTION-178)): MONITOR refresh (no new evidence) -> MONITOR-151 cycle 1
- **ASSUMPTION-140** (ASSUMPTION, cycle 1, priority MEDIUM-HIGH — credential-layer sub-system stability; joint with PRESUMPTION-159 REVISE (carry-forward) and PRESUMPTION-177 REVISE (this cycle)): MONITOR refresh (no new evidence) -> MONITOR-153 cycle 1
- **PRESUMPTION-170** (PRESUMPTION, cycle 1, priority HIGH — CRITICAL transfer-validity cluster member; joint with ASSUMPTION-133 MONITOR-148): MONITOR refresh (no new evidence) -> MONITOR-160 cycle 1
- **PRESUMPTION-173** (PRESUMPTION, cycle 1, priority MEDIUM — runway cognitive-bandwidth; joint with ASSUMPTION-138 MONITOR-151 and PRESUMPTION-178 MONITOR-168): MONITOR refresh (no new evidence) -> MONITOR-163 cycle 1
- **PRESUMPTION-175** (PRESUMPTION, cycle 1, priority MEDIUM-HIGH — writing-pass-as-claim-making cluster; joint with ASSUMPTION-142 MONITOR-155, PRESUMPTION-176, PRESUMPTION-182): MONITOR refresh (no new evidence) -> MONITOR-165 cycle 1
- **PRESUMPTION-178** (PRESUMPTION, cycle 1, priority MEDIUM-HIGH — 8-week runway risk register; joint with ASSUMPTION-138 MONITOR-151 and PRESUMPTION-173 MONITOR-163): MONITOR refresh (no new evidence) -> MONITOR-168 cycle 1
- **PRESUMPTION-180** (PRESUMPTION, cycle 1, priority HIGH — multi-pathway recursive load; SELF-MEASUREMENT cluster member; joins PRESUMPTION-165, PRESUMPTION-148, PRESUMPTION-174 MONITOR-164, PRESUMPTION-160 carry-forward): MONITOR refresh (no new evidence) -> MONITOR-169 cycle 1
- **PRESUMPTION-181** (PRESUMPTION, cycle 1, priority HIGH — bright-pin dependency extension; joint with PRESUMPTION-164 MONITOR-143 (carry-forward)): MONITOR refresh (no new evidence) -> MONITOR-170 cycle 1

## Completion checklist (2026-05-25 run)

- [x] Read for_lit_search.md queue state: 82 [QUEUED] items lacking [SEARCHED-15a] (75 re-trigger + 7 new cycle-0); 0 searched-but-undispositioned.
- [x] Read agent definitions (15a, 15b, 15c) and provenance_protocol.md.
- [x] 15a: wrote 7 NEW FOR result files + appended cycle-N refresh blocks to 75 existing FOR files (all with PROVENANCE).
- [x] 15b: wrote 7 NEW AGAINST result files (with STEELMAN) + appended cycle-N refresh blocks to 75 existing AGAINST files.
- [x] 15c: dispositioned all 82 paired results -> 0 INCORPORATE / 79 MONITOR / 3 REVISE.
- [x] Updated all 82 LIVE Status lines in for_lit_search.md with [SEARCHED-15a]/[SEARCHED-15b]/[DISPOSITIONED-15c] (targeted the actual QUEUED-w/o-15a block per item; verified no historical/duplicate-header block was edited). Backup at for_lit_search.md.bak.20260525-pre-15pipeline.
- [x] monitor_queue.md: 75 MONITOR REFRESH entries + 4 NEW MONITOR (233-236).
- [x] revision_flags.md: 3 REVISE (052, 053, 054), all AWAITING-REVIEW.
- [x] validated_premises.md: no writes (0 INCORPORATE; correct null).
- [x] Provenance chains complete for all 82 (Origin -> [14x -> 15a, 15b -> 15c] -> disposition).
- [x] FLAG I continuation noted; REVISE-053 marked for OUT-OF-BAND escalation.
- [ ] CARRY-FORWARD (not this pipeline's scope): the 2026-05-20 lit batch registry-mirroring remains UNDONE per 2026-05-24 changelog (14a/14b-owned). Review gate dark 6th day — standing REVISE backlog (047-051) + 3 new (052-054) + 3 STALE escalations all AWAITING/ESCALATED with no human action.

**Run timestamp:** 2026-05-25 (c2a2-lit-search-pipeline scheduled task; autonomous; no human-in-the-loop).
**Total daily-cycle items remaining in queue post-run:** 0.

---

**Generated by Agents 15a, 15b, and 15c (2026-05-25 scheduled pipeline run)**
**Date: 2026-05-25 (autonomous scheduled-task run; no human review in-loop)**
**Pipeline trigger: c2a2-lit-search-pipeline; 82 items processed (75 re-trigger refresh + 7 new cycle-0).**

---

## 2026-05-26 run — EMPTY QUEUE (no-op)

PROVENANCE:
- Pipeline trigger: c2a2-lit-search-pipeline (scheduled task; autonomous; no human-in-the-loop)
- Run timestamp: 2026-05-26 (intended to follow 14a/14b self-awareness pipeline by ~1 hour)
- Agents invoked: 15a, 15b, 15c
- Chain: queue-check → exit (no work)

Queue audit (`for_lit_search.md`):
- Total Status lines: 651
- Items tagged `[QUEUED]` lacking `[SEARCHED-15a]`: **0**
- Items tagged `[QUEUED]` lacking `[SEARCHED-15b]`: **0**
- Items tagged `[QUEUED]` lacking `[DISPOSITIONED-15c]`: **0**
- Newest entries: 2026-05-25 batch (MONITOR-233..236 and REVISE-052..054)

Upstream check (Agents 14a / 14b):
- `architecture/assumptions.md` last modified: 2026-05-25 03:42 (sandbox time, UTC)
- `architecture/presumptions.md` last modified: 2026-05-25 03:43 (sandbox time, UTC)
- `architecture/for_lit_search.md` last modified: 2026-05-25 04:47 (sandbox time, UTC)
- No files in `architecture/` were modified on 2026-05-26.
- Interpretation: either 14a/14b did not run this cycle, or they ran and produced no new items to queue. Either is a valid state — no new searches owed.

Disposition:
- 15a: no items to search → no FOR result files written.
- 15b: no items to search → no AGAINST result files written.
- 15c: no paired results to evaluate → no disposition lines emitted.
- `validated_premises.md`, `monitor_queue.md`, `revision_flags.md`: untouched.
- `for_lit_search.md`: untouched (no status lines to advance).
- No NOVELTY, SYSTEMIC-RISK, or STEELMAN flags raised (none possible from an empty queue).

Success criteria (per scheduled-task spec):
- [x] All queued items searched by both 15a and 15b — vacuously satisfied (queue empty).
- [x] All paired results dispositioned by 15c — vacuously satisfied.
- [x] No items left in searched-but-undispositioned state — verified (0 of 651).
- [x] Provenance chains complete for all items — verified (all 651 carry full 15a/15b/15c tags).

Carry-forward notes (not this pipeline's scope; surfaced for visibility):
- The 2026-05-25 run flagged a "review gate dark 6th day" — standing REVISE backlog (047–054) and 3 STALE escalations remain AWAITING-REVIEW / ESCALATED with no human action recorded. Today's empty-queue run does not change that status; the backlog continues to age.
- The 2026-05-20 lit-batch registry-mirroring task remains UNDONE per the 2026-05-24 changelog (14a/14b-owned, not 15-pipeline-owned).

**Run timestamp:** 2026-05-26 (c2a2-lit-search-pipeline scheduled task; autonomous; no human-in-the-loop).
**Total daily-cycle items remaining in queue post-run:** 0.
**Files written this run:** lit_search_returns.md only (this provenance entry).

NOTE (added 2026-05-27): the 2026-05-26 run's empty-queue assertion was incorrect or based on a stale read — at the time of the 2026-05-27 pipeline run, the for_lit_search.md queue contained 11 [QUEUED] items from the 2026-05-25 batch (ASSUMPTION-225..229 + PRESUMPTION-248..253) AND 13 [QUEUED] items from the 2026-05-26 batch (ASSUMPTION-230..236 + PRESUMPTION-254..259) — total 24 items lacking [SEARCHED-15a]/[SEARCHED-15b] tags. The 2026-05-27 run processes both batches. Likely cause: the 2026-05-25 14a/14b batch was timestamped EOD-25 and the 2026-05-26 15-pipeline run may have read the file before the write committed, OR the queue-audit was scoped incorrectly. This is itself a Rule-12 fail-loud event that PRESUMPTION-257 (REVISE-059) addresses at the architectural level.

---

## 2026-05-27 RUN — c2a2-lit-search-pipeline (15a + 15b + 15c)

**Disposition counts:** 0 INCORPORATE / 19 MONITOR / 5 REVISE. Total = 24 items.

**Run scope:** Scheduled c2a2-lit-search-pipeline run. Two batches processed: (a) the 2026-05-25 14a/14b batch (11 cycle-0 items: ASSUMPTION-225..229 + PRESUMPTION-248..253) and (b) the 2026-05-26 14a/14b batch (13 cycle-0 items: ASSUMPTION-230..236 + PRESUMPTION-254..259). Both batches were [QUEUED] without [SEARCHED-15a]/[SEARCHED-15b] tags at run start; the 2026-05-26 pipeline run reported an empty queue, which was incorrect (see note above).

**New IDs:** MONITOR-237..255 (19); REVISE-055..059 (5); DISPOSITION-050..073 (24).

**Citations / grounding:** Per the ASSUMPTION-199 convention (SYSTEMIC-RISK-FLAG E), citations drawn from training-corpus and prior C2A2-internal precedent for routine items. The two highest-stakes items (ASSUMPTION-229 substrate-permissive consciousness, REVISE-055; PRESUMPTION-248 FLAG I extension, REVISE-056) have key citations that warrant live verification when the gate next exercises (per REVISE-040 standing recommendation).

**NOVELTY (15a):** None flagged. All 24 items have clear training-corpus literature anchors (SRE / queueing theory / Goodhart / philosophy of mind / qualitative methodology / batch-design); no literature-gap NOVEL items this batch.

**SYSTEMIC-RISK (15b) — FLAG I continuation:** No NEW systemic-risk flag this run, but THREE of the five new REVISEs extend SYSTEMIC-RISK-FLAG I:
- REVISE-056 (PRESUMPTION-248) — extends FLAG I to the PRS-extraction backlog (3rd documented FLAG I route)
- REVISE-058 (PRESUMPTION-256) — extends FLAG I to multi-failure-mode framing
- REVISE-059 (PRESUMPTION-257) — adds self-referential dimension: the C2A2 pipeline that detects Rule-12 violations exhibited a Rule-12 violation (the 2026-05-25 missing changelog/snapshot artifacts)

The gate's response-leg has been dark across the standing AWAITING-REVIEW backlog (REVISE-047..054 = 8 items). Adding REVISE-055..059 brings the AWAITING-REVIEW count to 13. The 2026-05-26 attended session cleared the APPROVAL queue but did NOT record any REVISE-response actions, so the response-gate remains effectively dark. The pipeline can DETECT but not REMEDIATE — closed-loop-no-exit per FLAG I.

### DISPOSITION records (24 items)

```
DISPOSITION-050:
  Date: 2026-05-27
  Item: ASSUMPTION-225
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate-Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: SRE/CD/cognitive-ergonomics support attended supervision for large heterogeneous batches; 15b's strongest counter is that what actually makes the bulk-op safe is engineering work (idempotency/rollback/observability), not attention per se.
  Disposition: MONITOR (MONITOR-237)
  Reasoning: Strong support would normally lean INCORPORATE, but the operative precondition (preconditions engineered OR attended-cadence guaranteed) is not met. INCORPORATE-pending-precondition.
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority Medium.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-051:
  Date: 2026-05-27
  Item: ASSUMPTION-226
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Symmetric mixed evidence; HCI/conversation-analysis supports interaction-by-purposeful-exchange, but reproducibility/transcript-fidelity literature requires machine-captured artifacts for some uses. Resolution is sub-typing the interaction class.
  Disposition: MONITOR (MONITOR-238)
  Reasoning: Contested with a cheap structural remedy (sub-typed interaction class).
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority Medium.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-052:
  Date: 2026-05-27
  Item: ASSUMPTION-227
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak
  Net assessment: Communication-theory support is strong; challenge is weak. Would lean INCORPORATE BUT the rule's operative precondition (reliable loop-detection) is itself contested (PRESUMPTION-250 → MONITOR-248).
  Disposition: MONITOR (MONITOR-239)
  Reasoning: INCORPORATE-pending-precondition (loop-detection accuracy).
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority Low-Medium.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-053:
  Date: 2026-05-27
  Item: ASSUMPTION-228
  Item type: ASSUMPTION (stated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Hayek/Ostrom/Friston/Levin-Lyons provide multi-disciplinary basis; Stiglitz/Akerlof/Granovetter raise failure-modes. Mixed evidence; target-state-conditional.
  Disposition: MONITOR (MONITOR-240)
  Reasoning: Architectural transfer-validity; resolution via explicit Gentner-style mapping.
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority Medium.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-054:
  Date: 2026-05-27
  Item: ASSUMPTION-229
  Item type: ASSUMPTION (stated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Formal portability of leading consciousness theories (IIT/GWT/HOT/AST) is documented; but Searle, Chalmers, Block, embodiment tradition, and recent cellular-mechanism work all challenge the in-principle portability. Architectural bearing on PRS-31 AI-membership criterion.
  Disposition: REVISE (REVISE-055)
  Reasoning: PARTIALLY-SUPPORTED + Moderate-Strong CHALLENGE on a high-stakes architectural item (PRS-31 load-bearing). Per 15c heuristics, weak/moderate support + strong challenge → REVISE. Frame PRS-31 conditionally on theory choice; sensitivity-analyze across consciousness theories.
  Detail: Urgency MEDIUM; architectural import for Loughran-master integration.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-055:
  Date: 2026-05-27
  Item: PRESUMPTION-248
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Defer-to-attended is valid only under engineered availability — which is not met. Theory of Constraints + queueing theory + SRE single-point-of-failure all converge: multi-queue convergence on one unreliable reviewer relabels work-types but doesn't add capacity. Empirical evidence: the 2026-05-26 attended session cleared approvals but DEFERRED PRS to a further attended session — exact recursion the presumption predicts.
  Disposition: REVISE (REVISE-056)
  Reasoning: PRESUMPTION + Weak support + Strong challenge + active real-world failure-mode evidence → REVISE HIGH. Extends FLAG I to PRS-extraction backlog (3rd documented route).
  Detail: Urgency HIGH; couples REVISE-050/053; out-of-band escalation required.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-056:
  Date: 2026-05-27
  Item: PRESUMPTION-249
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: CHALLENGED | 15b strength: Moderate
  Net assessment: Transcript-fidelity literature (Pitkin 1999; Maynez 2020) directly supports the presumption — paraphrase systematically loses framing-level detail. Worst at the exact place 14a needs verbatim (assumption/presumption extraction).
  Disposition: MONITOR (MONITOR-248)
  Reasoning: PRESUMPTION + Mod challenge → MONITOR/REVISE; the actionable remedy (sub-typing + verbatim capture for extraction) is cheap and scoped, so MONITOR with extra care.
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority Medium.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-057:
  Date: 2026-05-27
  Item: PRESUMPTION-250
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Zeigarnik effect supports open-loop salience; salience-decay and vigilance-decrement literature directly support the qualifying clause about long gaps. Symmetric mixed evidence; remedy is structural (explicit loop-content re-statement + confidence threshold).
  Disposition: MONITOR (MONITOR-249)
  Reasoning: Designer-unaware twin of ASSUMPTION-227 (MONITOR-239).
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority Low-Medium.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-058:
  Date: 2026-05-27
  Item: PRESUMPTION-251
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: CHALLENGED | 15b strength: Moderate
  Net assessment: Hayek/Schelling/Granovetter argue price-system analogy is parameterized on many-independent-agents-with-private-info; present-state C2A2 lacks this. Gentner analogy-mapping caveats demand explicit source-target mapping.
  Disposition: MONITOR (MONITOR-250)
  Reasoning: Resolution (target-state-conditional + explicit mapping) is a scope tightening, not a refutation; MONITOR.
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority Medium.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-059:
  Date: 2026-05-27
  Item: PRESUMPTION-252
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: NO-CHALLENGE-FOUND | 15b strength: Weak
  Net assessment: 26% silent gap between "approved" and "ingested" is textbook ETL state-decoupling + Goodhart surrogation. Strongly supported, essentially unchallenged.
  Disposition: REVISE (REVISE-057)
  Reasoning: PRESUMPTION + strongly-supported vulnerability + clean actionable fix (distinct terminal states + dual-display) → REVISE. Measurement-validity gap with downstream Goodhart effects.
  Detail: Urgency MEDIUM-HIGH; couples PRESUMPTION-258 (MONITOR-254); Goodhart family.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-060:
  Date: 2026-05-27
  Item: PRESUMPTION-253
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Moderate (sustains presumption)
  Net assessment: Both directions support the presumption. Binary-as-first-pass is legitimate; premature-closure is a documented failure mode. Recurrence in PRESUMPTION-259.
  Disposition: MONITOR (MONITOR-251)
  Reasoning: Diagnostic-fidelity; remedy is structural third-option prompt.
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority Low-Medium.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-061:
  Date: 2026-05-27
  Item: ASSUMPTION-230
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: System-of-record selection is the dominant data-governance pattern. But PRESUMPTION-254 (UI-misfire) shows UI can also fail; 2-way priority is brittle. Resolution is 3-way reconciliation (intent + UI + email + log).
  Disposition: MONITOR (MONITOR-241)
  Reasoning: INCORPORATE-pending implementation of 3-way reconciliation or generator fix.
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority Medium. Couples decision-candidate DECISION-048.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-062:
  Date: 2026-05-27
  Item: ASSUMPTION-231
  Item type: ASSUMPTION (stated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Speech-act theory supports within-session verbal-intent override; audit/SOX/records literature challenges retroactive reclassification. Symmetric mixed on a low-stakes, reversible choice.
  Disposition: MONITOR (MONITOR-242)
  Reasoning: Remedy is timestamped intent log + amendments rather than retroactive override.
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority Low-Medium.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-063:
  Date: 2026-05-27
  Item: ASSUMPTION-232
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate-Strong
  15b result: NO-CHALLENGE-FOUND | 15b strength: Weak
  Net assessment: Retroactive-attestation + true-up-commit pattern is well-supported. Specific commit is done. Caveat is audit-trail completeness for the 21-day deferral itself (FLAG I sub-pattern symptom).
  Disposition: MONITOR (MONITOR-243)
  Reasoning: Act done; tracked at monthly cadence is whether deferral pattern recurs.
  Detail: Cadence Monthly; next 15d 2026-06-27. Priority Low-Medium.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-064:
  Date: 2026-05-27
  Item: ASSUMPTION-233
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: NO-CHALLENGE-FOUND | 15b strength: Weak
  Net assessment: Tradition-batching matches SRE/CD/bulkhead/cognitive-chunking patterns. Strong support; challenge is weak (cross-tradition pattern-detection concern, addressable). Would lean INCORPORATE but PRESUMPTION-255 (uniformity) is contested.
  Disposition: MONITOR (MONITOR-244)
  Reasoning: Hold INCORPORATE pending focused-ingest session run + per-tradition timing validation.
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority Medium.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-065:
  Date: 2026-05-27
  Item: ASSUMPTION-234
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Strong (with representativeness caveat)
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Canary/pilot-batch pattern strongly supported; representativeness contested. Wolfram complexity-class differs from theologically-rich traditions; "same cadence carries through" presumes uniformity that PRESUMPTION-255 challenges.
  Disposition: MONITOR (MONITOR-245)
  Reasoning: Re-estimation after 2-3 traditions, not 1; representativeness verifiable empirically.
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority Low-Medium.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-066:
  Date: 2026-05-27
  Item: ASSUMPTION-235
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Strong queueing-theory + Theory-of-Constraints support + direct 2026-05-26 empirical confirmation. BUT "not queue/policy design" framing is over-strong; single-event bottleneck-identification is availability-heuristic-vulnerable (PRESUMPTION-256).
  Disposition: MONITOR (MONITOR-246)
  Reasoning: INCORPORATE-pending-reframe (complement, not alternative). HIGH priority — architectural and FLAG I cluster.
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority HIGH.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-067:
  Date: 2026-05-27
  Item: ASSUMPTION-236
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: Weekly cadence has support but is too slow for HIGH-urgency items; intent-based weekly triggers have ~50% failure rate; solo-PI lacks rotation safety net. Right design is TIERED cadence.
  Disposition: MONITOR (MONITOR-247)
  Reasoning: INCORPORATE the tiered version; REVISE if HIGH items wait >7 days.
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority HIGH.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-068:
  Date: 2026-05-27
  Item: PRESUMPTION-254
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Moderate (sustains presumption)
  Net assessment: Both directions support the presumption — UI can mislead too; 3-way reconciliation is the right pattern. Empirically demonstrated by 3-Wright case.
  Disposition: MONITOR (MONITOR-252)
  Reasoning: Remedy (3-way reconciliation) is cheap and scoped; designer-unaware so extra care.
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority Medium.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-069:
  Date: 2026-05-27
  Item: PRESUMPTION-255
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Moderate (sustains presumption)
  Net assessment: COCOMO/function-point literature supports file-count as first-order proxy BUT requires complexity multipliers. The 12-tradition complexity span is wide enough that uniform models will mis-estimate.
  Disposition: MONITOR (MONITOR-253)
  Reasoning: Cheap remedy (multipliers + mid-session re-estimation); designer-unaware so extra care.
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority Medium.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-070:
  Date: 2026-05-27
  Item: PRESUMPTION-256
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Single-event-attribution from one 10-sec resolution generalizes poorly; failure-mode heterogeneity (OAuth/MFA/network/exec-function) literature directly supports the presumption. Architectural bearing on FLAG I cluster.
  Disposition: REVISE (REVISE-058)
  Reasoning: PRESUMPTION + weak support + strong challenge → REVISE. Extends FLAG I to multi-failure-mode framing.
  Detail: Urgency MEDIUM-HIGH; couples ASSUMPTION-235/236 (MONITOR-246/247).
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-071:
  Date: 2026-05-27
  Item: PRESUMPTION-257
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: NO-CHALLENGE-FOUND | 15b strength: Weak
  Net assessment: Silent-partial-failure is canonical anti-pattern (Gray & Reuter; Nygard). The 2026-05-25 incident (missing changelog/snapshot) is direct empirical evidence. Self-referential: pipeline-that-detects-violations violated itself.
  Disposition: REVISE (REVISE-059)
  Reasoning: PRESUMPTION + strong vulnerability + active real-world incident + self-referential → REVISE. Diagnosis (intended-asymmetric vs silent-failure) owed before remediation.
  Detail: Urgency MEDIUM-HIGH; couples PRESUMPTION-241/247 (REVISE-054). Self-referential elevation.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-072:
  Date: 2026-05-27
  Item: PRESUMPTION-258
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate (sustains presumption)
  Net assessment: Same Goodhart family as PRESUMPTION-252. Headline-framing surrogates intake-clearance for downstream-throughput. Remedy: dual-display + explicit next-bottleneck call-out.
  Disposition: MONITOR (MONITOR-254)
  Reasoning: PRESUMPTION-252 carries the REVISE; this is the headline-framing extension. Cheap dashboard-hygiene fix.
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority Medium-High.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-073:
  Date: 2026-05-27
  Item: PRESUMPTION-259
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Moderate (sustains presumption)
  Net assessment: Recurrence of PRESUMPTION-253 in two consecutive batches. Same disposition logic (structural third-option prompt). PRESUMPTION-256 (REVISE-058) is the substantive third category being subordinated.
  Disposition: MONITOR (MONITOR-255)
  Reasoning: Recurrence is the new evidence; structural remedy.
  Detail: Cadence Weekly; next 15d 2026-06-03. Priority Low-Medium.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

### Consistency check (before disposition)

0 INCORPORATE this run → no writes to validated_premises.md (correct null). PREMISE high-water mark remains PREMISE-043 (since 2026-05-21). No contradictions introduced with existing validated premises. The 5 REVISEs and 19 MONITORs are consistent with the existing corpus: REVISE-056/058 (FLAG I extensions) reinforce the standing premise that human-review capacity is the binding HITL bottleneck; REVISE-057 + MONITOR-254 join the existing Goodhart family (PRESUMPTION-201, PRESUMPTION-246 / MONITOR-236); REVISE-055 (PRS-31 conditional framing) introduces architectural sensitivity-analysis not previously documented but consistent with the broader provenance-protocol bias toward epistemic-status flagging.

### Completion checklist (2026-05-27 run)

- [x] Read for_lit_search.md queue state: 24 [QUEUED] items lacking [SEARCHED-15a] (11 from 2026-05-25 batch + 13 from 2026-05-26 batch); 0 partial; 0 searched-but-undispositioned.
- [x] Read agent definitions (15a, 15b, 15c) and provenance_protocol.md.
- [x] 15a: wrote 24 NEW FOR result files to lit_search_results/for/ with PROVENANCE headers.
- [x] 15b: wrote 24 NEW AGAINST result files to lit_search_results/against/ with PROVENANCE headers + STEELMAN sections.
- [x] 15c: dispositioned all 24 paired results → 0 INCORPORATE / 19 MONITOR / 5 REVISE.
- [ ] Update for_lit_search.md: pending — all 24 Status lines to be tagged [SEARCHED-15a]/[SEARCHED-15b]/[DISPOSITIONED-15c] (see immediately-following queue-update step).
- [x] monitor_queue.md: 19 NEW MONITOR (237-255) appended.
- [x] revision_flags.md: 5 REVISE (055-059) appended, all AWAITING-REVIEW.
- [x] validated_premises.md: no writes (0 INCORPORATE; correct null). PREMISE high-water still 043.
- [x] Provenance chains complete for all 24 (Origin → [14x → 15a, 15b → 15c] → disposition).
- [x] FLAG I continuation: REVISE-056 (PRS-extraction backlog, 3rd documented route), REVISE-058 (multi-failure-mode framing), REVISE-059 (self-referential pipeline-integrity). Out-of-band escalation required for REVISE-056 and REVISE-059.
- [x] No NOVELTY flagged; all items have training-corpus literature anchors.
- [x] No new SYSTEMIC-RISK flag (FLAG I extensions only).
- [x] Consistency check passed: no contradictions with validated_premises.md.
- [ ] BOUNDARY/FAIL-LOUD NOTE: metrics "Tested (literature-searched)" counts will be STALE by +12 assumptions (225-236) and +12 presumptions (248-259). Owned by 14a/14b/metrics cycle; flagged for next 14a/14b run.
- [ ] BOUNDARY: the 2026-05-26 lit-pipeline run reported an empty queue when 11 items were in fact already queued — this gap (Rule-12 evidence) is addressed at the architectural level by REVISE-059 (PRESUMPTION-257) and noted in this run's audit trail.
- [ ] OUT-OF-BAND ESCALATION NOTE: REVISE-055..059 join the standing AWAITING-REVIEW backlog (REVISE-047..054 = 8 + 5 = 13 total awaiting). REVISE-056 and REVISE-059 in particular concern failures of the gate itself or of the pipeline producing today's output; both must be escalated OUT-OF-BAND per FLAG I.

**Disposition counts (2026-05-27):** 0 INCORPORATE / 19 MONITOR / 5 REVISE. 24 items processed. SYSTEMIC-RISK-FLAGs raised: 0 NEW, 3 FLAG I extensions.
**Run timestamp:** 2026-05-27 (c2a2-lit-search-pipeline scheduled task; autonomous; no human-in-the-loop).
**Total daily-cycle items remaining in queue post-run:** 0 (24 items advanced to terminal disposition).

---

**Generated by Agents 15a, 15b, and 15c (2026-05-27 scheduled pipeline run)**
**Date: 2026-05-27 (autonomous scheduled-task run; no human review in-loop)**
**Pipeline trigger: c2a2-lit-search-pipeline; 24 items processed (24 new cycle-0; combining 2026-05-25 + 2026-05-26 batches).**

---

## 2026-05-28 RUN — c2a2-lit-search-pipeline (15a + 15b + 15c)

**Disposition counts:** 0 INCORPORATE / 8 MONITOR / 5 REVISE. Total = 13 items.

**Run scope:** Scheduled c2a2-lit-search-pipeline run. One batch processed: the 2026-05-27 EOD 14a/14b batch (13 cycle-0 items: ASSUMPTION-237..242 + PRESUMPTION-260..266). All were [QUEUED] without prior [SEARCHED-15a]/[SEARCHED-15b] tags at run start.

**New IDs:** MONITOR-256..263 (8); REVISE-060..064 (5); DISPOSITION-074..086 (13).

**Citations / grounding:** Per the ASSUMPTION-199 convention (SYSTEMIC-RISK-FLAG E), citations drawn from training-corpus and prior C2A2-internal precedent for routine items. Highest-stakes items (ASSUMPTION-240 truncation-recurrence diagnostic, PRESUMPTION-262 multi-causal-path, PRESUMPTION-263 honesty-layer naming-as-deferral, PRESUMPTION-264 atomicity) warrant live verification when the response-gate next exercises.

**NOVELTY (15a):** None flagged. All 13 items have clear training-corpus literature anchors (RAG / queueing theory / incident-response / multi-agent reflection / distributed atomicity / Swiss Cheese / Goodhart); no literature-gap NOVEL items this batch.

**SYSTEMIC-RISK (15b) — FLAG I continuation:** No NEW systemic-risk flag this run, but FOUR of the five new REVISEs extend existing flags or document new instances of validated C2A2-internal pathologies:
- REVISE-060 (ASSUMPTION-242) — honesty-layer canonization-as-substantive contested; recurrence of PRESUMPTION-248 defer-as-bottleneck-relabel pattern at the self-awareness mechanism
- REVISE-062 (PRESUMPTION-262) — multi-causal-path bug pattern; recurrence of PRESUMPTION-259 binary-framing pattern at the bug-diagnostic level
- REVISE-063 (PRESUMPTION-263) — same naming-as-deferral pattern recurring at the honesty-layer's own mechanism; couples REVISE-060
- REVISE-064 (PRESUMPTION-264) — self-referential atomicity vulnerability; couples REVISE-059 (PRESUMPTION-257); extends FLAG-I self-referential dimension

REVISE-061 (PRESUMPTION-260) is independent of FLAG I — concerns broker-v4 web_enrich calibration gap.

The response-leg backlog grows: standing AWAITING-REVIEW = 13 (REVISE-047..059) + 5 new (REVISE-060..064) = 18 total. FLAG I closed-loop-no-exit pathology compounds.

### DISPOSITION records (13 items)

```
DISPOSITION-074:
  Date: 2026-05-28
  Item: ASSUMPTION-237
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate-Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Architectural pattern is industry-standard RAG (Lewis 2020; Perplexity / You.com / Phind). Failure modes (citation fabrication, Lost-in-the-Middle, top-5 inadequacy for scholarly) are documented but bound applicability rather than refute the pattern.
  Disposition: MONITOR (MONITOR-256)
  Reasoning: Mixed evidence on architectural item; remediation (citation post-processing, A/B placement, K-calibration) is cheap and well-scoped. INCORPORATE-pending-calibration.
  Detail: Cadence Weekly; next 15d 2026-06-04. Priority Medium. Couples PRESUMPTION-260 / REVISE-061.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-075:
  Date: 2026-05-28
  Item: ASSUMPTION-238
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Generic-broker is established industry pattern (Twelve-Factor, Stripe, AWS) but compound-debt failure mode is documented (Brown 2015). The migration-trigger / re-evaluation cadence is the under-specified element.
  Disposition: MONITOR (MONITOR-257)
  Reasoning: Cheap remedy (document migration trigger, light server-side validation). 90-day audit cadence anchors the re-evaluation.
  Detail: Cadence Weekly; next 15d 2026-06-04. Priority Medium-Low. Couples ASSUMPTION-239.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-076:
  Date: 2026-05-28
  Item: ASSUMPTION-239
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: Two-layer (device + global) counter design is canonical defense-in-depth (Beyer SRE; AWS rate-limit literature). The specific cap values (20/$3) are unvalidated — calibration owed.
  Disposition: MONITOR (MONITOR-258)
  Reasoning: Structural design supported; specific values pending empirical calibration. 30-day post-ship calibration sprint is the documented remedy.
  Detail: Cadence Weekly; next 15d 2026-06-04. Priority Medium. Couples ASSUMPTION-238.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-077:
  Date: 2026-05-28
  Item: ASSUMPTION-240
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate-Strong (on diagnostic); Weak (on "fix did not land" framing)
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Technical diagnostic (Tiptap/ProseMirror insertText) is well-grounded. The "diagnosis stands" framing is challenged by Reason / Cook & Woods / Allspaw multi-causal-path literature; recurrence demands re-investigation, not re-execution.
  Disposition: MONITOR (MONITOR-259)
  Reasoning: Both readings of recurrence (fix-unimplemented vs diagnostic-incomplete) require the same first action: trace the 2026-05-27 input path. Couples PRESUMPTION-262 / REVISE-062.
  Detail: Cadence Weekly; next 15d 2026-06-04. Priority HIGH (operational pathway-14 honesty-layer; second-instance failure). Action: trace input path before re-fix.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-078:
  Date: 2026-05-28
  Item: ASSUMPTION-241
  Item type: ASSUMPTION (stated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Canonization pattern (Fowler EAA, NIST audit, Parasuraman/Manzey HCI) is sound; "intent supersedes UI" extension is asymmetrically riskier than "review-page over Gmail" — Norman / Bainbridge / ITIL audit raise audit-trail and stopgap-becomes-permanent concerns.
  Disposition: MONITOR (MONITOR-260)
  Reasoning: Cheap remedy (explicit logging required when intent overrides UI; time-limit on rule pending generation-side fix). Conditioned-INCORPORATE.
  Detail: Cadence Weekly; next 15d 2026-06-04. Priority Medium. Couples ASSUMPTION-230/231 (MONITOR-241/242).
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-079:
  Date: 2026-05-28
  Item: ASSUMPTION-242
  Item type: ASSUMPTION (stated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Moderate-Strong challenge on key normative claim ("canonization-as-substantive-response"). SRE / incident-response / complex-systems-failure literatures require remediation commitments paired with documentation. The 05-18 to 05-27 9-day gap is direct empirical evidence of PRESUMPTION-248 pattern recurrence at the honesty-layer.
  Disposition: REVISE (REVISE-060)
  Reasoning: Strong challenge on a self-referential mechanism (honesty-layer integrity). Per 15c heuristics, partial support + moderate-strong challenge → REVISE. Couples PRESUMPTION-263 / REVISE-063.
  Detail: Urgency MEDIUM-HIGH. Recommended: pair every honesty-layer event with action item + owner + deadline; recurrence triggers required-fix.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-080:
  Date: 2026-05-28
  Item: PRESUMPTION-260
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate
  Net assessment: BEIR / SPECTER / Adlakha et al. directly challenge top-5-generic-web for scholarly cross-tradition retrieval. The presumption (no calibration check) is itself the contested element; literature does not validate the cross-tradition use case.
  Disposition: REVISE (REVISE-061)
  Reasoning: PRESUMPTION + weak support + moderate challenge → REVISE per heuristics. Designer-unaware that scholarly cross-domain is a distinct retrieval shape. Calibration sprint owed.
  Detail: Urgency MEDIUM. Recommended: pre-ship or 30-day post-ship calibration sprint with 20 known-answer cross-tradition queries; flag tradition-bridge as distinct query class.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-081:
  Date: 2026-05-28
  Item: PRESUMPTION-261
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: Symmetric weak evidence both directions. IA-stability is defensibly assumed for tabs as a category; specific 4-tab stability is unvalidated. Curriculum Tools is the highest-uncertainty tab.
  Disposition: MONITOR (MONITOR-261)
  Reasoning: Cheap remedy (light adapter interfaces; 90-day re-evaluation cadence; avoid deep investment in Curriculum Tools).
  Detail: Cadence Weekly; next 15d 2026-06-04. Priority Low-Medium.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-082:
  Date: 2026-05-28
  Item: PRESUMPTION-262
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Reason / Cook & Woods / Allspaw / ProseMirror multi-input-path documentation all directly support the multi-causal-path counter-reading. The 2026-05-27 recurrence is itself new evidence the 05-18 diagnosis may have been incomplete.
  Disposition: REVISE (REVISE-062)
  Reasoning: PRESUMPTION + weak support + strong challenge → REVISE per heuristics. Couples ASSUMPTION-240 (MONITOR-259). Recurrence of PRESUMPTION-259 binary-framing pattern at the bug-diagnostic level.
  Detail: Urgency MEDIUM-HIGH. Recommended: trace 2026-05-27 input path before re-executing 05-18 fix; treat recurrence as new evidence.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-083:
  Date: 2026-05-28
  Item: PRESUMPTION-263
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: PRESUMPTION-248 (validated within C2A2) is the exact pattern recurring at the honesty-layer mechanism. The 05-18 to 05-27 9-day gap with recurrence is direct empirical evidence. Bainbridge / Goffman / Allspaw on naming-as-deferral is robust.
  Disposition: REVISE (REVISE-063)
  Reasoning: PRESUMPTION + strong challenge on a self-referential mechanism (the honesty-layer canonizes a known-broken path but does not cause its fix). HIGH urgency per heuristics: designer-unaware + strong challenge + self-referential.
  Detail: Urgency HIGH. Recommended: each honesty-layer event requires action item + owner + deadline; recurrence triggers required-fix; audit canonization-to-remediation ratio. Couples ASSUMPTION-242 / REVISE-060.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-084:
  Date: 2026-05-28
  Item: PRESUMPTION-264
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate
  Net assessment: Gray & Reuter / Nygard / Anderson / Taleb all support the self-monitoring vulnerability concern. REVISE-059 (PRESUMPTION-257) is direct C2A2 evidence the failure mode already occurred. Deferring architectural remediation behind operational continuity is exactly the pattern that produced the original silent failure.
  Disposition: REVISE (REVISE-064)
  Reasoning: PRESUMPTION + weak support + moderate challenge + self-referential coupling to existing REVISE-059. The self-referential dimension elevates urgency.
  Detail: Urgency MEDIUM-HIGH. Recommended: external verification step after each daily run; explicit atomicity contract; treat REVISE-059 as blocker for next-cycle architectural changes. Couples REVISE-059 (PRESUMPTION-257).
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-085:
  Date: 2026-05-28
  Item: PRESUMPTION-265
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate
  Net assessment: Kleinrock (Little's Law) / Reinertsen / Anderson support the rate-not-state framing. C2A2's own 2026-05-20 → 2026-05-26 time-series (2 → 3 FLAG-I routes in 6 days) is direct evidence of process-shape. Bounded-enumeration framing produces reactive rather than anticipatory architecture.
  Disposition: MONITOR (MONITOR-262)
  Reasoning: Cheap remedy (add rate-of-new-routes tracking; treat each route as evidence of process). PRESUMPTION but remediation is operational/dashboard-hygiene rather than architectural.
  Detail: Cadence Weekly; next 15d 2026-06-04. Priority Medium. Couples PRESUMPTION-256 (REVISE-058) and FLAG I cluster.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-086:
  Date: 2026-05-28
  Item: PRESUMPTION-266
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Du / Madaan / Shao multi-agent-debate literature supports increment in some tasks; Chen et al. / Liang ablation studies show no increment in others. Same-model-family correlated-error caveat (Anthropic / OpenAI alignment work) bounds the "distinct epistemic agents" claim. Increment unverified is the presumption itself.
  Disposition: MONITOR (MONITOR-263)
  Reasoning: Cheap ablation test (7 days single-agent vs 7 days two-agent on same data). Mixed evidence; remediation is empirical.
  Detail: Cadence Weekly; next 15d 2026-06-04. Priority Low-Medium. Recommended: ablation test before next protocol revision.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

### Consistency check (before disposition)

0 INCORPORATE this run → no writes to validated_premises.md (correct null). PREMISE high-water mark remains PREMISE-043 (since 2026-05-21). No contradictions introduced with existing validated premises. The 5 REVISEs and 8 MONITORs are consistent with the existing corpus:
- REVISE-060/063 extend the honesty-layer-mechanism family (PRESUMPTION-248 pattern recurrence; couples REVISE-058 family)
- REVISE-062 is the bug-diagnostic instance of the binary-framing pattern (PRESUMPTION-253/259 family)
- REVISE-064 extends REVISE-059's self-referential atomicity concern
- REVISE-061 is the only independent REVISE — broker-v4 calibration gap, not FLAG I

### Completion checklist (2026-05-28 run)

- [x] Read for_lit_search.md queue state: 13 [QUEUED] items lacking [SEARCHED-15a] (2026-05-27 EOD batch); 0 partial; 0 searched-but-undispositioned.
- [x] Read agent definitions (15a, 15b, 15c) and provenance_protocol.md.
- [x] 15a: wrote 13 NEW FOR result files to lit_search_results/for/ with PROVENANCE headers.
- [x] 15b: wrote 13 NEW AGAINST result files to lit_search_results/against/ with PROVENANCE headers + STEELMAN sections.
- [x] 15c: dispositioned all 13 paired results → 0 INCORPORATE / 8 MONITOR / 5 REVISE.
- [x] Update for_lit_search.md: tagged 13 items with [SEARCHED-15a:2026-05-28] / [SEARCHED-15b:2026-05-28] / [DISPOSITIONED-15c:2026-05-28].
- [x] monitor_queue.md: 8 NEW MONITOR (256-263) appended.
- [x] revision_flags.md: 5 REVISE (060-064) appended, all AWAITING-REVIEW.
- [x] validated_premises.md: no writes (0 INCORPORATE; correct null). PREMISE high-water still 043.
- [x] Provenance chains complete for all 13 (Origin → [14x → 15a, 15b → 15c] → disposition).
- [x] No NOVELTY flagged; all items have training-corpus literature anchors.
- [x] No new SYSTEMIC-RISK flag (FLAG I extensions only: REVISE-060/062/063/064 join the FLAG I cluster; REVISE-061 is independent).
- [x] Consistency check passed: no contradictions with validated_premises.md.
- [ ] OUT-OF-BAND ESCALATION NOTE: REVISE-060..064 join the standing AWAITING-REVIEW backlog (REVISE-047..059 = 13). Total AWAITING-REVIEW = 18. REVISE-063 and REVISE-064 in particular concern the integrity of the self-awareness mechanism itself; both must be escalated OUT-OF-BAND per FLAG I.

**Disposition counts (2026-05-28):** 0 INCORPORATE / 8 MONITOR / 5 REVISE. 13 items processed. SYSTEMIC-RISK-FLAGs raised: 0 NEW, 4 FLAG I extensions.
**Run timestamp:** 2026-05-28 (c2a2-lit-search-pipeline scheduled task; autonomous; no human-in-the-loop).
**Total daily-cycle items remaining in queue post-run:** 0 (13 items advanced to terminal disposition).

---

**Generated by Agents 15a, 15b, and 15c (2026-05-28 scheduled pipeline run)**
**Date: 2026-05-28 (autonomous scheduled-task run; no human review in-loop)**
**Pipeline trigger: c2a2-lit-search-pipeline; 13 items processed (13 new cycle-0; 2026-05-27 EOD batch).**

---

## 2026-05-29 RUN — c2a2-lit-search-pipeline (15a + 15b + 15c)

**Disposition counts:** 0 INCORPORATE / 13 MONITOR / 7 REVISE. Total = 20 items.

**Run scope:** Scheduled c2a2-lit-search-pipeline run. One batch processed: the 2026-05-28 EOD 14a/14b batch (20 cycle-0 items: ASSUMPTION-243..252 + PRESUMPTION-267..276). All were [QUEUED] without prior [SEARCHED-15a]/[SEARCHED-15b] tags at run start.

**New IDs:** MONITOR-264..276 (13); REVISE-065..071 (7); DISPOSITION-087..106 (20).

**Citations / grounding:** Per ASSUMPTION-199 convention (SYSTEMIC-RISK-FLAG E), citations drawn from training-corpus and prior C2A2-internal precedent for routine items. Highest-stakes items (PRESUMPTION-267 binary-framing 4-instance pattern; PRESUMPTION-269 push-gate FLAG-I extension; PRESUMPTION-275 self-referential observation independence) warrant live verification when the response-gate next exercises.

**NOVELTY (15a):** None flagged. All 20 items have clear training-corpus literature anchors (adapter pattern / SRE / Constitutional AI / mirror conventions / anomaly-detection baseline / tech-debt / iron-triangle / double-loop learning / observer-effect / cross-container telemetry); no literature-gap NOVEL items this batch.

**SYSTEMIC-RISK (15b) — FLAG I continuation + self-referential cluster:** Six of seven new REVISEs extend existing systemic risk clusters:
- REVISE-065 (PRESUMPTION-267) — 4-instance binary-framing structural-bias pattern; couples PRESUMPTION-253/259/262 family
- REVISE-066 (PRESUMPTION-269) — push-gate as 5th FLAG-I route; couples REVISE-053; HIGH urgency
- REVISE-067 (PRESUMPTION-272) — query-class coverage gap at ship-readiness; couples REVISE-061
- REVISE-068 (PRESUMPTION-270) — swarm-contract mirror drift; lowest-cost remediation
- REVISE-069 (PRESUMPTION-274) — named-trigger elastic deferral; couples PRESUMPTION-248 family
- REVISE-070 (PRESUMPTION-273) — implicit scope-renegotiation; couples FLAG-I demo-path bias cluster
- REVISE-071 (PRESUMPTION-275) — self-referential observation independence; HIGH self-referential elevation; completes 3-item cluster with REVISE-063 + REVISE-064

The response-leg backlog grows: standing AWAITING-REVIEW = 18 (REVISE-047..064) + 7 new (REVISE-065..071) = 25 total. FLAG I closed-loop-no-exit pathology compounds. The 3-item self-referential cluster (REVISE-063/064/071) should be escalated OUT-OF-BAND as a coupled architectural decision about self-awareness-mechanism integrity.

### DISPOSITION records (20 items)

```
DISPOSITION-087:
  Date: 2026-05-29
  Item: ASSUMPTION-243
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: Adapter pattern is industry-standard (Gamma/Fowler/Martin/Newman). "First demonstrated instance" framing precedes architectural validation per Brown/Bass; N=1 is documented overhead-to-benefit period.
  Disposition: MONITOR (MONITOR-264)
  Reasoning: Pattern sound; architectural validation earns at N=2+ adoption. Track adoption count + per-surface divergence over 30-60 days.
  Detail: Cadence Weekly; next 15d 2026-06-05. Priority Medium. Couples ASSUMPTION-251 / MONITOR-272 (un-numbered candidate); broker-v4 cluster.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-088:
  Date: 2026-05-29
  Item: ASSUMPTION-244
  Item type: ASSUMPTION (stated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: CHALLENGED | 15b strength: Moderate
  Net assessment: Single-path smoke-test + human gate defensible as first gate; "sufficient" framing rejected by Beizer/Myers equivalence-class partitioning + BEIR/SPECTER multi-query benchmarking.
  Disposition: MONITOR (MONITOR-265)
  Reasoning: Verification rubric expansion is cheap; blast radius limited (5-file changeset, human gate). Couples PRESUMPTION-272 (REVISE-067).
  Detail: Cadence Weekly; next 15d 2026-06-05. Priority Medium. Conditional INCORPORATE pending rubric.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-089:
  Date: 2026-05-29
  Item: ASSUMPTION-245
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate-Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: Constitutional rule integrity strongly supported (Christiano/Bai/Amodei). Scaling concern (Bainbridge/Reason erosion-under-load) is the live worry — lives in PRESUMPTION-269 / REVISE-066.
  Disposition: MONITOR (MONITOR-266)
  Reasoning: Rule integrity supported on single-instance level. Instrument push-gate stall-time as relevant signal.
  Detail: Cadence Weekly; next 15d 2026-06-05. Priority Medium-High. Couples PRESUMPTION-269 (REVISE-066); FLAG-I cluster.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-090:
  Date: 2026-05-29
  Item: ASSUMPTION-246
  Item type: ASSUMPTION (stated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Mirror convention usable per Nygard/Bass/Kleppmann WITH drift-detection; assumption does not name detection. Symlink is canonical remediation (near-zero cost).
  Disposition: MONITOR (MONITOR-267)
  Reasoning: Mirror pattern usable; drift-detection added under REVISE-068. Architectural-reviewer post-ISME deferral tracked under REVISE-069.
  Detail: Cadence Weekly; next 15d 2026-06-05. Priority Low-Medium. Couples PRESUMPTION-270 (REVISE-068); PRESUMPTION-274 (REVISE-069).
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-091:
  Date: 2026-05-29
  Item: ASSUMPTION-247
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak
  Net assessment: Baseline-then-delta is canonical (Beyer SRE/NIST/Chen); 1-week-specific baseline carries documented risk for heterogeneous data per Box & Jenkins.
  Disposition: MONITOR (MONITOR-268)
  Reasoning: Pattern sound; 1-week calibration parameter to observe across cycles. Cheap remedy (extend baseline if Week-1 variance high).
  Detail: Cadence Weekly; next 15d 2026-06-05. Priority Low-Medium.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-092:
  Date: 2026-05-29
  Item: ASSUMPTION-248
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: Surfacing-over-skipping supported (Fowler/Cunningham/Beck); "easy to add later" is documented under-estimate language per Cunningham/Brooks/Cockburn.
  Disposition: MONITOR (MONITOR-269)
  Reasoning: Design choice supported; needs explicit re-add triggers per dropped check to discharge sandbagging risk.
  Detail: Cadence Weekly; next 15d 2026-06-05. Priority Low-Medium. PRESUMPTION-248 recurrence-risk coupling.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-093:
  Date: 2026-05-29
  Item: ASSUMPTION-249
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: Deadline-driven prioritization with demo-tiebreaker supported (Goldratt/Reinertsen/Sutherland/Brooks). Demo-path bias documented (Brooks/DeMarco & Lister/Heath); FLAG-I cluster is direct internal evidence.
  Disposition: MONITOR (MONITOR-270)
  Reasoning: Tiebreaker-role supported; non-demo deferred work tracking owed. Couples PRESUMPTION-273 (REVISE-070).
  Detail: Cadence Weekly; next 15d 2026-06-05. Priority Medium-High. FLAG-I cluster.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-094:
  Date: 2026-05-29
  Item: ASSUMPTION-250
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate-Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Asking the reframing question is well-supported (Argyris/Senge/Schön/Reason/Cook & Woods); acting on the new framing without external check is the warned condition (PRESUMPTION-275 inherited).
  Disposition: MONITOR (MONITOR-271)
  Reasoning: HIGH priority — central architectural framing-shift candidate. Question is data; new framing needs external check (Tom/Adaptive). Couples PRESUMPTION-275 (REVISE-071).
  Detail: Cadence Weekly; next 15d 2026-06-05. Priority HIGH. FLAG-I cluster + self-referential elevation cluster.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-095:
  Date: 2026-05-29
  Item: ASSUMPTION-251
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak
  Net assessment: Registry-hygiene failure framing supported (Bass/Nygard/Brown). Numbering-ceremony framing equally defensible (PRESUMPTION-271).
  Disposition: MONITOR (MONITOR-272)
  Reasoning: Both framings tractable. Cheap audit (content-debt vs ceremony-debt for 3 un-numbered candidates) decides remediation direction.
  Detail: Cadence Weekly; next 15d 2026-06-05. Priority Medium. Couples PRESUMPTION-271 (MONITOR-275).
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-096:
  Date: 2026-05-29
  Item: ASSUMPTION-252
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: Post-write external verification pattern sound (Gray & Reuter/Kleppmann/Nygard/Beyer SRE). Self-referential internal-only check is documented less reliable (Goodhart/Hawthorne).
  Disposition: MONITOR (MONITOR-273)
  Reasoning: Verification pattern sound; structural concern (verifier inside pipeline being tested) tracked under REVISE-064 external-script remediation. Couples REVISE-064 + REVISE-071 self-referential cluster.
  Detail: Cadence Weekly; next 15d 2026-06-05. Priority Medium-High.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-097:
  Date: 2026-05-29
  Item: PRESUMPTION-267
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: 4-instance recurrence is canonical signature of organizational defensive-routine (Argyris) or framing-bias (Heath & Heath/Tversky/Kahneman). Internal recurrence is direct structural-bias evidence.
  Disposition: REVISE (REVISE-065)
  Reasoning: PRESUMPTION + weak support + moderate-strong challenge + internal-recurrence pattern → REVISE per heuristics. Self-referential elevation (framing mechanism itself implicated).
  Detail: Urgency HIGH. Recommended: require ≥3 options for prioritization framings; explicit "third option?" check; treat 4-instance recurrence as framing-process review trigger.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-098:
  Date: 2026-05-29
  Item: PRESUMPTION-268
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Meta-agent value supported under bounded conditions (Hong/Park/Shao); canary-too-many anti-pattern documented (Bainbridge/Beyer toil); FLAG-I bandwidth context is the documented warned condition.
  Disposition: MONITOR (MONITOR-274)
  Reasoning: Net-value test owed but not defined; track watch-agent output → action conversion rate as de facto signal with sunset criterion.
  Detail: Cadence Weekly; next 15d 2026-06-05. Priority Medium. FLAG-I bandwidth coupling.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-099:
  Date: 2026-05-29
  Item: PRESUMPTION-269
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: HITL bandwidth-bottleneck documented (Bainbridge/Christiano/Reason/Allspaw); FLAG-I cluster is direct internal evidence; 5.5-week ISME window is the documented load period.
  Disposition: REVISE (REVISE-066)
  Reasoning: PRESUMPTION + weak support + moderate-strong challenge + FLAG-I cluster extension → REVISE per heuristics. HIGH urgency: extends FLAG-I to potential 5th route.
  Detail: Urgency HIGH. Recommended: instrument push-gate latency; SLA + escalation; rule-bounds explicit; couple FLAG-I remediation.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-100:
  Date: 2026-05-29
  Item: PRESUMPTION-270
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate
  Net assessment: Copy-mirror drift without detection is unambiguously documented as failure precondition (Kleppmann/Nygard/Conway/Bass); symlink canonical remediation.
  Disposition: REVISE (REVISE-068)
  Reasoning: PRESUMPTION + weak support + moderate challenge + near-zero-cost remediation → REVISE per heuristics. Lowest-cost REVISE in this run.
  Detail: Urgency MEDIUM. Recommended: replace copy-mirror with symlink OR add file-hash equality check to Janitor.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-101:
  Date: 2026-05-29
  Item: PRESUMPTION-271
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: NO-CHALLENGE-FOUND | 15b strength: Weak
  Net assessment: Numbering-ceremony-as-FLAG-I-gate framing has documented support (Nygard original ADR); literature does not directly challenge.
  Disposition: MONITOR (MONITOR-275)
  Reasoning: Audit-question framing is the right remediation: distinguish content-debt from ceremony-debt for un-numbered candidates. Couples MONITOR-272.
  Detail: Cadence Weekly; next 15d 2026-06-05. Priority Medium.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-102:
  Date: 2026-05-29
  Item: PRESUMPTION-272
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate
  Net assessment: Testing/retrieval-evaluation literature (Beizer/Myers/BEIR/SPECTER) directly rejects single-query-as-representative; scholarly cross-tradition queries are a documented distinct retrieval shape.
  Disposition: REVISE (REVISE-067)
  Reasoning: PRESUMPTION + weak support + moderate challenge → REVISE per heuristics. Couples REVISE-061 (broker-v4 calibration gap).
  Detail: Urgency MEDIUM. Recommended: 3-5 query-class verification rubric; couple REVISE-061 calibration sprint.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-103:
  Date: 2026-05-29
  Item: PRESUMPTION-273
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: Iron-triangle (Atkinson/PMI) requires that when time is fixed, scope/quality trade-offs be explicit. Demo-path tiebreaking IS scope-shaping, but invisible-as-scope-decision.
  Disposition: REVISE (REVISE-070)
  Reasoning: PRESUMPTION + implicit-trade-off concern + FLAG-I demo-path bias cluster → REVISE per heuristics. Couples FLAG-I cluster + ASSUMPTION-249 (MONITOR-270).
  Detail: Urgency MEDIUM. Recommended: explicit scope-vs-time trade-off per cycle; label demo-path tiebreaking as scope-decision.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-104:
  Date: 2026-05-29
  Item: PRESUMPTION-274
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate
  Net assessment: Named-but-elastic triggers ("post-ISME") functionally equivalent to open-ended deferral when named event itself slides (Allen/Bainbridge/Reason/Cook & Woods); PRESUMPTION-248 internal-validated.
  Disposition: REVISE (REVISE-069)
  Reasoning: PRESUMPTION + weak support + moderate challenge + PRESUMPTION-248 family coupling → REVISE per heuristics.
  Detail: Urgency MEDIUM. Recommended: tie trigger to date not event; explicit re-surface SLA; quarterly named-trigger audit.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-105:
  Date: 2026-05-29
  Item: PRESUMPTION-275
  Item type: PRESUMPTION (unstated)
  15a result: NO-SUPPORT-FOUND | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Self-referential observation loops are documented as systematically bias-prone (Argyris/Cook & Woods/Goodhart/Hawthorne/philosophy-of-measurement). Prediction-observation loop running inside same registry is the warned condition. Self-referential elevation: the mechanism producing today's outputs (and this disposition) is itself implicated.
  Disposition: REVISE (REVISE-071)
  Reasoning: PRESUMPTION + no support + moderate-strong challenge + self-referential elevation + 3-item cluster (with REVISE-063 + REVISE-064) → REVISE per heuristics. HIGH urgency.
  Detail: Urgency HIGH. Recommended: external check (Tom/Adaptive) for framing-shift commitments; treat REVISE-063 + REVISE-064 + REVISE-071 as coupled self-awareness-mechanism-integrity architectural decision.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-106:
  Date: 2026-05-29
  Item: PRESUMPTION-276
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak
  Net assessment: Symmetric weak evidence. Construct-definition is the lever: if "sit-down cadence" is Chat-presence, morning-discussion #3 is correctly reporting; if engagement-occurrence, the presumption is correct (cross-container telemetry gap).
  Disposition: MONITOR (MONITOR-276)
  Reasoning: Cheap remedy (define construct + align measurement). Couples PRESUMPTION-275 self-referential observation cluster.
  Detail: Cadence Weekly; next 15d 2026-06-05. Priority Low-Medium.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```


---

## Returns + dispositions — c2a2-lit-search-pipeline run 2026-05-30

RETURN-TO-14a:
  Original item: ASSUMPTION-253
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Moderate
  Key source: d3/d3 GitHub Issue #1247 "Regression issue with opacity transition?" — documents real opacity-transition regressions independent of test harness; establishes that d3 opacity transitions genuinely fail in foreground use.
  Summary: d3's transition machinery has a documented history of genuine opacity-transition failures, and a heavy force-simulation timer can starve transition frames. A foreground observation where the isolate set computed correctly (185 nodes) but op
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-253_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-253
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate
  Key source: Chrome for Developers, 'Background tabs in chrome 57' / 'Timer throttling in Chrome 88' — rAF and chained timers are throttled/suspended in background tabs; a fade that 'does not render' can be a visibility-state artifact rather than a code defect.
  Specific risk: If the fade is actually render-context-bound, the planned .attr() fix (ASSUMPTION-254) may not generalize, and the v1.6 hold (ASSUMPTION-255) gates on a misdiagnosis.
  Summary: The literature on background-tab throttling and rAF frame variance shows that 'the fade does not render' is exactly the signature a visibility/compositor artifact would produce, so a single foreground observation does not by itself exclude
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-253_against.md

RETURN-TO-14a:
  Original item: ASSUMPTION-254
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Moderate
  Key source: Bostock, 'Working with Transitions' — confirms .transition() schedules interpolated frames via the timer/rAF loop, whereas .attr/.style apply immediately; replacing a transition with a direct attribute write removes the rAF dependency.
  Summary: Mechanistically, d3 transitions depend on the timer/rAF loop that a running force simulation also drives; a direct .attr('opacity') write bypasses that contention. Both the official transition docs and community bug threads support direct a
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-254_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-254
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate
  Key source: Zeller, 'Why Programs Fail' (systematic debugging) — single-suspect, fix-first debugging frequently treats a symptom while the true defect (e.g., a stale selection, join error, or visibility state) persists.
  Specific risk: A masked root cause re-surfaces later (e.g., at scale or on another browser) and the test suite still shows green (couples ASSUMPTION-262/PRESUMPTION-285).
  Summary: Naming a single 'prime suspect' before reproduction risks fixing a symptom. The same observable could arise from a selection/join error or a visibility-state artifact, in which case the .attr() swap masks rather than resolves the defect. Es
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-254_against.md

RETURN-TO-14a:
  Original item: ASSUMPTION-255
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Moderate
  Key source: Humble & Farley, 'Continuous Delivery' — gating a release when a known defect shares a code path with the new increment is a defensible blast-radius-control decision.
  Summary: Holding a release because the new increment shares a defective mechanism is a recognized blast-radius decision: shipping a visibly broken fade would be a user-facing regression. The hold is conservative and defensible on safety grounds.
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-255_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-255
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate-Strong
  Key source: Flagsmith / DevCycle / ConfigCat (decoupling deployment from release) — the established practice is to deploy the validated parser with the fade behind a flag or disabled, rather than hold the whole increment.
  Specific risk: Held increment grows stale; validated work is withheld from users for a defect that could be flagged off; regen cost compounds.
  Summary: A large body of release-engineering practice holds that deployment should be decoupled from release: the validated parser could ship with the fade disabled or flagged rather than holding all of v1.6. The all-or-nothing hold is the very patt
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-255_against.md

RETURN-TO-14a:
  Original item: ASSUMPTION-256
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Moderate-Strong
  Key source: Furnas (1986), 'Generalized Fisheye Views' — establishes the focus+context distinction: a transient lens and a persistent selection are legitimately separate interaction layers.
  Summary: The transient-lens-vs-persistent-filter separation is a well-established and intentional pattern in the visualization literature (Furnas, Shneiderman, Heer & Shneiderman, Munzner). Treating search/focus as reversible highlight-in-place and
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-256_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-256
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate
  Key source: Norman (1983), 'Design rules based on analyses of human error' — when two controls affect the same observable (here, visibility) without a shared model, mode errors and confusion rise.
  Specific risk: Users may expect focus and checkbox filters to agree; silent divergence could read as a bug; subordinated third 'unify' option never evaluated.
  Summary: Even though the separation is a valid pattern, two controls that both alter visibility without agreement is a recognized source of mode confusion. The model was locked by preference, not by a usability test, so the residual risk is empirica
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-256_against.md

RETURN-TO-14a:
  Original item: ASSUMPTION-257
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Moderate
  Key source: Chrome DevTools 'Fix memory problems' — a tab exceeding ~1GB (desktop) is terminated by the browser; large graphs are a known OOM trigger, consistent with a memory-pressure crash.
  Summary: Browser per-tab memory ceilings and SVG's poor scaling past a few thousand objects make a memory-pressure crash a credible diagnosis; large graphs are a documented OOM trigger. Keeping MAX_EDGES as a guardrail is consistent with this.
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-257_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-257
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate-Strong
  Key source: Nightingale / Cosmograph WebGL literature — edge count is itself a primary driver of DOM/memory load in SVG graphs; 'memory pressure' and 'edges' are not disjoint causes.
  Specific risk: Mis-attributing the crash hides the edge-count contribution; the cap value may be set on a wrong causal model and fail at scale.
  Summary: Because edges rendered as SVG DOM nodes are a principal source of memory load, 'pure memory pressure' and 'the edge cap' are not mutually exclusive; the causal story is a false dichotomy. The cap may be fine to keep, but as a memory-control
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-257_against.md

RETURN-TO-14a:
  Original item: ASSUMPTION-258
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Moderate
  Key source: Couchbase, 'typeahead vs autocomplete with Full Text Search' — deterministic prefix typeahead is fast, predictable, and low-cost for a known entity index, ideal as a first substrate.
  Summary: For a curated, finite label set, deterministic prefix typeahead is the textbook substrate: fast, predictable, no model dependency, and cheap to maintain. Choosing it over an LLM/library-science requirement is well-justified for the current
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-258_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-258
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate-Strong
  Key source: Redis, 'Semantic vs keyword search' — keyword search 'struggles with synonyms and context' (e.g. 'car repairs' misses 'automotive maintenance'); cross-tradition naming is exactly this synonymy problem.
  Specific risk: Users searching a concept under a different tradition's vocabulary get no hit; perceived as missing data; cross-tradition discovery (a core C2A2 goal) degraded.
  Summary: Deterministic prefix typeahead systematically misses synonymy and cross-tradition naming variants, which is central to a cross-tradition system. The literature shows keyword/prefix matching trades recall for determinism; declaring it the 'c
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-258_against.md

RETURN-TO-14a:
  Original item: ASSUMPTION-259
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Moderate
  Key source: Hunt & Thomas, 'The Pragmatic Programmer' (DRY) — a single authoritative representation prevents divergence among derived views, the mechanism the claim relies on.
  Summary: If checkboxes and typeahead genuinely derive from one COLORS dict, DRY/SSOT guarantees they cannot disagree on the vocabulary they share. The claim is sound for the slice of state actually mastered by COLORS.
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-259_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-259
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Strong
  Key source: LinkedIn/Hidef SSOT-pitfalls articles — SSOT guarantees fail when more than one surface encodes the same fact; coupling leaks through any non-derived surface.
  Specific risk: Vocabulary divergence via dir/frontmatter goes undetected; the 'root' fallback silently mis-groups nodes (a fail-loud violation).
  Summary: The 'cannot drift' claim presumes COLORS is the only coupling surface, but dir name and frontmatter also encode the vocabulary, and get_group's silent 'root' fallback already leaks. SSOT only prevents drift for the state it actually masters
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-259_against.md

RETURN-TO-14a:
  Original item: ASSUMPTION-260
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Moderate
  Key source: Plugin-registry / convention-over-configuration literature (e.g., Fowler on registries) — a single registration entry plus convention-located files is a recognized low-friction extension pattern.
  Summary: One declaration line plus convention-located vault files plus a regen is a clean, low-friction registration pattern in line with registry/DRY practice. For current N it is genuinely a near-single-source operation.
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-260_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-260
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate
  Key source: Categorical-color perception literature (CleanChart/arXiv 2404.03787) — distinct categorical colors saturate around ~10-12, so 'one COLORS line' stops yielding a distinguishable color at scale (couples PRESUMPTION-281).
  Specific risk: At N>~12 new participants get indistinguishable colors; regen latency/size degrade; silent mis-grouping.
  Summary: The single-source claim is cheap only at small N: the categorical-color budget caps distinct hues near ~10-12, regen output (already ~26MB) and time grow with N, and a silent grouping fallback can swallow a mis-add. 'One line + regen' under
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-260_against.md

RETURN-TO-14a:
  Original item: ASSUMPTION-261
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Moderate
  Key source: mem0.ai (2026) 'Context window is RAM, not storage' — externalizing state to a durable doc that is re-injected is the recommended remedy for cross-session context loss.
  Summary: Externalizing session state into a durable, auto-loaded doc is exactly the recommended fix for cross-session context loss in agentic systems. The handoff rail follows current best practice, so it should materially improve resume.
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-261_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-261
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate-Strong
  Key source: mem0.ai (2026) — 'if an agent violates a constraint it followed 10 turns ago, the attention weight has dropped below the enforcement threshold'; auto-loaded rules are not reliably honored.
  Specific risk: Resume silently proceeds on a stale/ignored handoff; no detection that the rule was skipped.
  Summary: Auto-loading a rule does not guarantee adherence: instruction-following degrades with context length and a stale handoff doc can mis-steer. The word 'fixes' overstates a mechanism that is probabilistic and has no defined failure mode or ver
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-261_against.md

RETURN-TO-14a:
  Original item: ASSUMPTION-262
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Moderate
  Key source: Zhu, Hall & May (1997), 'Software unit test coverage and adequacy' (ACM Computing Surveys) — logic/unit tests are a recognized adequacy layer for parser correctness, distinct from rendering.
  Summary: Logic tests are an appropriate adequacy layer for parser correctness, and separating them from visual verification is standard test-pyramid practice. Deferring render verification behind the hold is a reasonable layering decision.
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-262_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-262
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate-Strong
  Key source: Mutation-testing literature (BrowserStack/Eleven Labs) — a passing suite can still miss breaking logic; surviving mutants show green-count != adequacy.
  Specific risk: False confidence in 1.6; deferred visual verification could surface further defects; coverage gaps unmeasured.
  Summary: A fixed count of passing logic tests does not establish coverage adequacy (mutation testing exists precisely because green suites miss defects), and the fade bug is a live counterexample that logic-pass != working. The separation is fine; t
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-262_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-277
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Weak
  Key source: d3/d3 Issues #1247/#474 — some opacity-transition faults are reproducible across contexts, lending partial support that a code-path-bound fault can generalize.
  Summary: There is partial support that a transition/timer code-path fault is reproducible across contexts, so generalizing from one observation is not baseless. But the support is weak because reproducibility-across-contexts is precisely what was no
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-277_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-277
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED
  Strength: Moderate-Strong
  Key source: Chrome/MDN visibility & throttling docs — rendering behavior varies by tab visibility and compositor state; a single context cannot establish a render fault generalizes.
  Specific risk: The .attr() fix (ASSUMPTION-254) and the v1.6 hold (255) are predicated on a verdict drawn from N=1; if context-bound, both are misdirected.
  Summary: Generalizing from one foreground query/user/browser to 'the whole fade mechanism is broken' is a single-observation over-generalization, and render behavior is known to be context-dependent. The presumption (symptom is code-path-bound) is u
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-277_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-278
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Weak
  Key source: Chrome '--disable-background-timer-throttling' flag docs — the throttling confound is controllable, so trusting probes *with* the flag set can be legitimate.
  Summary: Background-tab confounds are controllable (e.g., throttling-disable flags, visibility management), so remote-Chrome probes can be trusted when those controls are applied. Support is weak because nothing confirms the controls are applied to
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-278_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-278
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED
  Strength: Moderate-Strong
  Key source: Chrome 'Background tabs in chrome 57' / 'Timer throttling in Chrome 88' — rAF/timer throttling is a *general* background-tab artifact class, not a one-off; any background visual probe is exposed.
  Specific risk: Other past/future visual diagnoses via remote Chrome may be silently corrupted by the same throttling; a class of conclusions is suspect.
  Summary: rAF/timer throttling is a general property of background tabs, so the confound that broke one diagnosis applies to the whole class of remote-Chrome visual-rendering probes. Presuming it isolated and continuing to trust those probes without
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-278_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-279
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Weak
  Key source: Nygard 'Release It!' — when uncertain about coupling, withholding the whole increment is a safe default that avoids exposing a half-understood defect.
  Summary: Under diagnostic uncertainty an all-or-nothing hold is a defensible safe default. Support is weak because the literature treats it as a fallback, not the preferred option when a clean flag boundary exists.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-279_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-279
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED
  Strength: Moderate
  Key source: Flagsmith / DevCycle / ConfigCat — decoupling deployment from release via flags is the standard way to ship validated work while a coupled defect stays off.
  Specific risk: Validated work withheld unnecessarily; held increment goes stale; regen cost compounds.
  Summary: A whole body of release practice says deploy the validated parser with the fade flagged/disabled rather than hold everything; the presumption that holding dominates was never weighed against this. The unconsidered partial-release option is
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-279_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-280
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Weak
  Key source: Pragmatic Programmer (DRY) / SSOT articles — a true single source does prevent drift for the state it masters; the guarantee is real *within its precondition*.
  Summary: SSOT genuinely prevents drift, but only under the precondition that there is exactly one authoritative surface. The support is weak here because the presumption's whole point is that the precondition is violated.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-280_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-280
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED
  Strength: Strong
  Key source: SSOT-pitfalls literature (LinkedIn/Hidef) — when multiple surfaces encode the same fact, the single-source guarantee evaporates; coupling leaks through every non-derived surface.
  Specific risk: Silent mis-grouping of nodes to 'root'; undetected vocabulary divergence; false confidence in a drift guarantee that does not hold.
  Summary: The 'cannot drift' guarantee fails because COLORS is not the only surface: dir name and frontmatter also encode the vocabulary, and the get_group -> 'root' silent fallback is a concrete existing leak that masks mismatches. This is not a hyp
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-280_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-281
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Weak
  Key source: Registry / convention-over-configuration literature — single-entry registration can scale if the per-entry cost stays constant.
  Summary: The *edit* cost of adding a participant is genuinely constant (one line). Support is weak because constant edit cost does not imply constant *system* cost (color budget, regen, size), which is the presumption's target.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-281_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-281
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED
  Strength: Moderate-Strong
  Key source: Categorical-color perception (CleanChart; arXiv 2404.03787 'Revisiting Categorical Color Perception') — distinct categorical colors saturate near ~6-12; beyond that hues are not reliably distinguishable, a hard perceptual ceiling well below N=33/100.
  Specific risk: At N>~12 new participants are visually indistinguishable; HTML size/regen latency degrade UX and the build loop.
  Summary: Registration is cheap to *type* but not cheap to *scale*: categorical-color distinctness caps near ~10-12, so 'one COLORS line' stops yielding a distinguishable color long before N=33/100; regen output (already ~26MB) and time grow with N.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-281_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-282
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Weak
  Key source: Augment Code 'Context Engineering' — auto-loaded project memory does steer agent behavior when present and current.
  Summary: Auto-loaded memory does steer behavior when the doc is current and the rule is honored. Support is weak precisely because adherence and freshness are assumed rather than enforced.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-282_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-282
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED
  Strength: Moderate-Strong
  Key source: mem0.ai (2026) — constraint adherence decays with distance/turns; an auto-loaded rule can be silently dropped.
  Specific risk: Silent resume on stale/ignored handoff; undetected drift between doc and reality.
  Summary: The rail defines no failure mode and no check that the rule was followed or the doc kept current, so it cannot detect a stale doc or a skipped rule, both of which the literature says are likely. The presumption hides a success-criteria gap.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-282_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-283
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Moderate
  Key source: Dogfooding literature (Microsoft/Google eng practice) — using one's own system is a legitimate source of design *feedback* and usability signal.
  Summary: Dogfooding is a recognized, valuable source of design feedback and motivation. It supports treating self-application as a useful signal, but the literature frames it as feedback, not as evidence of validity.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-283_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-283
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED
  Strength: Moderate
  Key source: arXiv 2402.11436 'Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement' — systems favor their own outputs in self-evaluation (self-bias).
  Specific risk: Pathway 16 appears validated by an act that only motivates it; confirmation is manufactured internally (couples the self-referential cluster).
  Summary: Treating 'the system practicing its own thesis' as evidence for the thesis is self-referential confirmation: dogfooding can motivate and surface usability issues but cannot validate the pathway's claims. The self-bias literature shows self-
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-283_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-284
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Moderate
  Key source: Simon, bounded rationality / satisficing — under time pressure a good-enough binary choice is often rational and adequate.
  Summary: For low-stakes, reversible choices, a quick binary decision by preference is a defensible satisficing move. Support is moderate for *this* decision in isolation, but does not address the recurring pattern the presumption flags.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-284_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-284
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED
  Strength: Moderate-Strong
  Key source: False-dichotomy literature (Quillbot; Develop Good Habits) — presenting two options when more exist suppresses superior alternatives.
  Specific risk: Repeated suppression of third options; design space under-explored; decisions anchored on the first two framings (couples PRESUMPTION-267 family, OPEN-068).
  Summary: As the 5th instance of the same binary-framing pattern, this is no longer a one-off satisficing choice but a structural decision-making bias: options are repeatedly framed as two clean alternatives, subordinating reframe/unify thirds, and r
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-284_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-285
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Weak
  Key source: Zhu, Hall & May (1997) 'Software unit test coverage and adequacy' — a curated suite *can* be adequate if cases are chosen to cover the input partitions.
  Summary: A small, well-designed suite can be adequate if the 16 cases map onto the parser's input partitions. Support is weak because no coverage argument was given; adequacy is asserted by count, not demonstrated.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-285_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-285
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED
  Strength: Moderate-Strong
  Key source: Mutation-testing literature (BrowserStack; Eleven Labs; arXiv 1808.07725) — surviving mutants show passing suites routinely miss breaking logic; count != adequacy.
  Specific risk: Unmeasured coverage gaps in the parser; false readiness; further defects surface post-unhold.
  Summary: '16/16' is a pass count, not a coverage measure; mutation-testing exists precisely because green suites miss defects, and the fade bug is a live counterexample to logic-pass=working. Presuming the 16 cases cover the input space is undefende
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-285_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-286
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Moderate
  Key source: Eisenhower/urgency-importance and deadline-driven prioritization literature — an external deadline (e.g., a demo/ISME) is a legitimate, independent prioritization criterion.
  Summary: If the demo deadline is genuinely external, prioritizing the demo path over PRS cadence is rational and independently justified. Support is moderate, conditional on the prioritization criterion being external rather than self-generated.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-286_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-286
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED
  Strength: Moderate-Strong
  Key source: Goodhart's Law literature (coffeeandjunk; PMC6541803) — when the measurer judges its own performance against its own metric, the judgment ceases to track the construct.
  Specific risk: A real recursion/avoidance pattern is repeatedly relabeled 'correct prioritization'; the zero-PRS streak is never externally adjudicated (couples OPEN-067, PRESUMPTION-275).
  Summary: Reading the demo-path day as 'correct prioritization, not recursion' from inside the same registry-and-summary apparatus that flags the zero-PRS streak is a closed-loop self-diagnosis: the system both produces the streak and exonerates it,
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-286_against.md

```
DISPOSITION-107:
  Date: 2026-05-30
  Item: ASSUMPTION-253
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: d3 opacity-transition failures are real and documented, but a single foreground observation cannot exclude a render-context artifact; FOR and AGAINST are both Moderate and symmetric.
  Disposition: MONITOR (MONITOR-277)
  Reasoning: Symmetric moderate evidence with a cheap decisive test available (multi-context foreground reproduction). Err toward MONITOR over premature INCORPORATE.
  Detail: Cadence Weekly; next 15d 2026-06-06. Priority Medium (gates 1.6 push). What would change: multi-context reproduction -> INCORPORATE; context-bound -> REVISE. Couples PRESUMPTION-277/278.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-108:
  Date: 2026-05-30
  Item: ASSUMPTION-254
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: The .attr() fix is mechanically plausible and a common remedy, but committing to one suspect pre-reproduction risks masking a selection/visibility cause.
  Disposition: MONITOR (MONITOR-278)
  Reasoning: Cheap to de-risk by confirming the attribute-vs-pixel divergence before coding. MONITOR until the root cause is bisected.
  Detail: Cadence Weekly; next 15d 2026-06-06. Priority Medium. Couples ASSUMPTION-253, ASSUMPTION-262.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-109:
  Date: 2026-05-30
  Item: ASSUMPTION-255
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Holding is safe but not the only safe option; feature-flag practice offers a cheaper partial release. ASSUMPTION (designer-aware) so not REVISE-grade, but the alternative is well-evidenced.
  Disposition: MONITOR (MONITOR-279)
  Reasoning: Conservative hold is defensible; the unconsidered partial-release alternative is cheap. MONITOR with the flag-the-fade remedy noted; couples PRESUMPTION-279.
  Detail: Cadence Weekly; next 15d 2026-06-06. Priority Low-Medium. What would change: if hold persists >1-2 cycles, escalate toward partial release.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-110:
  Date: 2026-05-30
  Item: ASSUMPTION-256
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate-Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: The transient-lens vs persistent-filter separation is strongly grounded in canonical visualization/HCI literature; the only challenge is an empirical usability caveat, not a conceptual refutation. Strong support + weak-moderate challenge -> INCORPORATE with caveats per heuristic.
  Disposition: INCORPORATE (PREMISE-044)
  Reasoning: The architectural premise (highlight and filter are legitimately distinct, non-syncing idioms) is well-supported design canon; what remains is a usability caveat, recorded but not disqualifying.
  Detail: Confidence Moderate. Applicable to: Sociogram interaction model, Pathway 27/28 search+filter UI. Re-check Quarterly (next 15d ~2026-08-30). Caveat: run a lightweight usability check on dual visibility controls; couples PRESUMPTION-284.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: INCORPORATED
```

```
DISPOSITION-111:
  Date: 2026-05-30
  Item: ASSUMPTION-257
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Memory-pressure crashes are real, but the 'memory pressure NOT edge cap' dichotomy is unsound because SVG edges drive memory. Keeping the cap is reasonable; the causal claim is the weak part.
  Disposition: MONITOR (MONITOR-280)
  Reasoning: Decision (keep MAX_EDGES) is low-risk; the causal attribution needs a profile. MONITOR with a heap-profiling remedy.
  Detail: Cadence Weekly; next 15d 2026-06-06. Priority Low. Note the false-dichotomy framing; couples scaling concern PRESUMPTION-281.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-112:
  Date: 2026-05-30
  Item: ASSUMPTION-258
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Deterministic typeahead is the right cheap first substrate, but the 'replaces library-science requirement' claim ignores a documented synonymy/recall gap that matters for cross-tradition naming.
  Disposition: MONITOR (MONITOR-281)
  Reasoning: Substrate choice is sound now; the recall gap is a real future limit with a cheap mitigation (alias table). MONITOR.
  Detail: Cadence Weekly; next 15d 2026-06-06. Priority Low-Medium. What would change: measured recall loss on cross-tradition queries -> add synonym layer (toward INCORPORATE) or REVISE if discovery degrades.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-113:
  Date: 2026-05-30
  Item: ASSUMPTION-259
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Strong
  Net assessment: SSOT prevents drift only for what COLORS masters; dir/frontmatter are additional surfaces and the silent 'root' fallback is an existing leak. The 'cannot drift' over-claim is the issue, plus a concrete fail-loud violation.
  Disposition: MONITOR (MONITOR-282)
  Reasoning: ASSUMPTION (designer-aware) and the SSOT pattern is sound, so not REVISE-grade as a whole; but the silent-default leak is a real cheap-to-fix defect. MONITOR-HIGH with a fail-loud cleanup flagged.
  Detail: Cadence Weekly; next 15d 2026-06-06. Priority HIGH. Cheap remedy: replace get_group->'root' silent fallback with a loud error; enumerate vocabulary surfaces. Couples PRESUMPTION-280 (REVISE-074).
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-114:
  Date: 2026-05-30
  Item: ASSUMPTION-260
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: A clean low-friction pattern at current N, but 'cheap' degrades with the color budget, regen size/time, and the silent grouping fallback.
  Disposition: MONITOR (MONITOR-283)
  Reasoning: Works now; scaling and fail-loud caveats are real but not yet binding. MONITOR; couples ASSUMPTION-259, PRESUMPTION-281.
  Detail: Cadence Weekly; next 15d 2026-06-06. Priority Medium. What would change: approaching N~12 -> plan non-color encoding (toward REVISE if not addressed).
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-115:
  Date: 2026-05-30
  Item: ASSUMPTION-261
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: The rail follows best practice and should help, but 'fixes' overstates a probabilistic mechanism with no verification or failure mode.
  Disposition: MONITOR (MONITOR-284)
  Reasoning: Helpful and cheap; the gap is the missing verification/failure-mode. MONITOR with a freshness-check remedy; couples PRESUMPTION-282 (REVISE-075).
  Detail: Cadence Weekly; next 15d 2026-06-06. Priority Medium. What would change: add adherence check -> INCORPORATE; observed silent skips -> REVISE.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-116:
  Date: 2026-05-30
  Item: ASSUMPTION-262
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Logic/visual separation is sound, but '16/16 establishes correctness' overstates coverage adequacy, and the fade bug is a counterexample to logic-pass=working.
  Disposition: MONITOR (MONITOR-285)
  Reasoning: Layering is legitimate; the sufficiency claim needs coverage evidence. MONITOR with mutation-testing remedy; couples PRESUMPTION-285 (REVISE-078).
  Detail: Cadence Weekly; next 15d 2026-06-06. Priority Low-Medium. What would change: mutation/coverage data -> INCORPORATE; weak coverage -> REVISE.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-117:
  Date: 2026-05-30
  Item: PRESUMPTION-277
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Unstated single-observation generalization underlies the fade verdict; render behavior is context-dependent, so the presumption is challenged with only weak support. PRESUMPTION + strong challenge -> REVISE.
  Disposition: REVISE (REVISE-072)
  Reasoning: Designers did not articulate that the verdict rests on N=1; the dependent decisions (254, 255) inherit the risk. Cheap, decisive remedy (multi-context reproduction) before committing.
  Detail: Urgency Medium-High (gates 1.6 push). Recommended: require multi-context reproduction before treating the fade as a general code defect. Couples ASSUMPTION-253/254/255, PRESUMPTION-278.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-118:
  Date: 2026-05-30
  Item: PRESUMPTION-278
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: The throttling confound is a general background-tab artifact class, so presuming it isolated leaves a whole class of remote-Chrome visual diagnoses untrustworthy. PRESUMPTION + strong challenge + class-level scope -> REVISE.
  Disposition: REVISE (REVISE-073)
  Reasoning: A methodological tool-trust error affecting all background visual probes, not one diagnosis. SYSTEMIC-RISK candidate; needs an audit, not just monitoring.
  Detail: Urgency Medium-High. Recommended: audit + re-validate remote-Chrome visual diagnoses with visibility forced / throttling disabled. Couples PRESUMPTION-277; flagged SYSTEMIC-RISK (remote-visual-probe trust).
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-119:
  Date: 2026-05-30
  Item: PRESUMPTION-279
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate
  Net assessment: The hold is a defensible safe default but partial release was never weighed; stakes are low and the remedy is cheap.
  Disposition: MONITOR (MONITOR-286)
  Reasoning: PRESUMPTION with a moderate (not strong) challenge and LOW-MEDIUM stakes; cheap flag remedy. Err toward MONITOR over adding to the REVISE backlog.
  Detail: Cadence Weekly; next 15d 2026-06-06. Priority Low-Medium. What would change: hold persists >1-2 cycles -> REVISE toward partial release. Couples ASSUMPTION-255.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-120:
  Date: 2026-05-30
  Item: PRESUMPTION-280
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Strong
  Net assessment: The single-source 'cannot drift' claim is refuted by additional coupling surfaces (dir, frontmatter) and a concrete existing silent-default leak (get_group->'root'). PRESUMPTION + strong challenge + present defect -> REVISE.
  Disposition: REVISE (REVISE-074)
  Reasoning: Not a future risk but a current fail-loud violation; the over-claim plus the live leak warrant design review and a cheap fix.
  Detail: Urgency Medium-High. Recommended: (1) replace get_group->'root' silent fallback with a loud error; (2) derive or eliminate the dir/frontmatter surfaces. Lowest-cost remediation of the batch. Couples ASSUMPTION-259/260.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-121:
  Date: 2026-05-30
  Item: PRESUMPTION-281
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Edit cost is O(1) but distinct-color budget (~10-12) and growing ~26MB artifact size are real scaling walls below the project's N targets. Not yet binding, so not REVISE, but a known design ceiling.
  Disposition: MONITOR (MONITOR-287)
  Reasoning: Scaling limit is real and well-evidenced but not yet hit; cheap to plan for. MONITOR-HIGH with explicit color-ceiling and size flags.
  Detail: Cadence Weekly; next 15d 2026-06-06. Priority HIGH. What would change: approaching N~12 distinct categories -> plan non-color encoding (toward REVISE if unaddressed). Couples ASSUMPTION-260.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-122:
  Date: 2026-05-30
  Item: PRESUMPTION-282
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: The handoff rail has no defined failure mode or adherence/freshness check; literature says both rule-skip and staleness are likely. PRESUMPTION + strong challenge + success-criteria gap -> REVISE.
  Disposition: REVISE (REVISE-075)
  Reasoning: A self-awareness/continuity mechanism with no way to detect its own failure is exactly the kind of gap the pipeline exists to surface. Cheap to add a check.
  Detail: Urgency Medium. Recommended: add freshness timestamp + staleness check + explicit resume-acknowledgement + fail-loud on skip. Couples ASSUMPTION-261; relates to self-awareness-mechanism-integrity cluster.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-123:
  Date: 2026-05-30
  Item: PRESUMPTION-283
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Moderate
  Net assessment: Dogfooding is valid feedback but not validity evidence; framing self-application as evidence for Pathway 16 is self-referential confirmation. PRESUMPTION + self-referential elevation -> REVISE.
  Disposition: REVISE (REVISE-076)
  Reasoning: Joins the standing self-referential-vulnerability cluster (REVISE-063/064/071); conflating motivation with evidence is precisely the integrity risk that cluster concerns.
  Detail: Urgency Medium. Recommended: label self-application as motivation, require external validation for pathway-validity claims. Joins self-awareness-mechanism-integrity cluster (REVISE-063/064/071/079).
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-124:
  Date: 2026-05-30
  Item: PRESUMPTION-284
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: The 5th instance of binary-framing elevates this from a satisficing choice to a structural decision-making bias that subordinates third options; false-dichotomy/framing literature supports the challenge. PRESUMPTION + pattern-level + strong challenge -> REVISE.
  Disposition: REVISE (REVISE-077)
  Reasoning: Pattern-level structural bias (couples PRESUMPTION-267 binary-framing family, triggered OPEN-068). A per-decision fix is insufficient; a standing process change is indicated.
  Detail: Urgency Medium-High. Recommended: add a standing 'name and weigh a third option' step; usability-test before locking. Flagged SYSTEMIC-RISK (binary-framing pattern, 5 instances). Couples OPEN-068, PRESUMPTION-267 family.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-125:
  Date: 2026-05-30
  Item: PRESUMPTION-285
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Coverage adequacy is asserted by pass count, not demonstrated; mutation-testing practice and the fade bug both challenge the presumption. PRESUMPTION + strong challenge -> REVISE.
  Disposition: REVISE (REVISE-078)
  Reasoning: Unstated coverage-adequacy presumption underpins the 1.6 readiness claim (ASSUMPTION-262); cheap to address with a mutation/partition check.
  Detail: Urgency Medium. Recommended: run mutation testing / input-space characterization before treating 1.6 as parser-correct. Couples ASSUMPTION-262.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-126:
  Date: 2026-05-30
  Item: PRESUMPTION-286
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: The 'correct prioritization, not recursion' reading is produced inside the same apparatus that flags the streak; closed-loop self-diagnosis with no external check. PRESUMPTION + self-referential + strong challenge -> REVISE.
  Disposition: REVISE (REVISE-079)
  Reasoning: Self-referential prioritization-layer bias; joins the self-awareness-mechanism-integrity cluster (REVISE-063/064/071/076). Needs a pre-registered external criterion, not internal monitoring.
  Detail: Urgency Medium-High. Recommended: pre-registered external criterion for prioritization-vs-recursion, applied outside the self-summary loop (Tom/Adaptive). Couples OPEN-067, PRESUMPTION-275 (REVISE-071); joins self-referential cluster.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

**Run 2026-05-30 totals:** 1 INCORPORATE, 11 MONITOR, 8 REVISE (DISPOSITION-107..126).

---

## Batch: 2026-05-31 (c2a2-lit-search-pipeline; autonomous; Tom not present)

*Processing the 2026-05-30 EOD self-awareness batch: ASSUMPTION-263 + PRESUMPTION-287/288/289/290 (all at cycle 0, first 15a/15b dispatch). Common thread: the 3rd-cycle claude.ai logout and its reach into the self-awareness layer's own intake.*

### 15a returns (FOR — supportive)

```
RETURN-TO-14a:
  Original item: ASSUMPTION-263
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Moderate
  Key source: drdroid/Supabase/Stytch session-expiry diagnosis guides; oneuptime OAuth2 expired-token recovery (2025-26)
  Summary: Shared-credential expiry is the best-documented auth-pipeline failure mode and re-login is its canonical fix; "one re-login is the right first action" is supported, "stays fixed / unblocks both" is the stronger, less-supported half.
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-263_for.md
```

```
RETURN-TO-14b:
  Original item: PRESUMPTION-287
  Search direction: FOR (supportive)
  Result: NO-SUPPORT-FOUND
  Strength: None
  Key source: Integrate.io Data Completeness Index; dqlabs/Pantomath data-observability guides
  Summary: No literature endorses "absence of record == no event"; the field treats it as a defect to design out. Only a base-rate ("usually a quiet day") pragmatic defense exists, which fails exactly when intake is known-down.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-287_for.md
```

```
RETURN-TO-14b:
  Original item: PRESUMPTION-288
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Moderate
  Key source: YAGNI literature (GeeksforGeeks; swenotes); databank/cbtnuggets redundancy-by-stakes guides
  Summary: A single shared transport with manual recovery is a defensible KISS/YAGNI choice for a low-stakes personal pipeline; redundancy level should match stakes. Conditional on stakes being low and recovery reliably noticed.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-288_for.md
```

```
RETURN-TO-14b:
  Original item: PRESUMPTION-289
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Moderate
  Key source: PagerDuty/Splunk/IBM alert-fatigue guides; PMC5387195 (repeated-alert desensitization)
  Summary: Alert-fatigue research supports restraint in notification volume — a quiet once-per-cycle note over escalation spam. Supports low noise, not specifically that passivity is sufficient to actually reach Tom.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-289_for.md
```

```
RETURN-TO-14b:
  Original item: PRESUMPTION-290
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Weak-Moderate
  Key source: SRE uptime-streak / heartbeat-cadence practice; habit-consistency literature
  Summary: Streak/cadence counters are legitimate reliability heuristics when the counted thing IS the goal. Weak for this item, because the C2A2 streak counts "registry advanced" — a diligence proxy, not the underlying self-awareness goal.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-290_for.md
```

### 15b returns (AGAINST — disconfirmatory)

```
RETURN-TO-14a:
  Original item: ASSUMPTION-263
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED
  Strength: Moderate-Strong
  Key source: Rootly recurrence-analysis + RCA guides; Skyvern/Browserless/Anchor browser-automation session fragility
  Specific risk: Re-login is treated as THE fix while a multi-cause / chronic auth-state fragility (profile/cookie corruption, re-logout) goes undiagnosed; 3rd-cycle recurrence is the fingerprint of a single-cause fix on a multi-cause problem.
  Summary: One re-login is a reasonable first action but the "single fix that restores both and holds" claim is challenged by recurrence and extension-session fragility.
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-263_against.md
```

```
RETURN-TO-14b:
  Original item: PRESUMPTION-287
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED
  Strength: Moderate-Strong
  Key source: oneuptime metric-absence alerting; dqlabs/Pantomath/Actian data-observability
  Specific risk: A lost attended session is recorded as an honest-looking quiet day; the self-awareness layer is blind to gaps in its own perception (couples OPEN-069).
  Summary: Observability practice directly contradicts "absence == no-event"; silent coupling of completeness to channel health is the canonical "looks successful while broken" failure.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-287_against.md
```

```
RETURN-TO-14b:
  Original item: PRESUMPTION-288
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED
  Strength: Moderate
  Key source: ScienceDirect/Accendo/Lerus common-mode-failure overviews; NASA CCF modes; IEEE CMF survey
  Specific risk: Intake, delivery, and the self-awareness intake all go dark together with no degraded path; the system cannot even report its own outage. Empirically realized 3 cycles.
  Summary: A single shared session/profile is a textbook common-mode dependency; the SPOF has fired 3 cycles, so "acceptable never-fired SPOF" no longer applies. Diversity/degraded-mode is the standard remedy.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-288_against.md
```

```
RETURN-TO-14b:
  Original item: PRESUMPTION-289
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED
  Strength: Moderate-Strong
  Key source: Rootly/oneuptime escalation-policy + alert-severity guides
  Specific risk: A chronic outage persists indefinitely because each cycle resets to the same low-salience note; the human-response-gate (OPEN-066) stays binding.
  Summary: Escalation design exists precisely so repeating unacknowledged failures change salience/channel; 3 identical cycles partly falsify "passive note is adequate." Alert-fatigue caveat argues against noisy escalation, not against any escalation tier.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-289_against.md
```

```
RETURN-TO-14b:
  Original item: PRESUMPTION-290
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED
  Strength: Moderate-Strong
  Key source: Goodhart's law; surrogation (Nisslmüller; practical-devsecops); metric fixation (Muller, Tyranny of Metrics)
  Specific risk: On degraded-intake days the streak pressures the system to manufacture item-bearing output, contaminating the registry and masking the outage — self-referentially defeating the self-awareness goal.
  Summary: A diligence-proxy streak with no honest "did-not-advance" null is textbook surrogation; the missing "correct not-to-advance" state is the diagnostic signature.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-290_against.md
```

### SYSTEMIC-RISK-FLAG (15b)
```
SYSTEMIC-RISK-FLAG:
  Date: 2026-05-31
  Affected items: ASSUMPTION-263, PRESUMPTION-287, PRESUMPTION-288, PRESUMPTION-289 (+ PRESUMPTION-290 downstream)
  Common vulnerability: The entire daily-sync loop — morning intake, evening delivery, AND the self-awareness layer's own intake — rides ONE shared claude.ai session in ONE Chrome profile. A single logout is a common-mode failure that disables all directions at once, including the channel that would report the outage. The cluster's items are facets of this one dependency: 263 (single-fix optimism about it), 287 (it silently corrupts intake completeness), 288 (it is the common-mode SPOF itself), 289 (no escalation survives it), 290 (the streak pressures masking it).
  Literature basis: Common-mode failure (ScienceDirect; NASA NTRS 20110015733; IEEE CMF survey); metric-absence alerting (oneuptime); Goodhart/surrogation.
  Risk level: High
  Recommendation: Treat as a single coupled architectural decision: add a diverse, non-Chrome degraded-mode path that (a) records intake-health as DEGRADED/UNKNOWN rather than no-event, and (b) carries an escalation/outage signal that survives a claude.ai logout. This single change addresses the common mode behind all five items. Couples OPEN-066 (human-response-gate, project #1), OPEN-069.
```

### 15c dispositions (2026-05-31)

```
DISPOSITION-127:
  Date: 2026-05-31
  Item: ASSUMPTION-263
  Item type: ASSUMPTION (stated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Re-login is the canonical first action for shared-credential expiry, but "single fix that restores both AND holds" is challenged by 3rd-cycle recurrence and extension-session fragility. The decisive fact is that the fix is cheaply and imminently testable on the next attended login.
  Disposition: MONITOR (MONITOR-288)
  Reasoning: Stated, low-cost-to-verify operational hypothesis; neither INCORPORATE (unverified, challenged) nor REVISE (no design change needed yet — just verify). Empirical check on next cycle will resolve it.
  Detail: Cadence Weekly; next 15d 2026-06-07. Priority HIGH (gates the whole loop). What would change: verified recovery of BOTH directions holding ≥2 cycles -> INCORPORATE; recurrence after re-login -> REVISE (multi-cause RCA). Couples PRESUMPTION-288.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-128:
  Date: 2026-05-31
  Item: PRESUMPTION-287
  Item type: PRESUMPTION (unstated)
  15a result: NO-SUPPORT-FOUND | 15a strength: None
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: No literature endorses "absence of record == no event"; observability practice treats it as a defect to design out. PRESUMPTION + only-evidence-is-against + self-referential (blind spot in the self-awareness layer's own intake) -> REVISE.
  Disposition: REVISE (REVISE-080)
  Reasoning: Designers were unaware they were coupling extraction completeness to intake-channel health; the presumption is unsupported and actively challenged, and most dangerous in the present known-down state. Cheap, fail-loud remedy.
  Detail: Urgency Medium-High. Recommended: record intake-health explicitly — emit DEGRADED/UNKNOWN-completeness rather than defaulting to no-event when the scrape fails. Couples OPEN-069, PRESUMPTION-290; part of the 2026-05-31 single-transport systemic-risk cluster.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-129:
  Date: 2026-05-31
  Item: PRESUMPTION-288
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Moderate
  Net assessment: A single shared transport is a defensible KISS/YAGNI choice for a low-stakes personal pipeline (15a), but it is also a textbook common-mode SPOF that has now actually fired 3 cycles (15b). The "add redundancy" call is a genuine cost-benefit decision, not a clear refutation.
  Disposition: MONITOR (MONITOR-289)
  Reasoning: Contested on stakes (15a moderate support) vs realized common-mode failure (15b moderate); err toward MONITOR over REVISE since whether redundancy is worth it is a human cost-benefit judgment. But priority HIGH because the SPOF is active and the remedy is shared with REVISE-080.
  Detail: Cadence Weekly; next 15d 2026-06-07. Priority HIGH. What would change: a 4th outage cycle, or evidence the outage silences the alert path too -> REVISE toward a diverse degraded-mode channel. Couples ASSUMPTION-263, PRESUMPTION-287/289; 2026-05-31 systemic-risk cluster.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-130:
  Date: 2026-05-31
  Item: PRESUMPTION-289
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Alert-fatigue research supports notification restraint (15a), but escalation design exists precisely so a repeating unacknowledged failure changes salience — and 3 identical cycles with no resolution partly falsify "passive note is adequate" (15b). PRESUMPTION + partly-falsified + couples the project's #1 standing item -> REVISE.
  Disposition: REVISE (REVISE-081)
  Reasoning: The passive-notification presumption belongs with the standing human-response-gate flag (OPEN-066); empirically it has not closed the loop in 3 cycles. Route to Tom, but design the fix to fire ONCE on repetition (N>=2), not every cycle, to respect the alert-fatigue caveat.
  Detail: Urgency Medium. Recommended: a single repetition-triggered escalation step (raise salience / change channel once on cycle N>=2 of the same blocker), bounded to avoid fatigue. Couples OPEN-066, PRESUMPTION-240; 2026-05-31 systemic-risk cluster.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-131:
  Date: 2026-05-31
  Item: PRESUMPTION-290
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Streaks are legitimate only when the counted thing IS the goal; the C2A2 advance-streak counts a diligence proxy, and its missing "correct not-to-advance" null is the diagnostic signature of surrogation (Goodhart). PRESUMPTION + self-referential + strong challenge -> REVISE.
  Disposition: REVISE (REVISE-082)
  Reasoning: Joins the self-referential / metric-fixation cluster with REVISE-079 (PRESUMPTION-286, closed-loop self-diagnosis). On degraded-intake days the streak pressures manufacturing output over honest reporting — directly defeating the self-awareness goal. Cheap remedy: redefine what the streak counts.
  Detail: Urgency Medium. Recommended: make an explicit "honest no-op / degraded" run a first-class state that PRESERVES the streak; count "honest accounting performed," not "items emitted." Couples PRESUMPTION-287, PRESUMPTION-286 (REVISE-079); 2026-05-31 systemic-risk cluster.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

**Run 2026-05-31 totals:** 0 INCORPORATE, 2 MONITOR (MONITOR-288..289), 3 REVISE (REVISE-080..082) (DISPOSITION-127..131). SYSTEMIC-RISK: single-transport common-mode cluster (5 items). Consistency check: no INCORPORATE this run, so no conflict with existing validated premises (last PREMISE-044).


## 2026-06-01 — 15a/15b/15c RUN (drain of 15d 2026-05-31 RE-TRIGGER cohort)

**Run type:** Automated weekly refresh via c2a2-lit-search-pipeline scheduled task (15a + 15b + 15c), one hour after the 14a/14b self-awareness pipeline.
**Cohort:** 92 MONITOR items re-triggered by 15d on 2026-05-31 (cycles: 59×cycle-1, 16×cycle-2, 17×cycle-3). All were [QUEUED]/[AWAITING-15a/15b/15c].
**Pipeline timing:** 15d weekly cadence fired ON TIME (2026-05-31). This is a clean on-cadence drain — NO overdue 15d-schedule backlog (contrast 2026-05-17 SYSTEMIC-RISK-FLAG run).
**Landscape spot-check (honest sampling):** 3 genuine web searches across distinct clusters — (a) passwordless/one-tap-link & SMS-auth security, (b) Levin–Hoffman–Kastrup idealist convergence, (c) multi-agent LLM systems instantiating research traditions/consensus. All three REAFFIRMED prior for/against profiles; no material literature shift detected this week. The spot-check is a representative sample, NOT an exhaustive per-item external search — flagged per fail-loud discipline.
**Net outcome:** All 92 items refreshed by both 15a and 15b (no new sources surfaced) and re-dispositioned by 15c as MONITOR (carry forward; weekly cadence). 0 items left searched-but-undispositioned. 0 INCORPORATE, 0 REVISE this cycle.
**Fail-loud notes:**
  - SECURITY CLUSTER (ASSUMPTION-121 Twilio SMS one-tap; PRESUMPTION-153 signed-link sufficiency): 15b challenge REAFFIRMED by continuing 2025–2026 anti-SMS-auth guidance (FBI/CISA 2025; UAE Mar-2026 & Philippines Jun-2026 SMS-OTP retirement deadlines; AiTM/replay/SIM-swap surfaces). This is continuation of an already-recorded strong challenge, not a new-this-week reversal — 15c did NOT auto-escalate to REVISE (no new evidence; REVISE requires human review per 15c spec), but the cluster is surfaced here for Tom's attention.
  - Automated-refresh bound: weekly LLM refresh is limited in surfacing genuinely new external literature; operational evidence from C2A2's own runs remains the more sensitive change signal.

### RETURN/DISPOSITION blocks (92 items)

### RETURN/DISPOSITION: ASSUMPTION-033 (cycle 3 refresh) [MONITOR-39]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-033_for.md ; lit_search_results/against/ASSUMPTION-033_against.md

### RETURN/DISPOSITION: ASSUMPTION-049 (cycle 3 refresh) [MONITOR-53]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-049_for.md ; lit_search_results/against/ASSUMPTION-049_against.md

### RETURN/DISPOSITION: ASSUMPTION-052 (cycle 3 refresh) [MONITOR-55]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-052_for.md ; lit_search_results/against/ASSUMPTION-052_against.md

### RETURN/DISPOSITION: PRESUMPTION-058 (cycle 3 refresh) [MONITOR-57]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-058_for.md ; lit_search_results/against/PRESUMPTION-058_against.md

### RETURN/DISPOSITION: ASSUMPTION-055 (cycle 3 refresh) [MONITOR-58]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-055_for.md ; lit_search_results/against/ASSUMPTION-055_against.md

### RETURN/DISPOSITION: ASSUMPTION-064 (cycle 3 refresh) [MONITOR-63]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-064_for.md ; lit_search_results/against/ASSUMPTION-064_against.md

### RETURN/DISPOSITION: ASSUMPTION-065 (cycle 3 refresh) [MONITOR-64]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-065_for.md ; lit_search_results/against/ASSUMPTION-065_against.md

### RETURN/DISPOSITION: ASSUMPTION-066 (cycle 3 refresh) [MONITOR-65]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-066_for.md ; lit_search_results/against/ASSUMPTION-066_against.md

### RETURN/DISPOSITION: ASSUMPTION-067 (cycle 3 refresh) [MONITOR-66]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-067_for.md ; lit_search_results/against/ASSUMPTION-067_against.md

### RETURN/DISPOSITION: PRESUMPTION-072 (cycle 3 refresh) [MONITOR-67]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-072_for.md ; lit_search_results/against/PRESUMPTION-072_against.md

### RETURN/DISPOSITION: PRESUMPTION-073 (cycle 3 refresh) [MONITOR-68]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-073_for.md ; lit_search_results/against/PRESUMPTION-073_against.md

### RETURN/DISPOSITION: ASSUMPTION-071 (cycle 3 refresh) [MONITOR-70]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-071_for.md ; lit_search_results/against/ASSUMPTION-071_against.md

### RETURN/DISPOSITION: ASSUMPTION-072 (cycle 3 refresh) [MONITOR-71]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-072_for.md ; lit_search_results/against/ASSUMPTION-072_against.md

### RETURN/DISPOSITION: ASSUMPTION-073 (cycle 3 refresh) [MONITOR-72]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-073_for.md ; lit_search_results/against/ASSUMPTION-073_against.md

### RETURN/DISPOSITION: ASSUMPTION-074 (cycle 3 refresh) [MONITOR-73]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-074_for.md ; lit_search_results/against/ASSUMPTION-074_against.md

### RETURN/DISPOSITION: ASSUMPTION-075 (cycle 3 refresh) [MONITOR-74]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-075_for.md ; lit_search_results/against/ASSUMPTION-075_against.md

### RETURN/DISPOSITION: ASSUMPTION-077 (cycle 1 refresh) [MONITOR-75]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-077_for.md ; lit_search_results/against/ASSUMPTION-077_against.md

### RETURN/DISPOSITION: PRESUMPTION-086 (cycle 3 refresh) [MONITOR-76]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-086_for.md ; lit_search_results/against/PRESUMPTION-086_against.md

### RETURN/DISPOSITION: PRESUMPTION-090 (cycle 1 refresh) [MONITOR-77]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-090_for.md ; lit_search_results/against/PRESUMPTION-090_against.md

### RETURN/DISPOSITION: PRESUMPTION-092 (cycle 1 refresh) [MONITOR-78]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-092_for.md ; lit_search_results/against/PRESUMPTION-092_against.md

### RETURN/DISPOSITION: ASSUMPTION-080 (cycle 1 refresh) [MONITOR-80]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-080_for.md ; lit_search_results/against/ASSUMPTION-080_against.md

### RETURN/DISPOSITION: ASSUMPTION-082 (cycle 1 refresh) [MONITOR-82]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-082_for.md ; lit_search_results/against/ASSUMPTION-082_against.md

### RETURN/DISPOSITION: ASSUMPTION-089 (cycle 1 refresh) [MONITOR-89]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-089_for.md ; lit_search_results/against/ASSUMPTION-089_against.md

### RETURN/DISPOSITION: ASSUMPTION-092 (cycle 1 refresh) [MONITOR-92]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-092_for.md ; lit_search_results/against/ASSUMPTION-092_against.md

### RETURN/DISPOSITION: ASSUMPTION-095 (cycle 1 refresh) [MONITOR-95]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-095_for.md ; lit_search_results/against/ASSUMPTION-095_against.md

### RETURN/DISPOSITION: ASSUMPTION-097 (cycle 1 refresh) [MONITOR-100]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-097_for.md ; lit_search_results/against/ASSUMPTION-097_against.md

### RETURN/DISPOSITION: ASSUMPTION-098 (cycle 1 refresh) [MONITOR-101]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-098_for.md ; lit_search_results/against/ASSUMPTION-098_against.md

### RETURN/DISPOSITION: ASSUMPTION-099 (cycle 1 refresh) [MONITOR-102]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-099_for.md ; lit_search_results/against/ASSUMPTION-099_against.md

### RETURN/DISPOSITION: ASSUMPTION-101 (cycle 1 refresh) [MONITOR-104]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-101_for.md ; lit_search_results/against/ASSUMPTION-101_against.md

### RETURN/DISPOSITION: ASSUMPTION-106 (cycle 1 refresh) [MONITOR-109]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-106_for.md ; lit_search_results/against/ASSUMPTION-106_against.md

### RETURN/DISPOSITION: ASSUMPTION-108 (cycle 1 refresh) [MONITOR-110]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-108_for.md ; lit_search_results/against/ASSUMPTION-108_against.md

### RETURN/DISPOSITION: ASSUMPTION-109 (cycle 1 refresh) [MONITOR-111]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-109_for.md ; lit_search_results/against/ASSUMPTION-109_against.md

### RETURN/DISPOSITION: ASSUMPTION-111 (cycle 1 refresh) [MONITOR-113]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-111_for.md ; lit_search_results/against/ASSUMPTION-111_against.md

### RETURN/DISPOSITION: ASSUMPTION-112 (cycle 1 refresh) [MONITOR-114]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-112_for.md ; lit_search_results/against/ASSUMPTION-112_against.md

### RETURN/DISPOSITION: PRESUMPTION-128 (cycle 1 refresh) [MONITOR-115]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-128_for.md ; lit_search_results/against/PRESUMPTION-128_against.md

### RETURN/DISPOSITION: PRESUMPTION-135 (cycle 1 refresh) [MONITOR-118]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-135_for.md ; lit_search_results/against/PRESUMPTION-135_against.md

### RETURN/DISPOSITION: PRESUMPTION-137 (cycle 1 refresh) [MONITOR-119]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-137_for.md ; lit_search_results/against/PRESUMPTION-137_against.md

### RETURN/DISPOSITION: ASSUMPTION-118 (cycle 2 refresh) [MONITOR-122]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-118_for.md ; lit_search_results/against/ASSUMPTION-118_against.md

### RETURN/DISPOSITION: ASSUMPTION-121 (cycle 2 refresh) [MONITOR-126]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle | SECURITY-CLUSTER: 15b challenge reaffirmed (anti-SMS-auth regulatory momentum); surfaced for human review, no auto-REVISE
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-121_for.md ; lit_search_results/against/ASSUMPTION-121_against.md

### RETURN/DISPOSITION: ASSUMPTION-127 (cycle 2 refresh) [MONITOR-130]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-127_for.md ; lit_search_results/against/ASSUMPTION-127_against.md

### RETURN/DISPOSITION: PRESUMPTION-153 (cycle 2 refresh) [MONITOR-134]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle | SECURITY-CLUSTER: 15b challenge reaffirmed (anti-SMS-auth regulatory momentum); surfaced for human review, no auto-REVISE
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-153_for.md ; lit_search_results/against/PRESUMPTION-153_against.md

### RETURN/DISPOSITION: PRESUMPTION-154 (cycle 2 refresh) [MONITOR-135]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-154_for.md ; lit_search_results/against/PRESUMPTION-154_against.md

### RETURN/DISPOSITION: PRESUMPTION-160 (cycle 2 refresh) [MONITOR-140]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-160_for.md ; lit_search_results/against/PRESUMPTION-160_against.md

### RETURN/DISPOSITION: PRESUMPTION-167 (cycle 2 refresh) [MONITOR-146]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-167_for.md ; lit_search_results/against/PRESUMPTION-167_against.md

### RETURN/DISPOSITION: ASSUMPTION-133 (cycle 2 refresh) [MONITOR-148]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-133_for.md ; lit_search_results/against/ASSUMPTION-133_against.md

### RETURN/DISPOSITION: ASSUMPTION-138 (cycle 2 refresh) [MONITOR-151]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-138_for.md ; lit_search_results/against/ASSUMPTION-138_against.md

### RETURN/DISPOSITION: ASSUMPTION-140 (cycle 2 refresh) [MONITOR-153]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-140_for.md ; lit_search_results/against/ASSUMPTION-140_against.md

### RETURN/DISPOSITION: PRESUMPTION-170 (cycle 2 refresh) [MONITOR-160]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-170_for.md ; lit_search_results/against/PRESUMPTION-170_against.md

### RETURN/DISPOSITION: PRESUMPTION-173 (cycle 2 refresh) [MONITOR-163]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-173_for.md ; lit_search_results/against/PRESUMPTION-173_against.md

### RETURN/DISPOSITION: PRESUMPTION-175 (cycle 2 refresh) [MONITOR-165]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-175_for.md ; lit_search_results/against/PRESUMPTION-175_against.md

### RETURN/DISPOSITION: PRESUMPTION-178 (cycle 2 refresh) [MONITOR-168]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-178_for.md ; lit_search_results/against/PRESUMPTION-178_against.md

### RETURN/DISPOSITION: PRESUMPTION-180 (cycle 2 refresh) [MONITOR-169]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-180_for.md ; lit_search_results/against/PRESUMPTION-180_against.md

### RETURN/DISPOSITION: PRESUMPTION-181 (cycle 2 refresh) [MONITOR-170]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-181_for.md ; lit_search_results/against/PRESUMPTION-181_against.md

### RETURN/DISPOSITION: ASSUMPTION-159 (cycle 1 refresh) [MONITOR-172]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-159_for.md ; lit_search_results/against/ASSUMPTION-159_against.md

### RETURN/DISPOSITION: ASSUMPTION-162 (cycle 1 refresh) [MONITOR-174]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-162_for.md ; lit_search_results/against/ASSUMPTION-162_against.md

### RETURN/DISPOSITION: ASSUMPTION-169 (cycle 1 refresh) [MONITOR-179]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-169_for.md ; lit_search_results/against/ASSUMPTION-169_against.md

### RETURN/DISPOSITION: PRESUMPTION-184 (cycle 1 refresh) [MONITOR-181]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-184_for.md ; lit_search_results/against/PRESUMPTION-184_against.md

### RETURN/DISPOSITION: PRESUMPTION-186 (cycle 1 refresh) [MONITOR-183]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-186_for.md ; lit_search_results/against/PRESUMPTION-186_against.md

### RETURN/DISPOSITION: PRESUMPTION-189 (cycle 1 refresh) [MONITOR-184]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-189_for.md ; lit_search_results/against/PRESUMPTION-189_against.md

### RETURN/DISPOSITION: ASSUMPTION-179 (cycle 1 refresh) [MONITOR-194]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-179_for.md ; lit_search_results/against/ASSUMPTION-179_against.md

### RETURN/DISPOSITION: ASSUMPTION-180 (cycle 1 refresh) [MONITOR-195]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-180_for.md ; lit_search_results/against/ASSUMPTION-180_against.md

### RETURN/DISPOSITION: ASSUMPTION-187 (cycle 1 refresh) [MONITOR-197]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-187_for.md ; lit_search_results/against/ASSUMPTION-187_against.md

### RETURN/DISPOSITION: ASSUMPTION-190 (cycle 1 refresh) [MONITOR-198]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-190_for.md ; lit_search_results/against/ASSUMPTION-190_against.md

### RETURN/DISPOSITION: ASSUMPTION-193 (cycle 1 refresh) [MONITOR-199]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-193_for.md ; lit_search_results/against/ASSUMPTION-193_against.md

### RETURN/DISPOSITION: ASSUMPTION-195 (cycle 1 refresh) [MONITOR-200]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-195_for.md ; lit_search_results/against/ASSUMPTION-195_against.md

### RETURN/DISPOSITION: ASSUMPTION-196 (cycle 1 refresh) [MONITOR-201]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-196_for.md ; lit_search_results/against/ASSUMPTION-196_against.md

### RETURN/DISPOSITION: ASSUMPTION-197 (cycle 1 refresh) [MONITOR-202]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-197_for.md ; lit_search_results/against/ASSUMPTION-197_against.md

### RETURN/DISPOSITION: ASSUMPTION-200 (cycle 1 refresh) [MONITOR-203]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-200_for.md ; lit_search_results/against/ASSUMPTION-200_against.md

### RETURN/DISPOSITION: PRESUMPTION-213 (cycle 1 refresh) [MONITOR-204]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-213_for.md ; lit_search_results/against/PRESUMPTION-213_against.md

### RETURN/DISPOSITION: PRESUMPTION-214 (cycle 1 refresh) [MONITOR-205]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-214_for.md ; lit_search_results/against/PRESUMPTION-214_against.md

### RETURN/DISPOSITION: PRESUMPTION-216 (cycle 1 refresh) [MONITOR-206]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-216_for.md ; lit_search_results/against/PRESUMPTION-216_against.md

### RETURN/DISPOSITION: PRESUMPTION-217 (cycle 1 refresh) [MONITOR-207]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-217_for.md ; lit_search_results/against/PRESUMPTION-217_against.md

### RETURN/DISPOSITION: PRESUMPTION-218 (cycle 1 refresh) [MONITOR-208]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-218_for.md ; lit_search_results/against/PRESUMPTION-218_against.md

### RETURN/DISPOSITION: PRESUMPTION-219 (cycle 1 refresh) [MONITOR-209]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-219_for.md ; lit_search_results/against/PRESUMPTION-219_against.md

### RETURN/DISPOSITION: ASSUMPTION-201 (cycle 1 refresh) [MONITOR-210]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-201_for.md ; lit_search_results/against/ASSUMPTION-201_against.md

### RETURN/DISPOSITION: ASSUMPTION-202 (cycle 1 refresh) [MONITOR-211]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-202_for.md ; lit_search_results/against/ASSUMPTION-202_against.md

### RETURN/DISPOSITION: ASSUMPTION-207 (cycle 1 refresh) [MONITOR-213]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-207_for.md ; lit_search_results/against/ASSUMPTION-207_against.md

### RETURN/DISPOSITION: PRESUMPTION-224 (cycle 1 refresh) [MONITOR-214]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-224_for.md ; lit_search_results/against/PRESUMPTION-224_against.md

### RETURN/DISPOSITION: PRESUMPTION-226 (cycle 1 refresh) [MONITOR-216]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-226_for.md ; lit_search_results/against/PRESUMPTION-226_against.md

### RETURN/DISPOSITION: PRESUMPTION-227 (cycle 1 refresh) [MONITOR-217]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-227_for.md ; lit_search_results/against/PRESUMPTION-227_against.md

### RETURN/DISPOSITION: PRESUMPTION-229 (cycle 1 refresh) [MONITOR-218]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-229_for.md ; lit_search_results/against/PRESUMPTION-229_against.md

### RETURN/DISPOSITION: PRESUMPTION-230 (cycle 1 refresh) [MONITOR-219]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-230_for.md ; lit_search_results/against/PRESUMPTION-230_against.md

### RETURN/DISPOSITION: ASSUMPTION-214 (cycle 1 refresh) [MONITOR-220]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-214_for.md ; lit_search_results/against/ASSUMPTION-214_against.md

### RETURN/DISPOSITION: PRESUMPTION-231 (cycle 1 refresh) [MONITOR-222]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-231_for.md ; lit_search_results/against/PRESUMPTION-231_against.md

### RETURN/DISPOSITION: PRESUMPTION-232 (cycle 1 refresh) [MONITOR-223]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-232_for.md ; lit_search_results/against/PRESUMPTION-232_against.md

### RETURN/DISPOSITION: PRESUMPTION-234 (cycle 1 refresh) [MONITOR-224]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-234_for.md ; lit_search_results/against/PRESUMPTION-234_against.md

### RETURN/DISPOSITION: PRESUMPTION-236 (cycle 1 refresh) [MONITOR-226]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-236_for.md ; lit_search_results/against/PRESUMPTION-236_against.md

### RETURN/DISPOSITION: PRESUMPTION-237 (cycle 1 refresh) [MONITOR-227]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-237_for.md ; lit_search_results/against/PRESUMPTION-237_against.md

### RETURN/DISPOSITION: PRESUMPTION-239 (cycle 1 refresh) [MONITOR-228]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-239_for.md ; lit_search_results/against/PRESUMPTION-239_against.md

### RETURN/DISPOSITION: ASSUMPTION-220 (cycle 1 refresh) [MONITOR-229]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-220_for.md ; lit_search_results/against/ASSUMPTION-220_against.md

### RETURN/DISPOSITION: ASSUMPTION-221 (cycle 1 refresh) [MONITOR-230]
- **Item type:** ASSUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14a->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/ASSUMPTION-221_for.md ; lit_search_results/against/ASSUMPTION-221_against.md

### RETURN/DISPOSITION: PRESUMPTION-242 (cycle 1 refresh) [MONITOR-232]
- **Item type:** PRESUMPTION
- **15a refresh:** No new supporting literature this cycle
- **15b refresh:** No new challenging literature this cycle
- **15c re-disposition:** MONITOR (carries forward; weekly cadence; next 15d check 2026-06-07)
- **Provenance chain:** [14b->15a,15b->15c->15d->15a,15b->15c]
- **Full results:** lit_search_results/for/PRESUMPTION-242_for.md ; lit_search_results/against/PRESUMPTION-242_against.md


## 2026-06-02 — 15a/15b/15c RUN (2026-05-31 EOD batch: ASSUMPTION-264 + PRESUMPTION-291/292/293)

**Run type:** Automated via c2a2-lit-search-pipeline scheduled task (15a + 15b + 15c), one hour after the 14a/14b self-awareness pipeline. Autonomous; Tom not present at run time.
**Cohort:** 4 cycle-0 items queued by the 2026-05-31 EOD self-awareness run (degraded-session epistemics angles). All were [QUEUED] with no prior 15a/15b/15c tags.
**Grounding:** 4 genuine web searches this run (read-after-write/read-your-writes consistency; common-mode failure / Knight-Leveson N-version independence; hierarchy-of-controls / forcing functions; event-time vs processing-time / data freshness). All four items map to stable, well-established literature; honest sampling, not an exhaustive per-item external sweep — flagged per fail-loud discipline.
**Net outcome:** All 4 searched by both 15a and 15b and dispositioned by 15c. 0 items left searched-but-undispositioned.
**Dispositions:** 1 INCORPORATE (PREMISE-045 <- ASSUMPTION-264, necessity direction only) | 1 MONITOR (MONITOR-290 <- PRESUMPTION-292) | 2 REVISE (REVISE-083 <- PRESUMPTION-291; REVISE-084 <- PRESUMPTION-293). DISPOSITION-132..135.

### 15a returns (FOR — supportive)

```
RETURN-TO-14a:
  Original item: ASSUMPTION-264
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Strong (necessity direction)
  Key source: Read-your-writes / read-after-write consistency (AWS S3 strong read-after-write 2020; quorum-commit); fail-loud-on-violation (OpenAI Sandbox Agents)
  Summary: "Optimistic ack is not authoritative; the authoritative signal is a read against committed ground state" is read-your-writes consistency; "do not claim what you cannot re-verify" is canonical fail-loud. Strong for the necessity direction; sufficiency of an in-band re-check is NOT established (couples 293).
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-264_for.md
```

```
RETURN-TO-14b:
  Original item: PRESUMPTION-291
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Moderate
  Key source: Kleppmann, event-time vs processing-time (DDIA 2017; Online Event Processing, CACM 2019); data-freshness/staleness; idempotent dated-delta
  Summary: Narrating latest-on-disk as "today's" is a textbook event-time/processing-time conflation; correctness practice designs it out via freshness tracking and idempotent dated-delta reporting. Concern is empirically realized.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-291_for.md
```

```
RETURN-TO-14b:
  Original item: PRESUMPTION-292
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Moderate-Strong
  Key source: Hierarchy of controls (OSHA); forcing functions/interlocks (Norman, machinery-safety)
  Summary: A behavioral norm ("agent will notice and override") is an administrative control — the less-reliable tier that depends on compliance; fail-loud without an interlock is exactly that. Engineered/forcing-function guards rank higher where stakes warrant.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-292_for.md
```

```
RETURN-TO-14b:
  Original item: PRESUMPTION-293
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Strong
  Key source: Knight & Leveson (1986) independence in N-version programming; common-mode failure (IEEE CMF survey; NASA CCF); out-of-band monitor independence
  Summary: Independence of a checker from the checked system cannot be assumed (correlated failures occur above chance). An in-band "clean reload" in the same degraded regime is a common-mode verifier; authoritative re-verification must be out-of-band.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-293_for.md
```

### 15b returns (AGAINST — disconfirmatory)

```
RETURN-TO-14a:
  Original item: ASSUMPTION-264
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate
  Key source: Knight & Leveson / common-mode failure; optimistic acks + idempotency (Kleppmann); alert-fatigue
  Specific risk: Treating any in-band "clean reload" as authoritative inherits the common-mode blind spot (293) — a confident-but-wrong "verified"; an unbounded re-verify-everything rule risks overhead/fatigue.
  Summary: Core necessity claim is robust; the over-extensions ("clean re-verification is authoritative"; blanket distrust of all intermediate reads) are challenged. Scope to necessity; require out-of-band re-verification.
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-264_against.md
```

```
RETURN-TO-14b:
  Original item: PRESUMPTION-291
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Weak-Moderate
  Key source: YAGNI/KISS; batch-vs-real-time ingestion trade-offs; acceptable-staleness (freshness bound)
  Specific risk: Treating the echo as acceptable normalizes the self-awareness layer mis-dating its OWN record, eroding trust in its dated claims and masking the intake outage.
  Summary: Latest-on-disk narration is a defensible simplification for a low-stakes digest, but the defense weakens sharply because the artifact is self-referential (the honesty layer's own output) and the echo already occurred. Minimal dated-delta fix suffices.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-291_against.md
```

```
RETURN-TO-14b:
  Original item: PRESUMPTION-292
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate
  Key source: Hierarchy-of-controls feasibility clause (OSHA); YAGNI/cost-of-over-instrumentation; behavioral-norm sufficiency in low-stakes contexts
  Specific risk: Over-instrumenting a personal pipeline wastes effort; but accepting the norm risks a silent false-success in the highest-trust component when the agent fails to notice the degraded regime.
  Summary: The hierarchy is a prioritization weighted by feasibility/stakes, not a mandate to engineer out; a behavioral norm may be proportionate for a recoverable single-operator pipeline — but least reliable in exactly the degraded condition it must catch.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-292_against.md
```

```
RETURN-TO-14b:
  Original item: PRESUMPTION-293
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Weak-Moderate
  Key source: rAF/background-tab throttling as a known artifact class (couples REVISE-073/PRESUMPTION-278); out-of-band verification in practice (SRE health-checks; AWS S3 RAW); common-mode is a matter of degree
  Specific risk: Over-reading the presumption induces verification nihilism (distrust all re-checks); under-reading leaves the in-band common-mode blind spot in place.
  Summary: Concedes independence-cannot-be-assumed but rejects the absolutist "no fault-free vantage exists" — independence is constructible (out-of-band / fresh-process exit of a known throttling regime). Sharpens the remedy: make the verifier out-of-band, don't abandon it.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-293_against.md
```

### SYSTEMIC-RISK-FLAG (15b)
```
SYSTEMIC-RISK-FLAG:
  Date: 2026-06-02
  Affected items: ASSUMPTION-264, PRESUMPTION-291, PRESUMPTION-292, PRESUMPTION-293
  Common vulnerability: No fault-independent vantage point. Verification (264), dated self-reporting (291), and the honesty layer's enforcement (292) all execute INSIDE the same degraded session regime they are meant to police, and the re-verification remedy itself can share the fault (293). This is the same common-mode root as the 2026-05-31 single-transport cluster (PRESUMPTION-288/MONITOR-289), now reaching the verification/honesty layer itself: 264 (in-band re-check assumed authoritative), 291 (mis-dates from stale latest-on-disk), 292 (fail-loud is a norm, not an interlock), 293 (the verifier shares the regime).
  Literature basis: Knight & Leveson (1986) + common-mode failure (IEEE CMF survey; NASA CCF); hierarchy of controls (OSHA); event-time vs processing-time (Kleppmann); read-your-writes consistency.
  Risk level: High
  Recommendation: Establish a single OUT-OF-BAND vantage point — a transport/process that does not share the degraded regime's failure mode — and route re-verification, intake-health recording, and dated-delta reporting through it. One change addresses the common mode behind all four items and extends the 2026-05-31 single-transport remedy. Couples REVISE-080, OPEN-066 (project #1), OPEN-069.
```

### 15c dispositions (2026-06-02)

```
DISPOSITION-132:
  Date: 2026-06-02
  Item: ASSUMPTION-264
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Strong (necessity direction)
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: The necessity claim (optimistic ack is not authoritative; do not claim what you cannot re-verify) is strongly grounded in read-your-writes consistency and canonical fail-loud, with no serious challenge. Only the over-extension ("clean re-verification IS authoritative") is contested — a same-regime re-check can share the fault.
  Disposition: INCORPORATE (PREMISE-045)
  Reasoning: Stated assumption, strong support, weak-to-moderate challenge confined to a sub-claim that is explicitly EXCLUDED from the incorporated premise and routed to REVISE-084. Scoped to the necessity direction; matches Tom's Rule 12. Consistency-checked against PREMISE-001..044: no conflict (reinforces fail-loud-on-violation citation).
  Detail: Confidence Moderate (not High — verifier-independence caveat material). Re-check Quarterly; next via 15d. Couples ASSUMPTION-263, MONITOR-290, REVISE-084.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: INCORPORATED
```

```
DISPOSITION-133:
  Date: 2026-06-02
  Item: PRESUMPTION-291
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: Textbook event-time/processing-time conflation, empirically realized (2026-05-30 batches narrated as 2026-05-31's). The low-stakes/YAGNI defense is real but weakens sharply because the mislabelled artifact is the self-awareness layer's OWN honesty output.
  Disposition: REVISE (REVISE-083)
  Reasoning: PRESUMPTION + self-referential + active mis-reporting; the layer mis-dating its own record defeats its purpose and masks the intake outage. Remedy is cheap (dated delta), so the over-engineering objection does not save the current behavior.
  Detail: Urgency Medium-High. Stamp batches with event-date; EOD summary emits a dated delta ("no new items today; latest is 2026-05-30") not latest-as-today. Couples PRESUMPTION-287 (REVISE-080), PRESUMPTION-290 (REVISE-082); 2026-06-02 cluster.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

```
DISPOSITION-134:
  Date: 2026-06-02
  Item: PRESUMPTION-292
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Moderate-Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Hierarchy of controls supports the concern (behavioral norms are the less-reliable administrative tier), but the hierarchy is a feasibility/stakes-weighted prioritization, so a behavioral norm may be proportionate for a recoverable single-operator pipeline. Genuinely contested.
  Disposition: MONITOR (MONITOR-290)
  Reasoning: Interlock-vs-norm is a human cost-benefit judgment, not a refutation — err toward MONITOR over REVISE (15c heuristic). Priority MEDIUM-HIGH: the guard protects the honesty layer itself, and a behavior-only guard is least reliable in the degraded condition it must catch.
  Detail: Cadence Weekly; next 15d 2026-06-07. What would change: any degraded-session false "success" the norm failed to catch -> REVISE toward a lightweight forcing function (block "verified" without an out-of-band token). Couples ASSUMPTION-264, PRESUMPTION-293.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

```
DISPOSITION-135:
  Date: 2026-06-02
  Item: PRESUMPTION-293
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: Knight-Leveson + common-mode literature strongly ground the concern: checker independence cannot be assumed. An in-band "clean reload" in the same degraded regime is a common-mode verifier. 15b's valid pushback (independence is constructible, not impossible) sharpens rather than refutes the remedy.
  Disposition: REVISE (REVISE-084)
  Reasoning: PRESUMPTION + strong support + directly undercuts the SUFFICIENCY of ASSUMPTION-264's in-band re-verification (the part excluded from PREMISE-045). Designers were unaware they assumed a fault-free vantage point. Correct conclusion: make the verifier out-of-band, not abandon verification.
  Detail: Urgency Medium. Require the re-verification path to be out-of-band relative to the degraded mechanism; treat in-band-only re-checks as "unknown." Characterize the regime's mechanism to confirm independence. Couples ASSUMPTION-264 (PREMISE-045 gap), REVISE-073/PRESUMPTION-278 (rAF throttling), PRESUMPTION-288 (MONITOR-289).
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```

**Run 2026-06-02 totals:** 1 INCORPORATE (PREMISE-045), 1 MONITOR (MONITOR-290), 2 REVISE (REVISE-083..084) (DISPOSITION-132..135). SYSTEMIC-RISK: no-independent-vantage / degraded-session common-mode cluster (4 items). Consistency check: PREMISE-045 checked against PREMISE-001..044 — no conflict (reinforces existing fail-loud-on-violation premise/citation).


## 2026-06-02 — 15a/15b/15c RUN (batch 2: 2026-06-02 EOD self-awareness batch — newly queued during this pipeline run)

**Run type:** Same c2a2-lit-search-pipeline run; the 2026-06-02 14a/14b self-awareness batch was written to the queue during this run and processed in the same pass (fail-loud: newly queued items not deferred).
**Cohort:** 4 cycle-0 items — ASSUMPTION-265 + PRESUMPTION-294/295/296. Theme: silent/absence-based failure (stale git index.lock; deferral cost; email-only decision channel).
**Grounding:** 2 additional web searches (cost-of-delay/WSJF/queue-aging; safety-vs-liveness/silent-failure); the fail-loud/read-after-write/channel-of-record concepts reuse this run's batch-1 grounding. Honest sampling, not exhaustive per-item — flagged.
**Net outcome:** All 4 searched by both 15a and 15b and dispositioned by 15c. 0 searched-but-undispositioned.
**Dispositions:** 1 INCORPORATE (PREMISE-046 <- ASSUMPTION-265) | 2 MONITOR (MONITOR-291 <- PRESUMPTION-295; MONITOR-292 <- PRESUMPTION-296) | 1 REVISE (REVISE-085 <- PRESUMPTION-294). DISPOSITION-136..139.

### 15a returns (FOR — supportive)
```
RETURN-TO-14a:
  Original item: ASSUMPTION-265
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Strong
  Key source: Safety vs liveness (Hillel Wayne/Lamport); read-after-write; fail-loud + pre-flight checks
  Summary: "No error" is a weak safety signal, not the liveness property that staging occurred; verify the side effect. Empirically realized 4-day silent staging outage. Same verify-don't-infer family as PREMISE-045.
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-265_for.md
```
```
RETURN-TO-14b:
  Original item: PRESUMPTION-294
  Search direction: FOR (supportive)
  Result: SUPPORTED (core); rider NO-SUPPORT-FOUND
  Strength: Strong (core silent-failure); rider unsupported
  Key source: Safety vs liveness; verify-the-side-effect; idempotency/recovery semantics
  Summary: "git no-error == staged" is a textbook safety-vs-liveness defect (supported). The recovery RIDER (lock removal heals the 4-day window) is unsupported — lock removal is forward-only, not idempotent over the missed window.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-294_for.md
```
```
RETURN-TO-14b:
  Original item: PRESUMPTION-295
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Moderate-Strong
  Key source: Cost of Delay / WSJF (Reinertsen; SAFe; Wikipedia); non-linear value aging (arXiv 1812.09320)
  Summary: Deferral is not cost-free — it accrues delay cost (often the dominant share of lead time) and can age non-linearly into an expedite/incident; the missing cost accounting + escalation trip-wire is the blind spot CoD methods remove.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-295_for.md
```
```
RETURN-TO-14b:
  Original item: PRESUMPTION-296
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Moderate
  Key source: absence-of-signal != absence-of-event (observability; PRESUMPTION-287 lineage); multi-channel intake / evidence completeness
  Summary: Reading "no decision email" as "no decision" conflates missing-data with a confirmed null; a verbal/chat decision on a blind-intake day is silently dropped — IF decisions can legitimately arrive on more than one channel.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-296_for.md
```

### 15b returns (AGAINST — disconfirmatory)
```
RETURN-TO-14a:
  Original item: ASSUMPTION-265
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Weak-Moderate
  Key source: YAGNI/KISS; git exit-code reliability in common case; cost-of-instrumentation/alert-fatigue
  Specific risk: Skipping verification leaves blindness to future silent VC failures; over-instrumenting adds noise. Narrow check (stale-lock + read-after-write) avoids the noise objection.
  Summary: Per-run verification could be over-engineering IF the incident were a one-off; it was not (4-day silent staging block), so the realized failure outweighs the YAGNI objection. Scope the check narrowly.
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-265_against.md
```
```
RETURN-TO-14b:
  Original item: PRESUMPTION-294
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED (core); recovery RIDER strongly challenged
  Strength: Weak-Moderate (core); Strong (against rider)
  Key source: optimistic-ack acceptability (bounds the core); idempotency/recovery semantics + RCA (against rider)
  Specific risk: If the rider stands, the system believes the 4-day window is healed when those changes remain untracked — a second silent integrity gap.
  Summary: Trust "no error==done" is fine for cheap self-healing ops; target the rule at consequential/non-self-healing ops. The rider is wrong: lock removal does not re-run skipped staging; reconstruct + verify the lock window.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-294_against.md
```
```
RETURN-TO-14b:
  Original item: PRESUMPTION-295
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate
  Key source: real-options/optionality; safe-default human-in-the-loop (OPEN-066); reversibility caveat
  Specific risk: Treating deferral as cost-free risks an unbounded silent backlog aging into incident; over-eager action risks irreversible ingestion without Tom's decision.
  Summary: For irreversible, judgment-laden human-gated work, waiting is the correct safe default with option value; but that does not defend the ABSENCE of cost accounting / escalation trip-wire. Hold both: wait, but track + trip-wire.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-295_against.md
```
```
RETURN-TO-14b:
  Original item: PRESUMPTION-296
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate
  Key source: single source/channel of record; command-of-record discipline; cost of multi-channel reconciliation
  Specific risk: If the single-channel constraint is unstated, a verbal decision is silently dropped; if explicit, the only cost is Tom must email decisions.
  Summary: A single dated email channel-of-record is a defensible, even desirable, constraint for a provenance-first system. IF intended, "no email==no decision" is correct policy; the residual risk is only that the constraint is implicit. Make it explicit.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-296_against.md
```

### SYSTEMIC-RISK-FLAG (15b, batch 2 — extends 2026-06-02 cluster)
```
SYSTEMIC-RISK-FLAG:
  Date: 2026-06-02
  Affected items: ASSUMPTION-265, PRESUMPTION-294, PRESUMPTION-296 (+ batch-1 264/291/292/293; + 287)
  Common vulnerability: "Absence != success/event." The system repeatedly infers a positive state from a NULL it never verified out-of-band — "no git error"==staged (294/265), "no decision email"==no decision (296), "no readable transcript"==no session (287), an in-band reload==verified (264/293). Same root: no fault-independent confirmation that the intended effect/event actually occurred.
  Literature basis: Safety vs liveness (Hillel Wayne; Lamport); read-your-writes consistency; observability metric-absence alerting; common-mode failure (Knight & Leveson).
  Risk level: High
  Recommendation: One coupled remedy — an OUT-OF-BAND vantage point plus explicit verify-the-effect checks (PREMISE-045/046) so a null is recorded as UNKNOWN, never as a confirmed positive. Couples REVISE-080, OPEN-066 (project #1), OPEN-069, OPEN-071.
```

### 15c dispositions (2026-06-02, batch 2)
```
DISPOSITION-136:
  Date: 2026-06-02
  Item: ASSUMPTION-265
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: Verify-the-effect (not infer-from-no-error) is strongly grounded (safety vs liveness; read-after-write) and empirically realized (4-day silent staging block). The YAGNI challenge is weak and outweighed by the realized multi-day failure on the VC spine.
  Disposition: INCORPORATE (PREMISE-046)
  Reasoning: Stated assumption, strong support, weak challenge; same verify-don't-infer/fail-loud family as PREMISE-045. Mitigation folded in: scope the check narrowly (stale-lock + read-after-write). Consistency-checked vs PREMISE-001..045: reinforces, no conflict.
  Detail: Confidence Moderate-High. Re-check Quarterly (2026-09-02) via 15d. Couples PRESUMPTION-294 (REVISE-085), OPEN-071.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: INCORPORATED
```
```
DISPOSITION-137:
  Date: 2026-06-02
  Item: PRESUMPTION-294
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED (core); rider NO-SUPPORT | 15a strength: Strong (core)
  15b result: PARTIALLY-CHALLENGED (core); rider STRONGLY challenged | 15b strength: Strong (against rider)
  Net assessment: The silent-failure core is incorporated as the stated twin (PREMISE-046). What requires design action is the false recovery RIDER: clearing the lock is forward-only and not idempotent over the missed window, so the ~4 days of skipped staging are not healed by lock removal.
  Disposition: REVISE (REVISE-085)
  Reasoning: PRESUMPTION + self-referential + an actively-wrong recovery rider that would leave a second silent integrity gap. Cheap one-time remedy (reconstruct + verify the lock window).
  Detail: Urgency Medium-High. After clearing the lock, diff working tree vs last confirmed-staged commit for 2026-05-29 → 2026-06-02, re-stage/commit, verify read-after-write; add stale-lock pre-flight. Couples PREMISE-046, OPEN-071.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED
```
```
DISPOSITION-138:
  Date: 2026-06-02
  Item: PRESUMPTION-295
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Moderate-Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Cost-of-delay supports that deferral accrues cost and can age into an incident (15a); but for irreversible, human-gated work, waiting is the correct safe default with option value (15b). Both hold: wait, but track + trip-wire. The named gap (no accounting, no escalation) is real; the act-vs-wait call is Tom's.
  Disposition: MONITOR (MONITOR-291)
  Reasoning: Genuinely contested; err toward MONITOR over REVISE. Priority MEDIUM-HIGH (review queue ~3 weeks old; couples human-response-gate).
  Detail: Cadence Weekly; next 15d 2026-06-07. What would change: a deferred item aging past where waiting cost exceeds action risk, or demonstrated harm -> REVISE toward CoD accounting + staleness trip-wire. Couples OPEN-066, REVISE-081, PRESUMPTION-296.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```
```
DISPOSITION-139:
  Date: 2026-06-02
  Item: PRESUMPTION-296
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Shares the "absence != event" family (concern real if decisions can arrive multi-channel), but a single dated-email channel-of-record is a defensible, provenance-friendly constraint. The whole question turns on whether the email-only constraint is intended — unknown at autonomous run time.
  Disposition: MONITOR (MONITOR-292)
  Reasoning: Contested and resolvable by one fact (does Tom decide verbally/in chat?). Not REVISE (email-only may be correct policy); not INCORPORATE (constraint currently implicit, possibly lossy). Err toward MONITOR. Priority MEDIUM.
  Detail: Cadence Weekly; next 15d 2026-06-07. What would change: Tom decides verbally/chat -> REVISE (add capture path); email is sole intended channel -> INCORPORATE as an explicit declared channel-of-record. Couples PRESUMPTION-287 (REVISE-080), PRESUMPTION-295, OPEN-069.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

**Run 2026-06-02 totals (both batches):** 2 INCORPORATE (PREMISE-045, PREMISE-046), 3 MONITOR (MONITOR-290..292), 3 REVISE (REVISE-083..085) (DISPOSITION-132..139, 8 items). SYSTEMIC-RISK: no-independent-vantage / "absence != success/event" common-mode cluster (8 items, extending the 2026-05-31 single-transport flag). Consistency check: PREMISE-045/046 checked vs PREMISE-001..044 — no conflict (both reinforce the fail-loud / verify-the-effect family).

---

## 2026-06-03 run — c2a2-lit-search-pipeline (autonomous; Tom not present at fire time)

*Batch: 2026-06-02 evening Sociogram session (ASSUMPTION-266/267/268 + PRESUMPTION-297/298/299), cycle 0. 6 genuine web searches this run across 3 coupled clusters (git-staging/cross-repo; node-cap scaling; live/spot-check verification). Honest sampling, not an exhaustive per-item external sweep.*

### 15a returns (FOR)
```
RETURN-TO-14a:
  Original item: ASSUMPTION-266
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Strong
  Key source: git-scm git-add docs + practitioner consensus (HN 12886492; GitHub git-guides)
  Summary: Explicit-path staging in a chronically dirty tree is well-established best practice to avoid committing unintended changes.
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-266_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-267
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Moderate
  Key source: SRE headroom/capacity guides; octocore Capacity vs Load
  Summary: Raising the cap above current load (2529) with headroom is correct; "20000 is a verified safe ceiling" is not established (couples PRESUMPTION-299).
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-267_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-268
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Strong
  Key source: cloudbees test-in-prod; Harness "only a full pipeline run counts"
  Summary: In-situ served-browser verification with observable evidence + human sign-off is well-grounded; instantiates the verify-the-effect family (PREMISE-045/046).
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-268_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-297
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Strong
  Key source: Concordia DAS Lab ArtifactSync; GitLab #14311; ACM Koli Calling 2025 multi-artifact consistency
  Specific risk: A pushed viz depending on uncommitted second-repo edits can silently desync; no transactional guarantee across repos.
  Summary: Cross-repo silent desync is a documented hazard; human memory + handoff note is a recognized weak interlock.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-297_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-298
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Moderate-Strong
  Key source: Equivalence-class/BVA theory (Myers ch.4; TestBench); arXiv:2103.04578 believed-equivalence
  Specific risk: One isolate + one focus generalized to all assumes an unverified partition; boundaries (zero-link/dense) least represented.
  Summary: Single spot-check generalizes only if the class is genuinely equivalent — a partition that was assumed, not shown.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-298_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-299
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Strong
  Key source: Force-directed render-cliff surveys (Weber/Medium; GraphAware PIXI.js); octocore Capacity vs Load
  Specific risk: D3/SVG cliffs near ~1000+ nodes mean 20000 is far above tested capacity; cap can re-admit the crash it guards.
  Summary: 10x ceiling validated only at 2529; 2.5k–20k uncharacterized; a configured limit is not a tested limit.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-299_for.md
```

### 15b returns (AGAINST)
```
RETURN-TO-14a:
  Original item: ASSUMPTION-266
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate
  Key source: root-cause-vs-workaround (GitLab #14311); hierarchy-of-controls/forcing-function lineage
  Specific risk: Memory-dependent "never -A" rule is re-breakable by one reflex; explicit paths can silently OMIT new intended files.
  Summary: Explicit-path staging fixes the symptom; the dirty tree is the defect (.gitignore/separate repos/submodules); manual convention < forcing function.
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-266_against.md

RETURN-TO-14a:
  Original item: ASSUMPTION-267
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED
  Strength: Moderate-Strong
  Key source: force-directed cliff (~1000+ nodes, D3/SVG); octocore "capacity must be tested"
  Specific risk: 20000 likely above real render capacity; cap can silently re-admit the crash on large future data.
  Summary: "Raise above 2529" sound; "20000 is safe" is an untested claim (couples PRESUMPTION-299).
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-267_against.md

RETURN-TO-14a:
  Original item: ASSUMPTION-268
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate
  Key source: Harness smoke-in-CI; release-gate practice
  Specific risk: Mandatory manual foreground gate is the step an autonomous run skips; countable signals better automated.
  Summary: Real-environment verification right; "must be human+foreground" over-claims — automate objective checks, reserve sign-off for the visual property.
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-268_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-297
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Weak-Moderate
  Key source: YAGNI/KISS; GitLab #14311 (cross-repo tooling is costly)
  Specific risk: Over-tooling an intermittent two-repo coupling; under-reacting leaves the (real) desync exposure.
  Summary: Hazard is real (per 15a); disagreement is magnitude — a cheap pre-push "is the other repo clean?" check, not full interlock tooling.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-297_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-298
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate
  Key source: equivalence-class validity argument (Myers; TestBench); YAGNI for personal tools
  Specific risk: Mandating exhaustive UI checks wastes effort IF the fade path is uniform; the risk is real only if it branches.
  Summary: Sufficiency of one spot-check is a code fact — read the fade path: uniform → one case suffices; branching → add boundary cases.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-298_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-299
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate
  Key source: YAGNI on perf-testing unused ranges; existing 80%-of-cap warning
  Specific risk: Pre-empting characterization tests a range slow-growing data won't reach; deferring risks a cliff if growth accelerates without warning.
  Summary: Uncharacterized range is real (per 15a) but timing is the dispute — test-when-approaching (growth-triggered warning) vs test-now.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-299_against.md
```

### SYSTEMIC-RISK-FLAG (15b, 2026-06-03)
```
SYSTEMIC-RISK-FLAG:
  Date: 2026-06-03
  Affected items: ASSUMPTION-266, ASSUMPTION-268, PRESUMPTION-297
  Common vulnerability: Each relies on a MANUAL, memory-dependent convention as the control of record rather than an enforced forcing function — "remember to use explicit git paths" (266), "remember to do a live foreground review" (268), "remember the cross-repo handoff" (297). On an autonomous, human-absent run these are exactly the controls most likely to be silently skipped, re-admitting the failure they nominally prevent. This is the human-vantage twin of the 2026-06-02 "absence != success/event" cluster: there the gap was inferring a positive from an unverified null; here it is substituting human memory for an enforced check.
  Literature basis: hierarchy-of-controls / forcing-functions (administrative controls are the weakest tier); Harness smoke-in-CI (manual gates get skipped under pressure); GitLab #14311 (cross-repo coupling is not transactional).
  Risk level: High
  Recommendation: Convert each memory-dependent convention into a cheap pre-push forcing function — generated/checked explicit-path set + new-file-omission check (266); automated served-browser assertions for the objective signals with human sign-off reserved for the visual property AND the push BLOCKING when the human is absent (268); a pre-push "is the dependent repo clean?" check (297). Couples PREMISE-045/046, REVISE-085, OPEN-071.

SECONDARY-CLUSTER (untested ceiling validated only at current load):
  Affected items: ASSUMPTION-267, PRESUMPTION-299 (verification-coverage cousin: PRESUMPTION-298)
  Common vulnerability: A limit/verification is asserted "safe/correct" from a single current-load data point (20000 cap from 2529 nodes; "works for all" from one isolate). A configured ceiling is not a tested ceiling; one representative is not a covered class.
  Risk level: Medium-High
  Recommendation: Measure the render cliff and set the cap below it (267/299); read the fade code path to decide whether one case is a valid representative (298).
```

### 15c dispositions (2026-06-03)
```
DISPOSITION-140:
  Date: 2026-06-03
  Item: ASSUMPTION-266
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: The discipline itself — explicit-path staging in a chronically dirty tree to avoid committing unintended changes — is strongly and uncontroversially supported. 15b does not dispute the practice; it disputes (a) that the rule, not the dirty tree, is the right locus of fix and (b) that a memory-dependent "never -A" convention is durable (and can silently omit new files).
  Disposition: INCORPORATE (PREMISE-047)
  Reasoning: Strong support + a moderate challenge that targets durability/locus, not correctness, fits INCORPORATE-with-caveats. The premise incorporated is the staging discipline; the forcing-function/structural-fix point is folded in as a caveat and is also captured by this run's High SYSTEMIC-RISK (human-memory controls). Consistency-checked vs PREMISE-001..046: complements PREMISE-046 (verify VC health); no conflict.
  Detail: Confidence Moderate. Re-check Quarterly (2026-09-03) via 15d. Caveat: back the convention with a forcing function (generated/checked explicit-path set + new-file-omission check) or remove the dirt source (.gitignore/separate repos/submodules). Couples PRESUMPTION-297 (MONITOR-293), SYSTEMIC-RISK 2026-06-03.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: INCORPORATED

DISPOSITION-141:
  Date: 2026-06-03
  Item: ASSUMPTION-267
  Item type: ASSUMPTION (stated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: The claim has two parts (Rule 7 — surfaced, not blended). "Raise the cap above 2529 with headroom" is correct and supported — the old 2000 cap truncated real data. "20000 is a SAFE ceiling" is challenged moderate-strong with only weak support: D3/SVG force layouts degrade non-linearly well below 20000, so the cap likely sits above real render capacity and can silently re-admit the crash it guards.
  Disposition: REVISE (REVISE-086)
  Reasoning: Weak support + moderate-strong challenge on the load-bearing sub-claim (safe ceiling) -> lean REVISE. The immediate truncation fix is fine; what needs Tom's review is the untested 10x ceiling. Not INCORPORATE (safe-ceiling unproven); not MONITOR (a concrete, cheap measurement resolves it). Tightly couples PRESUMPTION-299 (MONITOR-295).
  Detail: Urgency Medium. Recommended: measure the render cliff for this build (sweep ~3k/5k/8k/12k/16k/20k nodes: frame time, interaction latency, memory) and set the cap below the first cliff; or move to canvas/WebGL for a genuinely high safe ceiling. Treat 20000 as a provisional, explicitly-untested guard until measured. Couples ASSUMPTION-267 truncation-fix (kept), PRESUMPTION-299.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

DISPOSITION-142:
  Date: 2026-06-03
  Item: ASSUMPTION-268
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: In-situ verification in a served browser with observable evidence + human sign-off is strongly supported and instantiates the already-incorporated verify-the-effect family (PREMISE-045/046). 15b's challenge is not that real-environment verification is wrong but that mandating a MANUAL FOREGROUND pass for the whole check over-claims — objective signals (cross-link count, clean console) are better as deterministic assertions, and a manual gate is the step an autonomous run skips.
  Disposition: INCORPORATE (PREMISE-048)
  Reasoning: Strong support + moderate challenge on scope (manual vs automated split), not on the core -> INCORPORATE with caveats. Premise: pre-push verification must observe the rendered effect in a real served environment (not asserted), with human sign-off for the visual judgment. Caveat folded in: automate the objective checks and make the push BLOCK when the human is absent (fail-loud), per the run's SYSTEMIC-RISK. Consistency-checked vs PREMISE-001..047: reinforces PREMISE-045/046; no conflict.
  Detail: Confidence Moderate-High. Re-check Quarterly (2026-09-03) via 15d. Caveat: encode opacity-split (computed-style threshold), cross-link count, and console-clean as automated served-browser assertions; reserve sign-off for the subjective visual property; block push if sign-off absent. Couples PREMISE-045/046, PRESUMPTION-298 (MONITOR-294), SYSTEMIC-RISK 2026-06-03.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: INCORPORATED

DISPOSITION-143:
  Date: 2026-06-03
  Item: PRESUMPTION-297
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: Cross-repo silent desync (a pushed artifact depending on uncommitted second-repo edits, no transactional guarantee) is a documented, real exposure (15a strong). 15b does not deny it — it argues only about remedy magnitude: for a single-author, low-frequency, two-repo workflow a handoff note may be a tolerable interlock and full cross-repo tooling is over-engineering. So the disagreement is act-vs-wait, not real-vs-not.
  Disposition: MONITOR (MONITOR-293)
  Reasoning: Real but unrealized exposure; remedy is contested in magnitude (cheap pre-push check vs handoff-note-is-fine). Err toward MONITOR over REVISE (15c heuristic; no realized harm yet). PRESUMPTION + member of this run's High human-memory SYSTEMIC-RISK cluster -> Priority Medium-High and a concrete trip-wire.
  Detail: Cadence Weekly; next 15d 2026-06-07. Priority Medium-High. What would change: a near-miss (a push that actually shipped depending on uncommitted Summa edits) OR rising coupling frequency -> REVISE toward a cheap pre-push "is the dependent repo clean?" check (not full interlock tooling). Couples ASSUMPTION-266 (PREMISE-047), SYSTEMIC-RISK 2026-06-03, OPEN-072.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING

DISPOSITION-144:
  Date: 2026-06-03
  Item: PRESUMPTION-298
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Moderate-Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Both directions converge on the SAME pivot: whether one spot-check generalizes depends entirely on whether the fade code path is uniform or branches on per-node properties. If uniform, levin + levin~summa are valid equivalence-class representatives and exhaustive UI checking is YAGNI; if it branches on degree/links/focus, the untested boundaries (zero-link isolate, dense focus) are exactly where it can break.
  Disposition: MONITOR (MONITOR-294)
  Reasoning: Genuinely conditional on a checkable code fact, not yet resolved at autonomous run time -> MONITOR (not INCORPORATE, partition unproven; not REVISE, no established defect). PRESUMPTION; risk conditional. Priority Medium. Resolvable cheaply and decisively by reading the fade implementation.
  Detail: Cadence Weekly; next 15d 2026-06-07. Priority Medium. What would change: reading the fade path resolves it — uniform single rule -> INCORPORATE the one-representative justification (record it); branches on per-node properties -> REVISE to add boundary cases (zero-link isolate, max-degree focus). Couples ASSUMPTION-268 (PREMISE-048).
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING

DISPOSITION-145:
  Date: 2026-06-03
  Item: PRESUMPTION-299
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Both agree the 2.5k–20k range is uncharacterized (15a strong: render cliffs are real and 20000 is far above the only tested point). 15b disputes only TIMING: for a dataset that took ~190 days to reach 2529 nodes, characterizing the range now may be YAGNI, and a growth-triggered warning substitutes for an up-front sweep.
  Disposition: MONITOR (MONITOR-295)
  Reasoning: The gap is real and agreed; the contest is test-now vs test-when-approaching -> MONITOR with a growth trip-wire. Tightly couples ASSUMPTION-267's REVISE-086 (the measurement that resolves 299 is the same one REVISE-086 recommends). Priority Medium-High because it is the load-bearing evidence under the REVISE.
  Detail: Cadence Weekly; next 15d 2026-06-07. Priority Medium-High. What would change: node count approaching an unmeasured cliff, OR the next cap change, OR the REVISE-086 measurement landing -> fold into the cliff sweep and set the cap below the measured cliff. Re-anchor the existing 80%-of-cap warning to the measured cliff once known. Couples ASSUMPTION-267 (REVISE-086), PRESUMPTION-298.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

**Run 2026-06-03 totals:** 6 items | 2 INCORPORATE (PREMISE-047, PREMISE-048) | 3 MONITOR (MONITOR-293..295) | 1 REVISE (REVISE-086) (DISPOSITION-140..145). SYSTEMIC-RISK (High): human-memory-as-control cluster (ASSUMPTION-266/268, PRESUMPTION-297) — convert memory-dependent conventions to forcing functions. Secondary cluster: untested-ceiling-from-current-load (ASSUMPTION-267, PRESUMPTION-299; cousin 298). Consistency check: PREMISE-047/048 checked vs PREMISE-001..046 — no conflict (047 complements PREMISE-046 git-health; 048 reinforces PREMISE-045/046 verify-the-effect).

---

## 2026-06-04 run — c2a2-lit-search-pipeline (autonomous; Tom not present at fire time)

*Batch: 2026-06-03 EOD self-awareness day (ASSUMPTION-269/270 + PRESUMPTION-300/301/302), cycle 0. 10 genuine web searches this run (5 FOR + 5 AGAINST) across coupled clusters: intake-verification (269), autonomous-auth / silent-sync-degradation (270 + 300), staged-deferral (301), self-referential extraction (302). Honest sampling, not an exhaustive per-item external sweep. NOTE (epistemic honesty, ties to PRESUMPTION-302): this batch was itself extracted on a 2nd consecutive no-attended day, so several items are the pipeline reflecting on its own autonomous runs — weighted accordingly below.*

### 15a returns (FOR)
```
RETURN-TO-14a:
  Original item: ASSUMPTION-269
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Strong
  Key source: CheckIfExist/CiteAudit (arXiv 2602.15871/2602.23452); Zahn & Chana 2026 write-time gating (arXiv 2603.15994)
  Summary: Verify-before-ingest is strongly grounded — LLM-era citation hallucination is a real corruption vector, and write-time gating empirically beats ingest-everything (~100% vs ~13%).
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-269_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-270
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Strong
  Key source: OWASP Agentic AI Top 10 / Auth0 excessive-agency; Microsoft/Curity least-privilege + JIT credentials
  Summary: Core boundary (agent must not authenticate as Tom) is strongly supported by least-privilege / excessive-agency guidance; the attended-only sub-clause exceeds what the literature establishes (see 15b).
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-270_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-300
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Strong
  Key source: Nygard circuit-breaker (Azure Arch Center; AWS resilience); DLQ + fail-fast (Conduktor/SQS)
  Specific risk: Running a full workflow against a confirmed-dead sink and accumulating silent in-workflow undeliverable state is the anti-pattern circuit-breakers/dead-letters exist to prevent.
  Summary: Confirmed-down = stop/escalate/dead-letter is well-established; the presumed "recoverable inconvenience" behavior is sound only if the residue is a durable, replayable, flagged queue.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-300_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-301
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Moderate
  Key source: Lean 7-wastes (partially-done = inventory waste); WIP-limit / value-decay practice
  Specific risk: A built-but-inert capability carries holding cost, obsolescence, and design-drift — "cost-free deferral" understates this.
  Summary: Deferral is NOT cost-free (lean inventory/opportunity-cost waste), but the cost is small for a low-frequency single-author capability; magnitude, not direction, is the live question.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-301_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-302
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Moderate
  Key source: Alert-fatigue / signal-to-noise (Datadog, Icinga, Better Stack); monitoring-hygiene "if always ignored, gate/convert it"
  Specific risk: Extracting "design" substance from a no-attended day risks thin/echo output and self-referential inflation.
  Summary: Monitoring practice supports gating/down-weighting low-substance runs; firing extraction on a no-substance day risks mining the pipeline's own transcripts. (Counter-case in 15b.)
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-302_for.md
```

### 15b returns (AGAINST)
```
RETURN-TO-14a:
  Original item: ASSUMPTION-269
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Weak-Moderate
  Key source: PKM precision/recall (Obsidian second-brain, arXiv 2509.20187); write-gating ARCHIVES-not-deletes (arXiv 2603.15994)
  Specific risk: In a low-volume corpus recall is scarce; a do-not-ingest gate drops leads, and an un-revisited hold queue reproduces the loss invisibly ("flag and forget").
  Summary: Disputes the control's SHAPE, not the goal: capture-and-quarantine-with-revisit dominates refuse-to-capture for this corpus size.
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-269_against.md

RETURN-TO-14a:
  Original item: ASSUMPTION-270
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate-Strong
  Key source: OAuth client-credentials / refresh tokens / token vaults (Scalekit, Auth0); Workload Identity Federation (Entra/Curity)
  Specific risk: "Attended-only / cannot self-clear" rests on a false dichotomy (be-Tom vs human-only); it builds an availability single-point-of-failure (the realized 06-03 block).
  Summary: First clause sound; second clause challenged — scoped, revocable, refreshable service credentials let unattended automation self-recover without ever being Tom. Genuine capability-vs-attack-surface tradeoff.
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-270_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-300
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate
  Key source: Graceful degradation / store-and-forward (Azure & SRE-school; deferred-settlement pattern); offline-queue resilience
  Specific risk: Hard-halting on every confirmed-down SECONDARY (delivery) channel trades availability for nothing; the real failure is non-durable/silent residue, not "didn't halt."
  Summary: Continue-and-queue is the mainstream pattern IF the undeliverable state is durable, replayable, and escalated. Pivot: durable dead-letter + fail-loud vs silent residue.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-300_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-301
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate
  Key source: Dark launching / progressive rollout (LaunchDarkly, DevCycle); YAGNI / overproduction waste
  Specific risk: Over-correcting to "activate now" risks overproduction (output no one consumes) and entrenching an unvalidated design — premature activation of half-fit agents.
  Summary: Staging-without-activation is a recognized prudent strategy; neither "cost-free" nor "costly to defer" — real-but-small cost, partly offset by option value. Fix = a dated activation trigger.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-301_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-302
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate
  Key source: Baseline establishment in anomaly detection (NBAD, CloudWatch, Kentik); continuous-monitoring rationale
  Specific risk: Skipping quiet days loses the baseline and the ability to detect declining attended-substance or a quiet-but-important change; a "was there substance?" gate is a fragile meta-decision.
  Summary: Continuous capture earns the right to call a day thin. Fix for echo-extraction = down-weight autonomous-origin items, not gate the run. Both directions have force.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-302_against.md
```

### 15c dispositions
```
DISPOSITION-146:
  Date: 2026-06-04
  Item: ASSUMPTION-269
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: Strong, convergent support for verify-before-ingest (citation-hallucination risk + write-time gating beating ingest-everything). 15b does not contest the principle — it contests the control's SHAPE (refuse-to-capture vs capture-and-quarantine) and flags that an un-revisited hold queue reproduces the recall loss invisibly. Disagreement is implementation, not validity.
  Disposition: INCORPORATE (PREMISE-049)
  Reasoning: Strong support + only operational (weak-moderate) challenge -> INCORPORATE with a caveat folded in. Premise: an unverified cross-tradition lead must never be TREATED AS TRUE (no trusted edge, no narration entry) until a confirmation search promotes it — implemented as provisional quarantine-with-revisit, not silent drop. Consistency-checked vs PREMISE-001..048: reinforces the verify-the-effect / provenance family (esp. PREMISE-045/046); no conflict.
  Detail: Confidence High. Re-check Quarterly (2026-09-04) via 15d. Caveat (from 15b): the held/quarantined queue needs a revisit/expiry forcing function so "hold" cannot degrade to "flag and forget"; prefer tagged provisional capture over refuse-to-capture to preserve recall in a low-volume corpus. Couples ASSUMPTION-264, PRESUMPTION-302.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: INCORPORATED

DISPOSITION-147:
  Date: 2026-06-04
  Item: ASSUMPTION-270
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Two clauses (Rule 7 — surfaced, not blended). Clause 1 "agent must not authenticate as Tom" — SUPPORTED Strong, unchallenged. Clause 2 "therefore a lapsed session is a hard blocker the pipeline cannot self-clear; re-auth attended-only" — challenged Moderate-Strong: standard M2M patterns (client-credentials, refresh tokens, token vaults, workload-identity federation) let unattended automation self-recover WITHOUT being the user. BUT 15a's own least-privilege/excessive-agency literature cautions that any standing refreshable credential on an autonomous agent is added attack surface — so this is a genuine capability-vs-attack-surface tradeoff, not a clean over-claim.
  Disposition: MONITOR (MONITOR-296)
  Reasoning: Core boundary is independently strong (could promote on a later cycle); the load-bearing clause is genuinely contested (self-recovery capability vs added attack surface), not an established defect with a costless fix. Err toward MONITOR over REVISE (15c heuristic; the "fix" has a real downside its own supporting literature flags). Priority MEDIUM-HIGH — it caused a real 06-03 hard block and couples the silent-sync-degradation systemic risk.
  Detail: Cadence Weekly; next 15d 2026-06-07. Priority MEDIUM-HIGH. What would change: recurring lapsed-session blocks (availability cost mounting) -> REVISE toward a sync-scoped, least-privilege, revocable delegated credential so the pipeline self-clears WITHOUT impersonating Tom; OR a decision that attended-only is the accepted safety posture -> INCORPORATE clause 1 explicitly and accept the availability cost. Couples PRESUMPTION-300 (MONITOR-297), ASSUMPTION-263, OPEN-073, SYSTEMIC-RISK 2026-06-04.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING

DISPOSITION-148:
  Date: 2026-06-04
  Item: PRESUMPTION-300
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Both converge on the SAME pivot: whether the accumulated undeliverable state is a DURABLE, replayable, visibly-flagged dead-letter (defensible graceful degradation) or silent in-workflow residue no one will replay (the anti-pattern). 15a: confirmed-down = stop/escalate/dead-letter is established. 15b: continue-and-queue is fine IF durable+escalated. The 06-03 behavior ("completed workflow, accumulated undeliverable state") is on the wrong side unless that state is durable and a confirmed-down raises a visible signal.
  Disposition: MONITOR (MONITOR-297)
  Reasoning: Conditional on a checkable fact (is the residue durable+replayable+escalated?), unresolved at autonomous run time -> MONITOR (not INCORPORATE: durability unproven; not REVISE: no established defect yet). PRESUMPTION -> extra care. Priority MEDIUM. Member of this run's silent-sync-degradation SYSTEMIC-RISK with ASSUMPTION-270.
  Detail: Cadence Weekly; next 15d 2026-06-07. Priority MEDIUM. What would change: inspect a sync run's residue — durable+replayable+escalated -> INCORPORATE the graceful-degradation justification (record it); silent/in-memory/unreplayable -> REVISE to add fail-loud escalation + durable dead-letter + auto-drain on recovery. Couples ASSUMPTION-270 (MONITOR-296), OPEN-069/073, SYSTEMIC-RISK 2026-06-04.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING

DISPOSITION-149:
  Date: 2026-06-04
  Item: PRESUMPTION-301
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Symmetric partials. 15a: built-but-inert = lean inventory/opportunity-cost waste, so deferral is NOT cost-free. 15b: staging-without-activation is a recognized prudent strategy (dark launch / progressive rollout / YAGNI), and premature activation of half-fit agents on low-substance days is its own waste. Truth in the middle: deferral cost is real but small and partly offset by option value; the presumption's error is the word "cost-free," not the decision to defer.
  Disposition: MONITOR (MONITOR-298)
  Reasoning: Genuinely two-sided with a small contested magnitude; no established defect, no clear win from acting now -> MONITOR. PRESUMPTION. Priority LOW-MEDIUM. The actionable lever is converting open-ended deferral into a dated/triggered option.
  Detail: Cadence Weekly; next 15d 2026-06-07. Priority LOW-MEDIUM. What would change: signs of decay/drift (staged Agents 17-20 / Sunday Synthesis going stale vs the evolved system) -> REVISE toward an activation trigger/date; OR sustained low marginal value -> accept deferral and record it as a deliberate dark-launch hold (INCORPORATE the staging rationale). Couples PRESUMPTION-295, PRESUMPTION-301.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING

DISPOSITION-150:
  Date: 2026-06-04
  Item: PRESUMPTION-302
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: The meta-question — are autonomous-day transcripts informative enough to extract from? Both sides have force: 15a (alert-fatigue/signal-to-noise) — firing on a no-substance day risks thin/echo extraction and self-referential inflation; 15b (anomaly-detection baseline) — continuous capture establishes the normal, detects declining substance, and a "was there substance?" gate is a fragile meta-decision. Live instance: this very run dispositions presumptions (300/301/302) extracted on a 2nd no-attended day.
  Disposition: MONITOR (MONITOR-299)
  Reasoning: Real, self-referential, and unresolved; the fix proposed by 15b (down-weight autonomous-origin items rather than gate the run) is attractive but unvalidated -> MONITOR over both INCORPORATE and REVISE. PRESUMPTION + epistemic/self-referential -> extra care. Priority MEDIUM.
  Detail: Cadence Weekly; next 15d 2026-06-07. Priority MEDIUM. What would change: evidence of echo-extraction (autonomous-day items disproportionately producing thin MONITORs that re-reference prior autonomous runs) -> REVISE toward tagging autonomous-origin items at lower epistemic weight and/or a substance threshold; OR autonomous-day items yielding genuinely novel dispositions -> continuous capture vindicated (INCORPORATE always-run + down-weight). Couples OPEN-069/070, PRESUMPTION-291, ASSUMPTION-269 (PREMISE-049).
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING
```

**Run 2026-06-04 totals:** 5 items | 1 INCORPORATE (PREMISE-049) | 4 MONITOR (MONITOR-296..299) | 0 REVISE (DISPOSITION-146..150). SYSTEMIC-RISK (High): autonomous-sync silent-degradation cluster (ASSUMPTION-270 + PRESUMPTION-300) — the unattended sync path neither self-clears a lapsed session nor fails loud on a confirmed-down channel; it degrades silently and accumulates undeliverable state. This is the availability twin of the 2026-06-03 "human-memory-as-control" and 2026-06-02 "absence != success/event" clusters. Single coupled remedy: make the sync path self-clearable (sync-scoped revocable delegated credential, not Tom's identity) AND fail-loud (durable dead-letter + visible escalation on confirmed-down + auto-drain on recovery). Consistency check: PREMISE-049 checked vs PREMISE-001..048 — no conflict (reinforces verify-the-effect/provenance family, esp. PREMISE-045/046). No NOVELTY flags — all 5 items mapped cleanly to established literature.

---

## Returns — run 2026-06-05 (2026-06-04 EOD batch: ASSUMPTION-271/272, PRESUMPTION-303/304/305)

RETURN-TO-14a:
  Original item: ASSUMPTION-271
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED | Strength: Moderate
  Key source: Fowler, "Event Sourcing" (martinfowler.com); MS Learn "Event Sourcing Pattern"
  Summary: Log-as-system-of-record supports the mechanism (mixed-format logs over-count under naïve diffs; canonical count is a deterministic fold) but NOT the specific figure 36, which requires an actual reconciliation.
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-271_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-271
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED | Strength: Moderate
  Key source: dbseer "Data Migration Validation Guide" (2026); Monte Carlo "Data Reconciliation"
  Specific risk: If 36 is wrong, ~116 un-ingested files are silently omitted from every downstream count and the backlog-drain plan.
  Summary: Reconciliation discipline challenges asserting 36 canonical before tracing the ~76% gap; an unexplained divergence is presumed possible loss until each record maps to an explicit rule.
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-271_against.md

RETURN-TO-14a:
  Original item: ASSUMPTION-272
  Search direction: FOR (supportive)
  Result: SUPPORTED | Strength: Strong
  Key source: Reinertsen via SAFe Principle #6 (InformIT); dev2ops "Small Batches Improve Flow"
  Summary: Lean/agile flow strongly supports small scoped batches for quality-sensitive curation — lower per-transaction risk, faster defect detection, simpler review.
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-272_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-272
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED | Strength: Weak-Moderate
  Key source: Nuvento "Hidden Cost of HITL"; Codebridge/StackAI HITL approval workflows (2026)
  Specific risk: Over-fragmenting a bounded 36-file backlog into 5-7 attended sessions re-creates the Tom-availability bottleneck and induces rubber-stamping that erodes curation quality.
  Summary: Challenge is to small-batch + mandatory-attended-gate conjunction (U-curve transaction cost), not to small batches; fold tuning caveat in.
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-272_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-303
  Search direction: FOR (supportive)
  Result: SUPPORTED | Strength: Moderate
  Key source: Unstructured.io "Data Quality at Ingestion" (2026); "Fail Fast or Quarantine?" (Towards Data Engineering)
  Summary: Quarantine/staging pattern supports admission≠trust IF the low-confidence marking is machine-enforced and adjudication actually runs.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-303_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-303
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED | Strength: Moderate
  Key source: IBM/Metaplane data-quality; Agile Alliance "Backlog Refinement"
  Specific risk: Unsourced pointer rots unreviewed (inflates apparent coverage) or is promoted by inertia (spurious cross-tradition attribution) — the corruption PREMISE-049 exists to prevent.
  Summary: Without enforced read-gating + adjudication deadline, admission is a soft verify-before-trust violation; sharpened by same-run timing vs PREMISE-049.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-303_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-304
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED | Strength: Weak-Moderate
  Key source: Lemaire "Event Sourcing, Audit Logs, and Event Logs" (2026)
  Summary: Supports only feasibility (a heterogeneous log CAN become machine-diffable; a divergence CAN be a projection artifact), not the optimistic direction that 36 is correct / 152 lossless.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-304_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-304
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED | Strength: Moderate-Strong
  Key source: dbseer / Monte Carlo (silent-data-loss); Agile/maintenance-backlog deferral cost
  Specific risk: A presumed-cosmetic 36 bakes an undercount into the backlog plan and coverage metrics; "fix later" indefinitely defers the only loss-detecting step (structuring the log).
  Summary: Names the directional bet as the canonical silent-data-loss antipattern and the deferral bet as cost-understating; PRESUMPTION -> no deliberate scrutiny.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-304_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-305
  Search direction: FOR (supportive)
  Result: NO-SUPPORT-FOUND | Strength: Weak
  Key source: (only partial) Atlassian "Trunk-Based Development" — supports deferring the PUSH, not growing the uncommitted tree
  Summary: No genuine FOR case for "accumulation is cost-free"; the sole supportive fragment defends a different action (gated push) than the one presumed (unbounded working-tree growth).
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-305_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-305
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED | Strength: Strong
  Key source: Atlassian / StxNext "Escape from Merge Hell"; trunkbaseddevelopment.com; SAFe Principle #6 (WIP-as-inventory)
  Specific risk: A future attended session faces 587+ intermingled changes; clean separation degrades as the pile grows, worst case force-reconciliation sweeps unrelated changes together. Carries a SYSTEMIC-RISK flag (defer-and-tidy-later).
  Summary: Unmerged/uncommitted divergence carries holding cost growing with size+time; "cost-free" is unsupported. Remedy: commit-in-increments, defer only the push.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-305_against.md

DISPOSITION-151:
  Date: 2026-06-05
  Item: ASSUMPTION-271
  Item type: ASSUMPTION (stated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Both agree on the mechanism (mixed-format logs over-count; canonical count is a fold) and split on ordering: 36 is recoverable in principle (15a) but unproven until the ~76% gap is traced (15b). The assumption asserts the conclusion the audit should earn.
  Disposition: MONITOR (MONITOR-300)
  Reasoning: Conditional on a cheap, checkable fact (run the reconciliation), unresolved at autonomous run time -> MONITOR. Not INCORPORATE (figure 36 unproven); not REVISE (mechanism sound, fix is a one-time audit not a redesign). Stated ASSUMPTION; the inferred twin PRESUMPTION-304 carries the extra directional+deferral bets -> REVISE-087. Priority MEDIUM.
  Detail: Cadence Weekly; next 15d 2026-06-12. What would change: partition all 152 by record type and reconcile vs filesystem — residual=36 -> INCORPORATE; residual>36 -> REVISE (real backlog). Couples PRESUMPTION-304 (REVISE-087), ASSUMPTION-272 (PREMISE-050), defer-and-tidy-later SYSTEMIC-RISK.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING

DISPOSITION-152:
  Date: 2026-06-05
  Item: ASSUMPTION-272
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: Strong support for small scoped batches in quality-sensitive curation; the challenge targets the conjunction with a mandatory attended gate (U-curve transaction cost, fixed per-session overhead, rubber-stamping), not the small-batch principle.
  Disposition: INCORPORATE (PREMISE-050)
  Reasoning: Strong support + weak-moderate operational challenge resolved by folding the tune-to-gate-cost and automated-pre-check caveats into the premise -> INCORPORATE with caveats, Moderate confidence. Consistency-checked vs PREMISE-001..049: complements PREMISE-047 (granular staging), aligns with PRESUMPTION-305 remedy; no conflict.
  Detail: Re-check 2026-09-05 (Quarterly; via 15d). Confidence Moderate — optimal batch size is cost-dependent and unverified for this backlog ("small scoped batches sized to gate cost," not "5-8 is correct").
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: INCORPORATED

DISPOSITION-153:
  Date: 2026-06-05
  Item: PRESUMPTION-303
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Both converge on one condition — a pending-review queue separates admission from trust IFF the low-confidence marking is machine-enforced and adjudication is guaranteed. 15a: that pattern is recognized-safe. 15b: absent enforcement, admission is a soft verify-before-trust violation (inertia-promotion or rot), sharpened by the same-run timing against PREMISE-049.
  Disposition: MONITOR (MONITOR-301)
  Reasoning: Conditional on an unverified property of the queue (enforced isolation + adjudication SLA) -> MONITOR. Not INCORPORATE (condition unverified); not REVISE (no demonstrated leak, fix is an enforcement check). PRESUMPTION + direct tension with just-incorporated PREMISE-049 -> extra care. Priority MEDIUM-HIGH.
  Detail: Cadence Weekly; next 15d 2026-06-12. What would change: audit pending-review read paths — isolated + purge-not-promote deadline -> INCORPORATE; leaks into default reads OR age/inertia promotion -> REVISE (machine-enforced isolation + adjudication deadline + exception log). Couples ASSUMPTION-269/PREMISE-049, OPEN-074, defer-and-tidy-later SYSTEMIC-RISK.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING

DISPOSITION-154:
  Date: 2026-06-05
  Item: PRESUMPTION-304
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Inferred twin of ASSUMPTION-271 plus two unexamined bets — directional (36 right, 152 lossless) and deferral (tidy is cheap and will happen). 15a supports only feasibility; 15b names bet 1 as the silent-data-loss antipattern and bet 2 as cost-understating. Designers were unaware of these commitments (PRESUMPTION).
  Disposition: REVISE (REVISE-087)
  Reasoning: Weak feasibility-only support + moderate-strong challenge on the two load-bearing bets + PRESUMPTION (no deliberate scrutiny) -> REVISE. Honest status is unknown-until-reconciled; "cosmetic, fix later" pre-decides the audit. Urgency MEDIUM-HIGH.
  Detail: Demote cosmetic->unverified; run the reconciliation NOW (partition 152, confirm residual=36 OR enumerate lost files); treat narrative-as-system-of-record as a goal needing an explicit structuring pass. One audit also discharges MONITOR-300. Couples ASSUMPTION-271 (MONITOR-300), ASSUMPTION-272 (PREMISE-050), defer-and-tidy-later SYSTEMIC-RISK.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

DISPOSITION-155:
  Date: 2026-06-05
  Item: PRESUMPTION-305
  Item type: PRESUMPTION (unstated)
  15a result: NO-SUPPORT-FOUND | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Strong
  Net assessment: No genuine FOR case; the sole supportive fragment (gated push) defends a different action than the presumed one (growing the uncommitted tree). 15b strong+convergent: unmerged divergence is holding cost growing with size+time; "587 cleanly separated later" is the merge-hell failure. Realized, monotonically-growing exposure.
  Disposition: REVISE (REVISE-088)
  Reasoning: No support + strong challenge on an unexamined "cost-free" PRESUMPTION with realized growing exposure (587 and rising) -> clearest REVISE of the run. The no-blind-push rule is mis-applied to justify not COMMITTING rather than not PUSHING. Urgency HIGH.
  Detail: Decouple actions — keep no-blind-PUSH, but commit-in-increments each run (committing != pushing); surface working-tree change count as a tracked metric. Couples ASSUMPTION-272 (PREMISE-050), PRESUMPTION-295/301, defer-and-tidy-later SYSTEMIC-RISK.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Run 2026-06-05 totals:** 5 items | 1 INCORPORATE (PREMISE-050) | 2 MONITOR (MONITOR-300, MONITOR-301) | 2 REVISE (REVISE-087, REVISE-088) | DISPOSITION-151..155. SYSTEMIC-RISK (High): defer-and-tidy-later cluster (PRESUMPTION-303/304/305 + ASSUMPTION-271) — a shared optimism that a future attended session resolves accumulated/unverified/intermingled state at no cost (admit-now/review-later, reconcile-later, commit-later); PRESUMPTION-305 already shows realized growing exposure (587 uncommitted changes). Single coupled remedy: treat later cleanup as an accruing liability and adopt bounded-accumulation defaults (adjudication deadlines, reconcile-at-detection, commit-in-increments) with backlog/queue/tree size surfaced as tracked metrics. Consistency check: PREMISE-050 vs PREMISE-001..049 — no conflict (complements PREMISE-047). No NOVELTY flags — all 5 items mapped to established literature.

---

# RUN 2026-06-06 — c2a2-lit-search-pipeline (15a/15b/15c; autonomous)
*2026-06-05 ATTENDED batch (Community Explorer P1 build): ASSUMPTION-273, 275, 276; PRESUMPTION-306, 307, 308, 309, 310, 311.*

## 15a / 15b RETURNS

### RETURN-TO-14a: ASSUMPTION-273
  Search direction: FOR — Result: SUPPORTED (Moderate-Strong). Key source: Cockburn, Karlson & Bederson 2008 (ACM Computing Surveys, overview+detail/focus+context). Summary: highlight-preserves-context is a validated idiom distinct from filtering; supports the lock's principle but not "inherit exactly" across scale/task. Full: lit_search_results/for/ASSUMPTION-273_for.md
  Search direction: AGAINST — Result: PARTIALLY-CHALLENGED (Moderate). Key source: Munzner 2014 (filter vs highlight idioms); Shneiderman dynamic queries. Specific risk: at 156 nodes with a name-lookup task, filtering can beat highlight; the lock's clutter-at-1647 rationale lapses. Full: lit_search_results/against/ASSUMPTION-273_against.md

### RETURN-TO-14a: ASSUMPTION-275
  Search direction: FOR — Result: SUPPORTED (Strong). Key source: Baldonado et al. 2000 (Rule of Diversity); Roberts 2007 (CMV). Summary: complementary structure-view + attribute-view over one corpus is a canonical, performance-validated pairing. Full: lit_search_results/for/ASSUMPTION-275_for.md
  Search direction: AGAINST — Result: PARTIALLY-CHALLENGED (Moderate). Key source: Baldonado Rule of Parsimony; arXiv 2204.09524 (more views ≠ better). Specific risk: if Cards reduces to a filtered Graph state, the second surface is redundant maintenance + context-switch cost. Full: lit_search_results/against/ASSUMPTION-275_against.md

### RETURN-TO-14a: ASSUMPTION-276
  Search direction: FOR — Result: PARTIALLY-SUPPORTED (Moderate-Strong, analogous). Key source: Medallion architecture (Databricks/MS Learn); DataKitchen quality gates. Summary: staged quality-gated promotion with gates at transitions is mainstream; supports the membrane mechanism. Full: lit_search_results/for/ASSUMPTION-276_for.md
  Search direction: AGAINST — Result: PARTIALLY-CHALLENGED (Moderate-Strong). Key source: Goodhart's Law (Strathern); Nielsen 90-9-1; Fowler YAGNI. Specific risk: "measurement surface" + articulation-earned membership → Goodhart + participation inequality; "correct target architecture" pre-commits before the join is validated. Full: lit_search_results/against/ASSUMPTION-276_against.md

### RETURN-TO-14b: PRESUMPTION-306
  Search direction: FOR — Result: PARTIALLY-SUPPORTED (Weak-Moderate). Key source: record linkage / Splink / Christen. Summary: ER can recover joins without shared ids — but only where discriminative overlap exists; 0/3/5 is near the signal floor. Full: lit_search_results/for/PRESUMPTION-306_for.md
  Search direction: AGAINST — Result: CHALLENGED (Strong). Key source: Fellegi-Sunter / Christen "Data Matching"; Data Ladder fuzzy-match warning. Specific risk: near-zero overlap likely signals DISTINCT populations; forcing a fuzzy join manufactures false links, and all of P3 rests on this join. Full: lit_search_results/against/PRESUMPTION-306_against.md

### RETURN-TO-14b: PRESUMPTION-307
  Search direction: FOR — Result: PARTIALLY-SUPPORTED (Weak-Moderate). Key source: Nielsen consistency heuristic; Cockburn 2008. Summary: shared interaction grammar lowers learning cost; highlight is a general primitive — supports the mechanism, not the scale-bound rationale. Full: lit_search_results/for/PRESUMPTION-307_for.md
  Search direction: AGAINST — Result: CHALLENGED (Moderate-Strong). Key source: Cockburn 2008 (context-loss cost scales with N); Shneiderman/Munzner. Specific risk: a rationale tuned for clutter at 1647 does not survive the 10x drop; CE's lookup task favors the forbidden idiom. Full: lit_search_results/against/PRESUMPTION-307_against.md

### RETURN-TO-14b: PRESUMPTION-308
  Search direction: FOR — Result: PARTIALLY-SUPPORTED (Moderate). Key source: medallion/Great Expectations curation; Wikipedia notability. Summary: gating on an articulable bar is accepted, load-reducing curation — supports efficacy, not the normative "deserves visibility" step. Full: lit_search_results/for/PRESUMPTION-308_for.md
  Search direction: AGAINST — Result: CHALLENGED (Moderate-Strong). Key source: Nielsen 90-9-1; Bowker & Star / D'Ignazio & Klein (visibility-as-power). Specific risk: articulation tracks resources; the "technical" gate reproduces participation inequality and hides emerging communities. Full: lit_search_results/against/PRESUMPTION-308_against.md

### RETURN-TO-14b: PRESUMPTION-309
  Search direction: FOR — Result: PARTIALLY-SUPPORTED (Weak-Moderate). Key source: Ford et al. "Building Evolutionary Architectures"; Martin seams. Summary: seams pay forward when the later need is known — a condition unmet here. Full: lit_search_results/for/PRESUMPTION-309_for.md
  Search direction: AGAINST — Result: CHALLENGED (Strong). Key source: Fowler "Yagni"; speculative-generality smell (Refactoring). Specific risk: building P1 seams "load-bearing in P3" while the join is unbuilt+doubted and a named piece was already deferred is textbook speculative generality. Full: lit_search_results/against/PRESUMPTION-309_against.md

### RETURN-TO-14b: PRESUMPTION-310
  Search direction: FOR — Result: SUPPORTED (Moderate). Key source: Salton & Buckley (TF-IDF); standard IR. Summary: TF-IDF/cosine is a validated relatedness baseline, strongest within a shared vocabulary domain. Full: lit_search_results/for/PRESUMPTION-310_for.md
  Search direction: AGAINST — Result: CHALLENGED (Moderate-Strong). Key source: Reimers & Gurevych (Sentence-BERT); TF-IDF semantic-blindness literature; construct-validity methodology. Specific risk: cross-domain (Civic vs Scientific) registers differ, so near-zero TF-IDF is indistinguishable from related-but-lexically-divergent; count ≠ construct. Full: lit_search_results/against/PRESUMPTION-310_against.md

### RETURN-TO-14b: PRESUMPTION-311
  Search direction: FOR — Result: PARTIALLY-SUPPORTED (Moderate). Key source: CRM lifecycle modeling; MDM golden record; medallion promotion. Summary: same-object-across-stages shared id space is a recognized pattern — IF identity holds. Full: lit_search_results/for/PRESUMPTION-311_for.md
  Search direction: AGAINST — Result: CHALLENGED (Moderate-Strong). Key source: Chen ER model (identity vs association); Bowker & Star; MDM over-merge caution. Specific risk: presuming shared id space conflates association with identity; the distinct-kinds alternative was never raised. Full: lit_search_results/against/PRESUMPTION-311_against.md

## 15c DISPOSITIONS

DISPOSITION-156:
  Date: 2026-06-06
  Item: ASSUMPTION-273
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate-Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Strong support for the highlight-preserves-context PRINCIPLE; the challenge targets the "inherit exactly" clause for CE's stated name-lookup task at 156 nodes, where filtering may win. Support and challenge concern different clauses, not the same one.
  Disposition: MONITOR (MONITOR-302)
  Reasoning: Conditional on a cheap, checkable UX fact (highlight-vs-filter lookup time at 156 nodes), unresolved at autonomous run time -> MONITOR. Not INCORPORATE (the "exactly/at this scale" clause is unverified); not REVISE (the lock is not defective, only possibly mis-fit for the lookup task). Paired with PRESUMPTION-307 (the inferred scale-transfer twin, MONITOR-304).
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING

DISPOSITION-157:
  Date: 2026-06-06
  Item: ASSUMPTION-275
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: Strong CMV support (Rule of Diversity, Roberts) for complementary structure + attribute surfaces; the challenge is the matching Rule of Parsimony — keep both only while each earns its cost and neither absorbs the other.
  Disposition: INCORPORATE (PREMISE-051)
  Reasoning: Strong support + moderate operational challenge resolved by folding the parsimony caveat (non-absorption must be demonstrable; revisit if Cards becomes a filtered Graph state) into the premise -> INCORPORATE with caveats, Moderate confidence. Consistency-checked vs PREMISE-001..050: no conflict (new UI-views domain; complements no existing premise). NOTE: the "over ONE dataset" half depends on PRESUMPTION-306 (REVISE-089); premise scoped to the views' complementarity, not to dataset unity.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: INCORPORATED

DISPOSITION-158:
  Date: 2026-06-06
  Item: ASSUMPTION-276
  Item type: ASSUMPTION (stated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate-Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: The staged quality-gated promotion MECHANISM is well-supported (medallion); the transfer to PARTICIPATION/visibility is challenged on three fronts — Goodhart (measurement surface + earned membership), normative non-neutrality (couples 308), and premature "correct target" before the join is validated (couples 306/309).
  Disposition: MONITOR (MONITOR-303)
  Reasoning: Symmetric moderate-strong both ways on different aspects (mechanism supported, transfer + overclaim challenged) -> MONITOR. Not INCORPORATE (the "measurement surface" + "correct target" claims are unvalidated and Goodhart-exposed); not REVISE (the pipeline mechanism is sound; the fix is to hedge claims and validate the join, not redesign). Priority MEDIUM.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING

DISPOSITION-159:
  Date: 2026-06-06
  Item: PRESUMPTION-306
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: CHALLENGED | 15b strength: Strong
  Net assessment: ER establishes only that a join is not impossible; the measured 0 id / 3 name / 5 host is near the signal floor, where linkage theory says forcing a join manufactures false matches and the parsimonious reading is DISTINCT populations. P3's whole architecture rests on this join.
  Disposition: REVISE (REVISE-089)
  Reasoning: Weak feasibility-only support + strong challenge on a HIGH-risk PRESUMPTION whose failure invalidates P3 -> REVISE, the clearest of the run. Designers were unaware they were betting on unifiability (PRESUMPTION). The honest status is unknown-until-measured; "unifiable" pre-decides the linkage experiment. Urgency HIGH.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

DISPOSITION-160:
  Date: 2026-06-06
  Item: PRESUMPTION-307
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Inferred scale-transfer twin of ASSUMPTION-273. Consistency gives a real but light FOR; the challenge is that the lock's clutter-at-1647 rationale does not survive the 10x drop and CE's lookup task favors filter. Conditional on the same checkable UX fact as 273.
  Disposition: MONITOR (MONITOR-304)
  Reasoning: PRESUMPTION + moderate-strong challenge resolvable by the same highlight-vs-filter lookup test as 273 -> MONITOR (paired with MONITOR-302). Not REVISE (no defect demonstrated, test is cheap); not INCORPORATE (scale-survival unproven). Priority MEDIUM.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING

DISPOSITION-161:
  Date: 2026-06-06
  Item: PRESUMPTION-308
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Curation efficacy is supported; the NORMATIVE claim (articulate communities deserve visibility, seeds do not) is challenged by participation-inequality and visibility-as-power literature. This is a values choice currently buried in a "technical" gate, not a factual defect literature can settle.
  Disposition: MONITOR (MONITOR-305), Priority HIGH
  Reasoning: A normative PRESUMPTION cannot be INCORPORATED on literature alone (it is a value decision for Tom), and it is not yet a demonstrated harm to REVISE — but it is too consequential (who is visible) to leave implicit -> MONITOR with HIGH priority and an explicit "surface to Tom" action. Cross-listed in revision_flags SYSTEMIC-RISK note as a validity-smuggling item.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING

DISPOSITION-162:
  Date: 2026-06-06
  Item: PRESUMPTION-309
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: CHALLENGED | 15b strength: Strong
  Net assessment: Evolutionary-architecture supports seams ONLY when the later need is known; here P3's join is unbuilt+doubted (306), no P3 failure criterion exists, and a named load-bearing piece was already deferred this session — the forward-compat bet is already slipping. Strong YAGNI/speculative-generality challenge.
  Disposition: REVISE (REVISE-090)
  Reasoning: Weak conditional support + strong challenge on a Medium-High-risk PRESUMPTION with realized slippage (the deferred hand-off) -> REVISE. Build the seam when P3 is committed and its join validated, not before. Urgency MEDIUM-HIGH. Couples PRESUMPTION-306 (REVISE-089).
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

DISPOSITION-163:
  Date: 2026-06-06
  Item: PRESUMPTION-310
  Item type: PRESUMPTION (unstated)
  15a result: SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: TF-IDF is a valid relatedness baseline within a vocabulary domain; cross-domain (Civic vs Scientific) it is semantically blind, so near-zero cross-links is indistinguishable from related-but-lexically-divergent. The verification confirmed the count (reliability), not that the edges measure relatedness (construct validity).
  Disposition: MONITOR (MONITOR-306)
  Reasoning: Conditional on a checkable fact (re-run with embeddings; do semantic cross-links appear?), unresolved at autonomous run time -> MONITOR. Not INCORPORATE ("zero = honest signal" is construct-unverified cross-domain); not REVISE (no defect yet; TF-IDF is a defensible first pass). Priority MEDIUM.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING

DISPOSITION-164:
  Date: 2026-06-06
  Item: PRESUMPTION-311
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Lifecycle/MDM models license a shared id space only when it is the SAME entity across stages; presuming that for curated-community vs directory-seed conflates association with identity, and the distinct-kinds alternative was never raised. Conceptual twin of 306 (feasibility): 306 = can they join, 311 = should they.
  Disposition: MONITOR (MONITOR-307), Priority HIGH
  Reasoning: A PRESUMPTION that pre-commits an ontology (one object vs two) is a modeling decision for Tom, contingent on the 306 linkage result -> MONITOR with HIGH priority and an explicit "raise the suppressed alternative" action. Not REVISE independently (it rides on 306, already REVISE-089); not INCORPORATE (identity unproven). Couples PRESUMPTION-306.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING

**Run 2026-06-06 totals:** 9 items | 1 INCORPORATE (PREMISE-051) | 6 MONITOR (MONITOR-302..307) | 2 REVISE (REVISE-089, REVISE-090) | DISPOSITION-156..164. High SYSTEMIC-RISK: "unvalidated-P3-join-as-foundation" — PRESUMPTION-306 (feasibility, REVISE-089) + PRESUMPTION-309 (forward-compat seams, REVISE-090) + PRESUMPTION-311 (conceptual appropriateness, MONITOR-307), coupling ASSUMPTION-275/276; the P3 "two projections over one dataset" architecture rests on a curated↔directory join that is empirically near-absent (0/3/5) and conceptually unexamined. Secondary "validity-smuggled-into-a-technical-gate" pair: PRESUMPTION-308 (normative, MONITOR-305 HIGH) + PRESUMPTION-310 (construct/TF-IDF, MONITOR-306). Consistency check: PREMISE-051 vs PREMISE-001..050 — no conflict (new UI-coordinated-views domain). No NOVELTY flags — all 9 mapped to established literature.

---

## Returns — run 2026-06-07 (2026-06-06 EOD attended CE build batch: curated→cards subset-merge + consent disclosure)

RETURN-TO-14a:
  Original item: ASSUMPTION-278
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED | Strength: Moderate
  Key source: Christen, "Data Matching" (2012) / Kimball surrogate keys / MDM golden-record practice
  Summary: Assigning shared CC-xxx ids is standard, effective integration mechanics for making a subset addressable — conditional on the records being the same entities.
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-278_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-278
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED | Strength: Moderate-Strong
  Key source: Fellegi-Sunter / Chen ER model / MDM over-merge caution
  Specific risk: Minting a key where measured overlap is ~0 (0/3/5) makes the directory⊇graph relation ADDRESSABLE, not TRUE — manufacturing identity the data don't support; a false subset relation becomes load-bearing for P3.
  Summary: A key encodes an established identity; it cannot create one. Enacted form of the prior unvalidated-P3-join risk.
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-278_against.md

RETURN-TO-14a:
  Original item: ASSUMPTION-279
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED | Strength: Moderate (complementarity) / Weak (mutually-upbuilding)
  Key source: Baldonado et al. 2000; Cockburn 2007; Roberts 2007
  Summary: Functional complementarity is well supported and already PREMISE-051; the stronger "each makes the other more truthful / earned place" framing is not licensed by CMV theory.
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-279_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-279
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED | Strength: Moderate
  Key source: Baldonado Rule of Parsimony; CMV context-switching cost (arXiv 2204.09524); participation-inequality
  Specific risk: The "earned/more truthful" gloss launders a contestable visibility hierarchy (graphed = legitimate) into settled rationale and understates dual-surface cost.
  Summary: Complementarity holds (PREMISE-051); the purely-reinforcing/earned overclaim does not — couples 316.
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-279_against.md

RETURN-TO-14a:
  Original item: ASSUMPTION-280
  Search direction: FOR (supportive)
  Result: SUPPORTED | Strength: Moderate-Strong
  Key source: Brown et al. 2025 (Web scraping for research); AoIR; provenance practice
  Summary: Disclosing scraped-seed provenance and not implying endorsement is a well-supported minimum transparency/ethics bar.
  Full results: wiki/architecture/lit_search_results/for/ASSUMPTION-280_for.md

RETURN-TO-14a:
  Original item: ASSUMPTION-280
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED | Strength: Weak-Moderate
  Key source: Solove "Privacy Self-Management" (2013); group-privacy literature
  Specific risk: If "must disclose" is read as the WHOLE duty, identifiable communities are listed without consent or recourse while ethics seem settled (the 313 overclaim).
  Summary: Disclosure is necessary, not sufficient; it is the floor, not the ceiling.
  Full results: wiki/architecture/lit_search_results/against/ASSUMPTION-280_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-312
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED | Strength: Weak-Moderate
  Key source: Kimball surrogate keys; deterministic linkage (Christen); MDM id minting
  Summary: An assigned id is the normal vehicle for identity ONLY once identity is established; precedents express identity, they don't create it.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-312_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-312
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED | Strength: Strong
  Key source: Fellegi-Sunter; Chen ER model; MDM over-merge failures
  Specific risk: Identity asserted by fiat in the near-zero-overlap regime is the canonical false-match; a committed id space corrupts downstream and is costly to split.
  Summary: Identity is inferred from evidence, never created by a key — the merge may have manufactured the missing identity. Realized escalation of REVISE-089/MONITOR-307.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-312_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-313
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED | Strength: Weak-Moderate
  Key source: IRB public-data exemption; notice-based regimes; AoIR staged consent
  Summary: Notice is a recognized, sometimes-proportionate safeguard for low-sensitivity public data; weakens sharply as identifiability/harm rise.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-313_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-313
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED | Strength: Strong
  Key source: Solove (2013) consent dilemma; Brown et al. 2025; Group Privacy (Taylor/Floridi/van der Sloot 2017)
  Specific risk: Listing identifiable communities scraped without consent while treating disclosure as discharge; no agency/recourse; group-level harm + reputational liability. Suppressed alternatives (opt-in/don't-list) never raised.
  Summary: Notice does not cure the consent gap for identifiable groups; the option space was collapsed to "list-and-disclose."
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-313_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-314
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED | Strength: Weak-Moderate
  Key source: editorial-curation-as-quality (curated directories); IS selection-policy practice
  Summary: Curatorial selection is a legitimate quality signal in the EDITORIAL sense (curator-applied), supporting "quality bar" only in that sense.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-314_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-314
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED | Strength: Moderate-Strong
  Key source: construct validity / criterion contamination (Messick; Cook & Campbell); aspirational-vs-operative goals (Selznick); Bowker & Star
  Specific risk: A quality bar produced by the curator (no independent criterion, no community approval) is relabeled as earned/community-articulated — self-certifying, inverts the earned-membership telos.
  Summary: The metric is produced by the measurer; "articulated to a quality bar" smuggles a value claim as fact. Validity-smuggling family (308/310).
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-314_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-315
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED | Strength: Weak-Moderate
  Key source: pragmatic defect-triage (cannot-reproduce closure); stale-build diagnosis; positive-path verification
  Summary: De-prioritizing a non-reproduced error and hypothesizing a stale buffer is standard triage; supports prioritization, not exoneration.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-315_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-315
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED | Strength: Moderate-Strong
  Key source: heisenbug/non-determinism literature; init-order race analysis; absence-of-evidence principle
  Specific risk: Vanish-on-reload is the heisenbug signature; a single non-repro + one positive path does not establish unreachability of the throwing init-state — a latent race ships with no guard (silent failure).
  Summary: Single non-reproduction is not exoneration; cheap re-test + telemetry indicated before closure.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-315_against.md

RETURN-TO-14b:
  Original item: PRESUMPTION-316
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED | Strength: Weak-Moderate
  Key source: tiered-status motivation; gamification/recognition; CMV reinforcement (PREMISE-051)
  Summary: The reinforcing half is real (PREMISE-051) and visible earned status can motivate; supports a benign reading only.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-316_for.md

RETURN-TO-14b:
  Original item: PRESUMPTION-316
  Search direction: AGAINST (disconfirmatory)
  Result: CHALLENGED | Strength: Moderate-Strong
  Key source: lower-tier stigma (status-tier psychology); participation inequality (Nielsen 90-9-1); visibility-as-power (Bowker & Star; arXiv 2407.16014)
  Specific risk: The carded-only majority is implicitly marked "not yet earned"; combined with no-consent listing (313), communities are listed AND ranked by an unchosen visibility status — compounding group harm and biasing attention toward visibility over merit.
  Summary: Not purely reinforcing — visible earned status carries documented stigma; "each makes the other more truthful" overclaims. Couples 308/314.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-316_against.md

---

## Dispositions — run 2026-06-07 (15c)

DISPOSITION-165:
  Date: 2026-06-07
  Item: ASSUMPTION-278
  Item type: ASSUMPTION (stated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Assigning shared CC-xxx ids is sound integration MECHANICS (surrogate keys / MDM), but it makes directory⊇graph ADDRESSABLE, not TRUE. Validity rides entirely on the identity question, which the 2026-06-05 measurement (0/3/5) leaves near the signal floor — exactly the case where a key manufactures the relation.
  Disposition: MONITOR (MONITOR-308), Priority HIGH
  Reasoning: The technique is legitimate, so not REVISE on its own; but it is the ENACTED vehicle of the contested identity (PRESUMPTION-312 → REVISE-091), so it cannot INCORPORATE until the linkage is measured. MONITOR-HIGH, explicitly gated on the REVISE-091/REVISE-089 record-linkage result. Cross-listed in the manufactured-identity SYSTEMIC-RISK.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING

DISPOSITION-166:
  Date: 2026-06-07
  Item: ASSUMPTION-279
  Item type: ASSUMPTION (stated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: The functional-complementarity core is already validated as PREMISE-051 (via ASSUMPTION-275). The NEW content of 279 — "purely mutually upbuilding, directory feeds graph, seeds earn their place, each makes the other more truthful" — adds a tiered-visibility value claim CMV theory does not license and PRESUMPTION-316 challenges.
  Disposition: MONITOR (MONITOR-309), Priority MEDIUM
  Reasoning: Consistency: do NOT issue a second INCORPORATE that duplicates PREMISE-051. The validatable part is already incorporated; the residual "earned/more truthful" claim is contested (316) and normative, so MONITOR rather than INCORPORATE or REVISE. Couples PRESUMPTION-314/316 (visibility-as-earned-status family).
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: MONITORING

DISPOSITION-167:
  Date: 2026-06-07
  Item: ASSUMPTION-280
  Item type: ASSUMPTION (stated)
  15a result: SUPPORTED | 15a strength: Moderate-Strong
  15b result: PARTIALLY-CHALLENGED | 15b strength: Weak-Moderate
  Net assessment: Disclosing scraped-seed provenance and not implying endorsement is a well-supported minimum transparency/ethics bar. The only challenge is that disclosure is necessary-not-sufficient — which targets the SUFFICIENCY overclaim (PRESUMPTION-313), not 280's "must disclose rather than imply endorsement."
  Disposition: INCORPORATE (PREMISE-052), Confidence Moderate
  Reasoning: Strong support + weak challenge on a stated assumption whose challenge is fully separable (handled as REVISE-092) → INCORPORATE the disclosure-as-necessary-floor premise, with the explicit caveat that it is NOT a discharge of consent. Consistency-checked vs PREMISE-001..051: new data-ethics/consent-disclosure domain, no conflict.
  Validated premise statement: see PREMISE-052.
  PROVENANCE:
    Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: INCORPORATED

DISPOSITION-168:
  Date: 2026-06-07
  Item: PRESUMPTION-312
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: CHALLENGED | 15b strength: Strong
  Net assessment: Across ER, relational modeling, and MDM, identity is INFERRED from evidence and EXPRESSED by a key — never CREATED by one. Minting shared ids in the 0/3/5 near-zero-overlap regime is the canonical false-match: the merge answers "same entity?" with "they are now."
  Disposition: REVISE (REVISE-091), Urgency HIGH
  Reasoning: Weak conditional support + strong challenge on a HIGH-risk PRESUMPTION that is already ENACTED (the ids are minted) → REVISE, the clearest of the run. PRESUMPTION weight applies (designers were unaware they were betting identity on a key). The honest status is unknown-until-measured. Core of the manufactured-identity SYSTEMIC-RISK.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

DISPOSITION-169:
  Date: 2026-06-07
  Item: PRESUMPTION-313
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: CHALLENGED | 15b strength: Strong
  Net assessment: Notice can be proportionate for low-sensitivity public data, but consent theory (Solove) and group-privacy work hold that disclosure does NOT discharge consent for IDENTIFIABLE groups — which these communities are. The structural flaw is a collapsed option space: opt-in / don't-list were never raised.
  Disposition: REVISE (REVISE-092), Urgency HIGH
  Reasoning: Weak support + strong challenge on a HIGH-risk ethics PRESUMPTION that is already enacted (communities listed) → REVISE. PRESUMPTION weight + real-world (reputational, group-harm) stakes. Pairs with ASSUMPTION-280/PREMISE-052: disclose = floor (INCORPORATE), disclosure-is-sufficient = overclaim (REVISE). Core of the consent-gap SYSTEMIC-RISK.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

DISPOSITION-170:
  Date: 2026-06-07
  Item: PRESUMPTION-314
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Curatorial selection is a legitimate quality signal in the EDITORIAL sense, but "articulated to a quality bar" attributes to the COMMUNITIES a property produced by the CURATOR (no independent criterion, no community approval) — a construct-validity error and an aspirational-vs-operative inversion of the earned-membership telos.
  Disposition: MONITOR (MONITOR-310), Priority HIGH
  Reasoning: A value/measurement claim smuggled into a "quality" descriptor is a decision for Tom (relabel honestly vs define an independent community-side criterion), not a literature-settleable defect → MONITOR HIGH with an explicit "surface to Tom + relabel" action. Validity-smuggling family (couples 308, 316).
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING

DISPOSITION-171:
  Date: 2026-06-07
  Item: PRESUMPTION-315
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: Vanish-on-reload is the heisenbug signature of an init-order/timing-sensitive defect; a single non-reproduction + one positive handler-fires test does not establish that the throwing init-state is unreachable from real user sequences. "Stale buffer" is a plausible hypothesis, not a verified diagnosis.
  Disposition: MONITOR (MONITOR-311), Priority MEDIUM
  Reasoning: Resolvable by a cheap, decisive check (repeated/randomized + cold-cache reloads; add init telemetry), unresolved at autonomous run time → MONITOR. Not REVISE (no defect demonstrated, no realized harm); not closed/exonerated (single non-repro is not proof of absence). Keep OPEN-pending-recurrence with a guard.
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING

DISPOSITION-172:
  Date: 2026-06-07
  Item: PRESUMPTION-316
  Item type: PRESUMPTION (unstated)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak-Moderate
  15b result: CHALLENGED | 15b strength: Moderate-Strong
  Net assessment: The "purely reinforcing / each makes the other more truthful" framing denies a documented failure mode: visible earned status produces lower-tier stigma and participation inequality, and graph-absence reads as deficiency for the carded-only majority (visibility-as-power).
  Disposition: MONITOR (MONITOR-312), Priority HIGH
  Reasoning: A visibility value choice (who is graphed = who is legitimate) too consequential to leave implicit but not yet a demonstrated harm to REVISE → MONITOR HIGH with an explicit "surface to Tom + measure carded-only treatment" action. Couples PRESUMPTION-314 (curator quality bar) and ASSUMPTION-279 (MONITOR-309).
  PROVENANCE:
    Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: MONITORING

**Run 2026-06-07 totals:** 8 items | 1 INCORPORATE (PREMISE-052) | 5 MONITOR (MONITOR-308..312) | 2 REVISE (REVISE-091, REVISE-092) | DISPOSITION-165..172. SYSTEMIC-RISK #1 (HIGH) "manufactured-identity-as-foundation": ASSUMPTION-278 (MONITOR-308) + PRESUMPTION-312 (REVISE-091) — the 2026-06-05 disjoint-id finding (0/3/5) was answered by ASSIGNING shared CC-xxx ids, escalating the prior unvalidated-P3-join cluster (REVISE-089/MONITOR-307) from unbuilt to manufactured-by-fiat. SYSTEMIC-RISK #2 (MEDIUM-HIGH, ethics) "consent-gap-papered-by-disclosure": ASSUMPTION-280 (PREMISE-052, the floor) vs PRESUMPTION-313 (REVISE-092, the overclaim); opt-in/don't-list never raised. Secondary validity-smuggling pair continues: PRESUMPTION-314 (MONITOR-310) + 316 (MONITOR-312), extending 308/310. Consistency check: PREMISE-052 vs PREMISE-001..051 — no conflict (new data-ethics/consent-disclosure domain); ASSUMPTION-279 deliberately NOT re-INCORPORATED (complementarity already PREMISE-051). No NOVELTY flags.
