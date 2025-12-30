from turtle import Turtle,Screen
import villains
import heroes
print(heroes.gen())
print(villains.gen())


square = Turtle()
triangle=Turtle()
penta=Turtle()
hexa=Turtle()
hepta=Turtle()
octa=Turtle()
nona=Turtle()
deca=Turtle()


square.shape("turtle")
square.color("forest green")

# Draw triangle
triangle.speed(1)
triangle.color("black")


triangle.forward(100)
triangle.rt(120)
triangle.forward(100)
triangle.rt(120)
triangle.forward(100)






# Draw square
square.speed(1)
for _ in range(4):
    square.forward(100)
    square.left(90)
    square.forward(100)


#Draw pentagon
penta.color("red")
penta.speed(1)
for _ in range(5):
    penta.forward(100)
    penta.rt(72)




# Draw heptagon



hepta.color("orange")
hepta.speed(1)

for _ in range(6):
    hepta.forward(100)
    hepta.rt(60)



#Draw heptagon

hepta.speed(1)
hepta.color("brown")
for _ in range(7):
    hepta.forward(100)
    hepta.rt(51.42)


# Draw octagon
octa.speed(1)
octa.color("blue")
for _ in range(8):
    octa.forward(100)
    octa.rt(45)



#Draw nonagon
nona.color("pink")
nona.speed(1)
for _ in range (9):
    nona.fd(100)
    nona.rt(40)

# Draw decagon

deca.color("dark slate blue")
deca.speed(1)

for _ in range(10):
    deca.fd(100)
    deca.rt(36)



screen=Screen()
screen.exitonclick()
