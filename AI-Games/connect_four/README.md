# 🎯 Connect Four: User vs User (Terminal Edition)

A classic **Connect Four** game written in Python for two human players to enjoy right in the terminal.  
Drop discs into a 7‑column, 6‑row grid, and be the first to align four of your own discs horizontally, vertically, or diagonally!

---

## Table of Contents
1. [Gameplay Overview](#gameplay-overview)  
2. [Features](#features)  
3. [Requirements](#requirements)  
4. [Installation](#installation)  
5. [Running the Game](#running-the-game)  
6. [How to Play](#how-to-play)  
7. [Project Structure](#project-structure)  
8. [Screenshots](#screenshots)  
9. [Future Improvements](#future-improvements)  
10. [License](#license)  
11. [Credits](#credits)  

---

## Gameplay Overview
- **Board:** 2‑D list representing a 6 × 7 grid.  
- **Turns:** Players alternate selecting a column (0 – 6).  
- **Checks performed after each move:**  
  1. Four‑in‑a‑row, in any direction.  
  2. Full board (declares a draw).  
- **Feedback:** The board re‑renders in the terminal after every move and announces wins or draws.

---

## Features
- Interactive terminal interface with clear prompts.  
- Real‑time board rendering using ASCII characters.  
- Robust win & draw detection.  
- Clean, well‑commented source code—great for learning 2‑D array manipulation and basic game logic.

---

## Requirements
| Software | Version |
|----------|---------|
| Python   | 3.7 or newer |

No external libraries needed—everything is standard Python.

---

## Installation
Clone the repository (or download the ZIP):

```bash
git clone https://github.com/your‑username/connect_four.git
cd connect_four

Running the Game
,,,
python A_connect_four.py
,,,

You’ll see the empty board and a prompt for Player 1’s first move

How to Play

1.Select a column (0 – 6) when prompted.

2.The disc drops into the lowest empty row in that column.

3.Players alternate turns until someone gets four in a row or the board is full.

4.The game prints a victory message (or draw) and exits
---
Project Structure

connect_four/
├── A_connect_four.py       # Game source code
├── README.md               # This file
└── screenshots/            # Images for the README
    ├── starting.png
    ├── winning.png
    └── after_game_over.png

---

Screenshots

| Start of Game                        | Winning State                         | After Game Over                                 |
| ------------------------------------ | ------------------------------------- | ----------------------------------------------- |
| ![Start](./screenshots/starting.png) | ![Winning](./screenshots/wining.png) | ![Game Over](./screenshots/after%20game%20over.png) |

---

Future Improvements
Single‑player mode with a simple AI opponent.

GUI version (e.g., tkinter or pygame).

Highlight winning sequence on the board.

Enhanced input validation and error messages.

License
This project is licensed under the MIT License—see LICENSE for details.

Credits
Built with Python 3.

Game concept inspired by the original Connect Four (Howard Wexler & Ned Strongin).

---