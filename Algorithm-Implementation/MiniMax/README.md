# 🎮 Minimax Algorithm in C++

> Minimax is a classic recursive algorithm used in decision making and game theory to find the optimal move for a player, assuming the opponent also plays optimally. It evaluates the game tree to maximize the player's minimum gain.

---

## 📌 Features

- Works on a perfect binary tree game structure.
- Recursively evaluates all possible moves to a specified depth (height).
- Alternates between maximizing and minimizing players.
- Takes leaf node scores as input to evaluate terminal states.
- Outputs the optimal value for the starting player.

---

## 🔧 How the Algorithm Works

1. Represent the game as a tree where nodes correspond to game states.
2. The algorithm recursively explores all possible moves to the specified depth.
3. At maximizing levels, it picks the move with the highest value.
4. At minimizing levels, it picks the move with the lowest value.
5. The evaluation stops at the leaf nodes where scores are assigned.
6. The root’s returned value is the optimal outcome assuming perfect play.

---

## 🖥 Sample Input / Output

### Input

Enter height of the game tree: 3
Enter 8 leaf node values:
3 5 2 9 12 5 23 23


### Output

Optimal value: 12


---

## 🚀 Applications

| Domain         | Use Case                                      |
|----------------|-----------------------------------------------|
| **Game AI**    | Decision making in turn-based games like Chess, Tic-Tac-Toe |
| **Artificial Intelligence** | Strategy planning under adversarial conditions  |
| **Economic Modeling** | Simulating competitive scenarios                     |
| **Operations Research** | Optimal decision making in multi-agent systems     |

---

## ⏱ Complexity Analysis

| Metric     | Complexity                  |
|------------|-----------------------------|
| **Time**   | \(O(b^d)\), where \(b=2\) (binary tree), \(d\) = depth/height of tree |
| **Space**  | \(O(d)\) due to recursion stack               |

---

## 📄 Code Structure

- `main()` — Reads tree height and leaf node scores; runs minimax and prints result.
- `minimax()` — Recursive function alternating maximizing and minimizing steps.
- `evaluate()` — Returns leaf node score.

---

## ✅ Dependencies

- Standard C++ headers: `iostream`, `vector`, `climits`, `algorithm`

---

## 🧪 Compile & Run

```bash
# Compile
g++ minimax.cpp -o minimax

# Run
./minimax
```

Provide node/edge data and observe the greedy descent.

---

## 🙌 Contributions & Feedback

Pull requests, issue reports, and suggestions are welcome!