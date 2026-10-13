SEARCH-FOR-PRESUMPTION-1125:
  Date searched: 2026-10-13
  Original item: PRESUMPTION-1125
  Original statement: In redundant monitoring, does deferring to a co-located peer (rather than independent re-check)
    erase the reliability gain of redundancy (common-mode failure, N-version programming, diffusion of
    responsibility)?

  Premise tested (unstated, inferred by 14b): If a second monitor defers to a peer's result, or shares its
    environment, the redundancy gives little real reliability gain. Independence, not duplication, is what makes
    redundancy work.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1125
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-10-12 transcripts in which a redundant checker accepted a co-located peer's status
        rather than re-checking; queued 2026-10-12
      15a (2026-10-13): 3 web searches (Knight & Leveson N-version independence; beta-factor common-cause failure;
        social loafing in double-checking). 1 fetch: TU Berlin DepositOnce record for Cymek & Manzey 2022 (abstract
        read; PDF not opened).
    Current status: PARTIALLY-SUPPORTED (Moderate). The direction is supported, but "erase" is too strong.

  Search scope: PRELIMINARY. Software fault tolerance, reliability engineering (IEC 61508 CCF), and human-factors
    redundancy.

  Supporting evidence found: Partial (strong for "degrades"; mixed for "erases")

  Sources:
    1. Knight, J.C. & Leveson, N.G., 1986. "An Experimental Evaluation of the Assumption of Independence in
       Multiversion Programming." IEEE TSE 12(1):96-109. [search-result summary] 27 independently written versions,
       1M test cases each. Coincident failures were far more frequent than independence predicts, and the authors
       show N-version systems can in theory be less reliable than a single version. Relevance: direct. Even nominally
       independent redundancy shares failure modes, so deliberate deference makes this worse. Hatton's later
       replication reportedly agrees (not verified).
    2. Beta-factor common-cause-failure model (IEC 61508; ReliaSoft and Mälardalen University expositions).
       [search-result summary] With a common-cause fraction beta, a duplex system's failure rate is about beta*lambda
       instead of lambda^2. In one worked example, beta = 0.05 gives roughly a 500x degradation from the
       independent-redundancy estimate. Mitigation is "diversity plus separation". Relevance: quantitative grounding.
       Co-location raises beta, and deferring to the peer's verdict pushes beta toward 1, which removes the gain.
    3. Cymek, D.H. & Manzey, D., 2022. "Sequential human redundancy: Can social loafing diminish the safety of double
       checks?" J Exp Psychol: Applied 28(4):931-945. [FETCHED, abstract] Non-blinded second checkers (who saw the
       first checker's verdict) cut effort substantially. Blinded checkers did not, and their teams achieved
       near-perfect performance. Note: even non-blinded redundancy still beat a single checker. Relevance: supports
       the mechanism (deference reduces the second check's contribution) but contradicts "erase".
    4. Cymek, Jahn & Manzey (parallel monitoring of automation; TU Berlin). [search-result summary] Redundant
       crewmates cross-checked automation less, and team-level cross-checks did not differ significantly from a
       single operator, i.e. the gain could be fully cancelled. Individual performance feedback restored it.
       Relevance: closest support for "erase". Exact citation details not verified.

  Strength of support: Moderate. Strong that deference and co-location degrade redundancy. Mixed on full erasure.

  Summary: Three literatures support the premise. Software fault tolerance shows that nominally independent versions
    fail together far more than assumed. Reliability engineering quantifies how common-cause coupling (beta)
    collapses redundancy gains, with diversity and separation as the fix. Human-factors experiments show that a
    second checker who can see the first's verdict reduces effort (social loafing). Blinding and individual
    accountability prevent this. In one parallel-monitoring study, redundancy gave no significant gain. In the
    sequential study it still helped, so "erases" holds in some configurations and "reduces" in others. The design
    stance that a redundant check must re-derive independently, without reading the peer's verdict, is well supported.

  Caveats: (i) The human social-loafing mechanism (motivation, felt responsibility) does not map cleanly onto LLM
    agents. The closer analogue for agents is anchoring on a peer's output plus shared inputs and models (common
    mode). (ii) The Knight & Leveson results were contested by NVP proponents (Avizienis line), and the authors
    published a 1990 reply. (iii) Beta values are often expert-estimated.

  NOVELTY flag: Partial. The principle is established across fields. Its application to LLM-agent peer monitoring,
    where agents share a base model (a strong common mode), was not found in this search. A recent
    arXiv:2606.20158 "N-Version Programming with Coding Agents" appeared in results but was not read.

  Recommendation: PARTIALLY-SUPPORTED (Moderate). Supported as "substantially degrades and can erase"; not as "always
    erases". Recommend a follow-up read of arXiv:2606.20158.
