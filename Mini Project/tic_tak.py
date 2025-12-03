def create_board():
    """Initializes and returns an empty Tic-Tac-Toe board."""
    return [' ' for _ in range(9)] # Represents a 3x3 board as a 1D list

def display_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def player_move(board, player_char):
    """Prompts the current player for a move and updates the board."""
    while True:
        try:
            position = int(input(f"Player {player_char}, enter your move (1-9): ")) - 1
            if 0 <= position < 9 and board[position] == ' ':
                board[position] = player_char
                break
            else:
                print("Invalid move. Please choose an empty position between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_win(board, player_char):
    """Checks if the given player has won the game."""
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player_char for i in combo):
            return True
    return False

def check_tie(board):
    """Checks if the game is a tie (board is full and no winner)."""
    return ' ' not in board

def play_game():
    """Manages the main game loop for Tic-Tac-Toe."""
    board = create_board()
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board(board)
        player_move(board, current_player)

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_tie(board):
            display_board(board)
            print("It's a tie!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()