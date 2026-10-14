SEARCH-FOR-PRESUMPTION-1135:
  Date searched: 2026-10-14
  Original item: PRESUMPTION-1135
  Original statement: [inferred] Each health report presumes its own vantage suffices; none consumes the others' FAILs. Morning project status certified "no other issues" hours after scheduler health logged 7 FAILs; system health cited yesterday's telemetry failure. With 4+ overlapping monitors, no one owns the aggregate. Question tested: do multiple uncoordinated monitors raise or lower failure detection? Supportive direction: evidence that redundant monitors without aggregation or ownership lower detection, or fail to raise it.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1135
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cited evidence across 2026-10-13 transcripts and wiki files.
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Sagan SD, 2004. "The Problem of Redundancy Problem: Why More Nuclear Security Forces May Produce Less Nuclear Security." Risk Analysis 24(4):935-946. [Access level: secondary summaries; full text not read.] Argues that redundancy raises reliability only if the components fail independently. Organizational redundancy instead brings (i) common-mode error, (ii) social shirking, where each unit assumes another is responsible, and (iii) overcompensation, a false sense of security. This is the closest theoretical match to "4+ overlapping monitors, no one owns the aggregate."
    2. Ghaffarzadegan N, 2008 (Risk Analysis; 2007 System Dynamics Conference paper). System-dynamics test of Sagan. [Access level: snippet.] Simulation finds that social shirking creates inefficiency and makes common-mode error worse.
    3. Cheng L, 2005. Economics working paper on redundancy and free-riding (econwpa 0508004; exact title not verified). [Access level: snippet.] Formal model: more redundant members can lower system reliability, because each member's effort falls unless monitoring costs drop enough to offset it.
    4. Cymek DH, Jahn S, Manzey D, 2018 (and earlier conference version). "Redundant Automation Monitoring: Four Eyes Don't See More Than Two, if Everyone Turns a Blind Eye." TU Berlin DepositOnce. [Access level: abstract/snippet.] Experiment: participants who shared an automation-monitoring task did fewer cross-checks and found 25% fewer automation failures than solo monitors. Team performance did not beat solo performance. When individual performance feedback was expected (accountability and ownership), the team advantage reappeared. This is direct empirical support, and it also identifies the moderator that matters: individual ownership.
    5. Cymek DH, 2024. "Effects of blinded and nonblinded sequential human redundancy on inspection effort and inspection outcome in low prevalence visual search." (PMC11450219.) [Access level: snippet.] When the second checker could see the first checker's marks, the second checker's effort dropped substantially. Blinded (independent) redundancy showed no loafing and near-perfect team detection. This is conditional support: redundancy fails when it is not independent.
    6. Fischer P, Krueger JI, Greitemeyer T, et al., 2011. "The bystander-effect: A meta-analytic review..." Psychological Bulletin 137(4):517-537. [Access level: abstract/snippet.] 105 effect sizes, g = -0.35: the presence of others lowers individual intervention, through diffusion of responsibility among other mechanisms. This is background support for the human analogue. The effect weakens in clearly dangerous situations.
    7. Alarm-fatigue literature (integrative review of 72 articles; trade-press report of a CHEST 2017 ICU study). [Access level: snippet/secondary.] Desensitization is linked to high false-alarm rates, low positive predictive value, lack of standardization, and the number of alarming devices. This is weak support that many overlapping alarm sources degrade response. The studies did not isolate redundancy.

  Strength of support: Moderate-to-Strong

  Summary: Safety-science theory (Sagan), formal and simulation models (Cheng; Ghaffarzadegan) and controlled experiments (Cymek et al.) converge. Adding monitors without independence, aggregation or individual ownership often fails to raise detection and can lower it, through social shirking and diffusion of responsibility. The experimental work also gives the boundary conditions: redundancy does improve detection when checks are blinded or independent and each monitor is individually accountable. This matches the presumption's diagnosis. Several overlapping reports, none consuming the others' FAILs and none owning the aggregate, is the configuration the literature predicts will not deliver the expected reliability gain.

  Caveats: (a) Domain transfer. Most mechanisms are human-behavioural (loafing, responsibility diffusion), and LLM-agent monitors do not "shirk" in the motivational sense. The analogous mechanism for agents is structural: no component reads the others' outputs, and the shared inputs carry common-mode errors. The C2A2 failure pattern (one report certifying "no other issues" after another logged FAILs) fits the aggregation and ownership gap more than motivational loafing. (b) Cymek's results depend on the design (blinded vs. nonblinded; feedback vs. no feedback). (c) The alarm-fatigue evidence is indirect and partly from trade press. (d) Most sources were read only at abstract or snippet level.

  Search scope: 3 web searches (alarm fatigue and redundant alarms; Sagan redundancy; bystander/diffusion meta-analysis) plus 1 on redundant-inspection social loafing. 4 searches, 0 page fetches. Moderately comprehensive for the human-factors and safety literature. SRE/ops-specific literature (alert aggregation, "who owns the pager") was not searched; broader search recommended there.

  Recommendation: SUPPORTED
