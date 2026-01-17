from turtle import Turtle

class Paddle:
    def __init__(self,position,size):
        self.paddle=Turtle()
        self.paddle.penup()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.goto(position)
        self.paddle.shapesize(stretch_wid=size,stretch_len=1)



    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)






