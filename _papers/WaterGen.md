---
title: "WaterGen: Decoupling Scene and Medium in Underwater Image Generation"
authors:
    - Jiayi Wu
    - Tianfu Wang
    - Tianyi Xiong
    - Dehao Yuan
    - Xiaomin Lin
    - Md Jahidul Islam
    - Cornelia Fermuller
    - Christopher A. Metzler
    - Yiannis Aloimonos
links:
    paper: https://arxiv.org/abs/2606.31147
venue: European Conference on Computer Vision (ECCV)
date: 2026-09-01
---

Underwater computer vision tasks, such as detection, restoration, and segmentation, are limited by the scarcity of large-scale and diverse training data. We introduce WaterGen, a method for generating large-scale, realistic, and diverse underwater images that provides independent control of the scene and water medium conditions. Our approach treats underwater image generation as the decoupled control of two factors: realistic and diverse scene content, and accurate and controllable water medium effects. Our key insight is that scene generation and medium modeling can be decoupled within a latent diffusion framework: we first fine-tune a latent diffusion U-Net on degradation-free underwater images to generate diverse, realistic scene content, then formulate physically accurate medium degradation as a conditional decoding process applied to these latents. We leverage WaterGen to build large-scale synthetic underwater datasets and demonstrate that our synthetic data consistently improve downstream performance in underwater restoration and semantic segmentation.
