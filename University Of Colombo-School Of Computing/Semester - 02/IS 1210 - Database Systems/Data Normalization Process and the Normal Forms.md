>Next Topic : [[Structured Query Language (SQL)]]

>[!Intro]
>The primary goal of this topic is to demonstrate the process of **normalization** and apply specific techniques to produce a set of relations with desirable properties. It aims to help students:
>- Understand the purpose of normalization in **minimizing data redundancy** and eliminating **update anomalies**.
>- Analyze **functional dependencies** (FDs) between attributes to identify optimal groupings.
>- Identify and correct **partial, transitive, and multi-valued dependencies**.
>- Apply tests to reach specific **Normal Forms** (1NF, 2NF, 3NF, and BCNF).

# What is Normalization?

Normalization is a **[^1]bottom-up technique** or a **validation technique** used to produce a set of relations with minimal redundancy and close logical relationships between attributes. It begins by examining **functional dependencies**, which are constraints determining how one attribute (the determinant) relates to another.

# Problems Targeted by Normalization

The process specifically addresses issues caused by **data redundancy**, where the same piece of data is stored in multiple places. This redundancy leads to **update anomalies**:

- **Insertion Anomaly:** Being unable to insert data because other related data is missing (e.g., cannot add a new branch without a staff member if the staff ID is the primary key).
- **Deletion Anomaly:** Unintentionally losing data (e.g., deleting a staff member record that also happens to be the only record containing specific branch details).
- **Modification Anomaly:** When data is only partially updated, leading to inconsistencies.

# Functional Dependencies (FDs) and Decomposition

To fix these anomalies, larger relations are **decomposed** into smaller ones. Successful decomposition must be **lossless** (allowing the original table to be reconstructed) and **preserve dependencies**. Key types of dependencies analyzed include:

- **Full Functional Dependency:** An attribute depends on the entire determinant, not just a part of it.

- **Partial Dependency:** An attribute depends on only a part of a composite primary key.

- **Transitive Dependency:** An indirect relationship where A→B and B→C, meaning C is transitively dependent on A via B.

- **Multi-Valued Dependency (MVD):** When a value of A is associated with independent sets of values for B and C.

---

# Short Note - Data Normalization

- **Core Technique:** Uses a series of tests called **Normal Forms** to identify the optimal grouping for attributes.

- **Main Objective:** To create an accurate representation of data while ensuring facts are recorded only once—except for **foreign keys**, which are essential for joining related tables.

- **The "Determinant":** The attribute on the left-hand side of a functional dependency (A→B) that determines the value of another.

- **Normal Forms Covered:**
	- **1NF:** Elimination of repeating groups.
	- **2NF:** Elimination of **partial dependencies**.
	- **3NF:** Elimination of **transitive dependencies**.
	- **BCNF:** A stronger form of 3NF focusing on dependency preservation.

- **Benefits:** Databases become easier to access and maintain, storage costs are minimized, and data integrity is protected.

The **Normalization Process** is like **organizing a messy toolbox**: rather than throwing every tool, screw, and manual into one giant drawer (a redundant relation), you sort them into specific compartments based on their purpose (Normal Forms). This ensures that if you lose a specific wrench (Deletion Anomaly), you don't accidentally throw away the instruction manual for the drill that was stuck to it.

[^1]: The **bottom-up technique** refers specifically to the process of **data normalization**.
	
	Unlike top-down approaches (such as ER modeling) that start with a high-level organizational view, a bottom-up technique focuses on the following:
	
	- **Starting with Attributes:**
		It begins by examining the specific **attributes** (properties of data) and the **relationships** between them, which are known as **functional dependencies**.
	
	- **Building Relations:**
		By analyzing these dependencies, the designer uses a series of tests called **normal forms** to identify the **optimal grouping** for these attributes.
	
	- **Creating the Structure:**
		The ultimate goal of this bottom-up approach is to synthesize these small, detailed data requirements into a set of **well-designed relations** (tables) that support the organization's needs.
