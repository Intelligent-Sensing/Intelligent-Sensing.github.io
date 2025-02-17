---
title: Adaptive LPD Radar Waveform Design with Generative Deep Learning
authors:
    - Matthew R. Ziemann
    - Christopher A. Metzler
links:
    paper: https://ieeexplore.ieee.org/document/10887245
venue: IEEE Transactions on Radar Systems
date: 2025-02-07
---

We propose a learning-based method for adaptively generating  low probability of detection (LPD) radar waveforms that blend into their operating environment. Our waveforms are designed to follow a distribution that is indistinguishable from the ambient radio frequency (RF) background---while still being effective at ranging and sensing. To do so, we use an unsupervised, adversarial learning framework; our generator network produces waveforms designed to confuse a critic network, which is optimized to differentiate generated waveforms from the background. To ensure our generated waveforms are still effective for sensing, we introduce and minimize an ambiguity function-based loss on the generated waveforms. We evaluate the performance of our method by comparing the single-pulse detectability of our generated waveforms with traditional LPD waveforms using a separately trained detection neural network. We find that our method can generate LPD waveforms that reduce detectability by up to 90% while simultaneously offering improved ambiguity function (sensing) characteristics. Our framework also provides a mechanism to trade-off detectability and sensing performance.
