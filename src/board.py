import numpy as np

# تمثيل محتوي الخانه
ROWS = 6
COLS = 7
PLAYER = 1
AI = 2
EMPTY = 0


# انشاء مصفوفه كلها اصفار في بدايه اللعبه
def create_board():
    return np.zeros((ROWS, COLS), dtype=int)


# بتحط قطعه الاعب او  AI في مكانها
def drop_piece(board, row, col, piece):
    board[row][col] = piece


# بتتأكد هل العمود ينفع تبعب فيه ولا لا
# لو اول صف من فوق فاضي > يبقي العمود لسه فيه مكان
def is_valid_location(board, col):
    return board[0][col] == EMPTY


# بتجيب اول صف فاضي من تحت لفوق
# عشان القطعه ديما تفع في اخر مكان فاضي
def get_next_open_row(board, col):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == EMPTY:
            return r


# بترجع لسته بكل الاعمده الي ممكن نلعب فيها
def get_valid_locations(board):
    return [c for c in range(COLS) if is_valid_location(board, c)]
