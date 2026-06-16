SEARCH-AGAINST-PRESUMPTION-343:
  Date searched: 2026-06-12
  Original item: PRESUMPTION-343
  Original statement: "Disposition quality is batch-size invariant (a 188-item drain ≈ daily cadence quality)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-343
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference from 2026-06-11 EOD session
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Sanz, S., et al. (2025). "Systematic review of the effects of decision fatigue in healthcare professionals on medical decision-making." Health Psychology Review. — Meta-analysis finding that 45% of studies quantitatively assessing decision fatigue found significant effects; diagnostic, prescribing, and therapeutic decisions all show quality decrements as cumulative decision load increases, with later decisions trending toward less effortful defaults.
    2. PMC11808891 (2025). "Clinical decision fatigue: a systematic and scoping review with meta-synthesis." — Confirms that decision fatigue manifests as simplification and default-seeking in later items in a decision sequence; the pattern is not eliminated by expertise and is dose-dependent on decision volume.
    3. Propel Code (2025). "The Impact of PR Size on Code Review Quality: What Data Tells Us." — Empirical data from software code review showing PRs over 1,000 lines have 70% lower defect detection rates than small PRs; reviewers show "scope insensitivity," spending roughly the same total mental effort on large and small reviews, producing proportionally less scrutiny per item in larger batches.
    4. GitClear Research (2025). "30% Less is More: Code Review Strategies That Cut Pull Request Size." — Documents that large review batches trigger rubber-stamp approval behaviour under time and cognitive pressure; links directly to the "review-all-188-items" scenario.
    5. Mackworth, N.H. (1948). "The Breakdown of Vigilance During Prolonged Visual Search." Quarterly Journal of Experimental Psychology. — Original vigilance decrement study establishing that sustained attention tasks show performance degradation over time; the effect has been replicated across airport baggage screening, radiology reading, and quality inspection tasks.
    6. PMC6721323 (2019). "Vigilance Decrement and Enhancement Techniques: A Review." Brain Sciences. — Comprehensive review confirming vigilance decrement as a robust phenomenon in screening tasks; notes that the decrement is observable within the first 20-30 minutes of sustained work and is not eliminated by motivation or expertise.
    7. Baddeley, A. (2003). "Working memory: looking back and looking forward." Nature Reviews Neuroscience, 4, 829-839. — Working memory capacity constraints explain why large batches overwhelm the cognitive resources available for each individual decision; the central executive bottleneck limits the depth of processing available per item as queue length increases.

  Strength of challenge: Strong

  Summary: The claim that disposition quality is batch-size invariant is directly contradicted by convergent evidence from decision fatigue research, vigilance decrement studies, and empirical code review data. Decision fatigue literature shows that quality degrades as cumulative decision load increases, with later items in a sequence receiving less scrutiny and more default-seeking responses. Code review research shows a specific numerical relationship: defect detection drops 70% for batches over 1,000 lines. Vigilance decrement research establishes that sustained screening tasks show performance degradation within 20-30 minutes, regardless of expertise. A 188-item drain is not equivalent to a daily cadence of smaller batches: it concentrates cognitive load into a single session, depletes attentional resources faster, and creates serial-position effects where items late in the queue receive proportionally less scrutiny.

  Specific risks: Items in the latter portion of a 188-item batch will be under-scrutinised relative to daily cadence disposition. High-stakes items (challenges, falsifications, systemic risk flags) that happen to fall late in a large batch may be dispositioned as quickly as low-stakes items because reviewer resources are depleted. The pipeline will report "188 items processed" as a health indicator without capturing whether processing quality was equivalent across batch positions.

  Mitigations available: Cap single-session disposition batches at a maximum (empirical recommendation: 50-100 items); introduce mandatory breaks between sub-batches; apply stratified sampling to ensure high-priority items are distributed across the batch rather than concentrated at the end; track time-per-item as a quality proxy (declining time-per-item across a session is a leading indicator of fatigue-driven rubber-stamping).

  STEELMAN:
    Strongest counterargument: The C2A2 disposition agent is an LLM, not a human, and LLM "fatigue" is not directly analogous to human cognitive depletion within a single inference session. Within a context window, LLMs do not exhibit the progressive attentional depletion that underlies human decision fatigue; each item processed is not drawing on a depleting cognitive reserve in the way human working memory does. If disposition quality is consistent within the context window, batch size up to the context limit may genuinely be invariant.
    What would need to be true for C2A2 to be safe: LLM disposition quality would need to be empirically demonstrated to be context-position invariant — i.e., items at position 180 in a batch must receive equivalent quality treatment to items at position 5. This is not guaranteed; LLM performance degrades at long context positions ("lost in the middle" effect), which is an LLM-specific analogue of the vigilance decrement.
    How to test: Process the same set of 20 representative items twice — once as the first 20 items in a 188-item batch and once as a standalone batch — and compare disposition quality and confidence. Systematic divergence reveals position-dependent quality effects. Additionally, check whether items at different positions in past large batches received different average time-per-item or disposition depth.

  Search scope: Searched decision fatigue systematic reviews, vigilance decrement literature, code review quality studies (empirical), and cognitive load / working memory constraints. Comprehensive for primary challenge directions. Additional targeted search on "LLM performance long context position degradation" recommended given the LLM-specific analogue.

  Recommendation: CHALLENGED
