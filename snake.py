from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
speed = 20
angle = 90


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        parts = []
        for pos in positions:
            part = Turtle("square")
            part.color("white")
            part.pu()
            part.goto(pos)
            parts.append(part)
        self.parts = parts
        self.head = self.parts[0]

    def move(self):
        for part in range(len(self.parts) - 1, 0, -1):
            x = self.parts[part - 1].xcor()
            y = self.parts[part - 1].ycor()
            self.parts[part].goto(x, y)
        self.head.forward(speed)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def new_part(self):
        part = Turtle("square")
        part.color("white")
        part.pu()
        x = self.parts[len(self.parts) - 1].xcor()
        y = self.parts[len(self.parts) - 1].ycor()
        part.goto(x, y)
        self.parts.append(part)
