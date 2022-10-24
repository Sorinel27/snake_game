from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Score
import time
import os

marcel = Turtle()
screen = Screen()
food = Food()
parts = []
score = Score()
file = open("high_score.txt", "r+")


def main():
    screen.listen()
    screen.setup(width=700, height=700)
    screen.bgcolor("black")
    screen.title("Snake game")
    screen.tracer(0)
    snake = Snake()
    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    is_not_dead = True
    while is_not_dead:
        screen.update()
        time.sleep(0.1)
        if snake.head.distance(food) < 15:
            food.random_location()
            score.update()
            snake.new_part()
        for i in range(len(snake.parts) - 1, 1, -1):
            if snake.head.distance(snake.parts[i]) < 10:
                is_not_dead = False
                score.game_over()
                if score.current_score > int(file.readline()):
                    score.set_new_high_score()
        if snake.head.xcor() > 330 or snake.head.ycor() > 330 or snake.head.xcor() < -330 or snake.head.ycor() < -330:
            is_not_dead = False
            score.game_over()
            if score.current_score > int(file.readline()):
                score.set_new_high_score()
        snake.move()
    screen.exitonclick()


if __name__ == "__main__":
    main()
