import tkinter as tk
from game_screen import GameScreen

class GameModeSelection:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Select Game Mode")
        self.root.geometry("600x600")

    def play_with_friend(self):
        self.root.destroy()
        self.get_player_names()

    def play_with_computer(self):
        self.root.destroy()
        self.get_computer_settings()

    def get_player_names(self):
        self.root = tk.Tk()
        self.root.title("Player Names")
        self.root.geometry("600x600")

        tk.Label(self.root, text="Player X Name:", font=("Helvetica", 14)).pack(pady=10)
        self.player_x_name = tk.Entry(self.root, font=("Helvetica", 14))
        self.player_x_name.pack(pady=10)

        tk.Label(self.root, text="Player O Name:", font=("Helvetica", 14)).pack(pady=10)
        self.player_o_name = tk.Entry(self.root, font=("Helvetica", 14))
        self.player_o_name.pack(pady=10)

        tk.Button(self.root, text="Start Game", command=self.start_friend_game, font=("Helvetica", 14), width=10, height=2).pack(pady=20)

        self.root.mainloop()

    def get_computer_settings(self):
        self.root = tk.Tk()
        self.root.title("Computer Settings")
        self.root.geometry("600x600")

        tk.Label(self.root, text="Player Name:", font=("Helvetica", 14)).pack(pady=10)
        self.player_name = tk.Entry(self.root, font=("Helvetica", 14))
        self.player_name.pack(pady=10)

        tk.Label(self.root, text="Difficulty Level:", font=("Helvetica", 14)).pack(pady=10)
        self.difficulty = tk.StringVar(value="Easy")
        tk.Radiobutton(self.root, text="Easy", variable=self.difficulty, value="Easy", font=("Helvetica", 14)).pack()
        tk.Radiobutton(self.root, text="Medium", variable=self.difficulty, value="Medium", font=("Helvetica", 14)).pack()
        tk.Radiobutton(self.root, text="Hard", variable=self.difficulty, value="Hard", font=("Helvetica", 14)).pack()

        tk.Label(self.root, text="Choose Symbol:", font=("Helvetica", 14)).pack(pady=10)
        self.symbol = tk.StringVar(value="X")
        tk.Radiobutton(self.root, text="X", variable=self.symbol, value="X", font=("Helvetica", 14)).pack()
        tk.Radiobutton(self.root, text="O", variable=self.symbol, value="O", font=("Helvetica", 14)).pack()

        tk.Button(self.root, text="Start Game", command=self.start_computer_game, font=("Helvetica", 14), width=10, height=2).pack(pady=20)

        self.root.mainloop()

    def start_friend_game(self):
        player_x = self.player_x_name.get()
        player_o = self.player_o_name.get()
        self.root.destroy()
        game_screen = GameScreen(mode="friend", player_x=player_x, player_o=player_o)
        game_screen.run()

    def start_computer_game(self):
        player = self.player_name.get()
        difficulty = self.difficulty.get()
        symbol = self.symbol.get()
        self.root.destroy()
        game_screen = GameScreen(mode="computer", player=player, difficulty=difficulty, symbol=symbol)
        game_screen.run()

    def run(self):
        mode_label = tk.Label(self.root, text="Select Game Mode", font=("Helvetica", 24, "bold"))
        mode_label.pack(pady=50)

        friend_button = tk.Button(self.root, text="Play with a Friend", command=self.play_with_friend, font=("Helvetica", 18), width=20, height=2)
        friend_button.pack(pady=20)

        computer_button = tk.Button(self.root, text="Play with the Computer", command=self.play_with_computer, font=("Helvetica", 18), width=20, height=2)
        computer_button.pack(pady=20)

        self.root.mainloop()
