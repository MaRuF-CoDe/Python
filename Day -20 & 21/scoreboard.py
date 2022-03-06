from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.write(f"Score: {self.score}", align='center', font=('Courier', 20, 'normal'))
        self.hideturtle()

    def hitwall(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align='center', font=('Courier', 20, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align='center', font=('Courier', 20, 'normal'))

        
        