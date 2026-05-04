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
