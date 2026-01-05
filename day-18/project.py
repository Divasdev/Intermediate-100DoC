# import colorgram
#
# colors =colorgram.extract('image.jpeg',30)
# rgb_colors=[]
# for color in colors:
#
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)
import turtle as turtle_module
import random
from turtle import Screen

turtle_module.colormode(255)
tim= turtle_module.Turtle()
color_list=[(250, 248, 243), (251, 249, 250), (246, 250, 247), (243, 245, 248), (197, 164, 116), (130, 81, 51), (223, 211, 118), (80, 38, 29), (116, 41, 30), (169, 154, 28), (55, 85, 120), (71, 113, 79), (126, 157, 176), (186, 147, 150), (131, 148, 138), (123, 73, 77), (44, 50, 60), (45, 34, 38), (175, 105, 95), (48, 52, 50), (219, 179, 182), (218, 179, 174), (75, 72, 45), (102, 43, 46), (174, 102, 107), (116, 136, 123), (187, 205, 175), (44, 63, 92), (55, 72, 51), (98, 123, 162)]
tim.setheading(225)

for _ in range(10):

    tim.dot(20,random.choice(color_list))
    tim.forward(50)

screen=Screen()
screen.exitonclick()



