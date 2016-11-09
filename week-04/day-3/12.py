# create a 300x300 canvas.
# fill it with a checkerboard pattern.

from tkinter import *


def square_drawing(x, y, col):
    my_canvas.create_rectangle(x*size/8, y*size/8, (x+1)*size/8, (y+1)*size/8, fill=col)


size = 300


my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=size, height=size, bg='yellow')
my_canvas.pack()

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            color='black'
        else:
            color='white'
        square_drawing(i, j, color)


my_canvas.mainloop()
