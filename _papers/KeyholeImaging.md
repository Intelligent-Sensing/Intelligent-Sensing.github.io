---
title: "Keyhole Imaging: Non-Line-of-Sight Imaging and Tracking of Moving Objects Along a Single Optical Path"
authors:
    - Christopher A. Metzler
    - David B. Lindell
    - Gordon Wetzstein
links:
    paper: https://arxiv.org/abs/1912.06727
    code: https://github.com/computational-imaging/KeyholeImaging
venue: IEEE Transactions on Computational Imaging
date: 2021-01-01
---

Non-line-of-sight (NLOS) imaging and tracking is an emerging technology that allows the shape or position of objects around corners or behind diffusers to be recovered from transient, time-of-flight measurements. However, existing NLOS approaches require the imaging system to scan a large area on a visible surface, where the indirect light paths of hidden objects are sampled. In many applications, such as robotic vision or autonomous driving, optical access to a large scanning area may not be available, which severely limits the practicality of existing NLOS techniques. Here, we propose a new approach, dubbed keyhole imaging, that captures a sequence of transient measurements along a single optical path, for example, through a keyhole. Assuming that the hidden object of interest moves during the acquisition time, we effectively capture a series of time-resolved projections of the object's shape from unknown viewpoints. We derive inverse methods based on expectation-maximization to recover the object's shape and location using these measurements. Then, with the help of long exposure times and retroreflective tape, we demonstrate successful experimental results with a prototype keyhole imaging system.
