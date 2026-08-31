SEARCH-FOR-ASSUMPTION-1235:
  Date searched: 2026-08-31
  Original item: ASSUMPTION-1235
  Original statement: "This agent has no business running `git` at all." (i.e. a read-only analysis agent should not hold a version-control capability.)
  Generalizable limb searched: Should an agent whose remit is read-only analysis be denied general-purpose / state-mutating capabilities (shell, VCS) that its stated task does not require? Does narrowing capability measurably reduce incident rates?

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 3 queries run; no full-text reads. One
    normative standard (OWASP) read at snippet depth but its wording is quoted widely enough in
    results to be treated as reliable. The empirical incident-rate figure is from a vendor-adjacent
    survey seen only in snippet and should be treated as weak.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-1235
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced from the run's own critique of an out-of-scope `git` invocation by a read-only analysis agent
      15a: Searched for supporting literature (2026-08-31)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. OWASP Gen AI Security Project, 2025. "LLM06:2025 Excessive Agency." OWASP Top 10 for LLM
       Applications. — Directly on point. Names "excessive functionality" as a root cause and gives
       as its canonical example an agent that needs only to *read* documents from a repository but
       whose extension also carries modify/delete capability. Also states that generic open-ended
       tools (shell command runners, broad URL fetchers) "introduce unnecessary risk" and should be
       replaced by narrowly scoped, purpose-specific tools. `git` in a read-only analysis agent is
       precisely the pattern OWASP flags.
    2. MiniScope authors, 2025. "MiniScope: A Least Privilege Framework for Authorizing Tool
       Calling Agents." arXiv:2512.11147. — Argues least privilege must be automatically and
       rigorously enforced over tool-calling agents by reconstructing permission hierarchies over
       tool calls; premised on the claim that agents routinely hold capabilities beyond task need.
    3. SafeHarness (authors not captured in snippet), 2026. "SafeHarness: Lifecycle-Integrated
       Security Architecture for LLM-based Agent Deployment." arXiv:2604.13630. — Classifies every
       registered tool into risk tiers (read_only, write, execute, network, destructive) and
       enforces least privilege at the tool-execution boundary. Supports the specific move of
       separating a read_only grant from an execute grant, which is what `git` straddles.
    4. Overprivilege analysis of serverless policies, 2026. "Overprivilege Analysis of Security
       Policies in Serverless Cloud Applications." arXiv:2607.02875. — Empirical scale of the
       problem in an adjacent domain: 538,390 effective permissions granted against 1,896 actually
       required (~99.65% reduction potential; median 9 granted vs 1 required). Establishes that
       "why is this capability here at all?" is a well-founded question, not pedantry.
    5. "The 2026 Infrastructure Identity Survey," cited in secondary sources (nhimg.org). —
       Reports a 17% incident rate for least-privileged AI access vs 76% for over-privileged
       systems. SEEN ONLY AS A SECONDARY SNIPPET; primary methodology not inspected. Treat as
       suggestive, not established.

  Strength of support: Strong

  Summary: The normative literature is unambiguous and the claim maps onto a named, catalogued
    anti-pattern. OWASP LLM06 treats "capability held but not required by the task" as a
    vulnerability class in its own right, independent of whether harm has yet occurred, and its
    worked example (read access to a repository accompanied by unneeded modify/delete power) is
    almost a description of the item under review. Multiple 2025-2026 agent-security frameworks
    (MiniScope, SafeHarness, AgentWarden, ALPS) are built on the premise that agent tool grants are
    routinely wider than task need and that the gap is worth closing mechanically. Quantitative
    work in the adjacent serverless domain shows over-privilege of two orders of magnitude is the
    norm rather than the exception. The specific normative claim — a read-only analysis agent has
    no business holding a VCS capability — is therefore well supported by established practice.

  Caveats: (a) The literature is overwhelmingly *normative and architectural*; the direct empirical
    incident-rate evidence for privilege narrowing specifically in LLM agents is thin, and the one
    number found (17% vs 76%) came from a survey seen only at snippet depth in a vendor-adjacent
    outlet. (b) Almost all of it is framed around *security* harm — prompt injection, blast radius,
    irreversible action. `git log` / `git diff` is a read operation; the security frame supports
    denying `git` as a *binary* capability but does not by itself establish that read-only VCS
    queries are harmful. The literature's own remedy for this is the narrowly-scoped-tool
    principle: the answer it implies is not "no VCS" but "a read-only VCS-history tool, not the
    `git` binary." (c) The context carried from intake — that the out-of-scope call produced the
    run's only verified follow-through finding — is a *utility* consideration that this security
    literature does not weigh at all. Least-privilege sources optimise blast radius, not
    information yield, and none of the sources found address the case where the out-of-scope
    capability was the productive one. That tension is real and is left standing by this search.
    (d) The 99.65% serverless figure transfers only loosely: cloud IAM permission counts are not
    commensurable with an agent's tool list.

  Recommendation: SUPPORTED
