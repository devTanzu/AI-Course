# ⛏️ Depth‑Limited Search (DLS) in C++

![Depth‑Limited Search Banner](https://upload.wikimedia.org/wikipedia/commons/2/28/Depth-limited_search.svg)

> **Depth‑Limited Search** is a variant of Depth‑First Search that explores the search tree up to a user‑defined depth limit `L`. It prevents infinite descent in cyclic or infinite graphs and forms the basis for Iterative Deepening Search (IDS).

---

## 📌 Features

* Interactive CLI: specify number of nodes, edges, start/goal nodes, and depth limit
* Recursive implementation with early exit when goal is found
* Supports directed graphs (easily adapted for undirected)
* Reports success upon finding goal within limit or failure otherwise
* Minimal C++17 code with clear logic

---

## 🔧 How the Algorithm Works

1. **DLS** starts at the `current` node; if it equals the goal, success.
2. If the **depth limit** has reached 0, the call returns false (cutoff).
3. Otherwise, mark `current` as visited and recursively explore each unvisited neighbor with limit‑1.
4. Propagate success back up the recursion stack; if all neighbors fail and limit is exhausted, return false.

> Choosing an appropriate limit balances between resource usage and likelihood of reaching the goal.

---

## 🖥 Sample Input / Output

### ✅ Input

```
Enter number of nodes and edges: 6 7
Enter edges (u v):
0 1
0 2
1 3
1 4
2 4
3 5
4 5
Enter start, goal, and depth limit: 0 5 3
```

### 🔽 Output

```
Goal found at node: 5
```

### 🖼 Example Screenshots

**➡️ Input Example:**
![Input Screenshot](https://i.imgur.com/cSxgItR.png)

**✅ Output Example:**
![Output Screenshot](https://i.imgur.com/m6doQcj.png)

---

## 🚀 Applications of DLS

| Domain             | Use Case                                       |
| ------------------ | ---------------------------------------------- |
| **AI Search**      | Base for Iterative Deepening Search (IDS)      |
| **Puzzle Solving** | Preventing infinite recursion in cyclic spaces |
| **Robotics**       | Bounded exploration with resource constraints  |
| **Game Trees**     | Limited look‑ahead search in turn‑based games  |

---

## ⏱ Complexity Analysis

| Metric    | Complexity                                       |
| --------- | ------------------------------------------------ |
| **Time**  | `O(b^L)` – `b` branching factor, `L` depth limit |
| **Space** | `O(L)` – recursion stack only (no full frontier) |

---

## 📄 Code Structure

* `main()` – Reads graph, parameters, and invokes `DLS()`
* `DLS()` – Recursive Depth‑Limited Search function

```cpp
bool DLS(const vector<vector<int>>& graph,
         int current, int goal,
         int limit, vector<bool>& visited);
```

---

## ✅ Dependencies

* Standard C++17: `iostream`, `vector`

---

## 🧪 Compile & Run

```bash
# Compile
g++ dls.cpp -o dls

# Execute
./dls
```

Enter your graph, start & goal nodes, and chosen depth limit when prompted.

---

## 🙌 Contributions & Feedback

Feel free to open issues or submit pull requests for improvements, bug fixes, or feature additions.

