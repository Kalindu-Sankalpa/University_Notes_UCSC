>[!tip]
>A **Graph** is a non-linear data structure consisting of **Vertices** (nodes representing entities) and **Edges** (arcs representing the connections or relationships between them). Formally, a graph $G$ is defined as $G=(V,E)$.

---
# 1. Types and Terminology

- **Directed vs. Undirected:** In a **directed graph**, edges have a specific direction (from u to v); in an **undirected graph**, the direction is disregarded.
- **Weighted Graphs (Networks):** These graphs associate a numerical value (weight or cost) with each edge.
- **Adjacency:** Two nodes are **adjacent** if they are connected by an edge.
- **Path:** A sequence of vertices connecting two nodes. A **simple path** visits each vertex (except potentially the first and last) only once.
- **Cycle:** A simple path that starts and ends at the same vertex.
- **Degree:** The number of edges incident on a vertex. In directed graphs, we distinguish between **In-degree** (edges arriving) and **Out-degree** (edges leaving).

# 2. Graph Implementation (Representation)

There are two primary ways to store a graph in a computer's memory:

- **Adjacency Matrix:** A 2D square array where `Adj[i][j] = 1` if an edge exists and `0` otherwise. It is simple to implement and good for **dense graphs**, but it wastes memory for **sparse graphs**.
- **Adjacency List:** An array of linked lists where each index represents a vertex and its list contains its neighbors. This is much more **memory-efficient** for sparse graphs.

# 3. Graph Traversals

Traversal is the process of visiting all nodes in a specific order:

- **Depth-First Search (DFS):** Explores as deep as possible along a branch before **backtracking**. It is implemented using a **Stack** or recursion.
- **Breadth-First Search (BFS):** Explores all neighbor nodes at the current level before moving to the next level. It is implemented using a **Queue**.
![[DFS vs BFS graph traversal.png]]

# 4. Spanning Trees and MST

- **Spanning Tree:** A connected subgraph that includes **all vertices** but contains **no cycles**. A graph with n vertices will have $n−1$ edges in its spanning tree.
- **Minimum Spanning Tree (MST):** In a weighted graph, this is the spanning tree with the **minimum total edge weight**.
- **Kruskal’s Algorithm:** A greedy method that sorts all edges by weight and adds the cheapest ones that don't form a cycle.
- **Prim’s Algorithm:** A greedy method that starts from one node and "grows" the tree by repeatedly adding the cheapest edge connected to the current tree.

---
# Short Note for Memory:

- **Graph:** $G=(V,E) (Vertices + Edges)$.
- **DFS:** Think **Deep**; uses a **Stack**.
- **BFS:** Think **Wide**; uses a **Queue**.
- **MST Rule:** n vertices → $n−1$ edges.
- **MST Algorithms:** **Kruskal** (Edge-based) vs. **Prim** (Node-based).

---
# Fancy Examples:

- **Social Networks:** On **Facebook**, a person is a **Vertex**, and a "Friend" relationship is an **Undirected Edge**. On **Twitter**, a "Follow" is a **Directed Edge** because you can follow someone who doesn't follow you back.
- **GPS/Maps:** Cities are **Vertices**, and roads are **Edges**. The distance or travel time on a road is the **Weight**.
- **Civil Planning:** When connecting a set of houses to a **water or power line**, a **Minimum Spanning Tree** ensures every house is connected using the least amount of pipe or cable to save money.
---
# Lecture Notes
![[DSA - Lecture 10.pdf]]