---
title: "Parametric Shadow Control for Portrait Generation in Text-to-Image Diffusion Models"
authors:
    - Haoming Cai
    - Tsung-Wei Huang
    - Shiv Gehlot
    - Brandon Y. Feng
    - Sachin Shah
    - Guan-Ming Su
    - Christopher A. Metzler
links:
    paper: https://openaccess.thecvf.com/content/ICCV2025/html/Cai_Parametric_Shadow_Control_for_Portrait_Generation_in_Text-to-Image_Diffusion_Models_ICCV_2025_paper.html
    project: https://www.hm-cai.com/ShadowDirector/
venue: International Conference on Computer Vision (ICCV)
date: 2025-10-19
---

Text-to-image diffusion models excel at generating diverse portraits, but lack intuitive shadow control. Existing editing approaches, as post-processing, struggle to offer effective manipulation across diverse styles, and either rely on expensive real-world light-stage data collection or require extensive computational resources for training. To address these limitations, we introduce Shadow Director, a method that extracts and manipulates hidden shadow attributes within well-trained diffusion models. Our approach uses a small estimation network that requires only a few thousand synthetic images and hours of training—no costly real-world light-stage data needed. Shadow Director enables parametric and intuitive control over shadow shape, placement, and intensity during portrait generation while preserving artistic integrity and identity across diverse styles.
