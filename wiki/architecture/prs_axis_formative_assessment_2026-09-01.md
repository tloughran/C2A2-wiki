# Formative Assessment — the Narrative (PRS) Connectome, 2026-09-01

*Run at Tom's direction, in Cowork, on branch `claude/prs-visualization-test-8e37fb`. Not pushed.*
*Status: **findings + shipped fixes**. Evaluated against [[architecture/narrative_prs_connectome|the connectome model]], which is architecturally guiding.*

## What was done

A test corpus was built to be **structurally known in advance and deliberately unlike the live one**, then pushed through the unmodified production pipeline. Twenty landmark results — quantum mechanics 1900–1932 and deep learning 2012–2025, from Karpathy's domino image — written as full PRS triplets in each tradition's own vocabulary, with no tuning for word overlap, plus six hand-authored cross-connections stating the correspondences the image asserts.

The image is a good probe because it carries four separable claims: two distinct traditions; each a cascade; a structural correspondence between them; and a compression — the second cascade covers comparable ground in 13 years against 32. The instrument either draws each claim or it does not.

**It drew the first and got the other three wrong.**

The fixture lives at `wiki/c2a2-prs-3d/testcorpus/` and rebuilds with `scripts/regen_prs_testcorpus.sh`. It is a fixture, not vault content — these are not C2A2 research programs and they are deliberately outside the live corpus and its counts.

## Findings

**1 — The vertical axis inverted the comparison.** At the shipped `TAU_DAYS = 90`, thirteen years of deep learning received 22.66 column units and thirty-two years of quantum mechanics received 1.66. A reader trusting the axis concludes deep learning took longer. Decade labels 1900–1990 collapsed into an unreadable band, so the axis could not be used to check that impression either. On the linear control the same twenty narratives give 0.290 units per year each — parity to three decimals.

**2 — All six coils rendered as NaN, silently.** `ordToZ` took `log(1 + age/τ)`; a coil dated after the newest triplet has negative age, and once the gap exceeded τ the argument went negative. Six arcs were built, marked visible, given NaN vertices, drawn as nothing, and counted in the legend as six. The live build escaped only by accident of dating. The model's own directive — a coil sits where its bridging insight formed — puts coils at the newest point in the system, which is exactly the case that failed.

**3 — Automatic cross-tradition discovery found nothing, and cannot.** `gen_chains` scores word overlap between one narrative's solution and another's resource. Across all 200 cross-tradition pairs the best score was 0.061 on the tokens *plus* and *self*. The correspondences here are real and structural; the two traditions share no technical vocabulary. Word overlap is blind in precisely the case where finding a fiber is worth something. The same flaw, stricter, sits in the convergence-hub key: a shared resource requires 60 identical leading characters, so twenty resources produced twenty keys and zero hubs.

**4 — An empty generative layer failed validation and aborted the build.** `validate_prs_3d.py` returned 0.0 rather than *not applicable* for an empty array, and under `set -e` the regen wrapper stops. Any corpus whose traditions do not share vocabulary could not be built at all.

**5 — Two smaller ones.** Cross-tradition arcs took their endpoints from the *tradition* (first resource mesh of each) rather than from the finding, so N findings over one pair drew N identical lines. And the triplet counter sat on its placeholder until the first filter toggle.

**6 — The standing check had drifted from the template again.** `prs_axis_max_share.py` computed `rendered` as a linear map on ordinals while the template had been logarithmic since 2026-08-27 — the exact drift its own docstring warns about. It reported the right number anyway, because max_share is invariant under monotonic transforms. A check that cannot be wrong in the way it drifted is not thereby a good check.

## The generalizable lesson

`max_share` asks whether nodes land on the **same** level. It is tie-counting, and every monotonic transform preserves ties. So an axis that discriminates perfectly and is still unreadable — one tradition spread over the column, another pressed into a mat — scores healthy at every value of τ. The metric was fixed at the axis's previous failure and is structurally blind to this one.

**`rate_spread`** asks the other question: how many column units does each tradition get per year it actually spans? On an honest axis those rates sit within a small factor of each other; a linear axis gives exactly 1.00 by construction, so the floor is provable rather than asserted. It is added alongside `max_share`, not in place of it — the two fail apart, which is the whole point.

Measured: **34.89×** on the fixture at τ = 90, **1.00×** on its linear control, and **5.41×** on the live corpus, where MacIntyre receives 0.62 units per year and Loughran 3.34. The live picture was never reported as unhealthy by anything.

This is the same family as the frozen Level-2 signal stream and the metabolism lag gate that could only fail in one direction: **an assertion that cannot fail in the direction the system actually breaks reads as evidence of health.** The remedy each time is a second question asked off a different quantity, not a tighter threshold on the first.

## What changed in the code

- `ordToZ` clamps the ordinal to the corpus range before the log. Kills the NaN class.
- `generate_prs_3d.py` takes `--tau <days|linear>`; the default is unchanged, so the live build is untouched. It now prints the corpus baseline and warns when a corpus spanning more than five years is being rendered at the 90-day constant.
- `prs_axis_max_share.py` ports the real transform (reading `TAU_DAYS` out of the artifact so it cannot drift again) and adds `rate_spread`, with `--check` failing at 4.0.
- `validate_prs_3d.py` distinguishes an empty layer from an unpopulated one, and reports coils sitting past the newest triplet as a **warning** — the clamp handles them, but the altitude is then a ceiling, not a placement.
- `extract_prs_data.py` takes `--thinker-map` so a fixture can declare its own traditions without editing the live colour and discipline maps.
- The template calls `updatePrsCount()` at init, and draws one cross arc per tradition pair.

## What is deferred, and why

- **τ as a live slider with a two-handle age window.** [[SPEC_prs_time_axis_2026-08-27|The spec]] specifies it and warns that the meshes, threads, labels, coils and decade furniture are all built once with baked vertex positions. Bolting a slider on without reposition machinery would produce a control that moves nothing. `--tau` at build time is the honest interim.
- **Replacing lexical matching** in `gen_chains` and the hub key with embedding similarity or a model-scored analogy pass. This is the one item that is a project rather than a patch — and it is the half the model calls the point: *coils are not decoration; they are association fibers.*
- **A genuine `source_date`** carried from proposal frontmatter, still absent on every node.

## The method itself

The thing worth keeping is not the four defects. It is that **a fixture built to be unlike the corpus found in one pass what months of green gates did not.** Freshness checks ask whether the producer ran. Integrity checks ask whether the artifact parses. Neither asks whether the picture still means what the model says it means, and that question appears to need an adversarial corpus — one whose structure is known in advance, so that a wrong rendering is legible as wrong.

## Connections

Sits with [[architecture/narrative_prs_connectome|the narrative connectome model]] it is answerable to, and with [[traditions/loughran/prs_triplets|Loughran PRS-10 through PRS-12]], where the assessment enters the connectome it assesses — the self-documentation the model's third directive calls for. Read beside [[architecture/assumptions|the assumptions register]]. The side-by-side view is `wiki/prs_connectome_compare.html`: the live corpus in one pane, the fixture in the other with its axis switchable.
