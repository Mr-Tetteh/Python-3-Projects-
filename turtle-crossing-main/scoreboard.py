from  turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-290, +260)
        self.update_scoreboard()
        # self.goto(250)
        # self.write(align="center", font=("Segoe Script", 7, "normal"))
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT )


    def increase_level(self):
        self.level += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.hideturtle()
        self.write("GAME OVER😭😭", align="center", font=FONT)
