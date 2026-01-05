from turtle import Turtle,Screen,colormode
import random
tim =Turtle()

colormode(255)

tim.speed("fast")
tim.pensize(10)


def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color



direction = [0, 90, 180, 270]


def randomwalk():
    for _ in range(200):
        tim.setheading(random.choice(direction))
        tim.forward(random.randint(5,50))
        tim.color(random_color())
        tim.pencolor(random_color())

randomwalk()

screen=Screen()
screen.colormode(255)
screen.exitonclick()
