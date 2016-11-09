# create a 300x300 black canvas.
# draw a red horizontal line to its middle.
# draw a green vertical line to its middle.

from tkinter import *

my_graphics = Tk()

width = 300
height = 300


my_canvas = Canvas(my_graphics, bg = 'black', width=width, height=height)

my_canvas.create_line(0, height/2, width, height/2, fill = 'red', width = '3')
my_canvas.create_line(width/2, 0, width/2, height, fill = 'green', width = '3')


my_canvas.pack()

my_canvas.mainloop()

