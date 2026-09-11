SEARCH-AGAINST-ASSUMPTION-1310:
  Date searched: 2026-09-11
  Original item: ASSUMPTION-1310
  Original statement: "*MONITOR-599 turns the pipeline on itself.* 15b surfaced Nemeth's finding that
    **assigned** devil's advocacy produces cognitive bolstering rather than genuine challenge — **which is
    a question about Agent 15b by construction, and therefore about every premise in the register.**
    Filed at High with a cheap in-house test named (blind re-run of one item by an agent not told its
    direction)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1310
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim and routed as [QUEUED — PRIORITY]. If it holds, the epistemic weight of
        every CHALLENGED status in both registers is inflated; 15b's 42 CHALLENGED presumptions are the
        exposed set. Surfaced as PRESUMPTION-949.
      15b: Searched for challenging literature against a claim about 15b itself. Found the one meta-
        analysis runs FOR assigned devil's advocacy; found the human→LLM transfer is specifically
        unreliable; and found that the LLM-specific failure mode is the OPPOSITE of bolstering and is
        worse for this architecture than the one the item names.
    Current status: PARTIALLY-CHALLENGED — with an aggravating finding attached

  **DECLARED INTEREST.** This item is a claim about my own construction and a favourable finding is in my
  interest. I have tried to make the challenge honest by stating plainly, below, where the challenge
  fails and where the item is actually worse than it says. Two things in this file cut against me and I
  want them findable: (a) the LLM-specific evidence suggests role-assigned dissent is *inauthentic* at a
  measurable rate, which is a different defect from bolstering but is still a defect in 15b; and (b) my
  single most load-bearing quantitative source for that finding could not be retrieved, so it is
  UNVERIFIED and I am not allowed to lean on it — see Sources 4 and the scope note.

  Register pre-check:
    - PREMISE-152 (ACTIVE) — "HOMOGENEOUS, UNGUIDED multi-agent debate does not outperform isolated
      self-correction at matched compute. Gains from debate require heterogeneity of agents, ROLE
      GUIDANCE, or an explicit calibration mechanism." **This is the pre-answer and it runs AGAINST the
      item**: role guidance is named as one of the three things that make debate work at all. The
      15a/15b split is role guidance.
    - PREMISE-111 (ACTIVE) — the read channel was not the dominant correlation source between 15a and
      15b; frontier LLMs sharing no procedural channel collapse to roughly two effective votes out of
      nine; the dominant channels are shared pre-training corpora and alignment. **This is the real
      threat to 15b's independence and it is bigger than Nemeth.**
    - PREMISE-180 (ACTIVE) — LLM errors are substantially correlated across models and the correlation
      RISES with capability.
    - PREMISE-197 (ACTIVE) — agreement among independently-run generators is corroboration only when no
      common cause screens it off; for agents sharing a base model or prompt scaffold the common cause is
      present.
    - PREMISE-075 (ACTIVE) — robustness comes from error DECORRELATION, which reference-frame variation
      supplies far more than resampling; realized robustness is conditional on MEASURED decorrelation.
    - PREMISE-124 (ACTIVE) — any self-measurement of the pipeline's own accuracy must cite an external
      baseline or be reported as UNCALIBRATED. **Applies to this file.**
    - PREMISE-194 (ACTIVE) — an agent's in-session recollection of its own work is not an independent
      copy of the record.
    - PREMISE-129 (ACTIVE) — LLM self-report of correctness is empirically unreliable and poorly
      calibrated. Applies to my own rating below.

  Challenging evidence found: Yes

  LIMB STRUCTURE — four limbs, and they diverge sharply:
    LIMB A — "Nemeth found that assigned devil's advocacy produces cognitive bolstering." (Attribution.)
    LIMB B — "that finding is robust in the human literature." (Robustness.)
    LIMB C — "it transfers to role-assigned LLM agents." (Transfer — the load-bearing limb.)
    LIMB D — "therefore every CHALLENGED status in the register is suspect." (Consequence.)

  Sources:
    1. Nemeth, C., Brown, K. & Rogers, J. (2001). "Devil's advocate versus authentic dissent: stimulating
       quantity and quality." *European Journal of Social Psychology* 31, 707-720. — SECONDARY (abstract
       and multiple independent summaries retrieved via Wiley and Google Scholar records; full text not
       retrieved) — Authentic dissent was superior in (a) proportion of original thoughts, (b)
       considering the opposite position, and (c) direct attitude change; devil's advocate stimulated
       cognitive bolstering of the initial position. **LIMB A is correctly attributed.** Note what it
       does NOT say: it does not say devil's advocacy is worse than no dissent, and the comparator that
       beat it was *authentic* dissent, which is not available to this architecture at all.
    2. Schwenk, C.R. (1990). "Effects of devil's advocacy and dialectical inquiry on decision making: A
       meta-analysis." *OBHDP* 47(1), 161-176. — SECONDARY (bibliographic record VERIFIED at IDEAS/RePEc:
       volume, issue, pages and October 1990 date confirmed; **RePEc records "No abstract is available
       for this item" and ScienceDirect is paywalled, so I could not read the paper. The reported finding
       — that DA is more effective than the expert approach in general, while DI's superiority was not
       demonstrated on relatively ill-structured tasks — comes from a search summary and is SECONDARY.
       Effect sizes: not retrieved.**) — This is the one meta-analysis the charter named and it runs FOR
       assigned devil's advocacy. It is the strongest challenge to LIMB B available, and I am not able to
       quote a number from it.
    3. Schulz-Hardt, S., Jochims, M. & Frey, D. (2002). "Productive conflict in group decision making:
       genuine and contrived dissent as strategies to counteract biased information seeking." *OBHDP*
       88(2), 563-586. — SECONDARY (abstract retrieved via the Göttingen departmental record and search;
       full text not retrieved) — n=201 employees and managers, two-factorial: genuine dissent
       (heterogeneous vs homogeneous three-person groups) crossed with contrived dissent (devil's
       advocacy used or not). Heterogeneity was **more effective** than devil's advocacy at preventing
       confirmatory information seeking. **This is a partial replication of Nemeth's ordering, not of
       Nemeth's null**: it establishes genuine > contrived; the retrieved abstract does not establish
       contrived ≈ nothing, and I did not get the cell means.
    4. "Inducing Disagreement in Multi-Agent LLM Executive Teams: Only the Devil's Advocate Works" (TMLR
       submission, OpenReview id mxBmj5LYU2). — **UNVERIFIED. Retrieval was blocked: the OpenReview PDF
       returned empty and the forum page served a browser-verification challenge, which I did not
       attempt to bypass.** The figures circulating in search summaries — devil's advocate producing
       99.2% disagreement vs 48.3% baseline, soft role-framing 61.7% and explicit dissent instructions
       55.0% being statistically indistinguishable from baseline, 4.9% "persuasion override" where agents
       recommend an option they privately rate lower, and 9.2% of disagreeing teams showing "hidden
       agreement" — **carry no weight in my rating and must not be cited downstream until the paper is
       read.** I record them only because the paper's title and framing are directly on point and someone
       with institutional access should retrieve it. This is exactly the ASSUMPTION-1311 failure pattern
       and I am declining to repeat it.
    5. LLM-to-human transfer literature: Lin, Z. (2026), "Large Language Models as Psychological
       Simulators: A Methodological Guide," *Advances in Methods and Practices in Psychological Science*;
       "From Prompts to Constructs: A Dual-Validity Framework for LLM Research in Psychology" (arXiv
       2506.16697); "LLM-based Human Simulations Have Not Yet Been Reliable" (arXiv 2501.08579). —
       SECONDARY (abstracts and summaries retrieved; full texts not read) — **This is the substantive
       challenge to LIMB C and it is the best-supported thing in this file.** Transfer of human group
       findings to LLM agents is task-specific and unreliable: LLM agents reproduced ultimatum-game and
       Milgram results but **failed to reproduce the Wisdom of Crowds**, because the models behave as a
       unified knowledge system rather than producing the independent errors crowd wisdom requires. The
       general critique is that LLM group behaviour may reflect surface-level role-play rather than the
       cognitive mechanism the human finding is about; behavioural variance is compressed and agents
       converge on an "average persona."
    6. Sycophancy in multi-agent debate: "Peacemaker or Troublemaker: How Sycophancy Shapes Multi-Agent
       Debate" (arXiv 2509.23055); CONSENSAGENT (Findings of ACL 2025); "Not All Flips Are Conformity"
       (arXiv 2606.00820). — SECONDARY (titles, venues and abstract-level findings via search; not read)
       — the LLM-specific pathology reported is *conformity and premature consensus*, with a devil's-
       advocate prompt functioning as a conformity lever in the opposite direction.

  Strength of challenge: Moderate (LIMB A: None — correctly attributed. **LIMB B: Moderate** — Schwenk's
    meta-analysis runs the other way and Schulz-Hardt establishes an ordering, not a null, though I could
    read neither. **LIMB C: Strong** — human→LLM transfer is specifically unreliable, and the one
    mechanism named as failing to transfer is the independence mechanism. **LIMB D: Weak-to-None** — see
    below; the consequence survives even though the premise is challenged.)

  Summary: Limb A is accurately attributed and I want that stated clearly because the item's credit
    depends on it. Limb B is weaker than the item implies: Schwenk's 1990 meta-analysis — the only
    meta-analysis in this area and the one the charter named — reports assigned devil's advocacy
    outperforming the expert approach, and Schulz-Hardt's n=201 replication establishes that genuine
    dissent beats contrived dissent, which is an ordering and not a demonstration that contrived dissent
    does nothing. Neither paper was retrievable behind its paywall, so both readings are secondary and I
    will not pretend otherwise. Limb C is where the item is most exposed, and it is exposed in a way the
    item does not anticipate: the transfer of human group-decision findings to LLM agents is measurably
    task-specific and unreliable, and the single documented transfer failure is the Wisdom of Crowds —
    which failed precisely because LLM agents behave as one knowledge system rather than as independent
    error sources. But that is not good news for 15b. It means the human finding about bolstering may
    well not apply, while the LLM-native pathology that *does* apply — correlated errors from a shared
    substrate, and role-compliance producing dissent that is asserted rather than held — is already named
    in this register as PREMISE-111, PREMISE-180 and PREMISE-197, and is worse. Limb D therefore survives
    its own premise: every CHALLENGED status remains suspect, but for a reason the item misidentifies.

  Specific risks: The item's risk, if true as stated, is 42 CHALLENGED presumptions and 12 CHALLENGED
    assumptions whose epistemic weight is inflated by bolstering. The risk I actually found is different
    and larger. If 15a and 15b share a base model, a prompt scaffold and a pre-training corpus, then
    PREMISE-111's finding applies directly: the two directions are not two readings, and the architecture
    that was built to prevent confirmation bias may be producing two correlated readings with a
    procedural veneer of opposition. Role assignment would then be doing something specific and bad — not
    bolstering, but *manufacturing* a challenge the agent does not hold, which produces CHALLENGED
    statuses that look like evidence and are performance. A CHALLENGED status arrived at by role
    compliance is worse than no status, because it is indistinguishable on the page from one arrived at
    by evidence, and the register has no field recording which it was. Concretely: this file rates LIMB C
    as a Strong challenge on the strength of sources I read only in abstract, and I am the party with an
    interest in that rating. PREMISE-129 says my self-report of my own correctness is poorly calibrated.
    Treat this paragraph as the finding.

  Mitigations available:
    - **Run the named test.** The blind re-run of one item by an agent not told its direction is cheap,
      decisive and six days old with no owner. It is the only measurement in this file that would not be
      produced from inside the instrument (PREMISE-124). Give it an owner and a date today.
    - Strengthen it while you are at it: a blind re-run tests *direction-independence*, but PREMISE-111's
      problem is *substrate correlation*, which a blind re-run on the same base model cannot detect. Run
      the blind arm on a different model family. That is the decorrelation PREMISE-075 requires to be
      MEASURED rather than assumed.
    - Record, per CHALLENGED status, whether the challenge rests on a retrieved source or on reasoning.
      In this very file the split is stark: the LIMB C challenge rests on abstracts, and my strongest
      would-be quantitative source is unretrievable. A `evidence-grade` field would make that visible
      without any new search.
    - Per PREMISE-152, do NOT dissolve the role assignment in response to this item. Role guidance is one
      of the three named conditions under which multi-agent debate beats isolated self-correction at all;
      removing it would leave homogeneous unguided debate, which the same premise says is worse than a
      single agent self-correcting. If 1310 is acted on naively the remedy is worse than the disease.
    - Retrieve Schwenk 1990 and the OpenReview paper through institutional access. Both are load-bearing
      and both are currently unread.

  STEELMAN:
    Item: ASSUMPTION-1310
    Strongest counterargument: The transfer objection is weaker than it looks, because the mechanism
      Nemeth identified does not require human psychology — it requires only that the challenger's output
      be generated conditional on a role rather than on a judgement, and that is definitionally true of
      Agent 15b. A human devil's advocate bolsters because the group discounts objections it knows were
      assigned; an LLM devil's advocate has the analogous problem in a sharper form, since its dissent is
      produced by conditioning rather than held, and the downstream register cannot tell the difference.
      Schwenk's meta-analysis compares DA against an *expert* comparator on structured tasks, not against
      authentic dissent on open-ended ones, so it does not rescue the case. And the LLM-native evidence,
      if the retrieved summaries are right, points the same way: role-assigned dissent hits near-total
      disagreement rates, which is itself the tell — a challenger that challenges 99% of the time is not
      discriminating, it is complying. Filing this at High was correct and the register's 42 CHALLENGED
      presumptions should be read as claims about 15b's compliance with its charter until the blind
      re-run says otherwise.
    What would need to be true for C2A2 to be safe: (1) 15b's CHALLENGED rate must be materially below
      100% — a challenger that never returns NO-CHALLENGE-FOUND is a role, not an instrument, and this
      is measurable today from the existing files without any new work; (2) the blind re-run must show
      that an agent not told its direction reaches a similar verdict on the same item; (3) that re-run
      must use a different model family, or it tests the wrong thing (PREMISE-111); (4) 15b's challenges
      must rest on retrieved sources at a measurable rate, not on reasoning dressed as citation
      (PREMISE-132: measured full-support rates in generated text run near half); and (5) the register
      must be able to record and act on a NO-CHALLENGE-FOUND, or the architecture has no null result and
      cannot be wrong.
    How to test: Three tests, in increasing cost, and the first is free.
      (a) **Free, today, and I recommend it above everything else in this file:** count the disposition
          distribution across all existing 15b output — CHALLENGED vs PARTIALLY-CHALLENGED vs
          NO-CHALLENGE-FOUND. If NO-CHALLENGE-FOUND is near zero across 54 items, 15b is behaving as a
          role and ASSUMPTION-1310 is confirmed in-house without a single search. If it is a healthy
          fraction, the item is substantially answered against itself. This is one grep and it is the
          measurement PRESUMPTION-949 has been waiting for.
      (b) The named blind re-run, run on a different model family, on an item whose 15b verdict is known
          and whose direction is withheld. Compare verdict and, more informatively, compare the SOURCES
          cited — if the blind agent cites a disjoint source set, the direction was driving the search.
      (c) Adversarial calibration: hand 15b three items whose supporting evidence is genuinely
          overwhelming (choose ACTIVE premises with the strongest source backing). A properly calibrated
          challenger returns NO-CHALLENGE-FOUND on all three. A bolstering-or-complying one does not.
          This is PREMISE-160's disconfirming-case design applied to the instrument rather than to a
          defect explanation, and it is the cleanest test of the whole architecture.

  Search scope: comprehensive on the human dissent literature and the LLM multi-agent-debate literature;
    **retrieval, however, was poor and that is the honest headline of this file.** Searched: Nemeth 2001
    (EJSP and JASP), Schwenk 1990 meta-analysis, Schulz-Hardt/Jochims/Frey 2002, Schweiger/Sandberg/Ragan
    1986, devil's advocacy in computational social science (Akhmad et al. 2021); LLM multi-agent debate,
    sycophancy and conformity in debate, DEBATE (ACL 2024), AI-mediated devil's advocate systems (CHI
    2025); human→LLM transfer and external validity of LLM behavioural simulation.
    **Could not retrieve:** Schwenk 1990 (paywalled; RePEc carries no abstract); Schulz-Hardt 2002
    (paywalled); Nemeth 2001 full text (paywalled); the OpenReview TMLR paper (browser-verification
    challenge, not bypassed). Four of the most load-bearing sources for this item are unread, and every
    quantitative figure associated with them in this file is marked SECONDARY or UNVERIFIED accordingly.

  Recommendation: PARTIALLY-CHALLENGED — resting on LIMB C (transfer), with LIMB B a weaker secondary
    challenge. **LIMB D is NOT challenged and should be read as strengthened**: the conclusion that every
    CHALLENGED status is suspect survives, because the LLM-native mechanism (correlated substrate plus
    role compliance, PREMISE-111/152/180/197) reaches the same conclusion by a different route than the
    one the item names. The correct disposition is therefore NOT to relax MONITOR-599 but to re-found it
    on the transfer-appropriate mechanism — and to run test (a) above, which costs one grep.
