def print_board(board):
    """Displays the current state of the game board.

    Prints the Tic-Tac-Toe board in a grid format, separating cells with vertical bars
    and rows with horizontal lines. This provides a visual representation of the game
    state after each move.

    Args:
        board (list): The current state of the game board, represented as a 2D list.
                      Each cell contains 'X', 'O', or a space (' ') for empty cells.

    Returns:
        None"""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    """Checks if the given player has won the game.

    Evaluates the current state of the board to determine if the specified player
    has completed a winning combination. A player wins by filling an entire row,
    column, or diagonal with their symbol.

    Winning Conditions:
    - All cells in any row are occupied by the player.
    - All cells in any column are occupied by the player.
    - All cells in either diagonal are occupied by the player.

    Args:
        board (list): The current state of the game board as a 2D list.
        player (str): The symbol of the player to check ('X' or 'O').

    Returns:
        bool: True if the player has won, False otherwise"""
    # Check rows and columns
    for index in range(3):
        if all(board[index][col] == player for col in range(3)) or all(board[row][index] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    """Checks if the game board is full with no empty cells.

    Determines whether all cells on the board are occupied by either 'X' or 'O'.
    This is used to detect a draw when no player has won, but the board is full.

    Args:
        board (list): The current state of the game board as a 2D list.

    Returns:
        bool: True if all cells are filled, False otherwise."""
    return all(cell != " " for row in board for cell in row)


def get_player_move(board, current_player):
    """Prompts the current player to enter their move and validates the input.

    Continuously asks the player for row and column coordinates until a valid,
    unoccupied cell is selected on the board. Handles invalid inputs such as
    non-numeric values and out-of-range coordinates.

    Args:
        board (list): The current state of the game board, represented as a 2D list.
        current_player (str): The symbol of the current player ('X' or 'O').

    Returns:
        tuple: A tuple containing two integers, the row and column indices
               for the player's move (e.g., (0, 2))."""
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
    """Controls the main flow of the Tic-Tac-Toe game.

    Initializes the game board and alternates turns between two players ('X' and 'O').
    Continuously prompts players for moves, updates the board, and displays it
    after each turn. Checks for a winner or a draw after every move and ends the game
    accordingly.

    The game flow includes:
    - Setting up an empty 3x3 board.
    - Looping for up to 9 turns (max moves in Tic-Tac-Toe).
    - Getting and validating player moves using the get_player_move() function.
    - Displaying the updated board state.
    - Checking for a winner with check_winner() or a draw with is_full().
    - Declaring the result (win or draw) and ending the game.

    Returns:
        None"""
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
