import turtle as t
import random
turtle = t.Turtle()
t.colormode(255)

list = [0,90,180,270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_ = (r, g, b)
    return random_
turtle.pensize(10)
turtle.speed(9)

for _ in range(100):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(list))

screen = t.Screen()
screen.exitonclick()