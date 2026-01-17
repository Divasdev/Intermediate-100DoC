from turtle import Screen
from paddle import Paddle,Ball

import time

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create paddles
r_paddle = Paddle((350, 0), 5)
l_paddle = Paddle((-350, 0), 5)

# Create ball
ball = Ball()

# Keyboard bindings

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Wall collision
    if ball.ball.ycor() > 280 or ball.ball.ycor() < -280:
        ball.bounce_y()

    # Paddle collision (right)
    if ball.ball.distance(r_paddle.paddle) < 50 and ball.ball.xcor() > 320:
        ball.bounce_x()

    # Paddle collision (left)
    if ball.ball.distance(l_paddle.paddle) < 50 and ball.ball.xcor() < -320:
        ball.bounce_x()

    # Ball out of bounds
    if ball.ball.xcor() > 380 or ball.ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()