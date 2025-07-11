# 🔍 Iterative Deepening Search (IDS) Algorithm in C++

> Iterative Deepening Search combines the depth-first search's space efficiency and breadth-first search's completeness by performing depth-limited searches with increasing depth limits until the goal is found.

---

## 📌 Features

- Uses Depth-Limited Search (DLS) as a building block.
- Iteratively increases the depth limit to avoid the pitfalls of DFS and BFS.
- Stops when the goal node is found or maximum depth is reached.
- Works well for large or infinite search spaces where the depth of the solution is unknown.
- Supports directed graphs with user-defined nodes and edges.

---

## 🔧 How the Algorithm Works

1. Start with depth limit = 0.
2. Perform a depth-limited DFS (DLS) to the current limit.
3. If the goal is found, stop.
4. Otherwise, increase the depth limit and repeat.
5. Continue until the goal is found or the maximum depth limit is reached.

This method explores nodes level by level, but uses depth-first traversal with limited depth.

---

## 🖥 Sample Input / Output

### Input

Enter number of nodes and edges: 6 7
Enter edges (u v):
0 1
0 2
1 3
1 4
2 4
3 5
4 5
Enter start and goal node: 0 5


### Output
Goal found at depth 3


---

## 🚀 Applications

| Domain            | Use Case                                       |
|-------------------|------------------------------------------------|
| **Artificial Intelligence** | Search in large or infinite state spaces    |
| **Game Playing**  | Finding solutions in game trees                 |
| **Robotics**      | Planning with unknown or large search depths    |
| **Tree/Graph Traversal** | Memory-efficient exploration of nodes        |
| **Problem Solving** | Iterative refinement in unknown solution depths|

---

## ⏱ Complexity Analysis

| Metric     | Complexity                       |
|------------|---------------------------------|
| **Time**   | \(O(b^d)\), where \(b\) = branching factor, \(d\) = depth of solution |
| **Space**  | \(O(bd)\), linear space due to DFS stack                  |

---

## 📄 Code Structure

- `main()` — Reads graph input and runs IDS with a max depth.
- `IDS()` — Iterates increasing depth limits calling DLS.
- `DLS()` — Performs depth-limited DFS with visited tracking.

---

## ✅ Dependencies

- Standard C++ headers: `iostream`, `vector`

---

## 🧪 Compile & Run

```bash
# Compile
g++ ids.cpp -o ids

# Run
./ids
```

Enter your graph, start & goal nodes, and chosen depth limit when prompted.

---

## 🙌 Contributions & Feedback

Feel free to open issues or submit pull requests for improvements, bug fixes, or feature additions.