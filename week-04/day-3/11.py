# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *
import random
import webcolors


def square_drawing(size, color):
    my_canvas.create_rectangle((width-size)/2, (height-size)/2, (width+size)/2, (height+size)/2, fill=color)

def rgb():
    rgb = []
    for i in range(3):
        rgb.append(random.randint(0, 255))
    return (webcolors.rgb_to_hex(rgb))


width = 300
height = 300
rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', '#4B0082', '#8A2BE2']


my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=width, height=height, bg='black')
my_canvas.pack()

for i in range(7):
    square_drawing(300 - i*40, rainbow_colors[i])


my_canvas.mainloop()