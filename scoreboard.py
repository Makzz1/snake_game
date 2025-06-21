import turtle
import food

f = open(".venv/high_score.txt", "r")
high_score = int(f.read())
f.close()

FONT = ("arial", 20, "bold")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = high_score
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x=-120,y=260)
        self.pencolor("white")
        self.write(f'score : 0 high score : {self.high_score}', font=FONT)
    def update(self):
        self.clear()
        self.goto(x=-120, y=260)
        self.write(f'score : {self.score} high score : {self.high_score}', font= FONT)
    def game_over(self):
        self.pencolor("white")
        self.hideturtle()
        self.goto(x=-80, y=0)
        self.write("GAME OVER", font=FONT)
        self.goto(x=-80, y=-30)
        self.write("reset:press r", font=FONT)
        self.goto(x=-80,y=-60)
        self.write("to exit:press q",font=FONT)
        f = open(".venv/high_score.txt", "w")
        f.write(str(self.high_score))
        f.close()

