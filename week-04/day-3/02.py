# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.

from tkinter import *

my_graphics = Tk()

width = 600
height = 600
box_size = 300

my_canvas = Canvas(my_graphics, width = width, height = height, bg = "black")
my_canvas.pack()

my_canvas.create_line((width-box_size)/2, (height-box_size)/2, (width+box_size)/2, (height-box_size)/2, fill="red", width="3")
my_canvas.create_line((width+box_size)/2, (height-box_size)/2, (width+box_size)/2, (height+box_size)/2, fill="blue", width="3")
my_canvas.create_line((width-box_size)/2, (height+box_size)/2, (width+box_size)/2, (height+box_size)/2, fill="yellow", width="3")
my_canvas.create_line((width-box_size)/2, (height+box_size)/2, (width-box_size)/2, (height-box_size)/2, fill="green", width="3")

my_canvas.mainloop()
