---
title: "WaveMo: Learning Wavefront Modulations to See Through Scattering"
authors:
    - Mingyang Xie*
    - Haiyun Guo*
    - Brandon Y. Feng
    - Lingbo Jin
    - Ashok Veeraraghavan
    - Christopher A. Metzler
links:
    project: https://wavemo-2024.github.io/
venue: Conference on Computer Vision and Pattern Recognition (CVPR)
date: 2024-06-01
---

Imaging through scattering media is a fundamental and pervasive challenge in fields ranging from medical diagnostics to autonomous navigation. A promising strategy to overcome this challenge is wavefront modulation, which induces measurement diversity during image acquisition. Despite its importance, designing optimal wavefront modulations to image through scattering remains under-explored. This paper introduces a novel learning-based framework to address the gap. Our approach jointly optimizes wavefront modulations and a computationally lightweight feedforward "proxy" reconstruction network. This network is trained to recover scenes obscured by scattering, using measurements that are modified by these modulations. The learned modulations produced by our framework generalize effectively to unseen scattering scenarios and exhibit remarkable versatility. During deployment, the learned modulations can be decoupled from the proxy network to augment other more computationally expensive restoration algorithms. Through extensive experiments, we demonstrate our approach significantly advances the state of the art in imaging through scattering.
