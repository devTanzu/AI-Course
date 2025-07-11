# 🔍 Best-First Search with Heuristic in C++

![Best First Search](https://upload.wikimedia.org/wikipedia/commons/1/11/Best-first-search-animation.gif)

> **Best-First Search** is a heuristic-driven graph traversal algorithm that explores nodes based on their estimated cost (heuristic value) to the goal. It prioritizes nodes that appear to be closer to the goal, making it an informed and efficient search.

---

## 📌 Features

- Uses a priority queue (min-heap) ordered by heuristic values.
- Tracks and prints the exact path from the start node to the goal node.
- Supports undirected graphs with user-defined nodes, edges, and heuristic values.
- Displays nodes visited along with their heuristic values during traversal.
- Uses a parent array to reconstruct the path once the goal is reached.

---

## 🔧 How the Algorithm Works

1. Initialize a priority queue with the start node and its heuristic value.
2. While the queue is not empty:
   - Extract the node with the lowest heuristic value.
   - If this node is the goal, reconstruct and return the path.
   - Otherwise, mark it visited and enqueue all unvisited neighbors prioritized by their heuristic values.
3. If the queue empties without reaching the goal, report that the goal is unreachable.

---

## 🖥 Sample Input / Output

### Input

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
3 5
4 5
Enter start and goal node: 0 5


### Output

Visiting Node: 0 with Heuristic: 10
Visiting Node: 2 with Heuristic: 5
Visiting Node: 4 with Heuristic: 3
Visiting Node: 1 with Heuristic: 8
Visiting Node: 3 with Heuristic: 7
Visiting Node: 5 with Heuristic: 0
Goal Node 5 found!
Path: 0 2 4 5


---

## 🚀 Applications

| Domain            | Use Case                                              |
|-------------------|-------------------------------------------------------|
| **AI Pathfinding**| Efficient search in games and robotics                 |
| **Navigation**    | Route planning with heuristic guidance                  |
| **Networking**    | Packet routing with cost estimates                      |
| **Robotics**      | Real-time decision making with estimated costs          |
| **Search Algorithms** | Foundation for A* and other heuristic-based methods  |

---

## ⏱ Complexity Analysis

| Metric     | Complexity                          |
|------------|-----------------------------------|
| **Time**   | `O(V log V + E)` where V = nodes, E = edges (due to priority queue) |
| **Space**  | `O(V)` for storing visited, parents, and priority queue            |

---

## 📄 Code Structure

- `main()` — Reads graph data, heuristic values, and runs best-first search.
- Uses a priority queue ordered by heuristic.
- Reconstructs path via parent pointers once goal is reached.

---

## ✅ Dependencies

- Standard C++17 headers: `iostream`, `vector`, `queue`, `stack`

---

## 🧪 Compile & Run

```bash
# Compile
g++ best_first.cpp -o best_first

# Run
./best_first
```

Enter your graph, start & goal nodes, and chosen depth limit when prompted.

---

## 🙌 Contributions & Feedback

Feel free to open issues or submit pull requests for improvements, bug fixes, or feature additions.
