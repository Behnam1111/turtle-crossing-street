from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)
        self.level += 1

