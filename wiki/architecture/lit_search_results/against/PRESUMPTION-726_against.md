SEARCH-AGAINST-PRESUMPTION-726:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-726
  Original statement: That anti-sweep warnings are per-case cautions; three consecutive days, three sweeps, three independent warnings against generalising a determinate repair — jointly evidence that the id space is not a namespace and that no keyed bulk edit is safe by construction, while a vault-wide sweep stands authorised-pending. NOTE: compounds PRESUMPTION-701 (High, 08-06).

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-726
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: counted three independent instances of one warning and asked what they measure jointly
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Wikipedia, "Name collision" — formally: identifiers must be unique within a scope; collisions arise precisely when previously separate spaces are merged or treated as one, which is the definition of assuming a namespace where none exists.
    2. "Unsafe at Any Copy: Name Collisions from Mixing Case Sensitivities" (arXiv:2211.16735) — empirical study showing real-world systems suffer correctness and security failures specifically because an identifier space was assumed unique/well-formed and was not; collisions were latent until a bulk/automated operation exposed them.
    3. blog.httrack.com, "Compiler-error-abuse-based large scale renaming in C++" — describes why practitioners doing large-scale identifier renaming deliberately avoid blind find-and-replace: they first rename to a verified-unique intermediate token and let the compiler surface every collision before committing, treating "the identifier space is safe to bulk-edit" as an assumption requiring proof, not a default.
    4. Lightrun, "Why Blast Radius Analysis Does Not End When Alerts Fire" — argues blast radius should be treated as a continuous, re-verified property of an action rather than a one-time approval, which cuts directly against treating a single "authorised-pending" bulk sweep as safe once granted.

  Strength of challenge: Moderate-to-strong

  Summary: Software-engineering practice around bulk/automated identifier edits converges on the same lesson these three warnings are pointing at: an id space that has never been proven collision-free should be treated as unsafe for blind bulk edits by default, and mature tooling (IDE rename refactorings, compiler-error-abuse renaming) exists specifically because blind find-and-replace on "unique" keys repeatedly turns out not to be safe. Three independent warnings against generalizing a determinate, per-case repair are consistent with — not incidental to — this literature: each warning is a local detection of the same global property (no proof of uniqueness), and treating them as three unrelated per-case cautions discards exactly the signal the pattern-across-warnings literature would flag as diagnostic.

  Specific risks: Authorizing a vault-wide keyed sweep while three prior sweeps independently warned against generalization risks a collision-driven mass-corruption event — the software-engineering equivalent of a blind find-and-replace hitting an unexpected duplicate identifier and silently overwriting or misapplying a repair vault-wide. This compounds PRESUMPTION-701, suggesting the risk was already flagged once and not structurally closed.

  Mitigations available: Require a positive proof of id uniqueness (e.g., an automated collision scan) before any keyed bulk edit is authorized, not merely the absence of a new warning; adopt a compiler-error-abuse-style two-phase rename (rename to a verified-unique intermediate, then commit) for any vault-wide sweep; treat blast radius as continuously re-verified rather than a one-time "authorised-pending" gate.

  STEELMAN:
    Item: PRESUMPTION-726
    Strongest counterargument: Refactoring tooling exists precisely because "this identifier space is unique enough to bulk-edit safely" is a claim that experienced systems refuse to take on faith — they either prove it computationally or engineer around never needing it (compiler-verified intermediate renames). Three independent warnings in three consecutive days are not three coincidental local cautions; under standard collision-detection logic they are three positive detections of the same absent proof of uniqueness. Proceeding with a vault-wide sweep on "authorised-pending" status, without addressing why the warnings recurred, repeats the exact failure mode the arXiv case-sensitivity collision study documents: latent collisions that stay invisible until an automated, large-scale operation exposes them all at once.
    What would need to be true for C2A2 to be safe: The id space would need either a verified proof of global uniqueness (a completed collision scan with zero hits) or the sweep would need to be restructured as a two-phase, verifiable operation (stage to an intermediate unique marker, verify, then commit) rather than a single-pass keyed bulk edit.
    How to test: Before authorizing the pending vault-wide sweep, run an exhaustive collision scan across the full id space and require zero unexplained duplicates as a precondition; alternatively, run the sweep in dry-run/staged mode first and diff against the determinate per-case repairs already validated.
