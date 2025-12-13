import numpy as np

ROWS = 6
COLS = 7
PLAYER = 1
AI = 2
EMPTY = 0

def create_board():
    return np.zeros((ROWS, COLS), dtype=int)

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[0][col] == EMPTY

def get_next_open_row(board, col):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == EMPTY:
            return r

def get_valid_locations(board):
    return [c for c in range(COLS) if is_valid_location(board, c)]