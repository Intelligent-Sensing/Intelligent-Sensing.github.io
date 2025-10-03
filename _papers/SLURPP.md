---
title: "Single-Step Latent Diffusion for Underwater Image Restoration"
authors:
    - Jiayi Wu*
    - Tianfu Wang*
    - Md Abu Bakr Siddique
    - Md Jahidul Islam
    - Cornelia Fermuller
    - Yiannis Aloimonos
    - Christopher A. Metzler
links:
    paper: https://ieeexplore.ieee.org/abstract/document/11127006
    project: https://tianfwang.github.io/slurpp/
venue: IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)
date: 2025-08-15
---

Underwater image restoration algorithms seek to restore the color, contrast, and appearance of a scene that is imaged underwater. They are a critical tool in applications ranging from marine ecology and aquaculture to underwater construction and archaeology. While existing pixel-domain diffusion-based image restoration approaches are effective at restoring simple scenes with limited depth variation, they are computationally intensive and often generate unrealistic artifacts when applied to scenes with complex geometry and significant depth variation. In this work we overcome these limitations by combining a novel network architecture (SLURPP) with an accurate synthetic data generation pipeline. SLURPP combines pretrained latent diffusion models—which encode strong priors on the geometry and depth of scenes—with an explicit scene decomposition—which allows one to model and account for the effects of light attenuation and backscattering. To train SLURPP we design a physics-based underwater image synthesis pipeline that applies varied and realistic underwater degradation effects to existing terrestrial image datasets. This approach enables the generation of diverse training data with dense medium/degradation annotations. We evaluate our method extensively on both synthetic and real-world benchmarks and demonstrate state-of-the-art performance. Notably, SLURPP is over 200× faster than existing diffusion-based methods while offering ∼ 3dB improvement in PSNR on synthetic benchmarks. It also offers compelling qualitative improvements on real-world data.