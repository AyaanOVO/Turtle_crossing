import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(fun=player.up,key="Up")
screen.onkey(fun=player.down,key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() >= 278:
        score_board.level += 1
        score_board.reset_score()
        car.car_speed += 5
        player.goto_start()

    car.making_cars()
    car.car_run()

    for turtle in car.list_turtle:
        if turtle.distance(player) < 21:
            game_is_on = False
            score_board.game_over()



screen.exitonclick()




