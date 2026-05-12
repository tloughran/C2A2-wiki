SEARCH-FOR-PRESUMPTION-063:
  Date searched: 2026-04-21
  Original item: PRESUMPTION-063
  Original statement: "'Natural termination' is an acceptable default resolution for scheduled tasks that appear to be running indefinitely."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-063
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from evening sync invoking Monday's Levin-Friston precedent
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Let-it-crash literature (Erlang philosophy; Armstrong 2003): in some systems, allowing processes to terminate on their own rather than intervening is a valid default — provided there's a supervision tree monitoring termination. Supervision, not natural-termination-alone, is the pattern.
    2. Graceful-degradation literature (Nygard 2007 "Release It!"): intervening mid-execution can produce worse failure modes than allowing a misbehaving process to run its course if intervention paths are untested. Provides narrow support for read-only observation when intervention is unsafe.

  Strength of support: Weak

  Summary: No literature supports "natural termination as default" without a supervision layer or explicit safety condition. Erlang's let-it-crash requires a supervision tree; graceful-degradation requires tested intervention paths. The C2A2 scheduled-task layer has neither at present. Supportive literature would require the system to have a termination-detection primitive (it doesn't), a timeout invariant (it doesn't), or an explicit cost-budget ceiling (it doesn't for specialist tasks). The single-prior-instance (Monday's Levin-Friston) is not a precedent in any methodological sense — it is an N-of-1 observation that happens to have worked out.

  Caveats: (a) "Natural termination" may be a reasonable policy under a supervision layer, which C2A2 does not currently have; (b) the Monday precedent provides descriptive, not normative, support — it happened and terminated, but nothing about that outcome validated the policy; (c) candidate DECISION-024 (turn-cap default = 20) represents an alternative approach and the two are in direct tension.

  Recommendation: NO-SUPPORT-FOUND (natural-termination-as-default requires supervision/timeout primitives that C2A2 scheduled-task layer lacks; single-prior-instance is not a defensible precedent; direct tension with candidate DECISION-024)
