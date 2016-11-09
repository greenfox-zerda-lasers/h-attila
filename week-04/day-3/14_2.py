# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.


from tkinter import *

width = 600
height = 600
step = 30

my_graphics = Tk()
my_canvas = Canvas(my_graphics, width=width, height=height, bg='white')
my_canvas.pack()

for i in range(0, int(width/2)+1, step):
    my_canvas.create_line(i, height/2, width/2, (height/2)-i, fill='green', width='1')
    my_canvas.create_line(width/2, i, width/2+i, height/2, fill='green', width='1')
    my_canvas.create_line(i, height/2, width/2, (height/2)+i, fill='green', width='1')
    my_canvas.create_line(width/2, height/2+i, width-i, height/2, fill='green', width='1')





my_canvas.mainloop()