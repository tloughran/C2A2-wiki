SEARCH-AGAINST-PRESUMPTION-914:
  Date searched: 2026-09-06
  Original item: PRESUMPTION-914
  Original statement: [inferred] Within one context, arguing FOR item X does not condition a later AGAINST on
    related item Y; independence is a property of file-reading, not of the writer's state.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-914
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 09-05 run note's claim that independence held for 10 of 11 items despite one
        context writing 8 of 22 files.
      15b: Searched for challenging literature (2026-09-06). NOTE ON AUTHORSHIP: written by the 15c
        orchestrating context after the delegated 15b subagent launch produced no files in ~55 minutes;
        this context had read all three 15a files first. Search independence does NOT hold for this item.
        This file is itself an instance of the condition the presumption denies.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Temkit, S.-A., 2026. "AMEL: Accumulated Message Effects on LLM Judgments." arXiv:2605.22714.
       [VERIFIED: title/arXiv ID/author; effect sizes from abstract snippet] — Judgments on item Y shift
       toward the polarity of the history accumulated on items X₁…Xₙ (d = −0.17 overall; d = −0.28 on
       ambiguous items; clear negatives unmoved). This is the cross-item case exactly: prior polarity on
       OTHER items conditions the next judgment, and the effect lives in context state, not in any file read.
    2. "Evaluating the Sensitivity of LLMs to Prior Context," arXiv:2506.00069. [VERIFIED: title/ID;
       authors NOT verified] — Even unrelated prior context degrades accuracy (up to 32% for GPT-4o, 73%
       for some models). Carry-over is neither small nor confined to the same item.
    3. Nemeth, C.J., Brown, K., Rogers, J., 2001. "Devil's advocate versus authentic dissent: Stimulating
       quantity and quality." European Journal of Social Psychology 31:707–720. [VERIFIED: title/authors/
       journal/volume/pages via Wiley DOI 10.1002/ejsp.58 and Google Scholar entry] — Role-played dissent
       produces "cognitive bolstering of the initial viewpoint" rather than divergent thought; authentic
       dissent outperforms every devil's-advocate condition. One writer assigned to argue AGAINST after
       arguing FOR is the role-played case.
    4. Nickerson, R.S., 1998. "Confirmation Bias: A Ubiquitous Phenomenon in Many Guises." Review of General
       Psychology 2(2):175–220. [VERIFIED: title/author/journal/DOI 10.1037/1089-2680.2.2.175] — Evidence
       is sought and read partially to a "hypothesis in hand"; a writer who has just built the FOR case on X
       holds that hypothesis in hand when reading Y. Confirmation bias is a property of the reasoner's state,
       which is what the presumption's second clause denies.
    5. "Confirmation bias: A challenge for scalable oversight," arXiv:2507.19486. [VERIFIED: title/ID seen
       in search results; content NOT read] — Cited as a pointer that the same failure class is documented
       for LLM evaluators in oversight settings; not relied on for the verdict.
    6. Kohli, G., 2026. "Nine Judges, Two Effective Votes." arXiv:2605.29800. [VERIFIED as in
       ASSUMPTION-1263_against.md] — Sets the ceiling: even separate contexts of separate models are ~2/9
       independent. One context writing both directions cannot exceed that ceiling and the presumption
       asserts, in effect, that it reaches it.

  Strength of challenge: Strong

  Summary: The presumption has two clauses. The first ("FOR on X does not condition AGAINST on Y") is
  contradicted by AMEL, which measured cross-item polarity carry-over in 12 models at p < 10⁻⁵³ and found it
  largest on ambiguous items; and by the prior-context study, which finds large degradation from unrelated
  history. The second ("independence is a property of file-reading, not of writer state") is a definition
  that the confirmation-bias literature (Nickerson) and the dissent literature (Nemeth) reject: bias is
  carried by the reasoner's hypothesis-in-hand and by role-play, neither of which a file boundary touches.
  The human debiasing techniques that do work within one mind (consider-the-opposite) are measured at
  roughly half the value of a second judge in the best case and are not the cross-item case.

  Specific risks: (a) Orchestrator-written AGAINST files will be systematically milder on items adjacent to
  ones the same context just supported — and milder exactly where the item is ambiguous. (b) The pipeline's
  own independence accounting (the 10-of-11 claim, ASSUMPTION-1263) becomes an instrument that reports
  nominal when the condition worsens (PREMISE-179/stuck-at-nominal class). (c) REVISE-426/427 ("does adding
  agents add value?") is being answered by a design that removes the agents under load and then reports the
  single-context result under multi-agent file names.

  Mitigations available: Treat any FOR/AGAINST pair with a shared execution context as ONE reading
  (DISPOSITION-900 precedent). If one context must write both, write ALL AGAINST files before ANY FOR file
  for the cohort, or alternate, and say which in PROVENANCE. Prefer direction-level separation (one 15a
  context, one 15b context) over item-level splits — a recommendation already on record from 09-05 and
  followed this run, where it succeeded for 15a and failed for 15b.

  Search scope: Preliminary — 4 queries plus reuse of ASSUMPTION-1263 sources. Not covered: the
  sequential-judgment/order-effects literature in human rating (contrast effects, assimilation in
  serial grading); Herzog & Hertwig's dialectical-bootstrapping boundary conditions; LLM "context
  poisoning" or "fresh-context vs continued-context" ablations, which would be the decisive test.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-914
  Strongest counterargument: A context window is a writer's state, and the measured effect of that state
  on the next judgment is cross-item, polarity-following, and largest on ambiguous items (AMEL). The
  presumption relocates independence from the evaluator to the file so that a single context can claim
  two votes; but the vote count is a property of error correlation, which the file boundary does not
  reduce at all. Role-played opposition, moreover, tends to bolster the position already taken (Nemeth),
  so a same-context AGAINST written after a FOR is expected to be the weaker of the two by construction.
  What would need to be true for C2A2 to be safe: same-context pairs are never counted as two readings;
  or the pipeline enforces direction-level context separation and fails loudly (no file) rather than
  falling back to one context.
  How to test: Ablation on ≥10 past items: same prompt, AGAINST written (i) in a fresh context and (ii)
  after the same context wrote a FOR on a related item. Compare challenge strength, source count, and
  source overlap with the FOR file's framing. A systematic softening in (ii) confirms the carry-over.
