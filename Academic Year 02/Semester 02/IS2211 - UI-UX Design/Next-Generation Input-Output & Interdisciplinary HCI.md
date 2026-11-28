This topic note analyzes **next-generation input sensing pipelines** and **non-desktop output modalities**—covering sensor featurization, machine learning classification trade-offs, the Midas Touch false-positive dilemma, comparative trade-offs across Nontraditional Displays, Augmented Reality (AR), and Virtual Reality (VR), and an interdisciplinary HCI case study spanning perceptual haptics.

---

# 1. Sensor-Driven Input Architectures

Moving beyond standard mice, keyboards, and glass touchscreens requires capturing rich physical, acoustic, bioelectric, and electromagnetic human intent across the surrounding environment. Modern ubiquitous input systems—evolving directly from Richard Bolt's foundational *"Put-That-There"* multimodal voice-and-gesture prototype (SIGGRAPH '80)—relax rigid closed-world constraints using a unified **3-Stage Sensing Architecture**.

![[sensing_input_pipeline_and_output_modalities.png]]

## 1.1 The Three-Stage Sensing Pipeline

1. **Stage 1: Raw Sensor Acquisition:** Collecting high-frequency physical signals via commodity or wearable transducers:
   - *On-Body Acoustic Vibration (Skinput [Harrison et al. 2010]):* Uses resonant biomechanical vibration sensors strapped to the forearm to turn human skin into an acoustic touch input surface.
   - *Environmental Audio (Ubicoustics [Laput et al. 2018]):* Uses standard laptop or smartwatch microphones to recognize domestic events (running faucets, blenders, door knocks)—directly evolving into **Apple Watch's automatic handwashing detection**.
   - *60 GHz Millimeter-Wave Radar (Google Soli [Lien et al. 2016]):* Emits wide radio beams capturing micro-Doppler reflections from subtle sub-millimeter finger rubs and thumb snaps beyond screen bezels.
   - *Muscle Electromyography (EMG [Saponas et al. 2009]):* Forearm sensor bands read electrical action potentials fired by muscles prior to physical movement, enabling silent gesture detection.
   - *Additional Modalities:* Inertial accelerometers, video streams, whole-body RF antennas (*Humantenna* [Cohn 2012]), and ambient electromagnetic noise (*EM-Sense*).
2. **Stage 2: Domain-Specific Featurization (Feature Engineering):** Transforming noisy, high-bitrate raw waveforms into compact, maximally informative feature vectors for ML models:
   - *Audio & Vibration:* Applying **Fast Fourier Transforms (FFTs)** to extract frequency spectrograms, mean energy amplitudes, and inter-sensor amplitude ratios.
   - *Radar Reflections:* Computing spatial locations of RF scatter centers and their temporal velocity/motion trajectories.
   - *EMG Signals:* Partitioning waveforms into sliding windows to calculate **Root Mean Square (RMS)** ratios, frequency band energy, and cross-channel phase coherence.
3. **Stage 3: Classifier Training & Deployment Constraints:** Choosing model complexity based on deployment targets:
   - *Option A — High-Capacity Deep Learning:* Maximizes accuracy across complex domain shifts (e.g., *IMU2Doppler* [Bhalla, Goel, & Khurana 2021]) when unconstrained cloud or GPU compute is available.
   - *Option B — Low-Power Embedded Models:* Deploys lightweight classical classifiers (e.g., Random Forests or quantized decision trees used in *Google Soli*) when operating under tight mobile CPU, thermal, and battery envelopes.

