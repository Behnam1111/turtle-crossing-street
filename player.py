from turtle import Turtle
"""Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle 
north. """

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.set_position()

    def set_position(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(10)

    def is_collision_with_car(self, car):
        """Detect when the turtle player collides with a car and stop the game if this happens."""
        if self.distance(car) < 20:
            return True

    def is_finished(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
