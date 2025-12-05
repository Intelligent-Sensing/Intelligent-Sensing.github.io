---
title: "Flash-Split: 2D Reflection Removal with Flash Cues and Latent Diffusion Separation"
authors:
    - Tianfu Wang*
    - Mingyang Xie*
    - Haoming Cai
    - Sachin Shah
    - Christopher A. Metzler
links:
    paper: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Flash-Split_2D_Reflection_Removal_with_Flash_Cues_and_Latent_Diffusion_CVPR_2025_paper.pdf
    project: https://mingyangx.github.io/Flash-Split/
venue: Conference on Computer Vision and Pattern Recognition (CVPR)
date: 2025-06-01
---

Transparent surfaces, such as glass, create complex reflections that obscure images and challenge downstream computer vision applications. We introduce Flash-Split, a robust framework for separating transmitted and reflected light using a single (potentially misaligned) pair of flash/no-flash images. Our core idea is to perform flash-informed reflection separation iteratively in a low-dimensional latent space. Specifically, Flash-Split consists of two stages. Stage 1 separates the reflection latent and transmission latent via a dual-branch diffusion model that is conditioned on an encoded flash/no-flash latent pair. This stage effectively mitigates the flash/no-flash misalignment issue. Stage 2 restores high-resolution, faithful details to the separated latents via a cross-latent decoding process that is conditioned on the original images before separation. We validate Flash-Split on challenging real-world scenes and demonstrate it significantly outperforms existing methods.