SEARCH-FOR-PRESUMPTION-675:
  Date searched: 2026-08-05
  Original item: PRESUMPTION-675
  Original statement: That a documented limit is an enforced limit — three
    surfaces carry the visualization's limits (docs 2,000/3,000; code
    20,000/30,000; shipped artifact 3,864/98,201) and the artifact is legal on
    none of them, with no limit warning emitted.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-675
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by measuring the third surface the day's reports did not
        read
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Perry, D.E. & Wolf, A.L., 1992. "Foundations for the Study of Software
       Architecture." ACM SIGSOFT Software Engineering Notes 17(4): 40-52. —
       The origin of the distinction the item needs: architectural erosion
       (violation of stated principles) versus architectural drift
       (insensitivity to them). Both name the gap between a specification and
       what the running system does; neither treats the specification as
       self-enforcing.
    2. De Silva, L. & Balasubramaniam, D., 2012. "Controlling software
       architecture erosion: A survey." Journal of Systems and Software 85(1):
       132-151. — The standard survey of the field. Its premise is that
       divergence of implemented from specified structure is the default outcome
       absent an active control mechanism, and its finding that academic control
       methods have had limited industrial adoption means the default is what
       most systems actually experience.
    3. Li, R., Liang, P., Soliman, M. & Avgeriou, P., 2022. "Understanding
       software architecture erosion: A systematic mapping study." Journal of
       Software: Evolution and Process 34(3), e2423. — Confirms the phenomenon
       is stable across two decades and many names (architectural degeneration,
       decay, code decay, software entropy); the recurrence of the finding under
       independent terminologies is itself evidence that specified-equals-
       enforced does not hold.
    4. Tan, L., Yuan, D., Krishna, G. & Zhou, Y., 2007. "/*iComment: Bugs or Bad
       Comments?*/" SOSP 2007. — Empirical: extracting implicit rules from
       comments in Linux, Mozilla, Wine and Apache and checking them against
       code found confirmed comment-code inconsistencies, including outdated
       comments that later caused reported bugs. A documented constraint that
       has silently ceased to describe the code is the general case, not an
       outlier.
    5. Wen, F., Nagy, C., Bavota, G. & Lanza, M., 2019. "A Large-Scale Empirical
       Study on Code-Comment Inconsistencies." ICPC 2019. — Large-scale
       replication with causes characterised (deprecation, refactoring); the
       documented value goes stale by the ordinary mechanics of change, not by
       negligence.
    6. Vacuity in assertion-based verification (SystemVerilog assertion
       literature; standard practitioner treatment of vacuous success). — Bears
       directly on the second half of the item. An implication whose antecedent
       is never matched passes vacuously; a check that never fires is therefore
       not evidence of compliance and requires separate coverage evidence that
       the antecedent was ever reached. "No limit warning emitted" is
       information-free without that evidence.
    7. Policy-as-code / compliance-as-code practice literature (vendor and
       platform-engineering sources, 2024-2026). — The only route to support
       found. Where the constraint is itself the executable artifact and every
       other surface is generated from it, a documented limit is an enforced
       limit by construction. Note: this body is practitioner and vendor
       material with weak independent evaluation; the quantified claims in it
       (e.g. large reductions in misconfiguration) are not verified here.

  Strength of support: Weak

  Summary: No support was found for reading a documented limit as an enforced
    limit. The architecture-erosion literature is built on the opposite
    premise — that specified and implemented structure diverge by default unless
    an active control mechanism holds them together — and the code-comment
    inconsistency studies supply the fine-grained empirical version of the same
    result at the level of individual documented constraints. The one supportive
    route is real but narrow: under policy-as-code, where the document is the
    executable constraint and all other surfaces are generated from it, the
    identity holds by construction. The case reported fails that condition
    definitionally, since it has three independently authored surfaces (docs,
    code, artifact) with no generative relation among them; three surfaces is
    the signature of the drift condition, not the enforced one. The absence of a
    limit warning adds nothing on the supportive side: the assertion-vacuity
    literature is explicit that a check which never fires is not a passing check,
    and that establishing non-vacuity requires separate evidence the check was
    reached at all.

  Caveats: The erosion and code-comment literatures concern human-authored
    source and prose; a generated visualization artifact is a different object,
    and it is possible that the code limits (20,000/30,000) were deliberately
    raised and the docs simply not updated — an intentional change badly
    propagated rather than drift. That distinction does not change the
    conclusion for this item, since either way the documented figure does not
    describe what is enforced. The policy-as-code support would become real
    support if one surface were made generative and the other two derived from
    it; that conversion is well precedented and is the standard remedy the
    literature points to. Search scope note: no peer-reviewed empirical study of
    configuration drift rates was located — that literature is dominated by
    vendor material and is a genuine gap.

  Recommendation: NO-SUPPORT-FOUND

  Search scope: Adequate. Concepts searched: configuration drift and divergence
    of documented from actual state; software architecture erosion, drift and
    decay; code-comment inconsistency and documentation decay; detection of
    outdated documentation; policy-as-code, compliance-as-code and executable
    specification as single source of truth; assertion vacuity and the
    non-informativeness of an unfired check; monitoring the monitor.
