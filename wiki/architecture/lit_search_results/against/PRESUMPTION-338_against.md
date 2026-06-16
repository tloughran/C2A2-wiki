SEARCH-AGAINST-PRESUMPTION-338:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-338
  Original statement: The Chat⇄Cowork sync loop's restoration is durable — one success after eight days of failure re-establishes operational reliance, with lapse and recovery causes both unknown.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-338
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference (reliance resumed on one observed success; no root cause for either lapse or recovery)
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Beyer, Jones, Petoff & Murphy (eds.), 2016. "Site Reliability Engineering." O'Reilly. — Postmortem doctrine: an incident is not closed without an understood mechanism; "resolved without identified cause" incidents are tracked as open risks precisely because unexplained recoveries carry the original failure's full recurrence probability.
    2. Reason, 1990. "Human Error" (latent-failure / Swiss-cheese model). Cambridge UP. — Unexplained recovery typically means the latent condition persists and an unobserved alignment changed; the system has returned to the same trajectory that produced the failure, not to a safer one.
    3. OpsAtScale, "Root Cause Analysis and Postmortem: A Guide to Learning from Incidents." — Practice guidance: where root cause is unknown, plan further investigation and monitoring before restoring full reliance; "smooth restoration" without monitoring invites "cascading relapses."
    4. NXLog, "Watching the watchers." — Identifies credential/session expiry and silent config drift as classic causes of multi-day quiet outages that "recover" on a re-auth or update cycle — i.e., periodic mechanisms whose signature is exactly an unexplained lapse followed by an unexplained recovery, and which recur on the same period.
  Strength of challenge: Strong
  Summary: Reliability literature treats this presumption's structure — unknown failure cause, unknown recovery cause, single post-recovery success, restored reliance — as the textbook setup for recurrence. With both causes unknown, the hypothesis "periodic latent mechanism (token/session expiry, background update cycle, quota window)" is at least as likely as "fixed," and the eight-day duration is itself weak evidence of a cyclical mechanism. One success is a sample of n=1 from a process whose failure mode was silent; it bounds availability estimates at essentially nothing. The presumption's risk is not technical but operational: workflows re-anchor on the loop (cross-context state passing, scheduled handoffs), so the next silent lapse inherits a larger blast radius than the first.
  Specific risks: Silent recurrence during a critical multi-day sequence (e.g., a lit-search cycle or dyad pass) with work products stranded in one context; no detection until a human notices absence (cf. 336 — absence is already ambiguous in this system); accumulated reliance means the second outage costs more than the eight-day first one.
  Mitigations available: Daily heartbeat message through the loop with an alert-on-miss convention (turns silent failure into detected failure within 24h); keep a manual fallback path documented and exercised; log timestamps of any future lapse/recovery to test the periodicity hypothesis; cap criticality of what the loop carries until a cause is identified or a month of heartbeats accumulates.
  STEELMAN:
    Strongest counterargument: For a consumer-platform dependency, root cause is genuinely unobtainable — the lapse was plausibly a vendor-side defect fixed by a vendor-side deploy, which is both the most common explanation for spontaneous recovery in managed services and one under which the fix IS durable. Withholding reliance pending an impossible root-cause analysis would idle a working capability; rational practice is to resume use while watching.
    What would need to be true for C2A2 to be safe: The cause was vendor-side and patched; the loop's failure mode stays detectable quickly (someone notices within a day); no critical-path workflow depends on the loop without a fallback.
    How to test: Institute the heartbeat for 30 days — sustained success converts n=1 into a real availability estimate; any miss timestamps the recurrence and tests the expiry-cycle hypothesis (e.g., lapse at ~same interval).
  Search scope: 1 WebSearch ("incident resolved on its own unknown root cause recurrence self-healed reliability engineering postmortem unexplained recovery"); plus SRE/latent-failure canon.
  Recommendation: CHALLENGED
