SEARCH-AGAINST-PRESUMPTION-615:
  Date searched: 2026-08-01
  Original item: PRESUMPTION-615
  Original statement: [as queued] The presumption is that an evidence-quality caveat travels with the item; the same run supplies the counterexample (a 07-27 HOLD and a 07-19 authorship verification both failed to reach the 07-31 ingest). Nothing carries a confidence or provenance field from proposal into PRS record; a Phase-2 caveat and a Phase-1 hold share a structural fate.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-615
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from the commendation of caveat-writing set against two qualifiers failing to reach ingest
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Psallidas & Wu, "Smoke: Fine-grained Lineage at Interactive Speed," PVLDB 11(6), 2018. — States the field's central practical finding: current lineage systems incur high capture overhead, high query cost, or both, and per-tuple annotation writes can slow execution by more than an order of magnitude. The item's implicit prescription — carry a provenance field through every stage — is the expensive option, and the literature treats "capture everything" as the thing to be engineered around, not adopted.
    2. LIMA (SIGMOD 2021) and cell-level provenance in NumPy (arXiv 2506.18255). — Even optimised implementations report +15% to +35% runtime overhead. Cost is real and must be justified against the loss rate being prevented.
    3. Provenance calculi (arXiv 1310.6299; where/why/how distinctions). — These sources cut against the item as much as for it: they show that "provenance" is not one thing, and that a system must CHOOSE which notion to propagate. An undifferentiated demand that "the caveat travel with the item" does not specify which provenance notion is wanted, and the wrong choice propagates annotations that are technically correct and practically useless.
    4. The item's own evidence base: n=2 dropped qualifiers, both from the same ingest path, on one day. The general claim ("nothing in the ingest path carries a confidence or provenance field") is stated as an observation about what was "shown in the ingest path," i.e. from absence in a summary rather than from inspection of the path. Absence of evidence in a summary is weak evidence of absence in the code.
    5. Structural objection to the item's equivalence claim: a HOLD is a control-flow instruction (do not ingest) and a confidence caveat is a data annotation (ingest, but qualified). They fail in the same run, which is suggestive, but they have different carriers, different readers and different remedies; a common-cause inference from two co-occurring failures of different types is the weakest form of the argument.

  Strength of challenge: Moderate

  Summary: The item's core observation is well-grounded and 15b does not dispute that annotations must be designed to propagate. The challenge is to its scope and its costing. The lineage literature's dominant practical finding is that pervasive fine-grained annotation propagation is expensive — an order of magnitude in naive implementations, 15-35% in optimised ones — and the field's work is largely about deciding what NOT to capture. The item names no cost, no loss rate to be prevented (its denominator is the small one PRESUMPTION-604 flags), and no choice among the several distinct provenance notions the formalisms distinguish. Its structural equivalence claim — that a hold and a caveat share a fate — rests on two co-occurring failures of categorically different objects, which is the weakest available basis for a common-cause conclusion. The item is strong as a request that the PRS schema acquire a confidence field; it is weak as a general claim about the ingest path, which it infers from what a daily summary did not mention.

  Specific risks: Acting on the general form invites a pervasive provenance-propagation project with a measured cost and an unmeasured benefit, at a moment when the register is already carrying a 24-day undrained backlog. Acting on nothing risks the narrow, real failure recurring — PRS records written without the authorship note that existed upstream.

  Mitigations available: Yes, and the cheap one dominates: add a single confidence/provenance field to the PRS record schema and make the ingest fail loudly when a proposal carries a qualifier and the field would be empty. That is a targeted interlock (PREMISE-131's tier) rather than a lineage system, and it is testable against the two known cases.

  STEELMAN:
    Item: PRESUMPTION-615
    Strongest counterargument: The item generalises a schema omission into a pipeline-wide propagation defect, on two observations of different kinds, and prescribes — implicitly — the most expensive class of remedy the data-engineering literature knows. Provenance propagation is not a discipline you adopt; it is a set of distinct semantics (where, why, how, dependency) among which you must choose, each with a different cost, and the field's flagship results are about making capture cheap enough to be tolerable at all. Absent a measured loss rate, an identified provenance notion, and a cost comparison, "the caveat should travel with the item" is a slogan rather than a specification. Worse, the item's own equivalence claim conflates a control instruction with a data annotation; if those two have different carriers, then a single fix aimed at their supposed common cause will repair neither properly. The disciplined form of this finding is narrow: the PRS schema lacks a confidence field, one ingest dropped two qualifiers, add the field and an interlock, and measure the rate before generalising.
    What would need to be true for C2A2 to be safe: the remedy is scoped to the PRS schema plus an ingest-time interlock; the provenance notion wanted is named; the loss rate is measured over a denominator large enough to be worth acting on before any pipeline-wide propagation work is contemplated.
    How to test: Inspect the ingest path directly rather than inferring from the summary — enumerate every field the PRS writer can populate and check whether any accepts a confidence or provenance value. Binary, immediate, decisive against the item's general claim. Then, over all proposals filed to date that carried a qualifier, count how many resulting PRS entries show it: the item's own named rate, with the corpus rather than one run as the denominator.

  Recommendation: PARTIALLY-CHALLENGED
