import turtle
turtle.Screen().bgcolor("aqua")
turtle.Screen().title("Shapes")
pen = turtle.Turtle()

pen.forward(100)
pen.right(90)

pen.forward(50)
pen.right(90)

pen.forward(100)
pen.right(90)
pen.forward(50)

pen.penup()
pen.forward(200)
pen.pendown()

for i in range(4):
    pen.forward(100)
    pen.right(90)

turtle.done()
pen.hideturtle()

