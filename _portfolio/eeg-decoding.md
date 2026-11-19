---
title: "Adaptive EEG decoding"
order: 2
kicker: Machine learning
summary: "Adapting EEG foundation models to stroke motor imagery, with an emphasis on domain shift and performance for individual users."
excerpt: "Parameter-efficient adaptation and subject-level evaluation of EEG foundation models."
---

Strong performance on healthy-participant EEG does not necessarily transfer to recordings from people with stroke. I study how pretrained EEG models can be adapted and evaluated for motor imagery decoding across individuals.

## Approach

With Zihua Sun and Michelle J. Johnson, I evaluated low-rank adaptation (LoRA) of EEG foundation models for left- versus right-hand motor imagery decoding. Our study compared pretrained representations and adaptation methods using healthy-participant data and a stroke dataset containing 30 participants.

## Main findings

Healthy-to-stroke transfer without adaptation performed near chance. Adaptation improved some models, but performance varied across participants. These findings emphasize the importance of target-domain calibration and subject-level analysis rather than relying only on average accuracy.

## Ongoing direction

I am interested in making EEG decoding more useful for rehabilitation interfaces through reliable calibration, assessment across users and recording conditions, and evaluation of when a model’s output should lead to feedback.

## Related publication

[Lightweight Adaptation of EEG Foundation Models for Stroke Motor Imagery Decoding: Domain Shift and Subject-Level Robustness]({{ '/publications/2026-foundation-models/' | relative_url }}) — preprint, 2026. Equal contribution with Zihua Sun.
