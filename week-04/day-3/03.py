# create a 300x300 canvas.
# draw its diagonals in green.

from tkinter import *

width = 500
height = 500

my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=width, height=height, bg="black")
my_canvas.pack()

my_canvas.create_line(0, 0, width, height, fill="blue", width="3")
my_canvas.create_line(width, 0, 0, height, fill="green", width="3")

my_canvas.mainloop()

