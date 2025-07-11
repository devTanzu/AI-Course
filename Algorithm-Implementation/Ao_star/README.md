# 🔄 AO\* (Hill‑Climbing‑style) Search in C++

![AO\* Search Banner](https://upload.wikimedia.org/wikipedia/commons/4/43/Hill_climbing.gif)

> This implementation demonstrates a **Greedy Hill‑Climbing / AO**\*‑style search on a directed graph using heuristic values. The algorithm repeatedly moves to the neighbor with the lowest heuristic until no improvement is possible, representing a local optimum.

---

## 📌 Features

* Interactive CLI: specify node count, heuristic values, and edges
* Supports arbitrary directed graphs
* Prints the traversal path and the final “peak” node
* Compact, header‑only C++17 code

---

## 🔧 How the Algorithm Works

1. **Initialize** at the start node `current`.
2. **Evaluate neighbors**: choose the neighbor with strictly smaller heuristic `h(n)`.
3. **Move to best neighbor** if improvement exists; otherwise **stop** (local peak reached).
4. Repeat until no neighbor has a lower heuristic.

> Unlike exhaustive search, Hill‑Climbing focuses on **local** improvements; AO\* variants may incorporate AND/OR branching, but this simplified version demonstrates the core greedy ascent.

---

## 🖥 Sample Input / Output

### ✅ Input

```
Enter number of nodes: 5
Enter heuristic values:
7 6 3 1 0
Enter number of edges: 6
Enter edges (u v):
0 1
0 2
1 3
2 3
3 4
1 4
Enter start node: 0
```

### 🔽 Output

```
Current: 0 with h=7
Current: 2 with h=3
Current: 3 with h=1
Current: 4 with h=0
Reached peak at node: 4
```

### 🖼 Example Screenshots

**➡️ Input Example:**

![Input Screenshot](https://i.imgur.com/3D6Yj7I.png)

**✅ Output Example:**

![Output Screenshot](https://i.imgur.com/ZbPWeTx.png)

---

## 🚀 Applications

| Field                   | Use Case                                             |
| ----------------------- | ---------------------------------------------------- |
| **AI Planning**         | Quick heuristic descent for task planning            |
| **Robotics**            | Simple local navigation and obstacle avoidance       |
| **Operations Research** | Finding near‑optimal scheduling or routing solutions |
| **Machine Learning**    | Parameter tuning with greedy neighborhood search     |

---

## ⏱ Complexity Analysis

| Metric    | Complexity                                            |
| --------- | ----------------------------------------------------- |
| **Time**  | `O(V + E)` in the worst case (each edge visited once) |
| **Space** | `O(V)` for heuristic array and adjacency lists        |

> **Note**: This greedy approach may converge to **local optima**; without backtracking or randomness it cannot guarantee the global optimum in non‑convex search spaces.

---

## 📄 Code Structure

* `main()`                   – Reads input, drives search loop
* `vector<int> heuristic`    – Stores `h(n)` for each node
* `vector<vector<int>> graph` – Adjacency list of directed edges

---

## ✅ Dependencies

* Standard C++17: `iostream`, `vector`, `limits`

---

## 🧪 Try It Yourself

```bash
# Compile
g++ ao_star.cpp -o ao_star

# Run
./ao_star
```

Provide node/edge data and observe the greedy descent.

---

## 🙌 Contributions & Feedback

Pull requests, issue reports, and suggestions are welcome!

