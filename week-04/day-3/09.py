# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

from tkinter import *


def square_drawing(size):
    my_canvas.create_rectangle((width-size)/2, (height-size)/2, (width+size)/2, (height+size)/2, fill='yellow')


width = 300
height = 300

my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=width, height=height, bg='black')
my_canvas.pack()

square_drawing(200)
square_drawing(150)
square_drawing(100)

my_canvas.mainloop()

