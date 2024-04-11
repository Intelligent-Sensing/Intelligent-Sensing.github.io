---
title: Weakly-Supervised Semantic Segmentation of Ships Using Thermal Imagery
authors:
    - Rushil Joshi*
    - Ethan Adams*
    - Matthew R. Ziemann
    - Christopher A. Metzler
links:
    paper: https://arxiv.org/pdf/2212.13170.pdf
venue: Workshop on Naval Applications of Machine Learning
date: 2023-03-21
---

The United States coastline spans 95,471 miles; a distance that cannot be effectively patrolled or secured by manual human effort alone. Unmanned Aerial Vehicles (UAVs) equipped with infrared cameras and deep-learning based algorithms represent a more efficient alternative for identifying and segmenting objects of interest—namely, ships. However, standard approaches to training these algorithms require large-scale datasets of densely labeled infrared maritime images. Such datasets are not publicly available and manually annotating every pixel in a large-scale dataset would have an extreme labor cost. In this work we demonstrate that, in the context of segmenting ships in infrared imagery, weakly-supervising an algorithm with sparsely labeled data can drastically reduce data labeling costs with minimal impact on system performance. We apply weakly-supervised learning to an unlabeled dataset of 7055 infrared images sourced from the Naval Air Warfare Center Aircraft Division (NAWCAD). We find that by sparsely labeling only 32 points per image, weakly-supervised segmentation models can still effectively detect and segment ships, with a Jaccard score of up to 0.756.
