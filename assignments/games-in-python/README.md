
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a text-based Hangman game in Python. Practice string manipulation, loops, conditionals, user input, and random selection while creating a game that players can win or lose.

## 📝 Tasks

### 🛠️ Create the Game Setup

#### Description

Create the data and game setup needed to start a Hangman round. The program should randomly choose one word from a predefined list and prepare a hidden version of the word for the player.

#### Requirements

Completed program should:

- Store at least five possible words in a predefined list.
- Randomly select one word from the list for each game.
- Display the hidden word as underscores separated by spaces, such as `_ _ _ _ _`.
- Set a limit for the number of incorrect guesses.

### 🛠️ Implement the Guessing Loop

#### Description

Add the game loop that accepts letter guesses, updates the player’s progress, and ends when the player guesses the word or runs out of attempts.

#### Requirements

Completed program should:

- Ask the player to enter one letter at a time.
- Reveal every position containing a correctly guessed letter.
- Decrease the remaining attempts after an incorrect guess.
- Continue until the word is completely guessed or no attempts remain.
- Display a clear win message when the player guesses the word.
- Display a clear lose message and reveal the word when the player runs out of attempts.
