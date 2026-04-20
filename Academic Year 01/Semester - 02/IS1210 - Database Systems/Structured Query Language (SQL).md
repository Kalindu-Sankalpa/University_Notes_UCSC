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

# 7. Indexes

An **index** is a data structure designed to help the DBMS locate specific records in a file more quickly, significantly speeding up response times for user queries—especially in large tables. It works similarly to a book index by providing **fast access** and **topic-based navigation** without requiring a sequential search of every row. An index structure consists of a **Search Key** (a copy of a primary or candidate key stored in sorted order) and a **Data Reference/Pointer** (the physical disk address of the record).

While indexes are vital for performance and minimizing disk accesses, they are not strictly necessary for a DBMS to function. Designers must be cautious, as having **too many indexes** can slow down the performance of `INSERT`, `UPDATE`, and `DELETE` operations due to the overhead of updating index files every time table data changes.

## Types and Creation

- **Primary Index:** Built on the ordering key field of a sequentially ordered data file.
- **Clustering Index:** Built on a non-key field where the data file is sequentially ordered, allowing multiple records per index value.
- **Secondary Index:** Defined on a non-ordering field.
- **Dense vs. Sparse:** A **dense index** has an entry for every search key value, while a **sparse index** has entries for only some values.
- **Commands:** Use `CREATE [UNIQUE] INDEX` to define an index and `DROP INDEX` to remove it.

# 8. Views

A **view** is a **virtual relation** that does not physically exist in the database but is produced on request based on a defining query (**sub-select**). To the user, it appears as a real table with columns and rows, but the DBMS only stores its definition in the **system catalog**.
## Key View Concepts

- **Types:** Views can be **Horizontal** (restricting access to specific rows), **Vertical** (restricting access to specific columns), or **Grouped/Joined** (aggregating data or linking multiple tables).

- **Execution Mechanisms:** The DBMS handles views through **View Resolution** (merging the user query with the view definition at runtime) or **View Materialization** (storing the view as a temporary physical table for faster access in high-rate applications).

- **Updatability:** A view is updatable only if the DBMS can trace every row/column back to a single source table. Updates are generally restricted if the view uses `DISTINCT`, aggregate functions, `GROUP BY`, or joins.

- **WITH CHECK OPTION:** This clause ensures that any `INSERT` or `UPDATE` performed through the view does not cause a row to "migrate" (disappear) because it no longer satisfies the view's `WHERE` condition.

## WITH CHECK OPTION

The **WITH CHECK OPTION** in SQL is used with updatable views to prevent **"migrating rows,"** which are rows that would disappear from a view because an `INSERT` or `UPDATE` causes them to no longer satisfy the view's `WHERE` condition. When you have a **view hierarchy** (a view derived from another view), the two qualifiers **CASCADED** and **LOCAL** determine how these checks are applied across the different levels.

### 1. CASCADED (The Default Option)

If a view is created using **WITH CASCADED CHECK OPTION**, the DBMS enforces the `WHERE` conditions of that view and **all underlying views** it is derived from.

- **Strictness:** It is the most restrictive option.
- **Behavior:** Any row added or updated through this view must satisfy its own criteria and the criteria of every view beneath it in the hierarchy. Even if an underlying view does not have a check option of its own, the `CASCADED` qualifier will "reach down" and enforce those rules to ensure the row does not disappear from the current view.
### 2. LOCAL

If a view is created using **WITH LOCAL CHECK OPTION**, the DBMS only enforces the `WHERE` condition of the view being updated and any underlying views that **also** have their own check options.

- **Behavior:** A row is allowed to disappear from the current view **if and only if** it also disappears from the underlying derived view or base table. It essentially checks the current view's rules but is more "forgiving" regarding the rules of underlying views that lack their own check options.

---
### Example Illustration

Consider this hierarchy based on a **Staff** table:

1. **LowSalary** **View:** `SELECT * FROM Staff WHERE salary > 9000` (No check option).
2. **HighSalary** **View:** `SELECT * FROM LowSalary WHERE salary > 10000` (Derived from `LowSalary`).

**Scenario A: Using** **WITH LOCAL CHECK OPTION** **on** **HighSalary**

- If you try to update a salary to **9500**, the update **fails**. Why? Because 9500 is less than 10000, so it violates `HighSalary`'s rule, even though it still fits in `LowSalary`.
- If you try to update a salary to **8000**, the update **succeeds**. Why? Because while the row disappears from `HighSalary`, it _also_ disappears from the underlying `LowSalary` view. Under `LOCAL`, this "migration" is permitted.

