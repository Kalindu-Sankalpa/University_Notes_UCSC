# UCSC Notes Vault Conventions

This document specifies the exact structural, organizational, and Obsidian vault conventions established across the UCSC University Notes repository.

---

## 1. Directory Tree Architecture

```
University_Notes_UCSC/
├── Academic Year 01/
│   ├── Semester - 01/
│   └── Semester - 02/
├── Academic Year 02/
│   ├── Semester 01/
│   └── Semester 02/
├── Academic Year 03/       (Future)
├── Academic Year 04/       (Future)
├── Past Papers/
│   ├── Academic Year 01/
│   ├── Academic Year 02/
│   └── Past Papers.md
├── README.md
└── .agent/
```

### Module Folder Anatomy
Every module MUST reside in its respective Academic Year and Semester directory:
```
<Academic Year>/<Semester>/<CourseCode> - <Course Name>/
├── 📖 <CourseCode> - <Course Name>.md    # Hub / Lesson Plan Note
├── <Topic Name 1>.md                     # Individual Topic Note
├── <Topic Name 2>.md                     # Individual Topic Note
├── Lecture Notes/                        # Source PDF lecture slides
│   ├── <CourseCode> Lecture 01.pdf
│   └── <CourseCode> Lecture 02.pdf
└── Images/                               # Visual diagrams, PNGs, SVGs
    ├── <concept_diagram_1>.png
    └── <concept_diagram_2>.png
```

---

## 2. Naming Standards

| Item | Format / Pattern | Example |
| :--- | :--- | :--- |
| **Module Folder** | `<CourseCode> - <Course Name>` | `IS2202 - Advanced Data Structures and Algorithms` |
| **Hub / Lesson Plan Note** | `📖 <CourseCode> - <Course Name>.md` | `📖 IS2202 Advanced Data Structures and Algorithms.md` |
| **Topic Note** | `<Topic Name>.md` (No numbers in filename) | `B-Trees and Multi-Way Search Trees.md` |
| **Revision Guide** | `<CourseCode> - <Short Name> Exam Revision & Quick Reference Guide.md` | `IS2206 - BPM Exam Revision & Quick Reference Guide.md` |
| **Lecture Slides PDF** | `<CourseCode> Lecture <Num>.pdf` or `<CourseCode> - <Topic>.pdf` | `IS2202 Lecture 04.pdf` |
| **Diagrams / Images** | `snake_case` or hyphenated descriptive `.png`/`.jpg` | `btree_properties_structure.png` |
| **Past Paper PDF** | `<CourseCode> - <Course Name>.pdf` | `IS 2202 - Advanced Data Structures and Algorithms.pdf` |

---

## 3. Obsidian Syntax Rules

1. **Internal Note Linking:**
   - Always use Obsidian wikilinks: `[[Topic Name]]`.
   - Never use relative markdown paths like `[Topic](./Topic.md)` for internal vault notes.
   - Do NOT add aliases unless necessary (`[[Actual Note Name|Display Text]]`).

2. **Image Embeds:**
   - From topic notes, images in the local `Images/` folder can be referenced via:
     - Relative Markdown: `![Caption](Images/diagram_name.png)`
     - Or Obsidian Transclusion: `![[diagram_name.png]]`
   - Always include meaningful alt text/captions.

3. **Lecture Note Transclusions:**
   - Raw PDF lecture slides are transcluded at the end of each topic note:
     ```markdown
     ---
     # Lecture Notes
     ![[IS2202 Lecture 04.pdf]]
     ```
   - Because Obsidian indexes all attachments globally across the vault, the transclusion `![[Filename.pdf]]` renders the embedded PDF viewer natively.

4. **Tags:**
   - Main hub notes: `#Lesson-Plan`
   - Revision guides: `#Exam-Prep #<CourseCode> #Revision-Guide`
   - Past papers index: `#Past-Papers`

---

## 4. Vault Synchronization Checklists

When introducing a new module or academic year:
- [ ] Create the module folder under `Academic Year XX/Semester YY/`.
- [ ] Create `Lecture Notes/` and `Images/` subdirectories.
- [ ] Populate `Lecture Notes/` with source lecture PDFs.
- [ ] Write the Hub / Lesson Plan Note (`📖 <CourseCode> - <Course Name>.md`) with ILOs and `#Topic Covered`.
- [ ] Author topic notes with the standard numbered structure, bold lead-ins, tables, callouts, and PDF transclusions.
- [ ] Update `Past Papers/Past Papers.md` table to list the new course and link its past paper PDF if available.
- [ ] Update `README.md` to reflect the new module in the repository tree and notes coverage table.
