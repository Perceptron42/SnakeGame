from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game!")
screen.tracer(0) # so that no updates will happen on the screen until we ask for it

snake = Snake()
food = Food()
scoreboard = ScoreBoard()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # add a 1 second delay
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #detect collission with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_is_on = False
        scoreboard.game_over()

    #detect collission with tail
    for segment in snake.segments[1:]:
          if snake.head.distance(segment)<10:
                game_is_on = False
                scoreboard.game_over()


screen.exitonclick()