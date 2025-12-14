import tkinter as tk
from tkinter import messagebox
from board import *

SQUARE_SIZE = 80
WIDTH = COLS * SQUARE_SIZE
HEIGHT = (ROWS + 1) * SQUARE_SIZE


def draw_board(canvas, board):
    canvas.delete("all")
    for c in range(COLS):
        for r in range(ROWS):
            canvas.create_rectangle(
                c * SQUARE_SIZE,
                r * SQUARE_SIZE,
                (c + 1) * SQUARE_SIZE,
                (r + 1) * SQUARE_SIZE,
                fill="blue",
            )
            color = "white"
            if board[r][c] == PLAYER:
                color = "red"
            elif board[r][c] == AI:
                color = "yellow"

            canvas.create_oval(
                c * SQUARE_SIZE + 5,
                r * SQUARE_SIZE + 5,
                (c + 1) * SQUARE_SIZE - 5,
                (r + 1) * SQUARE_SIZE - 5,
                fill=color,
            )


def select_mode():
    mode = None

    def choose(m):
        nonlocal mode
        mode = m
        root.quit()

    root = tk.Tk()
    tk.Button(root, text="User vs AI", command=lambda: choose("user_vs_ai")).pack()
    tk.Button(root, text="AI vs AI", command=lambda: choose("ai_vs_ai")).pack()
    tk.Button(root, text="User vs User", command=lambda: choose("user_vs_user")).pack()
    root.mainloop()
    root.destroy()
    return mode
