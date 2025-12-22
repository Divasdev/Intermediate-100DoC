
#import another_module
#print(another_module.another_var)


# from turtle import Turtle, Screen
#
# timmy=Turtle()
# print(timmy)
# timmy.color("red","yellow")
# timmy.shape("turtle")
# timmy.forward(100)
# timmy.right(90)
#
#
#
#
# my_screen=Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from  prettytable import PrettyTable


table = PrettyTable()


table.add_column("Pokemon name",["Pikachu","charmander","Squirtle"])


table.add_column("Pokemon type",["Electric","water","Fire"])


table.align="c"

print(table)






