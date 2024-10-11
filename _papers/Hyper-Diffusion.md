---
title: "Hyper-Diffusion: Estimating Epistemic and Aleatoric Uncertainty with a Single Model"
authors:
    - Matthew A. Chan
    - Maria J. Molina
    - Christopher A. Metzler
links:
    paper: https://arxiv.org/pdf/2402.03478
venue: Conference on Neural Information Processing Systems (NeurIPS)
date: 2024-10-09
---

Estimating and disentangling epistemic uncertainty (uncertainty that can be reduced with more training data) and aleatoric uncertainty (uncertainty that is inherent to the task at hand) is critically important when applying machine learning (ML) to high-stakes applications such as medical imaging and weather forecasting. Conditional diffusion models' breakthrough ability to accurately and efficiently sample from the posterior distribution of a dataset now makes uncertainty estimation conceptually straightforward: One need only train and sample from a large ensemble of diffusion models. Unfortunately, training such an ensemble becomes computationally intractable as the complexity of the model architecture grows. In this work we introduce a new approach to ensembling, hyper-diffusion, which allows one to accurately estimate epistemic and aleatoric uncertainty with a single model. Unlike existing Monte Carlo dropout based single-model ensembling methods, hyper-diffusion offers the same prediction accuracy as multi-model ensembles. We validate our approach on two distinct tasks: x-ray computed tomography (CT) reconstruction and weather temperature forecasting.
