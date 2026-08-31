SEARCH-AGAINST-PRESUMPTION-903:
  Date searched: 2026-08-31
  Original item: PRESUMPTION-903
  Original statement: [inferred] Assumption extraction is time-indifferent; a missed day is
    deferred, not lost.
  Generalizable limb searched: Whether retrospective analysis recovers what contemporaneous analysis
    would have captured — evidence decay, hindsight bias, narrative smoothing, and the documented
    difference between contemporaneous records and post-hoc reconstruction.

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 3 queries run (2 Pass 1 + 1 Pass 2); no
    full-text reads. Sources are a mix of peer-reviewed cognitive psychology (PLOS ONE, Applied
    Cognitive Psychology, a qualitative healthcare study) and practitioner incident-management
    guidance; the latter is normative convention rather than measurement.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-903
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the treatment of a skipped extraction cycle as a scheduling matter — the
        backlog to be picked up later — rather than as an irreversible loss of extractable material.
      15b: Searched for challenging literature (2026-08-31)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Hindsight bias memory-distortion literature, represented by: Calvillo & Rutchick et al. as
       characterised in "Memory load of information encoded amplifies the magnitude of hindsight
       bias," PLOS ONE, 2023 (PMC10085031); and the working-memory hindsight-bias study in PubMed
       22871160. — Establish that a core component of hindsight bias is memory distortion:
       recollections of one's own prior judgements are biased toward the known outcome, and this
       distortion is *amplified* under memory load. Directly relevant: a delayed extraction operates
       under higher effective load and with the outcome already known, which is the condition under
       which distortion is documented to be worst.
    2. Sagar, Sharma, et al. (as indexed at PMC9378085), 2022. "A Qualitative Study Exploring the
       Role of Hindsight Bias in the Process of Reviewing Clinical Practice Prior to Adverse
       Incidents." — Direct evidence from incident review specifically: knowledge of the outcome
       shapes what reviewers gather and how they assess the decisions available at the time. This
       is the mechanism by which a delayed extraction does not merely capture less, but captures
       *differently* — reconstructing what was reasonable given what is now known.
    3. Memory bias definitional literature (ScienceDirect, "Memory Bias — an overview"). — States
       that memory biases are identified precisely by comparing retrospective reports against the
       same individuals' earlier contemporaneous reports, and that they are present across
       individuals and contexts. The methodological point matters: contemporaneous record is the
       *reference standard* against which retrospective accounts are scored, not an equivalent
       alternative to them.
    4. Eyewitness recall-timing research (PMC9225701, "The impact of recall timing on the
       preservation of eyewitness memory"; Maulina et al., 2024, "Testing the efficacy of the
       cognitive interview to road traffic accident investigations," Applied Cognitive Psychology,
       DOI 10.1002/acp.4177). — Support the retention-interval effect: memory fades rapidly with
       delay, and longer delays increase exposure to post-event information that is then
       incorporated into the account (the misinformation effect). The misinformation limb is the
       closer analogue for C2A2 than simple forgetting: intervening runs supply post-event material
       that gets folded into the later reconstruction.
    5. Wolters Kluwer, "Guidelines for Witness Interviews During an Incident Investigation"; SHRM,
       "How to Conduct Accident-Witness Interviews"; OSHAcademy course 162, "Accident Investigation:
       Basic". — Converging professional guidance that witnesses be interviewed as soon as possible,
       because delay causes memory distortion and loss of critical information and allows accounts
       to be contaminated by discussion with others. Normative practice codifying the research.
    6. Incident-management practitioner guidance (Atlassian, "The importance of an incident
       postmortem process"; Rootly postmortem meeting guide; FireHydrant retrospective template;
       Pragmatic Engineer, "Incident Review and Postmortem Best Practices"). — Converge on
       conducting postmortems within 24-72 hours, with 48 hours common, on the explicit reasoning
       that "the closer to the event, the fresher the memory and the more accurate the timeline" and
       that waiting means context slips away. Convention rather than measurement, but the
       convergence across independent vendors and practitioners is itself informative about
       observed practice.

  Strength of challenge: Strong

  Summary: The presumption treats extraction as a queue operation — work that waits without
    spoiling. Every source found contradicts this, and they do so through two distinct mechanisms
    that are worth separating. The first is decay: the retention-interval effect is one of the most
    robust findings in memory research, and the material available for extraction on day N+7 is a
    strict subset of what was available on day N. The second, and more damaging for C2A2's purposes,
    is *distortion*: hindsight bias systematically reshapes recollection toward the known outcome,
    and the incident-review study shows this operating in exactly the review setting at issue. The
    two mechanisms differ in their implications. Decay produces an obviously smaller yield, which
    might be tolerable and is at least detectable. Distortion produces a yield of the *same apparent
    size* that is selectively wrong — assumptions that look reasonable in light of what followed get
    smoothed away, and the ones that survive extraction are disproportionately those that the
    subsequent record happens to make salient. A delayed extraction will therefore not feel
    impoverished; it will feel coherent, which is worse. The misinformation-effect finding sharpens
    this: intervening runs are not neutral waiting time but active contamination, supplying material
    that gets incorporated into the reconstruction. The whole professional apparatus of incident
    investigation — interview promptly, postmortem within 48 hours, prefer contemporaneous records —
    exists because this is a known and non-recoverable loss.

  Specific risks: If extraction is not time-indifferent, a missed day is a permanent hole in the
    assumption register, and the hole is invisible: nothing in the record marks which assumptions
    were never surfaced. Worse, the deferred extraction that eventually runs will produce output
    that is *systematically biased toward coherence with what happened next* — meaning the
    assumptions most likely to be lost are exactly the ones that later turned out to matter, since
    those are the ones the subsequent narrative has already reinterpreted. This directly degrades
    the pipeline's core function. It also silently corrupts the evidence base for every downstream
    stage including this one: 15a/15b search literature against items that were themselves shaped by
    hindsight. A backlog of deferred extraction days will read as recoverable work when it is in
    fact a permanently reduced and skewed sample.

  Mitigations available: (a) Treat extraction as a perishable operation with a stated freshness
    window, and record the lag between event and extraction on every item so downstream stages can
    discount accordingly; (b) if a day is missed, mark it as a gap rather than as a queued item, so
    the register distinguishes "not yet extracted" from "extracted late" from "lost"; (c) preserve
    contemporaneous raw material — transcripts, tool logs, diffs — so that late extraction works
    from primary record rather than reconstruction, which converts a memory problem into a reading
    problem and largely neutralises both mechanisms; (d) where late extraction is unavoidable,
    borrow the cognitive-interview discipline of working from the record forward rather than from
    the outcome backward, to limit outcome-driven reinterpretation; (e) prioritise same-day
    extraction for high-consequence runs specifically, if universal same-day is not achievable.

  STEELMAN:
    Strongest counterargument: The entire memory literature cited presupposes that the extraction
      substrate is *memory*. For C2A2 it may not be. If assumptions are extracted from durable
      artefacts — session transcripts, committed files, tool-call logs, diffs — then the substrate
      does not decay at all, and an extraction run on day N+7 reads exactly the same bytes it would
      have read on day N. Hindsight bias requires the extractor to know the outcome, but an
      extractor scoped to a single day's artefacts, run in a fresh context, has no more outcome
      knowledge on day N+7 than it did on day N. On this reading the presumption is simply correct
      and the memory literature is inapplicable — the retrieval is archival, not mnemonic, and
      deferral costs nothing but latency.
    What would need to be true for C2A2 to be safe: The artefacts must be genuinely durable and
      complete — full transcripts retained, not summarised or compacted, and covering everything an
      assumption might be inferred from including reasoning that never reached a file. The deferred
      extraction must be scoped strictly to the target day's artefacts and run without visibility of
      subsequent runs, or hindsight contamination re-enters through the back door. And nothing
      extractable may exist only in a session context that has since been discarded. The third
      condition is the one most likely to fail: if any part of extraction depends on in-session
      state rather than persisted artefacts, that part is lost the moment the session ends, and the
      steelman collapses for that portion.
    How to test: Cleanly testable and worth doing. Take several past days for which same-day
      extraction was performed, discard the results, and re-run extraction from the retained
      artefacts alone at the current date. Compare yield and content against the original. Overlap
      measures how much survives; items present originally but absent now measure decay; items
      present now but absent originally measure hindsight-driven addition. The asymmetry between
      those last two categories distinguishes the decay mechanism from the distortion mechanism and
      would settle whether the archival steelman holds.

  Recommendation: CHALLENGED
