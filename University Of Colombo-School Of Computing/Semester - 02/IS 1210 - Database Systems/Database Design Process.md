>Next Topic : [[Data Normalization Process and the Normal Forms]]

>[!Intro]
>The primary goal of this topic is to teach the process of transforming real-world requirements into a structured database. Specifically, it aims to enable students to:
>- **Analyze database requirements** and evaluate design suitability.
>- Create **Entity-Relationship (ER) and Enhanced Entity-Relationship (EER) diagrams** to represent entities, attributes, and relationships.
>- **Translate (map) conceptual models** into relational schemas.
>- Resolve complex relationship types, such as **many-to-many (M:N)** and **recursive relationships**.

# Conceptual Design through ER Modeling

The design process begins with **Conceptual Design**, where the main objective is to create an accurate representation of data, relationships, and constrains relevant to the enterprise. This achieved using three classes of objects.

1. **Entities:**
	These are the "objects" in the system. They can be **strong** or **weak** (the latter depends on the existence of another entity).

2. **Attributes:**
	These describe the properties of entities. They include **identifying attributes** (keys), **composite attributes** (made of multiple parts), and **derived attributes** (calculated from other data).

3. **Relationships:**
	These define how entities interact. Designers must determine **connectivity** (1:1, 1:N, or M:N), **cardinality**, and **existence dependency** (whether a relationship is mandatory or optional).

# Enhanced Entity-Relationship (EER) Modeling

For more complex scenarios, **EER modeling** is used to represent higher-level abstractions:

- **Generalization and Specialization:** These are bottom-up and top-down approaches to grouping entities into **super-types and sub-types**.

- **Constraints:** Rules are applied to how entities are categorized and specialized.

![[University Of Colombo-School Of Computing/Semester - 02/IS 1210 - Database Systems/Images/img_01.svg]]
# Logical Design through Mapping

Once the conceptual model is complete, it must be converted into a **relational schema**. This involves:

- **Mapping Entities:** Regular, weak, and specialized entities are turned into tables.

- **Resolving Relationships:** Designers must decide how to represent 1:1, 1:N, and M:N relationships, often by using **foreign keys** or creating **junction tables**.

- **Cleanup:** Identifying and resolving **redundant or recursive relationships** to ensure a clean logical structure.

---

# Short Note - Database Design Process

- **Design Goal:** To build a "blueprint" (conceptual model) that accurately reflects the organization's data needs.

- **ER Diagramming:** This is the visual language of design, using **Entities** (nouns), **Attributes** (adjectives), and **Relationships** (verbs).

- **Hierarchy in Design:** **EER modeling** allows for "inheritance," where sub-type entities inherit attributes from a super-type.

- **The Transition:** Mapping is the bridge between the **Conceptual level** (real-world view) and the **Logical level** (the actual table structures and keys).

- **Resolution:** A critical part of logical design is breaking down **M:N (many-to-many) relationships**, as they cannot be directly implemented in a standard relational table.

The **Database Design Process** is like **architectural planning**: **Conceptual Design** is the artist's sketch of the building's look and purpose; **EER Modeling** is the detailed blueprint showing different room types (super-types vs. sub-types); and **Logical Design (Mapping)** is the technical specification that tells the builders exactly where the structural supports (keys and tables) must be placed to keep the building standing.