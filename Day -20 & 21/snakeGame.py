from turtle import Screen
from snake_class import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(600,600)
screen.title("The Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#  Detect Collisions with Food
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
# Detect collisions with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor()<-280:
        game_is_on = False
        scoreboard.hitwall()

screen.exitonclick()