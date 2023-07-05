from turtle import Screen

from paddle import Paddle

# TODO 1: Create the screen
screen = Screen()

screen.tracer(0)
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG GAME")

# TODO 2: Create and move a paddle
paddle = Paddle()
screen.update()

screen.tracer(1)
screen.listen()
screen.onkeypress(paddle.up, "Up")
screen.onkeypress(paddle.down, "Down")

# TODO 3: Create another paddle
# TODO 4: Create the ball and make it move
# TODO 5: Create collision with the wall and make it bounce
# TODO 6: Detect collision with paddle
# TODO 7: Detect when paddle misses
# TODO 8: Keep the score


screen.exitonclick()
