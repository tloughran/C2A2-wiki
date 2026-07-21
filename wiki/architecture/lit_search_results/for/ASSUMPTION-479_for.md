SEARCH-FOR-ASSUMPTION-479:
  Date searched: 2026-07-20
  Original item: ASSUMPTION-479
  Original statement: Well-evidenced observations are being attached to remedies unvalidated against the actual mechanism when a cheap discriminating test exists (7 of 12 items); three remedies route more signal into a channel with demonstrated zero throughput.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-479
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 lit-search pipeline REVISE-231 statement
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Fault detection and isolation literature (Wikipedia, "Fault detection and isolation"; "Finding faults: A scoping study of fault diagnostics for Industrial Cyber-Physical Systems," arXiv:2101.05451). — Direct theoretical grounding for the "discriminating test" concept the item invokes. States the core problem explicitly: "different faults may have similar symptoms, making it non-trivial to isolate the actual underlying cause," and that fault isolation "needs to be able to capture the key discriminating factors between different faults, even if the resulting symptoms are similar." The discriminating test is the field's central named construct, not an ad hoc coinage.
    2. Predictive-maintenance literature ("Explainable Predictive Maintenance," arXiv:2306.05120; ScienceDirect, "Fault diagnosis — an overview"). — Supplies the cost argument: "the underlying cause of the fault must be accurately identified; mistakes at this stage often manifest as replacing healthy components, not only incurring additional maintenance costs but also ultimately failing to prevent the imminent failure." This is precisely the item's claim — an unvalidated remedy costs effort *and* leaves the failure in place — stated as established maintenance doctrine.
    3. ITU Online, "What Is Fault Isolation?"; practitioner incident-response guidance. — "Fault isolation is the process of proving which component, dependency, or change caused the failure," and "a verification loop separates an educated guess from a confirmed diagnosis and keeps the same incident from returning tomorrow." Direct support for diagnosis-before-repair as a named discipline with a named cost of omission (recurrence).
    4. Senge, P. (1990), The Fifth Discipline — systems archetypes "Fixes that Fail" and "Shifting the Burden" (via Medium, "System Archetypes: The Recurring Patterns of Failure"). — Theoretical grounding for the second clause. "Fixes that backfire" is defined as "the use of a quick fix to reduce a problem symptom that works in the short run but at the cost of long-term consequences, which people often fail to see due to long system delays"; "Shifting the Burden" is defined as quick fixes addressing symptoms "while root causes remain unaddressed." Both name the item's pattern as a recurring, catalogued organisational failure mode.
    5. Goldratt, E.M., Theory of Constraints (Wikipedia; Theory of Constraints Institute). — Supports the "routes more signal into a zero-throughput channel" clause with the strongest available principle: work delivered to a non-constraint at above the constraint's rate produces only inventory. "If one department works faster than the bottleneck, it creates waste, rework, and frustration." Three remedies that increase input to a channel with demonstrated zero throughput are, in TOC terms, increasing WIP in front of a stopped constraint — the canonical error the theory exists to prevent.
    6. Braess's paradox and bufferbloat, cited as instances of fixes-that-backfire in "On Analyzing Self-Driving Networks: A Systems Thinking Approach" (arXiv:1804.03116). — Two formally documented cases where adding capacity or buffering to relieve congestion made system performance worse. Empirical precedent that the item's failure mode produces measurable harm, not just wasted effort.

  Strength of support: Strong

  Summary: ASSUMPTION-479 restates, in pipeline terms, a discipline that three separate engineering literatures treat as foundational. Fault detection and isolation supplies the exact construct the item relies on — the discriminating test that separates faults presenting identical symptoms — and treats the failure to run one as the defining error of the field, with the documented cost being both wasted repair and unfixed fault. Predictive maintenance quantifies this as replacing healthy components while the real failure proceeds. Systems dynamics catalogues the organisational form as "Fixes that Fail" and "Shifting the Burden," with the mechanism given as delayed feedback, which explains why the pattern persists undetected in a pipeline whose remedies are rarely followed up. The zero-throughput clause has the strongest single grounding: Theory of Constraints holds that output delivered to a stopped constraint is not throughput but inventory, and Braess's paradox and bufferbloat are formally documented cases where adding capacity to relieve congestion degraded the system. The item's ratio (7 of 12) is an internal count and is outside the scope of literature support, but the pattern it counts is real, named, and costly.

  Caveats: (a) All sources concern physical or network systems with observable state; an epistemic pipeline's "remedies" are process changes whose effect is slower and harder to attribute, so the delayed-feedback problem Senge identifies is worse here than in the source domains, not better. (b) The literature supports diagnosis-before-repair as a default but not as an absolute — in low-cost, reversible cases speculative repair is rational, and the item does not distinguish reversible from irreversible remedies. Some of the 7 may be cheap enough that the discriminating test is not worth running. (c) The item is itself a remedy-bearing observation ("run the one-line EPERM test before building any localhost server") and that particular remedy *is* the discriminating test, so it does not reproduce the pattern — but the second half ("audit standing REVISE items") is an unvalidated process remedy of exactly the kind the item criticises. (d) TOC assumes a single identifiable constraint; the pipeline may have several.

  Recommendation: SUPPORTED
