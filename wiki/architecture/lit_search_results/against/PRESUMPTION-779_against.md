# PRESUMPTION-779 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-779

**Date searched:** 2026-08-13

**Original item:** PRESUMPTION-779

**Original statement:** That a hold, once placed, stays correct — six queues 100% held for up to eleven consecutive runs with no re-audit and no expiry.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred from six queues held at 100% across up to eleven runs, with no re-audit mechanism and no expiry policy, that the system presumes a deferral decision remains valid indefinitely; risk graded High.
  - 15b: Searched for literature challenging the inference — expiry and auto-close policies in issue triage, the validity of prolonged protocolised deferral in clinical practice, and the costs of forced reassessment.
- **Current status:** PARTIALLY-CHALLENGED

**Polarity note (explicit inversion).** The AGAINST direction here is that 14b's worry is boundary-limited and its implied remedy — expiry or scheduled re-audit — is the specific intervention with the best-documented failure record in the nearest analogous domain.

### Challenging evidence found: Yes

### Sources

1. **"Should I Stale or Should I Close? An Analysis of a Bot That Closes Abandoned Issues and Pull Requests," BotSE workshop, 2019. [author list not confirmed in search snippets].** — Empirical analysis of the canonical implementation of exactly the remedy this item implies. The finding practitioners took from it, and the subsequent community reaction, is that automatic expiry of deferred items produces churn rather than resolution.
2. **Zimmermann, T., 2021. "Managing known issues: a refinement of the stale bot approach." [personal blog — non-peer-reviewed].** — Documents the concrete failure mode: auto-closure causes maintainers to redo triage and investigation work done six months to a year earlier, causes reporters' effort to be wasted, and causes the same problem to be re-reported repeatedly against a closed "stale" record. The cost of expiry is re-derivation of the very judgement the hold recorded.
3. **Verschelde, F., "Don't use stale bots." / community position statements (No Stale Bots). [blogs / advocacy sites — non-peer-reviewed, cited as evidence that the practice is contested, not as evidence of effect size].** — Staleness notifications "create artificial additional activity" for subscribers; the reported net effect is noise plus loss of triage state.
4. **"When less is more: Updates in active surveillance and watchful waiting in the management of prostate cancer," 2024 (PubMed 38697055); and "Watchful waiting versus active surveillance: appropriate patient selection" (PubMed 18765115).** — Prolonged deferral, correctly scoped, achieves outcomes comparable to immediate intervention while avoiding the harms of acting: 45–70% of appropriately selected patients avoid local therapy with comparable survival. This is the strongest general counterexample to "a hold decays": in a domain where the stakes are maximal and the observation period is measured in years, a hold that is *correctly scoped at placement* is expected to remain correct, and the literature's emphasis is on selection criteria at entry, not on expiry.
5. **Ancker, J.S. et al., 2017. "Effects of workload, work complexity, and repeated alerts on alert fatigue in a clinical decision support system." *BMC Medical Informatics and Decision Making* 17:36. [author attribution from search snippet; article and venue verified].** — Reminder acceptance dropped roughly 30% for each additional reminder per encounter and 10% for each five-percentage-point increase in the proportion of *repeated* reminders. A mandatory periodic re-audit of held queues is, structurally, a repeated reminder; the literature predicts its acceptance rate will fall with exactly the frequency that makes it useful.

### Strength of challenge: Moderate

### Summary

Two things are true and only one of them is the presumption. It is true that no mechanism exists to revisit a hold, and that is a real gap. It is not established that a hold decays with elapsed time, and the analogous literatures point the other way. In clinical deferral — the closest well-studied case of a judgement deliberately held open — validity is governed by entry criteria and by *trigger-based* reassessment (a defined progression signal), not by a clock; deferral sustained over years is a validated strategy, not a decaying one. In the closest software case, issue triage, the specific remedy this item implies has been implemented at scale as the stale bot, and the documented result is destroyed triage state, duplicated reports and re-litigation of judgements already made. And a scheduled re-audit across six queues is a repeated interruptive prompt, a class of control whose acceptance rate is empirically known to collapse under repetition. The presumption's evidential base is also weaker than it looks: a 100% hold rate over eleven runs is evidence of decay only if the underlying conditions that justified the holds were likely to have changed in that window, and nothing in the item establishes that base rate.

