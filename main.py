from tkinter import Tk, Label, Button, Frame
from cell import Cell
import settings
import utils
import sys
import os

root = Tk()
# override the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.resizable(False, False)
root.title("MINESWEEPER")


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, *sys.argv)


top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)

game_title.place(
    x=utils.width_prct(25), y=0
)

creator_title = Label(
    top_frame,
    bg='black',
    fg='blue',
    text='By Eli Meyer',
    font=('', 32)
)

creator_title.place(
    x=utils.width_prct(25), y=65
)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

restart_btn = Button(
    top_frame,
    command=restart_program,
    bg='black',
    fg='red',
    activeforeground='black',
    text='RESTART',
    font=('', 20)
)
restart_btn.place(
    x=utils.width_prct(0.5), y=utils.height_prct(1)
)

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)

center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)

Cell.randomize_mines()

# run the window
root.mainloop()
