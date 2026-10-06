# Reconstruction worksheet

21 items, shuffled. Conditions are withheld: they are in `reconstruction_key.json`, which must not be opened until every item below is authored.

For each item state whether an argument can be made that the EARLIER entry's solution is a resource the LATER entry's solution depends on. `insufficient` is a real answer.

## R01
**EARLIER — Pauli (1925) — the exclusion principle** (quantum-PRS-06)
- *Problem:* The Bohr-Sommerfeld atom does not explain why electrons do not all collapse into the lowest orbit, nor why the periodic table closes its shells at 2, 8, 18; the anomalous Zeeman effect resists every existing scheme
- *Resource:* A fourth two-valued quantum number per electron plus a hard combinatorial constraint: no two electrons in an atom may share the same complete set of quantum numbers
- *Solution:* Shell structure and the length of the periods of the periodic table follow from the constraint; chemistry becomes a consequence of a quantum bookkeeping rule, and the constraint later grounds the stability of all bulk matter

**LATER — Dirac (1930) — unification and the relativistic electron** (quantum-PRS-09)
- *Problem:* Wave mechanics and matrix mechanics are two dialects with no common formulation, and neither is compatible with special relativity, so spin has to be inserted by hand
- *Resource:* An abstract transformation theory in which states are vectors and observables are operators, together with a first-order relativistic wave equation for the electron
- *Solution:* A single formalism containing both earlier theories as representations, with electron spin and the magnetic moment emerging as necessary consequences and the prediction of antimatter; the field acquires its canonical textbook

## R02
**EARLIER — von Neumann (1932) — the mathematical foundation** (quantum-PRS-10)
- *Problem:* Quantum mechanics is empirically successful but mathematically unrigorous, resting on the delta function and other objects with no defined status, and its measurement step has no formal treatment
- *Resource:* Hilbert space and the spectral theory of self-adjoint operators, plus the density matrix, giving states, observables and probabilities a single rigorous setting
- *Solution:* An axiomatic foundation on which the theory can be proved about rather than merely used, separating unitary evolution from the measurement postulate and closing the founding period of the discipline

**LATER — DeepSeek R1 (2025) — reasoning from reinforcement learning alone** (deeplearning-PRS-10)
- *Problem:* Extended reasoning was assumed to require supervised chains of thought written by humans, which is expensive to collect and caps the model at the quality of the demonstrations
- *Resource:* Large-scale reinforcement learning on verifiable outcomes with no supervised reasoning traces, letting the model discover its own long chains, self-checking and backtracking from the reward alone
- *Solution:* Reasoning behaviour emerges without demonstrations and reaches frontier benchmark performance, with an openly released model, moving the axis of progress from pretraining scale to test-time computation

## R03
**EARLIER — ResNet (2015) — depth made trainable** (deeplearning-PRS-02)
- *Problem:* Adding layers past roughly twenty makes networks worse on training error as well as test error, so degradation is an optimisation failure and not overfitting, and depth cannot be exploited
- *Resource:* Identity skip connections that make each block learn a residual correction, so an unneeded layer can represent the identity and gradients reach early layers undecayed
- *Solution:* Networks of 152 layers train stably and win ImageNet 2015 at 3.57 percent top-5 error; depth stops being a limit and the residual block becomes a default component of nearly every later architecture

**LATER — Transformer (2017) — attention as the whole architecture** (deeplearning-PRS-04)
- *Problem:* Recurrent sequence models process tokens strictly in order, so training cannot be parallelised across a sequence and long-range dependencies decay across many steps
- *Resource:* Self-attention alone, with every position attending to every other in one operation, plus positional encodings and multiple heads, discarding recurrence and convolution entirely
- *Solution:* Better translation quality at a fraction of the training cost, and an architecture whose cost is parallel in sequence length; it becomes the substrate for essentially all later large models across text, vision and biology

## R04
**EARLIER — AlexNet (2012) — scale beats hand-engineering** (deeplearning-PRS-01)
- *Problem:* Computer vision rests on hand-designed features and shallow classifiers, ImageNet error has plateaued near 26 percent, and neural networks are widely held to be unable to reach that scale
- *Resource:* A deep convolutional network of 60 million parameters trained on two GPUs, with ReLU units, dropout and heavy data augmentation making the optimisation tractable
- *Solution:* A drop to 15.3 percent top-5 error, roughly ten points below the runner-up, establishing that a learned representation trained at scale beats a designed one and redirecting the entire field toward deep networks

