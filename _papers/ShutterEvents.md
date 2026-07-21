---
title: "ShutterEvents: Shutter Modulation for Static-Dynamic Scene Recovery"
authors:
    - Nevindu M. Batagoda
    - Ramchander Rao Bhaskara
    - Christopher A. Metzler
    - Adithya Pediredla
links:
    paper: https://par.nsf.gov/biblio/10692626
venue: IEEE International Conference on Computational Photography (ICCP)
date: 2026-07-13
---

Event cameras capture changes in log intensity asynchronously, enabling high temporal resolution and dynamic range for dynamic scenes. However, because they respond only to intensity changes, they are fundamentally insensitive to static or slowly varying content, leading existing event-to-video methods to rely on camera motion or hallucinate missing structure. We introduce ShutterEvents, a lightweight sensing framework that enables simultaneous recovery of static and dynamic scene content using a low-cost programmable LCD shutter. By imposing controlled temporal modulation on incoming light, static intensities are transformed into predictable brightness variations that generate informative events even under a stationary camera. We show that the induced mapping between event statistics and scene intensity is injective, enabling learning-free reconstruction of static structure directly from event measurements, and we propose an event decomposition algorithm that separates shutter-induced responses from true scene dynamics. Experiments on simulated and real data demonstrate that ShutterEvents recovers meaningful static structure while preserving dynamic fidelity, without long integration times and with minimal hardware overhead.
