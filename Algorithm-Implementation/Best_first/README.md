# 🚀 Greedy Best‑First Search in C++

![Best‑First Search Banner](https://upload.wikimedia.org/wikipedia/commons/6/66/Greedy_best_first_search.gif)

> **Greedy Best‑First Search (GBFS)** expands the node that appears to be closest to the goal, measured solely by a heuristic `h(n)`. It is memory‑efficient compared to Uniform‑Cost or A\* and often finds a good (though not always optimal) path quickly.

---

## 📌 Features

* Interactive CLI: enter node/edge count, heuristic values, start, and goal
* Uses a **min‑heap** (`priority_queue` with `std::greater`) ordered by `h(n)`
* Supports directed (or easily adapted to undirected) graphs
* Prints each visited node’s heuristic and reports goal discovery
* Lightweight, header‑only C++17 implementation

---

## 🔧 How the Algorithm Works

1. Push the **start node** into a priority queue keyed by `h(start)`.
2. Repeatedly **pop** the node with the *lowest* heuristic.
3. If this node is the **goal**, terminate successfully.
4. Otherwise, push all **unvisited neighbors** into the queue with their heuristic values.
5. Continue until the queue empties (goal unreachable) or goal is found.

> Unlike A\*, GBFS ignores path‑cost `g(n)` and optimizes solely on the heuristic estimate, trading optimality for speed.

---

## 🖥 Sample Input / Output

### ✅ Input

```
Enter number of nodes and edges: 6 7
Enter heuristic values for each node:
Heuristic[0]: 10
Heuristic[1]: 8
Heuristic[2]: 5
Heuristic[3]: 7
Heuristic[4]: 3
Heuristic[5]: 0
Enter edges (u v):
0 1
0 2
1 3
1 4
2 4
4 5
3 5
Enter start and goal node: 0 5
```

### 🔽 Output

```
Visiting Node: 0 with Heuristic: 10
Visiting Node: 2 with Heuristic: 5
Visiting Node: 4 with Heuristic: 3
Visiting Node: 5 with Heuristic: 0
Goal Node 5 found!
```

### 🖼 Example Screenshots

**➡️ Input Example:**
![Input Screenshot](https://i.imgur.com/t1C7fkT.png)

**✅ Output Example:**
![Output Screenshot](https://i.imgur.com/Yh1rX8g.png)

---

## 🚀 Applications of Greedy Best‑First Search

| Domain                 | Use Case                                                      |
| ---------------------- | ------------------------------------------------------------- |
| **Route Planning**     | Quick pathfinding when optimality can be sacrificed for speed |
| **Game Development**   | NPC navigation with low computation budget                    |
| **Web Crawling**       | Heuristic‑guided exploration of link graphs                   |
| **Robotics**           | Real‑time motion planning where a good path suffices          |
| **AI Problem Solving** | Approximate solutions in large search spaces                  |

---

## ⏱ Complexity Analysis

| Metric    | Complexity                       |
| --------- | -------------------------------- |
| **Time**  | `O(E · log V)` (heap operations) |
| **Space** | `O(V)` (visited + queue)         |

GBFS can explore fewer nodes than BFS in practice, but its worst‑case complexity is similar when heuristics are misleading.

---

## 📄 Code Structure Overview

* `main()` – Handles input, maintains visited set, and drives the search loop.
* `vector<int> heuristic` – Stores `h(n)` for each node.
* `vector<vector<int>> graph` – Adjacency list for directed edges.
* `priority_queue<pair<int,int>, …>` – Min‑heap based on heuristic.

---

## ✅ Dependencies

* Standard C++17: `iostream`, `vector`, `queue`, `functional`

---

## 🧪 Compile & Run

```bash
# Compile
g++ best_first.cpp -o best_first

# Execute
./best_first
```

Provide graph data, heuristics, and start/goal nodes when prompted.

---

## 🙌 Feedback & Contributions

Have suggestions or improvements? Open an issue or PR—community contributions are welcome!