**Scenario B: Using** **WITH CASCADED CHECK OPTION** **on** **HighSalary**

- If you try to update a salary to **9500**, it **fails** (violates `HighSalary`).
- If you try to update a salary to **8000**, it **also fails**. Because it is `CASCADED`, the DBMS protects the entire chain and will not let the row disappear from the hierarchy at all.

**Recommendation:** To avoid data anomalies and unexpected disappearances of records, the sources suggest that views should normally be created using the **WITH CASCADED CHECK OPTION**.

# 9. Transaction Control Language (TCL)

TCL commands manage **transactions** to ensure database consistency and reliability. A transaction is a **logical unit of work** (an action or series of actions) that reads or updates database contents. It must always transform the database from one **consistent state** to another, even if consistency is temporarily violated during execution.

## The ACID Properties All transactions must possess four basic properties:

1. **Atomicity:** The "all or nothing" rule; the transaction is performed in full or not at all.
2. **Consistency:** The transaction must maintain valid states and integrity rules.
3. **Isolation:** Transactions executing simultaneously must not interfere with each other.
4. **Durability:** Once committed, changes are permanent and survive subsequent system failures.

## TCL Commands and States

- **BEGIN TRANSACTION:** Marks the boundary of a unit of work.
- **COMMIT:** Permanently saves all transaction updates to the disk.
- **ROLLBACK:** Undoes all changes made by the transaction if an error occurs.
- **States:** A transaction moves from **Active** to **Partially Committed** (stored in memory buffer) and finally **Committed** (on disk), or it may enter a **Failed** state and be **Terminated**.

# 10. Data Control Language (DCL)

DCL provides the mechanism to ensure only authorized users can access the database, managing maintenance and user rights. SQL supports **Discretionary Access Control (DAC)**, where users are granted specific privileges on database objects at the owner's discretion.

## Privileges and Commands

- **Privileges:** The ISO standard defines specific actions a user can perform, including `SELECT` (retrieve), `INSERT` (add), `UPDATE` (modify), `DELETE` (remove), `REFERENCES` (integrity constraints), and `USAGE` (domains/character sets).
- **GRANT:** Used to give access rights to specific users or the `PUBLIC`. Adding `WITH GRANT OPTION` allows the recipient to pass those privileges to others.
- **REVOKE:** Used to remove previously granted privileges.
---
# Short Note: Structured Query Language (SQL)

- **Core Logic:** SQL is **non-procedural**; you specify the "what" (result) and the DBMS determines the "how" (execution path).

- **Data Integrity:** SQL is the primary tool for enforcing **Entity and Referential Integrity**, using primary and foreign keys to prevent "orphaned" or inconsistent records.

- **The Power of Metadata:** All DDL definitions (schemas, tables, constraints) are stored in the **System Catalog**, allowing the DBMS to maintain control over data as a resource.

- **Aggregate Filtering:** While **WHERE** filters individual rows _before_ groups are formed, **HAVING** filters the groups _after_ they are formed, always involving at least one aggregate function.

- **Join Strategy:** Multi-table queries typically link a **Foreign Key** in a "child" table to a **Primary Key** in a "parent" table.

- **Set Compatibility:** For **UNION, INTERSECT, or EXCEPT** to work, tables must have the same structure and corresponding columns must draw from the same **domain**.

- **Performance:** **Indexes** are the primary tool for query optimization, using sorted search keys and pointers to bypass slow sequential table scans.

- **Abstraction:** **Views** provide **data independence** and security by presenting users with customized, simplified "windows" into the data while hiding sensitive base table information.

- **Reliability:** **TCL** protects data through the **ACID** model, ensuring that complex operations (like a bank transfer) either complete perfectly or fail without leaving behind "half-finished" or inconsistent data.

- **Security:** **DCL** manages access via the **GRANT** and **REVOKE** system, ensuring that data is only accessible to those with the appropriate **privileges**.

**SQL** is like **directing an automated library**: the **DDL** is the set of rules for how books are categorized and where the shelves are built; the **DML** is the process of adding new books or updating their records; and the **SELECT statement** is the search terminal where you ask for specific titles or genres—the system doesn't require you to know which floor the book is on, it simply brings the result to you.

---
# Lecture Notes
![[IS1210 - SQL Part 1.pdf]]
![[IS1210 - SQL Part 2.pdf]]
![[IS1210 - SQL DDL.pdf]]
![[IS1210 - SQL DML Part 1.pdf]]
![[IS1210 - SQL DML Part 2.pdf]]