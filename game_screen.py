import tkinter as tk
from game_logic import GameLogic
import random

# Screen dimensions
WIDTH = 600
HEIGHT = 600
ROWS = 3
COLS = 3
SQSIZE = WIDTH // COLS
LINE_WIDTH = 15
CIRC_WIDTH = 15
CROSS_WIDTH = 20
RADIUS = SQSIZE // 4
OFFSET = 50

class GameScreen:
    def __init__(self, mode, player_x=None, player_o=None, player=None, difficulty=None, symbol=None):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.mode = mode
        self.player_x = player_x
        self.player_o = player_o
        self.player = player
        self.difficulty = difficulty
        self.symbol = symbol
        self.game_logic = GameLogic()
        self.current_turn_label = None
        self.score_label = None
        self.scores = {"X": 0, "O": 0}
        self.game_active = True  # Flag to indicate if the game is active

    def run(self):
        self.create_widgets()
        self.update_turn_display()
        self.root.mainloop()

    def create_widgets(self):
        board_frame = tk.Frame(self.root)
        board_frame.pack()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(board_frame, text="", width=10, height=3, font=("Helvetica", 20),
                                                command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.current_turn_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.current_turn_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text="Scores - X: 0, O: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        tk.Button(self.root, text="End Game", command=self.end_game, font=("Helvetica", 14)).pack(pady=10)

    def make_move(self, row, col):
        if self.game_active and self.buttons[row][col]["text"] == "":
            self.buttons[row][col]["text"] = self.game_logic.current_player
            self.game_logic.board[row][col] = self.game_logic.current_player
            if self.game_logic.check_winner():
                self.display_winner()
            elif self.game_logic.is_tie():
                self.display_tie()
            else:
                self.game_logic.switch_player()
                self.update_turn_display()
                if self.mode == "computer" and self.game_logic.current_player != self.symbol:
                    self.root.after(500, self.computer_move)

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.game_logic.board[i][j] == ""]
        if self.difficulty == "Easy":
            move = random.choice(empty_cells)
        elif self.difficulty == "Medium":
            move = self.medium_move(empty_cells)
        else:
            move = self.hard_move(empty_cells)
        self.make_move(*move)

    def medium_move(self, empty_cells):
        # Implement medium difficulty logic
        return random.choice(empty_cells)

    def hard_move(self, empty_cells):
        # Implement hard difficulty logic (e.g., minimax algorithm)
        return random.choice(empty_cells)

    def update_turn_display(self):
        self.current_turn_label.config(text=f"{self.game_logic.current_player}'s Turn")

    def display_winner(self):
        self.game_active = False  # Deactivate the game
        winner = self.game_logic.current_player
        self.scores[winner] += 1
        self.score_label.config(text=f"Scores - X: {self.scores['X']}, O: {self.scores['O']}")
        winner_label = tk.Label(self.root, text=f"{winner} Wins!", font=("Helvetica", 16))
        winner_label.pack(pady=20)
        self.show_end_options()

    def display_tie(self):
        self.game_active = False  # Deactivate the game
        tie_label = tk.Label(self.root, text="It's a Tie!", font=("Helvetica", 16))
        tie_label.pack(pady=20)
        self.show_end_options()

    def show_end_options(self):
        tk.Button(self.root, text="Play Again", command=self.reset_game, font=("Helvetica", 14)).pack(pady=10)
        tk.Button(self.root, text="End Game", command=self.end_game, font=("Helvetica", 14)).pack(pady=10)

    def reset_game(self):
        self.game_active = True  # Reactivate the game
        for row in self.buttons:
            for button in row:
                button["text"] = ""
        self.game_logic.reset()
        self.update_turn_display()

    def end_game(self):
        self.root.destroy()
