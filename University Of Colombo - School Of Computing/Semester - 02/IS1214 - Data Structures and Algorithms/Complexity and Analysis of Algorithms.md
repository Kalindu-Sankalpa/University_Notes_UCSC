>[!tip]
>Complexity Analysis is the mathematical technique used to characterize the time or space an algorithm requires relative to the size of its input $(n)$
. It allows us to compare different algorithms to see which one performs better as the problem gets larger, independent of the specific computer or programming language used.

---
# 1. Running Time: Actual vs. Theoretical

There are two ways to look at how **"fast"** a program is:
- **Actual Running Time:**
  Measured in seconds or milliseconds on real hardware. This is unreliable for comparison because it changes based on your CPU, RAM, and even how many other programs are open.
- **Theoretical Running Time (Time Complexity):**
  Instead of seconds, we count basic operations (like comparisons, assignments, or math steps). We express this using **Big O notation** to describe how the work increases as the input size $(n)$ grows.
