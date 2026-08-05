SEARCH-AGAINST-PRESUMPTION-673:
  Date searched: 2026-08-05
  Original item: PRESUMPTION-673
  Original statement: "That a workaround's cost is paid once; two independent agents disclosed the same day that they rebuild the same workarounds from scratch every run, both naming the durable fix, neither authorised to make it."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-673
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from two same-day disclosures of rebuilt workarounds, one carrying its own recurrence count
      15b: Searched for challenging literature on workaround recurrence, rediscovery cost, and why workarounds do not convert into fixes
    Current status: CHALLENGED
    Search scope: Comprehensive on the operations-management and software-maintenance literatures; preliminary on the LLM-agent-specific literature (thin as of 2026-08).

  Challenging evidence found: Yes — strong and convergent across three independent literatures

  Sources:
    1. Tucker, A. L., & Edmondson, A. C. (2003). "Why Hospitals Don't Learn from Failures: Organizational and Psychological Dynamics That Inhibit System Change." *California Management Review*, 45(2), 55–72. — Direct refutation. In observed nursing work, **93% of responses to system failures were first-order problem solving**: the immediate obstacle was cleared and the underlying cause was left untouched. The workaround cost was paid *every single time*, not once. This is the single strongest empirical result against PRESUMPTION-673.
    2. Tucker, A. L., Edmondson, A. C., & Spear, S. (2002). "When Problem Solving Prevents Organizational Learning." *Journal of Organizational Change Management*, 15(2), 122–137. — Names the mechanism: successful workaround *removes the signal* that would have triggered the durable fix. The better an agent is at working around, the less likely the fix is ever made. C2A2's agents are, by construction, very good at working around.
    3. Tucker, A. L., & Edmondson, A. C. (2002). "Managing Routine Exceptions: A Model of Nurse Problem-Solving Behavior." *Advances in Health Care Management*, 3, 87–113. — Quantifies the recurring tax: roughly one system failure per hour, ~15% of working time (≈1.2 h per 8-h shift) consumed by coping. The cost is a *rate*, not a one-off.
    4. SNAFUcatchers / Woods, D. D. (ed.), with Allspaw, J., Cook, R. I., et al. (2017). *STELLA: Report from the SNAFUcatchers Workshop on Coping With Complexity*. Columbus, OH. — Introduces **dark debt**: debt that lives in the *interactions* between components, is not recognisable at the time of creation, and cannot be found by inspecting the parts. Repeatedly-rebuilt workarounds are the canonical accumulation site. Directly contradicts "cost paid once" — dark debt's cost is unbounded and unmeasured until it manifests.
    5. Alter, S. (2014). "Theory of Workarounds." *Communications of the Association for Information Systems*, 34, Article 55. — Integrated framework covering how and why workarounds are created and, critically, why they **persist as standing features of operational systems** rather than resolving into design changes.
    6. Azad, B., & King, N. (2012). "Institutionalized Computer Workaround Practices in a Mediterranean Country: An Examination of Two Organizations." *European Journal of Information Systems*, 21(4), 358–372. — Empirical demonstration that workarounds *institutionalise*: they stop being temporary and become the de facto procedure, at which point the durable fix is never made because the workaround has become the system.
    7. von Mayrhauser, A., & Vans, A. M. (1995). "Program Comprehension During Software Maintenance and Evolution." *IEEE Computer*, 28(8), 44–55. — Program comprehension consumes roughly **half of maintenance effort**, and is a *reconstruction* process: knowledge is rebuilt from the artifact each time rather than retained. Every agent run that must re-derive the workaround pays this cost fresh. This is the mechanism for the "from scratch every run" observation.
    8. Aghajani, E., Nagy, C., Vega-Márquez, O. L., Linares-Vásquez, M., Moreno, L., Bavota, G., & Lanza, M. (2019). "Software Documentation Issues Unveiled." *ICSE 2019*. — 878 documentation artifacts; taxonomy of 162 issue types; documentation that would have captured a workaround is itself systematically outdated or incomplete, so the capture channel is unreliable.

  Strength of challenge: **Strong**

  Summary: The literature does not merely fail to support PRESUMPTION-673 — it directly and repeatedly refutes it, from three unrelated fields that converge on the same finding. Tucker and Edmondson's 93% figure is a near-exact analogue of C2A2's situation: capable actors under time pressure clear the immediate obstacle and do not touch the cause, and the resulting cost is a recurring per-episode tax rather than a one-time payment. Alter and Azad & King show the second stage: workarounds do not decay, they institutionalise, and once institutionalised the durable fix becomes *less* likely, not more. The STELLA report's dark-debt construct explains why the accumulated cost is invisible until it manifests as a failure. The program-comprehension literature supplies the specific mechanism for C2A2's stateless agents: knowledge is reconstructed, not retained, so every run pays full price. C2A2's case is worse than the studied cases in one respect and better in another: worse because its agents have no cross-run memory at all (a nurse at least remembers yesterday's workaround), better because its workarounds are disclosed in writing, which the nursing cases were not.

  Specific risks:
    (a) **Monotonic accumulation.** If N workarounds each cost c per run and none convert to fixes, per-run overhead grows as N·c without bound. Two disclosed today is the floor, not the count.
    (b) **Signal extinction (Tucker/Edmondson/Spear).** Each successful workaround suppresses the evidence that would justify authorising the durable fix. The system's competence at coping is the thing preventing its repair.
    (c) **Institutionalisation (Azad & King).** Once a workaround is rebuilt often enough, downstream artifacts come to depend on its specific shape, and the durable fix acquires a migration cost it did not originally have.
    (d) **Dark debt.** The disclosed workarounds are the visible ones. The literature predicts an unmeasured population of undisclosed ones living in agent-to-agent interactions.
    (e) **Authorisation bottleneck** — see SYSTEMIC-RISK-FLAG below. Both agents named the durable fix; neither could make it. The workaround is not being retained because nobody knows the fix; it is being retained because the fix requires a scarce authoriser.

  Mitigations available:
    (a) **Second-order problem solving as an explicit duty** (Tucker & Edmondson's own prescription): an agent that works around must file the cause, not just the symptom — C2A2 already does this; the gap is downstream.
    (b) **A workaround register with recurrence counts.** One of the two disclosures already carried its own count; make that mandatory and sort the register by count × cost. This converts dark debt into visible debt.
    (c) **A standing authorisation threshold**: any workaround rebuilt more than k times is pre-authorised for durable repair without a per-instance human decision. This is the direct antidote to (e) and does not require the human to act faster, only once.
    (d) **Externalise the reconstruction**: cache the workaround as an artifact (a script, a snippet, a prelude) so the per-run cost falls from re-derivation to retrieval, even where the durable fix is not authorised.

  Recommendation: **CHALLENGED (Strong)** — the premise that a workaround's cost is paid once is contradicted by direct empirical evidence in three literatures. C2A2 should treat rebuilt workarounds as a recurring rate, measure it, and pre-authorise repair above a recurrence threshold.

  STEELMAN:
    Item: PRESUMPTION-673
    Strongest counterargument: Tucker and Edmondson found that 93% of responses to system failure were workarounds that left the cause intact — and crucially, the *reason* was not laziness or ignorance. The nurses knew the fix. They were competent, motivated, and under time pressure, and the workaround was locally rational every single time. C2A2 has reproduced this exactly: two capable agents, both of whom *named the durable fix*, both of whom rebuilt the workaround instead, because neither was authorised to do otherwise. The literature's finding is that this configuration is stable and self-reinforcing: each successful workaround removes the evidence that would justify the fix, so the case for repair gets weaker precisely as the accumulated cost gets larger. Add the program-comprehension result — that stateless reconstruction consumes half of maintenance effort — and C2A2's per-run overhead is not a one-time onboarding cost but a permanent, growing tax, invisible in any single run because each run only sees its own share of it. The system is not paying once; it is paying an annuity it has never priced.
    What would need to be true for C2A2 to be safe: (a) the workaround set is small, bounded, and closed — no new members; (b) the per-run rebuild cost is genuinely trivial relative to run budget, and this has been *measured*, not assumed; (c) a channel exists by which recurrence count actually reaches an authoriser and produces a fix, with a demonstrated instance of it having done so; (d) the disclosed workarounds are the whole population, not the visible tail of a dark-debt distribution.
    How to test: One command. Grep the last 30 days of agent transcripts for workaround-disclosure language; count distinct workarounds and occurrences per workaround. Then, for each, check whether a durable fix was ever *made* (not merely proposed). If the fix-made count is zero while the occurrence count is > 1 for any workaround, the presumption is falsified directly. Second test: measure wall-clock or token cost of the rebuild segment in two consecutive runs; if it is non-trivial and equal, the cost is a rate.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-08-05
    Affected items: PRESUMPTION-673, PRESUMPTION-677 (also touches PRESUMPTION-675, PRESUMPTION-676)
    Common vulnerability: **Single-authoriser bottleneck.** PRESUMPTION-673's durable fixes are blocked because "neither [agent was] authorised to make it." PRESUMPTION-677 measures the queue in front of that same authoriser: 34 pending proposals, 136 REVISE, 137 MONITOR, 30 days with no decision. These are not two problems. They are one problem observed from both ends: the system generates repair work faster than its single authoriser can act on it, so repairs never land, so agents rebuild workarounds, so more disclosures are generated, which lengthens the same queue. This is a positive feedback loop with no damping term.
    Literature basis: Tucker & Edmondson (2003) on first-order problem solving; Little, J. D. C. (1961), "A Proof for the Queuing Formula: L = λW," *Operations Research*, 9(3), 383–387 — when arrival rate exceeds service rate the queue grows without bound and Little's Law ceases to hold in steady state; Anderson, D. J. (2010), *Kanban*, on WIP limits as the standard remedy; EEMUA 191 / ANSI-ISA-18.2 on the operator-rate ceiling.
    Risk level: **High**
    Recommendation: Introduce a class of repair that does not require the bottleneck resource — a standing pre-authorisation for workarounds above a recurrence threshold, and a WIP limit on new proposal generation until the existing queue drains. Fixing 677 without fixing 673's authorisation path only shortens the queue; fixing 673 without 677 only lengthens it.
