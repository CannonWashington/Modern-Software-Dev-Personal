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


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Tic-Tac-Toe Game")
    print_board(board)

    for turn in range(9):
        current_player = players[turn % 2]

        player_move(board, current_player)

        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            return

        if is_full(board):
            print("It's a draw!")
            return

    print("It's a draw!")


def player_move(board, current_player):
    while True:
        try:
            row, col = map(int, input(f"Player {current_player}, enter row and column (0-2): ").split())
            if board[row][col] == " ":
                board[row][col] = current_player
                break
            else:
                print("Cell is occupied. Try again.")
        except ValueError or IndexError:
            print("Invalid input. Enter row and column as numbers between 0 and 2.")


play_game()
