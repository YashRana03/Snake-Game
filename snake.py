from turtle import Screen, Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


# Snake class: Creates and controls the snake in the game
class Snake:

    def __init__(self):
        self.segments = []
        self.position = (0, 0)
        self.crete_snake()

    # Creates the snake body
    def crete_snake(self):
        for i in POSITIONS:
            self.add_seg(i)

    # Creates a single segment of the snake
    def add_seg(self, position):
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    # Resets the snake to its original position and length
    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.crete_snake()

    # Lengthens the snake by adding one segment
    def extend_snake(self):
        self.add_seg(self.segments[-1].position())

    # Moves the whole snake in the direction it is currently pointing towards
    def move(self, amount):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_position = self.segments[seg - 1].xcor()
            y_position = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_position, y_position)
        self.segments[0].forward(amount)

    # Sets the snake's direction to up/north
    def up(self):
        angle = self.segments[0].heading()
        if angle != 270:
            self.segments[0].setheading(90)

    # Sets the snake's direction to down/south
    def down(self):
        angle = self.segments[0].heading()
        if angle != 90:
            self.segments[0].setheading(270)

    # Sets the snake's direction to right/east
    def right(self):
        angle = self.segments[0].heading()
        if angle != 180:
            self.segments[0].setheading(0)

    # Sets the snake's direction to left/west
    def left(self):
        angle = self.segments[0].heading()
        if angle != 0:
            self.segments[0].setheading(180)



