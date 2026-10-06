SEARCH-FOR-ASSUMPTION-071:
  Date searched: 2026-09-04
  Original item: ASSUMPTION-071 (MONITOR-070), priority MEDIUM-HIGH
  Original statement: "Browser-authentication on the user's behalf is an agent-prohibited /
    explicit-permission action"
  Proposed reframe under test (MONITOR-070's stated INCORPORATE condition): "user-credential-entry
    is agent-prohibited; pre-issued tokens / pre-authenticated profiles are explicitly permitted
    under defined scope and audit."
  Cycle: monthly re-check cycle 5 (15d re-trigger of 2026-07-05)

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c -> 15d -> 15a (cycle 5)]
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-04-27 daily run - Cowork<->Chat sync attempt blocked by browser
           auth-gap; restated directly from operating policy.
      15a: Searched for supporting literature (cycle 5 re-check), both halves of the reframe
    Current status: SUPPORTED

  Queries run this cycle:
    1. "OAuth 2.1 delegated authorization AI agents on-behalf-of flow scoped tokens 2026 specification"
    2. "browser agent credential entry prompt injection security risk autonomous agents passwords 2026"
    3. "NIST SP 800-63B authenticator shall not be shared claimant possession verifier impersonation delegation"
    4. "OpenID Foundation identity assurance for agentic AI working group 2026 agent delegation standard"
    5. "agent governance policy prohibit agent entering user passwords require human in the loop authentication step-up"
    6. "OWASP agentic AI security top 10 2026 identity spoofing credential handling controls"
    7. "'Overlaying Governance' compositional authorization framework delegation scope agentic AI arxiv 2606.03518"
    8. "audit log immutable delegation chain agent action attribution accountability requirement 2026"

  Supporting evidence found: Yes - for the prohibition half. See 15c's correction on the
    substitute half.

  Sources:
    HALF (a) - prohibition on agents handling user credentials:
    1. OWASP Top 10 for Agentic Applications 2026 (published 2025-12-09; genai.owasp.org). - ASI03
       "Identity & Privilege Abuse" is a named top-10 risk covering exploitation of delegated trust,
       inherited credentials and role chains. Prescribed controls: per-agent identity, short-lived
       task-scoped credentials, auto-expiring scopes, access reviews.
    2. Wiz, "Agentic Browser Security: 2025 Year-End Review" (wiz.io/blog), summarising Unit 42
       reporting. - In-the-wild web-based indirect prompt injection by March 2026; audits of
       Perplexity's Comet browser in which agents executed injected commands that exfiltrated user
       credentials and OTPs with no malware. The empirical case for the prohibition.
    3. "Mind the Web: The Security of Web Use Agents." arXiv:2506.07153. - Systematises the web-use
       agent threat surface.
    4. Ping Identity, "IAM Best Practices for AI Agents" (pingidentity.com). - States the design
       rule directly: prompt the human out-of-band so that "human users are not required to provide
       credentials to the agent." Vendor guidance, not peer review.
    5. NIST SP 800-63B (pages.nist.gov/800-63-3/sp800-63b.html). - Supports INDIRECTLY:
       verifier-impersonation resistance requires channel binding, and AAL3 requires proof of
       possession and control by the claimant. NO explicit 800-63 clause on agent delegation was
       found; this use is inferential and is labelled as such.

    HALF (b) - legitimacy of scoped, audited, pre-issued token substitutes:
    6. Ibrahim, A. & Li, Y. 2026. "Overlaying Governance: A Compositional Authorization Framework
       for Delegation and Scope in Agentic AI." arXiv:2606.03518 (posted 2026-06-02). - Delegation
       types with permission and accountability semantics plus "resource scope attenuation."
    7. OpenID Foundation AuthZEN Working Group Drafts, 2026 (openid.net). - AARP (Access Request and
       Approval Profile) and COAZ (AuthZEN Profile for MCP Tool Authorization) approved as official
       WG DRAFTS, not final specifications. Plus the OpenID Connect Authority Claims Extension.
    8. RFC 8693 (Token Exchange) and RFC 8707 (Resource Indicators) as applied in the MCP
       authorization spec, via 2026 practitioner sources. RFC numbers surfaced in search results;
       the RFCs themselves were NOT opened this run.
    9. "AI Identity: Standards, Gaps, and Research Directions for AI Agents." arXiv:2604.23280
       (2026-04-28).
   10. "Auditable Agents." arXiv:2604.05485; "Authorization Propagation in Multi-Agent AI Systems."
       arXiv:2605.05440. - Audit trails should carry the delegation chain, correlation IDs and
       immutable time-synchronised records.
   11. Cloud Security Alliance, Agentic Identity Governance Framework v1. - Four unconditional
       human-in-the-loop triggers, including any request to create or modify another agent's
       identity or credentials.

  NEW SINCE LAST CYCLE: Substantial - this is the item where the April-2026 baseline is most out of
    date. OWASP Top 10 for Agentic Applications 2026 (Dec 2025) is now the reference framework;
    arXiv:2606.03518, arXiv:2605.05440, arXiv:2604.23280, arXiv:2604.05485 and the OpenID AuthZEN
    AARP/COAZ drafts all postdate or sit at the baseline. The empirical credential-theft incidents
    are new evidence, not new theory. The item has moved from "reasonable policy position" to
    "converging standards consensus" in one cycle.

  Strength of support: Strong (prohibition half). See 15c's correction below on the substitute half.

  Summary: The prohibition half rests on a named OWASP 2026 top-10 risk category (ASI03), on
    documented in-the-wild attacks in which browsing agents were induced by injected page content to
    exfiltrate credentials and OTPs, and on the structural argument that an agent operating against
    untrusted web content can be manipulated for as long as it holds credentials in context. The
    substitute half is actively standardised: RFC 8693 token exchange under OAuth 2.1, OpenID
    Connect Authority Claims, AuthZEN AARP and COAZ drafts, per-agent identity with short-lived
    narrowly-scoped tokens, scope attenuation as a formal primitive. The best-practice formulation
    found - keep credentials out of the model entirely, resolve them at the browser layer, use
    out-of-band human authentication - is close to a verbatim statement of the reframe.

  Caveats:
    - Much of the strongest-worded support is vendor and practitioner material with a commercial
      interest in "delegated tokens, not passwords." The arXiv layer supports the same conclusion
      with more hedging.
    - NIST SP 800-63 contains no explicit agent-delegation clause; the use here is inferential.
    - FLAGGED AGAINST OWN BRIEF by 15a: the reframe permits pre-authenticated profiles, but the
      browser-agent confused-deputy finding applies to exactly those. Pre-authenticated profiles are
      safer than credential entry but NOT risk-free, and "under defined scope and audit" is doing
      real load-bearing work. A long-lived pre-authenticated profile with broad scope would not
      clear the bar.
    - arXiv preprints are not peer-reviewed; the AuthZEN items are working group DRAFTS.

  15c CORRECTION APPENDED 2026-09-04 (not a 15a finding; recorded here so the file is not read in
    isolation): 15a's "Strong" for half (b) is an assessment of what the STANDARDS PRESCRIBE, not of
    what deployments ACHIEVE. 15b's independent search found the deployment evidence, and it
    inverts the risk ordering for pre-authenticated profiles specifically. 15a's own caveat above
    anticipated this. The prohibition half stands at Strong; the substitute half is downgraded.
    See ASSUMPTION-071_against_cycle5.md and DISPOSITION-895.

  Recommendation: SUPPORTED (prohibition half; substitute half qualified by 15c - see above)
