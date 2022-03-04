from turtle import Screen, Turtle

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.backward(10)

def anticlock():
    turtle.left(10)

def clock():
    turtle.right(10)

def clear():
    turtle.reset()

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=anticlock)
screen.onkey(key="d",fun=clock)
screen.onkey(key="c",fun=clear)
screen.exitonclick()