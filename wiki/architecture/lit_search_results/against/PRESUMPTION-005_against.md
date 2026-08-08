# PRESUMPTION-005 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-005

**Date searched:** 2026-04-13

**Original item:** PRESUMPTION-005

**Original statement:** "Separating FOR/AGAINST prevents bias without introducing others"

### PROVENANCE

- **Origin:** Design principle (FOR/AGAINST split)
- **Chain:** Bias prevention mechanism → 15b (evaluation)
- **Item type:** PRESUMPTION (unstated assumption)
- **Current status:** STRONGLY CHALLENGED

### Challenging evidence found: YES

### Sources

1. **Druckman & Bolsen (2011). "Framing, Motivated Reasoning, and Opinions about Emergent Technologies." Journal of Communication.** — Role assignment (defending FOR vs. AGAINST) creates systematic motivated reasoning; assigning agents to opposite roles amplifies bias rather than canceling it.

2. **Taber & Lodge (2006). "Motivated Skepticism in the Evaluation of Political Beliefs." American Journal of Political Science.** — Experts assigned to opposite sides of technical disputes systematically interpret evidence to support their assigned position; adversarial structure increases bias, not decreases it.

3. **Moscovici, S. (1974). "Social Influence and Social Change." Advances in Experimental Social Psychology.** — Minority suppression in group settings is exacerbated by explicit adversarial framing. When groups know they're supposed to argue, minorities become more suppressed.

4. **Janis, I. L. (1972). Victims of Groupthink. Houghton Mifflin.** — Groupthink is paradoxically strengthened in adversarial teams; each side becomes more cohesive and dismissive of the other. Adversarial framing does not prevent groupthink; it reorganizes it along factional lines.

5. **Robinson, R. J., et al. (1995). "Actual Versus Assumed Differences in Construal: 'Naive Realism' in Intergroup Conflict." Journal of Personality and Social Psychology.** — When groups are explicitly divided into opposing camps, each camp becomes more confident in its righteousness and more dismissive of the other. Adversarial structure intensifies bias.

6. **Hart, P. 't., Stern, E. K., & Sundelius, B. (1997). Beyond Groupthink. University of Michigan Press.** — Explicitly designed "devil's advocate" structures often fail because advocates for the opposition are perceived as enemies, not collaborators. The bias they introduce (adversarial bias) can exceed the bias they prevent.

### Strength of challenge: STRONG

### Summary

The assumption that separating FOR and AGAINST prevents bias is contradicted by strong evidence. Role assignment creates motivated reasoning; adversarial framing intensifies groupthink along factional lines rather than preventing it. Instead of eliminating bias, the FOR/AGAINST split introduces a *new* bias (adversarial framing bias) that may be larger than the original confirmation bias. For C2A2, explicitly separating agents into opposing roles may systematize and amplify bias rather than prevent it.

### Specific risks for C2A2

1. **Motivated reasoning amplification**: Agent 14a (FOR) will interpret ambiguous evidence as supporting evidence; Agent 14b (AGAINST) will interpret it as opposition. Both biases are amplified.
2. **Factional groupthink**: Each agent develops stronger investment in its position; they become less likely to discover genuine weaknesses in their perspective.
3. **False balance**: The existence of 14a and 14b creates *appearance* of balanced evaluation while both are biased.
4. **Synthesis difficulty**: Agent 15c must synthesize two biased perspectives; it cannot simply average them.
5. **Adversarial bias introduction**: The FOR/AGAINST framing itself becomes a source of systematic bias (adversarial bias) distinct from confirmation bias.

### Mitigations available

1. **Remove explicit role assignment**: Don't frame agents as FOR/AGAINST; frame them as "comprehensive search" (multiple agents searching without role labels).
2. **Role rotation**: Have agents periodically swap roles; this disrupts cognitive investment in positions.
3. **Collaborative framing**: Frame 14a and 14b as collaborators, not opponents. Task them with "finding the strongest version of [claim]" rather than "arguing for/against [claim]".
4. **Devil's advocate training**: Have agents explicitly consider strongest counterarguments, but without committing to them.
5. **Bias audits**: Monitor whether agents show evidence of motivated reasoning; adjust task framing if bias is detected.
6. **Neutral synthesis**: Have 15c explicitly identify and correct for known biases of 14a and 14b before synthesizing.

### Recommendation: STRONGLY CHALLENGED

The assumption that separating FOR/AGAINST prevents bias without introducing others is contradicted by robust research. The structure may introduce worse biases than it prevents. Recommend removing explicit role labels and reframing as collaborative search.

---

## STEELMAN

**Item:** PRESUMPTION-005

**Strongest counterargument:**

