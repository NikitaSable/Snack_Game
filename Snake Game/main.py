import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from update_level import UpdateLevel

block1_position = [(-180, 80), (-180, 100), (-180, 120), (-180, 140), (-180, 160), (-180, 180), (-180, 200)]
block2_position = [(180, -80), (180, -100), (180, -120), (180, -140), (180, -160), (180, -180), (180, -200)]
block3_position = [(-60, -80), (-80, -80), (-100, -80), (-120, -80), (-140,-80), (-160, -80), (-180,-80)]
block4_position = [(60, 80), (80, 80), (100, 80), (120, 80), (140,80), (160, 80), (180,80)]

level = UpdateLevel()
score = ScoreBoard()
food = Food()
snake = Snake()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
speed = 0.2

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")



game_on = True
while game_on:
    screen.update()
    time.sleep(speed)
    snake.move()
    if score.score > 2:
        level.leve1()
        for i in block1_position:
            if snake.head.distance(i):
                score.reset()
                snake.reset()

    if score.score > 5:
        level.leve2()
        for i in block2_position:
            if snake.head.distance(i):
                score.reset()
                snake.reset()

    if score.score > 6:
        level.leve3()
        for i in block3_position:
            if snake.head.distance(i):
                score.reset()
                snake.reset()
    if score.score > 7:
        level.leve4()
        for i in block4_position:
            if snake.head.distance(i):
                score.reset()
                snake.reset()


    if snake.head.distance(food) < 15:
        score.score_increase()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 260 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for i in snake.segment[1:]:
        if snake.head.distance(i) < 10 and i != snake.head:
            score.reset()
            snake.reset()




screen.exitonclick()