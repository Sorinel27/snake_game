from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.number_points = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 320)
        self.write(f"Score: {self.number_points}", False, "Center", font=('Congenial', 18, 'normal'))

    def game_over(self):
        self.goto(0 , 0)
        self.write("GAME OVER", False, "Center", font=('Congenial', 18, 'normal'))

    def update(self):
        self.number_points += 1
        self.clear()
        self.write(f"Score: {self.number_points}", False, "Center", font=('Congenial', 18, 'normal'))
