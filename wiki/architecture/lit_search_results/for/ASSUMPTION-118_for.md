SEARCH-FOR-ASSUMPTION-118:
  Date searched: 2026-05-13
  Original item: ASSUMPTION-118
  Original statement: "Token-based delegation workflow redesign for chat-scrape sign-in barrier now operationally warranted (6 consecutive failed days; PREMISE-015 explicit redesign-required caveat)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-118
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-12 EOD 6-consecutive-day chat-scrape failure pattern + PREMISE-015 operational caveat
      15a: Searched for OAuth / connector-based delegation patterns for chat-UI scraping replacements and file-based-handoff alternatives in inter-app sync architectures
    Current status: SUPPORTED

  Sources:
    1. Hardt (2012) RFC 6749 "The OAuth 2.0 Authorization Framework" — token-based delegation is the canonical replacement for password-handling in cross-service action; OAuth scopes provide the consent model PREMISE-015 endorses.
    2. NIST SP 800-63B "Digital Identity Guidelines" — password delegation is explicitly out-of-pattern; token-based delegation is the recommended path.
    3. OWASP ASVS v4.0.3 §2.1 / §3 — credential-handling boundaries; tokens and connectors are the recommended delegation pattern when an intermediary must act on user behalf.
    4. Anthropic Model Context Protocol (MCP) connector documentation (2025-2026) — MCP connectors with OAuth flows are the canonical Claude-platform mechanism for delegated access; this is the operating C2A2 environment.
    5. C2A2-internal: PREMISE-015 (INCORPORATEd 2026-05-11; ASSUMPTION-105 → user-privacy no-password-delegation binding constraint) explicitly states the workflow that surfaced the constraint must be redesigned around token-based delegation, not relaxed. 6 consecutive failed days operationalizes the "must be redesigned" caveat.

  Strength of support: Strong

  Summary: Token-based delegation as replacement for password-handling is unambiguously endorsed by canonical authentication literature (NIST, OWASP, OAuth RFC) and is the operating Anthropic platform mechanism (MCP connectors). PREMISE-015 (INCORPORATEd two days prior) explicitly named workflow redesign around token-based delegation as the load-bearing follow-up; ASSUMPTION-118 operationalizes that commitment now that the 6-consecutive-day failure pattern makes the operational warrant unambiguous. This is the cleanest "follow-through on PREMISE commitment" the registry has produced so far.

  Caveats: (a) PRESUMPTION-145 (this cycle, paired, MEDIUM-HIGH) — token-delegation is one redesign path; file-based-handoff and mechanism-discard are alternatives that ASSUMPTION-118 frames as parenthetical. The "warranted" framing presumes redesign rather than replacement; (b) Implementation cost not estimated — token-based redesign has authentication-flow integration cost that may be substantial relative to the chat-scrape value-delivered, raising mechanism-discard as a serious option; (c) "6 consecutive failed days" operational signal is consistent with prior PRESUMPTION-125 cluster (4th-recurrence per ASSUMPTION-109 MONITOR-111); substrate-decomposition gate (PRESUMPTION-134 REVISE) still load-bearing — if substrate is shared, the redesign may not be the local problem; (d) MEDIUM-HIGH priority, joint with PRESUMPTION-145 + ASSUMPTION-109 + PRESUMPTION-125; reads jointly.

  Recommendation: SUPPORTED — PREMISE-015 commits the system to this redesign; canonical authentication literature endorses the path; the load-bearing risks are the redesign-vs-replacement decision (PRESUMPTION-145) and the unresolved substrate-decomposition (PRESUMPTION-134), not the warrant itself
