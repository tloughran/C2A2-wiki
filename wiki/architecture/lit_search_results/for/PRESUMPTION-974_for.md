SEARCH-FOR-PRESUMPTION-974:
  Date searched: 2026-09-13
  Original item: PRESUMPTION-974
  Original statement: [inferred] That an in-house test named but unassigned is deferred work rather than
    declined work. 178 days owed across PREMISE-108/120/135 and REVISE-342, zero executed; all five
    remedial actions are greps; this register attaches such a test to nearly every item it files.
  Flagged CRITICAL by 14b: load-bearing for the entire self-awareness apparatus.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-974
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by reading 15b's four-item finding against this register's own filing habit. Routed
        against this register's interest: a CHALLENGED verdict invalidates the principal output format of
        Agents 14a and 14b.
      15a: Searched organisational and incident-review literature for evidence that action-item
        follow-through succeeds where ownership is assigned — i.e. that a named remedy is recoverable work
        rather than a dead letter.
    Current status: PARTIALLY-SUPPORTED

  Search scope: Web search across SRE/incident-review practice (Google postmortem action-item practice,
    USENIX ;login:, SRE book) and the goal-pursuit psychology of follow-through (implementation
    intentions). Also swept general meeting/action-item management writing, which returned almost entirely
    vendor marketing and was largely discarded — see the DO-NOT-CITE list. **Preliminary, not
    comprehensive** — no peer-reviewed project-management or organisational-behaviour database sweep was
    run. One source (USENIX) was read in full.

  Supporting evidence found: Partial

  Sources:
    1. Lunney, J., Lueder, S. & Beyer, B., 2017. "Postmortem Action Items: Plan the Work and Work the
       Plan." ;login: (USENIX) 42(1): 40–45. — **VERIFIED: read in full.** The single most on-point source
       found. It names ownership as the determining variable in exactly the terms this presumption needs:
       "The surest way for a postmortem author to ensure that an action item never gets completed is to
       leave it without an owner," with the mitigation "Always assign an owner for every action item as it
       is enacted, even if that owner's primary task is to find the best person for the job." It also
       reports, from thousands of Google postmortems, that "the most common shortcoming is lack of
       follow-up," and that while higher-priority items close faster on average, *among still-open items*
       priority does not significantly influence age — open P1s are nearly as old as open P3s. It further
       requires that items be worded Actionable, Specific and Bounded, and treats an unbounded or
       process-shaped item ("Investigate dependencies") as a defect. Finally, and directly against the
       deferred reading: "Encourage action item owners to close AIs that you'll never have time to
       address — don't keep them around forever. If an AI is obsolete or infeasible, it just distracts you
       from the AIs that still need work."
    2. Gollwitzer, P.M. & Sheeran, P., 2006. "Implementation intentions and goal achievement: A
       meta-analysis of effects and processes." Advances in Experimental Social Psychology 38: 69–119. —
       Theoretical grounding for the supportive direction: specifying in advance *who* will do *what*,
       *when* and *where* produces a medium-to-large effect on goal attainment (d = 0.65 across 94
       independent tests, >8,000 participants), operating through initiation of goal striving, shielding
       of ongoing pursuit, and disengagement from failing courses of action. A named, owned, scheduled test
       is an implementation intention; a named, unowned test is a bare goal intention. **SECONDARY** —
       abstract level, but d = 0.65 and k = 94 are stable across multiple independent reports and are
       reported here with moderate-to-high confidence.
    3. Beyer, B., Jones, C., Petoff, J. & Murphy, N. (eds.), 2016. Site Reliability Engineering, O'Reilly,
       ch. "Postmortem Culture: Learning from Failure." — The parent statement of the practice above.
       **SECONDARY** — known only through the USENIX article's citation of it.

  Strength of support: Moderate

  Summary: The incident-review literature supports the presumption's implicit theory in one specific
    respect: ownership, not intention, is what converts a named remedy into completed work, and Google's
    published practice treats assignment as the mitigation that makes an action item recoverable. The
    goal-pursuit meta-analytic evidence gives the same result from the other direction, with a
    medium-to-large effect for specifying agent and occasion. So the register's implicit claim that these
    tests could be discharged by assigning them is well founded. But the same literature supplies the
    condition under which the deferred reading fails, and the register meets that condition exactly. The
    named-but-unowned state is not described anywhere as a waiting state; it is described as the
    canonical failure mode. And Google's own guidance is that an item you will not get to should be
    *closed* rather than carried — which is the declined reading, adopted as best practice rather than as
    an accusation. The 178-day age with zero executions, across items that are unowned and whose remedies
    are all greps, is in that literature's terms an unbalanced action-item plan with lack-of-ownership
    anti-pattern, not a deferral.

  Caveats:
    - The supporting condition is absent in the case at hand. Every source found supports follow-through
      *conditional on assignment*; none supports the proposition that unassigned items remain live. The
      support therefore attaches to the remedy, not to the presumption's status quo.
    - Domain transfer: SRE postmortem practice concerns human engineering teams with issue trackers,
      sprint planning and executive escalation. An agent register that files its own tests has no
      equivalent of the Google mechanisms that actually do the work — burndown reporting, closure-time
      objectives, VP review. Transferring the finding without transferring the mechanism is not warranted.
    - Gollwitzer & Sheeran measure individual human goal pursuit under experimental conditions. Its
      transfer to an artificial register's self-filed tests is analogical, not direct.
    - The USENIX source is practitioner experience report, not a controlled study. It reports Google's
      aggregate observations and shows figures, but publishes no completion-rate statistic that can be
      cited as a measured base rate.
    - **DO-NOT-CITE — figures encountered but unverifiable.** "Action items from postmortems have a 30%
      completion rate industry-wide"; "below 50% means your postmortems are theater"; "aim for >85%
      completion"; "repeat incident rate fell from 45% to 12% over six months." All four appeared in
      vendor/consultancy blog posts (incident.io, ITOC360, Opsera, personal blogs) with no traceable
      source study. These are exactly the shape of the figure that burned the 2026-09-12 cycle. They are
      recorded here so that a later reader who encounters them knows they were seen and rejected, and must
      not be propagated into any estate document.

  Recommendation: PARTIALLY-SUPPORTED
