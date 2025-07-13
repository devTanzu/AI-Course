♟️ Simple Chess in Python (Pygame + python‑chess)
A lightweight, beginner‑friendly chess application where you control the White pieces against a modest AI (Black). Built purely with Python, Pygame, and python‑chess, it illustrates how GUI interaction and rule‑based logic can create an engaging board‑game experience.

🧠 How the AI Thinks
The computer follows a straightforward decision tree:

Safe captures first – it hunts for any capture that doesn’t immediately blunder material.

Checks second – if no capture is possible, it seeks moves that put your king in check.

Fallback: any legal move – when neither capture nor check is available, the AI selects the first legal move it finds.

This is intentionally simple—perfect for demonstrating turn logic without diving into heavyweight engines like Stockfish.

🛠️ What You’ll Need
bash
Copy
Edit
pip install pygame python-chess
Python 3.7 or newer

Pygame ( graphics and input )

python‑chess ( board representation & legality )

▶️ Getting Started
Clone or download this repository.

Make sure the directory includes the piece images, named exactly:

Copy
Edit
wp.png  bp.png
wr.png  br.png
wn.png  bn.png
wb.png  bb.png
wq.png  bq.png
wk.png  bk.png
Launch the game:

bash
Copy
Edit
python chess_game.py
🎮 Controls & Gameplay
Left‑click a White piece to select it.

Valid destinations glow green.

The chosen piece glows yellow.

Click a highlighted square to move.

The AI replies automatically after a brief pause.

Press R at any moment to restart.

The game finishes on checkmate, stalemate, draw by repetition/75‑move rule, or insufficient material.

📁 Recommended Folder Layout
markdown
Copy
Edit
simple_chess/
├── chess_game.py
├── assets/
│   ├── wp.png  …  bk.png
│   └── board_background.png
├── README.md
└── screenshots/
    ├── opening_screen.png
    ├── in_play.png
    └── checkmate_white.png
🚀 Current Feature Set
Click‑driven 8×8 board rendered with Pygame

Legal‑move highlights and move validation via python‑chess

Automatic pawn promotion to Queen

Text banner showing Check / Checkmate / Stalemate

Basic AI that plays “good enough” moves for casual practice

🔮 Ideas for Expansion
Side‑swap option (play as Black)

Move history panel with PGN export

Sound effects for moves and captures

Undo / Redo functionality

Stronger AI via Minimax or external UCI engine

Custom promotion dialog (choose Q/R/B/N)

📜 License
Released under the MIT License – experiment, change, or publish your modified versions freely.

