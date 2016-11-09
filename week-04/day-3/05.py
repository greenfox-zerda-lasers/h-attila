# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

from tkinter import *

def line_drawing(x, y):
    my_canvas.create_line(x, y, x+50, y, width='3', fill='blue')


width = 300
height = 300

my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=width, height=height, bg='yellow')
my_canvas.pack()

line_drawing(20,50)
line_drawing(120,50)
line_drawing(80,140)

my_canvas.mainloop()



