A **Stack** is a linear data structure that follows a very specific rule for managing data: elements can only be inserted or deleted from one end, known as the **TOP**.

# 1. The LIFO Principle

The defining characteristic of a stack is the **LIFO (Last-In, First-Out)** principle. This means the last element you put into the stack is the very first one you must take out.

- **Fancy Example:** Think of the **"Undo" button** in a text editor or the **"Back" button** in your web browser. Every action you take or page you visit is "pushed" onto a stack. When you want to go back, the computer "pops" the most recent item off the top to return you to your previous state.

# 2. Basic Stack Operations

To interact with a stack, we use a few fundamental operations:

- **Push:** Adds a new element to the top. Before doing this, the system checks for **Overflow**—a condition where the stack is already full and cannot accept more data.

- **Pop:** Removes the topmost element. Before popping, the system checks for **Underflow**—a condition where you try to remove an item from an empty stack.

- **Peek (or Top):** Lets you look at the value of the top element without actually removing it.

- **isEmpty / isFull:** Logical checks to see if the stack is completely empty or at maximum capacity.

# 3. Implementation Methods

There are two primary ways to build a stack in C:

- **Static Implementation (Arrays):** The stack has a **fixed size**. It is simple but can be inefficient if you don't use all the allocated space.

- **Dynamic Implementation (Linked Lists):** The stack **grows in size** as needed. This is more memory-efficient because it only uses space when data is actually added.

# 4. Why are Stacks Important?

Beyond simple data storage, stacks are essential for:

- **Mathematical Evaluations:** Converting expressions (like Infix to Post-fix) and solving them.

- **Syntax Checking:** Ensuring that parentheses `()` and braces `{}` in code are properly balanced and matched.

- **Recursion:** Stacks are used by the computer to manage function calls and solve complex puzzles like the **Towers of Hanoi**.

---

# Short Note for Memory:

- **TOP:** The only "door" into or out of the stack.

- **LIFO:** **L**ast **I**n, **F**irst **O**ut.

- **Push:** Add to Top.

- **Pop:** Remove from Top.

- **Overflow:** Too much data (Stack Full).

- **Underflow:** No data to give (Stack Empty).

---

# Analogy for Understanding:

Think of a **spring-loaded plate dispenser** in a cafeteria. When a dishwasher adds a plate, they "Push" it onto the top, and the whole pile moves down. When you need a plate, you "Pop" the one off the top. You can’t grab a plate from the middle or the bottom without removing everything above it first—that is the essence of a stack!