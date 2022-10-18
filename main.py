from turtle import Screen, Turtle
from snake import Snake
import turtle as t
import time

marcel = Turtle()
screen = Screen()
parts = []


def up():
    speed = 10
    for part in parts:
        part.fd(speed)
        part.left(90)
        speed += 10


def left():
    for i in reversed(range(len(parts))):
        x = parts[i - 1].xcor()
        y = parts[i - 1].ycor()
        parts[i].goto(x, y)
    parts[0].left(90)
    parts[0].fd(20)


def right():
    speed = 10
    for part in parts:
        part.fd(speed)
        part.right(90)
        speed += 10


def down():
    speed = 10
    for part in parts:
        part.fd(speed)
        part.left(90)
        speed += 10


def main():
    screen.listen()
    screen.setup(width=700, height=700)
    screen.bgcolor("black")
    screen.title("Snake game")
    screen.tracer(0)
    snake = Snake()
    is_not_dead = True
    while is_not_dead:
        screen.update()
        time.sleep(0.1)
        snake.move()
    screen.exitonclick()


if __name__ == "__main__":
    main()
