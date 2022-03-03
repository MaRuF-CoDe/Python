from turtle import Turtle,Screen
import random
turtle = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num):
    angle = 360/num
    for _ in range(num):
        turtle.forward(100)
        turtle.right(angle)
for num in range(3,11):
    turtle.color(random.choice(colours))
    draw_shape(num)      
screen = Screen()
screen.exitonclick()
