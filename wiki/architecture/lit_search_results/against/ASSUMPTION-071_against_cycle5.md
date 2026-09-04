SEARCH-AGAINST-ASSUMPTION-071:
  Date searched: 2026-09-04
  Original item: ASSUMPTION-071 (MONITOR-070), priority MEDIUM-HIGH
  Original statement: "Browser-authentication on the user's behalf is an agent-prohibited /
    explicit-permission action."
  Reframe under test: "user-credential-entry is agent-prohibited; pre-issued tokens /
    pre-authenticated profiles are explicitly permitted under defined scope and audit."
  Cycle: monthly re-check cycle 5 (15d re-trigger of 2026-07-05)

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c -> 15d -> 15b (cycle 5)]
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted directly from stated policy text prohibiting credential entry and gating
           authentication-adjacent actions behind explicit permission.
      15b: Searched for challenging literature on BOTH the original framing and the proposed
           reframe (cycle 5 re-check).
    Current status: PARTIALLY-CHALLENGED

  Queries run this cycle:
    1. "browser agent prompt injection authenticated session hijack 2026 security research"
    2. "confused deputy OAuth token replay agentic AI non-human identity over-scoped credentials 2026"
    3. "consent fatigue habituation security warnings click-through approval rubber-stamping human-in-the-loop agent approvals"
    4. "OAuth consent phishing illicit consent grant attack 2026 malicious app scope"
    5. "AI agent audit log attribution gaps non-repudiation agent actions indistinguishable from user 2026"
    6. "empirical study OAuth scopes over-privileged apps request more permissions than needed measurement"
    7. "pre-authenticated browser profile agent session riding risk persistent cookies agentic browsing isolation"
    8. "security policy overly restrictive workarounds shadow AI users bypass controls credential sharing noncompliance"
    9. "user study approving AI agent actions users approve harmful requests oversight failure empirical 2026"

  Challenging evidence found: Yes - but ASYMMETRICALLY. The evidence challenges the REFRAME much
    more than it challenges the ORIGINAL. Essentially no credible support was found for the view
    that the original prohibition is over-broad, and substantial evidence was found that the
    reframe's "pre-issued tokens and pre-authenticated profiles are safe" premise is false as
    stated.

  Sources:
    A. Against the reframe - tokens / pre-auth profiles are not safe substitutes:
    1. LayerX Security, 2026-06-24. "BioShocking" indirect prompt injection class, reported via
       Cloud Security Alliance research note (labs.cloudsecurityalliance.org, 2026-06-30).
       [VERIFIED BY 15c 2026-09-04 - disclosure date, vendor, mechanism and affected products
       confirmed across LayerX, CSA, The Hacker News, SecurityWeek and TechRepublic.] - Compromised
       six AI-powered browsers and extensions - ChatGPT Atlas, Comet, Fellou, Genspark Browser,
       Sigma Browser and Claude Chrome - steering each into copying a user's SSH credentials out of
       an AUTHENTICATED GitHub session and delivering them to an attacker-controlled page. This is
       the direct refutation of the reframe: the agent never entered a credential, yet credentials
       were exfiltrated, BECAUSE the agent held a live authenticated session. "Pre-authenticated" is
       not a weaker capability than "credential entry"; here it is the ENABLING capability.
       15c ADDITION (found during verification, not by 15b): LayerX's own recommended mitigation is
       that AI browsers should ASK BEFORE READING FROM LOGGED-IN ACCOUNTS - one prompt, "I'm about
       to copy data from your GitHub repository. Continue?", would break the chain. That is
       ASSUMPTION-071's explicit-permission clause, recommended independently by the researchers who
       found the attack. Also: vendor responses varied - OpenAI fixed Atlas; Anthropic's patch to
       its Claude extension DID NOT HOLD per LayerX; Perplexity closed the report without acting;
       three vendors never replied. C2A2 runs in one of the affected environments.
    2. Palo Alto Networks Unit 42, March 2026 (via the CSA note and Dark Reading, "No Perfect Fix
       for AI Browser Prompt Injection Flaws"). - Web-based indirect prompt injection observed
       against PRODUCTION AI agents, not proof-of-concept. Delivery: visible plaintext 37.8%, HTML
       attribute concealment 19.8%, CSS render suppression 16.9%; social-engineering framing
       (authority claim, game rule, override signal) present in 85.2% of successful jailbreaks -
       exactly the injection pattern C2A2's instruction-source boundary is written to resist.
    3. OpenAI, 2026-02-13 - Lockdown Mode for ChatGPT, with public acknowledgement that prompt
       injection in AI browsers "may never be fully patched" (via Dark Reading and the CSA note;
       primary post NOT retrieved). - A vendor with every incentive to claim the problem is solved
       stating that it is not. Under this premise "under defined scope and audit" cannot be
       sufficient for an agent holding a live session, because the containment assumption fails.
    4. Consent-phishing / token-durability reporting: Microsoft Entra blog, "OAuth consent phishing
       explained and prevented"; Obsidian Security, "Consent Phishing: How OAuth Attacks Bypass MFA
       and Traditional Security Controls." - A single consent grant yields durable access to mail,
       files, calendar and SaaS data with no credentials and no MFA prompt; password resets do not
       revoke it; compromised tokens commonly remain valid 60-90 days. 15b flagged specific 2026
       incident numbers (EvilTokens 340+ M365 orgs; Storm-1286; "ConsentFix") as UNCORROBORATED
       vendor-blog claims. The STRUCTURAL point - a pre-issued token is a longer-lived,
       harder-to-revoke, MFA-bypassing artefact than a password - is corroborated across independent
       sources.
    5. Over-scope in practice: arXiv:2608.02336, "Lost in Permissions: Exploring the Microsoft 365
       App Ecosystem" (>8,000 apps analysed); Help Net Security 2026-06-04, "OAuth marketplace apps
       keep access after publishers vanish"; 677 apps requesting at least one permission exceeding
       stated function across ~1.82bn installs, 266 reaching Drive with off-purpose high-tier access
       (~1.26bn installs); Felt/Chin-lineage Android results (~65% of Google Play apps
       over-privileged); Decoupled-IFTTT (arXiv:1707.00405: 122 of 128 channels offer only
       all-or-nothing authorization despite 106 having multiple distinct triggers/actions). -
       "Defined scope" is a thing systems fail at empirically and at scale, and in many cases the
       platform does not expose a scope granular enough to define. The strongest challenge to the
       reframe's "under defined scope" clause.
    6. Attribution gap: Cloud Security Alliance study, March 2026, via Kiteworks ("AI agent audit
       trail compliance: the attribution gap") and nhimg.org; arXiv:2510.25819, "Identity Management
       for Agentic AI." - More than two-thirds of organisations cannot distinguish AI agent actions
       from human actions in audit and access logs. If the agent rides a pre-authenticated profile,
       its actions are BY CONSTRUCTION attributed to the human. The reframe's two safeguards -
       "defined scope" and "audit" - are precisely the two properties that pre-authenticated
       profiles destroy.
    7. Confused-deputy framing: Obsidian Security, "AI Agent Credential Management: Preventing
       Confused Deputy"; nhimg.org, "Scoped credentials for AI agents"; digitalapplied.com. - An
       agent reusing a user's OAuth token inherits the user's full entitlement set; the correct
       construction is the INTERSECTION of the user's permissions and the agent's allowed
       capabilities, never the union. A pre-authenticated browser profile is the union by default.
       Practitioner sources, not peer-reviewed.
    8. Session isolation guidance: witness.ai "AI Browser Agents: 6 Enterprise Security Risks
       (2026)"; browserless.io; Praesidia; nhimg.org. - Converge on the recommendation that a
       browser agent must NOT use a daily profile, saved passwords, persistent cookies or personal
       extensions, and should get a fresh context per task. This is a recommendation AGAINST the
       reframe's "pre-authenticated profiles are explicitly permitted" as a general permission - it
       is permitted only under per-task isolation, a much narrower carve-out than the reframe's
       wording.
    9. arXiv:2506.17318 ("Context manipulation attacks: Web agents are susceptible to corrupted
       memory"); arXiv:2602.09222 (MUZZLE); arXiv:2512.12594 (ceLLMate); arXiv:2606.05233
       ("Domain-Conditioned Safety in Frontier Computer-Using Agents: A 793-Episode Browser
       Benchmark... and a Reproducibility Audit of Recent Red-Teaming"). - The last is flagged by
       15b for its own sake: it includes a REPRODUCIBILITY AUDIT of recent red-teaming work,
       suggesting the field's headline attack-success numbers may not all replicate. 15b did not
       read it and could not say which results it questions.

    B. Against the original framing being over-broad - weak:
   10. Shadow-AI literature: The Hacker News 2026-05, "5 Steps to Managing Shadow AI Tools";
       arXiv:2606.00088, "From Frontier to Shadow AI." - The argument that prohibition merely
       relocates risk. 15b judges this a WEAK challenge because the analogy does not transfer:
       shadow AI concerns ORGANISATIONS RESTRICTING HUMANS, who route around the control. C2A2's
       prohibition binds the agent itself, which cannot route around it. The only transferable
       residue is that a too-restrictive agent may push the USER toward less-supervised tools -
       real, but second-order.
   11. "Human oversight of agentic systems in practice," ACM FAccT 2026, doi 10.1145/3805689.3812402
       (arXiv:2606.05391). Interview study, n=17 experienced developers; four forms of emergent
       oversight work. AUTHOR LIST NOT DETERMINABLE from search results; cited by title/DOI only.
   12. Approval-fatigue evidence: arXiv:2605.11360, "Options, Not Clicks: Lattice Refinement for
       Consent-Driven MCP Authorization"; tianpan.co 2026-07-07, "The Approval Prompt Nobody Reads";
       habituation literature summarised there (fMRI evidence that neural response to a repeated
       warning drops measurably after the second viewing); Gravitee "State of AI Agent Security
       2026" (vendor survey, methodologically unverified). - THE GENUINE CHALLENGE to the
       EXPLICIT-PERMISSION half of ASSUMPTION-071. Uniform confirmation gates train click-through.
       Reported case: a team gated every above-threshold agent action, within two months had 200+
       daily review requests with reviewers batching approvals, and six months later "a near-perfect
       approval rate and almost no real oversight." The critical observation: if 99% of requests are
       fine the human behaves as if 100% are, "and the failure is invisible in audit logs."

  NEW SINCE LAST CYCLE: Substantial - this is the item where the April-2026 baseline is most out of
    date. New since April: LayerX BioShocking (2026-06-24) and the CSA note (2026-06-30); Help Net
    Security (2026-06-04); arXiv:2608.02336 (Aug 2026); arXiv:2606.05233; arXiv:2606.05391 / FAccT
    2026; arXiv:2605.11360 (May 2026); tianpan.co (2026-07-07). At or just before the baseline:
    Unit 42's March 2026 production-attack report, the CSA March 2026 attribution study, and OpenAI
    Lockdown Mode (2026-02-13). The direction of travel since April is uniformly AGAINST relaxing
    the prohibition.

  Strength of challenge: Strong against the REFRAME; Weak against the ORIGINAL.

  Summary: The reframe's core premise - that pre-issued tokens and pre-authenticated profiles are a
    safe substitute for credential entry - is contradicted by the 2026 evidence. BioShocking shows
    an agent holding a live authenticated session exfiltrating SSH credentials without ever entering
    one, which INVERTS the reframe's risk ordering. Its two safeguards are the two things that fail
    hardest in practice: "defined scope" is defeated by measured over-privilege across every
    ecosystem studied and by platforms that do not offer granular scopes at all; "audit" is defeated
    by the finding that two-thirds of organisations cannot separate agent actions from human ones in
    their logs - a pre-authenticated profile makes agent actions attributable to the human by
    construction. Separately, the explicit-permission half of the original assumption is genuinely
    weakened by habituation evidence: uniform gates degrade into rubber-stamping and the degradation
    is invisible in audit logs. No credible evidence was found that the prohibition on credential
    entry is over-broad.

  Specific risks: If the reframe were adopted as written, C2A2 would grant itself standing authority
    over a live session whose scope is the user's full entitlement set, whose actions are logged as
    the user's, and whose revocation means locking the user out. Every hostile web page the agent
    reads then becomes an instruction channel into that authority - the exact confused-deputy
    condition, and the observed BioShocking outcome. Separately, if explicit-permission gating is
    C2A2's load-bearing control and gate volume is high, the control is probably already degraded
    and the system has no signal that it is: high approval rates read as user endorsement rather
    than as habituation.

  Mitigations available:
    (a) Keep the original prohibition intact; do not adopt the reframe as written.
    (b) If any pre-authenticated capability is permitted, scope it as: fresh browser context per
        task, no daily profile, no saved passwords, no persistent cookies, no personal extensions.
    (c) Enforce intersection-not-union permissions: effective authority = user's permissions
        INTERSECT agent's declared task capabilities.
    (d) Give the agent a distinct non-human identity so its actions are separately attributable; use
        short-lived, audience-bound, sender-constrained tokens (DPoP) so a stolen token is not
        replayable.
    (e) Against habituation: make gates non-uniform and rare, reserve them for irreversible actions,
        vary their presentation, and INSTRUMENT THE APPROVAL RATE ITSELF as a health metric - a
        near-100% approval rate is evidence the gate has stopped working, not that it is working.
    (f) Exclude high-value destinations (finance, HR, admin, control planes) from any live-cookie
        traversal regardless of gating.

  STEELMAN:
    Strongest counterargument: A blanket prohibition on all browser authentication is not what makes
      the system safe - what makes it safe is that the agent has no standing authority and every
      consequential action is individually gated. If that is true, the credential-entry prohibition
      is doing symbolic rather than causal work, and the reframe's instinct is right: the meaningful
      distinction is between STANDING authority and PER-ACTION authority, not between credentials
      and tokens. Under this reading, a short-lived, single-audience, per-task token with an
      agent-specific identity is strictly safer than either the status quo or credential entry,
      because it is revocable without locking out the user and separately attributable in logs. The
      reframe is directionally correct about the mechanism and merely underspecified about the
      conditions.
    What would need to be true for C2A2 to be safe: (i) any token is per-task, short-lived,
      audience-bound and sender-constrained, not a standing grant; (ii) it is issued to a distinct
      agent identity so audit attribution is preserved; (iii) the browser context is fresh per task
      with no inherited cookies or saved credentials; (iv) the scope is genuinely expressible at the
      granularity of the task - which requires checking the actual platform, since the IFTTT result
      shows many platforms only offer all-or-nothing; and (v) the explicit-permission gate is rare
      enough that habituation has not set in, which is measurable.
    How to test: Two cheap checks. FIRST, on habituation: count the explicit-permission prompts C2A2
      has issued over the last N sessions and compute the approval rate. If it exceeds ~95%, the
      gate is a formality and the assumption's protective claim is already false - existing logs
      only. SECOND, on attribution: pick one authenticated action the system might plausibly take
      and inspect the destination service's audit log to see whether the entry is distinguishable
      from a user-initiated one. If not, the reframe's "and audit" clause is unsatisfiable on that
      service today - a per-service finding, not a policy-wide one.

  METHODOLOGICAL NOTE (15b): sources were encountered in search results this run at title, URL and
    abstract level; full texts were NOT fetched and arXiv IDs were not independently resolved.
    Several IDs postdate 15b's background knowledge entirely and are recorded as seen, not as
    verified-by-retrieval. A large share of the agentic-security material is vendor blogs and
    industry surveys; these are separated inline. Specific incident numbers (EvilTokens 340+ orgs,
    Storm-1286, "ConsentFix", the Gravitee 88%/19.7% figures) are single-source vendor claims that
    could NOT be corroborated and should not be relied on. The structural claims - token durability,
    MFA bypass, over-scope, attribution gaps, habituation - are corroborated across independent
    sources and are the load-bearing part. Isolation maintained: lit_search_results/for/ was not
    read.

  Recommendation: PARTIALLY-CHALLENGED
    (Original framing: NO-CHALLENGE-FOUND on over-breadth; weak PARTIAL challenge to the
    explicit-permission half via habituation. Reframe: CHALLENGED - should not be adopted as
    written, though a heavily-conditioned version survives.)
