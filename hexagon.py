import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
sides = 6
sidelength = 70
angle = 360 / sides
polygon = turtle.Turtle()

for i in range(sides):
    polygon.forward(sidelength)
    polygon.right(angle)
polygon.hideturtle()
turtle.done()


    
