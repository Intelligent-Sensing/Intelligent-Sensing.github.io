---
title: Transformers for Robust Radar Waveform Classification
authors:
    - Matthew R. Ziemann
    - Christopher A. Metzler
links:
    paper: https://ieeexplore.ieee.org/abstract/document/10052000
venue: 56th Asilomar Conference on Signals, Systems, and Computers
date: 2022-10-31
---

Radar pulse classification in noisy environments is an important but challenging task for cognitive radar systems. Deep learning based algorithms, such as convolutional neural networks (CNN), are remarkably effective at classifying radar pulses in low signal-to-noise ratio environments. However, these same algorithms are highly vulnerable to adversarial attacks-they can be tricked into misclassifying signals using relatively weak perturbations. We study a self-attention based alternative to CNNs-the Transformer-and its effectiveness as a radar pulse classifier. We compare the adversarial robustness of CNNs and Transformers to better understand their limitations. We find that Transformers are up to 2.3x more accurate in the presence of adversarial attacks while providing comparable accuracy when not under attack.
