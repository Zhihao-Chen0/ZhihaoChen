"""This is a 2 players local top-down game example.
Player 1 is 'X' and Player 2 is 'O'.
First player to align 3 characters horizontally, vertically, or diagonally wins.
More enhancements have been made to improve user experience and game flow.
1. Player can choose symbol at the start.
2. Added a timer for each move. Timer is set to 10 seconds. Real-time countdown is displayed.
"""

import time
import threading

class Player:
    """ Class representing a player in the game """
    def __init__(self, name, symbol=None):
        self.name = name
        self.symbol = symbol

class TicTacToe:
    """ Class representing the Tic Tac Toe game """

    def __init__(self):
        """Initialize the game board and current player."""
        self.board = [' ' for _ in range(9)]
        self.current_player = None
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")

    def display_board(self):
        """Display the game board."""
        for i in range(3):
            print("|".join(self.board[i*3:(i+1)*3]))
            if i < 2:
                print("-" * 6)

    def choose_symbol(self):
        """Allow player1 to choose a symbol. Player2 gets the other symbol."""
        while True:
            symbol = input("Player 1, choose your symbol (X/O): ").upper()
            if symbol in ['X', 'O']:
                self.player1.symbol = symbol
                self.player2.symbol = "O" if symbol == 'X' else "X"
                self.current_player = self.player1
                break
            print("Invalid choice. Please choose 'X' or 'O'.")

    def switch_player(self):
        """Switch the current player."""
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def mark_move(self, position):
        """
        Mark the move on the board.

        Args:
            position (int): Index (0-8) where the player wants to move.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if self.board[position] == ' ':
            self.board[position] = self.current_player.symbol
            return True
        return False

    def timed_input(self, prompt, timeout=10):
        """
        Prompt the user for input with a timeout.
        If the user does not respond within the timeout, return None.
        """
        user_input = [None]

        def ask():
            print(prompt, end='', flush=True)
            user_input[0] = input()

        thread = threading.Thread(target=ask)
        thread.daemon = True
        thread.start()

        for remaining in range(timeout, 0, -1):
            if user_input[0] is not None:
                break
            print(f"Time left: {remaining} seconds", end='\r')
            time.sleep(1)

        print(' ' * 30, end='\r')  # Clear the line
        thread.join(0.1)

        if user_input[0] is not None:
            return user_input[0]
        print("Time's up! You missed your turn.")
        return None
  
    def check_winner(self):
        """Check if there's a winner."""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        return None

    def is_draw(self):
        """Check if the game is a draw."""
        return ' ' not in self.board and self.check_winner() is None

    def play(self):
        """Main game loop."""
        print("Welcome to the 2 Player Top Down Game!")
        self.display_board()
        self.choose_symbol()
        print(f"{self.player1.name} is {self.player1.symbol} | "
              f"{self.player2.name} is {self.player2.symbol}")

        while True:
            try:
                print(f"{self.current_player.name}'s turn ({self.current_player.symbol})")
                move = self.timed_input(f"{self.current_player.name}, "
                                        f"enter your move (1-9): ", timeout=10)
                if move is None:
                    print(f"{self.current_player.name} missed the turn!")
                    self.switch_player()
                    continue

                try:
                    move = int(move) - 1
                    if move < 0 or move >= 9 or not self.mark_move(move):
                        print("Invalid move. You lose your turn.")
                        self.switch_player()
                        continue
                except ValueError:
                    print("Invalid input. You lose your turn.")
                    self.switch_player()
                    continue

                self.display_board()
                winner = self.check_winner()
                if winner:
                    print(f"{self.current_player.name} wins!")
                    break
                if self.is_draw():
                    print("It's a draw!")
                    break
                self.switch_player()

            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
