---
title: "High-Resolution Range Profile Target Recognition with Neuromorphic ADCs and Spiking Neural Networks"
authors:
    - Sanjaya Herath
    - Matthew R. Ziemann
    - Kevin Wagner
    - Christopher A. Metzler
links:
    paper: https://ieeexplore.ieee.org/abstract/document/10549488
venue: IEEE Radar Conference
date: 2024-06-13
---

Traditional analog-to-digital converters (ADCs) often struggle to balance high sampling rates with power efficiency, limiting their effectiveness in advanced radar and communication systems. Neuromorphic ADCs capture samples only when a signal crosses a specific threshold. This asynchronous sampling strategy effectively compresses incoming datastreams, enabling neuromorphic ADCs to achieve higher sampling rates at reduced power consumption compared to conventional ADCs. However, existing algorithms are poorly suited for processing the asynchronous samples. Conventional techniques like matched filters are inapplicable and most established deep learning algorithms expect regularly sampled data. This work introduces a spiking neural network (SNN) architecture specifically designed for processing asynchronous radar samples. Our novel approach is applied to Radar High-Resolution Range Profile (HRRP) based target classification. Remarkably, our experiments demonstrate that combining a neuromorphic ADC with an SNN achieves performance on par with high-sample-rate conventional ADCs paired with Convolutional Neural Networks (CNNs) while reducing the overall sampling rate by more than 95%.
