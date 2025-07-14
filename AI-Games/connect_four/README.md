🎯 Connect Four: User vs User (Terminal Edition)

This is a classic **Connect Four** game built with Python and designed to be played in the terminal. Two players take turns dropping discs into a vertical grid. The first to align four discs horizontally, vertically, or diagonally wins!

🧠 Game Logic Behind the Scenes

- The game board is a 2D list (6 rows × 7 columns).
- On each turn, the player selects a column to drop their disc.
- The program checks for:
  - Four in a row (in all directions)
  - Full board (for draw detection)
- The board is updated and printed after each move.



🛠️ Requirements

You only need:

Python 3.7+
No additional libraries or dependencies are required.

▶️ How to Run the Game

Clone or download this repository to your local machine.

Navigate to the game folder:

bash
Copy
Edit
cd connect_four
Run the game using:

bash
Copy
Edit
python A_connect_four.py
🎮 How to Play

Two players (Player 1 and Player 2) take alternate turns.

On your turn, input the column number (0–6) where you want to drop your disc.

The program will show the updated board after every move.

A message will display if a player wins or if the board is full (draw).



---

**Suggested file structure**

connect_four/
├── A_connect_four.py
├── README.md
└── screenshots/
├── starting.png
├── after_game_over.png
└── winini.png

---
> ## 🖼️ Screenshots


![screenshots](./screenshots/starting.png)

![screenshots](./screenshots/wining.png)

![screenshots](./screenshots/after%20game%20over.png)

---



🚀 Features

Interactive terminal-based interface

Real-time board rendering

Win and draw detection

Simple, clean code for learning logic and 2D arrays

❓ Future Improvements (Suggestions)

Add a single-player mode (with a basic AI)

GUI version using tkinter or pygame

Highlight winning sequence

Add input validation for better user experience

📜 License

This project is open-source and free to use under the MIT License.

💡 Credits

Built using Python

Game logic inspired by the original Connect Four game by Howard Wexler and Ned Strongin


---


