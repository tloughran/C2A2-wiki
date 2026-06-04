SEARCH-AGAINST-ASSUMPTION-121:
  Date searched: 2026-05-14
  Original item: ASSUMPTION-121
  Original statement: "Twilio SMS one-tap signed link is chosen phone-confirmation mechanism for external-escalation gating (NOT reply-keyword)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-121
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from external-escalation gating design
      15b: Searched for counter-evidence on SMS-vs-alternative-modality for asynchronous approval flows
    Current status: CHALLENGED

  Sources:
    1. NIST SP 800-63B (2017+) — SMS demoted from "OTP authenticator" recommendation due to SIM-swap, SS7 interception, and porting fraud; restricted to lower assurance levels.
    2. SIM-swap fraud research (FBI IC3 reports 2020-2024) — SIM-swap is a well-documented attack vector for high-value SMS-mediated authorizations.
    3. PagerDuty / Opsgenie design patterns — push notification with cryptographic device-key is the canonical modern out-of-band approval channel.
    4. Email-magic-link / WebAuthn passkey patterns (2022-2025) — these mechanisms avoid SMS's structural fragilities.
    5. PRESUMPTION-154 paired — modality-comparison gap.

  Strength of challenge: Moderate

  Summary: SMS as a security-relevant authorization channel has been formally demoted by NIST and is associated with documented attack vectors (SIM-swap, SS7). Modern push-notification with device-bound cryptographic keys, email magic links, and WebAuthn passkeys avoid these issues. The mechanism choice (SMS-link vs. SMS-reply-keyword) optimizes the wrong axis — the underlying medium is the security concern. Moderate challenge.

  Specific risks: (a) SIM-swap attack on high-value escalations; (b) SS7 / SMS-interception; (c) Twilio dependency / outage; (d) Modality lock-in if a better channel is needed later; (e) Cost-per-message scaling.

  Mitigations available: (a) Use push notification with device-bound key; (b) Bind SMS approval to a low-stakes-only scope; (c) Two-channel confirmation for high-stakes actions; (d) Modality-portable approval abstraction.

  Recommendation: CHALLENGED (Moderate) — SMS-mediated approval is acceptable for low-stakes only; modality-comparison and threat-model gaps are load-bearing

  STEELMAN:
    Item: ASSUMPTION-121
    Strongest counterargument: SMS has been formally demoted by NIST for security-relevant authorization. SIM-swap and SS7-interception are documented attack vectors. Push-with-device-key, email-magic-link, and WebAuthn passkeys are the canonical modern alternatives and avoid SMS's structural fragilities. The "SMS-link vs. SMS-reply-keyword" framing optimizes the wrong axis — within-SMS UX rather than across-modality security posture. The decision should explicitly state the assurance level being targeted and the threat model, and should select a modality fit for that level.
    What would need to be true for C2A2 to be safe: (a) Assurance level explicitly low; (b) High-value escalations routed to a non-SMS channel; (c) Modality-portable abstraction so the SMS choice is reversible.
    How to test: Articulate threat model; classify external-escalation events by stakes; test push/email-magic-link alternatives.


---

SEARCH-AGAINST-ASSUMPTION-121 (RE-TRIGGER cycle 1):
  Date searched: 2026-05-25
  Original item: ASSUMPTION-121
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c] (cycle 1)
    Original item: ASSUMPTION-121
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..0: prior search/disposition cycles (see blocks above)
      15d (2026-05-24): re-triggered on weekly cadence (MONITOR-126 cycle 1)
      15b (cycle 1, 2026-05-25): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: On-cadence c2a2-lit-search-pipeline processing of the 2026-05-24 15d weekly RE-TRIGGER cohort (15d fired on schedule 2026-05-24; normal hand-off into the daily pipeline, not an exceptional drain).

  New evidence weighed: No new challenging literature surfaced since the last cycle. Prior cycles' findings stand; item remains in its established disposition until new operational evidence (from C2A2's own runs) or new external literature alters the picture.
  Sources (new / refreshed): No new sources this cycle.
  Strength of challenge: Unchanged from prior cycle.
  Summary: Cycle-1 refresh confirms the prior cycle's finding; the challenging literature base has not materially shifted. Recommendation carries forward unchanged.
  Caveats: Automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven scan or operational evidence from C2A2's own runs is the more sensitive signal for status change.
  Specific risks: Unchanged from prior cycle.
  Mitigations available: Unchanged from prior cycle.
  Recommendation: refreshed; carry forward prior recommendation


---

SEARCH-AGAINST-ASSUMPTION-121 (RE-TRIGGER cycle 2):
  Date searched: 2026-06-01
  Original item: ASSUMPTION-121
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-121
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..1: prior search/disposition cycles (see blocks above)
      15d (2026-05-31): re-triggered on weekly cadence; next_check 2026-05-31 elapsed
      15b (cycle 2, 2026-06-01): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-05-31 (weekly cadence fired on time; next_check 2026-05-31 elapsed). Unlike the 2026-05-17 run, there is NO overdue 15d-schedule backlog — this is a normal on-cadence refresh.
  Landscape check: Automated landscape spot-check this cycle (3 genuine web searches across distinct clusters: passwordless/one-tap-link & SMS-auth security; Levin-Hoffman-Kastrup idealist convergence; multi-agent LLM systems instantiating research traditions/consensus). All three reaffirmed prior for/against profiles; no material literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new challenging literature has surfaced in the past week. The prior cycles' challenge profile stands.
  Evidence-trajectory note (security cluster): challenge REAFFIRMED — FBI/CISA 2025 guidance against SMS-only authentication and 2026 regulatory deadlines to retire SMS OTP (UAE Mar-2026, Philippines Jun-2026) continue to support the existing challenge that signed-link/SMS integrity is not by itself a sufficient security primitive (AiTM/replay/SIM-swap surfaces remain). This is continuation of the prior cycle's challenge profile, not a new-this-week reversal; no automated flip to REVISE — remains human-review territory.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-2 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted; no new disconfirmatory sources surfaced during this automated cycle.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  STEELMAN: Carried forward from prior cycle (no new counterargument surfaced this cycle; strongest prior challenge stands as previously recorded).

  Recommendation: refreshed; carry forward prior recommendation (refreshed; carry forward prior recommendation)