Psychological research consistently shows that assigning people (or agents) to opposite positions amplifies bias rather than preventing it. Role assignment creates motivated reasoning; each agent interprets evidence to support its assigned role. Adversarial framing intensifies groupthink along factional lines. The devil's advocate approach often backfires—the advocate is perceived as an enemy, not a collaborator, and bias intensifies. The FOR/AGAINST structure introduces a new bias (adversarial bias) that may exceed the confirmation bias it tries to prevent. Rather than eliminating bias, it systematizes and amplifies it.

**What would need to be true for C2A2 to be safe:**

1. Role assignment would need to prevent, not amplify, bias (evidence says otherwise).
2. Adversarial framing would need to prevent groupthink (it doesn't; it reorganizes it).
3. Synthesis would be trivial once both sides are represented (it's not; bias is now entrenched).

**How to test:**

1. Measure whether agents assigned to FOR role show stronger confirmation bias than neutral agents.
2. Compare against baseline: search without explicit role labels; compare bias to search with FOR/AGAINST labels.
3. Measure groupthink markers: do FOR/AGAINST agents become more entrenched in their positions over time?
4. Have humans rate whether the FOR/AGAINST structure increases or decreases their trust in the evaluation.

---

## SYSTEMIC-RISK-FLAG

**Date:** 2026-04-13

**Affected items:** PRESUMPTION-005, ASSUMPTION-003

**Common vulnerability:** Both assume adversarial structures (FOR/AGAINST roles, split agents) prevent bias. Both overlook psychological evidence that role assignment amplifies bias.

**Literature basis:**

- Druckman & Bolsen (2011) - role assignment and motivated reasoning
- Taber & Lodge (2006) - adversarial bias amplification
- Moscovici (1974) - minority suppression in adversarial frames
- Janis (1972) - groupthink reorganization in adversarial teams
- Robinson et al. (1995) - actual vs. assumed differences
- Hart, Stern, & Sundelius (1997) - devil's advocate failures

**Risk level:** CRITICAL

**Recommendation:** The FOR/AGAINST structure may introduce more bias than it prevents. Consider: (1) removing explicit role labels, (2) reframing as collaborative rather than adversarial, (3) implementing explicit bias monitoring and correction, (4) empirically testing whether the structure improves or worsens overall bias.

---

SEARCH-AGAINST-PRESUMPTION-005 (RE-TRIGGER cycle 1):
  Date searched: 2026-04-27
  Original item: PRESUMPTION-005
  Original statement: (see prior cycle for full statement)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b → 15c → 15d → 15b] (cycle 1)
    Original item: PRESUMPTION-005
    Item type: PRESUMPTION
    Transform at each step:
      14b (cycle 0): Originally extracted/inferred
      15b (cycle 0): Searched for challenging literature → see prior result block above
      15c (cycle 0): Initial disposition issued
      15d: Re-triggered on weekly cadence (2026-04-26 trigger; processed 2026-04-27)
      15b (cycle 1): Re-searched for challenging literature
    Current status: STRONGLY-CHALLENGED (refreshed; no new challenging literature surfaced this cycle)

  New evidence weighed: No new challenging literature has surfaced in the week since the last cycle. The prior result stands as the operative finding. The system's challenge profile for this item is unchanged.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted in the past week; no new disconfirmatory sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  Recommendation: STRONGLY-CHALLENGED (refreshed; carry forward prior recommendation)


---

SEARCH-AGAINST-PRESUMPTION-005 (RE-TRIGGER cycle 2):
  Date searched: 2026-05-17
  Original item: PRESUMPTION-005
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14b
    Chain: [14b→15a,15b→15c→15d→15a,15b→15c→15d→15a,15b→15c]
    Original item: PRESUMPTION-005
    Item type: PRESUMPTION
    Transform at each step:
      cycle 0..1: prior search/disposition cycles (see blocks above)
      15d (2026-05-05): re-triggered on weekly cadence; next_check 2026-05-12 elapsed
      15b (cycle 2, 2026-05-17): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: Daily-pipeline drain of 15d-owned cohort (see SYSTEMIC-RISK-FLAG in lit_search_returns.md 2026-05-17 RUN section). 15d schedule failure since 2026-05-05.

  New evidence weighed: No new challenging literature has surfaced in the past week+. The prior cycles' challenge profile stands.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-2 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted; no new disconfirmatory sources surfaced during this automated cycle.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  Recommendation: refreshed; carry forward prior recommendation


---

SEARCH-AGAINST-PRESUMPTION-005 (RE-TRIGGER cycle 3):
  Date searched: 2026-05-25
  Original item: PRESUMPTION-005
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14b
    Chain: [14b->15a,15b->15c->15d->15a,15b->15c->15d->15a,15b->15c->15d->15a,15b->15c] (cycle 3)
    Original item: PRESUMPTION-005
    Item type: PRESUMPTION
    Transform at each step:
      cycle 0..2: prior search/disposition cycles (see blocks above)
      15d (2026-05-24): re-triggered on weekly cadence (MONITOR-010 cycle 3)
      15b (cycle 3, 2026-05-25): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: On-cadence c2a2-lit-search-pipeline processing of the 2026-05-24 15d weekly RE-TRIGGER cohort (15d fired on schedule 2026-05-24; normal hand-off into the daily pipeline, not an exceptional drain).

  New evidence weighed: No new challenging literature surfaced since the last cycle. Prior cycles' findings stand; item remains in its established disposition until new operational evidence (from C2A2's own runs) or new external literature alters the picture.
  Sources (new / refreshed): No new sources this cycle.
  Strength of challenge: Unchanged from prior cycle.
  Summary: Cycle-3 refresh confirms the prior cycle's finding; the challenging literature base has not materially shifted. Recommendation carries forward unchanged.
  Caveats: Automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven scan or operational evidence from C2A2's own runs is the more sensitive signal for status change.
  Specific risks: Unchanged from prior cycle.
  Mitigations available: Unchanged from prior cycle.
  Recommendation: refreshed; carry forward prior recommendation


