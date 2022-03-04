from turtle import Turtle,Screen
import random

is_game_on = False

screen = Screen()
screen.setup (width=500, height=400)
bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win?")
color = ["red","blue","yellow","purple","orange","green"]
y_position = [-100,-60,-20,20,60,100]
all_turtle = []

for round in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[round])
    new_turtle.goto(x=-230,y=y_position[round])
    all_turtle.append(new_turtle)

if bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_game_on = False
            win_color = turtle.pencolor()
            if bet == win_color:
                print(f"You win . The {win_color} turtle wins.")
            else:
                print(f"You lost . The {win_color} turtle wins.")

        distance=random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()