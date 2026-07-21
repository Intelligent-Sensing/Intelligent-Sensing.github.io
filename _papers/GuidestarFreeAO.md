---
title: "Guidestar-Free Adaptive Optics with Asymmetric Apertures"
authors:
    - Weiyun Jiang
    - Haiyun Guo
    - Christopher A. Metzler
    - Ashok Veeraraghavan
links:
    project: https://weiyunjiang.com/guidestar-free-ao/
venue: ACM Transactions on Graphics (SIGGRAPH)
date: 2026-08-01
---

This work introduces the first closed-loop adaptive optics (AO) system capable of optically correcting aberrations in real-time without a guidestar or a wavefront sensor. Nearly 40 years ago, Cederquist et al. demonstrated that asymmetric apertures enable phase retrieval (PR) algorithms to perform fully computational wavefront sensing, albeit at high computational cost. Inspired by this and by recent machine-learning approaches, we introduce a guidestar-free AO framework built around asymmetric apertures and machine learning. Our approach combines three key elements: (1) an asymmetric aperture placed at the system's pupil plane that enables PR-based wavefront sensing, (2) a pair of machine learning algorithms that estimate the point-spread function from natural scene measurements and reconstruct phase aberrations, and (3) a spatial light modulator that performs optical correction. We experimentally validate this framework on dense natural scenes imaged through unknown obscurants, outperforming state-of-the-art guidestar-free wavefront shaping methods using an order of magnitude fewer measurements and three orders of magnitude less computation.
