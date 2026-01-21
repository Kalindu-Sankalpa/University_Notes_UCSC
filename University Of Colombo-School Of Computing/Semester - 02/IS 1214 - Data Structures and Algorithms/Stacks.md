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

---
# Lecture Notes

![[DSA - Lecture 02.pdf]]

---
# Code Examples

## Pseudo Code for Stack Push

```pseudo
PSEUDOCODE: PUSH OPERATION

PROCEDURE PUSH(STACK, TOP, MAX, ITEM)
1. [Check for overflow]
   IF TOP = MAX-1 THEN
	   PRINT "Stack Overflow"
      RETURN
   END IF

2. [Increment TOP]
   SET TOP = TOP + 1

3. [Insert item]
   SET STACK[TOP] = ITEM

4. [Success]
   PRINT "Element pushed successfully"
   RETURN
END PROCEDURE
```

# C code for Push Stack

```C
#include <stdio.h>
#define MAX 5  // Maximum size of stack

int stack[MAX];
int top = -1;  // Stack is empty

// Push function
void push(int item) {
    // Step 1: Check for overflow
    if (top == MAX - 1) {
        printf("Stack Overflow! Cannot push %d\n", item);
        return;
    }
    
    // Step 2: Increment TOP
    top++;
    
    // Step 3: Insert item
    stack[top] = item;
    
    // Step 4: Success
    printf("✓ Pushed %d onto stack\n", item);
}

// Display stack
void display() {
    if (top == -1) {
        printf("Stack is empty!\n");
        return;
    }
    
    printf("Stack (TOP → BOTTOM): ");
    for (int i = top; i >= 0; i--) {
        printf("%d ", stack[i]);
        if (i == top) printf("← TOP");
        printf("\n");
    }
}

// Main function
int main() {
    printf("=== Stack Push Operation ===\n\n");
    
    // Push some elements
    push(10);
    push(20);
    push(30);
    push(40);
    push(50);  // This fills the stack (MAX=5)
    
    printf("\nCurrent stack:\n");
    display();
    
    // Try to overflow
    printf("\nTrying to push 60 (should overflow):\n");
    push(60);
    
    return 0;
}
```