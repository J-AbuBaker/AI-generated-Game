# Tic-Tac-Toe Game

## Overview
The **Tic-Tac-Toe Game** is an engaging, interactive implementation of the classic Tic-Tac-Toe game with a professional graphical interface. This project offers multiple modes, allowing users to play against each other or challenge an AI opponent with adjustable difficulty levels. The design ensures a seamless user experience with intuitive controls and visually appealing elements.

## Features
- **Interactive Welcome Screen**: A clean and inviting start screen with a play button to initiate the game.
- **Game Mode Selection**: Players can select from different game modes:
  - **Play with a Friend**: Users can enter names for Player X and Player O and engage in a two-player match.
  - **Play with the Computer**: Users can enter their name, choose a symbol (X or O), and select one of three difficulty levels (Easy, Medium, Hard) to play against an AI opponent.
- **Game Interface**:
  - A dynamic 3x3 grid with clickable cells for easy interaction.
  - A real-time display of the current player's turn.
  - Clear visual feedback indicating the winner, with a red line highlighting the winning combination (row, column, or diagonal).
  - Live score tracking for both players.
  - Options to either restart the game or quit.
- **AI Opponent**: Varying difficulty levels, offering increasing challenges for the computer opponent based on the chosen difficulty.

## Project Structure
```
tic_tac_toe/
│
├── main.py                # Entry point for starting the game
├── welcome_screen.py      # Code for the welcome screen
├── game_mode_selection.py # Code for selecting the game mode
├── game_screen.py         # Core game logic and user interface
├── game_logic.py          # Logic for determining the game state (win/loss/draw)
└── README.md              # Project documentation and instructions
```

## How to Play
1. **Launch the Game**: Open the terminal and run `main.py` to start the game.
2. **Choose the Game Mode**:
   - Select **Play with a Friend** to compete with another player.
   - Choose **Play with the Computer** to challenge an AI opponent.
3. **Enter Your Details**:
   - If playing with a friend, input Player X and Player O names.
   - If playing against the computer, enter your name, select your symbol (X or O), and pick a difficulty level (Easy, Medium, Hard).
4. **Gameplay**:
   - Click on any empty cell to make your move.
   - The game will automatically display the current player's turn and highlight the winning combination with a red line when applicable.
5. **Restart or Quit**: After the game ends, choose whether to play again or quit the game.

## Acknowledgements
This project was developed with the support of **Microsoft Copilot** and is part of the **AI-generated Game Project in Advancing AI for Sustainable Development (AISD) Promotion Program**.