```python
# THREE-STAGE SENSING PIPELINE CONCEPTUAL ARCHITECTURE (Audio / Vibration)
import numpy as np

def stage2_featurize_window(raw_samples: np.ndarray, sample_rate: int = 16000) -> np.ndarray:
    """
    Converts raw 1D acoustic/vibration transducer signal into frequency-domain features.
    """
    # 1. Apply Hann window to mitigate spectral leakage before FFT
    windowed = raw_samples * np.hanning(len(raw_samples))
    # 2. Compute magnitude spectrum (Fast Fourier Transform)
    fft_magnitudes = np.abs(np.fft.rfft(windowed))
    # 3. Extract RMS energy + dominant spectral centroid features for lightweight classifier
    rms_energy = np.sqrt(np.mean(raw_samples ** 2))
    spectral_peaks = fft_magnitudes[:32] / (np.sum(fft_magnitudes) + 1e-8)
    return np.concatenate(([rms_energy], spectral_peaks))

def stage3_predict_with_midas_guard(features: np.ndarray, model, threshold: float = 0.88) -> str:
    """
    Executes embedded classification while guarding against Midas Touch false activations.
    """
    probs = model.predict_proba([features])[0]
    if np.max(probs) < threshold:
        return "IGNORE_AMBIENT_NOISE"  # Mitigates accidental triggering
    return model.classes_[np.argmax(probs)]
```

## 1.2 The Midas Touch Challenge
- **Implicit Intent Risk:** Unlike graphical buttons that wait explicitly for deliberate cursor clicks, continuous passive sensors interpret ambient life continuously.
- **False Positive Fatigue:** Everyday gestures or background conversations frequently mimic command signatures, triggering unwanted system activations (e.g., smart speakers falsely waking whenever someone mentions the name *"Alexa"* in conversation).
- **Engineering Countermeasures:** Designers implement **activation clutches** (explicit squeeze/pinch wake gestures), multi-modal verification (gaze + voice), and strict probabilistic confidence thresholds before committing state-changing actions.

---

# 2. Beyond Rectangular Monitors: Output Modalities & Trade-offs

When ubiquitous computation detaches from desktop desks, interfaces can no longer rely on users staring into stationary monitors. Contemporary HCI splits non-traditional output across three distinct technological paradigms:

## 2.1 Paradigm 1: Nontraditional Displays
- **Core Objective:** Embed output capabilities directly into human skin, garments, everyday physical artifacts, or autonomous swarms.
- **Representative Systems:**
  - *Epidermal & Textile Displays:* Ultra-thin ($35\mu\text{m}$) feel-through electro-tactile skin tattoos (*Tacttoo* [Withana 2018]), *Skintillates* on-body stickers [Lo 2016], and programmable light-woven fashion fabrics (*Ambient Experiments* [Daguin 2021]).
  - *3D-Printed Optics & Physical Swarms:* Optical light pipes fabricated inside 3D-printed parts (*Printed Optics* [Willis 2012]), motorized desktop robot swarms (*Zooids* [Le Goc 2016]), and flying luminous spherical drones (*iSphere* [Yamada 2017]).
- **Architectural Trade-off:** Offers extraordinary physical form-factor creativity, yet suffers from **specialized hardware fragility**, complex battery/power routing, and poor software generalization across devices.

## 2.2 Paradigm 2: Augmented Reality (AR) & Mixed Reality
- **Core Objective:** Sense physical room geometry in real time and project/overlay contextually anchored digital information directly onto physical surfaces.
- **Implementation Approaches:**
  - *Projector-Based Spatial AR:* Wearable shoulder depth-camera projectors turning skin or notebooks into interactive surfaces (*OmniTouch* [Harrison, Benko, & Wilson 2011]) or steerable room projectors (*Beamatron* [Wilson 2012]).
  - *Optical See-Through Head-Mounted Displays (HMDs):* Devices like Microsoft *HoloLens 2* deliver true **Mixed Reality**, enabling virtual holograms to collide with, occlude behind, and react to physical furniture.
- **Architectural Trade-off:** Enhances real-world workflows without blinding the user to physical safety, yet visual **"seams"** (luminance mismatch, narrow field of view, alignment jitter) expose the boundary between digital overlays and physical atoms.

## 2.3 Paradigm 3: Virtual Reality (VR)
- **Core Objective:** Completely occlude the surrounding physical room using head-worn stereoscopic displays, transporting the user into a synthetic computational environment (*"The Wonderland into which Alice walked"* — Ivan Sutherland, *The Ultimate Display*, 1965).
- **Architectural Trade-off:** Delivers unmatched sensory immersion and unconstrained spatial simulation, yet severs awareness of physical surroundings—causing catastrophic illusion breaks when users bump into physical walls or furniture.

