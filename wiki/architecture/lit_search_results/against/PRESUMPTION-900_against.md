SEARCH-AGAINST-PRESUMPTION-900:
  Date searched: 2026-08-31
  Original item: PRESUMPTION-900
  Original statement: [inferred] Convergence among independently generated proposals indicates
    redundancy rather than corroboration.
  Generalizable limb searched: Under what conditions does agreement between sources raise
    confidence, and is treating agreement as redundancy ever the correct default?

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: Good. 2 queries, both on-target, hitting a mature and unusually well-formalised
    literature. Books (Bovens & Hartmann 2003; Olsson 2005) accessed at snippet and review level
    only, not read. NOVELTY candidacy does not survive: this is one of the most thoroughly worked
    problems in formal epistemology.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-900
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the consolidation recommendation that the pipeline treats convergence as a
           sign of duplication rather than as evidence.
      15b: Searched for challenging literature (2026-08-31)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Bovens, L. & Hartmann, S. 2003. *Bayesian Epistemology*. Oxford University Press.
       (Snippet-level via PhilPapers, Google Books, and secondary discussion.)
       — Directly contradicts the presumption. Their Bayesian source-credibility model formalises
       witness agreement: corroborative testimony from two or more independent witnesses provides
       greater support for a hypothesis than testimony from one alone, with reliability and number
       of reports integrated via Bayes' theorem. Their Bayesian Coherentism holds that degree of
       confidence in the content of a set of propositions is positively affected by the coherence of
       the set. Agreement is evidence, not duplication.
    2. Lewis, C.I. (congruence of independently unreliable reports), as reconstructed and analysed in
       Olsson, E.J. 2005. *Against Coherence: Truth, Probability, and Justification*. Oxford
       University Press. (Snippet-level via NDPR review and secondary sources.)
       — Supplies the conditions and the sharpest counterweight. Agreement raises confidence when
       (i) the reports are independent and (ii) each report has some positive, however small, bearing
       on the claim. Where both hold, congruence can confer substantial probability even though each
       single report barely moves the needle. But Olsson's impossibility results show that coherence
       is not truth-conducive *in general*: without individual credibility, congruence does not imply
       truth. So the presumption is wrong, but its negation is not unconditional either.
    3. Roche, W. 2012. "Witness Agreement and the Truth-Conduciveness of Coherentist Justification."
       *The Southern Journal of Philosophy* 50(1). (Wiley; snippet-level.)
       — Refines the same point: witness agreement by itself implies neither an increase in the
       probability of truth nor a high probability of truth; the witnesses need some individual
       credibility, defined as accuracy better than chance.
    4. Bovens, L. & Hartmann, S. "Why There Cannot Be a Single Probabilistic Measure of Coherence."
       *Erkenntnis*. (philsci-archive.pitt.edu/2321/); with Meijs, W. "A Corrective to Bovens and
       Hartmann's Measure of Coherence" (philsci-archive.pitt.edu/2040/), and Wheeler, G. "Explaining
       the Limits of Olsson's Impossibility Result."
       — Records that the formal machinery is contested in its details. The emerging consensus in the
       probabilistic-coherence literature is that coherence cannot be truth-conducive unless sources
       are individually credible and collectively independent — which is the operative constraint for
       C2A2, not a reason to accept the presumption.

  Strength of challenge: Strong

  Summary: The presumption inverts the standard result. Across the Bayesian-epistemology literature —
  Lewis, Bovens and Hartmann, Olsson, Roche — agreement among sources is treated as the paradigm case
  of confirmation, and the interesting question is not whether it corroborates but under what
  conditions it does. Two conditions are named consistently: individual credibility (each source
  better than chance) and collective independence (no common cause of the agreement). Convergence is
  therefore *not* redundancy by default; it is corroboration by default, defeated by failure of
  either condition. What makes this more than a textbook correction for C2A2 is that the second
  condition is exactly the one the pipeline's own configuration puts in doubt, since its proposals
  are generated by agents sharing a base model. The correct posture is not the presumption but its
  conditionalised form: convergence among C2A2 agents is uninformative *because independence fails*,
  and the pipeline should say so explicitly rather than encoding a general rule that agreement means
  duplication. The distinction matters because the general rule will also fire on the cases where
  independence does hold.

  Specific risks: A pipeline that reads agreement as redundancy will systematically discard its own
  strongest evidence. Where three genuinely independent routes reach the same conclusion, the
  presumption converts a confirmation into a housekeeping problem. Compounding this, the presumption
  is self-concealing: because it deletes the convergence at intake, no downstream audit can recover
  how often convergence occurred, so the pipeline cannot measure the cost of its own rule. There is
  also an asymmetry risk — if convergence is discounted but divergence is treated as informative
  disagreement, the pipeline has an unmotivated bias toward whatever is idiosyncratic.

  Mitigations available: Replace the presumption with the two-condition test drawn from the
  literature: treat convergence as corroboration unless (a) sources cannot be shown better than
  chance on the item type, or (b) a common cause of the agreement can be identified. Record which
  disjunct fired. Preserve convergence counts as metadata even where consolidation occurs, so the
  rule's effects remain auditable. Do not let the correct local judgement about same-base-model
  agents harden into a general epistemic principle.

  STEELMAN:
    Strongest counterargument: In C2A2's actual configuration the independence condition fails so
    comprehensively that the presumption is a serviceable working rule even if it is false as stated.
    Agents share weights, prompt scaffolding, and retrieved context; their agreement is screened off
    by that common cause; and Olsson's results show that agreement without established individual
    credibility carries no truth-conduciveness anyway — and C2A2 has never established that its
    proposal-generating agents are better than chance on proposal quality. On that reading the
    presumption is an approximately correct local heuristic that has merely been stated in
    unwarranted generality.
    What would need to be true for C2A2 to be safe: either that the pipeline conditionalises the rule
    on an explicit independence judgement, or that it accepts a standing, written commitment that no
    agreement among its agents will ever be counted as evidence — and then applies that consistently,
    including to agreements it likes.
    How to test: Two measurements. (1) Credibility: on a held-out set with known-good dispositions,
    measure whether single-agent proposals are better than chance. If not, condition (i) fails and
    agreement is uninformative regardless of independence. (2) Independence: regenerate an intake
    under varied context/framing/ordering and measure how much agreement survives the manipulation —
    the effective-independent-votes measurement. Both are cheap, and (2) simultaneously settles
    ASSUMPTION-1242.

  Recommendation: CHALLENGED
