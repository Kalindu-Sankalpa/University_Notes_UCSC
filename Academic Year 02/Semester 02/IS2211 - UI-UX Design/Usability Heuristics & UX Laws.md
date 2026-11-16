Usability inspection methods and psychological interaction laws establish empirical baselines for evaluating and engineering user interfaces before usability defects impact production. This guide details cognitive walkthrough protocols, Don Norman's action cycles, Jakob Nielsen's 10 usability heuristics, and foundational behavioral laws including Fitts's, Hick's, and Miller's laws.

---

# 1. Expert Usability Inspection Frameworks

Expert inspection methods enable interaction designers and human factors specialists to assess interfaces systematically without recruiting large test cohorts, identifying high-severity defects early in the software lifecycle.

- **Discount Usability Engineering:** Coined by Jakob Nielsen, discount usability emphasizes lightweight, cost-effective evaluation techniques (such as heuristic evaluations and cognitive walkthroughs) that can be executed rapidly on paper sketches, Figma wireframes, or working prototypes.
- **The Evaluator Independence Principle:** Designers who authored an interface must never serve as the sole evaluators of their own work. Cognitive bias, familiarity with hidden workarounds, and creator attachment blind designers to interface ambiguities.
- **Optimal Evaluator Cohort:** Research demonstrates that aggregating the independent findings of **3 to 5 usability evaluators** identifies between $75\%$ and $85\%$ of all usability defects. Individual inspectors identify different subsets of issues, but adding beyond 5 evaluators yields diminishing returns relative to resource expenditure.

```
Usability Defects Identified (%)
100% ┌──────────────────────────────────────────────
 80% ├────────────────────────────● (3-5 Evaluators)
     │                       ●
     │                  ●
     │             ●
     │        ● (Single Evaluator: ~35%)
  0% └────────┴────────┴────────┴────────┴──────────
     0        1        2        3        4        5   (Number of Evaluators)
```

---

# 2. Don Norman’s Action Cycle & The Two Gulfs

Human interaction with any technical artifact progresses through Don Norman's Seven Stages of Action, which define two fundamental friction gaps: the **Gulf of Execution** and the **Gulf of Evaluation**.

![[norman_gulfs_interaction_model.png]]

### 2.1 The Seven Stages of Action

1. **Goal Formulation:** Establishing the desired high-level state (e.g., *"I want to submit my course assignment before midnight"*).
2. **Intention Specification:** Determining the sub-goal (e.g., *"Upload the completed PDF file"*).
3. **Action Specification:** Planning the specific sequence of physical manipulations (e.g., *"Click 'Choose File', navigate directory, click 'Open', tap 'Submit'"*).
4. **Action Execution:** Physically manipulating the hardware/input controls (e.g., cursor click, keyboard stroke, touch screen tap).
5. **State Perception:** Sensation of visual, auditory, or haptic sensory signals emitted by the device.
6. **State Interpretation:** Making cognitive sense of the sensory feedback (e.g., recognizing a green checkmark or progress spinner).
7. **Outcome Evaluation:** Comparing the resulting system state against the original goal.

### 2.2 The Gulf of Execution

- **Definition:** The cognitive distance between the user’s formulated goals and the physical actions supported by the interface.
- **The Core Question:** *"How do I make the system do what I want?"*
- **Design Resolution:** Provide obvious signifiers, clear affordances, logical action mappings, and constrain choices to physically valid interactions.

### 2.3 The Gulf of Evaluation

- **Definition:** The cognitive effort required by the user to perceive, decode, and interpret the current state of the system after performing an action.
- **The Core Question:** *"Did the system do what I intended, and what state is it in right now?"*
- **Design Resolution:** Deliver immediate, unambiguous, and perceptible feedback (e.g., status messages, state badges, toast notifications, and audible confirmation).

---

# 3. The Cognitive Walkthrough Protocol

The Cognitive Walkthrough is an action-centered, task-oriented inspection method developed by Wharton, Rieman, Lewis, and Polson that evaluates how easily first-time users can navigate an interface without prior training.

## 3.1 Preparation Prerequisites

