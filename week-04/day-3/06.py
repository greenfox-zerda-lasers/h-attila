# create a 300x300 canvas.
# draw a green 10x10 square to its center.

from tkinter import *

width = 300
height = 300
side = 100

my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=width, height=height)
my_canvas.pack()

my_canvas.create_rectangle((width-side)/2, (height-side)/2, (width+side)/2, (height+side)/2, fill='green')

my_canvas.mainloop()
