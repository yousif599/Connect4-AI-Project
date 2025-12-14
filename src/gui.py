import tkinter as tk
from board import ROWS, COLS, PLAYER, AI

SQUARE_SIZE = 80
WIDTH = COLS * SQUARE_SIZE
HEIGHT = (ROWS + 1) * SQUARE_SIZE

# Colors
BG_COLOR = "#111827"
BOARD_COLOR = "#1E3A8A"
EMPTY_COLOR = "#E5E7EB"
PLAYER_COLOR = "#DC2626"
AI_COLOR = "#FACC15"
HIGHLIGHT_COLOR = "#FFFFFF"


def draw_board(canvas, board, last_move=None):
    canvas.delete("all")

    for c in range(COLS):
        for r in range(ROWS):
            canvas.create_rectangle(
                c * SQUARE_SIZE,
                (r + 1) * SQUARE_SIZE,
                (c + 1) * SQUARE_SIZE,
                (r + 2) * SQUARE_SIZE,
                fill=BOARD_COLOR,
                outline=BOARD_COLOR,
            )

            color = EMPTY_COLOR
            if board[r][c] == PLAYER:
                color = PLAYER_COLOR
            elif board[r][c] == AI:
                color = AI_COLOR

            canvas.create_oval(
                c * SQUARE_SIZE + 5,
                (r + 1) * SQUARE_SIZE + 5,
                (c + 1) * SQUARE_SIZE - 5,
                (r + 2) * SQUARE_SIZE - 5,
                fill=color,
                outline=color,
            )

    if last_move:
        r, c = last_move
        canvas.create_oval(
            c * SQUARE_SIZE + 2,
            (r + 1) * SQUARE_SIZE + 2,
            (c + 1) * SQUARE_SIZE - 2,
            (r + 2) * SQUARE_SIZE - 2,
            outline=HIGHLIGHT_COLOR,
            width=3,
        )


def select_mode():
    mode = None
    difficulty = None

    def choose(m, d):
        nonlocal mode, difficulty
        mode = m
        difficulty = d
        root.quit()

    root = tk.Tk()
    root.configure(bg=BG_COLOR)
    root.title("Connect 4 - AI Project")

    tk.Label(
        root, text="Select Mode", bg=BG_COLOR, fg="white", font=("Arial", 16)
    ).pack(pady=10)

    for d in [("Easy", 2), ("Medium", 4), ("Hard", 6)]:
        tk.Button(
            root,
            text=f"User vs AI ({d[0]})",
            command=lambda dep=d[1]: choose("user_vs_ai", dep),
            width=25,
        ).pack(pady=3)

    tk.Button(
        root, text="AI vs AI", command=lambda: choose("ai_vs_ai", 4), width=25
    ).pack(pady=3)
    tk.Button(
        root,
        text="User vs User",
        command=lambda: choose("user_vs_user", None),
        width=25,
    ).pack(pady=3)

    root.mainloop()
    root.destroy()
    return mode, difficulty
