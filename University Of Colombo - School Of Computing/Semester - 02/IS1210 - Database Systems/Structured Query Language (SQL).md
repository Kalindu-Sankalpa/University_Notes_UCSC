>[!Intro]
>The primary goal of this topic is to equip students with the practical skills necessary to interact with a relational database using SQL. Specifically, it aims to enable students to:
>- **Formulate SQL queries** of varying complexity to retrieve and manipulate data,,.
>- **Define and manage database structures** including tables, indexes, and integrity constraints.
>- **Create and evaluate views** to simplify data access and enhance security,,.
>- **Develop database applications** by integrating SQL with other relevant tools and technologies.

# Introduction and Data Types

SQL is the standard language used for defining, manipulating, and controlling access to data within a relational database. It utilizes various **data types** to ensure data accuracy, including **Character** (CHAR, VARCHAR), **Numeric** (INTEGER, FLOAT, DECIMAL), **Binary Large Objects** (BLOB), and **Date/Time** formats.

# Data Definition Language (DDL)

The DDL component of SQL is used to define and modify the database structure. Key operations include:

- **Table Management:** Using `CREATE TABLE` to define new tables, `ALTER TABLE` to modify existing structures, and `DROP TABLE` to remove them.

- **Integrity Constraints:** Specifying rules such as `PRIMARY KEY`, `UNIQUE`, `NOT NULL`, and `CHECK` constraints. It also handles **referential integrity** through `FOREIGN KEY` definitions with specific actions like `CASCADE` or `RESTRICT`.

- **Indexes:** Using `CREATE INDEX` and `DROP INDEX` to improve data retrieval speeds.

# Data Manipulation Language (DML)

DML allows users to interact with the data stored in the tables:

- **Data Retrieval:** The `SELECT` statement is used to query data. It can be refined using the `WHERE` clause, relational operators, and keywords like `AND`, `OR`, `BETWEEN`, `IN`, and `LIKE`.

- **Advanced Querying:** SQL supports **aggregate functions** (COUNT, SUM, AVG, MAX, MIN) combined with `GROUP BY` and `HAVING` clauses to summarize data.

- **Complex Joins:** Users can combine data from multiple tables using **Natural Joins**, **Outer Joins**, and **Union** operations.

- **Subqueries:** SQL allows for **nested select statements** and correlated queries to perform sophisticated data analysis.

- **Modifying Data:** The `INSERT INTO`, `UPDATE`, and `DELETE` commands are used to add, modify, or remove records based on specific criteria or subqueries.

# Views

A **view** is a virtual table created via a `SELECT` statement. Topic six covers the **creation and removal of views**, their updatability, and their use in **improving security and simplifying complex queries** for the end-user.

---

# Short Note - Structured Query Language (SQL)

- **Core Function:** SQL serves as the comprehensive tool for both building a database (**DDL**) and interacting with its data (**DML**).

- **The SELECT Statement:** This is the most frequently used command, allowing users to specify exactly **what** data they need through filtering, sorting, and aggregating.

- **Relational Power:** Through **Joins and Subqueries**, SQL can link disparate tables together into a single, cohesive result set.

- **Integrity Enforcement:** SQL provides the syntax to strictly enforce **Entity and Referential Integrity**, ensuring the database remains accurate and consistent.

- **Virtualization:** **Views** allow designers to present "customized" windows into the data, hiding complexity or sensitive information from specific users.

**Structured Query Language (SQL)** is like **the control room of a massive automated warehouse**: **DDL** is the set of commands used to build the shelves and label the bins (creating tables and constraints); **DML** is the system used to stock items, move them around, or take them out (insert, update, delete); and the **SELECT statement** is the high-speed retrieval robot that can find a specific item or count every box in the building in seconds.