---
title: Seeing the World through Your Eyes
authors:
    - Hadi Alzayer*
    - Kevin Zhang*
    - Brandon Y. Feng
    - Christopher A. Metzler
    - Jia-Bin Huang
links:
    paper: https://openaccess.thecvf.com/content/CVPR2024/html/Alzayer_Seeing_the_World_through_Your_Eyes_CVPR_2024_paper.html
    project: https://world-from-eyes.github.io/
venue: Conference on Computer Vision and Pattern Recognition (CVPR)
date: 2024-06-01
---

The reflective nature of the human eye is an underappreciated source of information about what the world around us looks like. By imaging the eyes of a moving person, we capture multiple views of a scene outside the camera's direct line of sight through the reflections in the eyes. In this paper, we reconstruct a radiance field beyond the camera's line of sight using portrait images containing eye reflections.
This task is challenging due to 1) the difficulty of accurately estimating eye poses and 2) the entangled appearance of the iris textures and the scene reflections. To address these, our method jointly optimizes the cornea poses, the radiance field depicting the scene, and the observer's eye iris texture. We further present a regularization prior on the iris texture to improve scene reconstruction quality. Through various experiments on synthetic and real-world captures featuring people with varied eye colors, and lighting conditions, we demonstrate the feasibility of our approach to recover the radiance field using cornea reflections.
