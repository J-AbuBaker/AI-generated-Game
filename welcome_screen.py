import tkinter as tk
from game_mode_selection import GameModeSelection

class WelcomeScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("600x600")

    def start_game(self):
        self.root.destroy()
        game_mode = GameModeSelection()
        game_mode.run()

    def run(self):
        welcome_label = tk.Label(self.root, text="Welcome to Tic-Tac-Toe", font=("Helvetica", 24, "bold"))
        welcome_label.pack(pady=50)

        play_button = tk.Button(self.root, text="Play", command=self.start_game, font=("Helvetica", 18), width=10, height=2)
        play_button.pack(pady=20)

        self.root.mainloop()
