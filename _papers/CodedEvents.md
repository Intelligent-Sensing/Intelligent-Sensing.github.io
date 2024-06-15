---
title: "CodedEvents: Optimal Point-Spread-Function Engineering for 3D-Tracking with Event Cameras"
authors:
    - Sachin Shah
    - Matthew A. Chan
    - Haoming Cai
    - Jingxi Chen
    - Sakshum Kulshrestha
    - Chahat Deep Singh
    - Yiannis Aloimonos
    - Christopher A. Metzler
links:
    paper: https://openaccess.thecvf.com/content/CVPR2024/html/Shah_CodedEvents_Optimal_Point-Spread-Function_Engineering_for_3D-Tracking_with_Event_Cameras_CVPR_2024_paper.html
venue: Conference on Computer Vision and Pattern Recognition (CVPR)
date: 2024-06-01
---

Point-spread-function (PSF) engineering is a well-established computational imaging technique that uses phase masks and other optical elements to embed extra information (e.g., depth) into the images captured by conventional CMOS image sensors. To date, however, PSF-engineering has not been applied to neuromorphic event cameras; a powerful new image sensing technology that responds to changes in the log-intensity of light.
This paper establishes theoretical limits (Cramér Rao bounds) on 3D point localization and tracking with PSF-engineered event cameras. Using these bounds, we first demonstrate that existing Fisher phase masks are already near-optimal for localizing static flashing point sources (e.g., blinking fluorescent molecules). We then demonstrate that existing designs are sub-optimal for tracking moving point sources and proceed to use our theory to design optimal phase masks and binary amplitude masks for this task. To overcome the non-convexity of the design problem, we leverage novel implicit neural representation based parameterizations of the phase and amplitude masks. We demonstrate the efficacy of our designs through extensive simulations. We also validate our method with a simple prototype.
