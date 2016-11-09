# create a 300x300 canvas.
# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]


from tkinter import *

width = 300
height = 300

my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=width, height=height, bg='white')
my_canvas.pack()


def magic_function(list_of_points):
    for i in range(len(list_of_points)):
        my_canvas.create_line(list_of_points[i-1][0], list_of_points[i-1][1], list_of_points[i][0], list_of_points[i][1], fill='green', width='2')


magic_box = [[10, 10], [290,  10], [290, 290], [10, 290]]
magic_function(magic_box)

magic_lines = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]
magic_function(magic_lines)

my_canvas.mainloop()
