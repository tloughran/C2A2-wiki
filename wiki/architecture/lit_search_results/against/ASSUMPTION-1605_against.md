SEARCH-AGAINST-ASSUMPTION-1605:
  Date searched: 2026-09-22
  Original item: ASSUMPTION-1605
  Original statement: "A headline with a bare figure goes stale silently; a note ending `New
    total N, ratio R` cannot." Record shape, not author or band, determines whether staleness is
    detectable.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-1605
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted a format-level finding about self-invalidating records.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Kelly Sutton (2017), "Comment Drift" — describes how source-adjacent, self-referential
       annotations (comments living next to the code they describe) still silently desynchronize
       from reality, precisely because their proximity gives false confidence they're accurate.
       Directly analogous to a `New total N, ratio R` note: proximity/self-description does not
       by itself prevent silent staleness if nothing forces the note to be recomputed when the
       underlying total changes.
    2. GitHub issue thread, "documentation-and-adrs: no mechanism for detecting doc/code drift"
       (addyosmani/agent-skills #511, 2026) and Fiberplane Blog, "We built a linter for
       documentation rot" — establish that structured, provenance-carrying documentation
       (including examples that literally state derived values) still goes stale unless an
       active mechanism (CI check, linter, recomputation trigger) enforces consistency; the
       Fiberplane piece exists specifically because "self-documenting" text artifacts (code
       examples, worked figures) were found silently stale in practice at scale (23% of analyzed
       repos had stale code-element references per a cited study). This directly challenges the
       word "cannot": a `New total N, ratio R` note goes stale exactly like a bare figure if N or
       R is never recomputed against the current source — the note's shape makes staleness
       *detectable in principle* (a reader could recompute and compare) but does not make it
       *self-preventing*, and nothing in the claim's mechanism forces that check to happen.
    3. GitHub issue, "A quiet dataset's published `derived_from` never refreshes after a lineage
       change" (CannObserv/usa-wa #388) — a concrete real-world case of a provenance-labeled,
       structured record (analogous to "New total N, ratio R") going stale silently because nothing
       re-validated the derived value against its source after the source changed; the record's
       self-documenting shape did not prevent silent staleness in practice, only made staleness
       theoretically recoverable by someone who bothered to check.

  Strength of challenge: Moderate to Strong (against limb 2's "cannot"); Weak (against limb 1)

  Summary: Limb 1 ("bare figure goes stale silently") is essentially uncontested — nothing in
  the literature disputes that an undated, unattributed number decays invisibly. Limb 2's use
  of "cannot," however, overstates what a self-documenting shape achieves. The documentation-rot
  and comment-drift literature shows repeatedly that format alone (having the derivation spelled
  out inline) does not prevent silent staleness — it only creates the *possibility* of detecting
  staleness if an active agent (linter, reviewer, recomputation step) exploits that shape. Without
  such an active check, a `New total N, ratio R` note is just as capable of silently going stale
  as a bare figure; it merely fails more legibly *once someone looks*. The claim conflates
  "detectable in principle by a motivated reader" with "cannot go stale silently," which the
  drift/rot literature treats as two different things.

  Specific risks: If C2A2 treats provenance-carrying record shapes (e.g., `New total N, ratio R`)
  as self-policing and therefore deprioritizes active staleness checks on them, it inherits
  exactly the failure mode documentation-rot tooling was built to catch: structured,
  self-referential records that look trustworthy precisely because of their shape, while quietly
  diverging from the current source of truth.

  Mitigations available: Pair the self-documenting shape with an active recomputation/consistency
  check (the linter/CI pattern from Fiberplane) rather than relying on shape alone; treat "N,
  ratio R" as a detectability aid for reviewers, not a staleness-prevention guarantee.

  Search scope: Preliminary — 2 searches (code comment/documentation drift; provenance/lineage
  staleness in data records). Did not search domain-specific literature on financial/accounting
  self-documenting figures (e.g., footnoted totals in audited reports) which might bear more
  precisely on the "note ending in a computed ratio" case.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1605
  Strongest counterargument: "Cannot" is a claim about impossibility, but the drift/rot
  literature shows the actual failure mode is about enforcement, not shape: self-documenting
  records go stale silently all the time in practice (comment drift, stale doc examples, unrefreshed
  lineage fields) whenever nothing actively recomputes and checks them. The shape makes staleness
  auditable by an interested party; it does not make staleness self-announcing or impossible, which
  is what "cannot go stale silently" implies.
  What would need to be true for C2A2 to be safe: There would need to be an active, automatic
  process that recomputes N and R from current source data and flags divergence — at which point
  the record's shape is doing real preventive work rather than just latent detectability. Absent
  that automation, the claim should be softened to "a note ending in a derived figure is more
  readily auditable for staleness than a bare figure, but not immune to it."
  How to test: Take a sample of `New total N, ratio R`-style notes from the corpus, recompute N
  and R against current source data without relying on anyone having flagged a problem, and
  measure how many have silently diverged — if any have, "cannot" is empirically false.

SYSTEMIC-RISK-FLAG:
  Date: 2026-09-22
  Affected items: ASSUMPTION-1598, ASSUMPTION-1600, ASSUMPTION-1605
  Common vulnerability: All three claims license a binary/absolute inference (uniform verdict =
  broken; shared blind spot = "not validated"; self-documenting note = "cannot go stale") from a
  structural/formal property of a record or measurement, without requiring an independent,
  active check. In each case the literature found shows the formal property (uniformity, control
  independence, self-description) is necessary-but-not-sufficient — real systems fail silently or
  produce ambiguous signals unless something actively verifies against ground truth. If C2A2
  encodes any of these as hard rules rather than heuristics requiring corroboration, it
  systematically under-invests in active verification wherever a record's shape merely *permits*
  detection rather than *guaranteeing* it.
  Literature basis: Vaughan 1996 (normalization of deviance); common-method-bias reviews
  (Podsakoff et al. 2022); comment-drift/documentation-rot literature (Sutton 2017; Fiberplane
  2026; GitHub issue corpora on doc/lineage drift).
  Risk level: High
  Recommendation: Wherever C2A2 relies on a structural signature (uniformity, control-set
  agreement, record shape) as a proxy for correctness or staleness-immunity, require a paired
  active verification step rather than treating the structural signature as self-certifying.
