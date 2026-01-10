from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def move_anticlockwise():
    tim.forward(20)
    tim.left(20)
def move_clockwise():
    tim.forward(20)
    tim.right(20)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="c", fun=clear)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a",fun=move_anticlockwise)
screen.onkey(key="d",fun=move_clockwise)




screen.exitonclick()

