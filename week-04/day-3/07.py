# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *
import random
import webcolors


def rgb():
    rgb = []
    for i in range(3):
        rgb.append(random.randint(0, 255))
    return (webcolors.rgb_to_hex(rgb))


width = 600
height = 600

my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=width, height=height, bg='black')
my_canvas.pack()

for i in range(10):
    my_canvas.create_rectangle(random.randint(0,width), random.randint(0,width), random.randint(0,height), random.randint(0,height), fill=rgb())

my_canvas.mainloop()

