# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

from tkinter import *
import random
import webcolors


def square_drawing(size):
    my_canvas.create_rectangle((width-size)/2, (height-size)/2, (width+size)/2, (height+size)/2, fill=rgb())

def rgb():
    rgb = []
    for i in range(3):
        rgb.append(random.randint(0, 255))
    return (webcolors.rgb_to_hex(rgb))


width = 300
height = 300

my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=width, height=height, bg='black')
my_canvas.pack()

for i in range(20):
    square_drawing(300 - i*15)


my_canvas.mainloop()