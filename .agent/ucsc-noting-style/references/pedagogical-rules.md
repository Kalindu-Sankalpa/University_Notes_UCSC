# UCSC Notes Pedagogical & Content Rules

This document outlines the pedagogical philosophy, tone, formatting heuristics, and content standards required when crafting UCSC notes.

---

## 1. Pedagogical Tone & Target Audience

- **Target Audience:** Undergraduates in Information Systems (IS) and Computer Science (CS) at the University of Colombo School of Computing (UCSC).
- **Voice:** Clear, authoritative, academically rigorous, yet accessible. Avoid dry academic passive voice; use crisp, direct explanations that bridge high-level intuition and low-level mechanics.
- **Core Principle:** Teach the *why* alongside the *what*. When introducing an algorithm or architectural pattern, always explain the failure mode of simpler approaches (e.g., why BSTs fail on disk storage, necessitating B-Trees; why multipath inheritance causes ambiguity, requiring virtual base classes).

---

## 2. Sectional Formatting Heuristics

### A. Numbered Major Headings
All top-level sections in a topic note MUST be numbered:
- `# 1. Motivation / Core Concept`
- `# 2. Theoretical Architecture & Invariants`
- `## 2.1 Subtopic / Case Analysis`
- `### 2.1.1 Granular Breakdown`
- `# 3. Performance & Comparative Analysis`

*Do not use unnumbered top-level headings except for the concluding `# Lecture Notes` embed.*

### B. Bold Lead-in Bullet Points
Never write bare bullet points without an anchor term. Every bullet item must begin with a bold lead-in term or phrase:
```markdown
- **Uniform Depth:** All leaf nodes in a B-Tree must reside on the exact same depth level.
- **Key Capacity:** Each node stores between $\lceil m/2 \rceil - 1$ and $m - 1$ keys.
```

### C. Strategic Use of Obsidian Callouts
Callouts should be used sparingly and deliberately to highlight critical concepts:
- `> [!important] <Title>`: Use for fundamental theorems, system breakthroughs, and invariant solutions.
- `> [!tip] <Title>`: Use for course objectives, exam strategies, and best practices.
- `> [!warning] <Title>`: Use for compilation errors, memory leaks, security vulnerabilities, or anti-patterns.
- `> [!info] <Title>`: Use for historical context, syllabus context, or prerequisites.

---

## 3. High-Density Tables

Tables are mandatory whenever:
1. **Comparing Multiple Paradigms:** E.g., Symmetric vs. Asymmetric encryption, Stream vs. Block ciphers, Separate Chaining vs. Open Addressing.
2. **Summarizing Algorithmic Complexity:** Tables containing Operation, Average Time, Worst Time, Space Complexity, and Auxiliary Constraints.
3. **Classifying States / Phases:** E.g., BPM 6-phase lifecycle, CPU instruction cycle stages, or UML diagram classifications.

Example:
```markdown
| Operation | Average Case | Worst Case | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Search** | $O(\log n)$ | $O(\log n)$ | $O(1)$ |
| **Insert** | $O(\log n)$ | $O(\log n)$ | $O(1)$ |
| **Delete** | $O(\log n)$ | $O(\log n)$ | $O(1)$ |
```

---

## 4. Mathematical & Algorithmic Rigor (LaTeX / KaTeX)

- **Inline Math:** Wrap variables, asymptotic complexities, and arithmetic in single dollars:
  - `$O(\log_m n)$`, `$\Theta(V + E)$`, `$\alpha = \frac{n}{m}$`, `$\lceil m/2 \rceil$`.
- **Display Math:** Center formal definitions, series, or multi-variable formulas in double dollars:
  ```markdown
  $$\text{Load Factor } \alpha = \frac{n}{m} \quad \left(\frac{\text{Total Stored Elements}}{\text{Total Table Slots}}\right)$$
  ```
- **Instruction Counts & Derivations:** When deriving sequential code complexity, provide exact step derivations (e.g., $2n+2$, $3n^2+4n+2$).

---

## 5. Code Demonstration Standards

1. Always specify the language identifier (e.g. ````cpp`, ````c`, ````python`, ````sql`).
2. Code examples must be compilable, clean, and modern (e.g., C++11/C++17 standards, proper header includes).
3. Annotate syntax and failure points directly with inline comments:
   ```cpp
   // COMPILE ERROR: request for member 'name' is ambiguous!
   // With virtual inheritance, only one subobject exists in memory
   ```
4. Contrast the naive or error-prone approach with the idiomatic, correct solution.

---

## 6. Conceptual Analogies & Real-World Anchors

- **Intuitive Analogies:** Make abstract computer science concepts memorable (e.g., "grocery shopping analogy for time vs. space", "hash fingerprinting", "refining raw materials for normalization", "fat and shallow trees").
- **Enterprise Anchoring:** Conclude notes with a dedicated section listing where the concept is used in production systems (e.g., Linux kernel schedulers, PostgreSQL index engines, Git SHA-1 hashing, TLS certificates).
