---
title: Adaptive LPD Radar Waveform Design with Generative Adversarial Neural Networks
authors:
    - Matthew R. Ziemann
    - Christopher A. Metzler
links:
    paper: https://ieeexplore.ieee.org/document/10476876
venue: 57th Asilomar Conference on Signals, Systems, and Computers
date: 2023-10-31
---

We propose a novel method for generating low probability of detection (LPD) radar waveforms using unsupervised generative adversarial neural networks (GANs). To ensure our waveforms are hard to detect, we train a GAN to learn the statistical distribution of background radio frequency (RF) signals then use that GAN to generate novel waveforms that mimic the instantaneous background RF signals. To ensure our waveforms are still effective for sensing, we add an additional loss term based on the ambiguity function that optimizes the outputs to achieve the desired range and velocity resolutions. We evaluate the performance of our method by comparing the detectability of our generated waveforms with traditional LPD waveforms against a separately trained detection neural network. We find that our method can generate high-quality LPD waveforms that reduce detectability by up to 67%. These waveforms also have ambiguity functions with narrow mainlobes and low sidelobes, indicating they offer useful range and Doppler resolutions.
