"""
CodeOrbit Tech - AI Internship
Task 2: Tic-Tac-Toe with Simple AI

AI Module

This file contains the computer's decision-making logic.
The computer uses the Minimax algorithm to choose its move.
"""

from game import (
    COMPUTER,
    PLAYER,
    EMPTY,
    check_winner,
    is_draw,
    get_available_moves,
)


# ============================================================
# MINIMAX ALGORITHM
# ============================================================

def minimax(board, depth, is_maximizing):
    """
    Minimax algorithm for Tic-Tac-Toe.

    The computer tries to maximize its score.
    The player tries to minimize the computer's score.

    Returns:
        A numerical score representing the board position.
    """

    winner = check_winner(board)

    # Computer wins
    if winner == COMPUTER:
        return 10 - depth

    # Player wins
    if winner == PLAYER:
        return depth - 10

    # Draw
    if is_draw(board):
        return 0

    # --------------------------------------------------------
    # COMPUTER TURN - MAXIMIZE SCORE
    # --------------------------------------------------------

    if is_maximizing:

        best_score = -1000

        for move in get_available_moves(board):

            board[move] = COMPUTER

            score = minimax(
                board,
                depth + 1,
                False
            )

            board[move] = EMPTY

            best_score = max(
                best_score,
                score
            )

        return best_score

    # --------------------------------------------------------
    # PLAYER TURN - MINIMIZE SCORE
    # --------------------------------------------------------

    else:

        best_score = 1000

        for move in get_available_moves(board):

            board[move] = PLAYER

            score = minimax(
                board,
                depth + 1,
                True
            )

            board[move] = EMPTY

            best_score = min(
                best_score,
                score
            )

        return best_score


# ============================================================
# FIND BEST COMPUTER MOVE
# ============================================================

def get_best_move(board):
    """
    Find the best possible move for the computer.

    Returns:
        Board position from 0 to 8.
        Returns None if no moves are available.
    """

    available_moves = get_available_moves(board)

    if not available_moves:
        return None

    best_score = -1000
    best_move = available_moves[0]

    for move in available_moves:

        board[move] = COMPUTER

        score = minimax(
            board,
            0,
            False
        )

        board[move] = EMPTY

        if score > best_score:
            best_score = score
            best_move = move

    return best_move