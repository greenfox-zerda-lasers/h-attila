from tkinter import *
import random
import math
import time
import webcolors


size = 800

my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=size, height=size, bg='white')
my_canvas.pack()


def rgb():
    rgb = []
    for i in range(3):
        rgb.append(random.randint(0, 255))
    return webcolors.rgb_to_hex(rgb)


def magic_triangles(x, y, size):


    my_canvas.create_polygon(x, y, x + size / 2, y + size * math.sqrt(3) / 2, x + size, y, fill='white', outline=rgb(), width='1')
    my_canvas.update()

    if size > 8:

        magic_triangles(x, y, size/2)
        magic_triangles(x+size/2, y, size/2)
        magic_triangles(x+size/4, y + size*math.sqrt(3)/4, size / 2)



magic_triangles(0, 25, size)

my_canvas.mainloop()