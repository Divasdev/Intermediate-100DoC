from turtle import Turtle,Screen
from paddle import Paddle,Ball

r_paddle=Paddle((350,0),5)
l_paddle=Paddle((-350,0),5)




screen=Screen()
screen.tracer(0)
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.setup(800,600)
screen.bgcolor("black")
screen.title("pong")


ball =Ball()
game_is_on=True
while game_is_on:
     screen.update()
     ball.move()








screen.exitonclick()

