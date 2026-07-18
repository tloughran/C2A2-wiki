SEARCH-FOR-PRESUMPTION-463:
  Date searched: 2026-07-10
  Original item: PRESUMPTION-463
  Original statement: "Platform pause policy is stable and a synthetic query is a trustworthy activity proxy — the keep-warm loop needs no outcome verification."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-463
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inference from 2026-07-09 EOD cohort
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. IBM, 2024–2025. "What is Synthetic Monitoring?" ibm.com/think. — Establishes synthetic transactions as an accepted, mainstream proxy for real user activity: scripted agents simulate user interactions on a schedule and are treated as valid activity signals "24/7 regardless of whether real users are active." Supports the proxy half of the presumption.
    2. Catchpoint, current. "Synthetic Transaction Monitoring." catchpoint.com. — Industry guide treating synthetic transactions as sufficient stand-ins for real activity for availability purposes; notes synthetic monitoring exists precisely because real-user signals are absent when no users are active — the exact gap a keep-warm query fills.
    3. travisvn, 2024–2026. "supabase-pause-prevention." GitHub. — Documents the exact design in question (scheduled trivial query, no outcome verification loop) as a widely adopted, working community pattern for this exact platform; its sustained use is practitioner evidence that the open-loop design is adequate in practice for this low-stakes purpose.
    4. Supabase, 2026. "Project Pausing." Official docs. — The policy has been stable in its essentials (7-day low-activity window, database activity as criterion, warning email before pause, 90-day restore) across 2024–2026 practitioner writeups and current docs, supporting the "policy is stable" clause. The warning email itself acts as an out-of-band backstop that reduces the need for in-loop verification.

  Strength of support: Moderate (synthetic query as activity proxy; policy stability to date); Weak (no outcome verification needed)

  Summary: Two of the three clauses find real support. Synthetic transactions are an industry-standard proxy for genuine activity — an entire monitoring discipline is built on the premise that scripted interactions validly exercise a system on behalf of absent users — so treating a scheduled query as "activity" aligns with both monitoring practice and Supabase's own definition (database queries count). The pause policy has been observably stable across multiple years of documentation and community writeups, and Supabase's warning-email-before-pause plus 90-day restore window mean the failure mode of a silently broken keep-warm loop is cushioned by vendor-side backstops: a failed loop leads to a recoverable pause preceded by notice, not data loss. This low-consequence profile is the strongest available argument that the loop "needs no outcome verification" — verification effort should be proportional to failure cost.

  Caveats: No literature affirmatively endorses open-loop (unverified) keep-alive as best practice; support for the no-verification clause is inferential (low stakes + vendor backstops), not doctrinal — monitoring literature generally runs the other way (dead-man's-switch/heartbeat-check patterns exist because scheduled jobs fail silently). Policy stability to date is inductive: vendors change free-tier terms without notice, and the docs' "sufficient activity" hedge leaves Supabase discretion. The warning-email backstop only works if someone reads the email.

  Search scope confidence: comprehensive for synthetic-monitoring practice; preliminary for open-loop keep-alive as an endorsed design

  Recommendation: PARTIALLY-SUPPORTED
