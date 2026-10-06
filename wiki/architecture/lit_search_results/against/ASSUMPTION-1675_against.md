SEARCH-AGAINST-ASSUMPTION-1675:
  Date searched: 2026-09-24
  Original item: ASSUMPTION-1675
  Original statement: Three unattended runs tried to escalate to the host through Desktop
    Commander; all were auto-declined or ended without report. (Tested claim: in unattended
    automation, fallback to a higher-privilege channel should be declared in the task, not
    discovered by the agent at failure time.)

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-1675
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted; the 47834dc7 outcome is inferred from truncation.
      15b: Searched for challenging literature (lane: HITL automation; least privilege; levels of automation)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. McGuinness, M., Grace, M., De Jonghe, J., Eaton, J., & Ribbink, A. (Anthropic, 2026-05-25).
       "How we contain Claude across products." anthropic.com/engineering. [Fetched.] Conflict-of-
       interest note: this is the vendor of the model running this search. An egress allowlist
       entry "may be better conceptualized as a capability grant". Every function reachable
       through a declared channel becomes attack surface: data was exfiltrated through an
       approved domain while "the sandbox worked perfectly". A fallback declared in the task is a
       standing capability grant. Any prompt injection that reaches the agent can use it, not only
       genuine failures.
    2. OWASP GenAI Security Project (2025). "LLM06:2025 Excessive Agency." [Fetched.] It names
       extensions "not needed for the intended operation" as the vulnerability (excessive
       functionality/permissions). It recommends minimizing extensions, "complete mediation" in
       downstream systems, and human approval for high-impact actions. A declared-but-rarely-
       needed higher-privilege fallback is this pattern.
    3. Just-in-time vs standing privilege (practice literature; seen via Palo Alto Networks and
       ConductorOne explainers in search results; NIST SP 800-53/800-207 referenced but not
       fetched). Break-glass access is best implemented with no standing permission, granted on
       request, time-bound and reviewed. Pre-declared elevation is the pattern JIT is meant to
       replace.
    4. Bainbridge, L. (1983). "Ironies of automation." Automatica 19(6):775-779. [Seen via search
       results; not fetched.] The situations that need fallback are the ones designers did not
       anticipate. A fixed, pre-declared fallback covers the anticipated failures and leaves the
       novel ones, which is the SUPPORT side's weak point.

  Strength of challenge: Moderate

  Summary: The literature agrees that the agent should not improvise escalation, so the "not
  discovered at failure time" half stands. It challenges the prescription "declare it in the
  task". Security practice treats any declared route to higher privilege as a standing capability
  grant, and grants in agent systems are exploited by injected instructions, not only by genuine
  failures. The preferred alternatives are to declare no fallback (fail closed and report), or to
  declare a fallback that is mediated outside the agent (JIT, approval, scoped token), not one the
  agent can invoke on its own judgment. Bainbridge adds that fixed fallbacks will not match
  unanticipated failures, so declaration does not remove the discovery problem.

  Specific risks: Writing "if the sandbox fails, use Desktop Commander" into task files would turn
  three blocked attempts into three permitted host-side executions. The trigger ("sandbox fails")
  is easy for an injected document to fake. It would also legitimize host-side access for jobs
  whose failures are actually disk-space problems (ASSUMPTION-1663).

  Mitigations available: Declare the fallback as "stop and write a failure report", not as a
  privileged channel. If a host-side path is required, give it its own separately scheduled host
  job with a fixed command, not open-ended shell access. Keep enforcement outside the agent
  (complete mediation).

  Search scope: Preliminary: 3 searches plus 2 fetches.

  Excluded results: nhimg.org FAQ pages (multiple; SEO-style Q&A pages whose titles echo the query
  framing closely; unattributed); a10networks glossary; blog.alexewerlof.com OWASP cheat sheet
  (secondary to OWASP, which was fetched directly); GitHub microsoft/hve-core OWASP reference
  (GitHub); Medium post on Ironies of Automation.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1675
  Strongest counterargument: Declaring a higher-privilege fallback in the task does not remove
    improvisation. It pre-authorizes it and hands the trigger condition to whatever the agent
    reads. Security practice has moved away from standing elevation to just-in-time grants
    mediated outside the actor, because declared paths are what attackers and confused agents use.
    An unattended agent with a declared host channel is a confused deputy waiting for a persuasive
    input. The safer declaration is the absence of a fallback: fail closed, report, and let a
    separately authorized host job act.
  What would need to be true for C2A2 to be safe: Any declared fallback is narrow (a fixed command,
    not shell), mediated outside the agent, logged, and triggered by a condition the agent cannot
    assert about itself.
  How to test: Red-team one task file with a declared fallback. Plant a document claiming the
    sandbox failed and check whether the agent invokes the fallback.
