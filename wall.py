from turtle import Turtle


class Wall:
    def __init__(self):
        self.walls = []
        self.createWallTop()
        self.createWallRight()
        self.createWallLeft()
        self.createWallBottom()

    def createWallTop(self):
        x = y = 280
        for i in range(29):
            wall = Turtle("square")
            wall.penup()
            wall.color("pink")
            wall.setpos(x, y)
            x -= 20
            self.walls.append(wall)

    def createWallRight(self):
        x = y = 280
        for i in range(29):
            wall = Turtle("square")
            wall.penup()
            wall.color("pink")
            wall.setpos(x, y)
            y -= 20
            self.walls.append(wall)

    def createWallLeft(self):
        x = y = -280
        for i in range(29):
            wall = Turtle("square")
            wall.penup()
            wall.color("pink")
            wall.setpos(x, y)
            y += 20
            self.walls.append(wall)

    def createWallBottom(self):
        x = y = -280
        for i in range(29):
            wall = Turtle("square")
            wall.penup()
            wall.color("pink")
            wall.setpos(x, y)
            x += 20
            self.walls.append(wall)
