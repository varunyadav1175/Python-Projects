from turtle import Turtle

class Watermark(Turtle):
    def __init__(self):
        super().__init__()
        self.color("DarkOliveGreen")
        self.fillcolor("")
        self.hideturtle()
        self.goto(0,-60)
        self.write("PONG", align="center", font=("Helvetica", 80,"bold"))
        self.penup()