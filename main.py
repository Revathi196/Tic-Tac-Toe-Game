# main.py

def print_board(board):
    """Print the Tic-Tac-Toe board."""
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")

def check_win(board, player):
    """Check if the player has won the game."""
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    if all([board[i][i] == player for i in range(3)]):  # Check diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Check reverse diagonal
        return True
    return False

def is_full(board):
    """Check if the board is full."""
    return all(cell != " " for row in board for cell in row)

def player_turn(board, player):
    """Handle the turn of a player."""
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter the column (1-3): ")) - 1
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter valid numbers between 1 and 3.")

def main():
    """Run the Tic-Tac-Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        player_turn(board, current_player)
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
