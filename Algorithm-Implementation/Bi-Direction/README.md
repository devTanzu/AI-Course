# 🔁 Bidirectional Search in C++

![Bidirectional Search](https://upload.wikimedia.org/wikipedia/commons/9/9b/Bidirectional_search.svg)

> **Bidirectional Search** is an efficient graph traversal algorithm that runs two simultaneous BFS traversals — one forward from the start node and one backward from the goal node — until they meet. This reduces the effective search space from `O(b^d)` to `O(b^{d/2})`.

---

## 📌 Features

* Interactive CLI: define number of nodes, edges, start, and goal
* Undirected graph structure
* Performs two simultaneous BFS traversals
* Detects intersection between forward and backward paths
* Compact C++17 implementation using `queue` and `unordered_set`

---

## 🔧 How the Algorithm Works

1. **Initialize** two queues: one from the start node, one from the goal.
2. Expand both sides alternately using BFS.
3. Keep track of visited nodes in both directions.
4. If any node is found in both visited sets — a **meeting point** — the search terminates.
5. If queues are exhausted without meeting, no path exists.

> This algorithm is ideal for large undirected graphs with a unique start and goal.

---

## 🖥 Sample Input / Output

### ✅ Input

```
Enter number of nodes and edges: 6 7
Enter edges:
0 1
0 2
1 3
2 4
3 5
4 5
2 5
Enter start and goal: 0 5
```

### 🔽 Output

```
Path found (meeting point at 3 or 5)
```

### 🖼 Example Screenshots

**➡️ Input View:**
![Input Screenshot](https://i.imgur.com/NKOdx9h.png)

**✅ Output View:**
![Output Screenshot](https://i.imgur.com/WrdbRzK.png)

---

## 🚀 Applications

| Domain              | Use Case                                                     |
| ------------------- | ------------------------------------------------------------ |
| **Social Networks** | Find shortest connection between two users                   |
| **Routing Systems** | Pathfinding in road networks                                 |
| **AI/Game Agents**  | Shortest path search in symmetric game spaces                |
| **Web Crawling**    | Bidirectional traversal between pages                        |
| **Databases**       | Efficient relationship resolution in graph DBs (e.g., Neo4j) |

---

## ⏱ Complexity Analysis

| Metric    | Complexity                                             |
| --------- | ------------------------------------------------------ |
| **Time**  | `O(b^{d/2})` – much faster than BFS (`O(b^d)`)         |
| **Space** | `O(b^{d/2})` – stores visited nodes in both directions |

---

## 📄 Code Structure

* `main()` – Input reading, graph building, execution driver
* `bidirectional_search()` – Dual BFS and meeting point detection

```cpp
bool bidirectional_search(vector<vector<int>>& graph, int start, int goal);
```

---

## ✅ Dependencies

* C++17 Standard: `iostream`, `vector`, `queue`, `unordered_set`

---

## 🧪 Compile & Run

```bash
# Compile
g++ bidirectional.cpp -o bidirectional

# Execute
./bidirectional
```

Enter nodes, edges, and search endpoints during runtime.

---

## 🙌 Contributions & Feedback

Found a bug or have an enhancement in mind? Feel free to fork, submit a pull request, or share suggestions.


