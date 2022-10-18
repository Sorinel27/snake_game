from turtle import Screen, Turtle
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
    speed = 10
    for part in parts:
        part.fd(speed)
        part.left(90)
        speed += 10


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
    positions = [(0, 0), (-20, 0), (-40, 0)]
    for pos in positions:
        part = Turtle("square")
        part.color("white")
        part.pu()
        part.goto(pos)
        parts.append(part)
    is_not_dead = True
    while is_not_dead:
        screen.update()
        time.sleep(0.1)
        for part in parts:
            part.fd(1)

    screen.exitonclick()


if __name__ == "__main__":
    main()