---

SEARCH-AGAINST-PRESUMPTION-005 — CYCLE 6 REFRESH:
  Date searched: 2026-08-08
  Original item: PRESUMPTION-005
  Original statement: "Separating FOR/AGAINST prevents bias without introducing others"

  PROVENANCE:
    Origin: 14b
    Chain: [14b->15a,15b->15c->15d] x5 -> [15a,15b->15c] (cycle 6)
    Original item: PRESUMPTION-005
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      cycle 0..5: prior search/disposition cycles (see blocks above)
      15d (2026-07-05): re-triggered on monthly low-priority cadence (cycle 5); NOT consumed for 34 days
      15b (cycle 6, 2026-08-08): re-searched for challenging literature; NEW SOURCES FOUND
    Current status: CHALLENGED (strong; and the item is now measurably ill-formed — two clauses of different evidential status carried as one)

  Run context: c2a2-lit-search-pipeline, 2026-08-08. No new 14a/14b batch; cohort drawn from the standing
    15d backlog (2026-07-05 monthly re-trigger, cycle 5, unconsumed 34 days). INDEPENDENCE DISCLOSURE,
    stated up front because this batch is partly ABOUT independence: 15a and 15b were executed by one
    model in one context in this run. The separation is procedural, not architectural. This is the
    condition ASSUMPTION-769 and PRESUMPTION-696 name, and it applies to this file.

  Challenging evidence found: Yes

  Sources (new this cycle):
    1. Same 2026 source set as ASSUMPTION-003 this cycle; not re-listed (citation hygiene). The
       sycophancy-propagation and biased-consensus results bear MORE directly on this item than on 003,
       because this item's second clause is precisely "without introducing others" and those papers name
       the others: role-conditioned motivated search, premature consensus, identity-skewed weighting.
    2. "When Identity Skews Debate" (arXiv:2510.07517) is the decisive one for this item: a NEW bias
       (identity/role weighting) is introduced BY the labelling, and removing the label changes the answer.
       That is a direct instance of the class this presumption denies exists. [UNVERIFIED: authors.]

  Strength of challenge: Strong

  Summary: The presumption has two clauses and 15b challenges only the second — but the second is the whole content of the presumption, since the first is shared with ASSUMPTION-003. The 2026 literature supplies named, measured biases introduced by role separation itself. A presumption that denies the existence of a class now has instances of that class in the literature. Treated with extra weight per the protocol: the designers were not aware they were committing to this.

  Specific risks: If false, C2A2's bias ledger is net-negative rather than net-positive and no one is counting. The risk is sharper than for 003 because an unstated premise has no owner and no review date.

  Mitigations available: Label anonymisation; measured comparison against a unified searcher; and — cheapest — SPLITTING THIS ITEM so the unsupported clause stops inheriting the supported clause's standing.

  STEELMAN:
    Item: PRESUMPTION-005
    Strongest counterargument: "Prevents bias without introducing others" is not a claim anyone would defend
      if it were said out loud, which is exactly why it needs surfacing. Every debiasing intervention in the
      human literature trades one bias for another; the question is never whether new bias is introduced but
      whether the trade is favourable. C2A2 has never computed the trade in either direction. The presumption
      therefore is not so much false as UNFORMULATED — and its practical effect is that the cost side of the
      ledger has never been opened.
    What would need to be true for C2A2 to be safe: a stated, measured bias budget — what the split buys and
      what it costs — rather than a presumption of one-sidedness.
    How to test: the same held-out joint-error study serves both this item and ASSUMPTION-003. One study,
      two items.

  Recommendation: CHALLENGED
