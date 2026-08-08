SEARCH-FOR-PRESUMPTION-696:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-696
  Original statement: That the evaluator condition of REVISE-283 can be
    satisfied by a component built inside C2A2; the whole remedy space
    entertained is "add another agent," and whether an agent minted by the same
    designer, on the same model family, reading the same registers, counts as
    "a component that did not produce the artefact" is never asked. Risk: High.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-696
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the form of the remedy against the wording of the
        condition it must satisfy.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Institute of Internal Auditors, IPPF Standard 1100 "Independence and
       Objectivity" and Standard 1110 "Organizational Independence"
       (implementation guidance PDFs, theiia.org; also IPPF Practice Guide
       "Independence and Objectivity," October 2011). — The strongest direct
       support, and it supports the narrow reading. The entire internal audit
       profession rests on the proposition that a component built inside the
       organisation can carry an independence warrant. Independence is defined
       as freedom from conditions that threaten unbiased performance, and the
       guidance states it is achieved by ensuring the audit activity has no
       management responsibility for the functions it assesses and by
       separating management of the audit activity from functional oversight by
       senior management. That is a structural, internal remedy. Support for
       "a component built inside C2A2 can in principle satisfy an
       independence-of-evaluator condition" is direct and institutional.
    2. ISO 9001:2008, Clause 8.2.2 — "auditors shall not audit their own work."
       [Clause text as reported across several practitioner sources this
       session; the 2015 revision's equivalent wording was not verified.] —
       This is almost verbatim the condition REVISE-283 states. The standard
       treats it as satisfiable by internal reassignment: a different person in
       the same organisation, trained the same way, using the same procedures,
       counts. The presumption's implicit test — "did this component produce
       the artefact?" — is exactly the test the standard applies, and the
       standard does not additionally require substrate diversity.
    3. Practitioner and preprint work on the generation-verification gap
       (e.g. arXiv preprint "Learning to Self-Verify Makes Language Models
       Better Reasoners," ID 2602.07594 as returned; Tim Williams, "LLM
       Verification Loops: Best Practices and Patterns," Medium). [Both located
       by title/URL only; neither opened; authors, venue and any figures
       unverified. The Medium piece is non-peer-reviewed.] — Reports the
       asymmetry the remedy relies on: separating generation from review
       outperforms self-refinement, on the premise that checking is easier than
       producing. This is the theoretical grounding for "add another agent"
       being worth anything at all. It is weak evidence and I am marking it
       weak: the ~20% improvement figure appears in a practitioner blog post I
       did not open and should not be quoted as a measured result.
    4. Knight, J.C. & Leveson, N.G., 1986. "An Experimental Evaluation of the
       Assumption of Independence in Multiversion Programming." IEEE
       Transactions on Software Engineering. [Classic; PDFs located at
       sunnyday.mit.edu this session, not opened. Related: Brilliant, Knight &
       Leveson, "Analysis of Faults in an N-Version Software Experiment," IEEE
       TSE, DOI 10.1109/32.44387.] — Located as supporting evidence and it does
       not support. Twenty-seven versions written independently from one
       specification, one million test cases; coincident failures occurred far
       more often than independence predicts. The stated mechanism is the one
       this item names: shared specification, shared training background,
       shared reference material produce common misinterpretations. This is the
       single most on-point result for the half of the presumption the item
       says was never asked, and it is negative.
    5. Recent preprint literature on correlated verifiers in LLM stacks —
       titles located this session include "Partially Correlated Verifier
       Cascades in LLM Harnesses" (arXiv 2607.13918), "How Independent are
       Large Language Models? A Statistical Framework for Auditing Behavioral
       Entanglement and Reweighting Verifier Ensembles" (arXiv 2604.07650),
       "Chain-of-Models: Cross-Model Auditing for Bias-Robust LLM Judges"
       (arXiv 2607.28636). [All located by title and arXiv ID only. None
       opened. Authors, venues and all quantitative claims UNVERIFIED — I am
       recording that this body of work exists and points one way, not any
       specific number from it.] — The search summary reported figures such as
       an average 64.5% of self-generated errors surviving self-checking across
       14 open models, and that multi-agent critique with same-model copies
       performs no better than self-consistency. I did not verify either
       figure and it should not be cited downstream as verified. The direction
       is nonetheless consistent across every source located.
    6. Condorcet Jury Theorem and the ensemble diversity literature (general;
       see also Brown & Kuncheva, "'Good' and 'Bad' Diversity in Majority Vote
       Ensembles," located via ResearchGate this session — authors and year
       from established knowledge, not confirmed in the result snippet). —
       Theoretical grounding for why "add another agent" can help and the exact
       condition under which it stops helping. The theorem's guarantee requires
       independent errors, not merely independent outputs; under positively
       correlated errors the effective number of votes is much smaller than N
       and the ensemble degrades toward an echo chamber. This gives the
       presumption a principled form: internal evaluators help to the degree
       their errors decorrelate from the producer's, and not otherwise.

  Strength of support: Weak

  Summary: The presumption splits into two claims and the literature treats
    them very differently. On the narrow claim — that a component built inside
    the system can satisfy a "did not produce the artefact" condition — support
    is direct and institutional: the whole of internal audit practice is built
    on it, IIA Standards 1100/1110 define independence organisationally rather
    than externally, and ISO 9001's "auditors shall not audit their own work"
    states essentially the same condition REVISE-283 states while treating
    internal reassignment as sufficient to meet it. On the wider claim the item
    actually surfaces — that an agent minted by the same designer, on the same
    model family, reading the same registers, is thereby an independent
    evaluator — no supporting source was located and the most on-point evidence
    runs the other way. Knight and Leveson's multiversion experiment is the
    canonical measurement of exactly this failure, and its stated mechanism
    (shared specification, shared training, shared reference material) maps
    onto every one of the three sharings the item names. The Condorcet
    literature supplies the reason: majority-vote guarantees require
    independence of errors, not of components, and positively correlated errors
    shrink the effective vote count. A recent and rapidly growing preprint
    literature on same-family verifier correlation points the same way, though
    I could not verify its numbers. The honest FOR position is therefore
    conditional support: the remedy form is legitimate and well precedented,
    but its warrant is proportional to error decorrelation, which is precisely
    the quantity C2A2 has not measured.

  Caveats: Source 1's transfer is by analogy and the analogy is imperfect in a
    specific way. Internal auditors share an employer, a procedure manual and
    an incentive structure with the audited function, but they do not share a
    perceptual apparatus; two humans in one firm still see with different eyes.
    An agent on the same model family shares the failure modes of the substrate
    itself, which has no counterpart in the audit standards, and none of the
    audit literature located was written with that condition in view. Source 4
    is 1986 software engineering; transfer to LLM agents is by analogy on
    mechanism rather than by measurement, though the mechanism transfers
    unusually cleanly. Sources 3 and 5 are preprints and blog material located
    by title only and carry no verified figures; the generation-verification
    gap in particular is reported as contested in the same search results
    ("Mind the Gap," arXiv 2412.02674, and an OpenReview submission on
    self-verification limitations were both returned), so it should not be
    treated as settled. Publication bias is worth naming here in the unusual
    direction: negative results about verifier independence are currently
    fashionable and may be over-represented in 2025-26 preprints.

  NOVELTY-FLAG: Not raised. The general question of evaluator independence
    under shared substrate is actively worked on. One sub-question was not
    answered by any located source and may be worth flagging separately: no
    source was found that gives an operational test for whether a given
    internally-minted evaluator has decorrelated enough from the producer to
    satisfy an independence condition. The literature says the quantity
    matters; it does not say how to measure it cheaply in a system like C2A2.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Adequate; not comprehensive. Concepts searched: auditor and
    evaluator independence conditions and their institutional definitions;
    self-testing and self-verifying systems; correlated failure in homogeneous
    verification stacks; independence assumptions in ensemble and committee
    methods; N-version programming and the Knight-Leveson result; the
    generation-verification gap. Not searched: formal verification and
    proof-carrying approaches, which would speak to the one escape route the
    item's remedy space excludes (an evaluator that is not another agent at
    all); Byzantine fault tolerance and its independence assumptions; the
    security literature on trusted computing bases, which addresses "who
    verifies the verifier" directly. All three are recommended follow-ups.
