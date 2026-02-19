>[!tip] Introduction
>**Activity Diagrams** model the process steps or specific use-case activities within a system, representing its **dynamic behavior**. While they are similar to flowcharts, they are unique because they can graphically represent **parallel activities**.

# Key Components of Activity Diagrams

- **Activities:** Represent the performance of a behavior in the workflow, shown as **rounded rectangles**.
- **Transitions:** Arrows that show the passing of the flow of control from one activity to the next.
- **Initial and Final Nodes:** A **solid filled circle** indicates the starting point, while a **bull’s eye symbol** indicates the final activity.
- **Decision Points:** Branching points where control follows different paths based on a **guard condition** (a statement in square brackets).
- **Merge Points:** Used to combine multiple flows that were previously separated by a decision point back into a single flow.

# Synchronization: Forks and Joins

Activity diagrams use **synchronization bars** to manage concurrent workflows:

- **Fork:** A bar with one incoming transition and multiple outgoing transitions, splitting execution into **concurrent threads** that occur at the same time or in any order.
- **Join:** A bar with multiple incoming transitions and one outgoing transition; the flow cannot continue until **all incoming actions** are completed.

# Organizational Tools: Swimlanes

**Swimlanes** are used to partition a diagram into vertical columns. This allows the analyst to clearly show **who is responsible** (which actor or department) for each specific activity in a complex business process.

# Practical Application

Activity diagrams are highly useful for **communicating logic to programmers**. However, analysts are cautioned when using them with non-technical users, who may find them difficult to follow; for users, **use-case narratives** are often preferred.

---
# Short Note for Easy Memorization

- **Definition:** The "Workflow" or "Dynamic" model (Flowchart + Parallelism).
- **Nodes (Shapes):**
	- **Rounded Rectangle:** Activity (Action).
	- **Diamond:** Decision / Merge.
	- **Solid Circle:** Start.
	- **Bull’s Eye:** End.

- **Concurrency (Bars):**
	- **Fork:** 1 in → Many out (Split).
	- **Join:** Many in → 1 out (Wait for all).

- **Swimlanes:** Define **Accountability** (Who does what?).

---
# Lecture Notes
![[IS1208 - Activity Diagrams.pdf]]
