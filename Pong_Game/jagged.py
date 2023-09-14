from turtle import Turtle


class Jagged(Turtle):
    def __init__(self):
        super().__init__()
        self.positions = [(0, 380), (0, 340), (0, 300), (0, 260), (0, 220), (0, 180), (0, 140), (0, 100), (0, 60),
                          (0, 20), (0, -20), (0, -60), (0, -100), (0, -140), (0, -180), (0, -220), (0, -260), (0, -300),
                          (0, -340), (0, -380)]
        self.penup()
        self.color("red")
        self.shape("square")
        self.shapesize(1, 0.05)

    def topline(self):
        self.color("white")
        self.shape("square")
        self.shapesize(1, 40)
        self.goto(0, 305)

    def bottomline(self):
        self.color("white")
        self.shape("square")
        self.shapesize(1, 40)
        self.goto(0, -298)