### Specific risks

If the presumption is adopted with a time-based expiry, the predicted failures are concrete: holds released not because conditions changed but because a counter incremented; loss of the reasoning that placed the hold; the same items re-triaged repeatedly at full cost; and re-audit prompts that are dismissed unread by the third cycle, at which point the system has an audit mechanism that certifies without examining — a fail-open control of exactly the kind PREMISE-110 describes. If the presumption is dismissed, the real hazard remains: a hold placed on a condition that has since resolved silently, held forever because nothing is watching the condition.

### Mitigations available

(a) Attach a *release trigger* to each hold at the moment of placement — the specific observable whose change would make the hold wrong — rather than an expiry date. This is the active-surveillance pattern and it converts an unbounded deferral into a monitored one at near-zero recurring cost. (b) Re-audit on trigger, not on schedule, so the prompt rate stays low enough to survive. (c) If a periodic sweep is wanted anyway, make it a sampling sweep (audit a small random subset per run) rather than a full re-audit, which preserves signal while keeping the prompt rate under the fatigue threshold. (d) Record hold *age* and hold *reason* so that a hold whose stated reason has become unreadable can be surfaced without a blanket policy.

### Recommendation: PARTIALLY-CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-779

**Strongest counterargument:** The presumption smuggles in a decay model it never states. Holds do not rot on a clock; they become wrong when the condition that justified them changes, and elapsed time is only a proxy for that, and a poor one. The best-studied deliberate-deferral practice in any field — active surveillance — is built precisely on this distinction: entry criteria plus a defined progression trigger, with deferral sustained for years and outcomes comparable to immediate intervention. Meanwhile the remedy the item implies has been run as a natural experiment across the whole of open-source issue triage, and the stale bot is now widely regarded as a mistake: it destroys accumulated triage state, forces re-derivation of judgements already made, and converts a quiet backlog into a noisy one. Layer on the alert-fatigue evidence — acceptance of repeated prompts falls sharply with repetition — and a scheduled re-audit of six queues is predicted to become a rubber stamp within a few cycles, which is worse than no audit because it manufactures a false record of having looked. The honest version of the finding is not "holds decay" but "holds were placed without release conditions," and that is a defect at placement time, not a defect of duration.

**What would need to be true for C2A2 to be safe:** Every hold must record, at placement, the observable whose change would invalidate it, and that observable must be cheap to check. Given that, elapsed time carries no independent information and no expiry policy is needed. Absent that — if holds are placed with no stated condition — the presumption's worry is live, because there is then nothing to monitor and time is the only available proxy.

**How to test:** Sample the six held queues and, for each hold, attempt to reconstruct the condition that justified it. Two measurements settle the matter: the fraction of holds for which a release condition can be stated at all, and, among those, the fraction whose condition has already changed. If most holds have statable conditions and few conditions have changed, the presumption is overstated and the fix is annotation. If most holds have no statable condition, the presumption is right for a reason it did not give, and the fix is at placement rather than expiry.

---

## Search scope

Moderate. Query families executed: stale-bot and auto-close policies in issue triage and their criticism; watchful waiting and active surveillance as protocolised deferral; alert and reminder fatigue under repetition. Not searched: the WIP-ageing and queue-ageing literature in lean/kanban practice named in the item's search strategy, the bug-reopening literature (e.g. work on why closed bugs are reopened), and any formal treatment of decision half-life. Note that three of the five sources here are non-peer-reviewed practitioner sources, cited for the failure mode they document rather than for effect sizes. Broader search recommended.
