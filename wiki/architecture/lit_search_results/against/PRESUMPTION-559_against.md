SEARCH-AGAINST-PRESUMPTION-559:
  Date searched: 2026-07-28
  Original item: PRESUMPTION-559
  Original statement: [inferred] The external-referent audit (PREMISE-127/128/129 "all do cite external referents") presumes that citing a referent equals having been checked against it, and that the pipeline can audit its own external-referent property from inside; MONITOR-486's stated resolution (a decorrelated spot-check) was not performed.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-559
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: surfaced from a self-performed referent audit reported as a clean result
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Agrawal, A., Suzgun, M., Mackey, L. & Kalai, A. T. 2024. "Do Language Models Know When They're Hallucinating References?" Findings of the ACL: EACL 2024 (arXiv:2305.18248). — Directly challenges the second half of the presumption. The authors use CONSISTENCY CHECKS to identify hallucinated references WITHOUT consulting external resources, and find that models produce inconsistent author lists for hallucinated references while accurately recalling authors of real ones - i.e. the model "can be said to know when it is hallucinating references." So a pipeline can obtain a non-trivial, better-than-chance internal signal on its own citation property; "cannot audit from inside" is too strong.
    2. Zhang, J. et al. 2023. "SAC3: Reliable Hallucination Detection in Black-Box Language Models via Semantic-aware Cross-check Consistency." (arXiv:2311.01740); Manakul, P. et al. 2023, SelfCheckGPT. — Cross-checking across semantically perturbed queries and across model samples detects hallucination at useful accuracy with no external ground truth. This gives C2A2 a cheap decorrelation-by-sampling option that is strictly internal, weakening the claim that only a human or different model can settle the question.
    3. Institute of Internal Auditors. 2020. "The IIA's Three Lines Model: An Update of the Three Lines of Defense." — The governance standard that most sharply distinguishes assurance from operation nonetheless treats periodic SELF-assessment as a valid means of validating conformance with the Standards, and locates independence in reporting line and absence of operational responsibility rather than in different substrate. On this framework an internal audit is not void; it is lower-assurance and must avoid self-review of work the auditor performed. That is a graded standard, not the binary the presumption implies.
    4. Huang, J. et al. 2024. "Large Language Models Cannot Self-Correct Reasoning Yet." ICLR 2024 (arXiv:2310.01798). — Cited here as the boundary condition rather than as support for the presumption: the finding is specifically that intrinsic self-CORRECTION of reasoning degrades performance absent an external signal. Citation checking is not reasoning revision - it is a lookup-style factual consistency task, which is the class where Agrawal et al. and SelfCheckGPT show internal checks DO work. Transferring Huang et al.'s pessimism to citation auditing is a domain over-extension.

  Strength of challenge: Moderate

  Summary: The first half of the presumption - that citing a referent is not the same as having been checked against it - is not challenged by anything located; it is a straightforward distinction and the literature on misattributed references supports it. The second half is materially challenged. Agrawal et al. 2024 demonstrate that consistency checks with no external resource detect hallucinated references, and SAC3/SelfCheckGPT generalise this to cross-sample consistency, so a pipeline does have a real internal signal about its own citation property. The IIA Three Lines Model adds that self-assessment is a recognised, graded form of assurance whose weakness is self-review of one's own work, not internality as such. The correct reading is therefore not "internal audit is invalid" but "internal audit yields lower-grade assurance and must not be performed by the agent that produced the citations."

  Specific risks: If the presumption is over-read to mean no internal check has value, C2A2 defers all citation assurance to an external arbiter that has been unavailable for five consecutive dark syncs, and the register accumulates unverified referent claims indefinitely - a worse state than a cheap internal consistency check. If it is under-read, PREMISE-127/128/129 carry a clean-audit stamp that reflects only the presence of citation strings, and any fabricated or misattributed referent propagates into CROSS and FINDING layers with an assurance label attached.

  Mitigations available: (a) Run the Agrawal-style consistency check now: re-query for each cited referent's authors/venue/claim in a fresh context with no access to the premise text and flag disagreement - internal, cheap, better than nothing. (b) Enforce the IIA constraint: the checking agent must not be the agent that wrote the premise (decorrelation by role, achievable in-house). (c) Grade the audit result explicitly - "citation present" vs "citation consistency-checked" vs "citation externally verified" - so the assurance level travels with the claim. (d) Keep MONITOR-486 open until a genuinely decorrelated check is logged, and record the unperformed spot-check as an outstanding obligation rather than a resolved one.

  STEELMAN:
    Item: PRESUMPTION-559
    Strongest counterargument: Published work shows an LLM can detect its own hallucinated references from internal consistency alone, at accuracy well above chance and with no external resource, so the blanket claim that a pipeline cannot audit its own external-referent property from inside is empirically false for exactly this task. The self-correction pessimism usually invoked (Huang et al.) is about revising reasoning, not about checking bibliographic facts, and does not transfer. Governance practice agrees: internal assurance is graded, not void - what it forbids is self-review of one's own output, a constraint C2A2 can satisfy in-house by assigning the check to a different agent in a fresh context. Treating the audit as unperformable until an external human appears converts a solvable verification problem into a permanent backlog item.
    What would need to be true for C2A2 to be safe: the referent check is performed by an agent with no access to the premise text, in a fresh context, and its result is recorded with an explicit assurance grade; MONITOR-486 stays open until at least the consistency-check tier is logged.
    How to test: for each referent cited in PREMISE-127/128/129, independently elicit authors, venue, year and the specific claim attributed, in a context that does not contain the premise; count disagreements. A non-zero disagreement rate falsifies the clean-audit result immediately, with no external arbiter required.

  Recommendation: PARTIALLY-CHALLENGED