**LATER — ResNet (2015) — depth made trainable** (deeplearning-PRS-02)
- *Problem:* Adding layers past roughly twenty makes networks worse on training error as well as test error, so degradation is an optimisation failure and not overfitting, and depth cannot be exploited
- *Resource:* Identity skip connections that make each block learn a residual correction, so an unneeded layer can represent the identity and gradients reach early layers undecayed
- *Solution:* Networks of 152 layers train stably and win ImageNet 2015 at 3.57 percent top-5 error; depth stops being a limit and the residual block becomes a default component of nearly every later architecture

## R05
**EARLIER — Schrodinger (1926) — the wave equation** (quantum-PRS-08)
- *Problem:* Matrix mechanics works but is opaque, offers no continuous picture of the process, and is hard to apply; de Broglie's matter waves lack a governing equation of motion
- *Resource:* A differential wave equation for a complex amplitude over configuration space, whose stationary solutions are eigenfunctions and whose eigenvalues are the allowed energies of the system
- *Solution:* The hydrogen spectrum falls out as an eigenvalue problem in a familiar mathematical language, the theory becomes broadly calculable, and Schrodinger then proves his formulation equivalent to Heisenberg's

**LATER — AlphaFold 2 (2021) — a fifty-year problem closed** (deeplearning-PRS-08)
- *Problem:* Predicting a protein structure from its sequence had resisted fifty years of effort, and experimental determination is slow and expensive, so most known sequences have no structure
- *Resource:* An architecture built around the geometry of the problem, using attention over the multiple sequence alignment and over residue pairs, with an end-to-end structure module and recycling of its own predictions
- *Solution:* Median accuracy near experimental resolution at CASP14 and a public release of predicted structures for most known proteins, showing that a learned model can close a long-standing scientific problem outright

## R06
**EARLIER — Compton (1922) — the quantum carries momentum** (quantum-PRS-04)
- *Problem:* The light quantum was still widely read as a heuristic; a wave theory of X-ray scattering predicts no wavelength shift, and the case for genuinely particulate radiation rested on the photoelectric effect alone
- *Resource:* Treating an X-ray photon and a free electron as two particles in an elastic collision, and applying relativistic conservation of energy and momentum to predict the scattered wavelength as a function of angle
- *Solution:* A measured wavelength shift matching the collision prediction exactly, establishing that radiation carries momentum as well as energy; the particle aspect of light becomes an experimental fact rather than an interpretation

**LATER — DDPM (2020) — generation as learned denoising** (deeplearning-PRS-07)
- *Problem:* Generative adversarial networks produce sharp images but train unstably and collapse modes, while likelihood-based models are stable but blurry; no generative family was both reliable and high quality
- *Resource:* A fixed forward process that gradually adds Gaussian noise to data, with a network trained to reverse one step at a time, reducing generation to a sequence of simple denoising regressions
- *Solution:* Sample quality competitive with adversarial models under a stable regression objective, opening the diffusion line that becomes the standard method for image, audio and video generation

## R07
**EARLIER — Compton (1922) — the quantum carries momentum** (quantum-PRS-04)
- *Problem:* The light quantum was still widely read as a heuristic; a wave theory of X-ray scattering predicts no wavelength shift, and the case for genuinely particulate radiation rested on the photoelectric effect alone
- *Resource:* Treating an X-ray photon and a free electron as two particles in an elastic collision, and applying relativistic conservation of energy and momentum to predict the scattered wavelength as a function of angle
- *Solution:* A measured wavelength shift matching the collision prediction exactly, establishing that radiation carries momentum as well as energy; the particle aspect of light becomes an experimental fact rather than an interpretation

**LATER — ResNet (2015) — depth made trainable** (deeplearning-PRS-02)
- *Problem:* Adding layers past roughly twenty makes networks worse on training error as well as test error, so degradation is an optimisation failure and not overfitting, and depth cannot be exploited
- *Resource:* Identity skip connections that make each block learn a residual correction, so an unneeded layer can represent the identity and gradients reach early layers undecayed
- *Solution:* Networks of 152 layers train stably and win ImageNet 2015 at 3.57 percent top-5 error; depth stops being a limit and the residual block becomes a default component of nearly every later architecture

