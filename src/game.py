from board import ROWS, COLS, PLAYER, AI, EMPTY, get_valid_locations


# بتشوف الفوز افقي وا رائسي ولا قطري
def winning_move(board, piece):
    # Horizontal
    #   وعشان اعمل اربه متصله لازم ابدا من صفر لتلاته  عشان عدد الاعمده 7 COLS - 3 ليه
    for c in range(COLS - 3):
        for r in range(ROWS):
            if all(board[r][c + i] == piece for i in range(4)):
                return True

    # Vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r + i][c] == piece for i in range(4)):
                return True

    # Positive diagonal
    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True

    # Negative diagonal
    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True

    return False


def is_terminal_node(board):
    return (
        winning_move(board, PLAYER)
        or winning_move(board, AI)
        or len(get_valid_locations(board)) == 0
    )
