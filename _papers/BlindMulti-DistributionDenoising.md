---
title: "A Scalable Training Strategy for Blind Multi-Distribution Noise Removal"
authors:
    - Kevin Zhang
    - Sakshum Kulshrestha
    - Christopher A. Metzler
links:
    paper: https://ieeexplore.ieee.org/abstract/document/10729723
venue: IEEE Transactions on Image Processing
date: 2024-10-22
---

Despite recent advances, developing general-purpose universal denoising and artifact-removal networks remains largely an open problem: Given fixed network weights, one inherently trades-off specialization at one task (e.g., removing Poisson noise) for performance at another (e.g., removing speckle noise). In addition, training such a network is challenging due to the curse of dimensionality: As one increases the dimensions of the specification-space (i.e., the number of parameters needed to describe the noise distribution) the number of unique specifications one needs to train for grows exponentially. Uniformly sampling this space will result in a network that does well at very challenging problem specifications but poorly at easy problem specifications, where even large errors will have a small effect on the overall mean squared error. In this work we propose training denoising networks using an adaptive-sampling/active-learning strategy. Our work improves upon a recently proposed universal denoiser training strategy by extending these results to higher dimensions and by incorporating a polynomial approximation of the true specification-loss landscape. This approximation allows us to reduce training times by almost two orders of magnitude. We test our method on simulated joint Poisson-Gaussian-Speckle noise and demonstrate that with our proposed training strategy, a single blind, generalist denoiser network can achieve peak signal-to-noise ratios within a uniform bound of specialized denoiser networks across a large range of operating conditions. We also capture a small dataset of images with varying amounts of joint Poisson-Gaussian-Speckle noise and demonstrate that a universal denoiser trained using our adaptive-sampling strategy outperforms uniformly trained baselines.
