from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.condition = True
        self.head = self.segments[0]

    def createSnake(self):
        for i in STARTING_POSITIONS:
            self.addSegment(i)

    def addSegment(self, position):
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        self.addSegment(self.segments[-1].position())

    def move(self):
        for segNum in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[segNum - 1].xcor()
            newY = self.segments[segNum - 1].ycor()
            self.segments[segNum].goto(newX, newY)
        self.segments[0].fd(MOVE_DISTANCE)

    def Up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def Down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def Right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def Left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def reset(self):
        for seg in self.segments:
            seg.goto(2000, 2000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]
