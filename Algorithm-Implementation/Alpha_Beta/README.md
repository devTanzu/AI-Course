# ♟️ Minimax with Alpha–Beta Pruning in C++

![Alpha–Beta Pruning Banner](https://upload.wikimedia.org/wikipedia/commons/9/97/Alpha-beta_pruning.svg)

> **Alpha–Beta pruning** is an optimization technique for the **Minimax** algorithm that reduces the number of nodes evaluated in the game tree, enabling faster decision‑making in two‑player, perfect‑information games such as Chess, Checkers, and Tic‑Tac‑Toe.

---

## 📌 Features

* Interactive CLI—choose tree height and provide leaf scores
* **Automatic tree construction** for a complete binary game tree
* Implements **Maximizer vs. Minimizer** turn alternation
* Efficient pruning using running `alpha` and `beta` bounds
* Reports the **optimal game value** and shows pruning in action (via console output)

---

## 🔧 How the Algorithm Works

### 🧠 Minimax Recap

Minimax explores the entire game tree to choose a move that **maximizes** the player’s minimum gain, assuming the opponent plays perfectly.

### 🚀 Alpha–Beta Optimization

Alpha–Beta introduces two parameters:

* **α (alpha)** – best value that the Maximizer can guarantee so far.
* **β (beta)** – best value that the Minimizer can guarantee so far.

During traversal:

1. **Max nodes** update `alpha = max(alpha, best)`; prune subtree if `alpha ≥ beta`.
2. **Min nodes** update `beta = min(beta, best)`; prune subtree if `beta ≤ alpha`.

This pruning **skips evaluating** branches that cannot improve the final decision, significantly speeding up search without affecting correctness.

---

## 🖥 Sample Input / Output

### ✅ Input

```
Enter height of the game tree: 3
Enter 8 leaf node values:
3 17 2 12 15 25 2 5
```

### 🔽 Output

```
Optimal value with alpha-beta pruning: 12
```

### 🖼 Example Screenshots

**➡️ Input Example:**

![Input Screenshot](https://i.imgur.com/6qA4tq1.png)

**✅ Output Example:**

![Output Screenshot](https://i.imgur.com/batU9yM.png)

---

## 🚀 Applications of Alpha–Beta Pruning

| Domain               | Use Case                                                             |
| -------------------- | -------------------------------------------------------------------- |
| **Game AI**          | Chess engines (e.g., Stockfish), Checkers, Connect‑Four, Tic‑Tac‑Toe |
| **Robotics**         | Decision planning in adversarial environments                        |
| **Security**         | Intrusion‑detection simulations & attacker–defender models           |
| **Economics**        | Competitive market simulations                                       |
| **Operational R\&D** | Optimizing adversarial search problems in research and development   |

---

## ⏱ Complexity Analysis

| Metric               | Complexity                                             |
| -------------------- | ------------------------------------------------------ |
| **Time (No Prune)**  | `O(b^d)` – where `b` is branching factor, `d` is depth |
| **Time (Best‑Case)** | `O(b^{d/2})` with perfect ordering (50 % nodes pruned) |
| **Space**            | `O(b·d)` for recursion stack + evaluation scores       |

In practice, Alpha–Beta often yields **orders‑of‑magnitude** speedups versus plain Minimax, especially with good move ordering heuristics.

---

## 📄 Code Structure

* `main()` – Collects user input and prints the optimal value.
* `alpha_beta()` – Recursive Minimax with Alpha‑Beta pruning.
* `evaluate()` – Leaf‑node evaluation function (returns static score).

```cpp
int alpha_beta(int depth, int node_index, bool is_max,
               const vector<int>& scores, int h,
               int alpha, int beta);
```

---

## ✅ Dependencies

* Standard C++17 (STL): `iostream`, `vector`, `climits`, `algorithm`

---

## 🧪 Try It Yourself

```bash
# Compile
g++ alpha_beta.cpp -o alpha_beta

# Run
./alpha_beta
```

Enter the tree height `h` and provide `2^h` leaf scores when prompted.

---

## 🙌 Contributions & Feedback

Issues, pull requests, and suggestions are welcome! Feel free to fork and enhance the project.
