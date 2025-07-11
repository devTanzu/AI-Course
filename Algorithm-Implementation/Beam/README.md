# 🔦 Beam Search Algorithm in C++

![Beam Search Banner](https://upload.wikimedia.org/wikipedia/commons/6/6e/Beam_search_visualization.png)

> **Beam Search** is a heuristic search algorithm that explores a graph level‑by‑level like Breadth‑First Search (BFS) but restricts the frontier to a fixed number of the most promising nodes (the **beam width**). This keeps memory and time usage manageable while still biasing the search toward low‑cost (or low‑heuristic) paths.

---

## 📌 Features

* Interactive CLI: define start node, goal node, and **beam width**
* Heuristic‑guided sorting of each level’s frontier
* Works on **directed graphs** of arbitrary size
* Reports success when goal is reached or failure if beam is exhausted
* Simple, header‑only C++17 code for easy integration

---

## 🔧 How the Algorithm Works

1. **Initialize** the queue `Q` with the start node.
2. **Loop** until `Q` is empty:

   1. Expand all nodes in the current queue to produce a **next‑level list**.
   2. Sort that list by ascending heuristic `h(n)`.
   3. **Trim** the list to at most `beam_width` nodes.
   4. Replace `Q` with those trimmed nodes.
3. If the goal node is dequeued during expansion, **success**. Otherwise, **failure** once the queue empties.

This strategy balances exploration and exploitation: it **prunes** less promising branches early, reducing resource usage compared to full BFS.

---

## 🖥 Sample Input / Output

### ✅ Input

```
Enter number of nodes and edges: 7 8
Enter heuristic values:
10 8 5 7 3 2 0
Enter edges (u v):
0 1
0 2
1 3
1 4
2 4
2 5
4 6
5 6
Enter start, goal, and beam width: 0 6 2
```

### 🔽 Output

```
Goal found at node 6
```

### 🖼 Example Screenshots

**➡️ Input Example:**

![Input Screenshot](https://i.imgur.com/eUO6ASt.png)

**✅ Output Example:**

![Output Screenshot](https://i.imgur.com/Obj43R6.png)

---

## 🚀 Applications of Beam Search

| Domain                          | Use Case                                                             |
| ------------------------------- | -------------------------------------------------------------------- |
| **Natural Language Processing** | Decoding sequences in machine translation (e.g., Transformer models) |
| **Speech Recognition**          | Selecting most probable phoneme/word sequences                       |
| **Game AI**                     | Limited‑width look‑ahead in large branching games                    |
| **Robotics & Planning**         | Path planning with constrained computational resources               |
| **Combinatorial Optimization**  | Approximating solutions to NP‑hard problems (e.g., scheduling)       |

---

## ⏱ Complexity Analysis

| Metric    | Complexity                                                                                   |
| --------- | -------------------------------------------------------------------------------------------- |
| **Time**  | `O(w · d · b)` – where `w` = beam width, `d` = depth to goal, `b` = average branching factor |
| **Space** | `O(w · d)` – stores at most `w` nodes per level                                              |

Beam Search trades optimality for efficiency: **smaller beams** → faster but risk missing optimal path; **larger beams** → closer to BFS cost but higher accuracy.

---

## 📄 Code Structure Overview

* `main()` – Reads graph & heuristic, then performs Beam Search.
* `vector<int> heuristic` – Stores estimated cost to goal for each node.
* `vector<vector<int>> graph` – Adjacency list for directed edges.
* **Key Loop** – Builds `next_level`, sorts by heuristic, trims to `beam_width`.

---

## ✅ Dependencies

* Standard C++17 STL: `iostream`, `vector`, `queue`, `algorithm`

---

## 🧪 Compile & Run

```bash
# Compile
g++ beam_search.cpp -o beam_search

# Execute
./beam_search
```

Enter node/edge data, heuristics, and your desired beam width when prompted.

---

## 🙌 Feedback & Contributions

Feel free to open issues or submit pull requests. Your suggestions help improve this implementation!
