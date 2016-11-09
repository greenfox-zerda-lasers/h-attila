# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.


from tkinter import *


def line_drawing(x, y):

    for line_x in range(x, width-x, int((width-x)/x)):
        for line_y in range(y, height-y, int((height-y)/y)):
            my_canvas.create_line(width/2, height/2, line_x, line_y, fill='black')


width = 600
height = 600


my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=width, height=height, bg='yellow')
my_canvas.pack()


line_drawing(20, 20)


my_canvas.mainloop()