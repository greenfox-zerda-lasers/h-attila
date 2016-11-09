# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.


from tkinter import *

width = 600
height = 600
step = 10

my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=width, height=height, bg='white')
my_canvas.pack()

for i in range(0, width, step):
    my_canvas.create_line(i, 0, width, i, fill='blue', width='2')
    my_canvas.create_line(0, i, i, height, fill='green', width='2')



my_canvas.mainloop()