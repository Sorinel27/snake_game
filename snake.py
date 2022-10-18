from turtle import Turtle


class Snake:
    def __init__(self):
        parts = []
        positions = [(0, 0), (-20, 0), (-40, 0)]
        for pos in positions:
            part = Turtle("square")
            part.color("white")
            part.pu()
            part.goto(pos)
            parts.append(part)
        self.parts = parts

    def move(self):
        for part in range(len(self.parts) - 1, 0, -1):
            x = self.parts[part - 1].xcor()
            y = self.parts[part - 1].ycor()
            self.parts[part].goto(x, y)
        self.parts[0].forward(20)
        self.parts[0].left(90)
