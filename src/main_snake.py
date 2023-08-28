from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Check for collisions with food
    # Check for collisions with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        # You might want to add code here to grow the snake
        scoreboard.score += 1
        scoreboard.update_scoreboard()

        # You might want to add code here to grow the snake

    # Check for collisions with screen boundaries
    if (
        snake.segments[0].xcor() > 280
        or snake.segments[0].xcor() < -280
        or snake.segments[0].ycor() > 280
        or snake.segments[0].ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()

    # Check for collisions with snake's body
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 15:
            game_is_on = False


screen.exitonclick()
