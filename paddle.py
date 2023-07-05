from turtle import Turtle

PADDLE_WIDTH = 4
PADDLE_HEIGHT = 1
START_X = 350
START_Y = 0


class Paddle:
    def __init__(self):
        self.paddles = []
        self.first_paddle()

    def first_paddle(self):
        user_paddle = Turtle(shape="square")
        user_paddle.color("white")
        user_paddle.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        user_paddle.penup()
        user_paddle.goto(START_X, START_Y)
        self.paddles.append(user_paddle)

    def up(self):
        y = self.paddles[0].ycor()
        if y < 230:
            y += 20
        self.paddles[0].goto(x=START_X, y=y)

    def down(self):
        y = self.paddles[0].ycor()
        if y > -230:
            y -= 20
        self.paddles[0].goto(x=START_X, y=y)
