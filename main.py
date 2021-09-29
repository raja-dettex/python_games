from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

away_from_wall = [()]

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
food = Food()
scoreboard = Scoreboard()
Score = 0
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_my_snake()

    if snake.head.distance(food) < 15:
        food.refresh()

        scoreboard.check_score()
        snake.extend()
    x = snake.head.xcor()
    y = snake.head.ycor()
    if x > 290 or x < -290 or y > 290 or y < -290:
        scoreboard.reset()
        snake.reset()

    for segments in snake.my_snake:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()





















screen.exitonclick()

