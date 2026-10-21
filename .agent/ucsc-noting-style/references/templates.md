# UCSC Notes Templates Reference

This reference provides production-ready, copy-pasteable templates adhering to the UCSC Notes style for Obsidian.

---

## 1. Module Hub / Lesson Plan Note Template

**Filename convention:** `📖 <CourseCode> - <Course Name>.md` (e.g., `📖 IS2208 - Enterprise Architecture.md`)  
**Location:** Placed directly in the module's root folder (`Academic Year XX/Semester YY/<CourseCode> - <Course Name>/`).

```markdown
- **Course Code** : <CourseCode>
- **Course Name** : <Course Name>
- **Lecture** : <Lecturer Name(s) with title and/or email, separated by |>

#Lesson-Plan 

> [!important] Goal
> <1-2 paragraphs articulating the core mission, foundational philosophy, and practical significance of this course for an Information Systems / Computer Science undergraduate.>

---
# The specific objectives of the module include:

- **<Objective 1 Title>:** <Concise description of the objective, knowledge area, or skill acquired.>
- **<Objective 2 Title>:** <Concise description of the objective, knowledge area, or skill acquired.>
- **<Objective 3 Title>:** <Concise description of the objective, knowledge area, or skill acquired.>
- **<Objective 4 Title>:** <Concise description of the objective, knowledge area, or skill acquired.>
- **<Objective 5 Title>:** <Concise description of the objective, knowledge area, or skill acquired.>

---
# Topic Covered

1. [[<Topic 1 Name>]]
	- **<Core Concept A>:** <1-line summary of subtopic.>
	- **<Core Concept B>:** <1-line summary of subtopic.>
	- **<Core Concept C>:** <1-line summary of subtopic.>

2. [[<Topic 2 Name>]]
	- **<Core Concept A>:** <1-line summary of subtopic.>
	- **<Core Concept B>:** <1-line summary of subtopic.>

3. [[<Topic 3 Name>]]
	- **<Core Concept A>:** <1-line summary of subtopic.>
	- **<Core Concept B>:** <1-line summary of subtopic.>

---
# <CourseCode> Syllabus

![[<CourseCode> - Syllabus.pdf]]
```

---

## 2. Topic Note Template

**Filename convention:** `<Topic Name>.md` (e.g., `B-Trees and Multi-Way Search Trees.md`)  
**Location:** Placed in the module folder alongside the hub note.

```markdown
This topic covers <concise 1-2 sentence scope summary defining the core technical focus, theoretical foundations, key mechanisms, and practical applications of this lecture topic>.

---

# 1. <First Major Topic / Motivation / Background>

<Introductory prose explaining why this concept exists, what problem it solves, or its fundamental definition.>

- **<Key Term 1>:** <Clear, rigorous explanation of the term or concept.>
- **<Key Term 2>:** <Clear, rigorous explanation of the term or concept.>
- **<Trade-off / Comparison>:** <Discussion of pros, cons, and performance implications.>

> [!important] <Highlight Title>
> <Core takeaway, golden rule, or conceptual breakthrough that students must remember for exams and practical engineering.>

---

# 2. <Core Mechanism / Theoretical Architecture / Math>

<Technical breakdown of how the system/algorithm/model operates step-by-step.>

### 2.1 <Sub-mechanism or Rule Set>
1. **<Rule 1>:** <Description of rule or step.>
2. **<Rule 2>:** <Description of rule or step.>
3. **<Rule 3>:** <Description of rule or step.>

$$\text{Formula / Complexity: } <KaTeX Equation>$$

![<Descriptive Alt Text>](Images/<descriptive_image_name>.png)

---

# 3. <Comparative Analysis / Classification>

| <Dimension / Feature> | <Option A / Paradigm 1> | <Option B / Paradigm 2> |
| :--- | :--- | :--- |
| **<Aspect 1>** | <Description A1> | <Description B1> |
| **<Aspect 2>** | <Description A2> | <Description B2> |
| **<Time / Space Complexity>** | $<O(f(n))>$ | $<O(g(n))>$ |

---

# 4. <Code Implementation / Practical Demonstration>

```<language>
// Production-quality, clear, well-commented code demonstrating the concept
#include <iostream>

class Example {
    // Member explanations
};
```

---

# 5. <Real-World Applications & Industry Context>

- **<Application Domain 1>:** <How enterprise systems, databases, or operating systems use this.>
- **<Application Domain 2>:** <Real-world tool, framework, or standard utilizing this concept.>

---
# Lecture Notes
![[<CourseCode> Lecture <Number>.pdf]]
```

---

## 3. Exam Revision & Quick Reference Guide Template

**Filename convention:** `<CourseCode> - <Course Name> Exam Revision & Quick Reference Guide.md`  
**Location:** Placed in the module folder.

```markdown
# 📑 <CourseCode>: <Course Name> — Exam Quick Revision Guide

#Exam-Prep #<ShortCourseTag> #<CourseCode> #Revision-Guide

> [!Tip] Purpose of this Guide
> A high-yield, concise exam-revision summary covering the core definitions, formulas, modeling rules, analysis frameworks, and critical comparisons for **<CourseCode> (<Course Name>)**.

---

## 1. 🔄 <Core Framework / Lifecycle / Paradigm>

![[<Diagram Name>.png]]

| Phase / Element | Core Objective | Key Deliverable / Output |
| :--- | :--- | :--- |
| **1. <Name>** | <Objective> | <Deliverable> |
| **2. <Name>** | <Objective> | <Deliverable> |

---

## 2. 🏛️ <Key Rules & Invariants>

### <Concept Group 1>
* **<Rule 1>:** <Explanation>
* **<Rule 2>:** <Explanation>

### 🎯 <Decision Criteria / Matrix>
| Category | Symbol / Notation | Rule / Condition |
| :--- | :---: | :--- |
| **<Type A>** | `<symbol>` | <Evaluation logic> |
| **<Type B>** | `<symbol>` | <Evaluation logic> |

---

## 3. 📊 <Formulas & Quantitative Calculations>

#### 📐 <Formula Name 1>
$$\mathbf{<Equation>}$$
* $<Variable 1>$ = <Definition and units>
* $<Variable 2>$ = <Definition and units>

---

## 4. ⚠️ Common Exam Traps & Pitfalls
- **<Pitfall 1>:** <Explanation of mistake and how to avoid it.>
- **<Pitfall 2>:** <Explanation of mistake and how to avoid it.>
```
