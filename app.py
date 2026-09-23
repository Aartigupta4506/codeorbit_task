"""
CodeOrbit Tech - AI Internship
Task 2: AI Tic-Tac-Toe Game

Features:
- User vs Computer
- Minimax AI
- Easy, Medium and Hard difficulty
- Scoreboard
- Win, Loss and Draw detection
- New Game and Reset Score
"""

import random
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CodeOrbit AI Tic-Tac-Toe",
    page_icon="🎮",
    layout="centered"
)


# ============================================================
# GAME CONSTANTS
# ============================================================

EMPTY = ""
PLAYER = "X"
COMPUTER = "O"

WINNING_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


# ============================================================
# INITIALIZE GAME
# ============================================================

def initialize_game():
    """Start a new game."""

    st.session_state.board = [EMPTY] * 9
    st.session_state.game_over = False
    st.session_state.result = ""
    st.session_state.player_turn = True


if "board" not in st.session_state:
    initialize_game()


# ============================================================
# INITIALIZE SCORE
# ============================================================

if "player_score" not in st.session_state:
    st.session_state.player_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "draw_score" not in st.session_state:
    st.session_state.draw_score = 0


# ============================================================
# CHECK WINNER
# ============================================================

def check_winner(board):
    """Check whether there is a winner or draw."""

    for a, b, c in WINNING_COMBINATIONS:

        if (
            board[a] != EMPTY
            and board[a] == board[b]
            and board[b] == board[c]
        ):
            return board[a]

    if EMPTY not in board:
        return "Draw"

    return None


# ============================================================
# MINIMAX
# ============================================================

def minimax(board, maximizing):
    """Calculate the best possible move using Minimax."""

    result = check_winner(board)

    if result == COMPUTER:
        return 1

    if result == PLAYER:
        return -1

    if result == "Draw":
        return 0

    if maximizing:

        best_score = -float("inf")

        for i in range(9):

            if board[i] == EMPTY:

                board[i] = COMPUTER

                score = minimax(board, False)

                board[i] = EMPTY

                best_score = max(best_score, score)

        return best_score

    best_score = float("inf")

    for i in range(9):

        if board[i] == EMPTY:

            board[i] = PLAYER

            score = minimax(board, True)

            board[i] = EMPTY

            best_score = min(best_score, score)

    return best_score


# ============================================================
# BEST MOVE
# ============================================================

def get_best_move(board):
    """Find the best move for the computer."""

    best_score = -float("inf")
    best_move = None

    for i in range(9):

        if board[i] == EMPTY:

            board[i] = COMPUTER

            score = minimax(board, False)

            board[i] = EMPTY

            if score > best_score:

                best_score = score
                best_move = i

    return best_move


# ============================================================
# EASY AI
# ============================================================

def get_easy_move(board):
    """Select a random empty position."""

    available_moves = [
        i for i in range(9)
        if board[i] == EMPTY
    ]

    if available_moves:
        return random.choice(available_moves)

    return None


# ============================================================
# MEDIUM AI
# ============================================================

def get_medium_move(board):
    """
    Medium AI:
    Sometimes uses Minimax and sometimes random move.
    """

    if random.random() < 0.6:
        return get_best_move(board)

    return get_easy_move(board)


# ============================================================
# COMPUTER MOVE
# ============================================================

def computer_move():

    if st.session_state.game_over:
        return

    difficulty = st.session_state.difficulty

    if difficulty == "Easy":

        move = get_easy_move(
            st.session_state.board
        )

    elif difficulty == "Medium":

        move = get_medium_move(
            st.session_state.board
        )

    else:

        move = get_best_move(
            st.session_state.board
        )

    if move is not None:

        st.session_state.board[move] = COMPUTER

    result = check_winner(
        st.session_state.board
    )

    if result is not None:

        end_game(result)

    else:

        st.session_state.player_turn = True


# ============================================================
# END GAME
# ============================================================

