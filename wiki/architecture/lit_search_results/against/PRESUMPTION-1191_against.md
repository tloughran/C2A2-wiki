# PRESUMPTION-1191 — Literature Search AGAINST (15b)

Search scope: PRELIMINARY. Broader search recommended. Scheduled run 2026-10-28 (lock held by parent). Budget for this item: 1 web search (standard) of its own, 0 fetches; I also reuse the adversarial-collaboration search run for ASSUMPTION-1952 (counted there). I did not open lit_search_results/for/ or lit_search_returns.md.

Reading of "challenge": this item is a concern. Following the template convention (PRESUMPTION-1190), I search against the presumption as 14b states it: that "mature members" of each tradition are identifiable, reachable and independent, and that the gate is passable as designed. Evidence that sign-off gates stall without reviewer capacity therefore counts as a challenge to the presumption (and is consistent with 14b's concern). I did not verify the in-house facts (77 candidates, no named certifier, WATCH-003 at 23 checks).

```
SEARCH-AGAINST-PRESUMPTION-1191:
  Date searched: 2026-10-28
  Original item: PRESUMPTION-1191
  Original statement: "[inferred] The candidate-certification rule (DECISION-084) presumes that
    'mature members' of each tradition are identifiable, reachable, and independent of the
    outputs they certify. Today 77 physicalist-dialogue candidates were minted with no named
    certifier on either side ... Is the gate passable as designed?"
  Claim tested: Who counts as a competent/mature practitioner, and how do cross-paradigm
    validation schemes recruit certifiers? Do dual-sign-off gates stall without capacity
    planning?

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1191
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from DECISION-084 and the 77 uncertified candidates.
      15b: Searched for challenging literature (preliminary; 1 own search + 1 shared, 0 fetches)
    Current status: SEARCHED-15b — PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. "Code Review Analytics: WebKit as Case Study" (IFIP, hal-01373050). [snippet only]
       — Direct analogue. Required review "could cause delays in contributions being accepted,
       and risk to become a bottleneck if not enough reviewers are available." A sign-off gate
       is limited by reviewer supply, not by the rule.
    2. Meta Engineering (2022, "Improving code review time at Meta") and arXiv 2312.17169
       (reviewer recommendation at Meta). [snippet only]
       — Boundary condition. Developer dissatisfaction tracked the slowest 25% of reviews, so
       Meta adopted P75 time-in-review as its metric. Better reviewer routing cut tail latency
       for one recommender but did not significantly change overall review cycle time, and a
       workload-balancing recommender showed no significant change. Routing work to reviewers
       does not create reviewer capacity.
    3. Adversarial-collaboration reports (American Scientist; APA Monitor 2025). [snippet only;
       search counted under ASSUMPTION-1952]
       — Recruiting rival practitioners is the hard step. The practice stays rare;
       collaborations are time-consuming, fear of interpersonal conflict keeps people from
       starting, and some fall apart.

  Strength of challenge: Moderate on "passable as designed" (gates with insufficient reviewers
    become bottlenecks). Weak on "identifiable" and "independent": I found nothing on how
    cross-paradigm schemes define or recruit "mature" practitioners. Collins & Evans was not
    searched for this item.

  Summary: The literature I found treats sign-off gates as capacity-limited: when reviewers are
    scarce, the gate becomes the bottleneck, and better routing does not fix a supply
    shortage. Adversarial collaboration, the closest analogue to rival certification, is rare
    because recruiting and keeping rivals engaged is costly. A gate with no named certifier on
    either side has zero capacity, which the literature would predict stalls indefinitely.
    The search did not address what makes a practitioner "mature" or how independence is
    assured.

  Specific risks: The candidate ledger grows without discharge, like WATCH-003. Agents keep
    minting candidates that cannot be counted, so the system's output is unvalidated by its
    own rule. If certifiers are later drawn from people close to the build, independence
    fails silently.

  Mitigations available: Name certifiers before minting candidates, and cap open candidates
    per certifier (work-in-progress limit). Track time-to-certification at the tail (P75/P90),
    not the mean. Define "mature member" operationally (e.g., published in the tradition, not
    involved in the build). Add an expiry or "unresolved" outcome.

  Recommendation: PARTIALLY-CHALLENGED
```

```
STEELMAN:
  Item: PRESUMPTION-1191
  Strongest counterargument: Every documented sign-off gate is limited by reviewer supply,
    and the best-resourced software organisations could not route their way out of tail
    latency. A certification gate with no named certifiers has a capacity of zero; it will not
    "slowly" settle candidates, it will settle none. The system already has a precedent
    (WATCH-003) for human-ruling queues that stall. The rule as written guarantees an
    ever-growing ledger.
  What would need to be true for C2A2 to be safe: named, consenting certifiers exist for both
    traditions; their throughput exceeds the minting rate; and their independence from the
    outputs is defined and checked.
  How to test: Count candidates minted per day against certifications per day over two weeks.
    If the ratio stays above 1 with no certifier named, the gate is not passable as designed.
```

```
SYSTEMIC-RISK-FLAG (candidate):
  Date: 2026-10-28
  Affected items: ASSUMPTION-1952, PRESUMPTION-1191, PRESUMPTION-1192 (new candidate);
    PRESUMPTION-1193, PRESUMPTION-1194 (extend existing 'artefact-as-proof')
  Common vulnerability: (a) New: validation that depends on outside human judges who are not
    named, not resourced, or not independent of the build ("unstaffed or non-independent
    validation gate"). 1952 and 1191 depend on rival certifiers who do not yet exist; 1192's
    rival tradition has no insider judge. (b) Existing 'artefact-as-proof' (1184/1185/1187/
    1188/1189) is extended by 1193 (a commit stamp taken as proof of auditability) and 1194
    (the returned session list taken as proof of what happened that day).
  Literature basis: WebKit code-review analytics (reviewer supply bottleneck); Meta review-
    latency work; adversarial-collaboration reports (rarity, cost); Collins & Evans imitation
    game (insider judges required); Fluxicon / van der Aalst group on unrecorded manual
    activities; CASRAI and PeerJ/Software Heritage on version identifiers. All snippet-level.
  Risk level: High
  Recommendation: Record (a) as a second systemic candidate alongside 'artefact-as-proof'.
    Both share a pattern: the system names a check (certification, stamp, session list) and
    treats its existence as the check having been done.
```

Source quality: all sources are snippets; the Meta and arXiv material is the most rigorous. No source addressed the "mature practitioner" definition.
