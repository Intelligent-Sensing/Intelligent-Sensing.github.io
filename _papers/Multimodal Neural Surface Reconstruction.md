---
title: "Multimodal Neural Surface Reconstruction: Recovering the Geometry and Appearance of 3D Scenes from Events and Grayscale Images"
authors:
    - Sazan Mahbub
    - Brandon Y. Feng
    - Christopher A. Metzler
links:
    paper: https://openreview.net/pdf?id=8hz6X2GGnD
venue: NeurIPS Workshop on Deep Learning and Inverse Problems
date: 2023-11-03
---

Event cameras offer high frame rates, minimal motion blur, and excellent dynamic
range. As a result they excel at reconstructing the geometry of 3D scenes. However,
their measurements do not contain absolute intensity information, which can make
accurately reconstructing the appearance of 3D scenes from events challenging.
In this work, we develop a multimodal neural 3D scene reconstruction framework
that simultaneously reconstructs scene geometry from events and scene appearance
from grayscale images. Our framework—which is based on neural surface representations, as opposed to the neural radiance fields used in previous works—is able
to reconstruct both the structure and appearance of 3D scenes more accurately than
existing unimodal reconstruction methods.
