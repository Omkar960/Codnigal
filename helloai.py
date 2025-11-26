import turtle
screen = turtle.Screen()
turtle.pencolor("blue")
polygon = turtle.Turtle()

colour = input("What's your favourite colour: ")
color = colour.lower()
print("Hello I am an AI bot what's your name")
name = input()
print(" Hello",name,"how are you feeling today good or bad: ")

mood = input().lower()

if mood == "good":
    print("it's good to hear that")
elif mood == "bad":
    print("That's not nice to hear")
else:
    print("It's difficult to put feelings in words")

print("It was good talking to you!")

sport = input("What sport do you like more, football, basketball or rugby: ")

fav = sport.lower()

if fav == "football":
    print("That's the most popular sport")
elif fav == "basketball":
    print("It originated form Canada")
elif fav == "rugby":
    print("It's a very aggresssive sport")
else:
    print("Couldn't understand your message")

choice = input("What shape do you want me to draw, square,hexagon,triangle or circle: ")

a = choice.lower()

if a == "square":
    polygon.pencolor(color)
    polygon.fillcolor(color)
    polygon.begin_fill()
    for i in range (4):
        polygon.forward(50)
        polygon.right(90)
    polygon.end_fill()
    polygon.hideturtle()
elif a == "hexagon":
    polygon.pencolor(color)
    polygon.fillcolor(color)
    polygon.begin_fill()
    for i in range(6):
        polygon.forward(50)
        polygon.right(60)
    polygon.end_fill()
    polygon.hideturtle()
elif a == "triangle":

    polygon.pencolor(color)
    polygon.fillcolor(color)
    polygon.begin_fill()
    for i in range(3):
        polygon.forward(50)
        polygon.right(120)
    polygon.end_fill()
    polygon.hideturtle()
elif a == "circle":
    polygon.pencolor(color)
    polygon.fillcolor(color)
    polygon.begin_fill()
    polygon.circle(100)
    polygon.end_fill()
    polygon.hideturtle()
else:
    print("Shape not recognized")

turtle.done()