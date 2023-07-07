from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# TODO 1: Create the screen
time_sleep = 0.1
screen = Screen()

screen.tracer(0)
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG GAME")

# TODO 2: Create and move a paddle

r_paddle = Paddle((350, 0))
# TODO 3: Create another paddle
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()



screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

# TODO 4: Create the ball and make it move
ball = Ball()

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


# TODO 5: Create collision with the wall and make it bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


# TODO 6: Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
# TODO 7: Detect when paddle misses
# TODO 8: Keep the score

    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
