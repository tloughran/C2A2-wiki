SEARCH-AGAINST-PRESUMPTION-1125:
  Date searched: 2026-10-13
  Original item: PRESUMPTION-1125
  Original statement: [unstated] In redundant monitoring, does deferring to a co-located peer (rather
    than independent re-check) erase the reliability gain of redundancy (common-mode failure, N-version
    programming, diffusion of responsibility)?
  Under test: the premise that deferring to a peer ERASES the redundancy gain. I searched for evidence
    that the gain is reduced but not erased, and for evidence that independent re-checking is also less
    independent than assumed.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output for this item.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1125
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b (2026-10-12): Inferred from 2026-10-12 transcripts, where a second monitor deferred to a peer's
        status instead of re-checking.
      15b (2026-10-13): Searched for challenging literature. 3 searches: Knight & Leveson 1986
        N-version programming; sequential redundancy and social loafing (Cymek & Manzey); independent
        double checks in medication administration (Koyama et al. 2020). 1 fetch: DepositOnce record
        for Cymek & Manzey 2022 (abstract only).
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: PRELIMINARY. One fetched abstract. Everything else is snippets.
  Search scope: preliminary (3 searches, 1 fetch).

  Challenging evidence found: Partial
  Strength of challenge: Moderate

  Sources:
    1. Cymek DH & Manzey D. 2022. "Sequential human redundancy: Can social loafing diminish the safety
       of double checks?" J Exp Psychol Appl. doi:10.1037/xap0000439. [fetched, abstract only] In two
       experiments, when the second checker could see the first checker's verdicts (nonblinded), the
       second checker's effort dropped substantially. Yet "even nonblinded redundancy led to an overall
       safety advantage over a single-checker condition". Social loafing "does not necessarily reduce
       the gains in overall reliability". Blinded checking showed no loafing and near-perfect team
       performance. Bearing: this directly contradicts "erases". Deference degrades the gain without
       eliminating it, at least in this lab task.
    2. Cymek/Manzey group, 2018. "Redundant Automation Monitoring: Four Eyes Don't See More Than Two, if
       Everyone Turns a Blind Eye." Human Factors. [snippet] Collective monitoring without individual
       feedback produced fewer cross-checks and 25% fewer detected automation failures, so the team did
       not outperform individuals. With individual feedback expected, a team advantage appeared. Bearing:
       this is a boundary condition. Erasure is possible, and it depends on accountability design.
       Erasure is not inherent to having a peer.
    3. Knight JC & Leveson NG. 1986. "An Experimental Evaluation of the Assumption of Independence in
       Multiversion Programming." IEEE TSE 12(1):96-109. [abstract/snippet] Twenty-seven independently
       developed versions showed far more coincident failures than independence predicts, because
       people err "on the same hard parts". Bearing: this challenges the comparison, not the premise.
       An "independent re-check" by an agent sharing the same model, prompt template, or data also
       carries correlated failures. The gap between deferring and re-checking is smaller than the
       premise implies.
    4. Koyama AK, Maddox CS, Li L, Bucknall T, Westbrook JI. 2020. "Effectiveness of double checking to
       reduce medication administration errors: a systematic review." BMJ Qual Saf 29(7):595-603.
       [snippet] There is insufficient evidence that double checking reduces errors or harm. Only 3 of
       13 studies distinguished independent from "primed" checks. A companion observational study found
       92.5% of mandated double checks were primed and only 1.0% truly independent. Bearing: in the
       field, mandated independence collapses into deference, and the measured benefit of even nominal
       redundancy is weak. The evidence for an independence gain is thin in both directions.

  Summary: The direct experimental test of sequential deference (Cymek & Manzey 2022) finds that
    nonblinded checking reduces the second checker's effort but keeps a net reliability advantage over
    a single checker. That contradicts "erases". Erasure does appear when accountability is diffuse
    (2018). The N-version literature adds a deeper challenge: independent re-checks fail together much
    more than independence predicts, so the premise overstates what true re-checking buys when checkers
    share a substrate (same LLM, same prompts). Field evidence (Koyama 2020) shows nominal independence
    usually degrades into primed checking, with weak evidence of benefit either way.

  Specific risks: (a) C2A2 adds an "independent" re-check run by the same model with the same context
    and counts it as a second independent vote (Knight & Leveson). (b) Over-reacting by removing peer
    visibility entirely may waste the false-alarm reduction that seeing the first checker's verdict
    gives (the 2024 follow-up, snippet). (c) No per-checker accountability, which is the condition under
    which erasure did occur.

  Mitigations available: Blind the second checker to the first's verdict. Give each checker its own
    attributable record (individual accountability). Diversify the substrate (different method, data
    path, or model) rather than repeating the same check. Measure coincident-failure rates.

  STEELMAN:
    Item: PRESUMPTION-1125
    Strongest counterargument: "Erases" is empirically too strong. The best controlled test shows that
      a deferring second checker still adds net reliability. The real danger lies in the opposite
      direction: treating a re-check as independent because it was run separately, when
      correlated-failure research shows separately produced judgments fail together on the hard cases.
      For a pipeline of agents built on one model family, diversity of substrate matters more than
      blinding. Two blinded copies of the same checker may add less than one deferring checker that
      uses a different method.
    What would need to be true for C2A2 to be safe: Re-checks differ in method or data path, not only in
      invocation. Each checker's verdict is attributable. Deference is visible in logs.
    How to test: Seed known faults. Measure detection by checker A alone, by B deferring, by B blinded,
      and by B with a different method. Compare coincident misses.

  Boundary conditions identified:
    - The social-loafing results concern human motivation. Whether LLM agents "loaf" when shown a peer
      verdict is an anchoring question, not a motivational one, and it is untested here.
    - Knight & Leveson used human programmers. A 2026 report of an LLM-agent replication was seen in a
      blog snippet only and is unverified.

  Recommendation: PARTIALLY-CHALLENGED

  SYSTEMIC-RISK-FLAG: see SYSTEMIC-RISK-FLAG_2026-10-13_remedy-is-another-proxy_1778-1780-1124-1125-1127.md
