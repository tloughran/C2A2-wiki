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
