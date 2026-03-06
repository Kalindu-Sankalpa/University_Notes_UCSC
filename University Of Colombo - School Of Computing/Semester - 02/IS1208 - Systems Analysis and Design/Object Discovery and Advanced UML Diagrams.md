>[!abstract] Note!
>We shift from high-level workflows to **Object Discovery**, where we identify the specific building blocks of the system and how they are organized using advanced UML diagrams.

---

# 1. Identifying Objects and Responsibilities

To find the objects needed for a system, analysts perform **Noun and Verb Analysis** on requirements like User Stories and Use Case Narratives:

- **Identifying Objects (Nouns):** Analysts pick out nouns to find potential classes (e.g., "Customer," "Shopping Cart," "Order"). These must be filtered to remove redundant terms, attributes, or items outside the problem domain.
- **Identifying Responsibilities (Verbs):** Verb phrases identify what an object **knows** (attributes) and what it **does** (behaviors). For example, "Validate payment" or "Confirm order" become behaviors of a class.

**2. Class Stereotypes**

UML uses **stereotypes** to categorize classes based on their role within the system architecture:

- **Boundary Classes:** These provide the interface for actors or other systems to interact with the application.
- **Entity Classes:** These reflect real-world entities and perform internal tasks, usually storing data that needs to persist (e.g., "Account" or "Student").
- **Control Classes:** These act as mediators, managing the application logic and coordinating interactions between boundary and entity classes for specific use cases.

**3. Specialized UML 2.0 Diagrams**

Beyond class and activity diagrams, UML 2.0 includes specialized views for specific technical needs:

- **Component Diagram:** Documents the software architecture by showing how physical software parts (like executables, DLLs, and files) depend on one another.
- **Deployment Diagram:** Shows the **physical hardware architecture**, illustrating the computers (nodes), their connections, and which software components reside on which machine.
- **Timing Diagram:** Specifically designed to show **how long** an object remains in a particular state.
- **Interaction Overview Diagram:** A high-level view that combines activity diagrams with interaction fragments to show the flow between different interactions.

--------------------------------------------------------------------------------

**Short Note for Easy Memorization**

- **Object Discovery (N-V Method):**
    - **Nouns** → Potential Classes (Objects).
    - **Verbs** → Responsibilities (Behaviors).
- **The Three Stereotypes (BEC):**
    - **B**oundary: The "Face" (User Interface).
    - **E**ntity: The "Data" (Internal Records).
    - **C**ontrol: The "Brain" (Logic & Sequencing).
- **Specialized Diagrams:**
    - **Component:** Software "Parts" (DLLs/Files).
    - **Deployment:** Physical "Nodes" (Hardware/Servers).
    - **Timing:** Duration of states (Time-based).
- **Naming Rule:** **U**pperCamelCase for Classes; **l**owerCamelCase for Objects.

Does this help clarify how we "find" the objects? We can move on to **Week 12** next, which focuses on **Object Interaction and Sequence Modeling**.