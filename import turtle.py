import turtle
import random

screen = turtle.Screen()
screen.bgcolor("#10152f")
screen.title("Beautiful Flower Garden")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Draw a flower
def flower(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

    for i in range(12):
        t.color(color)
        t.begin_fill()
        t.circle(size, 60)
        t.left(120)
        t.circle(size, 60)
        t.left(150)
        t.end_fill()

    # Flower center
    t.penup()
    t.goto(x, y - 5)
    t.pendown()
    t.color("#FFD700")
    t.begin_fill()
    t.circle(size / 4)
    t.end_fill()

# Draw stem
def stem(x, y, height):
    t.penup()
    t.goto(x, y)
    t.setheading(-90)
    t.pendown()
    t.color("#32CD70")
    t.pensize(5)
    t.forward(height)

    # Leaves
    t.color("#228B22")
    t.begin_fill()
    t.circle(25, 90)
    t.left(90)
    t.circle(25, 90)
    t.end_fill()

# Flowers
flowers = [
    (-180, 100, 35, "#FF69B4"),
    (0, 180, 45, "#DA70D6"),
    (180, 100, 35, "#FF4500"),
    (-100, -30, 30, "#FFB6C1"),
    (100, -30, 30, "#9370DB")
]

for x, y, size, color in flowers:
    stem(x, y, 150)
    flower(x, y, size, color)

# Little stars
t.pensize(2)
for i in range(50):
    x = random.randint(-300, 300)
    y = random.randint(-250, 280)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#FFFACD")
    t.dot(random.randint(2, 5))

# Title
t.penup()
t.goto(0, 270)
t.color("#FFB6C1")
t.write("~ Magical Flower Garden ~",
        align="center",
        font=("Arial", 22, "bold"))

turtle.done()