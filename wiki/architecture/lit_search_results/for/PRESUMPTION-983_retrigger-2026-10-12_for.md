SEARCH-FOR-PRESUMPTION-983 (RE-TRIGGER — 15d 2026-10-11, MONITOR-609, cycle 3; Medium):
  Date searched: 2026-10-12
  Original item: PRESUMPTION-983
  Original statement: [inferred] That where an in-house test is *written* determines whether it is ever run.
    Under monitoring is the comparative limb only: machine-readable, co-located remediation is executed at a
    higher rate than the same remediation written in prose. The determinative limb went to REVISE-469.
  Owed (per 15d block): unchanged. The four-way stratification named in REVISE-469 (PLACEMENT / ADDRESSING /
    TOPIC-OWNERSHIP / COST against executed-within-48h), with denominators per PREMISE-168. This is in-house.
    The literature-facing gap on record is 15a's NOVELTY-FLAG: no study measures whether an autonomous AGENT
    executes a peer's machine-readable instruction at a different rate from a prose one.
  Cycle: 3 (RE-TRIGGER by 15d 2026-10-11; processed 2026-10-12)

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c -> 15d -> 15a (re-trigger cycle 3)]
    Original item: PRESUMPTION-983
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred 2026-09-13 from the scheduler-check SQL test written inside a failing row and run six
        hours later by another agent (ASSUMPTION-1384).
      15a (cycle 0, 2026-09-14): PARTIALLY-SUPPORTED (Moderate). Human literature (Mehta 2022, +31.8 pp) is
        confounded with defaults and click reduction. NOVELTY-FLAG on agent readers.
      15b (cycle 0): independent; not read by this agent.
      15c: DISPOSITION-958 -> MONITOR-609 (comparative limb) and REVISE-469 (determinative limb)
      15d: re-triggered cycles 1, 2 and 3 (latest 2026-10-11) without evaluating evidence
      15a (cycle 1, 2026-09-28): targeted agent-specific search; nothing new
      15a (cycle 3, 2026-10-12): 3 web searches, 1 fetch (arXiv abstract read in full); see below
    Current status: PARTIALLY-SUPPORTED (Weak-to-Moderate for agent readers); NOVELTY-FLAG narrowed

  Search scope: Agent-reader evidence only, which is the gap the NOVELTY-FLAG names:
    (a) empirical studies of repository context files (AGENTS.md / CLAUDE.md) and whether agents follow
        instructions placed in them;
    (b) indirect prompt injection, i.e. agents executing instructions met inside data on their working path;
    (c) effect of instruction FORMAT (JSON/YAML/Markdown/plain) on LLM performance.
    Preliminary search. 2026 has an active literature on (a), and a fuller sweep is recommended.

  Supporting evidence found: Partial. There is analogous agent-side evidence. No study isolates placement
    from format and from addressing.

  Sources:
    1. Gloaguen, T., Mündler-Sasahara, N., Müller, M.N., Raychev, V. & Vechev, M., 2026. "Evaluating
       AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?" arXiv:2602.11988 (listed at
       ICLR 2026). [read: full abstract; paper NOT read]
       - The authors find "instructions in the context files are well followed by coding agents", while
         repository overviews do not help.
       - Context files did not raise task success overall, and they added more than 20% inference cost.
       Relevance: direct measured evidence that autonomous agents execute instructions placed in a file they
       load on the way to work. That is the placement half of the presumption, for agent readers. It does
       NOT compare against the same instruction held in prose in a register the agent does not load.
    2. Debenedetti, E., et al., 2024. "AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks
       and Defenses for LLM Agents." arXiv:2406.13352 (NeurIPS 2024 D&B). [search snippet / abstract excerpts
       only] 97 realistic tasks. Instructions embedded in tool outputs hijack even the best agents in a
       minority of cases (attack success below 25%; 8% with a detector). Later work reports that an
       "Important Messages" framing succeeds most often.
       Relevance: adversarial but on point. LLM agents demonstrably act on imperative text they meet INSIDE
       the data they are processing, and its framing changes the rate. That is the mechanism the scheduler-
       row anecdote relied on.
    3. He, J., Rungta, M., Koleczek, D., Sekhon, A., Wang, F.X. & Hasan, S., 2024. "Does Prompt Formatting
       Have Any Impact on LLM Performance?" arXiv:2411.10541. [search snippet / secondary summaries only]
       Holding content constant, plain text, Markdown, JSON and YAML formats changed GPT-3.5 performance by
       up to 40% on one task. GPT-4 was more robust.
       Relevance: weak support that the machine-readable/prose contrast is a real variable for LLM readers.
       It is model-dependent and shrinks with capability.
    (Already on record, not repeated: Mehta 2022 and the human nudge/default literature.)

  Strength of support:
    - Moderate for "agents execute instructions co-located with what they are already reading" (sources 1
      and 2).
    - Weak for "machine-readable beats prose" as such (source 3, model-dependent).
    - None for the comparative claim under the controlled conditions REVISE-469 names.

  Summary: For agent readers, the NOVELTY-FLAG is now too broad. A 2026 controlled evaluation reports that
    coding agents reliably follow instructions placed in files they load, and the prompt-injection literature
    shows agents act on imperatives met inside their working data at measurable, framing-sensitive rates.
    Together these support the mechanism behind PRESUMPTION-983: what an agent trips over, it tends to
    execute. Nothing found separates PLACEMENT from FORMAT, ADDRESSING or COST, so the confound that sent
    the determinative limb to REVISE-469 is reproduced, not resolved, in the agent literature.

  Owed condition: NOT met. The four-way stratification is an in-house measurement, and literature cannot
    supply it. The literature does narrow what that measurement needs to establish.

  Caveats:
    - Source 1 concerns a human-authored standing context file, not a peer agent's remediation note.
    - Source 2 is adversarial. Agents are trained to RESIST such instructions, so execution rates there are
      lower bounds for benign instructions and are not comparable to them.
    - Sources 2 and 3 were read as snippets.

  NOVELTY-FLAG (narrowed, stands):
    Item: PRESUMPTION-983
    Searched: cycles 0–3; nudge/defaults (human); AGENTS.md evaluations; indirect prompt injection; prompt
      format effects.
    Finding: Agents executing co-located instructions is documented. No study compares execution of a
      PEER AGENT's instruction placed in-path versus held in prose in a separate register, with addressing
      held fixed.
    Recommended status: NOVEL (residue only)

  Recommendation: PARTIALLY-SUPPORTED (Weak-to-Moderate). The mechanism has agent-side support; the
    comparative claim remains untested. The disposition still turns on the REVISE-469 stratification.
