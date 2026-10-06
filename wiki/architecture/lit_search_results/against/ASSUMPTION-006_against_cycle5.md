SEARCH-AGAINST-ASSUMPTION-006:
  Date searched: 2026-09-02
  Original item: ASSUMPTION-006 (MONITOR-2)
  Original statement: "The PRS triplet (Problem–Representation–Solution) captures research progress."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b → 15c → 15d → 15b] (cycle-5 monthly re-check)
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: original extraction
      15c (2026-04-13): dispositioned MONITOR
      15d: re-triggered, cycle 5 (59 days overdue; last substantive search 2026-04-13)
      15b (2026-09-02): searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Jansen, P. A. (2026). "The Scientific Contribution Graph: Automated Literature-based
       Technological Roadmapping at Scale." arXiv:2605.15011 (submitted 2026-05-14).
       — The largest extant empirical structuring of research progress: 2 million scientific
       contributions from 230k open-access papers connected by 12.5 million prerequisite edges.
       The operative structure is a dense many-to-many prerequisite DAG (~6 prerequisites per
       contribution), NOT a chain of self-contained triplets. Also reports that contemporary
       models reach only 0.48 MAP on temporally-backtested prerequisite prediction — i.e. even
       with a graph representation richer than PRS, forward progress is only weakly predictable.
       This is the strongest single challenge and it is new since April.

    2. Shan, Y. "A New Functional Approach to Scientific Progress." (functional account:
       science progresses when more useful research problems AND their corresponding solutions
       are proposed) — together with the objections to it catalogued in the Stanford Encyclopedia
       of Philosophy entry "Scientific Progress" (plato.stanford.edu/entries/scientific-progress/,
       Spring 2026 edition). — Shan is the closest living philosophical relative of the PRS
       assumption, which makes the standing objections to Shan directly transferable. Bird objects
       that many genuine progressive contributions (e.g. the 1895 discovery of X-rays) add
       knowledge without involving dependency relations or new exemplary practices — i.e. progress
       occurs with no well-formed problem→solution pair to record. Dellsén raises a parallel
       objection from the noetic (understanding-based) account.

    3. Stanford Encyclopedia of Philosophy, "Scientific Progress" (Spring 2026 edition).
       — Documents four live and mutually incompatible accounts of progress (epistemic/Bird,
       semantic/Niiniluoto, functional/Shan, noetic/Dellsén). PRS commits C2A2 to exactly one of
       four contested accounts. There is no settled consensus that problem-solving is the correct
       unit; adopting it is a substantive and disputed philosophical bet, not a neutral encoding.

    4. Lugg, A. (1979). "Review Symposium: Laudan and the Problem-Solving Approach to Scientific
       Progress and Rationality." Philosophy of the Social Sciences 9(4).
       — Classic critique of the ancestor of PRS: argues the distance Laudan puts between
       "solving problems" and "explaining facts" rests on an implausible view of explanation.
       Applied to C2A2: recasting an explanatory contribution as a Problem/Solution pair may
       distort rather than record it.

    5. Grünbaum, A. — "Can a Theory Answer more Questions than One of its Rivals?" (cited in the
       Laudan critical literature surfaced this cycle; discussion in "Larry Laudan: Problems,
       Truth, and Consistency," Studies in History and Philosophy of Science,
       sciencedirect.com/science/article/pii/003936818290005X). — Raises the individuation
       problem: problems cannot be counted without a prior criterion for what makes two problems
       the same problem. C2A2 uses triplets as "the atomic unit of measured progress," which
       presupposes exactly the individuation criterion this literature says is missing. Note:
       surfaced via secondary discussion, not read in the original.

    6. Kuhn / Stegmüller "progress branching" (as characterised in the SEP entry and in Hektoen
       International, "Objections to Kuhn's theory of scientific progression"). — Multiple
       distinct routes can reach the same epistemic destination, and paradigm change can
       retroactively dissolve the problem a triplet was indexed to. A triplet whose Problem no
       longer exists is not a partial success; it is uninterpretable.

  Strength of challenge: Moderate

  Summary: PRS survives this cycle as a defensible but contested choice rather than a neutral
  one. Nothing found directly falsifies it — problem-and-solution IS a live, seriously defended
  account of progress (Shan's functional account). But three things count against it as an
  ATOMIC unit of MEASURED progress. First, the largest empirical attempt to structure real
  research progress at scale (Jansen 2026) converges on a dense prerequisite DAG averaging ~6
  incoming edges per contribution, not on discrete triplets. Second, the individuation problem is
  unresolved: counting triplets presupposes a criterion for problem-identity that the
  problem-solving tradition has never supplied. Third, Bird's objection bites specifically at the
  boundary C2A2 cares about — discoveries that add knowledge without a formulable problem/solution
  pair are simply invisible to a PRS-only encoding.

  Specific risks: If PRS is false as an atomic unit, C2A2's progress measurements are not merely
  noisy but non-comparable across traditions — two analysts splitting the same body of work into
  different numbers of triplets produce different "progress," with no fact of the matter
  adjudicating between them. Cross-tradition comparison (the whole point of holding 14 thinkers in
  one frame) then silently compares artefacts of the segmentation, not the work. Second risk:
  systematic blind spot for contributions of the X-ray type — a phenomenon noticed, a distinction
  drawn, a reframing offered — none of which fit a Problem/Solution slot and all of which are
  disproportionately common in the more speculative traditions in this vault. Third: dependency
  structure is lost. If real progress is a 6-edge-average DAG and C2A2 records 1-in/1-out
  triplets, the representation is lossy in a direction that makes progress look more linear and
  more attributable than it is.

  Mitigations available:
    1. Keep PRS as an index, demote it as a metric. Use triplets for retrieval and cross-linking;
       do not sum or compare triplet counts as a progress score.
    2. Add explicit prerequisite edges between triplets (Jansen's structure), so the DAG C2A2
       actually has is visible rather than implied.
    3. Add a non-PRS escape hatch: a "contribution without a problem" record type for
       observations, distinctions, and reframings that have no natural Solution slot.
    4. Record segmentation provenance — who split this work into these N triplets — so
       non-comparability is at least legible.
    5. Inter-coder reliability test on triplet segmentation (see How to test).

  STEELMAN:
    Item: ASSUMPTION-006
    Strongest counterargument: Problems and solutions are not the atoms of research; they are
    summary descriptions imposed after the fact, and the imposition is not unique. There is no
    principled way to count problems, so a triplet count measures the coder's granularity habits
    rather than the field's progress. Where progress has actually been structured at scale, it
    came out as a many-to-many prerequisite graph with ~6 antecedents per contribution and only
    0.48 MAP predictability — not a sequence of triplets. And the problem-solving account is one
    of four live and incompatible philosophical accounts, so PRS quietly settles by fiat a
    question the field has not settled, in a way that makes any contribution lacking a formulable
    problem (a new observation, a new distinction, a reframing) systematically invisible.
    What would need to be true for C2A2 to be safe: (a) PRS is used as an organising index rather
    than as a cardinal progress metric; (b) triplet boundaries are stable enough that independent
    coders agree — this is empirically checkable and currently unchecked; (c) contributions with
    no natural problem/solution shape are captured by some other record type rather than dropped;
    (d) no cross-tradition claim rests on comparing raw triplet counts.
    How to test: Yes, cheaply and directly. (1) Inter-coder reliability: have three independent
    passes segment the same 20 source documents into PRS triplets; compute agreement on triplet
    count and boundaries. Low agreement falsifies "atomic unit" immediately. (2) Coverage audit:
    take 50 contributions the vault already treats as significant and count how many resist PRS
    encoding without distortion. (3) Historical backtest: encode a known trajectory that contains
    a paradigm shift and check whether pre-shift triplets remain interpretable post-shift.

  Search scope: Queries actually run this cycle —
    - "critique of Laudan problem-solving model of scientific progress"
    - "scientific progress not linear branching model philosophy of science critique"
    - "operationalizing scientific progress metrics failure problem solution decomposition
       knowledge graph 2026"
    - "Stanford Encyclopedia scientific progress semantic epistemic functional accounts
       problem-solving objection"
    - "Shan functional account scientific progress objections Bird Dellsén research problem
       exemplary practice"
    - "'individuation of problems' Laudan counting problems solved objection incommensurability"
    - "2026 critique problem-solution triplet extraction scientific claims coverage misses
       implicit unstated assumptions LLM"
    - "'Scientific Contribution Graph' automated literature-based technological roadmapping
       prerequisite relationships arXiv 2605.15011"
    - "Dellsén noetic account scientific progress objection understanding versus problem solving
       2025 2026"
    Gaps: no full-text read of Shan, Lugg, or Grünbaum originals — those are characterised from
    the SEP entry and from search-result abstracts. No search of the science-of-science /
    bibliometrics literature on progress measurement. No search in languages other than English.

  Search confidence: comprehensive search (for the philosophy-of-progress and 2026 ML-structuring
  angles); preliminary for the bibliometrics/science-of-science angle — a broader search there is
  recommended.

  New since cycle 4 (i.e. since 2026-04-13):
    1. GENUINELY NEW AND MATERIAL: Jansen (2026), arXiv:2605.15011, published 2026-05-14 — after
       the April search. First at-scale empirical structuring of research progress (2M
       contributions / 12.5M prerequisite edges). Its DAG-with-many-prerequisites structure is
       the strongest available evidence that the atomic unit of progress is not a triplet, and
       its 0.48 MAP ceiling is the first quantitative handle on how predictable progress is under
       ANY structured representation.
    2. The SEP "Scientific Progress" entry now has a Spring 2026 edition carrying the four-account
       taxonomy including Shan's functional account and the Bird/Dellsén objections to it. The
       April file did not engage Shan at all, which was a real gap — Shan is the closest
       philosophical ally PRS has, and the objections to Shan are the objections that matter most.
    3. RECORD-INTEGRITY NOTE, not new literature: cycles 1, 2 and 3 (2026-04-27, 2026-05-17,
       2026-05-25) each recorded "no new challenging literature surfaced" with zero sources and no
       evidence of a search having been run. Those three entries should be treated as null, not as
       three independent confirmations. Cycle 5 is effectively the second real search on this item.
    4. RECORD-INTEGRITY NOTE: the cycle-0 (2026-04-13) source list on this item does not fully
       hold up. It defines PRS as "Problem-Response-State" — a DIFFERENT triplet from the
       "Problem–Representation–Solution" given in the current cycle-5 tasking. Much of the April
       challenge (arguing against "forward movement through states") attacks the Response/State
       reading and does not transfer cleanly to the Representation/Solution reading. Separately,
       the April entry cites "West & Bergman (2010), 'The Emergence of Irreversible Time and
       Thermodynamics from Quantum Mechanics,' Physical Review E, 102(6), 062110" — I searched for
       this specifically and could not locate it; the volume number is also inconsistent with the
       stated year. It should not be carried forward. The Zajonc (1968) mere-exposure citation is
       real but its application to PRS is a stretch.

  Recommendation: PARTIALLY-CHALLENGED
    Retain MONITOR. The challenge is real but bounded: PRS is defensible as an index and
    questionable as a cardinal metric. Priority action is not more literature search — it is the
    inter-coder reliability test above, which would settle the "atomic unit" question internally
    within a day. Also recommend reconciling the PRS definition drift between the April record and
    the current tasking before the next cycle, since the two readings attract different objections.
