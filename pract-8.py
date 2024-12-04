import math

# Display the Tic-Tac-Toe board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check if there are moves left
def is_moves_left(board):
    for row in board:
        if "_" in row:
            return True
    return False

# Evaluate the board
def evaluate(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":
            return 10 if board[i][0] == "O" else -10
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_":
            return 10 if board[0][i] == "O" else -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        return 10 if board[0][0] == "O" else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        return 10 if board[0][2] == "O" else -10

    return 0

# Min-Max function
def minimax(board, depth, is_max):
    score = evaluate(board)

    # If maximizer or minimizer has won
    if score == 10 or score == -10:
        return score

    # If no moves left, it's a draw
    if not is_moves_left(board):
        return 0

    if is_max:  # Maximizer (Computer)
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = "_"
        return best
    else:  # Minimizer (Human)
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = "_"
        return best

# Find the best move for the computer
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = "_"

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Main function to play Tic-Tac-Toe
def play_game():
    board = [["_"] * 3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    display_board(board)

    while True:
        # Human's turn
        print("Your turn (X). Enter row and column (0-2):")
        row, col = map(int, input().split())
        if board[row][col] != "_":
            print("Invalid move. Try again.")
            continue
        board[row][col] = "X"
        display_board(board)

        if evaluate(board) == -10:
            print("Congratulations! You win!")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break

        # Computer's turn
        print("Computer's turn (O):")
        move = find_best_move(board)
        board[move[0]][move[1]] = "O"
        display_board(board)

        if evaluate(board) == 10:
            print("Computer wins!")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break

# Run the game
play_game()
