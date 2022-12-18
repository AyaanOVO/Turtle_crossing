from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    car_speed = STARTING_MOVE_DISTANCE
    def __init__(self):
        self.list_turtle = []

    def making_cars(self):
        random_speed = random.randint(1,6)
        if random_speed == 1:
            mypet = Turtle("square")
            mypet.penup()
            mypet.shapesize(stretch_len=2, stretch_wid=1)
            mypet.color(random.choice(COLORS))
            mypet.goto(300, random.randint(-250, 250))
            mypet.setheading(180)
            self.list_turtle.append(mypet)


    def car_run(self):
        for turtle in self.list_turtle:
            turtle.forward(self.car_speed)



