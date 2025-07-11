# 🌲 Depth‑First Search (DFS) in C++

![DFS Banner](https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif)

> **Depth‑First Search (DFS)** is a fundamental graph traversal algorithm that explores as far as possible along each branch before backtracking. It is commonly used in applications like pathfinding, cycle detection, and topological sorting.

---

## 📌 Features

* Interactive CLI input for nodes, edges, and direction (directed or undirected)
* Uses a stack to explore deeper nodes first
* Prints full DFS path from start to goal (if found)
* Displays full graph structure before traversal
* Simple, reusable C++17 implementation

---

## 🔧 How the Algorithm Works

1. Initialize a **stack of paths**, beginning with the start node.
2. While the stack is not empty:

   * Pop the top path.
   * If the last node is the goal, return the path.
   * Else, mark it as visited.
   * Push all unvisited neighbors (in reverse order for proper stack ordering).
3. If the stack is exhausted, no path exists.

This DFS implementation uses **path stacks** instead of traditional recursion to track full paths.

---

## 🖥 Sample Input / Output

### ✅ Input

```
Enter number of nodes: 6
Enter number of edges: 7
Is the graph undirected? (1 for Yes, 0 for No): 1
Enter edges (format: from to):
0 1
0 2
1 3
1 4
2 4
3 5
4 5
Enter start node: 0
Enter goal node: 5
```

### 🔽 Output

```
Graph structure:
0: 1 2
1: 0 3 4
2: 0 4
3: 1 5
4: 1 2 5
5: 3 4

DFS Path from 0 to 5: 0 2 4 5
```

### 🖼 Screenshots

**➡️ Input Example:**
![Input Screenshot](https://i.imgur.com/Tu5eqEd.png)

**✅ Output Example:**
![Output Screenshot](https://i.imgur.com/71eDh2E.png)

---

## 🚀 Applications of DFS

| Domain                      | Use Case                                |
| --------------------------- | --------------------------------------- |
| **Pathfinding**             | Game navigation, maze solving           |
| **Graph Analysis**          | Detecting cycles, connected components  |
| **Topological Sort**        | Scheduling, dependency resolution       |
| **Artificial Intelligence** | Searching game trees or decision spaces |
| **Compilers**               | Control flow and data flow analysis     |

---

## ⏱ Complexity Analysis

| Metric    | Complexity               |
| --------- | ------------------------ |
| **Time**  | `O(V + E)`               |
| **Space** | `O(V)` (visited + stack) |

DFS is memory‑efficient in sparse graphs and provides full traversal.

---

## 📄 Code Structure

* `main()` – Handles input/output and drives the algorithm
* `dfs()` – DFS using a `stack` of node paths
* `printGraph()` – Displays adjacency list before search

---

## ✅ Dependencies

* Standard C++17: `iostream`, `vector`, `stack`, `unordered_map`, `unordered_set`

---

## 🧪 Compile & Run

```bash
# Compile
g++ dfs.cpp -o dfs

# Execute
./dfs
```

Provide the graph structure, direction type, and start/goal nodes when prompted.

---

## 🙌 Feedback & Improvements

Feel free to suggest enhancements or submit contributions. Collaboration is always welcome!
