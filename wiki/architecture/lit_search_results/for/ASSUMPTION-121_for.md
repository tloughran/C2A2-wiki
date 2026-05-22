SEARCH-FOR-ASSUMPTION-121:
  Date searched: 2026-05-14
  Original item: ASSUMPTION-121
  Original statement: "Twilio SMS one-tap signed link is chosen phone-confirmation mechanism for external-escalation gating (NOT reply-keyword)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-121
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from external-escalation gating design pass
      15a: Searched for one-tap-link confirmation UX in passwordless-auth and 2FA literature; webhook security patterns
    Current status: SUPPORTED

  Sources:
    1. Magic link / passwordless-auth literature (Auth0, Stytch, Clerk documentation 2023-2025) — one-tap signed-link patterns are standard for asynchronous approval flows.
    2. NIST SP 800-63B — SMS is acceptable for low-to-moderate assurance flows when properly designed; one-tap link reduces typing-error and replay-with-typo risk vs. reply-keyword.
    3. Twilio (2024) "Verify" product documentation — signed-link flows are the recommended pattern over keyword reply for non-interactive confirmation.
    4. OWASP ASVS §3 — signed URLs with short TTL + single-use are recommended for asynchronous user-action gating.
    5. Reply-keyword UX studies (Twilio dev-blog 2023; SendBird 2024) — keyword replies have higher abandon rates and parsing-error rates than one-tap links.

  Strength of support: Strong

  Summary: One-tap signed-link is the dominant pattern for asynchronous user-confirmation flows across passwordless-auth, magic-link, and 2FA literature. Reply-keyword has higher friction and parsing-error rates. Twilio's own product guidance favors signed-link patterns. Strong endorsement of the mechanism choice; the security details (TTL, single-use, signing key handling) are where the implementation work concentrates (paired with PRESUMPTION-153).

  Caveats: (a) SMS deliverability and SIM-swap risk are well-documented SMS-class concerns; (b) PRESUMPTION-153 (paired) — no threat model articulated for replay / key compromise / SMS interception; (c) PRESUMPTION-154 (paired) — alternative modalities (push, email-magic-link, in-cowork-confirmation) not compared.

  Recommendation: SUPPORTED — mechanism choice is well-supported; threat-model and alternative-modality audits are the load-bearing follow-ups
