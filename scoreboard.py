from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.goto(10,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Snake Game Score = {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        # self.goto(0, 270)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


