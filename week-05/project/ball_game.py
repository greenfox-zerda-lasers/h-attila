from tkinter import *
import time

canvas_size = 400
ball_size = 20

my_animation = Tk()
my_canvas = Canvas(my_animation, width=canvas_size, height=canvas_size, bg='white')
my_canvas.pack()
ball_position = []


class ball():


    def __init__(self, start_x, start_y, size, step=10):
        self.step = step
        self.the_ball = my_canvas.create_oval(start_x, start_y, start_x+size, start_y+size, fill='yellow')

    def move(self, ball_move_x='0', ball_move_y='0'):
        my_canvas.move(1, self.step, 0)
        ball_position = my_canvas.coords(self.the_ball)
        if ball_position[0] >= canvas_size-ball_size:
            self.step = -10
        elif ball_position[0] <= ball_size:
            self.step = 10


    def wall_touch_detect(self):
        pass



my_ball = ball(100, 300, ball_size)

for i in range(1000):
    my_ball.move()
    time.sleep(0.1)
    my_animation.update()

my_canvas.mainloop()





