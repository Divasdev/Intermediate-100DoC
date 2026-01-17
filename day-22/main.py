from turtle import Turtle,Screen
from paddle import Paddle

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))



# tim =Turtle("square")
# tim.color("white")
# tim.penup()
# tim.goto(350,0)
#
# tim.shapesize(stretch_wid=5,stretch_len=1)
#
#
#
# def go_up():
#     new_y=tim.ycor()+20
#     tim.goto(tim.xcor(),new_y)
#
#
#
#
# def go_down():
#     new_y=tim.ycor()-20
#     tim.goto(tim.xcor(),new_y)
#
#
#



screen=Screen()
screen.tracer(0)
screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")
screen.setup(800,600)
screen.bgcolor("black")
screen.title("pong")
game_is_on=True
while game_is_on:
     screen.update()
screen.exitonclick()

