# Rung 1 - Uptake: is listening legible without a model?

_Generated 2026-07-30 23:44 from `open-story-snapshot-2026-07-30.db` (read-only). Deterministic: TF-IDF, 200 shuffles, seed 1729. No model._

## Population

- turn-bearing sessions: **947**
- with a usable dialogue stream (>= 4 utterances): **61**
- skipped (too short for a control, < 4 utterances): **886**
- **substantive two-sided dialogues** (each role >=3 utts, >=10 utts total): **38** -- these are the only sessions where uptake is well-posed; the rest are single-prompt runs whose role-matched null is degenerate (lift==0 by construction).
- of measured, AI<->AI (`agent-*`): **0** (agent sessions are single-shot in this corpus; AI<->AI uptake is not yet measurable)
- **turn rows skipped as unreadable: 1452** across 191 sessions -- `data` empty or not JSON, so the row carries no content to score. The 2026-06-29 snapshot had **zero** such rows; this is upstream loss that appeared since, and it removes utterances that would otherwise count toward the thresholds below.

## The verdict (real predecessor vs. role-matched random partner)

`lift = mean(real adjacent cosine) - mean(role-matched random-partner cosine)`. Positive lift means an utterance resembles its ACTUAL predecessor more than a random same-role utterance from the same conversation -- specific uptake, not just shared topic. **Reported on the 38 substantive dialogues.**

- median real adjacent cosine: **0.079**
- median role-matched null cosine: **0.036**
- median **lift**: **+0.041**
- dialogues with positive lift: **37/38** (97%)
- dialogues where real beats role-matched null at p<0.05: **34/38** (89%)
- _(for contrast, across all 61 measured incl. degenerate runs: median lift +0.035, positive 56/61 -- the degenerate runs wash the median to ~0)_

## Direction (each is real - role-matched null, on substantive dialogues)

- mean **A->H** uptake lift (next human takes up the AI - the listening signal): **+0.024**, positive in **31/38**
- mean **H->A** uptake lift (AI takes up the human - sanity floor): **+0.065**, positive in **37/38**
- explicit back-reference rate on A->H pairs (marker or rare-term overlap): **65%**

## Per-session (substantive dialogues, top 20 by utterance count)

| session | utt | real | null | lift | p | A->H lift | H->A lift | ref% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `07ab764b-395e-` | 1063 | 0.006 | 0.008 | -0.002 | 0.995 | -0.002 | -0.002 | 28% |
| `5aa0f8ed-1b3d-` | 73 | 0.066 | 0.023 | +0.043 | 0.005 | +0.030 | +0.056 | 77% |
| `ed393c34-781c-` | 60 | 0.065 | 0.024 | +0.041 | 0.005 | +0.019 | +0.063 | 66% |
| `e3f8b703-41ee-` | 50 | 0.147 | 0.057 | +0.090 | 0.005 | +0.088 | +0.091 | 75% |
| `d8670eb0-0de3-` | 41 | 0.061 | 0.028 | +0.032 | 0.005 | +0.002 | +0.064 | 65% |
| `1aea1425-1726-` | 38 | 0.119 | 0.026 | +0.093 | 0.005 | +0.022 | +0.159 | 72% |
| `5df21d91-4bf0-` | 37 | 0.036 | 0.016 | +0.019 | 0.005 | +0.014 | +0.025 | 50% |
| `81638a6e-95f9-` | 36 | 0.126 | 0.044 | +0.082 | 0.005 | +0.069 | +0.096 | 82% |
| `9d9af05c-f8b8-` | 36 | 0.048 | 0.019 | +0.029 | 0.005 | +0.023 | +0.036 | 71% |
| `848b16f9-3f90-` | 32 | 0.108 | 0.035 | +0.073 | 0.005 | +0.063 | +0.082 | 67% |
| `dbb48bb5-a819-` | 30 | 0.081 | 0.033 | +0.048 | 0.005 | +0.021 | +0.073 | 57% |
| `b3a83dbf-7291-` | 28 | 0.081 | 0.031 | +0.050 | 0.005 | +0.041 | +0.059 | 62% |
| `83dd9511-b240-` | 26 | 0.097 | 0.039 | +0.058 | 0.005 | +0.013 | +0.100 | 75% |
| `ea7b2dcd-1d77-` | 26 | 0.188 | 0.083 | +0.105 | 0.005 | +0.123 | +0.086 | 91% |
| `f040b70a-a8db-` | 25 | 0.070 | 0.037 | +0.033 | 0.005 | +0.025 | +0.039 | 73% |
| `245f263e-34bb-` | 24 | 0.038 | 0.022 | +0.015 | 0.010 | +0.018 | +0.014 | 36% |
| `84f7ebea-2a49-` | 24 | 0.097 | 0.047 | +0.050 | 0.005 | +0.006 | +0.091 | 78% |
| `f28c796c-eac2-` | 24 | 0.113 | 0.046 | +0.068 | 0.005 | +0.007 | +0.122 | 64% |
| `d7ac629b-293d-` | 22 | 0.086 | 0.044 | +0.042 | 0.005 | +0.035 | +0.046 | 20% |
| `c9d9e7c9-dd6e-` | 21 | 0.159 | 0.077 | +0.082 | 0.005 | +0.054 | +0.113 | 78% |

## Honest limit

TF-IDF is lexical, so short human backchannels that genuinely listen but reuse few words score ~0. This makes every number above a **conservative lower bound** on uptake. It also bears asymmetrically on direction: **H->A** (the AI reusing the human's own vocabulary to answer) is lexically easy to see, while **A->H** (a brief human reply taking up a long AI answer) is exactly where lexical goes blind. So A->H being the noisier, sometimes-negative direction is expected -- and it is precisely the signal Rung 2's semantic judgment would buy. Signal present even through this lens is strong evidence; weak A->H is not evidence of absence.

