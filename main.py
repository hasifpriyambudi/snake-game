from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from wall import Wall
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
wall = Wall()

screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

condition = True
while condition:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Food
    if snake.head.distance(food) < 15:
        food.refreshFood()
        score.updateScore()
        snake.extend()

    # Hit Wall
    if snake.head.xcor() > 260 or snake.head.xcor() < -260 or snake.head.ycor() > 260 or snake.head.ycor() < -260:
        score.reset()
        snake.reset()

    # detect tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
