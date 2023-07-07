from turtle import Turtle

STRETCH_WIDTH = 5
STRETCH_LEN = 1


class Paddle(Turtle):
    def __init__(self, paddle_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LEN)
        self.penup()
        self.goto(paddle_position)

    def up(self):
        new_y = self.ycor()
        if new_y < 250:
            new_y += 20
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor()
        if new_y > -250:
            new_y -= 20
        self.goto(x=self.xcor(), y=new_y)
