# ⭐ A\* Search Algorithm in C++

![A\* Search Banner](https://upload.wikimedia.org/wikipedia/commons/5/5d/AstarProgressAnimation.gif)

> **A\*** (A-star) is a popular **pathfinding** and **graph traversal** algorithm used in various AI and game development applications. This implementation demonstrates a flexible, interactive CLI-based A\* pathfinder using C++.

---

## 📌 Features

* Interactive CLI input for nodes, edges, heuristics
* Supports both **directed** and **undirected** graphs
* Returns the shortest path from **start** to **goal**
* Dynamic priority queue based on `f(n) = g(n) + h(n)`
* Shows **no path** messages if unreachable

---

## 🔧 How the Algorithm Works

A\* uses a **best-first search** strategy and finds the least-cost path from a given start node to a goal node.

### 🧠 Key Concepts:

* `g(n)`: Cost from the start node to the current node `n`.
* `h(n)`: Heuristic estimate of the cost from `n` to the goal.
* `f(n) = g(n) + h(n)`: Estimated total cost of the path through `n`.

### 🔁 Process:

1. Start from the initial node, calculate `f(start)`.
2. Add it to a **priority queue** based on `f(n)`.
3. Expand the node with the **lowest f(n)**.
4. For each neighbor:

   * Calculate `tentative_g = g(current) + cost`.
   * If it improves a previous path, update `g`, recalculate `f`, and queue the new path.
5. Repeat until the goal is found or the queue is empty.

---

## 🛠 Sample Input/Output

### ✅ Input:

```
Enter number of nodes: 4
Enter heuristic values for each node:
Node 1: 1 7
Node 2: 2 6
Node 3: 3 2
Node 4: 4 0
Enter number of edges: 4
Is the graph undirected? (1 for Yes, 0 for No): 1
Enter edges with cost (format: from to cost):
1 2 1
2 3 3
1 3 4
3 4 2
Enter start node: 1
Enter goal node: 4
```

### 🕽 Output:

```
A* Path from 1 to 4: 1 2 3 4
```

### 🖼 Example Screenshots:

**➡️ Input Example:**

![Input Screenshot](https://i.imgur.com/Tej2Jtp.png)

**✅ Output Example:**

![Output Screenshot](https://i.imgur.com/dZYFgj2.png)

---

## 🚀 Applications of A\* Algorithm

| Application Area     | Use Case                                              |
| -------------------- | ----------------------------------------------------- |
| **Game Development** | NPC pathfinding in games like RPGs and strategy games |
| **Robotics**         | Route optimization for autonomous robot navigation    |
| **AI Agents**        | Decision-making in virtual environments               |
| **GPS & Mapping**    | Finding the shortest path in navigation systems       |
| **Network Routing**  | Optimizing packet flow paths in data networks         |

---

## ⏱ Time & Space Complexity

| Metric           | Complexity                                                                   |
| ---------------- | ---------------------------------------------------------------------------- |
| **Time (Worst)** | `O(E)` exponential in worst-case, but usually efficient with good heuristics |
| **Time (Best)**  | `O(log V)` if heuristics are perfect (like Dijkstra + perfect h)             |
| **Space**        | `O(V)` for storing nodes in the open/closed list                             |

---

## 📄 Code Structure

* `main()` – Takes user input and triggers search
* `a_star_search()` – Core logic for A\* algorithm
* `unordered_map<int, vector<pair<int,int>>>` – Graph representation
* `heuristic[]` – Stores heuristic estimates per node

---

## ✅ Dependencies

* C++ STL: `iostream`, `queue`, `vector`, `unordered_map`, `set`, `climits`

---

## 🧪 Try It Yourself

1. Compile using:

   ```bash
   g++ a_star.cpp -o a_star
   ./a_star
   ```

2. Input your graph, heuristics, and run the algorithm!

---

## 🛍 Feedback & Contributions

Feel free to fork, improve or report issues. Contributions are welcome!
