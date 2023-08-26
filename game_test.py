from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

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

    # Check for collisions with screen boundaries
    if (
        snake.segments[0].xcor() > 290
        or snake.segments[0].xcor() < -290
        or snake.segments[0].ycor() > 290
        or snake.segments[0].ycor() < -290
    ):
        game_is_on = False

    # Check for collisions with snake's body
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 15:
            game_is_on = False

screen.exitonclick()