Before executing a cognitive walkthrough, the evaluation team must assemble four concrete artifacts:
1. **Target User Profile:** Clear definition of user background knowledge, domain expertise, and digital literacy.
2. **Concrete Task Scenarios:** Representative tasks with a definite starting state and successful termination condition.
3. **Exact Happy Path Sequence:** The optimal, step-by-step action sequence required to complete the task using the interface.
4. **Interface Representation:** Screenshots, paper wireframes, Figma prototypes, or production builds for every single state transition in the sequence.

## 3.2 The Four Core Evaluation Questions

At every discrete action step in the path, evaluators analyze the interface against four mandatory cognitive questions:

1. **Goal Alignment:** *Will the user try to achieve the right effect?*
	- Does the user’s current mental goal match the intended effect of this specific step?
	- *Failure Example:* The system requires selecting a server region first, but the user's primary mental goal is typing their project title.
2. **Affordance Visibility:** *Will the user notice that the correct action is available?*
	- Is the button, link, or input field immediately visible and prominent, or is it hidden inside an unlabelled hamburger menu or below the fold?
	- *Failure Example:* A "Download Invoice" action is hidden inside an obscure three-dot context menu.
3. **Action Identification:** *Will the user associate the correct action with the effect they are trying to achieve?*
	- Does the label, icon, or signifier clearly convey the resulting action, matching the user’s natural vocabulary?
	- *Failure Example:* Labeling an account deletion button as "Prune Partition" instead of "Delete Account".
4. **Feedback Comprehension:** *If the correct action is performed, will the user see that progress is being made toward the solution of the task?*
	- Does the system provide instantaneous, interpretable feedback confirming that the action registered?
	- *Failure Example:* Clicking "Submit Application" produces no loading spinner or confirmation dialog for 5 seconds, causing the user to click repeatedly and trigger duplicate charges.

> [!important] The Walkthrough Failure Log
> Whenever an evaluator answers "No" to any of the four questions, a formal defect log entry must be documented specifying: (1) Step number, (2) User's perceived goal, (3) Exact failure question, and (4) Proposed architectural remediation.

---

# 4. Jakob Nielsen’s 10 Usability Heuristics

Jakob Nielsen and Rolf Molich formulated 10 general rules of thumb for interaction design that remain the industry benchmark for heuristic evaluation.

