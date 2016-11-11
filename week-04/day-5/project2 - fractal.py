from tkinter import *
import math
import time
import webcolors
import random

size = 800  # <------ Size of the canvas / polygon

my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=size, height=size, bg='white')
my_canvas.pack()



####    rgb() function creates the random color

def rgb():
    rgb = []
    for i in range(3):
        rgb.append(random.randint(0, 255))
    return webcolors.rgb_to_hex(rgb)



####    magic_fractal() creates the little strange things we draw to the canvas

def magic_fractal(x, y, size):
    time.sleep(0.001)


    ####    drawing the poligon's six points

    my_canvas.create_polygon(x, y,
                             x + size, y,
                             x + size * 3 / 2, y + size * math.sqrt(3) / 2,
                             x + size, y + size * math.sqrt(3),
                             x, y + size * math.sqrt(3),
                             x - size / 2, y + size * math.sqrt(3) / 2,
                             fill='white', outline=rgb(), width='1')

    my_canvas.update()


    ####    decision point: contiue drawing one level deepor or not

    if size > 5:
        magic_fractal(x, y, size / 3)
        magic_fractal(x + 2 / 3 * size, y, size / 3)
        magic_fractal(x + size, y + size * math.sqrt(3) / 3, size / 3)
        magic_fractal(x + 2 / 3 * size, y + size * math.sqrt(3) * 2 / 3, size / 3)
        magic_fractal(x, y + size * math.sqrt(3) * 2 / 3, size / 3)
        magic_fractal(x - size / 3, y + size * math.sqrt(3) / 3, size / 3)


magic_fractal(250, 100, size / 3)

my_canvas.mainloop()
