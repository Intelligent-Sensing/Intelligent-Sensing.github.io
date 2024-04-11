---
title: "SUD2: Supervision by Denoising Diffusion Models for Image Reconstruction"
authors:
    - Matthew A. Chan
    - Sean I. Young
    - Christopher A. Metzler
links:
    paper: https://openreview.net/pdf?id=wHnKIsCz4j
venue: NeurIPS Workshop on Deep Learning and Inverse Problems
date: 2023-11-03
---

Many imaging inverse problems—such as image-dependent in-painting and dehazing—are challeng-
ing because their forward models are unknown or depend on unknown latent parameters. While one
can solve such problems by training a neural network with vast quantities of paired training data,
such paired training data is often unavailable. In this paper, we propose a generalized framework
for training image reconstruction networks when paired training data is scarce. In particular, we
demonstrate the ability of image denoising algorithms and, by extension, denoising diffusion models,
to supervise network training in the absence of paired training data.