| Output Modality | Physical World Coupling | Hardware / Power Burden | Immersion vs. Awareness | Key Limitation |
| :--- | :--- | :--- | :--- | :--- |
| **Nontraditional Displays** | Embedded directly into skin, clothing, or objects | Very High (custom hardware & micro-batteries) | High real-world situational awareness | Extremely difficult to generalize and manufacture at scale |
| **Augmented Reality (AR)** | Digital overlays spatially anchored to live rooms | High (SLAM spatial tracking + optical waveguides) | Balanced dual reality | Noticeable optical/tracking seams between physical & virtual |
| **Virtual Reality (VR)** | Fully occludes physical environment | Moderate–High (headset optics + tracking) | Total synthetic immersion | Zero environmental safety awareness; physical collision risk |

---

# 3. HCI Interdisciplinarity: A Case Study in Haptic Illusions

A defining characteristic of modern HCI is its **interdisciplinary synthesis**. HCI is not merely visual UI styling—an HCI breakthrough can emerge simultaneously from an optimization algorithm, a psychological experiment, critical theory, hardware engineering, or creative interaction design. Each contribution must be evaluated rigorously **on its own disciplinary terms**.

![[hci_interdisciplinary_haptics_loop.png]]

## 3.1 Solving "Can't Touch This" Across Four Perspectives
A perennial bottleneck in VR and AR is the absence of tactile resistance: photorealistic virtual objects possess no physical mass, causing fingers to slice cleanly through solid digital surfaces. While purely mechanical hardware solutions like robotic exoskeletons (*PHANToM* [Massie & Salisbury 1994]) and weight-simulating controllers (*Grabity* [Choi 2017]) help, perceptual research reveals a far cleaner interdisciplinary solution—**Haptic Illusions**:

1. **Psychology & Social Science — The Visual Dominance Effect [Rock & Victor 1964]:**
   - *Empirical Discovery:* When tactile proprioception conflicts with visual perception, the human brain instinctively resolves the discrepancy in favor of **vision**.
   - *Classic Experiment:* Participants viewed a square block through optically distorting lenses while simultaneously touching it; afterward, participants sketched the **visually distorted shape** they saw—completely unaware that their sense of touch had felt a square.
2. **Systems Engineering — Haptic Retargeting [Azmandian et al. 2016]:**
   - *Algorithmic Innovation:* Exploiting Visual Dominance, engineers subtly warp the rendered 3D coordinates of a user's virtual hand as they reach out in VR.
   - *Result:* A single stationary wooden cube sitting on a physical desk dynamically maps onto *three separate virtual cubes* at different virtual locations—giving the user convincing physical touch across multiple digital objects with minimal hardware.
3. **HCI Theory — Crafting the Impossible [Abtahi et al. 2022]:**
   - *Theoretical Reframing:* Rather than slavishly mimicking mundane Earth physics in VR, designers should embrace **beyond-real capabilities**—dynamically scaling up arm reach across rooms or magnifying avatar stride length to maximize human efficacy.
4. **Interaction Design — TurkDeck [Cheng et al. 2015]:**
   - *Creative Low-Tech Reframing:* Instead of waiting decades for complex full-room motorized robotics, designers orchestrated human stagehands carrying lightweight foam walls, doors, and switches synchronized precisely to a VR headset user's path—delivering seamless, whole-room tactile realism instantly.

> [!tip] Evaluating Research Across HCI Disciplines
> When critiquing or reading interdisciplinary HCI work, apply a structured **3-Step Synthesis Protocol**:
> 1. **Reflection:** Articulate the author's core contribution and why it makes sense from *their* disciplinary lens (Engineering vs. Social Science vs. Design vs. Theory).
> 2. **Synthesis:** Assess persuasiveness on its own disciplinary terms (avoid rejecting a Design paper because it lacks a 500-person statistical field study).
> 3. **Future Work:** Identify novel downstream implications or follow-up prototypes inspired by the idea.

---

# Lecture Notes
![[IS2211 - 07b. Next-Generation Input-Output & Interdisciplinary HCI.pdf]]