def end_game(result):

    st.session_state.game_over = True
    st.session_state.result = result
    st.session_state.player_turn = False

    if result == PLAYER:

        st.session_state.player_score += 1

    elif result == COMPUTER:

        st.session_state.computer_score += 1

    elif result == "Draw":

        st.session_state.draw_score += 1


# ============================================================
# PLAYER MOVE
# ============================================================

def player_move(position):

    if st.session_state.game_over:
        return

    if not st.session_state.player_turn:
        return

    if st.session_state.board[position] != EMPTY:
        return

    # Player places X
    st.session_state.board[position] = PLAYER

    result = check_winner(
        st.session_state.board
    )

    if result is not None:

        end_game(result)
        return

    # Computer's turn
    st.session_state.player_turn = False

    computer_move()


# ============================================================
# HEADER
# ============================================================

st.title("🎮 AI Tic-Tac-Toe")

st.write(
    "Challenge the computer in Tic-Tac-Toe "
    "using an AI opponent."
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ Game Settings")

    difficulty = st.selectbox(
        "Select Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    st.session_state.difficulty = difficulty

    st.write("")

    st.info(
        "Hard mode uses the Minimax algorithm "
        "to choose the best possible move."
    )


# ============================================================
# SCOREBOARD
# ============================================================

st.subheader("🏆 Scoreboard")

score1, score2, score3 = st.columns(3)

with score1:

    st.metric(
        "👤 You",
        st.session_state.player_score
    )

with score2:

    st.metric(
        "🤖 Computer",
        st.session_state.computer_score
    )

with score3:

    st.metric(
        "🤝 Draws",
        st.session_state.draw_score
    )


st.divider()


# ============================================================
# GAME STATUS
# ============================================================

if st.session_state.game_over:

    if st.session_state.result == PLAYER:

        st.success("🎉 Congratulations! You Win!")

    elif st.session_state.result == COMPUTER:

        st.error("🤖 Computer Wins! Try Again.")

    else:

        st.warning("🤝 It's a Draw!")


else:

    if st.session_state.player_turn:

        st.info(
            "👉 Your turn — choose an empty square."
        )

    else:

        st.info(
            "🤖 Computer is making its move..."
        )


# ============================================================
# GAME BOARD
# ============================================================

for row in range(3):

    columns = st.columns(3)

    for col in range(3):

        position = row * 3 + col

        value = st.session_state.board[position]

        if value == EMPTY:
            button_text = "⬜"
        elif value == PLAYER:
            button_text = "❌"
        else:
            button_text = "⭕"

        with columns[col]:

            if st.button(
                button_text,
                key=f"cell_{position}",
                use_container_width=True,
                disabled=(
                    value != EMPTY
                    or st.session_state.game_over
                    or not st.session_state.player_turn
                )
            ):

                player_move(position)

                st.rerun()


# ============================================================
# GAME INFORMATION
# ============================================================

st.divider()

st.subheader("📌 Game Information")

info1, info2 = st.columns(2)

with info1:

    st.write("❌ **You:** X")

    st.write(
        f"🎯 **Difficulty:** "
        f"{st.session_state.difficulty}"
    )

with info2:

    st.write("⭕ **Computer:** O")

    st.write(
        "🧠 **AI:** Minimax"
    )


# ============================================================
# CONTROL BUTTONS
# ============================================================

st.divider()

button1, button2 = st.columns(2)

with button1:

    if st.button(
        "🔄 New Game",
        use_container_width=True
    ):

        initialize_game()
        st.rerun()


with button2:

    if st.button(
        "🗑️ Reset Score",
        use_container_width=True
    ):

        st.session_state.player_score = 0
        st.session_state.computer_score = 0
        st.session_state.draw_score = 0

        initialize_game()

        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "CodeOrbit Tech AI Internship • Task 2 • "
    "Rule-Based / Minimax Tic-Tac-Toe"
)