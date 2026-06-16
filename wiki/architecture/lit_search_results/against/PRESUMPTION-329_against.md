SEARCH-AGAINST-PRESUMPTION-329:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-329
  Original statement: Scrubbing the working tree discharges a public-exposure concern, leaving git history, published copies, and the underlying capability unexamined.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-329
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference from de-BOSCO scrub workflow (2026-06-09 EOD run): the operative belief "working-tree scrub = concern discharged" was never stated but was acted upon
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Meli, M., McNiece, S., Reaves, B., 2019. "How Bad Can It Git? Characterizing Secret Leakage in Public GitHub Repositories." NDSS. — Empirical at-scale study: leaked secrets persist in history and are harvested within minutes; removal from the working tree provides no remediation once content has been public.
    2. GitHub Docs, "Removing sensitive data from a repository." — Working-tree deletion leaves the data in every prior commit, in forks, cached views, and PR references; full remediation requires history rewrite (git-filter-repo/BFG), reflog expiry, garbage collection, collaborator rebases, and Support-mediated cache purges — none of which a tree scrub performs.
    3. Internet Archive removal guides (Vondran Legal; Lowcock, 2024-2025). — Published copies persist in Wayback and third-party caches after source removal; purge is discretionary, slow, and frequently incomplete: "published copies" is an independent exposure surface that scrubbing cannot reach.
    4. GitGuardian, "Remediate a leak on public GitHub." — Industry doctrine: once exposed, treat the material as compromised; remediation means invalidating what was exposed (rotation, disclosure decision), not deleting visible instances. Deletion-only response is a recognized anti-pattern ("security through description removal").
  Strength of challenge: Strong
  Summary: The presumption's embedded operative belief — that scrubbing the working tree discharges the concern — is contradicted by the entire secret-leakage remediation literature, which the 14b framing itself anticipates. Three surfaces survive a tree scrub untouched: (1) version-control history, where every scrubbed string remains retrievable from prior commits; (2) published/distributed copies (archives, caches, mirrors, any previously shared copy of the HTML), which are outside the author's write access; (3) the underlying capability or fact the strings described, which remains true and re-derivable regardless of textual removal — removing operational narration is description-hiding, not exposure reduction. Standard doctrine inverts the burden: exposed content is presumed compromised until each surface is positively cleared.
  Specific risks: Concern is closed in C2A2's records while the exposure persists; the gap is worst-case invisible — future contributors trust the closed status and republish or build on the artifact; if the scrubbed content identified a person or live capability, the identification survives in history/archives indefinitely.
  Mitigations available: Surface-by-surface audit checklist (history: git log -S across all repos; published copies: Wayback/cache lookup of every URL the artifact was served from; capability: explicit decision whether the described capability itself needs changing); history rewrite where needed; reclassify the item as "working tree remediated; surfaces X/Y/Z pending" instead of discharged.
  STEELMAN:
    Strongest counterargument: Proportionality. The leak literature concerns credentials with automated adversaries; this concern involves narrative strings in a personal project whose realistic audience is tiny. If the artifact was never in a public git remote and never crawled, the working tree may genuinely be the only exposure surface, making the scrub complete in fact even though the reasoning ("tree scrub = done") was unsound in general. Cheap partial remediation now can also beat expensive perfect remediation never.
    What would need to be true for C2A2 to be safe: No public remote ever contained the strings; no served URL was ever crawled or archived; the underlying capability/fact is benign if inferred; these are verified, not assumed.
    How to test: Run the surface audit: git log -S "bosco" in every repo touching the file; Wayback CDX query for any URL the visualization was hosted at; search engines for cached copies. Empty results convert the discharge from presumption to verified fact.
  Search scope: "secrets removed from repository remain in git history caches mirrors incomplete redaction incident"; "deleted web content persists Internet Archive wayback machine caches removal ineffective security through obscurity" (2 searches, shared with ASSUMPTION-299 domain); plus Meli et al. 2019 from established literature.
  Recommendation: CHALLENGED
