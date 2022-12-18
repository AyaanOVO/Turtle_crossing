from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    level = 1
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-210,250)
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def reset_score(self):
        self.clear()
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def game_over(self):
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(-20,0)
        tim.write("Game Over", align="center", font=("Arial", 15, "bold"))








