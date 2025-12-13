import numpy as np
from board import *
from game import *

def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER if piece == AI else AI

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 10
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 80

    return score

def score_position(board, piece):
    score = 0
    center_array = list(board[:, COLS // 2])
    score += center_array.count(piece) * 3

    for r in range(ROWS):
        row = list(board[r])
        for c in range(COLS - 3):
            score += evaluate_window(row[c:c+4], piece)

    for c in range(COLS):
        col = list(board[:, c])
        for r in range(ROWS - 3):
            score += evaluate_window(col[r:r+4], piece)

    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            score += evaluate_window([board[r+i][c+i] for i in range(4)], piece)
            score += evaluate_window([board[r+3-i][c+i] for i in range(4)], piece)

    return score

def minimax(board, depth, alpha, beta, maximizing, piece):
    valid_locations = get_valid_locations(board)

    if depth == 0 or is_terminal_node(board):
        if winning_move(board, piece):
            return None, 1e14
        elif winning_move(board, PLAYER if piece == AI else AI):
            return None, -1e14
        else:
            return None, score_position(board, piece)

    if maximizing:
        value = -np.inf
        best_col = np.random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp = board.copy()
            drop_piece(temp, row, col, piece)
            new_score = minimax(temp, depth-1, alpha, beta, False, piece)[1]
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value

    else:
        value = np.inf
        opp = PLAYER if piece == AI else AI
        best_col = np.random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp = board.copy()
            drop_piece(temp, row, col, opp)
            new_score = minimax(temp, depth-1, alpha, beta, True, piece)[1]
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value
