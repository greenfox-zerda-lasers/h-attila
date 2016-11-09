# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

from tkinter import *


def square_drawing(x, y):
    my_canvas.create_rectangle(x, y, x+50, y+50, fill='yellow')


width = 300
height = 300

my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=width, height=height, bg='black')
my_canvas.pack()

square_drawing(10, 10)
square_drawing(30, 30)
square_drawing(50, 50)

my_canvas.mainloop()

