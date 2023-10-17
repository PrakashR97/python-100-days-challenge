import time
from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

Time = 0.1
screen = Screen()
scoreboard = Scoreboard()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
# top_paddle = Paddle(100, 100)
screen.listen()
ball = Ball()

screen.onkey(r_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "Up")

screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

        # need to bounce

screen.exitonclick()
