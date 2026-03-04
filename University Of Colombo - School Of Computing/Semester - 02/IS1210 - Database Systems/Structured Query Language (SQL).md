>[!Intro] Objective Of SQL
>The primary objective of **Structured Query Language (SQL)** is to provide a standardized, **non-procedural language** that allows users to create database structures, perform data management tasks (insertion, modification, and deletion), and execute both simple and complex queries with minimal effort. It is designed to be **portable and intuitive**, using English-like syntax to transform relational inputs into required outputs.

# 1. Classification and Environment

SQL originated from the evolution of the relational model and was standardized by **ANSI and ISO**. It operates in two modes: **Interactive Mode** (direct terminal entry) and **Embedded Mode** (integrated into languages like Java or C++). The ISO standard classifies SQL into four sub-languages:

- **Data Definition Language (DDL):** Used for defining and modifying the **database schema**.
- **Data Manipulation Language (DML):** Used for **retrieving and modifying** the data within tables.
- **Data Control Language (DCL):** Used for managing **user permissions** and access.
- **Transaction Control Language (TCL):** Ensures the **consistency and reliability** of database transactions.

# 2. ISO SQL Data Types and Basics

SQL uses the terms **table, row, and column** to represent relations, tuples, and attributes. Keywords are **case-insensitive**, but **literal character data** must match the database exactly. Key data types include:

- **Numeric:** Divided into **Exact Numeric** (INT, SMALLINT, BIGINT, DECIMAL, NUMERIC) and **Approximate Numeric** for scientific data (FLOAT, REAL, DOUBLE PRECISION).

- **Character/String:** **CHAR** (fixed length, space-padded), **VARCHAR** (variable length), and **CLOB** (large objects with specific restrictions).

- **Boolean:** Supports **TRUE, FALSE, and UNKNOWN** (NULL).

- **Temporal:** Includes **DATE** (YYYY-MM-DD), **TIME** (HH:MM:SS), **TIMESTAMP** (both date and time), and **INTERVAL** (periods of time).

# 3. Data Definition and Integrity Enhancement (DDL)

DDL statements like `CREATE SCHEMA` and `CREATE TABLE` define the structure. The **Integrity Enhancement Feature** protects the database from inconsistency through several constraints:

- **Required Data:** Specified using the **NOT NULL** clause.

- **Domain Constraints:** Enforced via the **CHECK clause** or by creating a specific **DOMAIN**.

- **Entity Integrity:** Enforced by defining a **PRIMARY KEY** (must be unique and non-null).

- **Referential Integrity:** Enforced via **FOREIGN KEYS** that reference a parent table. Actions for updates or deletions include **CASCADE, SET NULL, SET DEFAULT, or NO ACTION**.

- **Schema Modification:** Tables are updated using **ALTER TABLE** (to add/drop columns or constraints) and removed using **DROP TABLE** (with RESTRICT or CASCADE options). **TRUNCATE** is used to clear all records quickly without destroying the structure.

# 4. Data Manipulation and Maintenance (DML)

DML statements allow for the maintenance of table contents:

- **INSERT:** Adds single or multiple rows; non-numeric values must be in **single quotes**.

- **UPDATE:** Modifies existing data, often using a **WHERE clause** to target specific rows.

- **DELETE:** Removes rows; if the WHERE clause is omitted, **all rows are deleted** but the table structure remains.

# 5. Advanced Data Retrieval

The **SELECT statement** is the most frequent SQL operation. The **sequence of processing** is: **FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY**.

- **Filtering & Formatting:** Users can use `DISTINCT` to eliminate duplicates and `AS` to create **aliases** for calculated fields.

- **Predicates:** Retrieval is refined using **BETWEEN** (range), **IN** (set membership), **LIKE** (pattern matching with `%` for zero/more characters and `_` for one character), and **IS NULL**.

- **Aggregation & Grouping:** Five functions (**COUNT, SUM, AVG, MIN, MAX**) summarize data. **GROUP BY** produces summary rows, while **HAVING** filters those groups based on aggregate conditions.

- **Sub-queries:** Inner SELECT statements can return **Scalar** (single value), **Row** (multiple columns, one row), or **Table** (multiple rows/columns) results to an outer query. Keywords like **ANY/SOME, ALL, and EXISTS** assist in complex sub-query logic.

# 6. Joins and Set Operations

To combine data from multiple tables, SQL uses **joins**:

- **Inner Join:** Pairs related rows where matching columns have the same value.

- **ANSI Join Syntax:** Includes `JOIN ON`, `JOIN USING`, and `NATURAL JOIN`.

- **Outer Joins:** **Left, Right, and Full Outer Joins** include unmatched rows from one or both tables, filling missing data with NULLs.

- **Set Operations:** **UNION, INTERSECT, and EXCEPT** (or MINUS) combine result tables that are **union-compatible** (same number of columns and data types).

---
# Short Note: Structured Query Language (SQL)

- **Core Logic:** SQL is **non-procedural**; you specify the "what" (result) and the DBMS determines the "how" (execution path).

- **Data Integrity:** SQL is the primary tool for enforcing **Entity and Referential Integrity**, using primary and foreign keys to prevent "orphaned" or inconsistent records.

- **The Power of Metadata:** All DDL definitions (schemas, tables, constraints) are stored in the **System Catalog**, allowing the DBMS to maintain control over data as a resource.

- **Aggregate Filtering:** While **WHERE** filters individual rows _before_ groups are formed, **HAVING** filters the groups _after_ they are formed, always involving at least one aggregate function.

- **Join Strategy:** Multi-table queries typically link a **Foreign Key** in a "child" table to a **Primary Key** in a "parent" table.

- **Set Compatibility:** For **UNION, INTERSECT, or EXCEPT** to work, tables must have the same structure and corresponding columns must draw from the same **domain**.

**SQL** is like **directing an automated library**: the **DDL** is the set of rules for how books are categorized and where the shelves are built; the **DML** is the process of adding new books or updating their records; and the **SELECT statement** is the search terminal where you ask for specific titles or genres—the system doesn't require you to know which floor the book is on, it simply brings the result to you.

---
# Lecture Notes
![[IS1210 - SQL Part 1.pdf]]
![[IS1210 - SQL Part 2.pdf]]
![[IS1210 - SQL DDL.pdf]]
![[IS1210 - SQL DML Part 1.pdf]]
![[IS1210 - SQL DML Part 2.pdf]]