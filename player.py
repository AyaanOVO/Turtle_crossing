from turtle import Turtle
from car_manager import CarManager
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.showturtle()

    def up(self):
        if (self.ycor() < FINISH_LINE_Y):
            self.forward(MOVE_DISTANCE)

    def down(self):
        if (self.ycor() > -FINISH_LINE_Y):
            self.backward(MOVE_DISTANCE)

    def goto_start(self):
        self.clear()
        self.goto(0, -280)