| # | Nielsen Usability Heuristic | Core Principle | Severe Violation Example | Recommended Remediation Pattern |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **Visibility of System Status** | System must keep users informed about what is happening through appropriate feedback within a reasonable time. | Uploading a 200MB file shows no progress bar or percentage, leaving the user guessing if the browser froze. | Display a persistent animated progress bar, transferred MB counter, and estimated completion time. |
| **2** | **Match Between System & Real World** | The system should speak the user's language with words, phrases, and concepts familiar to them, rather than internal jargon. | Banking app displays an error message stating: `SQL_TRANSACTION_DEADLOCK_EXCEPTION_0x88F`. | Translate technical errors into plain human language: *"Unable to process payment due to a temporary server issue. No funds were deducted."* |
| **3** | **User Control & Freedom** | Users frequently choose actions by mistake and need a clearly marked "emergency exit" to leave the unwanted state. | User accidentally deletes an entire directory with no confirmation or ability to undo. | Provide universal `Ctrl+Z` / `Cmd+Z` undo capabilities, a temporary "Undo" toast banner, and a Trash/Recycle bin recovery window. |
| **4** | **Consistency & Standards** | Users should not have to wonder whether different words, situations, or actions mean the same thing (Jakob's Law). | On one screen, primary actions are green pill buttons; on another screen, they are blue underline text links. | Implement a unified Figma design system with tokenized component libraries enforcing standardized button hierarchies across all screens. |
| **5** | **Error Prevention** | Either eliminate error-prone conditions or check for them and present users with a confirmation option before committing to the action. | Allowing users to type invalid date strings like `32/13/2026` into an open text box, crashing the form upon submit. | Use constrained date pickers, real-time input masks, and disable form submission until all mandatory validation rules pass. |
| **6** | **Recognition Rather than Recall** | Minimize user memory load by making elements, actions, and options visible. Users should not have to remember information from one part of the interface to another. | Multi-step insurance form requires typing an auto-generated policy ID from Step 1 manually into Step 4. | Persist and display the active policy ID and order summary continuously in a sticky sidebar drawer across all wizard steps. |
| **7** | **Flexibility & Efficiency of Use** | Accelerators (unseen by the novice user) may often speed up the interaction for the expert user. | Power users are forced to click through 4 hierarchical drop-down menus every time they want to save a record. | Provide configurable keyboard shortcuts (`Cmd+S`), global command palettes (`Cmd+K`), and recent items quick-access lists. |
| **8** | **Aesthetic & Minimalist Design** | Interfaces should not contain information that is irrelevant or rarely needed. Every extra unit of information competes with relevant units. | An analytics dashboard displays 45 unformatted numerical metric cards simultaneously on the home screen. | Apply progressive disclosure: show top 4 primary KPI indicators prominently, moving secondary telemetry into expandable drill-down tabs. |
| **9** | **Recognize, Diagnose, & Recover from Errors** | Error messages should be expressed in plain language (no codes), precisely indicate the problem, and constructively suggest a solution. | Displaying a generic red banner: *"Submission Failed: Invalid Input."* without pointing to which field failed. | Highlight the exact form field with a red border, focusing the cursor on it, and state: *"Password must contain at least 8 characters and one numerical digit."* |
| **10** | **Help & Documentation** | Even though it is better if the system can be used without documentation, it may be necessary to provide help and documentation that is easy to search. | Help center consists of a 400-page unindexed static PDF file. | Offer contextual in-app tooltips, onboarding micro-tours, and a searchable FAQ knowledge base integrated directly into the application header. |

---

# 5. Psychological UX Laws

User experience is fundamentally governed by human cognitive architecture, sensory processing thresholds, and biomechanical limitations.

![[ux_laws_summary_matrix.png]]

## 5.1 Fitts’s Law: Target Acquisition Ergonomics

Formulated by psychologist Paul Fitts in 1954, Fitts’s Law models the time required to rapidly move to a target area as a function of the target’s distance and width.

![[fitts_law_target_geometry.png]]

### Mathematical Formulation

$$\text{Movement Time } (MT) = a + b \cdot \text{ID} = a + b \cdot \log_2 \left( \frac{2D}{W} \right)$$

- $MT$: Movement time required to reach and click/tap the target.
- $a, b$: Empirical regression constants determined by the input device (e.g., mouse, trackpad, finger, stylus).
- $D$: Distance (amplitude) from the starting position to the center of the target.
- $W$: Width of the target measured along the axis of motion.
- $\text{ID} = \log_2(2D/W)$: The **Index of Difficulty** (measured in bits of information).

### Core Design Implications of Fitts’s Law

- **Desktop Screen Edges Have Infinite Width ($W = \infty$):** In desktop OS environments (such as macOS menu bars or Windows Taskbar), the physical display perimeter halts cursor movement regardless of mouse velocity. This effectively makes edge targets infinite in size, making corner and edge controls the fastest targets to acquire.
- **The Mobile Thumb Zone:** Mobile ergonomics dictate that primary interaction triggers (like "Proceed to Checkout" or navigation bars) should be positioned at the bottom of the viewport where the thumb naturally rests without joint strain.
- **Minimum Touch Target Standards:**
	- **WCAG 2.2 Success Criterion 2.5.8 (Target Size - Minimum):** Minimum $24 \times 24$ CSS pixels.
	- **Apple Human Interface Guidelines (HIG):** Minimum $44 \times 44$ points.
	- **Google Material Design 3:** Minimum $48 \times 48$ density-independent pixels (dp) with at least $8\text{ dp}$ of surrounding clearance.

## 5.2 Hick’s Law (The Hick-Hyman Law): Decision Latency

Formulated by William Edmund Hick and Ray Hyman, this law states that the time it takes to make a decision increases logarithmically with the number of choices presented.

$$\text{Reaction Time } (RT) = b \cdot \log_2(n + 1)$$

- Where $n$ is the number of equally probable alternatives, and $b$ is an empirical cognitive processing constant.
- **UI Application:** Eliminate decision paralysis by chunking large navigational directories, limiting top-level navigation items to $5 - 7$ options, and using **progressive disclosure** (revealing complex secondary parameters only when explicitly requested).

## 5.3 Miller’s Law: Working Memory Span

In 1956, cognitive psychologist George A. Miller published the foundational finding that the human working memory capacity can hold approximately **$7 \pm 2$ chunks** of information simultaneously.

- **Chunking in Interaction Design:** Rather than presenting users with an undifferentiated string of 16 digits, credit card inputs should automatically group numbers into 4 chunks of 4 digits (`4532  8190  2341  1092`).
- **Checkout Wizards:** Long registration or purchasing flows should be partitioned into discrete steps (e.g., `1. Shipping` $\rightarrow$ `2. Billing` $\rightarrow$ `3. Review`).

## 5.4 Jakob’s Law: External Consistency

Articulated by Jakob Nielsen, Jakob's Law states: *"Users spend most of their time on other websites."*

- **Mental Model Transfer:** Users arrive at your product with deeply ingrained expectations formed by industry leaders (e.g., Google, Amazon, Apple, YouTube).
- **Design Rule:** Innovate on core value propositions, but adhere strictly to established interface conventions (e.g., company logo positioned at top-left returning home, search bar at top-center, shopping cart at top-right). Unnecessary disruption of standard conventions causes immediate cognitive friction.

## 5.5 The Aesthetic-Usability Effect

First documented by researchers Masaaki Kurosu and Kaori Kashimura at the Hitachi Design Center in 1995, the Aesthetic-Usability Effect reveals that users perceive visually attractive designs as inherently more usable and effective.

- **The Halo Effect in UX:** An aesthetically polished interface induces positive affect, fostering user patience and predisposing users to overlook minor operational bugs or friction points.
- **The Design Trap:** High visual polish can mask deep architectural or informational flaws during early usability testing. Rigorous usability testing must evaluate underlying task efficiency independently of visual aesthetics.

## 5.6 The Peak-End Rule

Identified by Nobel laureate Daniel Kahneman, the Peak-End Rule states that humans judge past experiences predominantly based on two temporal moments: the **peak** (the most emotionally intense point, positive or negative) and the **end** (the final moment of the interaction).

- **Mitigating Negative Peaks:** Long processing delays or payment failures create catastrophic negative peaks. Designers must soften these friction points with clear progress indicators, humorous error states, or instant fallbacks.
- **Engineering Positive Ends:** Concluding an interaction with an unexpected positive delight (e.g., celebratory confetti animation upon task completion, instant receipt delivery, or loyalty bonus) leaves an enduring positive memory of the product.

## 5.7 Tesler’s Law: The Law of Conservation of Complexity

Formulated by computer scientist Larry Tesler while at Xerox PARC, this law states that every application has an inherent amount of irreducible complexity. The only variable is who bears that complexity: the software system or the user.

- **Developer Burden vs. User Effort:** If engineers invest additional effort into automating address auto-completion, geolocation deduction, and smart defaults, the user experience becomes effortless. Conversely, cutting development corners shifts that cognitive burden directly onto the end user.

```
Total Inherent System Complexity (Constant)
┌────────────────────────────────────────────────────────┐
│   System / Algorithmic Complexity  │  User Cognitive   │
│      (Handled by Engineers)        │      Effort       │
└────────────────────────────────────────────────────────┘
 ◄──────────────── Shifts Left ────────────── Shifts Right ────────►
 (Lazy engineering burdens users)       (Smart design relieves users)
```

## 5.8 Gestalt Principles of Perceptual Organization

Developed by the Berlin School of experimental psychology (Wertheimer, Koffka, Köhler), Gestalt principles describe how human visual perception automatically organizes disparate visual stimuli into unified wholes.

- **Law of Proximity:** Elements placed close to one another are perceived as sharing a common conceptual function or belonging to the same group. (Form input labels must be placed closer to their corresponding input box than to the preceding input box).
- **Law of Similarity:** Elements sharing identical visual characteristics (shape, color, size, orientation) are perceived as having identical functionality (e.g., all clickable links sharing identical teal coloring).
- **Law of Uniform Connectedness:** Elements visually connected by continuous lines, explicit enclosing borders, or unified background containers are perceived as more strongly related than elements related by proximity alone (e.g., card containers in modern web design).

---

# Lecture Notes
![[IS2211 - 03. Usability Heuristics & UX Laws.pdf]]
