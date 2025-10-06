"""This is a 2 players local top-down game example.
Player 1 is 'X' and Player 2 is 'O'.
First player to align 3 characters horizontally, vertically, or diagonally wins.
"""

class TicTacToe:
    """ Class representing the Tic Tac Toe game """

    def __init__(self):
        """Initialize the game board and current player."""
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def display_board(self):
        """Display the game board."""
        for i in range(3):
            print("|".join(self.board[i*3:(i+1)*3]))
            if i < 2:
                print("-" * 6)
    
    def switch_player(self):
        """Switch the current player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def mark_move(self, position):
        """
        Mark the move on the board.

        Args:
            position (int): Index (0-8) where the player wants to move.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

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

        while True:
            try:
                move = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1
                if move < 0 or move >= 9 or not self.mark_move(move):
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            self.display_board()
            winner = self.check_winner()
            if winner:
                self.display_board()
                print(f"Player {winner} wins!")
                break
            if self.is_draw():
                self.display_board()
                print("It's a draw!")
                break
            self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()