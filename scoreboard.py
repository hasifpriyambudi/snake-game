from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.score = 0
        with open("data.txt") as file:
            self.highScore = int(file.read())
        self.penup()
        self.goto(0, 245)
        self.color("white")
        self.writeScore()

    def writeScore(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highScore}", align=ALIGNMENT, font=FONT)

    def updateScore(self):
        self.score += 1
        self.writeScore()

    def reset(self):
        if self.score > self.highScore:
            with open("data.txt", "w") as file:
                file.write(str(self.score))
            self.highScore = self.score
        self.score = 0
        self.writeScore()
