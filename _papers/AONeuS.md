---
title: "AONeuS: A Neural Rendering Framework for Acoustic-Optical Sensor Fusion"
authors:
    - Mohamad Qadri*
    - Kevin Zhang*
    - Akshay Hinduja
    - Michael Kaess
    - Adithya Pediredla
    - Christopher A. Metzler
links:
    paper: https://arxiv.org/abs/2402.03309
    project: https://aoneus.github.io/
venue: SIGGRAPH
date: 2024-06-02
---

Underwater perception and 3D surface reconstruction are challenging problems with broad applications in construction, security, marine archaeology, and environmental monitoring. Treacherous operating conditions, fragile surroundings, and limited navigation control often dictate that submersibles restrict their range of motion and, thus, the baseline over which they can capture measurements. In the context of 3D scene reconstruction, it is well-known that smaller baselines make reconstruction more challenging. Our work develops a physics-based multimodal acoustic-optical neural surface reconstruction framework (AONeuS) capable of effectively integrating high-resolution RGB measurements with low-resolution depth-resolved imaging sonar measurements. By fusing these complementary modalities, our framework can reconstruct accurate high-resolution 3D surfaces from measurements captured over heavily-restricted baselines. Through extensive simulations and in-lab experiments, we demonstrate that AONeuS dramatically outperforms recent RGB-only and sonar-only inverse-differentiable-rendering--based surface reconstruction methods.