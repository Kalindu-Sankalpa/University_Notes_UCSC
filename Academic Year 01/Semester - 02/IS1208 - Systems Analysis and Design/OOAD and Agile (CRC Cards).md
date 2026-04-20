>[!tip] Introduction
>CRC Cards (Class-Responsibility-Collaborator), a simple yet powerful Agile technique used to bridge the gap between your static structural models (like Class Diagrams) and dynamic behavioral models (like Sequence Diagrams).

---
# 1. What are CRC Cards?

Instead of using complex software tools, this technique uses **4x6 index cards** to represent classes. Each card acts as a "placeholder for conversation" and identifies three critical pieces of information:

- **Class Name:** Written at the very top of the card.

- **Responsibilities:** Listed on the **left side**, these are the "knowing" (attributes) and "doing" (behaviors) duties of the class.

- **Collaborators:** Listed on the **right side**, these are the other classes that this specific class must interact with to fulfill its responsibilities.

# 2. CRC Cards in Practice

- **Encouraging Discussion:**
	The primary benefit is that they stimulate **team discussion and spirit**. Teams literally "walk through" a Use Case, picking up cards as each class begins to collaborate in the scenario.

- **Defining Higher-Level Behavior:**
	This process stops developers from viewing classes as "dumb data holders" and forces them to understand the actual **logic and communication** required for the system to function.

- **Identifying "New" Classes:**
	During a CRC session, you often discover the need for additional classes, such as **Till, Order, or Stock**, that weren't immediately obvious during initial requirements gathering.

# 3. CRC Good Practices

- **Cohesion:**
	If a card has too many responsibilities, it suffers from **low cohesion** and should likely be split into two or more classes.

- **Coupling:**
	If a card has too many collaborators, it has **high coupling**, which is a sign of a poor design that may be difficult to maintain.

- **Control Classes:**
	In more complex scenarios, **Control classes** are used to manage the "sequencing behavior" of a Use Case, acting as the "brain" that coordinates between Boundary and Entity classes.

---

# Short Note for Easy Memorization

- **CRC Format (L-R-C):**
    - **L**eft: Responsibilities (Knowing/Doing).
    - **R**ight: Collaborators (Who helps?).
    - **C**enter/Top: Class Name.

- **The "Agile" Card:** 4x6 index card; focuses on **interaction over documentation**.

- **Design Health:**
    - _Too many responsibilities?_ → Bad Cohesion (Split it).
    - _Too many collaborators?_ → High Coupling (Simplify it).

- **The Bridge:** It links the **"What is it?"** (Structure) to the **"How does it talk?"** (Behavior).