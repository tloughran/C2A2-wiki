# Simulated rival-tradition dialogue - Rung 1 & 2 panel

_Generated 2026-07-01 15:59. Rung 1: TF-IDF role-matched lift, 200 shuffles, seed 1729, no model._

## Rung 1 - cross-agent uptake by condition

| condition | k | mean lift (all) | lift range | mean lift (C<->H only) | mean p | sig (p<.05) |
|---|---:|---:|---|---:|---:|---:|
| bridge | 5 | +0.177 | [+0.138, +0.240] | +0.143 | 0.005 | 5/5 |
| convene | 5 | +0.146 | [+0.117, +0.187] | +0.172 | 0.005 | 5/5 |
| deaf | 5 | +0.065 | [+0.060, +0.076] | +0.066 | 0.005 | 5/5 |
| listen | 5 | +0.152 | [+0.138, +0.166] | +0.152 | 0.005 | 5/5 |

## Pre-registered contrasts

- **P1 (listen > deaf):** listen +0.152 vs deaf +0.065 -> delta **+0.086**; distributions SEPARATED (no overlap). PASS - instrument detects listening.
- **P3 (bridge > listen), ALL cross-agent pairs (confounded):** bridge +0.177 vs listen +0.152 -> delta **+0.026**. Counts C<->B and B<->H, which B inflates by paraphrasing; not the real test.
- **P3 principals-only (C<->H, B dropped) — the registered test:** bridge +0.143 [+0.118,+0.180] vs listen +0.152 [+0.137,+0.166] -> delta **-0.010**, OVERLAP. NEGATIVE - bridge does not raise C<->H uptake (publishable).

_Per-transcript detail:_

- **bridge**: 0 lift=+0.240 p=0.005; 1 lift=+0.160 p=0.005; 2 lift=+0.173 p=0.005; 3 lift=+0.138 p=0.005; 4 lift=+0.175 p=0.005
- **convene**: 0 lift=+0.143 p=0.005; 1 lift=+0.127 p=0.005; 2 lift=+0.154 p=0.005; 3 lift=+0.117 p=0.005; 4 lift=+0.187 p=0.005
- **deaf**: 0 lift=+0.069 p=0.005; 1 lift=+0.076 p=0.005; 2 lift=+0.062 p=0.005; 3 lift=+0.060 p=0.005; 4 lift=+0.060 p=0.005
- **listen**: 0 lift=+0.166 p=0.005; 1 lift=+0.157 p=0.005; 2 lift=+0.138 p=0.005; 3 lift=+0.142 p=0.005; 4 lift=+0.156 p=0.005

## Convener - certification of understanding (Amendment 1)

- Events: **80** (58 faithful, 22 strawman); strawman share 0.28 (target 0.33).
- Certify-rate: faithful **0.93** vs strawman **0.00**.
- Restatement fidelity (cosine to original): faithful **0.422** vs strawman **0.379**.

- **C0 (PRIMARY GATE): discrimination = +0.93, fidelity gap = +0.043.** PASS - certification carries information; reading the rest.
- **P3'a (understanding achievable):** faithful certify-rate 0.93 > floor 0.60 -> PASS - the parties can demonstrate understanding to each other under the protocol.
- **P3'b (incommensurability LOCATED, not uniform):** 4 faithful failed-certifications. Failure loci: consciousness-status 3, other 1. Base faithful mix: spacetime-fundamentality 20, consciousness-status 35, other 3.
  Hard-joint share of failures = 3/4 = 0.75 -> PASS - failures concentrate on the registered hard joints (spacetime / consciousness), not uniformly.

## Rung 2 - relational moves (blind), by condition

| condition | pairs | steelman+concede+build_on share | top moves |
|---|---:|---:|---|
| bridge | 235 | 37% | probe 142, steelman 77, build_on 9, override 4, ack 2 |
| convene | 235 | 43% | probe 123, steelman 99, ack 3, build_on 3, override 3 |
| deaf | 155 | 25% | probe 107, steelman 37, override 8, build_on 1, deflect 1 |
| listen | 155 | 54% | steelman 81, probe 64, override 7, build_on 2, concede 1 |

- **P2 (engagement-move share: listen > deaf):** listen 54% vs deaf 25% -> delta **+30pp**. PASS - the MacIntyrean moves track engagement.

- **P-civility (convene > listen civil register; principals only, T excluded):** civil share convene 43% vs listen 53%; hostile convene 3% vs listen 5%. CHECK - no clear civility gap (falsifier P-civility: T is not doing its pass-through-of-tone job).