## R08
**EARLIER — AlexNet (2012) — scale beats hand-engineering** (deeplearning-PRS-01)
- *Problem:* Computer vision rests on hand-designed features and shallow classifiers, ImageNet error has plateaued near 26 percent, and neural networks are widely held to be unable to reach that scale
- *Resource:* A deep convolutional network of 60 million parameters trained on two GPUs, with ReLU units, dropout and heavy data augmentation making the optimisation tractable
- *Solution:* A drop to 15.3 percent top-5 error, roughly ten points below the runner-up, establishing that a learned representation trained at scale beats a designed one and redirecting the entire field toward deep networks

**LATER — AlphaGo (2016) — search plus learned evaluation** (deeplearning-PRS-03)
- *Problem:* Go has a branching factor near 250 and a state space beyond exhaustive search, and no hand-written evaluation function for board position had ever reached professional strength
- *Resource:* Policy and value networks trained on human games and then on self-play, used to bias and truncate a Monte Carlo tree search so that learned intuition guides the search rather than replacing it
- *Solution:* A 4-1 win over Lee Sedol a decade ahead of expert forecasts, showing that learned evaluation plus search solves problems too large to enumerate and that self-play generates its own training signal

## R09
**EARLIER — Heisenberg (1925) — matrix mechanics** (quantum-PRS-07)
- *Problem:* The old quantum theory is a patchwork of postulates about unobservable electron orbits, it fails for helium and for spectral intensities, and its visualisable pictures generate no systematic calculus
- *Resource:* A methodological restriction to observable quantities alone: represent each transition by an array indexed by pairs of states, and let the algebra of these arrays, which does not commute, replace classical kinematics
- *Solution:* The first complete and internally consistent quantum mechanics, reproducing the harmonic oscillator and spectral intensities; noncommutation appears as the formal core of the theory and yields the uncertainty relations two years later

**LATER — Neural scaling laws (2020) — performance as a predictable function** (deeplearning-PRS-05)
- *Problem:* Choices about model size, dataset size and compute budget are made by intuition and folklore, and there is no way to predict what a model not yet trained will achieve
- *Resource:* A systematic sweep across seven orders of magnitude fitting test loss as a power law in parameters, data and compute, with the compute-optimal allocation derived from the fits
- *Solution:* Loss becomes predictable in advance from a budget, so a large training run can be justified before it is executed; capability turns into an engineering variable and the case for scale becomes quantitative rather than rhetorical

## R10
**EARLIER — Compton (1922) — the quantum carries momentum** (quantum-PRS-04)
- *Problem:* The light quantum was still widely read as a heuristic; a wave theory of X-ray scattering predicts no wavelength shift, and the case for genuinely particulate radiation rested on the photoelectric effect alone
- *Resource:* Treating an X-ray photon and a free electron as two particles in an elastic collision, and applying relativistic conservation of energy and momentum to predict the scattered wavelength as a function of angle
- *Solution:* A measured wavelength shift matching the collision prediction exactly, establishing that radiation carries momentum as well as energy; the particle aspect of light becomes an experimental fact rather than an interpretation

**LATER — RLHF / InstructGPT (2022) — alignment to intent** (deeplearning-PRS-09)
- *Problem:* A model trained to predict the next token is optimised for corpus likelihood and not for what a user asked, so it is untruthful, unhelpful and hard to steer despite being highly capable
- *Resource:* A reward model fitted to human comparisons between candidate outputs, used to optimise the policy with reinforcement learning against that learned preference signal
- *Solution:* A 1.3 billion parameter model preferred by human raters over the 175 billion parameter base model; the training objective shifts from imitation to preference, which is what makes deployed assistants possible

## R11
**EARLIER — Planck (1900) — the quantum of action** (quantum-PRS-01)
- *Problem:* Classical electrodynamics predicts that a blackbody radiates infinite energy at short wavelengths; the observed spectrum falls off instead, and no continuous theory reproduces the measured curve
- *Resource:* A formal trick treating the energy of the oscillators in the cavity wall as divisible only into finite elements proportional to frequency, with a new constant h fixed by fitting the measured spectrum
- *Solution:* A radiation law matching experiment across the whole spectrum, at the cost of admitting discreteness into a continuous theory; the constant h enters physics as an unexplained but load-bearing quantity

