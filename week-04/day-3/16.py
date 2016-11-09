# create a 300x300 canvas.
# make it look like a nigth sky:
# - The background should be black
# - The stars can be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

from tkinter import *
import random
import webcolors


def rgb():
    rgb = []
    for i in range(3):
        rgb.append(random.randint(0, 255))
    return (webcolors.rgb_to_hex(rgb))

size_of_canvas = 1000
size_of_box = 3
number_of_stars = 10000

my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=size_of_canvas, height=size_of_canvas, bg='black')
my_canvas.pack()

for i in range(number_of_stars):
    x = random.randint(0, size_of_canvas)
    y = random.randint(0, size_of_canvas)
    my_canvas.create_rectangle(x, y, x+size_of_box, y+size_of_box, fill=rgb())

my_canvas.mainloop()