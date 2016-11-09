from tkinter import *
import math
import time

my_graphics = Tk()


def nice_rectangle(size, m, n, offset):
    my_canvas.create_polygon(x - n*size + offset, y + m*size*math.sqrt(3)/2, x - size/2 - n*size + offset, y + size*math.sqrt(3)/2 + m*size*math.sqrt(3)/2, x + size/2 -n*size + offset, y + size * math.sqrt(3)/2 + m*size*math.sqrt(3)/2, fill='white')


width = 1000
height = 1000

x = width / 2
y = 50
size = 30

my_canvas = Canvas(my_graphics, width=width, height=height, bg='green')
my_canvas.pack()

for i in range(20):
    for j in range((i+1)):
        time.sleep(0.01)
        offset_x = i * size/2
        nice_rectangle(size, i, j, offset_x)
        my_canvas.update()

my_canvas.mainloop()
