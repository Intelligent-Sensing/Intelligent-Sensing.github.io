---
title: "Acoustic Neural 3D Reconstruction Under Pose Drift"
authors:
    - Tianxiang Lin
    - Mohamad Qadri
    - Kevin Zhang
    - Adithya Pediredla
    - Christopher A. Metzler
    - Michael Kaess
links:
    paper: https://arxiv.org/abs/2503.08930
venue: IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
date: 2025-10-19
---

We consider the problem of optimizing neural implicit surfaces for 3D reconstruction using acoustic images collected with drifting sensor poses. The accuracy of current state-of-the-art 3D acoustic modeling algorithms is highly dependent on accurate pose estimation; small errors in sensor pose can lead to severe reconstruction artifacts. In this paper, we propose an algorithm that jointly optimizes the neural scene representation and sonar poses by parameterizing the 6DoF poses as learnable parameters and backpropagating gradients through the neural renderer and implicit representation. We validate our algorithm on both real and simulated datasets, showing that it produces high-fidelity 3D reconstructions even under significant pose drift.
