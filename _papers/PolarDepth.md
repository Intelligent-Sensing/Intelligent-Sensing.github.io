---
title: "PolarDepth: Polarization-Guided Monocular Depth for Visual Odometry"
authors:
    - Naitri Rajyaguru
    - Tianfu Wang
    - Aryan Tajne
    - Botao He
    - Jiayi Wu
    - Cornelia Fermuller
    - Christopher A. Metzler
    - Yiannis Aloimonos
links:
    paper: https://ieeexplore.ieee.org/abstract/document/11488501
venue: IEEE Robotics and Automation Letters (RA-L)
date: 2026-04-20
---

Glass surfaces remain challenging for indoor robot perception: depth sensors and standard RGB monocular frameworks consistently fail on transparent, low-texture, and reflective regions. To this end, we present PolarDepth, a polarization-enhanced monocular depth framework for glass-dominant environments. Using a single polarization sensor, we obtain a standard RGB image together with polarization cues, which we encode as a three-channel "Polar-RGB" input. Our network independently predicts depth from RGB and Polar-RGB and fuses them with a learned per-pixel reliability gate that trusts RGB in diffuse regions while emphasizing polarization cues on reflective glass. Designed to integrate with RGB-trained foundation depth models, PolarDepth substantially reduces tracking errors in glass-walled environments for downstream visual odometry.
