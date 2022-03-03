from turtle import Turtle,Screen
import random
turtle = Turtle()

list = [0,90,180,270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# def choose_dir():
#     for _ in range(50):
#         return random.choice(list)
turtle.pensize(10)
turtle.speed(9)

for _ in range(100):
    turtle.color(random.choice(colours))
    turtle.forward(30)
    turtle.setheading(random.choice(list))

screen = Screen()
screen.exitonclick()