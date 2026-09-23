"""
CodeOrbit Tech - AI Internship
Task 2: Tic-Tac-Toe with Simple AI

Game Logic Module

This file contains:
- Board checking
- Win detection
- Draw detection
- Available moves
- Making moves
"""


# ============================================================
# CONSTANTS
# ============================================================

PLAYER = "X"
COMPUTER = "O"
EMPTY = ""


# ============================================================
# CREATE NEW BOARD
# ============================================================

def create_board():
    """
    Create and return an empty Tic-Tac-Toe board.
    """

    return [EMPTY] * 9


# ============================================================
# WINNING COMBINATIONS
# ============================================================

WINNING_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),

    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),

    (0, 4, 8),
    (2, 4, 6)
]


# ============================================================
# CHECK WINNER
# ============================================================

def check_winner(board):
    """
    Check whether X or O has won.

    Returns:
        "X" if player wins
        "O" if computer wins
        None if there is no winner
    """

    for a, b, c in WINNING_COMBINATIONS:

        if (
            board[a] != EMPTY
            and board[a] == board[b]
            and board[b] == board[c]
        ):
            return board[a]

    return None


# ============================================================
# CHECK DRAW
# ============================================================

def is_draw(board):
    """
    Check whether the game is a draw.

    A draw occurs when:
    - The board is completely filled
    - There is no winner
    """

    return (
        EMPTY not in board
        and check_winner(board) is None
    )


# ============================================================
# CHECK GAME OVER
# ============================================================

def is_game_over(board):
    """
    Check whether the game has finished.

    Returns:
        True if there is a winner or draw.
        False otherwise.
    """

    return (
        check_winner(board) is not None
        or is_draw(board)
    )


# ============================================================
# GET AVAILABLE MOVES
# ============================================================

def get_available_moves(board):
    """
    Return a list of empty cell indexes.
    """

    return [
        index
        for index, cell in enumerate(board)
        if cell == EMPTY
    ]


# ============================================================
# MAKE MOVE
# ============================================================

def make_move(board, position, player):
    """
    Place a player's symbol on the board.

    Parameters:
        board    : Current game board
        position : Cell index from 0 to 8
        player   : "X" or "O"

    Returns:
        True if the move was successful.
        False if the cell is already occupied
        or the position is invalid.
    """

    if position < 0 or position >= 9:
        return False

    if board[position] != EMPTY:
        return False

    if player not in [PLAYER, COMPUTER]:
        return False

    board[position] = player

    return True