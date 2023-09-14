from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from jagged import Jagged
from watermark import Watermark
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
for i in range(20):
    new_jagged = Jagged()
    new_jagged.goto(new_jagged.positions[i])
topline = Jagged().topline()
bottomline = Jagged().bottomline()
watermark = Watermark()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bouncex()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bouncex()

    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset()
        score.r_point()

screen.exitonclick()
