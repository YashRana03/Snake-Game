from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
# from logo import game_on
import time

game_on = True
BOUNDARY = 290
# Setting up the window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()

# Linking the keyboad keys to the appropriate functions/commands
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

while game_on:

    screen.update()
    time.sleep(0.05)
    snake.move(10)

    # Check if the snake has eaten the food and if so updates the score and increases the length of the snake
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.increase()

    # Check if the snake has it a boundary if so ends the game
    if snake.segments[0].xcor() > BOUNDARY or snake.segments[0].xcor() < -BOUNDARY or snake.segments[0].ycor() > BOUNDARY \
            or snake.segments[0].ycor() < -BOUNDARY:
        score.reset()
        time.sleep(2)
        snake.reset_snake()

    # Checks if the snake has hit itself if so ends the game
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 8:
            score.reset()
            time.sleep(1)
            snake.reset_snake()


screen.exitonclick()

