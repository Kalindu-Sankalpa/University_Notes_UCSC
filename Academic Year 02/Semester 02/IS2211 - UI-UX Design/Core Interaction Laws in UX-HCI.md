This topic note bridges foundational cognitive psychology and applied Human-Computer Interaction (HCI) critique—operationalizing **Hick's Law**, **Fitts's Law**, and **Miller's Law** as a unified diagnostic lens (**Choice**, **Movement**, and **Memory**) to systematically audit, expose friction within, and remediate production user interfaces.

---

# 1. The Applied Interaction Triad: Bridging Theory to Interface Critique

While broad heuristic frameworks establish baseline usability principles (see [[Usability Heuristics & UX Laws]]), real-world interface critiques require quantifiable laws governing **human cognition** and **motor mechanics**. Every interactive user journey relies on three simultaneous capabilities: choosing what to do (**Choice**), physically actuating the control (**Movement**), and retaining task context (**Memory**).

- **Conceptual Analogy:** Navigating a cluttered airport terminal during a tight flight connection parallels poor interface design. Unlabeled gates spanning 30 overlapping options trigger **decision paralysis** (Hick's Law); microscopic exit signage placed far down a narrow corridor induces **physical strain** (Fitts's Law); and memorizing a 12-step transit code across terminals triggers **working memory overload** (Miller's Law).

![[interaction_laws_triad_balance.png]]

> [!important] The Compound Friction Rule: Laws Operate Together, Never Alone
> Real digital products rarely violate just one law cleanly. An ungrouped 15-item menu (**Hick's Law** violation) rendered with tiny, tightly packed icons (**Fitts's Law** violation) accompanied by dense walls of instructional prose (**Miller's Law** violation) compounds into catastrophic user abandonment. Exceptional UX harmonizes **Choice · Movement · Memory** concurrently.

| Interaction Law | Core Cognitive / Motor Domain | Mathematical / Empirical Anchor | Primary UX Failure Mode | Primary Design Countermeasure |
| :--- | :--- | :--- | :--- | :--- |
| **Hick's Law** | Decision Latency (**Choice**) | $RT = a + b \cdot \log_2(n)$ | Choice paralysis, hesitation, elevated bounce rates | Progressive disclosure, semantic grouping, smart defaults |
| **Fitts's Law** | Motor Target Acquisition (**Movement**) | $MT = a + b \cdot \log_2\left(\frac{2D}{W}\right)$ | Mis-taps, cursor overshoot, thumb fatigue | Large target sizing ($\ge 44\text{--}48\text{ px}$), spacing, thumb zones |
| **Miller's Law** | Working Memory Span (**Memory**) | Capacity $\approx 7 \pm 2$ Chunks | Recall failure, cognitive overload, form drop-off | Chunking, progressive multi-step wizards, visual recognition |

---

# 2. Hick's Law: Minimizing Decision Latency

Formulated by psychologists William Edmund Hick and Ray Hyman (1952), **Hick's Law** (or the Hick-Hyman Law) proves that the time required for a user to reach a decision increases logarithmically with the number and complexity of available choices.

$$RT = a + b \cdot \log_2(n)$$

- **Variable Semantics:** $RT$ denotes Reaction Time, $a$ represents baseline cognitive/motor delay independent of choices, $b$ represents an empirically fitted slope derived from option complexity and familiarity, and $n$ denotes the count of equally probable alternatives.
- **Similarity & Grouping Amplifier:** Decision time spikes nonlinearly beyond the logarithmic baseline when choices appear visually identical, lack clear labels, or reside in ungrouped flat lists.

## 2.1 High-Impact UI/UX Hotspots
- **Navigation Menus:** Top-level global navigation bars stuffed with 12–20 unstructured links force continuous visual scanning before every click.
- **Settings Pages:** Flat enterprise configuration panels lacking logical tabs or category grouping bury critical security toggles inside visual noise.
- **Onboarding Screens:** Greeting new users with five diverging setup paths before delivering initial product value triggers immediate task abandonment.
- **Form Choices & Dashboards:** Unfiltered dropdowns containing dozens of options or executive dashboards exposing dozens of competing actions degrade decision confidence.
- **Primary Design Risk:** Users feel **overwhelmed**, hesitate excessively, experience choice paralysis, or abandon the workflow altogether.

## 2.2 Good vs. Bad UX Patterns & Design Guidelines
- **Anti-Patterns (Bad UX):** Exposing 15 top-level menu items simultaneously; rendering endless unsearchable dropdown lists; placing 3–4 competing Call-to-Action (CTA) buttons with identical visual weight on a single card.
- **Applied Guidelines (Good UX):**
  - **Reduce Visible Choices:** Ruthlessly prune redundant actions so users evaluate only immediate task-relevant controls.
  - **Group Related Options:** Organize sprawling controls into semantic categories using clean [[Information Architecture & User Flows]] taxonomies.
  - **Use Meaningful Labels:** Write explicit, action-oriented labels (e.g., *"Export as PDF"*) instead of vague jargon (e.g., *"Process Output"*).
  - **Show Essential Options First:** Highlight the primary happy-path workflow visually while pushing secondary routes backward in hierarchy.
  - **Hide Advanced Features Behind "More":** Apply **progressive disclosure** (e.g., collapsible accordions, contextual overflow menus `⋯`, or `"Advanced Settings"` drawers) alongside smart defaults and recommendations.

```html
<!-- HICK'S LAW REMEDIATION: Progressive Disclosure & Visual CTA Hierarchy -->
<section class="checkout-actions" aria-label="Primary Checkout Decision">
  <!-- 1. Essential, Smart Default Action (Highest Visual Salience) -->
  <button type="submit" class="btn-primary">
    Continue to Payment
  </button>

  <!-- 2. Secondary Controls Grouped Safely via Progressive Disclosure -->
  <details class="more-options">
    <summary>More Delivery & Promo Options</summary>
    <div class="disclosure-panel">
      <label><input type="checkbox" name="gift_wrap"> Add Gift Wrapping</label>
      <label><input type="text" name="promo" placeholder="Enter Promo Code"></label>
    </div>
  </details>
</section>
```

## 2.3 Hick's Law Quick Critique Questions
1. **Visible Choice Count:** How many choices does the user see at once on the target screen?
2. **Visual Priority:** Are all visible choices styled as equally important, creating CTA competition?
3. **Structural Compression:** Can adjacent choices be logically grouped or safely delayed to a later step?
4. **Premature Decision Burden:** Is the user forced to decide complex configuration parameters too early in the flow?

---

# 3. Fitts's Law: Optimizing Motor Acquisition & Ergonomics

Proposed by psychologist Paul Fitts (1954), **Fitts's Law** models human psychomotor speed: the time required to move a pointer or finger rapidly to a target region is a function of the **Distance ($D$)** to the target and the target's interactive **Width ($W$)**.

$$MT = a + b \cdot \log_2\left(\frac{2D}{W}\right)$$

- **Geometric Translation:** **Bigger targets ($W \uparrow$)** reduce movement precision demands and are dramatically faster and easier to click; **closer targets ($D \downarrow$)** minimize physical travel time across the viewport.
- **Index of Difficulty ($ID$):** The ratio $\log_2(2D/W)$ measures target acquisition difficulty in bits; shrinking a button by half while doubling its distance requires exponentially higher fine-motor stabilization.

## 3.1 High-Impact UI/UX Hotspots
- **Primary Buttons & CTAs:** High-frequency submit, checkout, and confirmation triggers demand generous hit-box padding.
- **Icons & Inline Links:** Bare standalone glyph icons (e.g., an $18 \times 18\text{ px}$ trash icon) force frustrating cursor hunting.
- **Mobile Navigation & Touch Targets:** Smartphone interfaces lack pixel-accurate mouse cursors; human fingertips typically cover an area of $40\text{--}50\text{ px}$ in diameter.
- **Critical Applicability Domains:** Essential across **mobile devices**, **accessibility** (users with motor tremors, arthritis, or low vision), and **one-handed use** where the natural thumb arc dictates ergonomic comfort.

![[good_vs_bad_ux_laws_critique.png]]

## 3.2 Good vs. Bad UX Patterns & Design Guidelines
- **Anti-Patterns (Bad UX):** Tiny unpadded buttons; interactive links packed tightly side-by-side; important primary submission actions stranded in the top-left corner far away from the user's resting cursor or thumb.
- **Applied Guidelines (Good UX):**
  - **Make Important Actions Large:** Scale primary CTA hit boxes prominently across both desktop and mobile breakpoints.
  - **Place Primary Actions in Easy-to-Reach Areas:** Anchor mobile navigation bars and key confirmation triggers inside the lower **natural thumb zone** (bottom 40% of the screen).
  - **Increase Spacing Between Clickable Elements:** Maintain explicit whitespace buffers ($\ge 8\text{ dp}$) between adjacent controls—especially separating irreversible destructive triggers (e.g., *Delete*) from frequent positive actions (e.g., *Save*).
  - **Avoid Tiny Icons Without Labels:** Pair compact glyphs with text labels or wrap icons inside enlarged transparent hit containers.
  - **Respect Minimum Touch Target Sizes:** Strictly enforce platform ergonomic baselines (Apple Human Interface Guidelines: $\ge 44 \times 44\text{ pt}$; Google Material Design 3: $\ge 48 \times 48\text{ dp}$; WCAG 2.2 Target Size AA: $\ge 24 \times 24\text{ CSS px}$ minimum, with $44 \times 44\text{ px}$ strongly preferred).

> [!tip] Desktop Edge Infinite-Target Hack
> On desktop viewports, display boundaries automatically stop mouse cursor movement. Anchoring menu bars, close buttons, or scrollbars flush against screen edges effectively gives those targets **infinite width ($W \to \infty$)** along the axis of movement—drastically accelerating acquisition speed (utilized by macOS top menu bars and Windows corner Start buttons).

```css
/* FITTS'S LAW IN PRODUCTION CSS: Ergonomic Touch Targets & Thumb Zone */
.mobile-primary-cta {
  /* Respect minimum 48px ergonomic height and wide horizontal target */
  min-height: 48px;
  min-width: 48px;
  width: 100%;
  padding: 12px 24px;
  font-weight: 600;
}

.action-toolbar {
  display: flex;
  align-items: center;
  /* Enforce Fitts's separation buffer (>= 8px/12px) to prevent accidental taps */
  gap: 12px;
}

/* Sticky bottom bar places primary CTA inside the one-handed mobile thumb zone */
.sticky-thumb-footer {
  position: sticky;
  bottom: 0;
  padding: 16px;
  background: #ffffff;
  border-top: 1px solid #e2e8f0;
}
```

## 3.3 Fitts's Law Quick Critique Questions
1. **Movement Distance ($D$):** How far must the user's cursor or thumb travel from the preceding interaction to finish the task?
2. **Ergonomic Reach:** Are primary action buttons positioned effortlessly within easy reach (thumb zone on mobile, natural flow on desktop)?
3. **Target Dimension ($W$):** Are interactive targets physically large enough for imprecise human fingers without zooming?
4. **Proximity Error Risk:** Could high-consequence mis-clicks occur because a destructive button sits too close to a primary button?

---

# 4. Miller's Law: Designing for Working Memory Span

Published by cognitive psychologist George A. Miller (1956), **Miller's Law** establishes that the average human being can retain approximately **$7 \pm 2$ items (chunks)** simultaneously in active working memory (with more recent cognitive science narrowing active unassisted recall closer to $4 \pm 1$ complex items).

- **Cognitive Load Priority:** Cognitive load matters substantially more than superficial visual aesthetics; a visually stunning interface that exhausts working memory fails its core usability mandate.
- **Chunking Mechanism:** Working memory bottlenecks are bypassed not by shrinking total information permanently, but by **chunking** disparate atomic data points into meaningful, pattern-recognizable units (e.g., formatting `0771234567` as `077 123 4567`).

## 4.1 High-Impact UI/UX Hotspots
- **Form Fields:** Massive ungrouped registration pages overwhelm visual scanning and trigger memory lapses mid-entry.
- **Navigation Menus:** Deeply nested navigation trees without visual landmarks force users to mentally track their hierarchical depth.
- **Instructions & Error Recovery:** Multi-clause troubleshooting instructions presented all at once vanish from working memory before the user executes Step 2.
- **Dashboards & Multi-Step Tasks:** Dense analytical screens cramming dozens of ungrouped KPIs or cross-screen purchase flows lacking persistent order summaries induce acute mental fatigue.

## 4.2 Good vs. Bad UX Patterns & Design Guidelines
- **Anti-Patterns (Bad UX):** Long 20-field forms dumped onto a single endless scroll page; dense walls of unformatted text blocks; presenting multiple complex instructions simultaneously; forcing users to remember temporary codes or pricing across disconnected screens.
- **Applied Guidelines (Good UX):**
  - **Break Content into Chunks:** Group fields logically (e.g., *Personal Details*, *Shipping Address*, *Payment Method*) with generous spacing between cards.
  - **Use Sections and Headings:** Anchor visual hierarchy with explicit scannable subheadings and bullet points.
  - **Avoid Long Lists:** Partition large data lists into digestible tabs, searchable tables, or paginated feeds.
  - **Show Progress Indicators:** Render explicit step counters (`Step 2 of 4: Delivery`) so users never wonder how much cognitive effort remains.
  - **Offload Memory to the Interface:** Prioritize **recognition over recall** by keeping persistent labels, format placeholders (`DD / MM / YYYY`), live inline validation hints, and persistent cart summaries visible on screen.

> [!warning] The "Magic Number 7" Misconception
> Miller's Law does **not** mandate forcing every navigation menu or grid to strictly contain 7 items. Rather, it dictates organizing complex information into **logical, scannable chunks** so no single working-memory unit exceeds comfortable processing bounds. Four deeply meaningful categories outperform seven ambiguous items.

```tsx
// MILLER'S LAW IN ACTION: Chunked Multi-Step Wizard & Memory Offloading
function CheckoutStepper({ currentStep }: { currentStep: number }) {
  const steps = ["1. Shipping", "2. Delivery", "3. Payment", "4. Review"];

  return (
    <nav aria-label="Checkout Progress" className="stepper-header">
      {/* Offloads mental tracking of remaining workflow stages */}
      {steps.map((label, idx) => (
        <span key={label} className={idx + 1 === currentStep ? "active-chunk" : "step-chunk"}>
          {label}
        </span>
      ))}
    </nav>
  );
}
```

## 4.3 Miller's Law Quick Critique Questions
1. **Recall Burden:** How many distinct facts, codes, or values must the user hold in short-term memory across screens?
2. **Instructional Chunking:** Are dense instructions, terms, or form fields broken into cohesive, manageable chunks?
3. **Recognition vs. Recall:** Is the interface forcing the user to rely on raw memory rather than persistent visual cues, labels, and hints?
4. **Workflow Simplification:** Can redundant sequential steps be automated, pre-filled, or simplified cleanly?

---

# 5. Compound Synergy & The 3-Step Systematic Interface Critique

Because **Choice (Hick)**, **Movement (Fitts)**, and **Memory (Miller)** operate concurrently during every human-computer interaction, professional UX designers apply a disciplined, repeatable audit workflow to move **From Theory $\rightarrow$ Interface Critique**.

![[systematic_ux_critique_workflow.png]]

## 5.1 The Three-Step Systematic Evaluation Protocol

1. **Step 1: Identify the User Task:**
   - **Goal Anchoring:** Define precisely what the end user is trying to accomplish before inspecting pixels (e.g., *"Find and reserve a library book"*, *"Complete e-commerce checkout"*, or *"Submit a university course registration form"*).
   - **Boundary Definition:** Specify the target persona's device context (one-handed mobile commuter vs. dual-monitor desktop analyst).
2. **Step 2: Observe the Interface:**
   - **Artifact Inventory:** Document every screen involved from entry point to confirmation state.
   - **Component Mapping:** Catalog navigation menus, CTA buttons, form input groupings, instructional copy, transition states, and target coordinates.
3. **Step 3: Apply Each Law Systematically:**
   - **Multi-Lens Pass:** Evaluate the inventoried components using the dedicated Quick Critique Questions for Hick's Law, Fitts's Law, and Miller's Law sequentially, logging every violation with a concrete architectural fix.

## 5.2 Worked Example: Critiquing a Legacy University Book Portal

Consider an unoptimized mobile library web portal where a student attempts **Task: "Find and reserve a textbook."**

| Critique Dimension | Observed Interface Violation | Impact on User Experience | Targeted UX Remediation |
| :--- | :--- | :--- | :--- |
| **Hick's Law (Choice)** | Landing page displays 18 flat department links, 6 search filter dropdowns, and 4 equally bright buttons (*Borrow*, *Hold*, *Cite*, *Export*) per book card. | Students experience immediate decision paralysis scanning dozens of redundant controls before searching. | Collapse search filters behind an expandable `"Filters"` drawer; designate *Reserve Book* as the sole high-contrast primary CTA. |
| **Fitts's Law (Movement)** | The `"Reserve"` link is a tiny $14\text{ px}$ unpadded text trigger at the top-right beside a tiny `"Cancel"` icon. | High mis-tap rates on mobile touchscreens; painful upward thumb stretching during one-handed lookup. | Convert `"Reserve"` into a full-width, $48\text{ px}$-tall bottom sticky button; separate destructive actions by $\ge 16\text{ px}$. |
| **Miller's Law (Memory)** | Reservation requires copying an 11-character ISBN manually from the search result page and pasting it into a separate 14-field reservation form with no progress bar. | Severe working memory failure (`Recall` over `Recognition`), forcing frantic tab-switching and abandonment. | Auto-populate the selected book's ISBN cleanly; split remaining confirmation into a 2-step progressive wizard with live preview card. |

> [!info] External Authoritative References (Lecture 05 Syllabus Sources)
> - **Laws of UX Repository:** [https://lawsofux.com/](https://lawsofux.com/) — Comprehensive visual reference library documenting cognitive heuristics and UX laws.
> - **Nielsen Norman Group (NN/g):** [https://www.nngroup.com/articles/fitts-law/](https://www.nngroup.com/articles/fitts-law/) — Empirical guidance on Fitts's Law target sizing, edge targets, and pop-up/pie menu applications.

---

# Lecture Notes
![[IS2211 - 05. Core Interaction Laws in UX-HCI.pdf]]
