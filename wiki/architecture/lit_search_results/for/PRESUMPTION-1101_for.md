SEARCH-FOR-PRESUMPTION-1101:
  Date searched: 2026-10-01
  Original item: PRESUMPTION-1101
  Original statement: Escalation-to-human designs need a policy for reviewer absence (expiry, default action, or batching); otherwise queues grow without bound.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1101
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across 09-30 sessions.
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. TianPan.co, 2026-05-17. "When No One Answers the Escalation: Human-in-the-Loop Is a Staffing Problem". https://tianpan.co/blog/2026/05/17/when-no-one-answers-the-escalation — reviewer absence, timeouts, default actions; queues grow without bound when load exceeds capacity. [fetched; practitioner blog]
    2. Beyer et al., 2016. SRE book ch. 6 — pager-fatigue: humans can react urgently only a few times a day. [fetched]
    3. AWS Well-Architected Agentic AI Lens, AGENTSEC04-BP02 "Human-in-the-loop for critical decisions". — vendor HITL guidance. [search-snippet]
    4. Cloudflare Agents docs, "Human-in-the-loop patterns". — approval-pattern documentation. [search-snippet]

  Strength of support: Moderate

  Summary: Practitioner literature states directly that escalation designs need timeout, default-action and batching policies. Queueing theory grounds the unbounded-growth claim; SRE alert-fatigue guidance supports the human-capacity limit. Best sources are practitioner/vendor material, not peer-reviewed.

  Caveats: Mostly 2026 blogs and vendor docs. Queue growth depends on arrival rate relative to capacity; not guaranteed in low-volume systems.

  Search scope: preliminary search — broader search recommended (web-only; practitioner and vendor sources dominate; no peer-reviewed primary studies located for the specific claim; fetched pages were passed through a summarizing model, so wording is paraphrase).

  Recommendation: SUPPORTED
