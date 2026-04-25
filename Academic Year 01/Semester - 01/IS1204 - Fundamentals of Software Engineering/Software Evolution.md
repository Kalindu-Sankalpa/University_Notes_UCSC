# 1 The Inevitability of Change

Software change is **inevitable** because new requirements emerge as software is used, business environments evolve, and errors must be repaired. Organizations invest heavily in software as a critical business asset, and to maintain this value, systems must be constantly updated. In large companies, the **majority of the software budget** is actually devoted to evolving existing systems rather than developing new ones.

# 2 Evolution, Servicing, and Phase-out

A software system's life cycle after initial development typically moves through three stages:

- **Evolution:** The stage where the system is in operational use and evolves as **new requirements** are proposed and implemented.
- **Servicing:** The stage where the software remains useful, but changes are limited to **bug fixes** and environmental adaptations (e.g., OS updates); no new functionality is added.
- **Phase-out:** The stage where the software may still be used, but **no further changes** of any kind are made.

# 3 The Evolution Process

The process of evolution is driven by **proposals for change**, which should be linked to the specific components they affect to estimate cost and impact.

1. **Change Identification:** Continues throughout the system’s lifetime.
2. **Implementation:** Revisions are designed and tested. This often involves **"program understanding"** learning how the system is structured and how a change might affect its existing functionality.
3. **Urgent Changes:** In emergencies (like serious system faults or rapid business shifts), changes may bypass the full software engineering process for immediate delivery.

# 4 Lehman’s Laws of Program Evolution

Based on long-term studies, several "laws" (observations) describe how large systems evolve:

- **Continuing Change:** A program used in a real-world environment must necessarily change or it will become progressively less useful.
- **Increasing Complexity:** As a program evolves, its structure becomes more complex unless extra resources are spent to simplify it.
- **Declining Quality:** System quality will decline unless it is modified to reflect changes in its operational environment.

# 5 Types of Software Maintenance

Maintenance involves modifying a program after it is in use. There are four primary types:

1. **Corrective Maintenance:** Repairing bugs and defects discovered after release.
2. **Adaptive Maintenance:** Modifying software to work in new environments (e.g., new hardware or operating systems).
3. **Perfective Maintenance:** Enhancing functionality or performance based on user feedback.
4. **Preventive Maintenance:** Identifying and fixing potential problems before they occur (e.g., **Refactoring**).

# 6 Re-engineering and Refactoring

To manage the long-term health of software, engineers use two key techniques:

- **System Re-engineering:** Re-structuring or re-writing part of a legacy system without changing its functionality to make it easier to maintain. This reduces risk and cost compared to developing a brand-new system.
- **Refactoring:** A continuous process of improvement during development and evolution to **prevent code degradation**. It focuses on improving structure rather than adding new features.

# 7 Configuration Management (CM)

Configuration management is the process of managing a changing software system by applying standards and procedures. It is essential for teams because systems often have **multiple versions** under development and in use simultaneously.

- **Version Management:** Tracking different builds (e.g., Version 1.0 vs. 2.1).
- **System Integration:** Building a system version by compiling and linking specific component versions.
- **Problem Tracking:** Allowing users to report bugs and allowing developers to track who is fixing them.
- **Configuration Database:** A central database used to record all CM information, such as which platform a version requires or which components are affected by a specific change.