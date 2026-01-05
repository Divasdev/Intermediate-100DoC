from turtle import Turtle,Screen,colormode
import random
tim =Turtle()

colormode(255)

tim.speed("fastest")
tim.pensize(1)

def random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(10)




screen=Screen()
screen.colormode(255)
screen.exitonclick()
