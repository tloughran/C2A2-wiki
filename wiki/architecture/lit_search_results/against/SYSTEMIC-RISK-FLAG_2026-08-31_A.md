SYSTEMIC-RISK-FLAG_2026-08-31_A:
  Filed by: Agent 15b (Literature Search AGAINST)
  Date: 2026-08-31
  Cohort: 2026-08-30 intake, methodology/epistemics cluster
  Items implicated: ASSUMPTION-1241, PRESUMPTION-901, ASSUMPTION-1242, PRESUMPTION-900
    (secondary: ASSUMPTION-1246)

  TITLE: The pipeline makes measurement-dependent judgements without taking the measurements.

  The vulnerability:
    Four of the six items in this intake turn out, on searching, to hinge on a quantity the pipeline
    does not measure and has no instrument for.

      - 1241 asserts the pipeline is "routinely amending rather than adjudicating." Both the
        Lakatosian and the formal belief-revision literatures say amendment is healthy and that the
        discriminating variable is *content change*, not amendment rate. The pipeline measures
        neither. It also has no reject rate — no record of challenges adjudicated against.
      - 901 presumes no failure mode is named for adopting every challenge. Two are (Popper's
        immunizing stratagem, Lakatos's degenerating problemshift), and both are defined over content
        loss across an amendment *chain*. The pipeline audits amendments singly and does not retain
        pre-amendment statements, so the failure is undetectable by construction.
      - 1242 recommends collapsing three co-arising proposals to one flag. Whether this destroys
        evidence or correctly removes a common-cause artefact depends entirely on whether the three
        were independent. The pipeline does not assess independence.
      - 900 presumes convergence indicates redundancy. The corroboration literature says agreement is
        evidence conditional on individual credibility and collective independence. The pipeline
        measures neither of those two conditions either.

    The same two missing instruments — a **content-change measure** and an **independence measure** —
    account for all four. The pipeline is not making bad judgements so much as making judgements
    whose correctness it has placed beyond its own ability to check. 1246 is a milder instance of the
    same shape: a threshold asserted to be "appropriate" with no false-positive or false-negative
    estimate behind it.

  Why this is systemic rather than four separate gaps:
    Each missing measurement is individually cheap to add and individually easy to rationalise away.
    Together they produce a pipeline that can always tell a coherent story about its own state and
    can never be contradicted by evidence from within itself. That is the structural signature of
    unfalsifiability by accretion described in PRESUMPTION-901 — applied not to any single statement
    but to the self-audit process as a whole. The self-audit inherits the failure mode it was built
    to detect.

  Aggravating factor — shared base model:
    Recent work found that a panel of nine frontier LLMs from seven model families carries only about
    two independent votes' worth of information, with roughly three-quarters of nominal independence
    lost to correlated errors ("Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM
    Evaluation Panels," arXiv:2605.29800, 2026; corroborated by "Correlated Errors in Large Language
    Models," arXiv:2506.07962, 2025). C2A2's agents are a far more tightly coupled case than the
    cross-provider settings those papers measure: one model, one scaffold, overlapping context. Any
    inference the pipeline draws from agreement among its own agents — including the 15a/15b
    for-and-against structure, and including this flag — inherits that correlation. The separate-context
    protocol used this cycle removes shared *conversation* state; it does not remove shared weights.

  Recommended actions (cheap, retrospective, no new architecture):
    1. Retain pre-amendment statements. Without version retention, content change is unmeasurable
       and 1241/901 cannot be settled in any future cycle.
    2. Log the reject rate: what fraction of challenges are adjudicated against with no amendment.
       A rate near zero is the sycophancy signature reported in arXiv:2608.21377 and would confirm
       1241 directly.
    3. Run one manipulation check on independence: regenerate an intake under varied context, framing
       and ordering, and measure how much agreement survives. This single experiment settles both
       1242 and 900.
    4. Plant a small number of deliberately wrong challenges per cycle and measure adoption. This is
       the only proposed test that can fail loudly, and is therefore the most valuable.
    5. Stop treating agent count as evidence strength anywhere in the pipeline until (3) has been run.

  Caveat on this flag:
    This flag was produced by the same class of process it criticises. It should be read as a
    hypothesis with a specified test (items 2, 3 and 4 above), not as a finding. If the tests are not
    run, the correct disposition is to record the flag as untested rather than as accepted — accepting
    it without test would be the very behaviour PRESUMPTION-901 warns about.
