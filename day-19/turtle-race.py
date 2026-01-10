import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color:")
print(user_bet)
colors = ["violet","indigo","blue","green","yellow","orange","red"]
y_positions=[-90,-60,-30,0,30,60,90]
all_turtle=[]

is_race_on=False
for turtle_index in range(0,7):

    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtle.append(new_turtle)
if user_bet:
    is_race_on=True

while is_race_on:


    for turtle in all_turtle:
        dist= random.randint(0,10)
        turtle.forward(dist)
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color== user_bet:

                print(f"You've! won the {winning_color} turtle is the winner!")
            else:
                print(f"You've! lost the {winning_color} turtle is the winner!")






screen.exitonclick()