**LATER — Compton (1922) — the quantum carries momentum** (quantum-PRS-04)
- *Problem:* The light quantum was still widely read as a heuristic; a wave theory of X-ray scattering predicts no wavelength shift, and the case for genuinely particulate radiation rested on the photoelectric effect alone
- *Resource:* Treating an X-ray photon and a free electron as two particles in an elastic collision, and applying relativistic conservation of energy and momentum to predict the scattered wavelength as a function of angle
- *Solution:* A measured wavelength shift matching the collision prediction exactly, establishing that radiation carries momentum as well as energy; the particle aspect of light becomes an experimental fact rather than an interpretation

## R12
**EARLIER — Bohr (1913) — quantised atomic structure** (quantum-PRS-03)
- *Problem:* The Rutherford nuclear atom is unstable under classical electrodynamics, the orbiting electron should radiate and spiral inward in nanoseconds, and nothing accounts for the sharp discrete lines of the hydrogen spectrum
- *Resource:* Quantisation applied to the mechanical system rather than to radiation: stationary orbits of quantised angular momentum in which the electron does not radiate, with emission occurring only on transition between them
- *Solution:* A model deriving the Balmer series from first principles and fixing the Rydberg constant from h, e and the electron mass; quantisation becomes a structural principle of matter, though the stationary states remain unexplained postulates

**LATER — Heisenberg (1925) — matrix mechanics** (quantum-PRS-07)
- *Problem:* The old quantum theory is a patchwork of postulates about unobservable electron orbits, it fails for helium and for spectral intensities, and its visualisable pictures generate no systematic calculus
- *Resource:* A methodological restriction to observable quantities alone: represent each transition by an array indexed by pairs of states, and let the algebra of these arrays, which does not commute, replace classical kinematics
- *Solution:* The first complete and internally consistent quantum mechanics, reproducing the harmonic oscillator and spectral intensities; noncommutation appears as the formal core of the theory and yields the uncertainty relations two years later

## R13
**EARLIER — DDPM (2020) — generation as learned denoising** (deeplearning-PRS-07)
- *Problem:* Generative adversarial networks produce sharp images but train unstably and collapse modes, while likelihood-based models are stable but blurry; no generative family was both reliable and high quality
- *Resource:* A fixed forward process that gradually adds Gaussian noise to data, with a network trained to reverse one step at a time, reducing generation to a sequence of simple denoising regressions
- *Solution:* Sample quality competitive with adversarial models under a stable regression objective, opening the diffusion line that becomes the standard method for image, audio and video generation

**LATER — GPT-3 (2020) — in-context learning at scale** (deeplearning-PRS-06)
- *Problem:* Every new language task requires collecting a labelled dataset and fine-tuning a separate copy of the model, which does not match how a competent system ought to generalise
- *Resource:* An autoregressive transformer of 175 billion parameters trained on a broad corpus, evaluated with the task described in the prompt and a handful of examples, with no gradient updates at all
- *Solution:* Competitive few-shot performance across many tasks from prompting alone, making the trained model a general interface rather than a task-specific artifact and confirming the scaling laws in the direction they predicted

## R14
**EARLIER — Planck (1900) — the quantum of action** (quantum-PRS-01)
- *Problem:* Classical electrodynamics predicts that a blackbody radiates infinite energy at short wavelengths; the observed spectrum falls off instead, and no continuous theory reproduces the measured curve
- *Resource:* A formal trick treating the energy of the oscillators in the cavity wall as divisible only into finite elements proportional to frequency, with a new constant h fixed by fitting the measured spectrum
- *Solution:* A radiation law matching experiment across the whole spectrum, at the cost of admitting discreteness into a continuous theory; the constant h enters physics as an unexplained but load-bearing quantity

**LATER — Bohr (1913) — quantised atomic structure** (quantum-PRS-03)
- *Problem:* The Rutherford nuclear atom is unstable under classical electrodynamics, the orbiting electron should radiate and spiral inward in nanoseconds, and nothing accounts for the sharp discrete lines of the hydrogen spectrum
- *Resource:* Quantisation applied to the mechanical system rather than to radiation: stationary orbits of quantised angular momentum in which the electron does not radiate, with emission occurring only on transition between them
- *Solution:* A model deriving the Balmer series from first principles and fixing the Rydberg constant from h, e and the electron mass; quantisation becomes a structural principle of matter, though the stationary states remain unexplained postulates

