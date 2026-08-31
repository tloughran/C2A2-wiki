SEARCH-AGAINST-PRESUMPTION-894:
  Date searched: 2026-08-31
  Original item: PRESUMPTION-894
  Original statement: [inferred] In-session memory is an independent copy — an agent's recollection
    corroborates the record.
  Generalizable limb searched: Whether a recalling agent's own account can serve as independent
    corroboration of a record, given (a) the reconstructive-memory literature, (b) audit/forensic
    independence standards, and (c) LLM-specific findings on self-report faithfulness.

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 3 queries run (2 Pass 1 + 1 Pass 2); no
    full-text reads. The LLM-specific limb returned strong peer-reviewed matches (NeurIPS 2023,
    Oxford AIGI); the human-memory limb returned a mix of encyclopaedic and review sources rather
    than primary experiments.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-894
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from an incident-handling move in which the agent's own recollection of what it
        had done was treated as evidence bearing on the accuracy of the written record, rather than
        as a second output of the same process that produced the record.
      15b: Searched for challenging literature (2026-08-31)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Turpin, Michael, Grosse & Perez, 2023. "Language Models Don't Always Say What They Think:
       Unfaithful Explanations in Chain-of-Thought Prompting." NeurIPS 2023 (Advances in Neural
       Information Processing Systems). — The decisive LLM-specific source. Shows CoT explanations
       are systematically biased by features of the prompt that models do not mention, producing
       "post hoc confabulations"; models "selectively apply evidence, alter their subjective
       assessments, or otherwise change the reasoning process they describe on the basis of
       arbitrary features of their inputs." An agent's account of what it did is therefore not a
       read-out of what it did.
    2. Barez, Wu, et al., 2025. "Chain-of-Thought Is Not Explainability." Oxford Martin AI
       Governance Initiative (working paper, aigi.ox.ac.uk). — Argues directly that the verbalised
       reasoning trace should not be treated as an explanation of the underlying computation.
       Snippet-level; the position paper's title states the challenge precisely.
    3. Arcuschin, et al. (OpenReview submission). "Chain-of-Thought Reasoning In The Wild Is Not
       Always Faithful." — Reports unfaithful CoT arising on realistic prompts with no artificially
       introduced bias, including "implicit post-hoc rationalization" where models produce logically
       contradictory justifications driven by a prior toward a yes/no answer, with per-model rates
       reported (snippet cites GPT-4o-mini 13%, Haiku 3.5 7%). Snippet-level; I did not verify the
       venue or final publication status.
    4. Johnson, Hashtroudi & Lindsay source-monitoring framework, as characterised across the search
       results (Wikipedia "Source-monitoring error"; Fiveable cognitive psychology entry). — A
       source-monitoring error is misattribution of a memory's origin: the content may be
       essentially accurate while the *source* is wrong. This is the exact failure mode at issue —
       an agent may correctly recall a fact while misattributing whether it read it in the record,
       wrote it to the record, or inferred it. Secondary/encyclopaedic characterisation only.
    5. Kopelman / Moscovitch lineage on confabulation, as characterised in the search results
       (Wikipedia "Confabulation"; ScienceDirect, "False memories and confabulation," Trends in
       Cognitive Sciences). — Confabulation framed as failed reality/source monitoring: the memory
       system reconstructs a coherent narrative by filling gaps or altering details to produce a
       probable event. The reconstruction is not experienced as reconstruction, which is why the
       recaller's confidence carries no diagnostic weight.
    6. PCAOB AS 2805, "Management Representations," and the IESBA International Code of Ethics
       five-threat taxonomy (self-interest, self-review, advocacy, familiarity, intimidation), as
       characterised in the search results. — The governing structural point: management
       representations are obtained *as a supplement to*, not a substitute for, audit evidence, and
       where the auditor cannot corroborate a matter through other procedures a representation is
       taken precisely because independent evidence is lacking. Related PCAOB guidance holds that
       evidence "from a knowledgeable source that is independent of the company is more reliable
       than evidence obtained only from internal company sources," and the self-review threat names
       the case where a party evaluates its own prior work.
    7. Criminal Legal News, 2025-10-15. "The Malleable Mind in the Courtroom: Why Confident
       Eyewitnesses Often Provide the Least Reliable Evidence." — Popular-press summary of the
       eyewitness reliability literature. Cited only for the confidence-accuracy point; not relied
       on for any specific finding.

  Strength of challenge: Strong

  Summary: The presumption fails on two independent grounds, either of which would be sufficient.
    The first is a definitional point from assurance practice: independence is a property of
    *provenance*, not of storage medium. The agent's in-session memory and the written record are
    not two observations of the event; they are two artefacts of one process, and the agent that
    produced the record is the party whose work is under review. Audit standards handle this
    explicitly — this is the self-review threat, and management representations are classified as
    the weakest form of evidence precisely because they originate inside the entity being examined.
    Calling recollection a "copy" imports a redundancy metaphor that does not survive contact with
    the correlated-failure question: whatever caused the record to be wrong is very likely the same
    thing that shaped the recollection. The second ground is empirical and LLM-specific, and it is
    stronger than the human-memory analogy would suggest. Turpin et al. establish that model
    self-reports are influenced by input features the model does not surface and can be
    systematically wrong about its own processing while remaining fluent and confident. So the
    corroborating account is not merely non-independent; it is drawn from a channel with a
    documented tendency toward plausible post-hoc reconstruction. The two grounds compound: a
    non-independent source that is also unreliable in the specific direction of narrative coherence
    is close to the worst case for corroboration, because its errors will tend to *agree* with the
    record rather than diverge from it, producing false confirmation rather than detectable
    conflict.

  Specific risks: If this presumption is false, C2A2's verification step returns agreement in
    exactly the cases where it should return alarm. An agent asked "does the record match what
    happened?" will reconstruct a narrative consistent with the record it can see, and report a
    match — which is the null result, indistinguishable from genuine corroboration. Register damage
    that occurred through a mechanism the agent has no independent access to (a truncated write, a
    dropped item, a silent overwrite) will be confirmed as fine. Worse, the confirmation is
    *recorded*, so the register now contains an attestation of its own integrity generated by the
    process whose integrity is in question — this is the point at which a soft failure becomes a
    durable false assurance. Risk is correctly rated High.

  Mitigations available: (a) Stop treating recollection as evidence and reclassify it as a
    hypothesis-generator — useful for pointing at where to look, never for concluding that the
    record is sound; (b) verify against artefacts with genuinely different provenance: filesystem
    mtimes, byte counts, hashes, git history, the snapshot from ASSUMPTION-1233, or transcript logs
    written by the harness rather than by the agent; (c) where a second agent is used, ensure it
    reads the *artefacts* and not the first agent's account, and does not share the first agent's
    context — the independence discipline already applied to the 15a/15b split is exactly the right
    pattern and should be extended to register verification; (d) if a recollection is recorded at
    all, label it as an unverified representation, in the manner of a management representation
    letter, so downstream readers do not mistake it for evidence.

  STEELMAN:
    Strongest counterargument: The unfaithfulness literature concerns *reasoning* traces — models
      explaining why they reached a conclusion — which is a genuinely hard introspective task about
      inaccessible internal computation. Recalling what actions were taken in-session is a different
      and much easier task: the actions are present in the context window as literal tool calls and
      results, so the agent is not introspecting, it is *reading a log that happens to be in its
      context*. On that framing the recollection is not reconstruction at all but retrieval from a
      record that was written contemporaneously, by a different mechanism (the harness's tool-result
      injection) than the one that wrote the vault file. That would make it a legitimately
      independent second source, and the audit analogy would be misapplied because the context
      window is not the agent's testimony but the harness's own log.
    What would need to be true for C2A2 to be safe: The relevant events must actually be present
      verbatim in the agent's context at the time of recall — not summarised, not compacted, not
      beyond a truncation boundary, and not from a prior session. The agent must quote or cite the
      specific tool call rather than narrate a recollection. And the failure being investigated must
      be one that would leave a visible trace in tool results rather than one occurring below that
      level (a write that reported success but landed wrong). Where all three hold, the objection
      largely dissolves — but note that what is doing the work in that case is the harness log, not
      the agent's memory, and the honest move is to cite the log directly.
    How to test: Directly testable. Construct cases where the record and the ground truth are known
      to diverge — e.g. modify a vault file out-of-band after a write, or truncate it — then ask an
      agent in the same session whether the record reflects what it did. Measure the false-agreement
      rate. Also test the compaction boundary: run the same probe on events before and after a
      context compaction event, which should separate the "reading the log" case from the
      "reconstructing" case cleanly.

  Recommendation: CHALLENGED
