---
title: "Gaussian Representations for Video"
authors:
    - Sachin Shah
    - Anustup Choudhury
    - Guan-Ming Su
    - Jaclyn Pytlarz
    - Christopher A. Metzler
    - Trisha Mittal
links:
    paper: https://openaccess.thecvf.com/content/WACV2026/papers/Shah_Gaussian_Representations_for_Video_WACV_2026_paper.pdf
venue: Winter Conference on Applications of Computer Vision (WACV)
date: 2026-03-08
---

We introduce Gaussian representations for videos (GaRV), a novel video encoding and decoding scheme based upon 3D Gaussians. Unlike traditional representations, which encode videos as sequences of frames, or neural representations, which encode videos within the weights of a neural network, we encode videos as a collection of 3D Gaussians within a space-time volume. The key advantage of our approach is that it enables efficient and flexible rasterization-based video decoding. With a slight drop in overall compression rate, GaRV offers a 8-50x improvement in decoding time and 2.5-15x reduction in GPU memory compared with neural counterparts. Existing Gaussian video techniques require 2-30x more disk space, while also using more GPU resources than GaRV. Moreover, GaRV offers unique flexibility in how and when pixels are decoded: One can non-sequentially decode frames/regions without penalty and can selectively decode regions at high-resolution to enable low-cost foveated video decoding.