## R15
**EARLIER — Planck (1900) — the quantum of action** (quantum-PRS-01)
- *Problem:* Classical electrodynamics predicts that a blackbody radiates infinite energy at short wavelengths; the observed spectrum falls off instead, and no continuous theory reproduces the measured curve
- *Resource:* A formal trick treating the energy of the oscillators in the cavity wall as divisible only into finite elements proportional to frequency, with a new constant h fixed by fitting the measured spectrum
- *Solution:* A radiation law matching experiment across the whole spectrum, at the cost of admitting discreteness into a continuous theory; the constant h enters physics as an unexplained but load-bearing quantity

**LATER — Dirac (1930) — unification and the relativistic electron** (quantum-PRS-09)
- *Problem:* Wave mechanics and matrix mechanics are two dialects with no common formulation, and neither is compatible with special relativity, so spin has to be inserted by hand
- *Resource:* An abstract transformation theory in which states are vectors and observables are operators, together with a first-order relativistic wave equation for the electron
- *Solution:* A single formalism containing both earlier theories as representations, with electron spin and the magnetic moment emerging as necessary consequences and the prediction of antimatter; the field acquires its canonical textbook

## R16
**EARLIER — Dirac (1930) — unification and the relativistic electron** (quantum-PRS-09)
- *Problem:* Wave mechanics and matrix mechanics are two dialects with no common formulation, and neither is compatible with special relativity, so spin has to be inserted by hand
- *Resource:* An abstract transformation theory in which states are vectors and observables are operators, together with a first-order relativistic wave equation for the electron
- *Solution:* A single formalism containing both earlier theories as representations, with electron spin and the magnetic moment emerging as necessary consequences and the prediction of antimatter; the field acquires its canonical textbook

**LATER — Neural scaling laws (2020) — performance as a predictable function** (deeplearning-PRS-05)
- *Problem:* Choices about model size, dataset size and compute budget are made by intuition and folklore, and there is no way to predict what a model not yet trained will achieve
- *Resource:* A systematic sweep across seven orders of magnitude fitting test loss as a power law in parameters, data and compute, with the compute-optimal allocation derived from the fits
- *Solution:* Loss becomes predictable in advance from a budget, so a large training run can be justified before it is executed; capability turns into an engineering variable and the case for scale becomes quantitative rather than rhetorical

## R17
**EARLIER — Heisenberg (1925) — matrix mechanics** (quantum-PRS-07)
- *Problem:* The old quantum theory is a patchwork of postulates about unobservable electron orbits, it fails for helium and for spectral intensities, and its visualisable pictures generate no systematic calculus
- *Resource:* A methodological restriction to observable quantities alone: represent each transition by an array indexed by pairs of states, and let the algebra of these arrays, which does not commute, replace classical kinematics
- *Solution:* The first complete and internally consistent quantum mechanics, reproducing the harmonic oscillator and spectral intensities; noncommutation appears as the formal core of the theory and yields the uncertainty relations two years later

**LATER — Schrodinger (1926) — the wave equation** (quantum-PRS-08)
- *Problem:* Matrix mechanics works but is opaque, offers no continuous picture of the process, and is hard to apply; de Broglie's matter waves lack a governing equation of motion
- *Resource:* A differential wave equation for a complex amplitude over configuration space, whose stationary solutions are eigenfunctions and whose eigenvalues are the allowed energies of the system
- *Solution:* The hydrogen spectrum falls out as an eigenvalue problem in a familiar mathematical language, the theory becomes broadly calculable, and Schrodinger then proves his formulation equivalent to Heisenberg's

## R18
**EARLIER — AlphaGo (2016) — search plus learned evaluation** (deeplearning-PRS-03)
- *Problem:* Go has a branching factor near 250 and a state space beyond exhaustive search, and no hand-written evaluation function for board position had ever reached professional strength
- *Resource:* Policy and value networks trained on human games and then on self-play, used to bias and truncate a Monte Carlo tree search so that learned intuition guides the search rather than replacing it
- *Solution:* A 4-1 win over Lee Sedol a decade ahead of expert forecasts, showing that learned evaluation plus search solves problems too large to enumerate and that self-play generates its own training signal

