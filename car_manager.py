from turtle import Turtle
import random

"""Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge 
of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for 
our little turtle) """

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1,6) == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            color = random.choice(COLORS)
            car.color(color)
            y_position = random.randint(-250, 250)
            car.goto(260, y_position)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

