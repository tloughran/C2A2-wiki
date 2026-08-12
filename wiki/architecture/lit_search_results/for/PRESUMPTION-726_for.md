SEARCH-FOR-PRESUMPTION-726:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-726
  Original statement: That anti-sweep warnings are per-case cautions; three consecutive days, three sweeps, three independent warnings against generalising a determinate repair — jointly evidence that the id space is not a namespace and that no keyed bulk edit is safe by construction, while a vault-wide sweep stands authorised-pending. NOTE: compounds PRESUMPTION-701 (High, 08-06).

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-726
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: counted three independent instances of one warning and asked what they measure jointly
      15a: Searched for supporting literature
    Current status: SUPPORTED (for the underlying pattern the presumption challenges) / mixed for the "per-case caution" framing itself

  Supporting evidence found: Yes

  Sources:
    1. Heinrich, H.W. (1931/1959). "Industrial Accident Prevention: A Scientific Approach" and the broader near-miss/precursor safety-science literature (e.g., PMC10654148, "Near-miss accidents data analysis and knowledge dissemination in water construction projects," 2023; PMC9140665, "Systematic Literature Review on Indicators Use in Safety Management Practices") [Heinrich citation unverified — classic reference, not directly retrieved this search] — establishes the foundational safety-science principle that near-misses/warnings are not isolated per-incident cautions but precursor signals whose repetition across independent occasions is evidence of a latent systemic hazard, and that treating them piecemeal (rather than aggregating) is a known failure mode ("near miss incidents... are largely ignored because no injury, damage, or loss actually occurred").
    2. Hollnagel, E. — Functional Resonance Analysis Method (FRAM) literature, e.g. PMC12229593, "Risk assessment in sociotechnical systems based on functional resonance analysis method" [unverified — from search snippet] — models systemic risk as emerging from the resonance/coupling of repeated variability across occasions, directly analogous to treating three independent sweep warnings as jointly diagnostic of a structural property (non-namespace id space) rather than three unrelated cautions.
    3. RFC 9562 (UUIDs) and general namespace/collision literature (learncpp.com "Naming collisions and an introduction to namespaces"; USPTO patents on namespace collision management, e.g. US10831380) [unverified — from search snippet] — confirms that "assumption of uniqueness" in identifier schemes is a well-known, recurring class of bug distinct from any single collision instance; the standard engineering response is to prove uniqueness formally (e.g., via UUID/InChI-grade guarantees) rather than infer it from absence of observed collisions.
    4. Blast-radius / dry-run change-management literature (Secoda, "Blast-radius Control"; industry sources noting "over 80% of unplanned IT outages originate from planned changes") [unverified — industry sources] — supports the item's implicit conclusion (no keyed bulk edit is safe by construction without a dry-run/blast-radius gate), reinforcing that mandatory dry-run-with-blast-radius-preview is the standard mitigation once uniqueness cannot be proven.

  Strength of support: Moderate

  Summary: Safety-science literature on near-miss/precursor analysis (Heinrich's tradition and later FRAM-based sociotechnical risk models) directly supports treating three independent, same-shaped warnings as jointly diagnostic of a systemic property rather than as three unrelated per-case cautions — this is close to a textbook case of precursor aggregation. Separately, software/identifier-engineering literature confirms that "false uniqueness" of keyed identifiers is a well-documented, recurring bug class, and that the standard remedy is formal uniqueness proof plus dry-run/blast-radius gating before any bulk keyed operation — which supports the presumption's practical conclusion that no keyed bulk edit is safe by construction absent such proof.

  Caveats: The safety-science analogy is drawn from physical/industrial and sociotechnical-accident domains, not from software identifier namespaces specifically — transfer to "the id space is not a namespace" is inferential, not a direct empirical match. No literature was found that specifically validates "anti-sweep warnings" or vault-scale keyed-ID sweeps as a named phenomenon; this appears to be domain-specific to the C2A2 system, and support here rests on structural analogy rather than a directly on-point study. Search was preliminary — a deeper pass through defect-cascading and near-miss-aggregation empirical studies (with quantitative precursor-ratio data, e.g. Heinrich's original 300:29:1 ratio and its later critiques) is recommended before treating this as comprehensively supported.

  Recommendation: SUPPORTED
