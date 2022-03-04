from turtle import Turtle,Screen
screen = Screen()
screen.setup (width=500, height=400)
bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win?")
color = ["red","blue","yellow","purple","orange","green"]
y_position = [-100,-60,-20,20,60,100]

for round in range(0,6):
    turtle1 = Turtle(shape="turtle")
    turtle1.penup()
    turtle1.color(color[round])
    turtle1.goto(x=-230,y=y_position[round])

# turtle2 = Turtle(shape="turtle")
# turtle2.penup()
# turtle2.color(color[1])
# turtle2.goto(x=-230,y=-60)

# turtle3 = Turtle(shape="turtle")
# turtle3.penup()
# turtle3.color(color[2])
# turtle3.goto(x=-230,y=-20)

# turtle4 = Turtle(shape="turtle")
# turtle4.penup()
# turtle4.color(color[3])
# turtle4.goto(x=-230,y=20)

# turtle5 = Turtle(shape="turtle")
# turtle5.penup()
# turtle5.color(color[4])
# turtle5.goto(x=-230,y=60)

# turtle6 = Turtle(shape="turtle")
# turtle6.penup()
# turtle6.color(color[5])
# turtle6.goto(x=-230,y=100)




screen.exitonclick()