**LATER — DeepSeek R1 (2025) — reasoning from reinforcement learning alone** (deeplearning-PRS-10)
- *Problem:* Extended reasoning was assumed to require supervised chains of thought written by humans, which is expensive to collect and caps the model at the quality of the demonstrations
- *Resource:* Large-scale reinforcement learning on verifiable outcomes with no supervised reasoning traces, letting the model discover its own long chains, self-checking and backtracking from the reward alone
- *Solution:* Reasoning behaviour emerges without demonstrations and reaches frontier benchmark performance, with an openly released model, moving the axis of progress from pretraining scale to test-time computation

## R19
**EARLIER — Heisenberg (1925) — matrix mechanics** (quantum-PRS-07)
- *Problem:* The old quantum theory is a patchwork of postulates about unobservable electron orbits, it fails for helium and for spectral intensities, and its visualisable pictures generate no systematic calculus
- *Resource:* A methodological restriction to observable quantities alone: represent each transition by an array indexed by pairs of states, and let the algebra of these arrays, which does not commute, replace classical kinematics
- *Solution:* The first complete and internally consistent quantum mechanics, reproducing the harmonic oscillator and spectral intensities; noncommutation appears as the formal core of the theory and yields the uncertainty relations two years later

**LATER — von Neumann (1932) — the mathematical foundation** (quantum-PRS-10)
- *Problem:* Quantum mechanics is empirically successful but mathematically unrigorous, resting on the delta function and other objects with no defined status, and its measurement step has no formal treatment
- *Resource:* Hilbert space and the spectral theory of self-adjoint operators, plus the density matrix, giving states, observables and probabilities a single rigorous setting
- *Solution:* An axiomatic foundation on which the theory can be proved about rather than merely used, separating unitary evolution from the measurement postulate and closing the founding period of the discipline

## R20
**EARLIER — Planck (1900) — the quantum of action** (quantum-PRS-01)
- *Problem:* Classical electrodynamics predicts that a blackbody radiates infinite energy at short wavelengths; the observed spectrum falls off instead, and no continuous theory reproduces the measured curve
- *Resource:* A formal trick treating the energy of the oscillators in the cavity wall as divisible only into finite elements proportional to frequency, with a new constant h fixed by fitting the measured spectrum
- *Solution:* A radiation law matching experiment across the whole spectrum, at the cost of admitting discreteness into a continuous theory; the constant h enters physics as an unexplained but load-bearing quantity

**LATER — AlexNet (2012) — scale beats hand-engineering** (deeplearning-PRS-01)
- *Problem:* Computer vision rests on hand-designed features and shallow classifiers, ImageNet error has plateaued near 26 percent, and neural networks are widely held to be unable to reach that scale
- *Resource:* A deep convolutional network of 60 million parameters trained on two GPUs, with ReLU units, dropout and heavy data augmentation making the optimisation tractable
- *Solution:* A drop to 15.3 percent top-5 error, roughly ten points below the runner-up, establishing that a learned representation trained at scale beats a designed one and redirecting the entire field toward deep networks

## R21
**EARLIER — ResNet (2015) — depth made trainable** (deeplearning-PRS-02)
- *Problem:* Adding layers past roughly twenty makes networks worse on training error as well as test error, so degradation is an optimisation failure and not overfitting, and depth cannot be exploited
- *Resource:* Identity skip connections that make each block learn a residual correction, so an unneeded layer can represent the identity and gradients reach early layers undecayed
- *Solution:* Networks of 152 layers train stably and win ImageNet 2015 at 3.57 percent top-5 error; depth stops being a limit and the residual block becomes a default component of nearly every later architecture

**LATER — AlphaGo (2016) — search plus learned evaluation** (deeplearning-PRS-03)
- *Problem:* Go has a branching factor near 250 and a state space beyond exhaustive search, and no hand-written evaluation function for board position had ever reached professional strength
- *Resource:* Policy and value networks trained on human games and then on self-play, used to bias and truncate a Monte Carlo tree search so that learned intuition guides the search rather than replacing it
- *Solution:* A 4-1 win over Lee Sedol a decade ahead of expert forecasts, showing that learned evaluation plus search solves problems too large to enumerate and that self-play generates its own training signal
