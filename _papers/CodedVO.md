---
title: "CodedVO: Coded Visual Odometry"
authors:
    - Sachin Shah*
    - Naitri Rajyaguru*
    - Chahat Deep Singh
    - Christopher A. Metzler**
    - Yiannis Aloimonos**
links:
    paper: https://ieeexplore.ieee.org/document/10564186
    project: https://prg.cs.umd.edu/CodedVO
venue: IEEE Robotics and Automation Letters (RA-L)
date: 2024-06-19
---

Autonomous robots often rely on monocular cameras for odometry estimation and navigation. However, the scale ambiguity problem presents a critical barrier to effective monocular visual odometry. In this paper, we present CodedVO, a novel monocular visual odometry method that overcomes the scale ambiguity problem by employing custom optics to physically encode metric depth information into imagery. By incorporating this information into our odometry pipeline, we achieve state-of-the-art performance in monocular visual odometry with a known scale. We evaluate our method in diverse indoor environments and demonstrate its robustness and adaptability. We achieve a 0.08m average trajectory error in odometry evaluation on the ICL-NUIM indoor odometry dataset.
