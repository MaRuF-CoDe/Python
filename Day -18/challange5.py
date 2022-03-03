import turtle as t
import random
turtle = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_ = (r, g, b)
    return random_

turtle.speed(0)


def size_of_gap(num):
    for _ in range(int(360/num)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading()+num)

size_of_gap(5)

screen = t.Screen()
screen.exitonclick()