User research bridges the gap between assumptions and human reality by gathering qualitative empathy and quantitative behavioral evidence to define genuine user needs. This guide details the research taxonomy, interview and survey protocols, data synthesis via affinity mapping, 4-quadrant empathy maps, and evidence-based user persona construction.

---

# 1. Foundations & Strategic Value of User Research

User research is the systematic investigation of target users, their work contexts, mental models, pain points, and aspirational goals to inform human-centered product strategy.

- **The False Consensus Effect:** Software engineers and product designers frequently commit the cognitive bias of assuming that end users think, navigate, and react just as they do. Empirical user research actively dismantles this bias by substituting speculation with verifiable observational data.
- **The IDEO Dictum:** As articulated by global design firm IDEO, *"Design for people, not for yourself."* Successful digital products succeed because they resolve authentic human friction rather than showcasing clever engineering capabilities.
- **Rework Cost Amortization (Boehm's Law):** Identifying a fundamental user flow defect during the early research and empathy phase costs approximately $1\times$ to resolve. Remediating that identical usability flaw during Figma high-fidelity prototyping costs roughly $10\times$, whereas refactoring a shipped, backend-integrated production codebase costs upwards of $100\times$.
- **Continuous Research Cadence:** Research is not an isolated initial hurdle; it spans two complementary modes across the product lifecycle:
	- **Exploratory (Generative) Research:** Conducted during the initial *Empathize* and *Define* phases to uncover latent problems, unarticulated workflows, and domain opportunities.
	- **Evaluative (Formative & Summative) Research:** Executed during and after the *Prototype* and *Test* phases to assess whether specific interface mechanisms satisfy user expectations and performance benchmarks.

```
       [ Exploratory Research ] ─────────► [ Ideation & Prototyping ]
        (Uncover Latent Needs)                 (Figma UI / Flows)
                 ▲                                     │
                 │                                     ▼
       [ Continuous Discovery ] ◄───────── [ Evaluative Testing ]
        (Telemetry & Analytics)             (Usability Audits / SUS)
```

---

# 2. Methodological Taxonomy: Christian Rohrer’s Research Matrix

To select the appropriate research instrument, designers utilize Christian Rohrer’s three-dimensional framework: **Qualitative vs. Quantitative**, **Behavioral (What users do) vs. Attitudinal (What users say)**, and **Context of Product Use**.

![[user_research_methods_matrix.png]]

### 2.1 The Two Primary Axes

- **Qualitative Dimension ("Why" & "How"):** Generates descriptive data, direct observations, emotional responses, and conceptual models. Answers *why* users struggle and *how* to repair the conceptual disconnect.
- **Quantitative Dimension ("How Many" & "How Much"):** Yields numerical, statistically verifiable datasets. Measures user success rates, task completion times, drop-off funnels, and benchmark metrics.
- **Behavioral Dimension ("What People Do"):** Directly records actual, unprompted user actions in a real or simulated operational context.
- **Attitudinal Dimension ("What People Say"):** Captures self-reported beliefs, stated perceptions, and expressed satisfaction levels (which often contradict actual behavior due to cognitive biases).

### 2.2 Comparative Analysis of Core Research Methodologies

| Research Method | Primary Axis | Focus Question | Sample Size ($N$) | Cost / Speed | Key Deliverable |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **User Interviews** | Qualitative / Attitudinal | Why do users experience friction? | $5 - 12$ | Low / Rapid | Raw interview transcripts, key thematic quotes |
| **Contextual Inquiry** | Qualitative / Behavioral | How do users execute tasks in situ? | $4 - 8$ | Moderate / Fieldwork | Environmental work models, physical workarounds |
| **Think-Aloud Testing** | Qualitative / Behavioral | Where does cognitive confusion occur? | $5$ per iteration | Low / Iterative | Usability defect logs, verbalized mental models |
| **Card Sorting (Open)** | Qualitative / Attitudinal | How do users mentally classify items? | $15 - 30$ | Low / Digital | Category clusters, dendrograms for IA |
| **Likert Surveys / SUS** | Quantitative / Attitudinal | How satisfied/confident are users? | $50 - 500+$ | Low / Automated | Normalized usability percentile ($0 - 100$) |
| **A/B Testing** | Quantitative / Behavioral | Which design variation yields higher conversion? | $1,000+$ | High / Scaled | Statistically significant conversion $\Delta\%$ |
| **Clickstream / Telemetry** | Quantitative / Behavioral | Where do users abandon the workflow? | Entire userbase | Automated / SaaS | Drop-off funnel analysis, heatmap overlays |

> [!important] The Triangulation Imperative
> Never rely on a single research methodology. Relying solely on attitudinal surveys exposes your design to self-reporting bias (users often say what makes them look competent or what they think the researcher wants to hear). Always **triangulate** attitudinal feedback with behavioral observation (e.g., pairing interviews with think-aloud usability testing and analytics drop-off logs).

---

# 3. Qualitative Research Methodologies

Qualitative inquiry provides deep contextual understanding, discovering the underlying motivations and cognitive friction that metrics alone cannot reveal.

## 3.1 Semi-Structured User Interviews

Semi-structured interviews utilize a standardized guide of open-ended questions while granting the researcher latitude to probe unexpected insights.

- **Open-Ended Phrasing:** Frame inquiries with *"How"*, *"Why"*, or *"Walk me through the last time you..."* to elicit narrative responses rather than binary *"Yes/No"* replies.
- **Neutrality & Non-Leading Questions:** Avoid prompting preferred answers.
	- ❌ *Leading Question:* "Do you think our study room booking app is much easier than checking WhatsApp?"
	- ✅ *Neutral Inquiry:* "How do you currently find out if a study room is vacant during peak hours?"
- **The "Five Whys" Root Cause Technique:** When an interviewee expresses a surface preference or frustration, gently probe deeper with successive "Why" questions to uncover systemic root causes.
- **Ethical Informed Consent:** Always obtain written or explicit recorded consent before starting an interview session, assuring confidentiality and GDPR/data privacy compliance.

## 3.2 Contextual Inquiry & Observational Shadowing

Contextual inquiry observes users in their natural operational environment while they perform genuine day-to-day tasks.

- **The Master-Apprentice Relationship:** The researcher adopts the posture of an apprentice learning a craft from a master craftsman, observing actions directly and asking clarifying questions without lecturing or offering unsolicited advice.
- **Physical Artifact Inspection:** Note sticky notes attached to computer monitors, unofficial paper cheat-sheets, duplicate browser tabs, or external calculator usage—these physical artifacts identify major gaps in the digital system's capabilities.

## 3.3 The Concurrent Think-Aloud (CTA) Protocol

Pioneered by Clayton Lewis and cognitive psychology, the think-aloud protocol requires participants to verbalize their inner monologue continuously while interacting with an interface.

- **Protocol Execution:** Prompt the participant: *"Please speak your thoughts out loud as you attempt to reserve hall B. Tell me what you are looking at, what you expect to happen, and whenever you feel uncertain."*
- **Researcher Facilitation:** Maintain silence during tasks; intervene only with neutral prompts when the participant goes silent: *"What are you thinking right now?"*
- **Nielsen's 5-User Rule:** Jakob Nielsen demonstrated that testing with **5 users** uncovers approximately $85\%$ of qualitative usability defects, after which diminishing returns set in:

$$U(n) = N \cdot \left(1 - (1 - L)^n\right)$$

Where $U(n)$ is the proportion of usability problems found, $n$ is the number of test participants, and $L$ is the proportion of usability problems discovered by a single evaluator (typically $L \approx 0.31$).

```
Usability Problems Found (%)
100% ┌───────────────────────────────────────────-·
 85% ├────────────────────────────● (5 Users)
     │                       ●
     │                  ●
     │             ●
     │        ●
  0% └────────┴────────┴────────┴────────┴────────┴─
     0        1        2        3        4        5   (Number of Test Users)
```

---

# 4. Quantitative Research & Usability Metrics

Quantitative research validates patterns across larger cohorts, providing measurable criteria for feature viability and redesign success.

## 4.1 Survey Instrument Architecture & Bias Mitigation

- **Brevity & Focus:** Limit exploratory surveys to under 10 focused questions to prevent participant fatigue and straight-lining (hastily clicking identical radio buttons).
- **Eliminating Double-Barreled Items:** Avoid joining distinct attributes into a single rating.
	- ❌ *Double-Barreled:* "Rate the usefulness and visual attractiveness of the navigation bar."
	- ✅ *Separated Items:* Item 1: "The navigation bar made it easy to find what I needed." / Item 2: "The visual design of the navigation bar was clear."
- **Standardized Likert Scales:** Utilize symmetrical, 5-point or 7-point Likert scales with explicit anchor labels:
	- $1 =$ Strongly Disagree, $2 =$ Disagree, $3 =$ Neutral, $4 =$ Agree, $5 =$ Strongly Agree.

## 4.2 System Usability Scale (SUS) Standardization

The System Usability Scale (SUS) is a globally recognized, 10-item standardized questionnaire yielding a single usability percentile score between $0$ and $100$.

- **Alternating Polarization:** SUS alternates between positive (odd questions: 1, 3, 5, 7, 9) and negative (even questions: 2, 4, 6, 8, 10) assertions to counteract acquiescence bias.
- **Mathematical Score Calculation:**
	- For each odd item ($1, 3, 5, 7, 9$), subtract 1 from the raw response: $S_i = R_i - 1$.
	- For each even item ($2, 4, 6, 8, 10$), subtract the raw response from 5: $S_i = 5 - R_i$.
	- Sum the 10 adjusted scores and multiply by $2.5$:

$$\text{SUS Score} = 2.5 \times \sum_{i=1}^{10} S_i$$

```python
def calculate_sus_score(responses: list[int]) -> float:
    """
    Computes normalized System Usability Scale (SUS) score from 10 raw Likert responses (1 to 5).
    """
    assert len(responses) == 10, "SUS requires exactly 10 responses"
    
    score_contributions = []
    for index, val in enumerate(responses):
        assert 1 <= val <= 5, f"Response out of bounds: {val}"
        if index % 2 == 0:  # Odd items (1-indexed: 1, 3, 5, 7, 9)
            score_contributions.append(val - 1)
        else:               # Even items (1-indexed: 2, 4, 6, 8, 10)
            score_contributions.append(5 - val)
            
    raw_sum = sum(score_contributions)
    sus_composite = raw_sum * 2.5
    return sus_composite

# Example: Highly usable application evaluation
sample_responses = [5, 1, 4, 1, 5, 2, 4, 1, 5, 2]
score = calculate_sus_score(sample_responses)
print(f"Calculated SUS Score: {score}/100") # Output: 80.0 (Grade A / Excellent)
```

> [!tip] Interpreting SUS Benchmarks
> The historical industry average for a SUS score is **$68.0$**. A score below $68$ indicates serious usability friction requiring remedial redesign. A score above **$80.3$** indicates top-quartile usability (Grade A), qualifying the system as highly recommended and intuitive.

---

# 5. Data Synthesis & Affinity Mapping

Raw interview transcripts and observational recordings must be processed systematically into actionable engineering specifications.

## 5.1 The Affinity Diagramming Workflow

1. **Extraction (Divergence):** Read through all interview transcripts and notes. Record discrete observations, verbatim quotes, user frustrations, and observed behaviors onto individual notes (one thought per note).
2. **Cluster Grouping (Convergence):** Spread the notes onto a shared canvas (physical whiteboard or Miro/FigJam). Allow the team to silently reorganize notes into natural semantic clusters based on shared themes rather than predefined categories.
3. **Hierarchy Labeling:** Assign concise header cards to each cluster summarizing the root insight (e.g., *"Unreliable notification delivery during schedule changes"*).
4. **Insight Prioritization:** Vote on the most critical themes using dot voting to establish foundational design requirements.

## 5.2 User Story Formulation (JTBD Alignment)

Convert affinity clusters into structured User Stories and Jobs To Be Done (JTBD) frameworks:

$$\text{As a } [\text{Persona Role}], \text{ I want to } [\text{Execute an Action}], \text{ so that } [\text{Achieve Core Value/Benefit}].$$

- **Example 1:** *"As an undergraduate commuting between classes, I want to view live seat availability on my phone with a single tap, so that I don't waste 20 minutes walking to a full library."*
- **Example 2:** *"As a student study group leader, I want to book a room and share calendar invitations directly to WhatsApp, so that our study group arrives on time without scheduling confusion."*

---

# 6. Empathy Mapping Framework

An empathy map is a collaborative visualization tool developed to synthesize qualitative research, establishing shared team empathy and exposing discrepancies between stated intentions and actual behavior.

![[empathy_map_structure.png]]

### 6.1 The Four Core Quadrants

1. **SAYS (Explicit Statements):**
	- Verbatim phrases spoken during interviews or focus groups.
	- *"I never check my university email during the weekend."*
	- *"The room reservation portal feels like it was designed 15 years ago."*
2. **THINKS (Mental Models & Unexpressed Thoughts):**
	- Internal beliefs, anxieties, and expectations that the user might hesitate to say aloud.
	- *"Am I making a fool of myself by asking the lab instructor for help?"*
	- *"Other students probably wrote scripts to snag rooms before anyone else."*
3. **DOES (Observable Actions & Physical Behaviors):**
	- Verifiable physical or digital actions taken to achieve goals.
	- Refreshes browser repeatedly at 7:59 AM.
	- Relies on informal batch WhatsApp chats to ask who is currently occupying lab desks.
4. **FEELS (Emotional & Affective States):**
	- Visceral emotional reactions throughout the user journey.
	- Overwhelmed by dense academic schedules, anxious about missing assignment deadlines, relieved when finding a quiet workspace with power outlets.

### 6.2 Pains and Gains Synthesis

- **Pains (Impediments & Fears):** Roadblocks, hidden costs, and points of cognitive failure (e.g., traveling across campus in the rain only to find an occupied room).
- **Gains (Aspirations & Success Metrics):** What makes the user feel empowered, efficient, and successful (e.g., instant booking confirmation and real-time quiet-zone indicators).

---

# 7. Constructing Evidence-Based User Personas

A user persona is an evidence-based archetype representing a distinct cluster of actual users who share behavioral patterns, mental models, goals, and operational environments.

![[user_persona_breakdown.png]]

## 7.1 Key Structural Elements of a Persona

- **Profile Identifier:** Realistic name, non-celebrity photograph, age, academic/professional role, and a summarizing archetype quote.
- **Demographics & Digital Literacy:** Daily operating devices (iOS, Android, Linux, macOS), tech fluency, and primary internet access constraints.
- **Core Goals & Motivations:** What the persona seeks to accomplish within the application context. Must focus on outcomes rather than specific UI controls.
- **Frustrations & Pain Points:** Concrete obstacles preventing the persona from reaching their desired goals.
- **Context of Use:** Physical, temporal, and emotional environment in which the application is operated.

## 7.2 Persona Anti-Patterns to Avoid

- **The "Proto-Persona" Fallacy:** Creating fictional characters based solely on team guesswork and stereotypes without conducting real empirical user interviews or observation.
- **The "Average User" Myth:** Attempting to design for an "average user" results in an elastic persona that pleases no one. Formulate $2 - 3$ distinct, sharply focused primary personas representing distinct user segments.
- **Irrelevant Trivia:** Avoid padding personas with extraneous details (e.g., favorite food, pet names) that have zero bearing on the digital product's functional requirements.

---

# 8. Context of Use & Hierarchical Task Analysis (HTA)

Designing robust systems requires analyzing the external environmental conditions and structural task breakdowns.

## 8.1 The Three Dimensions of Context

1. **Physical Environment:** Lighting conditions (glare from bright sun vs. dark study halls), acoustic noise, spatial constraints, and whether the user is stationary or walking while operating the interface.
2. **Technical Constraints:** Network stability, bandwidth fluctuations on campus Wi-Fi, battery life limitations, screen real estate, and touch target accessibility for one-handed thumb use.
3. **Social & Cognitive Context:** Level of cognitive fatigue, split attention (listening to a lecture while glancing at notifications), and privacy considerations in public computer labs.

## 8.2 Hierarchical Task Analysis (HTA) Example

HTA deconstructs an overall user goal into nested sub-tasks and operational plans:

```
Goal 0: Reserve a Campus Study Space for 2 Hours
  Plan 0: Do 1 -> 2 -> 3. If no rooms available in 2, do 4.
  1. Determine space requirements (Capacity >= 4, Quiet zone, Power outlets)
  2. Inspect available rooms:
       2.1 Open UCSC Campus Map / Room Directory
       2.2 Filter by current time window and feature tags
       2.3 Review room availability status
  3. Confirm selection:
       3.1 Tap "Reserve Slot"
       3.2 Authenticate with UCSC Student Single Sign-On (SSO)
       3.3 Receive QR Pass on smartphone wallet
  4. Contingency fallback:
       4.1 Subscribe to waitlist alert notifications
       4.2 Search alternative study common areas
```

---

# Lecture Notes
![[IS2211 - 02. User Research & Personas.pdf]]
