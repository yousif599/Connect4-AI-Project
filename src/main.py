import tkinter as tk
from tkinter import messagebox
import numpy as np

from board import *
from game import *
from minimax import *
from gui import *


def main():
    mode, depth = select_mode()
    if not mode:
        return

    board = create_board()
    current_player = PLAYER
    game_over = False
    last_move = None

    root = tk.Tk()
    root.configure(bg="#111827")
    root.title("Connect 4 AI")

    canvas = tk.Canvas(
        root, width=WIDTH, height=HEIGHT, bg="#111827", highlightthickness=0
    )
    canvas.pack()

    draw_board(canvas, board)

    # إعادة تشغيل اللعبة بدون إغلاق البرنامج.
    def restart():
        # بنقول لبايثون إننا هنعدّل متغيرات خارج الدالة
        nonlocal board, current_player, game_over, last_move
        board = create_board()
        current_player = PLAYER
        game_over = False
        last_move = None
        draw_board(canvas, board)

    def handle_click(event):
        nonlocal current_player, game_over, last_move

        if game_over or mode != "user_vs_ai" and mode != "user_vs_user":
            return

        col = event.x // SQUARE_SIZE
        if not is_valid_location(board, col):
            return

        row = get_next_open_row(board, col)
        drop_piece(board, row, col, current_player)
        last_move = (row, col)
        draw_board(canvas, board, last_move)

        if winning_move(board, current_player):
            winner = "Player 1" if current_player == PLAYER else "Player 2"
            messagebox.showinfo("Game Over", f"{winner} Wins!")
            game_over = True
            return

        if mode == "user_vs_ai":
            col_ai, _ = minimax(board, depth, -np.inf, np.inf, True, AI)
            row_ai = get_next_open_row(board, col_ai)
            drop_piece(board, row_ai, col_ai, AI)
            last_move = (row_ai, col_ai)
            draw_board(canvas, board, last_move)

            if winning_move(board, AI):
                messagebox.showinfo("Game Over", "AI Wins!")
                game_over = True

        else:  # mode == "user_vs_user":
            current_player = AI if current_player == PLAYER else PLAYER

    def ai_vs_ai():
        nonlocal current_player, game_over, last_move

        if game_over:
            return

        col, _ = minimax(board, 4, -np.inf, np.inf, True, current_player)
        row = get_next_open_row(board, col)
        drop_piece(board, row, col, current_player)
        last_move = (row, col)
        draw_board(canvas, board, last_move)

        if winning_move(board, current_player):
            winner = "AI 1" if current_player == PLAYER else "AI 2"
            messagebox.showinfo("Game Over", f"{winner} Wins!")
            game_over = True
            return

        current_player = AI if current_player == PLAYER else PLAYER
        root.after(600, ai_vs_ai)

    canvas.bind("<Button-1>", handle_click)

    tk.Button(root, text="Restart Game", command=restart, width=15).pack(pady=5)

    if mode == "ai_vs_ai":
        root.after(800, ai_vs_ai)

    root.mainloop()


if __name__ == "__main__":
    main()
