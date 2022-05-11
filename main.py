from tkinter import Tk, Label, Button, Frame
from tkinter.simpledialog import askstring

from cell import Cell
import settings
import utils
import sys
import os

name = askstring('Name', 'Welcome to minesweeper game, pleas enter your name')

root = Tk()
# override the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.resizable(False, False)
root.title("MINESWEEPER")

game_version = 'V2'


def restart_program():
    # Any unsaved data will be lost after using this function.
    python = sys.executable
    os.execl(python, python, *sys.argv)


def exit_to_desktop():
    sys.exit()


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

exit_btn = Button(
    top_frame,
    command=exit_to_desktop,
    bg='black',
    fg='red',
    activeforeground='black',
    text='EXIT',
    font=('', 20)
)
exit_btn.place(
    x=utils.width_prct(0.5), y=utils.height_prct(10)
)

Version = Label(
    top_frame,
    bg='black',
    fg='white',
    text=f"Game version: {game_version}",
    font=('', 25)
)

Version.place(
    x=utils.width_prct(81.5), y=0
)

username_display = Label(
    left_frame,
    bg='black',
    fg='white',
    text=f"Welcome {format(name)}",
    font=('', 25)
)

username_display.place(
    x=0, y=utils.height_prct(10)
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

