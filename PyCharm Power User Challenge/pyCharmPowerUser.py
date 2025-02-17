def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    # Check rows and columns
    for index in range(3):
        if all(board[index][col] == player for col in range(3)) or all(board[row][index] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def get_player_move(board, current_player):
    """Get and validate the player's move."""
    while True:
        try:
            row, col = map(int, input(f"Player {current_player}, enter row and column (0-2): ").split())
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell is occupied. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers for row and column.")
        except IndexError:
            print("Out of range. Please enter numbers between 0 and 2.")


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Tic-Tac-Toe Game")
    print_board(board)

    for turn in range(9):
        current_player = players[turn % 2]

        # Get and place the player's move
        row, col = get_player_move(board, current_player)
        board[row][col] = current_player

        print_board(board)

        # Check for winner or draw
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            return

        if is_full(board):
            print("It's a draw!")
            return

    print("It's a draw!")





play_game()
