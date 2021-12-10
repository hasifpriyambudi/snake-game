from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.score = 0
        self.penup()
        self.goto(0, 245)
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def updateScore(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
