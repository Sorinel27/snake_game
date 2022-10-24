from turtle import Turtle
import os

file = open("high_score.txt", "r+")
user_file = open("user.txt", "r+")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.high_score = file.readline()
        self.user = user_file.readline()
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 320)
        self.write(f"Score: {self.current_score}  High Score : {self.high_score} by {self.user}", False, "Center", font=('Congenial', 18, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "Center", font=('Congenial', 18, 'normal'))

    def update(self):
        self.current_score += 1
        self.clear()
        self.write(f"Score: {self.current_score}  High Score : {self.high_score} by {self.user}", False, "Center", font=('Congenial', 18, 'normal'))

    def set_new_high_score(self):
        self.high_score = self.current_score
        self.user = os.getlogin()
        user_file.truncate(0)
        user_file.close()
        file.truncate(0)
        file.close()
        with open("high_score.txt", "r+") as f:
            f.write(str(self.current_score))
            f.close()
        with open("user.txt", "r+") as f:
            f.write(os.getlogin())
            f.close()
