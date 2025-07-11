# ⛰️ Hill Climbing Algorithm in C++

![Hill Climbing](https://upload.wikimedia.org/wikipedia/commons/5/5f/Hill_Climbing_Optimization.gif)

> Hill Climbing is a heuristic search technique used for mathematical optimization problems. It iteratively moves toward increasing value of an objective function until a peak (local maximum) is reached.

---

## 📌 Features

- Optimizes a simple mathematical function (e.g., \( f(x) = -x^2 + 4x \))
- Starts from a user-defined point
- Moves in small steps based on a step size
- Stops when no improvement is found or max iterations reached
- Easy to modify for different objective functions

---

## 🔧 How the Algorithm Works

1. Start at an initial guess (`start`).
2. Evaluate the objective function at the current position.
3. Compare values at neighbors (`current + step_size` and `current - step_size`).
4. Move to the neighbor if it improves the function value.
5. Repeat until no neighbor improves the value or max iterations reached.

This greedy approach climbs uphill on the objective landscape, aiming to find a local maximum.

---

## 🖥 Sample Input / Output

### Input

Enter starting point: 0
Enter step size: 0.1
Enter maximum iterations: 100

shell
Copy
Edit

### Output

Hill Climbing Solution: x = 2, f(x) = 4


---

## 🚀 Applications

| Domain           | Use Case                                      |
|------------------|-----------------------------------------------|
| **Optimization** | Finding local maxima or minima in functions  |
| **Machine Learning** | Parameter tuning and training optimization  |
| **Robotics**     | Path planning and control                      |
| **Artificial Intelligence** | Heuristic search and game playing      |
| **Operations Research** | Resource allocation and scheduling         |

---

## ⏱ Complexity Analysis

| Metric     | Complexity             |
|------------|------------------------|
| **Time**   | \(O(k)\), where \(k\) is the maximum iterations |
| **Space**  | \(O(1)\) — constant space usage                   |

---

## 📄 Code Structure

- `main()` — Reads inputs, calls hill climbing, and prints solution.
- `hill_climbing()` — Performs iterative improvement on the function.
- `objective_function()` — Defines the function to optimize.

---

## ✅ Dependencies

- Standard C++ headers: `iostream`, `vector`, `cmath`, `algorithm`

---

## 🧪 Compile & Run

```bash
# Compile
g++ hill_climbing.cpp -o hill_climbing

# Run
./hill_climbing
```

Enter your graph, start & goal nodes, and chosen depth limit when prompted.

---

## 🙌 Contributions & Feedback

Feel free to open issues or submit pull requests for improvements, bug fixes, or feature additions.