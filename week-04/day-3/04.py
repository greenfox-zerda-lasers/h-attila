# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *

coordinates = [10, 50, 'red', 15, 100, 'blue', 200, 20, 'green']

def my_drawing(data_of_lines):

    width = 300
    height = 300

    my_graphics = Tk()
    my_canvas = Canvas(my_graphics, width=width, height=height, bg='black')
    my_canvas.pack()

    for i in range(3):
        my_canvas.create_line(data_of_lines[i*3], data_of_lines[i*3+1], width/2, height/2, fill=data_of_lines[i*3+2], width='3')
    my_canvas.mainloop()

my_drawing(coordinates)