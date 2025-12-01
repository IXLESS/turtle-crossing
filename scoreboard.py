from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-210, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    
    def next_level(self):
        self.score += 1
        self.update_score()