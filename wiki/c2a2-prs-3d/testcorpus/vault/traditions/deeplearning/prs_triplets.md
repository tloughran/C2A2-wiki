# Deep Learning (2012-2025) — PRS Triplets
*Test corpus. Encoded from the Karpathy domino image, 2026-09-01.*

## Triplets

PRS-01:
  Label: AlexNet (2012) — scale beats hand-engineering
  Problem: Computer vision rests on hand-designed features and shallow classifiers, ImageNet error has plateaued near 26 percent, and neural networks are widely held to be unable to reach that scale
  Resource: A deep convolutional network of 60 million parameters trained on two GPUs, with ReLU units, dropout and heavy data augmentation making the optimisation tractable
  Solution: A drop to 15.3 percent top-5 error, roughly ten points below the runner-up, establishing that a learned representation trained at scale beats a designed one and redirecting the entire field toward deep networks
  Date Added: 2012-12-03
  Source: Krizhevsky, Sutskever, Hinton, NeurIPS (2012)
  Confidence: High

PRS-02:
  Label: ResNet (2015) — depth made trainable
  Problem: Adding layers past roughly twenty makes networks worse on training error as well as test error, so degradation is an optimisation failure and not overfitting, and depth cannot be exploited
  Resource: Identity skip connections that make each block learn a residual correction, so an unneeded layer can represent the identity and gradients reach early layers undecayed
  Solution: Networks of 152 layers train stably and win ImageNet 2015 at 3.57 percent top-5 error; depth stops being a limit and the residual block becomes a default component of nearly every later architecture
  Date Added: 2015-12-10
  Source: He, Zhang, Ren, Sun, "Deep Residual Learning for Image Recognition" (2015)
  Confidence: High

PRS-03:
  Label: AlphaGo (2016) — search plus learned evaluation
  Problem: Go has a branching factor near 250 and a state space beyond exhaustive search, and no hand-written evaluation function for board position had ever reached professional strength
  Resource: Policy and value networks trained on human games and then on self-play, used to bias and truncate a Monte Carlo tree search so that learned intuition guides the search rather than replacing it
  Solution: A 4-1 win over Lee Sedol a decade ahead of expert forecasts, showing that learned evaluation plus search solves problems too large to enumerate and that self-play generates its own training signal
  Date Added: 2016-01-28
  Source: Silver et al., "Mastering the game of Go with deep neural networks and tree search", Nature (2016)
  Confidence: High

PRS-04:
  Label: Transformer (2017) — attention as the whole architecture
  Problem: Recurrent sequence models process tokens strictly in order, so training cannot be parallelised across a sequence and long-range dependencies decay across many steps
  Resource: Self-attention alone, with every position attending to every other in one operation, plus positional encodings and multiple heads, discarding recurrence and convolution entirely
  Solution: Better translation quality at a fraction of the training cost, and an architecture whose cost is parallel in sequence length; it becomes the substrate for essentially all later large models across text, vision and biology
  Date Added: 2017-06-12
  Source: Vaswani et al., "Attention Is All You Need" (2017)
  Confidence: High

PRS-05:
  Label: Neural scaling laws (2020) — performance as a predictable function
  Problem: Choices about model size, dataset size and compute budget are made by intuition and folklore, and there is no way to predict what a model not yet trained will achieve
  Resource: A systematic sweep across seven orders of magnitude fitting test loss as a power law in parameters, data and compute, with the compute-optimal allocation derived from the fits
  Solution: Loss becomes predictable in advance from a budget, so a large training run can be justified before it is executed; capability turns into an engineering variable and the case for scale becomes quantitative rather than rhetorical
  Date Added: 2020-01-23
  Source: Kaplan et al., "Scaling Laws for Neural Language Models" (2020)
  Confidence: High

PRS-06:
  Label: GPT-3 (2020) — in-context learning at scale
  Problem: Every new language task requires collecting a labelled dataset and fine-tuning a separate copy of the model, which does not match how a competent system ought to generalise
  Resource: An autoregressive transformer of 175 billion parameters trained on a broad corpus, evaluated with the task described in the prompt and a handful of examples, with no gradient updates at all
  Solution: Competitive few-shot performance across many tasks from prompting alone, making the trained model a general interface rather than a task-specific artifact and confirming the scaling laws in the direction they predicted
  Date Added: 2020-05-28
  Source: Brown et al., "Language Models are Few-Shot Learners" (2020)
  Confidence: High

PRS-07:
  Label: DDPM (2020) — generation as learned denoising
  Problem: Generative adversarial networks produce sharp images but train unstably and collapse modes, while likelihood-based models are stable but blurry; no generative family was both reliable and high quality
  Resource: A fixed forward process that gradually adds Gaussian noise to data, with a network trained to reverse one step at a time, reducing generation to a sequence of simple denoising regressions
  Solution: Sample quality competitive with adversarial models under a stable regression objective, opening the diffusion line that becomes the standard method for image, audio and video generation
  Date Added: 2020-06-19
  Source: Ho, Jain, Abbeel, "Denoising Diffusion Probabilistic Models" (2020)
  Confidence: High

PRS-08:
  Label: AlphaFold 2 (2021) — a fifty-year problem closed
  Problem: Predicting a protein structure from its sequence had resisted fifty years of effort, and experimental determination is slow and expensive, so most known sequences have no structure
  Resource: An architecture built around the geometry of the problem, using attention over the multiple sequence alignment and over residue pairs, with an end-to-end structure module and recycling of its own predictions
  Solution: Median accuracy near experimental resolution at CASP14 and a public release of predicted structures for most known proteins, showing that a learned model can close a long-standing scientific problem outright
  Date Added: 2021-07-15
  Source: Jumper et al., "Highly accurate protein structure prediction with AlphaFold", Nature (2021)
  Confidence: High

PRS-09:
  Label: RLHF / InstructGPT (2022) — alignment to intent
  Problem: A model trained to predict the next token is optimised for corpus likelihood and not for what a user asked, so it is untruthful, unhelpful and hard to steer despite being highly capable
  Resource: A reward model fitted to human comparisons between candidate outputs, used to optimise the policy with reinforcement learning against that learned preference signal
  Solution: A 1.3 billion parameter model preferred by human raters over the 175 billion parameter base model; the training objective shifts from imitation to preference, which is what makes deployed assistants possible
  Date Added: 2022-03-04
  Source: Ouyang et al., "Training language models to follow instructions with human feedback" (2022)
  Confidence: High

PRS-10:
  Label: DeepSeek R1 (2025) — reasoning from reinforcement learning alone
  Problem: Extended reasoning was assumed to require supervised chains of thought written by humans, which is expensive to collect and caps the model at the quality of the demonstrations
  Resource: Large-scale reinforcement learning on verifiable outcomes with no supervised reasoning traces, letting the model discover its own long chains, self-checking and backtracking from the reward alone
  Solution: Reasoning behaviour emerges without demonstrations and reaches frontier benchmark performance, with an openly released model, moving the axis of progress from pretraining scale to test-time computation
  Date Added: 2025-01-22
  Source: DeepSeek-AI, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" (2025)
  Confidence: High
