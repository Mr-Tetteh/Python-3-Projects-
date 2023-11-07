from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=800, height=600 )
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_Paddle = Paddle((-350, 0))
my_ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_Paddle.move_up, "w")
screen.onkey(l_Paddle.move_down, "s")

game_on = True

while game_on:
    time.sleep(my_ball.move_speed)
    screen.update()
    my_ball.move_ball()

    #Detecting for collision with wall
    if my_ball.ycor() > 280 or my_ball.ycor() < - 280:
        my_ball.bounce_y()

    # Detect for collision with paddles
    if my_ball.distance(r_paddle) < 50 and my_ball.xcor() > 320 or my_ball.distance(l_Paddle) < 50 and my_ball.xcor() <- 320:
        my_ball.bounce_x()

    # Detect if ball goes out of bounds
    if my_ball.xcor() > 380:
        my_ball.reset_ball()
        score.l_point()

    if my_ball.xcor() <- 380:
        my_ball.reset_ball()
        score.r_point()


screen.exitonclick()
