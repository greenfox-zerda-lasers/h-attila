from tkinter import *


my_graphics = Tk()


size = 600

my_canvas = Canvas(my_graphics, width=size, height=size, bg='yellow')
my_canvas.pack()


def nice_lines(x_pos, y_pos, size):
    if size > 10:
        my_canvas.create_rectangle(x_pos, y_pos, x_pos + size, y_pos+size)
        nice_lines(x_pos, y_pos + size/3, size/3)
        my_canvas.create_rectangle(x_pos, y_pos, x_pos + size, y_pos+size)
        nice_lines(x_pos + size*2/3, y_pos + size/3, size/3)
        my_canvas.create_rectangle(x_pos, y_pos, x_pos + size, y_pos+size)
        nice_lines(x_pos + size*1/3, y_pos, size/3)
        my_canvas.create_rectangle(x_pos, y_pos, x_pos + size, y_pos+size)
        nice_lines(x_pos + size*1/3, y_pos + size*2/3, size/3)


nice_lines(0, size/3, size/3)
nice_lines(size/3, 0, size/3)
nice_lines(size*2/3, size/3, size/3)
nice_lines(size/3, size*2/3, size/3)

my_canvas.mainloop()