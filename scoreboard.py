from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setpos(0, 280)
        self.hideturtle()
        self.score = 0
        with open("data.txt") as data:
            self.High_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score : {self.score} HiGH Score : {self.High_score}")

    def check_score(self):
        self.score += 1

        self.update_scoreboard()

    def reset(self):
        if self.score > self.High_score:
            self.High_score = self.score
        with open("data.txt", "w") as data:
            data.write(f"{self.High_score}")

        self.score = 0
        self.update_scoreboard()

    # def final_result(self):
    #
    #     self.goto(-20, 0)
    #     self.write("GAME OVER")
