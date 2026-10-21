#!/usr/bin/env python3
"""
UCSC Notes Module Scaffolder
Creates a new module directory with the standardized UCSC noting layout:
  - Hub Note: 📖 <CourseCode> - <Course Name>.md
  - Subdirectories: Lecture Notes/, Images/
  - Optional Topic Note stubs linked to the hub note
"""

import argparse
import os
import sys
from pathlib import Path

def normalize_academic_year(year_input: str) -> str:
    cleaned = year_input.strip()
    if cleaned.isdigit():
        return f"Academic Year {int(cleaned):02d}"
    if cleaned.lower().startswith("year"):
        num = "".join(filter(str.isdigit, cleaned))
        return f"Academic Year {int(num):02d}"
    if "academic year" in cleaned.lower():
        num = "".join(filter(str.isdigit, cleaned))
        return f"Academic Year {int(num):02d}"
    return cleaned

def normalize_semester(sem_input: str, year_num: int) -> str:
    cleaned = sem_input.strip()
    num = 1
    if cleaned.isdigit():
        num = int(cleaned)
    elif "sem" in cleaned.lower():
        num = int("".join(filter(str.isdigit, cleaned)) or 1)
    
    # Year 01 uses "Semester - 01" / "Semester - 02", Year 02+ uses "Semester 01" / "Semester 02"
    if year_num == 1:
        return f"Semester - {num:02d}"
    return f"Semester {num:02d}"

def create_module(
    base_dir: Path,
    year_str: str,
    sem_str: str,
    course_code: str,
    course_name: str,
    lecturers: str = "TBA",
    topics: list = None
):
    year_num = int("".join(filter(str.isdigit, year_str)) or 1)
    year_dir_name = normalize_academic_year(year_str)
    sem_dir_name = normalize_semester(sem_str, year_num)
    
    module_folder_name = f"{course_code} - {course_name}"
    module_path = base_dir / year_dir_name / sem_dir_name / module_folder_name
    
    # Create module directory and assets folders
    module_path.mkdir(parents=True, exist_ok=True)
    lecture_notes_dir = module_path / "Lecture Notes"
    images_dir = module_path / "Images"
    lecture_notes_dir.mkdir(exist_ok=True)
    images_dir.mkdir(exist_ok=True)
    
    topics = topics or []
    
    # Build Hub / Lesson Plan Note content
    hub_filename = f"📖 {course_code} - {course_name}.md"
    hub_path = module_path / hub_filename
    
    topics_covered_block = []
    if topics:
        for idx, topic in enumerate(topics, 1):
            topics_covered_block.append(f"{idx}. [[{topic}]]\n\t- **Key Concepts:** Overview, definitions, and foundational mechanics.")
    else:
        topics_covered_block.append("1. [[Topic 01 Name]]\n\t- **Key Concepts:** Foundational definitions and principles.")
    
    hub_content = f"""- **Course Code** : {course_code}
- **Course Name** : {course_name}
- **Lecture** : {lecturers}

#Lesson-Plan 

> [!important] Goal
> The primary goal of {course_code}: {course_name} is to equip students with comprehensive theoretical foundations and practical competencies in this domain.

---
# The specific objectives of the module include:

- **Mastering Foundational Principles:** Developing a deep understanding of core concepts, architectures, and theoretical paradigms.
- **Applied Engineering & Analysis:** Evaluating performance trade-offs, formal models, and system behaviors under real-world constraints.
- **Practical Implementation:** Building and validating solutions using standard industry tooling, languages, and frameworks.

---
# Topic Covered

{chr(10).join(topics_covered_block)}

---
# {course_code} Syllabus

![[{course_code} - Syllabus.pdf]]
"""
    
    if not hub_path.exists():
        hub_path.write_text(hub_content, encoding="utf-8")
        print(f"Created Hub Note: {hub_path.relative_to(base_dir)}")
    else:
        print(f"Hub Note already exists: {hub_path.relative_to(base_dir)}")
        
    # Create topic stubs
    for topic in topics:
        topic_path = module_path / f"{topic}.md"
        if not topic_path.exists():
            stub_content = f"""This topic covers the fundamental concepts, theoretical models, practical mechanics, and implementation details of {topic}.

---

# 1. Introduction and Motivation

Detailed breakdown of {topic}, why it is needed, and the core problems it addresses.

- **Foundational Definition:** Rigorous explanation of the primary concept.
- **Architectural Motivation:** Engineering context and trade-offs.

> [!important] Core Insight
> Key takeaways and governing rules for {topic}.

---

# 2. Mechanics and Core Architecture

### 2.1 Theoretical Principles
- **Invariants:** Mandatory rules and constraints.
- **Operational Steps:** Step-by-step lifecycle or algorithm.

---

# 3. Comparative Analysis & Performance

| Technique / Approach | Time Complexity | Space Complexity | Practical Notes |
| :--- | :--- | :--- | :--- |
| **Standard Approach** | $O(n)$ | $O(1)$ | Baseline behavior |
| **Optimized Approach** | $O(\\log n)$ | $O(n)$ | Scalable solution |

---

# 4. Real-World Applications
- **Industry Systems:** Usage in databases, operating systems, and distributed platforms.

---
# Lecture Notes
![[{course_code} - {topic}.pdf]]
"""
            topic_path.write_text(stub_content, encoding="utf-8")
            print(f"Created Topic Stub: {topic_path.relative_to(base_dir)}")
            
    print("\n[SUCCESS] Module scaffolding complete!")
    print(f"Target Directory: {module_path}")

def main():
    parser = argparse.ArgumentParser(description="Scaffold a new UCSC Notes Module")
    parser.add_argument("--year", required=True, help="Academic Year (e.g. 2 or 'Academic Year 02')")
    parser.add_argument("--sem", required=True, help="Semester (e.g. 1 or 'Semester 01')")
    parser.add_argument("--code", required=True, help="Course Code (e.g. IS2208)")
    parser.add_argument("--name", required=True, help="Course Name (e.g. 'Enterprise Architecture')")
    parser.add_argument("--lecturer", default="TBA", help="Lecturer name(s)")
    parser.add_argument("--topics", nargs="*", default=[], help="List of topic titles")
    parser.add_argument("--root", default=".", help="Root path of the repository")

    args = parser.parse_args()
    base_dir = Path(args.root).resolve()
    
    create_module(
        base_dir=base_dir,
        year_str=args.year,
        sem_str=args.sem,
        course_code=args.code,
        course_name=args.name,
        lecturers=args.lecturer,
        topics=args.topics
    )

if __name__ == "__main__":
    main()
