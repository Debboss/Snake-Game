from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()  # Add this line to lift the pen before moving
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # Clear previous score display
        self.write(f"Score: {self.score}", align="center", font=("Arial", int(24), "normal"))


    def game_over(self):
        self.goto(0, 0)  # Center the turtle
        self.write("GAME OVER", align="center", font=("Arial", int(24), "normal"))
