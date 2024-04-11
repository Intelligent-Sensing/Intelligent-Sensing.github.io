---
title: "Turbugan: An Adversarial Learning Approach to Spatially-Varying Multiframe Blind Deconvolution with Applications to Imaging Through Turbulence"
authors:
    - Brandon Y. Feng*
    - Mingyang Xie*
    - Christopher A. Metzler
links:
    paper: https://ieeexplore.ieee.org/abstract/document/10012058
venue: IEEE Journal on Selected Areas in Information Theory
date: 2022-09-01
---

We present a self-supervised and self-calibrating multi-shot approach to imaging through atmospheric turbulence, called TurbuGAN. Our approach requires no paired training data, adapts itself to the distribution of the turbulence, leverages domain-specific data priors, and can generalize from tens to thousands of measurements. We achieve such functionality through an adversarial sensing framework adapted from CryoGAN, which uses a discriminator network to match the distributions of captured and simulated measurements. Our framework builds on CryoGAN by (1) generalizing the forward measurement model to incorporate physically accurate and computationally efficient models for light propagation through anisoplanatic turbulence, (2) enabling adaptation to slightly misspecified forward models, and (3) leveraging domain-specific prior knowledge using pretrained generative networks, when available. We validate TurbuGAN on both computationally simulated and experimentally captured images distorted with anisoplanatic turbulence.
