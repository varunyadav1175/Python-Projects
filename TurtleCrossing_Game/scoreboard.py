from turtle import Turtle
FONT = ("Courier", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(-290,280)
        self.Level = 1
        self.write(f"Level = {self.Level}", align="left", font=FONT)

    def update_score(self):
        self.Level += 1
        self.clear()
        self.write(f"Level = {self.Level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align="center", font=("Courier", 42, "bold"))





