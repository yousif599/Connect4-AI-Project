import tkinter as tk
import numpy as np

from board import *
from game import *
from minimax import *
from gui import *


def main():
    mode = select_mode()
    if not mode:
        return

    board = create_board()
    current_player = PLAYER
    game_over = False

    root = tk.Tk()
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()

    draw_board(canvas, board)

    def click(col):
        nonlocal current_player, game_over
        if game_over or not is_valid_location(board, col):
            return

        row = get_next_open_row(board, col)
        drop_piece(board, row, col, current_player)
        draw_board(canvas, board)

        if winning_move(board, current_player):
            tk.messagebox.showinfo("Game Over", "Player wins!")
            game_over = True
            return

        if mode == "user_vs_ai":
            col_ai, _ = minimax(board, 5, -np.inf, np.inf, True, AI)
            row_ai = get_next_open_row(board, col_ai)
            drop_piece(board, row_ai, col_ai, AI)
            draw_board(canvas, board)

            if winning_move(board, AI):
                tk.messagebox.showinfo("Game Over", "AI wins!")
                game_over = True
            return

        current_player = AI if current_player == PLAYER else PLAYER

    frame = tk.Frame(root)
    frame.pack()

    for c in range(COLS):
        tk.Button(frame, text=str(c + 1), command=lambda x=c: click(x)).pack(
            side=tk.LEFT
        )

    root.mainloop()


if __name__ == "__main__":
    main()
