---
title: "LaVR: Scene Latent Conditioned Generative Video Trajectory Re-Rendering using Large 4D Reconstruction Models"
authors:
    - Mingyang Xie
    - Numair Khan
    - Tianfu Wang
    - Naina Dhingra
    - Seonghyeon Nam
    - Haitao Yang
    - Zhuo Hui
    - Christopher A. Metzler
    - Andrea Vedaldi
    - Hamed Pirsiavash
    - Lei Luo
links:
    paper: https://arxiv.org/abs/2601.14674
venue: Conference on Computer Vision and Pattern Recognition (CVPR)
date: 2026-06-01
---

Given a monocular video, the goal of video re-rendering is to generate views of the scene from a novel camera trajectory. Existing methods face two challenges: geometrically unconditioned models lack spatial awareness, leading to drift and deformation under viewpoint changes, while geometrically-conditioned models depend on estimated depth and explicit reconstruction, making them susceptible to depth inaccuracies and calibration errors. We address these challenges by using the implicit geometric knowledge embedded in the latent space of a large 4D reconstruction model to condition the video generation process. These latents capture scene structure in a continuous space without explicit reconstruction, providing a flexible representation that allows the pretrained diffusion prior to regularize errors more effectively. By jointly conditioning on these latents and source camera poses, our model achieves state-of-the-art results on the video re-rendering task.
