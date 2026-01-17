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





class Ball:
    def __init__(self):
        self.ball=Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0,0)
        self.ball.speed("fast")
        self.x_move=3
        self.y_move=3

    def move(self):
        new_x=self.ball.xcor() + self.x_move
        new_y=self.ball.ycor() + self.y_move
        self.ball.goto(new_x,new_y)




