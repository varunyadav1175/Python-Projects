from turtle import Turtle
ALIGNMENT ="center"
FONT = ("Courier", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.write(f"Score = {self.score}",False,ALIGNMENT , FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}",False,ALIGNMENT , FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def final_score(self):
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER",False,ALIGNMENT , ("Courier", 24, "bold"))
        self.goto(0,265)
        self.color("yellow")
        self.write(f"Final Score: {self.score}",False,ALIGNMENT , ("Courier", 18, "bold"))
