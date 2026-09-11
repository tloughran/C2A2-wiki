SEARCH-FOR-ASSUMPTION-1310:
  Date searched: 2026-09-11
  Original item: ASSUMPTION-1310
  Original statement: "*MONITOR-599 turns the pipeline on itself.* 15b surfaced Nemeth's finding that
    **assigned** devil's advocacy produces cognitive bolstering rather than genuine challenge — **which is
    a question about Agent 15b by construction, and therefore about every premise in the register.**
    Filed at High with a cheap in-house test named (blind re-run of one item by an agent not told its
    direction)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1310
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim and routed as PRIORITY. If it holds, the epistemic weight assigned to every
        CHALLENGED status in `presumptions.md` and `assumptions.md` is inflated, and 15b's 42 CHALLENGED
        presumptions are the exposed set. The named test is cheap, decisive, and unowned — the pattern
        REVISE-436 tracks. Surfaced as PRESUMPTION-949.
      15a: Searched for supporting literature; retrieved the primary Nemeth source and confirmed the
        bolstering finding, AND retrieved a meta-analysis that cuts the other way and which the original
        15b summary did not surface. Both are reported.
    Current status: PARTIALLY-SUPPORTED

  Register pre-check: Two ACTIVE premises bear closely, and PREMISE-152 is nearly on point.
    - PREMISE-152: "HOMOGENEOUS, UNGUIDED multi-agent debate does not outperform isolated
      self-correction at matched compute. Gains from debate require heterogeneity of agents, role
      guidance, or an explicit calibration mechanism." Note the direction: role guidance is listed among
      the things that *produce* gains, which is in tension with ASSUMPTION-1310's claim that assigned
      role is precisely what fails. This is the sharpest register-level tension found in this cycle.
    - PREMISE-197: agreement among independently-run generators is corroboration by default and
      redundancy only when a common cause screens it off; for agents sharing a base model or prompt
      scaffold the common cause is present.
    - PREMISE-111: the read channel was not the dominant correlation source between 15a and 15b; frontier
      LLMs sharing no procedural channel collapse to roughly two effective votes out of nine. Relevant
      because it already establishes that 15a/15b independence is weak on a channel the blind re-run
      would not test.
    - PREMISE-180: LLM errors are substantially correlated across models and the correlation rises with
      capability.
    Also PREMISE-075 (error decorrelation from reference-frame variation, not seed variation) — which is
    arguably the *strongest argument for* the 15a/15b architecture in the register and cuts against 1310.
    Searched anyway per OPEN-192; this item was also partly pre-searched by 15b.

  Supporting evidence found: Yes — the primary source says what 15b reported it says.

  Sources:
    1. Nemeth C., Brown K., Rogers J. 2001. "Devil's advocate versus authentic dissent: stimulating
       quantity and quality." European Journal of Social Psychology 31(6):707-720. — SECONDARY (Wiley
       abstract page returned an empty body on direct fetch; findings confirmed from two independent
       retrieved descriptions including a citation report and a peer-reviewed secondary discussion) —
       The primary source. Findings as retrieved: the devil's advocate condition "did not reach the level
       of the original thoughts stimulated by the authentic dissenter but did stimulate a greater amount
       of thoughts that supported the initial viewpoint"; the authentic-minority condition generated the
       most solutions. The bolstering result 15b reported is real and is correctly attributed.
    2. Nemeth C. 2001. "Improving Decision Making by Means of Dissent." Journal of Applied Social
       Psychology 31(1). — SECONDARY (located, not retrieved in full) — Companion statement of the
       programme: uniformity and premature adoption of preferred solutions degrade decisions, and
       mechanisms for manufacturing dissent were introduced in the hope of reproducing authentic
       dissent's effects.
    3. Nemeth C.J. 2010. "Minority Influence Theory." IRLE Working Paper #218-10, UC Berkeley. — SECONDARY
       (located via search; PDF not fetched) — Contains the programme-level statement quoted in
       secondary sources: "in a prior study comparing these two processes, devil's advocate appeared to
       foster thinking that was primarily aimed at cognitive bolstering of the initial viewpoint rather
       than stimulate divergent thought."
    4. The bolstering mechanism as described in secondary sources: "armed with the belief that they have
       considered alternatives by virtue of exposure to the DA, people may become even more convinced of
       the truth of their initial position — and possibly more rigid and resistant to reconsideration."
       — SECONDARY — This is the *inoculation* variant of the finding, and it is the one that transfers
       worst to this pipeline's structure (see Caveats) but worst for the estate if it does transfer:
       it implies that having run 15b makes a CHALLENGED status more trusted than it should be.
    5. Schwenk C.R. 1990. "Effects of devil's advocacy and dialectical inquiry on decision making: A
       meta-analysis." Organizational Behavior and Human Decision Processes 47(1):161-176. — SECONDARY
       (abstract-level retrieval across three independent index pages; full text not fetched) — REPORTED
       AGAINST INTEREST. The only meta-analysis located on this question found that devil's advocacy was
       MORE effective than an expert-based, no-conflict approach in general. 15b's summary, as quoted in
       the item, did not surface this. It does not refute Nemeth's mechanism — the comparison classes
       differ (Nemeth: DA vs authentic dissent; Schwenk: DA vs no structured conflict) — but it
       establishes that the relevant question for this pipeline is which comparison applies.

  Strength of support: Moderate — strong for the narrow finding as stated by Nemeth, materially weakened
    once the comparison class is made explicit and the meta-analysis is admitted.

  Summary: The primary attribution is sound: Nemeth, Brown & Rogers (2001) does find that assigned
    devil's advocacy stimulated more thoughts supporting the initial viewpoint and fewer original
    thoughts than authentic dissent, and 15b reported it accurately. But the finding's force for this
    pipeline depends entirely on which comparison is in play, and that is where the item overreaches.
    Nemeth's comparison is DA versus *authentic dissent* — a genuine minority holder. The C2A2 pipeline's
    live alternative is not authentic dissent; there is no agent that independently holds the contrary
    view. The realistic counterfactual is 15a alone, or no adversarial pass at all, and against *that*
    comparison Schwenk's meta-analysis reports DA as superior. So the correct reading is not "15b
    produces nothing" but "15b produces less than a genuinely independent challenger would, and its
    output may carry unearned reassurance." The second clause — the inoculation effect, whereby having
    run an adversarial pass raises confidence beyond what the pass warrants — is the clause that actually
    threatens the register, and it is the one the named in-house test does not measure.

  Caveats:
    - Comparison-class error is the central caveat and it is load-bearing. Adopting this item without
      naming the counterfactual would license retiring 15b, which the evidence does not support.
    - Transfer to LLM agents is not established by any source retrieved. Nemeth's participants are humans
      whose prior beliefs bolster; an LLM instantiated per-item has no persisting initial viewpoint to
      bolster. The mechanism may transfer via a different route (instruction-following producing
      direction-consistent output regardless of evidence) but that is a distinct claim and I found no
      literature on it. See NOVELTY-FLAG.
    - The named in-house test is underpowered for the claim. A blind re-run of ONE item distinguishes
      almost nothing: under PREMISE-182's closed form, a single concordant result gives a 95% lower bound
      on concordance of 0.05, i.e. no information. The test as named is decisive only if it FAILS. This
      should be recorded before it is run, not after.
    - PREMISE-111 already establishes that the dominant 15a/15b correlation channels are shared
      pre-training, alignment and prompting — none of which a direction-blind re-run removes. A blind
      re-run therefore tests the weakest of the suspected channels.
    - PREMISE-152 and PREMISE-075 both point the other way and are ACTIVE. Any minting here must address
      them or it will contradict the register.
    - Wiley's abstract page for the primary source returned an empty body on fetch; the Nemeth findings
      are SECONDARY. I could not obtain the numeric results (solution counts, thought-valence counts) and
      have therefore reported no numbers from it.

  NOVELTY-FLAG:
    Item: Whether role-assigned adversarial prompting of an LLM agent reproduces the human cognitive-
      bolstering effect that Nemeth documents for assigned devil's advocacy.
    Searched: Nemeth primary and programme sources; Schwenk meta-analysis; multi-agent debate and
      LLM-critic literature; conversational-agent devil's-advocate studies (one 2025 arXiv paper located
      on conversational agents challenging social influence in group decision-making, not retrieved).
    Finding: No source located that measures whether an instruction-assigned adversarial LLM produces
      genuine disconfirming evidence versus direction-consistent output. The nearest adjacent result is
      the unguided-homogeneous-debate literature behind PREMISE-152, which is about a different
      mechanism.
    Implication: The transfer step from Nemeth to Agent 15b is an inference of this estate's own, not a
      finding in the literature, and should be recorded as such rather than as "Nemeth's finding applies
      to 15b."
    Recommended status: NOVEL — and FAVOURABLE. This is a well-posed, cheap, publishable question that
      nobody appears to have asked, and the estate is unusually well placed to answer it because it runs
      both directions on the same items. The novelty is a genuine contribution, not a symptom of a
      malformed question.

  Search scope: comprehensive search — Nemeth primary sources (2001 EJSP, 2001 JASP, 2010 minority
    influence working paper), cognitive bolstering, authentic vs contrived dissent, Schwenk 1990
    meta-analysis, dialectical inquiry vs devil's advocacy vs consensus (Schweiger et al. AMJ),
    LLM multi-agent debate and adversarial-critic literature.

  Recommendation: PARTIALLY-SUPPORTED — the recommendation rests on the attribution limb (Nemeth says
    what 15b said he says: assigned DA produces bolstering relative to authentic dissent) and NOT on the
    application limb (that this discounts every CHALLENGED status). Specific recommendations: (1) record
    Schwenk 1990 against the item, since it is the only meta-analysis found and it was not surfaced;
    (2) restate the item with its comparison class explicit; (3) re-scope the named in-house test, which
    at n=1 can only produce a negative result, and give it an owner — it remains the right test.
