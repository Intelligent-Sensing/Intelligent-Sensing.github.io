---
title: "Repurposing Pre-trained Video Diffusion Models for Event-based Video Interpolation"
authors:
    - Jingxi Chen
    - Brandon Y. Feng
    - Haoming Cai
    - Tianfu Wang
    - Levi Burner
    - Dehao Yuan
    - Cornelia Fermuller
    - Christopher A. Metzler
    - Yiannis Aloimonos
links:
    paper: https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_Repurposing_Pre-trained_Video_Diffusion_Models_for_Event-based_Video_Interpolation_CVPR_2025_paper.pdf
    project: https://vdm-evfi.github.io/
venue: Conference on Computer Vision and Pattern Recognition (CVPR)
date: 2025-06-01
---

Video Frame Interpolation aims to recover realistic missing frames between observed frames, generating a high-frame-rate video from a low-frame-rate video. However, without additional guidance, large motion between frames makes this problem ill-posed. Event-based Video Frame Interpolation (EVFI) addresses this challenge by using sparse, high-temporal-resolution event measurements as motion guidance. This guidance allows EVFI methods to significantly outperform frame-only methods. However, to date, EVFI methods have relied upon a limited set of paired event-frame training data, severely limiting their performance and generalization capabilities. In this work, we overcome the limited data challenge by adapting pre-trained video diffusion models trained on internet-scale datasets to EVFI. We experimentally validate our approach on real-world EVFI datasets, including a new one we introduce. Our method outperforms existing methods and generalizes across cameras far better than existing approaches.
