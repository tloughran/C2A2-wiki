SEARCH-AGAINST-ASSUMPTION-1595:
  Date searched: 2026-09-22
  Original item: ASSUMPTION-1595
  Original statement: "A guideline breached by every instance of a task class, always for the same
    stated reason, no longer distinguishes necessary cost from thrash."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-1595
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Read five same-day declared budget breaches as a population rather than singly.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Vaughan, D. (1996). "The Challenger Launch Decision: Risky Technology, Culture, and
       Deviance at NASA." University of Chicago Press. Coined "normalization of deviance" —
       the process by which repeated, uniform breach of a safety threshold, each time excused
       by the same production-pressure rationale, becomes the accepted norm precisely because
       nothing catastrophic follows. This is the mirror image of the claim: Vaughan's case shows
       a uniform breach pattern is exactly the situation where the guideline should be read as
       still valid (and violated dangerously), not as invalidated by its own uniform breach.
    2. Goodhart, C. (1975, popularized via Wikipedia "Goodhart's law" and Manheim & Garrabrant
       2018 "Categorizing Variants of Goodhart's Law," arXiv). "When a measure becomes a target,
       it ceases to be a good measure." Relevant to the *limit vs. target* distinction named in
       the literature lane: a budget ceiling breached uniformly could indicate the ceiling has
       been adopted as a target to game, rather than evidence the ceiling itself lacks
       discriminating power — a different causal story than "thrash," with different remedies.
    3. Frontiers in Digital Health (2022 systematic review), "Computational approaches to
       alleviate alarm fatigue in intensive care medicine," and PMC3752621 (empiric alarm PPV
       study) — establish that threshold-based alarms are deliberately over-sensitive (high
       sensitivity, low specificity) by design, so a high uniform breach rate is an expected,
       intentional design property, not proof the threshold fails to distinguish real from
       spurious cases. This undercuts the inference step (uniform breach → guideline
       non-discriminating) but does not itself argue the guideline is fine; it only shows one
       plausible design reason breach could be uniform without being "thrash."

  Strength of challenge: Moderate

  Summary: The claim conflates "always breached, always for the same reason" with "no longer
  discriminates." The normalization-of-deviance literature shows the identical empirical
  signature — uniform, repeatedly-excused breach — can instead mark a real risk being tolerated
  away, which is the opposite conclusion from "the guideline is stale/thrash." The alarm-fatigue
  literature shows deliberately over-sensitive thresholds produce high uniform breach rates by
  design, which is a second competing explanation. Goodhart's law adds a third: uniform breach
  under a shared excuse may reflect gaming a limit that has become a target, not the limit's
  irrelevance. None of these decisively falsify the claim in its narrow form ("no longer
  distinguishes necessary cost from thrash") — they establish it is one hypothesis among at
  least three with the same observable signature, and the two most authoritative bodies of
  literature (safety-critical systems, ICU alarms) point toward NOT relaxing the guideline on
  uniform-breach evidence alone.

  Specific risks: If C2A2 auto-relaxes or discounts a budget guideline whenever breaches are
  uniform and same-cause, it recreates the NASA O-ring failure mode: repeated tolerance of a
  real, worsening risk because "it happens every time, for the same normal-sounding reason, and
  nothing bad has happened yet." The claim as stated has no mechanism to distinguish this case
  from genuine over-calibration.

  Mitigations available: Require an independent severity/outcome signal (not just breach
  uniformity) before treating uniform breach as evidence of a bad threshold — e.g., check whether
  the "same stated reason" corresponds to a stable, audited cost driver (supports thrash
  reading) vs. an unaudited/rationalized one (supports normalization-of-deviance reading).
  Track trend, not just cross-sectional uniformity — Vaughan's cases show drift over repeated
  cycles, which a five-instance same-day snapshot cannot see.

  Search scope: Preliminary — 3 targeted searches (normalization of deviance, Goodhart's law,
  alarm fatigue/threshold calibration). Did not exhaustively survey bounded-resource quota
  design literature (e.g., operations research on service-level thresholds) or search for
  direct rebuttals of normalization-of-deviance theory itself.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1595
  Strongest counterargument: The normalization-of-deviance literature (Vaughan 1996) describes
  exactly the surface pattern in the claim — uniform breach, same excuse each time, no
  catastrophe yet — and treats it as the signature of a guideline being correctly restrictive
  but organizationally eroded, the opposite of the claim's conclusion. Because both readings
  ("guideline is stale" and "guideline is being normalized away") produce identical five-instance
  evidence, the claim's inference is underdetermined by the data it relies on.
  What would need to be true for C2A2 to be safe: The "same stated reason" would need to be
  externally auditable and stable (e.g., a fixed, known cost floor for the task class) rather
  than a rationalization that could itself be drifting; and there should be no safety-critical
  consequence riding on the guideline, since Vaughan's cases are specifically ones where cost
  pressure eroded a safety-relevant limit.
  How to test: Track the "same stated reason" against an independent ground-truth cost measure
  over many more cycles (not just one same-day population of five) and check whether the
  rationale's magnitude is stable/audited or itself creeping upward — creep would support
  normalization-of-deviance over thrash.
