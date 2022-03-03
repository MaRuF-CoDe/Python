from turtle import Turtle,Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("#285078")

# To Draw a Square 
# for _ in range(4):
#     turtle.forward(10)
#     # turtle.left(90)


# For Dashed Line

for _ in range (15):
    # pick the pen up to leave white space between dashes
    turtle.forward(10)
    turtle.penup()
    # put the pen down and draw the second dash
    turtle.forward(10)
    turtle.pendown()
    

screen = Screen()
screen.exitonclick()