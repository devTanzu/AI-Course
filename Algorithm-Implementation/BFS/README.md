# 🔍 Breadth‑First Search (BFS) in C++

![BFS Banner](https://upload.wikimedia.org/wikipedia/commons/4/46/Animated_BFS.gif)

> **Breadth‑First Search (BFS)** is a classic graph traversal algorithm used to find the shortest path in an unweighted graph. It explores all neighboring nodes level‑by‑level using a queue data structure.

---

## 📌 Features

* Interactive CLI: define number of nodes, edges, and direction (directed or undirected)
* Accepts custom graph edges and performs BFS between any two valid nodes
* Displays full path from start to goal node (if reachable)
* Uses a queue of paths, not just nodes, to simplify path reconstruction

---

## 🔧 How the Algorithm Works

1. Start by pushing a **path** with the starting node into a queue.
2. Pop the **front** path from the queue.
3. Check the **last node** in the path:

   * If it’s the goal, return the path.
   * Else, expand all unvisited neighbors.
4. For each neighbor:

   * Clone the current path and append the neighbor.
   * Push the new path into the queue.
5. Continue until goal is found or all paths are exhausted.

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

BFS Path from 0 to 5: 0 1 3 5
```

### 🖼 Example Screenshots

**➡️ Input:**
![Input Screenshot](https://i.imgur.com/fvwdrKk.png)

**✅ Output:**
![Output Screenshot](https://i.imgur.com/0quF1a1.png)

---

## 🚀 Applications of BFS

| Domain               | Use Case                                            |
| -------------------- | --------------------------------------------------- |
| **Shortest Path**    | Unweighted pathfinding between nodes                |
| **Network Analysis** | Finding connectivity or levels in graphs            |
| **AI & Robotics**    | Planning in unweighted state spaces                 |
| **Social Networks**  | Finding mutual connections or degrees of separation |
| **Web Crawlers**     | Level‑order exploration of webpages                 |

---

## ⏱ Complexity Analysis

| Metric    | Complexity                   |
| --------- | ---------------------------- |
| **Time**  | `O(V + E)`                   |
| **Space** | `O(V)` (queue + visited set) |

---

## 📄 Code Structure

* `main()` – Handles user input and calls `bfs()`
* `bfs()` – Performs queue‑based traversal and tracks paths
* `printGraph()` – Debugging helper to visualize the graph

---

## ✅ Dependencies

* Standard C++17: `iostream`, `vector`, `queue`, `unordered_map`, `unordered_set`

---

## 🧪 Compile & Run

```bash
# Compile
g++ bfs.cpp -o bfs

# Run
./bfs
```

Provide the graph details and search parameters at runtime.

---

## 🙌 Contributions & Feedback

Feel free to improve the implementation or suggest enhancements. Happy to collaborate!


