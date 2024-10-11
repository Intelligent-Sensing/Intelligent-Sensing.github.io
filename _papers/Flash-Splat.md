---
title: "Flash-Splat: 3D Reflection Removal with Flash Cues and Gaussian Splats"
authors:
    - Mingyang Xie*
    - Haoming Cai*
    - Sachin Shah
    - Yiran Xu
    - Brandon Y. Feng
    - Jia-Bin Huang
    - Christopher A. Metzler
links:
    paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/10739.pdf
    project: https://flash-splat.github.io
venue: European Conference on Computer Vision (ECCV)
date: 2024-09-29
---

We introduce a simple yet effective approach for separating transmitted and reflected light. Our key insight is that the powerful novel view synthesis capabilities provided by modern inverse rendering methods (e.g., 3D Gaussian splatting) allow one to perform flash/no-flash reflection separation using unpaired measurements -- this relaxation dramatically simplifies image acquisition over conventional paired flash/no-flash reflection separation methods. Through extensive real-world experiments, we demonstrate our method, Flash-Splat, accurately reconstructs both transmitted and reflected scenes in 3D. Our method outperforms existing 3D reflection separation methods, which do not leverage illumination control, by a large margin.
