💣 Number Heist - Guess the Vault Code Game
Number Heist is an exciting, interactive command-line game written in Python where you play as a daring codebreaker trying to crack a secret vault code. Your mission: guess the correct number between 1 and 100 within 7 attempts to unlock the vault and win the heist!

🎯 Game Description
The program randomly selects a secret vault code between 1 and 100.

You have 7 attempts to guess the correct number.

After each guess, the game provides feedback:

If your guess is the correct number, you unlock the vault and win immediately.

If your guess is wrong, the game tells you if your guess was too high or too low initially.

For subsequent guesses, it gives you hints on whether you are getting warmer (closer) or colder (farther) compared to your previous guess.

If your guess is the same distance away as before, it lets you know you're at the same distance.

If you fail to guess the code within 7 attempts, the vault remains locked and the heist fails.

🚀 How to Play
Run the game script (number_heist.py) using Python 3.

Enter your guesses when prompted (only numbers between 1 and 100).

Use the hints to adjust your next guess.

Crack the code before your attempts run out!

🛠️ Features
Randomly generated vault code every game session

Input validation to ensure numbers are within the valid range

Friendly feedback on guess accuracy and relative closeness

Limited number of attempts for added challenge

Clear success and failure messages

📋 Code Overview
The game logic is implemented in a function called number_heist() that:

Prints a welcome message and instructions

Generates a secret number with random.randint(1, 100)

Uses a loop to allow up to 7 guess attempts

Compares each guess to the secret number and provides feedback

Tracks the difference between the guess and secret number to provide "warmer" or "colder" hints

Ends the game when the player guesses correctly or exhausts all attempts

🔧 Requirements
Python 3.x

Standard library only (uses built-in random module)

💡 How to Run
Clone the repository and run the script:

bash
Copy
Edit
python number_heist.py
