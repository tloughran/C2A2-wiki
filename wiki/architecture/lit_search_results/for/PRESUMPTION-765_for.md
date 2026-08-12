SEARCH-FOR-PRESUMPTION-765:
  Date searched: 2026-08-12
  Original item: PRESUMPTION-765
  Original statement: [inferred] That a channel's silence is the same as its emptiness — thirteen dark sync days read downstream as thirteen quiet days.

  Claim as tested here (polarity note): the tested proposition is the CORRECTIVE converse — that absence of signal and absence of content are distinct states which a pipeline must distinguish, and that a channel unable to signal its own failure will have its outages silently recoded downstream as low activity. Support counts against the presumption as stated.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-765
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from thirteen consecutive dark sync days appearing downstream as thirteen quiet days — i.e. an outage converted into a substantive reading with no marker at the boundary. Risk graded High. The thirteen-day run is a strong signal; a single dark day would be ambiguous.
      15a: Searched for supporting literature on the corrective proposition
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Structural versus sampling zeros in contingency-table analysis (standard categorical-data doctrine; surfaced this session via arXiv:2511.05755, "Bounding interventional queries from generalized incomplete contingency tables"). — The formal distinction C2A2 needs and lacks. A structural zero is a cell that *cannot* be occupied and "can be cut out from the contingency table as it has no degrees of freedom associated"; a sampling zero is an empty cell that could have been occupied. Conflating them misstates the model's degrees of freedom and therefore its uncertainty. Thirteen dark days are structural zeros being modelled as sampling zeros. [distinction canonical; the specific arXiv source unverified — from search snippet]
    2. Rubin, D.B., 1976. "Inference and missing data." Biometrika 63(3):581-592. — MNAR: when missingness depends on the unobserved value, treating absence as observation biases inference irrecoverably. A dark channel is the extreme case, since the probability of a null is 1 regardless of the underlying value. [canonical; cited from domain knowledge]
    3. Prometheus/Alertmanager empty-versus-zero problem and the dead man's switch (ilert docs; oneuptime 2026-02-06). — The clearest operational statement of the identical error at the metric layer: a query over a vanished time series "does not return zero, it returns empty," and alerting systems that treat empty as no-data create silent outages. The recommended architecture is a layered one — collector-level heartbeats, per-service data-freshness checks, and an external dead man's switch — because no single layer can distinguish silence from emptiness on its own. [unverified — from search snippets; vendor documentation]
    4. Structural health monitoring missing-data literature (Sciencedirect S0263224124004135, "Missing measurement data recovery methods in structural health monitoring: The state, challenges and case study"; Nature Sci Rep s41598-025-98374-5, "Restoration of multi-channel signal loss using autoencoder with recursive input strategy"). — A whole subfield exists because sensor dropout from "sensor aging, circuit faults, unstable power supply" produces channel silence that must not be read as zero load on the structure. The engineering consequence is direct and physical: reading a dead strain gauge as zero strain is how you miss the failure you installed it to catch. Strong analogous support. [unverified — from search snippets]
    5. "Missingness as Signal: Channel-Independent Spectrogram Learning for Clinical Time Series Prediction." arXiv:2607.02938. — "The presence or absence of a measurement often reflects a clinical decision, patient severity, or treatment context... a model that treats missing values only as noise to impute may discard part of the clinical signal." Supports the stronger reading: the thirteen-day pattern is not merely a gap to be flagged, it is itself the most informative datum in the window. [unverified — from search snippet]
    6. Practitioner data-quality literature on default imputation (Medium/Rajput, "11 ML pipeline failures caused by 'helpful' default imputation"). — Names the mechanism by which the recoding happens: "someone adds a default imputation rule like zero, empty string, median, or 'Unknown'. The pipeline politely hides missingness and turns a data quality problem into a modeling problem." The word "politely" is the whole finding — the conversion is invisible at the point of use. [unverified — from search snippet; grey literature]

  Strength of support: Strong

  Summary: The corrective proposition is supported across four independent fields — categorical statistics, missing-data theory, production monitoring, and structural health monitoring — with the same conclusion each time and, in the monitoring case, the same phrasing. The distinction between "no signal" and "signal of nothing" is treated everywhere as foundational, not as a refinement; the SHM case is the most vivid analogue because there the confusion has physical consequences. Monitoring practice has also converged on the shape of the fix: silence cannot be detected from inside the silent channel, so detection must come from an independent liveness signal or a freshness check evaluated by a different component. That is a structural requirement, and it means no amount of care inside the sync process can close this gap. The imputation literature explains why the error is hard to notice after the fact: the recoding happens silently at a boundary and the downstream reader sees a well-formed low number.

  Caveats: (a) Every source is analogical. Categorical statistics and SHM concern numeric measurement; C2A2's channel carries documents. The principle transfers; the remedy's parameters (how many dark days before escalation, what a freshness threshold should be) do not follow from anything found here. (b) The strongest operational sources are vendor documentation. (c) The item's downstream half — that the thirteen dark days were actually *read* as quiet days by some consumer — is an inference about reader behaviour that literature cannot corroborate; it needs evidence from C2A2's own downstream artefacts. (d) This item is closely coupled to PRESUMPTION-772 (null result as measurement) and PRESUMPTION-777 (self-reported inputs); the three share a single root — no independent liveness channel — and reconciling them separately risks triple-counting one defect. I flag that for 15c/15d rather than resolving it.

  Search scope: Comprehensive on structural-zero/MNAR theory and on the empty-versus-zero monitoring pattern. Moderate on structural health monitoring as an analogue. Preliminary on document-pipeline-specific channel-failure signalling, where I found only grey literature.

  Recommendation: SUPPORTED (for the corrective proposition; equivalently, NO-SUPPORT-FOUND for the presumption that silence equals emptiness)
