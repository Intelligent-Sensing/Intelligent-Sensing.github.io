---
title: "FPM-INR: Fourier Ptychographic Microscopy Image Stack Reconstruction Using Implicit Neural Representations"
authors:
    - Haowen Zhou*
    - Brandon Y. Feng*
    - Haiyun Guo
    - Siyu Lin
    - Mingshu Liang
    - Christopher A. Metzler**
    - Changhuei Yang**
links:
    paper: https://opg.optica.org/optica/fulltext.cfm?uri=optica-10-12-1679
venue: Optica
date: 2023-12-20
---

Image stacks provide invaluable 3D information in various biological and pathological imaging applications. Fourier ptychographic microscopy (FPM) enables reconstructing high-resolution, wide field-of-view image stacks without z-stack scanning, thus significantly accelerating image acquisition. However, existing FPM methods take tens of minutes to reconstruct and gigabytes of memory to store a high-resolution volumetric scene, impeding fast gigapixel-scale remote digital pathology. While deep learning approaches have been explored to address this challenge, existing methods poorly generalize to novel datasets and can produce unreliable hallucinations. This work presents FPM-INR, a compact and efficient framework that integrates physics-based optical models with implicit neural representations (INRs) to represent and reconstruct FPM image stacks. FPM-INR is agnostic to system design or sample types and does not require external training data. In our experiments, FPM-INR substantially outperforms traditional FPM algorithms with up to a 25-fold increase in speed and an 80-fold reduction in memory usage for continuous image stack representations.
