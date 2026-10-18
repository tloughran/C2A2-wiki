SEARCH-AGAINST-PRESUMPTION-1166:
  Date searched: 2026-10-18
  Run ID: local-6a3310ea-2026-10-18
  Original item: PRESUMPTION-1166
  Original statement: "Supervisory-control and out-of-the-loop automation literature (e.g. Bainbridge 1983 'Ironies of Automation'; Endsley & Kiris 1995 on out-of-the-loop performance): what happens to an automated monitoring system when the human supervisor is absent, and which handover practices reduce the damage?"
  Presumption under test (as framed for 15b): Unattended scheduled automation (C2A2 lit-search, self-awareness extraction and monitor pipelines) with periodic human review by Tom is safe enough, and handover/escalation practices can contain the damage of supervisor absence.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1166
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference from 2026-10-17 transcripts.
      15b: Searched for challenging literature; found 9 relevant sources (supervisory control, out-of-the-loop, complacency/automation bias, takeover, handover accidents, alarm fatigue, latent failure, human-oversight policy). Strength: Moderate-to-Strong.
    Current status: SEARCHED-15b (15b recommendation: PARTIALLY-CHALLENGED)

  Challenging evidence found: Yes (strong for the "periodic review catches failures" half; partial for the "handover practices contain damage" half)
  Search scope: PRELIMINARY — 11 WebSearch calls, 1 fetch (a full secondary summary of Bainbridge with direct quotes). No primary paper read in full. No source studies unattended LLM/agent pipelines directly, so every source is a transfer from aviation, process control, driving, healthcare or government algorithms. Broader search recommended, especially on software/MLOps monitoring.

  Sources:
    1. Bainbridge, L., 1983. "Ironies of Automation." Automatica 19(6): 775-779. — The better the automation, the rarer and harder the cases left for the human. Monitors cannot check fast, fully specified decisions in real time ("the human monitor has been given an impossible task"). Skills decay, and self-correcting automation can hide trends until they are out of control. [Evidence level: full secondary summary with direct quotes (ferd.ca notes, fetched); abstract and multiple snippets. Primary PDF exists (gwern.net, ckrybus.com) but was not fetched.]
    2. Endsley, M.R. & Kiris, E.O., 1995. "The Out-of-the-Loop Performance Problem and Level of Control in Automation." Human Factors 37(2): 381-394. doi:10.1518/001872095779064555. — Passive monitoring lowers situation awareness; low SA went with slower decisions after the automation failed. Full automation did worst, manual best. [Evidence level: abstract (TRID index) plus Wikipedia/secondary summary.]
    3. Parasuraman, R. & Manzey, D., 2010. "Complacency and Bias in Human Use of Automation: An Attentional Integration." Human Factors 52(3): 381-410. doi:10.1177/0018720810376055. — Complacency appears under multi-task load (the supervisor has other work), affects experts as well as novices, and is not removed by practice. Automation bias is not prevented by training or instructions. [Evidence level: abstract and secondary snippets.]
    4. Onnasch, L., Wickens, C.D., Li, H. & Manzey, D., 2014. "Human Performance Consequences of Stages and Levels of Automation: An Integrated Meta-Analysis." Human Factors 56(3). — Meta-analysis of 18 experiments: higher automation helps routine performance but hurts performance and SA when it fails ("lumberjack effect": the higher the tree, the harder it falls). Contested by Jamieson & Skraaning for professional operators; Wickens et al. replied. [Evidence level: abstract and secondary snippets; volume/issue from memory of the standard citation, year varies 2013/2014 across records.]
    5. Zhang, B., de Winter, J., Varotto, S., Happee, R. & Martens, M., 2019. "Determinants of take-over time from automated driving: A meta-analysis of 129 studies." Transportation Research Part F 64: 285-307. doi:10.1016/j.trf.2019.04.020. — Takeover is slow and highly variable; shorter time budgets worsen outcomes. [Evidence level: title/abstract snippet only; pooled figures NOT seen.]
    6. Cullen, Lord, 1990. The Public Inquiry into the Piper Alpha Disaster; and Wilkinson & Lardner (IChemE Hazards XXIII, paper 16). — The night shift restarted a pump without knowing a safety valve had been removed, because the permit and handover system did not carry the plant's real state. Wilkinson & Lardner say shift-handover failures remain a major contributor to major accidents (Buncefield, Texas City). WA regulator guidance links handover failures to Piper Alpha, Grangemouth, Texas City and Buncefield. [Evidence level: secondary summaries and snippets; Cullen report not read.]
    7. Alarm-fatigue literature: Winters et al., 2018 (systematic review, seen only via a secondary site); Michels et al., 2025 scoping review (PMC12181921, BMC Nursing); UCSF bedside-monitor study (88.8% of 12,671 arrhythmia alarms false positives). — Frequent non-actionable alarms make people dismiss or respond slowly to alerts and disable them. Evidence that mitigation works is weak. [Evidence level: snippets; Winters UNVERIFIED firsthand.]
    8. Cook, R.I., 1998/2000. "How Complex Systems Fail." Cognitive Technologies Laboratory, Univ. of Chicago. — Complex systems always contain changing latent failures and "run as broken systems". Each flaw alone looks minor, so periodic inspection tends to dismiss it. [Evidence level: snippets quoting the text; full text at how.complexsystems.fail, not fetched. Practitioner essay, not peer-reviewed.]
    9. Green, B., 2022. "The flaws of policies requiring human oversight of government algorithms." Computer Law & Security Review 45: 105681. doi:10.1016/j.clsr.2022.105681. — Review of 41 policies: evidence suggests people cannot perform the oversight such policies require, and oversight rules give a false sense of security that legitimises flawed systems. Proposes institutional oversight backed by evidence. [Evidence level: abstract (arXiv 2109.05067) and snippets.]
    10. (Adjacent, weak) Sculley, D. et al., 2015. "Hidden Technical Debt in Machine Learning Systems." NeurIPS 2015: 2503-2511. — In production ML, debt and erosion "compound silently" at system level and are hard to detect. Supports "silent failure", but its monitoring section was not seen. [Evidence level: abstract and intro snippets only.]

  Strength of challenge: Moderate-to-Strong
    - Strong against "periodic human review is enough to catch failures" (sources 1-4, 8, 9 agree across domains).
    - Moderate against "handover/escalation practices contain the damage". The literature does not say handover practices are useless. It says they often fail in practice (6), alerts degrade with volume (7), and takeover is slow and unreliable (5). It does name practices that help (see Mitigations).

  Summary: The supervisory-control literature mostly predicts the reverse of the comfortable reading. The more reliably automation runs unattended, the less able the absent supervisor is to spot or fix its failures when they come. Their situation awareness, skill and attention to the system all decline (Bainbridge; Endsley & Kiris; Onnasch et al.). Complacency and automation bias are not fixed by expertise, training or instructions, and they get worse when the supervisor has competing work, which is the C2A2 situation (Parasuraman & Manzey). Handover is a documented route into major accidents when the record of system state is incomplete (Piper Alpha). Alert-based escalation loses force as volume rises (alarm fatigue). Cook and Green add that latent faults are normal and look minor when inspected, and that nominal "human in the loop" oversight can give false assurance.

  Specific risks for C2A2:
    - Silent drift: pipelines can produce well-formed but wrong output (bad citations, wrong status tags, duplicate runs). Every run looks normal, so periodic review approves it (Bainbridge's "acceptable at meta-level" problem; Cook's latent failures).
    - Rubber-stamp review: Tom reviews many agent outputs among other work, which is the multi-task condition where complacency is strongest. Review volume can grow faster than his attention.
    - Escalation fatigue: if monitors and flag files (SYSTEMIC-RISK flags, warnings) fire often, they will be skimmed or ignored, and real flags will be lost.
    - Handover gaps: run state carried between runs, twins or sessions (lock files, queue tags, partially processed items) is a Piper Alpha-type risk if the record is incomplete.
    - Lumberjack effect: the more the chain is automated (14b → 15a/15b → reconciliation), the worse a single upstream error spreads before anyone notices.
    - False assurance: the provenance and review machinery itself may make outputs look "checked" without anyone having checked them (Green).

  Mitigations available (named in the literature; 15b reports them, does not recommend design):
    - Keep the human in the loop sometimes: have the human run some steps manually or check spot samples in depth, to preserve skill and SA (Bainbridge; Endsley & Kiris intermediate levels of control; Kaber & Endsley 1997).
    - Run automation at a pace and with a trace the human can follow; check effects (outputs against ground truth) rather than procedures (Bainbridge).
    - Prefer safe stop: halt and hold for review when anomalies appear, rather than continue (Bainbridge).
    - Structured written handover that records actual system state, with more care at abnormal times (Cullen; WA regulator; Wilkinson & Lardner).
    - Keep alerts few and actionable; cut non-actionable alerts (alarm-fatigue literature, though evidence that this works is weak).
    - Seed known faults (canaries) to test whether review actually catches them. This is an empirical test of oversight in Green's sense.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1166
  Strongest counterargument: Bainbridge's central irony is that the supervisor of a well-running automated system is given an impossible task. They are asked to catch rare, subtle failures in a system they no longer actively operate, with fading skills and context, under competing demands. Forty years of experiments (Endsley & Kiris; Parasuraman & Manzey; Onnasch et al.) show passive monitoring reliably lowers detection and recovery, and expertise and instructions do not fix it. Periodic review of unattended runs is the weakest form of supervision. It sees only artefacts, after the fact, and those artefacts look fine when the failure is silent. Handover and escalation fail in exactly the conditions that matter: incomplete state records (Piper Alpha), alert overload (alarm fatigue), and slow, error-prone takeover (Zhang et al.). Calling this "safe enough" may be the false assurance Green describes.
  What would need to be true for C2A2 to be safe:
    - Failures are low-consequence and reversible: wiki files are versioned, nothing irreversible is triggered unattended, and mistakes can be fixed at the next review without lasting harm. (This is the strongest point FOR the presumption. Most supervisory-control results come from time-critical, high-hazard domains such as flight, driving, process plants and ICUs, where seconds matter. C2A2 has days of slack, which is Bainbridge's "slow failure" case where stopping to look is possible.)
    - Review checks content against ground truth (spot-check citations, compare outputs), not just that the run completed.
    - Alerts and flags are rare enough to be read.
    - Each run writes an explicit record of state and anomalies for the next run or reviewer.
  How to test:
    - Fault injection: plant a fabricated citation, a wrong status tag or a duplicate run in one pipeline output, and measure whether and when Tom's periodic review catches it.
    - Audit a sample of past unattended outputs in depth and compare the error rate with what earlier reviews flagged.
    - Count flags and warnings per week against how many were acted on (an alarm-fatigue proxy).
    - Track review time per output as volume grows.

CANDIDATE SYSTEMIC-RISK (noted for 14b / Agent 12; no separate flag file written):
  Date: 2026-10-18
  Affected items: PRESUMPTION-1166, and likely every C2A2 item that relies on scheduled unattended runs being checked later by a human. This includes the 14a/14b → 15a/15b → reconciliation chain itself, monitor agents, and PRESUMPTION-1149 (twin-run lock protocol; seen only as a format reference, whose duplicate-run failures are a handover/state-record problem). Item IDs beyond 1149 were not checked; 14b should enumerate them.
  Common vulnerability: Safety rests on an absent supervisor's later review catching silent, plausible-looking failures. The supervisory-control literature predicts this review gets worse the better the automation usually works, and nominal oversight can create false assurance.
  Literature basis: Bainbridge 1983; Endsley & Kiris 1995; Parasuraman & Manzey 2010; Onnasch et al. 2014; Green 2022; Cook 1998/2000.
  Risk level: High (not Critical, because C2A2 failures are mostly slow and reversible)
  Recommendation: The system should consider empirically testing whether its human review catches seeded faults before treating unattended operation plus review as a validated safeguard.

FETCH LOG:
  - ferd.ca/notes/paper-ironies-of-automation.html — fetched OK (secondary summary with direct Bainbridge quotes).
  - No other fetches attempted. No fetch failures. Primary PDFs (Bainbridge, Cook, Green arXiv, Zhang TU Delft OA) are available but were not read.
