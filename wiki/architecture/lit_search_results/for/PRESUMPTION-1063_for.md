SEARCH-FOR-PRESUMPTION-1063:
  Date searched: 2026-09-22
  Original item: PRESUMPTION-1063
  Original statement: Substituting oldest-day work for an empty queue is a choice, not a necessity, and
    its costs and yields have never been set against each other.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1063
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Noted that twenty-nine runs chose one response to an empty queue and none named an
        alternative.
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Hsee, C. K., Yang, A. X., & Wang, L. (2010). "Idleness Aversion and the Need for Justifiable
       Busyness." Psychological Science, 21(7), 926-930. DOI:10.1177/0956797610374738. — Establishes
       experimentally that agents strongly prefer any justifiable activity over idling, independent of
       whether that activity is instrumentally useful. Directly supports the presumption's implicit
       mechanism: choosing "oldest-day work" over remaining idle is plausibly driven by
       idleness-aversion rather than by a considered cost/yield comparison, i.e. it is a psychological
       default, not a derived necessity.
    2. Queueing-theory idle-server / vacation-queue literature (general operations-research tradition;
       see e.g. discussion of N-policy queues and "working vacation" models, and MDPI 2025 "Performance
       Analysis and Cost Optimization of the M/M/1/N Queueing System with Working Vacation and Working
       Breakdown"). — Establishes that what a server does during idle periods (stop entirely, work at
       reduced rate, or perform alternative/preparatory tasks) is a first-class, explicitly modeled
       policy decision in the field, with different policies yielding different cost-optimal outcomes.
       This directly supports "substituting oldest-day work... is a choice, not a necessity": the
       literature treats it as exactly the kind of choice that requires a stated policy and a cost
       model, neither of which the brief says was ever produced for these 29 runs.
    3. General queueing cost-optimization framing (practitioner/OR sources): "if costs are assigned to
       factors such as customer waiting time and server idle time, it's possible to investigate how to
       design a system at minimum total cost" — this is precisely the missing comparison the
       presumption flags as absent; the literature shows such a comparison is standard practice where
       idle-time policy is taken seriously, reinforcing that its absence here is a gap rather than an
       unavoidable default.

  Strength of support: Strong

  Summary: The presumption has two parts — (a) the substitution is a choice among alternatives, not a
    forced move, and (b) its costs/yields have never been compared. Queueing theory directly supports
    (a): idle-period policy (stop, slow down, or do alternative work) is a standard, explicitly modeled
    design decision with multiple named alternatives in the literature, confirming that "no alternative
    was named" in the 29 runs reflects an omission, not an absence of alternatives. The idleness-aversion
    literature supports why the default might have gone unexamined: humans (and plausibly agents trained
    on human-generated patterns) have a documented bias toward filling idle time with any justifiable
    activity, which would produce exactly the pattern 14b observed (uniform selection of one response,
    no alternatives considered) without any actual cost/yield analysis (b) having occurred.

  Caveats: The idleness-aversion literature is about human psychology; its application to an agentic
    system's behavior is an analogy, not a direct finding about AI agents choosing work in an empty
    queue — plausible if the agent's policy was learned from human-generated text/behavior patterns, but
    not confirmed. The queueing-theory literature supports that idle-policy comparison is standard
    practice in principle; it does not confirm that a "make-work" substitution specifically (as opposed
    to true rest/stop) is suboptimal in this context — that determination would require the actual cost
    data the presumption says is missing.

  Search scope: Preliminary — two searches covering queueing-theory idle-server policy and
    idleness-aversion psychology. Recommend a follow-up search specifically on "make-work" costs in
    automated/algorithmic review systems (as opposed to human workplace idleness) for a tighter domain
    match.

  Recommendation: SUPPORTED
