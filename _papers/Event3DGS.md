---
title: "Event3DGS: Event-Based 3D Gaussian Splatting for High-Speed Robot Egomotion"
authors:
    - Tianyi Xiong*
    - Jiayi Wu*
    - Botao He
    - Cornelia Fermuller
    - Yiannis Aloimonos
    - Heng Huang
    - Christopher A. Metzler
links:
    paper: https://openreview.net/pdf?id=EyEE7547vy
    project: https://tyxiong23.github.io/event3dgs
venue: 8th Annual Conference on Robot Learning (CoRL)
date: 2024-09-05
---

By combining differentiable rendering with explicit point-based scene representations, 3D Gaussian Splatting (3DGS) has demonstrated breakthrough 3D reconstruction capabilities. However, to date 3DGS has had limited impact on robotics, where high-speed egomotion is pervasive: Egomotion introduces motion blur and leads to artifacts in existing frame-based 3DGS reconstruction methods. To address this challenge, we introduce Event3DGS, an event-based 3DGS framework. By exploiting the exceptional temporal resolution of event cameras, Event3GDS can reconstruct high-fidelity 3D structure and appearance under high-speed egomotion. Extensive experiments on multiple synthetic and real-world datasets demonstrate the superiority of Event3DGS compared with existing event-based dense 3D scene reconstruction frameworks; Event3DGS substantially improves reconstruction quality (+3dB) while reducing computational costs by 95%. Our framework also allows one to incorporate a few motion-blurred frame-based measurements into the reconstruction process to further improve appearance fidelity without loss of structural accuracy.
