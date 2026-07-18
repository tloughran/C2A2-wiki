SEARCH-FOR-PRESUMPTION-476:
  Date searched: 2026-07-13
  Original item: PRESUMPTION-476
  Original statement: "An in-run self-caught, self-fixed tool defect needs no independent confirmation — the erring run certifies its own fix and the exoneration of all prior output."

  PROVENANCE:
    Origin: 14b
    Chain: 14b -> 15a
    Original item: PRESUMPTION-476
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference from the 2026-07-12 resolver-defect episode (fifth member of the self-certifying family)
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. [Kephart, J. & Chess, D. (2003). "The Vision of Autonomic Computing." IEEE Computer 36(1). — Establishes self-healing (autonomous failure detection and recovery) via the MAPE-K loop as a legitimate design objective. Supports the LEGITIMACY of in-run self-repair.]
    2. [Psaier, H. & Dustdar, S. (2011). "A survey on self-healing systems: approaches and systems." Computing 91(1). — Surveys production self-healing architectures; documents that closed-loop detect-diagnose-repair works in deployed systems.]
    3. [Kudrjavets, G., Nagappan, N. & Ball, T. (2006). "Assessing the Relationship Between Software Assertions and Faults." ISSRE / MSR-TR-2006-54. — Two Microsoft components: higher assertion density gives a statistically significant DECREASE in fault density, and assertions caught a large share of bugs. The strongest real evidence that in-process self-checks catch real defects cheaply and early.]
    4. [Arcaini, P., Riccobene, E. & Scandurra, P. (2015). "Modeling and Analyzing MAPE-K Feedback Loops for Self-Adaptation." SEAMS. — Formalises MAPE-K — but notably requires EXTERNAL model checking to establish loop correctness, which cuts against the presumption as much as for it.]
  Strength of support: Weak
  Summary: The literature robustly supports in-run self-detection as a cheap, early, effective DETECTOR, and C2A2's in-run catch is therefore a real and creditable event, not an accident. That is the whole of the support. Not one source argues that a self-repairing component's own report constitutes adequate certification of its repair, and none addresses retroactive exoneration of output already emitted. Indeed the autonomic-computing framework assumes an EXTERNAL specification or knowledge base against which "healthy" is judged: the erring component is never the arbiter of its own health. The support covers the presumption's antecedent (self-catching is good) and none of its consequent (therefore no independent check is needed).
  Caveats: The Arcaini et al. result is close to a counterexample within the supportive literature itself — the self-adaptation loop's correctness must be established externally. Note also the clean logical gap: the presumption conflates "the fix is correct" with "prior output was unaffected," and no source found licenses that inference.
  Recommendation: PARTIALLY-SUPPORTED
